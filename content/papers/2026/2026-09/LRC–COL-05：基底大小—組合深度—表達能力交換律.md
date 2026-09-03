# LRC–COL-05：基底大小—組合深度—表達能力交換律
## The Tradeoff Law of Basis Size, Composition Depth, and Expressive Capacity

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

LRC–COL-03 與 LRC–COL-04 分別建立了複合符號算子語言的有效下界與有效上界：operator 太少，目標域覆蓋不足、組合深度過高；operator 太多，則出現 selection entropy、semantic collision、context cost、version burden 與 active-set overload。兩篇合起來得到一個靜態有效區間：

$$
N_{\min}^{effective}
\le
N
\le
N_{\max}^{effective}.
$$

但這仍沒有回答真正的語言設計核心：

> **在這個區間內，多增加一個 operator，到底可以換回多少 composition depth、多少語義保真、多少學習成本、多少執行效率與多少 action yield？**

本文提出 **Basis–Depth–Expressivity Tradeoff（基底—深度—表達能力交換律）**，把 operator 數量 $N$ 、組合深度 $d$ 、operator 粒度 $g$ 、有效表達容量 $C_{eff}$ 、語義保真 $F_{sem}$ 、學習成本 $C_{learn}$ 、選擇成本 $C_{sel}$ 與 Language Action Yield $Y_L$ 放入同一聯合模型。

本文首先指出：在最粗略的無型別近似中，若一個語言有 $N$ 個 operator、最大組合深度 $d$，可生成的 syntactic structures 數量通常會隨 $N$ 與 $d$ 超線性甚至指數級成長；因此較大的 $N$ 可以用較淺的 $d$ 達到相似表達覆蓋。但 syntactic capacity 不等於 effective semantic capacity。大量 expression 可能非法、同義、不可學、不可穩定執行，故真正有效容量必須乘上 validity、semantic distinctness、learnability 與 fidelity 修正。

本文提出一個粗略但有用的容量關係：

$$
\boxed{
C_{eff}(N,d,g)
=
C_{syn}(N,d,g)
\cdot
p_{valid}
\cdot
p_{distinct}
\cdot
p_{learn}
\cdot
p_{faithful}.
}
$$

並進一步提出一個候選交換約束：若目標域中至少有 $M_{eff}$ 個必須可區分的有效行為，而每個 operator 在平均深度上提供約 $\log N$ 的選擇資訊，則在簡化條件下可能存在：

$$
\boxed{
d\log N
\gtrsim
\log M_{eff},
}
$$

或：

$$
\boxed{
N
\gtrsim
M_{eff}^{1/d}.
}
$$

這不是普遍定理，而是第一版「基底變大可以換深度下降」的資訊容量近似。

本文另外建立 **Depth Fidelity Law**：若每一層 composition 的平均條件保真率為 $q<1$，最簡獨立近似下：

$$
F_{comp}(d)
\approx
q^d.
$$

因此，對目標保真門檻 $\tau_F$，存在：

$$
\boxed{
d_{\max}^{F}
=
\frac{\ln\tau_F}{\ln q}.
}
$$

這使 macro operator、crystallized operator 與 higher-granularity operator 的價值可以第一次用「省下幾層 composition 所換回的 fidelity」來衡量，而不只看 token 壓縮。

本文最終將最佳語言設計寫成：

$$
\boxed{
(N^*,d^*,g^*)
=
\arg\max
J(N,d,g)
}
$$

subject to coverage、fidelity、learning、selection、risk 與 active-set constraints。本文主張未來 AI-native composite language 的真正設計對象不是「最小字典」或「最多 operator」，而是一個 **Basis–Depth–Granularity Pareto Surface**。

---

## 關鍵詞

operator basis；composition depth；expressivity；granularity；semantic fidelity；compositional generalization；macro operator；RISC/CISC；Pareto frontier；AI-native language

---

# 1. 上下界之間真正缺的東西

前兩篇已經得到：

$$
N_{\min}^{effective}
$$

與：

