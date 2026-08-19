# GPC-CS Theorem Registry

**Series:** Generalized Phase Communication and Carrier Safety  
**Scope:** Papers 00–10  
**Version:** v1.0  
**Date:** 2026-08-14  

## 1. Registry policy

- `Formal core`：系列後續定理實際依賴的核心結果。
- `Formal supporting result`：支援核心結果、但不是主幹節點。
- `Classical theorem/corollary`：既有數學定理在 GPC-CS 語境下的直接使用或轉寫。
- `Counterexample`：用構造反例證明某種一般蘊含不成立。
- `Framework proposition`：系列的條件式結構主張，不冒充既有數學新定理。
- 每篇末尾 A/B/C… 的摘要命題另存為 `Summary Claims`，**不重複計入 theorem dependency nodes**。

## 2. Formal registry

| ID | Paper | Type | Name | Registry Role | Proof / Origin | Depends On | Downstream | Note |
|---|---|---|---|---|---|---|---|---|
| P00.C1 | P00 | Proposition | 訊息安全不足命題 | Framework foundational claim | Framework/conditional | P00 definitions | P01,P02 | 訊息本身安全不足以推出載體狀態安全。 |
| P00.C2 | P00 | Proposition | 序列閉包命題 | Framework foundational claim | Elementary set-theoretic | P00.C1 | P01.T5.1 | 安全更新集合若封閉，有限序列亦保持安全。 |
| P00.C3 | P00 | Proposition | 全域安全非局部性命題 | Framework foundational claim | Framework/counterexample-ready | P00.C1 | P01,P08,P09 | 局部安全不足以推出全域關係安全。 |
| P01.T4.1 | P01 | Theorem | 安全強度包含定理 | Formal core | Series-derived | P01 definitions | P01.T5.1,P04.T6.1 | 建立 universal / robust viable / viable / safe-set 的包含關係。 |
| P01.T5.1 | P01 | Theorem | 有限組合安全閉包定理 | Formal core | Elementary induction | P01.T4.1 | P04.T6.1,P04 switching | 逐算子保持安全域則任意有限組合保持。 |
| P01.P5.2 | P01 | Proposition | 單點安全不具組合性 | Counterexample | Constructive counterexample | P01 definitions | P04,P06 | 單點測試安全不能推出序列安全。 |
| P01.P8.1 | P01 | Proposition | 擾動裕度充分條件 | Formal supporting result | Metric-ball argument | P01 margin | P02.T19.1,P09 | 擾動小於安全裕度則單步仍安全。 |
| P01.P11.1 | P01 | Proposition | 局部安全不推出關係安全 | Counterexample | Constructive counterexample | P01 relational safety | P05,P08,P09 | 建立 relational safety 必要性。 |
| P02.T5.1 | P02 | Theorem | Fiber Factorization Criterion | Formal core | Standard factorization criterion, recontextualized | P02 observable family | P02.T7.1,P03.T6.1,P07.T6.1,P10.T5.1 | 可觀測量可經 T 因子化 iff 在 T-fibers 上常數。 |
| P02.C6.1 | P02 | Corollary | 非單射不必然語義有損 | Formal corollary | Derived | P02.T5.1 | P03 | non-injective 不等於 task-loss。 |
| P02.T7.1 | P02 | Theorem | 別名化不可恢復定理 | Formal core | Derived contradiction | P02.T5.1 | P03,P06 | 跨語義類 aliasing 使 final-signal-only exact decode 不可能。 |
| P02.T9.1 | P02 | Theorem | 本地重建資訊增益上界 | Formal core | Information-theoretic derivation | Data processing + chain rule | P06,P07 | 重建增加的資訊受 side information 條件互資訊限制。 |
| P02.P13.1 | P02 | Proposition | Exact Cycle Consistency 不推出語義保真 | Counterexample | Constructive counterexample | P02 definitions | P06,P07 | cycle consistency 與 semantic fidelity 分離。 |
| P02.P15.1 | P02 | Proposition | 語義保真與安全性不存在一般蘊含 | Counterexample pair | Constructive counterexamples | P01,P02 | P03,P05,P10 | fidelity 與 safety 為不同層。 |
| P02.T17.1 | P02 | Theorem | 轉導—重建誤差傳播界 | Formal core | Lipschitz composition | P02 Lipschitz assumptions | P03.T26.1,P05,P09 | 跨載體誤差如何進入狀態更新。 |
| P02.C19.1 | P02 | Corollary | 單步轉導錯配安全充分條件 | Formal corollary | Derived | P01.P8.1,P02.T17.1 | P03 | 將誤差上界接到安全裕度。 |
| P02.T20.1 | P02 | Theorem | 兩段轉導錯配界 | Formal supporting result | Triangle inequality + Lipschitz | P02 definitions | P09 | 多段 transduction error composition。 |
| P03.T6.1 | P03 | Theorem | 連續同步任務降維下界 | Formal core | Adapted from invariance of domain | P02.T5.1 + topology assumptions | P03 aliasing, P09 | 同步維度低於 task quotient 維度時連續精確單射不可能。 |
| P03.T10.1 | P03 | Theorem | 有限記憶上下文別名化定理 | Formal core | Pigeonhole principle | Finite memory model | P03.T12.1,P06 | M bits 不足以精確區分超過 2^M 個必要 context。 |
| P03.T12.1 | P03 | Theorem | 吞吐—記憶聯合辨識界 | Formal core | Counting bound | P03 finite channel/memory assumptions | P04,P09 | 通信率與記憶共同限制可辨識歷史數。 |
| P03.T18.1 | P03 | Theorem | 持續超載 backlog 發散定理 | Formal core | Telescoping lower bound | Queue-style recurrence | P08,P09 | 長期平均 arrival-service 正差使 backlog 至少線性發散。 |
| P03.C26.1 | P03 | Corollary | 容量—保真—安全單步充分條件 | Formal corollary | Derived | P01.P8.1,P02.T17.1,P03 capacity envelope | P09 | 容量誤差包絡與安全 margin 接合。 |
| P04.T6.1 | P04 | Theorem | 最大遞歸前向不變安全核 | Formal core | Set-theoretic invariance | P01.T4.1,P01.T5.1 | P04.T21.1,P09 | K_O(S) 是 S 中最大 O-forward-invariant 子集。 |
| P04.T8.1 | P04 | Theorem | Lipschitz 遞歸增益界 | Formal supporting result | Induction | P04 Lipschitz assumption | P04.T10.1,P09 | d(O^n x,O^n y) <= L^n d(x,y)。 |
| P04.T10.1 | P04 | Theorem | 安全 contraction corollary | Classical corollary | Banach contraction adapted | P04.T6.1 + Banach assumptions | P05.T11.1 | 閉安全集內 contraction 給出唯一安全固定點與收斂。 |
| P04.T12.1 | P04 | Theorem | 不安全極限的有限逃逸定理 | Formal supporting result | Closed-set limit argument | Closed safe set + convergence | P04.T13.1 | 若軌跡收斂到安全域外點，有限步必逃逸。 |
| P04.T13.1 | P04 | Theorem | 不安全吸引 basin 必然逃逸 | Formal core | Metric separation argument | P04.T12.1 + attractor separation | P05,P09 | 安全初態若落在不安全吸引 basin，有限時間逃逸。 |
| P04.T21.1 | P04 | Theorem | 共同收縮 Lyapunov 定理 | Formal core | Recursive Lyapunov decrease | P04 operator family | P05.T4.1,P09.T37.1 | 共同 Lyapunov decrease 保證任意切換收縮。 |
| P04.C22.1 | P04 | Corollary | Lyapunov sublevel 共同安全不變集 | Formal corollary | Derived | P04.T21.1 | P05,P09 | sublevel set 形成共同安全核心。 |
| P04.T29.1 | P04 | Theorem | 順序安全裕度定理 | Formal core | Metric-ball margin argument | P01 margin + order defect | P06 | 非交換順序差小於安全裕度則換序仍安全。 |
| P05.T4.1 | P05 | Theorem | 二載體 small-gain 收縮定理 | Formal core | 2x2 spectral calculation | P04.T21.1 + cross-gain model | P09 | gamma_AB gamma_BA < (1-a_A)(1-a_B) => rho(M)<1。 |
| P05.T11.1 | P05 | Theorem | 聯合 contraction 安全定理 | Classical corollary | Banach contraction adapted | P01 relational safety,P04.T10.1 | P09.T37.1 | 雙載體閉安全域內 contraction 給出唯一安全聯合固定點。 |
| P05.T14.1 | P05 | Theorem | Generalized Synchronization Manifold Invariance | Formal core | Direct invariance argument | P05 manifold definition | P07,P09 | 同步關係 h 的相容條件保證流形不變。 |
| P06.T3.1 | P06 | Theorem | Exact Recovery iff Injective | Formal core | Elementary left-inverse theorem | P06 update map | P06.T6.1,P06.T8.1,P07 | final-state-only exact recovery iff 更新映射在域上單射。 |
| P06.C4.1 | P06 | Corollary | 非單射更新不可由 final state 精確恢復 | Formal corollary | Derived | P06.T3.1 | P07 | state merging 導致 exact recovery 不可能。 |
| P06.T6.1 | P06 | Theorem | Compact-to-Hausdorff Continuous Recovery | Classical topology | Compact-to-Hausdorff homeomorphism theorem | P06.T3.1 + topology assumptions | P10 | 連續單射在 compact/Hausdorff 條件下具有連續 inverse。 |
| P06.T8.1 | P06 | Theorem | 資訊論 Exact Recovery 判準 | Formal core | Discrete entropy criterion | P06.T3.1 | P07 | exact recovery from Y iff H(X|Y)=0（離散設定）。 |
| P06.P11.1 | P06 | Proposition | Delete–Restore Separation | Framework proposition | State-space separation | P06 update/delete definitions | P07,P10 | 刪除輸入記錄不等於狀態 inverse。 |
| P06.T17.1 | P06 | Theorem | History Inversion Order | Formal core | Composition inverse law | P04 order sensitivity | P06.T23.1 | 歷史逆轉必須按逆序執行 inverse operators。 |
| P06.T23.1 | P06 | Theorem | Hidden-History Non-Markov 定理 | Formal core | Contradiction | P06 hidden state model | P07,P10 | 同可見狀態若因 hidden history 導致不同下一狀態，visible state 非充分 Markov state。 |
| P07.T3.1 | P07 | Theorem | 淨漂移不超過累積路徑變差 | Formal supporting result | Triangle inequality | P07 identity-related metric | P07 path dependence | D_I(0,T) <= V_I(0,T)。 |
| P07.T6.1 | P07 | Theorem | Observable-Profile Non-Identification | Formal core | Non-injectivity argument | P07 observable map Psi | P10.T5.1 | 若 Psi 非單射，profile equality 不推出 full-state identity。 |
| P07.T9.1 | P07 | Theorem | 閾值連續關係非傳遞定理 | Formal core | Constructive metric counterexample | P07 metric threshold | P07.T16.1 | epsilon-neighborhood similarity 一般不是等價關係。 |
| P07.T16.1 | P07 | Theorem | Branching Insufficiency Theorem | Formal core | Classical identity contradiction | P07 continuity criterion | P10 | 允許分支的 continuity criterion 不能無條件充分推出 classical identity。 |
| P08.T3.1 | P08 | Theorem | 失效總數方差分解定理 | Formal core | Variance decomposition | P08 Bernoulli failures | P08.T6.1,P09 | Var(K) 包含 individual variance 與 pairwise covariance。 |
| P08.T6.1 | P08 | Theorem | 相關冗餘底限定理 | Formal core | Derived algebra | P08.T3.1 + equicorrelation model | P09 | rho>0 時平均失效比例方差有非零 floor。 |
| P08.T14.1 | P08 | Theorem | Common-Cause Floor 定理 | Formal core | Total probability | P08 mixture model | P09 | 系統失效概率至少為 common-cause probability q。 |
| P08.P18.1 | P08 | Proposition | 結構異質不推出失效獨立 | Counterexample | Shared dependency counterexample | P08 heterogeneity definitions | P09 | 高度異質仍可因共同必要依賴完全相關失效。 |
| P08.P32.1 | P08 | Proposition | Pairwise Independent 不推出 Jointly Independent | Counterexample | XOR construction | P08 probability model | P09,P10 | 二階統計不足以刻畫高階群體尾風險。 |
| P08.T37.1 | P08 | Theorem | 較低 pairwise covariance 降低總失效數方差 | Formal supporting result | Direct from P08.T3.1 | Equal marginals | P09 | 二階韌性比較定理。 |
| P08.T53.1 | P08 | Theorem | Common Update Homogenization | Formal core | Contraction iteration | P04.T8.1 | P09 | 共同 contraction update 使 pairwise heterogeneity 指數下降。 |
| P09.T7.1 | P09 | Theorem | 路徑增益展開定理 | Formal core | Matrix-power walk expansion | P09 gain matrix | P09.T10.1 | (G^k)_ij 等於所有長度 k walks 的增益總和。 |
| P09.T10.1 | P09 | Theorem | 總網路敏感度 Neumann 定理 | Formal core | Matrix Neumann series | P09.T7.1 + rho(G)<1 | P09.T16.1,P10 | T_G=(I-G)^-1。 |
| P09.T15.1 | P09 | Theorem | 無擾動安全盒定理 | Formal core | Monotone comparison induction | P09 gain model | P09.T16.1 | G mu <= lambda mu 建立前向不變 deviation box。 |
| P09.T16.1 | P09 | Theorem | 含擾動安全盒定理 | Formal core | Monotone comparison | P09.T15.1 | P09.T37.1,P10.T29.1 | G mu + eta <= mu 建立 robust safety box。 |
| P09.T32.1 | P09 | Theorem | 有限 Cascade Closure 定理 | Formal core | Finite monotone set iteration | P08 common-mode seed + P09 cascade map | P10.T35.1 | 有限節點 monotone cascade 有最小 fixed-point closure。 |
| P09.T37.1 | P09 | Theorem | 共通安全包絡定理 | Formal core | Uniform invariant-box argument | P04.T21.1,P05.T11.1,P09.T16.1 | P10.T29.1 | 對所有 mode 的共同 envelope 保證任意 state-dependent switching 不越界。 |
| P10.T5.1 | P10 | Theorem | Property Observability Fiber Theorem | Formal core | Factorization criterion | P02.T5.1,P07.T6.1 | P10.T35.1 | property 可由 observation 完全辨識 iff 在 observation fibers 上常數。 |
| P10.C8.1 | P10 | Corollary | Observation-Only Safety Impossibility | Formal corollary | Derived | P10.T5.1 | P10 verification boundary | 安全歧義 fiber 存在時無 observation-only exact safety classifier。 |
| P10.T14.1 | P10 | Theorem | Kalman Rank Criterion | Classical theorem | Classical observability theorem | LTI assumptions | P10.T29.1 | rank(O_n)=n iff 初態可由 n 步無雜訊輸出唯一辨識。 |
| P10.T29.1 | P10 | Theorem | Robust Verification Transfer Theorem | Formal core | Lipschitz margin argument | P01 safety margin,P09.T37.1 | Runtime transfer | L_h epsilon < model margin 則部署狀態仍安全。 |
| P10.T35.1 | P10 | Theorem | Finite-Test Non-Universality Theorem | Formal core | No-free-lunch counterconstruction | Finite proper test subset | P10.T38.1,P10.T42.1 | 有限成功測試在無額外結構時不證明 universal safety。 |
| P10.T38.1 | P10 | Theorem | Falsification Asymmetry Theorem | Formal core | Quantifier logic + P10.T35.1 | P10.T35.1 | Series closure | 一個反例足以推翻全稱命題；未找到反例不等於證明。 |
| P10.T42.1 | P10 | Theorem | Zero-Failure Confidence Bound | Statistical theorem | Exact binomial one-sided bound | iid Bernoulli testing | Series closure | 零失敗樣本只給 p <= 1-delta^(1/n)，不給 p=0。 |

