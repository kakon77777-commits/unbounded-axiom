# MWT-10：World Memory, Compression, and Long-Horizon Mathematical Persistence
## 世界記憶、雙軌壓縮、依賴式遺忘、可重建性與長期數學持續存在

**英文題名：** *MWT-10: World Memory, Compression, and Long-Horizon Mathematical Persistence — Dual-Track Compression, Dependency-Aware Forgetting, Reconstructability, and Persistent Mathematical Worlds*  
**系列：** Mathematical World Theory（MWT）  
**篇次：** 10  
**文件編號：** EML-MWT-10-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-19  
**版本：** v0.1  
**文件性質：** 數學世界論第十篇形式母稿／World Memory Layer／Long-Horizon Persistence／第一輪核心系列封頂篇  
**前置文件：** MWT-01 ～ MWT-09  
**狀態：** 可使用研究稿；提供 reference memory-tier / reconstruction evaluator；本篇完成 MWT v0.1 第一輪 01～10 核心架構  

---

## 摘要

MWT-01 至 MWT-09 已建立一個可以被表示、合法作用、非交換排程、暫時閉合、無界 refinement、跨尺度耦合、接受 query、承擔全域量詞並接受資源核算的數學世界 runtime。這套架構若只運行數分鐘或數天，問題尚不明顯；但如果它真的要運行數年、數十年甚至跨多代 AI，下一個瓶頸不是再增加一個 solver，而是：

> **世界如何記住自己，而不被自己的歷史淹死？**

若每一輪都保留完整 active transcript、完整 proof trace、所有 branch、所有中間 simulation、所有失敗 search、所有版本與所有 duplicate presentation，則 MWT-09 的 resource accounting 很快指出：

$$
\boxed{
\text{Perfect Active Recall}
\rightarrow
\text{Context Explosion}.
}
$$

反過來，如果系統只保存高層摘要，則又可能丟失：

- 原始 source；
- proof witness；
- identity distinctions；
- branch-specific history；
- counterexample context；
- version lineage；
- reconstruction evidence。

因此 MWT-10 提出 **World Memory Architecture（WMA）**，以兩條互補軸治理長期記憶：

第一條軸是 **fidelity axis**：

$$
\boxed{
\text{Lossless Source Track}
\;\parallel\;
\text{Generative Semantic Track}.
}
$$

第二條軸是 **activation axis**：

$$
\boxed{
\text{Active}
\rightarrow
\text{Operational}
\rightarrow
\text{Dormant}
\rightarrow
\text{Archive}.
}
$$

兩軸交叉後形成一個多層記憶矩陣，而不是單一「memory store」。

本文明確吸收既有 GCMS 雙軌記憶主張：**原文無損還原**與**近無損語義重建**不是同一件事。若原始 artifact $x$ 經 lossless codec：

$$
E_L(x)=c,
$$

則要求：

$$
\boxed{
D_L(c)=x
}
$$

在指定 bit / canonical source identity 下成立。若是 semantic compression：

$$
E_S(x)=m,
$$

則 reconstruction：

$$
R_S(m,\Gamma)
=
\widehat x
$$

只要求相對 inquiry family $\mathcal Q$ 與 identity specification $\mathfrak I$：

$$
\boxed{
\widehat x
\equiv_{\mathfrak I,\mathcal Q}
x.
}
$$

因此：

$$
\boxed{
\text{semantic reconstructability}
\neq
\text{byte-identical recoverability}.
}
$$

任何系統若把生成式重建說成原文回復，就是 memory provenance error。

本文定義 MWT World Memory State：

$$
\boxed{
\mathfrak M_t^{W}
=
(
M_t^{A},
M_t^{O},
M_t^{S},
M_t^{C},
M_t^{D},
M_t^{R},
M_t^{H},
M_t^{Q},
M_t^{X}
).
}
$$

其中：

- $M_t^{A}$：Active Memory，當前 query / solve 必須直接載入的高頻狀態；
- $M_t^{O}$：Operational Memory，對 legality、identity、branch routing、reopen 與近期推理足夠的壓縮狀態；
- $M_t^{S}$：Source Memory，原始 artifacts、proof objects、datasets、documents、exact snapshots；
- $M_t^{C}$：Certificate Memory，proof / legality / coverage / coupling / resource certificates；
- $M_t^{D}$：Dormant Memory，已知但目前不載入；
- $M_t^{R}$：Reconstruction Memory，生成核、semantic fingerprints、summary graphs、reconstruction recipes；
- $M_t^{H}$：History / Lineage Memory，版本、branch、merge、migration、causal provenance；
- $M_t^{Q}$：Quarantine / Candidate Memory，尚未被 Stable Core 接受、可能衝突或污染的知識；
- $M_t^{X}$：External / Archived Memory，content-addressed external archive 與 materialization pointers。

此九元結構仍只是 MWT 的 memory runtime presentation，並非 World primitive。

本文進一步提出 **Reconstruction Contract**：

$$
\boxed{
\mathcal C_R(m)
=
(
L,
\mathfrak I,
\mathcal Q,
\Gamma,
A,
\varepsilon,
V
).
}
$$

其中：

- $L$：reconstruction level；
- $\mathfrak I$：identity requirement；
- $\mathcal Q$：future query family；
- $\Gamma$：required contextual anchors；
- $A$：archive/source anchors；
- $\varepsilon$：允許 loss；
- $V$：version / verifier。

Reconstruction level 至少分：

1. **L0 — Byte Exact**：逐 byte / canonical source exact；
2. **L1 — Structural Exact**：AST / graph / proof DAG exact；
3. **L2 — Semantic Equivalent**：對指定 identity / inquiry 等價；
4. **L3 — Operational Sufficient**：足以重建 future legality / query behavior；
5. **L4 — Heuristic Recall**：只保留提示性記憶，不可作正式 evidence。

這使 memory system 不再只有「記得／忘了」，而有「能重建到哪一層」的正式狀態。

本文同時建立 **Dependency-Aware Forgetting**。active eviction、semantic compression、archive、tombstone、physical deletion 必須區分。對 memory item $m$，如果存在 hard dependent：

$$
m
\rightarrow_{\mathrm{hard}}
y
$$

且 $y$ 沒有替代 reconstruction path，則不能直接 physical delete。本文定義 forgetting judgment：

$$
\boxed{
\Gamma
\vdash
\operatorname{Forget}_{\tau}(m)
\Downarrow_{\mathsf{Mem}}
f,
}
$$

其中：

$$
f
\in
\{
\mathsf{Allow},
\mathsf{Block},
\mathsf{Defer},
\mathsf{Conflicted}
\}.
}
$$

forgetting type $\tau$ 至少包括：

- Active Eviction；
- Summary Replacement；
- Dormantization；
- Archive；
- Tombstone；
- Physical Deletion。

最重要的一條是：

$$
\boxed{
\text{not active}
\neq
\text{forgotten}
\neq
\text{deleted}.
}
$$

本文亦吸收 GCMS「來源—候選—接受知識」的三區治理思想。新 information 不直接寫入 Stable Memory，而先進：

$$
\boxed{
Z_{\mathrm{source}}
\rightarrow
Z_{\mathrm{candidate}}
\rightarrow
Z_{\mathrm{accepted}}.
}
$$

其中 candidate 可以：

- pending verification；
- conflicting；
- low-confidence；
- source-only；
- speculative。

這防止 memory poisoning 與「看到就相信」的長期累積錯誤。

對長期 archive，本文引入 content-addressed persistence。若 exact artifact：

$$
x
$$

以 cryptographic content fingerprint：

$$
h(x)
$$

作 addressing key，則相同 bytes 可以 deduplicate，舊版本可 write-once 保留。Venti 已是成熟外部例子：以內容 hash 作 block identifier、支援 write-once archival 與 duplicate coalescing。MWT 只吸收此工程原則，不把 hash identity 誤寫成 semantic identity。

本文亦引入 persistent data structure 思想：Driscoll–Sarnak–Sleator–Tarjan 的經典工作顯示資料結構可以在更新後仍保留舊版本可訪問性。MWT 的 world lineage 因此可採：

$$
\boxed{
\text{new version does not destroy old version}.
}
$$

這對 theorem migration、branch reopening 與 proof revocation 尤其重要。

對 change propagation，self-adjusting computation 提供另一個成熟接口：當 memory / input 更新時，可以沿 dependency 只重新計算受影響區域，而非完整重跑。MWT 將它接成：

$$
\boxed{
\text{Memory Change}
\rightarrow
\text{Dependency Impact}
\rightarrow
\text{Incremental Revalidation}.
}
$$

在 2026 年長期 Agent memory 研究中，也已出現與 MWT-10 高度鄰接的方向：MemRefine 直接把 memory management 表述為 fixed-budget 下 merge / delete / preserve；RaMem 指出 retrieval relevance 不足以證明 memory 對當前 query 有效，必須重新帶回事件時間、session、participants 等 context；LeanMem 則明確按 compressibility、temporal dynamics 與 fidelity requirements 將歷史內容分成不同 memory types，而不是一律 summary。MWT 不等同這些 Agent memory 系統，但將它們作為「長期記憶必須分層、分 fidelity、分 context-validity」的最新外部實證接口。

