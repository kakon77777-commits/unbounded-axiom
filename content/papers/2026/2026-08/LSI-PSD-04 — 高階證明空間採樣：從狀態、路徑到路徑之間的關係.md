# LSI-PSD-04 — 高階證明空間採樣：從狀態、路徑到路徑之間的關係

## Higher-Order Proof-Space Sampling: From States and Routes to Relations Among Routes

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 04  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Higher-Order Sampling and Route-Relation Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文提出「高階證明空間採樣」作為長程 AI 數學研究的操作性框架。本文中的一階、二階、三階與 $k$ 階，描述的是**研究對象的階層**：狀態、狀態間轉換、轉換間關係，以及關係之上的關係；它們不等同於微積分中的導數階數、攝動展開階數、張量階數、邏輯的高階語言階數或任何既有數學術語中的「order」。本文所有高階分類首先是 proof-space observatory 的研究標記；除非另有形式證明，不得把「某篇論文出現 second-order / higher-order 字樣」直接當成高階 proof-space sampling 的證據。本文不主張有限 corpus 的高階重訪能證明某未解命題錯誤、不可證、獨立或定義失敗。

---

## 摘要

當一個 AI 數學研究系統只做數十輪工作時，「找到新的命題、引理、估計、表示或反例候選」通常足以描述研究進展；但當同一問題被持續研究數百、數千甚至更多輪之後，研究對象會逐漸發生階層轉移。系統不再只採樣「證明空間中的點」，而開始採樣「從一個點到另一個點的轉換」；當多條不同路徑反覆撞上同一障礙時，研究又會轉向「路徑與路徑之間的關係」；當這些關係本身出現匯流、反饋、再進入與族級 no-go 結構時，研究便開始進入更高階的 proof-space sampling。

本文建立一個可操作的高階證明空間框架。令固定問題 $Q$ 、搜尋制度 $R$ 下的可觀測研究狀態空間為：

$$
\Omega_R^{(0)}(Q).
$$

本文把 proof move、representation change、lemma introduction、normalization、rescaling、compactness passage、contradiction step 等可審計轉換視為一階關係物件：

$$
\Omega_R^{(1)}(Q)
=
\mathcal T(\Omega_R^{(0)}(Q)).
$$

接著，若研究開始比較兩條或多條 proof route 是否同構、是否匯流到共同 obstruction、是否共享同一依賴核、是否可互相替換，則研究對象進入：

$$
\Omega_R^{(2)}(Q)
=
\mathcal R(\Omega_R^{(1)}(Q)).
$$

更一般地，本文以型別化遞迴表示：

$$
\Omega_R^{(k+1)}(Q)
=
\mathcal F_k(\Omega_R^{(k)}(Q)),
$$

其中 $\mathcal F_k$ 不被預設為單一函數空間，而是一族允許的關係、組合、等價、匯流、回饋與族級摘要算子。

本文的核心主張不是「研究階數越高越接近真理」，而是：**當一階 novelty 下降時，高階關係仍可能持續產生新資訊；因此只以新 theorem count 或新文本比例衡量長程研究，會漏掉重要的結構性進展。** 為此，本文定義 order-conditioned novelty：

$$
\nu_k(N),
$$

order-conditioned coverage：

$$
I_k(N),
$$

order-conditioned audited yield：

$$
\rho_k(N),
$$

以及 confluence degree、re-entry depth、route-family entropy、feedback depth、higher-order survival ratio 等觀測量。本文進一步定義 $K$ 階局部飽和：只有當指定 basin 中從 $0$ 階到 $K$ 階的新增已驗證等價類同時持續接近零，才可把該 basin 標為「 $K$ -order locally saturated」。即使如此，依照 LSI-PSD-01 的證明空間非結論原則，也不能推出底層數學空間已被耗盡。

本文把 2025--2026 年 formal theorem proving 的最新發展視為工程佐證而非等價物。LeanNavigator 直接把 Lean proof search 表示為 state-transition graph；LeanProgress 從局部 tactic prediction 轉向全 proof trajectory 的剩餘步數預測；AlphaProof 使用 proof-state representation 與 tree search；Goedel-Architect、LEAP 與 LeanMarathon 以 lemma dependency graph、blueprint 與 AND-OR DAG 保存全域證明結構；Chain-of-States 工作則顯式把 informal proof 轉為中介 proof-state 序列。這些系統共同說明：現代 theorem proving 已經把「狀態、轉換、軌跡、依賴圖」視為可計算物件，但目前主流目標仍主要是提高 proof success。本文則把相同類型的結構提升為**研究科學的觀測對象**，詢問不同路由如何重訪、匯流、被排除、形成族級障礙，以及這些關係在長期生成中是否自身飽和。

本文最後將框架套入 NS-203 corpus 作為初步案例。既有 observatory 的 tier 標記被重新解釋為 heuristic evidence，而非本體階數： $T_1$ 表示狀態或新路由採樣， $T_2$ 表示可辨識的回訪／轉換比較， $T_3$ 表示關係、匯流或回饋， $T_X$ 表示族級、all-order 或更高階 recurrence 候選。本文不以這些標記宣稱 Navier--Stokes 已飽和，而只把它們視為建立高階 proof-space observatory 的第一個長程語料測試。

**關鍵詞：** 高階證明空間採樣、proof trajectory、proof state、state-transition graph、route relation、confluence、obstruction、feedback、re-entry、local saturation、order-conditioned novelty、proof-space dynamics、AI 數學研究、Navier--Stokes corpus

---

# 1. 為什麼「又一篇新論文」逐漸不再是正確的研究單位

## 1.1 早期研究的自然單位是候選結果

在一個尚未被大量探索的問題上，研究者自然會問：

- 是否有新的 lemma？
- 是否有新的 estimate？
- 是否有新的 counterexample candidate？
- 是否有新的 representation？
- 是否有新的 proof strategy？

令第 $i$ 次研究產物為：

$$
g_i.
$$

早期可以近似把：

$$
g_i
$$

看成對研究空間的一個新採樣點。

若每個 $g_i$ 都帶來新的已驗證結構，則：

$$
\Delta I_0(i)>0.
$$

這時候「論文數」「lemma 數」「新概念數」雖然粗糙，仍有一定解釋力。

## 1.2 長程研究會改變問題本身的資料結構

當研究進入數百輪之後，常出現以下模式：

1. 新 representation 其實導回以前見過的 obstruction；
2. 新 lemma 只是舊 lemma 在不同尺度或座標下的改寫；
3. 不同 method family 共享同一個失敗核心；
4. 研究開始問「為什麼這幾條路都失敗？」；
5. 某個 no-go 不再只排除一個 lemma，而排除一整族 escalation；
6. 某條已排除路線在新的 parent assumption 下重新進場；
7. failure trace 本身成為下一輪的研究資料。

此時，研究的資訊不只存在於：

$$
\{g_i\}_{i=1}^N.
$$

還存在於：

$$
\{g_i\to g_j\},
$$

以及：

$$
\{(g_i\to g_j)\sim(g_p\to g_q)\},
$$

甚至存在於「這些關係之間的關係」。

因此長程研究真正需要的資料結構不是平面文件庫，而是一個分層關係系統。

## 1.3 本文的核心問題

本文問：

> 當研究系統開始反覆研究「路徑怎麼走」「不同路徑為什麼匯流」「匯流之後又如何形成新的反饋」時，我們應如何定義它正在採樣的對象？

答案不能只是：

> 它又寫了一篇 paper。

因為 paper 是容器，不是 proof-space 的自然型別。

---

# 2. 與現代 formal theorem proving 的接點

## 2.1 Proof state 已經是工程上的標準物件

在 interactive theorem proving 中，一個中間狀態不是模糊的「想法」，而可以是明確的 formal state：

$$
s_t
=
(\Gamma_t,G_t,M_t),
$$

其中：

- $\Gamma_t$ 是當前 local context；
- $G_t$ 是尚未關閉的 goals；
- $M_t$ 是 tactic、library、identifier 或其他 metadata。

對 tactic $a_t$，proof assistant 執行：

$$
s_{t+1}
=
T(s_t,a_t).
$$

這本身已是一個動力系統式描述。

## 2.2 LeanNavigator：證明可以被表示成 state-transition graph

Yin 與 Gao 在 2025 年的 LeanNavigator 工作中，直接把 Lean proof exploration 描述為 state graph：節點是 Lean states，邊是 tactic transitions。這個設計用於大量生成可驗證的 theorem-proof data，證明「完整 proof script」並不是唯一合理的資料單位。

其最簡單形式可寫成：

