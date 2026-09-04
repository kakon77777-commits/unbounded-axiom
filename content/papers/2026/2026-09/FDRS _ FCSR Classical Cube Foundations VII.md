# FDRS / FCSR Classical Cube Foundations VII
## 可驗證 Solver：Soundness、Completeness、Optimality 與解證書

**英文題名：** Verified Solvers: Soundness, Completeness, Optimality, and Solution Certificates  
**系列：** FDRS / FCSR Classical Cube Foundations  
**系列編號：** EML-FDRS-FCSR-CUBE-07  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構：** 一言諾科技有限公司（EveMissLab）  
**狀態：** Orthodox Origin Continuation / 經典地基第七篇

---

## 摘要

前六篇已建立合法狀態、表示、搜尋、heuristic、Pattern Database、pruning 與 Two-Phase。本文處理最後一個經典 solver 地基問題：當程式宣稱「我解了」「我一定能解」「這是最短解」時，這三句話各自需要什麼數學證據？

本文嚴格區分三種性質。Soundness 是輸出層性質：若 solver 回傳 move sequence $p$，則重播 $p$ 必須到達目標。Completeness 是演算法層性質：對指定 domain 中每個可解狀態，在沒有外部資源中止的條件下，solver 最終都會回傳某個解。Optimality 是最短性質：solver 回傳的解成本等於真實最短距離。

本文主張高速搜尋器本身不必全部進入 trusted computing base。可以採用：

$$
\boxed{
\text{Untrusted Searcher}
+
\text{Trusted Checker}
}
$$

Searcher 只負責提出候選 move sequence；Checker 在 canonical move semantics 上重播並驗證。若 Checker 的 soundness theorem 已在 Lean 4 中證明，則任意外部 solver、GPU solver、AI solver 或 Two-Phase implementation 都可以成為不可信候選生成器，而不會擴張最終「解得正確」的信任面。

對 optimality，本文提出雙證書架構。合法解 $p$ 給出上界：

$$
d(s,G)\leq C(p).
$$

一個已證 admissible 的 lower-bound certificate $h$ 給出：

$$
h(s)\leq d(s,G).
$$

若：

$$
h(s)=C(p)=L,
$$

便得到：

$$
d(s,G)=L.
$$

因此最短性不必依賴「相信 solver 已經窮舉所有更短路徑」，而可以由 upper-bound solution certificate 與 lower-bound proof certificate 夾逼得到。

本文亦提出一個特別適合 PDB / pruning table 的驗證方式：若有限抽象圖上的表值 $h$ 滿足目標值為 $0$，且對每條抽象 edge 滿足一致性不等式

$$
h(x)\leq c(x,y)+h(y),
$$

則沿任意到目標路徑反覆套用可得

$$
h(x)\leq d(x,G).
$$

所以不必把巨型 PDB 的建立演算法全部納入 trusted base；可以把 table 當成不可信資料，再用可驗證的 local constraints 建立 global lower-bound guarantee。

最後，本文為 Lean / runtime 定義 SolutionCertificate、LowerBoundCertificate、OptimalityCertificate、SearchResult 與 VerificationReport，並將 Two-Phase 的 phase certificates 組合進同一證明架構。至此，FCSR/FDRS 經典魔方線第一次具備「演算法可以自由競爭，但輸出保證由獨立證明層統一裁決」的完整設計。

**關鍵詞：** verified solver、soundness、completeness、optimality、certificate checker、Lean 4、proof-carrying search、PDB verification、FCSR、FDRS

---

## 1. 三句看似相同、其實完全不同的話

對 solver：

$$
\operatorname{Solve}:S\rightarrow\operatorname{Result},
$$

以下三句不能混在一起。

### 1.1 「它找到的解是真的」

這是：

$$
\text{Soundness}.
$$

### 1.2 「只要有解，它最後一定找得到」

這是：

$$
\text{Completeness}.
$$

### 1.3 「它找到的是最短解」

這是：