本文最終建立 **Long-Horizon Persistence Principle**：

$$
\boxed{
\text{Persistent Mathematical World}
=
\text{small active state}
+
\text{reconstructable compressed memory}
+
\text{immutable provenance anchors}
+
\text{dependency-aware retrieval}
+
\text{versioned lineage}.
}
$$

並提出 World Memory Store、Source Archive、Semantic Reconstruction Store、Certificate Cache、Dependency Index、Recall Controller、Forgetting Gate、Deduplication Engine、Integrity/Revalidation Engine、Migration Engine、Lineage Ledger、Memory Budget Manager 等十二個最低模組。

MWT-10 同時作為 MWT v0.1 第一輪 01～10 核心系列的封頂篇：世界現在已經能被表示、判定、排程、穩定、擴張、耦合、詢問、全域證明、核算資源，並記住自身。下一階段不應無止境新增「第 11 篇」，而應開始把 01～10 回收成統一 MWT v0.2 mother runtime / implementation specification。

**關鍵詞：** Mathematical World Theory、world memory、long-horizon persistence、semantic compression、lossless archive、reconstructability、content-addressed storage、persistent data structures、dependency-aware forgetting、agent memory、AI-native mathematics

---

# 0. 本文的責任：世界若不能記得自己，就不能長期存在

一個短期 mathematical runtime 可以把所有東西放 RAM。

一個長期 world 不行。

若：

$$
|H_t|
\rightarrow
\infty,
$$

但 active budget：

$$
B_{\mathrm{ctx}}
$$

有限，

就必須有：

$$
\boxed{
\text{Memory Governance}.
}
$$

---

# 1. Memory 不是 Archive

Archive 只回答：

> 原始東西還在嗎？

Memory 還要回答：

- 現在要不要載入？
- 怎麼找到？
- 它可信嗎？
- 它和什麼有關？
- 壓縮後還能重建什麼？
- 哪些 future queries 需要它？
- 哪個版本有效？

所以：

$$
\boxed{
\text{Memory}
\supsetneq
\text{Storage}.
}
$$

---

# 2. Memory 不是 Context

LLM context：

$$
C_t
$$

只是 active presentation。

不能：

$$
\boxed{
\text{not in context}
\Rightarrow
\text{forgotten}.
}
$$

真正 long-term memory 必須存在 context 之外。

---

# 3. World Memory State

定義：

$$
\boxed{
\mathfrak M_t^{W}
=
(
M_t^{A},
M_t^{O},
M_t^{S},
M_t^{C},
M_t^{D},
M_t^{R},
M_t^{H},
M_t^{Q},
M_t^{X}
).
}
$$

---

# 4. Active Memory

$$
M_t^{A}
$$

是當前 query / world solve 直接載入的 memory working set。

它應很小。

---

# 5. Operational Memory

$$
M_t^{O}
$$

保存：

- current stable core summary；
- open obligations；
- relevant branches；
- active identity；
- legality dependencies；
- reopen triggers。

它比 archive 小，但比 active context大。

---

# 6. Source Memory

$$
M_t^{S}
$$

保存：

- canonical source；
- raw data；
- exact proof object；
- original document；
- snapshot；
- user-provided artifact。

這是 evidence anchor。

---

# 7. Certificate Memory

$$
M_t^{C}
$$

保存：

- proof certificate；
- quantifier compression certificate；
- legality certificate；
- coupling certificate；
- resource certificate；
- verification result。

Certificate 可獨立於 human summary 保存。

---

# 8. Dormant Memory

$$
M_t^{D}
$$

是已知可用但目前不載入的結構。

例如舊 presentation、低 priority branch、inactive theory。

---

# 9. Reconstruction Memory

$$
M_t^{R}
$$

保存：

- generative kernel；
- semantic fingerprint；
- relation graph；
- structural summary；
- retrieval cue；
- reconstruction recipe。

---

# 10. History / Lineage Memory

$$
M_t^{H}
$$

保存：

- version chain；
- branch / merge；
- migration；
- invalidation；
- causal provenance；
- revision reason。

---

# 11. Quarantine / Candidate Memory

$$
M_t^{Q}
$$

保存：

- unverified source；
- speculative claim；
- conflicting candidate；
- low-confidence extraction；
- poisoned / suspicious memory。

---

# 12. External / Archived Memory

$$
M_t^{X}
$$

保存 content-addressed external artifact references、cold storage pointers 與 materialization metadata。

---

# 13. Memory Tier 不等於 Truth Tier

source archive可以保存錯誤論文。

accepted memory也可能未來被推翻。

所以：

$$
\boxed{
\text{storage tier}
\neq
\text{truth status}.
}
$$

---

# 14. Fidelity Axis

記憶至少分：

$$
\boxed{
\mathsf{Exact}
\parallel
\mathsf{Semantic}
\parallel
\mathsf{Operational}
\parallel
\mathsf{Heuristic}.
}
$$

---

# 15. Exact Lossless Track

codec：

$$
E_L,
D_L
$$

要求：

$$
\boxed{
D_L(E_L(x))
=
x.
}
$$

identity 可為：

- bytes；
- canonical UTF-8；
- AST；
- normalized proof term。

---

# 16. Semantic Track

$$
E_S(x)=m,
$$

$$
R_S(m,\Gamma)=\widehat x.
$$

要求：

$$
\boxed{
\widehat x
\equiv_{\mathfrak I,\mathcal Q}
x.
}
$$

---

# 17. Operational Track

不需要重建原物件。

只要求 memory state：

$$
m_O
$$

足以對 future query family：

$$
\mathcal Q_O
$$

做出相同 required decisions：

$$
\boxed{
\operatorname{Decide}_{\mathcal Q_O}(m_O)
=
\operatorname{Decide}_{\mathcal Q_O}(x).
}
$$

---

# 18. Heuristic Track

只作：

- hint；
- retrieval seed；
- brainstorming cue。

不得作 formal evidence。

---

# 19. Reconstruction Contract

定義：

$$
\boxed{
\mathcal C_R(m)
=
(
L,
\mathfrak I,
\mathcal Q,
\Gamma,
A,
\varepsilon,
V
).
}
$$

---

# 20. Reconstruction Level L0

$$
\boxed{
L0=\mathsf{ByteExact}.
}
$$

要求：

$$
\widehat x=x
$$

在 canonical bytes。

---

# 21. L1 — Structural Exact

要求：

$$
\operatorname{Struct}(\widehat x)
=
\operatorname{Struct}(x).
$$

例如 AST / graph / proof DAG exact。

---

# 22. L2 — Semantic Equivalent

要求：

$$
\widehat x
\equiv_{\mathfrak I,\mathcal Q}
x.
$$

語句可不同。

---

# 23. L3 — Operational Sufficient

只要求 future decisions / predictions / legality outcomes足夠。

---

# 24. L4 — Heuristic Recall

不保證等價。

只保留「可能有用」。

---

# 25. Wrong-Level Claim

如果 L2 reconstruction 被說成 L0 recovery：

$$
\boxed{
\mathsf{MemoryIdentityError}.
}
$$

這是 GCMS 雙軌思想在 MWT 的正式版本。

---

# 26. Reconstruction Loss

定義：

$$
\boxed{
\mathcal L_R
=
\operatorname{Loss}
(
x,
\widehat x
\mid
\mathfrak I,\mathcal Q
).
}
$$

不要求單一數值。

---

# 27. Reconstruction Witness

任何 compressed memory：

$$
m
$$

都應有：

$$
\boxed{
C_m^{R}.
}
$$

證明它宣稱的 reconstruction level。

---

# 28. Compression Is a Transformation

$$
\boxed{
K:
x
\to
m.
}
$$

因此 compression 自身必須接受 MWT-02 legality、MWT-03 order 與 MWT-09 resource accounting。

---

# 29. Compression Is Not Automatically Monotone Good

更高 compression：

$$
|m|\downarrow
$$

可能：

$$
\mathcal L_R\uparrow.
$$

所以最小 memory size不是唯一目標。

---

# 30. Compression Contract

定義：

$$
\boxed{
\mathcal C_K
=
(
D,
L,
\mathfrak I,
\mathcal Q,
B,
C_R,
C_{\mathrm{archive}}
).
}
$$

---

# 31. Query-Relative Compression

同一 artifact：

$$
x
$$

對 query family：

$$
\mathcal Q_1
$$

可以大幅壓縮，

但對：

$$
\mathcal Q_2
$$

不可壓。

所以：

$$
\boxed{
\text{compressibility is query-relative}.
}
$$

---

# 32. Time-Relative Compression

近期 detail 可能 high value。

十年後只需 summary。

但某 legal/proof source 永遠不能丟 exact archive。

因此 retention policy 也隨 time / role 變。

---

# 33. Semantic Deduplication

兩 memory entries：

$$
m_1,m_2
$$

