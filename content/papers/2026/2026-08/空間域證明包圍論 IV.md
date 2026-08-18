# 空間域證明包圍論 IV
## Proof Trace Compilation 與 Verification Amortization
### Spatial-Domain Proof Enclosure IV: Proof Trace Compilation, Closure Bases, and Verification Amortization

**Version:** v0.1  
**Date:** 2026-08-14  
**Status:** formal research framework / theorem-style reduction; not a claim that proof search generically becomes easier  
**Canonical source:** UTF-8 Markdown; canonical mathematics uses ` $...$ ` and `$$...$$` only.

---

## 摘要

前三篇空間域證明包圍論建立了三個 closure 前提：Paper 01 要求 survivor envelope 永遠保留所有真實反例；Paper 02 要求 representation 不得壓掉 proof-relevant counterexample fibers；Paper 03 要求 local routes 必須有 global cover certificate，必要時再加 structural gluing certificate。至此，一個全域閉合證明可以被描述為一組有 scope、dependency、version 與 replay semantics 的正式證書。

本文處理下一個問題：

> 當長時間研究已經累積大量 theorem cuts、route certificates、local refutations、coverage certificates 與 gluing artifacts，哪些歷史可以被安全地編譯成後續研究可直接使用的 pruning state，而不必每輪重新支付完整 discovery 與 verification 成本？

本文首先把 proof history 定義為一個 versioned dependency DAG。每個 certificate node 均攜帶 statement、scope、dependencies、representation version、checker、payload 與可排除區域。只有 local checker 通過、所有 dependencies 仍 active、scope 與 representation fingerprint 未失效的節點，才能進入 active proof state。

對一個 closure target $q$，本文定義其 **dependency closure basis**：

$$
\boxed{
\mathcal B(q)
=
\operatorname{Anc}(q)\cup\{q\}.
}
$$

在 checker compositionality 與 dependency completeness 成立時，重播 $\mathcal B(q)$ 足以重建 $q$ 的有效性；所有不在 target ancestor closure 中的 discovery history 對該 target 的 replay 可以安全歸檔。這不保證 $\mathcal B(q)$ 是最小 basis，但建立了第一個可機械抽取的 sound closure basis。

接著本文把已驗證 exclusion certificates 編譯成 **Compiled Pruning State**。對 route state $x$，令

$$
\kappa_t(x)
=
\#\{v\in A_t:x\in E_v\}
$$

為 active exclusion support multiplicity。若

$$
\kappa_t(x)>0,
$$

則至少存在一張 active sound certificate 排除 $x$，因此 $x$ 可以不重新進入 theorem discovery。若 dependency 失效，本文證明 **support-aware rollback theorem**：只需要 reopen 那些所有 exclusion supports 都同時失效的點，而不是把整個歷史研究清空。

本文再證明 **incremental replay equivalence theorem**。若每個 checker 僅依賴其明示父節點、checker 決定性成立且 dependency DAG 完整，則某些 nodes 改變後，只重播其 descendant dirty closure，所得結果與完整從頭 replay 等價。這將「留下痕跡」提升成一個可操作的增量驗證原則。

為避免把快取誤當證明，本文嚴格區分：

$$
\boxed{
\text{Search-State Compilation}
\neq
\text{Proof-Certificate Compilation}.
}
$$

Lean proof-state snapshot 可以避免重建 elaborated proof context；proof patterns、verified lemmas 與 closure certificates 則可以承擔邏輯有效性。前者是 operational accelerator，後者才是 proof artifact。

本文最後建立完整攤銷成本模型。若未編譯時每個任務平均成本為 $c_F$，compiled hit 成本為 $c_H<c_F$，hit rate 為 $h$，一次性建造／basis verification 成本為 $B$，每任務維護成本為 $m$，則

$$
C_{\rm comp}(N)
=
B
+
N\left[h c_H+(1-h)c_F+m\right].
$$

與未編譯成本

$$
C_{\rm base}(N)=Nc_F
$$

相比，定義

$$
\Delta
:=
h(c_F-c_H)-m.
$$

若

$$
\Delta>0,
$$

則 break-even condition 為

$$
\boxed{
N>\frac{B}{\Delta}.
}
$$

因此「越來越快」不是免費定理，而是一個可驗證的 amortization condition。本文不提前宣稱 Discovery–Verification Inversion 必然發生；該 phase transition 留給 Paper 05。Paper 04 僅建立使其可以被嚴格測量的 compiled-state、rollback、incremental replay 與成本地基。

---

## 關鍵詞

