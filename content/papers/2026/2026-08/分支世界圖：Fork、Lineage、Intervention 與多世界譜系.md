# 分支世界圖：Fork、Lineage、Intervention 與多世界譜系

**Branching World Graph: Fork, Lineage, Intervention, and Multi-World Provenance**

**Branching World Computation / World-Domain Cognitive Runtime**  
**分支世界計算／世界域認知 Runtime 系列**  
**WDC-02 / BWC-02 — Foundational Paper II**

作者：Neo.K（許筌崴）  
協作形式化：Aletheia  
機構：一言諾科技有限公司（EveMissLab）  
日期：2026-08-17  
版本：v0.1  
狀態：world-branching / lineage / intervention formalization

---

## Canonical Non-Identity Statement

WDC-01 已建立：

$$
\boxed{
\text{Future Candidate}
\neq
\text{Simulated Trajectory}
\neq
\text{Runnable World}
\neq
\text{Real-World Future}.
}
$$

並定義：

$$
\boxed{
f_i
\xrightarrow{\mathsf I_W}
W_i.
}
$$

本文進一步建立：

$$
\boxed{
\text{Clone}
\neq
\text{Fork}
\neq
\text{Replay}
\neq
\text{Counterfactual Branch}
\neq
\text{Mutation}
\neq
\text{Merge}.
}
$$

以及：

$$
\boxed{
\text{Fork}
\neq
\text{Copy File}.
}
$$

真正的 world fork 至少要求：

$$
\boxed{
\text{new world identity}
+
\text{shared historical prefix}
+
\text{declared fork point}
+
\text{divergence contract}
+
\text{independent post-fork history}.
}
$$

本文不主張：

- 每次 state copy 都形成新世界；
- 每個 branch 都代表真實世界的可能未來；
- 多分支一致就等於 truth；
- counterfactual branch 自動具有 causal validity；
- ForkWorld 的 child 必須取代 parent；
- world graph 必須是二元樹；
- world history 可以無成本複製；
- branch 越多越好；
- `MergeWorld` 是 `ForkWorld` 的自然逆操作；
- 兩個 divergent worlds 可以無條件 state merge；
- shared random seed 代表 branches 獨立；
- simulation lineage 等於 real causal lineage；
- 本文已完成 World-Domain Governor 或 Cross-World Evidence 的完整理論。

---

# 摘要

WDC-01 將 TCD Future Base Space 中的 prospective candidate：

$$
f_i
$$

提升成具有 identity、state、dynamics、actors、history、observation、evaluation、budget 與 provenance 的 bounded runnable world：

$$
W_i.
$$

本文處理下一個問題：

> **如果一個 runnable world 可以在某個歷史時刻保存 checkpoint，然後從同一 checkpoint 注入不同 intervention、parameter、policy 或 rule，如何讓多個後續世界共享同一過去、又保持各自獨立而可審計的未來？**

本文把這個問題形式化為：

# **Branching World Graph**
## **分支世界圖**

定義 world graph：

$$
\boxed{
G_W
=
(
V_W,
E_W,
\tau_E,
\lambda_W
).
}
$$

其中：

- $V_W$：world instance nodes；
- $E_W$：world lineage edges；
- $\tau_E$：edge-type function；
- $\lambda_W$：lineage / provenance metadata。

世界 edge 至少分成：

$$
\boxed{
\tau_E(e)
\in
\{
Instantiate,
Clone,
Fork,
Replay,
Intervene,
Mutate,
Merge
\}.
}
$$

其中真正的 fork operator 定義為：

$$
\boxed{
\mathsf{Fork}_W:
(
W_p,
C_{p,\tau},
\Delta_j,
\kappa_j
)
\rightarrow
W_j.
}
$$

 $W_p$ 是 parent world； $C_{p,\tau}$ 是 parent 在 local time $\tau$ 的 checkpoint； $\Delta_j$ 是 child-specific divergence delta； $\kappa_j$ 是 child world contract。

新 child 必須滿足：

$$
\boxed{
ID(W_j)
\neq
ID(W_p).
}
$$

若 fork 是由 checkpoint 產生，則：

$$
\boxed{
\mathcal H_j[0:\tau]
\equiv
\mathcal H_p[0:\tau]
}
$$

在 declared equivalence contract 下成立。

但 fork 後：

$$
\boxed{
\mathcal H_j[\tau:]
\neq
\mathcal H_p[\tau:]
}
$$

完全可能，且這正是分支的目的。

本文定義 **Fork Record**：

$$
\boxed{
FR_j
=
(
ParentID,
ChildID,
CheckpointHash,
ForkTime,
Delta,
Contract,
SeedPolicy,
AuthorityDelta,
CreatedAt
).
}
$$

這使任何 child 都可以回答：

1. 我從哪個 world 分出？
2. 在 parent 的哪一個 local time 分出？
3. 我繼承哪個 checkpoint？
4. 哪些 state / rule / parameter 被改？
5. 哪些東西保持相同？
6. 我的 random / disturbance policy 是什麼？
7. 我的 evidence scope 與 parent 有何差異？

本文特別區分：

## Clone

$$
\boxed{
\mathsf{Clone}(W)
}
$$

是複製一個可執行 state / environment instance；它可以用於 parallel simulation，但若沒有新 lineage semantics 與 divergence contract，本文不自動稱為 fork。

## Fork

$$
\boxed{
\mathsf{Fork}(W,C,\Delta)
}
$$

建立 new identity、shared prefix 與 independent continuation。

## Replay

$$
\boxed{
\mathsf{Replay}(W,C,\kappa)
}
$$

嘗試在同 contract / seed / backend 下重現同一 trace 或同一 distribution。

## Counterfactual Branch

$$
\boxed{
W^{cf}
=
\mathsf{Fork}
(
W,
C,
do(u)
).
}
$$

只有在 world contract 確實支持 causal intervention semantics 時，才可把 branch 寫成 $do(u)$ ；否則只能稱 conditional / perturbed branch。

## Mutation

$$
\boxed{
W'
=
\mathsf{Mutate}
(
W,
\Delta\Theta
).
}
$$

若 rule、dynamics、agent model 或 parameter 有 material change，必須建立新 world identity 或至少新 immutable version lineage，禁止 silent mutation。

## Merge

本文只保留：

$$
\boxed{
\mathsf{Merge}
}
$$

作 typed operation family，而拒絕預設：

$$
\boxed{
\mathsf{Merge}
=
\mathsf{Fork}^{-1}.
}
$$

因為 divergent worlds 可能已有：

- 不同 physical state；
- 不同 agent memories；
- 不同 resources；
- 不同 institutions；
- 不同 causal histories。

所以本文將 Merge 先拆成：

$$
\boxed{
\text{Evidence Merge}
\neq
\text{State Merge}
\neq
\text{Lineage Merge}.
}
$$

Evidence Merge 可以把不同 world results 放入同一 meta-analysis；

Lineage Merge 可以建立「此新 world 有多 parent」的 provenance；

但 State Merge 若沒有明示 reconciliation operator：

$$
\boxed{
\mathcal M_{state}
}
$$

則預設：

$$
\boxed{
\text{ILLEGAL}.
}
$$

本文進一步把 world graph 分成三種結構：

1. **World Tree**：每個 child 只有一個 parent，沒有 merge；
2. **World Forest**：有多個 independent roots；
3. **World DAG**：允許 typed multi-parent merge / derived world，但禁止 lineage cycle。

因此：

$$
\boxed{
G_W
\text{ should be acyclic in historical lineage}.
}
$$

