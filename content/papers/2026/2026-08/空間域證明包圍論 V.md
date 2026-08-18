# 空間域證明包圍論 V
## Discovery–Verification Inversion：編譯證明空間、Frontier Drift 與驗證主導相位
### Spatial-Domain Proof Enclosure V: Discovery–Verification Inversion, Compiled Proof Space, Frontier Drift, and Verification-Dominated Regimes

**Version:** v0.1  
**Date:** 2026-08-14  
**Status:** theorem / hypothesis / benchmark framework; not a claim that mathematical discovery generically accelerates  
**Canonical source:** UTF-8 Markdown; canonical mathematics uses ` $...$ ` and `$$...$$` only.

---

## 摘要

空間域證明包圍論前四篇依次建立：sound survivor envelope、route representation faithfulness、global coverage / closure certificate，以及 proof trace compilation / incremental replay。Paper 04 因而第一次使「已證歷史不必每輪重算」成為一個可驗證的計算命題，但它刻意沒有證明更強的直覺：

> 當 survivor domain 持續收縮、proof trace 持續累積並被編譯後，後續 theorem discovery 是否真的會越來越便宜，而研究成本逐步轉移到 verification、coverage、gluing 與 maintenance？

本文正式研究此現象，稱為 **Discovery–Verification Inversion**，簡稱 DVI。

本文首先證明必須區分兩種 discovery cost。第一種是**已知域／例行查詢解析成本**

$$
D_t^{\mathrm{resolve}},
$$

即候選 route state 是否已被 active certificates、closure basis 或 compiled pruning state 解決。第二種是**frontier discovery cost**

$$
D_t^{\mathrm{frontier}},
$$

即找到下一個真正改變 survivor envelope、typed gap、RouteCert 或 Global Closure Certificate 的非冗餘 theorem cut 所需成本。

對固定 query distribution，若 compiled region 單調擴張且 compiled-hit cost 不高於 full resolution cost，本文證明

$$
\boxed{
D_{t+1}^{\mathrm{resolve}}
\le
D_t^{\mathrm{resolve}}.
}
$$

這是一個真正的 compilation monotonicity theorem。但若研究 query distribution 本身向剩餘 frontier 漂移，成本差可精確分解為

$$
\boxed{
\Delta D_t^{\mathrm{resolve}}
=
-G_t^{\mathrm{compile}}
+
P_t^{\mathrm{drift}},
}
$$

其中 $G_t^{\mathrm{compile}}$ 是新增 compiled region 帶來的節省，而 $P_t^{\mathrm{drift}}$ 是研究重心向更難 survivor frontier 移動造成的分布漂移項。只有當

$$
G_t^{\mathrm{compile}}>P_t^{\mathrm{drift}}
$$

時，例行 query-resolution 才保證加速。

本文進一步證明一個重要 no-go：若 query distribution 被嚴格限制在 unresolved frontier 上，則 compiled-hit 的直接收益為零。故

$$
\boxed{
\text{known-region acceleration}
\not\Rightarrow
\text{frontier theorem discovery acceleration}.
}
$$

因此本文把 DVI 分為弱式與強式。**Weak DVI** 只要求例行解析成本下降且 verification share 上升；**Strong DVI** 則要求每個非冗餘 frontier theorem cut 的 discovery cost 也呈下降趨勢。後者不是本文定理，而是可否證研究假說。

令

$$
W_t
=
C_t^{\mathrm{verify}}
+C_t^{\mathrm{coverage}}
+C_t^{\mathrm{glue}}
+C_t^{\mathrm{maintain}}
+C_t^{\mathrm{replay}}
$$

為 verification bundle，定義 verification share

$$
\boxed{
\sigma_t
=
\frac{W_t}{D_t+W_t}.
}
$$

本文證明：若 $D_t$ 下降且 $W_t$ 上升，則 $\sigma_t$ 必定上升。更進一步，如果 discovery savings 大於 verification growth，則可以同時出現

$$
\boxed{
\text{total cost 下降}
\quad+
\text{verification share 上升}.
}
$$

這正是「研究整體越來越快，但最後主要時間花在驗證」的數學上可一致情形。

本文最後提出一套 **DVI Benchmark Protocol**，要求固定模型／工具版本、 paired cold-vs-compiled runs、隨機化 task order、完整計入 build / indexing / maintenance 成本、把 routine-resolution 與 frontier discovery 分開計量，並以 formal checker / proof kernel 驗證所有 accepted proof artifacts。只有在此類 longitudinal benchmark 中觀察到可重現趨勢，才可聲稱 DVI 發生。

本文因此得到的最強結論不是「後期研究必然越來越快」，而是：

$$
\boxed{
\textbf{SDPE 中的速度反轉可以被精確分解、測量、證偽，並與單純 cache speedup 嚴格區分。}
}
$$

---

## 關鍵詞

空間域證明包圍；Discovery–Verification Inversion；proof compilation；frontier drift；verification dominance；proof reuse；incremental verification；survivor space；frontier hardening；amortization；AI theorem proving；longitudinal benchmark

---

# 1. 前四篇留下的正式狀態

考慮全域命題

$$
\forall d\in D,\;P(d),
$$

真實反例集合為

