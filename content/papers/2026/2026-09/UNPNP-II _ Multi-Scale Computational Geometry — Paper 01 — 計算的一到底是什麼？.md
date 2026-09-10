# UNPNP-II / Multi-Scale Computational Geometry — Paper 01
## 計算的一到底是什麼？
### Computational Unitization: Primitive Relativity, Scale-Dependent “One”, and the Missing Foundation of Shortest-Route Computation

**系列名稱：** UNPNP-II｜Multi-Scale Computational Geometry  
**系列中文名：** UNPNP 第二層：多尺度計算幾何與相對最短路徑  
**篇次：** Paper 01 / 08  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-08  
**文件性質：** 計算本體論／多尺度計算／UNPNP 擴充母篇  
**狀態：** Canonical Draft

---

## 摘要

經典演算法分析通常從一組已經指定好的 primitive operations 出發，再討論操作次數、時間複雜度、空間複雜度、臨界路徑或通訊成本。然而，在跨層次軟體、AI-native runtime、異質計算、分散式系統、巨集、函式、模組、Agent workflow、預編譯路徑與計算結晶同時存在的環境中，一個更早、也更基本的問題會浮現：

> **究竟什麼才算一次計算？**

一個 machine instruction 可以算作一；一個函式呼叫也可以算作一；一個巨集、一個模組、一個完整演算法、一個 Agent action，甚至一條經過驗證並被結晶化的跨底空間路徑，都可能在不同抽象層被視為一個單位。

因此：

$$
\boxed{
1_{\mathrm{instruction}}
\neq
1_{\mathrm{function}}
\neq
1_{\mathrm{algorithm}}
\neq
1_{\mathrm{crystal}}
}
$$

這不是算術中的 $1\neq1$，而是**計算單位語義的不同**。

本文提出 **Computational Unitization，計算單位化**，作為 UNPNP 第二層的第一個基礎概念。其核心主張是：

$$
\boxed{
\text{A computational unit is not an ontological atom.}
}
$$

更準確地說：

$$
\boxed{
\text{計算的一，是相對於 computational chart 被定義的一。}
}
$$

本文將 computational chart 暫定為：

$$
\chi
=
\langle
g,\sigma,o,\tau,\kappa,p,\lambda
\rangle,
$$

其中：

- $g$：granularity，粒度；
- $\sigma$：scale，尺度；
- $o$：observer，觀察者；
- $\tau$：temporal / causal organization，時間與因果組織；
- $\kappa$：computational geometry，計算幾何；
- $p$：24 計算形態中的局部形態；
- $\lambda$：72 格動力學中的局部轉移律。

在此基礎上，本文引入單位化算子：

$$
\boxed{
U_\chi:
\mathcal C
\rightarrow
\mathcal C/\chi
}
$$

用以表示：同一底層計算結構 $\mathcal C$，在不同 chart 下會被切分成不同的有效計算單位。

本文同時強調，將十個底層步驟包成一個 API、巨集或函式，不代表底層運算真的只剩一步。因此必須區分：

$$
\boxed{
\text{Surface Unit Count}
\neq
\text{Topological Depth}
\neq
\text{Causal Depth}
\neq
\text{Physical Work}
}
$$

進一步，本文將 computational unit 分為至少五種不同意義：

1. syntactic unit；
2. interface unit；
3. topological unit；
4. semantic unit；
5. physical unit。

而真正的 Computational Crystallization，則被重新理解為一種特殊的 upward unitization：一段已驗證的低層路徑被提升為較高尺度的新 primitive。

因此：

$$
\boxed{
\text{Path}^{(k)}
\rightarrow
\text{Primitive}^{(k+1)}
}
$$

並不等於：

$$
\boxed{
\text{Work}^{(k)}
\rightarrow0.
}
$$

UNPNP 過去對 Path Compilation、Hyperlink、Adaptive Corridor 與 Computational Crystallization 的定義仍成立；缺少的只是「路徑在哪個尺度上被定義」以及「一步的邊界由誰決定」。這一層補齊後，後續才有資格正式討論 observer-relative shortest route、point-line-surface-field computational geometry、跨 24／72 格 route composition，以及 MWT × GCM × UNPNP 的統一。