$$
N_{\max}^{effective}.
$$

但假設：

$$
N_{\min}=20,
\qquad
N_{\max}=200.
$$

那麼到底：

- 30 好？
- 60 好？
- 100 好？
- 150 好？

仍然不知道。

因為：

$$
\boxed{
N
}
$$

本身不是效用。

真正要看：

$$
\boxed{
N
\rightarrow
d
\rightarrow
F_{sem}
\rightarrow
C_{learn}
\rightarrow
C_{exec}
\rightarrow
Y_L.
}
$$

---

# 2. 第一條基本交換律

直覺上：

$$
N\downarrow
\Rightarrow
d\uparrow.
$$

因為 primitive 少，高階能力需要更多層 composition。

反之：

$$
N\uparrow
\Rightarrow
d\downarrow.
$$

因為更多中階／高階 operator 可以直接承載常見子程序。

因此：

$$
\boxed{
N
\leftrightarrow
d.
}
$$

但這不是嚴格線性，真正關係更像：

$$
\boxed{
d
=
f(
N,
G,
g,
\Omega,
A
).
}
$$

---

# 3. Workload Distribution

令 $\Omega$ 是目標域，實際 workload 由：

$$
\mu(\omega)
$$

決定。

因此最重要的不是單一 worst-case expression depth，而可能是：

$$
\boxed{
\bar d_{\mathcal O}
=
\mathbb E_{\omega\sim\mu}
[
D_{\mathcal O}(\omega)
].
}
$$

其中 $D_{\mathcal O}(\omega)$ 是使用 basis $\mathcal O$ 表達任務 $\omega$ 所需的最小有效深度。

高風險系統仍需另外追蹤：

$$
\boxed{
d_{worst}
=
\sup_{\omega\in\Omega_{critical}}
D_{\mathcal O}(\omega).
}
$$

---

# 4. Expression Length 與 Depth 不同

兩個 expression 可能一個長但平衡、另一個短但串行。

所以：

$$
\boxed{
L_e
\neq
d_e.
}
$$

對 AI 而言，composition depth 會影響：

- intermediate state；
- dependency chain；
- error propagation；
- context maintenance；
- tool sequencing；
- branch recovery。

因此：

$$
\boxed{
\text{same expression length}
\neq
\text{same cognitive difficulty}.
}
$$

---

# 5. Syntactic Capacity

最粗略地，若有 $N$ 個一元 operators、深度最多 $d$，sequence 數量約：

$$
\sum_{k=1}^{d}N^k.
$$

若 $N>1$：

$$
\boxed{
C_{syn}
\sim
O(N^d).
}
$$

若 operators 有多種 arity，expression tree 數量還會再乘上 tree-structure 的組合，因此 syntactic capacity 可能增長得更快。

---

# 6. Syntax Capacity 極度高估真正能力

很多 combination：

- type-invalid；
- semantic-equivalent；
- Agent 學不會；
- execution 不穩定。

所以通常：

$$
\boxed{
C_{syn}
\gg
C_{eff}.
}
$$

本文提出：

$$
\boxed{
C_{eff}
=
C_{syn}
\cdot
p_{valid}
\cdot
p_{distinct}
\cdot
p_{learn}
\cdot
p_{faithful}.
}
$$

因此：

$$
\boxed{
Expressivity
=
f(
N,d,g,G,T,A
).
}
$$

只說「這套語言有 100 個 operator」幾乎沒有足夠資訊。

---

# 7. 第一版容量下界近似

假設目標域中至少有 $M_{eff}$ 個必須可區分的 target behaviors。

若每層大約提供 $\log N$ 的 operator identity information，簡化地：

$$
\boxed{
d\log N
\gtrsim
\log M_{eff}.
}
$$

因此：

$$
\boxed{
N
\gtrsim
M_{eff}^{1/d}.
}
$$

這不是普遍定理，因為 type system、arity、parameters、recursion 與 memory 都可以改變容量。本文只把它稱為：