$$
\mathcal C
=
\{d\in D:\neg P(d)\}.
$$

Paper 01 維持 sound survivor invariant：

$$
\boxed{
\mathcal C\subseteq\Omega_t.
}
$$

Paper 02 要求 route representation 不得把 proof-relevant counterexample fibers 靜默壓掉。

Paper 03 建立 Global Closure Certificate：

$$
\mathsf{GCC}
=
\langle
Master,Atlas,CoverCert,LocalCerts,BoundaryCert,LiftCerts,
GlueMode,GlueCert,DepDAG,Version,Replay
\rangle.
$$

Paper 04 把已驗證歷史編譯為 dependency DAG、closure basis、support index 與 incremental replay state。對 route state $x$，

$$
\kappa_t(x)
=
\#\{v\in A_t:x\in E_v\}
$$

表示 active exclusion support multiplicity；若

$$
\kappa_t(x)>0,
$$

則至少一張 active sound certificate 已排除 $x$。

Paper 04 因而證明：

$$
\boxed{
\text{verified proof history}
\to
\text{compiled pruning state}
}
$$

可以是 sound 的。

但它沒有證明：

$$
\boxed{
\text{compiled proof state}
\Longrightarrow
\text{frontier theorem discovery 越來越容易}.
}
$$

這正是本文要處理的區分。

---

# 2. Fresh literature grounding

## 2.1 Proof-state snapshotting：加速 reconstruction，不等於加速 discovery

Shen 與 Shi 2026 年的 Lean 4 proof-state snapshotting 工作指出，portfolio tactic search 的大量 wall time 可能來自每個 branch 重複載入 import 與重新 elaborating theorem context，而非 tactic 本身。其 48 個 miniF2F-v2 benchmark 中報告 5.6--50 倍 wall-time speedup。

該研究同時清楚區分：其主要 benchmark 測量的是 tactic-search infrastructure speed，而非一般 theorem discovery difficulty。

本文因此採用：

$$
\boxed{
\text{reconstruction avoidance}
\neq
\text{frontier discovery acceleration}.
}
$$

## 2.2 Proof-certificate recycling：verification 也可以被攤銷

Kaufmann 與 Hofstadler 2025 年的 algebraic proof certificate recycling 把重複 algebraic proof fragments 提煉成可再 instantiate 的 proof rules，並在其 checker 中降低 proof size 與 verification time。

因此 verification 不必被模型化成只能單調增加；它本身也可以受到 compilation / pattern reuse 影響。

這一點對 DVI 很重要：

$$
\boxed{
\text{verification share 上升}
\not\Rightarrow
\text{verification absolute cost 必然上升}.
}
$$

## 2.3 Accumulated proof knowledge：已有領域性 reuse evidence

CircuitProver 2026 在 63 個 hardware theorem-proving tasks 上累積 proving traces 與 verified theorems。其 ablation 報告 accumulated proof knowledge 減少 proof construction redundancy，降低 proof length 與 verification time。

LeanAgent 則從 lifelong theorem proving 角度研究持續擴張的 formal knowledge base 與 backward transfer。

這些工作支持「累積 verified proof knowledge 可改善後續任務」的可能性，但都不能推出一般數學研究中的 Strong DVI。

## 2.4 Dependency closure 也可能使 frontier 變難

VeriSoftBench 2026 收集 500 個 repository-scale Lean proof obligations，發現 success 與 transitive repository dependence 有顯著關聯：需要較大、多跳 dependency closure 的任務更難成功；只提供 curated dependency closure 比暴露整個 repository 好，但仍留有顯著困難。

這為本文的 **frontier-hardening counterforce** 提供直接外部背景：

$$
\boxed{
\text{knowledge base 變大}
\not\Rightarrow
\text{remaining theorem 變簡單}.
}
$$

## 2.5 Scalable strict verification 是獨立工作負擔

AXLE 2026 把 strict proof verification、metadata extraction、multi-version support 與 per-request isolation 作為大規模 Lean infrastructure 的核心功能，顯示在 AI theorem-proving workflow 中，verification 本身已是一個需要獨立 scale 的系統層。

本文不把 AXLE 的 throughput 當作 DVI evidence；它只支持 verification workload 應被獨立計量，而不能隱藏在「prover succeeded」一個 bit 裡。

---

# 3. 第一個關鍵區分：Routine Resolution 與 Frontier Discovery

## Definition 3.1 — Routine Resolution Cost

設 route-state space 為 $X$。時刻 $t$ 的 compiled-known region 定義為

$$
\boxed{
K_t
:=
\{x\in X:\kappa_t(x)>0\}
\cup
K_t^{\rm reusable},
}
$$

其中 $K_t^{\rm reusable}$ 可以包含已有 active RouteCert / verified pattern 能直接處理的 states。

對 query $x$，若 $x\in K_t$，使用 compiled path 的成本為

$$
c_H(x),
$$

若 $x\notin K_t$，完整展開成本為

$$
c_F(x),
$$

並假設

$$
0\le c_H(x)\le c_F(x).
$$

令研究 query distribution 為 $\mu_t$，定義例行解析成本：

