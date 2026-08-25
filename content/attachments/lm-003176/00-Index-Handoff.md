# 從計算 24／72 範式到全域計算方法論
## 理論地圖、實驗回投與後續系列交接索引 v0.1

- 系列：Global Computation Methodology Series
- 文件性質：總綱 / canonical handoff / theory map
- 日期：2026-08-23
- 作者：Neo.K
- 協作：Aletheia / GPT
- 狀態：公開版草稿
- 邊界聲明：本文是理論整合文件，不宣稱建立新的計算複雜度定理、物理定律或通用最優調度定理。

---

## 摘要

本文件整理一條由「計算形態分類」逐步推進到「全域計算方法論」的研究路徑。其起點是計算 24 範式與七十二格計算動力學：前者嘗試將計算的底空間、更新組織與觀察方式分解成一個可組合的計算形態空間；後者再加入轉移律軸，使同一計算形態可以在確定、機率或量子等不同演化語義下運行。

這兩者的初始角色偏向分類學與形式空間，但後續 Runtime Routing、GCRGDC、MWT 與 DGW 實驗顯示：真正重要的問題不只是「一個計算屬於哪一格」，而是「世界中的不同作用域如何同時採用不同計算形態、如何被全域約束耦合、如何依解析度物化、如何被觀察者投影，以及如何在有限活動支援下保留無界展開能力」。

因此，本系列提出新的上層定位：

$$
\boxed{
\mathfrak P_{24},\mathfrak P_{72}
=
\text{Computational Configuration Spaces}
}
$$

而不是完整的全域計算理論本身。全域計算方法論研究的是：給定一個世界狀態、若干作用域、若干候選計算形態、轉移律、資源與全域約束，如何形成一個可演化、可組合、可切換、可局部物化、可歷史追溯的 Runtime。

核心命題是：

$$
\boxed{
\text{Global Computation}
\neq
\text{One Computation Everywhere}
}
$$

而應理解為：

$$
\boxed{
\text{Global Computation}
=
\text{Globally Coherent Heterogeneous Computation}
}
$$

---

# 1. 從「計算模型」到「計算配置」

傳統計算理論通常從某一種固定模型出發，例如圖靈機、RAM、Actor、資料流、cellular automata、hybrid automata、stochastic process 或 quantum circuit。每一種模型都透過選定 primitive 建立嚴格語義。

但若研究對象本身是一個多域、多尺度、多觀察者、異質硬體與多種更新律同時存在的世界，那麼一個固定模型未必適合成為唯一上層表示。

因此問題應改寫為：

> 一個 Runtime 是否可以把「使用哪一種計算形態」本身也視為可配置、可切換、可組合的狀態？

---

# 2. 計算 24 範式

最小形式為：

$$
\boxed{
\mathfrak P_{24}
=
\mathfrak B_2
\times
\mathfrak U_4
\times
\mathfrak O_3
}
$$

其中：

$$
\mathfrak B_2=\{C,D\}
$$

表示 continuous-like / discrete-like 底空間；

$$
\mathfrak U_4=\{S,J,P,R\}
$$

表示 sequential、jump/selective、parallel、recognition/retrieval 更新組織；

$$
\mathfrak O_3=\{C,D,X\}
$$

表示 continuous observation、discrete observation、cross/mixed observation。

因此：

$$
|\mathfrak P_{24}|=2\times4\times3=24.
$$

24 的用途不是宣稱宇宙只有 24 種計算，而是提供一個有限、可尋址、可比較的 Runtime configuration basis。

---

# 3. 七十二格計算動力學

加入轉移律：

$$
\mathfrak L_3=\{F,K,Q\}
$$

其中：

- $F$：function-like deterministic transition；
- $K$：classical stochastic kernel；
- $Q$：quantum channel-like transition。

因此：

$$
\boxed{
\mathfrak P_{72}
=
\mathfrak P_{24}
\times
\mathfrak L_3
}
$$

$$
|\mathfrak P_{72}|=72.
$$

一句話：

$$
\boxed{
24=\text{How computation is organized}
}
$$

