# AI-Native Unified Search Intelligence (AUSI) Series — Paper 06

## 反證優先與缺口驅動搜尋：Counter-Evidence、Coverage Gap、Uncertainty-Directed Search 與自主研究閉環

**English Title:** *Counter-Evidence-First and Gap-Driven Search: Coverage Gaps, Uncertainty-Directed Retrieval, and the Autonomous Research Loop*

**Version:** v0.1  
**Date:** 2026-08-31  
**Status:** Canonical Draft  
**Series:** AI-Native Unified Search Intelligence (AUSI)  
**Predecessor:** Paper 05 — *從搜尋結果到證據：Provenance、Verification、Evidence Ledger 與可驗證研究資料生命週期*  
**Reference Implementation Direction:** `ai-web-research`

---

## 摘要

多輪搜尋並不必然產生真正的研究能力。若下一輪 query 只是上一輪 query 的改寫、同義詞擴展，或根據目前已有答案尋找更多相似結果，系統即使執行數百次搜尋，也可能只是在增加重複證據與確認偏誤。真正的自主研究需要另一種驅動方式：下一個搜尋行動應由「目前證據結構缺什麼」決定，而不是只由「上一個 query 是什麼」決定。

本文提出 **Gap-Driven Search（缺口驅動搜尋）** 與 **Counter-Evidence-First Scheduling（反證優先排程）**。本文延續 Paper 05 的 Claim–Evidence Graph、Evidence Ledger 與 Evidence Gap，將 Search Planner 的主要狀態更新改寫為：

$$
\Pi_{t+1}
=
f(
G_E,
G_C,
G_U,
G_D,
G_T,
G_P,
G_R,
G_{CE},
B_t
)
$$

其中 $G_E$ 為 evidence gap、 $G_C$ 為 coverage gap、 $G_U$ 為 uncertainty gap、 $G_D$ 為 diversity / independence gap、 $G_T$ 為 temporal / version gap、 $G_P$ 為 policy / provider gap、 $G_R$ 為 representation / terminology gap， $G_{CE}$ 為 Claim–Evidence Graph， $B_t$ 為剩餘搜尋 budget。AI 的下一步可以因此變成「尋找 primary source」「搜尋指定 jurisdiction」「尋找與目前結論衝突的證據」「驗證某一版本」「切換到獨立來源」「沿 citation graph 擴張」「尋找未覆蓋術語」，而不是單純產生更多 query。

本文將 counter-evidence 定義為針對目前高影響命題、具有高度單邊 evidence structure 或高不確定性的 claim，主動尋找 `CONTRADICT`、`QUALIFY`、alternative explanation、boundary condition 或 source disagreement 的搜尋策略。這與「永遠相信反對證據」不同，也不把哲學上的 falsificationism 簡化成工程規則；其目標是避免 planner 的 Search Graph 被目前最容易找到的支持證據鎖定。心理學中的 confirmation bias 研究、active learning 中的 uncertainty sampling、fact verification 中的 `SUPPORTS / REFUTES / NOT ENOUGH INFO` 區分，以及 systematic review 方法學中對多方法搜尋、citation searching、可重現搜尋與停止理由的要求，都為此提供既有研究基礎。

本文提出 Gap Vector、Gap Priority Function、Expected Gap Reduction、Counter-Evidence Trigger、Coverage Tensor、Diminishing Novelty、Branch Saturation、Negative Search Result、Search Exhaustion Profile 與 Reopening Trigger。對 open-world search，本文拒絕宣稱「搜尋完成等於世界上沒有更多結果」；停止只表示在已聲明的方法、provider、語言、時間、分類與成本邊界內，mandatory gaps 已達到 acceptance threshold，或下一步 expected gap reduction 已低於成本／風險門檻。

最後，本文建立 AUSI Autonomous Research Loop：

$$
\text{Claim}
\rightarrow
\text{Evidence}
\rightarrow
\text{Gap}
\rightarrow
\text{Search Plan}
\rightarrow
\text{New Evidence}
\rightarrow
\text{Reverification}
\rightarrow
\text{Updated Gap}
$$

此閉環是 Paper 01–06 第一次完整連接 Search Method、Planner、Source Policy、Evidence Ledger 與動態研究策略，並為 Paper 07 的 Search Receipt、經驗累積與自我改進建立最後一個理論前置層。

**關鍵詞：** Gap-Driven Search、Counter-Evidence Search、Coverage Gap、Uncertainty Sampling、Confirmation Bias、Fact Verification、Search Saturation、Active Learning、Autonomous Research、Evidence Gap、Search Planner

---

# 1. 問題：多輪搜尋不等於自主研究

假設一個 AI 已經執行：

$$
Q_1,Q_2,\ldots,Q_{100}
$$

仍不能推出：

$$
\text{Research Quality}\gg0
$$

如果：

$$
Q_{t+1}
\approx
\operatorname{Paraphrase}(Q_t)
$$

或：

$$
Q_{t+1}
=
\operatorname{ExpandTerms}(Q_t)
$$

那麼系統可能只是反覆探索同一局部資訊區域。

因此本文提出：

$$
\boxed{
\text{Search Iteration}
\neq
\text{Research Adaptation}
}
$$

真正的 adaptation 要求：

$$
\text{evidence state changed}
\Rightarrow
\text{search strategy may change}
$$

---

# 2. 從 Query-Driven 到 Gap-Driven

Query-driven loop：

$$
Q_t
\rightarrow
R_t
\rightarrow
Q_{t+1}
$$

Gap-driven loop：

$$
S_t
\rightarrow
G_t
\rightarrow
\Pi_{t+1}
\rightarrow
O_{t+1}
\rightarrow
E_{t+1}
\rightarrow
G_{t+1}
$$

其中：

- $S_t$：Search State；
- $G_t$：Gap State；
- $\Pi_{t+1}$：下一輪 Search Plan；
- $O_{t+1}$：搜尋 observation；
- $E_{t+1}$：更新後 Evidence State。

因此：

$$
\boxed{
\Pi_{t+1}
=
f(G_t,S_t)
}
$$

而不只是：

$$
Q_{t+1}=f(Q_t)
$$

---

# 3. Confirmation Bias 為何與搜尋系統有關

Nickerson 將 confirmation bias 概括為傾向以偏向既有 beliefs、expectations 或 hypothesis 的方式尋找或解釋 evidence。Klayman 則提醒 confirmation bias 並不是單一、簡單、同質的心理現象；不同 task 中的 positive test strategy 可能具有不同效果。

因此本文不做：

