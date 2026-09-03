# LRC–COL-03：複合符號算子族的最小 ε-完備基底
## The Minimal ε-Complete Basis of Composite Symbolic Operators

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-21**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

如果未來要建立一套供 AI、人類與多 Agent 系統共同學習、傳播、組合並最終接入現實行動的複合符號語言，一個最直接的問題是：

> **最少究竟需要多少個基礎算子？**

這個問題看似只是「找最小 vocabulary」，實際上至少包含兩個完全不同的概念。

第一種是**形式最小完備（formal minimal completeness）**：只問某一組 primitive operators 是否能在理論上生成目標域中的所有函數、語義結構或行動程序。經典形式系統已經提供極端例子：單一 NAND connective 即可表示所有布林真值函數；組合邏輯中，有限的 combinatory basis 也可以具有極強的生成能力。這證明「非常小的基底可以非常完備」，但同時也暴露另一面：形式上能生成，不代表表示短、容易學、容易讀、容易傳播，或適合 AI 在有限深度與有限上下文中穩定使用。

第二種是本文真正關注的**有效最小完備（effective minimal completeness）**：在指定目標域、Agent、組合文法、最大深度、資源預算與允許誤差下，最少需要多少 operator，才能讓 Agent 在 novel composition 上以足夠高的語義保真度、執行成功率與傳播穩定性完成任務。

因此本文提出：

$$
\boxed{
N_{\min}^{formal}
\neq
N_{\min}^{effective}.
}
$$

並建立第一版 ε-完備基底模型。本文把最小基底問題重新表達為一個多目標 constrained optimization：operator 數量越少，通常需要更深的組合、更高的解碼成本與更長的學習時間；operator 數量越多，又會增加選擇、記憶、歧義、版本治理與語義漂移風險。

本文進一步提出「型別化閉包（typed closure）」、「深度受限覆蓋（depth-bounded coverage）」、「Agent-conditioned completeness」、「冗餘穩健性」、「宏算子／結晶算子分層」與「有效基底區間」等概念，並主張實用符號語言的目標不應是找到理論上最少的 primitive，而應找到：

$$
\boxed{
\text{最小但仍可學、可組、可傳、可執行、可檢查的有效基底。}
}
$$

這一篇不試圖給出固定的數字答案，而是先定義「最小」究竟應如何被研究。

---

## 關鍵詞

複合符號算子；最小完備基底；ε-完備；compositionality；combinatory logic；functional completeness；AI 語言；operator basis；typed closure；systematic generalization

---

# 1. 問題：最少幾個符號才夠？

假設我們想設計一套新的 AI-native composite operator language。

最直接的工程問題是：

> 是否可以先找最少的一組原子算子，再用組合生成一切？

形式上：

$$
\mathcal O
=
\{O_1,\ldots,O_N\}.
$$

配上一套組合規則：

$$
G.
$$

希望：

$$
\operatorname{Closure}(\mathcal O,G)
$$

足以覆蓋目標域：

$$
\Omega.
$$

因此：

$$
\boxed{
N_{\min}
=
\min |\mathcal O|.
}
$$

但如果只寫到這裡，問題幾乎一定被定義錯。

因為「能生成」至少有三種不同意思：

1. **理論上存在某個表達式；**
2. **有限資源下能找到那個表達式；**
3. **AI 能學會並在新問題中穩定使用那個表達式。**

這三者不是一回事。

---

# 2. 經典反例：極小基底可以形式完備

在布林邏輯中，單一 NAND connective 就可以表示所有 truth functions。

因此：

$$
\boxed{
N_{\min}^{Boolean}
=1
}
$$

在某種形式定義下完全可能。

但用大量 NAND 展開複雜邏輯式時，表示會迅速變得：

- 很長；
- 很難讀；
- 很難除錯；
- 很難維護。

所以：

$$
\boxed{
\text{Functional Completeness}
\neq
\text{Human / AI Usability}.
}
$$

---

# 3. 組合邏輯的另一個提醒

Combinatory logic 中，有限 combinatory basis 可以具有 combinatorial completeness。

例如：

$$
\{S,K\}
$$

可以定義大量其他 combinators。

這顯示：

$$
\boxed{
\text{small primitive basis}
\Rightarrow
\text{large expressive closure}
}
$$

是可能的。

但若每次都只使用最原始 basis，常會產生非常長的項。

因此實務上會重新引入：

- $I$ ；
- $B$ ；
- $C$ ；
- $W$ ；
- 其他 derived combinators；

作為 abbreviation / reusable operators。

這與 LRC–COL 的核心問題完全同構：

