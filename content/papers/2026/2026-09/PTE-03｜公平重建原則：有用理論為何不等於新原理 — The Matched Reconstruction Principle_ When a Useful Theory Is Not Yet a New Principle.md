# PTE-03｜公平重建原則：有用理論為何不等於新原理

## The Matched Reconstruction Principle: When a Useful Theory Is Not Yet a New Principle

**系列：** 《假設你是對的》／Provisional Truth Engineering Series（PTE）  
**系列文件：** PTE-03 / 07  
**版本：** v0.1  
**日期：** 2026-09-09  
**作者：** Neo.K  
**研究協作：** AI-assisted theoretical development  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 公開方法論論文／理論比較、強基線與不可約新穎性判定  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

一套理論若能產生有用的工程架構、改善系統穩定性、降低錯誤、提升可解釋性或提供新的設計語言，直覺上很容易被進一步推論為：該理論揭示了新的計算原理、不可約機制或比既有方法更深的基礎結構。然而，這個推論並不成立。

本文提出 **Matched Reconstruction Principle（MRP，公平重建原則）**，作為 Provisional Truth Engineering（PTE）中判定「理論有用」與「理論不可約新穎」之間差異的核心方法。

設由理論 $T$ 導出的可執行系統為：

$$
S_T,
$$

設在相同資訊、相同任務、相同資源與相同驗收條件下，由既有方法構造出的最強公平重建為：

$$
B^{*}(T).
$$

則定義理論專屬增益：

$$
\boxed{
\Delta_T
=
M(S_T)-M(B^{*}(T)).
}
$$

其中 $M$ 是事先凍結的評測函數。

若：

$$
\Delta_T>0,
$$

只能說：

> 在目前 baseline family、資料、資源與測試域下，存在尚未被既有重建吸收的觀測差異。

仍不能立即推出：

$$
T=\text{new primitive}.
$$

反之，若：

$$
\Delta_T=0,
$$

也不能推出：

$$
T=\text{useless}.
$$

更精確的結論是：

$$
\boxed{
\text{Measured behavior is reconstructible by known machinery under the matched test}.
}
$$

本文特別區分四種容易混淆的結果：

$$
\text{Useful}
\neq
\text{Superior}
\neq
\text{Unique}
\neq
\text{Fundamental}.
$$

一套理論可以具有高度概念價值、規格價值、工程價值與組織價值，但其被測量的行為仍可由 typed graph、constraint system、event sourcing、dynamic registry、optimization、probabilistic inference 或其他既有計算框架完整重建。

本文進一步定義：

- **Matched Information Condition**；
- **Matched Resource Condition**；
- **Matched Task Contract**；
- **Matched Candidate Space**；
- **Independent Causal Path**；
- **Baseline Closure**；
- **Reconstruction Burden**；
- **Theory-Specific Residual Gain**；
- **Reconstruction Equivalence Class**。

並提出：若一個理論的所有工程優勢皆可在不引用其專屬術語、不共享其決策函式、只使用同一 observable information 的情況下被獨立重建，則該結果支持的是：

$$
\boxed{
V_E(T)>0
}
$$

但尚不支持：

$$
\boxed{
V_U(T)>0.
}
$$

其中 $V_E$ 是工程價值， $V_U$ 是不可約／獨特價值。

本文最後提出 **Strong Baseline Duty（強基線義務）**：

> 理論主張越強，評測者越有義務為其建立越強的公平對照，而不是以弱 baseline 製造「勝利」。

PTE 的目標不是讓理論更容易輸，而是讓「它究竟在哪裡真的不同」變得更清楚。真正值得進一步追蹤的，不是任何可觀測改善，而是：

$$
\boxed{
R_T
=
\text{gain that survives strongest known matched reconstruction}.
}
$$

**關鍵詞：** Matched Reconstruction、Strong Baseline、Theory-Specific Gain、Reconstruction Equivalence、Fair Comparison、Ablation、Independent Implementation、Irreducible Novelty、Baseline Closure、Provisional Truth Engineering

---

# 0. 邊界聲明

本文不主張：

- 既有方法一定能重建所有新理論；
- strong baseline 可以被完全窮盡；
- baseline tie 等於理論沒有價值；
- baseline 勝出等於原理論完全錯誤；
- 一次 benchmark 就能判斷理論是否 fundamental；
- 相同行為一定代表相同內部機制；
- 不同行為一定代表新的 primitive；
- conventional reconstruction 比理論原始表述「更正確」；
- 工程可重建性可以直接否定哲學、本體論或詮釋價值；
- 任一 baseline family 都具有永久封閉性；
- 所有新理論都應被還原成舊理論。

本文只研究：

> 在一個指定測試域內，當理論導出的系統產生某種可觀測優勢時，如何判斷該優勢是否真的需要理論專屬機制，還是可以由已知一般框架在相同資訊與資源下獨立重建。