$$
\boxed{
D_t^{\rm resolve}
:=
\int_X
\left[
\mathbf 1_{K_t}(x)c_H(x)
+
\mathbf 1_{X\setminus K_t}(x)c_F(x)
\right]
\,d\mu_t(x).
}
$$

這個量測的是「面對當前 query stream，已編譯證明空間替我們省掉多少重複展開」。

## Definition 3.2 — Frontier Discovery Cost

定義一個 theorem cut 為 **nonredundant**，若它至少改變下列之一：

$$
\Omega_t,
\qquad
\mathbf G_t,
\qquad
\mathsf{RouteCert}_t,
\qquad
\mathsf{GCC}_t,
$$

且該改變通過相應 checker / coverage / representation obligations。

令

$$
\boxed{
D_t^{\rm frontier}
}
$$

表示從進入 active unresolved frontier，到得到下一個 accepted nonredundant theorem cut 所需的完整 discovery resources。

可以用：

- model calls；
- tokens；
- CPU / GPU time；
- explored proof states；
- rejected theorem proposals；
- failed route branches；
- human mathematical review time；
- symbolic / numerical experiment cost；

等向量或加權 scalar 表示。

## No-Go 3.3 — 兩種 discovery cost 不可混淆

$$
\boxed{
D_t^{\rm resolve}\downarrow
\not\Rightarrow
D_t^{\rm frontier}\downarrow.
}
$$

proof cache、snapshot、compiled support index 首先直接影響的是前者。

後者只有在 survivor geometry、route branching、premise structure、proof distance 或 theorem interaction 真正變簡單時才會下降。

---

# 4. Fixed-Distribution Compilation Monotonicity

## Theorem 4.1 — Fixed-Distribution Compilation Monotonicity

假設：

1. query distribution 固定：

$$
\mu_{t+1}=\mu_t=\mu;
$$

2. compiled region 單調擴張：

$$
K_t\subseteq K_{t+1};
$$

3. hit / miss costs 在兩輪間不變；
4. 對所有 $x$：

$$
c_H(x)\le c_F(x).
$$

則：

$$
\boxed{
D_{t+1}^{\rm resolve}
\le
D_t^{\rm resolve}.
}
$$

### Proof

兩輪唯一可能改變成本的 points 位於

$$
K_{t+1}\setminus K_t.
$$

對這些 points，成本由 $c_F(x)$ 降為 $c_H(x)$。故

$$
D_t^{\rm resolve}
-
D_{t+1}^{\rm resolve}
=
\int_{K_{t+1}\setminus K_t}
(c_F-c_H)
\,d\mu
\ge0.
$$

 $\square$

## Corollary 4.2 — Strict acceleration condition

若

$$
\mu(K_{t+1}\setminus K_t)>0
$$

且在一個 positive-measure subset 上

$$
c_H<c_F,
$$

則：

$$
\boxed{
D_{t+1}^{\rm resolve}
<
D_t^{\rm resolve}.
}
$$

這是 SDPE 中第一個「已知域越大，例行解析越便宜」的真正 theorem。

---

# 5. Frontier Drift Decomposition

實際研究的 query distribution 通常不固定。隨著已知區域被編譯，研究者會主動把注意力移向未解 frontier。

因此上一節的 monotonicity theorem 需要加入 distribution drift。

## Definition 5.1 — Compilation Gain

令新增 compiled region 為

$$
\Delta K_t
=
K_{t+1}\setminus K_t.
$$

定義：

$$
\boxed{
G_t^{\rm compile}
:=
\int_{\Delta K_t}
(c_F-c_H)
\,d\mu_t.
}
$$

## Definition 5.2 — Frontier Drift Penalty

令新一輪 cost function 為

$$
c_{t+1}(x)
=
\mathbf 1_{K_{t+1}}c_H(x)
+
\mathbf 1_{X\setminus K_{t+1}}c_F(x).
$$

定義 distribution-shift term：

$$
\boxed{
P_t^{\rm drift}
:=
\int_X
c_{t+1}(x)
\,d(\mu_{t+1}-\mu_t)(x).
}
$$

此量可以為正、零或負。

## Theorem 5.3 — Exact Compilation–Drift Decomposition

在 $K_t\subseteq K_{t+1}$ 且 hit / miss cost functions 固定時：

$$
\boxed{
D_{t+1}^{\rm resolve}
-
D_t^{\rm resolve}
=
-G_t^{\rm compile}
+
P_t^{\rm drift}.
}
$$

### Proof

寫成：

$$
\int c_{t+1}\,d\mu_{t+1}
-
\int c_t\,d\mu_t
$$

並加減

$$
\int c_{t+1}\,d\mu_t.
$$

第一部分是固定舊 distribution 下的 compiled-region gain：

$$
\int(c_{t+1}-c_t)d\mu_t
=
-G_t^{\rm compile}.
$$

第二部分正是 distribution drift：

$$
\int c_{t+1}d(\mu_{t+1}-\mu_t)
=
P_t^{\rm drift}.
$$

 $\square$

## Corollary 5.4 — Acceleration balance condition

$$
\boxed{
D_{t+1}^{\rm resolve}<D_t^{\rm resolve}
\iff
G_t^{\rm compile}>P_t^{\rm drift}.
}
$$

這把「越來越快」第一次拆成兩個可量化的競爭項：

