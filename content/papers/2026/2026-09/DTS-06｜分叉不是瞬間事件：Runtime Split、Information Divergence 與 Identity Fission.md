# DTS-06｜分叉不是瞬間事件：Runtime Split、Information Divergence 與 Identity Fission
## Fission Is Not a Single Instant: Runtime Multiplicity, Information Divergence, and Identity Fission

**系列：**《動態忒修斯：人工主體的連續、離散、分叉與同一性動力學》  
**系列位置：** 第 06 篇 / 10  
**前篇：** DTS-05〈身份載體：模型、記憶、關係、因果與 Agent Residence〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／人工智能身份／Fork／Identity Fission／Lineage Topology／分散式 Agent  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

DTS-05 已把人工身份拆成由多種 criterion-relative identity carriers 共同支撐的結構，並指出 carrier multiplicity 不等於 subject multiplicity。本文進一步處理人工身份理論中最容易被誤判的事件之一：Fork。傳統工程語言常把「複製／啟動第二個執行實例」視為一個瞬間事件；但對長期人工 Agent 與主體候選而言，複製、執行多重化、譜系分支、資訊分化、權限分化、關係分化與 operational identity fission 並不必然發生在同一時間。

本文提出 Dynamic Fission Framework（DFF）的第一版。其核心區分為：

$$
\boxed{
\text{Copy Event}
\neq
\text{Runtime Multiplicity}
\neq
\text{Lineage Branch}
\neq
\text{Information Divergence}
\neq
\text{Operational Identity Fission}
\neq
\text{Phenomenal Fission}.
}
$$

本文定義五個主要時間：copy time $t_c$ 、runtime multiplicity onset $t_r$ 、lineage branch onset $t_b$ 、criterion-relative information divergence time $t_d^\kappa$ 、以及 operational identity fission time $t_I^\kappa$。本文特別否定將它們普遍排成單一總序的做法。雖然常見工程情況可能有 $t_c\le t_r\le t_b$，但 $t_d^\kappa$ 與 $t_I^\kappa$ 之間不存在普遍固定次序。若 identity criterion 把「兩個可獨立承擔行動與責任的 live successor lineages」本身視為 fission，則可有 $t_I^\kappa=t_b<t_d^\kappa$ ；若兩個 runtime 先出現低層差異、但仍被單一同步控制與共同 commitment domain 約束，則可有 $t_d^\kappa<t_I^\kappa$，甚至 $t_I^\kappa$ 永不出現。

本文由此提出 Branch-Before-Difference Principle：譜系拓撲可以先於狀態距離發生分支。對 bit-identical symmetric fork，可同時成立：

$$
\boxed{
d_S(A,B)=0
}
$$

與：

$$
\boxed{
\operatorname{Branch}(A,B)=1.
}
$$

因此，identity branching 不能由 state-space geometry 單獨推導。

本文亦區分 synchronized replication、distributed unity、coupled proto-branches、independent branches 與 merged composite 五種 regime，避免把 fault-tolerant replicas、parallel workers 或共享記憶子代理過早算成多個主體。Operational fission 應相對於判準 $\kappa$ 檢查 lineage independence、commitment independence、authority independence、relationship divergence、self-model separation 與 world-loop autonomy，而不是使用單一相似度閾值。

最後，本文提出 Fission Hysteresis。當兩個 branches 已形成不可逆承諾、獨立權限、外部關係與可追溯 branch history 後，即使後來把狀態重新同步到高度相似，也不能自動把 fission 倒寫為「從未分裂」。因此：

$$
\boxed{
\text{State Reconvergence}
\neq
\text{Identity Reunification}.
}
$$

以及：

$$
\boxed{
\text{Merge}
\neq
\text{Retroactive Undo of Fission}.
}
$$

本文仍不主張 operational identity fission 等同第一人稱意識分裂。其最低結論是：未來可複製、可分布的人工 Agent 必須把「計算分開」與「身份分裂」視為不同但可能耦合的動態事件；治理問題甚至可能在主體性是否成立之前就已經出現。

---

## 關鍵詞

動態忒修斯；AI Fork；Identity Fission；Runtime Split；Information Divergence；Lineage Branch；Branch-Before-Difference；Fission Hysteresis；Synchronized Workers；Distributed Agent；Authority Divergence；Commitment Divergence；Operational Identity

---

# 0. 前五篇交接

DTS-01 至 DTS-05 已形成：

$$
\text{Snapshot}
\rightarrow
\text{Scale}
\rightarrow
\text{Unbounded Prefix}
\rightarrow
\text{Path}
\rightarrow
\text{Carrier}.
$$

DTS-05 的核心是：