$$
\boxed{
\text{Derived Operator}
=
\text{not formally necessary}
\quad
\text{but possibly operationally valuable}.
}
$$

---

# 4. 所以要區分兩種「最小」

本文正式定義：

## 4.1 Formal Minimal Basis

$$
\boxed{
N_{\min}^{formal}
}
$$

只問：

> 存不存在一組最小 primitive，使每個目標都可在理論上表示？

---

## 4.2 Effective Minimal Basis

$$
\boxed{
N_{\min}^{effective}
}
$$

問：

> 在有限 Agent 能力、組合深度、時間、記憶、誤差、傳播與執行限制下，最少多少 operator 才真正可用？

一般預期：

$$
\boxed{
N_{\min}^{effective}
\ge
N_{\min}^{formal}.
}
$$

而且常常：

$$
N_{\min}^{effective}
\gg
N_{\min}^{formal}.
$$

---

# 5. 為什麼要加入 ε？

如果目標域很大甚至近似無界，

要求：

$$
Coverage=1
$$

可能不切實際。

因此引入：

$$
\epsilon.
$$

允許：

$$
Coverage
\ge
1-\epsilon.
$$

也就是：

$$
\boxed{
\epsilon\text{-complete}.
}
$$

它不是說「允許亂錯」。

而是承認：

- domain 有尾部；
- rare cases 成本很高；
- 某些任務可退回自然語言或 fallback operator。

---

# 6. 目標域 Ω 必須先被定義

沒有：

$$
\Omega,
$$

就沒有：

$$
N_{\min}.
$$

例如：

### Ω₁
只處理布林邏輯。

### Ω₂
處理一般函數組合。

### Ω₃
處理 AI 元認知操作。

### Ω₄
處理一般工具 Agent。

### Ω₅
處理跨 domain reality-coupled action。

它們的：

$$
N_{\min}
$$

不可能相同。

因此：

$$
\boxed{
N_{\min}
=
N_{\min}(\Omega).
}
$$

---

# 7. 目標域不是只有「任務列表」

更一般地：

$$
\Omega
$$

可以是：

- semantic transformations；
- cognitive operations；
- tool actions；
- workflows；
- communication acts；
- world-state transitions。

因此一個 LRC–COL operator 不一定只是「詞義」。

它可能直接代表：

$$
\boxed{
\text{semantic + operational contract}.
}
$$

---

# 8. 第一版 formal ε-completeness

令：

$$
\llbracket e\rrbracket
$$

表示 expression $e$ 的形式語義。

對每個：

$$
\omega\in\Omega,
$$

若存在：

$$
e_{\omega}
\in
\mathcal L(\mathcal O,G)
$$

使：

$$
d(
\llbracket e_{\omega}\rrbracket,
\omega
)
\le
\epsilon,
$$

則：

$$
(\mathcal O,G)
$$

對：

$$
\Omega
$$

是 ε-complete。

---

# 9. Formal Minimum

因此：

$$
\boxed{
N_{\min}^{formal}
(
\Omega,\epsilon,G
)
=
\min_{\mathcal O}
|\mathcal O|
}
$$

subject to：

$$
Coverage_{\epsilon}^{formal}
(
\mathcal O,G;\Omega
)
\ge
1-\epsilon.
$$

---

# 10. 但形式定義缺少「深度」

一個 expression：

$$
e
$$

可能有：

$$
depth(e)=1000.
$$

理論上能表達，

實際 AI 根本無法穩定 compose。

所以加入最大深度：

$$
d_{\max}.
$$

---

# 11. Depth-Bounded Completeness

定義：

$$
Coverage_{\epsilon,d}
=
P_{\omega\sim\mu_{\Omega}}
[
\exists e:
depth(e)\le d
\land
d(\llbracket e\rrbracket,\omega)\le\epsilon
].
$$

因此：

$$
\boxed{
N_{\min}^{formal}
(
\Omega,\epsilon,G,d
)
}
$$

會隨：

$$
d
$$

改變。

---

# 12. 基底—深度交換律

一般來說：

$$
N\downarrow
\Rightarrow
d\uparrow.
$$

如果多增加 derived operators：

$$
N\uparrow,
$$

則常可：

$$
d\downarrow.
$$

因此：

$$
\boxed{
N
\leftrightarrow
d
}
$$

是最核心的 trade-off 之一。

---

# 13. 兩個退化極端

## Extreme A — One Macro per Task

如果：

$$
\Omega
=
\{\omega_1,\ldots,\omega_M\},
$$

我們可以為每個目標建立：

$$
O_i=\omega_i.
$$

那麼：

$$
N=M
$$

且：

$$
d=1.
$$

這是：

$$
\boxed{
\text{memorization language}.
}
$$

