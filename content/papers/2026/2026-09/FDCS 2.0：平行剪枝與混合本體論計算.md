# FDCS 2.0：平行剪枝與混合本體論計算

## 約束可能域、平行分支、不變性提取、AI 自適應探索與可重新開啟證書

**英文題名：** *FDCS 2.0: Parallel Pruning and Hybrid Ontological Computation — Constraint-Bounded Possibility Domains, Parallel Branches, Invariance Extraction, AI-Adaptive Exploration, and Reopenable Certificates*  
**文件編號：** EML-FDCS-PPA-HOC-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-21  
**版本：** v0.1  
**文件性質：** FDCS 2.0 foundational extension / 初版  
**狀態：** Research Draft；未主張一般實證有效性  
**前置理論：** MWT、FDCS 2.0 Formal Core、IRCI 2.0 interface、Observer-Resource Predictability Frontier  
**概念來源：** 2026-02 未發表舊稿《FDCS 2.0 終極版：平行剪枝與混合本體論計算》  
**Canonical source：** UTF-8 Markdown；數學 delimiter 僅 ` $...$ ` 與 `$$...$$`

---

# 摘要

本文提出 FDCS 2.0 的平行剪枝與混合本體論計算擴展。其歷史來源是一個較早期、未發表的 FDCS 構想：當系統參數具有高度時變性、異質性、情境依賴或不可由單一點估計充分表示時，不必只求一組「最佳參數」，而可以先建立受約束的可能域，展開多個平行候選分支，計算其演化，再從中尋找對參數、分支、模型或局部擾動較穩健的結構。

本文保留此核心思想，但撤回舊版本中過強的推論。特別地，本文不再將「95% 的離散網格點滿足某性質」提升為本體論必然；不再將 49% 確定性與 51% 真隨機視為 FDCS 的固定世界比例；不再把 GPU 並行、邏輯平行分支與物理同步視為同一概念；也不再主張約束計算可以一般性取代測量、實驗或 causal identification。

新版建立五個核心結構。第一，**Admissible Possibility Domain**：所有可計算分支都必須相對於明示的 world boundary、model family、constraint set、legality rules、query、observer、resource budget 與 version 建立。第二，**Parallel Branch Space**：平行性首先是邏輯上的多分支共存，是否真的並行計算由 runtime scheduler 決定。第三，**Typed Hybrid Transition**：不同演化步驟可以是 deterministic、stochastic、agent-choice、adversarial、unknown 或 hybrid，而不要求以固定百分比混合。第四，**Parallel Pruning Algorithm 2.0（PPA 2.0）**：候選域先經 legality，再執行 branch expansion、evaluation、counterexample search、sound pruning、robustness extraction 與 certificate generation。第五，**Reopenable Certificate**：任何「穩健」「普遍」「近似不變」結論都只在其明示的 domain/model/boundary/version contract 下成立，當新 evidence、bridge、model、boundary 或 refinement 出現時可以被 reopen。

本文進一步區分三種不同強度的結果：有限完整域上的 domain-universal invariance、相對某測度的 measure-relative robustness，以及只對特定離散／採樣集合成立的 sample/grid coverage。本文證明：若有限 admissible domain 已被完整枚舉且不存在 unresolved branches，則所有分支皆滿足性質 $P$ 足以形成該 domain contract 下的 universal certificate；反之，僅有有限 grid 上的高比例覆蓋，在沒有額外 continuity、regularity、interval enclosure 或 covering-error bound 時，不能推出連續域上的同等比例。這直接取代舊版「95% 法則」。

最後，本文將「Computational Ontology」重新定義為一種 **ontology-computation discipline**：它不是把 World 等同於可計算可能空間，而是在 MWT/FDCS 已聲明的 representation/runtime boundary 中，對可能態、演化、分支與不變結構進行可追溯、可證書化、可重新開啟的計算。

**關鍵詞：** FDCS、Parallel Pruning、Computational Ontology、Hybrid Ontological Computation、Possibility Domain、Robustness、Invariant、Counterexample Search、AI Adaptive Exploration、MWT

---

# 0. 本文的位置：不是重新定義 FDCS Core

FDCS 2.0 formal core 已將 FDCS 定義為 MWT runtime 的 causal specialization：

$$
\boxed{
\mathfrak C_{\Gamma}(t)
=
\operatorname{CProj}_{\Gamma}
\left(
\mathfrak L_W(t)
\right).
}
$$

並固定：

$$
\boxed{
\mathbf W
\neq
\mathfrak W_t^{\mathrm{act}}
\neq
\mathfrak L_W(t)
\neq
\mathfrak C_{\Gamma}(t).
}
$$

本文不改動此核心。本文新增的是：

$$
\boxed{
\text{如何在一個已被合法界定的 causal/model possibility domain 中，
展開、計算、剪枝與提取穩健結構。}
}
$$

因此：

$$
\boxed{
\mathrm{PPA/HOC}
\subset
\mathrm{FDCS}_{2.0}\text{ extension layer}.
}
$$

---

# 0.1 Formal Status Register

本文強制區分：

$$
\mathsf{Definition}
\neq
\mathsf{RuntimeContract}
\neq
\mathsf{Proposition}
\neq
\mathsf{ConditionalTheorem}
\neq
\mathsf{ModelFamily}
\neq
\mathsf{Hypothesis}.
$$