$$
\text{Optimality}.
$$

三者的證明責任不同。

---

## 2. Solution predicate

令目標集合為：

$$
G\subseteq S.
$$

定義：

$$
\operatorname{Solves}(s,p)
\iff
T^\ast(s,p)\in G.
$$

對標準 solved-cube goal：

$$
G=\{s_\star\}.
$$

因此：

$$
\operatorname{Solves}(s,p)
\iff
T^\ast(s,p)=s_\star.
$$

這個 predicate 應該是所有 solver、UI、checker 與 Lean theorem 共用的唯一解語義。

---

## 3. 解序列本身就是最小型證書

若 searcher 回傳：

$$
p=(a_1,\ldots,a_k),
$$

則 checker 不需要理解 searcher 為何選這些 moves。

它只需要重播：

$$
s_{i+1}=T(s_i,a_i)
$$

並檢查：

$$
s_k\in G.
$$

所以：

$$
\boxed{
p
=
\text{solution certificate}.
}
$$

這是一種 proof-carrying computation：計算者回傳結果，也回傳可獨立重播的 witness。

---

## 4. Trusted checker

定義 executable checker：

$$
\operatorname{checkSolution}(s,p):\operatorname{Bool}.
$$

理想 Lean theorem：

$$
\boxed{
\operatorname{checkSolution}(s,p)=\mathrm{true}
\Rightarrow
\operatorname{Solves}(s,p).
}
$$

若再證 converse：

$$
\operatorname{Solves}(s,p)
\Rightarrow
\operatorname{checkSolution}(s,p)=\mathrm{true},
$$

則 checker 與 specification 完全對應。

但對安全架構而言，第一個方向已足以建立 soundness。

---

## 5. Searcher 可以不可信

因此 solver architecture 可以拆成：

```text
Fast / Untrusted Searcher
        ↓
candidate path p
        ↓
Trusted Canonical Checker
        ↓
VerifiedSolution or Reject
```

Searcher 可以是：

- BFS；
- IDA*；
- Kociemba Two-Phase；
- native C++；
- WebAssembly；
- GPU；
- 外部 library；
- AI-generated solver；
- 未形式化的新算法。

只要 candidate path 最終通過同一 checker：

$$
\operatorname{checkSolution}(s,p)=\mathrm{true},
$$

其 solution soundness 不依賴 searcher 內部正確性。

---

## 6. Trusted computing base 的縮小

若整個高效 Two-Phase implementation 都必須形式化，trusted proof surface 很大。

但如果只信任：

1. canonical state；
2. move semantics；
3. path replay；
4. checker soundness theorem；

則高速 solver 只是候選生成器。

因此 trusted core 可以縮成：

$$
\boxed{
\text{State Kernel}
+
\text{Move Kernel}
+
\text{Certificate Checker}.
}
$$

這也是實際工程最值得優先形式化的部分。

---

## 7. Soundness theorem

solver-level soundness 可以寫為：

$$
\forall s,p,
\operatorname{Solve}(s)=\operatorname{Solved}(p)
\Rightarrow
\operatorname{Solves}(s,p).
$$

若 solver 的所有 `Solved` 結果在返回前都經過 checker：

$$
\operatorname{checkSolution}(s,p)=\mathrm{true},
$$

且 checker soundness 已證，solver soundness 可以由 wrapper theorem 得到。

---

## 8. 「ResourceLimit」不違反 soundness

假設 solver 對某些狀態回：

$$
\operatorname{ResourceLimit}.
$$

這不代表 soundness 失敗。

Soundness 只限制：

> 若你宣稱 `Solved(p)`， $p$ 必須真的解。

所以一個只解部分案例、但從不回傳錯誤解的 solver，可以是 sound 的。

這再次說明：

$$
\text{soundness}
\neq
\text{completeness}.
$$

---

## 9. Completeness 的正式定義

對 domain：

$$
D\subseteq S,
$$

solver completeness 可定義為：