$$
\boxed{
\text{Compilation Gain}
\quad\text{vs}\quad
\text{Frontier Drift}.
}
$$

---

# 6. Frontier Cache Nullity

## Proposition 6.1 — Direct Compiled-Hit Nullity on a Strict Frontier

若時刻 $t$ 的工作 distribution 完全支撐於 unresolved frontier：

$$
\mu_t(K_t)=0,
$$

則：

$$
\boxed{
D_t^{\rm resolve}
=
\int_X c_F(x)d\mu_t(x).
}
$$

即 compiled-hit 在此 distribution 下的直接收益為零。

### Interpretation

這不是說歷史 theorem 對 frontier 沒有幫助。

它仍可能透過：

- 降低 branching factor；
- 提供 reusable lemmas；
- 縮短 proof distance；
- 改善 route selection；
- 產生 stronger invariant；
- 排除 spurious subroutes；

間接幫助 frontier。

但這些是**結構性 discovery acceleration**，不是單純 cache hit。

因此：

$$
\boxed{
\text{Strong DVI}
}
$$

是一個非平凡研究假說。

---

# 7. Verification Bundle

Paper 04 已提供多種 verification-side cost primitives。本文將其合併為：

$$
\boxed{
W_t
:=
C_t^{\rm verify}
+
C_t^{\rm coverage}
+
C_t^{\rm glue}
+
C_t^{\rm maintain}
+
C_t^{\rm replay}.
}
$$

其中：

- $C^{\rm verify}$：local theorem / certificate checking；
- $C^{\rm coverage}$：route / branch / boundary completeness audit；
- $C^{\rm glue}$：constructive mode 的 overlap / cocycle / global compatibility audit；
- $C^{\rm maintain}$：dependency metadata、versioning、support index、storage；
- $C^{\rm replay}$：dirty closure / target basis incremental replay。

總 discovery cost 定義為：

$$
\boxed{
D_t
:=
D_t^{\rm resolve}
+
D_t^{\rm frontier}.
}
$$

總成本：

$$
\boxed{
C_t^{\rm total}
=
D_t+W_t.
}
$$

---

# 8. Verification Share 與 Dominance

## Definition 8.1 — Verification Share

$$
\boxed{
\sigma_t
:=
\frac{W_t}{D_t+W_t}.
}
$$

若

$$
\sigma_t>\frac12,
$$

則稱當前 epoch 為 **verification-dominated**。

## Theorem 8.2 — Verification-Share Monotonicity

若

$$
D_{t+1}\le D_t
$$

且

$$
W_{t+1}\ge W_t,
$$

則：

$$
\boxed{
\sigma_{t+1}\ge\sigma_t.
}
$$

至少一個 inequality 嚴格時，verification share 嚴格上升。

### Proof

需要證：

$$
\frac{W_{t+1}}{D_{t+1}+W_{t+1}}
\ge
\frac{W_t}{D_t+W_t}.
$$

等價於

$$
W_{t+1}D_t
\ge
W_tD_{t+1}.
$$

由

$$
W_{t+1}\ge W_t
$$

及

$$
D_t\ge D_{t+1}
$$

立即成立。

 $\square$

## Corollary 8.3 — Eventual relative verification dominance

若

$$
D_t\to0
$$

且存在 $w_0>0$ 使充分大 $t$ 均有

$$
W_t\ge w_0,
$$

則：

$$
\boxed{
\sigma_t\to1.
}
$$

注意：這只表示**相對 share** 趨近驗證主導，不表示 $W_t$ 必須絕對增加。

---

# 9. Productive Inversion：整體更快但驗證比重更高

原始直覺最有意思的形式不是「verification 變慢」，而是：

> 整體研究成本下降，但 discovery 下降得更快，因此 verification 成為主要成本。

## Theorem 9.1 — Productive Absolute Inversion Condition

假設：

$$
D_{t+1}<D_t,
$$

$$
W_{t+1}>W_t,
$$

且 discovery savings 大於 verification growth：

$$
\boxed{
D_t-D_{t+1}
>
W_{t+1}-W_t.
}
$$

則同時有：

$$
\boxed{
C_{t+1}^{\rm total}<C_t^{\rm total}
}
$$

及

$$
\boxed{
\sigma_{t+1}>\sigma_t.
}
$$

因此：

$$
\boxed{
\text{overall acceleration}
+
\text{verification-share growth}
}
$$

在數學上完全可以同時發生。

這正是本文稱為 **productive inversion** 的 regime。

---

# 10. DVI 的分級定義

為避免一個模糊名稱承擔過多主張，本文定義四層現象。

## Definition 10.1 — Reuse Acceleration

若在可比 task distribution 上：

$$
\boxed{
D_t^{\rm resolve}
\text{ 呈顯著下降趨勢},
}
$$

則稱為 reuse acceleration。

這是目前最容易由 compilation 理論與工程實驗支持的一層。

## Definition 10.2 — Verification-Dominance Transition

若存在 $t_*$ 使

$$
\sigma_t<\frac12
$$

在 $t<t_*$ 的一個穩定區間成立，而

$$
\sigma_t>\frac12
$$

在 $t>t_*$ 的一個穩定區間成立，稱發生 verification-dominance transition。