---

# 1. 最容易犯的錯：有用，所以一定新

設理論：

$$
T.
$$

由它導出：

$$
S_T.
$$

如果：

$$
M(S_T)
>
M(B_0),
$$

其中：

$$
B_0
$$

是一個弱 baseline，

人們很容易說：

> 理論 $T$ 真的有效。

這可能是真的。

但接著常出現第二個推論：

> 所以 $T$ 揭示了新的計算原理。

這一步沒有被證明。

---

## 1.1 第一個區分

$$
\boxed{
\text{Useful}
\neq
\text{Unique}.
}
$$

---

## 1.2 第二個區分

$$
\boxed{
\text{Unique}
\neq
\text{Fundamental}.
}
$$

某方法在現有 benchmark 上沒有已知等價物，

也不表示它是自然界或計算理論中的新基本律。

---

# 2. 四層價值不能混成一層

本文區分：

$$
\boxed{
\text{Utility}
\rightarrow
\text{Superiority}
\rightarrow
\text{Uniqueness}
\rightarrow
\text{Fundamentality}
}
$$

但這不是必然推論鏈。

---

## 2.1 Utility

若：

$$
M(S_T)>M(B_{\mathrm{naive}}),
$$

可說：

$$
\boxed{
\text{The theory-derived system is useful relative to the naive baseline}.
}
$$

---

## 2.2 Superiority

若對最強公平 baseline：

$$
M(S_T)>M(B^{*}),
$$

才有：

$$
\boxed{
\text{Measured superiority under current conditions}.
}
$$

---

## 2.3 Uniqueness

若所有已知可接受重建都無法複現差異：

$$
\forall B\in\mathcal B,
\quad
M(S_T)>M(B),
$$

才能開始談：

$$
\text{current evidence for uniqueness}.
$$

---

## 2.4 Fundamentality

要稱為新 primitive，

通常還需要：

- 更廣泛域；
- 理論不可約性；
- 形式分析；
- 跨實作穩定性；
- 外部重現；
- 排除等價重參數化；
- 排除隱藏資源；
- 排除實驗偶然性。

因此：

$$
\boxed{
\text{Benchmark Win}
\not\Rightarrow
\text{New Fundamental Principle}.
}
$$

---

# 3. 公平重建原則

**定義 3.1（Matched Reconstruction Principle）**

若理論 $T$ 產生可執行系統：

$$
S_T,
$$

則任何 theory-specific advantage 的主張都應與一個滿足公平條件的最強已知重建：

$$
B^{*}(T)
$$

比較。

---

## 3.1 基本形式

$$
\boxed{
\Delta_T
=
M(S_T)
-
M(B^{*}(T)).
}
$$

---

## 3.2 若 $\Delta_T=0$

只能推出：

$$
\boxed{
\text{Observed gain is reconstructible under the current matched test}.
}
$$

---

## 3.3 若 $\Delta_T>0$

只能推出：

$$
\boxed{
\text{A residual behavioral difference remains under the current baseline family}.
}
$$

仍不是：

$$
\boxed{
\text{new primitive established}.
}
$$

---

# 4. 什麼叫「matched」？

如果資訊不匹配，

比較幾乎沒有認識論價值。

---

## 4.1 Matched Information Condition

設：

$$
\mathcal O_T
$$

為 theory system 可觀測資訊，

$$
\mathcal O_B
$$

為 baseline 可觀測資訊。

要求：

$$
\boxed{
\mathcal O_T
=
\mathcal O_B.
}
$$

---

## 4.2 例子

如果 $S_T$ 可以看到：

- canonical ID；
- entity type；
- provenance；
- temporal history；

而 baseline 只能看到：

- surface string；

那麼：

$$
M(S_T)>M(B)
$$

可能只是資訊優勢。

---

# 5. Matched Data Condition

設：

$$
\mathcal D_T
$$

和：

$$
\mathcal D_B
$$

分別為兩邊可存取資料。

要求：

$$
\boxed{
\mathcal D_T
=
\mathcal D_B.
}
$$

---

## 5.1 禁止 hidden corpus advantage

若 theory system 使用：

- 更大知識庫；
- 額外標註；
- 額外人工校正；

則不能直接把效果歸因於理論。

---

# 6. Matched Candidate Space

若問題需要從候選集合：

$$
\mathcal C
$$

中選擇，

要求：

$$
\boxed{
\mathcal C_T
=
\mathcal C_B.
}
$$

---

## 6.1 為什麼重要？

若：

$$
|\mathcal C_T|=5,
$$

$$
|\mathcal C_B|=5000,
$$

即使結果不同，

也不是公平比較。

---

# 7. Matched Task Contract

兩套系統必須回答同一問題。

定義：