$$
\text{Human Confirmation Bias}
=
\text{AI Search Failure}
$$

的簡化類比。

但 AI Search Planner 存在一個結構上相似的危險：

> 當新 query 由目前暫時結論生成時，暫時結論會反過來限制下一輪可見資訊空間。

例如：

```text
initial hypothesis
↓
supporting query
↓
supporting results
↓
stronger supporting query
↓
more supporting results
```

形成：

$$
H_t
\rightarrow
Q_t^+
\rightarrow
E_t^+
\rightarrow
H_{t+1}^{\text{stronger}}
$$

若缺少 counter-search branch，這個 loop 可以自我強化。

---

# 4. Counter-Evidence-First 不是「反對永遠優先」

本文中的 `Counter-Evidence-First` 不是「只相信反對意見」，也不是「每個 claim 一定要找一個反例才算完成」。

而是：

> 當 evidence structure 顯著單邊、claim impact 高、或目前 conclusion 對反證高度敏感時，Planner 應提高尋找 counter-evidence 的 priority。

因此：

$$
\operatorname{CounterPriority}(c)
=
f(
I(c),
A(c),
U(c),
D(c)
)
$$

其中：

- $I(c)$：claim impact；
- $A(c)$：evidence asymmetry；
- $U(c)$：uncertainty；
- $D(c)$：decision sensitivity。

---

# 5. 與 Falsificationism 的關係

Popper 對 falsifiability 的討論強調，一個科學理論需要能與可能觀察發生衝突。

AUSI 的 counter-evidence search 可以從這種科學方法論精神獲得啟發，但本文不主張：

$$
\text{Counter-Evidence Search}
=
\text{Popperian Falsificationism}
$$

因為很多搜尋任務不是科學理論檢驗；evidence 可能只是 qualification，而非直接 falsification；observation 本身可能不可靠；complex theories 可能涉及 auxiliary assumptions；專利、經濟、氣象等任務也具有不同 verification semantics。

因此 counter-evidence 是工程搜尋策略，而不是完整科學哲學。

---

# 6. FEVER 的 Evidence-State 啟發

FEVER 將 claim verification 標記為：

```text
SUPPORTS
REFUTES
NOT ENOUGH INFO
```

這個三分法提醒 Search Planner：

$$
\text{No Supporting Evidence Found}
\neq
\text{Refuted}
$$

以及：

$$
\text{No Refuting Evidence Found}
\neq
\text{Supported}
$$

因此 AUSI 使用：

```text
supported
contradicted
qualified
insufficient_evidence
unsearched
searched_not_found
```

等不同狀態，而不是二元 true / false。

---

# 7. Active Learning 的啟發

Lewis 與 Gale 在 1994 年研究 uncertainty sampling：不是隨機選更多資料，而是優先選擇分類器最不確定的 training instances。Settles 對 active learning 的整理又將 uncertainty sampling、query-by-committee、expected model change、expected error reduction 與 density-weighted methods 等策略納入共同框架。

AUSI 不把 search 等同 active learning，但借用一個核心思想：

> **下一個資訊取得行動可以由「目前最需要減少的不確定性」決定。**

因此：

$$
a^*
=
\arg\max_a
\mathbb{E}[
\Delta U(a)
]
$$

可以是 Planner 的一個 objective。

---

# 8. Information Gain 與 Gap Reduction

一般 information gain：

$$
IG(a)
$$

問：

> 此 action 預期帶來多少新資訊？

Gap reduction：

$$
GR(a)
$$

則問：

> 此 action 預期減少多少與目前 task acceptance 直接相關的缺口？

可能存在：

$$
IG(a_1)>IG(a_2)
$$

但：

$$
GR(a_1)<GR(a_2)
$$

例如 $a_1$ 找到 100 篇相關新聞，而 $a_2$ 找到缺失的官方 primary dataset；對當前 task， $a_2$ 更有價值。

---

# 9. Gap Vector

本文定義：

$$
\mathbf{G}_t
=
(
G_E,
G_C,
G_U,
G_D,
G_T,
G_P,
G_R
)_t
$$

其中：

- $G_E$：Evidence Gap；
- $G_C$：Coverage Gap；
- $G_U$：Uncertainty Gap；
- $G_D$：Diversity / Independence Gap；
- $G_T$：Temporal / Version Gap；
- $G_P$：Provider / Policy Gap；
- $G_R$：Representation / Terminology Gap。

這些 gap 不一定全部是 scalar。

---

# 10. Evidence Gap

Paper 05 已提出 $G_E(c)$，表示 claim $c$ 距離 evidence acceptance criteria 還缺什麼。

例如：

```text
missing_primary_source
missing_independent_support
missing_counter_evidence_check
unresolved_contradiction
missing_anchor
missing_version
low_directness
```

因此 Evidence Gap 是最直接的 replanning trigger。

---

# 11. Coverage Gap

定義 task coverage universe：

$$
\Omega_T
=
\Omega_{\text{term}}
\times
\Omega_{\text{source}}
\times
\Omega_{\text{time}}
\times
\Omega_{\text{language}}
\times
\Omega_{\text{jurisdiction}}
\times
\Omega_{\text{class}}
\times
\Omega_{\text{method}}
$$

已覆蓋：

$$
\Omega_t^{\text{covered}}
$$

則概念上：

$$
G_C
=
\Omega_T
\setminus
\Omega_t^{\text{covered}}
$$

open-world 中 $\Omega_T$ 通常無法完整列舉，因此這是 operational coverage space，而不是宇宙全體資訊。

---

# 12. Coverage Tensor

為避免只存單一 coverage 百分比，可以定義：

$$
\mathcal{C}_t
[
\text{source},
\text{method},
\text{language},
\text{time},
\text{class}
]
$$

例如 patent search：

```text
CPC class A: covered by lexical + semantic
CPC class B: classification only
JP language: not searched
US: searched
EP: searched
pre-2010: weak coverage
citation graph: only forward
```

這比：

```text
coverage = 82%
```

更可操作。

---

# 13. Uncertainty Gap

定義：

$$
G_U
=
\{
u_i
\mid
u_i>\tau_i
\}
$$

uncertainty 可以來自 entity identity、claim interpretation、source identity、evidence relation、data version、provider coverage 與 conflicting observations。

Planner 可針對最高 uncertainty region 搜尋。

---

# 14. Diversity / Independence Gap

如果目前：

$$
E^+(c)
=
\{e_1,e_2,e_3,e_4\}
$$

但：

$$
Origin(e_1)=\cdots=Origin(e_4)
$$

則：

$$
G_D(c)\gg0
$$