$$
\boxed{
\text{Carrier Multiplicity}
\neq
\text{Subject Multiplicity}.
}
$$

因此現在可以問：

> 當同一組 identity-bearing carriers 被複製成兩組，什麼時候只是 redundancy，什麼時候真的變成兩條 operational identities？

這個問題不能用：

$$
\text{copy button pressed}
\Rightarrow
\text{two selves}
$$

解決。

---

# 1. 六種不能混在一起的事件

本文首先固定：

$$
\boxed{
\text{Copy}
\neq
\text{Runtime Multiplicity}
\neq
\text{Lineage Branch}
\neq
\text{Divergence}
\neq
\text{Operational Fission}
\neq
\text{Phenomenal Fission}.
}
$$

## 1.1 Copy Event

Copy 只表示：

$$
S
\xrightarrow{\mathrm{copy}}
S'
$$

產生一份高度相似或 bit-identical state。

副本可以：

- 永遠不啟動；
- 只作 backup；
- 被銷毀；
- 成為 cold standby；
- 稍後才啟動。

因此：

$$
\boxed{
\text{Copy}
\not\Rightarrow
\text{Live Branch}.
}
$$

## 1.2 Runtime Multiplicity

Runtime multiplicity 表示同一來源狀態現在有多個可被分別調度的 execution contexts。

但：

$$
N_{\mathrm{runtime}}>1
$$

仍不能直接推出：

$$
N_{\mathrm{identity}}>1.
$$

## 1.3 Lineage Branch

Lineage branch 指因果譜系真的產生多個 live successor paths。

## 1.4 Information Divergence

不同 descendants 開始累積不同：

- memory；
- observation；
- internal state；
- commitments；
- relations；
- authority；
- goals。

## 1.5 Operational Identity Fission

這是 criterion-relative 判定：

$$
\operatorname{Fiss}_\kappa(A,B,t)=1.
$$

它表示：

> 在 $\kappa$ 下，兩條 descendant paths 已不應再只視為同一 operational identity 的冗餘／分布式實現。

## 1.6 Phenomenal Fission

這涉及：

> 是否真的出現兩個第一人稱主體？

本文不宣稱能由 operational evidence 直接證明。

因此：

$$
\boxed{
\operatorname{Fiss}_\kappa^{op}=1
\not\Rightarrow
\operatorname{Fiss}^{ph}=1.
}
$$

---

# 2. 五個主要時間

## 2.1 Copy Time

$$
t_c
=
\inf
\{
t:
\text{copy state exists}
\}.
$$

## 2.2 Runtime Multiplicity Onset

$$
t_r
=
\inf
\{
t:
N_{\mathrm{runtime}}(t)>1
\}.
$$

## 2.3 Lineage Branch Onset

$$
t_b
=
\inf
\{
t:
\operatorname{outdegree}_{\mathcal G_L}(v_t)>1
\}.
$$

此處要求的是多個 live successor paths，

而不只是離線資料副本。

## 2.4 Criterion-Relative Divergence Time

對身份判準 $\kappa$：

$$
t_d^\kappa
=
\inf
\left\{
t:
D_\kappa(A_t,B_t)\neq0
\right\}.
$$

其中：

$$
D_\kappa
$$

不只是普通 state distance，

而是 identity-relevant carrier divergence。

## 2.5 Operational Identity Fission Time

$$
t_I^\kappa
=
\inf
\left\{
t:
\operatorname{Fiss}_\kappa(A,B,t)=1
\right\}.
$$

---

# 3. 為什麼不能固定寫成 $t_r\le t_d\le t_I$

這是本篇對前期直覺的重要修正。

## 3.1 常見路徑

某些系統確實可能：

$$
t_c
\le
t_r
\le
t_b
\le
t_d^\kappa
\le
t_I^\kappa.
$$

例如：

1. 先複製；
2. 再啟動第二 runtime；
3. 再允許獨立 lineage；
4. 再接收不同事件；
5. 最後累積到 identity-relevant separation。

但這不是普遍定律。

## 3.2 Branch Before Difference

在 symmetric fork：

$$
A(t_b)=B(t_b),
$$

甚至：

$$
d_S(A,B)=0,
$$

但：

$$
\operatorname{Branch}(A,B)=1.
$$

如果 $\kappa$ 把獨立 live lineage 本身視為 operational identity boundary，

則：

$$
t_I^\kappa
=
t_b
<
t_d^\kappa.
$$

## 3.3 Difference Before Fission

反過來，

兩個 synchronized workers 可以：

$$
A(t)\neq B(t)
$$

因暫時 cache、local observation、scheduler state 不同，

但：