$$
\mathcal G_{state}
=
(V_s,E_t),
$$

其中：

$$
V_s=\{s_0,s_1,\ldots\},
$$

$$
E_t\subseteq V_s\times\mathcal A\times V_s.
$$

這為本文的 $\Omega^{(0)}$ 與 $\Omega^{(1)}$ 提供了直接工程類比。

## 2.3 LeanProgress：從局部 tactic 轉向全局 trajectory

LeanProgress 的核心動機是：只預測下一步 tactic，不足以知道目前是否真的接近完成。其 progress predictor 估計從某 proof state 到完成還需要多少步。

可抽象為：

$$
P_{rem}(s_t)
\approx
\operatorname{dist}(s_t,S_{done}).
$$

這裡已經出現一個重要轉變：

$$
\text{local action quality}
$$

與：

$$
\text{global trajectory position}
$$

不是同一個量。

對長程研究而言也一樣。一篇局部看似新的論文，可能只是在舊 route 上向前或向後移動；真正的 novelty 要看它在整體 trajectory graph 中的位置。

## 2.4 AlphaProof 與 tree search

2025 年公開於 Nature 的 AlphaProof 將 Lean proof state、policy/value-like guidance 與專門 tree search 結合，顯示 proof solving 可以被視為對巨大狀態樹的策略性探索。

但 tree search 的成功也提醒我們：

$$
\text{visit count}
\neq
\text{semantic coverage}.
$$

同一語義區域可以因 representation、branching 與 tactic surface 被多次造訪。

因此本文不直接把 search tree depth 當高階採樣階數。

## 2.5 Goedel-Architect、LEAP 與 blueprint graph

2026 年的 Goedel-Architect 把大型 theorem proof 先表成 definition / lemma dependency blueprint，再平行關閉 open lemma nodes；若失敗，則用 failure 反向修改 blueprint。

可抽象為：

$$
\mathcal B
=
(V_L,E_D),
$$

其中：

$$
V_L
=
\{\text{definitions and lemmas}\},
$$

$$
E_D
=
\{\text{declared dependencies}\}.
$$

LEAP 同樣以 hierarchical decomposition 與 AND-OR DAG 維持證明計畫，而 LeanMarathon 則把 evolving blueprint 當成長程 multi-agent formalization 的共享系統紀錄。

這幾個系統共同指出：

$$
\boxed{
\text{Proof solving itself already needs graph-level memory.}
}
$$

本文進一步問：

$$
\boxed{
\text{Long-horizon research needs graph-of-graphs memory嗎？}
}
$$

答案至少在操作上是肯定的。

## 2.6 Chain of States：中介狀態是可生成的研究物件

2025 年 Chain-of-States 工作把 informal reasoning 分解成一系列中介 formal states，再生成 adjacent transitions 所需的 tactics。這說明 proof trajectory 不是只有 solver 內部才存在，它也可以作為跨 representation 的明確中介語言。

本文將這個觀念一般化：

> 不只 theorem proof 可以被拆成 states；長程 research program 也可以被拆成 research states，而 research transitions 本身可以成為下一階研究對象。

---

# 3. 型別先行：避免把所有「階」混成一團

## 3.1 Order 不是形容詞，而是研究對象的型別

本文定義一個 sampling order map：

$$
\operatorname{ord}:\mathcal X\to\mathbb N_0.
$$

其中：

$$
\operatorname{ord}(x)=k
$$

表示研究產物 $x$ 的主要新資訊位於 $k$ 階 proof-space object。

這不是說 $x$ 只能包含一種階數，而是說其 novelty claim 的主型別是什麼。

## 3.2 一個最重要的反例

若某篇 PDE 論文研究：

$$
\partial_t^2 u,
$$

或者寫出：

$$
\text{second-order correction},
$$

它完全可能仍然只是一階 proof-state sampling。

因此：

$$
\boxed{
\text{Mathematical order}
\neq
\text{proof-space sampling order}.
}
$$

同理：

$$
\text{higher-order logic}
$$

不自動等於本文的 higher-order proof-space sampling。

## 3.3 型別錯置會製造假的高階訊號

假設 corpus 中有 100 篇文章含有字串：

`second-order`。

直接計數只能得到：

$$
N_{lex}(`second-order`)=100.
$$

它不能推出：

$$
N_{proof}^{(2)}=100.
$$

本文因此要求：高階判定必須使用結構證據，而不是單字證據。

---

# 4. 零階空間：研究狀態與候選數學物件

## 4.1 定義零階 proof-space object

對問題 $Q$ 與搜尋制度 $R$，令：

$$
\Omega_R^{(0)}(Q)
$$

表示可被系統辨識、保存與比較的基礎 research-state objects。

典型元素包括：

- theorem candidate；
- lemma candidate；
- assumption set；
- counterexample candidate；
- invariant；
- estimate；
- normal form；
- representation；
- obstruction state；
- formal proof state；
- verified partial result。

## 4.2 零階不是「低級」

 $0$ 階只是 base type。

一個極深的定理本身仍然可以是：

$$
x\in\Omega^{(0)}.
$$

高階不是價值排序。

因此本文拒絕：

$$
\operatorname{ord}(x)>\operatorname{ord}(y)
\Rightarrow
\operatorname{Value}(x)>\operatorname{Value}(y).
$$

## 4.3 零階 novelty

經過 LSI-PSD-03 的 quotient 後，令 $[x]_0$ 表示零階語義等價類。

第 $N$ 輪的 audited zero-order novelty 可寫成：

$$
\nu_0(N)
=
\frac{
\#\{\text{new audited }[x]_0\text{ introduced near }N\}
}{
\#\{\text{audited zero-order candidates near }N\}
}.
$$

若：

$$
\nu_0(N)\to0,
$$

只能說零階新等價類的邊際產出下降。

不能說：

$$
\Omega^{(0)}
\text{ 已被耗盡}.
$$

---

# 5. 一階空間：從「有什麼」轉向「怎麼走」

## 5.1 Proof move 作為物件

若：

$$
x,y\in\Omega^{(0)},
$$

且某可審計操作 $T$ 使：

$$
T:x\mapsto y,
$$

則可把 $T$ 視為一階物件。

令：

$$
\Omega_R^{(1)}(Q)
=
\{T\mid T:x\to y,\ x,y\in\Omega_R^{(0)}(Q)\}.
$$

## 5.2 一階物件不只 tactic

在長程數學研究中， $T$ 可以是：

- introduce auxiliary quantity；
- switch representation；
- pass to a blow-up sequence；
- normalize；
- rescale；
- take a compactness limit；
- derive contradiction；
- localize；
- integrate by parts；
- apply monotonicity；
- pass from local to global criterion；
- compile informal statement into formal lemma；
- add or remove an assumption；
- transfer a lemma to a neighboring PDE；
- route around an obstruction。

## 5.3 Route 是 transition 的組合

一條 proof route：

$$
r
=
T_m\circ\cdots\circ T_2\circ T_1.
$$

其起點與終點為：

$$
r:x_0\to x_m.
$$

route identity 不能只由終點決定。

可能有：

$$
r_a(x)=r_b(x)=y,
$$

但：

$$
r_a\not\sim_{route}r_b.
$$

因為兩條路使用不同 assumptions、不同 intermediate lemmas 或不同 dependence structure。

## 5.4 何時稱為一階 novelty

如果一篇研究稿只產生一個新 theorem statement，通常主要是零階 novelty。

如果它的核心是：

> 已知 $x$ 與 $y$，本文建立一種以前沒有的可驗證轉換 $T:x\to y$。

則其主要 novelty 可標記為：

$$
\operatorname{ord}=1.
$$

---

# 6. 二階空間：研究不同 proof routes 之間的關係

## 6.1 二階不是再走一次路

如果系統只是：

$$
x\xrightarrow{T}y\xrightarrow{U}z,
$$

這仍然可以只是較長的一階 route。

二階的關鍵不是 composition length，而是研究：

$$
T\quad\text{和}\quad U
$$

之間的關係。

## 6.2 二階關係的基本類型

令：

$$
T_a,T_b\in\Omega^{(1)}.
$$

二階物件可以包括：

### 6.2.1 Route equivalence

$$
T_a\sim_{route}T_b.
$$

表示兩者在指定 quotient 下共享同一 proof skeleton。

### 6.2.2 Route dominance

$$
T_a\preceq T_b.
$$

表示 $T_a$ 的成功條件、成本或 assumption demand 在某意義上優於 $T_b$。

### 6.2.3 Route incompatibility

$$
T_a\perp_R T_b.
$$

表示兩條路需要互相衝突的 assumptions、normalizations 或 representations。