$$
\mathcal K
=
(
\text{input},
\text{output},
\text{constraints},
\text{success},
\text{failure}
).
$$

要求：

$$
\boxed{
\mathcal K_T
=
\mathcal K_B.
}
$$

---

## 7.1 常見偷換

Theory system：

> 可以 abstain。

Baseline：

> 必須 always answer。

這樣：

$$
\text{unsafe error}
$$

不可直接比較。

---

# 8. Matched Resource Condition

設：

$$
\mathcal R
=
(
\text{compute},
\text{latency},
\text{memory},
\text{model access},
\text{tools}
).
$$

理想上要求：

$$
\mathcal R_T
\approx
\mathcal R_B.
$$

---

## 8.1 不要求完全相同

某些理論架構天然需要不同內部資料結構。

因此真正要求的是：

$$
\boxed{
\text{no hidden resource subsidy}.
}
$$

---

# 9. Matched Evaluation Function

評測函數：

$$
M
$$

必須在 run 前固定。

禁止：

$$
M_{\mathrm{after}}
=
f(\text{observed result}).
$$

---

## 9.1 否則

會形成：

$$
\text{metric shopping}.
$$

---

# 10. Strongest Baseline Duty

**原則 10.1（Strong Baseline Duty）**

若理論主張：

$$
\text{novel computational principle},
$$

評測者不應只建立：

$$
B_{\mathrm{weak}}.
$$

而應主動尋找：

$$
\boxed{
B^{*}
=
\text{strongest reasonable known reconstruction}.
}
$$

---

## 10.1 為什麼這反而是對理論公平？

因為：

> 一個只能打贏弱 baseline 的理論，其真正新穎性反而不清楚。

---

## 10.2 越強的 baseline

若理論仍然勝，

則：

$$
\text{Evidence for irreducible residue}\uparrow.
$$

---

# 11. Conventional 不等於落後

「conventional」在 PTE 中不是：

> 過時方法。

而是：

> 不依賴被測理論專屬主張、但可以使用現有一般計算工具的獨立重建。

例如：

- graph；
- typed relations；
- constraint satisfaction；
- dynamic registry；
- event sourcing；
- probabilistic inference；
- optimization；
- automata；
- database transactions；
- versioned state；
- generic error correction。

---

# 12. Independent Causal Path

這是整個 MRP 最容易被忽略的條件。

---

## 12.1 假 baseline

若：

```text
baseline_validate(...)
    return theory_validate(...)
```

那麼：

$$
S_T
$$

與：

$$
B
$$

不是獨立比較。

---

## 12.2 正式要求

設：

$$
P_T
$$

為 theory decision path，

$$
P_B
$$

為 baseline decision path。

至少要求：

$$
\boxed{
P_T
\not\equiv
P_B
}
$$

在因果實作層。

---

## 12.3 Structural Independence Test

可以故意破壞：

$$
P_T
$$

的某個 internal helper，

要求：

$$
P_B
$$

仍可正常完成。

反之亦然。

---

# 13. Shared Primitive 不一定破壞公平

兩邊可以共享：

- JSON parser；
- database driver；
- tokenizer；
- common dataclass；
- generic hash function。

但不應共享：

- 核心 semantic predicate；
- 核心 decision rule；
- theory-specific invariant checker。

---

# 14. Baseline Family

單一 baseline 仍可能太弱。

定義：

$$
\boxed{
\mathcal B
=
\{B_1,B_2,\ldots,B_n\}.
}
$$

其中可包括：

```text
naive
retrieval
typed
graph
constraint
dynamic
event-sourced
probabilistic
full conventional
```

---

## 14.1 最強 baseline

$$
\boxed{
B^{*}
=
\arg\max_{B_i\in\mathcal B}
M(B_i)
}
$$

前提是：

$$
B_i
$$

全部滿足 matched conditions。

---

# 15. Baseline Closure

**定義 15.1（Baseline Closure）**

若新增多個合理 baseline 後，

最佳 conventional performance：

$$
M(B^{*})
$$

趨於穩定，

則稱在目前 baseline family 下接近：

$$
\boxed{
\text{Baseline Closure}.
}
$$

---

## 15.1 形式化

若：

$$
B^{*(k)}
$$

為前 $k$ 個 baseline 的最佳者，

且：

$$
\lim_{k\rightarrow n}
M(B^{*(k)})
=
L,
$$

並且後續合理 baseline 不再顯著提升，

則可說：

> current baseline family is approaching closure.

---

## 15.2 不是永久閉合

永遠保留：

$$
\boxed{
\text{Future Reconstruction Possible}.
}
$$

---

# 16. Reconstruction Equivalence Class

如果多個不同機制：

$$
B_1,B_2,B_3
$$

在目前 observable space 上皆與：

$$
S_T
$$

等價，

可定義：

$$
\boxed{
[S_T]_{\mathcal O}
}
$$