| ID | 陳述 | Status |
|---|---|---|
| F0 | World 不等於 possibility domain / model family / computed branches | $\mathsf{ImportedAxiom}$ |
| D1 | Admissible Possibility Domain | $\mathsf{Definition}$ |
| D2 | Parallel Branch Object / Branch Space | $\mathsf{Definition}$ |
| D3 | Typed Hybrid Transition | $\mathsf{Definition}$ |
| R1 | legality-first possibility admission | $\mathsf{RuntimeContract}$ |
| D4 | PPA 2.0 pipeline | $\mathsf{Definition}+\mathsf{RuntimeContract}$ |
| D5 | domain-universal invariance | $\mathsf{Definition}$ |
| D6 | measure-relative robustness | $\mathsf{Definition}$ |
| D7 | unresolved-aware robustness interval | $\mathsf{Definition}$ |
| T1 | finite exhaustive invariance certificate | $\mathsf{ConditionalTheorem}$ |
| P1 | finite grid coverage does not imply continuum coverage | $\mathsf{Proposition}$ |
| T2 | sound quotient pruning under property-preserving equivalence | $\mathsf{ConditionalTheorem}$ |
| P2 | noncommutative C0 coarsening cannot erase order losslessly | $\mathsf{Proposition}$ |
| R2 | surrogate prediction cannot directly become exact certificate | $\mathsf{RuntimeContract}$ |
| H1 | AI adaptive exploration policy | $\mathsf{ModelFamily}$ |
| H2 | threshold $\tau$ selection | $\mathsf{DecisionPolicy}$ |
| D8 | Computational Ontology as runtime discipline | $\mathsf{Definition}$ |

---

# 1. 從點估計到約束可能域

舊構想中最重要的轉向可以保留：

$$
\boxed{
\text{single best point}
\rightarrow
\text{explicit admissible domain}.
}
$$

但新版不主張 measurement 無用，而採：

$$
\boxed{
\text{measurement}
+
\text{theory}
+
\text{constraints}
+
\text{uncertainty sets}
+
\text{model families}.
}
$$

測量可以收窄 domain；理論可以排除不合法狀態；先驗限制可以提供 hard boundary；歷史資料可以改變 measure 或 exploration priority。

## 1.1 Candidate Possibility Domain

給定 inquiry context：

$$
\Gamma
=
(
\mathfrak B^{(v)},
Q,
O,
R,
\mathcal M,
\mathcal C,
\Lambda,
\mathfrak I,
\mathcal T
),
$$

其中 $\mathfrak B^{(v)}$ 為 world boundary version， $Q$ 為 query， $O$ 為 observer， $R$ 為 resource budget， $\mathcal M$ 為 model family， $\mathcal C$ 為 constraints， $\Lambda$ 為 legality rules， $\mathfrak I$ 為 identity specification， $\mathcal T$ 為 temporal/version scope。

先建立 candidate possibility carrier：

$$
\widetilde{\Omega}_{\Gamma}^{(v)}.
$$

它可以包含 initial states、parameter intervals、disturbances、external events、agent-choice branches、model variants、bridge variants、resolution variants 與 scheduler/path variants。

## 1.2 Admissible Possibility Domain

定義：

$$
\boxed{
\Omega_{\Gamma}^{(v)}
=
\left\{
\omega
\in
\widetilde{\Omega}_{\Gamma}^{(v)}
:
\operatorname{Adm}_{W,\Gamma}(\omega)
=
\mathsf{Legal}
\right\}.
}
$$

此 domain 不等於 World 的全部物理可能態，只代表在指定 boundary、model、constraints、identity、legality、resolution 與 version 下，當前被允許進入此計算的候選可能域。

## 1.3 Domain Coverage 是一個責任

若宣稱「覆蓋所有合理可能」，至少必須交代：合理由什麼 contract 定義、是否有未建模變量、model family 是否完整、boundary 是否固定、agent choice 如何表示、是否有 unresolved region、continuum 是否只以 finite grid 近似、grid error 是否有 certificate，以及新 evidence 是否會觸發 reopen。

因此：

$$
\boxed{
\text{large finite grid}
\neq
\text{all possibilities}.
}
$$

---

# 2. Parallel Branch Space

令：

$$
\omega\in\Omega_{\Gamma}^{(v)}
$$

是一個 admissible possibility seed。經 branch expansion：

$$
\operatorname{Expand}_{\Gamma}
:
\omega
\mapsto
\mathcal B(\omega).
$$

完整 branch family：

$$
\boxed{
\mathbb B_{\Gamma}^{(v)}
=
\bigcup_{\omega\in\Omega_{\Gamma}^{(v)}}
\mathcal B(\omega).
}
$$

每個 branch 至少帶 branch ID、initial state、parameters、model reference、disturbance、agent-choice path、history/order、legality、provenance、certificate 與 version。

## 2.1 三種「平行」必須分離

$$
\boxed{
\text{logical branch coexistence}
\neq
\text{computational concurrency}
\neq
\text{physical simultaneity}.
}
$$

多個 branch 可邏輯共存；runtime 可選擇 GPU、CPU、distributed workers 或 sequential execution；World 中事件是否物理同時則是另一個問題。

---

# 3. Typed Hybrid Ontological Computation

舊版固定使用 $49\%+51\%$ 表示 deterministic 與 true-random components。本文撤回固定比例，保留真正有價值的部分：

$$
\boxed{
\text{不同 transition 的生成機制可能不同。}
}
$$

對 interaction / transition $e$，定義：

$$
\boxed{
\tau_{\Gamma}(e)
\in
\{
\mathsf{Deterministic},
\mathsf{Stochastic},
\mathsf{AgentChoice},
\mathsf{Adversarial},
\mathsf{Unknown},
\mathsf{Hybrid}
\}.
}
$$

Deterministic 使用 $T(s)=s'$ ；Stochastic 使用明示 kernel $K(s'|s)$ ；AgentChoice 只聲明 admissible action set / policy family，不自動等同 random draw；Adversarial 表示下一步可能由有目標的對手選擇；Unknown 表示目前無合法模型足以分類；Hybrid 則允許多種 typed components 共存。

因此：

$$
\boxed{
\mathsf{AgentChoice}
\neq
\mathsf{Stochastic}
}
$$

