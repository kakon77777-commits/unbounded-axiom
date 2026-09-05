# GIRA-A03｜資訊海不是世界模型：去重、版本、時態、語義與 X 次結構化
## The Information Ocean Is Not a World Model: Deduplication, Versioning, Temporality, Semantics, and X-Order Structuring

**系列：** Global Intelligence: Existence, Recognition, and Operational Reach（GIRA）  
**系列中文名：** 全域智能：存在、識別與操作域系列  
**篇次：** Paper 03 / 09  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-04  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Global AI 資訊架構／動態世界狀態／語義演化／知識工程

---

## 摘要

GIRA-A01 已區分 ASI 與 Global AI，指出超級智能能力不自動等於全域操作架構；GIRA-A02 則進一步提出 Global Cognitive Atlas，主張全域認知不應被理解為單一巨大表示，而應維持多觀察者、多方法、多表示的有效域、轉換、邊界與 coherence。本文處理第三個基礎問題：即使一個 AI 已能存取極大規模的全球網路、資料庫、新聞、論文、企業資訊、感測資料與歷史檔案，它仍然不因此擁有世界模型。

本文提出：

$$
\boxed{
\text{Information Ocean}
\neq
\text{World Model}.
}
$$

全球資訊具有高度重複、轉述、版本分歧、時間錯位、語義異名、來源衝突、推論混入事實、過期狀態與不同觀察尺度。若 AI 只是持續收集與召回，它得到的可能是更大的資訊海，而不是更高品質的世界認知。真正的 Global AI 必須把原始資訊經過多次、不同目的的結構轉換，使之成為可追蹤、可更新、可比較、可查詢、可驗證且可用於決策的世界狀態。

本文將原始資訊量記為：

$$
D_{\mathrm{raw}}(t),
$$

而將有效世界資訊記為：

$$
D_{\mathrm{eff}}(t).
$$

一般而言：

$$
\boxed{
D_{\mathrm{eff}}(t)
\ll
D_{\mathrm{raw}}(t).
}
$$

這個差距並不表示大部分資料「沒有價值」，而是表示大部分資料不能直接作為世界狀態使用。它們必須先經過 identity resolution、deduplication、source binding、temporal normalization、claim separation、provenance、semantic alignment、conflict preservation、versioning 與 state extraction。

本文將這個過程概念化為 **X-Order Structuring**：

$$
S^{(0)}
\rightarrow
S^{(1)}
\rightarrow
S^{(2)}
\rightarrow
\cdots
\rightarrow
S^{(x)},
$$

其中 $x$ 不是固定常數，而是依任務、領域、時間尺度與所需精度動態決定。最簡化地：

$$
S^{(0)}
=
\text{raw signals},
$$

$$
S^{(1)}
=
\text{canonicalized entities and sources},
$$

$$
S^{(2)}
=
\text{claims, events, relations, and versions},
$$

$$
S^{(3)}
=
\text{temporal state and dependency structure},
$$

$$
S^{(4)}
=
\text{causal, strategic, and systemic abstractions},
$$

$$
S^{(5)}
=
\text{query-conditioned active world projection}.
$$

本文強調，真正的高階結構化不是「壓縮越多越好」。每一層都可能丟失資訊，因此必須保留 canonical source、provenance、representation identity 與 rebuildability。這與既有 Multi-Representation Memory Fabric 的原則一致：

$$
\boxed{
R_i(m)
\neq
m.
}
$$

任何向量、圖、矩陣、摘要、狀態表、embedding 或 active context，都只是受治理記憶的 representation，而不是 memory identity 或 epistemic authority 本身。

本文亦承接 SEDB 的事件溯源與主張帳本模型，採用：

$$
\boxed{
\mathcal K_t
=
(
V_t,
E_t,
C_t,
P_t,
T_t,
\Lambda_t,
\Delta_t
)
}
$$

作為動態知識狀態的參考骨架，並將狀態更新寫為：

$$
\boxed{
\mathcal K_{t+1}
=
\mathcal U(
\mathcal K_t,
\Delta_t
).
}
$$

Global AI 因而不應在每次新資料出現時重新「理解整個 Internet」，而應持續估計：

$$
\boxed{
\Delta W_t
=
W_{t+1}
-
W_t,
}
$$

即世界究竟改變了什麼。

本文最後提出 **Global State Refinement Pipeline**：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Preserve}
\rightarrow
\text{Resolve}
\rightarrow
\text{Deduplicate}
\rightarrow
\text{Temporalize}
\rightarrow
\text{Semanticize}
\rightarrow
\text{Relate}
\rightarrow
\text{Abstract}
\rightarrow
\text{Project}
\rightarrow
\text{Verify}.
}
$$

其中 Preserve 必須先於高階壓縮，以確保任何 derived world state 都可以追溯、重算與撤回。真正的 Global AI 不應擁有一個「永遠正確的真理資料庫」，而應維持一套可以知道何者是觀察、推論、假說、衝突、撤回、過期、未知與可驗證狀態的動態資訊基礎設施。