可能 semantic duplicate。

可以：

$$
m_1
\equiv_{\mathfrak I}
m_2.
$$

但 merge 前要檢查：

- provenance；
- time；
- version；
- source；
- conflict。

---

# 34. Byte Deduplication

若：

$$
x_1=x_2
$$

bytes exact，

content-addressed archive可以共享同一 block/object。

這比 semantic dedup 強得多。

---

# 35. Hash Identity

若：

$$
h(x_1)=h(x_2),
$$

工程上可以在 collision assumptions 下作 byte identity key。

但：

$$
\boxed{
h(x_1)=h(x_2)
\not\Rightarrow
\text{semantic theorem equivalence by itself}.
}
$$

---

# 36. Content-Addressed Archive

定義：

$$
\boxed{
A_{\mathrm{CAS}}
:
h(x)
\mapsto
x.
}
$$

同 content 可 dedup。

新版本 content 產生新 address。

---

# 37. Venti Interface

Venti 的成熟設計以內容 hash 作 block identifier，帶來 write-once archival 與 duplicate coalescing。

MWT 可把這種設計作 Source Archive backend。

但 MWT 不依賴特定 hash 或 storage system。

---

# 38. Persistent Data Structure

更新：

$$
S_t
\to
S_{t+1}
$$

不銷毀：

$$
S_t.
$$

即：

$$
\boxed{
\text{new state coexists with old version access}.
}
$$


# 39. Persistent Data Structure Interface

Driscoll、Sarnak、Sleator、Tarjan 的 persistent data structure 工作已建立一個重要工程思想：

> 更新不必抹掉舊版本；舊／新版本可以被共同尋址。

MWT 將此吸收為：

$$
\boxed{
\text{revision}
\neq
\text{destruction of provenance}.
}
$$

---

# 40. Fully Persistent vs Partially Persistent

如果只能查舊版本、但只修改最新版本，可視為 partial persistence。

如果任意版本都能派生新版本，接近 full persistence。

MWT branch / theory fork 更需要後者精神。

---

# 41. Version Graph

定義：

$$
\boxed{
\mathcal G_t^{V}
=
(
\mathcal V_t,
E_{\mathrm{parent}},
E_{\mathrm{merge}},
E_{\mathrm{migration}}
).
}
$$

版本不是單一線性序列。

可以 branch。

---

# 42. Snapshot

snapshot：

$$
S^{(v)}
$$

是某時刻完整可重建 state anchor。

但不需要每一 revision 都存 full copy。

可以：

- delta；
- structural sharing；
- CAS；
- periodic checkpoint。

---

# 43. Structural Sharing

若新 state：

$$
S'
$$

只改小部分，

不需複製全部：

$$
S.
$$

共享未改部分可以降低 storage。

---

# 44. Delta Chain

可以保存：

$$
S_{t+1}
=
S_t+\Delta_t.
$$

但 delta chain 過長會提高 reconstruction cost。

因此需要 checkpoint policy。

---

# 45. Checkpoint Interval

令：

$$
k
$$

為 checkpoint 間隔。

太小：

- storage 高。

太大：

- replay 高；
- failure recovery 慢。

這是 MWT-09 resource tradeoff。

---

# 46. Reconstruction Cost

對 archived state：

$$
S_t,
$$

定義：

$$
\boxed{
C_{\mathrm{reconstruct}}(S_t).
}
$$

memory 壓縮不能只看 storage size。

還要看未來 reconstruction cost。

---

# 47. Memory Cost Profile

定義：

$$
\boxed{
\kappa_M(m)
=
(
S_{\mathrm{store}},
C_{\mathrm{write}},
C_{\mathrm{retrieve}},
C_{\mathrm{reconstruct}},
C_{\mathrm{verify}},
C_{\mathrm{maintain}}
).
}
$$

---

# 48. Compression Tradeoff

可形成：

$$
\boxed{
\text{storage}
\leftrightarrow
\text{reconstruction}
\leftrightarrow
\text{fidelity}
}
$$

三方 tradeoff。

---

# 49. Long-Horizon Memory Budget

定義：

$$
\boxed{
B_M
=
(
B_A,
B_O,
B_D,
B_X,
B_{\mathrm{retrieval}},
B_{\mathrm{reconstruct}},
B_{\mathrm{maintenance}}
).
}
$$

不同 memory tier 有不同 budget。

---

# 50. Active Memory Is Scarce

$$
B_A
$$

通常最昂貴，因為 active memory 直接占：

- context；
- RAM；
- attention；
- synchronization。

所以 active tier 必須 aggressively selective。

---

# 51. Archive Can Be Large

$$
B_X
$$

可遠大於：

$$
B_A.
$$

因此合理設計不是刪掉全部歷史，而是：

$$
\boxed{
\text{cold large archive}
+
\text{small hot state}.
}
$$

---

# 52. Recall

對 query：

$$
q,
$$

定義：

$$
\boxed{
\operatorname{Recall}(q,\mathfrak M^W)
\to
\mathcal M_q.
}
$$

 $\mathcal M_q$ 是 query-specific retrieval bundle。

---

# 53. Recall Is Not Similarity Search Only

memory relevance不等於：

$$
\operatorname{sim}(q,m).
$$

還需要：

- validity；
- time；
- source；
- identity；
- branch；
- version；
- context。

---

# 54. Contextual Reinstatement

retrieved fragment：

$$
m
$$

若離開原事件 context，

可能被錯用。

因此 recall bundle 應帶：

$$
\boxed{
\Gamma_m^{\mathrm{origin}}.
}
$$

---

# 55. RaMem Interface

2026 年 RaMem 特別指出：

> 被壓縮成 reusable fragment 的記憶若丟失時間、session、participants 等原始情境，內容相關不等於對目前 query 有效。

MWT 將此吸收成：

$$
\boxed{
\text{retrieval relevance}
\neq
\text{evidential validity}.
}
$$

---

# 56. Query Recall Contract

定義：

$$
\boxed{
\mathcal C_{\mathrm{recall}}(q)
=
(
\mathcal Q,
\mathfrak I,
T,
V,
L_{\min},
B
).
}
$$

決定：

- 要哪種 memory；
- 最低 fidelity；
- time scope；
- version；
- budget。

---

# 57. Recall Fidelity

proof query 可能要求：

$$
L0/L1
$$

source / proof exact。

brainstorm query 可以：

$$
L3/L4.
$$

因此 retrieval policy 不應固定。

---

# 58. Heterogeneous Memory Types

不是所有歷史都應同一處理。

例如：

- stable profile；
- temporal event；
- exact source；
- procedural skill；
- theorem certificate；

其更新／壓縮方式不同。

---

# 59. LeanMem Interface

2026 年 LeanMem 的重要工程訊號是：

> 歷史內容應依 compressibility、temporal dynamics、fidelity requirements 分類，不應全部走同一 summarization pipeline。

MWT 將這個思想提升成 memory-tier admission。

---

# 60. Memory Compression Spectrum

同一 experience 可以逐步壓成：

$$
\boxed{
\text{episode}
\rightarrow
\text{summary}
\rightarrow
\text{skill}
\rightarrow
\text{rule}
}
$$

但越高壓縮通常 specificity 越低。

---

# 61. Experience Compression Interface

2026 年 Experience Compression Spectrum 將 memory、skills、rules 放在不同 compression levels 上。

MWT 可以借用這個觀察：

$$
\boxed{
\text{compression level should be adaptive}.
}
$$

不是所有知識永遠固定一層。

---

# 62. Multi-Level Compression

memory item：

$$
x
$$

可以同時保存：

- L0 archive；
- L2 semantic summary；
- L3 operational state；
- L4 retrieval cue。

這不是重複浪費。

是不同 query 的不同 latency/fidelity cache。

---

# 63. Memory Pyramid

概念上：

$$
\boxed{
\begin{array}{c}
\text{Active Cue}\\
\text{Operational Summary}\\
\text{Semantic Graph}\\
\text{Exact Source / Certificate}\\
\text{Cold Archive}
\end{array}
}
$$

上層小、快。

下層大、精確。

---

# 64. Forgetting

定義 forgetting action：

$$
\operatorname{Forget}_{\tau}(m).
$$

 $\tau$ 不同，語義不同。

---

# 65. Active Eviction

只從：

$$
M^A
$$

移出。

item 仍在 operational / archive。

---

# 66. Summary Replacement

full active form 被：

$$
s(m)
$$

取代。

source anchor仍存在。

---

# 67. Dormantization

memory 不再主動召回，但保留 index / provenance。

---

# 68. Archive

移到：

$$
M^X.
$$

retrieval latency升高。

---

# 69. Tombstone

內容可能不再 active可用，但保留：

- ID；
- deletion reason；
- dependency；
- archive pointer；
- hash。

---

# 70. Physical Deletion

真正刪除 underlying data。

這是最強 forgetting。

門檻最高。

---

# 71. Forgetting Judgment

定義：