除非另有合法 reduction。

---

# 4. C0 的重新定義：Resolution-Relative Zero-Lag

令 query relevant horizon 為 $H_{\Gamma}>0$，事件間 delay 為 $\Delta t$，tolerance 為 $\varepsilon_t>0$。定義：

$$
\boxed{
C_0^{(\Gamma,\varepsilon_t)}
\iff
\frac{|\Delta t|}{H_{\Gamma}}
\le
\varepsilon_t.
}
$$

其含義是：對此 query resolution 而言，delay 可以視為 zero-lag class；不是宇宙中的絕對零時間。

若：

$$
A\circ B(s)
\neq
B\circ A(s),
$$

即使 $A\sim_{C_0}B$，runtime 仍不得刪除 order。

### 命題 P2

若 exact successor reconstruction 是 audit contract 的一部分，且 $A\circ B(s)\neq B\circ A(s)$，則任何把 $(A,B)$ 與 $(B,A)$ 壓成同一無序事件集合的 zero-lag encoding 都不是 lossless。

**證明。** 若兩 order 被壓成同一 representation，decoder 無法同時唯一重建兩個不同 successor；若輸出兩個 successor，又無法知道實際 path。故 exact ordered reconstruction 失敗。□

---

# 5. Parallel Pruning Algorithm 2.0

PPA 2.0 不再是：

$$
\text{grid}
\rightarrow
\text{simulate}
\rightarrow
\text{95\%}
\rightarrow
\text{ontological truth}.
$$

新版定義：

$$
\boxed{
\mathsf{Compile}
\rightarrow
\mathsf{Generate}
\rightarrow
\mathsf{Admit}
\rightarrow
\mathsf{Expand}
\rightarrow
\mathsf{Evaluate}
\rightarrow
\mathsf{Partition}
\rightarrow
\mathsf{CounterexampleSearch}
\rightarrow
\mathsf{Prune}
\rightarrow
\mathsf{Extract}
\rightarrow
\mathsf{Certify}
\rightarrow
\mathsf{Reopen}.
}
$$

## 5.1 Inquiry Contract

$$
\mathfrak Q_{\mathrm{PPA}}
=
(
Q,
\mathfrak B^{(v)},
\mathcal M,
\mathcal C,
\Lambda,
\mathfrak I,
\mu,
\tau,
R,
\Pi_{\mathrm{out}}
).
$$

 $\mu$ 為 robustness measure， $\tau$ 為可選 decision threshold， $R$ 為 resource budget。

## 5.2 Legality-First Admission

candidate generation 可以很激進，但：

$$
\text{candidate}
\neq
\text{admitted branch}.
$$

候選依 legality 分為 Legal、Illegal、Undetermined、Conflicted；只有 Legal 進 active domain，Undetermined 與 Conflicted 必須保存。

## 5.3 Outcome Partition

對 property $P$，將已評估 branches 分成：

$$
\mathbb B_P,
\qquad
\mathbb B_{\neg P},
\qquad
\mathbb B_U,
\qquad
\mathbb B_C.
$$

不能只保留二值成功／失敗。

## 5.4 Counterexample Search

對 universal claim，一個合法反例就足以破壞 universal certificate。因此 PPA 應優先搜索 decision boundary、model disagreement、bridge-loss high region、high uncertainty、rare but legal extreme region、noncommutative path 與 uncovered domain。

## 5.5 Sound Pruning

允許的 pruning 至少包括 Illegal Pruning、Infeasible Pruning、Equivalence Quotient、Dominance Pruning、Certified Region Pruning。若只是 resource 不足，必須標記 Deferred。

$$
\boxed{
\mathsf{Deferred}
\neq
\mathsf{Pruned}
\neq
\mathsf{Refuted}.
}
$$


---

# 6. 三種結果強度：Universal、Robust、Sample Coverage

新版將舊稿中混在一起的三種結論強度拆開。

## 6.1 Domain-Universal Invariance

定義：

$$
\boxed{
\operatorname{UInv}
\left(
P
\mid
\Omega_{\Gamma}^{(v)},
F_{\Gamma}^{(v)}
\right)
=
1
}
$$

當且僅當：

$$
\forall
\omega
\in
\Omega_{\Gamma}^{(v)},
\qquad
P
\left(
F_{\Gamma}^{(v)}(\omega)
\right)
=
\mathsf{True},
$$

且 coverage contract 完整。

這是一個 **domain-relative universal**，仍不等於 $P$ 在 World totality 中普遍為真。

## 6.2 Finite Exhaustive Invariance Theorem

### 定理 T1

若：

1. $\Omega_{\Gamma}^{(v)}$ 為 finite；
2. 每個 $\omega\in\Omega_{\Gamma}^{(v)}$ 都已合法 admit；
3. 每個 $\omega$ 都被完整 evaluate；
4. 沒有 unresolved / conflicted branch；
5. 對所有 $\omega$， $P(F_{\Gamma}^{(v)}(\omega))=\mathsf{True}$ ；

則：

$$
\operatorname{UInv}
\left(
P
\mid
\Omega_{\Gamma}^{(v)},
F_{\Gamma}^{(v)}
\right)
=
1.
$$

**證明。** 條件 1–4 給出 domain 上的 complete finite coverage；條件 5 對 domain 每個元素成立，直接得到 universal quantification。□

這證明的是「指定 finite domain contract 內的 universal」，不是 World-total necessity。

## 6.3 Measure-Relative Robustness

若有明示 measure $\mu$，定義 resolved robustness：

$$
\boxed{
\operatorname{Rob}_{\mu}
(P)
=
\frac{
\mu(\mathbb B_P)
}{
\mu(\mathbb B_P)
+
\mu(\mathbb B_{\neg P})
}.
}
$$

