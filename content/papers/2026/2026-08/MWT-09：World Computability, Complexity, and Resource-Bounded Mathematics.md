# MWT-09：World Computability, Complexity, and Resource-Bounded Mathematics
## 可計算性、可判定性、證明成本、預處理、攤銷資源與 AI 世界的可負擔數學

**英文題名：** *MWT-09: World Computability, Complexity, and Resource-Bounded Mathematics — Computability, Decidability, Proof Cost, Preprocessing, Amortized Resources, and Feasible Mathematics for AI Worlds*  
**系列：** Mathematical World Theory（MWT）  
**篇次：** 09  
**文件編號：** EML-MWT-09-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-19  
**版本：** v0.1  
**文件性質：** 數學世界論第九篇形式母稿／Computability Layer／Complexity Accounting／Resource-Bounded AI Mathematics  
**前置文件：** MWT-01 ～ MWT-08  
**狀態：** 可使用研究稿；提供 reference resource evaluator；不宣稱建立新的通用複雜度類以取代經典計算複雜度理論  

---

## 摘要

MWT-08 已建立 Global Quantifier Compression Certificate，使有限可檢查 kernel 能在 coverage、lift 與 soundness 證書齊備時承擔 $\forall$ 的全域責任。但一個 finite certificate「存在」，並不代表它在現實 runtime 中容易被找到、生成、儲存、傳輸或驗證；一個 algorithm「可計算」，也不代表它在目前 AI、硬體、時間、能源、context、通訊與 branch budget 下實際可完成。

本文提出 **World Computability and Resource Layer（WCRL）**，將 MWT 中常被混在一起的概念嚴格拆分。其第一條母原則為：

$$
\boxed{
\text{Existence}
\neq
\text{Representability}
\neq
\text{Computability}
\neq
\text{Decidability}
\neq
\text{Verifiability}
\neq
\text{Tractability}
\neq
\text{Feasibility}
\neq
\text{Execution}
\neq
\text{Acquisition}.
}
$$

此式不是一條普遍線性蘊含鏈，而是一組必須分開標記的資格軸。不同問題類型的軸之間具有不同邏輯關係。例如對經典語言判定問題，在固定 Turing-machine model 下，decidable language 同時可 recognizable 與 co-recognizable；而「存在容易驗證的 witness」則是另一種 certificate-relative 性質，不能無條件由 computability 推出。

本文定義一個 **Computation Episode**：

$$
\boxed{
\chi
=
(
q,
P,
e,
M,
\Gamma,
H,
B,
A
),
}
$$

其中：

- $q$：query / task；
- $P$：presentation；
- $e$：encoding；
- $M$：computational model / machine model；
- $\Gamma$：assumptions / legality / environment；
- $H$：可合法使用的歷史、cache、precomputation 與 learned structure；
- $B$：resource budget；
- $A$：algorithm / solver / proof-search procedure。

因此計算成本永遠不是裸：

$$
T(n).
$$

更一般地，MWT 使用 typed **Resource Cost Profile**：

$$
\boxed{
\kappa(\chi)
=
(
T,
S,
W,
D,
C_{\mathrm{comm}},
C_{\mathrm{io}},
C_{\mathrm{transfer}},
C_{\mathrm{proof}},
L_{\mathrm{proof}},
C_{\mathrm{verify}},
N_{\mathrm{branch}},
C_{\mathrm{external}},
C_{\mathrm{human}},
E
).
}
$$

其中可分別表示：

- wall-clock / sequential time；
- memory / storage；
- total work；
- critical-path span；
- communication；
- I/O；
- cross-presentation / resolution transfer；
- proof generation cost；
- proof length；
- certificate verification；
- branch count / branch exploration；
- external API / tool；
- human intervention；
- energy 或其他工程資源。

不是每個 domain 都需要全部資源，也不要求這些資源被壓成一個 scalar。

本文因此區分：

$$
\boxed{
\text{Complexity}
}
$$

與：

$$
\boxed{
\text{Feasibility under budget}.
}
$$

一個 algorithm family 可以具有良好的 asymptotic class，但在某個實際 instance 因常數、資料搬移、證明物件大小、通訊或記憶體而不可負擔；反過來，一個 asymptotically expensive method 在小輸入、重複 workload、強 precomputation 或高平行硬體下可以在當前 runtime 完成。

本文亦正式處理 MWT 既有「動態速率／解空間重寫」主線最容易被誤讀的地方。智慧體可以透過長期：

- concept integration；
- theorem indexing；
- cache；
- representation rewriting；
- bridge construction；
- precomputed data；
- solver compilation；
- specialized hardware；
- multi-agent preparation；

把後續一次 query 的 online latency 壓得非常低。但成本不會因此自動從計算歷史中消失。本文將成本拆成：

$$
\boxed{
C_{\mathrm{total}}^{(N)}
=
C_{\mathrm{offline}}
+
\sum_{i=1}^{N}
C_{\mathrm{online},i}
+
C_{\mathrm{maintenance}}
+
C_{\mathrm{migration}}.
}
$$

攤銷成本為：

$$
\boxed{
\overline C_N
=
\frac{
C_{\mathrm{total}}^{(N)}
}{N}.
}
$$

因此：

$$
\boxed{
\text{instant-looking solve}
}
$$

可以是真實工程進步，也可能只是昂貴歷史成本已被 amortize；只有在明確 computation model 中，才有資格宣稱經典 complexity class 發生改變。

本文進一步提出 **Complexity Conservation of Accounting Principle**：

> **表示重寫、預處理、外部工具、資料庫、advice、模型訓練、cache、human labor 與歷史推理都可以降低當前 online cost，但只要它們對任務有必要，就必須被放進某一個合法 accounting boundary；不能因把成本移出 query 執行階段，就宣稱成本不存在。**

這不是物理守恆定律，也不主張所有資源可互相換算。它只是計算核算規則。

本文將「問題改寫／繞過」也納入 task identity。若原 task：

$$
q
$$

被改成：

$$
q',
$$

並且：

$$
q'\equiv_{\mathfrak I_q}q
$$

有 certificate，則可視為合法 task-equivalent bypass；否則只是解了一個不同問題。這直接延續解空間幾何計算論中「Find / Verify / Ask / Generate / Create / Bypass」的區分，同時避免用重新定義成功條件來偽造複雜度突破。

在 proof 層，本文把：

$$
\boxed{
\text{Provability}
}
$$

拆成：

1. proof exists relative to formal system；
2. proof can be found；
3. proof can be represented / stored；
4. proof can be transmitted；
5. proof can be checked；
6. proof can be checked within budget。

Cook–Reckhow proof complexity 提供經典外部接口：不同 propositional proof systems 可以在 proof length / simulation efficiency 上有巨大差異；因此「一個定理有證明」與「當前 proof system 能短證明它」不是同一問題。MWT-09 將 proof length、proof-search cost 與 verification cost 分別入帳。

在多 AI / solver federation 層，本文加入 communication complexity。若 agent $A$ 已知 $x$ 、agent $B$ 已知 $y$，共同計算 $f(x,y)$ 的成本不只在各自 local compute；跨 agent 必須交換多少 information 本身就是一級資源。Yao 的 communication-complexity 路線提供經典外部參照。這對 MWT-03 multi-AI scheduler、MWT-06 solver federation 與 MWT-07 proof/computation federation尤其重要。

本文最後提出 Resource Registry、Complexity Contract Store、Offline/Online Ledger、Proof-Cost Ledger、Communication Ledger、Feasibility Engine、Amortization Engine、Lower-Bound / Impossibility Registry、Resource Replan Engine 與 Resource-Aware Commit Gate 十個最低模組。

MWT-09 的核心不是發明新的 P/NP 替代品，而是給 MWT 一個不能逃帳的計算層：

$$
\boxed{
\text{「原理上可以」}
\neq
\text{「這個世界狀態現在做得到」}.
}
$$

**關鍵詞：** Mathematical World Theory、computability、decidability、complexity、resource boundedness、proof complexity、verification cost、amortized complexity、preprocessing、communication complexity、AI-native mathematics

---

# 0. 本文的責任：把「能」拆開

一句：

> 「這個 AI 能解。」

至少可能表示：

1. 理論上存在 algorithm；
2. algorithm 在某 computation model 可計算；
3. algorithm 一定 halt；
4. output 可驗證；
5. runtime 在合理 complexity；
6. 目前硬體裝得下；
7. 目前 budget 跑得完；
8. 所需資料可取得；
9. 所需 proof 可生成；
10. 最後真的已執行成功。

這十件事不是同一件事。

---

# 1. 第一個分離：Truth 與 Computability

命題：

$$
\phi
$$

可以在某模型／世界相對意義下有真值，

但不代表存在有效程序決定：

$$
\phi.
$$

Turing 1936/1937 的工作已建立：