---

# 1. 問題不是「哪條路最短」，而是「什麼叫一步」

假設一個計算過程：

$$
a_1\rightarrow a_2\rightarrow\cdots\rightarrow a_{10}.
$$

如果把這十個步驟寫成一個巨集，從 API surface 看似乎只有一次呼叫，但底層 execution 仍存在十個 transition。

因此：

$$
\boxed{
\text{one call}
\neq
\text{one computational transition}
}
$$

這個命題在 UNPNP Series 06 已經出現，但本文把問題推得更底：如果一個函式不是天然的一，那 machine instruction 是否就是天然的一？答案仍然是否定的。

一個 machine instruction 可以在微架構層拆成 fetch、decode、rename、dispatch、execute、memory access、commit；再向下又能拆成 logic gates、transistor switching、signal propagation 與 physical state transition。

所以：

$$
\boxed{
\text{primitive}
=
\text{primitive relative to a chosen level}
}
$$

而不是宇宙中絕對不可再分的計算原子。

---

# 2. Computational Unitization

令：

$$
\mathcal C
$$

表示一個可被分析的計算結構。它可以是 program execution、causal DAG、state-transition system、field evolution、distributed workflow、AI agent trace 或 world-level computation。

給定 computational chart：

$$
\chi,
$$

定義：

$$
\boxed{
U_\chi(\mathcal C)=\mathcal C_\chi.
}
$$

 $\mathcal C_\chi$ 是同一底層計算在該 chart 下的 unitized representation。

因此「計算單位」不是 $\mathcal C$ 的天然原子，而是：

$$
\boxed{
\text{Unit}
=
\text{A chart-relative bounded computational object}.
}
$$

---

# 3. Computational Chart

第一版採：

$$
\boxed{
\chi
=
\langle
g,\sigma,o,\tau,\kappa,p,\lambda
\rangle.
}
$$

這七項不宣稱終極完備，只是目前最小可工作的 unitization context。

## 3.1 Granularity $g$

回答「什麼被當成一個計算單位？」例如 gate、instruction、statement、function、module、algorithm、agent action、workflow、subspace。

同一 execution 在兩個粒度下可以有：

$$
N_{g_1}\gg N_{g_2}.
$$

## 3.2 Scale $\sigma$

Granularity 回答「一切多大」，scale 回答「現在觀察哪一層世界」。

第一版可使用：

$$
\sigma\in\{\mu^-,\mu,m,M,M^+\}
$$

表示 recursive-micro、micro、meso、macro、recursive-macro。

真正核心是：

$$
\boxed{
\text{scale is recursively extensible}.
}
$$

## 3.3 Observer $o$

同一排序操作，user 看來可能只有「排序」一步；programmer 看來是一個 function；compiler 看來是大量 block；CPU 看來則是大量 instruction 與微操作。

因此：

$$
\boxed{
L(\Gamma)=L(\Gamma\mid o).
}
$$

## 3.4 Temporal / Causal Organization $\tau$

若十個 operation 互相獨立：

$$
W=10,
\qquad
D=1,
$$

其中 $W$ 是 total work， $D$ 是 causal / parallel depth。

因此：

$$
\boxed{
\text{Work Count}
\neq
\text{Causal Depth}.
}
$$

## 3.5 Computational Geometry $\kappa$

第一版允許：

$$
\kappa
\in
\{
\text{point},
\text{line},
\text{jump-line},
\text{surface},
\text{cluster},
\text{field},
\text{recursive}
\}.
$$

它描述的不是必然的歐氏位置，而是：

$$
\boxed{
\text{dependency geometry}.
}
$$

## 3.6 Computational Form $p$

局部 route segment 可帶：

$$
p\in\mathfrak P_{24}.
$$

因此每一段可以明確標記其底空間、更新組織與觀察方式。

## 3.7 Transition Law $\lambda$

局部 transition 再帶：