即使 evidence count 已很多。

此時 Planner 應：

$$
M_{\text{independent-source-search}}
$$

而不是再找第五篇轉載。

---

# 15. Temporal / Version Gap

若 claim 需要：

```text
latest value
```

但 evidence 是：

```text
2025-12 snapshot
```

則：

$$
G_T>0
$$

若兩個來源值不同但 vintage 不明：

$$
G_T
=
\text{version ambiguity}
$$

此時應執行：

$$
M_{\text{version-resolve}}
$$

而不是 generic corroboration search。

---

# 16. Provider / Policy Gap

可能知道某資料存在，但目前 surface：

```text
automation = denied
```

則：

$$
G_P
=
\text{authorized provider unavailable}
$$

Planner 可以搜尋 official API、bulk dataset、licensed mirror 或 other authorized source。

這延續 Paper 04。

---

# 17. Representation / Terminology Gap

搜尋失敗可能不是資料不存在，而是 query representation 太窄。

例如 patent prior art 中 modern product term 可能在舊專利中以不同 engineering vocabulary 表示。

因此：

$$
G_R
=
\text{representation blind spot}
$$

可以觸發 synonym expansion、historical terminology、classification search、multilingual search、function-based decomposition 或 semantic search。

---

# 18. Gap Priority Function

不是所有 gap 都同樣重要。

定義：

$$
Priority(g)
=
w_I I(g)
+
w_R R(g)
+
w_U U(g)
+
w_A A(g)
-
w_C C(g)
$$

其中：

- $I(g)$：對最終 conclusion impact；
- $R(g)$：residual risk；
- $U(g)$：uncertainty；
- $A(g)$：acceptance necessity；
- $C(g)$：resolution cost。

高風險 task 可以把 $A(g)$ 設成 hard gate。

---

# 19. Expected Gap Reduction

對 action $a$：

$$
EGR(a)
=
\mathbb{E}
[
\|\mathbf{G}_t\|
-
\|\mathbf{G}_{t+1}\|
\mid a
]
$$

更一般可以使用 task-weighted distance：

$$
EGR_T(a)
=
\mathbb{E}
[
D_T(\mathbf{G}_t)
-
D_T(\mathbf{G}_{t+1})
]
$$

Planner 可最大化：

$$
\frac{EGR_T(a)}{\operatorname{Cost}(a)}
$$

但 high-risk mandatory gap 不應只靠 ratio 排序。

---

# 20. Gap-to-Method Mapping

例如：

```text
missing_primary_source
    → primary_source_resolution

missing_independent_support
    → source_diversification

unresolved_contradiction
    → contradiction_resolution

missing_version
    → temporal_version_search

uncovered_classification
    → classification_search

uncovered_language
    → multilingual_search

representation_blind_spot
    → query_divergence / semantic search

policy_blocked
    → authorized_provider_search
```

因此：

$$
G
\rightarrow
M
$$

成為 Method Registry 的重要 relation。

---

# 21. Gap-to-Provider Mapping

同一 gap 也可能要求特定 provider class。

例如：

```text
missing legal status
→ patent office legal-status source

missing weather quality flag
→ official meteorological dataset

missing historical economic vintage
→ revision-aware economic provider
```

所以：

$$
G
\rightarrow
(M,P)
$$

比 generic search 更精確。

---

# 22. Counter-Evidence Trigger

對 claim $c$ 定義：

$$
A_c
=
\frac{
W(E^+(c))
}{
W(E^-(c))+W(E^q(c))+\epsilon
}
$$

其中：

- $E^+$：support；
- $E^-$：contradict；
- $E^q$：qualify。

若：

$$
A_c>\tau_A
$$

且：

$$
Impact(c)>\tau_I
$$

則 counter-search priority 上升。

這不是因為 support 多就是錯，而是因為高影響命題在證據高度單邊時值得主動測試 blind spot。

---

# 23. Counter-Evidence 的種類

Counter-evidence 不只有直接反例。

## 23.1 Direct Contradiction

明確指出 claim 不成立。

## 23.2 Boundary Condition

指出 claim 只在特定條件成立。

## 23.3 Alternative Explanation

同一 observation 可由不同原因解釋。

## 23.4 Measurement Conflict

不同 measurement method 得到不同結果。

## 23.5 Version Conflict

不同時間 / revision 產生不同值。

## 23.6 Population Conflict

不同 sample / jurisdiction / subgroup 不一致。

## 23.7 Source Critique

來源本身被 correction、retraction 或 methodological criticism。

---

# 24. Counter-Query Generation

假設 claim：

$$
c:
X\rightarrow Y
$$

Counter-query 不應只生成：

```text
X does not cause Y
```

還可以生成：

```text
X Y null result
X Y replication failure
X Y boundary conditions
X Y alternative explanation
X Y criticism
X Y contradictory evidence
X Y subgroup differences
X Y revised data
```

不同 domain 可由 Domain Pack 提供 templates。

---

# 25. 反證搜尋不能製造 False Balance

如果高品質 evidence 已極度集中在一個方向，counter-search 不能為了形式平衡而把低品質反對來源提升成同等權重。

因此：

$$
\operatorname{SearchForCounter}
\neq
\operatorname{EqualWeightCounter}
$$

反證優先是 search scheduling policy，不是 evidence weighting policy。

---

# 26. Counter-Evidence Quality Gate

反證結果仍需 Paper 05 verification。

因此：

$$
R_{\text{counter}}
\rightarrow
E_c^-
\rightarrow
E_v^-
$$

只有 verified counter-evidence 才應改變 Claim–Evidence Graph。

---

# 27. Negative Search Result

「沒找到」本身也需要結構化。

定義 Negative Search Result：

$$
N_s
=
(
M,
P,
Q,
scope,
time,
filters,
result=0
)
$$

它代表：

> 在這個明確搜尋範圍內沒有找到符合條件的結果。

但：

$$
N_s
\not\Rightarrow
\text{global nonexistence}
$$

---

# 28. Searched-Not-Found 與 Unsearched 分離

狀態：

```text
UNSEARCHED
SEARCHED_NOT_FOUND
FOUND_UNVERIFIED
FOUND_VERIFIED
FOUND_CONTRADICTED
```

必須不同。

這使 Planner 不會反覆重搜已經完整執行過的相同 branch。

---

# 29. Search Exhaustion Profile

對某 branch $b$：

$$
X_b
=
(
M_b,
P_b,
scope_b,
iterations_b,
novelty_b,
eligible_b
)
$$

用來描述：

> 這個 branch 搜到什麼程度？