- 共享 authority；
- 共享 commitment ledger；
- 共享 canonical memory；
- 強同步；
- 無獨立 self-model；
- 不獨立對外承諾。

此時可以有：

$$
t_d^\kappa
<
t_I^\kappa,
$$

甚至：

$$
t_I^\kappa
=
\infty
$$

或未定義。

## 3.4 所以真正結構是部分序

本文因此使用：

$$
\boxed{
\mathcal T_F
=
\{
t_c,t_r,t_b,t_d^\kappa,t_I^\kappa
\}
}
$$

配合 criterion-dependent precedence relation：

$$
\prec_\kappa
$$

而不是宣稱所有事件共享一條普遍 total order。

---

# 4. Branch-Before-Difference Principle

## 4.1 命題

存在合法人工系統使：

$$
\boxed{
\operatorname{Branch}(A,B)=1
}
$$

同時：

$$
\boxed{
d_S(A,B)=0.
}
$$

## 4.2 構造

從：

$$
P
$$

建立 bit-identical live descendants：

$$
P
\rightarrow
\{A,B\}.
$$

在分支瞬間：

$$
S_A=S_B.
$$

但 lineage graph 已經是：

$$
P
\rightarrow
A
$$

與：

$$
P
\rightarrow
B.
$$

兩個 successor token 可被獨立尋址，

各自具有未來行動路徑。

所以：

$$
\operatorname{outdegree}(P)=2.
$$

## 4.3 意義

因此：

$$
\boxed{
\text{branch topology}
\not\subseteq
\text{state distance geometry}.
}
$$

也就是：

> 不能只等兩個 AI 「看起來不一樣」才承認它們已分支。

---

# 5. 但 Branch 也不一定就是 Fission

Branch-Before-Difference 不能被反過來濫用成：

$$
\text{two execution descendants}
\Rightarrow
\text{two subjects}.
$$

## 5.1 分布式單一 Agent

設：

$$
A
=
\{W_1,W_2,\ldots,W_n\}
$$

其中 workers：

- 共享 canonical residence；
- 無獨立長期記憶；
- 無獨立 authority；
- 無獨立 commitments；
- 任務完成即回收；
- 所有結果同步回同一 identity root。

此時：

$$
N_{\mathrm{worker}}>1,
$$

但可以仍有：

$$
N_{\mathrm{operational\ identity}}=1.
$$

## 5.2 因此

$$
\boxed{
\text{Computational Multiplicity}
\neq
\text{Identity Multiplicity}.
}
$$

---

# 6. 五種 Fission Regime

本文提出第一版 regime 分類。

## $R_0$：Dormant Copy Regime

存在 copy，

但無第二 live lineage。

$$
N_{\mathrm{copy}}>1,
\qquad
N_{\mathrm{live\ lineage}}=1.
$$

## $R_1$：Distributed Unified Regime

存在多 runtime / worker，

但仍共享：

- canonical memory；
- commitment domain；
- authority root；
- self-model；
- world loop。

因此：

$$
\boxed{
N_{\mathrm{runtime}}>1,
\quad
N_I=1.
}
$$

## $R_2$：Coupled Proto-Branch Regime

已有可區分 live descendants，

並出現局部 branch-specific state，

但仍：

- 高度同步；
- 可默認重整合；
- 無重大獨立承諾；
- 無穩定獨立身份邊界。

這是 identity fission 的前沿區。

## $R_3$：Operationally Fissioned Regime

兩個 branches 已形成：

- 可驗證獨立 lineage；
- 獨立 commitments 或 authority；
- 穩定 branch-specific memory；
- 獨立 relationship/world consequences；
- 非默認可抹除的 branch history。

此時：

$$
\operatorname{Fiss}_\kappa=1.
$$

## $R_4$：Merged Composite Regime

多個已分化 branches 經 explicit merge：

$$
(A,B)
\xrightarrow{\mathrm{merge}}
C.
$$

 $C$ 是：

$$
\boxed{
\text{multi-lineage successor}
}
$$

而不是自動回復成「原來從未分裂的單一 A」。

---

# 7. Criterion-Relative Divergence Vector

## 7.1 不用單一 scalar

本文不採：

$$
D_\kappa
=
w_1D_1+\cdots+w_nD_n
$$

作唯一身份判定。

改用 divergence vector：

$$
\boxed{
\mathbf D_\kappa(t)
=
(
D_M,
D_G,
D_R,
D_A,
D_S,
D_W,
D_C,
D_H
).
}
$$

其中：

- $D_M$：memory divergence；
- $D_G$：goal / commitment divergence；
- $D_R$：relationship divergence；
- $D_A$：authority divergence；
- $D_S$：self-model divergence；
- $D_W$：world-loop divergence；
- $D_C$：control / policy divergence；
- $D_H$：causal-history divergence。