$$
\boxed{
\Gamma
\vdash
\operatorname{Forget}_{\tau}(m)
\Downarrow_{\mathsf{Mem}}
f.
}
$$

其中：

$$
f
\in
\{
\mathsf{Allow},
\mathsf{Block},
\mathsf{Defer},
\mathsf{Conflicted}
\}.
}
$$

---

# 72. Forgetting Gate Family

至少：

$$
\boxed{
\begin{aligned}
g_1&=\mathsf{Dependency},\\
g_2&=\mathsf{Reconstructability},\\
g_3&=\mathsf{EvidenceRetention},\\
g_4&=\mathsf{Lineage},\\
g_5&=\mathsf{LegalPolicy},\\
g_6&=\mathsf{FutureQueryRisk},\\
g_7&=\mathsf{ArchiveIntegrity},\\
g_8&=\mathsf{ReplacementAvailability}.
\end{aligned}
}
$$

---

# 73. Hard Dependency

若：

$$
m
\rightarrow_{\mathrm{hard}}
y
$$

且 $y$ 未另有 reconstruction source，

physical delete 被：

$$
\boxed{
\mathsf{Block}.
}
$$

---

# 74. Soft Dependency

如果 memory 只提高速度，

但不是 correctness requirement，

可以 archive / evict。

---

# 75. Dependency Index

定義：

$$
\boxed{
\mathcal G_t^{M}
=
(
\mathcal M_t,
E_{\mathrm{hard}},
E_{\mathrm{soft}},
E_{\mathrm{source}},
E_{\mathrm{reconstruct}},
E_{\mathrm{conflict}}
).
}
$$

forgetting 前查這張 graph。

---

# 76. Dependency-Aware Forgetting

核心：

$$
\boxed{
\text{forget based on downstream effect, not age alone}.
}
$$

old memory 可能仍是 proof root。

new memory 可能只是 disposable cache。

---

# 77. Age-Based Eviction Is Insufficient

LRU 對 cache 有用。

但 theorem archive 不能因「很久沒看」就刪 proof source。

所以 MWT 只把 recency 當 preference signal。

---

# 78. Value Is Query-Distribution Relative

memory：

$$
m
$$

的 future value：

$$
V(m\mid\mathcal D_Q)
$$

依未來 query distribution。

這通常只能估計。

---

# 79. Irreplaceable Memory

如果：

- source unique；
- no backup；
- reconstruction impossible；

標：

$$
\boxed{
\mathsf{Irreplaceable}.
}
$$

應優先 exact archive / replication。

---

# 80. Reconstructable Memory

如果：

$$
m
$$

可由：

$$
A_1,\ldots,A_k
$$

合法重建，

可以更 aggressive evict。

---

# 81. Reconstruction Dependency

定義：

$$
\boxed{
A_1,\ldots,A_k
\Rightarrow_R
m.
}
$$

如果任一 anchor 失效，

reconstructability 可能下降。

---

# 82. Reconstruction Redundancy

多條獨立 reconstruction path：

$$
R_1,R_2
$$

可提高 robustness。

但增加 storage。

---

# 83. Forgetting Is Noncommutative

先忘：

$$
m_1
$$

再忘：

$$
m_2
$$

可能合法。

反序可能破壞 reconstruction path。

所以：

$$
\boxed{
F_{m_2}\circ F_{m_1}
\neq
F_{m_1}\circ F_{m_2}.
}
$$

forgetting 也進 MWT-03 scheduler。

---

# 84. Compression Order Is Noncommutative

先 semantic merge 再 source dedup，

與先 source dedup 再 semantic merge，

可能留下不同 provenance graph。

所以 memory maintenance需要 history。

---

# 85. Three-Zone Governance

延續 GCMS：

$$
\boxed{
Z_S
\rightarrow
Z_C
\rightarrow
Z_A.
}
$$

---

# 86. Source Zone

$$
Z_S
$$

表示：

> 我們收到／讀到了什麼。

不等於相信。

---

# 87. Candidate Zone

$$
Z_C
$$

表示：

> 可能值得納入 world knowledge，但尚未完成驗證／衝突消解。

---

# 88. Accepted Zone

$$
Z_A
$$

表示：

> 已通過當前 acceptance contract，可供 Stable Core / query 使用。

---

# 89. Rejected Does Not Mean Deleted

candidate 被 reject，

source 可繼續 archive。

未來新 context 可以 reopen。

---

# 90. Memory Poisoning

如果未驗證內容直接：

$$
Z_S
\to
Z_A,
$$

長期系統容易累積：

- hallucination；
- malicious injection；
- outdated claim；
- source confusion。

---

# 91. Candidate Conflict

新 memory：

$$
m_n
$$

與 accepted：

$$
m_a
$$

衝突，

不應直接 overwrite。

進：

$$
\boxed{
M^Q.
}
$$

---

# 92. Conflict-Aware Save

save operation 先查：

$$
\operatorname{Neighbors}(m_n).
$$

如果 contradiction candidate：

$$
\boxed{
\text{save}
\rightarrow
\text{conflict obligation}.
}
$$

---

# 93. Memory Integrity

exact archive item：

$$
x
$$

可以定期驗：

$$
h(x)
$$

與 stored fingerprint。

這能偵測 bit-level corruption。

---

# 94. Semantic Integrity

semantic summary：

$$
s
$$

無法只靠 hash 證明沒有失真。

需要：

$$
\boxed{
\operatorname{Audit}
(
s,x,\mathfrak I,\mathcal Q
).
}
$$

---

# 95. Summary Drift

多次：

$$
x
\to
s_1
\to
s_2
\to
s_3
$$

可能累積語義漂移。

因此：

$$
\boxed{
\text{recompress from summary}
}
$$

與：

$$
\boxed{
\text{recompress from source}
}
$$

必須分開。

---

# 96. Source-Refresh Compression

定期從：

$$
x_{\mathrm{source}}
$$

重新生成：

$$
s'
$$

可以校正 summary drift。

---

# 97. Recursive Compression Debt

如果只能從已壓縮 memory 再壓縮，

產生：

$$
\boxed{
D_{\mathrm{comp}}.
}
$$

未來需要 source audit。

---

# 98. Proof Summary

proof：

$$
\pi
$$

可以有 human summary：

$$
s_\pi.
$$

但 theorem validity仍由：

$$
\pi
$$

或 certificate 支持。

---

# 99. Proof Cache

已驗證 proof 可以 cache：

$$
\boxed{
(\phi,h(\pi),V_{\mathrm{checker}},\mathsf{verified})
}
$$

未必要每次 full replay。

---

# 100. Cached Verification Is Version-Relative

checker / library 更新後，

舊 verification cache可能需要：

$$
\boxed{
\mathsf{Revalidate}.
}
$$

---

# 101. Certificate Cache Hierarchy

可以：

- full proof；
- proof hash；
- verified result；
- independent recheck result。

不同 risk query選不同 replay depth。

---

# 102. Memory Recall as Evidence

如果 query 要正式 evidence，

recall 必須回到：

$$
M^S/M^C.
$$

不能只拿 L4 heuristic cue。

---

# 103. Evidence Escalation

流程：

$$
\boxed{
\text{cue}
\to
\text{summary}
\to
\text{source}
\to
\text{certificate}
}
$$

按 query risk逐級提升。

---

# 104. Lazy Materialization

不要一開始載完整 source。

只有需要時：

$$
\operatorname{Materialize}(h(x)).
$$

這節省 active context。

---

# 105. Memory Page-In / Page-Out

可以類比 virtual memory：

- page-in relevant memory；
- page-out inactive memory。

但 semantic memory selection 比 OS page replacement 更複雜。

---

# 106. Self-Calling Memory

GCMS 已提出：

> memory system 應在某些條件主動喚起自身，而不只被 user explicit query 觸發。

MWT 將其稱：

$$
\boxed{
\mathsf{RecallTrigger}.
}
$$

---

# 107. Recall Trigger Types

至少：

1. query match；
2. legality dependency；
3. conflict；
4. certificate expiry；
5. branch reopen；
6. identity ambiguity；
7. similar past failure；
8. resource optimization；
9. version migration。

---

# 108. Proactive Recall Is Bounded

不能每輪把所有相關 memory 都喚醒。

需要：

$$
B_{\mathrm{recall}}.
$$

否則 memory 自調用會重新造成 context explosion。


# 109. Memory Retrieval Budget

定義：

$$
\boxed{
B_{\mathrm{recall}}
=
(
b_{\mathrm{items}},
b_{\mathrm{tokens}},
b_{\mathrm{latency}},
b_{\mathrm{source}},
b_{\mathrm{verify}}
).
}
$$

retrieval planner 要在 fidelity 與 cost 之間選擇。

---

# 110. Retrieval Portfolio

對 query：

$$
q,
$$

可以同時召回：

- 1 個高層 summary；
- 3 個 source anchors；
- 1 個 proof certificate；
- 2 個 conflict candidates。

不是只回 top- $k$ 相似 chunks。

---

# 111. Recall Diversity

如果所有 recalled memory 都來自同一 summary lineage，