### 6.2.4 Confluence

若：

$$
T_a(x_a)\to O,
$$

$$
T_b(x_b)\to O,
$$

即使 $x_a\neq x_b$，若最終都導向同一 canonical obstruction $O$，則形成 confluence relation。

### 6.2.5 Mutual compensation

某些方法單獨不足，但：

$$
T_a\oplus T_b
$$

能封閉彼此的 error term。

這也是二階關係。

## 6.3 定義二階空間

本文以：

$$
\Omega_R^{(2)}(Q)
=
\mathcal R_1(\Omega_R^{(1)}(Q))
$$

表示一階路由上的可審計關係族。

 $\mathcal R_1$ 不是 powerset 的同義詞，而是觀測站實際允許保存的 typed relations。

---

# 7. 三階空間：關係本身開始形成結構

## 7.1 從多條 confluence 到 confluence family

假設已經辨識：

$$
C_1:
T_1,T_2,T_3\to O_1,
$$

$$
C_2:
T_4,T_5\to O_2,
$$

$$
C_3:
T_6,T_7,T_8\to O_1.
$$

現在研究者發現：

$$
C_1\sim C_3.
$$

這時研究對象已不是單條 route，也不是單次 confluence，而是 confluence relations 之間的關係。

這就是三階的典型形式。

## 7.2 Feedback 作為三階訊號

若某個二階結論：

$$
R(T_a,T_b)
$$

被送回搜尋系統，改變下一輪允許的 transitions：

$$
\Pi_{N+1}
=
\Phi(\Pi_N,R(T_a,T_b)),
$$

其中 $\Pi_N$ 是當前 route policy，則形成：

$$
\text{relation}
\to
\text{search-policy update}.
$$

若後續再研究這個 update 是否產生新的 confluence 或 avoidance pattern，便出現明顯的 higher-order feedback。

## 7.3 三階空間

可寫成：

$$
\Omega_R^{(3)}(Q)
=
\mathcal R_2(\Omega_R^{(2)}(Q)).
$$

典型元素包括：

- confluence-of-confluences；
- relation-family equivalence；
- route-class feedback；
- no-go inheritance between method families；
- family-level re-entry；
- repeated obstruction migration pattern。

---

# 8. 一般 $k$ 階空間：必須是 typed recursion，而不是無限制元語言

## 8.1 遞迴定義

本文不嘗試聲稱存在唯一自然的高階 proof-space hierarchy。

操作上定義：

$$
\Omega_R^{(k+1)}(Q)
=
\mathcal F_k(\Omega_R^{(k)}(Q)),
$$

其中：

$$
\mathcal F_k
$$

是一組被 observatory 明確註冊的 higher-order constructors。

## 8.2 Constructor registry

例如：

$$
\mathcal F_k
=
\{
\operatorname{Relate},
\operatorname{Compose},
\operatorname{Quotient},
\operatorname{Converge},
\operatorname{Confluence},
\operatorname{Feedback},
\operatorname{Reenter},
\operatorname{InheritNoGo}
\}.
$$

只有通過這些 typed constructors 產生、並保留 provenance 的物件，才有資格被標為更高階。

## 8.3 為什麼不能讓階數無限制自由膨脹

如果只要說一句：

> 我在思考「我在思考 proof route」

就把階數加一，則：

$$
\operatorname{ord}
$$

會變成修辭遊戲。

因此本文要求：

$$
\boxed{
\text{Higher order requires a new typed relational object with auditable inputs and outputs.}
}
$$

## 8.4 Order ceiling 不是數學天花板

實際 observatory 可能只維護：

$$
k\leq K_{obs},
$$

例如：

$$
K_{obs}=3.
$$

更高階全部先標：

$$
T_X.
$$

這只是資料工程決策，不代表真實研究只有三階。

---

# 9. 四層操作標記： $T_1,T_2,T_3,T_X$

## 9.1 為什麼不用直接把所有 artifact 精確標 $k$

現實 corpus 很髒。

一篇 paper 可能同時包含：

- 新 lemma；
- 舊 route 回訪；
- route comparison；
- family-level no-go。

因此，對 legacy corpus 強行給單一精確階數會過度自信。

本文建議第一版 observatory 採四層 tier：

$$
T_1,
T_2,
T_3,
T_X.
$$

## 9.2 $T_1$：狀態或新路由採樣

判準包括：

- 新 zero-order semantic class；
- 新 proof move；
- 新 route family；
- 未有明確 route-relation novelty。

## 9.3 $T_2$：回訪、transition comparison 或同一 obstruction 的再採樣

需要至少一項結構證據：

- explicit revisit；
- same canonical obstruction under a new route；
- route-to-route comparison；
- reusable transition relation；
- dependency transfer between route families。

## 9.4 $T_3$：relation/confluence/feedback

需要研究對象本身已是 route relations，例如：

- obstruction confluence；
- coupled confluence；
- confluence feedback；
- no-go inheritance between relation families；
- relation-induced policy update。

## 9.5 $T_X$：高階候選，不假裝精確

用於：

- all-order family analysis；
- higher-order recurrence；
- repeated feedback-of-feedback；
- method-family closure；
- evidence 顯示階數超過 observatory 現有 schema。

 $T_X$ 不是「無限階」。

它只表示：

$$
\operatorname{ord}(x)>K_{obs}
$$

或：

$$
\operatorname{ord}(x)
\text{ 尚無法可靠解析}.
$$

---

# 10. Order-conditioned novelty：為什麼一階飽和後仍可能有新資訊

## 10.1 單一 novelty 指標會混掉相變

若只定義：

$$
\nu(N),
$$

則無法分辨：

- 新 theorem 下降；
- 新 routes 下降；
- 新 route relations 上升；
- 新 obstruction families 上升。

因此本文改用：

$$
\boldsymbol\nu(N)
=
(\nu_0(N),\nu_1(N),\ldots,\nu_K(N)).
$$

## 10.2 一個典型的高階相變

早期：

$$
\nu_0\gg0,
\qquad
\nu_1\gg0.
$$

中期可能變成：

$$
\nu_0\downarrow,
\qquad
\nu_1>0,
\qquad
\nu_2\uparrow.
$$

再後期：

$$
\nu_0\approx0,
\qquad
\nu_1\approx0,
\qquad
\nu_2>0.
$$

這表示不是「研究死了」，而是 novelty 從 object level 移到 relational level。

## 10.3 Order-conditioned novelty 定義

令第 $k$ 階經 audited quotient 後的等價類集合為：

$$
\mathcal C_k(N).
$$

定義窗口 $W$ 內的新類率：

$$
\nu_k^{(W)}(N)
=
\frac{
|\mathcal C_k(N-W+1:N)\setminus\mathcal C_k(1:N-W)|
}{
\max(1,|\mathcal C_k(N-W+1:N)|)
}.
$$

這個量仍受抽取品質影響，所以必須附：

$$
\operatorname{Conf}_k(N).
$$

## 10.4 不能把低 novelty 自動解釋成 saturation

低：

$$
\nu_k
$$

可能來自：

- extraction model 變差；
- corpus mode 變窄；
- prompt 固化；
- verifier 過度嚴格；
- representation collapse；
- 真正局部飽和。

因此 saturation 需要多指標共同支持。

---

# 11. Order-conditioned coverage：邏輯空間積分的高階版本

## 11.1 從單一積分到積分向量

LSI-PSD-02 定義 proof-space coverage 的理想形式。

本文把它分階：

$$
I_k(N)
=
\int_{\Omega^{(k)}/\sim_k}
c_{k,N}([\xi])\,d\mu_k([\xi]).
$$

因此：

$$
\mathbf I(N)
=
(I_0(N),I_1(N),\ldots,I_K(N)).
$$

## 11.2 不同階的 measure 不必同質

 $\mu_0$ 可以關注 theorem/lemma semantic classes。

 $\mu_1$ 可以關注 route families。

 $\mu_2$ 可以關注 confluence、dominance、incompatibility 等 relation classes。

所以不能把：

$$
I_0+I_1+I_2
$$

當成天然有意義的純量。

需要權重：

$$
I_{agg}(N)
=
\sum_{k=0}^{K}
\lambda_k I_k(N),
$$

且：

$$
\lambda_k
$$

必須由研究目的明示。

## 11.3 Coverage 的真正意義是「已審計可區分結構」

本文再次強調：

$$
I_k
$$

不是「真實數學空間百分之幾已經走完」。

它是：

> 在目前 observatory schema、quotient、evidence rule 與 sampling regime 下，被辨識與審計的第 $k$ 階結構覆蓋代理量。