**關鍵詞：** Global AI、資訊海、世界模型、X 次結構化、去重、版本控制、時態資料、SEDB、語義演化、事件溯源、主張帳本、Provenance、Dynamic World State、Delta State、Multi-Representation Memory

---

# 1. 問題：如果 AI 能讀完整個網路，它就理解世界了嗎？

令網路與外部資料形成原始資訊域：

$$
\mathcal I_{\mathrm{raw}}.
$$

AI 可以具有非常大的可達範圍：

$$
A_{\mathrm{data}}
\approx
\mathcal I_{\mathrm{raw}}.
$$

這仍然不能推出：

$$
\boxed{
A_{\mathrm{data}}
=
W_t.
}
$$

其中 $W_t$ 表示時間 $t$ 的有效世界狀態。網路保存的是大量表述，不是天然正規化的世界狀態。

---

# 2. 一個世界事件可以生成大量資訊物件

假設世界中發生事件：

$$
e.
$$

它可能生成官方公告、新聞、公司聲明、社群貼文、分析文章、二次轉述、多語言翻譯、影片與後續更正。因此一個事件可以對應：

$$
\{d_1,d_2,\ldots,d_n\}.
$$

若 AI 把每個 $d_i$ 都當作獨立世界事實，則：

$$
\boxed{
\text{representation multiplicity}
\rightarrow
\text{false world multiplicity}.
}
$$

---

# 3. Entity Resolution

不同來源可能使用全名、縮寫、舊名、品牌名、子公司名、翻譯名或拼寫差異表示同一實體。因此：

$$
n_{\mathrm{surface}}
>
n_{\mathrm{entity}}.
$$

Global AI 需要 canonical entity identity：

$$
E^\ast.
$$

並將：

$$
e_1,e_2,\ldots,e_k
$$

映射到：

$$
E^\ast.
$$

這個映射不能只靠字串相似度，還需要 time、jurisdiction、ownership、identifier、address、legal status 與 provenance。

所以：

$$
\boxed{
\text{Name Similarity}
\neq
\text{Entity Identity}.
}
$$

---

# 4. 去重不是刪除重複文字

Global AI 所需的去重至少包括：

- exact duplicate；
- semantic duplicate；
- event duplicate；
- derivative duplicate；
- version duplicate；
- partial duplicate。

因此：

$$
\boxed{
\text{Deduplication}
\neq
\text{Deletion}.
}
$$

更合理的是建立 equivalence、derivation 與 version relation。

---

# 5. 去重後仍應保留來源差異

假設：

$$
d_1
\sim
d_2
$$

表示兩份資料指向同一事件。這不代表：

$$
d_1=d_2.
$$

因為兩者可能有不同時間、作者、證據、wording、authority 與 correction history。

因此 canonical state 應保留：

$$
E^\ast
+
\{d_i\}
+
\{P_i\},
$$

而不是把所有來源抹平成一份摘要。

---

# 6. Claim 不等於 Fact

SEDB 已提出：

$$
\boxed{
\text{Claim}
\neq
\text{Fact}.
}
$$

對來源 $s$ 提出的命題 $c$，應表示為：

$$
C
=
(
s,
p,
o,
\text{scope},
\text{status},
\text{time},
\text{provenance}
).
$$

而不是直接寫入 WorldFact。

---

# 7. 認識論狀態必須是一等資料

Global AI 至少應區分：

$$
\boxed{
\mathrm{OBS}
\neq
\mathrm{INF}
\neq
\mathrm{HYP}
\neq
\mathrm{CON}
\neq
\mathrm{RET}
\neq
\mathrm{UNK}.
}
$$

若沒有這層，AI 很容易形成：

$$
\text{Inference}_t
\rightarrow
\text{Fact}_{t+1},
$$

經過多輪後造成自我污染。

---

# 8. 時間不是單一 timestamp

至少應區分：

$$
t_{\mathrm{valid}},
\quad
t_{\mathrm{record}},
\quad
t_{\mathrm{publish}},
\quad
t_{\mathrm{mention}},
\quad
t_{\mathrm{inference}}.
$$

因此：

$$
\boxed{
\text{Timestamp}
\neq
\text{Temporal Semantics}.
}
$$

---

# 9. 多時間系統為什麼重要？

假設政策 $P$ 在 $t_1$ 生效，但新聞在 $t_0<t_1$ 提前報導。如果 AI 只保留 publish time，它可能在歷史重建時把政策提前生效。

因此：

$$
\boxed{
\text{publication history}
\neq
\text{world-state history}.
}
$$

---

# 10. 版本不等於覆寫

傳統 CRUD 很容易：

$$
v_1
\rightarrow
v_2
$$

後只保留 $v_2$。但 Global AI 需要知道 $v_1$ 曾經存在、何時被取代、哪些結論基於 $v_1$ 、 $v_2$ 改了什麼，以及是否需要重算 downstream state。

所以：