可能產生 shared compression blind spot。

因此高風險 query 可以要求：

$$
\boxed{
\text{source-lineage diversity}.
}
$$

---

# 112. Memory Confidence Is Not Retrieval Score

vector similarity：

$$
s(q,m)
$$

只表示 retrieval signal。

不能直接當：

$$
\operatorname{Truth}(m).
$$

---

# 113. Memory Validity Horizon

某 memory：

$$
m
$$

可能有：

$$
H_V(m)
=
[t_0,t_1].
$$

過期後可以：

- recall as historical；
- revalidate；
- quarantine。

---

# 114. Temporal Memory

事件型 memory 需要：

- event time；
- observation time；
- recording time；
- revision time。

這些時間不應全部壓成一個 timestamp。

---

# 115. Event Time vs Mention Time

某 query 問：

> 當時發生什麼？

需要 event-time memory。

問：

> 我何時第一次知道？

需要 knowledge / mention time。

因此 temporal provenance 是 query-dependent。

---

# 116. Lineage

長期 world memory 形成：

$$
\boxed{
\mathcal L_M
=
(
M^{(0)},
\Delta_0,
M^{(1)},
\Delta_1,
\ldots
).
}
$$

每次 memory migration 都保留 transition witness。

---

# 117. Migration

memory format：

$$
F^{(v)}
\to
F^{(v+1)}
$$

需要：

$$
\boxed{
\operatorname{Migrate}_{v\to v+1}.
}
$$

---

# 118. Migration Certificate

$$
\boxed{
C_{\mathrm{mig}}
=
(
C_{\mathrm{source}},
C_{\mathrm{mapping}},
C_{\mathrm{loss}},
C_{\mathrm{verify}}
).
}
$$

不能只「匯入成功」。

---

# 119. Lossless Migration

若：

$$
R_{v+1}
(
\operatorname{Migrate}(x)
)
=
R_v(x)
$$

在 L0/L1 contract 下，

可稱 lossless migration。

---

# 120. Semantic Migration

若只保持：

$$
\equiv_{\mathfrak I,\mathcal Q},
$$

則是 semantic migration。

需要明示 loss。

---

# 121. Migration Debt

如果某 legacy artifact 無法完全遷移，

保留：

$$
\boxed{
D_{\mathrm{mig}}.
}
$$

以及 old reader / archived environment。

---

# 122. Executable Archive

對 proof/software-dependent artifact，

只存 bytes 可能不夠。

還需要：

- runtime；
- compiler；
- library；
- model；
- environment metadata。

因此：

$$
\boxed{
\text{artifact preservation}
\neq
\text{execution preservation}.
}
$$

---

# 123. Environment Capsule

可以為高價值 proof / computation 保存：

$$
\boxed{
E_{\mathrm{capsule}}
=
(
\text{source},
\text{dependencies},
\text{versions},
\text{config},
\text{checksums}
).
}
$$

---

# 124. Replayability

memory item：

$$
m
$$

若可重新產生：

$$
y
$$

且：

$$
y
\equiv_{\mathfrak I}
y_{\mathrm{old}},
$$

稱：

$$
\boxed{
\mathsf{Replayable}_{\mathfrak I}.
}
$$

---

# 125. Replayability Is Not Bitwise Determinism

stochastic / parallel systems 可以不 bitwise identical，

但仍 operational equivalent。

所以 replay也帶 identity specification。

---

# 126. Long-Horizon Integrity

對幾十年 archive，

需要定期：

- hash audit；
- replica check；
- format migration；
- dependency validation；
- certificate recheck。

memory persistence 是 active maintenance，不是寫一次就永遠安全。

---

# 127. Bit Rot / Format Rot / Semantic Rot

至少分：

### Bit Rot

raw bytes損壞。

### Format Rot

bytes 在，但 parser / runtime 消失。

### Semantic Rot

格式可讀，但 definitions / assumptions / external references 已改。

三者 repair 不同。

---

# 128. Source Anchor

任何 L2/L3 memory 最好能追到：

$$
\boxed{
A(m)
}
$$

source anchor。

如果沒有，標：

$$
\mathsf{UnanchoredSemanticMemory}.
$$

---

# 129. Unanchored Memory

某些 human / AI idea 沒有原始 artifact。

可以保存，但 evidence maturity低。

不能偽造 source。

---

# 130. Memory Acceptance Workflow

新 memory：

$$
m_n
$$

最低流程：

```text
1. ingest source
2. assign provenance
3. detect duplicates
4. detect conflict
5. classify fidelity requirement
6. place in source/candidate/accepted zone
7. build indexes / summaries
8. create reconstruction contract
9. attach retention policy
10. update dependency graph
```

---

# 131. Memory Consolidation

多個 episodes：

$$
e_1,\ldots,e_n
$$

可 consolidated 成：

$$
k.
$$

但：

$$
k
$$

應指回 supporting episodes。

---

# 132. Consolidation Is Not Evidence Multiplication

五個 summaries 都來自同一 source，

不等於五個 independent evidence。

lineage 必須保存。

---

# 133. Semantic Merge

若：

$$
m_1,m_2
$$

都表達同一 stable claim，

可以 merge semantic nodes。

但 source provenance：

$$
p_1,p_2
$$

保持多源。

---

# 134. Dedup vs Consolidation

byte dedup：

$$
x_1=x_2.
$$

semantic consolidation：

$$
x_1\equiv_{\mathfrak I}x_2.
$$

兩者不能共用同一判定器。

---

# 135. Memory Pollution

若 hallucinated / malicious / stale memory進 Accepted Zone，

它會透過：

- query answer；
- proof planning；
- solver selection；
- new memory synthesis；

遞歸污染。

所以 long-term memory error 可能累積放大。

---

# 136. Pollution Propagation Graph

定義：

$$
\boxed{
\mathcal G_{\mathrm{poll}}
}
$$

追蹤：

$$
m_{\mathrm{bad}}
\leadsto
\{
c_1,c_2,\ldots
\}.
$$

修正 memory 後可 targeted revalidation。

---

# 137. Quarantine Reopen

如果 candidate 後來取得新 certificate，

$$
M^Q
\to
M^{\mathrm{accepted}}.
$$

反之 accepted memory 被反例擊中，可：

$$
M^{\mathrm{accepted}}
\to
M^Q.
$$

memory status 可逆，但 history保留。

---

# 138. Memory Revocation

對已 accepted：

$$
m
$$

可：

$$
\boxed{
\operatorname{Revoke}(m).
}
$$

所有 hard dependents 進 MWT-04 revalidation queue。

---

# 139. Revocation Does Not Delete Archive

錯誤 theorem 被撤銷，

historical source 仍然有研究價值。

所以：

$$
\boxed{
\text{invalidated}
\neq
\text{erased}.
}
$$

---

# 140. Forgetting and Ethics / Governance

若 memory 涉及：

- private data；
- legal retention；
- deletion request；
- security；

physical deletion policy 可覆蓋 epistemic retention。

但 deletion event 必須有 governance provenance。

---

# 141. Mathematical Retention vs Data Governance

MWT 不主張：

> 為了數學完整就永遠不能刪資料。

外部治理可以要求刪除。

此時 downstream certificate / memory status 要誠實降級。

---

# 142. Memory Budget Optimization

對 memory set：

$$
\mathcal M,
$$

可研究：

$$
\boxed{
\max
\operatorname{FutureUtility}
(
\mathcal M'
)
}
$$

subject to：