$$
\boxed{
\text{Basis–Depth Capacity Heuristic}.
}
$$

它真正告訴我們的是：

> **越要求少步完成，越需要更多語義被預先結晶進 operator。**

---

# 8. Operator Granularity

引入第三個核心量：

$$
\boxed{
g(O).
}
$$

表示 operator 承載的語義／行動粒度。

最簡化可以：

$$
\boxed{
g(O)
=
L_0(
Expand(O)
),
}
$$

即該 operator 展開成最低階 primitives 後，大約相當於多少 primitive operations。

整套 basis 的 usage-weighted 平均 granularity：

$$
\boxed{
\bar g
=
\mathbb E_{O\sim usage}
[
g(O)
].
}
$$

通常 $\bar g\uparrow$ 會讓 $d\downarrow$，但 operator 越粗也會增加 semantic contract、internal branch、parameter schema 與 applicability cost。

因此：

$$
\boxed{
g\uparrow
\not\Rightarrow
Y_L\uparrow.
}
$$

---

# 9. 太細 vs 太粗

## Too Fine

- $N$ 小；
- $d$ 大；
- repeated composition；
- error accumulation。

## Too Coarse

- macro 數量增長；
- overlap；
- poor reuse；
- God Operator risk。

因此存在：

$$
\boxed{
g^*.
}
$$

真正要找的是：

$$
\boxed{
(N^*,d^*,g^*).
}
$$

---

# 10. Depth Fidelity Law

假設每一層 composition $C_i$ 在上游正確的條件下，平均保持語義正確的機率為 $q_i$。

若簡化為：

$$
q_i=q,
$$

且近似獨立，則：

$$
\boxed{
F_{comp}(d)
\approx
q^d.
}
$$

例如：

$$
0.99^{10}\approx0.904,
$$

而：

$$
0.98^{20}\approx0.668.
$$

所以「每一步只錯一點」在深鏈上仍可能累積成顯著風險。

---

# 11. Fidelity-Constrained Depth Ceiling

若最低要求：

$$
F_{comp}\ge\tau_F,
$$

則：

$$
q^d\ge\tau_F.
$$

因此：

$$
\boxed{
d
\le
d_{\max}^{F}
=
\frac{\ln\tau_F}{\ln q}.
}
$$

這代表：

> **再小的 formal basis，也不能假設可以任意深地展開。**

如果 per-step fidelity 有限，composition depth 就存在實際 reliability ceiling。

---

# 12. Heterogeneous Fidelity 與 Correlated Error

若不同 operator fidelity 不同：

$$
\boxed{
F_{comp}
\approx
\prod_{i=1}^{d}q_i.
}
$$

低 fidelity operator 會形成 chain bottleneck。

但實際 error 不一定獨立；早期 interpretation error 可能改變後續所有 branch，因此 $q^d$ 只是一階 baseline。

可定義：

$$
\boxed{
A_d
=
\frac{
ObservedFailure(d)
}{
1-q^d
}.
}
$$

如果 $A_d>1$，代表存在 nonlinear amplification。

---

# 13. Macro 可以換回 Fidelity

假設 macro $O_M$ 把原本 $k$ 層 composition 壓成 1 層。

若 macro fidelity：

$$
q_M
$$

高於：

$$
q^k,
$$

則：

$$
\boxed{
\Delta F_M
=
q_M-q^k
>0.
}
$$

所以 macro 的收益至少包含：

$$
\boxed{
\Delta Token
+
\Delta Depth
+
\Delta Fidelity
+
\Delta Latency.
}
$$

不是只有文字縮短。

如果 $q_M<q^k$，則 macro 雖然更短，卻變成語義黑箱：

$$
\boxed{
\text{Depth Compression}
\neq
\text{Reliability Gain}.
}
$$

---

# 14. Macro Admission Gate

對 recurring motif $m$，由 $k_m$ 個 low-level operations 組成。

第一版 macro gain：

$$
\boxed{
Gain_m
=
f_m
[
\alpha(k_m-1)
+
\beta\Delta F_m
+
\gamma\Delta Y_m
+
\eta\Delta L_m
].
}
$$