空間域證明包圍；proof trace compilation；closure basis；verification amortization；proof reuse；proof-state snapshot；incremental replay；dependency DAG；stale propagation；rollback；compiled pruning；proof certificate；AI theorem proving

---

# 1. 前三篇留下的正式狀態

設原始命題為

$$
\forall d\in D,\;P(d),
$$

真實反例集合為

$$
\mathcal C
=
\{d\in D:\neg P(d)\}.
$$

Paper 01 建立 sound survivor invariant：

$$
\boxed{
\mathcal C\subseteq\Omega_t.
}
$$

每一個 theorem cut 只能在保留所有真反例的前提下更新：

$$
\Omega_{t+1}
=
\Omega_t\cap H_t.
$$

Paper 02 建立 route-domain faithfulness。對

$$
\phi:D\to X,
$$

表示壓縮不能靜默丟失 proof-relevant fibers；若表示不 exact，mixed fibers 必須保留、refine 或 whole-fiber certify。

Paper 03 進一步建立 Global Closure Certificate：

$$
\mathsf{GCC}
=
\langle
Master,Atlas,CoverCert,LocalCerts,BoundaryCert,LiftCerts,
GlueMode,GlueCert,DepDAG,Version,Replay
\rangle.
$$

因此當前問題不再只是「有沒有很多 theorem」，而是：

$$
\boxed{
\text{如何把可重播 proof history 壓縮成可持續使用的 active proof state？}
}
$$

---

# 2. Fresh literature grounding

## 2.1 Proof-state snapshotting

Shen 與 Shi 在 2026 年的 Lean 4 工作指出，平行 tactic search 中大量成本可來自每個 branch 重建已經 elaborated 的 proof state。其 snapshotting 方法直接重用 server 中現存的 elaborated state，在其 48 個 miniF2F-v2 benchmark 上報告 5.6--50 倍 wall-time speedup，平均約 14 倍。

本文只取一個原則：

$$
\boxed{
\text{reconstructing an already-known proof state can dominate branch cost.}
}
$$

但 snapshot 不等於 theorem certificate。

## 2.2 Recycling algebraic proof certificates

Kaufmann 與 Hofstadler 在 2025 年提出可重用 algebraic proof patterns。經過一次 PatternNew 驗證後，PatternApply 可在符合 interface 與 substitution constraints 時重新 instantiate 已驗證 proof fragment；其實驗顯示 proof steps、file size、memory 與 checking time 均可下降。

這是本文 **certificate compilation** 的直接外部類比：

$$
\boxed{
\text{verified proof fragment}
\to
\text{typed reusable pattern}
\to
\text{cheaper valid instantiation}.
}
$$

## 2.3 Proof accumulation and reusable theorem libraries

CircuitProver 在 2026 年把 proving traces 與 verified theorems 蒸餾成可重用 Lean library；63 個 hardware tasks 的實驗中，其 accumulated proof knowledge 在 ablation 中降低 proof length 16.3% 並降低 verification time 23.2%。Rtl2lean 亦建立 hierarchical theorem library，報告 358 個 foundational lemmas 中有 287 個可自動 reuse，reusable lemma ratio 為 80.2%。

這些工作證明「verified knowledge reuse」不是純哲學假設，但其領域是 hardware theorem proving；本文不把這些實驗數字外推成一般數學定律。

## 2.4 Lifelong theorem proving and scalable verification

LeanAgent 使用 dynamic database 處理持續擴張的 formal knowledge，並研究 stability / backward transfer。AXLE 則顯示大規模 AI theorem proving 需要 strict verification、metadata extraction、multi-version support 與 per-request isolation，而不只是能 compile 一份 Lean 檔案。

這些工作支持本文的一項設計要求：

$$
\boxed{
\text{reuse 必須與 version / dependency / strict verification 綁定。}
}
$$

---

# 3. Verified Proof History

## Definition 3.1 — Proof History DAG

定義時刻 $t$ 的 proof history 為有限 DAG：

$$
\boxed{
\mathcal H_t=(V_t,E_t).
}
$$

每個 node $v\in V_t$ 是一個 certificate record：

$$
\boxed{
\operatorname{Cert}(v)
=
\langle
Stmt_v,
Scope_v,
Deps_v,
Route_v,
Version_v,
Fingerprint_v,
Checker_v,
Payload_v,
Region_v,
Status_v
\rangle.
}
$$

其中 $Region_v$ 可為空；只有 exclusion certificates 才需要具體排除區域。

Edge

$$
(u,v)\in E_t
$$

表示 $v$ 的 validity 顯式依賴 $u$。

## Definition 3.2 — Dependency Completeness

