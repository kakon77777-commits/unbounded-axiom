# 局部 O(1) 不等於全域 O(1)：API、Oracle、預計算、Advice 與外包計算的複雜度邊界

## Local $O(1)$ Is Not Global $O(1)$: Complexity Boundaries of APIs, Oracles, Precomputation, Advice, and Outsourced Computation

**系列：** Computational Space and Hyperconnected Complexity Series  
**Paper：** 05 / 09  
**作者：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-29  
**文件性質：** 計算複雜度方法論／Oracle 與外包計算／非一致性與預計算邊界  
**前置文件：**
- Paper 01《計算機不是處理器：可定址狀態轉換空間的重新定義》
- Paper 02《從 1 到 X：符號、地址、展開與狀態翻轉計算》
- Paper 03《超連接計算：從無限維奧賽羅到極限 MSSP–RDR》
- Paper 04《複雜度位移原則：時間路徑如何轉移為空間、連接、歷史與外部能力》

**研究狀態：** 理論澄清、成本邊界與量詞分析；本文不修改標準 $P$ 、 $NP$ 、oracle machine、advice complexity 或 nonuniform complexity 的既有定義，不宣稱任何經典複雜度類塌縮。

---

## 摘要

超連接計算將大量能力轉換成可直接定址的狀態通道。當一個複雜服務可以被：

```text
solve(x)
```

一次呼叫時，caller 所見的操作數可能接近常數；當一個 oracle query 被抽象成單一步驟時，oracle machine 也可以在單次 query 中取得原本極難計算的答案；當一個問題族的答案被預先計算成 lookup table，online lookup 同樣可能近似 $O(1)$。

因此，一個極端超連接系統很容易產生以下表象：

$$
\boxed{
\text{所有能力都是一次呼叫}
\Rightarrow
\text{所有問題都是 }O(1).
}
$$

本文系統性否定這個推論。

本文的核心區分是：

$$
\boxed{
O(1)_{\mathrm{invocation}}
\neq
O(1)_{\mathrm{resolution}}
\neq
O(1)_{\mathrm{provider}}
\neq
O(1)_{\mathrm{construction}}
\neq
O(1)_{\mathrm{closed}}.
}
$$

本文將一次「看似常數」的超連接求解拆成：

$$
\boxed{
C_{\mathrm{query}}
=
C_{\mathrm{encode}}
+
C_{\mathrm{resolve}}
+
C_{\mathrm{invoke}}
+
C_{\mathrm{communicate}}
+
C_{\mathrm{provider}}
+
C_{\mathrm{verify}}.
}
$$

若還要把能力形成過程納入：

$$
\boxed{
C_{\mathrm{lifecycle}}
=
C_{\mathrm{construct}}
+
C_{\mathrm{precompute}}
+
C_{\mathrm{store}}
+
C_{\mathrm{query}}
+
C_{\mathrm{maintain}}.
}
$$

本文進一步區分五種容易被混淆的情況：

1. **API externalization**：caller 成本降低，但 provider 仍計算；
2. **oracle-relative computation**：在指定 oracle 模型中 query 成本可被抽象為一步；
3. **precomputation**：offline 成本換取 online 加速；
4. **advice / nonuniform state**：不同 input size 可接收外部提供的 size-dependent information；
5. **true uniform algorithmic reduction**：存在單一可有效生成的演算法，在標準模型中真正降低 asymptotic complexity。

因此：

$$
\boxed{
\text{Cheap Access}
\neq
\text{Cheap Construction}
\neq
\text{Cheap Global Computation}.
}
$$

本文亦指出超連接計算最終必須處理一個量詞問題：

$$
\forall x\,\exists a_x
$$

並不推出：

$$
\exists A\,\forall x.
$$

同樣：

$$
\forall n\,\exists S_n
$$

也不保證存在一個 uniform polynomial-time constructor：

$$
G(1^n)\mapsto S_n.
$$

這條量詞邊界是封閉系統 P/NP 與 Agentic P/NP 的重要前置條件。

**關鍵詞：** $O(1)$ 、API、Oracle、Advice、Precomputation、Nonuniformity、Complexity Boundary、Hyperconnected Computation、P/NP、Outsourcing

---

# 1. 最危險的一句話

假設未來 MSSP–RDR 已經極度成熟。

所有 capability 都有 address：

$$
1_i.
$$

使用者說：

```text
solve_sat(instance)
```

系統：

1. 找到 SAT capability；
2. 呼叫 provider；
3. 得到答案。

從 caller 視角：

$$
\boxed{
1\text{ call}.
}
$$

那麼可以說：

$$
C_{\mathrm{invoke}}=O(1)
$$

嗎？

在適當的 interface cost model 中，可以。

但可以說：

$$
SAT\in O(1)
$$

嗎？

一般不可以。

這是本文必須守住的第一道邊界。

---

# 2. 一個 Call 到底代表什麼？

令：

$$
a
$$

為一個 address。

caller：

$$
a(x).
$$

高階抽象中可寫：

$$
\boxed{
a:x\mapsto y.
}
$$

但完整展開可能是：

$$
x
\rightarrow
\text{serialize}
\rightarrow
\text{route}
\rightarrow
\text{authenticate}
\rightarrow
\text{provider}
\rightarrow
\text{compute}
\rightarrow
\text{return}
\rightarrow
\text{verify}
\rightarrow
y.
$$

所以：

$$
\boxed{
\operatorname{CallCount}=1
}
$$

與：

$$
\boxed{
\operatorname{Work}=1
}
$$

沒有一般等價關係。

---

# 3. Invocation Complexity

本文定義：

$$
\boxed{
C_{\mathrm{invoke}}(a)
}
$$

為「已知 address 且 provider 已存在」時，啟動該 capability 的局部操作成本。

對固定 interface，它可能近似：

$$
O(1).
$$

例如：

```text
CALL FOO
```

或：

```text
POST /solve
```

這個說法本身完全合法。

問題只出現在有人把它升級成：

$$
\boxed{
C_{\mathrm{problem}}=O(1).
}
$$

---

# 4. Resolution Complexity

在超連接世界中，甚至 address 都可能未知。

輸入：

$$
q
$$

需要先：

$$
q
\rightarrow
a_i.
$$

因此定義：

$$
\boxed{
C_{\mathrm{resolve}}(q).
}
$$

如果 capability registry 很大：

$$
|\mathcal A|=N,
$$

resolution 本身可能：

$$
O(\log N),
$$

$$
O(N),
$$