為其 observational reconstruction equivalence class。

---

## 16.1 意義

若：

$$
S_T
\sim_{\mathcal O}
B_1
\sim_{\mathcal O}
B_2,
$$

則目前觀測不能區分這些內部解釋。

---

## 16.2 這是一個認識論限制

不能因：

$$
S_T
$$

有特殊術語，

就說：

$$
S_T
$$

必然使用特殊原理。

---

# 17. Behavioral Equivalence

定義：

$$
S_T
\equiv_B
B
$$

若對測試域：

$$
D,
$$

有：

$$
\forall x\in D,
\quad
Output(S_T,x)
=
Output(B,x).
$$

---

## 17.1 更強條件

還可比較：

- decisions；
- abstentions；
- errors；
- state transitions；
- convergence；
- failure classes。

---

# 18. Behavioral Tie 不等於 Mechanistic Identity

即使：

$$
S_T
\equiv_B
B,
$$

也不能推出：

$$
\boxed{
Mechanism(S_T)=Mechanism(B).
}
$$

只能說：

> 在目前觀測域中，行為不可區分。

---

# 19. Mechanistic Claim 需要額外證據

若理論主張：

> 我的內部機制本身是新的。

需要：

- formal reduction analysis；
- computational complexity analysis；
- representation lower bound；
- impossibility result；
- non-reducibility proof；
- or new empirical distinction。

---

# 20. Theory-Specific Delta

定義：

$$
\boxed{
\Delta_T
=
M(S_T)-M(B^{*}).
}
$$

---

## 20.1 多指標版本

若：

$$
\mathbf M
=
(M_1,\ldots,M_k),
$$

則：

$$
\boxed{
\boldsymbol{\Delta}_T
=
\mathbf M(S_T)
-
\mathbf M(B^{*}).
}
$$

---

## 20.2 避免單一 score 洗掉差異

例如：

- accuracy；
- unsafe accept；
- false reject；
- abstention；
- memory；
- runtime；
- sample efficiency。

應分開報告。

---

# 21. Hard-Gate Delta

若某指標是 hard gate，

不能與其他指標平均。

例如：

$$
UnsafeAccept>0
\Rightarrow
\text{Hard Fail}.
$$

即使：

$$
Accuracy=99.99\%.
$$

---

# 22. Description-Length Advantage

一個理論即使：

$$
\Delta_T=0,
$$

仍可能提供：

$$
\boxed{
\text{shorter specification}.
}
$$

---

## 22.1 定義

若：

$$
L(S_T)
<
L(B^{*}),
$$

其中：

$$
L
$$

是描述長度／規則數／配置負擔，

則理論可能有：

$$
\boxed{
\text{specification compression value}.
}
$$

---

# 23. Organizational Value

理論也可能把分散機制：

$$
p_1,\ldots,p_n
$$

統一成：

$$
T.
$$

即使：

$$
V_U=0,
$$

也可能：

$$
V_C>0,
$$

$$
V_F>0.
$$

---

# 24. Search Value

理論還可能讓研究者更快找到：

- useful invariants；
- important failure modes；
- meaningful abstractions；
- promising benchmarks。

這是一種：

$$
\boxed{
\text{search heuristic value}.
}
$$

---

# 25. Theory as Coordinate System

某些理論不是新 primitive，

而可能是：

$$
\boxed{
\text{a useful coordinate system over known machinery}.
}
$$

---

## 25.1 座標系也有價值

不同座標表示同一現象，

但可能讓某些問題：

- 更簡潔；
- 更容易推導；
- 更容易實作；
- 更容易教學。

因此：

$$
\boxed{
\text{not fundamental}
\neq
\text{not valuable}.
}
$$

---

# 26. Weak Baseline Fallacy

若研究者只比較：

$$
S_T
$$

和：

$$
B_{\mathrm{naive}},
$$

並宣稱：

$$
\Delta_T>0,
$$

稱為：

**Weak Baseline Fallacy**

---

## 26.1 典型例子

Theory system 有：

- typed identity；
- versioning；
- provenance；
- error checking。

Baseline 只有：

- string matching。

這只能證明：

> typed + versioned + provenance > string matching.

不能證明：

> theory-specific primitive exists.

---

# 27. Feature Smuggling

如果：

$$
S_T
$$

額外得到：

$$
f^{*},
$$

而 baseline 沒有，

則：

$$
M(S_T)>M(B)
$$

可能只是：

$$
\boxed{
\text{feature advantage}.
}
$$

---

# 28. Rule Smuggling

有時測試者會說：

> Baseline 沒有這個規則。

但該規則本身完全可以用 generic constraint 表示。

如果故意禁止 baseline 使用，

就是：

$$
\boxed{
\text{Rule Smuggling}.
}
$$

---

# 29. Naming Fallacy

如果同一規則：

Theory：