其中：

- $f_m$：workload frequency；
- $(k_m-1)$：省下的 depth；
- $\Delta F_m$：fidelity gain；
- $\Delta Y_m$：action-yield gain；
- $\Delta L_m$：語言／token 壓縮。

成本：

$$
\boxed{
Cost_m
=
C_{define}
+
C_{learn}
+
C_{select}
+
C_{version}
+
C_{collision}.
}
$$

只有：

$$
\boxed{
Gain_m>Cost_m
}
$$

才適合進 stable macro layer。

---

# 15. Frequency–Depth Exchange

這讓前篇的「高頻結晶、低頻組合」得到更清楚的形式。

若 $f_m$ 高，depth saving 被反覆享受：

$$
Gain\propto f_m.
$$

相反，一個只用一次的 macro 還要被定義、命名、學習與治理，通常不值得永久加入 global language。

因此可分：

### Stable Operator
長期高頻，進 global language。

### Local Macro
domain / project 內使用。

### Ephemeral Macro
session 生成，用完可消失。

---

# 16. Basis Size 也會增加 Selection Cost

LRC–COL-04 已定義 selection entropy：

$$
H_{sel}.
$$

粗略可寫：

$$
\boxed{
C_{sel}
\propto
H_{sel}.
}
$$

若候選近似均勻：

$$
p_i=\frac1{N_A},
$$

則：

$$
H_{sel}=\log N_A.
$$

真實情況中還要加入 semantic collision：

$$
C_{sel}
=
f(
N_A,
H_{sel},
\rho_{col}
).
$$

因此新增 macro 是在用：

$$
\boxed{
\Delta C_{sel}
\leftrightarrow
-\Delta d
}
$$

交換 selection complexity 與 composition depth。

---

# 17. RISC / CISC 類比

CPU instruction-set 設計長期存在類似取捨：

- 少而簡單的 instructions；
- 多而複雜的 instructions；
- code density；
- decode complexity；
- execution efficiency。

現代 CPU 甚至會把複雜 instruction 內部分解成較簡單 micro-ops。

這不是證明 COL 一定等同 CPU ISA，但提供重要工程類比：

$$
\boxed{
\text{rich surface instruction}
\rightarrow
\text{simpler internal primitives}.
}
$$

---

# 18. COL 可能是雙層 ISA

未來可以：

$$
\boxed{
\text{Surface Operators}
\rightarrow
\text{Canonical Micro-Operators}.
}
$$

表面層：

- 對人／AI 易用；
- 粒度較高。

kernel 層：

- basis 小；
- semantics 穩定；
- runtime 可驗證。

因此：

$$
\boxed{
\mathcal O_{surface}
\xrightarrow{Compile}
\mathcal O_{kernel}^{*}.
}
$$

而：

$$
N_S>N_K
$$

完全合理。

---

# 19. Compiler Fidelity

雙層設計把新風險移到：

$$
\boxed{
F_{compile}.
}
$$

總 fidelity：

$$
\boxed{
F_{total}
=
F_{parse}
F_{compile}
F_{execute}.
}
$$

因此 surface vocabulary 雖然好用，仍必須能穩定編譯回 kernel semantics。

---

# 20. Surface Depth 與 Kernel Depth

表面：

$$
d_S
$$

可能很小。

kernel 展開：

$$
d_K
$$

可能很大。

因此：

$$
\boxed{
d_S
\neq
d_K.
}
$$

兩者都重要。

 $d_S$ 影響 planning、readability、composition burden； $d_K$ 影響 runtime、latency、verification 與 low-level error。

可以先用：

$$
\boxed{
d_{eff}
=
\alpha d_S
+
\beta d_K
+
\gamma d_{tool}.
}
$$

作為候選有效深度。

---

# 21. Expression Depth 不等於 Transformer Depth

本文的 $d$ 是 operator expression 的組合深度，不是 Transformer layer depth。