$$
\operatorname{Cost}(\mathcal M')
\leq B_M.
$$

但 FutureUtility通常不可精確知道。

---

# 143. MemRefine Interface

2026 年 MemRefine 將 long-term agent memory 管理直接形式化為：

> 在固定 storage budget 下，對 memories 做 merge / delete / preserve，以保留 downstream usefulness。

MWT 將其視為 memory-budget optimization 的最新專門 backend。

但 MWT 加入：

- proof/source anchors；
- reconstruction levels；
- dependency hard constraints；
- Stable Core governance。

---

# 144. Budgeted Merge Cannot Override Hard Evidence Retention

即使 memory budget 很小，

proof root：

$$
m_p
$$

若是唯一 hard source，

不能只因 compression optimizer覺得低 relevance 就刪。

hard retention先於 utility optimization。

---

# 145. Compression Gain

定義：

$$
\boxed{
G_K
=
\frac{
S_{\mathrm{before}}
-
S_{\mathrm{after}}
}{
S_{\mathrm{before}}
}.
}
$$

只是 storage gain。

不是 memory quality。

---

# 146. Reconstruction Quality

定義 profile：

$$
\boxed{
Q_R
=
(
Q_{\mathrm{exact}},
Q_{\mathrm{semantic}},
Q_{\mathrm{operational}},
Q_{\mathrm{provenance}}
).
}
$$

不要求 scalar。

---

# 147. Compression Pareto Frontier

memory policies：

$$
\pi_i
$$

可以比較：

- storage；
- recall latency；
- reconstruction fidelity；
- maintenance；
- privacy；
- provenance。

保留 Pareto frontier。

---

# 148. No Universal Compression Ratio

不同 domains：

- proofs；
- dialogue；
- numerical fields；
- source code；

可壓縮性差很多。

所以 MWT 不定 universal 10x / 100x 目標。

---

# 149. Long-Horizon Knowledge Lifecycle

一個 memory item：

$$
m
$$

可以經：

$$
\boxed{
\text{Ingest}
\to
\text{Candidate}
\to
\text{Accept}
\to
\text{Use}
\to
\text{Compress}
\to
\text{Dormant}
\to
\text{Reopen}
\to
\text{Revise}
\to
\text{Archive}.
}
$$

不必單向。

---

# 150. Memory Dynamic Fixed Point

對目前 workload：

$$
\mathcal D_Q
$$

與 budget：

$$
B_M,
$$

如果：

- no mandatory migration；
- no unsafe compression debt；
- active tier within budget；
- retrieval/reconstruction contracts satisfied；

可以定義：

$$
\boxed{
\operatorname{MDFP}
(
\mathfrak M^W
)
=1.
}
$$

這只是 memory quiescence。

---

# 151. Memory Reopen

新 query / theorem / version 可以觸發：

$$
\boxed{
\operatorname{ReopenMemory}(m).
}
$$

例如：

- weak summary 不夠；
- proof source需要 full replay；
- old branch重新有價值。

---

# 152. Memory Reopen Is a Core Requirement

如果 compression 後永遠無法回 source，

那只能稱 destructive compression。

對高價值 knowledge，MWT 優先：

$$
\boxed{
\text{reopenable compression}.
}
$$

---

# 153. World Memory Store

第一個 MWT-10 runtime 模組：

$$
\boxed{
\mathsf{WMS}.
}
$$

管理 memory tiers 與 metadata。

---

# 154. Source Archive

第二個：

$$
\boxed{
\mathsf{SA}.
}
$$

負責 exact / content-addressed artifacts。

---

# 155. Semantic Reconstruction Store

第三個：

$$
\boxed{
\mathsf{SRS}.
}
$$

保存 generative kernels、summaries、semantic graph、reconstruction recipes。

---

# 156. Certificate Cache

第四個：

$$
\boxed{
\mathsf{CCache}.
}
$$

保存 proof / validation results 與 version scope。

---

# 157. Dependency Index

第五個：

$$
\boxed{
\mathsf{DI}.
}
$$

支援：

- forgetting；
- revocation；
- reopen；
- incremental revalidation。

---

# 158. Recall Controller

第六個：

$$
\boxed{
\mathsf{RC}_{M}.
}
$$

依 query contract組 recall portfolio。

---

# 159. Forgetting Gate

第七個：

$$
\boxed{
\mathsf{FG}.
}
$$

判定 eviction / archive / deletion。

---

# 160. Deduplication Engine

第八個：

$$
\boxed{
\mathsf{DE}.
}
$$

分開：

- byte dedup；
- structural dedup；
- semantic consolidation。

---

# 161. Integrity / Revalidation Engine

第九個：

$$
\boxed{
\mathsf{IRE}.
}
$$

做：

- hash audit；
- certificate expiry；
- semantic drift audit；
- source refresh。

---

# 162. Migration Engine

第十個：

$$
\boxed{
\mathsf{ME}_{M}.
}
$$

處理 format / schema / proof-library migration。

---

# 163. Lineage Ledger

第十一個：

$$
\boxed{
\mathsf{LL}.
}
$$

保存 world memory lineage、merge、fork、revocation。

---

# 164. Memory Budget Manager

第十二個：

$$
\boxed{
\mathsf{MBM}.
}
$$

讀 MWT-09 resource budget，決定 tier allocation。

---

# 165. Reference Memory Evaluator

本 Source Pack 附：

```text
mwt10_memory_reference.py
```

固定最低 v0.1 semantics：

- memory tier；
- reconstruction level；
- exact vs semantic reconstruction guard；
- hard-dependent forgetting block；
- active eviction vs physical deletion distinction；
- query recall fidelity requirement；
- accepted / candidate / source zone separation。

它不是 semantic compressor，也不是 vector database。

---

# 166. MWT-10 Minimal Constitution

v0.1 固定三十四條：

### M1 — Memory Is Not Context

不在 active context 不等於忘記。

### M2 — Memory Is Not Storage

storage 只是一層。

### M3 — Runtime Memory Is Not World

 $\mathfrak M^W$ 仍是 presentation。

### M4 — Exact and Semantic Tracks Must Be Separated

生成重建不得冒充 bit-exact recovery。

### M5 — Reconstruction Level Must Be Declared

每個壓縮 memory 要說能重建到哪一層。

### M6 — Compression Is Query-Relative

對不同 future queries 可壓縮程度不同。

### M7 — Compression Is Not Automatically Better

更小可能意味更高 loss。

### M8 — Source Anchors Are Preferred for Formal Evidence

高風險 claim 不應只依 heuristic memory。

### M9 — Certificates Are Memory Objects

proof / legality / coverage certificates要獨立保存。

### M10 — Active Memory Must Be Bounded

長期 world 不允許 context 單調無限增長。

### M11 — Dormant and Archived Memory Are First-Class

不 active 的 knowledge仍可存在。

### M12 — Content Addressing Is Byte-Level, Not Semantic Truth

hash identity 不等於 theorem equivalence。

### M13 — New Versions Must Not Destroy Provenance by Default

重要舊版本需可追溯。

### M14 — Structural Sharing Is Allowed

不必複製全部 history。

### M15 — Reconstruction Cost Is a Resource

壓縮不能只看 storage。

### M16 — Recall Is Context-Sensitive

相似度不是 evidential validity。

### M17 — Recall Fidelity Is Query-Sensitive

proof query 和 brainstorming query 不同。

### M18 — Source/Candidate/Accepted Zones Must Be Separated

新資訊不可直接污染 Stable Core。

### M19 — Conflict Must Quarantine Before Overwrite

衝突 memory 不得靜默覆蓋舊 accepted knowledge。

### M20 — Forgetting Has Types

evict、summarize、archive、delete 不可混稱。

### M21 — Physical Deletion Has the Highest Burden

唯一 source / hard dependency 不能隨便刪。

### M22 — Forgetting Is Dependency-Aware

age / recency 不是唯一依據。

### M23 — Forgetting May Be Noncommutative

maintenance order 需進 scheduler。

### M24 — Compress Is Not Erase

高價值 memory 優先可重建式壓縮。

### M25 — Recursive Compression Can Drift

summary-of-summary 必須追蹤 compression debt。

### M26 — Exact Integrity and Semantic Integrity Are Different

hash audit 不能驗證 summary truth。

### M27 — Migration Must Carry Fidelity Contract

格式升級不是無條件 lossless。

### M28 — Replayability Is Identity-Relative

不要求所有系統 bitwise replay。

### M29 — Long-Horizon Persistence Requires Maintenance

archive 不是寫一次就永遠安全。

### M30 — Invalidated Knowledge May Remain Historical

撤銷不等於抹去歷史。

### M31 — Memory Governance Can Override Epistemic Retention

合法 deletion request 可要求物理刪除，但 downstream 狀態必須降級。

### M32 — Budget Optimization Cannot Override Hard Retention

memory utility score不能刪唯一 proof root。

### M33 — Memory Answers Must Preserve Provenance

recall 到 output 的 lineage 可審計。

### M34 — First-Cycle MWT Closure

MWT-10 完成 MWT v0.1 第一輪 01～10 核心層；後續優先統合與實作，不以無限追加篇次取代工程收斂。

---

# 167. 命題：Semantic Reconstruction Does Not Imply Exact Recovery

若：

$$
\widehat x
\equiv_{\mathfrak I,\mathcal Q}
x
$$

但：

$$
\widehat x\neq x
$$

bytes，

則只能宣稱 L2／L3 reconstructability，不能宣稱 L0。

---

# 168. 命題：Active Eviction Does Not Destroy Archived Memory

若：

$$
m
$$

只從：

$$
M^A
$$

移到：

$$
M^D/M^X,
$$

且 archive pointer 保留，

則 memory item仍可未來 materialize。

---

# 169. 命題：Hard Dependency Blocks Unrecoverable Physical Deletion

若：

$$
m
\to_{\mathrm{hard}}y
$$

且不存在：

$$
R(A)=m
$$

替代 reconstruction path，

則由 M21/M22：

$$
\operatorname{DeletePhysical}(m)
$$

不能被預設 Allow。

---

# 170. 命題：Byte Dedup Does Not Merge Provenance

即使：

$$
x_1=x_2
$$

bytes，

若 source provenance不同：

$$
p_1\neq p_2,
$$

archive 可共享 content object，

但 provenance records仍應保留兩條。

---

# 171. 條件定理：Safe Semantic Compression

若：

1. source $x$ exact archive存在；
2. semantic compressed memory $m=K(x)$ ；
3. reconstruction contract指定 $(\mathfrak I,\mathcal Q)$ ；
4. audit證：
   $$
   R(m)\equiv_{\mathfrak I,\mathcal Q}x;
   $$
5. archive pointer與version完整；

則 $m$ 可在該 query scope 取代 $x$ 作 active semantic memory，而不宣稱 exact source 被刪除。

---

# 172. 條件定理：Safe Active Forgetting

若：

1. item $m$ 不再 mandatory active；
2. hard dependents有可用替代 source；
3. archive / dormant pointer valid；
4. recall contract仍可滿足；

則：

$$
\boxed{
\operatorname{EvictActive}(m)
}
$$

可在目前 scope Allow。

---

# 173. 條件定理：Persistent World Lineage

若每次 world-state revision：

$$
v\to v+1
$$

都保存：

- parent pointers；
- migration certificate；
- source/certificate roots；
- tombstones；
- continuity witness；

則長期 runtime 可以建立可追溯 memory lineage，即使 active state 經多次壓縮與 coarsening。

---

# 174. 研究猜想：Small Active Core, Huge Reopenable World

成熟 AI mathematics 最可行的形態可能是：

$$
\boxed{
\text{small active state}
+
\text{massive content-addressed archive}
+
\text{query-conditioned reconstruction}.
}
$$

而不是「把所有知識放進 context」。

---

# 175. 研究猜想：Memory Compression Becomes a Mathematical Operation

當 memory summaries、proof caches、branch compression開始影響未來 theorem search 時，compression 本身可能需要被視為：

$$
\boxed{
\text{first-class mathematical transformation}.
}
$$

其 soundness 需要和 ordinary proof step 一樣被審計。

---

# 176. 研究猜想：Long-Horizon AI Will Need Adaptive Compression Levels

固定「所有 memory 都 summary 成同樣長度」可能不是 scalable solution。

更可能是：

$$
\boxed{
\text{query/fidelity/risk-conditioned multilevel compression}.
}
$$

這與 2026 年 long-term agent memory 的 emerging trend 一致。

---

# 177. 研究猜想：Reconstructability Is More Important Than Raw Retention Rate

對真正長期 world，

比「保存了多少 tokens」更重要的可能是：

> 重要 claims、proofs、lineages 在需要時能否被合法重建到正確 fidelity。

---

# 178. 研究猜想：Memory Pollution Is a Recursive Risk

一個錯誤 accepted memory 若被用來：

- 生成新 theorem；
- 做 summary；
- 教另一 agent；
- 建新 bridge；

會造成 recursive contamination。

因此 long-horizon memory validation 的重要性可能隨時間超線性增加。

---

# 179. 開放問題

### O1 — Universal Reconstruction Metric

不同 memory types 是否存在共同 reconstructability framework？

### O2 — Minimal Sufficient Memory

對 query distribution，最小 operational memory 是什麼？

### O3 — Future Query Unknown

如果不知道未來會問什麼，compression contract 如何保守設計？

### O4 — Proof Archive Longevity

proof assistant 幾十年後如何 replay？

### O5 — Semantic Drift Detection

summary 何時已偏離 source？

### O6 — Dependency-Aware Deletion Complexity

大型 memory graph 上安全 deletion 是否昂貴？

### O7 — Memory Poisoning Recovery

已污染多層 derived knowledge 後如何最小化回滾？

### O8 — Cross-Agent Memory Inheritance

另一 AI 如何繼承 memory 而不把 identity / provenance 混掉？

### O9 — Content-Addressed Semantic Objects

semantic identity 能否建立類 content-addressed 的可證標準？

### O10 — Century-Scale Mathematical World

如何使 theorem、proof、software、data、environment 在百年尺度仍可解讀與重驗？

---

# 180. 外部研究接口：Persistent Data Structures

Driscoll、Sarnak、Sleator、Tarjan 1989 的經典工作研究更新後仍可存取舊版本的 persistent data structures。

MWT 以它作 version-preserving memory 的基本理論接口。

---

# 181. 外部研究接口：Venti

Quinlan 與 Dorward 2002 的 Venti 以內容 hash 作 archival block address，提供 write-once 與 deduplication 特性。

MWT 以它作 exact source archive 的成熟工程參照。

---

# 182. 外部研究接口：Self-Adjusting Computation

Acar 等人的 self-adjusting computation 研究以 dependency / memoization / change propagation 讓輸入變更後只更新受影響計算。

MWT 將它接入：

$$
\boxed{
\text{memory update}
\to
\text{dependency slice}
\to
\text{incremental revalidation}.
}
$$

---

# 183. 外部研究接口：MemRefine

MemRefine 2026 對 hard storage budget 下的長期 Agent memory 進行 merge / delete / preserve 決策，並指出 surface similarity 不足以決定 factual value。

MWT 將其視為 budgeted semantic memory maintenance backend。

---

# 184. 外部研究接口：RaMem

RaMem 2026 指出被 retrieval 的 memory fragment 若缺 event time、session、participants 等 context，可能看起來相關但並非有效 evidence。

MWT 將 context reinstatement 納入 Recall Contract。

---

# 185. 外部研究接口：LeanMem

LeanMem 2026 按 compressibility、temporal dynamics 與 fidelity requirement 對歷史內容採不同 memory representation與 maintenance策略。

MWT 將它視為 heterogeneous memory-tier design 的最新鄰接工作。

---

# 186. 外部研究接口：Experience Compression Spectrum

2026 的 Experience Compression Spectrum 將 episodic memory、procedural skill、declarative rules 理解為不同 compression levels，並指出跨 level adaptive compression 是重要缺口。

MWT 以此支援 multi-level compression，而不接受固定 compression level。

---

# 187. 與 GCMS 的接口

GCMS 已經提出：

- 生成式壓縮記憶；
- 原文無損軌；
- 語義生成軌；
- 多路徑知識索引；
- 自調用 memory；
- pollution / candidate / accepted governance；
- 多智能體認知繼承。

MWT-10 不取代 GCMS。

更準確地：

$$
\boxed{
\text{GCMS}
=
\text{MWT Memory Layer 的重要 specialized architecture candidate}.
}
$$

---

# 188. 與 MWT-09 的接口

MWT-09 說：

$$
\text{storage / verification / maintenance}
$$

都要付成本。

MWT-10 回答：

> 怎麼在有限 budget 中配置 memory tiers。

---

# 189. 與 MWT-08 的接口

Global Quantifier Certificate：

$$
C_{\forall}
$$

不能只存 theorem sentence。

MWT-10 管：

- proof object；
- coverage roots；
- checker version；
- compression；
- replay。

---

# 190. 與 MWT-07 的接口

Query Compiler 生成 Recall Contract：

$$
\mathcal C_{\mathrm{recall}}(q).
$$

Memory Layer 只 materialize 必要 fidelity。

---

# 191. 與 MWT-06 的接口

World Solve 的：

- checkpoints；
- coupling histories；
- solver states；
- residual histories；

由 Memory Layer 決定哪部分 active、哪部分 archive。

---

# 192. 與 MWT-05 的接口

refinement 新增：

- dimensions；
- presentations；
- observers；

也會新增 memory burden。

coarsening 與 memory compression共同控制 active support。

---

# 193. 與 MWT-04 的接口

MWT-04 原本：

$$
\mathcal H_t
=
(
M_t^{\mathrm{op}},
R_t^{\mathrm{archive}}
).
$$

MWT-10 將這一簡寫展開成完整 memory architecture。

---

# 194. MWT-01～10 第一輪閉合

現在可以完整列出：

$$
\boxed{
\begin{array}{ll}
\text{MWT-01} & \text{World / Presentation}\\
\text{MWT-02} & \text{Legality}\\
\text{MWT-03} & \text{Scheduling / Noncommutativity}\\
\text{MWT-04} & \text{World State / Dynamic Fixed Point}\\
\text{MWT-05} & \text{Unbounded Refinement}\\
\text{MWT-06} & \text{Global Coupling / World Solve}\\
\text{MWT-07} & \text{Query / Inference Federation}\\
\text{MWT-08} & \text{Global Quantification / Coverage}\\
\text{MWT-09} & \text{Computability / Resources}\\
\text{MWT-10} & \text{Memory / Long-Horizon Persistence}.
\end{array}
}
$$

---

# 195. 第一輪 Mother Cycle

十篇合併後：

$$
\boxed{
\begin{aligned}
\mathbf W
&\xRightarrow{\text{Presentation}}
\mathcal G^P\\
&\xrightarrow{\text{Legality}}
\mathcal I^+\\
&\xrightarrow{\text{Schedule}}
\mathcal G^I\\
&\xrightarrow{\text{Commit}}
\mathfrak S^{\mathrm{MWT}}\\
&\xrightarrow{\text{Refine}}
\mathfrak S'\\
&\xrightarrow{\text{Couple/Solve}}
\Omega\\
&\xrightarrow{\text{Query}}
\mathfrak A_{\mathfrak Q}\\
&\xrightarrow{\text{Quantify}}
C_{\forall}\\
&\xrightarrow{\text{Resource}}
\mathcal M_B\\
&\xrightarrow{\text{Memory}}
\mathfrak M^W\\
&\rightsquigarrow
\text{Reopen / Continue}.
\end{aligned}
}
$$

---

# 196. 為什麼先停在 10？

因為現在基本運行責任已完整覆蓋：

- 表示；
- 作用；
- 順序；
- 狀態；
- 擴張；
- 耦合；
- 提問；
- 全域；
- 資源；
- 記憶。

繼續增加 MWT-11、12、13 很容易重新碎片化。

---

# 197. 下一階段不是 MWT-11

下一階段建議：

$$
\boxed{
\text{MWT v0.2 Integration}
}
$$

工作是：

1. 統一 01～10 symbols；
2. 消除跨篇重複；
3. 建 mother runtime schema；
4. 統一 certificate hierarchy；
5. 建 reference implementation；
6. 建第一個 experimental mathematical world；
7. 做 falsification / benchmark。

---

# 198. MWT v0.2 Mother Runtime 候選

可寫：

$$
\boxed{
\mathfrak R_{\mathrm{MWT}}
=
(
\mathsf{PReg},
\mathsf{LE},
\mathsf{NCS},
\mathsf{WSS},
\mathsf{Ref},
\mathsf{GCC},
\mathsf{QC},
\mathsf{UCV},
\mathsf{FE},
\mathsf{WMS}
).
}
$$

對應十篇。

---

# 199. 第一個 Experimental World

最好的第一個實驗不是「全數學」。

而是 bounded world：

- 2～3 presentations；
- 2 solvers；
- proof + computation；
- finite domain；
- versioned memory；
- one refinement path；
- one coupling query。

讓十個 layers 全部真的跑一次。

---

# 200. 一句話版

> **MWT-10 將長期數學記憶建立為「小型 active state＋可重建壓縮層＋精確 source/certificate archive＋版本 lineage」的多層世界記憶，而不是無限 transcript。原文逐位元無損與生成式語義重建被永久分成雙軌；每個 compressed memory 都必須聲明能重建到 Byte Exact、Structural Exact、Semantic Equivalent、Operational Sufficient 或 Heuristic Recall 的哪一層。記憶的 eviction、summary、dormant、archive、tombstone 與 physical deletion 也被分開，任何遺忘都要檢查 hard dependencies、reconstructability 與 evidence retention。新資訊經 Source→Candidate→Accepted 三區治理，衝突先 quarantine，不直接污染 Stable Core。由此，MWT 可以在有限 active memory 下保存巨大、版本化、可追溯、可重新展開的數學世界；而 MWT-01～10 至此完成第一輪核心閉合，下一階段應轉向 v0.2 統合與實驗 runtime，而不是繼續無限制增加篇次。**

---

# 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $\mathfrak M_t^W$ | MWT World Memory State |
| $M^A$ | Active Memory |
| $M^O$ | Operational Memory |
| $M^S$ | Source Memory |
| $M^C$ | Certificate Memory |
| $M^D$ | Dormant Memory |
| $M^R$ | Reconstruction Memory |
| $M^H$ | History / Lineage Memory |
| $M^Q$ | Quarantine / Candidate Memory |
| $M^X$ | External / Archived Memory |
| $E_L,D_L$ | lossless encode/decode |
| $E_S,R_S$ | semantic compression/reconstruction |
| $\mathcal C_R$ | Reconstruction Contract |
| $\mathcal C_K$ | Compression Contract |
| $\mathcal L_R$ | reconstruction loss |
| $\mathcal G^M$ | memory dependency graph |
| $\mathcal C_{\mathrm{recall}}$ | Recall Contract |
| $B_M$ | memory budget |
| $\mathsf{WMS}$ | World Memory Store |
| $\mathsf{SA}$ | Source Archive |
| $\mathsf{SRS}$ | Semantic Reconstruction Store |
| $\mathsf{CCache}$ | Certificate Cache |
| $\mathsf{DI}$ | Dependency Index |
| $\mathsf{RC}_M$ | Recall Controller |
| $\mathsf{FG}$ | Forgetting Gate |
| $\mathsf{DE}$ | Deduplication Engine |
| $\mathsf{IRE}$ | Integrity/Revalidation Engine |
| $\mathsf{ME}_M$ | Migration Engine |
| $\mathsf{LL}$ | Lineage Ledger |
| $\mathsf{MBM}$ | Memory Budget Manager |

---

# 附錄 B：v0.1 非主張清單

MWT-10 不主張：

1. 所有數學歷史都應永遠保存 active；
2. 所有資料都不能刪；
3. semantic summary 可取代 exact source；
4. LLM reconstruction 等於原文還原；
5. content hash 等於 semantic identity；
6. cryptographic hash 永遠沒有 collision；
7. 所有 memory 可無損壓縮；
8. 所有 memory 都應用同 compression level；
9. retrieval similarity 等於 evidence validity；
10. recent memory 永遠比 old memory 有價值；
11. LRU 足以治理 theorem memory；
12. accepted knowledge 永不被撤銷；
13. candidate memory 一定錯；
14. quarantine 等於永久 reject；
15. archived memory 永遠可直接執行；
16. bytes 保存就保證未來 software 可重放；
17. summary drift 能完全自動偵測；
18. reconstruction path 永遠低成本；
19. forgetting operations 都交換；
20. physical deletion 可以無視 dependencies；
21. proof cache 永遠不需 reverify；
22. exact source 每次 query 都應 materialize；
23. Agent memory benchmark 等於長期數學記憶；
24. MemRefine、RaMem、LeanMem 等於 MWT；
25. persistent data structures 等於 MWT world-state；
26. Venti 等於 semantic memory；
27. archive 寫一次後不需維護；
28. cross-agent memory inheritance 不會造成 identity drift；
29. compression ratio 可以單獨衡量 memory quality；
30. 小 active state 必然足夠所有未來問題；
31. GCMS 被 MWT 取代；
32. MWT-10 已解決百年 digital preservation；
33. MWT-01～10 已成為完整 foundation of mathematics；
34. 第一輪封頂表示 MWT 永不再修訂。

---

# 附錄 C：外部研究接口與參考文獻

1. James R. Driscoll, Neil Sarnak, Daniel D. Sleator, and Robert E. Tarjan, **Making Data Structures Persistent**, *Journal of Computer and System Sciences*, 38(1), 1989, pp. 86–124. DOI: 10.1016/0022-0000(89)90034-2.  
2. Sean Quinlan and Sean Dorward, **Venti: A New Approach to Archival Data Storage**, FAST 2002, USENIX.  
3. Umut A. Acar, Matthias Blume, and Jacob Donham, **A Consistent Semantics of Self-Adjusting Computation**, ESOP 2007 / later Journal of Functional Programming version.  
4. Minjae Kim, Jinheon Baek, Soyeong Jeong, and Sung Ju Hwang, **MemRefine: LLM-Guided Compression for Long-Term Agent Memory**, 2026, arXiv:2606.13177.  
5. Wei Yang et al., **RaMem: Contextual Reinstatement for Long-term Agentic Memory**, 2026, arXiv:2606.22844.  
6. Xing Zhang et al., **Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents**, 2026, arXiv:2604.15877.  
7. Yuxin Liao et al., **LeanMem: Simple and Efficient Long-Term Memory for LLM Agents**, 2026, arXiv:2608.03463.  

---

# 附錄 D：內部依賴

MWT-10 直接依賴：

- MWT-01 ～ MWT-09
- GCMS《生成式壓縮記憶系統技術白皮書》
- GCMS《生成式壓縮記憶：人類如何在大型知識網路中保存與重建自身作品》
- GCMS《無損保存與近無損語義重建：GCMS 的雙軌記憶架構》
- GCMS《多路徑知識索引》
- GCMS《自調用記憶》
- GCMS《記憶污染與三區治理》
- GCMS《從個人記憶到多智能體認知繼承》
- GCMS《終局猜想：遞歸生成式認知基礎設施》
- RDSS operational memory / archival history
- MWT-04 world-state lineage
- MWT-09 resource accounting

MWT-10 不取代 GCMS；它把 GCMS 中成熟的 memory architecture 提升成 MWT 長期數學世界的一個正式內部層。

---

# 附錄 E：MWT v0.1 第一輪封頂聲明

MWT-01～10 現階段構成一個**描述性—形式化—工程接口混合的研究架構**。

它已具備：

- 核心 primitive 與 presentation separation；
- legality；
- scheduler；
- world-state；
- refinement；
- coupling；
- query；
- quantifier coverage；
- resource accounting；
- memory persistence。

但它尚未具備：

- 統一 machine-checkable formal semantics；
- 一個完整 proof of consistency；
- 對所有 backend 的 soundness theorem；
- 大規模 benchmark；
- production runtime；
- 對既有數學 foundations 的替代資格。

因此第一輪真正的完成，不是宣稱「理論已終極完成」，而是：

$$
\boxed{
\text{核心責任已足夠完整，現在該停止擴篇，開始統合、實作與反證。}
}
$$
