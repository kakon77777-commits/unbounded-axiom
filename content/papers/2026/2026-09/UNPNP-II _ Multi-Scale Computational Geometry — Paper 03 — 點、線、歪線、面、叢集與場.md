# UNPNP-II / Multi-Scale Computational Geometry — Paper 03
## 點、線、歪線、面、叢集與場
### Computational Dependency Geometry Beyond Ordinary Graph Paths

**系列名稱：** UNPNP-II｜Multi-Scale Computational Geometry  
**系列中文名：** UNPNP 第二層：多尺度計算幾何與相對最短路徑  
**篇次：** Paper 03 / 08  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-08  
**文件性質：** 計算幾何／依賴拓樸／多尺度計算路徑論／UNPNP 擴充論文  
**前置：** Paper 01《計算的一到底是什麼？》；Paper 02《最短路徑不存在於真空中》  
**狀態：** Canonical Draft

---

## 摘要

UNPNP-II Paper 01 已指出，計算中的「一步」不是天然原子，而是相對 computational chart 被定義的有效單位；Paper 02 進一步指出，「最短路徑」因此也不是脫離尺度、觀察者、World boundary 與成本語義的絕對對象。

然而，這兩個結論仍預設了一個更深的問題尚未解決：

> **計算本身真的總是「一條路」嗎？**

傳統路徑語言天然偏向：

$$
v_1
\rightarrow
v_2
\rightarrow
\cdots
\rightarrow
v_n.
$$

但實際計算可能呈現：

- 一個已結晶的點；
- 一條序列線；
- 一條跳躍／稀疏歪線；
- 一個可並行展開的面；
- 多個區域化互動的叢集；
- 一個整體共同演化的場；
- 一個每個節點又可展開成世界的遞歸幾何。

因此本文提出：

$$
\boxed{
\text{Computational Route}
\supset
\text{Ordinary Graph Path}.
}
$$

並將計算幾何暫時分為：

$$
\boxed{
\mathfrak G_C
=
\{
\mathsf{Pt},
\mathsf{Ln},
\mathsf{Jl},
\mathsf{Sf},
\mathsf{Cl},
\mathsf{Fd},
\mathsf{Rc}
\}.
}
$$

其中：

- $\mathsf{Pt}$：Point，點；
- $\mathsf{Ln}$：Line，線；
- $\mathsf{Jl}$：Jump / Skew Line，跳線／歪線；
- $\mathsf{Sf}$：Surface，面；
- $\mathsf{Cl}$：Cluster，叢集；
- $\mathsf{Fd}$：Field，場；
- $\mathsf{Rc}$：Recursive Geometry，遞歸幾何。

本文強調，這套命名借用了幾何語言，但不是宣稱所有計算都必須嵌入歐氏空間。其核心研究對象是：

$$
\boxed{
\text{dependency geometry}
}
$$

即：

> 在指定 computational chart 下，哪些計算單位彼此依賴、可同時演化、可跳躍尋址、可聚類、可跨域耦合、可遞歸展開，以及哪些結構可被視為新的高階單位？

本文將普通路徑：

$$
\Gamma
=
(v_0,e_1,v_1,\ldots,e_n,v_n)
$$

擴張為：

$$
\boxed{
\mathcal R
=
\langle
U,
E,
H,
\preceq,
\mathcal K,
\mathcal F,
\Sigma,
\Pi
\rangle
}
$$

其中：

- $U$：computational units；
- $E$：binary transitions；
- $H$：hyperedges / multi-unit coupling；
- $\preceq$：causal / dependency partial order；
- $\mathcal K$：cluster decomposition；
- $\mathcal F$：field-like coupled evolution；
- $\Sigma$：scale / recursive embedding；
- $\Pi$：observer / projection structure。

這使 UNPNP 的「路」從單一 traversal graph 上的 path，擴張成可同時容納線性、並行、稀疏、叢集、場與遞歸結構的 **Computational Route Object**。

本文進一步主張：

$$
\boxed{
\text{Different computational geometries require different route metrics.}
}
$$

例如：

- 線更適合用 additive path cost；
- 面更需要 work–depth；
- 叢集需要 intra / inter-cluster cost；
- 場可能需要 action、energy、dissipation 或 trajectory functional；
- 遞歸幾何需要跨尺度 refinement / coarsening cost。

因此，所謂「最短路」不能只在不同 route 之間比較，也必須先判定：

> **現在面對的是哪一種 dependency geometry？**

本文最後把這套幾何與 24／72 計算配置、GCM 的 heterogeneous domains、MWT 的 World / presentation 分離，以及 UNPNP 的 Path Compilation / Crystallization 正式接軌。結果不是建立另一套互斥分類，而是建立一個可由 Runtime 動態選擇與切換的 geometry layer。

---

# 1. 一條線只是計算世界的一種特殊情況

最熟悉的計算表示是：

$$
u_1
\rightarrow
u_2
\rightarrow
\cdots
\rightarrow
u_n.
$$

它適合描述：