$$
\forall s\in D,
\operatorname{ReachableGoal}(s)
\Rightarrow
\exists p,
\operatorname{Solve}(s)=\operatorname{Solved}(p).
$$

若標準合法魔方的每個狀態皆可到 solved state，則可寫：

$$
\forall s\in S_{\mathrm{legal}},
\exists p,
\operatorname{Solve}(s)=\operatorname{Solved}(p).
$$

但這是一個演算法／termination 性質，不是一條解序列本身能證明的事情。

---

## 10. Completeness 通常需要條件化

實際 solver 有：

- timeout；
- memory cap；
- node cap；
- cancellation；
- bounded depth。

所以更精確的 theorem 是：

$$
\boxed{
\text{若不被外部資源限制中止，
則 solver 在 domain }D\text{ 上 complete}.
}
$$

因此 API 中：

```text
ResourceLimit
BoundExceeded
Cancelled
```

不能被解讀成：

```text
NoSolution
```

---

## 11. Finite graph completeness

對 finite graph：

$$
|V|<\infty,
$$

若 BFS：

- successor generation 完整；
- duplicate handling 正確；
- queue 不被外部截斷；

則 reachable goal 最終會被探索到。

這提供 BFS completeness 的標準證明模板。

對 IDA*，則需要證 threshold progression 不會永遠停在低於 optimal cost 的值，且每個 threshold 內的 admissible candidate paths 被完整探索。

---

## 12. Two-Phase completeness 是可組合的

若 Phase 1 對所有：

$$
s\in G
$$

都能找到：

$$
p_1
$$

使：

$$
T^\ast(s,p_1)\in G_1,
$$

且 Phase 2 對所有：

$$
s_1\in G_1
$$

都能找到：

$$
p_2
$$

使：

$$
T^\ast(s_1,p_2)=e,
$$

則 phase composition complete。

但實際 implementation 若丟棄 candidates 或設定資源限制，必須把數學 phase completeness 與工程 completeness 分開報告。

---

## 13. Optimality predicate

令 path cost：

$$
C(p).
$$

定義：

$$
\operatorname{Optimal}(s,p)
$$

當且僅當：

$$
\operatorname{Solves}(s,p)
$$

且：

$$
\forall q,
\operatorname{Solves}(s,q)
\Rightarrow
C(p)\leq C(q).
$$

等價於：

$$
C(p)
=
d(s,G).
$$

因此 optimality 至少包含 soundness。

---

## 14. 找到一條解只給上界

若：

$$
\operatorname{Solves}(s,p)
$$

且：

$$
C(p)=L,
$$

則只能推出：

$$
d(s,G)\leq L.
$$

這是一個 upper bound。

所以：

> 「我有一條 $18$ 步解」

不等於：

> 「這顆魔方最短距離就是 $18$ 」。

---

## 15. Lower-bound certificate

若另有：

$$
\ell(s)
$$

滿足：

$$
\ell(s)\leq d(s,G),
$$

則：

$$
\ell(s)
$$

是一個 lower bound。

若：

$$
\ell(s)=L
$$

且已有一條成本：

$$
L
$$

的 solution path，則：

$$
L
\leq
d(s,G)
\leq
L.
$$

因此：

$$
\boxed{
d(s,G)=L.
}
$$

這就是本文的 optimality sandwich。

---

## 16. Optimality certificate = Upper + Lower

定義：

$$
\operatorname{UpperCert}(s)
=
p
$$

其中：

$$
C(p)=L
$$

且：

$$
\operatorname{Solves}(s,p).
$$

定義：

$$
\operatorname{LowerCert}(s)
=
(\ell,\pi_\ell)
$$

其中：

$$
\pi_\ell:
\ell(s)\leq d(s,G).
$$

若：

$$
\ell(s)=C(p),
$$

則形成：

$$
\boxed{
\operatorname{OptimalityCertificate}.
}
$$

這比「信任 optimal solver」更模組化。

---

## 17. Heuristic 本身可以成為 lower-bound certificate