$$
\lambda\in\mathfrak L_3=\{\mathsf F,\mathsf K,\mathsf Q\}.
$$

因此 $(p,\lambda)$ 構成該段 local computational configuration。

---

# 4. 「一」至少有五種不同語義

本文至少區分：

$$
1_{\mathrm{syn}},
1_{\mathrm{if}},
1_{\mathrm{top}},
1_{\mathrm{sem}},
1_{\mathrm{phy}}.
$$

## 4.1 Syntactic Unit

語法上一個單位。例如 `do_task()` 是一次呼叫，但可能隱藏大量操作。

## 4.2 Interface Unit

API 或 UI 暴露的一個 action。例如一個 HTTP request 或 `smart_move("bank")`。

## 4.3 Topological Unit

在當前 execution topology 中的一個 node / edge transition。如果原本多階 traversal 被真正改寫成新的直接 transition，才可能在這一層真正縮短。

## 4.4 Semantic Unit

相對 task contract，內部差異暫時不重要的一個工作單位。例如 `bank_and_return` 可以包含 move、inventory scan、deposit 與 return，但在上層任務語義中仍是一個 operation。

## 4.5 Physical Unit

相對某個物理或硬體模型的一次操作。本文不宣稱它是宇宙最終不可約原子。

因此：

$$
\boxed{
\text{syntactic one}
\neq
\text{computational one}.
}
$$

---

# 5. 「包成一」與「真的變成一」

若：

$$
\Gamma=a_1\rightarrow\cdots\rightarrow a_{10},
$$

至少存在四種壓縮：

1. Naming Compression：只是給十步一個名字；
2. Interface Compression：caller 只看到一個 API；
3. Topological Compression：實際 execution topology 變短；
4. Computational Crystallization：新路徑經驗證後被升格成新的 reusable primitive。

因此：

$$
\boxed{
\text{Naming}
\neq
\text{Interface}
\neq
\text{Topology}
\neq
\text{Crystallization}.
}
$$

---

# 6. 並行揭示「十個可以同時是一和十」

若：

$$
a_1,\ldots,a_{10}
$$

互相獨立，則：

$$
W=10,
$$

但在資源足夠時：

$$
D=1.
$$

若 observer 只關心整批完成，還可以有：

$$
H_o=1.
$$

因此：

$$
\boxed{
(W,D,H_o)=(10,1,1).
}
$$

這不是矛盾，而是三種不同度量。

---

# 7. 計算路徑長度必須向量化

本文提出：

$$
\boxed{
\mathbf L_\chi(\Gamma)
=
(H,W,D,T,M,X).
}
$$

其中：

- $H$：hop count；
- $W$：total work；
- $D$：causal / parallel depth；
- $T$：wall-clock；
- $M$：memory / materialization；
- $X$：cross-boundary transitions。

後續可擴充 communication、verification、energy、observation loss、precompute、update、maintenance。

---

# 8. 「最短」不是單值概念

若路徑 A：

$$
H_A=3,
\qquad
W_A=100,
$$

而路徑 B：

$$
H_B=10,
\qquad
W_B=30,
$$

則沒有脫離 objective 的「誰比較短」。

定義：

$$
J_\omega(\Gamma)
=
\omega_HH+
\omega_WW+
\omega_DD+\cdots
$$

再有：

$$
\boxed{
\Gamma^*_{\chi,\omega}
=
\arg\min_\Gamma J_\omega(\Gamma\mid\chi).
}
$$

因此：

$$
\boxed{
\text{Shortest}
=
\text{chart-relative and objective-relative}.
}
$$

---

# 9. 向下展開：一重新變成多

定義 refinement operator：

$$
\boxed{
R_\downarrow:
u^{(k)}
\rightarrow
\{u_1^{(k-1)},\ldots,u_n^{(k-1)}\}.
}
$$

它回答：

> 這個目前被視為「一」的東西，裡面到底是什麼？

因此 algorithm 可以展開成 modules，module 可以展開成 functions，function 可以展開成 statements，並持續遞歸。

---

# 10. 向上收斂：多也可以變成新的一