但外部研究提供一個有用提醒：NAACL 2024 在控制總參數量後發現 deeper transformers 的 compositional generalization 通常較好，但額外 depth 的收益快速遞減。

這不能推出 operator expression 越深越好；它反而提醒：

$$
\boxed{
\text{depth capacity and depth burden must be distinguished}.
}
$$

---

# 22. Compositional Complexity 的實證邊界

NAACL 2025 的 morphology compositionality 研究顯示，LLM 在 novel roots 與更高 morphological complexity 下表現明顯下降。

ACL Findings 2024 的 grounded compositionality 工作則發現，模型對 unseen sequence lengths 與 novel combinations of seen base components 仍有困難。

因此：

$$
\boxed{
\text{known primitives}
+
\text{known semantics}
\not\Rightarrow
\text{arbitrary depth generalization}.
}
$$

---

# 23. Training Envelope 與 Depth Extrapolation

令：

$$
d_{train}
$$

是 training / exposure 中常見最大深度。

測試：

$$
d_{test}>d_{train}
$$

就是：

$$
\boxed{
\text{depth extrapolation}.
}
$$

可定義：

$$
\boxed{
G_d
=
Performance(d).
}
$$

並找：

$$
\boxed{
d_{crit}
=
\min
\{
d:
Performance(d)<\tau_P
\}.
}
$$

這就是某 Agent 在某 basis 下的實際 depth ceiling。

---

# 24. Depth Rescue

如果新增 macro 後，某 task：

$$
D_{\mathcal O}(\omega)>d_{crit}
$$

變成：