$$
\boxed{
\text{Update}
\neq
\text{Overwrite}.
}
$$

更適合：

$$
v_1
\xrightarrow{\Delta_1}
v_2
\xrightarrow{\Delta_2}
v_3.
$$

---

# 11. Event Sourcing 的世界歷史啟發

若每次狀態改變都保存事件：

$$
\Delta_t,
$$

則：

$$
W_{t+1}
=
\mathcal U(
W_t,
\Delta_t
).
$$

本文不要求特定 Event Sourcing 實作，只要求：

$$
\boxed{
\text{State change should remain reconstructable}.
}
$$

---

# 12. 網路資訊具有高度派生性

假設原始資料：

$$
d_0
$$

被 $d_1$ 引用，再被 $d_2$ 轉述，再被 $d_3$ 摘要。

如果 AI 只看到：

$$
d_1,d_2,d_3,
$$

可能誤以為有三個獨立來源。

因此需要 derivation graph：

$$
d_0
\rightarrow
d_1
\rightarrow
d_2
\rightarrow
d_3.
$$

---

# 13. Provenance 不是附加 metadata

W3C PROV 將 provenance 表示為 Entity、Activity、Agent 與 derivation 等關係。對 Global AI 而言，provenance 應視為：

$$
\boxed{
\text{epistemic structure}.
}
$$

因為兩個內容相同的 claim，如果來源鏈不同，其可信度與獨立性可能完全不同。

---

# 14. 多來源不等於多證據

假設：

$$
s_2
\leftarrow
s_1,
$$

$$
s_3
\leftarrow
s_1.
$$

那麼：

$$
N_{\mathrm{sources}}=3
$$

卻可能只有：

$$
N_{\mathrm{independent\ evidence}}=1.
$$

因此：

$$
\boxed{
\text{Source Count}
\neq
\text{Evidence Independence}.
}
$$

---

# 15. 歷史網路需要時間旅行

若今天 $t_2$ 查詢過去 $t_1$，Global AI 不應只用今天頁面的最新版本回答。它應區分：

$$
\text{What is known now about }t_1
$$

與：

$$
\text{What was knowable at }t_1.
$$

HTTP Memento 以 datetime negotiation、Memento 與 TimeMap 等機制提供 Web 資源時間版本存取的標準化思路。

因此：

$$
\boxed{
\text{Historical Reconstruction}
\neq
\text{Present-Day Retelling}.
}
$$

---

# 16. 文明動態記憶的核心是 State Difference

既有「網路資訊海作為文明動態記憶」提出：

$$
N_d(t)
=
\operatorname{Top3}(
\Delta K_d(t)
).
$$

其中最重要的不是 Top3，而是：

$$
\boxed{
\Delta K.
}
$$

世界持續變化時，真正稀缺的認知資源不是再讀一次全部資料，而是知道什麼變了。

---

# 17. 世界狀態與世界差分

令世界狀態：

$$
W_t.
$$

Global AI 的更新更接近：

$$
\boxed{
W_{t+1}
=
\Psi(
W_t,
D_{t+1},
\Delta D_t,
P_t
).
}
$$

並顯式保存：

$$
\Delta W_t
=
W_{t+1}
-
W_t.
$$

---

# 18. Delta-First 世界模型

本文提出：

$$
\boxed{
\text{Delta-First World Maintenance}.
}
$$

系統平常優先計算：

$$
\Delta W_t
$$

而不是反覆全量重建 $W_t$。只有在 schema 變更、ontology 失效、大規模資料污染、新方法出現或 consistency check 失敗時，才做較大範圍 rebuild。

---

# 19. 什麼叫 X 次結構化？

正式定義：

$$
S^{(0)}
=
\mathcal I_{\mathrm{raw}}.
$$

第 $k$ 層結構化為：

$$
\boxed{
S^{(k+1)}
=
\Phi_k(
S^{(k)},
Q_t,
M_t,
B_t
).
}
$$

其中 $Q_t$ 是當前問題， $M_t$ 是方法集合， $B_t$ 是資源預算。

因此：

$$
x
=
x(
Q_t,
\Omega,
\epsilon,
B_t
).
$$

---

# 20. 第一層：Canonicalization

$$
S^{(0)}
\rightarrow
S^{(1)}.
$$

處理 source identity、document identity、entity identity、format normalization、language mapping、exact duplicate 與 version linkage。

目標是：

$$
\boxed{
\text{知道哪些東西其實是同一個東西。}
}
$$

---

# 21. 第二層：Claim and Event Structuring

$$
S^{(1)}
\rightarrow
S^{(2)}.
$$

將文件拆成 event、claim、observation、actor、relation、evidence、version 與 scope。

此時 Document 不再是核心最小單位。

---

# 22. 第三層：Temporal and Relational State

$$
S^{(2)}
\rightarrow
S^{(3)}.
$$

建立：

$$
G_t
=
(V_t,E_t)
$$

與多時間系統 $T_t$。

系統開始能回答：誰和誰有關、何時開始、何時失效、哪條關係是推論、哪條關係有直接來源。