而不是二元：

```text
done / not done
```

---

# 30. Diminishing Novelty

第 $t$ 輪新增候選：

$$
N_t
$$

去重後新穎結果：

$$
N_t^{new}
$$

Novelty Rate：

$$
\nu_t
=
\frac{|N_t^{new}|}{|N_t|+\epsilon}
$$

若連續多輪：

$$
\nu_t<\tau_\nu
$$

可能表示 branch 接近 saturation。

但 saturation 只是停止訊號之一。

---

# 31. Evidence Yield

更重要的是：

$$
\eta_t
=
\frac{
|\Delta E_v|
}{
Cost_t
}
$$

即每單位成本新增 verified evidence。

可能：

$$
\nu_t\gg0
$$

但：

$$
\eta_t\approx0
$$

代表找到很多新結果，卻沒有提高 evidence state。

---

# 32. Branch Saturation

定義：

$$
Sat(b)
=
f(
\nu_t,
\eta_t,
coverage_b,
iterations_b
)
$$

當 novelty 很低、verified evidence yield 很低、mandatory local coverage 已滿足時，可以停止該 branch。

---

# 33. Global Stop 與 Branch Stop 分離

一個 Search Graph 可能：

```text
branch A = saturated
branch B = unresolved
branch C = policy blocked
branch D = high-value new path
```

因此：

$$
Stop(b_A)=1
$$

不表示：

$$
Stop(\Pi)=1
$$

Global stopping 必須看所有 mandatory gaps。

---

# 34. Systematic Review 方法學的啟發

PRISMA-S 要求完整報告 databases / information sources、full search strategies、citation searching、dates、records management 與 search peer review 等。

TARCiS 又特別要求 citation searching 說明 seed references、direction、date、iteration count、indexes 與 stopping reason。

這些既有方法學表明：

> 完整、可重現的搜尋不能只留下「我查過」。

AUSI 將這些要求一般化到 Search Receipt 與 Branch Exhaustion Profile。

---

# 35. Citation Search Iteration

若 citation searching 找到新的 eligible records，可以考慮用新 records 再做下一輪 citation search。

形式上：

$$
Seeds_{t+1}
=
Seeds_t
\cup
Eligible_t^{new}
$$

AUSI 可以使用 $\nu_t$ 與 $\eta_t$ 輔助 stopping。

---

# 36. Completeness 不應被偽裝

對 open-world search，通常無法證明：

$$
Recall=1
$$

因此最終報告不應宣稱：

> 已確認不存在其他相關資料。

除非 task / database space 本身封閉且可證明完整枚舉。

更合理是：

> 在已聲明 search space 中未發現其他符合條件結果。

---

# 37. Coverage Claim 需要 Scope

例如：

```text
searched:
  providers = [A, B, C]
  languages = [en, zh]
  date_range = 2000-2026
  methods = [lexical, semantic, citation]
  jurisdictions = [US, EP]
```

因此：

$$
\operatorname{CoverageClaim}
=
(\Omega_{\text{declared}},\Omega_{\text{covered}})
$$

---

# 38. Uncertainty-Directed Search

若 Claim–Evidence Graph 中某 edge：

$$
r(e,c)
$$

confidence 低，Planner 可以優先搜索 clearer primary source、alternative wording、direct measurement 或 domain-specific database。

這與 active learning 的 uncertainty-driven acquisition 類似，但搜尋對象是外部 evidence。

---

# 39. Committee Disagreement

如果多 verifier：

$$
V_1(e,c),V_2(e,c),\ldots,V_n(e,c)
$$

高度不一致，則：

$$
Disagree(e,c)\gg0
$$

可以成為 query trigger。

這概念上類似 query-by-committee：

> 分歧越大，越值得取得新資訊。

---

# 40. Decision Sensitivity

不是所有不確定性都值得同樣成本。

若最終 decision：

$$
D
$$

對 claim $c$ 非常敏感：

$$
\frac{\partial D}{\partial c}\gg0
$$

則 $c$ 的 gap priority 應提高。

這在 FTO、regulatory、investment 與 safety 任務特別重要。

---

# 41. Value of Gap Resolution

定義：

$$
VGR(g)
=
P(\text{resolution}\mid a)
\times
Impact(g)
$$

再扣除：

$$
Cost(a)+Risk(a)
$$

形成 action priority。

---

# 42. Search Portfolio

Planner 不一定只選一個 action。

可以選：

$$
A_t
=
\{a_1,\ldots,a_k\}
$$

形成 search portfolio。

例如：

```text
primary source resolution
+
counter-evidence search
+
independent-provider check
```

三個 branch 平行。

---

# 43. Portfolio Diversification

若所有 actions 都使用 same provider、same query representation、same language、same source community，則 portfolio 看似多路，其實高度相關。

因此定義 action correlation：

$$
\rho(a_i,a_j)
$$

Planner 可偏好：

$$
\text{high expected gain}
+
\text{low redundancy}
$$

---

# 44. Search Diversity 不只是 Provider Diversity

Diversity 可以包含：

$$
D
=
(
D_{\text{provider}},
D_{\text{method}},
D_{\text{language}},
D_{\text{perspective}},
D_{\text{representation}},
D_{\text{origin}}
)
$$

只換搜尋引擎但 query 完全相同，不一定產生方法 diversity。

---

# 45. Gap Clustering

大量 claims 可能共享同一 gap。

例如：

```text
20 claims all need same official dataset
```

可聚類：

$$
\{g_1,\ldots,g_{20}\}
\rightarrow
G^*
$$

用一個 acquisition action 同時解決。

這降低重複搜尋成本。

---

# 46. Gap Dependency Graph

有些 gap 必須先解決。

例如：

```text
entity identity unresolved
↓
cannot select correct dataset
↓
cannot verify observation
```

建立：

$$
G_G
=
(V_G,E_G)
$$

Planner 應先解 upstream gap。

---

# 47. Representation Gap 可以造成 False Negative

如果：

$$
Q=\text{modern term}
$$

而歷史來源使用：

$$
Q'=\text{old terminology}
$$

則：

$$
Search(Q)=\varnothing
$$

不表示：

$$
RelevantDocs=\varnothing
$$

因此 negative result 之後要檢查 representation gap。

---

# 48. Provider Gap 可以造成 False Negative

同理：

$$
P_1(Q)=\varnothing
$$

不表示：

$$
P_2(Q)=\varnothing
$$

因此 `searched_not_found` 必須綁定 provider scope。

---

# 49. Method Gap 可以造成 False Negative

Lexical search 沒找到：