$$
\boxed{
72=\text{How that computational form evolves}
}
$$

---

# 4. 24/72 為什麼還不夠

24/72 仍未回答：

1. 哪個作用域使用哪一格？
2. 不同域可否同時使用不同格？
3. 何時切換 computational form？
4. 何時切換 transition law？
5. 哪些狀態需要 materialize？
6. 觀察者切換解析度是否改變世界本身？
7. 如何在有限資源下保留無界遞歸展開？
8. 終點相同但歷史不同是否等價？
9. 異質 local solvers 如何形成 global legality？

這些問題把研究從 taxonomy 推向 Runtime methodology。

---

# 5. MWT 的回投

MWT 的基礎分界是：

$$
\boxed{
\mathbf W
\neq
\text{World 的任何單一表示}
}
$$

Runtime tuple、圖、場、空間、狀態機都只是 World 的有限表示或展開語言。

因此全域計算方法論不應把某一 Runtime representation 升格成 World 本身。

---

# 6. GCRGDC 的回投

GCRGDC 建立：

$$
\boxed{
\text{Computation}
\neq
\text{Observation}
}
$$

世界持續演化：

$$
\mathfrak G_t\xrightarrow{\Phi_G}\mathfrak G_{t+1},
$$

Observer 取得：

$$
Y_O(t)=\Pi_O(\mathfrak G_t).
$$

因此：

$$
\boxed{
\text{local observation}
\not\Rightarrow
\text{local-only computation}
}
$$

這個分界後來成為 DGW 實驗的核心之一。

---

# 7. DGW 的真正研究價值

DGW 使用幾何只是為了讓 Runtime 問題可見。

## 7.1 Observer 與 world evolution 分離

Focus、Zoom、Contextual / Immersive、Lens、projection layer 切換不得偷偷推進 world epoch：

$$
\Delta t_{\mathrm{world}}=0.
$$

## 7.2 無界遞歸與有限活動視窗

世界可以概念上：

$$
W_0\to W_1\to W_2\to\cdots
$$

但 Runtime 只維持有限 active horizon：

$$
|\mathcal H_{\mathrm{active}}|\le 3.
$$

所以：

$$
\boxed{
\text{Finite Active Realization}
+
\text{Unbounded Extensibility}
}
$$

## 7.3 Materialization 不等於計算存在

尚未被 UI 展開的 child state 仍可存在於 canonical world。

因此：

$$
\boxed{
\text{Materialization}
\neq
\text{Computation Start}
}
$$

## 7.4 失敗實驗的價值

DGW 曾出現「active nodes 已固定，但每 tick 還掃所有 dormant history」的效能錯誤。

因此得到：

$$
\boxed{
\text{Bounded Active Semantics}
\neq
\text{Bounded Runtime Cost}
}
$$

若 clone、scan、render、archive access 沒有同步收斂，理論上的 bounded active support 仍不足以保證工程成本 bounded。

---

# 8. 全域計算方法論的最小形式

提出：

$$
\boxed{
\mathcal M_G
=
\langle
W,
\mathfrak P,
\mathfrak L,
\mathcal D,
\Lambda,
\mathcal C,
\mathcal S,
\Pi,
\mathcal H
\rangle
}
$$

其中：

- $W$：world state presentation；
- $\mathfrak P$：computational form space；
- $\mathfrak L$：transition-law family；
- $\mathcal D$：domains；
- $\Lambda$：resolution / materialization policy；
- $\mathcal C$：global constraints / couplings；
- $\mathcal S$：scheduling / composition / routing；
- $\Pi$：observer projections；
- $\mathcal H$：history / provenance。

對每個 domain：

$$
p_i(t)\in\mathfrak P,
\qquad
\ell_i(t)\in\mathfrak L.
$$

局部演化：

$$
\Phi_i^{p_i,\ell_i}.
$$

全域演化：

$$
\boxed{
\Phi_G(t)
=
\operatorname{Compose}_{\mathcal C_G(t)}
\left(
\Phi_1^{p_1,\ell_1},
\dots,
\Phi_n^{p_n,\ell_n}
\right)
}
$$