所以：

$$
\operatorname{Rob}_{\mu}(P)=0.95
$$

只表示：在該 measure contract 下，95% 的 resolved mass 支持 $P$。

它不表示：

$$
P
=
\text{95\% true}.
$$

## 6.4 Unresolved-Aware Robustness Interval

若 unresolved/conflicted mass 不為零，只報 resolved ratio 會過度樂觀。

令：

$$
M
=
\mu(\mathbb B_P)
+
\mu(\mathbb B_{\neg P})
+
\mu(\mathbb B_U)
+
\mu(\mathbb B_C).
$$

定義：

$$
\boxed{
R^{-}
=
\frac{\mu(\mathbb B_P)}{M},
}
$$

以及：

$$
\boxed{
R^{+}
=
\frac{
\mu(\mathbb B_P)
+
\mu(\mathbb B_U)
+
\mu(\mathbb B_C)
}{M}.
}
$$

於是：

$$
\boxed{
R^{-}
\le
R_{\mathrm{contract}}
\le
R^{+}.
}
$$

這使 Unknown / Unresolved / Conflicted 成為 robustness 計算的一級責任。

---

# 7. 95% 不再是真理常數

舊稿將 $\tau=0.95$ 描述為接近最優的本體論 threshold。本文撤回。

新版：

$$
\boxed{
\tau
=
\text{decision-policy parameter}.
}
$$

不同 query 可以使用 0.5、0.9、0.95、0.99、1.0，甚至完全不用 scalar threshold。工程安全、exploratory science、universal theorem、asymmetric loss problem 的 threshold 都不應相同。

因此：

$$
\boxed{
95\%
\neq
\text{ontological constant}.
}
$$

---

# 8. Grid Coverage 不能直接升級成 Continuum Coverage

### 命題 P1

對 continuum domain：

$$
\Omega=[0,1],
$$

有限 grid：

$$
G\subset[0,1],
$$

即使：

$$
\frac{
|\{x\in G:P(x)\}|
}{
|G|
}
=
1,
$$

也不推出：

$$
\mu
\{
x\in[0,1]:P(x)
\}
=
1.
$$

**證明：反例。**

令：

$$
P(x)
=
\begin{cases}
\mathsf{True}, & x\in G,\\
\mathsf{False}, & x\notin G.
\end{cases}
$$

則 grid coverage 為 1。但對 Lebesgue measure，有限 $G$ 的 measure 為零，因此：

$$
\mu
\{
x:P(x)=\mathsf{True}
\}
=
0.
$$

故有限 grid 上 100% 成立，仍不足以推出 continuum 上任意正比例。□

## 8.1 Continuum Promotion 需要額外證書

若要從 finite evaluation 推到 continuum，至少需要某類額外結構，例如：

- Lipschitz / Hölder bound；
- monotonicity theorem；
- interval arithmetic enclosure；
- verified numerics；
- covering-number bound；
- reachability enclosure；
- certified surrogate error；
- symbolic proof；
- exhaustive finite partition with enclosure。

因此：

$$
\boxed{
\text{grid density}
\neq
\text{coverage proof}.
}
$$

---

# 9. Sound Equivalence Pruning

平行態空間可能巨大，因此剪枝仍然必要。但只有在 equivalence contract 足夠強時，才能用 representative 取代整個 class。

令 $\sim_Q$ 為 query-relative equivalence relation。若：

$$
b_1\sim_Q b_2,
$$

必須保證：

$$
P(F(b_1))
=
P(F(b_2))
$$

對目標 property 成立。

## 9.1 Quotient-Pruning Theorem

### 定理 T2

假設：

1. $\sim_Q$ 將 branch space 分成 equivalence classes；
2. 對每一 class $[b]$，所有元素在 query $Q$ 下有相同 property outcome；
3. 每個 class 至少 evaluate 一個 representative。

則對判斷：

$$
\forall b\in\mathbb B,\ P(F(b)),
$$

只檢查 quotient representatives 與檢查完整 branch space 等價。

**證明。** 每個 branch 屬於某 equivalence class。由條件 2，representative 與 class 內所有 branches 的 property outcome 一致。故所有 representatives 滿足 $P$ 當且僅當所有 branches 滿足 $P$。□

## 9.2 Pruning Certificate

每次剪枝至少記錄：

$$
\mathcal C_{\mathrm{prune}}
=
(
\text{region},
\text{reason},
\text{theorem},
\text{query},
\text{version},
\text{loss},
\text{reopen}
).
$$

不能只寫：

> pruned because low probability.

---

# 10. AI-Adaptive Parallel Pruning

舊構想後期已出現一個重要轉向：不必永遠均勻窮舉，可以讓 AI 找最值得計算的位置。新版正式保留，但強制分離：

$$
\boxed{
\text{AI exploration recommendation}
\neq
\text{certificate}.
}
$$

## 10.1 Exploration Policy

定義：

$$
\pi_E
:
\mathcal S_{\mathrm{search}}
\rightarrow
\omega_{\mathrm{next}}.
$$

AI 可以依 uncertainty、counterexample likelihood、decision-boundary proximity、model disagreement、uncovered volume、bridge loss、novelty、causal sensitivity、certificate deficit 或 expected information gain 選擇下一個 branch / region。

## 10.2 Certificate Separation Rule

若 surrogate model $\widehat F$ 預測某 region 全部滿足 $P$，但該 region 沒有 verified error bound，則只能記：

$$
\mathsf{SurrogatePrediction}.
$$

不能記：

$$
\mathsf{CertifiedInvariant}.
$$

只有 exact evaluation、verified enclosure、formal proof 或 certified error bound 才能提升 certificate maturity。

## 10.3 Counterexample-Directed Adaptive Loop