幾乎沒有 composition。

---

## Extreme B — Tiny Generative Basis

另一端：

$$
N
$$

極小，

但每個高階功能都需要很深組合。

這是：

$$
\boxed{
\text{minimal primitive language}.
}
$$

formal 很漂亮，

operational 可能很差。

---

# 14. 真正最佳點在中間

所以真正要找的是：

$$
\boxed{
(N^*,d^*)
}
$$

而不是單獨：

$$
N_{\min}.
$$

可寫：

$$
(N^*,d^*)
=
\arg\max
U(N,d).
$$

---

# 15. Effective Completeness 必須加入 Agent

形式語義不知道「誰在用」。

AI 語言必須加入：

$$
A.
$$

所以：

$$
\boxed{
N_{\min}^{effective}
=
N_{\min}^{effective}
(
\Omega,A,\epsilon,G,d,B
).
}
$$

其中：

$$
B
$$

是資源預算。

---

# 16. Agent-Conditioned Coverage

定義：

$$
Coverage_{\epsilon}^{A}
=
P_{\omega\sim\mu_{\Omega}}
[
D(
Exec_A(
Compose_A(\omega)
),
Target(\omega)
)
\le\epsilon
].
$$

這裡不再只問：

> expression 存不存在？

而問：

> **Agent 是否能找到、理解、組合並正確執行？**

---

# 17. Effective ε-Completeness

如果：

$$
Coverage_{\epsilon}^{A}
\ge
1-\epsilon
$$

而且：

- depth ≤ $d$ ；
- cost ≤ $B$ ；
- novel composition success 達標；
- stability 達標；

則稱：

$$
\boxed{
(\mathcal O,G)
\text{ is effectively ε-complete for }A.
}
$$

---

# 18. 為什麼 current LLM 讓這個區分必要？

近年的 compositional-generalization 研究持續顯示：

> 已知 primitives 並不保證模型能在 novel combination 中穩定使用它們。

例如：

- morphology primitive 已知；
- concept order 已知；
- semantic parsing primitives 覆蓋；

模型仍可能在：

- novel roots；
- 更高 complexity；
- minimum-coverage demonstrations；

下失敗。

因此：

$$
\boxed{
\text{Primitive Coverage}
\neq
\text{Systematic Composition}.
}
$$

---

# 19. Minimum Coverage 不是 Effective Completeness

假設 training examples 已經覆蓋：

$$
\{O_1,\ldots,O_N\}.
$$

即：

$$
PrimitiveCoverage=1.
$$

仍可能：

$$
NovelCompositionAccuracy\ll1.
$$

所以：

$$
\boxed{
\text{seen all parts}
\neq
\text{can compose all parts}.
}
$$

---

# 20. 組合能力至少有三層

## Level 1 — Primitive Recognition

認得：

$$
O_i.
$$

## Level 2 — Familiar Composition

會執行訓練中常見：

$$
O_i\circ O_j.
$$

## Level 3 — Systematic Novel Composition

能把已知 primitives 放進：

- 新順序；
- 新深度；
- 新 domain；
- 新 relation；

仍正確執行。

真正 effective completeness 至少要測 Level 3。

---

# 21. Behavioral Systematicity vs Representational Systematicity

即使模型行為上通過某 benchmark，

也不能直接推出：

> 它內部形成了某種特定 compositional representation。

因此本文只需要：

$$
\boxed{
\text{Operational Systematicity}.
}
$$

不主張特定 hidden representation。

---

# 22. 型別化閉包

如果 operator 無型別，

任意：

$$
O_i\circ O_j
$$

都可以寫，

但很多組合沒有意義。

所以需要：

$$
\boxed{
\tau(O_i):
D_{in}
\rightarrow
D_{out}.
}
$$

---

# 23. Typed Composition

只有：

$$
D_{out}(O_i)
\sim
D_{in}(O_j)
$$

時：

$$
O_j\circ O_i
$$

才合法。

因此 closure 不是：

$$
\mathcal O^*
$$

完全自由組合，

而是：

$$
\boxed{
Closure_T(\mathcal O,G).
}
$$

---

# 24. 型別本身會增加基底成本

加入 types：

- 增加 specification；
- 增加 learning burden；

但：

- 降低 nonsense composition；
- 提高 fidelity；
- 降低 search space。

所以：

$$
\boxed{
\text{Type Cost}
\leftrightarrow
\text{Composition Safety}.
}
$$

---

# 25. 第一版 Operator Type Families

未來可考慮至少六類。

### T1 — Semantic Operators

例如：

- bind；
- compare；
- transform；
- abstract。

### T2 — Control Operators