- instruction sequence；
- procedural workflow；
- pipeline；
- finite-state transition；
- ordered proof steps；
- dependency chain。

這種表示非常重要，但它只處理：

$$
\boxed{
\text{one-dimensional dependency order}.
}
$$

若實際系統存在大量同步、並行、multi-input coupling、distributed interaction、field update 或 recursive sub-world，強迫它變成一條線，可能只是：

$$
\boxed{
\text{serialization of a richer structure}.
}
$$

而不是結構本身。

---

# 2. Dependency Geometry

給定 computation：

$$
\mathcal C
$$

與 computational chart：

$$
\chi,
$$

其依賴幾何定義為：

$$
\boxed{
\mathfrak G_\chi(\mathcal C).
}
$$

它描述：

1. 哪些 unit 存在；
2. 哪些 unit 具有直接依賴；
3. 哪些 unit 可同時作用；
4. 哪些 unit 需要 multi-way coupling；
5. 哪些 unit 形成局部 cluster；
6. 哪些 state 以 field-like relation 共同演化；
7. 哪些 unit 可以展開成下層 geometry。

---

# 3. 幾何是比喻，也不是比喻

稱「點、線、面、場」確實借用了幾何詞彙，但不同 dependency structure 真正導致不同 ordering、critical path、synchronization、parallelism、locality、communication 與 cost functional。

因此：

$$
\boxed{
\text{geometry}
=
\text{structure of computational dependence under a chart}.
}
$$

---

# 4. Point｜點

令：

$$
u
$$

在當前 chart 中被視為不可再展開的有效 primitive，則：

$$
\boxed{
\mathfrak G_\chi(u)=\mathsf{Pt}.
}
$$

例如 constant-time lookup、compiled function、verified crystal、atomic transaction、model inference call 或 hardware primitive。

重要的是：

$$
\boxed{
\mathsf{Pt}^{(k)}
\not\Rightarrow
\mathsf{Pt}^{(k-1)}.
}
$$

高層的一個點，向下可能是一整個世界。

---

# 5. Earned Point

若：

$$
\Gamma^{(k-1)}
$$

經：

$$
\Gamma^{(k-1)}
\rightarrow
\widehat{\ell}
\rightarrow
\kappa^{(k)},
$$

則：

$$
\kappa^{(k)}
$$

可以在上層成為：

$$
\boxed{
\mathsf{Pt}^{(k)}.
}
$$

這叫 **Earned Point**：由低層已驗證結構提升而來的高層計算點。

---

# 6. 點不是零成本

即使：

$$
H=1,
$$

仍可能：

$$
W\gg1.
$$

因此：

$$
\boxed{
\text{Point geometry}
\neq
\text{zero physical work}.
}
$$

點只代表在當前 chart 中，內部 dependency 暫不作為 route selection 的一級對象。

---

# 7. Line｜線

$$
u_1
\rightarrow
u_2
\rightarrow
\cdots
\rightarrow
u_n.
$$

定義：

$$
\boxed{
\mathsf{Ln}
=
\text{a predominantly ordered dependency chain}.
}
$$

其自然 cost：

$$
C_{\mathrm{Ln}}
=
\sum_{i=1}^{n}
c_i.
$$

---

# 8. Line 的核心不是視覺上的直

真正條件是：

$$
u_i
\prec
u_{i+1}
$$

形成主要 ordered chain。

所以：

$$
\boxed{
\text{Line}
=
\text{serializable dependency geometry}.
}
$$

---

# 9. Jump-Line / Skew-Line｜跳線／歪線

若 route 透過 index、semantic address、heuristic、sparse selection、hyperlink 或 retrieval 直接跳至非鄰近 unit：

$$
u_1
\rightarrow
u_{17}
\rightarrow
u_{231}
\rightarrow
u_{900},
$$

本文稱：

$$
\boxed{
\mathsf{Jl}.
}
$$

---

# 10. 歪線不是壞掉的直線

它的真正含義是：

$$
\boxed{
\text{adjacency is replaced by selective addressability}.
}
$$

因此它直接承接：

$$
\text{Hyperlink}
=
\text{Addressable Cross-Subspace Transition}.
$$

---

# 11. Jump-Line Cost

$$
C_{\mathrm{Jl}}
=
C_{\mathrm{address}}
+
C_{\mathrm{resolve}}
+
C_{\mathrm{guard}}
+
C_{\mathrm{cross}}
+
C_{\mathrm{verify}}.
$$

所以：

$$
\boxed{
\text{fewer hops}
\not\Rightarrow
\text{lower total cost}.
}
$$

---

# 12. Surface｜面

假設：