---

# 12. Confluence：高階採樣最重要的可測訊號之一

## 12.1 定義 canonical obstruction

令：

$$
O\in\mathcal O
$$

表示經 LSI-PSD-03 商化後的 obstruction class。

例如多篇文章雖使用不同語言，但若都可審計地歸結為：

> 某 critical norm 無法被現有 estimate 關閉，

則可候選地歸入同一 $[O]$。

## 12.2 Confluence set

對 obstruction $O$，定義：

$$
\operatorname{In}(O)
=
\{r\in\mathcal R_1:r\to O\}.
$$

confluence degree：

$$
C_{deg}(O)
=
|\operatorname{In}(O)/\sim_{route}|.
$$

它計算的不是文章數，而是**不同 route classes** 有多少條匯入同一 obstruction。

## 12.3 Weighted confluence

若不同 route 的獨立性不同，可定義：

$$
C_w(O)
=
\sum_{[r]\in\operatorname{In}(O)/\sim_{route}}
w_{ind}([r]).
$$

其中：

$$
0\leq w_{ind}\leq1.
$$

## 12.4 高 confluence 的解釋

高：

$$
C_w(O)
$$

可能表示：

1. $O$ 是真正深層的 structural obstruction；
2. observatory quotient 太粗，把不同障礙錯合併；
3. 所有 route 共享隱藏 assumptions；
4. search regime 有共同 blind spot；
5. problem representation 把不同路徑投影到相同表面失敗。

所以 confluence 是診斷訊號，不是判決。

---

# 13. Re-entry：被排除的路徑為什麼還會再次出現

## 13.1 重複不一定是退化

假設 route family $R_a$ 在第 $n$ 輪被判定：

$$
R_a\to\text{insufficient under }A.
$$

到第 $m>n$ 輪，新的 assumption set $A'$ 出現：

$$
A'\neq A.
$$

若 $R_a$ 在 $A'$ 下重新進場，這不一定是「AI 忘了以前失敗」。

## 13.2 定義 re-entry

令：

$$
\operatorname{Exit}(R_a,n,A)=1
$$

表示在 regime $A$ 下被排除。

若之後：