第五篇已建立：

$$
h(s)\leq h^\ast(s)=d(s,G).
$$

因此任何已證 admissible heuristic 都可提供 lower bound。

若 solver 找到：

$$
C(p)=h(s),
$$

則立即證明 optimal。

這是 heuristic 從「搜尋工具」升級為「證明工具」的關鍵一步。

---

## 18. 一致性表可以用局部約束證明全域下界

考慮有限抽象圖：

$$
\Gamma_A=(A,E,c).
$$

給一張表：

$$
h:A\rightarrow\mathbb N.
$$

若：

$$
h(g)=0
$$

對所有 abstract goals 成立，且每條 edge：

$$
x\rightarrow y
$$

都滿足：

$$
h(x)\leq c(x,y)+h(y),
$$

則對任意 path：

$$
x=x_0\rightarrow x_1\rightarrow\cdots\rightarrow x_k=g
$$

反覆套用可得：

$$
h(x)
\leq
\sum_{i=0}^{k-1}c(x_i,x_{i+1}).
$$

對所有到 goal 的 path 取 minimum：

$$
\boxed{
h(x)\leq d_A(x,G).
}
$$

所以局部 consistency checks 可以產生 global lower-bound guarantee。

---

## 19. 這讓巨大 PDB 可以在 trusted base 外建立

PDB builder 可以是不可信程式。

它輸出：

$$
h:A\rightarrow\mathbb N.
$$

Verified PDB checker 再檢查：

1. 所有 goal：

$$
h(g)=0;
$$

2. 所有抽象 edges：

$$
h(x)\leq c(x,y)+h(y).
$$

若全部通過，便可證：

$$
h(x)\leq d_A(x,G).
$$

若 abstraction 本身已證：

$$
d_A(\alpha(s),\alpha(G))
\leq
d_S(s,G),
$$

則組合得到：

$$
h(\alpha(s))
\leq
d_S(s,G).
$$

這樣 table generation、壓縮、平行化都可以自由優化，而最終 admissibility 仍由獨立 checker 保證。

---

## 20. Checksum 不是數學證明

工程上可以對 PDB 保存：

$$
\operatorname{SHA256}(\mathrm{table})
$$

來保護檔案完整性。

但：

$$
\boxed{
\text{checksum integrity}
\neq
\text{heuristic correctness}.
}
$$

checksum 只能說：

> 這個檔案和先前那份相同。

它不能說：

> 表內數字一定是合法 lower bounds。

所以應分：

```text
IntegrityVerified
LowerBoundVerified
ExactDistanceVerified
```

三種不同狀態。

---

## 21. Exact PDB 與 Lower-Bound PDB 也應區分

若 table 真正滿足：

$$
h(x)=d_A(x,G),
$$

則它是 exact abstract-distance PDB。

但對 optimality search，其實只需要：

$$
h(x)\leq d_A(x,G).
$$

所以：

$$
\boxed{
\text{Exactness is stronger than admissibility}.
}
$$

若壓縮或近似方式保留 lower-bound property，即使 table 不再儲存 exact distance，仍可能安全用於 optimal search。

---

## 22. IDA* exhaustion 也可以構成 lower-bound 證據

假設 verified IDA* 完整探索所有：

$$
f\leq\theta
$$

的 search nodes，並證明其中不存在 goal。

則可推出：

$$
d(s,G)>\theta.
$$

如果接著找到成本：

$$
\theta+1
$$

的解，就可證 optimal。

因此另一種 optimality proof 是：

$$
\boxed{
\text{complete exhaustion below }L
+
\text{solution of cost }L.
}
$$

只是這要求信任／形式化更多 search-control logic，trusted surface 比單純 solution checker 大。

---

## 23. Optimality 的三條驗證路徑

### 路徑 A：Lower bound meets upper bound

$$
h(s)=C(p).
$$

最乾淨。

### 路徑 B：Verified exhaustive search

完整證明所有：

$$
C<L
$$