---

# 23. 第四層：Dependency and System Structure

$$
S^{(3)}
\rightarrow
S^{(4)}.
$$

這一層處理 dependency、bottleneck、substitution、flow、hierarchy、cluster、feedback 與 propagation。

它是從 knowledge graph 走向 system model 的關鍵。

---

# 24. 第五層：Causal and Strategic Abstraction

$$
S^{(4)}
\rightarrow
S^{(5)}.
$$

在有足夠證據與方法時，建立 causal hypothesis、intervention model、game structure、strategic option、risk propagation 與 counterfactual dependency。

但這些必須保留：

$$
\mathrm{INF}
$$

或：

$$
\mathrm{HYP}
$$

狀態。

---

# 25. 第六層：Query-Conditioned Active Projection

對查詢：

$$
q_t
$$

生成：

$$
\boxed{
P_t(q)
=
\operatorname{Project}(
S^{(\leq x)},
q_t,
B_t
).
}
$$

這是 working context。

因此：

$$
\boxed{
\text{World State}
\neq
\text{Working Context}.
}
$$

---

# 26. X 次結構化不是單向 ETL

實際系統會回流。

例如 $S^{(5)}$ 發現因果模型矛盾，可能回到 $S^{(2)}$ 重新檢查 claim identity。

所以：

$$
\boxed{
S^{(k)}
\leftrightarrow
S^{(j)}.
}
$$

X 次結構化更接近多層可逆 refinement graph。

---

# 27. 結構化越高，資訊損失風險越高

假設：

$$
R_k:
S^{(0)}
\to
S^{(k)}.
$$

通常：

$$
\operatorname{Info}(S^{(k)})
<
\operatorname{Info}(S^{(0)}),
$$

但：

$$
\operatorname{Actionability}(S^{(k)})
>
\operatorname{Actionability}(S^{(0)})
$$

可能成立。

因此真正的工程張力是：

$$
\boxed{
\text{Compression}
\leftrightarrow
\text{Reconstructibility}.
}
$$

---

# 28. Canonical Source 與 Derived Representation 必須分離

Multi-Representation Memory Fabric 提出：

$$
\boxed{
R_i(m)
\neq
m.
}
$$

對 canonical object $m$，可以產生 vector、graph、matrix、summary 與 state representation。

任何 derived representation 都不能單獨取得：

$$
\boxed{
\text{epistemic authority}.
}
$$

---

# 29. 摘要資料庫的風險

若：

$$
s
=
\operatorname{Summarize}(d),
$$

然後刪除 $d$，則：

$$
\boxed{
\text{summary error}
\rightarrow
\text{irreversible memory corruption}.
}
$$

更安全的是保留：

$$
s
\xrightarrow{\operatorname{source}}
d.
$$

---

# 30. Embedding 全部內容也不夠

向量表示擅長 semantic retrieval，但通常不原生表示 valid time、version lineage、provenance、epistemic status、exact identity、contradiction type 與 authority。

因此：

$$
\boxed{
\text{Vector Search}
\neq
\text{World-State Maintenance}.
}
$$

---

# 31. 圖資料庫也不是世界模型本身

圖：

$$
G=(V,E)
$$

非常適合表示關係。

但若邊沒有 time、scope、claim identity、source、status 與 version，則：

$$
A\xrightarrow{\operatorname{supports}}B
$$

仍然過度粗糙。

所以：

$$
\boxed{
\text{Graph}
\neq
\text{Epistemically Governed Graph}.
}
$$

---

# 32. 不同資料表示不需要互相取代

本文採取：

$$
\boxed{
\text{One governed state}
+
\text{many representations}.
}
$$

不同 representation 可服務 exact retrieval、fuzzy discovery、graph traversal、matrix computation、temporal comparison、symbolic reasoning 與 human audit。

---

# 33. 資料新不等於世界新

網路每天有大量：

$$
\Delta D_t.
$$

但其中可能大部分只是 repost、commentary、translation、repackaging 與 repeated statistics。

因此：

$$
\boxed{
\Delta D_t
\neq
\Delta W_t.
}
$$

---

# 34. World Novelty

對新資料 $d$，定義概念量：

$$
\boxed{
N_W(d)
=
\operatorname{Distance}
(
W_t,
W_t\oplus d
).
}
$$

如果加入 $d$ 後 $W_t$ 幾乎不變，則：

$$
N_W(d)\approx0.
$$

這表示內容新，但世界狀態不新。

---

# 35. State-Changing Information

定義：

$$
\boxed{
\mathcal I_{\Delta W}
=
\{d:
\Delta W(d)
\neq0
\}.
}
$$

Global AI 的 attention 應優先處理 $\mathcal I_{\Delta W}$，而不是只追求 latest。

因此：

$$
\boxed{
\text{latest}
\neq
\text{important}.
}
$$

---

# 36. 過期資訊污染