若所有能影響 $v$ correctness 的 formal assumptions、representation versions、theorems、coverage objects 與 gluing objects，都透過 $Deps_v$ 或其 fingerprint 顯式記錄，則稱 dependency metadata **complete**。

這是一項系統義務，不是自動成立的數學真理。

---

# 4. Active validity 與 stale state

## Definition 4.1 — Locally Valid Node

node $v$ 在時刻 $t$ locally valid，若：

1. $Checker_v(Payload_v)=\mathsf{PASS}$ ；
2. $Scope_v$ 與當前 problem scope 相容；
3. $Route_v$ representation contract 仍有效；
4. $Version_v$ / $Fingerprint_v$ 與 active environment 相容。

## Definition 4.2 — Active Node

遞迴定義： $v$ active，若 $v$ locally valid，且

$$
\boxed{
\forall u\in Deps_v,\;u\text{ active}.
}
$$

active nodes 集合記為

$$
A_t\subseteq V_t.
$$

其 complement 中由 dependency 失效造成者稱 stale nodes。

## Proposition 4.3 — Descendant Staleness

若 node $u$ 失效，而所有 descendant certificates 的 validity 均要求其顯式 dependencies active，則每個依賴 $u$ 的 descendant 都必須標記為 stale，直到它被重新驗證或改寫 dependency。

### Proof

沿 DAG 的 topological order 歸納即可。若 $v$ 直接依賴 stale node，則 active condition 失敗；再逐層傳播到 descendants。 $\square$

---

# 5. Closure Basis

長時間 discovery history 不等於 final replay 必須重播所有歷史節點。

## Definition 5.1 — Target Certificate

令

$$
q\in V_t
$$

為我們想重播的 target，例如：

- 某個 local exclusion theorem；
- 某個 cover certificate；
- 某個 boundary certificate；
- 最終 $\mathsf{GCC}$。

## Definition 5.2 — Canonical Dependency Closure Basis

令

$$
\operatorname{Anc}(q)
$$

為 DAG 中所有可到達 $q$ 的 ancestors。定義：

$$
\boxed{
\mathcal B_{\rm dep}(q)
:=
\operatorname{Anc}(q)\cup\{q\}.
}
$$

## Theorem 5.3 — Ancestor Closure Sufficiency

假設：

1. checker semantics compositional；
2. dependency metadata complete；
3. 每個 node checker 只讀自身 payload、active environment fingerprint 與直接 parents 的 verified outputs。

則重播

$$
\mathcal B_{\rm dep}(q)
$$

足以得到和完整 history replay 相同的 $q$ validity 結果。

### Proof

對 $\mathcal B_{\rm dep}(q)$ 的 topological ordering 作歸納。base nodes 不需要外部 history nodes。若所有 parents 已得到與 full replay 相同的 verified outputs，則 compositional deterministic checker 對當前 node 也產生相同結果。由於任何能影響 $q$ 的 dependency 都在 ancestor closure 內，最終 $q$ 結果相同。 $\square$

## Remark 5.4 — Basis 不等於 minimum basis

 $\mathcal B_{\rm dep}(q)$ 是一個可機械抽取的 sound basis，但不保證 cardinality 或 replay cost 最小。若存在 alternative certificates、redundant cover charts、multiple independent support paths，還可以進一步壓縮。

因此：

$$
\boxed{
\text{sound closure basis extraction}
\neq
\text{minimum closure basis optimization}.
}
$$

本文只要求前者。

---

# 6. Compiled Pruning State

## Definition 6.1 — Active Exclusion Certificate

若 active node $v$ 證明某個 region $E_v$ 與真實反例集 disjoint：

$$
\boxed{
E_v\cap\mathcal C=\varnothing,
}
$$

則稱 $v$ 為 active exclusion certificate。

## Definition 6.2 — Support Index

對 route state $x$，定義 active supports：

$$
S_t(x)
:=
\{v\in A_t:x\in E_v\}.
$$

定義 support multiplicity：

$$
\boxed{
\kappa_t(x)
:=
|S_t(x)|.
}
$$

## Definition 6.3 — Compiled Pruning State

定義：

$$
\boxed{
\mathsf{CPS}_t
=
\langle
\Omega_t,
\mathcal B_t,
\mathcal I_t,
\kappa_t,
\mathbf G_t,
DepDAG_t,
Version_t,
Replay_t
\rangle.
}
$$

其中 $\mathcal I_t$ 是從 route region / features 到 active exclusion supports 的索引。

## Theorem 6.4 — Safe Compiled Pruning

若

$$
\kappa_t(x)>0,
$$

且 support index 完整、所有 indexed supports active 且 sound，則