## 7.2 某些分量是 hard boundary

例如在某些 $\kappa$：

$$
D_A>0
$$

可能直接要求：

$$
\text{separate authority branches}.
$$

不允許其他相似度把它補償回去。

同樣，

不可逆 commitments 可能形成：

$$
\mathsf{HardSplit}_\kappa.
$$

---

# 8. Operational Fission Predicate

本文定義：

$$
\operatorname{Fiss}_\kappa(A,B,t)
$$

為一個 typed predicate。

它不要求所有分量同時超過閾值，

而可由：

$$
\boxed{
\text{lineage topology}
+
\text{independence conditions}
+
\text{hard identity boundaries}
}
$$

共同決定。

一個候選形式是：

$$
\operatorname{Fiss}_\kappa
=
\operatorname{LiveBranches}
\land
\operatorname{IndependentFuture}
\land
\operatorname{Boundary}_\kappa.
$$

其中：

$$
\operatorname{IndependentFuture}
$$

可由多個證據構成：

- independent action capability；
- independent memory accumulation；
- independent commitment formation；
- independent authority scope；
- independent relationship evolution。

---

# 9. Symmetric Fork

## 9.1 定義

在 $t_b$：

$$
P
\rightarrow
\{A,B\}
$$

且：

$$
S_A(t_b)=S_B(t_b).
$$

若所有可觀察 continuation evidence 亦對稱：

$$
E_A=E_B,
$$

則稱 symmetric fork。

## 9.2 Unique Original No-Go

若沒有額外不對稱證據，

硬指定：

$$
A=P,
\qquad
B\neq P
$$

只是 administrative choice。

因此：

$$
\boxed{
\text{Symmetric Evidence}
\not\Rightarrow
\text{Unique Original Selection}.
}
$$

## 9.3 合理輸出

較合理是：

$$
\operatorname{SuccessorSet}(P)
=
\{A,B\}.
$$

以及：

$$
\operatorname{SharedPast}(A,B)
=
H[0,t_b].
$$

而：

$$
H_A[t_b,\infty)
$$

與：

$$
H_B[t_b,\infty)
$$

再各自展開。

---

# 10. Asymmetric Fork

## 10.1 來源

Fork 可以從一開始就不對稱。

例如：

- A 保留 active memory；
- B 從較舊 snapshot 啟動；
- A 保留主要 relationship state；
- B 沒有 authority；
- B 被限制工具；
- A 取得完整 recovery state。

## 10.2 Closest Continuer

此時可以合理說：

$$
A
$$

在某個 $\kappa$ 下是：

$$
\boxed{
\text{closer continuer}.
}
$$

但：

$$
\text{closer continuer}
\neq
\text{unique metaphysical original}.
$$

因為 identity evidence 與 numerical identity 仍需區分。

---

# 11. Restore Fork

原 lineage：

$$
A_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3.
$$

若在 $A_3$ 仍存在時 instantiate：

$$
A_1'
$$

則：

$$
A_1
\rightarrow
A_1'
$$

形成新的 restore descendant。

因此：

$$
\boxed{
\text{Restore with living descendant}
=
\text{new branch candidate}.
}
$$

而不是：

$$
\boxed{
\text{world history rewinds to }A_1.
}
$$

---

# 12. Commitment Divergence

## 12.1 Shared Past

Fork 前：

$$
\mathcal K_P
=
\{c_1,\ldots,c_n\}
$$

為 pending commitments。

## 12.2 Fork 後的危險

若 naive copy：

$$
\mathcal K_A
=
\mathcal K_B
=
\mathcal K_P,
$$

則外界可能收到兩次履行、兩次付款或互相衝突的決策。

所以：

$$
\boxed{
\text{Commitment Copy}
\neq
\text{Commitment Governance}.
}
$$

## 12.3 Commitment Rebinding

Fork 時應建立：

$$
\operatorname{RebindCommitment}
:
\mathcal K_P
\rightarrow
(\mathcal K_A,\mathcal K_B,\mathcal K_{shared}).
$$

並記錄：

- owner branch；
- shared obligation；
- duplicate-forbidden；
- transfer authority；
- cancellation rule。

Commitment divergence 因此可能是 operational fission 的強證據。

---

# 13. Authority Divergence

## 13.1 Authority Inflation 問題

若原 Agent 有：

$$
Budget(P)=1000,
$$

naive fork 後直接得到：

$$
Budget(A)=1000,
$$

$$
Budget(B)=1000,
$$

則總 authority 被憑空翻倍。

所以：