若 claim $c_t$ 在時間 $t$ 正確，後來被 $c_{t+1}$ 取代，而 retrieval 仍以語義相似度召回 $c_t$，就可能造成 stale truth contamination。

因此每個 claim 需要 validity state。

---

# 37. Stale 不等於 False

歷史 claim：

$$
c_t
$$

在今天可能不是 current，但仍可能是描述當時世界的正確歷史資料。

所以：

$$
\boxed{
\text{stale}
\neq
\text{false}.
}
$$

---

# 38. 同一事件存在不同觀察尺度

事件 $e$ 可以在 micro、meso、macro 尺度被描述。

因此：

$$
\boxed{
\text{same raw event}
\rightarrow
\text{multiple scale states}.
}
$$

這也是 X 次結構化的另一個維度。

---

# 39. 高階趨勢不能直接寫回底層事實

若 AI 從大量 micro events 推導：

$$
H_{\mathrm{macro}},
$$

應標記為 $\mathrm{INF}$ 或 $\mathrm{HYP}$，不能再把它當作獨立觀察支持自己，否則形成：

$$
\boxed{
\text{epistemic feedback loop}.
}
$$

---

# 40. 自我引用污染

若 AI 推論 $I_t$ 被公開後，又被下一輪系統抓回並誤認為獨立來源：

$$
I_t
\rightarrow
I_t^{\mathrm{web}}
\rightarrow
I_{t+1},
$$

就會形成虛假增強。

因此 Global AI 必須標記：

$$
\boxed{
\text{derivation lineage}.
}
$$

---

# 41. Dynamic Database 與 Static Corpus 的差別

Static Corpus 假設資料相對固定。

Dynamic World Database 則要求：

$$
D_t
\neq
D_{t+1}.
$$

更重要的是 schema 甚至也可能變：

$$
Schema_t
\neq
Schema_{t+1}.
$$

概念會 split、merge、rename、deprecate、revive、generalize 與 specialize。

---

# 42. 世界本體也可能演化

令 ontology：

$$
\mathcal O_t.
$$

Global AI 不應假設：

$$
\mathcal O_t
=
\mathcal O_0
\quad
\forall t.
$$

新科技、新制度與新概念可能造成：

$$
\mathcal O_{t+1}
=
\Gamma(
\mathcal O_t,
\Delta W_t
).
$$

---

# 43. Schema Migration 本身是認知事件

若概念 $C$ 分裂成 $C_1,C_2$，舊資料不能只留在舊分類中，而需要重分類並保留歷史分類狀態。

因此：

$$
\boxed{
\text{schema evolution}
\subset
\text{world-model history}.
}
$$

---

# 44. 世界模型不是最新真相表

更合理的世界模型包含：

$$
\boxed{
\text{current state}
+
\text{history}
+
\text{provenance}
+
\text{uncertainty}
+
\text{conflict}
+
\text{unknown}.
}
$$

可寫成：

$$
W_t
=
(
S_t,
H_t,
P_t,
U_t,
C_t,
N_t
).
$$

---

# 45. Conflict Preservation

若兩個高品質來源衝突，Global AI 不應立即 SelectOne。

它可以保留：

$$
\boxed{
C_t
=
\{c_1,c_2\}
}
$$

直到取得足夠 evidence。

Conflict 也是 world state，不只是 database error。

---

# 46. Unknown Preservation

同樣：

$$
\mathrm{UNK}
$$

是一種：

$$
\boxed{
\text{explicit epistemic state}.
}
$$

若系統不能保存 unknown，就容易用 plausible generation 把 unknown 填滿。

---

# 47. Global State Refinement Pipeline

本文提出：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Preserve}
\rightarrow
\text{Resolve}
\rightarrow
\text{Deduplicate}
\rightarrow
\text{Temporalize}
\rightarrow
\text{Semanticize}
\rightarrow
\text{Relate}
\rightarrow
\text{Abstract}
\rightarrow
\text{Project}
\rightarrow
\text{Verify}.
}
$$

---

# 48. Preserve 為什麼必須靠前？

任何後續步驟都可能錯。

若結構化錯誤，但原始 $d$ 仍存在，可以 rebuild。若原始資料被不可逆壓縮掉，就無法復原。

因此：

$$
\boxed{
\text{Preserve before irreversible abstraction}.
}
$$

---

# 49. Resolve

Resolve 處理 identity、source、duplicate、version、language、format 與 entity binding。

這是資料從 documents 進入 world objects 前的第一道門。

---

# 50. Temporalize

Temporalize 不只是加日期，而是建立：

$$
\boxed{
\text{what was true when}
}
$$

以及：

$$
\boxed{
\text{what was known when}.
}
$$

---

# 51. Semanticize

Semanticize 將資料轉成 claim、event、relation、concept、state、observation 與 hypothesis，但每個轉換都保留 SourceBinding。

---

# 52. Relate

Relate 建立：

$$
G_t,
$$

包含 support、contradiction、dependency、derivation、ownership、flow、sequence 與 causality candidate。

---

# 53. Abstract