- sequence；
- branch；
- loop；
- stop。

### T3 — Epistemic Operators

- query；
- verify；
- challenge；
- update。

### T4 — Memory Operators

- store；
- retrieve；
- supersede；
- link。

### T5 — Agent Operators

- delegate；
- object；
- merge；
- negotiate。

### T6 — Reality-Coupling Operators

- invoke tool；
- execute；
- commit；
- rollback。

---

# 26. 這六類是不是最小？

不知道。

本文刻意不宣稱：

$$
6
$$

就是最小類型數。

它們只是：

$$
\boxed{
\text{candidate functional decomposition}.
}
$$

真正最小需要後續證明／實驗。

---

# 27. Type Family 與 Primitive Count 不同

即使有：

$$
6
$$

類，

每類可能：

- 1 個 primitive；
- 10 個 primitive；
- 100 個 primitive。

所以：

$$
\boxed{
N_{\text{type}}
\neq
N_{\text{operator}}.
}
$$

---

# 28. 原子、複合、結晶三層

未來最實用的語言可能不是只有一層 basis。

而是：

$$
\boxed{
\mathcal O
=
\mathcal O_0
\cup
\mathcal O_1
\cup
\mathcal O_2.
}
$$

### $\mathcal O_0$ — Primitive

最基本。

### $\mathcal O_1$ — Composite

常見組合。

### $\mathcal O_2$ — Crystallized Macro

高頻成熟 workflow。

---

# 29. 為什麼分層可以更有效？

如果所有東西都壓到 primitive：

$$
d\uparrow.
$$

如果所有東西都變 macro：

$$
N\uparrow.
$$

分層可以：

$$
\boxed{
\text{balance vocabulary size and depth}.
}
$$

---

# 30. Derived Operator 不應被當 primitive

例如：

$$
O_B
=
O_3\circ O_2\circ O_1.
$$

如果：

$$
O_B
$$

只是頻繁重用，

可以作為 derived operator。

formal basis 仍不必增加：

$$
N_{\min}^{formal}.
$$

但 effective basis 可以包含它。

---

# 31. 所以 Effective Basis 可以有冗餘

formal minimal basis：

$$
\mathcal B_f.
$$

effective basis：

$$
\mathcal B_e
=
\mathcal B_f
\cup
\mathcal R,
$$

其中：

$$
\mathcal R
$$

是有價值的冗餘／derived operators。

因此：

$$
\boxed{
\text{Redundancy}
\neq
\text{Waste}.
}
$$

---

# 32. 冗餘的四種正向功能

## R1 — Depth Reduction

降低：

$$
d.
$$

## R2 — Error Correction

提供 alternative route。

## R3 — Human / AI Readability

讓結構更透明。

## R4 — Cross-Agent Translation

某些 macro 可以成為 shared semantic anchor。

---

# 33. 冗餘也有成本

太多 derived operators 會：

- vocabulary explosion；
- synonym collision；
- version burden；
- selection confusion。

所以冗餘需要：

$$
\boxed{
\text{Marginal Utility Gate}.
}
$$

---

# 34. Minimal Robust Basis

因此可以定義：

$$
\boxed{
N_{\min}^{robust}
}
$$

為：

> 在指定 noise / failure / transfer 條件下，仍能達標的最小 operator count。

通常：

$$
N_{\min}^{robust}
\ge
N_{\min}^{effective}
\ge
N_{\min}^{formal}.
$$

---

# 35. 這三個最小值很重要

$$
\boxed{
N_{\min}^{formal}
}
$$

能不能表達。

$$
\boxed{
N_{\min}^{effective}
}
$$

AI 能不能有效使用。

$$
\boxed{
N_{\min}^{robust}
}
$$

在 noise / transfer / drift 下能不能維持。

---

# 36. Learning Cost

operator basis 越大：

$$
N\uparrow
$$

一般會增加：

$$
C_{learn}.
$$

但 basis 越小，

composition depth：

$$
d\uparrow
$$

也增加 learning difficulty。

所以：

$$
\boxed{
C_{learn}
=
f(N,d,G,T,A).
}
$$

---

# 37. U 型學習成本猜想

可以提出：

$$
\boxed{
C_{learn}(N)
}
$$

可能呈 U 型。

### 太少 operator

- deep composition；
- long expressions；
- difficult abstraction。

### 太多 operator

- memory burden；
- selection ambiguity；
- synonym confusion。

中間存在：

$$
N_{learn}^*.
$$

---

# 38. Execution Cost 也可能 U 型

太少：

$$
d\uparrow
\Rightarrow
C_{exec}\uparrow.
$$

太多：