$$
\boxed{
\text{precisely stated}
\not\Rightarrow
\text{algorithmically decidable}.
}
$$

因此 MWT 永遠不能把「數學問題存在」偷換成「一定可被 AI 算完」。

---

# 2. 第二個分離：Computability 與 Complexity

即使 function：

$$
f
$$

computable，

仍可能需要極高時間／空間。

Hartmanis–Stearns 與其後 complexity theory 的核心就是：

> 不只問能不能算，也問在何種 resource bound 內能算。

---

# 3. 第三個分離：Complexity 與 Feasibility

如果：

$$
T(n)=n^3,
$$

在 asymptotic 意義是 polynomial。

但：

$$
n=10^{12}
$$

仍可能完全不可執行。

反過來：

$$
2^n
$$

在：

$$
n=20
$$

可能很容易。

所以：

$$
\boxed{
\text{complexity class}
\neq
\text{instance feasibility}.
}
$$

---

# 4. 第四個分離：Verification 與 Discovery

certificate：

$$
w
$$

可能很容易驗：

$$
V(x,w)=1.
$$

但找到：

$$
w
$$

可能很難。

這是 NP 型思考的重要來源之一。

但 MWT 不宣稱：

$$
\boxed{
\text{verification always cheap}.
}
$$

驗證成本也必須測量。

---

# 5. 第五個分離：Provability 與 Proof Search

在 formal system：

$$
T,
$$

可能存在：

$$
\pi
$$

使：

$$
T\vdash_{\pi}\phi.
$$

但 proof search procedure：

$$
A
$$

可能在當前 budget 找不到 $\pi$。

因此：

$$
\boxed{
\text{proof exists}
\neq
\text{proof found}.
}
$$

---

# 6. 第六個分離：Proof Found 與 Proof Checkable under Budget

即使 proof：

$$
\pi
$$

已取得，

如果：

$$
|\pi|
>
B_{\mathrm{storage}},
$$

或：

$$
T_{\mathrm{verify}}(\pi)
>
B_{\mathrm{time}},
$$

當前 runtime 仍不能完整驗證。

---

# 7. 第七個分離：Answer Exists 與 Answer Acquired

外部資料庫可能已經存在 answer。

但：

- 不知道位置；
- 無權存取；
- network unavailable；
- retrieval cost too high；

則當前 query：

$$
\boxed{
\text{not acquired}.
}
$$

---

# 8. Capability Profile

本文不把上述概念強迫排成單一 chain。

定義：

$$
\boxed{
\mathsf{CapProf}(\chi)
=
(
R,
C,
D,
S^+,
S^-,
V,
F,
E,
A
).
}
$$

其中：

- $R$：representable；
- $C$：computable；
- $D$：decidable；
- $S^+$：positive semi-decision / recognizability；
- $S^-$：negative semi-decision；
- $V$：certificate-verifiable；
- $F$：resource-feasible；
- $E$：currently executable；
- $A$：answer acquired。

每一項可：

$$
\{\mathsf{Yes},\mathsf{No},\mathsf{Unknown},\mathsf{Contextual}\}.
$$

---

# 9. Computation Episode

定義：

$$
\boxed{
\chi
=
(
q,
P,
e,
M,
\Gamma,
H,
B,
A
).
}
$$

沒有：

$$
P,e,M
$$

就談 complexity，通常太粗。

---

# 10. Encoding Matters

同一 mathematical object：

$$
x
$$

可以有不同 encoding：

$$
e_1(x),
\quad
e_2(x).
$$

input size：

$$
n_i
=
|e_i(x)|
$$

不同。

所以：

$$
T(n)
$$

必須帶 encoding context。

---

# 11. Artificial Compression Warning

若使用一個 encoding：

$$
e^\star
$$

把巨大 answer 預先編進短 symbol，

不能只算短 symbol decode 前的 cost。

decode / dictionary / precomputation 仍需入帳。

---

# 12. Machine Model Matters

同一 task 在：

- Turing machine；
- RAM；
- GPU；
- distributed cluster；
- quantum computer；
- theorem prover；

成本表示不同。

Blum 1967 的 machine-independent complexity framework 提供一個重要經典方向：複雜度度量需要滿足明確可計算性條件，而不是任意稱某個數字為「成本」。

MWT 不重新發明 Blum axioms，但吸收其 discipline：

$$
\boxed{
\text{complexity measure must expose its measurement contract}.
}
$$

---

# 13. Complexity Contract

定義：

$$
\boxed{
\mathfrak C_{\kappa}
=
(
M,
e,
\mathcal R,
n,
\mathsf{mode},
v
).
}
$$

其中：

- $M$：machine model；
- $e$：encoding；
- $\mathcal R$：resource dimensions；
- $n$：size measure；
- mode：worst / average / amortized / expected / instance；
- $v$：version。

---

# 14. Resource Cost Profile

$$
\boxed{
\kappa(\chi)
=
(
T,
S,
W,
D,
C_{\mathrm{comm}},
C_{\mathrm{io}},
C_{\mathrm{transfer}},
C_{\mathrm{proof}},
L_{\mathrm{proof}},
C_{\mathrm{verify}},
N_{\mathrm{branch}},
C_{\mathrm{external}},
C_{\mathrm{human}},
E
).
}
$$

不是所有項目都要數值化。

可以是：

- exact；
- asymptotic；
- interval；
- symbolic bound；
- unknown。

---

# 15. Time

$$
T
$$

可以分：

- CPU time；
- wall clock；
- iterations；
- logical steps。

---

# 16. Space

$$
S
$$

包括：

- working memory；
- persistent storage；
- context window；
- checkpoint state。

---

# 17. Work 與 Span

對 parallel computation：

$$
W
$$

是 total work，

$$
D
$$

是 critical-path depth / span。

只報 wall-clock 會掩蓋大量並行資源。

---

# 18. Communication

$$
C_{\mathrm{comm}}
$$

量測：

- bits；
- messages；
- rounds；
- latency；
- synchronization。

多 AI runtime 特別需要。

---

# 19. I/O

大模型／大型證明庫：

$$
C_{\mathrm{io}}
$$

可能比 arithmetic 本身昂貴。

因此 storage access 不能自動視為免費。

---

# 20. Transfer Cost

跨 presentation：

$$
P_i\to P_j
$$

需要：

$$
C_{\mathrm{transfer}}.
$$

例如：

- symbolic→numeric；
- coarse→fine；
- proof→human explanation；
- data serialization。

---

# 21. Proof Generation Cost

$$
C_{\mathrm{proof}}
$$

是找到 / 生成 proof 的成本。

與 proof verification 分開。

---

# 22. Proof Length

$$
L_{\mathrm{proof}}
=
|\pi|.
$$

短 proof 與長 proof 的工程價值不同。

---

# 23. Verification Cost

$$
C_{\mathrm{verify}}
=
\operatorname{Cost}
(
V(\pi)
).
$$

certificate-carrying mathematics 的主要目標之一是：

$$
C_{\mathrm{verify}}
\ll
C_{\mathrm{generation}}
$$

在適用情況下。

但這不是 universal law。

---

# 24. Branch Cost

MWT-03 的 branch space：

$$
N_{\mathrm{branch}}
$$

本身是一級成本。

即使每支很便宜，

$$
N_{\mathrm{branch}}
\to
2^n
$$

仍可能爆炸。

---

# 25. External Cost

$$
C_{\mathrm{external}}
$$

可包括：

- API；
- web；
- database；
- laboratory；
- cloud；
- licensed solver。

---

# 26. Human Cost

$$
C_{\mathrm{human}}
$$

可以是：

- review；
- formalization；
- semantic judgment；
- governance approval。

AI-native 不等於人類成本永遠為零。

---

# 27. Energy

$$
E
$$

是可選工程資源。

MWT 不將 energy 直接當抽象 complexity class，除非 computational model 明示。

---

# 28. Budget Vector

世界狀態給：

$$
\boxed{
B_t
=
(
B_T,
B_S,
B_W,
B_D,
B_{\mathrm{comm}},
B_{\mathrm{io}},
B_{\mathrm{proof}},
B_{\mathrm{verify}},
B_{\mathrm{branch}},
B_{\mathrm{external}},
B_{\mathrm{human}},
B_E
).
}
$$

---

# 29. Hard Budget

某些資源是硬上限：

$$
\kappa_i
\leq
B_i.
$$

違反就：

$$
\boxed{
\mathsf{InfeasibleNow}.
}
$$

---

# 30. Soft Budget

其他資源可以超支，但產生：

- warning；
- debt；
- reprioritization。

硬／軟必須明示。

---

# 31. Resource Feasibility Judgment

定義：

$$
\boxed{
\Gamma
\vdash
\chi
\Downarrow_{\mathsf{Res}}
r
}
$$