```text
1. seed admissible domain
2. evaluate initial representatives
3. estimate coverage gaps
4. search likely counterexamples
5. refine high-risk / high-uncertainty regions
6. certify safe/equivalent regions
7. prune only certified regions
8. defer unresolved regions when budget exhausted
9. return robustness interval + unresolved obligations
10. reopen when new evidence/model/boundary appears
```

所以：

$$
\boxed{
\text{adaptive search}
+
\text{sound certificates}
>
\text{blind brute-force enumeration}
}
$$

作為工程目標成立；本文不把它提升成一般 complexity theorem。

---

# 11. Open-System Possibility Domains

舊稿雖承認 parameter 會變，卻容易把「合理區間」寫得像永久固定。新版允許：

$$
\boxed{
\Omega_{\Gamma,t}^{(v)}
\neq
\Omega_{\Gamma,t+1}^{(v+1)}.
}
$$

domain 可以因 new evidence、external event、technology change、policy change、new bridge、new observer、boundary expansion、model revision、identity refinement 或 discovered counterexample 而更新。

定義：

$$
\operatorname{UpdateDomain}
:
\left(
\Omega_t,
e,
\Gamma_t
\right)
\mapsto
\Omega_{t+1}.
$$

每次更新保留 lineage：

$$
\Omega_t
\rightarrow
\Omega_{t+1}.
$$

舊 certificate 可以變成：

$$
\mathsf{Stale}
$$

或：

$$
\mathsf{ReopenRequired}.
$$

而不是被刪除。

---

# 12. Reopenable Computational Certificate

對 property $P$，定義：

$$
\boxed{
\mathcal C_P
=
\left\langle
P,
\Gamma,
\Omega^{(v)},
F^{(v)},
\mu,
\text{coverage},
\text{robustness},
\text{unresolved},
\text{counterexamples},
\text{proofs},
\text{resource},
\text{history},
\text{reopen}
\right\rangle.
}
$$

certificate 必須回答：property 是什麼、domain 是什麼、boundary version 是什麼、models 是什麼、measure 是什麼、是否 complete enumeration、哪些 region unresolved、有無 counterexamples、哪些 region 被剪枝及其理由、使用多少 resource，以及何時必須 reopen。

---

# 13. Computational Refutability

舊稿後段提出「計算可辯駁性」，方向保留但重新形式化。

PPA certificate 可以被以下事件削弱或撤銷：

- **Domain Refutation**：原 domain 漏掉合法 region；
- **Model Refutation**：原 dynamics / bridge / transition semantics 不成立；
- **Counterexample Refutation**：找到合法 $\omega^\star$ 使 $P(F(\omega^\star))=\mathsf{False}$ ；
- **Numerical Refutation**：原計算存在 numerical / implementation error；
- **Measure Refutation**：robustness 的 $\mu$ 不再適用；
- **Boundary Refutation**：world boundary 改變。

因此：

$$
\boxed{
\text{certificate}
=
\text{replayable and challengeable object}.
}
$$

不是不可證偽宣言。

---

# 14. Computational Ontology 的新版定義

舊稿曾接近：

$$
\text{ontology}
=
\text{computable possibility space}.
$$

本文撤回此等同。

## 14.1 Definition D8

**Computational Ontology** 在 FDCS 2.0 中定義為：

> 對一個已聲明的 world/model boundary 所承載之可能態、關係、演化、分支、身份、約束與不變結構，進行可定址、可追蹤、可證書化與可重新開啟的計算表示與推理 discipline。

形式上：

$$
\boxed{
\mathfrak O_{\Gamma}^{\mathrm{comp}}
=
\left\langle
\Omega,
\mathbb B,
\mathcal T,
F,
\Lambda,
\mu,
\mathcal P,
\mathcal C,
\mathcal H,
\mathcal R
\right\rangle.
}
$$

其中 $\Omega$ 是 admissible domain， $\mathbb B$ 是 branch space， $\mathcal T$ 是 typed transitions， $F$ 是 evaluation/evolution， $\Lambda$ 是 legality， $\mu$ 是可選 measure， $\mathcal P$ 是 pruning structure， $\mathcal C$ 是 certificates， $\mathcal H$ 是 history， $\mathcal R$ 是 reopen conditions。

永久保持：

$$
\boxed{
\mathfrak O_{\Gamma}^{\mathrm{comp}}
\neq
\mathbf W.
}
$$

## 14.2 Hybrid Ontological Computation

定義：

$$
\boxed{
\mathrm{HOC}_{\Gamma}
=
\operatorname{Compute}
\left(
\mathfrak O_{\Gamma}^{\mathrm{comp}}
\right).
}
$$

computation 可以聯邦使用 deterministic solver、stochastic simulator、theorem prover、interval solver、optimization、agent simulation、adversarial search、retrieval、empirical data、AI surrogate 與 human judgment adapter，但不同 solver 的 evidence status 必須分開。

---

# 15. 與實證的關係：不是取代，而是重分工

新版不主張：

$$
\text{computation}
>
\text{experiment}.
$$

而是：

$$
\boxed{
\begin{aligned}
\text{measurement}&\rightarrow\text{constrain/calibrate domain},\\
\text{experiment}&\rightarrow\text{test model/transition/bridge},\\
\text{computation}&\rightarrow\text{explore consequences},\\
\text{counterexample search}&\rightarrow\text{stress universal claims},\\
\text{PPA certificate}&\rightarrow\text{record conditional robustness}.
\end{aligned}
}
$$

PPA 不自動取代 observational evidence、natural experiments、comparative cases、mechanism evidence、archival data 或 model criticism。

---

# 16. 與 FDCS 2.0 Core 的接口

PPA 使用：

$$
\operatorname{CProj}_{\Gamma}
$$

取得 query-relevant causal slice，不直接掃描 World totality。