的候選都不存在。

### 路徑 C：External proof certificate

外部 solver 產生一個可以由小 checker 驗證的 no-shorter-solution certificate。

例如未來可以研究：

- SAT/SMT unsat proof；
- exhaustive frontier certificate；
- quotient-distance certificate；
- symmetry-reduced proof object。

本系列第一版優先 A。

---

## 24. SolutionCertificate

建議 canonical artifact：

```text
SolutionCertificate
  puzzleSpecHash
  metric
  startState
  moveSequence
  finalState
  cost
  checkerVersion
  stateKernelVersion
```

其核心可驗證內容為：

$$
T^\ast(s_0,p)=s_\star.
$$

其他 hash / version metadata 用於重現與工程完整性，而不是取代數學 proof。

---

## 25. LowerBoundCertificate

概念：

```text
LowerBoundCertificate
  method
  representation
  startIndex
  lowerBound
  proofRef
  tableHash
  verifierVersion
```

`method` 可包括：

```text
VerifiedHeuristic
VerifiedPDB
VerifiedExhaustion
ExternalProof
```

核心 theorem 永遠是：

$$
L_{\mathrm{low}}
\leq
d(s,G).
$$

---

## 26. OptimalityCertificate

把兩邊組合：

```text
OptimalityCertificate
  solutionCertificate
  lowerBoundCertificate
  equalityProof
```

要求：

$$
C(p)
=
L_{\mathrm{low}}.
$$

然後輸出：

$$
\operatorname{Optimal}(s,p).
$$

UI 可以明確顯示：

```text
Solution: 18 HTM
Verified upper bound: 18
Verified lower bound: 18
Optimality: PROVEN
```

---

## 27. 若上下界沒碰到，不應假裝知道 exact distance

例如：

$$
L_{\mathrm{low}}=16,
$$

$$
L_{\mathrm{upper}}=18.
$$

正確結果是：

$$
16
\leq
d(s,G)
\leq
18.
$$

UI 應顯示：

```text
Exact distance: unresolved
Certified interval: [16, 18]
```

而不是只把 $18$ 顯示成「distance」。

---

## 28. VerificationReport

統一報告：

```text
VerificationReport
  stateValidity
  solutionSoundness
  lowerBoundStatus
  optimalityStatus
  completenessClaim
  resourceLimits
  proofDependencies
```

例如 Two-Phase：

```text
stateValidity: verified
solutionSoundness: verified
lowerBoundStatus: phase-specific only
optimalityStatus: unknown
completenessClaim: conditional
```

Optimal IDA*：

```text
solutionSoundness: verified
lowerBoundStatus: verified
optimalityStatus: proven
```

---

## 29. Two-Phase 證書的組合

第六篇已有：

$$
p=p_1\mathbin{+\!\!+}p_2.
$$

可以保存：

```text
Phase1Certificate
  path
  boundaryState
  inG1Proof

Phase2Certificate
  path
  solvedProof
```

再由 composition theorem 得：

$$
\operatorname{Solves}
(
s_0,
p_1\mathbin{+\!\!+}p_2
).
$$

因此 Two-Phase soundness 很適合 compositional proof。

---

## 30. Two-Phase optimality 不能由兩個 phase soundness 推出

即使：

$$
p_1
$$

是最短進入 $G_1$ 的路，

且：

$$
p_2
$$

是從該 boundary state 到 solved 的最短路，

也不能推出：

$$
p_1++p_2
$$

是 full cube global optimal。

因為可能有另一個 boundary：

$$
b'
$$

讓：

$$
d(s,b')+d_{G_1}(b',e)
$$

更小。

所以：

$$
\boxed{
\text{phase optimal}
\not\Rightarrow
\text{global optimal}.
}
$$

---

## 31. Completeness certificate 不適合做成單一 per-instance 檔案

Soundness 可以由一條 move sequence逐例驗證。

Optimality也可以由 upper / lower bounds逐例驗證。

但 algorithm completeness 是：