其中：

$$
r
\in
\{
\mathsf{Feasible},
\mathsf{Infeasible},
\mathsf{Deferred},
\mathsf{Unknown},
\mathsf{Conflicted}
\}.
}
$$

---

# 32. Feasible

所有 hard budgets 有證據可滿足。

---

# 33. Infeasible

至少一個 hard budget 有確定 violation。

這不等於：

$$
\boxed{
\text{mathematically impossible}.
}
$$

---

# 34. Deferred

目前 budget 不足，但存在合理未來 resource / scheduling path。

---

# 35. Unknown

cost bound 尚未得到。

---

# 36. Conflicted

不同 cost model / estimator / runtime 給不相容結果。

---

# 37. Feasibility Is Time-Indexed

今天：

$$
\mathsf{Infeasible}_{t}
$$

明天 hardware / algorithm 改善後：

$$
\mathsf{Feasible}_{t+1}.
$$

所以 feasibility 不是 theorem truth。

---

# 38. Complexity Class Is Family-Level

對 problem family：

$$
\Pi
=
\{
x_n
\},
$$

才適合談：

$$
O(f(n)).
$$

單一 instance 更適合談實測／bound resource profile。


# 39. Instance Feasibility Is Not Asymptotic Classification

對單一 instance：

$$
x,
$$

MWT 應報：

$$
\boxed{
\kappa(A,x)
}
$$

及：

$$
B_t,
$$

而不是只報：

$$
A\in P.
$$

---

# 40. Worst-Case、Average、Expected、Amortized 必須分開

同一 algorithm 可以有：

$$
T_{\mathrm{worst}}(n),
$$

$$
T_{\mathrm{avg}}(n),
$$

$$
\mathbb E[T(n)],
$$

$$
T_{\mathrm{amort}}(n).
$$

這些不是同一 claim。

---

# 41. Dynamic World 需要更多 Mode

MWT 再增加：

- migration cost；
- revalidation cost；
- cache-warm cost；
- cold-start cost；
- incremental-update cost；
- full-rebuild cost。

因為 world-state 長期存在，不是每次從空白開始。

---

# 42. Offline / Online Split

令：

$$
C_{\mathrm{offline}}
$$

是 query 前已投入的成本。

例如：

- model training；
- theorem indexing；
- preprocessing；
- data structure construction；
- proof library compilation；
- bridge building；
- representation learning。

query 發生後是：

$$
C_{\mathrm{online}}.
$$

---

# 43. Total Cost

對 $N$ 次 queries：

$$
\boxed{
C_{\mathrm{total}}^{(N)}
=
C_{\mathrm{offline}}
+
\sum_{i=1}^{N}
C_{\mathrm{online},i}
+
C_{\mathrm{maintenance}}
+
C_{\mathrm{migration}}.
}
$$

---

# 44. Amortized Cost

$$
\boxed{
\overline C_N
=
\frac{
C_{\mathrm{total}}^{(N)}
}{N}.
}
$$

如果：

$$
N
$$

很大，

昂貴 offline structure 可以非常值得。

---

# 45. Instant-Looking Intelligence

一個成熟 AI 在：

$$
10\text{ ms}
$$

回答問題，

可能只是：

$$
\boxed{
\text{years of training}
+
\text{indexing}
+
\text{cached world state}
+
\text{online lookup}.
}
$$

這仍然是真實能力。

但不能只用：

$$
10\text{ ms}
$$

代表全部 computation cost。

---

# 46. Historical Cost

MWT 允許：

$$
\boxed{
C_{\mathrm{history}}
}
$$

表示先前 closure cycles 累積並可重用的結構成本。

---

# 47. Historical Cost Is Not Repaid Every Query

核算歷史成本不表示每次 query 都要把訓練成本完整再加一次。

正確做法可依 task 設：

- sunk cost；
- amortized allocation；
- marginal cost；
- maintenance cost。

但 accounting boundary 必須透明。

---

# 48. Complexity Conservation of Accounting Principle

本文提出一個工程原則：

$$
\boxed{
\text{必要成本不能只因被移到別的階段而消失。}
}
$$

如果一個 online algorithm 依賴：

$$
D_{\mathrm{pre}}
$$

而建立 $D_{\mathrm{pre}}$ 成本巨大，

則至少在 total / amortized accounting 中要出現。

---

# 49. 這不是物理守恆定律

名稱中的「conservation」只表示：

> 不允許 cost boundary 偷換。

它不主張：

- time 可完全換成 space；
- energy 等於 communication；
- 所有資源有共同單位。

---

# 50. Preprocessing

給 problem family：

$$
x
\mapsto
P(x),
$$

可以先建：

$$
\boxed{
D_n
}
$$

處理 input-size $n$ 或固定 domain 的共通結構。

---

# 51. Preprocessing Changes the Computation Model

如果：

$$
D_n
$$

依賴 $n$ 而不依賴 specific $x$，

這與 nonuniform advice / preprocessing model 鄰接。

若：

$$
D_x
$$

直接把 specific input answer 預先算好，

則 online cost 變小並不令人意外。

---

# 52. Advice Is Not Free Uniform Computation

若 algorithm：

$$
A(x,a_n)
$$

使用 advice：

$$
a_n,
$$

複雜度 claim 必須說：

- advice size；
- how advice is obtained；
- uniform / nonuniform model。

不能把 advice 當宇宙送來的免費 oracle。

---

# 53. Oracle / Tool Cost

如果 query 呼叫：

$$
\mathcal O
$$

作 oracle，

可以在 oracle model 內將 call 視為 unit cost。

但若要描述實際 world runtime，

需要額外：

$$
C_{\mathcal O}.
$$

---

# 54. External Intelligence Cost

Ask：

$$
\mathsf{Ask}(A_j)
$$

可以大幅縮短 agent $A_i$ 的 local computation。

但 global accounting 增加：

- communication；
- remote compute；
- trust verification。

---

# 55. Representation Rewrite

MWT-05 允許：

$$
P
\xrightarrow{R}
P'.
$$

如果：

$$
A'
$$

在 $P'$ 上非常快，

總 cost 至少：