每個 branch evaluation 可以產生 typed causal record：

$$
\mathfrak r_{x\rightarrow y}^{\Gamma,t,b,h,v}.
$$

PPA 不把它們重新壓成單一 $[0,1]$ 權重。

所有 cross-ledger branch 必須通過 legality 才可 commit；若 $A\circ B\neq B\circ A$，branch identity 必須保存 order。

實際 run 仍滿足 finite active support：

$$
\boxed{
|\mathcal A_{q,\Gamma,\varepsilon,R}(t)|
<
\infty.
}
$$

resource 不足時應標記 Defer，而不是假裝 exhaustive。


---

# 17. 與 IRCI 2.0 的接口

IRCI 2.0 提供：

$$
\text{open-ended recursive refinement}.
$$

PPA 2.0 提供：

$$
\text{which regions to expand / prune / certify}.
$$

二者可形成：

$$
\boxed{
\mathrm{IRCI}_{2.0}
+
\mathrm{PPA}_{2.0}
=
\text{adaptive recursive causal exploration}.
}
$$

## 17.1 Branching-Aware Refinement Budget

對 recursive region 使用 query-relative shell mass：

$$
M_n^{(r)}(\alpha).
$$

若：

$$
\sum_n M_n^{(r)}(\alpha)<\infty,
$$

可以建立 finite-error truncation。PPA 可把 truncation certificate 作為 pruning reason，但不能用舊式單一路徑 $\lambda^k$ 取代完整 branching mass。

---

# 18. Observer-Resource Interface

PPA 結論也依 resource。

低 budget $R_1$ 可能只探索：

$$
\Omega_1\subset\Omega.
$$

高 budget $R_2>R_1$ 可能探索：

$$
\Omega_2,
\qquad
\Omega_1\subseteq\Omega_2.
$$

所以：

$$
\boxed{
\text{absence of discovered counterexample}
\neq
\text{absence of counterexample}.
}
$$

certificate 必須記錄 search horizon、active support 與 deferred regions。

---

# 19. Synthetic Example：R0 非交換政策世界

本節只使用完全合成、可手算的 reference world，不作現實經濟結論。

初始：

$$
P_0=100.
$$

兩個同類但異質 operator：

$$
A(P)=P+10,
$$

$$
B(P)=0.9P.
$$

兩個合法 order：

$$
AB,
\qquad
BA.
$$

結果：

$$
B(A(100))=99,
$$

$$
A(B(100))=100.
$$

因此：

$$
A\circ B
\neq
B\circ A.
$$

Demand：

$$
D(P)=200-P.
$$

則：

$$
D_{AB}=101,
$$

$$
D_{BA}=100.
$$

## 19.1 Universal Property Example

令：

$$
P_1:
D\ge100.
$$

在 finite domain：

$$
\Omega
=
\{AB,BA\},
$$

兩個 branches 都滿足 $P_1$。因為 domain 已完整枚舉且沒有 unresolved branch：

$$
\boxed{
\operatorname{UInv}(P_1\mid\Omega)=1.
}
$$

這是一個 bounded domain-universal certificate，不表示所有現實政策世界都滿足此性質。

## 19.2 Robustness Example

令：

$$
P_2:
P_{\mathrm{final}}<100.
$$

則：

$$
P_2(AB)=\mathsf{True},
$$

$$
P_2(BA)=\mathsf{False}.
$$

若對兩 branch 使用 uniform measure：

$$
\mu(AB)=\mu(BA)=\frac12,
$$

則：

$$
\boxed{
\operatorname{Rob}_{\mu}(P_2)
=
0.5.
}
$$

所以 PPA 只能說：在這個 bounded synthetic contract 中，該性質 robustness 為 0.5。

## 19.3 Refinement 與 Reopen

Demand model 從：

$$
D_{\mathrm{coarse}}(P)
=
200-P
$$

refine 成：

$$
D_R(P)=120-0.7P,
$$

$$
D_I(P)=90-0.4P.
$$

在 $P=99$ 得：

$$
D_{\mathrm{refined}}=101.1.
$$

舊 certificate 不刪除，而標記：

$$
\mathsf{Stale/ReopenRequired}.
$$

這是 open-system PPA 的最小 executable interpretation。

---

# 20. PPA 2.0 Reference Pseudocode

```text
function PPA2(query_contract):

    Gamma = compile(query_contract)

    candidate_domain =
        generate_candidate_domain(Gamma)

    partition =
        legality_partition(candidate_domain)

    legal_domain = partition.legal
    unresolved_admission = partition.undetermined
    conflicted_admission = partition.conflicted

    branch_space =
        expand_branches(
            legal_domain,
            Gamma
        )

    results = {}
    deferred = {}

    while budget_remains(Gamma.resource):

        target =
            exploration_policy.select(
                branch_space,
                results,
                deferred
            )

        if target is None:
            break

        result =
            typed_evaluate(
                target,
                Gamma
            )

        results[target.id] = result

        counterexamples =
            update_counterexample_index(
                result,
                Gamma.property
            )

        pruning_certificates =
            sound_prune(
                branch_space,
                results,
                Gamma
            )

    coverage =
        compute_coverage(
            branch_space,
            results,
            pruning_certificates
        )

    robustness_interval =
        compute_unresolved_aware_bounds(
            results,
            deferred,
            unresolved_admission,
            conflicted_admission,
            Gamma.measure
        )

    certificate =
        build_certificate(
            Gamma,
            legal_domain,
            branch_space,
            results,
            counterexamples,
            pruning_certificates,
            coverage,
            robustness_interval,
            reopen_conditions
        )

    return certificate
```

---

# 21. AI-Native Runtime Architecture

建議模組：