$$
selection\ search\uparrow
\Rightarrow
C_{exec}\uparrow.
$$

所以：

$$
\boxed{
N^*
}
$$

可能同時由 learning + execution 決定。

---

# 39. Semantic Fidelity

基底太小，

高階語義要經很多 composition：

$$
O_1\circ O_2\circ\cdots.
$$

每層可能有 drift：

$$
\delta_i.
$$

所以：

$$
F_{sem}(d)
$$

可能隨 $d$ 下降。

---

# 40. 但 macro 太多也會造成 drift

macro operator：

$$
O_M
$$

如果 definition 不穩，

會形成：

$$
\boxed{
\text{semantic black box}.
}
$$

所以：

$$
N\uparrow
$$

也不保證：

$$
F_{sem}\uparrow.
$$

---

# 41. Operator Granularity

每個 operator 的「粒度」可以表示：

$$
g(O).
$$

太細：

- composition 深。

太粗：

- reuse narrow；
- semantics complex。

因此存在：

$$
\boxed{
g^*
}
$$

最佳粒度。

---

# 42. 最小基底其實是多維問題

真正變數：

$$
\boxed{
(N,d,g,T,G,A,B,\epsilon).
}
$$

所以：

$$
N_{\min}
$$

不是獨立量。

---

# 43. 第一版 Effective Objective

可寫：

$$
\boxed{
J(\mathcal O,G)
=
\alpha Coverage
+
\beta F_{sem}
+
\gamma Y_L
+
\eta Transfer
-
\lambda C_{learn}
-
\mu C_{exec}
-
\nu Drift.
}
$$

目標：

$$
\max J.
$$

subject to：

$$
|\mathcal O|\le N,
\qquad
depth\le d,
\qquad
Risk\le R_{\max}.
$$

---

# 44. Minimal Effective Basis 定義

因此：

$$
\boxed{
N_{\min}^{effective}
=
\min |\mathcal O|
}
$$

subject to：

$$
Coverage\ge1-\epsilon,
$$

$$
F_{sem}\ge\tau_F,
$$

$$
Generalization\ge\tau_G,
$$

$$
LearningCost\le B_L,
$$

$$
ExecutionCost\le B_E,
$$

$$
Risk\le R_{\max}.
$$

這比單純 formal completeness 更接近未來工程需要。

---

# 45. Static Minimum vs Dynamic Minimum

本文先只處理某一固定時間：

$$
t.
$$

因此：

$$
N_{\min}^{effective}(t).
$$

但 AI 內化 macro 後：

$$
t+1
$$

可能變。

完整動態留給 LRC–COL-06。

---

# 46. Distribution μΩ 很重要

Coverage：

$$
P_{\omega\sim\mu_{\Omega}}
$$

依賴任務分布。

如果：

- 99% 都是簡單任務；
- 1% 是超複雜任務；

ε-complete 可能忽略 tail。

因此高風險 tail 不能只靠 frequency。

---

# 47. Risk-Weighted Coverage

可定義：

$$
\boxed{
Coverage_R
=
1-
\frac{
\mathbb E[
Risk(\omega)\cdot Failure(\omega)
]
}{
\mathbb E[Risk(\omega)]
}.
}
$$

這避免：

> rare catastrophic cases 被 ε 當成可忽略。

---

# 48. 因此 ε 也應該條件化

可以有：

$$
\epsilon_{normal}
$$

與：

$$
\epsilon_{critical}.
$$

高風險 operator：

$$
\epsilon_{critical}
\ll
\epsilon_{normal}.
$$

---

# 49. Domain Decomposition

大域：

$$
\Omega
$$

可能拆成：

$$
\Omega
=
\Omega_1
\cup
\cdots
\cup
\Omega_m.
$$

每個 domain 有 local basis：

$$
\mathcal O_i.
$$

加 shared core：

$$
\mathcal O_C.
$$

所以總語言可能：

$$
\boxed{
\mathcal O
=
\mathcal O_C
\cup
\bigcup_i\mathcal O_i.
}
$$

---

# 50. Universal Core + Domain Extension

這可能是未來最重要的架構之一：

$$
\boxed{
\text{Small Universal Core}
+
\text{Domain-Specific Extensions}.
}
$$

而不是企圖一個平坦 vocabulary 覆蓋一切。

---

# 51. Core 的理想功能

Universal Core 應優先承載：

- composition；
- control；
- reference；
- query；
- update；
- branch；
- stop；
- tool invoke。

domain extension 再承載：

- finance；
- biology；
- game；
- robotics。

---

# 52. 是否能存在真正 universal core？

這仍是猜想。

需要研究：

$$
\boxed{
N_C
}
$$