$$
\{u_i\}_{i=1}^{n}
\xrightarrow{\parallel}
\{u_i'\}_{i=1}^{n}.
$$

大量 unit 可以同時更新。

若把它序列化成：

$$
u_1\rightarrow u_2\rightarrow\cdots\rightarrow u_n,
$$

只是 representation choice。

本文稱：

$$
\boxed{
\mathsf{Sf}.
}
$$

---

# 13. 面的核心量不是邊數

對 surface：

$$
W=n
$$

可能很大，

但：

$$
D\approx1
$$

可能很小。

所以自然 metric 是：

$$
\boxed{
(W,D).
}
$$

---

# 14. Surface 與 Parallel Form 不同層

24 範式中的：

$$
\mathsf P
$$

常投影成 surface geometry，但：

$$
\boxed{
\mathsf P
\neq
\mathsf{Sf}.
}
$$

一個是 update organization，一個是 dependency geometry。

---

# 15. 一個面裡仍然可以有線

如果：

$$
L_1,\ldots,L_k
$$

各自是 sequential chain，但彼此可並行，整體仍可形成：

$$
\boxed{
\mathsf{Sf}
=
\text{parallel composition of lower-order geometries}.
}
$$

---

# 16. Cluster｜叢集

若 computation 形成：

$$
K_1,\ldots,K_m
$$

且通常：

$$
C_{\mathrm{intra}}
\ll
C_{\mathrm{inter}},
$$

或群內 dependency density 明顯較高，則稱：

$$
\boxed{
\mathsf{Cl}.
}
$$

---

# 17. Cluster 不一定是互斥 Partition

可以有：

$$
K_i\cap K_j\neq\varnothing.
$$

叢集可以動態形成、合併、分裂、重疊或共享 boundary。

---

# 18. Cluster Cost

$$
\boxed{
C_{\mathrm{Cl}}
=
C_{\mathrm{intra}}
+
C_{\mathrm{inter}}
+
C_{\mathrm{coord}}
+
C_{\mathrm{partition}}.
}
$$

---

# 19. Hypernode

一個 cluster：

$$
K_i
$$

可以在 macro chart 中壓成：

$$
v_i^{\mathrm{hyper}}.
$$

因此：

$$
\boxed{
\text{Cluster}^{(k)}
\rightarrow
\text{Point}^{(k+1)}.
}
$$

---

# 20. Field｜場

如果：

$$
\phi(x,t)
$$

在 domain：

$$
\Omega
$$

中整體演化：

$$
\partial_t\phi
=
F[\phi],
$$

則稱：

$$
\boxed{
\mathsf{Fd}.
}
$$

---

# 21. 場不是很多獨立點的簡單總和

即使離散化成：

$$
\{\phi_i\}_{i=1}^{n},
$$

仍不能推出：

$$
\boxed{
\text{discretized representation}
=
\text{independent-point ontology}.
}
$$

因為 coupling law 可能決定整體演化。

---

# 22. Field Route

在 field geometry 中，route 更接近：

$$
\boxed{
\gamma:
t\mapsto\phi_t.
}
$$

其 cost 可能是：

$$
J[\gamma]
=
\int_{t_0}^{t_1}
\mathcal L(
\phi_t,
\dot\phi_t,
t
)
dt.
$$

---

# 23. Field Shortest 不是 Graph Hop Shortest

可能關心 action、energy、dissipation、transition time、control effort 或 information loss。

因此：

$$
\boxed{
\text{graph distance}
}
$$

可能不是主要 metric。

---

# 24. Recursive Geometry｜遞歸幾何

若：

$$
u^{(k)}
$$

在尺度 $k$ 是一個 unit，但：

$$
R_\downarrow(u^{(k)})
=
\mathcal W^{(k-1)},
$$

則：

$$
\boxed{
\mathsf{Rc}.
}
$$

---

# 25. Recursive Point

$$
\boxed{
\mathsf{Pt}^{(k)}
=
\mathcal W^{(k-1)}
}
$$

在 projection-relative 意義下可以成立。

例如：

```text
macro: AI agent = one node
meso: planner + memory + tools + validator
micro: model operations + tool execution + state changes
```

---

# 26. Recursive Edge

一條高層 edge：

$$
e^{(k)}
$$

可能展開為：

$$
\Gamma^{(k-1)}.
$$

所以：

$$
\boxed{
\text{Edge}^{(k)}
=
\text{Route}^{(k-1)}.
}
$$

---

# 27. Recursive Surface

一個上層 surface 的 cell 可以是下層 cluster 或 field。

因此：

$$
\boxed{
\text{geometry can be nested across scale}.
}
$$

---

# 28. Geometry 不必互斥

一個 computation 可以同時：

- local line；
- meso cluster；
- parallel surface；
- macro recursive geometry。

因此不要求：

$$
\mathfrak G_\chi(\mathcal C)
$$

只能是一個標籤。

---

# 29. Geometry Mixture

可選擇定義：

$$
\nu_{\mathcal C}:
\mathfrak G_C
\rightarrow
[0,1]
$$

描述某 chart 下的幾何成分。

這只是可用 representation，不是唯一形式。

---

# 30. Geometry Path

計算也可能隨成熟度改變 geometry：

$$
\boxed{
\mathsf{Ln}
\rightarrow
\mathsf{Jl}
\rightarrow
\mathsf{Sf}
\rightarrow
\mathsf{Pt}.
}
$$

例如逐步搜尋、建立 index、批次並行、最後結晶成 lookup primitive。

---

# 31. Geometry Transition

定義：

$$
\boxed{
T_G:
g_i\rightarrow g_j.
}
$$

它有成本：

$$
C_{G\text{-switch}}.
$$

可能包括 build index、partition cluster、vectorize、compile 或 crystallize。

---

# 32. Geometry Transition 不是免費 Re-labeling

如果只是把：

$$
u_1\rightarrow\cdots\rightarrow u_{100}
$$

命名成：

```text
fast()
```

沒有改 dependency 與 execution cost，就不算真正：

$$
\mathsf{Ln}\rightarrow\mathsf{Pt}.
$$

---

# 33. Geometry-Preserving Compression

若只改 representation：

$$
\mathcal G\rightarrow\widehat{\mathcal G}
$$

但 dependency topology 未實質改變，則只是：

$$
\boxed{
\text{geometry-preserving compression}.
}
$$

---

# 34. Geometry-Rewriting Compilation

若：

$$
\mathcal G\rightarrow\mathcal G'
$$

且：

$$
\mathcal G'\not\simeq_{\mathrm{top}}\mathcal G,
$$

但：

$$
\operatorname{Semantics}(\mathcal G')
\simeq
\operatorname{Semantics}(\mathcal G),
$$

則可稱：

$$
\boxed{
\text{geometry-rewriting compilation}.
}
$$

---

# 35. UNPNP Path Compilation 是其中一種

原本：

$$
\mathsf{Ln}:
B_1\rightarrow B_2\rightarrow\cdots\rightarrow B_n
$$

編譯成：

$$
B_1\xrightarrow{\widehat{\ell}}B_n.
$$

這可能是：

$$
\mathsf{Ln}\rightarrow\mathsf{Jl}
$$

甚至：

$$
\mathsf{Ln}\rightarrow\mathsf{Pt}.
$$

因此：

$$
\boxed{
\text{Path Compilation}
\subseteq
\text{Dependency Geometry Rewriting}.
}
$$

---

# 36. Computational Route Object

普通 path：

$$
\Gamma
=
(v_0,e_1,v_1,\ldots,e_n,v_n)
$$

不足以統一描述上述結構。

本文提出：

$$
\boxed{
\mathcal R
=
\langle
U,
E,
H,
\preceq,
\mathcal K,
\mathcal F,
\Sigma,
\Pi
\rangle.
}
$$

---

# 37. $U$：Computational Units

$$
U=\{u_1,\ldots,u_n\}.
$$

其 unit boundary 由 Paper 01 的：

$$
U_\chi
$$

決定。

---

# 38. $E$：Binary Transitions

$$
E\subseteq U\times U.
$$

表示 ordinary typed dependency / transition。

---

# 39. $H$：Hyperedges

如果：

$$
\{u_1,u_2,u_3\}
$$

必須共同作用才能產生 $v$：

$$
\boxed{
h:
\{u_1,u_2,u_3\}
\rightarrow
v.
}
$$

binary graph 可能丟失 joint dependency。

---

# 40. $\preceq$：Causal Partial Order

不要求 total order。

$$
u_i\preceq u_j
$$

表示 $u_i$ 因果上必須先於 $u_j$。

若：

$$
u_i\parallel u_j,
$$

則兩者可能並行。

---

# 41. $\mathcal K$：Cluster Structure

$$
\mathcal K=\{K_1,\ldots,K_m\}.
$$

可為 partition、cover 或 dynamic grouping。

---

# 42. $\mathcal F$：Field Structure

記錄 local coupling、continuous state、density、potential、global functional 或 neighborhood law。

---

# 43. $\Sigma$：Scale Embedding

記錄：

$$
u_i^{(k)}
\leftrightarrow
\mathcal W_i^{(k-1)}
$$

及：

$$
R_\downarrow,
R_\uparrow.
$$

---

# 44. $\Pi$：Observer Projection

不同 observer：

$$
o_i
$$

只看到：

$$
\Pi_{o_i}(\mathcal R).
$$

同一 route object 可以被投影成 point、line、cluster、dashboard action 或 API call。

---

# 45. Route Object 不是 World 本身

繼承 MWT：

$$
\boxed{
\mathbf W
\neq
\mathcal R.
}
$$

Computational Route Object 只是：

$$
\boxed{
\text{route-oriented presentation of world computation}.
}
$$

---

# 46. Geometry-Specific Metric Family

$$
\boxed{
\mathfrak M_G
=
\{
d_{\mathrm{Pt}},
d_{\mathrm{Ln}},
d_{\mathrm{Jl}},
d_{\mathrm{Sf}},
d_{\mathrm{Cl}},
d_{\mathrm{Fd}},
d_{\mathrm{Rc}}
\}.
}
$$

---

# 47. Point Metric

$$
C_{\mathrm{Pt}}
=
C_{\mathrm{lookup}}
+
C_{\mathrm{guard}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{update}}.
$$

---

# 48. Line Metric

$$
C_{\mathrm{Ln}}
=
\sum_i
c(u_i,u_{i+1}).
$$

---

# 49. Jump-Line Metric

$$
C_{\mathrm{Jl}}
=
\sum_j
(
c_{\mathrm{address}}
+
c_{\mathrm{resolve}}
+
c_{\mathrm{cross}}
+
c_{\mathrm{verify}}
)_j.
$$

---

# 50. Surface Metric

至少：

$$
\boxed{
C_{\mathrm{Sf}}
=
(W,D,S,C_{\mathrm{sync}}).
}
$$

---

# 51. Cluster Metric

$$
\boxed{
C_{\mathrm{Cl}}
=
C_{\mathrm{intra}}
+
C_{\mathrm{inter}}
+
C_{\mathrm{coord}}
+
C_{\mathrm{partition}}.
}
$$

---

# 52. Field Metric

例如：

$$
J[\gamma]
=
\int
\mathcal L\,dt,
$$

或：

$$
C_{\mathrm{Fd}}
=
(
E_{\mathrm{energy}},
T,
D_{\mathrm{dissipation}},
I_{\mathrm{loss}}
).
$$

---

# 53. Recursive Metric

$$
C_{\mathrm{Rc}}
=
C_{\mathrm{macro}}
+
C_{\mathrm{refine}}
+
C_{\mathrm{micro}}
+
C_{\mathrm{coarsen}}
+
C_{\mathrm{cross-scale}}.
$$

---

# 54. 不可直接用 Hop Count 跨 Geometry 比較

如果 line route：

$$
H_A=5,
$$

而 surface：

$$
W_B=100,\qquad D_B=1,
$$

不能直接說 1 比 5 短。

需先指定 common objective。

因此：

$$
\boxed{
\text{cross-geometry comparison requires metric translation}.
}
$$

---

# 55. Common Resource Vector

Geometry-specific metric 最後投影到：

$$
\mathbf C
=
(
H,W,D,T,M,K,V,P,U,E,R,L_O
).
$$

然後由：

$$
J_\omega
$$

或 Pareto order 比較。

---

# 56. Geometry 與 24／72 不同層

$$
\boxed{
\mathfrak G_C
\neq
\mathfrak P_{24}
\neq
\mathfrak P_{72}.
}
$$

24／72 回答 computational form / transition law；geometry 回答 dependency arrangement。

---

# 57. 但二者高度耦合

例如：

$$
D\text{-}S\text{-}D\text{-}F
$$

常自然形成 line；

$$
D\text{-}P\text{-}D\text{-}F
$$

常自然形成 surface。

但不是一一對應定理。

---

# 58. Recognition 常投影成 Point

$$
R
$$

recognition / retrieval 對 caller 常像：

$$
\mathsf{Pt}.
$$

但內部 model 仍可能是一個巨大 parallel field 或 cluster。

---

# 59. Jump Update 常投影成 Jump-Line

$$
J
$$

與：

$$
\mathsf{Jl}
$$

具有自然接口，尤其在 sparse search、index、semantic hyperlink 與 selective refinement。

---

# 60. GCM Domain 可以攜帶 Geometry

令：

$$
g_i(t)\in\mathfrak G_C.
$$

則可擴成：

$$
\boxed{
\Phi_i(t)
=
\Phi(
D_i,
p_i,
\lambda_i,
g_i,
c_i
).
}
$$

---

# 61. 同一 World 可同時存在多種 Geometry

例如：

$$
D_1:\mathsf{Fd},
\quad
D_2:\mathsf{Cl},
\quad
D_3:\mathsf{Ln},
\quad
D_4:\mathsf{Pt}.
$$

全域不是把它們轉成同一 geometry，而是合法組合。

---

# 62. Cross-Geometry Bridge

若：

$$
D_i:\mathsf{Fd}
$$

而：

$$
D_j:\mathsf{Ln},
$$

則需要：

$$
\boxed{
B_{ij}^{g_i\rightarrow g_j}.
}
$$

例如 sampling、discretization、aggregation、embedding、event extraction 或 reconstruction。

---

# 63. Bridge 不是免費

$$
\boxed{
C_{\partial G}
=
C_{\mathrm{convert}}
+
C_{\mathrm{materialize}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{loss}}.
}
$$

跨 geometry shortcut 必須把 boundary cost 算進去。

---

# 64. Geometry Switching 可以產生 Complexity Transfer

例如：

$$
\mathsf{Ln}
\rightarrow
\mathsf{Jl}
$$

需要先：

$$
C_{\mathrm{build}}>0.
$$

但重複 $N$ 次後若：

$$
C_{\mathrm{build}}
+
NC_{\mathrm{Jl}}
<
NC_{\mathrm{Ln}},
$$

則 geometry rewrite 有 lifecycle value。

---

# 65. Geometry Compilation

$$
\boxed{
\operatorname{GC}:
(
\mathcal R,g_i
)
\rightarrow
(
\widehat{\mathcal R},g_j
).
}
$$

要求 semantics-preserving 且 lifecycle utility 為正。

---

# 66. Geometry Crystal

若新 geometry 長期穩定：

$$
\boxed{
K_G(
\widehat{\mathcal R},
g_j
)
=
\kappa_G.
}
$$

它結晶的不是一個結果，而是一種依賴重組模式。

---

# 67. Sequential → Parallel Crystal

若原本：

$$
a_1\rightarrow a_2\rightarrow a_3\rightarrow a_4
$$

後來發現：

$$
a_1\parallel a_2\parallel a_3,
$$

可形成：

$$
\mathsf{Ln}\rightarrow\mathsf{Sf}.
$$

驗證後可成 parallel primitive。

---

# 68. Search → Retrieval Crystal

原本：

$$
u_1\rightarrow\cdots\rightarrow u_n.
$$

建立 index：

$$
I.
$$

後：

$$
q\rightarrow I(q)\rightarrow u_k.
$$

因此：

$$
\mathsf{Ln}
\rightarrow
\mathsf{Jl}
\rightarrow
\mathsf{Pt}
$$

可能依成熟度逐層成立。

---

# 69. Multi-Agent → Cluster

多 Agent：

$$
A_1,\ldots,A_n
$$

若形成局部高互動群組，可：

$$
\text{flat graph}
\rightarrow
\mathsf{Cl}.
$$

macro routing 先處理 cluster，再按需展開。

---

# 70. Grid → Field

離散 cell：

$$
x_{ij}
$$

可以在 macro observer 下重構為：

$$
\phi(x,y,t).
$$

所以：

$$
\mathsf{Sf}\rightarrow\mathsf{Fd}
$$

可以是 observer / scale transition，不代表本體改變。

---

# 71. Geometry 是 Observer-Relative

對 CPU：

$$
\mathsf{Sf}
$$

可能是 SIMD lanes。

對 programmer：

同一行為可能是：

$$
\mathsf{Pt}
$$

的 `matrix_multiply()`。

所以：

$$
\boxed{
g(\mathcal C)
=
g(\mathcal C\mid o,\sigma,\chi).
}
$$

---

# 72. Observer-Relative 不等於任意

高層 point 仍必須攜帶 hidden-resource receipt：

- latency；
- memory；
- energy；
- failures；
- internal version。

否則 abstraction 會製造 false shortest。

---

# 73. Geometry Receipt

```text
GeometryReceipt
- geometry_id
- world_revision
- chart
- observer
- scale
- units
- geometry_type
- dependency_digest
- causal_digest
- resource_model
- source_projection
- validation
- epoch
```

---

# 74. Geometry Transition Receipt

```text
GeometryTransitionReceipt
- source_geometry
- target_geometry
- transformation
- semantic_invariants
- cost_before
- cost_after
- bridge_cost
- verification
- valid_domain
- fallback
```

---

# 75. False Geometry

如果 Runtime 誤把 hidden-dependent tasks 當成 surface-independent，可能造成：

- race；
- inconsistency；
- causal violation。

所以：

$$
\boxed{
\text{geometry inference is correctness-critical}.
}
$$

---

# 76. Geometry Uncertainty

對未知程式可保留：

$$
P(g\mid \text{evidence})
$$

或：

$$
\mathcal U_G.
$$

不必硬標單一 geometry。

---

# 77. Geometry Refinement

新 evidence 到來時：

$$
g_t\rightarrow g_{t+1}.
$$

例如：

$$
\mathsf{Sf}\rightarrow\mathsf{Cl}
$$

或：

$$
\mathsf{Pt}\rightarrow\mathsf{Ln}.
$$

---

# 78. Decrystallization as Geometry Reopening

若 hot point：

$$
\kappa
$$

失效：

$$
\mathsf{Pt}^{(k)}
\rightarrow
\mathsf{Rc}
\rightarrow
\mathsf{Ln}^{(k-1)}.
$$

重新打開內部 route。

---

# 79. Debug Geometry 不一定等於 Execution Geometry

- race condition → surface / partial order；
- latency bottleneck → line / critical path；
- distributed coordination → cluster；
- numerical instability → field；
- hidden abstraction bug → recursive geometry。

因此：

$$
\boxed{
\text{debug geometry}
\neq
\text{execution geometry}.
}
$$

---

# 80. Geometry-Specific Verification

Line：

- stepwise correctness。

Surface：

- independence；
- synchronization。

Cluster：

- boundary consistency；
- protocol correctness。

Field：

- stability；
- invariants；
- discretization error。

Recursive：

- cross-scale refinement correctness。

---

# 81. Geometry Router

AI-native Runtime 可定義：

$$
\boxed{
\mathcal M_{\mathrm{geom}}
:
(
s,q,\chi,\mathcal H,B,R
)
\mapsto
g_t.
}
$$

它回答：

> 現在應把問題看成點、線、面、叢集還是場？

---

# 82. Geometry Router 與 Adaptive Corridor

可以：

$$
\mathcal M_{\mathrm{geom}}
\rightarrow
g_t
$$

再：

$$
\mathcal M_{\mathrm{corridor}}(g_t)
\rightarrow
\Phi_t.
$$

更強則聯合：

$$
\boxed{
(g_t,\Phi_t)
=
\arg\min_{g,\Phi}
J(g,\Phi).
}
$$

---

# 83. Computational Geometry Field

對大型 world：

$$
\boxed{
\Gamma_G:
D_i\mapsto g_i.
}
$$

不同 domain 可以各自採不同 geometry。

---

# 84. Geometry Field 可以動態更新

$$
\Gamma_G(t)
\neq
\Gamma_G(t+1).
$$

例如：

- sparse region → jump-line；
- dense independent region → surface；
- stable region → point；
- uncertain region → recursive refinement。

---

# 85. Global Geometry 不等於 One Geometry Everywhere

$$
\boxed{
\text{Global Computational Geometry}
\neq
\text{One Geometry Everywhere}.
}
$$

更準確：

$$
\boxed{
\text{Global Geometry}
=
\text{Coherent Composition of Heterogeneous Dependency Geometries}.
}
$$

---

# 86. Unknown Geometry 是合法狀態

$$
g=\mathsf{Unknown}
$$

必須是一級狀態。

不能因為分析工具只會畫 graph，就假設 unknown computation 是 line。

---

# 87. Geometry Discovery

```text
observe
→ trace
→ infer dependency
→ detect concurrency
→ detect clustering
→ detect field-like coupling
→ detect recursive structure
→ propose geometry
→ validate
```

---

# 88. Geometry Evidence 不只來自 Source

應包含：

- source；
- runtime trace；
- profiler；
- causal logs；
- hardware；
- message history；
- state transitions；
- memory access；
- observer projection。

因此：

$$
\boxed{
\text{source dependency}
\neq
\text{runtime dependency}.
}
$$

---

# 89. Geometry Evolution Path

$$
g_0
\rightarrow
g_1
\rightarrow
\cdots
\rightarrow
g_T.
$$

這個歷史本身應保存。

---

# 90. Same Macro Geometry 不等於 Same Derivation

兩個 Runtime 最後都是：

$$
\mathsf{Pt},
$$

一個可能由 line 結晶，另一個由 field approximation 結晶。

所以：

$$
\boxed{
\text{same macro geometry}
\neq
\text{same derivation}.
}
$$

---

# 91. 與 MWT 的接口

MWT 的 World primitive：

$$
\mathbf W
$$

不等於任何單一 presentation。

所以：

$$
\mathsf{Pt},
\mathsf{Ln},
\mathsf{Sf},
\mathsf{Fd}
$$

都只是 computational presentations。

本文不把任何 geometry 宣稱成 World ontology。

---

# 92. 與 GCM 的接口

GCM Domain：

$$
D_i
$$

可帶：

$$
p_i,\lambda_i
$$

而本文補：

$$
g_i.
$$

因此局部配置可記為：

$$
\boxed{
c_i
=
\langle
p_i,
\lambda_i,
g_i,
\sigma_i,
o_i
\rangle.
}
$$

---

# 93. 與 24／72 的接口

局部 route segment：

$$
\boxed{
r_i
=
\langle
p_i,
\lambda_i,
g_i
\rangle.
}
$$

例如：

$$
\langle
D\text{-}P\text{-}D,
F,
\mathsf{Sf}
\rangle.
$$

---

# 94. 不建立新的封閉乘法分類

本文拒絕直接把：

$$
24\times7\times3
$$

稱成新「完備範式」。

因為 geometry：

- 可混合；
- 可遞歸；
- observer-relative；
- vocab 可擴張。

所以：

$$
\boxed{
\mathfrak G_C
=
\text{extensible runtime geometry vocabulary}.
}
$$

---

# 95. 第一個實驗世界：Line

建立嚴格因果鏈：

$$
u_1\prec u_2\prec\cdots\prec u_n.
$$

Geometry-aware 與 line-only runtime 應近似一致。

這是 control。

---

# 96. 第二個實驗世界：Surface

大量 independent tasks。

若全部強制序列化，應導致：

$$
D_{\mathrm{line}}
\gg
D_{\mathrm{surface}}.
$$

---

# 97. 第三個實驗世界：Cluster

群內高耦合、群間低耦合。

測：

$$
C_{\mathrm{flat}}
$$

與：

$$
C_{\mathrm{cluster-aware}}.
$$

---

# 98. 第四個實驗世界：Field

用局部 coupling 形成整體演化，測 graph discretization 與 field-aware solver representation 的差異。

---

# 99. 第五個實驗世界：Recursive

macro node 可展開 micro graph。

測：

- always-expanded；
- always-coarse；
- adaptive refine / coarsen。

---

# 100. 實驗比較

固定 task，比較：

1. line-only representation；
2. geometry-aware routing；
3. geometry-aware + crystallization。

測：

- total work；
- critical depth；
- route search；
- synchronization；
- bridge cost；
- verification；
- failure；
- route quality。

---

# 101. 成功條件

如果在某 workload family：

$$
C_{\mathrm{geom-aware}}
<
C_{\mathrm{line-only}}
$$

穩定成立，且 correctness 不下降，則 dependency geometry 具有獨立 runtime 價值。

---

# 102. 失敗條件同樣重要

若 cluster 完全可由一般 graph partitioning 處理，surface 完全只等價既有 work-depth model，且新 abstraction 沒有跨域統一或 runtime routing 增益，應縮減術語。

因此：

$$
\boxed{
\text{new abstraction}
\neq
\text{claim of new mathematics}.
}
$$

---

# 103. 下一個真正缺口：時間與因果

至此我們已分離：

- point；
- line；
- jump-line；
- surface；
- cluster；
- field；
- recursive geometry。

但還不能把：

$$
\text{geometry}
$$

直接當：

$$
\text{time}.
$$

---

# 104. State Distance

兩個 state：

$$
s_i,s_j
$$

可以有：

$$
d_S(s_i,s_j).
$$

---

# 105. Causal Distance

$$
d_C(s_i,s_j)
$$

表示最小必要 causal depth。

---

# 106. Temporal Distance

$$
d_T(s_i,s_j)
$$

表示 event time / wall-clock。

---

# 107. Geometric Distance

$$
d_G(s_i,s_j)
$$

表示指定 dependency geometry 下的 route distance。

一般：

$$
\boxed{
d_S
\neq
d_C
\neq
d_T
\neq
d_G.
}
$$

---

# 108. 核心定律一

$$
\boxed{
\textbf{
Ordinary graph paths are a special case of computational routes.
}
}
$$

---

# 109. 核心定律二

$$
\boxed{
\textbf{
Different dependency geometries require different route metrics.
}
}
$$

---

# 110. 核心定律三

$$
\boxed{
\textbf{
A point at one scale may be a world at another scale.
}
}
$$

---

# 111. 核心定律四

$$
\boxed{
\textbf{
Geometry transitions are computational operations, not free relabelings.
}
}
$$

---

# 112. 核心定律五

$$
\boxed{
\textbf{
Global computation may require heterogeneous geometries to coexist coherently.
}
}
$$

---

# 113. 對 UNPNP 的重新表述

UNPNP-I 的 Path：

$$
\Gamma
$$

現在被包含於：

$$
\boxed{
\text{Computational Route Object}.
}
$$

而 Path Compilation 的更一般版本是：

$$
\boxed{
\text{Dependency Geometry Rewriting}.
}
$$

---

# 114. 對最短路徑的重新表述

$$
\arg\min_\Gamma C(\Gamma)
$$

只是：

$$
g=\mathsf{Ln}
$$

且 metric 固定時的特例。

完整問題開始變成：

$$
\boxed{
\arg\min_{g,\mathcal R}
J_g(
\mathcal R
\mid
\mathbf W,
\chi,
q,
B,
Risk
).
}
$$

---

# 115. Paper 04 的正式接口

下一篇：

## 時間不等於路長
### State Distance, Causal Depth, Temporal Order, Parallel Depth, and the Separation of Computational Histories

它將回答：

$$
\boxed{
\text{State Change}
\neq
\text{Causal Change}
\neq
\text{Temporal Change}
\neq
\text{Geometric Change}.
}
$$

也就是：

> 十個 operation 同時執行時，工作量是十、因果深度可能是一、wall-clock 可能是一個時間窗，而最終狀態變化又是另一個量。到底哪一個才叫「路長」？

---

# 結論

如果把所有計算都寫成：

$$
v_1
\rightarrow
v_2
\rightarrow
\cdots
\rightarrow
v_n,
$$

我們確實得到一張 graph。

但這張 graph 有時只是：

$$
\boxed{
\text{a serialized projection of richer computation}.
}
$$

實際計算可以呈現：

$$
\mathsf{Pt},
\mathsf{Ln},
\mathsf{Jl},
\mathsf{Sf},
\mathsf{Cl},
\mathsf{Fd},
\mathsf{Rc},
$$

以及它們的混合與遞歸組合。

因此本文提出：

$$
\boxed{
\text{Computational Route}
\supset
\text{Graph Path}.
}
$$

並以：

$$
\boxed{
\mathcal R
=
\langle
U,
E,
H,
\preceq,
\mathcal K,
\mathcal F,
\Sigma,
\Pi
\rangle
}
$$

作為第一版廣義 route object。

這使「路」不再只是一串 binary edges，而成為：

> **在指定 World presentation、尺度與 observer 下，用來描述計算單位之間依賴、耦合、並行、聚類、場演化與遞歸嵌套的可路由結構。**

所以真正的最短路徑問題，不只是：

$$
\min_\Gamma C(\Gamma),
$$

而開始成為：

$$
\boxed{
\min_{g,\mathcal R}
J_g(
\mathcal R
\mid
\mathbf W,
\chi,
q,
B,
Risk
).
}
$$

也就是：

$$
\boxed{
\textbf{
在找最短路以前，
先判斷現在的計算究竟是一個點、一條線、一個面、一個叢集、一個場，
還是一個可以繼續展開的世界。
}
}
$$

這就是 UNPNP 從「超連結路徑論」正式進入「多尺度計算幾何」的關鍵一步。