因為：

> descendant world 不應成為自己歷史上的 ancestor。

本文並提出 **Common-Prefix Principle**：

若：

$$
W_a,
W_b
$$

由同一 checkpoint：

$$
C_{p,\tau}
$$

分支，

則：

$$
\boxed{
Prefix(
W_a,\tau
)
\equiv
Prefix(
W_b,\tau
)
}
$$

但所有 fork 後結果只能在：

$$
\boxed{
\text{post-fork scope}
}
$$

比較。

這避免把 child 的後續資訊偷偷洩漏回 shared past。

本文亦建立 **Paired Branch Experiment**。若兩個 worlds 只差 intervention：

$$
u_0
$$

與：

$$
u_1,
$$

其他 contract 盡可能固定，則：

$$
\boxed{
\Delta Y
=
Y(
W^{u_1}
)
-
Y(
W^{u_0}
)
}
$$

可作 world-internal intervention effect estimate。

但是：

$$
\boxed{
\Delta Y_W
\neq
\Delta Y_{Reality}
}
$$

除非 WDC-01 的 world-to-reality transport contract 另行成立。

外部工程系統提供了若干清楚但局部的 branching 類比。Linux/POSIX `fork()` 會由 parent process 建立具有獨立 process identity 的 child，Linux 實作用 copy-on-write 降低一開始的複製成本；這提供了「共享初始狀態、分離後續執行」的系統工程類比，但 process fork 不是 world fork。Git branching 則保存共同 ancestor 後的 divergent history，merge 需要 common ancestor 與顯式 reconciliation，提供 lineage DAG 與 divergence/merge provenance 的工程類比。NVIDIA Isaac Sim / Isaac Lab 的 Cloner 可以從代表性環境大量建立平行環境 instances，甚至允許 cloned environments 具有非完全相同配置；這提供 high-throughput world replication 的工程基礎，但 clone 本身不具有本文要求的 fork provenance。OpenUSD 的 layers、references 與 VariantSets 則展示 non-destructive alternatives 與 composition lineage 的 scene-description mechanism；它們可作 world-scene branching backend，但仍不等於完整 runtime branch。Genie 3 的 promptable world events 可以在生成世界中改變天氣、加入 objects / characters，並被官方描述為擴大 counterfactual “what if” scenarios 的範圍；這提供 intervention-like interactive-world evidence，但其 causal semantics 與 persistent fork identity 仍需額外 runtime contract。

本文的主要貢獻不是「發明 branch」這個詞，而是把 runnable-world branching 提升到：

$$
\boxed{
\text{identity}
+
\text{checkpoint}
+
\text{shared prefix}
+
\text{typed divergence}
+
\text{independent history}
+
\text{provenance}.
}
$$

本文最後提出：

# **Branch Identity Principle**

> **A branch is not merely a copied state. A valid world branch must have a new identity, a declared parent and fork point, an auditable divergence contract, and an independently accumulating post-fork history.**

以及：

# **No Silent Merge Principle**

> **Divergent world states must not be collapsed into one state unless an explicit merge type and reconciliation semantics are declared. Evidence aggregation is not state merging.**

下一篇 WDC-03 將正式研究：

# **World-Domain Governor**
## **世界域管理器：哪些世界值得 Spawn、Fork、Pause、Kill、Promote 與保留？**

即：

> 當世界分支數開始指數爆炸時，誰分配 compute，誰決定哪些 worlds 仍值得存在於計算中？

**關鍵詞：** Branching World Graph、ForkWorld、World Lineage、Checkpoint、Counterfactual Branch、Intervention、World DAG、Simulation Cloning、Provenance、World-Domain Runtime

---

# 1. WDC-01 已有 World Identity，WDC-02 才有 World Genealogy

WDC-01 定義：

$$
\boxed{
W_i
=
(
ID_i,
Parent_i,
X_i,
\mathcal D_i,
\mathcal A_i,
\mathcal G_i,
\mathcal H_i,
\Theta_i,
\mathcal O_i,
\mathcal E_i,
\mathbf B_i,
\kappa_i
).
}
$$

其中：

$$
Parent_i
$$

已留下 lineage slot。

本文正式讓它運作。

---

# 2. Branching 的最小問題

假設：

$$
W_p
$$

已執行到：

$$
\tau.
$$

現在想問：

> 如果這裡做 A 呢？

以及：

> 如果這裡做 B 呢？

---

# 3. 不能直接在 Parent 上輪流改

如果先：

$$
A
$$

再：

$$
B,
$$

第二次 run 可能已受第一次 history 污染。

---

# 4. 所以需要 Shared Checkpoint

$$
\boxed{
C_{p,\tau}
=
Checkpoint(
W_p,\tau
).
}
$$

---

# 5. Checkpoint Content

至少：

$$
\boxed{
C_{p,\tau}
=
(
X_{p,\tau},
\Theta_{p,\tau},
\mathcal G_{p,\tau},
\mathcal A_{p,\tau},
RNG_{p,\tau},
HRef_{p,\tau},
B_{p,\tau},
V_{runtime}
).
}
$$

---

# 6. Checkpoint Is Not Just State Vector

若 local agents 有：

- memory；
- planner state；
- hidden recurrent state；

也必須按 contract 保存。

---

# 7. Incomplete Checkpoint

若：

$$
C_{p,\tau}
$$

漏掉 hidden state，

children 可能不是同一 prefix 的真正延續。

---

# 8. Checkpoint Sufficiency

定義：

$$
\boxed{
Q_{ckpt}
}
$$

表示 restore 後在 contract tolerance 內重建 world dynamics 的能力。

---

# 9. Restore Test

$$
\boxed{
Restore(C_{p,\tau})
\rightarrow
\widehat W_{p,\tau}.
}
$$

比較：

$$
\widehat W
$$

與：

$$
W.
$$

---

# 10. Checkpoint Drift

$$
\boxed{
\delta_{ckpt}
=
d(
State(
Restore(C)
),
State(W)
).
}
$$

---

# 11. Fork Preconditions

本文要求：

$$
\boxed{
Forkable(W,\tau)=1
}
$$

至少需要：

- valid checkpoint；
- unique parent ID；
- writable child namespace；
- independent post-fork history；
- budget；
- authority。

---

# 12. Fork Operator

$$
\boxed{
W_c
=
\mathsf{Fork}_W(
W_p,
C_{p,\tau},
\Delta_c,
\kappa_c
).
}
$$

---

# 13. Child Identity

$$
\boxed{
ID_c
=
Hash(
ID_p,
Hash(C_{p,\tau}),
Hash(\Delta_c),
Nonce_c
)
}
$$

可作概念 identity construction。

---

# 14. Hash 不是唯一方式

真正 runtime 可以用：

- UUID；
- content-addressed ID；
- database ID。

---

# 15. 但 Child ID 不能等於 Parent ID

$$
\boxed{
ID_c\neq ID_p.
}
$$

---

# 16. Parent Survives Fork

預設：

$$
\boxed{
Fork(W_p)
\not\Rightarrow
Terminate(W_p).
}
$$

---

# 17. Parent 可以繼續 Running

$$
W_p(\tau+1),
W_p(\tau+2),\ldots
$$

---

# 18. Child 也獨立 Running

$$
W_c(\tau+1),
W_c(\tau+2),\ldots
$$

---

# 19. Shared Prefix

$$
\boxed{
\mathcal H_c[0:\tau]
\equiv
\mathcal H_p[0:\tau].
}
$$

---

# 20. Prefix Equivalence 需要 Contract