$$
M_{\text{lexical}}(Q)=\varnothing
$$

不表示 semantic / graph / classification search 也找不到。

因此：

$$
\text{Not Found}
=
\text{Method-Relative Observation}
$$

---

# 50. Counter-Evidence Gap

定義：

$$
G_-(c)
=
\begin{cases}
1, & \text{counter-search required but not performed}\\
0, & \text{counter-search requirement satisfied}
\end{cases}
$$

高風險 claim 可把它列為 mandatory gap。

---

# 51. Asymmetric Search Budget

Counter-search budget 不必與 support search budget 一樣。

可以依：

$$
B_-(c)
=
f(
Impact(c),
Asymmetry(c),
Risk(c)
)
$$

動態分配。

---

# 52. Counter Search Failure 不等於 Confirmed

如果完整 counter-search branch：

$$
R^-=\varnothing
$$

只表示：

> 在已聲明 counter-search scope 中沒有找到 verified contradiction。

不等於：

$$
c=\text{proven true}
$$

---

# 53. Qualification-First Search

某些 claim 不是「真 / 假」問題，而是 scope 過寬。

例如：

> 某方法永遠優於另一方法。

此時最有價值的 query 可能是：

```text
under what conditions does it fail?
for which populations?
for which datasets?
what assumptions are required?
```

因此：

$$
M_{\text{qualification-search}}
$$

可以比 direct contradiction 更有效。

---

# 54. Boundary Search

定義：

$$
Boundary(c)
$$

搜尋 lower / upper bound、domain of validity、time validity、jurisdiction、population 與 dependency assumptions。

這能減少 AI 由局部 evidence 做全域推論。

---

# 55. Adversarial Search Perspective

可以建立 adversarial role：

```text
Current synthesis:
    claim C seems supported

Adversarial planner:
    what evidence would most strongly overturn or narrow C?
```

但 adversarial planner 只能提 query / method proposal。

它不能自行偽造 opposition。

---

# 56. Multi-Agent 不是必要條件

反證搜尋可以由單一 planner 的 branch、rule-based counter module、secondary model 或 human reviewer 執行。

因此：

$$
\text{Counter Search}
\neq
\text{Multi-Agent Requirement}
$$

避免將方法論綁到特定 Agent 架構。

---

# 57. Search Gap State Machine

Gap 可以：

```text
OPEN
PLANNED
SEARCHING
PARTIALLY_RESOLVED
RESOLVED
BLOCKED
REVIEW_REQUIRED
REOPENED
```

比：

```text
todo / done
```

更適合研究。

---

# 58. Gap Reopening

已解決 gap 也可能重新打開。

例如 new revision、new contradiction、source retracted、policy changed、claim scope expanded 或 provider index updated。

因此：

$$
Resolved(g,t_1)
\not\Rightarrow
Resolved(g,t_2)
$$

---

# 59. Reopening Trigger

定義：

$$
Reopen(g)
=
1
$$

當：

```text
new_evidence_impacts_gap
version_changed
source_invalidated
verification_failed
task_scope_changed
monitoring_condition_triggered
```

---

# 60. Continuous Research

某些研究不是一次性，例如 patent watch、economic data revision、weather warnings、regulation updates 與 academic new papers。

此時：

$$
Stop
$$

代表：

> 本輪 closed。

不是：

> 永久 completed。

---

# 61. Search Epoch

定義：

$$
\mathcal{E}_k
$$

為一輪 research epoch。

每個 epoch 有：

```text
start state
search plan
evidence changes
gap changes
stop reason
```

新事件可開：

$$
\mathcal{E}_{k+1}
$$

---

# 62. Autonomous Research Loop

完整閉環：

$$
C_t
\rightarrow
E_t
\rightarrow
G_t
\rightarrow
\Pi_{t+1}
\rightarrow
R_{t+1}
\rightarrow
E_{t+1}
\rightarrow
C_{t+1}
$$

其中 claim 也可以被 strengthened、weakened、split、qualified 或 withdrawn。

---

# 63. Claim Revision

若 evidence 指出原 claim 太寬：

$$
c:
\forall x,P(x)
$$

可改成：

$$
c':
\forall x\in S,P(x)
$$

因此研究閉環不只改搜尋，也改 claim representation。

---

# 64. Hypothesis Set

可以維持：

$$
\mathcal{H}
=
\{h_1,\ldots,h_n\}
$$

而不是過早只保留一個 current answer。

Search 可以比較 alternative hypotheses。

---

# 65. Hypothesis Elimination 與 Retention

新 evidence $e$ 可以 eliminate、weaken、strengthen 或 leave unresolved 某 hypothesis。

這更接近研究，而非答案生成。

---

# 66. Contradiction Resolution Plan

遇到 contradiction：

$$
e_a \;\bot\; e_b
$$

Planner 不應立即平均。

應先分類可能原因：

```text
version
definition
population
unit
time
jurisdiction
methodology
source error
real dispute
```

再生成 targeted Search Plan。

---

# 67. Version Conflict Example：Economics

若兩個 GDP 值不同：

```text
source A = first release
source B = revised release
```

則：

$$
\operatorname{Contradiction}=0
$$

而：

$$
\operatorname{VersionRelation}=\text{supersedes}
$$

Gap resolution 應查 vintage metadata。

---

# 68. Station Conflict Example：Meteorology

兩個站點觀測不同：

$$
x_A\neq x_B
$$

不代表來源錯誤。

可能是 spatial difference、station relocation、instrument difference、quality flag 或 observation interval。

因此 gap 驅動查 station metadata。

---

# 69. Patent Conflict Example

一份 patent family member 的 claim：

$$
c_{US}
$$

與另一 jurisdiction：

$$
c_{EP}
$$

可能不同。

因此 prior-art / FTO search 不能把 family-level semantic similarity 當 claim-level identity。

Gap 是：

```text
jurisdiction-specific claim version unresolved
```

---

# 70. Academic Conflict Example

兩篇 paper 結論相反。

Planner 可以找 replication、meta-analysis、比較 sample、比較 measurement、比較 publication year 或找 corrections。

這是 contradiction-driven search。

---

# 71. Gap-Driven Search Templates

SearchMethod Registry 可以新增：

```text
resolve_primary_source(gap)
resolve_version(gap)
resolve_identity(gap)
seek_independent_support(gap)
seek_counter_evidence(gap)
seek_qualification(gap)
expand_terminology(gap)
expand_classification(gap)
expand_language(gap)
expand_provider(gap)
resolve_policy_surface(gap)
```

---

# 72. Planner API

可以提供：