## Definition 10.3 — Weak Discovery–Verification Inversion

若同一 longitudinal window 內：

$$
\boxed{
D_t^{\rm resolve}\downarrow
}
$$

且

$$
\boxed{
\sigma_t\uparrow,
}
$$

稱為 **Weak DVI**。

Weak DVI 不要求 frontier theorem discovery 變容易。

## Definition 10.4 — Strong Discovery–Verification Inversion

若同一 longitudinal window 內除了 verification share 上升，還觀察到每個 accepted nonredundant theorem cut 的：

$$
\boxed{
D_t^{\rm frontier}\downarrow,
}
$$

則稱為 **Strong DVI**。

Strong DVI 是本文的主要 open empirical hypothesis。

## Definition 10.5 — Productive DVI

若 DVI window 同時滿足：

$$
\boxed{
C_t^{\rm total}\downarrow,
}
$$

則稱為 Productive DVI。

這排除了「只是 verification system 變得非常低效，所以 verification share 上升」的假象。

---

# 11. Discovery–Verification Inversion Hypothesis

## Hypothesis 11.1 — Weak DVI Hypothesis

在以下條件下的長時程、相關 theorem family 中：

1. route representation 穩定；
2. proof trace 被完整編譯；
3. compiled pruning hit rate 提高；
4. one-time build / maintenance cost 已完整記帳；
5. benchmark difficulty ordering 受控；

存在可重現 window，使：

$$
\boxed{
D_t^{\rm resolve}\downarrow
\quad\text{且}\quad
\sigma_t\uparrow.
}
$$

此 hypothesis 已獲現有 proof-reuse / snapshot literature 的間接支持，但本文不宣稱其對任意數學 domain 成立。

## Hypothesis 11.2 — Strong DVI Hypothesis

若 SDPE survivor contraction 不只增加 known-region hits，而真正降低：

- effective branching；
- proof route distance；
- premise ambiguity；
- candidate theorem freedom；
- unresolved constraint dimension；

則可能存在 regime：

$$
\boxed{
D_t^{\rm frontier}\downarrow
}
$$

同時

$$
\boxed{
\sigma_t\uparrow.
}
$$

這是「跨過某個全域量詞障礙後，後面的研究本身開始越算越快」的正式強版本。

它目前仍是 hypothesis。

---

# 12. Frontier Hardening：DVI 的主要反向力

Survivor space 變小不代表剩餘問題變容易。

可能出現：

$$
\Omega_{t+1}\subsetneq\Omega_t,
$$

但所有容易 cases 都已排除，剩下的是：

- singular cases；
- measure-zero exceptional families；
- high dependency-depth states；
- large-parameter extremal configurations；
- representation singular fibers；
- global gluing obstructions。

因此：

$$
\boxed{
D_{t+1}^{\rm frontier}>D_t^{\rm frontier}
}
$$

完全可能。

本文稱此現象為：

$$
\boxed{
\textbf{Frontier Hardening}.
}
$$

VeriSoftBench 中 transitive dependency closure 越大、proof success 越低的觀察，是這種 counterforce 的一個 formal-software domain 例子。

---

# 13. Phase Diagram

本文建議至少區分四種 proof-space regime。

## Phase A — Exploration-Dominated

- compiled hit rate 低；
- survivor space 大；
- routine / frontier discovery 均昂貴；
- verification share 較低。

## Phase B — Compilation-Dominated

- known region 快速累積；
- $D^{\rm resolve}$ 明顯下降；
- frontier cost 未必下降；
- proof trace / closure basis 開始回本。

## Phase C — Discovery–Verification Inversion

- routine discovery 已高度編譯；
- 若 Strong DVI 成立，frontier discovery 也下降；
- verification / coverage / maintenance 成為主要 share；
- total cost 可以繼續下降。

## Phase D — Frontier-Hardening / Exceptional-Survivor Regime

- survivor domain 非常小；
- 但剩餘結構極端、奇異或 global；
- $D^{\rm frontier}$ 重新上升；
- verification 也可能高昂。

因此 DVI 不必是最終永久相位。

Paper 06 的 measure-zero / exceptional survivor 理論會直接研究 Phase D 的可能性。

---

# 14. Linear Hit-Rate Phase Model

為了給出最小可解析模型，假設 compiled hit rate 為

$$
h\in[0,1].
$$

routine discovery cost：

$$
\boxed{
D(h)
=
c_F-h\Delta c,
}
$$

其中

$$
\Delta c=c_F-c_H>0.
$$

假設 verification / maintenance bundle 近似：

$$
\boxed{
W(h)
=
W_0+\lambda h,
}
$$

其中 $\lambda\ge0$。

## Proposition 14.1 — Linear Verification-Dominance Threshold

當

$$
\Delta c+\lambda>0
$$

時，verification dominance

$$
W(h)>D(h)
$$

等價於：

$$
\boxed{
h>h_*}
$$

其中

$$
\boxed{
 h_*
 =
 \frac{c_F-W_0}{\Delta c+\lambda}.
}
$$

若

$$
0<h_*<1,
$$

則模型中存在一個 genuine phase-crossing point。

此模型只是一個 analytic toy model，不是一般 theorem-proving complexity law。

---