或更複雜。

如果 selector 使用 AI：

$$
C_{\mathrm{resolve}}
$$

還可能包含模型 inference。

所以：

$$
\boxed{
O(1)_{\mathrm{invoke}}
\not\Rightarrow
O(1)_{\mathrm{resolve}}.
}
$$

---

# 5. Provider Complexity

一旦 address 解析完成：

$$
a_i
\rightarrow
P_i,
$$

真正 provider 執行：

$$
P_i(x)\rightarrow y.
$$

定義：

$$
\boxed{
C_{\mathrm{provider}}(x).
}
$$

它可能是：

$$
O(n),
\quad
O(n\log n),
\quad
O(n^k),
\quad
O(2^n).
$$

caller 完全可以不知道。

因此：

$$
\boxed{
C_{\mathrm{invoke}}=O(1)
}
$$

與：

$$
\boxed{
C_{\mathrm{provider}}=O(2^n)
}
$$

可以同時成立。

---

# 6. Closed-System Cost

若把 caller、network、provider 與 verifier 全部包入：

$$
\mathfrak B,
$$

則：

$$
\boxed{
C_{\mathrm{closed}}
=
C_{\mathrm{resolve}}
+
C_{\mathrm{invoke}}
+
C_{\mathrm{communication}}
+
C_{\mathrm{provider}}
+
C_{\mathrm{verify}}.
}
$$

這才是：

> 系統真正完成這次任務所消耗的必要成本。

所以：

$$
\boxed{
C_{\mathrm{local}}
\ll
C_{\mathrm{closed}}
}
$$

完全可能。

---

# 7. API：最常見的工程外包

假設：

```text
answer = api.solve(x)
```

caller 端：

$$
C_{\mathrm{caller}}
=
O(1)
$$

次 API invocation。

server：

$$
C_{\mathrm{server}}
=
T(n).
$$

network：

$$
C_{\mathrm{net}}
=
N(n).
$$

則：

$$
\boxed{
C_{\mathrm{closed}}
=
O(1)
+
T(n)
+
N(n)
+
C_{\mathrm{verify}}.
}
$$

只要：

$$
T(n)
$$

不是常數，

全域就不是常數。

---

# 8. API 真正降低的是什麼？

API 仍然可以帶來巨大真實進步。

它可以降低：

$$
C_{\mathrm{implementation}}
$$

對 caller 的負擔。

降低：

$$
C_{\mathrm{integration}}.
$$

降低：

$$
C_{\mathrm{deployment}}.
$$

降低：

$$
C_{\mathrm{coordination}}.
$$

所以：