```text
detect_gaps(state)
rank_gaps(gaps, task)
map_gap_to_methods(gap)
estimate_gap_reduction(action)
plan_gap_resolution(gap)
execute_gap_plan(plan)
update_gap_state(observation)
reopen_gap(event)
```

---

# 73. Gap Receipt

Search Receipt 應記錄：

```text
gap_id
gap_type
why_opened
priority
actions_attempted
providers
methods
negative_results
evidence_found
resolution_state
stop_reason
residual_uncertainty
```

這使「為什麼搜這一輪」可審計。

---

# 74. Search Transparency

PRISMA-S 的精神可以一般化為：

> Search Method 本身是 research method，必須可報告。

因此最終 result 應能重建：

$$
\text{Why this branch existed}
$$

而不只是：

$$
\text{What query was sent}
$$

---

# 75. Negative Evidence 與 Absence Evidence

本文避免將：

$$
\text{absence of evidence}
$$

與：

$$
\text{evidence of absence}
$$

混為一談。

Evidence of absence 需要 task-specific measurement model。

---

# 76. Closed-World Search

如果 domain $\Omega$ 是可枚舉、版本固定、查詢完備的 database，

則有可能建立：

$$
SearchAll(\Omega,Q)=\varnothing
$$

作為較強 negative evidence。

這與 open-world Web Search 不同。

---

# 77. Open-World Search

open-world 中：

$$
R=\varnothing
$$

只表示：

$$
R(M,P,Q,t)=\varnothing
$$

而不是：

$$
\forall x,\neg Relevant(x)
$$

這必須寫入系統語義。

---

# 78. Search Cost Ceiling

Gap 可能永遠無法完全消失。

因此每個 gap 可有：

$$
B_g
$$

最大 resolution budget。

若耗盡：

```text
UNRESOLVED_BUDGET_LIMIT
```

而不是硬改成 resolved。

---

# 79. Policy-Blocked Gap

若最佳 source 被 Paper 04 阻擋：

```text
BLOCKED_POLICY
```

Planner 嘗試 alternative source。

若仍沒有：

```text
REVIEW_REQUIRED / RESIDUAL_GAP
```

---

# 80. Human Escalation Gap

某些 gap 只能由 expert 判斷，例如 claim construction、legal interpretation、ambiguous study quality 或 conflicting definitions。

因此：

$$
G\rightarrow HumanReview
$$

是合法 Search Plan terminal。

---

# 81. Search Stopping

Global stop 要求至少：

$$
G_{\text{mandatory}}
\le
\tau_G
$$

以及：

$$
\max_a EGR(a)-Cost(a)<\epsilon
$$

或 forced stop。

即：

$$
Stop
=
GoalSatisfied
\lor
MarginalValueLow
\lor
ForcedStop
$$

延續 Paper 03。

---

# 82. Stop Reason 必須可區分

```text
ACCEPTANCE_MET
SATURATED
BUDGET_LIMIT
POLICY_BLOCKED
PROVIDER_EXHAUSTED
HUMAN_REVIEW_REQUIRED
TIME_LIMIT
NO_FEASIBLE_ACTION
```

其中只有部分表示成功。

---

# 83. Saturation 不是 Complete Recall

即使：

$$
\nu_t\rightarrow0
$$

也不能推出：

$$
Recall=1
$$

saturation 是：

> 在目前 search process 下，新增資訊趨近變少。

不是：

> 世界上沒有遺漏資訊。

---

# 84. Counter-Evidence Saturation

Counter branch 也可 saturation。

例如多個反向 query、provider、方法都沒有產生 verified counter-evidence。

可以記：

```text
counter_search_scope
counter_methods
counter_providers
counter_novelty
counter_verified_yield
```

再關閉該 branch。

---

# 85. Search Confidence 不應取代 Gap State

系統不應只輸出：

```text
confidence = 0.93
```

因為無法知道：

> 0.07 是缺什麼？

Gap state 可以回答：

```text
primary source complete
independence incomplete
counter-search complete
version complete
JP jurisdiction unsearched
```

這更可行動。

---

# 86. Domain Pack：Patent Intelligence

Prior-art gap vector 可以包含：

```text
terminology
CPC/IPC
jurisdiction
language
priority period
citation graph
family normalization
claim mapping
non-patent literature
```

FTO 還加入：

```text
current legal status
jurisdiction-specific claims
product-feature mapping
```

---

# 87. Domain Pack：Economics

Gap 可以包含：

```text
series identity
official source
unit
seasonal adjustment
vintage
revision
frequency
missing observation
```

counter-evidence 可以是 alternative official estimate 或 methodological revision，而不是隨便找相反評論。

---

# 88. Domain Pack：Meteorology

Gap：

```text
station identity
coverage period
quality flags
spatial representativeness
instrument changes
missingness
alternate dataset
```

---

# 89. Domain Pack：Academic Research

Gap：

```text
foundational papers
recent papers
counter-position
replication
systematic review
citation graph
methodological critique
uncovered terminology
```

---

# 90. Domain Pack：Standards / Regulation

Gap：

```text
current version
superseded version
jurisdiction
effective date
official text
implementation guidance
amendments
exceptions
```

---

# 91. Benchmark

建立 Gap-Driven Autonomous Search Benchmark。

任務應包含：

- hidden primary source；
- misleading duplicate sources；
- strong support but one decisive counterexample；
- version conflict；
- multilingual missing evidence；
- provider-specific blind spot；
- classification-only discoverable result；
- unsupported overbroad claim；
- policy-blocked source with legal alternative；
- negative open-world search。

---

# 92. Baselines

## B0 — Single Search

固定一次 retrieval。

## B1 — Iterative Query Rewrite

每輪改寫 query。

## B2 — Query Expansion

固定方法、多 query。

## B3 — Search Agent

模型自行多輪搜尋，但沒有 explicit gap state。

## Proposed — Gap-Driven Planner

使用 Evidence Gap、Coverage Tensor、Counter Trigger、Uncertainty、Branch Saturation 與 Gap Receipt。

---

# 93. Metrics

$$
\text{Verified Coverage}
$$

$$
\text{Gap Resolution Rate}
$$

$$
\text{Counter-Evidence Discovery Rate}
$$

$$
\text{Qualification Discovery Rate}
$$

$$
\text{Independent Evidence Gain}
$$

$$
\text{False Completion Rate}
$$

$$
\text{Premature Stop Rate}
$$

$$
\text{Redundant Search Rate}
$$

$$
\text{Negative-Result Calibration}
$$

$$
\text{Cost per Resolved Mandatory Gap}
$$