```text
PPA Runtime
├── Inquiry Compiler
├── Domain Constructor
├── Legality Gate
├── Branch Expander
├── Transition Type Registry
├── Solver Federation
├── Counterexample Engine
├── Adaptive Explorer
├── Equivalence / Dominance Prover
├── Pruning Certificate Store
├── Coverage Engine
├── Robustness Engine
├── Resource Controller
├── Provenance / History Store
└── Reopen Engine
```

AI 可以負責 domain proposal、model comparison、counterexample proposal、search priority、branch clustering、symbolic conjecture、bridge candidate generation 與 explanation projection；但 commit boundary 仍需 legality / certificate。

---

# 22. Machine Schema Sketch

```yaml
ppa_run:
  run_id:
  world_ref:
  boundary_version:
  inquiry_contract:
  model_family:
  constraint_set:
  legality_ruleset:
  identity_spec:
  measure_spec:
  threshold_policy:
  resource_budget:

  possibility_domain:
    candidate_regions:
    legal_regions:
    illegal_regions:
    undetermined_regions:
    conflicted_regions:

  branch_space:
    branch_ids:
    transition_types:
    history_refs:

  evaluations:
    computed:
    deferred:
    failed:

  counterexamples:
  pruning_certificates:
  coverage_certificate:

  robustness:
    resolved_ratio:
    lower_bound:
    upper_bound:
    measure_ref:

  conclusion:
    status:
    claim:
    maturity:

  provenance:
  certificates:
  reopen_conditions:
```

---

# 23. 結論狀態 Vocabulary

PPA 不應只有：

```text
ontologically_certain
parameter_dependent
```

新版至少使用：

```text
DomainUniversal
RobustAboveThreshold
RobustBelowThreshold
ParameterSensitive
ModelSensitive
CounterexampleFound
CoverageIncomplete
Unresolved
Conflicted
ResourceLimited
Stale
ReopenRequired
```

---

# 24. 舊稿概念遷移表

| 舊概念 | v0.1 新版 |
|---|---|
| 不測量參數 | 點估計之外，加入 constraint-bounded domain |
| 區間窮舉 | admissible possibility domain exploration |
| 所有可能 | 只有完整 coverage certificate 才可宣稱 exhaustive |
| 95% = 本體必然 | measure-relative robustness / decision threshold |
| 95% 法則最優 | 撤回； $\tau$ 為 decision policy |
| 49% fixed + 51% true random | typed hybrid transitions |
| 意志 = true random | AgentChoice 獨立 type，不做形上等同 |
| C0 = 零滯物理同步 | resolution-relative zero-lag class |
| GPU 同時計算 = 平行世界 | logical / computational / physical parallelism 分離 |
| 本體論剪枝 | certified parallel pruning |
| 不可證偽 | reopenable computational certificate |
| 實驗非必要 | measurement / experiment / computation 分工 |
| 大網格 = 全域覆蓋 | grid coverage 不得無證升到 continuum |
| brute force | adaptive counterexample-directed exploration |
| 模擬結果 = 世界結論 | model/domain-relative certificate |
| Computational Ontology = World ontology | ontology-computation runtime discipline |
| 參數區間固定 | versioned open-system domain |
| 剪掉低概率例外 | counterexamples 必須保留；pruning 需 sound certificate |

---

# 25. 本文不主張

本文不主張：

1. PPA 已取代實驗科學；
2. 所有社會參數都不可測；
3. 所有系統都適合區間／可能域方法；
4. 95% 有特殊本體論地位；
5. agent choice 等於 true randomness；
6. 49/51 是任何自然或社會系統的固定比例；
7. finite grid 可以自動代表 continuum；
8. GPU enumeration 等於窮舉 World；
9. AI surrogate prediction 等於 formal certificate；
10. all-to-all enumeration 是 PPA 的必要條件；
11. sound pruning 對所有 model family 都容易建立；
12. domain-universal 等於 World-universal；
13. computational ontology 等於 metaphysical ontology；
14. 沒找到 counterexample 就證明不存在 counterexample；
15. PPA 已解決一般 causal identification；
16. simulation 等於 observation；
17. robust conclusion 永遠不需要 reopen。

---

# 26. 可證偽／可失敗點

## 26.1 Domain Misspecification

重要合法 region 未進 $\Omega$。

## 26.2 Model Misspecification

 $F$ 沒有承載 relevant dynamics。

## 26.3 Bridge Error

cross-domain transport 失真。

## 26.4 Measure Dependence

robustness 結論高度依賴 $\mu$。

## 26.5 Pruning Unsoundness

剪掉了會改變 conclusion 的 branch。

## 26.6 Resource Failure

search budget 太小。

## 26.7 Adaptive Search Bias

AI 一直在熟悉區域取樣，漏掉 rare counterexample。

## 26.8 Open-System Drift

domain/version 更新速度高於 certificate 更新速度。

因此：

$$
\boxed{
\text{PPA can fail}
}
$$

是理論的必要部分。

---

# 27. 研究與工程 Gate

## Gate A — Finite Exact Domain

在完全有限、可手算 domain 上建立 exact certificate。FDCS R0 已提供此類最小世界。

## Gate B — Grid-to-Continuum Certification

至少建立一種 interval enclosure、Lipschitz bound 或 verified cover，使 finite computation 可以合法外推。

## Gate C — Sound Quotient Pruning

實作 query-relative equivalence certificate。

## Gate D — Counterexample-Directed Search

比較 uniform grid 與 adaptive exploration 的 counterexample discovery efficiency。

## Gate E — Mixed Transition Runtime

同一 possibility domain 中同時處理 deterministic、stochastic、agent-choice、adversarial、unknown。

## Gate F — Reopen Benchmark

在 domain/model version 改變後，驗證 stale certificate、dependency impact 與 recomputation。

## Gate G — External Domain Benchmark

最後才進入真實經濟、社會、工程或生態資料。