$$
D_{\mathcal O'}(\omega)\le d_{crit},
$$

則新增 operator 把原本超過 Agent compositional horizon 的任務壓回可用區。

本文稱：

$$
\boxed{
\text{Depth Rescue}.
}
$$

這種情況可能造成 basis utility 的離散跳升。

---

# 25. Utility 可能出現 Phase Transition

macro 跨過 $d_{crit}$ 時：

$$
J(N)
$$

可能突然上升。

反過來，新增相似 operators 使 $\rho_{col}$ 跨過 selection threshold，也可能突然下降。

因此：

$$
\boxed{
J(N)
}
$$

可能：

- 非平滑；
- 有多個局部 optimum；
- 出現 phase-transition-like behavior。

---

# 26. Pareto Surface

因此最合理結果不是：

> 最佳 N = 57。

而是：

$$
\boxed{
\mathcal P
=
Pareto(
N,
d,
g,
F_{sem},
C_{learn},
C_{sel},
Y_L
).
}
$$

---

# 27. Workload-Specific Optimum

對 workload $\mu_1$：

$$
(N_1^*,d_1^*,g_1^*).
$$

對 $\mu_2$：

$$
(N_2^*,d_2^*,g_2^*).
$$

可能完全不同。

因此：

$$
\boxed{
\text{No workload-free optimum}.
}
$$

---

# 28. Motif Distribution 比 Task Identity 更重要

令 $m$ 是 recurrent compositional motif，分布：

$$
p(m).
$$

macro crystallization 應主要依 recurring motif，而不是 task 名稱。

可建立：

$$
\boxed{
\min
\mathbb E_{\omega}
[
Depth(\omega\mid\mathcal M)
]
+
\lambda|\mathcal M|
+
\mu C_{sel}(\mathcal M).
}
$$

這已經接近一個真正可實作的 macro-selection objective。

---

# 29. Dictionary Learning 類比

這和：

- dictionary learning；
- byte-pair merge；
- macro compression；

有結構相似處。

都是在找：

> 哪些 recurring units 值得升格成可重用單位？

但 COL 還多：

- semantics；
- action；
- type；
- risk。

所以不能只按 frequency merge。

---

# 30. Operator Granularity 需要 Domain / Risk Conditioning

例如：

### File System
`move_file`

可能是合適粒度。

### Deployment
`release_production`

可能太粗，因為包含：

- tests；
- approvals；
- rollback；
- migration。

所以：

$$
\boxed{
g^*
=
g^*(Domain,Risk).
}
$$

高風險 domain 可能傾向更細粒度，以提高 verification 與 rollback；高頻低風險 domain 則可能適合較粗 macro。

---

# 31. Semantic Depth vs Action Depth

如果 expression 最後只生成文字，depth error 主要是 semantic。

如果每層都直接 action：

$$
O_1\rightarrow W_1\rightarrow O_2\rightarrow W_2,
$$

錯誤會立刻進世界。

因此區分：

$$
d_s
$$

語義 composition depth，

與：

$$
d_a
$$

外部 action chain depth。

可以：

$$
\boxed{
d_{risk}
=
\alpha d_s+\beta d_a,
\qquad
\beta>\alpha
}
$$

用於高實體風險 domain。

---

# 32. Verification 可以換更深的 d

如果每隔 $k$ 層插入：

$$
Verify,
$$

可以阻止 error 長鏈無限制累積。

所以：

$$
\boxed{
\text{verification can buy compositional depth}.
}
$$

這意味著真正交換關係已經擴展成：

$$
\boxed{
N
\leftrightarrow
d
\leftrightarrow
g
\leftrightarrow
v
}
$$

其中 $v$ 是 verification density。

---

# 33. 深本身不是絕對壞

真正高風險的是：

- 無檢查深鏈；
- high-coupling 深鏈；
- low-fidelity 深鏈。

因此：

$$
\boxed{
\text{Depth Cost}
=
f(
Fidelity,
Verification,
Reversibility,
Coupling
).
}
$$

sandbox / simulation / rollback 都會改變可接受的 depth。

---

# 34. 總成本模型

對 workload $\mu$：

$$
\boxed{
C_{total}
=
C_{basis}
+
C_{learn}
+
C_{select}
+
C_{compose}
+
C_{verify}
+
C_{execute}
+
C_{risk}.
}
$$

通常：

$$
N\uparrow
\Rightarrow
C_{basis}\uparrow,
$$

$$
N\uparrow
\Rightarrow
C_{select}\uparrow,
$$

但：

$$
N\uparrow
\Rightarrow
C_{compose}\downarrow.
$$

自然會出現中間 optimum。

---

# 35. 聯合最佳化

因此真正最佳設計：

$$
\boxed{
(N^*,d^*,g^*,v^*)
=
\arg\min
C_{total}
}
$$

subject to：

$$
Coverage\ge\tau_C,
$$

$$
Fidelity\ge\tau_F,
$$

$$
Y_L\ge\tau_Y,
$$

$$
Risk\le R_{max}.
$$

---

# 36. Basis 必須和 Runtime 一起設計

形式最小只問 $N$。

工程語言需要：

$$
\boxed{
N+d+g+v+runtime.
}
$$

完整系統：

$$
\boxed{
Operator Library
\rightarrow
Retriever
\rightarrow
Composer
\rightarrow
Compiler
\rightarrow
Verifier
\rightarrow
Executor.
}
$$

basis optimum 取決於整條鏈。

---

# 37. 本篇十二個正式命題

## BD-P1 — Basis–Depth Tradeoff
在固定 coverage 與 granularity family 下， $N\downarrow\Rightarrow d\uparrow$ 通常成立。

## BD-P2 — Effective Capacity Correction
syntactic capacity 必須經 validity、distinctness、learnability、fidelity 修正。

## BD-P3 — Fidelity-Constrained Depth
若 per-step fidelity $q<1$，存在有限 $d_{\max}^{F}$。

## BD-P4 — Macro Depth Rescue
適當 macro 可以把原本超過 Agent depth horizon 的 task 壓回可用區。

## BD-P5 — Macro Selection Cost
macro 增加會降低 depth，但提高 selection complexity。

## BD-P6 — Optimal Granularity
存在 domain-conditioned $g^*$。

## BD-P7 — Dual-Level Basis
surface operator basis 與 kernel micro-operator basis 可以不同。

## BD-P8 — Frequency-Weighted Crystallization
高頻 recurrent motifs 更值得永久 macro 化。

## BD-P9 — Long-Tail Composition
低頻 long-tail 更適合由 shared basis 動態組合或 ephemeral macro 處理。

## BD-P10 — Verification Buys Depth
verification density 上升可以提高可安全支持的有效 composition depth。

## BD-P11 — Workload-Conditioned Optimum
不存在脫離 workload distribution 的 universal $(N^*,d^*,g^*)$。

## BD-P12 — Phase-Transition Utility
basis expansion、collision 與 depth rescue 可能讓效用曲線出現非平滑 phase transition。

---

# 38. 第一版實驗設計

固定 target workload：

$$
\Omega_0.
$$

建立數個 basis：

$$
N=
8,16,32,64,128.
$$

對每個 basis：

1. 自動找最短 composition；
2. 測平均 depth；
3. 測 max depth；
4. 測 novel composition；
5. 測 fidelity；
6. 測 selection；
7. 測 latency；
8. 測 action yield。

---

# 39. Macro Sweep

固定 primitive kernel。

逐步加入 top-frequency motifs：

$$
M=0,5,10,20,40.
$$

測：

$$
\bar d(M),
$$

$$
F_{sem}(M),
$$

$$
C_{sel}(M),
$$

$$
Y_L(M).
$$

找：

$$
M^*.
$$

---

# 40. Depth Extrapolation Test

training：

$$
d\le d_{train}.
$$

testing：

$$
d=d_{train}+1,\ldots,d_{train}+k.
$$

找：

$$
d_{crit}.
$$

這會直接告訴我們：

> 什麼時候需要 macro rescue。

---

# 41. Granularity Sweep

同一功能設三種版本：

### Fine
小 operators。

### Medium
中粒度。

### Coarse
macro-heavy。

比較：

- learning；
- selection；
- execution；
- transfer；
- fidelity。

---

# 42. Verification Sweep

同一 composition depth $d$，設 verification 每：

$$
1,2,4,8,\infty
$$

層一次。

測：

- fidelity；
- latency；
- total yield。

找：

$$
v^*.
$$

---

# 43. 期望得到的不是單一最佳點

不同 risk / workload 下：

$$
(N^*,d^*,g^*,v^*)
$$

不同。

真正產物應是一張 Policy Map，例如：

```text
Low-risk repetitive
→ coarser macros

High-risk irreversible
→ finer operators + dense verification

High-entropy long-tail
→ small core + dynamic composition

High-frequency stable
→ crystallize recurring motifs
```

---

# 44. 靜態交換律的最後形式

本篇把靜態語言設計壓成：

$$
\boxed{
\mathcal T_S:
(N,d,g,v)
\mapsto
(
Coverage,
Fidelity,
Learning,
Selection,
Yield,
Risk
).
}
$$

這就是：

$$
\boxed{
\text{Static Basis–Depth Tradeoff Surface}.
}
$$

---

# 45. 與下一篇的接口

目前假設：

- workload 固定；
- Agent 固定；
- basis 固定；
- macro frequency 固定。

實際系統中：

- AI 會學；
- workload 會變；
- macros 會結晶；
- operators 會 retire；
- Agent capacity 會升級。

因此：

$$
(N^*,d^*,g^*)
$$

會隨時間變。

下一篇就正式把：

$$
\boxed{
\mathcal T_S
}
$$

變成：

$$
\boxed{
\mathcal T_D(t).
}
$$

---

# 46. 本篇核心公式組

有效容量：

$$
\boxed{
C_{eff}
=
C_{syn}
p_{valid}
p_{distinct}
p_{learn}
p_{faithful}.
}
$$

容量近似：

$$
\boxed{
d\log N
\gtrsim
\log M_{eff}.
}
$$

深度 fidelity：

$$
\boxed{
F_{comp}(d)\approx q^d.
}
$$

fidelity depth ceiling：

$$
\boxed{
d_{\max}^{F}
=
\frac{\ln\tau_F}{\ln q}.
}
$$

macro gain：

$$
\boxed{
Gain_m
=
f_m[
\alpha\Delta d
+\beta\Delta F
+\gamma\Delta Y
+\eta\Delta L
].
}
$$

聯合 optimum：

$$
\boxed{
(N^*,d^*,g^*,v^*)
=
\arg\min C_{total}.
}
$$

---

# 47. 非主張

本文不主張：

1. $d\log N\gtrsim\log M$ 是普遍定理；
2. composition error 真正獨立；
3. $F=q^d$ 足以描述真實 Agent；
4. RISC/CISC 與 AI operator language 完全等價；
5. macro 越多越好；
6. high-frequency motif 一定要 macro 化；
7. coarse operators 一定適合低風險工作；
8. universal $(N^*,d^*,g^*)$ 存在；
9. Transformer network depth 等於 operator composition depth；
10. static optimum 會在未來維持不變。

本文只提出：

$$
\boxed{
\text{Basis size, composition depth, operator granularity, and verification density form a coupled design space whose optimum must be evaluated through effective expressivity, fidelity, learning, selection, action yield, and risk.}
}
$$

---

# 48. 文獻錨點

1. **Combinatory Logic / Small Complete Bases**  
   經典 combinatory logic 顯示小型 combinatory basis 可以具有極高生成能力；derived combinators 則說明形式上不必要的高階 unit 可以顯著縮短 expression。這提供「basis size vs expression complexity」的形式錨點。

2. **RISC/CISC Instruction-Set Tradeoff**  
   電腦架構長期存在「較少簡單 instructions vs 較多複雜 instructions」的 code density、decode complexity、execution cost 交換；現代 ISA 亦常將複雜 instructions 內部分解為 micro-operations。本文僅把它作為工程類比，不視為 COL 的直接證明。

3. **The Impact of Depth on Compositional Generalization in Transformer Language Models（NAACL 2024）**  
   在控制總參數量後，較深 Transformer 通常有較好的 compositional generalization，但額外 depth 的收益快速遞減。本文的 expression depth 與 network depth 不同，但此結果提醒「depth capacity」與「depth cost」都需要實證處理。

4. **Evaluating Morphological Compositional Generalization in Large Language Models（NAACL 2025）**  
   顯示 LLM 在 novel roots 與更高 morphological complexity 下 compositional generalization 明顯下降，支持「增加組合複雜度可能降低 effective fidelity」。

5. **Compositional Generalization with Grounded Language Models（ACL Findings 2024）**  
   顯示 grounded language models 對 unseen sequence lengths 與 seen primitives 的 novel combinations 仍有困難，支持對 depth extrapolation 單獨建模。

6. **Exploring Compositional Generalization of Large Language Models（NAACL SRW 2024）**  
   研究 compositional instructions，報告由高階 compositional instructions 向低階的泛化與反向泛化並不對稱，說明 curriculum 與 composition order 對 effective language learning 有實際影響。

---

# 49. 下一篇

## LRC–COL-06：靜態完備區間與動態完備區間
### Static and Dynamic Completeness Intervals of Composite Operator Languages

下一篇將把目前：

$$
\boxed{
I_{\mathcal O}^{S}
=
[
N_{\min}^{effective},
N_{\max}^{effective}
]
}
$$

從固定切片擴張成：

$$
\boxed{
I_{\mathcal O}^{D}(t)
=
[
N_{\min}(t),
N_{\max}(t)
].
}
$$

正式研究：

- Agent 學習為何可能讓 $N_{\min}$ 收縮；
- 新 domain 為何又讓 $N_{\min}$ 擴張；
- retriever / context 升級如何推高 $N_{\max}$ ；
- operator crystallization / retirement 如何改變區間；
- 是否存在 interval hysteresis；
- 語言是否會出現 expansion → saturation → compression → re-expansion 的週期；
- $(N^*,d^*,g^*)$ 如何成為時間函數。

**END — LRC–COL-05 v0.1**