$$
\boxed{x\notin\mathcal C.}
$$

因此 search system 可安全跳過重新 discovery 該 candidate。

### Proof

存在 $v\in S_t(x)$，故 $x\in E_v$。由 soundness， $E_v\cap\mathcal C=\varnothing$。因此 $x\notin\mathcal C$。 $\square$

這是 proof trace compilation 最直接的「快速通道」。

---

# 7. Support-Aware Rollback

最粗暴的 rollback 是任一 dependency 改變就清空全部 compiled state。這通常沒有必要。

令一組 certificates 由於 version change、scope change 或 dependency failure 被 invalidate。其 staleness descendant closure 記為

$$
Z^+.
$$

令 invalidation 前後 support multiplicity 分別為

$$
\kappa_{\rm old}(x),
\qquad
\kappa_{\rm new}(x).
$$

## Definition 7.1 — Reopen Region

定義：

$$
\boxed{
R(Z^+)
:=
\{x:\kappa_{\rm old}(x)>0,\;\kappa_{\rm new}(x)=0\}.
}
$$

## Theorem 7.2 — Support-Aware Rollback Theorem

在 support index 完整且所有 remaining active supports sound 的前提下，invalidation $Z^+$ 後：

1. $x\in R(Z^+)$ 必須 reopen 或重新 certify；
2. 若 $\kappa_{\rm new}(x)>0$，則 $x$ 仍可保持 pruned；
3. 不需要因一張 certificate 失效而 reopen 所有曾被它覆蓋的 states。

### Proof

若 $\kappa_{\rm new}(x)>0$，仍存在 active sound exclusion certificate 排除 $x$，由 Theorem 6.4 可繼續 prune。只有當所有 supports 均失效時，舊的 compiled exclusion 不再有 active witness，因此必須重新進入 survivor / verification pipeline。 $\square$

這使 rollback 從：

$$
\boxed{
\text{certificate-level invalidation}
}
$$

轉成：

$$
\boxed{
\text{support-aware region reopening}.
}
$$

---

# 8. Incremental Replay

## Definition 8.1 — Dirty Closure

若 change set 為

$$
M\subseteq V_t,
$$

定義 dirty closure：

$$
\boxed{
Dirty(M)
=
M\cup\operatorname{Desc}(M).
}
$$

## Theorem 8.2 — Incremental Replay Equivalence

假設：

1. dependency DAG complete；
2. 每個 node checker deterministic；
3. checker 只依賴 node payload、declared environment fingerprint 與 direct parent verified outputs；
4. $M$ 之外的 node payload / environment fingerprint 未改變。

則只重新 replay $Dirty(M)$，並重用其他 active node 的 verified outputs，得到的整體 active/stale assignment 與 full replay 相同。

### Proof

在 topological order 中考慮所有 nodes。不在 $Dirty(M)$ 的 node 既不是 changed node，也不存在從 $M$ 到它的 dependency path，因此其 payload、fingerprint 與所有 ancestor verified outputs 均未改變，可安全保留。對 $Dirty(M)$ nodes 依 topological order 重新計算；每一步 parents 都已經是正確的新值。因此結果與 full replay 完全一致。 $\square$

## Corollary 8.3 — Incremental GCC Replay

若 $\mathsf{GCC}$ 不在 $Dirty(M)$，則其 validity 不受此次 change 影響。

若 $\mathsf{GCC}\in Dirty(M)$，只需重播其 dirty ancestor support，而不是整份 discovery history。

---

# 9. Proof Pattern Compilation

proof reuse 不一定只是重用完整 theorem。某些歷史 proof fragment 可以被抽象成 pattern。

## Definition 9.1 — Verified Proof Pattern

定義：

$$
\boxed{
\Pi
=
\langle
I,
A,
O,
\pi,
\operatorname{InstCheck}
\rangle.
}
$$

其中：

- $I$：formal inputs；
- $A$：admissible instantiation constraints；
- $O$：formal outputs；
- $\pi$：一次性驗證過的 proof fragment；
- $\operatorname{InstCheck}$：每次 reuse 的 instantiation checker。

pattern certification 證明：

$$
\boxed{
\forall\theta\in A,
\quad
I(\theta)
\Longrightarrow
O(\theta).
}
$$

## Theorem 9.2 — Sound Pattern Reuse

若 pattern certificate active，且新的 instantiation $\theta$ 通過 $\operatorname{InstCheck}$ 並滿足 $I(\theta)$，則可以直接 commit $O(\theta)$，不需要重新 discovery $\pi$ 的內部推導。

這只是 universal instantiation，但它正式區分：

$$
\boxed{
\text{reusing a verified proof schema}
}
$$