# 15. Verification Share 的三種完全不同原因

觀察到

$$
\sigma_t\uparrow
$$

可能至少有三種原因。

## 15.1 Healthy inversion

$$
D_t\downarrow
$$

且 $W_t$ 上升較慢或下降較慢，總成本仍下降。

## 15.2 Verification regression

$$
D_t\approx\text{constant}
$$

但

$$
W_t\uparrow\uparrow.
$$

verification share 雖上升，系統其實變差。

## 15.3 Discovery collapse without verification growth

兩者都下降，但 discovery 降得更快：

$$
D_t\downarrow\downarrow,
\qquad
W_t\downarrow.
$$

此時 verification 成為相對主導，但 absolute verification 並未增加。

因此任何 DVI claim 必須同時報告：

$$
\boxed{
D_t,
W_t,
C_t^{\rm total},
\sigma_t.
}
$$

只報 $\sigma_t$ 沒有意義。

---

# 16. Hidden Cost Transfer No-Go

Compilation 可能把 online cost 轉成 offline cost。

必須計入：

- closure basis 建造；
- proof-state snapshot capture；
- index construction；
- embedding / retrieval index；
- certificate storage；
- dependency extraction；
- version migration；
- stale propagation；
- coverage recomputation；
- proof kernel replay；
- human audit。

因此：

$$
\boxed{
\text{online latency 下降}
\not\Rightarrow
\text{amortized total research cost 下降}.
}
$$

Paper 04 的 break-even condition 必須保留。

---

# 17. DVI Benchmark Protocol

本文提出一個可否證的 longitudinal benchmark protocol。

## 17.1 三種 task queue

### Queue A — Replay / Known

已由 active certificates / patterns 處理過的同型或可安全 instantiate cases。

用途：測量

$$
D^{\rm resolve}.
$$

### Queue B — Near-Frontier Transfer

仍未直接關閉，但與既有 proof basis 有強 dependency / representation overlap 的新 tasks。

用途：測量 compilation 對相鄰 frontier 的 transfer。

### Queue C — True Frontier

要求產生一個 accepted nonredundant theorem cut，真正改變：

$$
\Omega,
\quad
\mathbf G,
\quad
RouteCert,
\quad\text{或}\quad
GCC.
$$

用途：測量

$$
D^{\rm frontier}.
$$

---

# 18. Benchmark Controls

任何 DVI benchmark 至少要求：

1. **固定 prover / model version**；
2. **固定 Lean / checker / solver version**；
3. **固定或完整記錄 hardware / concurrency**；
4. **paired cold-start vs compiled-state runs**；
5. **task ordering randomized / counterbalanced**；
6. **完整記錄 one-time build costs**；
7. **compiled cache hit 必須有 certificate semantics**；
8. **accepted theorem 必須通過 formal checker 或獨立 proof audit**；
9. **難度不可只按時間自然遞增而不做控制**；
10. **frontier theorem 必須定義 nonredundancy**；
11. **dependency / version change 要觸發 dirty replay**；
12. **失敗 proposal 也計成本**。

否則非常容易把 curriculum effect、hardware warmup、caching 或 task-selection bias 誤認成 DVI。

---

# 19. 最小觀測資料表

每個 epoch $t$ 至少保存：

$$
\boxed{
\begin{aligned}
&D_t^{\rm resolve},\\
&D_t^{\rm frontier},\\
&C_t^{\rm verify},\\
&C_t^{\rm coverage},\\
&C_t^{\rm glue},\\
&C_t^{\rm maintain},\\
&C_t^{\rm replay},\\
&h_t,\\
&\chi_t,\\
&|Dirty_t|,\\
&|R_t|,\\
&|V_t|,\\
&|\mathcal B_t|,\\
&|\Omega_t|_{\rm diagnostic},\\
&\mathbf G_t.
\end{aligned}
}
$$

其中

$$
|\Omega_t|_{\rm diagnostic}
$$

可以是 cardinality、volume、sampled proxy 或其它 domain-dependent diagnostic；它不是 closure certificate。

真正的 global validity 仍由 Paper 03 的 GCC 決定。

---

# 20. Empirical DVI 判定規則

給定 window

$$
I=[t_0,t_1],
$$

對每個 cost series 計算 robust 或 ordinary trend slope。

## Weak DVI acceptance

至少要求：

$$
\operatorname{slope}_I(D^{\rm resolve})<0,
$$

$$
\operatorname{slope}_I(\sigma)>0,
$$

並且 paired compiled-vs-cold difference 顯著且可重現。

## Strong DVI acceptance

另外要求：

$$
\boxed{
\operatorname{slope}_I(D^{\rm frontier})<0.
}
$$

## Productive DVI acceptance

再要求：

$$
\boxed{
\operatorname{slope}_I(C^{\rm total})<0.
}
$$

## Verification-dominance crossing

若 window 內存在穩定 crossover：

$$
\boxed{
\sigma_t:\;<1/2\to>1/2,
}
$$

則額外標記 verification-dominated phase transition。

---

# 21. 為什麼 Strong DVI 特別難證

若研究者只查 unresolved frontier，Proposition 6.1 已證明 direct cache-hit savings 消失。

因此 Strong DVI 需要一個真正的 structural mechanism，例如：