---

# 94. Gap Efficiency

定義：

$$
GE
=
\frac{
\sum_g w_g\Delta G_g
}{
Cost
}
$$

用來衡量搜尋真正解決多少 task-relevant uncertainty。

---

# 95. Redundancy Rate

若新結果大多是 duplicates、same origin、same evidence role 或 same method blind spot，則：

$$
RR
=
\frac{
N_{\text{redundant}}
}{
N_{\text{retrieved}}
}
$$

Gap-driven planner 應降低 $RR$。

---

# 96. False Completion Rate

系統宣稱 completed，但 mandatory gap 實際仍 open：

$$
FCR
=
\frac{
N_{\text{false-complete}}
}{
N_{\text{complete}}
}
$$

這對高風險 task 很重要。

---

# 97. 初步研究命題

## P6.1 — Gap-Driven Planning Hypothesis

以 explicit gap state 生成 Search Plan，應比單純 query reformulation 更有效率地提高 verified evidence coverage。

## P6.2 — Counter-Evidence Scheduling Hypothesis

對高影響且 evidence asymmetric 的 claims，主動 counter-search 應提高 contradiction / qualification discovery rate，並降低過度確信。

## P6.3 — Uncertainty-Directed Search Hypothesis

將高不確定但高決策影響的 claim / relation 優先搜尋，應提高單位搜尋成本的 decision-relevant information gain。

## P6.4 — Coverage Tensor Hypothesis

多軸 coverage representation 應比單一 coverage score 更能辨識 language、provider、classification 與 temporal blind spots。

## P6.5 — Branch Saturation Hypothesis

利用 novelty + verified evidence yield + local mandatory coverage 決定 branch stopping，應降低 redundant search，而不顯著提高 mandatory-gap miss rate。

## P6.6 — Negative-State Typing Hypothesis

區分 `UNSEARCHED` 與 `SEARCHED_NOT_FOUND`，應降低重複搜尋與錯誤 absence inference。

## P6.7 — Gap Reopening Hypothesis

允許已 resolved gaps 因 revision、retraction、新 contradiction 或 task change 重新開啟，可提高 long-running research system 對世界變化的適應性。

---

# 98. 工程落地

對 `ai-web-research`，可以新增：

```text
gaps/
    models.py
    detector.py
    coverage.py
    uncertainty.py
    counter.py
    priority.py
    saturation.py
    negative_results.py
    reopening.py

planning/
    gap_planner.py
    portfolio.py
    branch_state.py

evidence/
    gap_projection.py
```

---

# 99. Gap Object

```text
Gap
├── gap_id
├── type
├── claim_refs
├── evidence_refs
├── coverage_axis
├── severity
├── mandatory
├── uncertainty
├── impact
├── estimated_cost
├── suggested_methods
├── suggested_provider_classes
├── status
├── attempts
└── reopen_triggers
```

---

# 100. Counter Search Object

```text
CounterSearchTask
├── target_claim
├── current_support
├── current_contradictions
├── qualification_state
├── asymmetry
├── impact
├── query_templates
├── method_candidates
├── budget
└── stopping_profile
```

---

# 101. Canonical Autonomous Research Loop

```text
Task
↓
Initial Search Plan
↓
Authorized Acquisition
↓
Evidence Verification
↓
Claim–Evidence Graph
↓
Gap Detection
↓
Gap Prioritization
↓
Counter / Coverage / Uncertainty Search
↓
New Evidence
↓
Reverification
↓
Claim Revision
↓
Gap Recalculation
↓
Branch Stop / Global Stop / Reopen
```

---

# 102. 核心不變量

## I1 — Iteration ≠ Adaptation

$$
Q_{t+1}\neq\text{proof of adaptive research}
$$

## I2 — Not Found ≠ False

$$
\text{SEARCHED\_NOT\_FOUND}
\neq
\text{REFUTED}
$$

## I3 — No Counter-Evidence ≠ Proven

$$
E^-=\varnothing
\not\Rightarrow
c=\text{true}
$$

## I4 — Counter Search ≠ Counter Weight

搜尋反證不表示反證自動與支持證據等權。

## I5 — Saturation ≠ Complete Recall

$$
\nu\rightarrow0
\not\Rightarrow
Recall=1
$$

## I6 — Coverage Is Scoped

所有 coverage claim 必須帶 search scope。

## I7 — Negative Result Is Method–Provider Relative

$$
N_s=N_s(M,P,Q,t)
$$

## I8 — Gap State Drives Replanning

$$
G_t
\rightarrow
\Pi_{t+1}
$$

## I9 — Mandatory Gap Cannot Be Softly Traded Away

高風險 mandatory gap 不得只因 cost 高而被 utility 抵銷。

## I10 — Resolved ≠ Permanently Closed

$$
Resolved(g,t_1)
\not\Rightarrow
Resolved(g,t_2)
$$

## I11 — Contradiction Must Be Explained Before Averaging

版本、定義、population 等可能是假 contradiction。

## I12 — Research Can Revise Claims

搜尋閉環不只修改 query，也可以修改 claim。

---

# 103. 限制

第一，Gap detection 本身可能錯誤。如果 Task Interpreter 未辨識真正的 mandatory coverage axes，Planner 仍可能漏搜。

第二，counter-evidence search 可能被低品質、極端或非代表性內容污染，因此 counter result 仍需完整 Evidence Verification。

第三，coverage universe 在 open-world search 中不可完整觀察；Coverage Tensor 只能表達已聲明的 operational scope。

第四，uncertainty score 可能受 model calibration 影響；因此不能只以 LLM self-confidence 決定搜尋 priority。

第五，active learning 的 uncertainty sampling 與 external evidence search 並非同一問題；本文只借用「資訊取得可由 uncertainty 驅動」的思想。

第六，saturation threshold 高度依 domain 而變；patent search、systematic review、一般 Web QA 不應共用相同停止閾值。

第七，counter-evidence-first 不能被誤用為 false balance；evidence weighting 仍應依 evidence quality，而非 search branch identity。

第八，部分 claim 可能在有限資源下永遠保持 unresolved；系統必須允許 residual uncertainty。

第九，Gap Graph 與 Search Graph 都可能快速膨脹，需要 clustering、hierarchical planning 與 budget control。

---

# 104. 結論

AI 原生搜尋從這一篇開始不再主要由 query 驅動。

前五篇已建立：

$$
\text{Method}
+
\text{Planner}
+
\text{Policy}
+
\text{Evidence}
$$

但只有當 Evidence State 能反過來生成下一輪搜尋，系統才形成真正閉環。