Abstract 產生 trend、bottleneck、regime、cluster、system risk 與 strategic variable。

所有高階 abstraction 都應明示 derived status。

---

# 54. Project

Project 依當前問題 $q_t$ 生成 active context：

$$
C_t(q).
$$

因此：

$$
\boxed{
\text{Canonical World State}
\neq
\text{Active Context}.
}
$$

---

# 55. Verify

Verify 可以包括 source check、contradiction search、temporal consistency、schema validation、formal proof、simulation、independent Agent review 與 human review。

驗證後才允許 state promotion。

---

# 56. State Promotion

令新 claim $c$ 初始為：

$$
\mathrm{INF}.
$$

驗證後可能：

$$
\mathrm{INF}
\rightarrow
\mathrm{OBS},
$$

或：

$$
\mathrm{INF}
\rightarrow
\mathrm{CON},
$$

甚至：

$$
\mathrm{INF}
\rightarrow
\mathrm{RET}.
$$

因此世界資料庫是：

$$
\boxed{
\text{epistemic state machine}.
}
$$

---

# 57. 壓縮率不是越高越好

定義：

$$
\rho_k
=
\frac{
|S^{(k)}|
}{
|S^{(0)}|
}.
$$

真正關心的是：

$$
\boxed{
\eta_k
=
\frac{
\text{decision-relevant structure retained}
}{
\text{storage or context cost}
}.
}
$$

不是單純追求：

$$
\rho_k\to0.
$$

---

# 58. 錯誤壓縮可能比不壓縮更危險

若壓縮遺失一個低頻但高影響信號：

$$
x^\ast,
$$

可能有：

$$
\operatorname{Importance}(x^\ast)
\gg
\operatorname{Frequency}(x^\ast).
$$

因此 frequency-based compression 不適合作為唯一策略。

---

# 59. Importance-Preserving Compression

本文提出概念量：

$$
\boxed{
\operatorname{IPC}(C)
=
P(
\text{critical structure survives compression}
).
}
$$

壓縮器不只要保持平均語義，還要保持 chokepoint、anomaly、rare risk、irreversible event 與 strategic dependency。

---

# 60. 資料品質不是單一分數

一個資料物件可以有：

$$
Q(d)
=
(
q_{\mathrm{source}},
q_{\mathrm{time}},
q_{\mathrm{identity}},
q_{\mathrm{independence}},
q_{\mathrm{precision}},
q_{\mathrm{scope}},
q_{\mathrm{freshness}}
).
$$

因此：

$$
\boxed{
\text{High Quality}
\neq
\text{High Relevance}.
}
$$

---

# 61. 新穎性與品質必須分離

定義資料品質 $Q(d)$ 、世界新穎度 $N_W(d)$ 與當前查詢相關度 $R_q(d)$。

則：

$$
\boxed{
\operatorname{Value}(d)
=
F(
Q(d),
N_W(d),
R_q(d)
).
}
$$

---

# 62. Canonicality

Canonical 不表示唯一真理，而表示系統目前正式承認、可追溯、可版本化的受治理狀態入口。

因此：

$$
\boxed{
\text{Canonical}
\neq
\text{infallible}.
}
$$

canonical state 可以 revise、retract、supersede、branch 與 merge。

---

# 63. 世界狀態也可能分支

若兩個高可信模型無法調和：

$$
W_t^{(a)}
$$

與：

$$
W_t^{(b)},
$$

系統可暫時維持：

$$
\boxed{
\{W_t^{(a)},W_t^{(b)}\}.
}
$$

而不是強迫統一。

---

# 64. Branch 不等於失敗

如果世界證據本身未決，分支可能比單一答案更正確。

Global AI 的成熟度可以部分由：

$$
\boxed{
\text{ability to preserve unresolved branches}
}
$$

衡量。

---

# 65. Dynamic World State 需要 Wake Conditions

若某狀態 $s$ 目前穩定，系統不需要一直高成本重算。

可以設定：

$$
\operatorname{Wake}(s)
=
\begin{cases}
1,&\text{if triggering delta appears}\\
0,&\text{otherwise}.
\end{cases}
$$

因此：

$$
\boxed{
\text{Persistent World State}
\neq
\text{Continuous Full Inference}.
}
$$

---

# 66. Hot / Warm / Cold State

概念上：

$$
\mathcal W
=
W_{\mathrm{hot}}
\cup
W_{\mathrm{warm}}
\cup
W_{\mathrm{cold}}.
$$

Hot 對應高變動、高決策相關狀態；Warm 對應中等變化依賴；Cold 對應歷史與低變動狀態。

這不只是 storage optimization，也是 attention architecture。

---

# 67. 世界狀態與注意力耦合

若：

$$
\Delta W_t(v)
$$

很大，則：

$$
a_{t+1}(v)
\uparrow.
$$

若：

$$
\Delta W_t(v)\approx0
$$

且無高風險依賴，則：

$$
a_{t+1}(v)
\downarrow.
$$

這自然接到 GIRA-A04。