---

# 28. 新版核心定義

本文將舊構想正式收斂成：

$$
\boxed{
\begin{aligned}
\mathrm{PPA}_{2.0}
={}&
\mathrm{Admissible\ Possibility\ Domain}\\
&+
\mathrm{Parallel\ Branch\ Expansion}\\
&+
\mathrm{Legality\text{-}First\ Filtering}\\
&+
\mathrm{Typed\ Hybrid\ Transitions}\\
&+
\mathrm{Adaptive\ Exploration}\\
&+
\mathrm{Counterexample\ Search}\\
&+
\mathrm{Sound\ Pruning}\\
&+
\mathrm{Invariant/Robustness\ Extraction}\\
&+
\mathrm{Certificate\ Generation}\\
&+
\mathrm{Reopenable\ Boundary}.
\end{aligned}
}
$$

Hybrid Ontological Computation 則為：

$$
\boxed{
\mathrm{HOC}_{\Gamma}
=
\operatorname{Compute}
\left(
\mathfrak O_{\Gamma}^{\mathrm{comp}}
\right),
}
$$

且：

$$
\boxed{
\mathfrak O_{\Gamma}^{\mathrm{comp}}
\neq
\mathbf W.
}
$$

---

# 29. 一句話版

> **FDCS 2.0 的平行剪枝不是用大量模擬把「高比例結果」升格為真理，而是在明示的 world/model boundary、constraints、legality、measure、history 與 resource contract 下，系統性展開 admissible causal possibilities，優先尋找反例，使用可證明安全的剪枝降低計算量，最後輸出帶 coverage、robustness、unresolved obligations、provenance 與 reopen conditions 的可重放證書。**

---

# 30. 結論

這份初版保留了舊 FDCS「從單點預測走向可能域計算」的核心直覺，但把它從過強的本體論宣言改造成一個可以被檢查、被反駁、被重新開啟的 causal computation framework。

最重要的修正可以壓成五句：

$$
\boxed{
\text{可能域}
\neq
\text{World totality}.
}
$$

$$
\boxed{
\text{高比例}
\neq
\text{本體必然}.
}
$$

$$
\boxed{
\text{平行計算}
\neq
\text{物理同步}.
}
$$

$$
\boxed{
\text{agent choice}
\neq
\text{固定百分比隨機}.
}
$$

$$
\boxed{
\text{沒有找到反例}
\neq
\text{反例不存在}.
}
$$

但舊稿最重要的問題意識仍可保留：對於參數、規則、背景與局部路徑高度可變的系統，科學問題不一定只能問成「唯一真值是多少」或「唯一未來會發生什麼」；另一種合法問題是：**在一個明示且可被挑戰的可能域內，哪些結構對變化保持穩健，哪些只在特定 region 成立，哪裡存在反例，以及我們還有多少 domain 沒有真正算到。**

因此新版核心不再是：

> 從實證驗證到本體必然。

而改為：

$$
\boxed{
\text{From point prediction to certified possibility analysis.}
}
$$

不是宣稱已算完所有可能，而是讓「我們到底算了哪些可能、漏了哪些、為何能剪、結論對什麼有效、何時必須重開」全部成為一級數學與 runtime 對象。

這才是 Parallel Pruning 與 Hybrid Ontological Computation 在 FDCS 2.0 中可以長期保留的正式位置。

---

# 附錄 A：核心符號

| 符號 | 含義 |
|---|---|
| $\mathbf W$ | MWT World primitive |
| $\Gamma$ | PPA/FDCS inquiry context |
| $\widetilde{\Omega}_{\Gamma}^{(v)}$ | candidate possibility domain |
| $\Omega_{\Gamma}^{(v)}$ | admissible possibility domain |
| $\mathbb B_{\Gamma}^{(v)}$ | parallel branch space |
| $\tau_{\Gamma}(e)$ | transition type |
| $C_0^{(\Gamma,\varepsilon_t)}$ | resolution-relative zero-lag judgment |
| $F_{\Gamma}^{(v)}$ | branch evaluation/evolution |
| $P$ | target property |
| $\operatorname{UInv}$ | domain-universal invariance |
| $\operatorname{Rob}_{\mu}$ | measure-relative robustness |
| $R^{-},R^{+}$ | unresolved-aware robustness bounds |
| $\pi_E$ | adaptive exploration policy |
| $\mathcal C_{\mathrm{prune}}$ | pruning certificate |
| $\mathcal C_P$ | property conclusion certificate |
| $\mathfrak O_{\Gamma}^{\mathrm{comp}}$ | computational ontology runtime object |
| $\mathrm{HOC}_{\Gamma}$ | hybrid ontological computation |

---

# 附錄 B：歷史概念處理原則

本稿把 2026-02 未發表舊稿視為 concept source，而非已發表先行版本。

因此：

- 不使用「修訂第二版」語言；
- 本文直接定為 v0.1 初版；
- 舊稿中未被驗證的數字不繼承為 empirical result；
- 舊稿中過強的 theorem 名稱不繼承 theorem status；
- 舊稿的 PPA、possible-space、hybrid-computation、computational-refutability、AI adaptive exploration 概念被保留並重新形式化；
- 舊稿中的政治案例不作本文 foundational evidence；
- 後續若需要，可另做 domain-specific application paper。

---

# 附錄 C：下一篇接口

推薦下一步：

## PPA 2.0 Reference Runtime v0.1

以目前 FDCS R0 為基礎新增：

1. possibility-domain registry；
2. finite exhaustive certificate；
3. uniform-grid explorer；
4. counterexample-directed explorer；
5. quotient-pruning certificate；
6. unresolved-aware robustness interval；
7. domain-version reopen；
8. surrogate/certificate separation。

這將使本文從 formal extension 進入 executable method。