因此本文提出：

$$
\boxed{
\text{Evidence State}
\rightarrow
\text{Gap State}
\rightarrow
\text{Search Plan}
}
$$

以及：

$$
\boxed{
\Pi_{t+1}
=
f(
G_E,
G_C,
G_U,
G_D,
G_T,
G_P,
G_R,
G_{CE},
B_t
)
}
$$

下一輪 Search Plan 不再只是問：

> 「還可以怎麼改寫 query？」

而是問：

> 「目前哪一個高價值缺口仍然阻止我完成任務？」

因此 AI 可以選擇：

```text
找 primary source
找另一個獨立來源
找反證
找 qualification
查版本
查另一語言
查另一 classification
換 provider
補 citation graph
解 entity identity
```

這使：

$$
\text{Search}
$$

開始真正成為：

$$
\text{Evidence-directed epistemic action}
$$

Counter-Evidence-First 的核心也不是「反對優先於支持」，而是：

$$
\boxed{
\text{High-impact asymmetric evidence should trigger deliberate challenge}
}
$$

其目的不是製造平衡，而是避免搜尋策略被目前最容易取得的支持 evidence 鎖住。

最終 AUSI Autonomous Research Loop 為：

$$
\boxed{
\text{Claim}
\rightarrow
\text{Search}
\rightarrow
\text{Evidence}
\rightarrow
\text{Gap}
\rightarrow
\text{Counter / Coverage / Uncertainty Search}
\rightarrow
\text{New Evidence}
\rightarrow
\text{Claim Revision}
\rightarrow
\text{Replan / Stop}
}
$$

到 Paper 06，AUSI 已完成第一個完整的 autonomous research control loop。

下一篇也就是七篇核心論文的最後一篇：

> **Paper 07 — 搜尋作為可學習的認知程序：Search Receipt、經驗累積、策略評估與自我改進**

它將回答：

> 如果每次搜尋都留下完整 Search Receipt、Gap Resolution 與 Evidence Outcome，AI 能不能從過去搜尋經驗學會「什麼任務在什麼狀態下，用什麼搜尋策略最有效」？

形式上將進入：

$$
P(
\Pi
\mid
T,
S,
H_{\text{search}}
)
$$

使 AUSI 從「可規劃搜尋」再前進到「可從搜尋經驗改善規劃」。

---

# References

[1] Nickerson, R. S. (1998). *Confirmation Bias: A Ubiquitous Phenomenon in Many Guises*. Review of General Psychology, 2(2), 175–220. DOI: 10.1037/1089-2680.2.2.175.

[2] Klayman, J. (1995). *Varieties of Confirmation Bias*. Psychology of Learning and Motivation, 32, 385–418. DOI: 10.1016/S0079-7421(08)60315-1.

[3] Lewis, D. D., & Gale, W. A. (1994). *A Sequential Algorithm for Training Text Classifiers*. Proceedings of SIGIR 1994, 3–12. DOI: 10.1007/978-1-4471-2099-5_1.

[4] Settles, B. (2009). *Active Learning Literature Survey*. Computer Sciences Technical Report 1648, University of Wisconsin–Madison.

[5] Settles, B. (2012). *Active Learning*. Synthesis Lectures on Artificial Intelligence and Machine Learning. Morgan & Claypool.

[6] Thorne, J., Vlachos, A., Christodoulopoulos, C., & Mittal, A. (2018). *FEVER: a Large-scale Dataset for Fact Extraction and VERification*. Proceedings of NAACL-HLT 2018. arXiv:1803.05355.

[7] Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., et al. (2021). *PRISMA-S: an Extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews*. Systematic Reviews, 10, 39. DOI: 10.1186/s13643-020-01542-z.

[8] Hirt, J., Nordhausen, T., Fuerst, T., Ewald, H., Appenzeller-Herzog, C., & TARCiS Study Group. (2024). *Guidance on Terminology, Application, and Reporting of Citation Searching: the TARCiS Statement*. BMJ, 385:e078384. DOI: 10.1136/bmj-2023-078384.

[9] Bates, M. J. (1989). *The Design of Browsing and Berrypicking Techniques for the Online Search Interface*. Online Review, 13(5), 407–424.

[10] Marchionini, G. (2006). *Exploratory Search: From Finding to Understanding*. Communications of the ACM, 49(4), 41–46.

[11] Avriel, M., & Williams, A. C. (1970). *The Value of Information and Stochastic Programming*. Operations Research, 18(5), 947–954.

[12] Li, X., Dong, G., Jin, J., et al. (2025). *Search-o1: Agentic Search-Enhanced Large Reasoning Models*. Proceedings of EMNLP 2025.

[13] Li, X., Jin, J., Dong, G., et al. (2025). *WebThinker: Empowering Large Reasoning Models with Deep Research Capability*. Advances in Neural Information Processing Systems 38.

[14] Page, M. J., Moher, D., Bossuyt, P. M., et al. (2021). *PRISMA 2020 Explanation and Elaboration: Updated Guidance and Exemplars for Reporting Systematic Reviews*. BMJ, 372:n160.

[15] Popper, K. R. (1959). *The Logic of Scientific Discovery*. Hutchinson.

[16] Min, S., Krishna, K., Lyu, X., et al. (2023). *FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation*. Proceedings of EMNLP 2023.

[17] Yang, G. H., Dong, X., Luo, J., & Zhang, S. (2018). *Session Search Modeling by Partially Observable Markov Decision Process*. Information Retrieval Journal, 21(1), 56–80.

---

# Series Continuation

**Paper 07 — 搜尋作為可學習的認知程序：Search Receipt、經驗累積、策略評估與自我改進**

下一篇將把歷史搜尋執行資料表示為：

$$
H_{\text{search}}
=
\{
(T_k,S_k,\Pi_k,\mathcal{R}_k,E_k,G_k,O_k)
\}_{k=1}^{N}
$$

研究：

- Search Receipt schema；
- plan/outcome attribution；
- method effectiveness；
- provider effectiveness；
- domain-conditioned strategy performance；
- cost / latency learning；
- failed-search learning；
- strategy replay；
- policy-aware historical learning；
- planner evaluation；
- offline search-policy learning；
- exploration vs exploitation across future tasks；
- Search Strategy Memory。

最終目標不是讓 AI 記住「答案」，而是讓 AI 累積：

> **怎麼找答案的經驗。**

也就是從：

$$
\text{Search Intelligence}
$$

進一步走向：

$$
\boxed{
\text{Learning Search Intelligence}
}
$$