與

$$
\boxed{
\text{copying an old proof because it looks similar}.
}
$$

後者沒有 soundness 保證。

---

# 10. Search-State Compilation 不等於 Proof-Certificate Compilation

本文把 reuse 分成兩層。

## 10.1 Search-State Compilation

例如：

- elaborated Lean proof state snapshot；
- tactic branch state；
- retrieval index；
- theorem embeddings；
- cached route features；
- heuristic branch scores。

這些可以大幅降低 discovery overhead。

但一般不直接證明：

$$
\forall x\in D\;P(x).
$$

## 10.2 Proof-Certificate Compilation

包括：

- kernel-checked theorem；
- independently replayable proof certificate；
- verified proof pattern；
- active exclusion certificate；
- cover certificate；
- boundary / gluing certificate；
- dependency-closed GCC basis。

它們能承擔 logical validity。

因此：

$$
\boxed{
\mathsf{Snapshot}
\not\Rightarrow
\mathsf{Proof}.
}
$$

以及：

$$
\boxed{
\text{fast retrieval}
\not\Rightarrow
\text{safe pruning}.
}
$$

除非 retrieval result 再連到 active proof certificate。

---

# 11. Known / Unknown Gate

先前「已知則編譯，未知則展開」在 SDPE 中可精確改寫。

## Definition 11.1 — Compiled Mode

candidate $x$ 可進入 Compiled Mode，若：

1. route representation certificate active；
2. $x$ 不屬於 unresolved singular fiber；
3. $\kappa_t(x)>0$，或存在其它 active certified route decision；
4. relevant boundary / version / dependency gaps 為空。

## Definition 11.2 — Exploration Mode

若 candidate 落入：

$$
G_D,
\quad
G_B,
\quad
G_{\partial},
\quad
G_C,
\quad
G_G,
\quad
G_R,
$$

或其所有 supports stale，則必須回到 Exploration / Verification Mode。

因此：

$$
\boxed{
\text{Known}
\Rightarrow
\text{Compile},
\qquad
\text{Unknown / Stale / Boundary}
\Rightarrow
\text{Expand}.
}
$$

這不是 AI confidence threshold，而是 certificate-state transition。

---

# 12. Verification Amortization

現在正式把「後面可能越來越快」拆成可計算條件。

令未使用 compiled state 時，每一個相關任務平均成本為

$$
\boxed{
c_F
:=
c_D+c_V,
}
$$

其中 $c_D$ 是 discovery / reconstruction cost， $c_V$ 是 verification cost。

compiled system 有：

- 一次性 build + basis verification cost $B$ ；
- cache / certificate hit rate $h\in[0,1]$ ；
- hit 時 lookup + replay / instantiation cost $c_H$ ；
- miss 時仍支付 $c_F$ ；
- 每任務平均 maintenance cost $m$。

則 $N$ 個任務的 compiled total cost：

$$
\boxed{
C_{\rm comp}(N)
=
B
+
N\left[
 h c_H
 +(1-h)c_F
 +m
\right].
}
$$

baseline：

$$
\boxed{
C_{\rm base}(N)
=Nc_F.
}
$$

## Theorem 12.1 — Amortization Break-Even

定義每任務淨收益：

$$
\boxed{
\Delta
:=
h(c_F-c_H)-m.
}
$$

若

$$
\Delta\le0,
$$

則在此成本模型下，增加任務數不能攤銷一次性 build cost。

若

$$
\Delta>0,
$$

則 compiled system 比 baseline 便宜當且僅當：

$$
\boxed{
N>\frac{B}{\Delta}.
}
$$

### Proof

$$
C_{\rm base}(N)-C_{\rm comp}(N)
=
N\left[h(c_F-c_H)-m\right]-B
=N\Delta-B.
$$

因此差值為正恰當且僅當 $N>B/\Delta$。 $\square$

## Corollary 12.2 — Asymptotic Average Cost

若 $B$ 固定，則：

$$
\boxed{
\lim_{N\to\infty}
\frac{C_{\rm comp}(N)}{N}
=
h c_H+(1-h)c_F+m.
}
$$

因此一次性建造成本可以被攤薄，但 maintenance 與 per-hit replay 不會因 $N\to\infty$ 自動消失。

---

# 13. Pattern Verification Amortization

若某個 proof pattern 一次驗證成本為

$$
V_0,
$$

每次合法 instantiation 檢查成本為

$$
v,
$$

重用 $N$ 次總 verification cost：

$$
V_N=V_0+Nv.
$$

因此平均：

$$
\boxed{
\frac{V_N}{N}
=v+\frac{V_0}{N}.
}
$$