---

# 68. Information-to-State Conversion Efficiency

定義：

$$
\boxed{
\eta_{IS}
=
\frac{
\text{verified state-changing information}
}{
\text{raw information processed}
}.
}
$$

若：

$$
\eta_{IS}\ll1,
$$

表示系統花大量算力處理重複與低狀態價值資訊。

Global AI 的競爭力可能很大部分來自：

$$
\eta_{IS}\uparrow.
$$

---

# 69. State Reconstruction Cost

令：

$$
C_R(W_t)
$$

表示從保存的 source、events、versions 與 representations 重建 $W_t$ 的成本。

系統需要在高壓縮與低重建成本之間取得平衡。

---

# 70. Epistemic Debt

若系統持續產生 derived state，卻不保留 source、lineage、version、status 與 uncertainty，則形成：

$$
\boxed{
D_E
=
\text{Epistemic Debt}.
}
$$

隨時間累積後，世界模型可能變得不可審計。

---

# 71. 全域資料優勢不只是資料更多

真正的優勢可能是：

$$
\boxed{
\text{better state conversion}.
}
$$

包括更少重複、更準 entity identity、更完整 temporal state、更強 provenance、更低 stale contamination、更好 unknown preservation 與更有效 active projection。

因此：

$$
\boxed{
\text{Global Data Advantage}
\neq
\text{Data Volume Advantage}.
}
$$

---

# 72. 對 ASI 的限制

即使：

$$
I_{\mathrm{ASI}}
\gg
I_{\mathrm{human}},
$$

若它被餵入：

$$
D_{\mathrm{raw}}
$$

而缺乏 structuring、temporality、provenance 與 verification，仍可能受到 information architecture bottleneck。

因此：

$$
\boxed{
\text{ASI}
+
\text{Internet}
\not\Rightarrow
\text{Global World Model}.
}
$$

---

# 73. ASI 可以自行發明這些方法嗎？

可能。

如果 ASI 具有 meta-cognition、architecture invention、autonomous experimentation 與 persistent tooling，它可能自行建立：

$$
\Phi_1,\Phi_2,\ldots,\Phi_x.
$$

但這仍然證明需要這些轉換，而不是證明它們不需要存在。

因此：

$$
\boxed{
\text{method discoverability}
\neq
\text{method dispensability}.
}
$$

---

# 74. Global AI 資訊層的七條不變量

$$
\boxed{
\text{Source}
\neq
\text{Claim}
}
$$

$$
\boxed{
\text{Claim}
\neq
\text{Fact}
}
$$

$$
\boxed{
\text{Current}
\neq
\text{Historical}
}
$$

$$
\boxed{
\text{State}
\neq
\text{Projection}
}
$$

$$
\boxed{
\text{New Content}
\neq
\text{New World State}
}
$$

$$
\boxed{
\text{Representation}
\neq
\text{Authority}
}
$$

$$
\boxed{
\text{Compression}
\neq
\text{Deletion}.
}
$$

---

# 75. Global Information Architecture

綜合本文：

$$
\boxed{
\mathfrak I_G
=
(
\mathcal S,
\mathcal E,
\mathcal C,
\mathcal P,
\mathcal T,
\mathcal V,
\mathcal R,
\mathcal W,
\Delta
).
}
$$

其中：

- $\mathcal S$：sources；
- $\mathcal E$：entities／events；
- $\mathcal C$：claims；
- $\mathcal P$：provenance；
- $\mathcal T$：temporal semantics；
- $\mathcal V$：versions；
- $\mathcal R$：representations；
- $\mathcal W$：world states；
- $\Delta$：state-change events。

---

# 76. 與 Global Cognitive Atlas 的關係

A02 的：

$$
\mathfrak A_G
$$

處理不同 observer、method、representation 如何形成全域認知。

A03 的：

$$
\mathfrak I_G
$$

處理原始資訊如何被轉成可供這些認知 charts 使用的受治理狀態。

因此兩者形成：

$$
\boxed{
\mathfrak I_G
\leftrightarrow
\mathfrak A_G.
}
$$

---

# 77. 可觀測預測

本文提出六個預測：

1. 高階 Agent 的競爭差異會越來越多來自 state architecture，而不只是 model benchmark。
2. 大型企業 AI 將逐步從 RAG 文件庫走向 claim、event、provenance、temporal state 型架構。
3. AI memory 將由單一 vector store 走向 multi-representation governed fabric。
4. 世界監控型 AI 的核心輸出將從 summary 轉向 $\Delta W_t$。
5. 重要資訊排序將越來越重視 state-changing novelty，而不是 publication recency。
6. 高自治 Agent 若缺乏 provenance 與 epistemic status，會累積自我引用污染與 stale truth。

---

# 78. 與既有 EveMissLab 研究的關係

## 78.1 網路資訊海作為文明動態記憶

既有研究提出：

$$
\text{Daily Delta}
\rightarrow
\text{Temporal Record}
\rightarrow
\text{Domain History}
\rightarrow
\text{Dynamic Memory}.
$$