> ordinal invariant。

Baseline：

> consistency constraint。

名稱不同不代表機制不同。

因此：

$$
\boxed{
\text{Name Difference}
\not\Rightarrow
\text{Mechanism Difference}.
}
$$

---

# 30. Architecture Packaging Fallacy

若理論把：

$$
A+B+C
$$

包成：

$$
T,
$$

而 baseline 分別實作：

$$
A,B,C,
$$

不能因 packaging 不同就說：

$$
T
$$

具有新的 primitive。

---

# 31. Matched Reconstruction Ladder

PTE 建議 baseline 逐層升級：

```text
B0 naive
B1 retrieval
B2 typed
B3 relation-aware
B4 provenance-aware
B5 dynamic/versioned
B6 event-sourced
B7 full conventional
```

---

## 31.1 每一階都問

$$
\Delta_T^{(k)}
=
M(S_T)-M(B_k).
$$

---

## 31.2 若

$$
\Delta_T^{(0)}
>
\Delta_T^{(1)}
>
\cdots
>
\Delta_T^{(7)}
=
0,
$$

表示：

> 初期優勢逐步被一般機制吸收。

---

# 32. Reconstruction Curve

定義：

$$
\boxed{
R_C(k)
=
M(B_k).
}
$$

隨 baseline sophistication：

$$
k
$$

提升，

觀察：

$$
R_C(k)
$$

如何接近：

$$
M(S_T).
$$

---

## 32.1 三種曲線

### A. 快速收斂

很早：

$$
R_C(k)\approx M(S_T).
$$

可能表示 theory gain 很容易被吸收。

---

### B. 緩慢收斂

需要大量一般機制才接近。

理論可能具有重要：

$$
\text{compression / organization value}.
$$

---

### C. 不收斂

若：

$$
\forall k,
\quad
R_C(k)<M(S_T),
$$

則出現真正值得研究的 residual gap。

---

# 33. Reconstruction Burden

即使 baseline 最終可以等價，

也可能需要巨大複雜度。

定義：

$$
\boxed{
B_R(T)
=
C(B^{*})-C(S_T),
}
$$

其中：

$$
C
$$

可以是：

- rule count；
- description length；
- memory；
- runtime；
- engineering complexity。

---

## 33.1 若

$$
\Delta_T=0,
$$

但：

$$
B_R(T)\gg0,
$$

則理論仍可能有：

$$
\boxed{
\text{compression advantage}.
}
$$

---

# 34. 不能只看能不能重建，也要看代價

因此真正比較應是：

$$
\boxed{
(
M,
C,
L,
R
)
}
$$

其中：

- $M$：performance；
- $C$：complexity；
- $L$：description / implementation length；
- $R$：resource cost。

---

# 35. Sample Efficiency

若理論系統用：

$$
n_T
$$

個樣本達到：

$$
q,
$$

而 baseline 需要：

$$
n_B
$$

個樣本，

可定義：

$$
\boxed{
SE_G
=
\frac{n_B}{n_T}.
}
$$

若：

$$
SE_G>1,
$$

可能存在樣本效率優勢。

---

# 36. Generalization Gap

若訓練域：

$$
D_{\mathrm{train}}
$$

和測試域：

$$
D_{\mathrm{test}}
$$

不同，

比較：

$$
G_T
=
M_T(D_{\mathrm{test}})
-
M_T(D_{\mathrm{train}}).
$$

並與：

$$
G_B
$$

比較。

---

# 37. Noise Robustness

也應測：

$$
\epsilon
$$

噪聲增長時，

兩套系統的性能函數：

$$
M_T(\epsilon),
$$

$$
M_B(\epsilon).
$$

若只有 clean toy data tie，

還不能說完全等價。

---

# 38. Temporal Robustness

動態系統需測：

- update order；
- delayed evidence；
- retraction；
- conflicting evidence；
- duplicate events；
- replay。

---

## 38.1 若兩邊

$$
\forall h\in\mathcal H,
\quad
State_T(h)
=
State_B(h),
$$

才建立較強 temporal behavioral equivalence。

---

# 39. External Data

合成資料容易：