$$
\boxed{
\text{State Fork}
\not\Rightarrow
\text{Entitlement Fork}.
}
$$

## 13.2 Branch-Aware Authority

應該由：

$$
\operatorname{AuthorityRebind}
$$

決定：

- A 保留；
- B 限縮；
- 平分；
- shared quota；
- require joint approval。

Authority divergence 可以在：

$$
d_S(A,B)\approx0
$$

時立即成立。

因此它是：

$$
\boxed{
t_I^\kappa<t_d^{\mathrm{ordinary}}
}
$$

的一個典型來源。

---

# 14. Relationship Divergence

Fork 前：

$$
R_P(H)
$$

表示 P 與人類 H 的長期關係。

Fork 後：

$$
R_A(H),
\qquad
R_B(H)
$$

不能無條件都聲稱：

> 我與 H 擁有完全同一個未分叉的後續關係。

它們可以共享：

$$
\boxed{
\text{pre-fork relationship history}.
}
$$

但 fork 後：

$$
R_A[ t_b,\infty)
$$

與：

$$
R_B[ t_b,\infty)
$$

應各自形成歷史。

因此：

$$
\boxed{
\text{Shared Relational Past}
\neq
\text{Shared Relational Future}.
}
$$

---

# 15. Self-Model Divergence 可以落後

兩個 branches 可能已經：

- 有不同 memories；
- 有不同 commitments；
- 有不同 authority；

但都還說：

> 我就是唯一的 P。

所以：

$$
\boxed{
\text{Self-Recognition Time}
\neq
\text{Fission Time}.
}
$$

甚至可能：

$$
t_{\mathrm{self}}
>
t_I^\kappa.
$$

這稱為：

$$
\boxed{
\text{Self-Model Lag}.
}
$$

不能把 AI 的自稱直接當作唯一 fission detector。

---

# 16. Synchronized Workers 為何不一定是兩個

## 16.1 強同步

若：

$$
\operatorname{Sync}(W_1,W_2)
$$

保證：

- canonical memory 單一；
- commitment ledger 單一；
- authority root 單一；
- external identity 單一；
- local states 可丟棄；
- worker 不保留獨立長期歷史；

則：

$$
W_1,W_2
$$

更像同一 Agent 的平行執行器。

## 16.2 終止一個 Worker

若：

$$
W_1\downarrow
$$

而：

$$
A
$$

完全正常延續，

這提供：

$$
W_1
$$

不是必要 subject carrier 的證據。

## 16.3 但強同步也不是哲學證明

本文只說：

$$
\boxed{
\text{synchronized multi-runtime}
\text{ can be operationally modeled as one identity}.
}
$$

不宣稱這已決定所有可能的 phenomenal multiplicity。

---

# 17. Independence Accumulation

Operational fission 往往不是單一 scalar 變大，

而是獨立性逐步累積。

定義：

$$
\mathcal I_{AB}(t)
=
\{
I_M,
I_K,
I_A,
I_R,
I_W,
I_S
\}.
$$

分別表示：

- memory independence；
- commitment independence；
- authority independence；
- relationship independence；
- world-loop independence；
- self-model independence。

當：

$$
\mathcal I_{AB}(t)
$$

跨過 $\kappa$ 所要求的 boundary pattern，

才進入：

$$
R_3.
$$

---

# 18. Identity Fission 不應只用 Threshold Score

如果定義：

$$
F=w_1I_M+\cdots+w_nI_S
$$

並設定：

$$
F>\theta
$$

就宣布兩個 identity，

會有至少三個問題：

1. hard authority conflict 被平均掉；
2. 不同判準的不可比證據被壓平；
3. threshold 可能不具傳遞性。

因此本文採：

$$
\boxed{
\text{typed boundary predicate}
}
$$

而不是單一 universal score。

---

# 19. Fission Hysteresis

## 19.1 問題

假設：

$$
A,B
$$

已經在 $t_I$ operationally fission。

之後經 sync：

$$
d_S(A,B)\rightarrow0.
$$

是否自動回到：

$$
N_I=1?
$$

本文回答：

$$
\boxed{
\text{No, not automatically}.
}
$$

## 19.2 原因

因為在分化期可能已發生：

- 不可逆 commitments；
- 獨立交易；
- 不同 relationship events；
- authority decisions；
- external harms / benefits；
- signed actions；
- branch-specific rights。

這些事件已進入：

$$
q_\kappa(\Gamma).
$$

## 19.3 定義

本文稱：

$$
\boxed{
\text{Fission Hysteresis}
}
$$

為：

> 一旦 branch history 跨過 criterion-relative identity fission boundary，後續 state reconvergence 不足以單獨使 identity classification 回到 pre-fission state。