$$
\operatorname{Enter}(R_a,m,A')=1,
$$

且存在可審計 novelty：

$$
A'\not\sim A,
$$

則稱為 legitimate re-entry。

## 13.3 Re-entry depth

若同一路由族多次：

$$
\text{enter}
\to
\text{fail}
\to
\text{reformulate}
\to
\text{re-enter},
$$

可定義：

$$
D_{re}(R_a)
=
\#\{\text{audited legitimate re-entries of }R_a\}.
$$

高 $D_{re}$ 是高階研究的重要訊號，因為研究已經不只比較 route，而在研究 route 對 context 的依賴。

---

# 14. Feedback depth：研究結果開始改變研究制度

## 14.1 普通研究輸出

一般：

$$
\text{search}
\to
\text{result}.
$$

## 14.2 反身研究輸出

高階 proof-space observatory 會出現：

$$
\text{search}
\to
\text{relation discovery}
\to
\text{policy update}
\to
\text{new search}.
$$

令 search policy 為：

$$
\Pi_N.
$$

如果第 $N$ 輪的 relation object $R_N$ 使：

$$
\Pi_{N+1}
=
\Psi(\Pi_N,R_N),
$$

則形成第一層 feedback。

## 14.3 二次 feedback

若系統又研究：

$$
\Psi
$$

本身造成的 bias、blind spot 或 route-collapse，並再更新：

$$
\Psi_{N+1}
=
\Theta(\Psi_N,F_N),
$$

則 feedback depth 再增加。

## 14.4 定義 feedback depth

操作上：

$$
D_{fb}
=
\max\{d:\text{存在 }d\text{ 層可追溯的 relation-to-policy feedback chain}\}.
$$

這個量與「meta-level 越高越真」無關。

它只描述研究制度的反身深度。

---

# 15. Route-family entropy：高階採樣不能只看階數

## 15.1 一萬輪全在同一路線上沒有多樣性

假設 $N$ 個 artifacts 全部落入同一 route family：

$$
R_1.
$$

即使有大量細節變化，其 family diversity 仍低。

## 15.2 定義 route-family entropy

若第 $k$ 階有 route/relation families：

$$
\mathcal F_k
=
\{F_1,\ldots,F_m\},
$$

其樣本比例：

$$
p_i
=
\frac{n_i}{\sum_j n_j}.
$$

定義：

$$
H_k^{route}
=
-\sum_{i=1}^{m}p_i\log p_i.
$$

normalized entropy：

$$
\widehat H_k^{route}
=
\frac{H_k^{route}}{\log m}.
$$

## 15.3 高階與高 entropy 是不同軸

可能：

$$
\operatorname{ord}\uparrow,
\qquad
H^{route}\downarrow.
$$

表示系統在很深地研究同一小群路線。

也可能：

$$
\operatorname{ord}\approx1,
\qquad
H^{route}\uparrow,
$$

表示仍在廣泛探索很多新 route。

因此需要至少二維描述：

$$
(\operatorname{order},\operatorname{diversity}).
$$

---

# 16. Audited yield：高階研究是否真的產生可靠資訊

## 16.1 不能只因為 higher-order 很酷就加分

高階 meta-analysis 很容易變成：

- 漂亮但不可驗證的分類；
- LLM 自己替自己的路線找共同點；
- 以修辭代替 theorem relation；
- 把共同用詞誤判成共同 obstruction。

所以必須定義 audited yield。

## 16.2 Order-conditioned audited yield

令：

$$
A_k(N)
$$

為第 $N$ 輪附近生成的 $k$ 階候選數。

令：

$$
V_k(N)
$$

為其中被獨立 verifier、形式檢查、雙路徑審計或可重現證據支持的新等價類數。

定義：

$$
\rho_k(N)
=
\frac{V_k(N)}{\max(1,A_k(N))}.
$$

## 16.3 高階幻覺的警報

若：

$$
A_k\uparrow
$$

但：

$$
\rho_k\to0,
$$

則表示系統可能正在生成大量 meta-language，而不是可靠 higher-order knowledge。

這是 observatory 必須特別防守的模式。

---

# 17. $K$ 階局部飽和

## 17.1 為什麼只說「飽和」太粗

一個 proof basin $B$ 中可能：

$$
\nu_0^B\approx0,
$$

但：

$$
\nu_2^B>0.
$$

這表示 base objects 已經很少新增，但 route relations 仍在快速生長。

## 17.2 定義候選

令：

$$
B\subseteq\Omega_R(Q)
$$

為由 representation、method family、assumption regime 或 obstruction family 定義的局部 basin。

若對：

$$
0\leq k\leq K,
$$

在長窗口 $W$ 中同時滿足：

$$
\nu_k^B(N)<\epsilon_k,
$$

$$
\rho_k^B(N)<\eta_k,
$$

$$
\Delta I_k^B(N)<\delta_k,
$$

且 route-family entropy 沒有出現新的顯著上升，則可標：

$$
\operatorname{Sat}_K(B;N,W)=1.
$$

## 17.3 這仍然只是 operational saturation

即使：

$$
\operatorname{Sat}_K(B)=1,
$$

也不推出：

$$
B
\text{ 在真實數學空間中已完全被枚舉}.
$$

更不推出：

$$
Q
\text{ 不可證或問錯了}.
$$

本文把這一點稱為：

$$
\boxed{
\text{Order-Saturation Non-Conclusion Rule}.
}
$$

它是 LSI-PSD-01 非結論原則的高階版本。

---

# 18. 高階採樣與局部 proof basin

## 18.1 Basin 不是地理比喻，而是搜尋約束集合

可以由下列條件定義 basin：

$$
B
=
B(\mathcal L,\mathcal M,\mathcal A,\mathcal O),
$$

其中：

- $\mathcal L$：representation language；
- $\mathcal M$：method family；
- $\mathcal A$：assumption regime；
- $\mathcal O$：target obstruction family。

## 18.2 同一問題可以同時存在不同 sampling order

例如：

$$
B_1:
\nu_0\approx0,
\nu_1\approx0,
\nu_2>0,
$$

而：

$$
B_2:
\nu_0>0.
$$

所以：

$$
\boxed{
\text{Sampling order is local to a basin, not a global scalar of the problem.}
}
$$

## 18.3 這解釋 NS corpus 的一個表面矛盾

在初步 observatory 中，某些 NS 支線已出現 confluence、feedback、all-order escalation；同時固定窗口 novelty 並沒有顯示整個 corpus 全域 collapse。

兩者並不矛盾。

可能只是：

$$
B_{X72}
$$

已進入較高階重訪，而：

$$
B_{other}
$$

仍然在產生低階新 route。

---

# 19. NS-203 corpus：如何重新解讀第一版 tier

## 19.1 資料地位

既有 NS Proof-Space Sampling Observatory 對保守篩選後的 corpus 得到：

$$
N_{NS}=203
$$

個 paper-like artifacts。

第一版 heuristic tier 為：

$$
T_1=84,
$$

$$
T_2=107,
$$

$$
T_3=10,
$$

$$
T_X=2.
$$

本文把這些數字視為：

$$
\boxed{
\text{instrument-development observations, not theorem-level facts.}
}
$$

## 19.2 為什麼 $T_2$ 很大並不奇怪

長程 corpus 中大量工作會呈現：

- revisit；
- reuse；
- obstruction recurrence；
- route transfer；
- second pass audit。

只要分類器偏向「看到 recurrence 就算二階」，就可能高估 $T_2$。

所以 v2 observatory 必須把 $T_2$ 再拆：

$$
T_{2a}=\text{same-state revisit},
$$

$$
T_{2b}=\text{same-route revisit},
$$

$$
T_{2c}=\text{route comparison},
$$

$$
T_{2d}=\text{cross-route obstruction recurrence}.
$$

其中真正強的二階證據主要是後兩者。

## 19.3 X72 的 confluence chain

初步 corpus 中，X72 後期直接使用 obstruction confluence、coupled confluence、confluence feedback 等研究語言。

這些詞本身仍不是證明。

但若對應實際 dependency graph 顯示：

$$
\{R_a,R_b,R_c\}
\to
O,
$$

之後又研究：

$$
\operatorname{Rel}(R_a,R_b,R_c),
$$

再讓 relation 結果改變下一輪 route policy，則這是乾淨的 $T_3$ evidence。

## 19.4 All-order 不等於無限階 proof-space

某篇文章若研究：

$$
\text{all-order escalation of a mathematical estimate family},
$$

不能直接說：

$$
\operatorname{ord}=\infty.
$$

只有當它對「method-family escalation 本身」建立可審計的 relation-level no-go，才可作 $T_X$ 候選。

這是本文對第一版 observatory 最重要的修正之一。

---

# 20. 一個合成例子：從零階到三階

## 20.1 零階

假設研究問題為：

$$
Q:
\text{證明某能量 }E(t)\text{ 在指定條件下有界}.
$$

得到新估計：

$$
E(t)
\leq
E(0)+C\int_0^t F(s)\,ds.
$$

這是零階新物件。

## 20.2 一階

研究者發現可透過兩條方法：

$$
R_A:
E\to\text{localization}\to\text{bootstrap},
$$

$$
R_B:
E\to\text{frequency split}\to\text{bootstrap}.
$$

這是 route-level，一階物件。

## 20.3 二階

兩條路都失敗於：

$$
O:
\text{critical remainder cannot be absorbed}.
$$

並證明這不是字面巧合，而是在 quotient 後共享同一 scaling defect。

此時：

$$
R_A\to O,
$$

$$
R_B\to O
$$

形成二階 confluence。

## 20.4 三階

又發現第三、第四種完全不同方法也匯入 $O$，於是研究者提出：

$$
C_O
=
\operatorname{ConfluenceFamily}(O).
$$

接著把 $C_O$ 用來禁止下一輪再走所有保留同 scaling defect 的 routes。

搜尋 policy 更新：

$$
\Pi_{N+1}
=
\Pi_N
\setminus
\{R:\operatorname{Defect}(R)=\operatorname{Defect}(O)\}.
$$

這就是三階 relation-to-policy feedback。

---

# 21. 高階 no-go：失敗也可以有階數

## 21.1 零階 no-go

$$
L
\text{ 為假或不足}.
$$

只排除單一候選。

## 21.2 一階 no-go

$$
R
\text{ 在條件 }A\text{ 下不能閉合}.
$$

排除一條 route。

## 21.3 二階 no-go

若證明一整類 routes：

$$
\mathcal R_D
=
\{R:\operatorname{Defect}(R)=D\}
$$

都共享同一 fatal obstruction，則：

$$
\forall R\in\mathcal R_D,
\qquad
R\to O_D.
$$

這是 method-family no-go。

## 21.4 更高階 no-go

若即使對：

$$
\mathcal R_D
$$

進行固定類型的 correction family：

$$
C^{(1)},C^{(2)},\ldots,C^{(m)},
$$

都只能把 obstruction 推到同一 quotient class，則可能形成更高階 escalation no-go。

但此類聲稱必須有形式證據，不能只靠「試很多次都不行」。

---

# 22. 高階採樣與方法族的「家譜」

## 22.1 Route 不應只存 flat label

假設：

$$
R_{A.1},R_{A.2},R_{A.3}
$$

都是從 parent method $R_A$ 變形而來。

如果把它們當三條完全獨立 route，會高估 confluence independence。

## 22.2 Method genealogy

定義 genealogy graph：

$$
\mathcal G_{gen}
=
(V_R,E_{parent}).
$$

若：

$$
R_{A.2}
=
\operatorname{Modify}(R_A,\theta_2),
$$

則有：

$$
R_A\to R_{A.2}.
$$

## 22.3 Independent confluence 應折扣共同祖先

可定義 route independence：

$$
w_{ind}(R_i,R_j)
=
1-\frac{
\operatorname{SharedAncestorMass}(R_i,R_j)
}{
\operatorname{TotalAncestorMass}(R_i,R_j)
}.
$$

因此三條 sibling routes 同時撞牆，不應等價於三條跨方法族 routes 同時撞牆。

這對 NS 這種長支線研究尤其重要。

---

# 23. 研究路由的同構與 representation sensitivity

## 23.1 數學等價不代表搜尋等價

LSI-PSD-03 已建立：

$$
\text{Mathematical redundancy}
\not\Rightarrow
\text{search-dynamical redundancy}.
$$

高階採樣必須繼承這一點。

如果兩條 routes 在命題層等價：

$$
R_a\sim_{math}R_b,
$$

但 AI prover 對它們成功率差異很大：

$$
P_{succ}(R_a)\neq P_{succ}(R_b),
$$

則在 search-space higher-order analysis 中不能完全合併。

## 23.2 雙身份資料結構

每條 route 建議同時保存：

$$
ID_{math}(R),
$$

$$
ID_{search}(R).
$$

前者用於 theorem-level quotient。

後者保留：

- syntax；
- library context；
- state encoding；
- tactic history；
- prompt lineage；
- prover version；
- model version；
- budget。

## 23.3 高階 relation 也要雙層

因此：

$$
\Omega^{(2)}_{math}
$$

與：

$$
\Omega^{(2)}_{search}
$$

也不應被混成一個空間。

同一 confluence 在數學上可能是一個 obstruction，在 search dynamics 中則可能由完全不同的 failure mechanisms 造成。

---

# 24. Graph-of-graphs：高階 observatory 的自然資料模型

## 24.1 Layer 0：semantic object graph

$$
G_0
=
(V_0,E_0).
$$

節點：

- claims；
- assumptions；
- lemmas；
- obstructions；
- statuses。

## 24.2 Layer 1：route graph

$$
G_1
=
(V_1,E_1).
$$

節點可以是 route segments，邊表示：

- extension；
- refinement；
- parent-child；
- reuse；
- re-entry。

## 24.3 Layer 2：relation graph

$$
G_2
=
(V_2,E_2).
$$

節點本身是：

$$
\text{relations over }G_1.
$$

例如：

- confluence object；
- dominance object；
- incompatibility object；
- no-go family；
- compensation pair。

## 24.4 Layer 3：policy-feedback graph

$$
G_3
$$

記錄：

$$
G_2
\to
\Pi
\to
G_1'
$$

也就是 relation-level knowledge 如何改變後續 route generation。

## 24.5 為什麼單一 property graph 仍然可以實作

工程上不一定真的需要四個資料庫。

可以用 typed hypergraph：

$$
\mathcal H
=
(V,E,\tau_V,\tau_E),
$$

其中：

$$
\tau_V(v)
\in
\{state,route,relation,policy,obstruction,claim\}.
$$

這樣較容易在 Neo4j、PostgreSQL graph extension 或自製 JSONL pipeline 中落地。

---

# 25. 建議的 canonical record schema

每個高階 observation 至少需要：

```yaml
observation_id: LSI-HO-000001
problem_id: NS-3D-global-regularity
artifact_id: ...
order_tier: T3
order_confidence: 0.82
object_type: confluence
inputs:
  - route_id: R-X72-18-A
  - route_id: R-X72-18-B
output:
  obstruction_id: O-CANON-0042
relation_type: converges_to_same_obstruction
evidence:
  - dependency_trace
  - matched_assumption_signature
  - normalized_obstruction_signature
verifier_status: partially_audited
provenance:
  source_file: ...
  source_span: ...
  extractor_version: ...
  reviewer: ...
```

這個 schema 的重點不是 YAML。

重點是：

$$
\boxed{
\text{order claim itself must carry evidence and provenance.}
}
$$

---

# 26. 高階關係的可信度

## 26.1 Relation confidence

對 relation $r$：

$$
\operatorname{Conf}(r)
=
f(E_{formal},E_{struct},E_{semantic},E_{indep}).
$$

其中：

- $E_{formal}$：形式互推／kernel evidence；
- $E_{struct}$：dependency / graph structure；
- $E_{semantic}$：語義審計；
- $E_{indep}$：獨立 evaluator agreement。

## 26.2 三值而非強迫二值

延續 LSI-PSD-03：

$$
R_{ij}
\in
\{
\text{supported},
\text{rejected},
\text{undetermined}
\}.
$$

對高階 relation 尤其重要。

因為：

$$
\text{undetermined}
$$

比錯誤地合併兩條深層 route 更安全。

---

# 27. 防止「AI 自己替自己證明高階」

## 27.1 Self-confirming relation problem

若同一模型：

1. 生成兩篇 proof attempts；
2. 再判斷兩篇其實匯流；
3. 再宣稱匯流是一個深層 obstruction；

則存在循環：

$$
M
\to
G
\to
M(G)
\to
\text{claim about }G.
$$

這不能被當成獨立證據。

## 27.2 最低限度的解耦

建議至少分離：

$$
M_{gen},
$$

$$
M_{rel},
$$

$$
V_{formal},
$$

$$
A_{human/independent}.
$$

其中：

- $M_{gen}$ 生成研究；
- $M_{rel}$ 抽取高階關係；
- $V_{formal}$ 驗證可形式化部分；
- 獨立 audit 處理不可形式化語義。

## 27.3 模型不同不等於證據獨立

兩個 LLM 即使品牌不同，也可能共享：

- 訓練資料；
- proof conventions；
- benchmark bias；
- common mathematical priors。

因此 independent weight 仍應折扣。

---

# 28. 與 AND-OR graph 的差異

## 28.1 AND-OR graph 解的是「如何完成這個 proof」

形式 proof search 中，AND node / OR node 常用於表示：

- 所有子目標都要完成；
- 多個候選 tactic 只需一條成功。

其主要目標仍是：

$$
\exists\text{ successful proof path}.
$$

## 28.2 高階 proof-space observatory 問的是另一件事

本文更關心：

$$
\text{哪些 path families 被反覆嘗試？}
$$

$$
\text{哪些 path families 共享 obstruction？}
$$

$$
\text{哪些 failure relations 改變了後續搜尋？}
$$

因此它不是替代 theorem prover，而是 theorem-research layer。

---

# 29. 與 reinforcement learning state hierarchy 的差異

## 29.1 可以借用 MDP 語言，但不能偷換

若：

$$
\mathcal MDP
=(S,A,P,R,\gamma),
$$

proof state 與 tactic 很容易映射到：

$$
S,A.
$$

但本文的：

$$
\Omega^{(2)},\Omega^{(3)}
$$

不只是 belief state 或 option hierarchy。

它們是**研究關係本身的知識物件**。

## 29.2 高階關係可以跨 episode 存活

一個 obstruction confluence：

$$
O_c
$$

可以跨越上百次獨立 proof episodes 保留。

所以它屬於：

$$
\text{persistent research memory},
$$

不是單 episode transition。

---

# 30. 高階採樣的三種「真正新增」

## 30.1 Relational novelty

發現兩條原本被視為無關的 routes 其實共享同一 structural core。

$$
R_a\sim_{new}R_b.
$$

## 30.2 Constraint novelty

發現一個 relation 能排除一整族 future routes。

$$
\mathcal R_{future}
\cap
\mathcal R_{forbidden}
=
\varnothing.
$$

## 30.3 Routing novelty

發現一個 higher-order signal 可以重排 search priority：

$$
\Pi_{N+1}
\neq
\Pi_N.
$$

這三種都可能在沒有新增 theorem statement 的情況下產生真實研究價值。

---

# 31. 什麼叫「X 階採樣」才不會變成誇張口號

## 31.1 最弱定義

如果 observatory 最多可靠區分到 $K$ 階，而某 artifact 有強證據顯示其核心 novelty 位於更高 relation level，則標：

$$
T_X.
$$

## 31.2 不允許的說法

不能因為：

- 文章很長；
- 提到 all-order；
- 提到 infinite hierarchy；
- 有很多 nested lemmas；
- AI 自稱 meta-meta reasoning；

就標成 $T_X$。

## 31.3 建議證據門檻

至少需要：

1. 其 input objects 已被審計為 relation-level objects；
2. 新結果是這些 relation objects 之間的新結構；
3. 該結構影響 route classification、no-go inheritance 或 search policy；
4. provenance 可追溯；
5. 至少一部分 relation 可被獨立重現。

---

# 32. 高階採樣與「研究越來越快」的可能性

## 32.1 為什麼 higher-order memory 可能加速研究

如果每次都從零開始：

$$
C_N
\sim
N\cdot C_{search}.
$$

但若已知：

$$
\mathcal R_{bad},
$$

下一輪可以直接剪枝：

$$
\Pi_{N+1}
\leftarrow
\Pi_N\setminus\mathcal R_{bad}.
$$

因此有效搜尋空間：

$$
|\Omega_{eff}(N+1)|
<
|\Omega_{eff}(N)|.
$$

## 32.2 這就是 proof-space compression 的工程版本

高階關係把大量歷史壓成少數可重用 constraint：

$$
\{R_1,\ldots,R_{1000}\}
\to
\{O_1,O_2,O_3\}.
$$

如果 $O_i$ 是可靠的，未來不需要重跑全部歷史。

這和 memoization 類似，但壓縮單位是 semantic relation，而不只是 exact state。

## 32.3 但錯誤高階壓縮會造成災難

若把其實可行的 route 誤歸入 no-go family：

$$
R^*\in\widehat{\mathcal R}_{bad},
$$

則系統可能永久剪掉真正的證明路徑。

因此 higher-order memory 越強，rollback 與 uncertainty tracking 越重要。

---

# 33. 反例：高階採樣不一定帶來收斂

## 33.1 Meta-explosion

系統可能不斷生成：

$$
\text{relations about relations about relations}
$$

而沒有任何 constraint power。

這形成：

$$
H_{meta}\uparrow,
\qquad
I_{useful}\approx0.
$$

## 33.2 Taxonomy trap

分類越來越細：

$$
T_1
\to
T_{1a},T_{1b},T_{1c},\ldots
$$

也不代表更接近真理。

分類只是工具。

## 33.3 Observer overfitting

observatory 可能根據目前 203 篇 NS corpus 建出非常細的 route ontology，卻只適用於這批文件。

一旦加入另一個 PDE corpus：

$$
\operatorname{Transfer}(Ontology_{NS})
\approx0.
$$

就表示它是 corpus-specific overfit。

---

# 34. 跨問題 transfer：高階知識最值得測的地方

## 34.1 一個 obstruction family 如果能跨問題重現，價值更高

假設 NS 中的 route relation：

$$
R_{NS}^{(2)}
$$

可以映射到 SQG、Boussinesq 或其他 evolution PDE：

$$
\Phi:
R_{NS}^{(2)}
\to
R_{PDE}^{(2)}.
$$

如果映射保留：

- assumption signature；
- scaling role；
- obstruction role；
- closure status；

那它可能是更一般的 proof asset。

## 34.2 Transfer score

定義：

$$
T_{score}(r)
=
\frac{
\#\text{domains where relation }r\text{ is independently useful}
}{
\#\text{domains tested}
}.
$$

高：

$$
T_{score}
$$

能幫助區分：

- corpus-specific recurrence；
- genuine methodological structure。

---

# 35. 與「真理—生成性反轉」的橋接

後續 LSI-PSD-07 將研究 truth、fidelity 與 generativity。

高階採樣在那裡扮演關鍵角色：

如果某個 parent framing 產生：

$$
\text{大量 zero-order descendants},
$$

接著又形成：

$$
\text{route families},
$$

再形成：

$$
\text{confluence families},
$$

那麼即使 parent problem 最後被重新定義，其研究史仍可能保留大量高階可遷移結構。

所以：

$$
\boxed{
\text{Generativity should be measured across sampling orders, not only by descendant count.}
}
$$

---

# 36. 與「生產性錯置」的橋接

假設兩個 definitions：

$$
D,
\qquad
D'.
$$

 $D'$ 可能不是更正確，但它打開更多 route variation：

$$
|\Omega_{D'}^{(1)}|
>
|\Omega_D^{(1)}|.
$$

更重要的是，也可能產生更多高階 relation：

$$
|\Omega_{D'}^{(2)}|
>
|\Omega_D^{(2)}|.
$$

這表示「生成性」不只是一階產量，而可能是：

$$
G(D)
=
\sum_{k=0}^{K}
\lambda_k
G_k(D).
$$

後續論文將檢驗這個方向。

---

# 37. 研究制度的階層化停止條件

## 37.1 一階停止條件

若：

$$
\nu_0\downarrow,
$$

系統不應立刻停止。

應檢查：

$$
\nu_1,\nu_2.
$$

## 37.2 關係層停止條件

若：

$$
\nu_0\approx0,
$$

$$
\nu_1\approx0,
$$

但：

$$
\nu_2>0,
$$

則應從「找新 route」切換為：

$$
\text{audit relation structure}.
$$

## 37.3 $K$ 階停止條件

若在 basin $B$：

$$
\forall k\leq K,
\qquad
\nu_k^B<\epsilon_k,
$$

並且：

$$
\rho_k^B<\eta_k,
$$

則 system action 不應是：

> 宣布問題錯了。

而應是：

$$
\boxed{
\text{Current basin / regime saturated; escalate representation audit.}
}
$$

---

# 38. 高階研究的 escalation ladder

當 basin 飽和，可依序嘗試：

## 38.1 Representation escalation

$$
\mathcal L
\to
\mathcal L'.
$$

## 38.2 Method escalation

$$
\mathcal M
\to
\mathcal M\cup\Delta\mathcal M.
$$

## 38.3 Assumption audit

$$
\mathcal A
\to
\operatorname{Audit}(\mathcal A).
$$

## 38.4 Problem reformulation

$$
Q
\to
Q'.
$$

## 38.5 Intelligence / compute escalation

$$
B
\to
B'.
$$

每次 escalation 都應開新 regime ID，避免把不同制度的 sampling history 混在一起。

---

# 39. High-order proof-space record 的最小可重建性

一個高階 conclusion 若要被未來 AI 使用，不能只保存一句：

> 這條路之前試過了，不行。

至少要保存：

$$
\mathcal H
=
(A,R,O,E,V,C),
$$

其中：

- $A$：assumptions；
- $R$：route signature；
- $O$：obstruction signature；
- $E$：evidence；
- $V$：verifier state；
- $C$：context / regime。

只有這樣未來才能判斷：

$$
\text{old no-go}
$$

是否真的適用於新情況。

---

# 40. 高階 observatory 的 v0.2 計算流程

建議 pipeline：

```text
Artifacts
  -> claim / lemma / assumption extraction
  -> semantic quotient
  -> route reconstruction
  -> route genealogy
  -> canonical obstruction mapping
  -> relation extraction
  -> confluence / dominance / incompatibility audit
  -> feedback / re-entry detection
  -> order-tier classification
  -> order-conditioned novelty and coverage
  -> local saturation report
```

其中任何一步的低信心都要向後傳遞 uncertainty。

---

# 41. 建議的核心指標總表

## 41.1 Base metrics

$$
N_0
=
\#\text{zero-order audited classes}.
$$

$$
N_1
=
\#\text{route classes}.
$$

$$
N_2
=
\#\text{route-relation classes}.
$$

## 41.2 Novelty vector

$$
\boldsymbol\nu(N)
=
(\nu_0,\nu_1,\ldots,\nu_K).
$$

## 41.3 Coverage vector

$$
\mathbf I(N)
=
(I_0,I_1,\ldots,I_K).
$$

## 41.4 Audited yield vector

$$
\boldsymbol\rho(N)
=
(\rho_0,\rho_1,\ldots,\rho_K).
$$

## 41.5 Confluence

$$
C_w(O).
$$

## 41.6 Re-entry depth

$$
D_{re}(R).
$$

## 41.7 Feedback depth

$$
D_{fb}.
$$

## 41.8 Route entropy

$$
\widehat H_k^{route}.
$$

## 41.9 Transfer score

$$
T_{score}(r).
$$

這些量共同描述研究，而不是讓單一「progress percentage」承擔全部意義。

---

# 42. 四個可檢驗預測

## 預測一：長程 corpus 會出現 sampling-order migration

若同一問題持續研究，應可觀察：

$$
\text{novelty mass}
$$

從：

$$
k=0,1
$$

逐漸部分轉移到：

$$
k=2,3.
$$

不是所有問題都必然發生，但在高密度長程研究中應可測。

## 預測二：高 confluence basin 的零階 novelty 會先下降

若某 basin 有高：

$$
C_w(O),
$$

其後續研究可能更容易形成 route relation 分析，而不是持續產生大量完全獨立 base objects。

## 預測三：有 persistent higher-order memory 的 agent 會少做無效重訪

比較：

$$
Agent_{flat}
$$

與：

$$
Agent_{HO}.
$$

應看到：

$$
\operatorname{InvalidRevisitRate}(Agent_{HO})
<
\operatorname{InvalidRevisitRate}(Agent_{flat}).
$$

## 預測四：過度激進的 higher-order compression 會提高 false-prune risk

若 quotient / no-go inheritance 太激進：

$$
\operatorname{FalsePruneRate}\uparrow.
$$

所以有效系統應存在 accuracy--compression tradeoff。

---

# 43. 與目前 AI theorem proving 發展的關係

現代 formal theorem proving 已清楚朝下列方向前進：

- proof states 不只輸入模型，而是可搜尋節點；
- proof trajectory 可以被評估；
- failure signal 可以回饋 search；
- lemma dependency 可以先被規劃成 blueprint；
- multi-agent 可以分工關閉不同 lemma nodes；
- state graph 可以作大規模資料生成來源；
- proof plan 可以被保存為 DAG。

本文認為下一個自然問題是：

> 當同一研究問題跨越數千次 episodes 後，這些 episode 之間的關係本身是否應被當成第一級研究資料？

本文的答案是肯定的。

這不是因為高階語言比較漂亮，而是因為缺少它時，系統無法區分：

$$
\text{new theorem},
$$

$$
\text{new route},
$$

$$
\text{old route revisit},
$$

$$
\text{new relation among old routes}.
$$

---

# 44. 本文與前三篇的依賴關係

## 44.1 對 LSI-PSD-01 的依賴

第 1 篇建立：

$$
\text{search regime}
\neq
\text{mathematical reality}.
$$

本文所有 sampling order 都只屬於可觀測 regime。

## 44.2 對 LSI-PSD-02 的依賴

第 2 篇建立：

$$
I_N,
\qquad
\Delta I_N,
$$

與多層 coverage。

本文將其展開為：

$$
I_k(N).
$$

## 44.3 對 LSI-PSD-03 的依賴

第 3 篇建立 semantic quotient。

沒有 quotient，就無法可靠判斷：

$$
\text{revisit},
$$

$$
\text{confluence},
$$

$$
\text{route family}.
$$

因此：

$$
\boxed{
\text{Higher-order sampling requires quotient-aware identity.}
}
$$

---

# 45. 本文的非主張

本文不主張：

1. 階數越高越接近真理；
2. 階數越高代表 AI 越智能；
3. meta-analysis 可以取代 theorem proof；
4. 出現 `second-order` 字樣就等於二階 proof-space sampling；
5. 大量 recurrence 就證明問題 framing 錯誤；
6. route confluence 就證明存在唯一 obstruction；
7. $K$ 階局部飽和就證明底層 proof space 被耗盡；
8. NS-203 已經達到全域 saturation；
9. P/NP 或 Navier--Stokes 因長期未證而應被重新定義；
10. LLM 對 route relation 的判斷可以不經 audit 當作數學等價；
11. 更細的 taxonomy 本身就是研究進展；
12. $T_X$ 表示無限階；
13. 所有研究問題都會經歷相同 sampling-order migration；
14. formal theorem proving 的 state graph 與 informal research proof-space 完全同構；
15. 本文已給出一個完備的 higher-order proof ontology。

---

# 46. 限制

## 46.1 Order assignment 仍具有模型依賴

即使 schema 明確，legacy text 仍可能缺少足夠 provenance 來重建 route relations。

因此：

$$
\operatorname{ord}_{obs}
$$

是一個帶不確定性的估計。

## 46.2 Relation extraction 比 theorem extraction 更難

單一 theorem statement 可以被 parser 抽取。

但：

> 兩條不同方法共享同一真正 obstruction

往往需要：

- 深層語義判斷；
- assumptions 對齊；
- proof dependency audit；
- 可能的形式化重建。

這會是目前 observatory 的主要瓶頸。

## 46.3 高階 measure 未必存在天然概率結構

 $\mu_k$ 的定義可能高度依賴 task。

因此本文不宣稱：

$$
I_k
$$

具有唯一自然的 measure-theoretic 定義。

它首先是一族可操作 coverage functional。

## 46.4 NS corpus 仍是單一問題族

要驗證框架是否普遍，需要加入：

- Collatz；
- BSD；
- combinatorics；
- formal olympiad proof；
- program verification；
- 其他 PDE。

只有跨域 transfer 後，才能判斷哪些 higher-order relations 是一般性的。

---

# 47. 結論：研究本身會成為下一階研究對象

長程 AI 數學研究最重要的變化，不只是生成速度提高。

真正的結構變化是：

$$
\text{research outputs}
$$

逐漸變成下一輪研究的 objects。

第一階段研究：

$$
\text{What mathematical objects exist?}
$$

第二階段研究：

$$
\text{How do proof states transform?}
$$

再下一階段：

$$
\text{How are proof routes related?}
$$

更後面：

$$
\text{How do those relations themselves recur, converge, inherit failure, and modify search?}
$$

因此本文把長程研究寫成：

$$
\Omega^{(0)}
\to
\Omega^{(1)}
\to
\Omega^{(2)}
\to
\cdots
\to
\Omega^{(K)}.
$$

但這不是一條「往真理上升」的階梯。

它是一條**研究對象階層化**的路徑。

真正需要觀察的是：

$$
\nu_k,
\qquad
I_k,
\qquad
\rho_k,
\qquad
C_w,
\qquad
D_{re},
\qquad
D_{fb},
\qquad
H_k^{route}.
$$

當：

$$
\nu_0\to0
$$

時，研究未必停止。

它可能只是開始問：

> 為什麼我們總是走回同一個地方？

而當這個問題也被反覆研究時，proof space 便不再只是「候選證明的集合」，而開始呈現一個可被觀測、壓縮、比較與重新路由的動態結構。

本文因此提出系列中的第四個核心命題：

$$
\boxed{
\textbf{Long-horizon proof search can migrate from sampling mathematical states to sampling relations among proof routes.}
}
$$

以及它的保守版本：

$$
\boxed{
\textbf{Higher-order recurrence is evidence about the structure of a research regime, not a verdict on the underlying mathematical proposition.}
}
$$

這為下一篇「局部飽和與全域開放」建立基礎：如果 sampling order 可以因 basin 而不同，那麼所謂「證明空間飽和」就必須從一開始被理解為局部、階層依賴且制度相對的現象。

---

# 參考文獻

1. Yin, D., & Gao, J. (2025). **Generating Millions Of Lean Theorems With Proofs By Exploring State Transition Graphs.** arXiv:2503.04772. https://arxiv.org/abs/2503.04772

2. Huang, S., Song, P., George, R. J., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925. https://arxiv.org/abs/2502.17925

3. Hubert, T. et al. (2025). **Olympiad-level formal mathematical reasoning with reinforcement learning.** Nature. https://www.nature.com/articles/s41586-025-09833-y

4. Chung, J.-H. et al. (2026). **Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement.** arXiv:2606.06468. https://arxiv.org/abs/2606.06468

5. Kung, P. N. et al. (2026). **LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks.** arXiv:2606.03303. https://arxiv.org/abs/2606.03303

6. Wang, Z., Yang, B., Zhou, S., Li, C., Zhang, Y., Dong, B., & Wen, Z. (2025). **Translating Informal Proofs into Formal Proofs Using a Chain of States.** arXiv:2512.10317. https://arxiv.org/abs/2512.10317

7. Kurgan, S. et al. (2026). **TheoremGraph: Bridging Formal and Informal Mathematics.** arXiv:2606.25363. https://arxiv.org/abs/2606.25363

8. **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** (2026). arXiv:2606.05400. https://arxiv.org/abs/2606.05400

9. **VERITAS: Verifier-Guided Proof Search for Zero-Shot Formal Theorem Proving.** (2026). arXiv:2606.19399. https://arxiv.org/abs/2606.19399

10. **TreeThink: A Modular Tree Search Library for Mathematical Reasoning with LLMs.** (2026). arXiv:2607.11258. https://arxiv.org/abs/2607.11258

11. Dong, K., & Ma, T. (2025). **STP: Self-play LLM Theorem Provers with Iterative Conjecturing and Proving.** Proceedings of the 42nd International Conference on Machine Learning, PMLR 267. https://proceedings.mlr.press/v267/dong25h.html

12. Song, P., Yang, K., & Anandkumar, A. (2025). **Lean Copilot: Large Language Models as Copilots for Theorem Proving in Lean.** Proceedings of the International Conference on Neuro-symbolic Systems, PMLR 288. https://proceedings.mlr.press/v288/song25a.html

13. **TheoremBench: Evaluating LLMs on Theorem Proving in Formal Mathematics.** (2026). arXiv:2606.09450. https://arxiv.org/abs/2606.09450

14. Lyu, H. et al. (2026). **Rtl2lean: Automated RTL-to-Lean Translation with Hierarchical Theorem Generation and Lemma Reuse.** arXiv:2607.16855. https://arxiv.org/abs/2607.16855

---

## 附錄 A：符號表

| 符號 | 意義 |
|---|---|
| $Q$ | 研究問題 |
| $R$ | 搜尋制度 / research regime |
| $\Omega_R^{(0)}(Q)$ | 基礎 research-state objects |
| $\Omega_R^{(1)}(Q)$ | proof moves / route objects |
| $\Omega_R^{(2)}(Q)$ | route relations |
| $\Omega_R^{(k)}(Q)$ | 第 $k$ 階 proof-space objects |
| $\mathcal F_k$ | 第 $k$ 階到第 $k+1$ 階的 typed constructor family |
| $T_1,T_2,T_3,T_X$ | legacy corpus 的四層操作 tier |
| $\nu_k(N)$ | 第 $k$ 階 novelty |
| $I_k(N)$ | 第 $k$ 階 coverage functional |
| $\rho_k(N)$ | 第 $k$ 階 audited yield |
| $C_w(O)$ | obstruction 的 weighted confluence |
| $D_{re}(R)$ | route 的 re-entry depth |
| $D_{fb}$ | feedback depth |
| $H_k^{route}$ | 第 $k$ 階 route-family entropy |
| $T_{score}$ | relation 的跨域 transfer score |
| $\operatorname{Sat}_K(B)$ | basin $B$ 的 $K$ 階操作性局部飽和標記 |

---

## 附錄 B：最小實驗設計

若要把本文從方法論變成可檢驗研究，可進行以下實驗：

### B.1 Corpus

使用至少三種長程研究 corpus：

$$
C_1=\text{NS-203},
$$

$$
C_2=\text{另一個未解數學問題 corpus},
$$

$$
C_3=\text{formal theorem proving traces}.
$$

### B.2 雙人／雙模型標註

隨機抽取 artifact pairs 與 route families，標註：

$$
\operatorname{ord},
$$

$$
\operatorname{route\_family},
$$

$$
\operatorname{obstruction\_id},
$$

$$
\operatorname{confluence}.
$$

計算 inter-rater agreement。

### B.3 自動抽取與人工 gold set 比較

測：

$$
Precision_k,
\qquad
Recall_k,
\qquad
F1_k.
$$

若 $T_3/T_X$ precision 很低，則不得用它們支持 higher-order saturation claim。

### B.4 時序測試

按真實時間排序 corpus，計算：

$$
\nu_k^{(W)}(N)
$$

與 random permutation baseline 比較。

### B.5 Transfer 測試

把從 NS 得到的 obstruction relation ontology 移植到另一 PDE corpus。

如果：

$$
T_{score}\approx0,
$$

則原 taxonomy 很可能只是 corpus-specific。

---

## 附錄 C：一句話版本

$$
\boxed{
\text{一開始研究答案；之後研究路徑；再之後，研究為什麼不同路徑總是彼此相遇。}
}
$$

這三個階段不代表越來越接近真理。

它們代表：

$$
\boxed{
\text{研究本身正在成為新的研究對象。}
}
$$