$$
\boxed{
C_{\mathrm{rewrite}}
+
C_{A'}
+
C_{\mathrm{reconstruct}}
+
C_{\mathrm{verify}}.
}
$$

---

# 56. Representation Speedup

若：

$$
C_{\mathrm{rewrite}}
$$

可被 amortize，

新的 representation 可以帶來巨大實際 speedup。

這是真正值得研究的 AI-native phenomenon。

但它不是自動：

$$
P=NP.
$$

---

# 57. Input-Size Blowup

如果 rewrite：

$$
R
$$

把：

$$
|x|=n
$$

變成：

$$
|R(x)|
=
2^n,
$$

而新 solver 對新 size 是 linear，

總體仍可能 exponential。

所以 representation comparison 必須追蹤 size map：

$$
\boxed{
n'
=
g(n).
}
$$

---

# 58. Compression Caveat

如果：

$$
R
$$

把很多資訊壓進一個 opaque symbol，

需要考慮：

- decompression；
- lookup；
- dictionary；
- collision / identity；
- hidden advice。

---

# 59. Task Rewrite / Bypass

解空間幾何計算論已提出：

$$
\mathsf{Bypass}.
$$

MWT-09 只在：

$$
\boxed{
q'
\equiv_{\mathfrak I_q}
q
}
$$

有 certificate 時，稱 $q'$ 是 task-equivalent bypass。

---

# 60. Task Redefinition Is Not Complexity Improvement

如果：

$$
q'
$$

只是降低了成功標準，

那只是換問題。

不能用：

$$
C(q')
<
C(q)
$$

宣稱：

$$
q
$$

被更快解決。

---

# 61. Functional Equivalence Can Be Enough

有些工程 query 本來只要求：

$$
\text{functional terminal state}.
$$

此時 bypass 完全合法。

所以是否「換問題」由 Inquiry Contract / identity specification 決定。

---

# 62. Dynamic Rate Theory Interface

既有動態速率／解空間主線強調：

> 智慧體透過歷史累積、表示重寫、工具與概念橋接，可改變有效解空間距離。

MWT-09 接受這一點。

但將：

$$
\boxed{
\text{effective online distance reduction}
}
$$

與：

$$
\boxed{
\text{classical complexity-class collapse}
}
$$

分開。

---

# 63. Effective Distance

可以定義任務相對：

$$
d_{\mathrm{eff}}(q\mid H_t,P_t,\mathcal O_t)
$$

作 heuristic / structural measure。

但它不是經典 complexity measure，除非另有 machine model 與 cost theorem。

---

# 64. Historical Acceleration

如果：

$$
H_{t+1}
\supset H_t
$$

使：

$$
C_{\mathrm{online}}(q\mid H_{t+1})
<
C_{\mathrm{online}}(q\mid H_t),
$$

可以稱：

$$
\boxed{
\text{historical acceleration}.
}
$$

這是 AI learning / memory 的自然效果。

---

# 65. Amortized Intelligence

對 query distribution：

$$
\mathcal D_Q,
$$

長期 system cost 可研究：

$$
\boxed{
\mathbb E_{q\sim\mathcal D_Q}
[
C_{\mathrm{online}}(q\mid H_t)
].
}
$$

AI 的價值可能主要表現在 distribution-relative amortization，而不是所有 worst-case instance。

---

# 66. Worst-Case Must Remain Visible

即使平均非常快：

$$
\mathbb E[T]\ll T_{\mathrm{worst}},
$$

high-risk domain 仍可能需要 worst-case bound。

不能只報平均。

---

# 67. Proof Resource Profile

對 proof：

$$
\pi,
$$

定義：

$$
\boxed{
\kappa_{\pi}
=
(
C_{\mathrm{search}},
L_{\pi},
S_{\pi},
C_{\mathrm{transfer}},
C_{\mathrm{verify}},
C_{\mathrm{replay}}
).
}
$$

---

# 68. Proof Exists

$$
\exists\pi:
T\vdash_{\pi}\phi.
$$

這是 provability。

---

# 69. Proof Search

algorithm：

$$
A_T(\phi)
$$

要找：

$$
\pi.
$$

其：

$$
C_{\mathrm{search}}
$$

可能非常大。

---

# 70. Proof Length

不同 proof systems：

$$
P_1,P_2
$$

可能對同一 tautology 有不同最短 proof length。

Cook–Reckhow 1979 的 propositional proof-system framework 正是 proof complexity 的經典接口。

---

# 71. Proof-System Relative Efficiency

如果：

$$
P_1
$$

可 polynomially simulate：

$$
P_2,
$$

則 $P_1$ 對 $P_2$ proofs 可控制 polynomial blowup。

MWT 不需要重新定義這個理論，只需把 proof-system identity 加入 complexity contract。

---

# 72. Short Theorem Statement, Long Proof

$$
|\phi|
\ll
|\pi|
$$

完全可能。

所以 storage / transfer / verification 可以成為主要瓶頸。

---

# 73. Proof Compression

可以建立壓縮 proof：

$$
\widehat\pi.
$$

但 checker 必須知道如何解壓／驗證。

如果 decompressor 不可信，壓縮只是把 trusted base 搬家。

---

# 74. Proof-Carrying World State

MWT Stable Core 中的重要 theorem 可以存：

$$
\boxed{
(
\phi,
C_{\forall},
\kappa_{\pi},
V_{\mathrm{checker}}
).
}
$$

使 future AI 能決定是否：

- full replay；
- trust cached verification；
- independent verify。

---

# 75. Verification Is a Computation Too

$$
V(\pi,\phi)
$$

有：

$$
T_V,
S_V.
$$

所以：

$$
\boxed{
\text{certificate}
\neq
\text{zero-cost certainty}.
}
$$

---

# 76. Streaming Verification

某些 certificate 可以 streaming check，

降低 memory。

所以：

$$
\boxed{
\text{proof size}
>
\text{memory}
}
$$

不一定立即表示不可驗。

取決於 checker architecture。

---

# 77. Verification Parallelism

proof DAG 可以部分並行 check。

因此要分：

$$
W_V,
D_V.
$$

這再次說明 wall-clock 不是唯一資源。

---

# 78. Search vs Verification Asymmetry

如果：

$$
C_{\mathrm{search}}
\gg
C_{\mathrm{verify}},
$$

最適合：

- expensive producer；
- many cheap consumers。

這是 certificate economy 的核心工程情境。

---

# 79. Verification Can Be Hard Too

某些 proof representation 的 checking 本身可能需要昂貴 subprocedure。

因此：

$$
\boxed{
\text{proof provided}
\not\Rightarrow
\text{verification trivially cheap}.
}
$$

---

# 80. Cook’s Theorem-Proving Complexity Interface

Cook 1971 將 theorem-proving procedures 的 complexity 與 NP-completeness 問題帶入現代 complexity theory。

MWT-09 的作用不是重述 Cook theorem，而是把：

- solve；
- witness；
- verify；
- proof-search；

的不同 cost 放入 World Query accounting。

---

# 81. Decidability

對 language：

$$
L,
$$

若存在 machine：

$$
M
$$

對每個 input 都 halt 並正確接受／拒絕，

則：

$$
\boxed{
L
\text{ decidable}.
}
$$

---

# 82. Semi-Decidability / Recognizability

若 machine：

- 對 $x\in L$ 最終 accept；
- 對 $x\notin L$ 可能永不停止；

則：

$$
L
$$

recognizable / semi-decidable。

---

# 83. Positive and Negative Semi-Decision

若：

$$
L
$$

與：

$$
\overline L
$$

都 recognizable，

則在經典 setting 下可 dovetail 成 decision procedure。

因此 positive / negative recognizability 需要分別標。

---

# 84. Undecidability Is Not Resource Infeasibility

$$
\boxed{
\text{undecidable}
}
$$

表示不存在該 model 下 total decision algorithm。

$$
\boxed{
\text{infeasible}
}
$$

只表示目前 budget / algorithm 不足。

不能混。

---

# 85. Unknown Is Not Undecidable

如果我們尚未找到 algorithm：

$$
\boxed{
\text{unknown computability status}
}
$$

不能直接升級成 undecidable。

---

# 86. Complexity Lower Bound

若能證：

$$
T_A(n)
\geq
f(n)
$$

對某 model / algorithm family，

這是 resource impossibility certificate。

---

# 87. Lower Bound Is Model-Relative

改：

- machine model；
- randomized allowance；
- approximation；
- preprocessing；
- hardware；

lower bound statement可能改變。

所以：

$$
\boxed{
\text{lower bound}
}
$$

必須帶 computation contract。

---

# 88. Time Hierarchy Interface

Hartmanis–Stearns 的工作建立時間資源層級的基本思想：

> 給更多可構造時間，可以嚴格增加某些可判定問題的能力。

MWT 吸收的不是某個單一定理形式，而是：

$$
\boxed{
\text{resource bounds can define genuine capability boundaries}.
}
$$

---

# 89. Space Complexity

memory 不是 time 的附屬量。

Savitch 1970 等經典結果顯示 nondeterministic / deterministic space 關係具有自己的結構。

MWT 因此不能只以 FLOPs / seconds 表示全部 complexity。

---

# 90. Time–Space Tradeoff

algorithm：

$$
A_1
$$

可能快但吃 memory，

$$
A_2
$$

慢但省 memory。

所以 resource comparison 更自然是：

$$
\boxed{
\text{Pareto relation}.
}
$$

---

# 91. Resource Pareto Frontier

對 candidate algorithms：

$$
\mathcal A,
$$

保留所有非支配：

$$
A_i.
$$

不同 runtime budgets 可以選不同點。

---

# 92. No Universal Scalar Cost

若硬把：

$$
T,S,C,E
$$

全部乘權重：

$$
w_TT+w_SS+\cdots,
$$

這只是某 policy。

不能冒充 universal complexity measure。


# 93. Communication Complexity

多智能體世界中：

$$
A
$$

持有：

$$
x,
$$

$$
B
$$

持有：

$$
y.
$$

要共同計算：

$$
f(x,y),
$$

除了 local compute，

還要問：

$$
\boxed{
\text{至少交換多少資訊？}
}
$$

---

# 94. Yao Interface

Yao 1979 的 communication-complexity 路線建立：

> distributed computation 的 information exchange 本身可以形成獨立 complexity measure。

MWT 將：

$$
C_{\mathrm{comm}}
$$

作 multi-AI / solver federation 的第一級成本。

---

# 95. More Agents Can Increase Communication

加入：

$$
A_3,\ldots,A_m
$$

可能降低 local computation，

但：

$$
C_{\mathrm{comm}}
$$

與 synchronization 可能上升。

所以：

$$
\boxed{
\text{more agents}
\neq
\text{monotone speedup}.
}
$$

---

# 96. Communication Rounds

除了 bit count：

$$
b,
$$

round count：

$$
r
$$

也很重要。

高 latency network 中：

$$
10
$$

個小 round 可能比一次大 message 更慢。

---

# 97. Shared Memory Is Not Free Communication

如果 agents 共用：

$$
M_{\mathrm{shared}},
$$

仍有：

- memory bandwidth；
- consistency；
- locking；
- cache invalidation；
- serialization。

MWT 不因 API 表面像「讀同一資料」就令 communication cost 為零。

---

# 98. Knowledge Transfer Cost

把一個 theorem / model 從 agent：

$$
A_i
$$

傳給：

$$
A_j
$$

還可能需要：

$$
C_{\mathrm{semantic\ transfer}}
$$

例如：

- re-encoding；
- formal-system translation；
- context reconstruction。

---

# 99. Multi-AI Work/Span/Communication Profile

對 branch federation：

$$
\boxed{
\kappa_{\mathrm{MAI}}
=
(
W,
D,
C_{\mathrm{comm}},
R_{\mathrm{round}},
S_{\mathrm{shared}},
N_{\mathrm{agent}}
).
}
$$

這比單一 wall-clock 更能描述 AI 海戰術。

---

# 100. Parallel Speedup Upper Bound Is Structural

如果 dependency span：

$$
D
$$

很長，

再多 agent 也不能把所有 sequential dependence 消失。

MWT-03 的 causal partial order 因此直接形成 parallel complexity 的下界來源。

---

# 101. Scheduler-Induced Cost

scheduler 本身需要：

- dependency detection；
- independence verification；
- branch reduction；
- rollback；
- commit。

所以：

$$
\boxed{
C_{\mathrm{schedule}}
}
$$

也應進大型 World Solve accounting。

---

# 102. Branch-Reduction Cost

DPOR / quotient 可以減少 branch count，

但建立 independence / equivalence certificate 自己也有成本：

$$
C_{\mathrm{reduce}}.
$$

若：

$$
C_{\mathrm{reduce}}
>
C_{\mathrm{naive}}
$$

在小問題上，reduction 不值得。

---

# 103. Query Complexity

MWT-07 的 query 不只是 answer computation。

總成本至少：

$$
\boxed{
C_Q
=
C_{\mathrm{compile}}
+
C_{\mathrm{plan}}
+
C_{\mathrm{route}}
+
C_{\mathrm{execute}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{synthesize}}.
}
$$

---

# 104. Planning Can Dominate

對簡單 query：

$$
C_{\mathrm{plan}}
>
C_{\mathrm{answer}}
$$

完全可能。

所以 query compiler 應有 fast path。

---

# 105. Proof Query Complexity

proof query：

$$
C_Q^{\mathrm{proof}}
$$

還包含：

- formalization；
- theorem retrieval；
- proof search；
- counterexample search；
- checker；
- cross-verification。

---

# 106. Coverage Complexity

MWT-08 要建立：

$$
C_{\forall}.
$$

其成本：

$$
\boxed{
C_{\mathrm{global}}
=
C_{\mathrm{kernel}}
+
C_{\mathrm{coverage}}
+
C_{\mathrm{lift}}
+
C_{\mathrm{sound}}
+
C_{\mathrm{verify}}.
}
$$

---

# 107. Small Kernel, Expensive Lift

即使：

$$
|\mathcal K_{\forall}|
$$

很小，

找到：

$$
C_{\mathrm{lift}}
$$

仍可能極難。

所以 quantifier compression 的瓶頸未必是 case count。

---

# 108. Certificate Size vs Search Cost

一個非常短：

$$
C_{\forall}
$$

可能需要極昂貴 search 才找到。

因此：

$$
\boxed{
\text{short certificate}
\neq
\text{cheap discovery}.
}
$$

---

# 109. World-Solve Complexity

MWT-06 的 World Solve 總成本：

$$
\boxed{
C_{\mathrm{WS}}
=
\sum_i C_{\mathcal S_i}
+
\sum_{ij}C_{\mathfrak p_{ij}}
+
C_{\mathrm{iteration}}
+
C_{\mathrm{residual}}
+
C_{\mathrm{schedule}}
+
C_{\mathrm{refinement}}
+
C_{\mathrm{commit}}.
}
$$

---

# 110. Coupling Iteration Count

如果 coupling fixed-point iteration：

$$
z^{k+1}
=
\Phi(z^k),
$$

需要：

$$
K
$$

輪，

則 local solver cost 會被 multiplicative reuse：

$$
\sum_{k=1}^{K}
\sum_i
C_{\mathcal S_i}^{(k)}.
$$

---

# 111. Strong Coupling Can Be Expensive

implicit coupling 提升 stability / consistency，

但可能增加：

- rollback；
- repeated local solves；
- residual checks。

所以 stronger coupling 不等於 free correctness。

---

# 112. Weak Coupling Can Carry Debt

explicit / weak coupling 較便宜，

但可能留下：

$$
D_C^{\mathrm{coupling}}.
$$

resource decision 因而和 accuracy / residual contract 耦合。

---

# 113. Refinement Complexity

MWT-05 每個 refinement：

$$
r
$$

有：

$$
C_r
=
C_{\mathrm{novelty}}
+
C_{\mathrm{admission}}
+
C_{\mathrm{migration}}
+
C_{\mathrm{reopen}}
+
C_{\mathrm{reconverge}}.
$$

---

# 114. Refinement Can Save Future Cost

refinement 雖然當下昂貴，

卻可能：

$$
C_{\mathrm{online}}^{\mathrm{future}}
\downarrow.
$$

因此 expansion decision 應考慮 long-horizon amortization。

---

# 115. Over-Refinement Cost

增加不必要 dimension：

$$
d_1,\ldots,d_m
$$

可能讓：

- solver；
- query planner；
- bridge；
- memory；

全部變貴。

所以 refinement value 必須扣掉 downstream complexity。

---

# 116. Resource-Aware Refinement Value

可定義候選 profile：

$$
\boxed{
V_R(r)
=
(
\Delta\mathrm{Fidelity},
\Delta\mathrm{Coverage},
\Delta\mathrm{Capability},
-\Delta C_{\mathrm{long-term}}
).
}
$$

不要求 scalar 化。

---

# 117. World-State Maintenance Complexity

即使沒有新 query，

MWT world-state 仍可能需要：

- certificate expiry；
- revalidation；
- index maintenance；
- archive compaction；
- version migration。

因此：

$$
\boxed{
C_{\mathrm{maint}}
}
$$

是一級成本。

---

# 118. Stable Core Has Carrying Cost

Stable Core 越大，

不一定越好。

每個 stable item 可能需要：

- storage；
- dependency tracking；
- future reopen checks。

所以：

$$
\boxed{
\text{knowledge retention}
}
$$

也有 complexity。

---

# 119. Resource-Bounded Mathematics

本文定義：

$$
\boxed{
\mathcal M_B
}
$$

為：

> 在 budget profile $B$ 下，當前可被安全表示、查詢、計算、驗證、耦合與維護的 active mathematical runtime。

它不是「數學真理只到 budget 為止」。

只是 active operational subset。

---

# 120. Mathematical Truth Is Not Budget-Relative by Definition

如果 claim：

$$
\phi
$$

具有 formal truth / theorem status，

budget 不改變其 truth。

budget 改變的是：

- 我們能不能知道；
- 驗不驗得完；
- 能不能重放；
- 能不能使用。

---

# 121. Epistemic Accessibility Is Resource-Relative

因此：

$$
\boxed{
\text{truth status}
\neq
\text{accessible status}.
}
$$

MWT Resource Layer 管後者。

---

# 122. Resource Horizon

對 task：

$$
q,
$$

可以定義：

$$
\boxed{
H_B(q)
}
$$

表示：

> 在 budget family $B$ 下，目前可到達的 solution / verification frontier。

它是 runtime frontier，不是 ontology boundary。

---

# 123. Feasible Region

對 algorithm set：

$$
\mathcal A,
$$

定義：

$$
\boxed{
\mathcal F_B
=
\{
A:
\kappa(A)\preceq B
\}.
}
$$

若 resource partial order 無法全比，

 $\mathcal F_B$ 由 hard constraints 定義。

---

# 124. Resource Partial Order

若：

$$
\kappa(A)
\leq
\kappa(B)
$$

逐 component，

且至少一項嚴格小，

則 $A$ dominates $B$。

---

# 125. Incomparable Algorithms

可能：

$$
T_A<T_B
$$

但：

$$
S_A>S_B.
$$

兩者不可比較。

MWT 保留：

$$
\boxed{
\text{Pareto set}.
}
$$

---

# 126. Resource Policy

不同 task 可以偏好：

- low latency；
- low energy；
- low human cost；
- high verification。

政策：

$$
\Pi_B
$$

從 Pareto set 選 execution plan。

政策不是 complexity theorem。

---

# 127. Resource Replanning

若 runtime 發現：

$$
\widehat C
>
B,
$$

可以：

1. change solver；
2. coarsen；
3. add agents；
4. reduce branches；
5. switch proof system；
6. retrieve existing certificate；
7. defer；
8. return Unknown。

---

# 128. Resource Replan Is Not Silent Claim Weakening

若為了省成本把：

$$
\forall
$$

改成 finite sample，

Answer Contract 必須改成：

$$
\mathsf{FiniteVerified}.
$$

不能仍輸出 UniversalProved。

---

# 129. Graceful Degradation

高 resource plan失敗後，

可以輸出較弱但誠實的結果：

$$
\boxed{
\text{exact proof}
\to
\text{scoped proof}
\to
\text{finite verification}
\to
\text{unknown}.
}
$$

每次降級要標 status。

---

# 130. Resource Debt

如果系統暫時使用：

- stale proof；
- coarse solver；
- incomplete cross-check；

產生：

$$
\boxed{
D_{\mathrm{res}}.
}
$$

進 MWT-04 obligation queue。

---

# 131. Debt Has Interest

resource debt 可能使未來：

- revalidation；
- migration；
- conflict resolution；

成本增加。

所以 debt 不是免費延後。

---

# 132. Resource Reopen

當：

$$
B_{t+1}>B_t
$$

或新 algorithm 出現，

過去：

$$
\mathsf{Deferred}
$$

tasks 可自動 reopen。

---

# 133. Hardware Reopen

新硬體：

- GPU；
- accelerator；
- larger memory；
- cluster；

可以改：

$$
\mathsf{FeasibleNow}.
$$

但 formal computability status通常不因硬體品牌改變。

---

# 134. Algorithmic Reopen

新 algorithm：

$$
A'
$$

可以真正改 family complexity upper bound。

這與單純加硬體不同。

---

# 135. Proof-System Reopen

新 proof system：

$$
P'
$$

可能給更短 proof：

$$
L_{P'}(\phi)
\ll
L_P(\phi).
$$

所以舊「proof infeasible」可以 reopen。

---

# 136. Resource Certificate

對 execution：

$$
\chi,
$$

建立：

$$
\boxed{
C_{\mathrm{res}}(\chi)
=
(
\mathfrak C_{\kappa},
\widehat\kappa,
B,
C_{\mathrm{estimate}},
C_{\mathrm{actual}}
).
}
$$

---

# 137. Estimated vs Actual Cost

執行前：

$$
\widehat\kappa.
$$

執行後：

$$
\kappa_{\mathrm{actual}}.
$$

兩者差異：

$$
\boxed{
r_{\mathrm{cost}}
=
\kappa_{\mathrm{actual}}
-
\widehat\kappa.
}
$$

可用來校正 planner。

---

# 138. Cost Model Drift

hardware、data、network 改變後：

$$
\widehat\kappa^{(v)}
$$

可能失準。

cost models 也需要 version / revalidation。

---

# 139. Lower-Bound Registry

本文新增：

$$
\boxed{
\mathsf{LBR}.
}
$$

保存：

- time lower bounds；
- space lower bounds；
- proof lower bounds；
- communication lower bounds；
- model assumptions。

---

# 140. Lower Bound as Pruning Certificate

如果候選 plan 必然：

$$
C>B,
$$

可直接 prune。

不必真的跑到資源耗盡。

---

# 141. Impossibility vs Infeasibility Registry

分：

$$
\boxed{
\mathsf{Impossible}_{M}
}
$$

與：

$$
\boxed{
\mathsf{Infeasible}_{B}.
}
$$

前者是 model-relative computability / theorem lower-bound status。

後者是 budget status。

---

# 142. Resource Registry

第一個 MWT-09 runtime 模組：

$$
\boxed{
\mathsf{RR}.
}
$$

記錄：

- hardware；
- memory；
- agents；
- storage；
- network；
- external tools；
- budgets。

---

# 143. Complexity Contract Store

第二個模組：

$$
\boxed{
\mathsf{CCS}.
}
$$

保存：

- encoding；
- machine model；
- resource measure；
- asymptotic mode；
- version。

---

# 144. Offline / Online Ledger

第三個模組：

$$
\boxed{
\mathsf{OOL}.
}
$$

追蹤：

- precompute；
- training；
- indexing；
- cache；
- per-query marginal cost；
- amortization。

---

# 145. Proof-Cost Ledger

第四個模組：

$$
\boxed{
\mathsf{PCL}.
}
$$

保存：

- proof system；
- proof-search cost；
- length；
- verify cost；
- replay status。

---

# 146. Communication Ledger

第五個模組：

$$
\boxed{
\mathsf{CommL}.
}
$$

保存：

- messages；
- bits；
- rounds；
- participants；
- semantic transfer cost。

---

# 147. Feasibility Engine

第六個模組：

$$
\boxed{
\mathsf{FE}.
}
$$

輸入：

$$
(\widehat\kappa,B,\Gamma)
$$

輸出：

$$
\mathsf{Feasible/Infeasible/Deferred/Unknown/Conflicted}.
$$

---

# 148. Amortization Engine

第七個模組：

$$
\boxed{
\mathsf{AE}.
}
$$

計算：

- total；
- marginal；
- amortized；
- maintenance；
- migration。

---

# 149. Lower-Bound / Impossibility Registry

第八個模組：

$$
\boxed{
\mathsf{LIR}.
}
$$

對 planner 提供不可突破的已證 resource boundaries。

---

# 150. Resource Replan Engine

第九個模組：

$$
\boxed{
\mathsf{RRE}.
}
$$

當 plan 超 budget 時尋找：

- alternative；
- weaker valid answer；
- more agents；
- preprocessing；
- new representation；
- defer。

---

# 151. Resource-Aware Commit Gate

第十個模組：

$$
\boxed{
\mathsf{RCG}.
}
$$

commit 前確認：

- actual cost ledger complete；
- no hidden hard budget violation；
- evidence status 未因 resource degradation 被偷換；
- debt 已登錄。

---

# 152. Reference Resource Evaluator

本 Source Pack 附：

```text
mwt09_resource_reference.py
```

固定最低語義：

- typed resource vector；
- componentwise hard budget feasibility；
- Unknown cost；
- offline / online / amortized accounting；
- task-equivalent bypass guard；
- proof search / verify cost separate。

它不是 complexity theorem prover，也不判 P/NP。

---

# 153. MWT-09 Minimal Constitution

v0.1 固定三十二條：

### R1 — Truth Is Not Computability

真值／定理地位不自動提供 algorithm。

### R2 — Computability Is Not Complexity

能算不代表便宜。

### R3 — Complexity Is Not Instance Feasibility

asymptotic class 不決定目前 instance 是否跑得動。

### R4 — Feasibility Is Not Truth

budget 只影響可取得性。

### R5 — Unknown Is Not Undecidable

沒有 algorithm 不等於證明不存在 algorithm。

### R6 — Undecidable Is Not Merely Expensive

不存在 total decision algorithm 與超 budget 必須分離。

### R7 — Encoding Is Part of Complexity

input representation 不可省略。

### R8 — Machine Model Is Part of Complexity

不同 model 的 complexity claim 不可直接混。

### R9 — Resource Measures Are Typed

time、space、communication、proof、energy 不預設可合成單一 scalar。

### R10 — Worst/Average/Expected/Amortized Must Be Distinguished

不得偷換 complexity mode。

### R11 — Offline Cost Does Not Vanish

必要 preprocessing 必須在某 accounting boundary 出現。

### R12 — Online Speedup Can Be Real

承認 cache、training、representation rewrite 帶來真正 marginal speedup。

### R13 — Amortization Must State Workload

沒有 $N$ / query distribution，攤銷 claim 不完整。

### R14 — Advice/Oracle Must Be Declared

外部能力不可默認免費。

### R15 — Representation Rewrite Includes Translation Cost

不能只算新 solver。

### R16 — Size Blowup Must Be Tracked

representation 轉換後 input size 變化必須入 complexity。

### R17 — Bypass Requires Task-Identity Certificate

解不同問題不能冒充 speedup。

### R18 — Proof Existence Is Not Proof Discovery

provability 與 proof search 分離。

### R19 — Proof Length Is a Resource

短 proof / 長 proof 不同。

### R20 — Verification Is a Computation

certificate checking 也有 time/space cost。

### R21 — More Agents Are Not Free Speedup

通信、同步、重複工作必須入帳。

### R22 — Branch Count Is a Resource

非交換分支不能視為免費。

### R23 — Query Planning Has Cost

工具選擇與 obligation graph construction 也消耗資源。

### R24 — World Solve Includes Coupling Cost

不能只加 local solver FLOPs。

### R25 — Refinement Has Migration and Reopen Cost

新 dimension 不是免費。

### R26 — Stable Knowledge Has Maintenance Cost

certificate / dependency / archive 需要維護。

### R27 — Lower Bounds Are Contract-Relative

model / randomness / approximation / preprocessing 必須明示。

### R28 — Resource Replanning Cannot Weaken Claims Silently

資源不足時只能輸出較弱且標記的 status。

### R29 — Deferred Work Is Reopenable

新資源／新算法可重新啟動。

### R30 — Cost Estimates Are Versioned

估算器也可能漂移。

### R31 — Resource Debt Is Explicit

低成本 shortcut 的未清責任不能隱藏。

### R32 — Resource Accounting Returns to World State

重要 execution cost / debt / lower bound 應可進 MWT-04 state。

---

# 154. 命題：Online Cost Reduction Does Not Imply Total-Cost Reduction

存在 workflow：

$$
C_{\mathrm{offline}}
\gg0
$$

使：

$$
C_{\mathrm{online}}'
<
C_{\mathrm{online}},
$$

但：

$$
C_{\mathrm{offline}}
+
C_{\mathrm{online}}'
>
C_{\mathrm{online}}
$$

對第一次 query。

所以 online speedup 不推出 single-use total speedup。

---

# 155. 命題：Amortization Can Reverse the Comparison

若：

$$
C_{\mathrm{offline}}>0
$$

但：

$$
C_{\mathrm{online}}'
\ll
C_{\mathrm{online}},
$$

則存在足夠大：

$$
N
$$

使：

$$
C_{\mathrm{offline}}
+
N C_{\mathrm{online}}'
<
N C_{\mathrm{online}}.
$$

因此 preprocessing 可在 repeated workload 上真正降低 total cost。

---

# 156. 命題：Finite Proof Size Does Not Bound Search Cost

由定義：

$$
L_{\pi}<\infty
$$

只限制 proof representation size。

不提供：

$$
C_{\mathrm{search}}
$$

的上界。

因此：

$$
\boxed{
\text{short proof may still be hard to find}.
}
$$

---

# 157. 命題：Communication-Free Multi-Agent Speedup Cannot Be Assumed

若 task outputs 需要整合不同 agents 的 private states，

則至少需要某種 information transfer / shared-memory interaction。

所以把：

$$
C_{\mathrm{comm}}=0
$$

當預設是不合法的 complexity simplification。

---

# 158. 命題：Budget Violation Does Not Establish Uncomputability

若：

$$
\widehat T>B_T,
$$

只能推出：

$$
\mathsf{InfeasibleNow}
$$

在該 plan / budget。

不能推出：

$$
\mathsf{Uncomputable}.
$$

---

# 159. 條件定理：Componentwise Feasibility

若對所有 hard resource dimensions：

$$
i,
$$

都有 certified：

$$
\kappa_i(\chi)\leq B_i,
$$

且沒有 unresolved mandatory cost，

則：

$$
\boxed{
\Gamma
\vdash
\chi
\Downarrow_{\mathsf{Res}}
\mathsf{Feasible}.
}
$$

由本文 feasibility definition 成立。

---

# 160. 條件定理：Amortized Break-Even Point

若：

$$
C_{\mathrm{online}}'
<
C_{\mathrm{online}},
$$

則 preprocessing strategy 相對 baseline 的 break-even query count：

$$
\boxed{
N^\star
>
\frac{
C_{\mathrm{offline}}
}{
C_{\mathrm{online}}
-
C_{\mathrm{online}}'
}
}
$$

在忽略 maintenance / migration 且成本可加的簡化模型下成立。

這是工程比較，不是 universal complexity theorem。

---

# 161. 研究猜想：AI Mathematics Is Primarily Amortized

長期 AI 數學系統的優勢可能大量來自：

- theorem cache；
- bridge reuse；
- formal library；
- learned search policy；
- world-state persistence；

使 repeated related queries 的 marginal cost 持續下降。

---

# 162. 研究猜想：Proof Search Becomes the Dominant Scarce Resource

當 checker 越來越可靠且平行化後，某些大型 theorem 的真正瓶頸可能更集中於：

$$
\boxed{
\text{finding compact global certificates}
}
$$

而不是 checking 已知 certificate。

---

# 163. 研究猜想：Communication-Limited Multi-AI Mathematics

當 agent 數量極大時，瓶頸可能從 local reasoning 轉向：

- context synchronization；
- evidence dedup；
- proof transport；
- global merge。

因此 AI 海戰術存在 communication phase transition。

---

# 164. 研究猜想：Representation Rewrite as Complexity Engineering

對固定 task distribution，AI 自動生成新 presentation / bridge 可能成為一種真正的 complexity engineering：

$$
\boxed{
\text{pay once to reshape problem space}
\rightarrow
\text{reduce repeated future cost}.
}
$$

但其收益必須以 total / amortized accounting驗證。

---

# 165. 開放問題

### O1 — Universal Resource Vector

是否存在足夠小但高覆蓋的 MWT resource vocabulary？

### O2 — Cross-Model Complexity Translation

不同 machine / presentation 的 complexity 如何合法比較？

### O3 — Hidden Precomputation

如何偵測模型輸出中被 training / cache 隱藏的歷史成本？

### O4 — Proof Search Cost

如何對 agentic proof search 建立可預測 upper / lower bounds？

### O5 — Multi-AI Communication

多 agent theorem proving 的 communication complexity 如何形式化？

### O6 — Query Planning Complexity

生成最小充分 obligation graph 本身有多難？

### O7 — Branch Complexity

contextual trace quotient 下的真正有效 branch complexity 如何量測？

### O8 — Dynamic Resource Classes

world state 持續 refinement 時，problem family 的 complexity class 如何版本化？

### O9 — Long-Horizon Amortization

多年 world-state 投資如何公平分攤到未來 queries？

### O10 — Feasible Universal Proof

存在短 theorem statement但任何已知 proof 都超大時，AI 應如何管理 Stable Core？

---

# 166. 外部研究接口：Turing Computability

Turing 的《On Computable Numbers, with an Application to the Entscheidungsproblem》建立現代 computability 的核心模型，並展示存在 algorithmic undecidability。

MWT-09 以此保留：

$$
\boxed{
\text{well-defined mathematical task}
\not\Rightarrow
\text{total decision algorithm}.
}
$$

---

# 167. 外部研究接口：Hartmanis–Stearns Complexity

Hartmanis 與 Stearns 1965 的工作系統化研究 algorithm 所需 computation resources，並奠定 complexity hierarchy 的早期核心。

MWT 以此作「computability 與 resource complexity 分離」的經典接口。

---

# 168. 外部研究接口：Blum Complexity Measures

Blum 1967 建立 machine-independent complexity-measure framework，強調合法 complexity measure 本身需要形式條件。

MWT 不重建 Blum theory，而吸收：

$$
\boxed{
\text{resource measure must be declared, not rhetorically invented}.
}
$$

---

# 169. 外部研究接口：Cook

Cook 1971 的 theorem-proving complexity 工作將 efficient verification、nondeterministic computation 與 NP-completeness 的現代結構推到核心位置。

MWT 將 solve / witness / verify / proof search 分離，避免把它們混成一個「難」。

---

# 170. 外部研究接口：Savitch

Savitch 1970 對 nondeterministic 與 deterministic tape complexity 的關係展示：

$$
\boxed{
\text{space}
}
$$

有獨立於 time 的理論結構。

因此 MWT resource profile 永遠至少允許 time / space 分離。

---

# 171. 外部研究接口：Cook–Reckhow Proof Complexity

Cook 與 Reckhow 1979 建立 propositional proof systems relative efficiency 的經典框架。

MWT 將其作：

- proof length；
- proof-system selection；
- simulation overhead；

的外部理論接口。

---

# 172. 外部研究接口：Yao Communication Complexity

Yao 1979 將 distributed parties 為計算 function 所需 communication 提升成 complexity 問題。

這直接支援 MWT multi-AI / solver federation 的：

$$
C_{\mathrm{comm}}.
$$

---

# 173. 與解空間幾何計算論的接口

既有 GCS 已指出：

- 表示可以改寫；
- 工具可以增加；
- 任務等價終態可以建立；
- 歷史概念積分可形成幾何快速通道。

MWT-09 不否定這些現象，而是要求每一種 speedup 回答：

$$
\boxed{
\text{cost moved where?}
}
$$

以及：

$$
\boxed{
\text{task identity preserved嗎?}
}
$$

---

# 174. 與 P/NP 動態速率主線的接口

既有動態速率思想可重新定位為：

$$
\boxed{
\text{history-conditioned effective computation rate}.
}
$$

它可以研究：

- preprocessing；
- amortization；
- representation learning；
- reusable world state。

但不能無條件替代 classical P/NP quantifier / machine model。

---

# 175. 與 MWT-08 的接口

MWT-08 生成：

$$
C_{\forall}.
$$

MWT-09 問：

- 找得到嗎？
- 多大？
- 驗得完嗎？
- 存得下嗎？

因此：

$$
\boxed{
\text{logical sufficiency}
\neq
\text{resource sufficiency}.
}
$$

---

# 176. 與 MWT-07 的接口

Query Planner 不只 route capability，也要 route：

$$
\boxed{
\text{capability}
+
\text{cost}
+
\text{budget}.
}
$$

---

# 177. 與 MWT-06 的接口

World Solve 的 solver federation 要帶：

- local cost；
- coupling cost；
- communication；
- iteration count；
- transfer；
- rollback。

---

# 178. 與 MWT-05 的接口

refinement 可以增加能力，也會增加：

- dimension；
- state；
- migration；
- maintenance cost。

因此 refinement admission 必須讀 Resource Layer。

---

# 179. 與 MWT-04 的接口

resource debt、deferred tasks、actual cost、lower-bound certificates都可進：

$$
\mathcal U_t,
\quad
\mathcal V_t,
\quad
\mathcal R_t.
$$

新資源可以 reopen。

---

# 180. MWT-01～09 的鏈

現在 MWT 可以寫成：

$$
\boxed{
\begin{aligned}
\text{Present}
&\rightarrow
\text{Judge}\\
&\rightarrow
\text{Schedule}\\
&\rightarrow
\text{World-State}\\
&\rightarrow
\text{Refine}\\
&\rightarrow
\text{Couple}\\
&\rightarrow
\text{Query}\\
&\rightarrow
\text{Quantify}\\
&\rightarrow
\text{Account Resources}\\
&\rightarrow
\text{Execute / Defer / Replan}\\
&\rightarrow
\text{Update / Reopen}.
\end{aligned}
}
$$

---

# 181. 下一篇接口

下一篇最自然的是：

# **MWT-10：World Memory, Compression, and Long-Horizon Mathematical Persistence**

因為 MWT-09 已經證明：

> 知識不是免費保存的。

下一步就必須處理：

$$
\boxed{
\text{一個運行十年、百年的 AI 數學世界，
怎麼記住自己而不被自己的歷史淹死？}
}
$$

MWT-10 將處理：

- operational memory；
- archival memory；
- proof compression；
- dependency-aware forgetting；
- reconstructability；
- cache；
- semantic deduplication；
- memory tiers；
- long-horizon provenance；
- catastrophic context inflation；
- reopenable compressed history。

---

# 182. 一句話版

> **MWT-09 將「數學上存在解／證明」與「AI 現在取得得了」徹底分離：computability、decidability、proof existence、proof search、proof length、verification、time、space、parallel work/span、communication、branch、I/O、transfer、external tool 與 human cost 都是不同的 resource axes。AI 可以靠 training、cache、representation rewrite、precomputation 與長期 world-state 把 online solve 壓得極短，但必要歷史成本必須在 total、marginal 或 amortized accounting 中出現；若繞過原問題，也必須有 task-identity certificate。MWT 因此不把「理論上能做」等同「目前做得到」，也不把「做不到目前 budget」等同「不可計算」——它建立的是一個能精確說明成本在哪裡、什麼現在可負擔、什麼應延後、什麼需要新算法或新硬體重新開啟的資源有界數學世界。**

---

# 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $\chi$ | Computation Episode |
| $\mathsf{CapProf}$ | capability profile |
| $\mathfrak C_{\kappa}$ | Complexity Contract |
| $\kappa(\chi)$ | typed Resource Cost Profile |
| $T$ | time |
| $S$ | space / memory |
| $W$ | total work |
| $D$ | span / critical path |
| $C_{\mathrm{comm}}$ | communication cost |
| $C_{\mathrm{io}}$ | I/O cost |
| $C_{\mathrm{transfer}}$ | representation/scale transfer cost |
| $C_{\mathrm{proof}}$ | proof generation/search cost |
| $L_{\mathrm{proof}}$ | proof length |
| $C_{\mathrm{verify}}$ | proof/certificate verification cost |
| $N_{\mathrm{branch}}$ | branch cost/count |
| $B_t$ | resource budget vector |
| $C_{\mathrm{offline}}$ | preprocessing/history investment |
| $C_{\mathrm{online}}$ | marginal online cost |
| $\overline C_N$ | amortized cost |
| $\mathcal F_B$ | feasible algorithm region |
| $D_{\mathrm{res}}$ | resource debt |
| $\mathsf{RR}$ | Resource Registry |
| $\mathsf{CCS}$ | Complexity Contract Store |
| $\mathsf{OOL}$ | Offline/Online Ledger |
| $\mathsf{PCL}$ | Proof-Cost Ledger |
| $\mathsf{CommL}$ | Communication Ledger |
| $\mathsf{FE}$ | Feasibility Engine |
| $\mathsf{AE}$ | Amortization Engine |
| $\mathsf{LIR}$ | Lower-Bound / Impossibility Registry |
| $\mathsf{RRE}$ | Resource Replan Engine |
| $\mathsf{RCG}$ | Resource-Aware Commit Gate |

---

# 附錄 B：v0.1 非主張清單

MWT-09 不主張：

1. 所有數學真理都可計算；
2. 所有可計算問題都可判定；
3. 所有可判定問題都實際可負擔；
4. polynomial time 永遠在實務快速；
5. exponential time 永遠在所有 instance 不可用；
6. verification 永遠比 discovery 便宜；
7. 有 proof 就一定容易找到 proof；
8. proof 很短就一定容易生成；
9. proof 很長就一定無法 streaming verify；
10. time 是唯一 complexity resource；
11. space 可以由 time 完全取代；
12. communication 在 multi-AI 中可以忽略；
13. 更多 agents 永遠更快；
14. cache / training 是免費；
15. offline cost 每次 query 都必須完整重算；
16. amortized cost 可不指定 workload；
17. representation rewrite 自動改善 classical complexity class；
18. input encoding 可以任意把答案預編碼而不計成本；
19. oracle / advice 可以默認免費；
20. task bypass 永遠等於原問題求解；
21. dynamic rate theory 已證明 P=NP 或 P≠NP；
22. feasibility 是數學真值；
23. budget exhaustion 是 undecidability；
24. unknown algorithm 等於不存在 algorithm；
25. 所有 resource dimensions 可合成 universal scalar；
26. 所有 lower bounds 跨 machine models 保持；
27. proof systems 的 shortest proof 都可計算取得；
28. MWT 能自動預測任何 computation 的 exact cost；
29. world-state 越大越好；
30. resource debt 沒有長期成本；
31. AI hardware 增加會改變所有 formal computability results；
32. MWT-09 是經典 complexity theory 的替代品。

---

# 附錄 C：外部研究接口與參考文獻

1. A. M. Turing, **On Computable Numbers, with an Application to the Entscheidungsproblem**, *Proceedings of the London Mathematical Society*, Series 2, 42, 1936/1937, pp. 230–265. DOI: 10.1112/plms/s2-42.1.230.  
2. Juris Hartmanis and Richard E. Stearns, **On the Computational Complexity of Algorithms**, *Transactions of the American Mathematical Society*, 117, 1965, pp. 285–306. DOI: 10.1090/S0002-9947-1965-0170805-7.  
3. Manuel Blum, **A Machine-Independent Theory of the Complexity of Recursive Functions**, *Journal of the ACM*, 14(2), 1967, pp. 322–336. DOI: 10.1145/321386.321395.  
4. Stephen A. Cook, **The Complexity of Theorem-Proving Procedures**, STOC 1971, pp. 151–158. DOI: 10.1145/800157.805047.  
5. Walter J. Savitch, **Relationships between Nondeterministic and Deterministic Tape Complexities**, *Journal of Computer and System Sciences*, 4(2), 1970, pp. 177–192. DOI: 10.1016/S0022-0000(70)80006-X.  
6. Stephen A. Cook and Robert A. Reckhow, **The Relative Efficiency of Propositional Proof Systems**, *The Journal of Symbolic Logic*, 44(1), 1979, pp. 36–50. DOI: 10.2307/2273702.  
7. Andrew Chi-Chih Yao, **Some Complexity Questions Related to Distributive Computing (Preliminary Report)**, STOC 1979, pp. 209–213. DOI: 10.1145/800135.804414.  

---

# 附錄 D：內部依賴

MWT-09 直接依賴：

- MWT-01《World Primitive 與 Presentation Theory》
- MWT-02《Global Legality Calculus》
- MWT-03《Global Interaction Graph and Noncommutative Scheduler》
- MWT-04《World State, Branch Convergence, and Dynamic Fixed Points》
- MWT-05《Unbounded Refinement, World Expansion, and Resolution Dynamics》
- MWT-06《Global Coupling Calculus and Multi-Resolution World Solve》
- MWT-07《Global Query Semantics, World Inference, and Proof/Computation Federation》
- MWT-08《Global Quantification, Coverage, and Universal Proof Obligations》
- 《超越 P/NP 二分：解空間幾何計算論的總命題》
- 《動態速率理論與 P vs. NP 問題的結構連續模型》
- 《P/NP 的量詞張力重構》
- P/NP 數學構造狀態機主線

本文接受「空間改寫與歷史累積可以改變有效求解成本」，但要求把 classical complexity、online complexity、amortized cost 與 task identity 分離。