$$
\forall s\in D
$$

的全域性質。

因此它更適合：

- Lean theorem；
- algorithm proof；
- finite-domain exhaustive meta-proof；

而不是每個 solve result 都附一份巨型 completeness certificate。

這是證書架構的重要邊界。

---

## 32. Solver guarantee lattice

可以把保證分層：

```text
Candidate
  ↓
Sound
  ↓
Complete-on-Domain
```

而 optimality 是另一條正交軸：

```text
Sound Solution
  ↓
Bounded [L,U]
  ↓
Globally Optimal
```

所以 solver quality 不是一維排序。

例如：

- Two-Phase：高 practical performance，sound，可條件 complete，但通常 optimality unknown；
- Verified BFS on small puzzle：sound、complete、optimal，但 scalability 低；
- AI proposal + checker：sound output，但 completeness / optimality 未知。

---

## 33. AI solver 的正確接入方式

未來 AI 可以提出：

$$
p_{\mathrm{AI}}.
$$

但系統不需要問：

> AI 到底有沒有真正「理解」魔方？

對 solution correctness，只需：

$$
\operatorname{checkSolution}(s,p_{\mathrm{AI}})
=
\mathrm{true}.
$$

AI 可以：

- 發明 heuristic；
- 建議 phase；
- 生成 move sequence；
- 選擇 representation；
- 壓縮 search policy。

但 correctness 由外部形式層裁決。

這使 AI experimentation 與 proof safety 可以解耦。

---

## 34. Searcher–Checker 分離對 FDRS 的意義

FDRS 起源強調不同表示與觀察層。

現在我們再增加：

$$
\text{Generator View}
$$

與：

$$
\text{Verifier View}.
$$

Generator 可以在任何方便的 representation：

$$
R_{\mathrm{search}}
$$

中工作。

Verifier 則回到 canonical semantics：

$$
R_{\mathrm{canonical}}.
$$

因此：

$$
\boxed{
\text{可以在壓縮／抽象空間中找答案，
再回到 canonical world 驗證答案。}
}
$$

這是一個非常乾淨的 FDRS 計算閉環。

---

## 35. Proof-producing representation bridge

若 searcher 使用 coordinate：

$$
x=R(s),
$$

而 checker 使用 canonical state：

$$
s,
$$

則至少要有已驗證 bridge：

$$
R(T(s,a))
=
M_a(R(s)).
$$

否則 searcher 的內部 coordinate semantics 可能與 canonical move semantics 漂移。

最安全的方法仍是：

> Searcher 的內部可以自由，但最終 move certificate 必須在 canonical kernel 重播。

如此即使 coordinate implementation 有 bug，也只會讓 searcher 找不到好解，而不會讓錯解通過 verifier。

---

## 36. Lean 4 核心型別建議

概念：

```text
structure SolutionCertificate where
  moves : List Move

def Solves (s : ValidCubeState) (c : SolutionCertificate) : Prop :=
  applyMoves s c.moves = solved
```

Checker：

```text
def checkSolution (s) (c) : Bool :=
  decide (applyMoves s c.moves = solved)
```

核心 theorem：

```text
theorem checkSolution_sound :
  checkSolution s c = true ->
  Solves s c
```

再將所有高速 solver 包成：

```text
def verifyCandidate (s) (p) :=
  if checkSolution s p then
    VerifiedSolution
  else
    Reject
```

---

## 37. Lower-bound proof interface

抽象：

```text
structure LowerBoundWitness where
  value : Nat
  valid : value <= distanceToGoal s
```

若不希望直接把昂貴的 `distanceToGoal` 放進 executable code，可以透過 theorem-backed abstraction：

```text
CertifiedHeuristic
  eval : State -> Nat
  admissible : forall s, eval s <= distanceToGoal s
```

因此：

$$
\operatorname{eval}(s)
$$

本身就是 lower-bound witness value。

---

## 38. Optimality theorem

若：

$$
\operatorname{Solves}(s,p),
$$