是否在 domain 擴張時近似穩定。

如果：

$$
N_C
$$

不斷上升，

就不存在小型 universal core。

---

# 53. Lower Bound 可以怎麼找？

真正證明：

$$
N_{\min}
$$

需要 lower bound。

可能方法包括：

- distinguishability；
- algebraic independence；
- type necessity；
- information-theoretic bound；
- computational expressivity；
- task partition complexity。

本文暫不聲稱哪個足夠。

---

# 54. Information-Theoretic Lower Bound

若目標域有：

$$
M
$$

個需要區分的 primitive semantic states，

而每個 operator 可提供有限 distinguishability，

可導出：

$$
\boxed{
N
\ge
\frac{
H(\Omega)
}{
Capacity(O)
}
}
$$

類似下界。

但 operator 可組合，

所以實際 bound 需要加入：

$$
d.
$$

---

# 55. Compositional Capacity

如果每個 depth 可組：

$$
N^d
$$

個表達，

表面容量近似：

$$
\sum_{k=1}^{d}N^k.
$$

但這只是 syntax capacity。

真正 semantic capacity：

$$
C_{sem}
$$

通常小於它，

因為：

- synonym；
- invalid composition；
- semantic collision。

---

# 56. Effective Capacity

所以：

$$
\boxed{
C_{eff}
=
C_{syntactic}
\cdot
p_{valid}
\cdot
p_{distinct}
\cdot
p_{learnable}
\cdot
p_{faithful}.
}
$$

這是一個重要候選近似。

---

# 57. 最小基底與壓縮不是同一目標

如果追求：

$$
N\downarrow,
$$

可能讓 expression：

$$
|e|\uparrow.
$$

總 token 反而增加。

所以：

$$
\boxed{
\text{Minimal Vocabulary}
\neq
\text{Minimal Description Length}.
}
$$

---

# 58. MDL-like Criterion

可以比較：

$$
\boxed{
L_{total}
=
L(\mathcal O)
+
L(G)
+
L(Data\mid\mathcal O,G).
}
$$

也就是：

- 定義 basis 的成本；
- 定義 grammar 的成本；
- 用它表達實際 workload 的成本。

這很接近真正語言設計。

---

# 59. Operator Dictionary Cost

若 basis 很大：

$$
L(\mathcal O)\uparrow.
$$

若 basis 太小：

$$
L(Data\mid\mathcal O,G)\uparrow.
$$

因此仍可能有中間 optimum。

---

# 60. AI Learner 讓 MDL 再多一項

對 AI：

$$
L_{effective}
=
L(\mathcal O)
+
L(G)
+
L(Data)
+
C_{learn}(A).
$$

因為有些形式上很短的語言，

AI 可能非常難學。

---

# 61. Current LLM 的 Compositionality 提醒

2025 年研究顯示，systematic generalization 表現會隨 training component distribution 的 entropy 變化；而 morphology compositionality 在 novel roots 與更高複雜度時仍會明顯下降。

這表示：

$$
\boxed{
\text{learnability depends on exposure structure, not only basis definition}.
}
$$

---

# 62. 所以 basis 不是單獨設計的

完整設計包含：

$$
\boxed{
\text{Basis}
+
\text{Grammar}
+
\text{Curriculum}
+
\text{Examples}
+
\text{Validation}.
}
$$

最小 operator 數只是其中一項。

---

# 63. Curriculum-Conditioned Minimum

可定義：

$$
\boxed{
N_{\min}^{effective}
(
\Omega,A,\mathcal C
)
}
$$

其中：

$$
\mathcal C
$$

是 curriculum / exposure policy。

同一 basis，

不同 curriculum，

effective completeness 可能不同。

---

# 64. Cross-Agent Minimum

對 Agent A：

$$
N_{\min}^A=30.
$$

對 Agent B：

$$
N_{\min}^B=50.
$$

可能成立。

因此若要通用傳播：

$$
\boxed{
N_{\min}^{shared}
=
\min N
}
$$

subject to：

$$
\forall A_i:
Coverage(A_i)\ge1-\epsilon.
$$

---

# 65. Shared Minimum 可能比單 Agent 更大

$$
\boxed{
N_{\min}^{shared}
\ge
\max_i
N_{\min}^{A_i}
}
$$

通常只是候選關係，

因為共享 operator 可能反過來幫助 cross-agent alignment。

需要實驗。

---

# 66. Translation Layer

若不同 agent 適合不同 local basis：

$$
\mathcal O_A,
\mathcal O_B,
$$

不一定要強迫共同 basis。

可以：

$$
\boxed{
\mathcal O_A
\leftrightarrow
\Phi
\leftrightarrow
\mathcal O_B.
}
$$

 $\Phi$ 是 shared interchange layer。