$$
\boxed{
\text{survivor contraction}
\to
\text{effective branching reduction}
}
$$

或：

$$
\boxed{
\text{constraint accumulation}
\to
\text{premise ambiguity reduction}
}
$$

或：

$$
\boxed{
\text{compiled theorem graph}
\to
\text{shorter route to next cut}.
}
$$

這些機制與單純 cache lookup 不同。

因此下一步若要證 Strong DVI，必須建立 proof-space geometry 與 discovery complexity 之間的 bridge theorem。

這正是「解空間幾何計算論」與 SDPE 真正開始交會的地方。

---

# 22. Counterexamples to naive DVI claims

## No-Go 22.1 — Survivor Shrinkage Implies Faster Frontier Discovery

可以有：

$$
K_t\subset K_{t+1}
$$

但 query distribution 同時漂移到更昂貴 frontier，因此

$$
D_{t+1}^{\rm resolve}>D_t^{\rm resolve}.
$$

更不用說 $D^{\rm frontier}$。

## No-Go 22.2 — Higher Hit Rate Implies Total Speedup

若 maintenance / indexing / replay cost 增長超過 hit savings，則：

$$
h_{t+1}>h_t
$$

仍可以

$$
C_{t+1}^{\rm total}>C_t^{\rm total}.
$$

## No-Go 22.3 — Higher Verification Share Implies Discovery Acceleration

若 discovery 不變而 verification regression：

$$
W_t\uparrow,
$$

則 $\sigma_t$ 一樣會上升。

## No-Go 22.4 — Snapshot Speedup Is Strong DVI Evidence

proof-state snapshotting 可以大幅減少 reconstruction cost，但該 benchmark 本身並不測量一般 frontier theorem discovery。

## No-Go 22.5 — Proof Reuse in One Domain Proves Universal DVI

Circuit / algebraic / repository benchmarks 可以證明 reuse benefit 在其 domain 存在，不能外推成一般 mathematical research law。

## No-Go 22.6 — Verification Must Grow Absolutely

verification share 可以因 discovery cost 降得更快而上升，即使 $W_t$ 本身下降。

## No-Go 22.7 — DVI Must Be Permanent

後期 survivor 可能變成 singular / exceptional / measure-zero hard core，使 frontier discovery 再度變難。

---

# 23. 與「空間域包圍越跑越快」直覺的精確關係

最早直覺可以寫成：

$$
\Omega_0
\supseteq
\Omega_1
\supseteq
\cdots,
$$

因此剩餘驗證空間下降，研究可能加速。

Paper 05 現在把這句話拆成：

$$
\boxed{
\text{Domain Contraction}
\not\Rightarrow
\text{Discovery Acceleration directly}.
}
$$

真正的 causal chain 至少要是：

$$
\boxed{
\begin{aligned}
&\text{Certified Domain Contraction}\\
&\downarrow\\
&\text{Proof Trace Compilation}\\
&\downarrow\\
&\text{Compiled-Hit Gain / Structural Branch Reduction}\\
&\downarrow\\
&\text{Lower Effective Discovery Cost}\\
&\downarrow\\
&\text{Verification Share Rebalancing}.
\end{aligned}
}
$$

其中每個箭頭都需要獨立驗證。

---

# 24. Paper 05 的 falsifiability

DVI 並不是只能被支持、不能被反駁的敘事。

以下任何結果都可以反駁特定版本：

## Weak DVI falsifier

長期 compiled hit rate 上升後，控制 query distribution 仍觀察不到

$$
D^{\rm resolve}\downarrow.
$$

## Strong DVI falsifier

在多個控制 domain 上，survivor contraction 持續發生，但

$$
D^{\rm frontier}
$$

穩定不降或上升。

## Productive DVI falsifier

verification / maintenance growth 長期吞掉所有 discovery savings，使

$$
C^{\rm total}
$$

不降。

## Phase-transition falsifier

 $\sigma_t$ 沒有穩定 regime shift，只呈 task-dependent noise。

因此本文提出的是一個可以被 longitudinal evidence 擊敗的研究假說。

---

# 25. Theorem / Hypothesis / External Input Ledger

## 25.1 Internal theorems / propositions

1. Fixed-Distribution Compilation Monotonicity；
2. Strict Compilation Acceleration Criterion；
3. Exact Compilation–Drift Decomposition；
4. Frontier Cache Nullity；
5. Verification-Share Monotonicity；
6. Eventual Relative Verification Dominance；
7. Productive Absolute Inversion Condition；
8. Linear Verification-Dominance Threshold。

## 25.2 Definitions / measurement architecture

1. Routine Resolution Cost；
2. Frontier Discovery Cost；
3. Verification Bundle；
4. Verification Share；
5. Reuse Acceleration；
6. Weak DVI；
7. Strong DVI；
8. Productive DVI；
9. Frontier Hardening；
10. DVI Benchmark Protocol。

## 25.3 Open hypotheses

1. Weak DVI occurs reproducibly in sufficiently related long-horizon proof families；
2. Strong DVI occurs after structural survivor contraction in some mathematical domains；
3. a stable verification-dominated phase transition exists in sufficiently compiled SDPE systems；
4. proof-space geometry can provide sufficient conditions for frontier discovery acceleration。