故：

$$
\boxed{
\lim_{N\to\infty}\frac{V_N}{N}=v.
}
$$

這是最簡單的 certificate amortization theorem。

但如果每次 instantiation 的 environment / scope 都不同到需要完整重驗，則 $v$ 可以接近 $V_0$，此時 reuse 幾乎沒有收益。

---

# 14. Closure-Basis Compression Ratio

令完整 discovery history node 數為

$$
|V_t|,
$$

target dependency basis 大小為

$$
|\mathcal B_{\rm dep}(q)|.
$$

定義 structural compression ratio：

$$
\boxed{
\chi_q
:=
\frac{|\mathcal B_{\rm dep}(q)|}{|V_t|}.
}
$$

若

$$
\chi_q\ll1,
$$

表示大量 discovery history 對 target replay 已非必要。

但 cardinality ratio 不等於 cost ratio。每個 node replay 成本可以差很多，因此更合理的 weighted ratio 為：

$$
\boxed{
\chi_q^{(w)}
=
\frac{\sum_{v\in\mathcal B_{\rm dep}(q)}w(v)}
{\sum_{v\in V_t}w(v)}.
}
$$

其中 $w(v)$ 可以是 verification time、memory、certificate size 或 trust cost。

---

# 15. Incremental Global Closure Certificate

Paper 03 的 $\mathsf{GCC}$ 本身也應視為 dependency DAG 的 terminal node，而不是一份靜態 PDF。

定義：

$$
q_{\rm GCC}
$$

為 global closure target。

其 dependency closure basis 至少包含：

- master survivor certificate；
- active RouteCerts；
- cover certificate；
- local refutation certificates；
- boundary certificates；
- required lift certificates；
- constructive mode 下的 gluing certificate；
- dependency/version fingerprints。

若某一 local theorem 改版，只需：

$$
\boxed{
\text{invalidate}
\to
\text{mark descendants dirty}
\to
\text{support-aware reopen}
\to
\text{incremental replay}
\to
\text{recompute GCC status}.
}
$$

因此 $\mathsf{GlobalClosed}$ 不應是永久布林旗標，而是：

$$
\boxed{
\mathsf{GlobalClosed}_t
=
\operatorname{Replay}(\mathcal B_{\rm dep}(q_{\rm GCC}),Version_t).
}
$$

---

# 16. Compiled State 與 discovery acceleration 的嚴格邊界

Paper 04 能證明的不是：

$$
\boxed{
\text{theorem discovery 必然隨時間變快}.
}
$$

本文只證明幾種更窄的 reduction：

1. **reconstruction avoidance**：若 proof state / certificate state 已保存，就不必從頭重建；
2. **safe pruning**：若 candidate 已被 active certificate 排除，就不必重新 discovery；
3. **basis replay**：target 只需重播其 dependency basis；
4. **incremental replay**：change 只需重播 dirty descendants；
5. **pattern reuse**：已驗證 schema 可用便宜 instantiation checker 重用；
6. **amortization**：若 $\Delta>0$ 且 reuse 次數超過 break-even，平均成本下降。

真正的：

$$
C^{\rm discover}_t\downarrow
$$

與

$$
C^{\rm verify}_t+C^{\rm coverage}_t+C^{\rm glue}_t\uparrow
$$

是否出現 phase transition，留到 Paper 05 實驗與形式化。

---

# 17. No-Go Ledger

## No-Go 17.1 — Cache Equals Proof

cached search state、embedding、retrieval hit、tactic snapshot 都不是 proof certificate。

## No-Go 17.2 — Old Certificate Remains Valid Forever

任何 dependency、scope、representation、kernel / checker version 改變都可能使 certificate stale。

## No-Go 17.3 — One Stale Certificate Requires Full Reset

若同一 region 仍有其它 active supports，不必 reopen。

## No-Go 17.4 — Discovery History Equals Closure Basis

大量歷史探索可能對 final target replay 完全不再需要。

## No-Go 17.5 — Closure Basis Automatically Minimal

canonical ancestor basis 只保證 sound，不保證 minimum cost。

## No-Go 17.6 — Compiled Mode May Absorb Unknown Regions

未覆蓋 gap、boundary、mixed fiber、stale region 必須保留 Exploration Mode。

## No-Go 17.7 — Verification Can Be Skipped After Compilation

編譯只能把 full replay 改成 basis replay / instantiation replay / incremental replay；不能把 logical verification 變成零。

## No-Go 17.8 — Hidden Build Cost Can Be Ignored

若只計算 online lookup 而忽略 build、basis verification、maintenance 與 rollback，會製造假的 speedup。