定義 coarse-graining：

$$
\boxed{
R_\uparrow:
\{u_1^{(k)},\ldots,u_n^{(k)}\}
\rightarrow
u^{(k+1)}.
}
$$

但任何 syntactic grouping 都可以 coarse-grain。

真正值得研究的是：

$$
\boxed{
K:\Gamma^{(k)}\rightarrow\kappa^{(k+1)}.
}
$$

這就是 Computational Crystallization。

---

# 11. Earned Primitive｜獲得式原語

本文提出：

> 一個低層結構經過穩定化、驗證、壓縮與有效度證明後，在較高層被合法視為預設計算單位。

形式：

$$
\boxed{
\operatorname{EarnedPrimitive}(\Gamma,D,V,U)=\kappa.
}
$$

其中：

- $D$：valid domain；
- $V$：verification；
- $U$：lifecycle utility。

這個 primitive 不是天然的，而是「賺到」的。

---

# 12. Earned 不代表不可逆

任何高層 primitive 應保留：

$$
\boxed{
\operatorname{Decrystallize}(\kappa)\rightarrow\Gamma.
}
$$

因此：

$$
\boxed{
\text{primitive}
\neq
\text{opaque black box}.
}
$$

必須保存 provenance、source path、guard、validator、invalidation condition 與 fallback。

---

# 13. 點不一定是最小的

一個高層 point：

$$
v^{(k)}
$$

可以在 finer chart 展開成：

$$
\mathcal W^{(k-1)}.
$$

因此：

$$
\boxed{
\text{Point}^{(k)}
=
\text{World}^{(k-1)}
}
$$

可以作為 scale-relative relation 成立。

反方向，一整個 world 也可以在更高層 orchestration 中成為一個 node。

這不是本體等價，而是 projection relation。

---

# 14. 與 Mathematical World Theory 的接口

MWT 採 $\mathbf W$ 為 World primitive，而 graph、tuple、state machine、field、manifold 等都是 World presentation。

因此本文明確規定：

$$
\boxed{
\text{unitization acts on presentations, not on World ontology itself}.
}
$$

即真正被 unitize 的是：

$$
U_\chi\left(\rho_{\alpha,O,t}(\mathbf W)\right),
$$

而不是宣稱直接把 World 本體切成天然原子。

---

# 15. 與 Global Computation Methodology 的接口

GCM 允許 Runtime 動態建立：

$$
\mathcal D_t=\{D_1,\ldots,D_n\}.
$$

Domain 不是永久本體分割，而是 Runtime 為計算建立的作用範圍。

因此 unitization 可以被理解為 domain induction 的局部版本。

不同 chart：

$$
\chi_1\neq\chi_2
$$

可以得到：

$$
\mathcal D_t^{\chi_1}
\neq
\mathcal D_t^{\chi_2}.
$$

---

# 16. 與 24／72 的接口

本文不把 granularity、scale、observer、geometry 全部直接乘入 24／72，避免產生分類爆炸。

維持：

$$
\boxed{
24/72
=
\text{local computational configuration}.
}
$$

而：

$$
g,\sigma,o,\kappa,\tau
$$

屬於 route chart。

所以不同尺度的 unit 可以使用不同 computational form：

$$
\boxed{
p^{(k)}\neq p^{(k+1)}
}
$$

完全合法。

例如：

```text
micro: D-P-D-F
meso:  D-J-D-F
macro: C-P-C-K
meta:  D-R-D-F
```

---

# 17. 同一演算法不是永遠同一個「一」

一個演算法 $A$ 在 programmer chart 中可能是一個 unit；在 profiler chart 中可能是 functions；在 distributed runtime 中可能是 tasks；在 user chart 中又可能只是一個 action。

所以應寫：

$$
\boxed{
\operatorname{Cardinality}_\chi(A)
}
$$

而不是假設存在唯一：

$$
\operatorname{Cardinality}(A).
$$

---

# 18. Source Structure 不等於 Execution Structure

一行程式碼、一個函式、一個 AST node，都不應被直接當成實際 execution unit。