## 25.4 External grounding

- Lean proof-state snapshotting；
- algebraic proof-certificate recycling；
- CircuitProver reusable verified library；
- LeanAgent lifelong theorem proving；
- VeriSoftBench dependency-closure difficulty；
- AXLE scalable strict proof verification。

---

# 26. Checker Scope

companion checker 驗證 finite / synthetic models 中：

1. fixed-distribution compilation monotonicity；
2. exact frontier-drift decomposition；
3. frontier cache nullity；
4. verification-share monotonicity；
5. productive absolute inversion algebra；
6. linear phase threshold；
7. naive DVI false-positive counterexamples；
8. synthetic Weak DVI classification；
9. synthetic Strong/Productive DVI classification。

checker 不證：

$$
\boxed{
\text{一般數學研究一定存在 DVI}.
}
$$

亦不證任何特定 AI prover 的 frontier discovery cost 隨時間下降。

---

# 27. 前五篇形成的新 stack

Paper 01：

$$
\boxed{
\text{Survivor Soundness}.
}
$$

Paper 02：

$$
\boxed{
\text{Representation Faithfulness}.
}
$$

Paper 03：

$$
\boxed{
\text{Global Coverage / Closure}.
}
$$

Paper 04：

$$
\boxed{
\text{Trace Compilation / Incremental Replay}.
}
$$

Paper 05：

$$
\boxed{
\text{Cost-Phase Separation / DVI Falsifiability}.
}
$$

因此現在可以寫成：

$$
\boxed{
\begin{aligned}
&\text{Correct Proof Space}\\
&\downarrow\\
&\text{Certified Contraction}\\
&\downarrow\\
&\text{Compiled History}\\
&\downarrow\\
&\text{Measured Discovery / Verification Dynamics}\\
&\downarrow\\
&\text{Empirically Testable Phase Structure}.
\end{aligned}
}
$$

---

# 28. 下一篇：Survivor Measure、零測度與不可約例外集

Paper 05 已證明一個非常重要的限制：

$$
\boxed{
\text{survivor space 變小}
\not\Rightarrow
\text{frontier 變容易}.
}
$$

真正最危險的情形恰好可能是：

$$
\mu(\Omega_t)\to0,
$$

但剩餘 survivor 逐漸集中到極端、奇異、fractal 或 representation-singular set。

因此下一篇直接進入：

$$
\boxed{
\textbf{SDPE Paper 06 — Survivor Measure、零測度與不可約例外集}.
}
$$

它將回答：

> 空間域包圍如果一直縮，究竟什麼意義下是真的「接近證完」？什麼情況只是把問題壓成一個更難的 measure-zero exceptional core？

這也是判定 Strong DVI 能否長期存在的必要下一層。

---

# 29. Final Status

本文的核心結論可壓縮成三句。

第一：

$$
\boxed{
\text{Compiled proof history 可以定理化地降低例行 query-resolution 成本。}
}
$$

第二：

$$
\boxed{
\text{這不等於 frontier theorem discovery 自動變容易。}
}
$$

第三：

$$
\boxed{
\text{「整體更快，但驗證成為主要成本」是一個數學上可一致、可測量、可否證的 phase regime。}
}
$$

因此最早的直覺「跨過全域量詞後可能越算越快」現在被正式拆成兩層：

$$
\boxed{
\text{Weak form：已證區域編譯帶來重複搜尋成本下降；}
}
$$

與

$$
\boxed{
\text{Strong form：survivor geometry 本身開始降低下一個新 theorem 的發現成本。}
}
$$

前者已有 theorem 與工程 precedent；後者是本系列接下來真正需要驗證的研究命題。

---

# References

1. Austin Shen and Yunong Shi, **Keep the Proof State Live: Snapshotting for Efficient Tactic Search in Lean 4**, arXiv:2605.25556, 2026.
2. Daniela Kaufmann and Clemens Hofstadler, **Recycling Algebraic Proof Certificates**, arXiv:2507.20267, 2025.
3. Ziyi Yang, Wenji Fang, Chen Chen, Zhiyao Xie, Hongce Zhang, **CircuitProver: Agentic Lean 4 Theorem Proving with Reusable Circuit Proof Library for Hardware Verification**, arXiv:2607.27259, 2026.
4. Adarsh Kumarappan et al., **LeanAgent: Lifelong Learning for Formal Theorem Proving**, arXiv:2410.06209, 2024.
5. Yutong Xin, Qiaochu Chen, Greg Durrett, Işil Dillig, **VeriSoftBench: Repository-Scale Formal Verification Benchmarks for Lean**, arXiv:2602.18307, 2026.
6. Jimmy Xin et al., **AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities**, arXiv:2606.26442, 2026.
7. Prior SDPE artifact: **Paper 01 — Global Quantifiers, Counterexample Domains, and Verifiable Contraction**.
8. Prior SDPE artifact: **Paper 02 — Route-Domain Completeness and Representation Non-Collapse**.
9. Prior SDPE artifact: **Paper 03 — Multidimensional Coverage, Gaps, and Global Closure Certificates**.
10. Prior SDPE artifact: **Paper 04 — Proof Trace Compilation and Verification Amortization**.