## No-Go 17.9 — High Hit Rate Guarantees Speedup

若 maintenance 很高或 $c_H\approx c_F$，即使 $h$ 很高也可能有

$$
\Delta\le0.
$$

## No-Go 17.10 — Average Amortization Controls Worst-Case

平均成本下降不保證 frontier theorem 的 worst-case discovery 成本下降。

---

# 18. Paper 04 Runtime Contract

Paper 04 對未來 SDPE Runtime 新增以下最低組件：

$$
\boxed{
\mathsf{TraceCompiler}
}
$$

抽取 target closure basis；

$$
\boxed{
\mathsf{SupportIndexer}
}
$$

維護 candidate-to-certificate support；

$$
\boxed{
\mathsf{DependencyInvalidator}
}
$$

計算 stale descendant closure；

$$
\boxed{
\mathsf{RollbackPlanner}
}
$$

只 reopen support 歸零的 regions；

$$
\boxed{
\mathsf{IncrementalReplay}
}
$$

重播 dirty closure；

$$
\boxed{
\mathsf{PatternRegistry}
}
$$

保存可實例化 verified proof patterns；

$$
\boxed{
\mathsf{CostLedger}
}
$$

記錄 build、discovery、verification、coverage、glue、maintenance、rollback 與 reuse costs。

完整 pipeline 更新成：

$$
\boxed{
\begin{aligned}
&\mathsf{Detect}\to\mathsf{Route}\to\mathsf{KnownnessGate}\to\\
&\mathsf{CompiledPrune}\;\vee\;\mathsf{Explore}\to\\
&\mathsf{Verify}\to\mathsf{CoverageAudit}\to\mathsf{GlueAudit}\to\\
&\mathsf{Commit}\to\mathsf{TraceCompile}\to\mathsf{IndexUpdate}.
\end{aligned}
}
$$

任何 dependency change 則走：

$$
\boxed{
\mathsf{Invalidate}
\to
\mathsf{DirtyClosure}
\to
\mathsf{SupportRollback}
\to
\mathsf{IncrementalReplay}.
}
$$

---

# 19. 與記憶編譯型計算存在論的接軌

先前「記憶編譯型狀態智能體」提出：昂貴的搜尋、推理、驗證與試錯可以被編譯成可重用的狀態分類、索引、策略與驗證結構；「已知則編譯，未知則展開」則要求未知或漂移狀態退出快速通道。

SDPE Paper 04 將此概念限制成 proof-safe 版本：

$$
\boxed{
\text{Memory Compilation}
\to
\text{Certificate Compilation}
}
$$

只允許 active certificate 支持的區域進入 Compiled Mode。

同樣，先前「快速究竟有多快」要求完整成本帳本，而非只計 online latency。本文的 $B,h,c_H,c_F,m$ 模型正是 proof-space 的第一個簡化版本。

---

# 20. 與解空間幾何的接軌

proof trace compilation 可以被看成對 proof-state / survivor-space geometry 的改寫。

歷史 theorem cuts 不是單純增加文本，而是在建立：

- forbidden regions；
- certified bridges；
- equivalent subproblems；
- terminal closure states；
- reusable patterns；
- low-cost verification channels。

因此有效 proof distance 可能下降。

但 Paper 04 不把這種幾何直覺直接等同於 complexity theorem。只有經過成本 ledger 的 amortization condition 才能稱為實際 speedup。

---

# 21. Theorem / Hypothesis / External Input Ledger

## 21.1 Internal theorems / propositions

1. Descendant Staleness；
2. Ancestor Closure Sufficiency；
3. Safe Compiled Pruning；
4. Support-Aware Rollback；
5. Incremental Replay Equivalence；
6. Sound Pattern Reuse；
7. Amortization Break-Even；
8. Asymptotic Average Cost；
9. Pattern Verification Amortization。

## 21.2 System assumptions

1. dependency metadata complete；
2. checker compositionality；
3. deterministic replay；
4. version / scope fingerprint completeness；
5. support index completeness。

這些是 runtime correctness obligations，不可偷偷當成 theorem。

## 21.3 External technical grounding

- Lean proof-state snapshotting；
- reusable algebraic proof certificates；
- reusable Lean theorem libraries；
- lifelong formal theorem proving；
- scalable strict multi-version proof verification infrastructure。

## 21.4 Open hypotheses

Paper 04 不證：

$$
\boxed{
\text{Discovery--Verification Inversion}.
}
$$

它只建立 Paper 05 可以測量此現象所需的 formal state 與 cost primitives。

---

# 22. Checker Scope

companion checker 驗證 finite toy models 中：