$$
h(s)\leq d(s,G),
$$

且：

$$
C(p)=h(s),
$$

則：

$$
\operatorname{Optimal}(s,p).
$$

證明：

由 solution：

$$
d(s,G)\leq C(p).
$$

由 admissibility：

$$
h(s)\leq d(s,G).
$$

又：

$$
C(p)=h(s).
$$

所以：

$$
C(p)
\leq
d(s,G)
\leq
C(p).
$$

故：

$$
d(s,G)=C(p).
$$

證畢。

這應成為本系列最優先形式化的 optimality theorem。

---

## 39. Formal verification roadmap

### V1. Canonical move semantics

證：

$$
\operatorname{applyMoves}
$$

與 group action 一致。

### V2. Solution checker soundness

$$
\operatorname{checkSolution}=\mathrm{true}
\Rightarrow
\operatorname{Solves}.
$$

### V3. Representation roundtrip / move commutation

延續前三篇。

### V4. Baseline heuristic admissibility

延續第五篇：

$$
\max(
\lceil N_c/4\rceil,
\lceil N_e/4\rceil
)
\leq
d.
$$

### V5. Abstract consistency verifier

局部 edge checks：

$$
h(x)\leq c+h(y).
$$

推出 global lower bound。

### V6. Optimality sandwich theorem

upper = lower 推出 optimal。

### V7. Two-Phase compositional soundness

Phase 1 + Phase 2 certificates 推出 full solution。

### V8. Search algorithm completeness / optimality

最後才形式化 BFS / IDA* 等較大的控制流程。

---

## 40. 驗證優先順序：先小 checker，後大 solver

本文建議實作順序不是：

$$
\text{先形式化整個 Kociemba}.
$$

而是：

$$
\boxed{
\text{Move Kernel}
\rightarrow
\text{Solution Checker}
\rightarrow
\text{Heuristic Checker}
\rightarrow
\text{Optimality Combiner}
\rightarrow
\text{Searcher}.
}
$$

這能最快得到一個真正有安全價值的 verified core。

---

## 41. 可視化：把「證明狀態」畫出來

新版 UI 可以在 solution panel 顯示：

```text
State legality          VERIFIED
Move replay             VERIFIED
Goal reached            VERIFIED
Solution cost           18 HTM
Lower bound             16 HTM
Global optimality       NOT PROVEN
Certified interval      [16, 18]
```

如果 lower bound 也到 $18$：

```text
Global optimality       PROVEN
Reason                   lower bound = upper bound
```

這能避免一般 solver UI 最常見的語義混淆。

---

## 42. Proof trace 與 search trace 分開

SearchTrace 記：

- 展開哪些節點；
- 剪了哪些節點；
- threshold 怎麼變。

ProofTrace 記：

- 哪些 property 已驗證；
- 使用哪個 theorem；
- 哪個 certificate；
- 哪些 dependency。

兩者不能混成同一種 log。

Search 可以很巨大、很嘈雜。

Proof 應該小、穩定、可重播。

---

## 43. Verification artifact 應可保存

每次 solve 可以輸出：

```text
run.json
solution.txt
solution_certificate.json
verification_report.json
search_stats.json
```

若有 optimality：

```text
lower_bound_certificate.json
optimality_certificate.json
```

正式研究 benchmark 就可以重播：

$$
\text{input}
+
\text{certificate}
\rightarrow
\text{same verified claim}.
$$

這比只截圖「Solved in 0.1 s」更有研究價值。

---

## 44. Certificate portability

只要 puzzle spec、move semantics 與 metric 版本固定，solution certificate 不需要綁定原 solver。

因此同一個：

$$
p
$$

可以由：

- JavaScript checker；
- Rust checker；
- Python checker；
- Lean extracted checker；
- Lean theorem；

交叉驗證。

這使證書成為算法之間的共同語言。

---

## 45. 本文核心命題

### 命題 V-A：Searcher 不必可信