這可能比 universal one-size-fits-all 更有效。

---

# 67. 最小基底的第一批命題

## MB-P1 — Formal–Effective Gap

$$
N_{\min}^{effective}
>
N_{\min}^{formal}
$$

在一般 AI language domain 中常成立。

---

## MB-P2 — Basis–Depth Tradeoff

$$
N\downarrow
\Rightarrow
d\uparrow
$$

在固定 coverage 下大致成立。

---

## MB-P3 — U-Shaped Effective Cost

總：

$$
C_{learn}+C_{exec}+C_{govern}
$$

對 $N$ 可能呈 U 型。

---

## MB-P4 — Redundancy Benefit

少量 derived redundancy 可降低 depth 與 error，

所以：

$$
N^*>N_{\min}^{formal}.
$$

---

## MB-P5 — Typed Closure Benefit

型別限制會降低無效組合率，

即使增加 grammar cost，

仍可能提高 effective yield。

---

## MB-P6 — Primitive Coverage Insufficiency

看過所有 primitive 不足以保證 systematic novel composition。

---

## MB-P7 — Curriculum Dependence

effective minimum 依 exposure curriculum 改變。

---

## MB-P8 — Universal-Core Hypothesis

可能存在相對小且跨 domain 穩定的 shared core，

再搭配 domain extensions。

---

## MB-P9 — Risk-Weighted Completeness

高風險 domain 的 minimal basis 必須以 risk-weighted coverage 定義，

不能只看 average coverage。

---

## MB-P10 — Dynamic Minimum

 $N_{\min}^{effective}$ 隨 Agent 內化、環境與 operator crystallization 動態變化。

---

# 68. 我們現在仍不能回答「到底是幾個」

這一篇最重要的誠實結論是：

$$
\boxed{
\text{目前沒有理據直接說 }N_{\min}=20,50,100,\text{或任何固定數字。}
}
$$

因為還沒有指定：

- $\Omega$ ；
- Agent；
- ε；
- depth；
- type system；
- curriculum；
- risk；
- budget。

---

# 69. 但現在可以開始估

一旦固定一個 benchmark domain：

$$
\Omega_0,
$$

就可以開始：

1. 建 candidate primitives；
2. 測 coverage；
3. 做 ablation；
4. 減少 operators；
5. 量 depth；
6. 量 learning time；
7. 量 generalization；
8. 找 Pareto frontier。

---

# 70. Basis Ablation Algorithm

初始 basis：

$$
\mathcal O_0.
$$

每次嘗試移除：

$$
O_i.
$$

如果：

$$
\Delta Coverage<\tau_C
$$

且：

$$
\Delta Cost\le\tau_K,
$$

可以移除。

反覆：

$$
\boxed{
\mathcal O_t
\rightarrow
\mathcal O_{t+1}.
}
$$

最後得到 empirical minimal basis candidate。

---

# 71. 但 greedy ablation 不保證全局最小

因為：

- $O_1$ 單獨可刪；
- $O_2$ 單獨可刪；
- 但兩個一起刪可能失去 closure。

所以真正 search 可能需要：

- subset search；
- integer optimization；
- evolutionary search；
- MDL objective；
- graph cut；
- differentiable selection。

後續再研究。

---

# 72. Basis Graph

可以建立：

$$
G_B=(V,E).
$$

node：

$$
O_i.
$$

edge 表示：

- can-derive；
- substitutes；
- composes-with；
- required-by；
- conflicts-with。

最小 basis 變成：

$$
\boxed{
\text{graph reduction problem}.
}
$$

---

# 73. Derivability Matrix

定義：

$$
D_{ij}=1
$$

若：

$$
O_j
$$

可由其他 basis 在深度 ≤ $d$ 下導出。

那麼：

$$
O_j
$$

是 formal redundant。

但如果導出深度很高，

它可能仍是 effective necessary。

---

# 74. Effective Necessity

定義：

$$
EN(O_j)
=
Gain_{depth}
+
Gain_{fidelity}
+
Gain_{learn}
+
Gain_{transfer}
-
Cost_{vocab}.
$$

如果：

$$
EN(O_j)>0,
$$

即使 formal redundant，也值得保留。

---

# 75. 這是本篇最核心的新觀念之一

$$
\boxed{
\text{Formal Redundancy}
\neq
\text{Effective Redundancy}.
}
$$

一個 formally redundant operator 可能是 operationally essential。

---

# 76. 與 LRC–COL-02 的連接

前篇定義：

$$
Y_L.
$$

因此 basis 選擇應考慮：