1. dependency ancestor basis replay；
2. descendant staleness；
3. sound compiled pruning；
4. support-aware rollback；
5. incremental replay equivalence；
6. redundant-history basis compression；
7. known / unknown gate；
8. amortization break-even algebra；
9. pattern verification amortization。

checker 不證一般 theorem proving complexity、AI research acceleration、formalization correctness of arbitrary mathematics，亦不宣稱 discovery cost 必然遞減。

---

# 23. Paper 05 的輸入

Paper 04 現在提供可以被觀測的時間序列：

$$
\boxed{
\begin{aligned}
&C_t^{\rm discover},\\
&C_t^{\rm verify},\\
&C_t^{\rm coverage},\\
&C_t^{\rm glue},\\
&C_t^{\rm maintain},\\
&C_t^{\rm replay},\\
&h_t,\\
&\chi_t,\\
&|Dirty_t|,\\
&|R_t|.
\end{aligned}
}
$$

因此下一篇可以真正研究：

$$
\boxed{
\textbf{SDPE Paper 05 — Discovery--Verification Inversion.}
}
$$

核心問題不再只是直覺上的「越證越快」，而是：

$$
\boxed{
\text{是否存在可重現的 phase regime，使 marginal discovery cost 下降，}
}
$$

同時：

$$
\boxed{
\text{verification / coverage / maintenance share 上升？}
}
$$

---

# 24. Final Status

Paper 01 回答：

$$
\boxed{
\text{怎麼安全縮 survivor space？}
}
$$

Paper 02 回答：

$$
\boxed{
\text{怎麼保證 route representation 沒有先把反例壓掉？}
}
$$

Paper 03 回答：

$$
\boxed{
\text{怎麼證 local routes 真正 cover 並 closure global domain？}
}
$$

Paper 04 現在回答：

$$
\boxed{
\text{怎麼把這些已驗證歷史編譯成可增量重用、可 rollback、可攤銷的 proof state？}
}
$$

整個 closure stack 因此成為：

$$
\boxed{
\begin{aligned}
&\text{Sound Survivor Envelope}\\
&\downarrow\\
&\text{Faithful Route Representation}\\
&\downarrow\\
&\text{Global Coverage / Closure Certificate}\\
&\downarrow\\
&\text{Closure Basis}\\
&\downarrow\\
&\text{Compiled Pruning State}\\
&\downarrow\\
&\text{Incremental Replay / Support-Aware Rollback}.
\end{aligned}
}
$$

至此，「把痕跡留下來」已不只是 provenance 原則，而被提升成一個正式的計算命題：

$$
\boxed{
\textbf{如果 proof trace 具有完整 dependency、scope、version 與 replay semantics，}
}
$$

則它可以被編譯成 sound pruning 與 incremental verification infrastructure，而不是每輪重新展開整個 proof history。

---

# References

1. Austin Shen and Yunong Shi, **Keep the Proof State Live: Snapshotting for Efficient Tactic Search in Lean 4**, arXiv:2605.25556, 2026.
2. Daniela Kaufmann and Clemens Hofstadler, **Recycling Algebraic Proof Certificates**, arXiv:2507.20267, 2025.
3. Ziyi Yang, Wenji Fang, Chen Chen, Zhiyao Xie, Hongce Zhang, **CircuitProver: Agentic Lean 4 Theorem Proving with Reusable Circuit Proof Library for Hardware Verification**, arXiv:2607.27259, 2026.
4. Hongqin Lyu, Junxing Dong, Yonghao Wang, Zhiteng Chao, Tiancheng Wang, Huawei Li, **Rtl2lean: Automated RTL-to-Lean Translation with Hierarchical Theorem Generation and Lemma Reuse**, arXiv:2607.16855, 2026.
5. Adarsh Kumarappan et al., **LeanAgent: Lifelong Learning for Formal Theorem Proving**, arXiv:2410.06209, 2024.
6. Jimmy Xin et al., **AXLE: A Cloud Infrastructure for Lean 4 Theorem Proving Utilities**, arXiv:2606.26442, 2026.
7. Prior SDPE artifact: **Paper 01 — Global Quantifiers, Counterexample Domains, and Verifiable Contraction**.
8. Prior SDPE artifact: **Paper 02 — Route-Domain Completeness and Representation Non-Collapse**.
9. Prior SDPE artifact: **Paper 03 — Multidimensional Coverage, Gaps, and Global Closure Certificates**.
10. Prior internal series artifact: **記憶編譯型計算存在論**.
11. Prior internal series artifact: **解空間幾何計算論：從 P/NP 二分到概念積分快速通道**.