## 3. Series theorem spine

### Safe-set spine

$P00.C1 \rightarrow P01.T4.1 \rightarrow P01.T5.1 \rightarrow P04.T6.1 \rightarrow P04.T21.1 \rightarrow P05.T4.1 \rightarrow P09.T37.1 \rightarrow P10.T29.1$

### Transduction / observability spine

$P02.T5.1 \rightarrow P02.T7.1 \rightarrow P07.T6.1 \rightarrow P10.T5.1$

### Recoverability / continuity spine

$P06.T3.1 \rightarrow P06.T17.1 \rightarrow P07.T16.1 \rightarrow P10.T5.1$

### Common-mode / cascade spine

$P08.T3.1 \rightarrow P08.T6.1 \rightarrow P09.T32.1 \rightarrow P10.T35.1 \rightarrow P10.T38.1$

## 4. Formalization priority

若之後進 Lean / Coq，建議優先順序：

1. P01.T4.1 / P01.T5.1 — 集合與不變性地基。
2. P02.T5.1 / P02.T7.1 — fiber / factorization。
3. P04.T6.1 / P04.T21.1 — 遞歸安全核與共同 Lyapunov。
4. P06.T3.1 / P06.T17.1 — 可恢復性與歷史逆序。
5. P08.T3.1 / P08.T6.1 — 相關失效統計。
6. P09.T7.1 / P09.T16.1 / P09.T32.1 — 網路傳播與 cascade closure。
7. P10.T5.1 / P10.T29.1 / P10.T35.1 / P10.T38.1 — 可觀測與驗證收束。

## 5. Status

**Core theorem registry complete for Foundation Cycle Papers 00–10.**