$$
\boxed{
Y_{\mathcal O}.
}
$$

如果刪掉 operator：

$$
N\downarrow,
$$

卻讓：

$$
Y_L\downarrow,
$$

那不是好的最小化。

---

# 77. Effective Minimality 的真正含義

因此本文最後把「最小」重新定義成：

> **在滿足 coverage、fidelity、learnability、generalization、risk 與 resource constraints 下，不再能刪除任何 operator 而不讓整體效用跌出可接受區間。**

形式：

$$
\boxed{
\forall O_i\in\mathcal O^*:
J(\mathcal O^*-\{O_i\})<\tau_J.
}
$$

這是：

$$
\boxed{
\text{locally irreducible effective basis}.
}
$$

全局最小則是更強問題。

---

# 78. 本篇核心公式組

Formal ε-completeness：

$$
\boxed{
Coverage_{\epsilon}^{formal}
\ge
1-\epsilon.
}
$$

Depth-bounded minimum：

$$
\boxed{
N_{\min}^{formal}
(
\Omega,\epsilon,G,d
).
}
$$

Effective minimum：

$$
\boxed{
N_{\min}^{effective}
(
\Omega,A,\epsilon,G,d,B
).
}
$$

Robust minimum：

$$
\boxed{
N_{\min}^{robust}
\ge
N_{\min}^{effective}
\ge
N_{\min}^{formal}.
}
$$

Effective objective：

$$
\boxed{
J
=
\alpha Coverage
+
\beta Fidelity
+
\gamma ActionYield
+
\eta Transfer
-
\lambda LearningCost
-
\mu ExecutionCost
-
\nu Drift.
}
$$

---

# 79. 非主張

本文不主張：

1. NAND / combinatory logic 直接等同 AI 語言設計；
2. 存在跨所有 domain 的固定最小 operator 數；
3. 更少 operator 一定更好；
4. 更多 macro 一定更好；
5. formal completeness 能推出 AI generalization；
6. current LLM compositionality 已足以支撐任意深度 operator language；
7. typed closure 是唯一設計；
8. 六類 candidate type 是最終類型；
9. global minimal basis 容易計算；
10. ε 可以用單一固定值跨風險 domain。

本文只提出：

$$
\boxed{
\text{The useful minimum of a composite operator language is an agent-, domain-, depth-, budget-, risk-, and error-conditioned quantity, not merely a formal cardinality.}
}
$$

---

# 80. 文獻錨點

1. **Combinatory Logic — Stanford Encyclopedia of Philosophy**  
   記錄 NAND 單一 connective 的功能完備例子，以及 $\{S,K\}$ combinatory basis 的 combinatorial completeness。這些形式系統說明極小 basis 可以具有極大 expressive closure，同時也顯示 derived combinators 對縮短表示與保持透明性很有實用價值。

2. **Systematic Generalization in Language Models Scales with Information Entropy（ACL Findings 2025）**  
   顯示 systematic generalization 的困難與 training component distribution 的 entropy 有關，說明 learnability 不只取決於 primitives 是否存在。

3. **Evaluating Morphological Compositional Generalization in Large Language Models（NAACL 2025）**  
   顯示 LLM 在 novel word roots 與更高 morphological complexity 下 compositional generalization 明顯下降，支持「組合深度／複雜度會影響 effective completeness」。

4. **MC²: A Minimum-Coverage and Dataset-Agnostic Framework for Compositional Generalization of LLMs on Semantic Parsing（EMNLP Findings 2025）**  
   顯示即使 demonstration 數量落在 theoretical minimum-coverage 下，advanced LLMs 仍不能保證跨 dataset 取得良好 compositional generalization；primitive coverage 本身不足以等同 effective compositional competence。

5. **Behavioural vs. Representational Systematicity in End-to-End Models（ACL 2025）**  
   強調 behavioral systematicity 與 representational systematicity 的區分。本系列目前只要求可觀察的 operational systematicity，不對 AI hidden representation 作過度主張。

---

# 81. 下一篇

## LRC–COL-04：最大有效算子集與語言複雜度上界
### The Maximum Effective Operator Set and the Upper Bound of Language Complexity

下一篇將從另一端研究：

> **不是最少幾個才夠，而是最多增加到多少之後，新 operator 開始讓整體語言變差？**

將正式定義：

$$
N_{\max}^{effective}
$$

並研究：

- vocabulary explosion；
- selection entropy；
- synonym collision；
- operator interference；
- versioning burden；
- context cost；
- long-tail underuse；
- semantic fragmentation；

何時讓：

$$
\Delta Y_{\mathcal O}<0.
$$

**END — LRC–COL-03 v0.1**