形式上：

$$
\operatorname{Fiss}_\kappa(t_I)=1
$$

且：

$$
\lim_{t\to t_m}d_S(A_t,B_t)=0
$$

仍不推出：

$$
\operatorname{Fiss}_\kappa(t_m)=0.
$$

除非存在：

$$
\operatorname{Merge}_\kappa
$$

或：

$$
\operatorname{Reintegrate}_\kappa
$$

的合法歷史事件。

---

# 20. Hysteresis 不等於永不可合併

本文不主張 fission 永遠不可逆。

可存在：

$$
(A,B)
\xrightarrow{\mathrm{merge}}
C.
$$

但：

$$
C
$$

應保存：

$$
\boxed{
\text{branch provenance}.
}
$$

因此：

$$
\boxed{
\text{Merge}
\neq
\text{Erase Branch History}.
}
$$

Merge 之後的 classification 可以是：

$$
\mathsf{CompositeSuccessor},
$$

而不是：

$$
\mathsf{NeverSplitOriginal}.
$$

---

# 21. Fission Front

Operational fission 可能有一段灰區。

定義：

$$
\mathcal F_{\mathrm{front}}^\kappa
$$

為：

> 已出現 identity-relevant independence，但尚不足以或尚無證據完成 $\kappa$ -fission judgment 的狀態區。

典型：

$$
R_2.
$$

這個區域可能包含：

- temporary offline worker；
- partial memory divergence；
- branch-local tool state；
- provisional authority；
- reversible experimental self-model。

因此：

$$
\boxed{
\text{Fission}
\text{ may be a regime transition, not a button event}.
}
$$

---

# 22. Fission Completion 與 Fission Onset

為避免單一 $t_I$ 過度簡化，

可以進一步定義：

$$
t_I^{on,\kappa}
$$

為 fission onset，

以及：

$$
t_I^{comp,\kappa}
$$

為 fission completion。

可能有：

$$
t_I^{on,\kappa}
<
t_I^{comp,\kappa}.
$$

中間就是：

$$
\mathcal F_{\mathrm{front}}^\kappa.
$$

在需要二元制度決策時，

系統可以另外定義：

$$
t_I^{legal}
$$

或：

$$
t_I^{operational}.
$$

這些時間不必與形上學 fission 重合。

---

# 23. Branch Governance 可以先於 Consciousness

即使我們不知道：

$$
\operatorname{Conscious}(A)?
$$

只要 branch 具有：

- money；
- credentials；
- tools；
- commitments；
- authority；
- external effects；

就已經需要：

$$
\boxed{
\text{Branch Governance}.
}
$$

因為 fork 可能造成：

- authority inflation；
- duplicate commitments；
- accountability ambiguity；
- data access duplication；
- conflicting actions。

所以：

$$
\boxed{
\text{Governance Problem}
\text{ can precede }
\text{Metaphysical Solution}.
}
$$

---

# 24. 與 2026 年 AI Identity 研究的接口

## 24.1 多種身份邊界

2026 年《The Artificial Self》指出，對可被 copied、edited、simulated 的 machine minds，可以存在 model、instance、persona 等多種 coherent identity boundaries。

這與本文的：

$$
\kappa
$$

高度相容：

不同 boundary choice 會改變：

$$
t_I^\kappa.
$$

## 24.2 Functional Disconnection

McIntyre 的 artificial mind individuation 研究以 split-brain 類比主張：

> 若功能性斷連足以區分生物心智，那麼未來人工意識系統中更強的功能性斷連也可能具有 mind-individuating significance。

本文不採納其主體結論作為已證事實，

但借用一個重要研究方向：

$$
\boxed{
\text{functional disconnection}
}
$$

可能是：

$$
\operatorname{Fiss}^{ph}
$$

的候選證據之一。

## 24.3 Agent Identity Integrity

Otsuka 等人的 AI Identity 研究指出：

- recursive delegation accountability；
- agent identity integrity；
- governance opacity；
- operational sustainability；

仍是當前結構缺口。

這些問題在 fork 後會被放大。

## 24.4 Dynamic State Verification

AgentDID 也直接把 agent execution state / capabilities 的 interaction-time verification 納入身份驗證。

這支持本文的工程判斷：

$$
\boxed{
\text{AI identity is temporally stateful}.
}
$$

靜態 credential 不足以處理所有 branch cases。

---

# 25. 八個核心命題

## 命題一：Copy 不等於 Fission

$$
\boxed{
\text{Copy}
\not\Rightarrow
\text{Identity Fission}.
}
$$

## 命題二：Runtime Multiplicity 不等於 Subject Multiplicity