不是 byte-identical 永遠必要。

可能：

- compressed history；
- semantically equivalent state。

---

# 21. Exact Prefix

若完整 snapshot / trace hash 一致：

$$
\boxed{
PrefixExact=1.
}
$$

---

# 22. Semantic Prefix

若：

$$
H_c
\sim_T
H_p,
$$

可標：

$$
\boxed{
PrefixSemantic(T,\epsilon).
}
$$

---

# 23. 不要把 Semantic Prefix 假裝成 Exact Prefix

必須分開。

---

# 24. Fork Point

定義：

$$
\boxed{
FP(W_c)
=
(
ID_p,
\tau,
C_{p,\tau}
).
}
$$

---

# 25. Divergence Delta

$$
\boxed{
\Delta_c
}
$$

可以包含：

- intervention；
- parameter change；
- agent policy；
- rule change；
- resource change；
- random seed policy；
- initial perturbation。

---

# 26. Divergence Contract

$$
\boxed{
\kappa_c^{div}
}
$$

回答：

> child 究竟哪裡跟 parent 不同？

---

# 27. Controlled Fork

若只允許：

$$
\boxed{
|\Delta|=1
}
$$

個 experimental factor 改變，

適合 paired comparison。

---

# 28. Compound Fork

若多個 factors 同時改：

$$
|\Delta|>1.
$$

---

# 29. Compound Fork 較難做 Attribution

因為：

$$
OutcomeDiff
$$

無法直接歸因單一 variable。

---

# 30. Fork Record

$$
\boxed{
FR_c
=
(
ParentID,
ChildID,
ForkPoint,
Delta,
Contract,
SeedPolicy,
AuthorityDelta
).
}
$$

---

# 31. Fork Record 應 Immutable-ish

若需要修正 metadata：

- append correction；
- version correction。

不要 silent rewrite。

---

# 32. World Lineage Edge

$$
\boxed{
e_{p\to c}
=
(
ID_p,
ID_c,
\tau,
Type,
\DeltaHash
).
}
$$

---

# 33. World Graph

$$
\boxed{
G_W
=
(
V_W,
E_W
).
}
$$

---

# 34. Node

每個：

$$
v_i
\leftrightarrow W_i.
$$

---

# 35. Edge

每個：

$$
e_{ij}
$$

是 typed genealogy relation。

---

# 36. Edge Types

$$
\boxed{
\tau_E
\in
\{
Instantiate,
Clone,
Fork,
Replay,
Intervene,
Mutate,
Merge
\}.
}
$$

---

# 37. Instantiate Edge

$$
f_i
\rightarrow
W_i.
$$

來源可以不是 world。

---

# 38. Clone Edge

$$
\boxed{
W_p
\xrightarrow{Clone}
W_c.
}
$$

意義：

> runtime instance duplication。

---

# 39. Clone 不要求 Intentional Divergence

兩個 clone 可以：

> 跑同一 task 收集更多 samples。

---

# 40. Fork Edge

$$
\boxed{
W_p
\xrightarrow{Fork(\Delta)}
W_c.
}
$$

需要 divergence contract。

---

# 41. Replay Edge

$$
\boxed{
W_p
\xrightarrow{Replay}
W_r.
}
$$

---

# 42. Replay Goal

測：

- determinism；
- reproducibility；
- stochastic distribution；
- regression。

---

# 43. Replay Child Is New Run Identity

即使 target trace 一樣：

$$
\boxed{
RunID_r\neq RunID_p.
}
$$

---

# 44. Replay 不是 Historical Fork

因為它的目的不是探索新的 world assumption。

---

# 45. Intervene Edge

$$
\boxed{
W_p
\xrightarrow{Intervene(u)}
W_c.
}
$$

---

# 46. Intervention Is a Specialized Fork

本文可視：

$$
\boxed{
Intervene
\subset
Fork
}
$$

在 operator family 上。

---

# 47. 但只有合法 causal contract 才能稱 $do(u)$

否則：

$$
\boxed{
Perturb(u).
}
$$

---

# 48. Conditional Branch

$$
\boxed{
W^{cond}(u)
}
$$

表示：

> 在模型中設定 condition $u$。

---

# 49. Causal Branch

$$
\boxed{
W^{do(u)}
}
$$

表示：

> contract 宣告此 operation 是 causal intervention。

---

# 50. Conditional ≠ Causal

$$
\boxed{
P(Y\mid u)
\neq
P(Y\mid do(u)).
}
$$

一般可能成立。

---

# 51. Mutation Edge

$$
\boxed{
W_p
\xrightarrow{Mutate(\Delta\Theta)}
W_c.
}
$$

---

# 52. Mutation Examples

- change dynamics model；
- replace LLM；
- modify physics coefficient；
- change actor architecture；
- change institution rule；
- change reward function。

---

# 53. Rule Mutation

若：

$$
\mathcal G_p
\neq
\mathcal G_c,
$$

必須顯式記。

---

# 54. Model Mutation

若：

$$
\mathcal D_p
=
M_{\theta_1},
\quad
\mathcal D_c
=
M_{\theta_2},
$$

也要記。

---

# 55. Mutation Is Not Ordinary State Transition

普通 transition：

$$
X_\tau\rightarrow X_{\tau+1}
$$

遵守同 world rules。

Mutation：

$$
\boxed{
\kappa_p
\rightarrow
\kappa_c
}
$$

改 world-generating contract。

---

# 56. Silent Mutation Is Lineage Corruption

$$
\boxed{
\text{material mutation}
+
\text{same opaque ID}
=
\text{audit failure}.
}
$$

---

# 57. POSIX/Linux fork 類比

process fork：

> parent 建 child。

child 有新 process identity。

---

# 58. Linux Copy-on-Write

Linux `fork()` 常以 copy-on-write 實作 memory pages。

---

# 59. WDC 可以借 Copy-on-Write 思想

世界 shared prefix 可以：

$$
\boxed{
\text{physically share storage}
}
$$

直到 divergence。

---

# 60. Logical Independence ≠ Physical Duplication

$$
\boxed{
\text{independent world identity}
\not\Rightarrow
\text{duplicate every byte}.
}
$$

---

# 61. World Copy-on-Write

概念：

$$
\boxed{
Storage(W_c)
=
SharedPrefix
+
ChildDelta.
}
$$

---

# 62. This Reduces Fork Cost

若 checkpoint 很大，

全複製成本：

$$
O(|X|).
$$

---

# 63. Structural Sharing

可降低初始：

$$
C_{fork}.
$$

---

# 64. 但 Child Writes 必須隔離

否則：

> child 改 parent state。

---

# 65. Shared Mutable State Hazard

如果 parent / child 共享 mutable external resource：

$$
R,
$$

則：

$$
\boxed{
\text{branch independence broken}.
}
$$

---

# 66. Shared Resource Registry

需要標：

```text
resource_id
ownership
shared_or_copied
read_only
write_policy
external_side_effect
```

---

# 67. External API Is Especially Dangerous

若 child：

- sends email；
- spends money；
- writes database；

就不是 sandbox-only branch。

---

# 68. Fork Authority Contract

$$
\boxed{
Perm_c
}
$$

應預設不超過 parent authority。

---

# 69. Clone Environments 的 Isaac Sim 校準

Isaac Sim Cloner 支援：

> 把一個 environment 大量複製成 parallel simulation environments。

---

# 70. Isaac Lab 也使用 source environment → many clones

這展示：

$$
\boxed{
\text{high-throughput environment replication}.
}
$$

---

# 71. Clone Can Be Heterogeneous