本文將它提升為 Global AI 的世界狀態維護層。

## 78.2 SEDB

SEDB 已提出：

$$
\mathcal K_t
=
(
V_t,
E_t,
C_t,
P_t,
T_t,
\Lambda_t,
\Delta_t
).
$$

本文採用其 claim-first、event sourcing、provenance、multi-time、epistemic status 與 semantic evolution 作為 X 次結構化的重要工程候選。

## 78.3 Multi-Representation Memory Fabric

MRMF 已提出：

$$
R_i(m)\neq m.
$$

以及 One Governed Memory State + Many Replaceable Representations。

本文將其擴張到 Global AI：世界狀態可以有多表示，但任何表示不能自行取得 world authority。

## 78.4 GIRA-A02

A02 提出 Global AI 需要 atlas of world models。

本文補上：atlas 所依賴的資料本身必須先經受治理的動態結構化。

---

# 79. 外部標準支點

W3C PROV 提供 Entity、Activity、Agent 與 derivation 等 provenance 表示框架，說明 provenance 可以成為可互操作的一等資料結構，而不只是純文字註記。

RFC 7089 HTTP Memento 提供 Web 資源 datetime negotiation、Memento 與 TimeMap 機制，說明時間版本與某個時間點的資源狀態存取可以被正式協議化。

本文不主張直接以 PROV-O 或 Memento 實作全部 Global AI world state；它們只是提供成熟的外部支點。

---

# 80. 結論

本文的核心命題是：

$$
\boxed{
\text{Information Ocean}
\neq
\text{World Model}.
}
$$

以及：

$$
\boxed{
\text{More Information}
\not\Rightarrow
\text{More Effective Global Cognition}.
}
$$

真正的 Global AI 需要把：

$$
D_{\mathrm{raw}}
$$

經過：

$$
S^{(0)}
\rightarrow
S^{(1)}
\rightarrow
\cdots
\rightarrow
S^{(x)}
$$

轉換成：

$$
W_t.
$$

而世界狀態又必須持續更新：

$$
W_t
\xrightarrow{\Delta W_t}
W_{t+1}.
$$

因此未來真正稀缺的能力可能不是誰能收集最多資料，而是：

> **誰能以最低認知與計算成本，把最大規模的異質資訊轉換成最可靠、可追溯、可重建、可更新的世界狀態。**

可以概括為：

$$
\boxed{
\text{Global Intelligence}
\text{ requires information-to-state conversion intelligence.}
}
$$

最後提出 Global AI 的資料原則：

$$
\boxed{
\text{Preserve the source, govern the state, derive the representation, and update by delta.}
}
$$

只有當 AI 能持續知道哪些資料是同一件事、哪些只是轉述、哪些已過期、哪些是觀察、哪些是推論、哪些仍有爭議、哪些真的改變了世界狀態，以及哪些高階表示可以被重建，它才真正從「讀取資訊海」走向「維持世界模型」。

下一篇 GIRA-A04 將研究：

$$
\boxed{
\text{當世界模型已經建立，AI 如何知道現在真正重要的是哪裡？}
}
$$

也就是動態關鍵節點、瓶頸、注意力與全域認知資源配置。

---

# 參考文獻與前置研究

## EveMissLab / Neo.K 既有研究

1. Neo.K with Aletheia, **GIRA-A01｜ASI 不等於 Global AI：智能能力類別與全域操作架構類別的分離**, 2026.
2. Neo.K with Aletheia, **GIRA-A02｜局部全域與真正全域認知：觀察者、方法論座標與認知域**, 2026.
3. Neo.K, **網路資訊海作為文明動態記憶：總論與未來命題**, EML-IIODO-TH-10, 2026.
4. Neo.K, **AI 原生語義演化資料庫：從事件溯源、主張帳本到動態語義圖查詢語言的系統架構**, SEDB / SEQL Technical Whitepaper v1.0, 2026.
5. Neo.K, **多表示記憶 Fabric：向量、符號、矩陣、圖、原文與狀態庫的共存**, AI 自主上下文記憶與認知編譯系列 Paper 05, 2026.
6. Neo.K with Aletheia, **ACWC-01｜母模型＋超算為何仍不等於 AI 原生計算世界**, 2026.

## 外部參考

7. W3C Provenance Working Group, **PROV-O: The PROV Ontology**, W3C Recommendation, 2013.
8. W3C Provenance Working Group, **PROV-DM: The PROV Data Model**, W3C Recommendation, 2013.
9. H. Van de Sompel et al., **RFC 7089 — HTTP Framework for Time-Based Access to Resource States (Memento)**, 2013.

---

# Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面的渲染版本不應被視為 canonical source。

數學公式 canonical delimiter 僅使用：

- inline math：` $...$ `
- display math：`$$...$$`

不得以 Unicode 數學字元替換 LaTeX source，不進行 `unicode_escape` 類 round-trip，不自行改寫反斜線、delimiter 或公式原始碼。