並：

$$
W_{t+1}=\Phi_G(t)(W_t).
$$

---

# 9. 全域的重新定義

Global 不等於：

- all-to-all；
- 同一算法；
- 同一資料表示；
- 同一時間步；
- 全部 materialize；
- 全部同步 barrier。

而是：

$$
\boxed{
\text{Global}
=
\text{coherence relative to a designated World boundary}
}
$$

同一操作可以：

$$
\mathrm{Global}_{W}(\mathcal U)
\land
\mathrm{Local}_{H}(\mathcal U).
$$

---

# 10. 相關研究的定位

本系列與既有研究有明確交集：

1. **Heterogeneous computing**：處理 CPU/GPU/accelerator 的映射、同步與資源配置。
2. **Task/dataflow runtime**：把計算轉成 task graph，再做 temporal/spatial scheduling。
3. **Hybrid systems**：研究 continuous dynamics 與 discrete transition 的組合。
4. **Edge/cloud scheduling**：研究不同節點與資源的動態 offloading。
5. **Stochastic / quantum process semantics**：提供不同 transition law 的既有數學基礎。

本系列不取代這些領域，而是問：

> 若 computational form、transition law、domain、resolution 與 observation 都可以成為 Runtime configuration，如何建立統一的 global composition 方法論？

---

# 11. 六篇核心論文

Series-00 之外，正式規劃：

1. **全域計算方法論：異質計算的全域一致組合**
2. **計算形態空間：從 24 範式與 72 格動力學到可路由計算配置**
3. **動態計算路由：多域、多範式與異質轉移律的 Runtime 組合**
4. **計算不等於觀察：全域演化、局部物化與解析度相對計算**
5. **有限活動實現與無界計算展開：遞歸世界的資源受限全域計算**
6. **終點不等於歷史：非交換計算序列、世界狀態與可追溯全域演化**

---

# 12. 核心命題總表

$$
\boxed{
\text{Computation}\neq\text{Observation}
}
$$

$$
\boxed{
\text{Global Computation}\neq\text{One Computation Everywhere}
}
$$

$$
\boxed{
\text{Global Computation}
=
\text{Globally Coherent Heterogeneous Computation}
}
$$

$$
\boxed{
\text{Global Dependency}
\neq
\text{Full Materialization}
}
$$

$$
\boxed{
\text{Recursive Globality}
\neq
\text{Recursive Full Expansion}
}
$$

$$
\boxed{
\text{Finite Active Realization}
+
\text{Unbounded Extensibility}
}
$$

$$
\boxed{
\text{State Equality}
\not\Rightarrow
\text{History Equality}
}
$$

---

# 13. 結論

24/72 的價值不是提供一張分類表，而是提供一個 Runtime 可以操作的 computational configuration space。GCRGDC 與 DGW 的價值也不只是幾何，而是把 observation、materialization、recursive globality、bounded active support 與 heterogeneous composition 變成可執行問題。

因此整條路徑可壓成：

$$
\boxed{
\text{Computational Taxonomy}
\to
\text{Computational Configuration Space}
\to
\text{Runtime Routing}
\to
\text{Global Computation Methodology}
}
$$

---

## 參考文獻與相關工作（精選）

1. Fang, J., Huang, C., Tang, T., & Wang, Z. *Parallel Programming Models for Heterogeneous Many-Cores: A Survey*. 2020.
2. De Matteis, T., Gianinazzi, L., de Fine Licht, J., & Hoefler, T. *Streaming Task Graph Scheduling for Dataflow Architectures*. 2023.
3. Taha, W. M., Taha, A.-E. M., & Thunberg, J. *Hybrid Systems*. 2020.
4. Boné, A. et al. *A task-based data-flow methodology for programming heterogeneous systems with multiple accelerator APIs*. 2026.
5. *Towards an Optimized Heterogeneous Distributed Task Scheduler in OpenMP Cluster*. IEEE SC24-W, 2024.
6. *CaRCS: Joint Optimization of Computing-Aware Routing and Collaborative Scheduling in Computing Power Networks*. IEEE Network, 2025.