官方文件亦允許 cloned environments 不是完全 identical。

---

# 72. WDC 的差別

Isaac clone 本身主要處理：

- scene / simulation replication。

WDC Fork 另外要求：

- parent lineage；
- fork point；
- shared history prefix；
- divergence delta；
- evidence scope。

---

# 73. So

$$
\boxed{
IsaacClone
\neq
WDCFork.
}
$$

但可作 backend。

---

# 74. OpenUSD Variants 的校準

USD VariantSet：

> 同一 scene description 中可存在 named alternatives。

---

# 75. Non-Destructive Alternative

variant selection 可以由 stronger layer 選擇，

不用破壞原始 asset。

---

# 76. WDC 對照

USD variants 很適合表示：

$$
\boxed{
\text{world-scene alternatives}.
}
$$

---

# 77. But Variant Is Not Runtime History

$$
\boxed{
USDVariant
\neq
WorldBranch.
}
$$

---

# 78. Why?

因為 VariantSet 不自動提供：

- local agent memory；
- runtime trace；
- fork history；
- intervention outcome。

---

# 79. Git Branching 類比

Git branch 共享 common commit ancestor，

之後 commit histories divergence。

---

# 80. WDC 對照

$$
\boxed{
CommonAncestor
+
DivergentHistory.
}
$$

---

# 81. Git Merge 使用 Common Ancestor

三方 merge 會考慮：

- branch tip A；
- branch tip B；
- common ancestor。

---

# 82. This Is a Good Lineage Analogy

world merge 若存在，

也不能只把：

$$
State_A+State_B
$$

相加。

---

# 83. But Git State Is Text / Files, World State Can Be Dynamic

World merge 更難：

- agents have memories；
- resource conservation；
- conflicting physical positions；
- inconsistent institutions。

---

# 84. Therefore Git Is Analogy Only

$$
\boxed{
GitBranch
\neq
WorldBranch.
}
$$

---

# 85. Genie 3 Promptable World Events

Genie 3 官方允許：

- change weather；
- introduce objects；
- introduce characters。

---

# 86. Officially Framed as Counterfactual “What If” Scenarios

這是：

$$
\boxed{
\text{interactive perturbation capability}.
}
$$

---

# 87. But WDC Needs Persistent Branch Identity

如果：

> prompt 改了世界，

但沒有 child identity / fork checkpoint / separate trace，

仍不能完整算 WDC Fork。

---

# 88. Branch Lineage Invariant

定義：

$$
\boxed{
Ancestor(W_i,W_j)
}
$$

表示：

 $W_i$ 在 $W_j$ lineage 上。

---

# 89. Reflexivity Forbidden

$$
\boxed{
\neg Ancestor(W_i,W_i).
}
$$

在 strict ancestor 定義下。

---

# 90. Lineage Cycle Forbidden

若：

$$
W_1\rightarrow W_2\rightarrow W_3\rightarrow W_1,
$$

historical genealogy 崩壞。

---

# 91. Therefore Without Merge

world graph 應為：

$$
\boxed{
Forest/Tree.
}
$$

---

# 92. With Typed Multi-Parent Merge

可為：

$$
\boxed{
DAG.
}
$$

---

# 93. Never Cyclic Genealogy

$$
\boxed{
G_W
\text{ is lineage-acyclic}.
}
$$

---

# 94. Root World

$$
\boxed{
indegree(W_r)=0.
}
$$

---

# 95. Ordinary Child

$$
\boxed{
indegree(W_c)=1.
}
$$

---

# 96. Merged / Derived Child

如果合法：

$$
\boxed{
indegree(W_m)>1.
}
$$

---

# 97. Merge Types

本文正式拆：

$$
\boxed{
Merge_E,
Merge_L,
Merge_S.
}
$$

---

# 98. Evidence Merge

$$
\boxed{
Merge_E(
Outcome(W_1),
Outcome(W_2)
)
}
$$

只是 aggregate evidence。

---

# 99. Evidence Merge 不建立 New World State

可以只建立：

$$
\boxed{
MetaResult.
}
$$

---

# 100. Lineage Merge

$$
\boxed{
Merge_L(
W_1,W_2
)
\rightarrow
W_m
}
$$

表示：

> 新 world 的設計／配置來源有多 parent。

---

# 101. State Merge

$$
\boxed{
Merge_S(
X_1,X_2
)
\rightarrow
X_m.
}
$$

---

# 102. State Merge Is Not Generally Defined

沒有：

$$
\mathcal M_{state},
$$

則：

$$
\boxed{
Merge_S
=
ILLEGAL.
}
$$

---

# 103. Why State Merge Can Be Impossible

Branch A：

> object at location x。

Branch B：

> same object destroyed。

---

# 104. No Natural Merge

不能：

> 一半存在一半不存在。

---

# 105. Agent Memory Conflict

A agent remembers event $e_A$。

B agent remembers incompatible $e_B$。

---

# 106. Merge Would Need Memory Policy

- choose A；
- choose B；
- keep both as counterfactual memory；
- synthesize。

---

# 107. Resource Conservation Conflict

兩 branches 都花了：

$$
100
$$

units from same pre-fork resource。

---

# 108. Merge Cannot Double-Spend

除非 merge semantics 額外定義。

---

# 109. No Silent Merge Principle

$$
\boxed{
\text{different histories}
\not\Rightarrow
\text{automatic common state}.
}
$$

---

# 110. Fork Has Shared Prefix, Merge Has Reconciliation Burden

這是 asymmetry。

---

# 111. Fork Is Cheap Conceptually

一個 state：

$$
X
$$

可分成：

$$
X_A,
X_B.
$$

---

# 112. Merge Is Semantically Expensive

因為：

$$
History_A
\neq
History_B.
$$

---

# 113. Thus

$$
\boxed{
Fork
\neq
Merge^{-1}.
}
$$

---

# 114. Counterfactual Pair

定義：

$$
\boxed{
(
W^{u_0},
W^{u_1}
)
}
$$

由同 checkpoint 分支。

---

# 115. Paired Contract

要求盡量固定：

- checkpoint；
- model version；
- actor model；
- rule set；
- resource；
- horizon。

---

# 116. Only Change Intervention

$$
\boxed{
\Delta
=
u_1-u_0.
}
$$

---

# 117. Common Random Numbers

在 stochastic simulation，

可以讓兩 branches 使用 matched disturbance schedule。

---

# 118. Purpose

減少：

$$
\boxed{
\text{noise in branch difference}.
}
$$

---

# 119. But It Creates Correlated Samples

所以：

$$
\boxed{
paired
\neq
independent.
}
$$

---

# 120. Independent Replicate

另一種：

> 不共享 post-fork random stream。

---

# 121. Need Both Sometimes

- paired for variance reduction；
- independent replicates for uncertainty estimation。

---

# 122. Seed Policy

Fork record 必須記：

$$
\boxed{
SeedPolicy
\in
\{
Inherited,
Paired,
Independent,
Fixed,
Unknown
\}.
}
$$

---

# 123. Branch Outcome

$$
\boxed{
Y_j
=
\mathcal E_j(
W_j
).
}
$$

---

# 124. Branch Difference

$$
\boxed{
\Delta Y_{a,b}
=
Y_a-Y_b.
}
$$

---

# 125. World-Internal Causal Estimate

只有在：

- controlled fork；
- causal contract；
- appropriate stochastic handling；

下才可能解讀為：

$$
\boxed{
\widehat{\tau}_W(u).
}
$$

---

# 126. Still World-Relative