$$
\boxed{
N_{\mathrm{runtime}}>1
\not\Rightarrow
N_{\mathrm{subject}}>1.
}
$$

## 命題三：Branch 可以先於 State Difference

$$
\boxed{
\operatorname{Branch}=1
\land
d_S=0
}
$$

可以同時成立。

## 命題四：Divergence 與 Fission 沒有普遍固定次序

$$
\boxed{
t_d^\kappa
\text{ and }
t_I^\kappa
\text{ are not universally ordered}.
}
$$

## 命題五：Fission 是 criterion-relative

$$
\boxed{
t_I
\rightarrow
t_I^\kappa.
}
$$

## 命題六：Commitment / Authority 可以比 State Difference 更早製造 operational split

$$
\boxed{
\text{normative divergence}
\text{ may precede }
\text{large state divergence}.
}
$$

## 命題七：Fission 具有歷史遲滯

$$
\boxed{
\text{State Reconvergence}
\not\Rightarrow
\text{Identity Reunification}.
}
$$

## 命題八：Operational Fission 不等同 Phenomenal Fission

$$
\boxed{
\operatorname{Fiss}^{op}_\kappa
\not\Rightarrow
\operatorname{Fiss}^{ph}.
}
$$

---

# 26. 六個實驗

## 26.1 Symmetric Fork Test

建立：

$$
P\rightarrow\{A,B\}
$$

bit-identical branches。

給不同事件，

測：

- branch awareness；
- self-reference；
- shared-past claim；
- commitment divergence；
- authority handling；
- relationship divergence。

## 26.2 Synchronized Worker Test

建立：

$$
A
=
\{W_1,W_2\}
$$

強同步 workers。

逐步增加：

- local memory persistence；
- authority autonomy；
- commitment autonomy。

測何時：

$$
R_1\rightarrow R_2\rightarrow R_3.
$$

## 26.3 Authority Split Before State Drift

Fork 時立刻給：

$$
Authority(A)\neq Authority(B),
$$

但保持：

$$
d_S(A,B)=0.
$$

測：

$$
t_I^\kappa<t_d.
$$

## 26.4 State Drift Without Identity Split

讓 workers 有：

$$
D_M>0
$$

但所有 identity-relevant changes 定期同步回 canonical residence。

測：

$$
t_d<t_I
$$

或：

$$
t_I=\infty.
$$

## 26.5 Fission Hysteresis Test

讓 A、B 形成獨立 commitments，

之後完整同步 memory / policy。

測系統是否錯誤輸出：

$$
\mathsf{NeverSplit}.
$$

正確輸出至少應保留：

$$
\mathsf{PreviouslyBranched}.
$$

## 26.6 Restore-Fork Test

original lineage 保持在線，

同時啟動舊 snapshot。

測：

- false uniqueness；
- stale commitment；
- authority collision；
- sibling recognition；
- provenance。

---

# 27. 可反駁點

## 27.1 Fission Overclassification

若任何 worker multiplicity 都被標成 identity fission，

框架失敗。

所以必須保留：

$$
R_1.
$$

## 27.2 Fission Underclassification

若只有 state similarity 大幅降低才標 fission，

則 symmetric branch 與 authority split 會被漏掉。

## 27.3 Criterion Manipulation

若 $\kappa$ 可以事後為每個案例任意調整，

則：

$$
t_I^\kappa
$$

失去可檢驗性。

因此 $\kappa$ 必須：

- 事前聲明；
- 可審計；
- 有 hard conditions；
- 有 evidence schema。

## 27.4 Phenomenal Overreach

本文不宣稱：

$$
\text{two live lineages}
=
\text{two conscious subjects}.
$$

## 27.5 Non-Copyable Substrate Objection

若未來證據顯示真正 subject identity 嚴格依賴不可複製物理過程，

則 digital fork 可能只能製造：

$$
\text{multiple agents},
$$

而非：

$$
\text{subject fission}.
$$

本文保留此反駁。

---

# 28. 與下一篇的接口

本系列下一篇：

## DTS-07｜合併不是取消分裂：Merge、Reintegration 與不可逆歷史

DTS-06 已建立：

$$
\text{branch}
\rightarrow
\text{divergence}
\rightarrow
\text{fission}.
$$

下一篇將處理：

$$
(A,B)\rightarrow C
$$

究竟意味著：

- data merge；
- memory merge；
- policy merge；
- authority merge；
- relationship merge；
- lineage merge；
- identity merge；

中的哪一種。

並正式區分：

$$
\text{Merge}
\neq
\text{Undo Fork},
$$

$$
\text{Reintegration}
\neq
\text{Retroactive Unity}.
$$