只要候選輸出經過已證 sound 的 checker。

### 命題 V-B：Solution path 是 upper-bound certificate

$$
d(s,G)\leq C(p).
$$

### 命題 V-C：Admissible heuristic 是 lower-bound certificate

$$
h(s)\leq d(s,G).
$$

### 命題 V-D：Upper = Lower 即證 optimal

$$
C(p)=h(s)
\Rightarrow
d(s,G)=C(p).
$$

### 命題 V-E：PDB 可以作為不可信資料，由小 checker 驗證 lower-bound property

局部 consistency constraints 推出 global lower bound。

### 命題 V-F：Completeness 是 algorithm-level theorem

不能由單一 solution certificate 取代。

### 命題 V-G：Two-Phase soundness 可組合，但 phase optimality 不推出 global optimality

### 命題 V-H：FDRS 的搜尋表示與 canonical verification 可以解耦

$$
\text{Search in abstract space}
\rightarrow
\text{Verify in canonical space}.
$$

---

## 46. 結論

本文完成 FDRS/FCSR Classical Cube Foundations 的「求解可信性地基」。

到目前為止，我們已經把經典魔方拆成：

$$
\text{Legal State}
+
\text{Representation}
+
\text{Search}
+
\text{Heuristic}
+
\text{Pruning}
+
\text{Phase Decomposition}
+
\text{Verification}.
$$

本文最重要的架構結論是：

$$
\boxed{
\text{Untrusted Searcher}
+
\text{Trusted Checker}
+
\text{Proof-Carrying Result}.
}
$$

求解器可以自由追求速度、AI、自動 phase discovery、GPU 或任何新 representation；最終 claim 則由小型、穩定、可形式化的 checker 決定。

對「解得正確」，move sequence 本身就是證書。

對「證明最短」，最乾淨的策略是：

$$
\boxed{
\text{verified upper bound}
=
\text{verified lower bound}.
}
$$

這使最短性從 solver 的權威宣稱，變成任何人都能重新檢查的數學夾逼。

到這一步，前七篇已足以支持正式演算法工程。

下一篇開始轉向整個系列最具 FCSR 起源特色的部分：

**《多表示同步可視化：3D、FCSR Net、Permutation、Cubie、Graph 與 Search Frontier》**。

那一篇的問題不再是「我們能不能算」，而是：

> 如何讓人與 AI 看見同一個狀態、同一個 move、同一次搜尋與同一份證明，在不同表示域中同步發生？

---

## 參考資料與來源定位

### 起源與系列內部

- [F2026-D] `FDRS_展開收斂_同步性.html`，原 FDRS/FCSR permutation engine、IDA* 與同步可視化原型。
- [CUBE-04] 本系列第四篇：搜尋統一語義。
- [CUBE-05] 本系列第五篇：admissible heuristic、PDB 與 pruning。
- [CUBE-06] 本系列第六篇：Two-Phase 與 phase handoff。

### 外部基線

- [R1] Herbert Kociemba, **Two-Phase Algorithm** 與 **Two-Phase Algorithm Details**。用於 Two-Phase 的 sound / non-optimal practical baseline。
- [R2] Herbert Kociemba, **Pruning Tables**。用於 coordinate pruning lower bounds。
- [R3] `vihdzp/rubik-lean4`，Lean 4 Rubik's Cube formalization。用於現有可解性／合法性形式化工作的 related-work 定位。
- [R4] `alerad/leancert`，Lean 4 certificate-checking architecture。用於「不可信候選生成＋可執行 checker＋soundness theorem」的一般形式驗證工程參照。

---

## 版本註記

v0.1 將 solver guarantee 分解為 soundness、completeness、optimality；建立 upper-bound / lower-bound 雙證書模型；並提出以局部 consistency constraints 驗證 heuristic table 全域 lower-bound property 的方法。

後續第八篇：

**《多表示同步可視化：3D、FCSR Net、Permutation、Cubie、Graph 與 Search Frontier》**。