$$
\boxed{
\text{API abstraction can reduce engineering complexity
without reducing the underlying problem's asymptotic complexity}.
}
$$

這兩者都是真實成果。

只是不能偷換。

---

# 9. Oracle Machine：理論上最乾淨的版本

給定 language：

$$
L.
$$

oracle：

$$
O_L(x)
$$

直接回答：

$$
x\in L?
$$

在 oracle machine 模型中：

$$
\boxed{
\text{oracle query}
}
$$

可以被規定成一個抽象步驟。

因此 relative complexity：

$$
P^{O_L}
$$

等類別有完全合法的理論意義。

但：

$$
\boxed{
P^{O_L}
}
$$

不是普通：

$$
P.
$$

因為 machine model 已改變。

---

# 10. Oracle 的真正意義

Oracle 不是假裝問題簡單。

它是在說：

> **假設某能力已被外部提供，其他問題在此能力存在時有多難？**

因此：

$$
\boxed{
\text{Oracle Complexity}
=
\text{Conditional Complexity}.
}
$$

條件是：

$$
O_L
$$

可用。

這與 Hyperconnected Computation 極其相似。

---

# 11. MSSP–RDR 可以看成 operational oracle fabric 嗎？

部分可以。

若：

$$
\mathcal A
=
\{
A_1,\ldots,A_N
\}
$$

且每一個 capability 都能被 address：

$$
1_i
$$

調用，

對 caller 而言，它們具有 oracle-like 性質。

但和抽象 oracle 不同：

- provider 有真實實作；
- provider 可能 failure；
- 有 latency；
- 有版本；
- 有 cost；
- 有 permission；
- 有 verification。

所以更準確是：

$$
\boxed{
\text{Operational Oracle Fabric}.
}
$$

---

# 12. 超連接計算不是把 oracle 當免費

成熟 Hyperconnected Runtime 應該記：

$$
\boxed{
C(1_i)
}
$$

不是只記：

$$
1_i\rightarrow A_i.
$$

也就是 capability manifest 應包含：

- expected latency；
- execution cost；
- hardware requirement；
- external dependency；
- confidence；
- verification cost。

---

# 13. Lookup Table：封閉世界最極端版本

設：

$$
f:
D_N\rightarrow Y
$$

且：

$$
D_N
$$

有限。

如果預先保存：

$$
T[x]=f(x),
$$

則：

$$
\boxed{
f(x)
=
T[x].
}
$$

適當 RAM/hash model 中，

lookup 可近似：

$$
O(1).
$$

這是真的。

---

# 14. 但 table 有多大？

如果：

$$
|D_N|=2^n,
$$

則完整 table 可能需要：

$$
\Omega(2^n)
$$

entries。

所以：

$$
\boxed{
C_{\mathrm{query}}=O(1)
}
$$

同時：

$$
\boxed{
C_{\mathrm{storage}}=\Omega(2^n)
}
$$

可以成立。

---

# 15. 誰建立 table？

更關鍵是：

$$
\boxed{
C_{\mathrm{build}}(T).
}
$$

如果每個答案：

$$
f(x)
$$

原本都很難求，

則建立 table 可能需要：

$$
\sum_{x\in D_N}C(f(x)).
$$

因此：

$$
\boxed{
\text{lookup compression}
}
$$

可能是：

$$
\boxed{
\text{massive offline precomputation}.
}
$$

---

# 16. Precomputation

對 input：

$$
x
$$

的 online algorithm：

$$
A(x).
$$

若在 query 前先建立：

$$
P_n,
$$

則：

$$
A(x\mid P_n).
$$

可能顯著更快。

因此：

$$
\boxed{
C_{\mathrm{online}}
(
x\mid P_n
)
<
C_{\mathrm{online}}
(x).
}
$$

這本身沒有問題。

---

# 17. Precompute Boundary

真正要問：

$$
\boxed{
C_{\mathrm{precompute}}(P_n)
}
$$

以及：

$$
\boxed{
|P_n|.
}
$$

如果：

$$
C_{\mathrm{precompute}}(P_n)
$$

或：

$$
|P_n|
$$

exponential，

那 online polynomial 不代表普通 uniform polynomial-time algorithm。

---

# 18. Precompute Once, Reuse Many Times

工程上，precompute 仍可能極有價值。

若：

$$
P_n
$$

使用：

$$
N
$$

次，

平均：

$$
\overline C_N
=
\frac{
C_{\mathrm{precompute}}
+
\sum_i C_{\mathrm{query},i}
}{
N
}.
$$

只要：

$$
N
$$

夠大，

amortized cost 可很低。

因此：

$$
\boxed{
\text{amortized usefulness}
\neq
\text{classical class collapse}.
}
$$

---

# 19. Advice：更敏感的邊界

在 complexity theory 中，nonuniform advice 允許 machine 對每個 input length：

$$
n
$$

獲得一段：

$$
a_n
$$

只依賴 $n$ 、不依賴具體 input 的 advice。

可寫：

$$
M(x,a_{|x|}).
$$

如果：

$$
|a_n|
$$

受到 polynomial bound，

便形成如：

$$
P/poly
$$

這類 nonuniform 模型。

---

# 20. Advice 的核心不是「作弊」

Advice model 是合法理論工具。

它問的是：

> 如果每個 input length 都可以帶入一份額外的 size-dependent information，計算能力會變成什麼？

因此：

$$
\boxed{
\text{Advice}
=
\text{explicit nonuniform external information}.
}
$$

---

# 21. 超連接系統很容易不自覺變成 advice system

假設每個 input size：

$$
n
$$

都有：

$$
S_n
$$

一套特製：

- model；
- table；
- circuit；
- index；
- solver bundle。

則 runtime：

$$
x
\rightarrow
S_{|x|}
\rightarrow
y.
$$

如果：

$$
S_n
$$

不是由 uniform efficient process 產生，

那系統其實帶有 nonuniformity。

---

# 22. Uniformity 是不能繞過的核心

經典算法要求的是某種 uniform：

$$
\boxed{
\text{one finite effective description}
}
$$

可以處理任意 input size。

若每個：

$$
n
$$

都需要全新的人為設計：

$$
A_n,
$$

則：

$$
\{A_n\}
$$

不必然是一個 uniform algorithm。

所以：

$$
\boxed{
\forall n\,\exists A_n
\not\Rightarrow
\exists A\,\forall n.
}
$$

---

# 23. 更細的量詞

對 language：

$$
L,
$$

錯誤直覺可能是：

$$
\forall x\in L,\exists A_x
$$

能快速回答 $x$。

但這非常弱。

因為可以直接令：

$$
A_x
$$

把答案硬編碼。

真正需要的是：

$$
\boxed{
\exists A_L
\forall x.
}
$$

而且：

$$
A_L
$$

具有符合要求的 asymptotic bound。

---

# 24. Instance-Specific Solver 幾乎總是能做得很短

給定固定 instance：

$$
x_0,
$$

可以建立：

```text
if input == x0:
    return answer0
```

對這個 instance：

$$
O(1).
$$

但這顯然沒有解決 problem family。

因此：

$$
\boxed{
\text{instance tractability}
\neq
\text{family tractability}.
}
$$

---

# 25. Hyperconnected trap

極限 MSSP–RDR 很容易產生：

$$
\{1_x\}_{x\in D}.
$$

每一個：

$$
1_x
$$

都直接返回答案。

那麼：

$$
\forall x,\quad
C_{\mathrm{invoke}}(1_x)=O(1).
$$

但如果：

$$
|\{1_x\}|
$$

exponential，

只是把 problem family 編碼成巨大 capability space。

---

# 26. 所以 edge count 也可能藏著答案

假設 graph：

$$
G_n
$$

為每個 input size 建立。

如果：

$$
G_n
$$

直接 encode 所有正確答案，

則：

$$
\boxed{
\text{computation}
\rightarrow
\text{graph structure}.
}
$$

query 變短。

但：

$$
|G_n|
$$

可能爆炸。

這正是：

# Complexity Spatialization

的極端版本。

---

# 27. Circuit View

另一種理解是：

每個 input size：

$$
n
$$

建立 circuit：

$$
C_n.
$$

如果：

$$
|C_n|
$$

polynomial，

這是極有意義的 nonuniform tractability。

如果：

$$
|C_n|
$$

exponential，

仍可理論求解，但沒有得到我們想要的 efficient family。

所以：

$$
\boxed{
\text{direct transition}
}
$$

仍需問其：

$$
\boxed{
\text{representation size}.
}
$$

---

# 28. 一個 Symbol 可以指向巨大 Circuit

若：

$$
1_n
\rightarrow
C_n,
$$

則 address size 可以很小。

例如：

$$
|\operatorname{name}(C_n)|=O(\log n)
$$

甚至固定格式。

但：

$$
|C_n|
$$

仍可能：

$$
2^n.
$$

所以：

$$
\boxed{
\text{small pointer}
\neq
\text{small referent}.
}
$$

這是 $1\rightarrow X$ 理論非常重要的限制。

---

# 29. Pointer Compression Fallacy

本文稱此錯誤為：

# Pointer Compression Fallacy

即：

> 因為一個巨大結構可以用短 pointer 表示，所以該巨大結構本身也具有短生成／建造成本。

形式上：

$$
|\operatorname{addr}(X)|
\ll
|X|
$$

不能推出：

$$
C_{\mathrm{construct}}(X)
\ll
|X|.
$$

---

# 30. Name Is Not Construction

例如：

$$
1_{\text{Wikipedia}}
$$

可以是很短的網址。

但：

$$
1_{\text{Wikipedia}}
$$

不等於 Wikipedia 的建造成本。

同樣：

$$
1_{\text{model}}
$$

不等於模型訓練成本。

$$
1_{\text{SAT-oracle}}
$$

也不等於 SAT oracle 的實現成本。

所以：

$$
\boxed{
\text{Name Complexity}
\neq
\text{Construction Complexity}.
}
$$

---

# 31. Representation Compression 與 Generative Compression

這裡要分兩種。

## Referential Compression

$$
1_X
\rightarrow
X
$$

只是 address 指向已有 $X$。

## Generative Compression

存在短 generator：

$$
G
$$

使：

$$
G(s_X)\rightarrow X.
$$

如果：

$$
C_G(X)
$$

很低，

這才是真正更強的壓縮。

因此：

$$
\boxed{
\text{short reference}
\neq
\text{short generator}.
}
$$

---

# 32. 超連接系統真正想要的是短 generator

如果每一條 edge 都要人工預建，

Hyperconnected Computation 很快會遇到：

$$
|E|\rightarrow\text{explosion}.
$$

所以真正強的架構需要：

$$
\boxed{
\mathcal G(q)
\rightarrow
e_q
}
$$

而且：

$$
C_{\mathcal G}(q)
$$

本身可控制。

這就是 Paper 03 的 Generative Hyperconnectivity。

---

# 33. 但 generator 也不能當免費 oracle

如果：

$$
\mathcal G
$$

內部：

$$
C_{\mathcal G}(q)=2^n,
$$

即使生成出的 edge 讓 execution：

$$
O(1),
$$

仍只有：

$$
\boxed{
\text{execution compression}.
}
$$

沒有：

$$
\boxed{
\text{global polynomial reduction}.
}
$$

---

# 34. Solver Construction Boundary

因此一個完整 solver pipeline：

$$
q
\rightarrow
A_q
\rightarrow
y
$$

至少拆成：

$$
\boxed{
C_{\mathrm{total}}
=
C_{\mathrm{construct}}(A_q)
+
C_{\mathrm{execute}}(A_q,q)
+
C_{\mathrm{verify}}.
}
$$

如果：

$$
C_{\mathrm{execute}}=O(1),
$$

但：

$$
C_{\mathrm{construct}}=2^n,
$$

總體仍可能 exponential。

---

# 35. Training-Time Externalization

AI 更容易出現此問題。

模型：

$$
M
$$

在 inference 時：

$$
M(x)\rightarrow y
$$

很快。

但 training：

$$
C_{\mathrm{train}}
$$

極大。

如果同一模型被廣泛重用，

這是非常成功的 amortization。

但不能說：

$$
\boxed{
\text{training problem itself became }O(1).
}
$$

---

# 36. Foundation Model 作為超大型 Advice-like State？

需要謹慎。

模型參數：

$$
\theta
$$

可以被理解為歷史資料與 optimization 的結果。

在某些分析視角下，它具有：

$$
\boxed{
\text{large persistent external state}
}
$$

的作用。

但不能直接把現代模型等同傳統 advice string，因為：

- 訓練過程不同；
- 輸入範圍不同；
- correctness 不同；
- asymptotic family 定義不同。

所以只能說：

$$
\boxed{
\text{structurally analogous in the sense of prepaid persistent state},
}
$$

不是理論等同。

---

# 37. Remote Agent

若：

$$
A_1
$$

遇到難題就問：

$$
A_2,
$$

且：

$$
A_2
$$

已有答案，

對：

$$
A_1
$$

成本低。

但是集體：

$$
A_1\cup A_2
$$

的形成成本、推理成本與記憶仍存在。

因此：

$$
\boxed{
\text{individual cognitive tractability}
\neq
\text{collective formation complexity}.
}
$$

---

# 38. Civilization Oracle

把整個人類文明當外部資料源：

$$
O_{\mathrm{civilization}}.
$$

一個人查：

```text
What is the FFT algorithm?
```

很快得到答案。

這不代表 FFT 被「第一次發現」的成本也是低的。

所以：

$$
\boxed{
\text{civilizational memory turns discovery into retrieval}.
}
$$

這是真實歷史加速。

---

# 39. Retrieval Is Not Discovery

本文正式區分：

$$
\boxed{
C_{\mathrm{retrieve}}
}
$$

與：

$$
\boxed{
C_{\mathrm{discover}}.
}
$$

對已有知識：

$$
C_{\mathrm{retrieve}}\ll C_{\mathrm{discover}}
$$

非常常見。

這正是知識文明的核心優勢。

---

# 40. Agentic Systems 會進一步放大這個差異

未來 agent：

$$
A_t
$$

可以使用：

- theorem database；
- code registry；
- proof archive；
- API ecosystem；
- past agent results。

所以：

$$
C_{\mathrm{retrieve}}
$$

會持續下降。

但研究全新問題時：

$$
C_{\mathrm{discover}}
$$

仍可能很高。

這就是 Agentic P/NP 要研究的另一層。

---

# 41. $O(1)$ 本身也依 machine model

即使 hash lookup 常被寫：

$$
O(1),
$$

也依賴：

- RAM model；
- word size；
- hash assumptions；
- expected vs worst-case；
- memory access model。

所以：

$$
\boxed{
O(1)
}
$$

永遠不是完全脫離模型的絕對敘述。

---

# 42. Input Reading Lower Bound

如果 input：

$$
x
$$

長度為：

$$
n,
$$

而算法必須讀完整 input，

則僅輸入讀取就可能：

$$
\Omega(n).
$$

所以聲稱：

$$
O(1)
$$

通常還要問：

> input 是否已經以某種 address / compressed state 預先存在？

這再次回到 computational boundary。

---

# 43. 一個 API Call 可能傳輸 O(n) Data

例如：

```text
solve(1GB_file)
```

call count 是 1。

但傳輸：

$$
1\text{GB}.
$$

因此：

$$
\boxed{
\text{Call Count Complexity}
\neq
\text{Communication Complexity}.
}
$$

---

# 44. Symbolic Call 也可能包含巨大 Input Handle

如果：

$$
1_D
$$

指向已有 dataset：

$$
D,
$$

則：

```text
analyze(dataset_id)
```

看似 input 很小。

但：

$$
D
$$

已經 materialized 在另一個位置。

所以：

$$
\boxed{
\text{input complexity has also been spatialized}.
}
$$

---

# 45. State-Resident Input

本文稱這種情況：

# State-Resident Input

即 input 不再透過 query text 完整提供，而已存在：

$$
D\in\mathfrak C_t.
$$

query 只傳：

$$
1_D.
$$

此時：

$$
C_{\mathrm{communication}}
$$

降低，

但：

$$
C_{\mathrm{storage}}
$$

存在。

---

# 46. Output 也可以如此

如果結果：

$$
Y
$$

極大，

系統只返回：

$$
1_Y.
$$

caller 看見：

$$
O(1)
$$

大小的 handle。

但：

$$
|Y|
$$

未消失。

所以：

$$
\boxed{
\text{output handle size}
\neq
\text{output state size}.
}
$$

---

# 47. Handle-Based Computation

未來超連接系統可能大量使用：

$$
1_X
$$

而不是 materialize $X$ 到 caller。

因此：

$$
1_A
\rightarrow
1_B
\rightarrow
1_C
$$

可以代表巨大 distributed computation。

這是很強的工程架構。

但 complexity accounting 必須沿 handle lineage 展開。

---

# 48. Lazy Materialization

若：

$$
X
$$

只在需要時 materialize，

可以節省：

$$
C_{\mathrm{active}}.
$$

所以：

$$
\boxed{
\text{lazy computation}
}
$$

可以真實降低無用工作。

這是 genuine reduction，不只是 hiding。

因此 Paper 04 的原則仍然成立：

> 要查帳，不是預設一切都沒變。

---

# 49. Memoization

若：

$$
f(x)
$$

第一次算完，

保存：

$$
M[x]=f(x).
$$

第二次：

$$
O(1)
$$

lookup。

這是：

$$
\boxed{
\text{instance-specific historical acceleration}.
}
$$

但對新：

$$
x',
$$

仍需重新算。

所以：

$$
\boxed{
\text{past solved instances}
\neq
\text{uniform future solver}.
}
$$

---

# 50. Infinite Memoization Thought Experiment

若理論上把所有：

$$
x
$$

答案都 memoize，

任何未來 query 都近似：

$$
O(1).
$$

但：

$$
\boxed{
\text{the memory state itself becomes the problem solution table}.
}
$$

其形成與大小就是核心成本。

這正是封閉有限世界與無界 asymptotic world 的根本差異。

---

# 51. Fixed Finite Domain 與 Asymptotic Domain

若：

$$
D
$$

固定有限，

那所有函數：

$$
f:D\to Y
$$

都能被 table 表示。

所以對固定 $D$：

$$
\boxed{
\text{lookup tractability is trivial in principle}.
}
$$

經典 complexity 真正關心：

$$
D_n,
\qquad
n\rightarrow\infty.
$$

也就是 family 如何擴張。

---

# 52. 超連接空間也必須隨 n 擴張

若：

$$
\mathfrak C_n
$$

是 input size $n$ 的 hyperconnected solver space，

就需要問：

$$
\boxed{
|\mathfrak C_n|
}
$$

如何增長。

以及：

$$
\boxed{
C_{\mathrm{build}}(\mathfrak C_n)
}
$$

如何增長。

如果：

$$
|\mathfrak C_n|=2^{\Theta(n)},
$$

則單次 query 即使 $O(1)$，也沒有得到 polynomial-size structure。

---

# 53. Hyperconnected Complexity 的核心三量

對 size $n$：

$$
\boxed{
H_n
=
(
S_n,
B_n,
Q_n
)
}
$$

其中：

- $S_n$：hyperconnected state / structure size；
- $B_n$：building / generation cost；
- $Q_n$：query cost。

極端查表：

$$
Q_n=O(1),
$$

但：

$$
S_n,B_n
$$

可能 exponential。

---

# 54. 真正強的超連接結果

若能做到：

$$
\boxed{
S_n=\operatorname{poly}(n),
}
$$

$$
\boxed{
B_n=\operatorname{poly}(n),
}
$$

且：

$$
\boxed{
Q_n=\operatorname{poly}(n),
}
$$

這才開始具有與經典 tractability 更強的關聯。

如果：

$$
Q_n=O(1)
$$

只是額外漂亮。

關鍵仍在 uniform constructibility。

---

# 55. Uniform Hyperconnection Generator

定義：

$$
\boxed{
G(1^n)
\rightarrow
\mathfrak C_n.
}
$$

若：

$$
C_G(n)=\operatorname{poly}(n)
$$

且：

$$
|\mathfrak C_n|=\operatorname{poly}(n),
$$

則：

$$
\mathfrak C_n
$$

是 polynomially constructible hyperconnected structure。

這是一個比「每個 n 有一個神秘網路」更強的條件。

---

# 56. Instance-Generated Channel

更動態版本：

$$
\boxed{
G(x)
\rightarrow
e_x.
}
$$

若：

$$
C_G(x)=\operatorname{poly}(|x|),
$$

且：

$$
e_x
$$

完成：

$$
x\rightarrow y
$$

的成本亦 polynomial，

那就不是把 exponential cost 偷藏到 channel generation。

---

# 57. 這接近真正的 algorithm

其實如果：

$$
G(x)
$$

能 polynomial time 產生 polynomial-cost solver path，

那：

$$
\boxed{
G
}
$$

本身已經非常接近普通 uniform algorithmic solution。

因此 Hyperconnected Computation 若要真正碰經典 $P/NP$，最終仍逃不掉：

$$
\boxed{
\text{uniform efficient construction}.
}
$$

---

# 58. 這是一個很重要的收束

超連接並沒有「繞過」經典複雜度理論。

它只是把問題拆得更細：

$$
\boxed{
\text{Where does the solver come from?}
}
$$

$$
\boxed{
\text{Where is it stored?}
}
$$

$$
\boxed{
\text{Who pays for it?}
}
$$

$$
\boxed{
\text{Can it be generated uniformly?}
}
$$

---

# 59. External Provider 也可以是 polynomial

不是所有外包都不合法。

如果 provider：

$$
P
$$

本身有 polynomial algorithm，

那整體：

$$
C_{\mathrm{closed}}
$$

仍可能 polynomial。

因此：

$$
\boxed{
\text{externalization}
}
$$

不自動破壞 tractability。

真正關鍵是 provider 的成本。

---

# 60. Distributed Polynomial Computation

多台機器：

$$
M_1,\ldots,M_k
$$

共同工作。

只要資源 accounting 仍保持 polynomial bounds，

仍可以是有效 tractable computation。

所以：

$$
\boxed{
\text{distributed}
\neq
\text{non-polynomial}.
}
$$

---

# 61. Parallelism 的陷阱

假設：

$$
2^n
$$

台機器同時各測一個 candidate。

wall-clock：

$$
O(1)
$$

或：

$$
O(n)
$$

可能成立。

但 processor count：

$$
2^n.
$$

因此：

$$
\boxed{
T_{\mathrm{wall}}\downarrow
}
$$

不代表：

$$
\boxed{
W_{\mathrm{total}}\downarrow.
}
$$

---

# 62. Work Complexity

定義：

$$
\boxed{
W
=
\sum_i
T_i
}
$$

或更一般地計算 total primitive work。

因此平行算法至少要區分：

$$
\boxed{
T_{\mathrm{span}}
}
$$

與：

$$
\boxed{
W_{\mathrm{work}}.
}
$$

這對「極致同步／相位計算看似 O(1)」尤其重要。

---

# 63. Phase Computation 的同一問題

若：

$$
N
$$

個物理元件同時演化，

時間可能近似：

$$
O(1)
$$

但硬體規模：

$$
O(N)
$$

甚至：

$$
O(N^2)
$$

coupling。

因此：

$$
\boxed{
\text{parallel physical evolution}
\neq
\text{zero resource complexity}.
}
$$

---

# 64. 一個符號控制 2^n 個元件

如果：

$$
1
\rightarrow
X_{2^n}
$$

一個控制符號啟動：

$$
2^n
$$

物理單元，

caller complexity：

$$
O(1).
$$

hardware complexity：

$$
\Omega(2^n).
$$

這是最純粹的：

# Control-to-Resource Expansion

---

# 65. Control Complexity 與 Realization Complexity

因此新增分離：

$$
\boxed{
C_{\mathrm{control}}
\neq
C_{\mathrm{realization}}.
}
$$

Hyperconnected Computation 可以把：

$$
C_{\mathrm{control}}
$$

壓得極低。

但真正世界仍受：

$$
C_{\mathrm{realization}}
$$

約束。

---

# 66. Verification 不能被忘記

假設 external provider 返回：

$$
y.
$$

如果：

$$
y
$$

不可驗證，

那 caller 並沒有完成可靠 computation。

因此：

$$
\boxed{
C_{\mathrm{task}}
=
C_{\mathrm{obtain}}
+
C_{\mathrm{verify}}
}
$$

至少成立。

---

# 67. NP 的特殊趣味

對 NP language，

正確 witness 在 polynomial time 可驗證。

這使：

$$
\boxed{
\text{find}
}
$$

與：

$$
\boxed{
\text{verify}
}
$$

高度不對稱。

如果 oracle 給 witness：

$$
w,
$$

verification 可能 polynomial。

但：

$$
\boxed{
\text{oracle gave the hard part}.
}
$$

所以：

$$
\text{cheap verification}
$$

仍不等於：

$$
\text{cheap discovery}.
$$

---

# 68. 外包 Witness

極端 MSSP–RDR：

$$
x
\rightarrow
\text{WitnessProvider}
\rightarrow
w
\rightarrow
V(x,w).
$$

本地：

$$
\operatorname{poly}(n).
$$

但 provider：

$$
C_{\mathrm{find}}(w)
$$

未必 polynomial。

因此：

$$
\boxed{
NP\text{-verification tractability}
}
$$

不能被誤寫為：

$$
P=NP.
$$

---

# 69. Positive Result 的 Constructive Burden

如果未來要宣稱：

$$
P=NP,
$$

真正具有工程意義的正向 witness 應包含：

$$
\boxed{
A_{\mathrm{SAT}}
}
$$

並證明：

$$
T_A(n)
\leq
n^k
$$

或其他 polynomial bound。

只說：

> 有一個 API 可以回答 SAT。

完全不夠。

---

# 70. API Behind the Curtain

真正要問：

$$
\boxed{
\text{What is behind the API?}
}
$$

如果背後：

$$
A_{\mathrm{SAT}}
$$

真的 polynomial，

那是重大結果。

如果背後：

$$
2^n
$$

search，

只是 outsourcing。

---

# 71. Hyperconnected P/NP 的第一道審查

任何聲稱：

> 超連接讓 NP 問題變簡單。

至少要回答：

1. capability 如何建立？
2. capability size 如何隨 $n$ 成長？
3. provider runtime 如何成長？
4. 是否使用 exponential parallelism？
5. 是否使用 nonuniform advice？
6. 是否使用 oracle assumption？
7. 是否只解有限 instance set？
8. 是否改寫 task contract？

---

# 72. Complexity Boundary Certificate

本文提出一個候選證書：

$$
\boxed{
C_B
=
(
\mathfrak B,
M,
R,
P,
A,
V
)
}
$$

其中：

- $\mathfrak B$：accounting boundary；
- $M$：machine / computational model；
- $R$：resource vector；
- $P$：precompute / preprocessing allowance；
- $A$：advice / external information allowance；
- $V$：verification obligation。

任何重大 complexity claim 都應附帶：

$$
C_B.
$$

---

# 73. 例如「API 是 O(1)」

正確聲明：

> 在 caller-side interface model 中，假設 endpoint address 已知、request size 有界、network/provider 成本排除於 boundary 外，API invocation count 為 $O(1)$。

這是精確的。

錯誤聲明：

> 這個 problem 現在是 $O(1)$。

兩者不是同一句話。

---

# 74. Closed Boundary Expansion Test

如果懷疑某個 $O(1)$ 是外包造成，

做：

$$
\boxed{
\mathfrak B_0
\subset
\mathfrak B_1
\subset
\cdots
\subset
\mathfrak B_k
}
$$

逐步擴大 accounting boundary。

如果 cost 隨 boundary 擴大重新出現，

則：

$$
\boxed{
\text{the complexity was externalized}.
}
$$

---

# 75. Boundary Expansion Example

第一層：

$$
\mathfrak B_0
=
\text{caller}.
$$

看到：

$$
O(1).
$$

第二層：

$$
\mathfrak B_1
=
\text{caller + network}.
$$

看到：

$$
O(n).
$$

第三層：

$$
\mathfrak B_2
=
\text{caller + network + provider}.
$$

看到：

$$
O(2^n).
$$

此時即可定位：

$$
\boxed{
\text{complexity resides in provider}.
}
$$

---

# 76. Precompute Expansion Test

同樣，

先只看：

$$
C_{\mathrm{online}}.
$$

再加入：

$$
C_{\mathrm{offline}}.
$$

如果：

$$
O(1)
\rightarrow
O(2^n),
$$

則：

$$
\boxed{
\text{online speed was prepaid}.
}
$$

---

# 77. Advice Expansion Test

如果不同：

$$
n
$$

需要不同：

$$
S_n,
$$

則問：

$$
\boxed{
\text{Who constructs }S_n?
}
$$

若沒有 uniform efficient constructor，

則 complexity 被放在 nonuniform structure 中。

---

# 78. State Formation Test

若 solver state：

$$
\Sigma_n^\star
$$

使 query 很快，

問：

$$
\boxed{
C(
\Sigma_0
\rightarrow
\Sigma_n^\star
).
}
$$

如果 formation cost exponential，

不能把 query cost 當成 total capability cost。

---

# 79. 超連接真正的價值反而更清楚了

經過這些限制後，Hyperconnected Computation 並沒有失去價值。

反而可以精確說：

它真正擅長降低：

$$
\boxed{
C_{\mathrm{resolve}},
C_{\mathrm{coord}},
C_{\mathrm{integration}},
C_{\mathrm{reuse}},
C_{\mathrm{communication\ planning}}.
}
$$

並透過 historical reuse 降低：

$$
C_{\mathrm{average}}.
$$

這些都是巨大的工程收益。

---

# 80. 超連接不需要假裝解掉複雜度理論

真正有力的主張是：

$$
\boxed{
\text{Hyperconnected Computation changes
the distribution and reuse of computational burden.}
}
$$

而不是：

$$
\boxed{
\text{Hyperconnected Computation automatically collapses all complexity classes.}
}
$$

---

# 81. Closed-System Hyperconnected Tractability

現在可以提出：

若在指定 boundary：

$$
\mathfrak B
$$

中，

對任務族：

$$
Q,
$$

存在 Hyperconnected Runtime：

$$
H,
$$

使：

$$
\boxed{
C_{\mathrm{closed}}
(
q\mid H
)
\leq
\operatorname{poly}(|q|)
}
$$

對所有：

$$
q\in Q,
$$

則可稱：

# Closed-System Hyperconnected Tractability

這仍是一個新的系統級概念，不自動等同經典 $P$。

---

# 82. 為什麼不直接叫 P？

因為：

$$
H
$$

可能包含：

- persistent state；
- multiple machines；
- distributed providers；
- dynamic capabilities；
- precomputation；
- agent history。

這些 machine assumptions 比標準 deterministic Turing machine 更豐富。

所以需要保留新的名稱。

---

# 83. 但可以建立對應條件

如果進一步證明：

1. $H$ 可由標準 machine polynomially simulate；
2. 所有 persistent state 可 polynomially construct；
3. advice 不超出合法 uniform bound；
4. communication、hardware、parallel work 都 polynomial；
5. task family 與 classical language 對應；

才可能把結論提升回經典 complexity claim。

---

# 84. Simulation Bridge

因此未來需要：

$$
\boxed{
\mathsf{Sim}:
H
\rightarrow
M_{\mathrm{standard}}
}
$$

並證明：

$$
C_{\mathsf{Sim}}
=
\operatorname{poly}.
$$

這是 Hyperconnected P/NP 與 classical P/NP 之間的必要橋。

---

# 85. 第一道主命題：Local–Global Separation

## Local–Global Complexity Separation Principle

存在計算架構使：

$$
\boxed{
C_{\mathrm{local}}(q)=O(1)
}
$$

同時：

$$
\boxed{
C_{\mathrm{closed}}(q)=\Omega(f(n)),
}
$$

其中：

$$
f(n)\rightarrow\infty.
$$

因此：

$$
\boxed{
O(1)_{\mathrm{local}}
\not\Rightarrow
O(1)_{\mathrm{global}}.
}
$$

---

# 86. 第二道主命題：Reference–Referent Separation

若：

$$
a_X
$$

是 $X$ 的 address，

則：

$$
\boxed{
|a_X|
\ll
|X|
}
$$

不推出：

$$
\boxed{
C_{\mathrm{construct}}(X)
\leq
\operatorname{poly}(|a_X|).
}
$$

即：

$$
\boxed{
\text{short reference}
\neq
\text{cheap referent}.
}
$$

---

# 87. 第三道主命題：Offline–Online Separation

存在：

$$
P_n
$$

使：

$$
C_{\mathrm{online}}
(
x\mid P_n
)
=O(1),
$$

但：

$$
C_{\mathrm{precompute}}(P_n)
$$

可為 exponential。

因此：

$$
\boxed{
O(1)_{\mathrm{online}}
\not\Rightarrow
O(1)_{\mathrm{lifecycle}}.
}
$$

---

# 88. 第四道主命題：Nonuniformity Warning

$$
\boxed{
\forall n\,\exists S_n
}
$$

不推出存在 uniform efficient constructor：

$$
\boxed{
\exists G\,
\forall n:
G(1^n)=S_n.
}
$$

因此：

$$
\boxed{
\text{size-indexed solver availability}
\neq
\text{uniform algorithm availability}.
}
$$

---

# 89. 第五道主命題：Parallelism Accounting

若：

$$
T_{\mathrm{wall}}(n)=O(1)
$$

透過：

$$
P(n)=2^n
$$

processors 達成，

則：

$$
\boxed{
\text{constant wall time}
}
$$

不代表：

$$
\boxed{
\text{polynomial total work}.
}
$$

---

# 90. 第六道主命題：Task-Identity Constraint

若：

$$
q'
$$

因放寬成功條件而變簡單，

則：

$$
C(q')<C(q)
$$

不能被當成：

$$
q
$$

的 complexity collapse。

必須有：

$$
\boxed{
q'\equiv_{\mathfrak I_q}q.
}
$$

---

# 91. 七種「假的全域 O(1)」

本文總結七種常見來源：

1. **Interface O(1)**  
   一個 function/API call。

2. **Pointer O(1)**  
   一個小 handle 指向巨大資料。

3. **Lookup O(1)**  
   巨大預計算 table。

4. **Oracle O(1)**  
   把困難能力列為 primitive。

5. **Parallel-time O(1)**  
   用超大量 hardware 換 wall time。

6. **Advice-assisted O(1)**  
   外部提供巨大／nonuniform state。

7. **Instance-hardcoded O(1)**  
   每個 instance 個別存答案。

它們都可以在各自局部模型中合法是 $O(1)$。

但都不能自動升級成：

$$
O(1)_{\mathrm{uniform\ closed}}.
$$

---

# 92. 真正的全域 O(1) 要多強？

如果真的宣稱：

$$
C_{\mathrm{closed}}(n)=O(1),
$$

那至少意味：

- input handling；
- routing；
- compute；
- provider；
- output；
- verification；

全部在指定 resource model 中與 $n$ 無關。

對非平凡可變長 input 問題，這本身就是非常強的聲明。

所以應極度謹慎。

---

# 93. 更合理的目標不是追求 O(1)

實際工程中，更重要可能是：

$$
\boxed{
C_{\mathrm{closed,new}}(n)
<
C_{\mathrm{closed,old}}(n).
}
$$

或：

$$
\boxed{
\overline C_N
\downarrow.
}
$$

或：

$$
\boxed{
d_{\mathrm{eff}}
\downarrow.
}
$$

不需要每次都追求戲劇性的：

$$
O(1).
$$

---

# 94. Hyperconnected Tractability 的成熟版本

因此一個成熟定義應包含：

$$
\boxed{
\mathfrak H
=
(
\mathfrak B,
\mathcal M,
\mathcal A,
\mathcal G,
\mathbf C,
\mathcal V
).
}
$$

其中：

- $\mathfrak B$：system boundary；
- $\mathcal M$：machine/configuration model；
- $\mathcal A$：available capabilities；
- $\mathcal G$：channel/capability generator；
- $\mathbf C$：resource accounting；
- $\mathcal V$：verification rules。

沒有這些，單說「超連接很快」不夠。

---

# 95. 與 Ultimate P/NP 的接點

現在我們可以更清楚地重述：

Ultimate / Agentic P/NP 不應問：

> 如果所有答案都已經在外面，AI 是否能一秒拿到？

那太容易。

真正問題是：

$$
\boxed{
\text{一個智能計算系統如何形成、
發現、生成、驗證與維持那些讓問題變 tractable 的能力？}
}
$$

這才是：

# Algorithmic Emergence

而不是只有 Algorithmic Existence。

---

# 96. Solver Availability 與 Solver Emergence

區分：

$$
\boxed{
\exists A
}
$$

和：

$$
\boxed{
\Sigma_t
\xrightarrow{\text{agentic process}}
A.
}
$$

若：

$$
A
$$

已經放在 registry，

availability 問題簡單。

若：

$$
A
$$

尚不存在，

emergence 問題才開始。

---

# 97. 複雜度外包的最終邊界

如果一個系統永遠可以說：

> 「外面有某個神秘 provider 幫我算。」

那任何問題都能形式上變：

$$
O(1)_{\mathrm{local}}.
$$

這顯然無法區分真正能力。

因此最終必須封閉 boundary：

$$
\boxed{
\mathfrak B_{\mathrm{closed}}.
}
$$

這就是下一篇真正要處理的主題。

---

# 98. Paper 06 的問題

如果不准無限外包，

而是指定：

$$
\boxed{
\text{所有必要計算責任都必須在某一封閉邊界中被核算},
}
$$

那麼：

- local；
- remote；
- precompute；
- model；
- memory；
- hardware；
- history；

要如何統一歸責？

這就是：

# Computational Boundary Theory

---

# 99. 系列第二部分目前的位置

Paper 04 建立：

$$
\boxed{
\text{Complexity Displacement Principle}.
}
$$

本文 Paper 05 建立：

$$
\boxed{
O(1)_{\mathrm{local}}
\neq
O(1)_{\mathrm{global}}.
}
$$

下一篇 Paper 06 將建立：

$$
\boxed{
\text{Closed / Open Computational Boundary}.
}
$$

完成後才有足夠基礎正式進入封閉世界 P/NP。

---

# 100. 結論

超連接計算最極端的夢想是：

$$
\boxed{
\text{一個符號}
\rightarrow
\text{一個能力}.
}
$$

如果每個能力都有唯一 address，

那高階 caller 確實可以生活在一個近似：

$$
\boxed{
O(1)_{\mathrm{invocation}}
}
$$

的世界。

這不是幻覺。

它是 abstraction、reuse、routing、API、memory 與歷史積累共同創造的真實文明能力。

但：

$$
\boxed{
\text{一個符號能叫到某個能力，
不代表建立、維持與執行該能力只需要一個符號的成本。}
}
$$

因此：

$$
\boxed{
\text{Name}
\neq
\text{Construction}.
}
$$

$$
\boxed{
\text{Pointer}
\neq
\text{Referent}.
}
$$

$$
\boxed{
\text{Invocation}
\neq
\text{Execution}.
}
$$

$$
\boxed{
\text{Retrieval}
\neq
\text{Discovery}.
}
$$

$$
\boxed{
\text{Online}
\neq
\text{Lifecycle}.
}
$$

$$
\boxed{
\text{Local}
\neq
\text{Closed}.
}
$$

所以本文最核心公式是：

$$
\boxed{
O(1)_{\mathrm{local}}
\not\Rightarrow
O(1)_{\mathrm{closed}}.
}
$$

而對 P/NP 更關鍵的是：

$$
\boxed{
\forall x\,\exists A_x
\not\Rightarrow
\exists A\,\forall x.
}
$$

以及：

$$
\boxed{
\forall n\,\exists S_n
\not\Rightarrow
\exists G_{\mathrm{poly}}\,
\forall n:
G_{\mathrm{poly}}(1^n)=S_n.
}
$$

因此，如果未來某個極限 MSSP–RDR 系統宣稱：

> 「我所有 NP 問題都只需要一次 capability call。」

真正需要問的並不是：

> 「call 是不是一步？」

而是：

$$
\boxed{
\text{這些 capability 從哪裡來？}
}
$$

$$
\boxed{
\text{它們的大小是多少？}
}
$$

$$
\boxed{
\text{它們如何隨 input size 擴張？}
}
$$

$$
\boxed{
\text{能否由一個 uniform efficient process 建立？}
}
$$

只有當這些問題也得到受控答案，超連接計算才有可能從：

$$
\boxed{
\text{Local Hyperconnected Tractability}
}
$$

向真正更強的：

$$
\boxed{
\text{Closed-System Computational Tractability}
}
$$

前進。

---

## 本篇核心分離式

$$
\boxed{
O(1)_{\mathrm{invoke}}
\neq
O(1)_{\mathrm{provider}}
}
$$

$$
\boxed{
O(1)_{\mathrm{online}}
\neq
O(1)_{\mathrm{lifecycle}}
}
$$

$$
\boxed{
\text{short pointer}
\neq
\text{small structure}
}
$$

$$
\boxed{
\text{short reference}
\neq
\text{short generator}
}
$$

$$
\boxed{
\text{instance-specific solver}
\neq
\text{uniform solver}
}
$$

$$
\boxed{
\text{constant wall time}
\neq
\text{constant total work}
}
$$

以及最重要的：

$$
\boxed{
O(1)_{\mathrm{local}}
\neq
O(1)_{\mathrm{global}}.
}
$$

---

## 下一篇

**Paper 06 / 09**

# 計算邊界論：封閉系統、開放系統與複雜度責任的重新定位

## Computational Boundary Theory: Closed Systems, Open Systems, and the Relocation of Complexity Responsibility