compiler optimization、JIT、vectorization、GPU offload、partial evaluation、memoization 都可能改變 execution topology。

因此：

$$
\boxed{
\text{Source Structure}
\neq
\text{Execution Structure}.
}
$$

---

# 19. Chart Selection 本身也有成本

如果 AI 要判斷現在應該看 instruction、function、module 或 world，則：

$$
\operatorname{SelectChart}
$$

本身就是計算。

因此：

$$
\boxed{
C_{\mathrm{total}}
=
C_{\mathrm{chart}}
+
C_{\mathrm{route}}
+
C_{\mathrm{execute}}
+
C_{\mathrm{verify}}
+\cdots
}
$$

不能把 chart selection 當成免費 oracle。

---

# 20. 過細與過粗都會失敗

如果粒度太細，可能出現 state explosion、routing overhead、context explosion、verification explosion。

所以：

$$
\boxed{
\text{maximum resolution everywhere}
}
$$

不是合理策略。

如果粒度太粗，又可能隱藏 bottleneck、causal dependency、side effect、parallelism，並產生 false shortest path。

所以：

$$
\boxed{
\text{one giant macro}
}
$$

也不是合理策略。

---

# 21. Task-Relative Unitization

最佳粒度應相對任務：

$$
\boxed{
g^*
=
\arg\min_g
J\left(U_g(\mathcal C)\mid q,o,B,R\right).
}
$$

其中：

- $q$：task；
- $o$：observer；
- $B$：budget；
- $R$：risk / correctness requirement。

同理，debug、planning、execution、audit 可以需要不同 scale。

因此：

$$
\boxed{
\text{Scale Selection}
=
\text{Runtime Decision}.
}
$$

---

# 22. Unitization Receipt

任何重要 unitization 最好留下：

$$
\boxed{
\operatorname{UnitReceipt}
=
\langle\chi,S,R,V,C,t\rangle.
}
$$

其中：

- $\chi$：chart；
- $S$：source structure；
- $R$：reason；
- $V$：validation；
- $C$：cost；
- $t$：version / epoch。

這樣未來才可以回答：

> 為什麼這十個 operation 被視為一？

---

# 23. Representational Unitization 與 Computational Reunitization

若只是：

$$
U_{\chi_1}(\mathcal C)
\rightarrow
U_{\chi_2}(\mathcal C)
$$

而 execution 完全沒變，這只是：

$$
\boxed{
\text{Representational Unitization}.
}
$$

若重新切分後 execution topology 也變：

$$
\mathcal C\rightarrow\mathcal C',
$$

且：