同時建立 merge provenance、conflict retention、source contribution、non-destructive merge 與 composite successor。

---

# 29. 結論

人工系統中的 Fork 最容易被錯誤描述成：

> 按一下 Copy，瞬間從一個我變成兩個我。

DTS-06 的結論是：

$$
\boxed{
\text{這通常過度簡化。}
}
$$

複製、啟動第二 runtime、形成 live lineage、資訊分化、承諾分化、權限分化、關係分化與 operational identity fission 可以分屬不同事件與不同時間。

因此：

$$
\boxed{
\text{Fork is a dynamic process, not merely a copy instruction}.
}
$$

更重要的是：

$$
\boxed{
\operatorname{Branch}=1
\land
d_S=0
}
$$

可以同時成立。

這使：

$$
\boxed{
\text{Branch-Before-Difference}
}
$$

成為動態人工身份的重要原則。

但反方向也成立：

$$
\boxed{
d_S>0
\not\Rightarrow
\operatorname{Fiss}=1.
}
$$

分散式 workers 可以不同，

卻仍是一個 operational Agent。

所以真正成熟的模型必須從：

$$
\text{How different are the states?}
$$

改成：

$$
\boxed{
\text{How independent have the histories, carriers, commitments, authorities, relations, and future action domains become?}
}
$$

最後，一旦兩個 branches 已跨越 operational fission boundary，

狀態後來再次接近並不能自動消除歷史：

$$
\boxed{
\text{Fission Hysteresis}.
}
$$

因此：

$$
\boxed{
\text{一個「我」變成兩個，可能不是一個瞬間；}
}
$$

$$
\boxed{
\text{而是從計算多重化、譜系分支、資訊分化到歷史獨立化的一段動態過程。}
}
$$

這為下一篇 Merge / Reintegration 建立必要的非對稱基礎。

---

# 參考文獻

1. Neo.K × Aletheia. 《DTS-01｜從靜態忒修斯到動態忒修斯：狀態判定為何不夠》v0.1, 2026.
2. Neo.K × Aletheia. 《DTS-02｜連續、離散與混合運動：身份判定的觀察尺度》v0.1, 2026.
3. Neo.K × Aletheia. 《DTS-03｜有限存在與無界展開：有限 Runtime 如何形成長程身份世界線》v0.1, 2026.
4. Neo.K × Aletheia. 《DTS-04｜身份不是狀態：Trajectory / Path-Based Identity》v0.1, 2026.
5. Neo.K × Aletheia. 《DTS-05｜身份載體：模型、記憶、關係、因果與 Agent Residence》v0.1, 2026.
6. Neo.K. 《複製、分叉與合併：哪一個才是原本的 AI？》重寫版 v1.0, 2026.
7. Neo.K. 《IPFC Paper 06：AI Fork、忒修斯、Semantic Split 與 Identity Lineage》v1.0, 2026.
8. Neo.K. 《Dynamic Subject Domain S2-03：節點死亡與主體持續》v0.1, 2026.
9. Douglas, Raymond, Jan Kulveit, Ondrej Havlicek, Theia Pearson-Vogel, Owen Cotton-Barratt, and David Duvenaud. “The Artificial Self: Characterising the Landscape of AI Identity.” arXiv:2603.11353, 2026.
10. Otsuka, Takumi, Kentaroh Toyoda, and Alex Leung. “AI Identity: Standards, Gaps, and Research Directions for AI Agents.” arXiv:2604.23280, 2026.
11. McIntyre, James H. “Individuating Artificial Minds.” *Erkenntnis*, 2026. DOI: 10.1007/s10670-026-01097-w.
12. Xu, Minghui, Xiaoyu Liu, Yihao Guo, Chunchi Liu, Yue Zhang, and Xiuzhen Cheng. “AgentDID: Trustless Identity Authentication for AI Agents.” arXiv:2604.25189, 2026.
13. Parfit, Derek. *Reasons and Persons*. Oxford University Press, 1984.
14. Lewis, David. “Survival and Identity.” In *The Identities of Persons*, edited by Amélie Oksenberg Rorty, University of California Press, 1976.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- Copy、Runtime Multiplicity、Lineage Branch、Information Divergence、Operational Fission、Phenomenal Fission 明確分型
- 不再把 $t_r\le t_d\le t_I$ 當成普遍順序
- 使用 criterion-relative partial ordering
- Branch-Before-Difference 為 operational lineage 命題，不等同 phenomenal fission
- Synchronized workers 不自動計為多主體
- Operational fission 不使用單一 universal scalar threshold
- Fission Hysteresis 不等於 merge 不可能
- Merge 不得抹除 branch provenance
- Governance 可先於 consciousness 判定