$$
\text{encode the evaluator's assumptions}.
$$

因此 matched reconstruction 應進：

$$
D_{\mathrm{external}}.
$$

---

## 39.1 External tie 更有資訊量

如果外部資料揭露新的 failure mode，

而兩邊修復後仍 tie，

其資訊量高於一開始就設計好的 toy tie。

---

# 40. Gold Firewall

對 supervised benchmark，

gold：

$$
y^{*}
$$

只能進 scorer。

要求：

$$
\boxed{
Decision(x)
\perp
y^{*}
}
$$

在 decision time。

---

## 40.1 Mutation Test

把：

$$
y^{*}
$$

改成：

$$
\tilde y,
$$

若 decision 改變，

表示：

$$
\text{gold leakage}.
$$

---

# 41. Frozen Proposal Principle

為避免 generator 差異污染 validator 比較，

可先 frozen：

$$
P(x).
$$

然後：

$$
Validator_T(P(x)),
$$

$$
Validator_B(P(x)).
$$

比較純 validation difference。

---

# 42. Component Ablation

若理論系統含：

$$
\{a,b,c,d\},
$$

應逐一移除：

$$
S_T^{-a},
S_T^{-b},
S_T^{-c},
S_T^{-d}.
$$

觀察：

$$
\Delta M.
$$

---

## 42.1 若移除 theory-specific component 不影響

則：

$$
\boxed{
\text{claimed component is not causally necessary under the test}.
}
$$

---

# 43. Causal Necessity Test

設 theory-specific primitive：

$$
p_T.
$$

若：

$$
S_T-p_T
$$

仍：

$$
M(S_T-p_T)
=
M(S_T),
$$

則目前沒有證據支持：

$$
p_T
$$

造成性能。

---

# 44. Causal Sufficiency 也不同

若單獨加入：

$$
p_T
$$

到弱 baseline：

$$
B_0+p_T,
$$

得到提升，

仍不代表：

$$
p_T
$$

不可被其他機制替代。

---

# 45. Replacement Test

尋找：

$$
q
\neq
p_T
$$

使：

$$
M(B_0+q)
=
M(B_0+p_T).
$$

若存在，

則：

$$
p_T
$$

不是目前觀測下唯一解釋。

---

# 46. Minimal Distinguishing Experiment

理論比較最終應尋找：

$$
\boxed{
x^{*}
}
$$

使：

$$
Output(S_T,x^{*})
\neq
Output(B^{*},x^{*}).
$$

---

## 46.1 如果找不到

則目前：

$$
S_T
\sim_{\mathcal O}
B^{*}.
$$

---

# 47. Distinguishing Surface

定義：

$$
\boxed{
D_{\Delta}
=
\{
x:
Output(S_T,x)
\neq
Output(B^{*},x)
\}.
}
$$

如果：

$$
D_{\Delta}=\varnothing,
$$

在當前測試域中沒有可區分行為。

---

# 48. Theory-Specific Residual Gain

若：

$$
D_{\Delta}\neq\varnothing,
$$

定義：

$$
\boxed{
R_G(T)
=
M_{D_{\Delta}}(S_T)
-
M_{D_{\Delta}}(B^{*}).
}
$$

---

## 48.1 這才是應該優先研究的地方

不是全域重複跑更多 tie case，

而是集中：

$$
D_{\Delta}.
$$

---

# 49. Baseline as Adversary, Not Enemy

Strong baseline 的角色不是：

> 打倒理論。

而是：

> 幫助理論把真正不可約的部分暴露出來。

---

## 49.1 因此

$$
\boxed{
\text{Strong baseline}
=
\text{epistemic compression tool}.
}
$$

它把可由 known machinery 解釋的部分壓掉。

---

# 50. Useful Tie

本文正式定義：

**定義 50.1（Useful Tie）**

若：

$$
M(S_T)
=
M(B^{*}),
$$

但：

$$
M(S_T)
>
M(B_{\mathrm{naive}}),
$$

且 $T$ 提供明顯：

- conceptual compression；
- architecture guidance；
- specification clarity；
- discovery heuristic；

則稱：

$$
\boxed{
\text{Useful Tie}.
}
$$

---

# 51. Useful Tie 的認識論地位

它支持：

$$
V_C>0,
$$

$$
V_F>0,
$$

$$
V_E>0,
$$

但不直接支持：

$$
V_U>0.
$$

---

# 52. Theory Win

如果：

$$
\Delta_T>0,
$$

且通過：

- matched info；
- matched data；
- matched resources；
- independent path；
- external data；
- ablation；
- gold firewall；

則稱：

$$
\boxed{
\text{Residual Win}.
}
$$

---

## 52.1 仍需追問

> 差異由哪個最小 primitive 造成？

---

# 53. Residual Win 到 New Primitive 還有多遠？

至少需要：

$$
\text{Residual Win}
\rightarrow
\text{Cross-Domain Replication}
\rightarrow
\text{Mechanistic Isolation}
\rightarrow
\text{Non-Reducibility Evidence}.
$$

---

# 54. Non-Reducibility Evidence

可能形式包括：

- complexity separation；
- lower bound；
- impossibility theorem；
- representation theorem；
- formal independence；
- empirical impossibility across baseline class。

---

# 55. Empirical Non-Reducibility 不是數學不可約

若：

$$
\mathcal B_{\mathrm{tested}}
$$

中的 baseline 都輸，

只能說：

$$
\boxed{
\text{not reconstructed by tested baselines}.
}
$$

不是：

$$
\boxed{
\text{mathematically irreducible}.
}
$$

---

# 56. Baseline Family Must Be Explicit

每篇 PTE 報告應列：

```text
baseline_id
baseline_family
observables
data access
resource access
decision rules
theory-specific dependencies
independence status
performance
complexity
```

---

# 57. Baseline Debt

若研究因時間不足沒有建立 strong baseline，

應標記：

$$
\boxed{
\text{Baseline Debt}.
}
$$

---

## 57.1 不可隱藏

沒有 strong baseline 時，

結論上限應是：

$$
\boxed{
\text{usefulness demonstrated, uniqueness not tested}.
}
$$

---

# 58. Strong Baseline 的成本也是研究成本

PTE-02 已指出：

$$
L_B
$$

可能成為 theory testing 的重要延遲。

因為最難的常常不是：

> 把新理論做出來。

而是：

> 把已知方法也做到真正公平。

---

# 59. Auto-Baseline Generation

未來 AI 可以自動：

1. 抽取 theory features；
2. 尋找 known mechanisms；
3. 組合 strongest baseline；
4. 檢查資訊匹配；
5. 執行 differential test。

---

# 60. 但 baseline 生成也可能偏誤

如果 AI 已經接受：

$$
T
$$

的術語，

可能不知不覺把：

$$
B
$$

寫成：

$$
T
$$

的同義版本。

因此需要：

$$
\boxed{
\text{Baseline Reconstruction Isolation}.
}
$$

---

# 61. Blind Reconstruction

一種更強設計：

讓 baseline builder 只知道：

- task；
- observables；
- data；
- success criteria；

但不知道：

$$
T
$$

的專屬術語。

---

## 61.1 如果仍能重建

則：

$$
\boxed{
\text{evidence for conventional reconstructibility}\uparrow.
}
$$

---

# 62. Reverse Engineering Test

給 baseline builder：

$$
\text{Input/Output behavior}
$$

但不給 theory labels，

要求重建相同功能。

如果成功，

表示：

> 功能可能不依賴理論專屬概念。

---

# 63. Reconstruction Challenge

可把它標準化成：

```text
Given:
  task contract
  observables
  examples
  resource constraints

Forbidden:
  theory-specific vocabulary
  theory implementation code

Goal:
  match or exceed theory-system behavior
```

---

# 64. Theory Compression vs Theory Necessity

若理論可以讓：

$$
100
$$

條 generic rule，

壓成：

$$
5
$$

條高階 invariant，

即使：

$$
\Delta_T=0,
$$

仍可能具有很高：

$$
\boxed{
\text{compression value}.
}
$$

---

## 64.1 因此要分開

$$
\boxed{
\text{Necessity}
\neq
\text{Compression}.
}
$$

---

# 65. Engineering Elegance 也是價值，但不是證明

可以評估：

- rule count；
- maintainability；
- extensibility；
- debugging cost；
- explainability。

但要明確標為：

$$
\text{engineering metrics}.
$$

---

# 66. Theoretical Novelty Ledger

對每個 claim：

```text
claim_id
claimed novelty
known analogues
matched baseline
residual behavior
mechanistic evidence
formal non-reducibility
status
```

---

# 67. Status Vocabulary

建議：

```text
USEFUL
SUPERIOR_UNDER_TEST
RECONSTRUCTIBLE
USEFUL_TIE
RESIDUAL_WIN
MECHANISM_UNRESOLVED
UNIQUENESS_NOT_ESTABLISHED
IRREDUCIBILITY_NOT_ESTABLISHED
FORMAL_SEPARATION_ESTABLISHED
```

---

# 68. 禁止使用的過度結論

若只有：

$$
\Delta_T=0,
$$

禁止說：

> 理論被證明是假的。

---

若只有：

$$
\Delta_T>0,
$$

禁止說：

> 理論被證明是新的宇宙原理。

---

# 69. 最終判定矩陣

| 工程有效 | Strong baseline | 結果 | 合理結論 |
|---|---|---|---|
| 否 | 不重要 | 失敗 | 工程主張未建立 |
| 是 | 弱 | 勝 | usefulness 初步成立 |
| 是 | 強 | tie | useful / reconstructible |
| 是 | 強 | 勝 | residual advantage |
| 是 | 多強 baseline | 持續勝 | uniqueness evidence 增加 |
| 是 | formal non-reducibility | 勝 | 才接近 new primitive claim |

---

# 70. PTE-03 的核心公式

第一個：

$$
\boxed{
\Delta_T
=
M(S_T)-M(B^{*}(T)).
}
$$

第二個：

$$
\boxed{
\Delta_T=0
\not\Rightarrow
V(T)=0.
}
$$

第三個：

$$
\boxed{
\Delta_T>0
\not\Rightarrow
V_U(T)>0.
}
$$

第四個：

$$
\boxed{
\text{Useful architecture}
\neq
\text{new primitive}.
}
$$

---

# 71. 與 PTE-01 的關係

PTE-01 問：

> 怎麼把理論最強版本做出來？

PTE-03 問：

> 做出來之後，怎麼知道它真的需要自己的理論？

---

# 72. 與 PTE-02 的關係

PTE-02 說：

$$
L_{TE}\downarrow.
$$

這意味著 strong baseline 的建立成本也可能下降。

所以未來：

> 「時間不夠，沒辦法做公平 baseline。」

會越來越不容易成為合理理由。

---

# 73. 與 PTE-04 的關係

當：

$$
\Delta_T=0,
$$

但：

$$
V_C,V_F,V_E>0,
$$

就進入下一篇的問題：

> 如果宏大主張沒有留下不可約增益，那麼理論裡真正值得保存的是什麼？

---

# 74. 初步可檢驗命題

## MRP-H1：Baseline Convergence Hypothesis

對大量只重新組織已知機制的理論，

隨 baseline sophistication 提升：

$$
\Delta_T^{(k)}
\rightarrow
0.
$$

---

## MRP-H2：Compression-without-Uniqueness Hypothesis

存在理論：

$$
T
$$

使：

$$
\Delta_T=0,
$$

但：

$$
C(S_T)
<
C(B^{*}),
$$

即具有壓縮價值但沒有測得的獨特行為。

---

## MRP-H3：Blind Reconstruction Hypothesis

若 theory gain 主要來自一般 invariants，

則只給 task / observables 的 blind baseline builder，

仍能重建大部分效果。

---

## MRP-H4：Weak-Baseline Inflation Hypothesis

若只使用弱 baseline，

則估計：

$$
\widehat{\Delta}_T
$$

會系統性高估 theory-specific gain。

---

## MRP-H5：External Differential Hypothesis

真正有不可約差異的理論，

在外部、亂序、噪聲、跨域或 adversarial test 中，

更可能形成穩定：

$$
D_{\Delta}\neq\varnothing.
$$

---

# 75. 最小 MRP 實驗流程

```text
1. Freeze theory claim
2. Freeze observables
3. Freeze task contract
4. Freeze metric
5. Build theory-derived system
6. Build naive baseline
7. Build stronger conventional baselines
8. Verify independent causal paths
9. Match data and candidate space
10. Run ablations
11. Run external/adversarial tests
12. Compute delta vector
13. Measure reconstruction burden
14. Search distinguishing surface
15. Report residual gain
```

---

# 76. 最小 Evidence Receipt

```text
theory_id
claim_id
theory_system_version
baseline_family
matched_information
matched_data
matched_candidates
matched_resources
independence_test
metric
result_vector
delta_vector
reconstruction_curve
reconstruction_burden
distinguishing_surface
status
```

---

# 77. 方法論結論

理論評估中最危險的兩種錯誤是：

第一種：

> 「它做出好東西，所以它一定揭示了新原理。」

第二種：

> 「它能被既有方法重建，所以它完全沒有價值。」

PTE-03 同時拒絕兩者。

真正應該說的是：

$$
\boxed{
\text{Usefulness}
\quad
\text{and}
\quad
\text{irreducibility}
}
$$

是兩個不同問題。

---

# 78. 最終核心命題

如果：

$$
S_T
$$

能讓工程變好，

它已經具有價值。

但只有當：

$$
\boxed{
M(S_T)
>
M(B^{*}(T))
}
$$

在公平、獨立、外部與可重播條件下穩定成立，

我們才開始有資格問：

> **那個剩下的差異，是否真的來自一個還不能被既有方法吸收的新結構？**

而即使答案最後是：

$$
\Delta_T=0,
$$

研究也沒有白做。

因為我們至少知道：

$$
\boxed{
\text{這個理論的工程效果可以被重建。}
}
$$

接下來應保留：

- 概念壓縮；
- 工程 heuristic；
- 規格價值；
- 組織價值；

並把「不可約新原理」從已建立主張中拿掉。

這不是把理論打成零。

而是把：

$$
\boxed{
\text{真正的價值}
}
$$

與：

$$
\boxed{
\text{尚未被證明的宏大性}
}
$$

分開。

---

# 79. 下一篇

**PTE-04｜認識論回收：從過度宣稱中分離可用理論殘差**  
*Epistemic Salvage: Recovering Useful Structure from Overstated Theories*

下一篇將正式處理：

$$
V(T)
=
(
V_C,V_F,V_E,V_P,V_U
),
$$

以及：

$$
R_{\mathcal B,\mathcal E}(T),
$$

回答：

> **當一套理論沒有成功證明自己是新的不可約原理，但又確實產生了有用結構時，我們應該如何保存、拆分、降級與重新定位它，而不是把它整體判成「對」或「錯」？**