$$
\operatorname{Semantics}(\mathcal C')
\simeq
\operatorname{Semantics}(\mathcal C),
$$

同時：

$$
J(\mathcal C')<J(\mathcal C),
$$

才稱：

$$
\boxed{
\text{Computational Reunitization}.
}
$$

---

# 24. UNPNP-I 與本文的關係

UNPNP-I 已建立：complexity transfer、subspace hyperlink、Adaptive Corridor、Path Compilation、Computational Crystallization、EHPE 與 Safe Reachable World。

本文不推翻其中任何一項。

本文補的是：

$$
\boxed{
\text{what counts as a path segment?}
}
$$

原本：

$$
\operatorname{PC}(\Gamma)=\widehat\ell.
$$

現在可以寫成：

$$
\boxed{
\operatorname{PC}_\chi(\Gamma)
=
\widehat\ell_{\chi'}.
}
$$

甚至：

$$
\chi'\neq\chi.
$$

也就是 Path Compilation 可能同時改寫 route 與 chart。

---

# 25. Route-to-Point Transition

若：

$$
\Gamma^{(k)}
$$

被結晶：

$$
K(\Gamma^{(k)})=\kappa^{(k+1)},
$$

則在上層 chart：

$$
\boxed{
\Gamma^{(k)}
\sim
v^{(k+1)}.
}
$$

一條 route 可以成為一個 point。

遇到 debug、shift、invalidation、anomaly 或 audit 時，又可以反向：

$$
v^{(k+1)}
\rightarrow
\Gamma^{(k)}.
$$

因此：

$$
\boxed{
\text{Point}
\leftrightarrow
\text{Route}
}
$$

是多尺度計算中的雙向關係。

---

# 26. 五條核心定律

### 定律一

$$
\boxed{
\textbf{There is no scale-free computational one.}
}
$$

不存在脫離尺度的「計算的一」。

### 定律二

$$
\boxed{
\textbf{One interface action does not imply one computational transition.}
}
$$

介面上的一，不等於計算拓撲上的一。

### 定律三

$$
\boxed{
\textbf{A verified route may become one primitive at a higher scale.}
}
$$

一條已驗證路徑，可以在更高尺度成為新的「一」。

### 定律四

$$
\boxed{
\textbf{Unitization is observer-relative but not arbitrary.}
}
$$

observer-relative 不等於任意，仍受 semantics、causality、resource、verification、provenance 約束。

### 定律五

$$
\boxed{
\textbf{Shortest-route claims are incomplete until the unitization chart is specified.}
}
$$

沒有先說「一步怎麼算」，就不能完整地說哪條路最短。

---

# 27. 從 Absolute Shortest Path 到 Relative Shortest Route

原本：

$$
\Gamma^*=\arg\min_\Gamma C(\Gamma).
$$

本文改成：

$$
\boxed{
\mathcal R^*_{\chi,\omega}
=
\arg\min_{\mathcal R}
J_\omega(\mathcal R\mid\chi).
}
$$

如果 chart 本身也可選：

$$
\boxed{
(\mathcal R^*,\chi^*)
=
\arg\min_{\mathcal R,\chi}
J(\mathcal R,\chi\mid\mathbf W,q,B,R).
}
$$

這才是後續 Multi-Scale Computational Route Theory 的真正入口。

---

# 28. 這不是要求暴力搜尋全部 Chart

 $|\mathfrak X|$ 可能巨大。

所以未來需要：

- adaptive chart selection；
- coarse-to-fine refinement；
- local revealing；
- crystal reuse；
- GCM routing；
- 24／72 configuration switching；
- chart invalidation。

因此 chart search 自己也需要 corridor 與 crystallization。

---

# 29. 對 AI-native Runtime 的意義

AI 不應只問：

> 下一步做什麼？

還應能問：

> 我是不是看得太細？

> 這一串已經成熟到可以視為一個 primitive 了嗎？

> 這個目前被視為「一」的東西是否需要重新打開？

所以新 runtime loop 可以寫成：

```text
Observe
→ Choose Scale
→ Unitize
→ Route
→ Execute
→ Verify
→ Crystallize / Decrystallize
→ Re-unitize
```

---

# 30. 對高階 AI 思考成本的意義

如果所有已知工作永遠重新展開到最低尺度：

$$
C_{\mathrm{reason}}
$$

會持續膨脹。

成熟系統應允許：

$$
\boxed{
\text{known structure}
\rightarrow
\text{higher-level earned primitive}.
}
$$

只有在 novelty、failure、distribution shift 或 audit 出現時才向下 refinement。

---

# 31. Abstraction 必須搭配 Reopenability

高階抽象不能永久遮蔽低階錯誤。

若：

$$
\kappa^{(k+1)}
$$

失敗，必須可以：

$$
\kappa^{(k+1)}
\rightarrow
\Gamma^{(k)}
\rightarrow
\Gamma^{(k-1)}.
$$

因此：

$$
\boxed{
\text{abstraction}
+
\text{reopenability}
}
$$

必須同時成立。

---

# 32. 對軟體工程的重新理解

傳統 abstraction 強調 hiding implementation details。

本文更強調：

$$
\boxed{
\text{compress implementation for ordinary use}
+
\text{preserve lawful decompression for verification}.
}
$$

即：

$$
\text{abstraction}
\neq
\text{forgetting}.
$$

---

# 33. 對演算法分析的重新理解

經典複雜度分析本身沒有問題，因為它通常先指定 machine model 與 primitive set。

本文只是指出：

$$
\boxed{
\text{complexity result}
=
\text{result relative to a computational model and primitive set}.
}
$$

在 AI-native Runtime 中，primitive set 自己也可能成為 adaptation 的研究對象。

---

# 34. P/NP 邊界仍然保留

本文不主張：

> 把昂貴計算包成一個 primitive，就能把 NP 問題變成 P。

若：

$$
\Gamma\rightarrow\kappa,
$$

仍必須計入 build、training、indexing、compilation、verification、maintenance、storage 等成本。

因此：

$$
\boxed{
\text{unit count reduction}
\neq
\text{complexity elimination}.
}
$$

這與 UNPNP-I 的 complexity transfer 完全一致。

---

# 35. 真正新增的是 Unit Boundary 成為變數

以前：

$$
C(\Gamma)
$$

中的 $\Gamma$ 已經被切好了。

現在：

$$
\boxed{
\Gamma=\Gamma(\chi).
}
$$

所以：

$$
C(\Gamma)=C(\Gamma(\chi)).
$$

而 $\chi$ 本身也必須進入 optimization。

---

# 36. 研究可反駁條件

本文至少在以下情況需要修正：

1. computational unitization 無法在實際 runtime 中產生可重複效用；
2. observer / scale 差異只是語言重述，對 routing 與 cost 沒有實質作用；
3. route-to-point crystallization 完全可被既有 abstraction 解釋，且沒有新增分析價值；
4. chart-selection overhead 長期高於 optimization gain；
5. granularity switching 無法可靠驗證；
6. unitization receipt 無法支援 debug、replay 與 provenance。

---

# 37. 實驗接口

第一批實驗可以直接利用：

- Generative Agents；
- Adventure Land；
- synthetic world；
- compiler traces；
- workflow runtime。

比較：

$$
\chi_{\mathrm{fine}}
$$

與：

$$
\chi_{\mathrm{coarse}}
$$

下的：

- unit count；
- work；
- depth；
- latency；
- reasoning calls；
- verification；
- crystal hit rate。

---

# 38. 與 Paper 02 的接口

本文回答：

> 什麼算一步？

下一篇回答：

> 如果「一步」本身是相對的，那麼「最短」還能不能被定義？

即：

**Paper 02｜最短路徑不存在於真空中：Observer、Granularity、Scale 與 Objective-Relative Shortest Routes**

---

# 結論

計算理論通常從 primitive operations 開始。

但 AI-native 計算世界迫使我們再往前問：

> primitive 到底從哪裡來？

本文的回答是：

$$
\boxed{
\text{primitive}
=
\text{unit relative to a computational chart}.
}
$$

因此：

$$
\boxed{
1_{\mathrm{instruction}}
\neq
1_{\mathrm{function}}
\neq
1_{\mathrm{algorithm}}
\neq
1_{\mathrm{world}}
}
$$

並不矛盾。

它們只是不同尺度的「一」。

一個低層 world 可以在高層成為一個 point；一條低層 path 可以在高層成為一條 edge；一組經驗證操作可以在更高層成為新的 primitive。

因此：

$$
\boxed{
\text{Point}^{(k)}
=
\text{World}^{(k-1)}
}
$$

與：

$$
\boxed{
\text{Path}^{(k)}
\rightarrow
\text{Primitive}^{(k+1)}
}
$$

成為 UNPNP-II 的第一組基本關係。

這也意味著，任何「最短路徑」主張在沒有指定：

- 什麼算一步；
- 站在哪個尺度；
- 誰在觀察；
- 看的是工作量、因果深度、時間還是 interface hop；

以前，都不完整。

因此本文最終濃縮為：

$$
\boxed{
\textbf{
沒有脫離尺度的計算之一，
也沒有脫離計算之一的最短路徑。
}
}
$$

而這正是 UNPNP 從「改寫路徑」走向：

$$
\boxed{
\textbf{
改寫什麼叫一步、什麼叫路，以及什麼可以成為新的計算原語
}
}
$$

所需要的第一個正式定義。