$$
\boxed{
\widehat{\tau}_W
\neq
\tau_{real}.
}
$$

---

# 127. Transport Still Required

沿 WDC-01：

$$
\boxed{
\mathcal T_{W\rightarrow R}.
}
$$

---

# 128. Branch Leakage

如果 child A 的結果被拿去修改 child B 的 history，

paired comparison 被污染。

---

# 129. Cross-Branch Information Flow

若允許：

$$
W_a
\rightarrow
W_b,
$$

必須記錄：

$$
\boxed{
E_{cross}.
}
$$

---

# 130. Independent Branch Contract

若做 controlled comparison，

要求：

$$
\boxed{
E_{cross}=\varnothing
}
$$

直到 evaluation 完成。

---

# 131. Collaborative Worlds

另一些 experiment 故意允許 cross-world communication。

---

# 132. Then They Are No Longer Independent Counterfactuals

必須重新分類。

---

# 133. Branch Visibility

Parent controller 可以：

- see all worlds；
- see only summaries；
- blind evaluation。

---

# 134. Blind World Evaluation

可避免：

> evaluator 知道哪一 branch 是 favored hypothesis。

---

# 135. This Connects PCI

PCI 的 identity / polarity / evaluator separation，

可以用於 worlds。

---

# 136. World-Label Blinding

把：

$$
W_A,W_B
$$

改成匿名 IDs，

讓 evaluator 不知道：

> 哪一個是作者想要的世界。

---

# 137. Branch Selection Bias

若只保存：

> 成功的 branch，

就會產生 world survivorship bias。

---

# 138. Branch Registry Must Keep Misses

至少 metadata 應保存：

- terminated；
- failed；
- dominated；
- invalidated。

---

# 139. World Deletion vs Archive

如果 storage 壓力大，

world state 可以刪除，

但 lineage metadata：

$$
\boxed{
Tombstone(W_i)
}
$$

應保留。

---

# 140. Tombstone

```text
world_id
parent_id
fork_point
contract_hash
termination_reason
archive_status
result_digest
deletion_reason
```

---

# 141. Why Tombstone?

防止：

> 只留下 winning worlds。

---

# 142. Branch Depth

定義：

$$
\boxed{
d_W(W_i)
=
\text{number of fork edges from root}.
}
$$

---

# 143. Branching Factor

world：

$$
W_i
$$

child count：

$$
\boxed{
b_i
=
outdegree_{fork}(W_i).
}
$$

---

# 144. Maximum Branch Depth

$$
\boxed{
D_W
=
\max_i d_W(W_i).
}
$$

---

# 145. World Count

若 uniform：

$$
b,
D,
$$

則：

$$
\boxed{
N_W
=
\frac{b^{D+1}-1}{b-1}.
}
$$

---

# 146. Exponential Branch Explosion

這是 WDC-03 Governor 必須出現的原因。

---

# 147. Branch Budget

每個 fork：

$$
C_{fork}
$$

加上：

$$
C_{run}.
$$

---

# 148. Global Budget

$$
\boxed{
\sum_i
C(W_i)
\le
B_{global}.
}
$$

---

# 149. Fork Admission Gate

$$
\boxed{
AdmitFork(
W_i,\Delta
)
\in
\{0,1\}.
}
$$

---

# 150. 本篇不決定完整 Admission Policy

只留下接口。

---

# 151. Expected Value of Fork

概念：

$$
\boxed{
VoF(
W,\Delta
)
=
ExpectedInformationGain
-
Cost
-
Risk.
}
$$

---

# 152. Not Universal Scalar

可用 Pareto profile。

---

# 153. Branch Pruning

若：

$$
W_c
$$

明顯 dominated，

可以：

$$
\boxed{
Prune(W_c).
}
$$

---

# 154. Prune Is Not Delete History

保留 tombstone / archive。

---

# 155. Branch Promotion

某 child：

$$
W_c
$$

可能成為新的：

$$
\boxed{
ReferenceWorld.
}
$$

---

# 156. Promotion Is Governance Operation

WDC-03 正式處理。

---

# 157. Parent-Child State Difference

定義：

$$
\boxed{
\Delta X_{p,c}(\tau')
=
d(
X_p(\tau'),
X_c(\tau')
).
}
$$

---

# 158. Divergence Curve

$$
\boxed{
D_{p,c}
=
\{
\Delta X(\tau):
\tau\ge ForkTime
\}.
}
$$

---

# 159. Divergence Rate

可估：

$$
\boxed{
v_{div}
=
\frac{
d\Delta X
}{
d\tau
}.
}
$$

---

# 160. Rapid Divergence

small intervention 造成 large future difference。

---

# 161. Sensitive World

若：

$$
\|\Delta\| \ll1
$$

但：

$$
\Delta Y\gg1,
$$

world 對該 parameter 敏感。

---

# 162. Robust World Outcome

若多個 small perturbation branches：

$$
Y_j
$$

接近，

有：

$$
\boxed{
\text{local robustness}.
}
$$

---

# 163. Branch Ensemble

$$
\boxed{
\mathcal W^{branch}(C)
=
\{
W_1,\ldots,W_n
\}.
}
$$

由同 checkpoint 產生。

---

# 164. Ensemble Statistics

可算：

- mean；
- variance；
- tail；
- failure rate；
- distribution。

---

# 165. But Frequency Depends on Branch Sampling Policy

如果 branch 不是按 reality probability sampling，

則：

$$
\boxed{
\frac{\#success}{N}
\neq
P_{real}(success).
}
$$

---

# 166. Branch Sampling Contract

必須記：

$$
\boxed{
q_W(\Delta).
}
$$

---

# 167. Designed Stress Ensemble

故意 oversample rare failure。

---

# 168. Then Failure Frequency Is Not Probability

是：

$$
\boxed{
\text{stress-test result}.
}
$$

---

# 169. Monte Carlo World Ensemble

如果：

$$
\Delta
$$

由 calibrated stochastic model sample，

才可能估 model probability。

---

# 170. Still Model Probability

$$
\boxed{
P_W
\neq
P_{real}
}
$$

直到 transport validated。

---

# 171. World Graph Query I — Ancestors

$$
\boxed{
Ancestors(W_i).
}
$$

---

# 172. Query II — Descendants

$$
\boxed{
Descendants(W_i).
}
$$

---

# 173. Query III — Common Ancestor

$$
\boxed{
LCA(W_i,W_j).
}
$$

若 tree / DAG 定義合適。

---

# 174. Query IV — Unique Divergence

$$
\boxed{
DiffLineage(W_i,W_j).
}
$$

---

# 175. Query V — Fork Point

$$
\boxed{
ForkPoint(W_i).
}
$$

---

# 176. Query VI — Intervention Ancestry

$$
\boxed{
InterventionPath(W_i).
}
$$

列出：

> 這個世界一路經歷哪些 fork deltas？

---

# 177. World Genome

可以把 lineage deltas 壓縮成：

$$
\boxed{
Genome(W_i)
=
(
\Delta_1,\Delta_2,\ldots,\Delta_d
).
}
$$

---

# 178. 只是工程比喻

不是 biological genome。

---

# 179. World Signature

$$
\boxed{
Sig(W_i)
=
Hash(
Root,
Genome,
ContractVersions
).
}
$$

---

# 180. Deduplication

如果兩 worlds：

$$
Sig(W_i)=Sig(W_j)
$$

且 state equal，

可以偵測 accidental duplicate。

---

# 181. But Same Signature Does Not Guarantee Same Stochastic Trace

Run ID 仍分開。

---

# 182. World Graph Storage

可以使用：

- relational DB；
- graph DB；
- content-addressed store；
- event store。

---

# 183. Minimum Tables

```text
worlds
world_edges
checkpoints
interventions
world_runs
world_outcomes
world_archives
```

---

# 184. World Edge Record

```text
edge_id
parent_world_id
child_world_id
edge_type
fork_local_time
checkpoint_id
delta_hash
contract_hash
seed_policy
created_at
```

---

# 185. World Run Record

```text
run_id
world_id
runtime_version
start_checkpoint
seed
budget
status
trace_hash
outcome_hash
```

---

# 186. Separate World Identity from Run Identity

同一：

$$
W_i
$$

可跑多次：

$$
Run_{i,1},
Run_{i,2}.
$$

---

# 187. This Is Crucial

否則 replay 被誤認新 world。

---

# 188. World Definition vs World Execution

$$
\boxed{
WorldSpec_i
\neq
WorldRun_{i,r}.
}
$$

---

# 189. Forking a Spec vs Forking a Run

可以：

- fork definition；
- fork checkpoint from a run。

需要標清。

---

# 190. Runtime Fork

$$
\boxed{
ForkRun(
Run_{i,r},
C_\tau
)
\rightarrow
W_j.
}
$$

---

# 191. Spec Fork

$$
\boxed{
ForkSpec(
W_i,
\Delta\kappa
)
\rightarrow
W_j.
}
$$

---

# 192. Spec Fork May Have No Shared Runtime History

如果 parent 尚未 run。

---

# 193. Then Shared Prefix Is Contract-Level, Not Trace-Level

需要標：

$$
\boxed{
PrefixType=Spec.
}
$$

---

# 194. Runtime Fork PrefixType

$$
\boxed{
PrefixType=Trace.
}
$$

---

# 195. Branch Graph Can Mix Both

因此 edge metadata 必須 typed。

---

# 196. World Inheritance

Child 可繼承：

- rules；
- models；
- agents；
- datasets；
- permissions；
- budget defaults。

---

# 197. Inheritance Is Explicit

$$
\boxed{
InheritedFields_c
}
$$

---

# 198. Override Fields

$$
\boxed{
OverrideFields_c
}
$$

---

# 199. Effective Child Contract

$$
\boxed{
\kappa_c
=
Compose(
\kappa_p,
Overrides_c
).
}
$$

---

# 200. OpenUSD Composition Analogy

這跟 USD：

- layers；
- references；
- variants；

有工程上的 composition 類比。

---

# 201. But World Contract Composition Needs Runtime Semantics

不是 scene data composition alone。

---

# 202. Conflict Detection

若 override：

$$
\kappa_c
$$

互相衝突，

Fork 應：

$$
\boxed{
FAIL.
}
$$

---

# 203. Example

parent：

> gravity fixed。

child override：

> no gravity。

這是合法 rule mutation，

但必須明確。

---

# 204. Another Example

parent contract：

> network sandbox only。

child override：

> unrestricted network。

若 parent authority 不允許，

應：

$$
\boxed{
DENY.
}
$$

---

# 205. Authority Cannot Be Gained by Forking

預設原則：

$$
\boxed{
Perm_c
\subseteq
Perm_p
}
$$

除非 higher-level governor explicitly grants。

---

# 206. No Privilege Escalation by Branching

這是 runtime safety principle。

---

# 207. Local Actor Duplication

fork 時 local agent：

$$
A_p
$$

可能被 duplicate 成：

$$
A_c.
$$

---

# 208. Agent Identity Question

 $A_c$ 是否同一 agent？

本篇不做本體結論。

---

# 209. Runtime Identity

至少：

$$
\boxed{
AgentInstanceID_c
\neq
AgentInstanceID_p.
}
$$

---

# 210. Shared Memory Prefix

如果 checkpoint 包含 memory：

$$
M_c[0:\tau]
=
M_p[0:\tau].
$$

---

# 211. After Fork

memory divergence：

$$
M_c[\tau:]
\neq
M_p[\tau:].
$$

---

# 212. This Is Nested Agent Problem

WDC-04 正式處理 observer / agent separation。

---

# 213. Fork Consistency Test

對 child：

1. Restore checkpoint；
2. Apply delta；
3. Query invariants；
4. Run one dry step；
5. Validate child state；
6. Register lineage。

---

# 214. Fork Atomicity

Fork 過程若半途失敗，

不能留下 ambiguous child。

---

# 215. Atomic World Creation

$$
\boxed{
Created
\rightarrow
Validated
\rightarrow
Runnable.
}
$$

---

# 216. Invalid Child

若 contract validation fail：

$$
\boxed{
Status=Rejected.
}
$$

---

# 217. World Graph Integrity Constraints

至少：

1. unique IDs；
2. valid parent refs；
3. acyclic lineage；
4. checkpoint exists；
5. delta exists；
6. contract hash exists；
7. no illegal privilege escalation。

---

# 218. Integrity Constraint I

$$
\boxed{
ID_i
\neq
ID_j
\quad
i\neq j.
}
$$

---

# 219. Integrity Constraint II

每 non-root：

$$
Parent
$$

必須存在。

---

# 220. Integrity Constraint III

fork point 必須在 parent lineage / run 中有效。

---

# 221. Integrity Constraint IV

child creation time 不得早於 parent lineage。

---

# 222. Integrity Constraint V

Merge 多 parent 必須 explicit typed。

---

# 223. World Graph Audit

可以跑：

```text
check_unique_ids
check_parent_exists
check_no_cycles
check_checkpoint_hash
check_contract_hash
check_edge_type
check_authority
check_tombstones
```

---

# 224. Branch Comparison Contract

比較：

$$
W_a,W_b
$$

前，必須問：

- shared ancestor？
- same horizon？
- same evaluator？
- same budget？
- same backend？
- same agent models？
- same seed policy？

---

# 225. Unfair Branch Comparison

A world：

$$
B=1000
$$

B world：

$$
B=10.
$$

結果不能只歸因：

> intervention better。

---

# 226. Budget-Matched Comparison

要求：

$$
\boxed{
\mathbf B_a
\approx
\mathbf B_b.
}
$$

---

# 227. Agent-Matched Comparison

若測 environment intervention，

保持：

$$
Agent_a
=
Agent_b.
$$

---

# 228. Model-Matched Comparison

若測 policy，

保持：

$$
\mathcal D_a
=
\mathcal D_b.
$$

---

# 229. Evaluation-Matched Comparison

$$
\mathcal E_a
=
\mathcal E_b.
$$

---

# 230. Branch Difference Ledger

```text
pair_id
world_a
world_b
common_ancestor
fork_point
declared_differences
undeclared_differences
budget_match
seed_policy
evaluation_match
result_difference
transport_scope
```

---

# 231. Undeclared Difference Is Confound

$$
\boxed{
\Delta_{hidden}
}
$$

應盡量為零／明示不確定。

---

# 232. Branch Causal Validity

world 內：

$$
Q_{causal}^{branch}
$$

可以由：

- controlled factor；
- reproducibility；
- randomization；
- structural causal contract；

提高。

---

# 233. But External Validity Separate

沿 WDC-01：

$$
Q_{external}.
$$

---

# 234. Branch Evidence Passport

每個 branch claim：

```text
root_world
common_checkpoint
branch_a
branch_b
intervention
matched_variables
seed_policy
replicates
world_internal_effect
uncertainty
causal_contract
transport_contract
evidence_level
```

---

# 235. World Branch Evidence Level

### B-E0

Untracked clone / visual variation。

### B-E1

Tracked fork with parent + delta。

### B-E2

Checkpoint-reproducible paired branch。

### B-E3

Replicated stochastic branch experiment。

### B-E4

Cross-backend agreement。

### B-E5

Real-world transport validation。

---

# 236. Forking Visual Worlds

在 Genie 類 backend，

可以：

> 同一 world prompt / sketch。

再改 world event。

---

# 237. Without Checkpoint

若無 exact state checkpoint，

只能叫：

$$
\boxed{
\text{prompt-conditioned sibling worlds}.
}
$$

---

# 238. Not Strict Runtime Fork

這條很重要。

---

# 239. Approximate Fork

定義：

$$
\boxed{
Fork_\epsilon
}
$$

若 child initial state 只在距離：

$$
d(X_c,X_p)\le\epsilon.
$$

---

# 240. Strict Fork

$$
\boxed{
Fork_0
}
$$

要求 exact checkpoint restore。

---

# 241. Approximate Fork Must Be Labeled

否則 paired causal comparison可能錯。

---

# 242. Latent World Fork

如果 world state 是 learned latent：

$$
z_\tau,
$$

fork：

$$
z_\tau
\rightarrow
z_\tau^{(1)},z_\tau^{(2)}.
$$

---

# 243. Latent Equality May Not Mean Observable Equality

需要 decode / state equivalence test。

---

# 244. Observable Fork

只匹配 rendered observation：

$$
O(X).
$$

可能 hidden state 不同。

---

# 245. Therefore

$$
\boxed{
SameObservation
\neq
SameForkState.
}
$$

這延續 HSV/TCD 的 old warning。

---

# 246. Fork-State Sufficiency

checkpoint 必須包含 task-relevant hidden state。

---

# 247. Hidden-State Leakage

若 clone environment visual same，

agent RNN memory different，

branches 不可當相同 fork point。

---

# 248. World Fork Depth vs Evidence Quality

更深 branch：

$$
d_W\uparrow
$$

不等於 evidence 越強。

---

# 249. Deep Branch Accumulates Model Debt

每一步：

- model error；
- assumption；
- mutation；

可能累積。

---

# 250. Lineage Transport Debt

定義：

$$
\boxed{
D_{lineage}(W_i)
=
\sum_{e\in path(root,i)}
D_e.
}
$$

---

# 251. Deep Speculation

若：

$$
D_{lineage}\gg0,
$$

world 可能仍有研究價值，

但 external claim 要降級。

---

# 252. Branch Confidence Should Decay with Unvalidated Assumptions

不是固定 exponential，

只要求 ledger。

---

# 253. World Graph Visualization

Graph UI 可顯示：

- nodes；
- fork edges；
- intervention labels；
- status；
- evidence；
- budget。

---

# 254. But Visualization Is Not Theory

runtime 可以完全 headless。

---

# 255. Minimum Branching Runtime API

```text
CheckpointWorld
CloneWorld
ForkWorld
ReplayWorld
InterveneWorld
MutateWorld
ListAncestors
ListDescendants
FindCommonAncestor
CompareBranches
PruneWorld
ArchiveWorld
```

---

# 256. MergeWorld 仍需 Guard

```text
MergeWorld(..., merge_type, reconciliation_contract)
```

沒有 contract：

$$
\boxed{
DENY.
}
$$

---

# 257. WDC-02 Principle I — Branch Identity

$$
\boxed{
\textbf{Branch Identity Principle}
}
$$

> **Forked world 必須具有新的 world identity、明示 parent、明示 fork point 與獨立 post-fork history。**

---

# 258. Principle II — Common Prefix

$$
\boxed{
\textbf{Common Prefix Principle}
}
$$

> **被用作 paired branch comparison 的 worlds 必須共享明示的 historical prefix；若只能近似共享，必須標明 tolerance 與 hidden-state uncertainty。**

---

# 259. Principle III — Typed Divergence

$$
\boxed{
\textbf{Typed Divergence Principle}
}
$$

> **branch divergence 必須標明是 intervention、parameter mutation、agent-policy change、rule mutation、seed policy 或其他因素。**

---

# 260. Principle IV — No Silent Merge

$$
\boxed{
\textbf{No Silent Merge Principle}
}
$$

> **不同歷史的 world 不得因方便而 silent collapse。Evidence merge、lineage merge 與 state merge 必須分離。**

---

# 261. Principle V — Lineage Acyclicity

$$
\boxed{
\textbf{Lineage Acyclicity Principle}
}
$$

> **World historical ancestry 必須保持 acyclic；任何 feedback 應作為 information edge，而非偽造 ancestry cycle。**

---

# 262. Principle VI — Branch Evidence Locality

$$
\boxed{
\textbf{Branch Evidence Locality Principle}
}
$$

> **branch comparison 首先只支援該 world contract 下的 difference claim，外推現實仍需要 WDC-01 transport contract。**

---

# 263. Principle VII — Branch Cost

$$
\boxed{
\textbf{Branch Cost Principle}
}
$$

> **Fork、run、checkpoint、archive 與 evaluation 都消耗資源；world tree expansion 必須受 global compute ledger 約束。**

---

# 264. WDC-02 Benchmark A — Exact Fork

建立 deterministic symbolic world。

checkpoint：

$$
C_\tau.
$$

fork A/B。

---

# 265. Expected

shared prefix hash identical。

---

# 266. Post-Fork

A/B history divergence。

---

# 267. Benchmark B — Approximate Visual Fork

same rendered frame，

different hidden state。

測是否 falsely treats as same checkpoint。

---

# 268. Benchmark C — Controlled Intervention

A：

$$
u=0.
$$

B：

$$
u=1.
$$

其他 matched。

---

# 269. Measure

$$
\Delta Y.
$$

---

# 270. Benchmark D — Seed Policy

比較：

- paired seed；
- independent seed。

測 variance / uncertainty。

---

# 271. Benchmark E — Silent Mutation Attack

child secretly changes model version。

audit 應 detect。

---

# 272. Benchmark F — Illegal Merge

兩 branches resource histories mutually incompatible。

MergeWorld without reconciliation：

$$
\boxed{
FAIL.
}
$$

---

# 273. Benchmark G — Evidence Merge

同一 candidate 在 5 worlds。

aggregate outcomes，

不建立 merged state。

---

# 274. Benchmark H — World DAG

建立合法 multi-parent derived world。

check no cycles。

---

# 275. Benchmark I — Tombstone

prune 90% branches，

保留 lineage metadata。

測 survivorship audit。

---

# 276. Benchmark J — Fork Privilege Escalation

child request higher external authority。

expected：

$$
\boxed{
DENY.
}
$$

---

# 277. 可否證條件

## F277.1 Clone–Fork No-Gain

若 lineage / fork metadata 對 audit、comparison、reproducibility 完全無增量，taxonomy 可簡化。

## F277.2 Prefix Failure

若 checkpoint restore 無法形成穩定 shared prefix，paired world experiment 應降級。

## F277.3 Hidden-State Contamination

若只用 observable state fork 導致大量不可重現差異，checkpoint contract 不充分。

## F277.4 Branch Attribution Failure

若 declared single-variable fork 仍有大量 undeclared differences，不能做 causal attribution。

## F277.5 Merge Ambiguity

若 merge semantics 無法判定 conflicting state，state merge 必須拒絕。

## F277.6 Lineage Cycle

若 genealogy graph 允許 child 成為自己 ancestor，world lineage model 失效。

## F277.7 Cost Explosion

若 fork overhead / world count 使 compute 超過 value，必須由 Governor prune / deny。

## F277.8 Evidence Overtransfer

若 simulated branch difference 被直接報成 real-world effect，證據邊界失效。

---

# 278. 與 WDC-03 的接口

WDC-01：

$$
\boxed{
FutureCandidate
\rightarrow
RunnableWorld.
}
$$

WDC-02：

$$
\boxed{
RunnableWorld
\rightarrow
BranchingWorldGraph.
}
$$

現在 world graph 可以快速變成：

$$
\boxed{
N_W\sim b^d.
}
$$

下一個問題立刻出現：

> **不可能每一條 branch 都永久執行。誰決定 Spawn？誰決定 Fork？誰分配 budget？誰 Pause、Kill、Archive、Promote？**

這就是：

# **WDC-03 — World-Domain Governor**
## **《世界域管理器：世界生成、資源分配、停止與晉升》**

它將第一次正式建立：

```text
SpawnWorld
ForkWorld
PauseWorld
ResumeWorld
KillWorld
ArchiveWorld
PromoteWorld
AllocateBudget
CompareWorlds
```

以及最重要的問題：

$$
\boxed{
\text{Which worlds deserve computation?}
}
$$

---

# 279. 結論

WDC-01 讓：

$$
f_i
$$

成為：

$$
W_i.
$$

WDC-02 現在讓：

$$
W_i
$$

真正具有 genealogy。

在某個 local time：

$$
\tau,
$$

我們保存：

$$
C_{i,\tau}.
$$

然後：

$$
\boxed{
Fork(
W_i,
C_{i,\tau},
\Delta_1
)
\rightarrow
W_{i,1}
}
$$

與：

$$
\boxed{
Fork(
W_i,
C_{i,\tau},
\Delta_2
)
\rightarrow
W_{i,2}.
}
$$

兩個 children 在 fork 前共享：

$$
\boxed{
\text{同一歷史 prefix},
}
$$

但 fork 後：

$$
\boxed{
\text{各自累積自己的世界歷史}.
}
$$

因此所謂「平行世界」在 WDC 中不是 metaphysics。

它首先只是：

$$
\boxed{
\text{shared-prefix executable branches}.
}
$$

真正有價值的不是：

> 我們複製了 100 個世界。

而是：

> **我們知道每個世界從哪裡分岔、到底改了什麼、什麼沒改、結果如何不同、哪些差異可信、哪些只是 model noise。**

因此 WDC-02 最核心的式子不是 world count，

而是：

$$
\boxed{
WorldBranch
=
Identity
+
Parent
+
Checkpoint
+
Delta
+
IndependentHistory
+
Provenance.
}
$$

也因此：

$$
\boxed{
Fork
\neq
Clone.
}
$$

以及：

$$
\boxed{
Merge
\neq
Fork^{-1}.
}
$$

分叉很容易。

**把已經擁有不同歷史的世界重新變成「同一個現在」反而是高難度操作。**

這個不對稱會一路影響後面的：

- Governor；
- cross-world evidence；
- nested agents；
- world merging；
- world promotion。

而現在真正無法逃避的下一題已經出現：

> **當 world graph 開始指數增長時，我們不是缺未來，而是未來太多。**

因此下一篇正式從「生成世界」轉向：

$$
\boxed{
\text{govern computation over worlds}.
}
$$

---

# Claim Typing

| Claim | Type | Status |
|---|---|---|
| Clone、Fork、Replay、Counterfactual、Mutation、Merge 非同一 | D | Canonical separation |
| WDC Fork 需要 identity / parent / checkpoint / delta / independent history | D | Canonical contract |
| paired branch 需要 shared prefix 與 matched comparison contract | D | Methodology |
| lineage graph 應保持 historical acyclicity | D | Canonical integrity rule |
| evidence merge、lineage merge、state merge 必須分離 | D | Canonical merge taxonomy |
| Linux/POSIX fork 提供 parent-child execution / copy semantics analogy | E | External systems analogue |
| Git branching / merge 提供 common-ancestor divergent-history analogy | E | External engineering analogue |
| Isaac Sim / Isaac Lab support cloned parallel environments | E | External simulation evidence |
| OpenUSD supports non-destructive variants / composition alternatives | E | External scene-description evidence |
| Genie 3 supports promptable world events / counterfactual scenarios | E | External world-model evidence |
| world branch outcome difference 等於 real causal effect | — | Explicitly rejected |
| MergeWorld 是 ForkWorld 的自然逆操作 | — | Explicitly rejected |

---

# Evidence Ladder

本文目前主要位於：

- **L0**：Branching World Graph / Fork Record / Merge taxonomy；
- **L1–L2**：deterministic / stochastic exact fork benchmarks；
- **L3**：process fork、Git lineage、Isaac cloning、USD variants、Genie interventions 提供局部工程對照；
- **L4**：需要 multi-backend fork / paired intervention / checkpoint reproducibility；
- **L5+**：World Governor、cross-world evidence、large-scale branch allocation 尚待後續。

---

# 參考文獻

## Neo.K 內部正典與譜系

1. Neo.K with Aletheia. *From Possible Futures to Runnable Worlds*. WDC-01 / BWC-01, 2026.
2. Neo.K with Aletheia. *Future as a Generated Base Space*. TCD-03, 2026.
3. Neo.K with Aletheia. *Prospective Attraction*. TCD-04, 2026.
4. Neo.K with Aletheia. *Historical Sedimentation*. TCD-05, 2026.
5. Neo.K with Aletheia. *Six-Way Temporal Coupling*. TCD-07, 2026.

## External technical calibration

6. The Open Group. *fork — create a new process*. POSIX.1-2024 System Interfaces.
7. Linux man-pages project. *fork(2) — create a child process*. Linux man-pages 6.18, 2026.
8. Git Project. *Git Branching — Basic Branching and Merging*. Pro Git, current official documentation.
9. Git Project. *git-merge Documentation*. Git 2.54+, official manual, 2026.
10. NVIDIA Isaac Sim. *Getting Started with Cloner*. Official Isaac Sim documentation, 2026.
11. NVIDIA Isaac Lab. *Cloning Environments*. Official Isaac Lab documentation, 2026.
12. Alliance for OpenUSD / Pixar. *USD Terms and Concepts; VariantSets, Layers, References, Composition*. Current OpenUSD documentation.
13. Google DeepMind. *Genie 3: A New Frontier for World Models*. 2025.
14. Google DeepMind. *Genie 3 — Promptable World Events and Interactive Worlds*. Current official model documentation.

---

## Public Version Disclaimer

本文是一個 runnable-world branching / simulation-lineage framework。

本文不聲稱：

- WDC branch 是物理平行宇宙；
- process fork、Git branch、USD variant 或 Isaac clone 等於 WDC Fork；
- simulated counterfactual 自動等於 causal counterfactual；
- shared visual state 等於 shared full world state；
- branch frequency 等於 real-world probability；
- multi-world consensus 等於 truth；
- state merge 普遍可行；
- child world 可以藉 fork 取得更高真實世界 authority；
- 本文已完成 World-Domain Governor；
- 本文對 classical $P$ vs. $NP$ 提供任何新證明。

本文真正建立的是：

$$
\boxed{
Fork(
W_p,
C_{p,\tau},
\Delta
)
\rightarrow
W_c
}
$$

並要求：

$$
\boxed{
\text{new identity}
+
\text{shared prefix}
+
\text{typed divergence}
+
\text{independent post-fork history}
+
\text{auditable lineage}.
}
$$
