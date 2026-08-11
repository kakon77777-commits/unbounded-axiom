# MCDM v0.2：數學猜想的量詞—證明不對稱與研究路由矩陣

**MCDM v0.2: A Quantifier–Proof-Asymmetry and Research-Routing Matrix for Mathematical Conjectures**

作者：Neo.K  
系列：全域量詞—證明張力—研究路由系列 IV  
版本：v0.2  
前版：MCDM v0.1（2026-07-24）  
日期：2026-08-10  
文件性質：理論論文／AI 數學研究基礎設施／猜想資料庫規格

---

## 摘要

既有「數學猜想難度矩陣」（Mathematical Conjecture Difficulty Matrix, MCDM）v0.1 提出：

$$
\boxed{
\mathfrak D(C)
=
(B,I,E,F,V,R,G,U)
}
$$

作為數學猜想的基本障礙向量，分別描述背景負載、核心洞見障礙、執行負載、形式化成熟度、可驗證性、研究阻力、全域耦合度與判定域不確定性。原框架並加入人類摘要難度 $L_0-L_9$ 、AI 可攀爬性 $A_0-A_5$ 與研究進展累積性 $P_0-P_5$ ，明確反對將所有數學難度壓縮成單一固定分數。

然而，MCDM v0.1 尚未顯式描述一種重要困難：**同一猜想在正向證成與反向證偽時，可能具有完全不同的量詞結構、證書形式、搜索空間與全域控制要求。**

例如：

$$
C:
\forall xP(x)
$$

與其否定：

$$
\neg C:
\exists x\neg P(x)
$$

分別要求全域控制與單點反例；但：

$$
C:
\exists A\forall xP(A,x)
$$

的否定卻是：

$$
\neg C:
\forall A\exists x\neg P(A,x),
$$

此時一個 point counterexample 已經不足，而可能需要 adversarial family、counterstrategy 或 universal obstruction。

本文因此提出 MCDM v0.2。新版保留原：

$$
\boxed{
\mathfrak D_0(C)
=
(B,I,E,F,V,R,G,U)
}
$$

作為向後相容的核心難度層，不直接增加更多普通障礙維度；而在其上新增：

$$
\boxed{
\mathfrak Q(C)
}
$$

——量詞—證明剖面；

以及：

$$
\boxed{
\mathfrak R(C\mid S,t)
}
$$

——solver-relative research routing layer。

完整架構為：

$$
\boxed{
\mathrm{MCDM}_{0.2}
=
[
\mathfrak D_0,
\mathfrak Q,
\mathfrak R
].
}
$$

其中 $\mathfrak Q$ 記錄：

- 正／反量詞簽名；
- 量詞交替與依賴；
- 原始與有效全域量詞負擔；
- 全域量詞壓縮器；
- global witness uniformity；
- quantifier-swap risk；
- proof/refutation tension；
- quantifier closure 與 coverage。

 $\mathfrak R$ 則根據：

$$
T^+,\;T^-,
\qquad
A^+,\;A^-,
\qquad
P^+,\;P^-,
\qquad
V^+,\;V^-
$$

建立研究路由。

因此 MCDM v0.2 不再只回答：

> 一個猜想有多難？

而進一步回答：

$$
\boxed{
\begin{aligned}
&\text{它在哪一個量詞位置真正被卡住？}\\
&\text{證成和證偽哪一邊比較可攻擊？}\\
&\text{目前缺少的是 witness、strategy、invariant 還是 obstruction？}\\
&\text{哪一種人類／AI solver 最適合攻擊哪一條路？}\\
&\text{算力、形式化與研究時間應投入哪裡？}
\end{aligned}
}
$$

本文最終將 MCDM 從猜想難度描述框架升級為：

$$
\boxed{
\text{Mathematical Research Routing Infrastructure}.
}
$$

---

# 1. MCDM v0.1 的原始問題意識

MCDM v0.1 的核心主張是：

$$
\boxed{
\text{數學猜想的難度不是單一分數，而是一個障礙向量。}
}
$$

原版認為，長期未解猜想與一般封閉數學題的困難本質不同。它們可能面臨：

- 解決方向未知；
- 理論框架不足；
- 局部進展不能閉合；
- 候選證明難以驗證；
- 公理域甚至可能不確定。

因此原版提出：

$$
\boxed{
\mathfrak D_0(C)
=
(B,I,E,F,V,R,G,U).
}
$$



---

# 2. 原八維度保持不變

MCDM v0.2 不廢除原八維。

原因很簡單：

本系列新增的是：

$$
\boxed{
\text{proof architecture}
}
$$

而不是發現：

$$
B,I,E,F,V,R,G,U
$$

本身錯誤。

因此：

$$
\boxed{
\mathrm{MCDM}_{0.1}
\subset
\mathrm{MCDM}_{0.2}
}
$$

在資料結構與概念相容意義上成立。

---

# 3. 原版最接近此次發現的是 $G$

原 MCDM 定義：

$$
G
=
\text{Global Coupling}.
$$

 $G_0$ 表示可完全分解，

而最高：

$$
G_6
$$

表示：

> 可能只有整體新框架才能閉合。



這已經抓到：

$$
\boxed{
\text{局部成果未必能合成全域成果。}
}
$$

但是 $G$ 沒有回答：

> 那個「全域」到底是哪一個量詞？

---

# 4. 全域耦合與全域量詞不是同一件事

例如兩個命題：

$$
C_1:
\forall xP(x),
$$

$$
C_2:
\forall x\exists y\forall zQ(x,y,z).
$$

兩者都可能：

$$
G=6.
$$

但其證明結構完全不同。

 $C_1$ 只需某種：

$$
\forall x
$$

控制。

 $C_2$ 則可能需要：

$$
x
\mapsto
y_x
$$

的 strategy，

而：

$$
y_x
$$

又必須對全部：

$$
z
$$

有效。

所以：

$$
\boxed{
G
=
\text{耦合程度}
}
$$

而：

$$
\boxed{
\mathfrak Q
=
\text{耦合背後的邏輯骨架}.
}
$$

---

# 5. 原版 $U$ 也已經留下接口

MCDM v0.1 的：

$$
U
=
\text{Decidability Uncertainty}
$$

並不是單純表示「目前沒解」。

它從：

$$
U_0
$$

「普通證明或反例即可解決」，

一路到：

$$
U_6
$$

「已證明相對指定公理系統獨立」。



所以原框架已經承認：

$$
\boxed{
\text{不同猜想可能需要不同 resolution mode}.
}
$$

但沒有正式解釋：

> 為什麼某些猜想適合 proof，而某些適合 disproof？

---

# 6. v0.1 其實已經預留 resolution modes

原猜想卡已包含：

```yaml
candidate_resolution_modes:
  - proof
  - disproof
  - finite_counterexample
  - conditional_theorem
  - method_relative_impossibility
  - independence_result
  - reformulation
  - decomposition
```



v0.2 的任務不是增加更多名稱。

而是回答：

$$
\boxed{
\text{如何根據命題本身，自動判斷這些 route 的結構成本？}
}
$$

---

# 7. 三篇前置論文帶來的新結構

本系列前三篇依次提出：

### I. Global Quantifier Compression

$$
\forall
$$

不能由任意巨大有限測試直接替代。

需要：

$$
\boxed{
\mathrm{GQCM}
}
$$

——Global Quantifier Compression Mechanism。

---

### II. Proof–Refutation Quantifier Asymmetry

同一猜想：

$$
C
$$

應分別分析：

$$
\mathcal Q^+(C)
$$

與：

$$
\mathcal Q^-(C).
$$

並區分：

$$
T^+(C),
\qquad
T^-(C).
$$

---

### III. Quantifier Uniformity

P/NP 分析進一步揭露：

$$
\forall x\exists W_x
\centernot\Rightarrow
\exists W\forall x.
$$

這導出：

$$
\boxed{
\text{Global Witness Uniformity}
}
$$

與：

$$
\boxed{
\text{Quantifier Swap Error}.
}
$$

這三項現在整合進 MCDM。

---

# 8. MCDM v0.2 的三層架構

正式定義：

$$
\boxed{
\mathrm{MCDM}_{0.2}
(C\mid S,t)
=
\left[
\mathfrak D_0(C),
\mathfrak Q(C),
\mathfrak R(C\mid S,t)
\right].
}
$$

其中：

$$
\mathfrak D_0
$$

回答：

> 猜想被什麼一般障礙阻擋？

$$
\mathfrak Q
$$

回答：

> 正證／證偽的邏輯張力是什麼？

$$
\mathfrak R
$$

回答：

> 對目前 solver 而言，應該怎麼研究？

---

# 9. Layer 1：Core Difficulty

保持：

$$
\boxed{
\mathfrak D_0(C)
=
(B,I,E,F,V,R,G,U).
}
$$

這一層保持 v0.1 backward compatibility。

舊資料庫不必重做。

只要：

$$
\boxed{
\text{append new layers}.
}
$$

---

# 10. Layer 2：Quantifier–Proof Profile

定義：

$$
\boxed{
\mathfrak Q(C)
=
(
Q^+,
Q^-,
A_Q,
D_Q,
Q_{\mathrm{eff}}^+,
Q_{\mathrm{eff}}^-,
K^+,
K^-,
W^+,
W^-,
J,
T^+,
T^-,
\Delta T,
QCC,
QCov
).
}
$$

以下逐一定義。

---

# 11. 正向量詞簽名 $Q^+$

令猜想在選定 representation：

$$
R_C
$$

下寫成 prenex-like structure：

$$
Q_1x_1
Q_2x_2
\cdots
Q_nx_nP.
$$

定義：

$$
\boxed{
Q^+(C)
=
(Q_1,\ldots,Q_n).
}
$$

---

# 12. 反向量詞簽名 $Q^-$

定義：

$$
\boxed{
Q^-(C)
=
Q^+(\neg C).
}
$$

例如：

$$
Q^+
=
(\forall,\exists,\forall)
$$

則：

$$
Q^-
=
(\exists,\forall,\exists).
$$

因此猜想卡第一次直接保存：

$$
\boxed{
\text{truth-direction asymmetry}.
}
$$

---

# 13. 不保存唯一量詞形式

同一猜想可能有：

$$
R_1,
R_2,\ldots,R_k
$$

等價表示。

所以資料庫應存：

$$
\boxed{
Q(C\mid R_i).
}
$$

而非宣稱：

$$
Q(C)
$$

永遠唯一。

這非常重要。

因為一個好的 reformulation 本身就可能：

$$
\boxed{
\text{降低有效量詞負擔}.
}
$$

---

# 14. 量詞交替 $A_Q$

定義：

$$
\boxed{
A_Q
=
\#\{
i:
Q_i\neq Q_{i+1}
\}.
}
$$

但 v0.2 明確禁止：

$$
\boxed{
A_Q
=
\text{數學難度}.
}
$$

它只是一項 proof-architecture descriptor。

---

# 15. 量詞依賴複雜度 $D_Q$

比交替更重要的是依賴。

例如：

$$
\forall x
\exists y
\forall z
\exists w.
$$

可能需要：

$$
y=f(x),
$$

$$
w=g(x,z).
$$

因此建立：

$$
\boxed{
\mathcal G_Q(C)
}
$$

——Quantifier Dependency Graph。

並由此得到：

$$
D_Q.
$$

---

# 16. 原始與有效量詞負擔

定義：

$$
Q_{\mathrm{raw}}
$$

為原始表示中的量詞負擔。

而：

$$
\boxed{
Q_{\mathrm{eff}}
(
C
\mid
\mathcal K_t
)
}
$$

表示使用當前：

- reductions；
- symmetries；
- classification；
- equivalence；
- completeness；
- invariants；

後仍未被壓縮的量詞結構。

所以真正研究的是：

$$
\boxed{
Q_{\mathrm{eff}},
}
$$

而不是單純數：

$$
\forall
$$

出現幾次。

---

# 17. 正向與反向 $Q_{\mathrm{eff}}$

正式分成：

$$
\boxed{
Q_{\mathrm{eff}}^+
}
$$

與：

$$
\boxed{
Q_{\mathrm{eff}}^-.
}
$$

因為同一 theorem 可能大幅降低：

$$
T^+
$$

卻完全不降低：

$$
T^-.
$$

---

# 18. 全域量詞壓縮器 $K^+$

定義：

$$
K^+
$$

為目前可用的正向 Global Quantifier Compression Mechanisms。

可能包括：

$$
\boxed{
\begin{aligned}
&\text{induction},\\
&\text{well-founded order},\\
&\text{global invariant},\\
&\text{monotone quantity},\\
&\text{classification},\\
&\text{complete representative},\\
&\text{finite obstruction},\\
&\text{global flow},\\
&\text{domain lift}.
\end{aligned}
}
$$

---

# 19. 反向壓縮器 $K^-$

負向則可能包括：

$$
\boxed{
\begin{aligned}
&\text{point counterexample},\\
&\text{counterexample family},\\
&\text{adversarial operator},\\
&\text{counterstrategy},\\
&\text{diagonal obstruction},\\
&\text{lower-bound invariant},\\
&\text{impossibility theorem}.
\end{aligned}
}
$$

所以：

$$
\boxed{
K^+
\neq
K^-.
}
$$

---

# 20. Compressor Gap

定義：

$$
\boxed{
K_{\mathrm{gap}}^\pm
}
$$

表示：

> 從目前最強局部控制，到足以閉合該方向全部有效量詞，還缺多遠？

建議暫用：

$$
K_0-K_5.
$$

### $K_0$

已有完整壓縮器。

### $K_1$

只缺小型技術閉合。

### $K_2$

已有大範圍控制。

### $K_3$

只有局部或 restricted-domain 壓縮。

### $K_4$

只有候選方向。

### $K_5$

目前甚至不知道應尋找哪種全域結構。

---

# 21. Witness Type $W^\pm$

量詞結構決定候選證書的型態。

因此記錄：

$$
\boxed{
W^\pm
\in
\{
\text{point},
\text{finite-family},
\text{parametric},
\text{function},
\text{strategy},
\text{higher-order strategy}
\}.
}
$$

這讓研究系統知道：

> 到底應搜尋一個數字、一個函數，還是一個策略？

---

# 22. Global Witness Uniformity

設目標需要：

$$
\exists W\forall x.
$$

若目前只有：

$$
\forall x\exists W_x,
$$

則定義：

$$
\boxed{
J_{\mathrm{uniform}}>0.
}
$$

表示存在 witness uniformity gap。

這在 complexity、algorithm synthesis 與 constructive mathematics 中尤其重要。

---

# 23. Quantifier Swap Risk

定義：

$$
\boxed{
J_{\mathrm{swap}}
}
$$

描述目前研究路線是否存在：

$$
\forall x\exists W_x
\quad\rightsquigarrow\quad
\exists W\forall x
$$

這類非法量詞交換風險。

可以分：

$$
J_0-J_4.
$$

### $J_0$

形式化已保證無交換。

### $J_1$

自然語言可能歧義，但結構清楚。

### $J_2$

部分推導依賴 uniformity 尚未證明。

### $J_3$

主要結論可能依賴量詞交換。

### $J_4$

當前候選證明核心就是非法交換。

---

# 24. 這一項特別適合 AI proof audit

AI 很容易產生自然語言：

> 對任意 $x$ ，我們都能選一個合適的 $y$ ，因此存在一個統一方案。

但：

$$
\forall x\exists y
$$

不自動意味着：

$$
\exists y\forall x.
$$

即使真正需要的是：

$$
\exists f\forall x,
$$

也必須證明：

$$
f
$$

存在且具有正確依賴。

因此：

$$
\boxed{
J_{\mathrm{swap}}
}
$$

很適合作為 machine proof critic 的專門檢查項。

---

# 25. 正證張力 $T^+$

定義：

$$
\boxed{
T^+
=
\mathcal T^+
(
Q_{\mathrm{eff}}^+,
A_Q,
D_Q,
K_{\mathrm{gap}}^+,
J,
I,E,G,V
).
}
$$

本文暫時**不**將 $\mathcal T$ 固定成線性加權公式。

因為：

$$
\boxed{
\text{不同維度可能具有非線性瓶頸關係}.
}
$$

---

# 26. 證偽張力 $T^-$

同理：

$$
\boxed{
T^-
=
\mathcal T^-
(
Q_{\mathrm{eff}}^-,
A_Q,
D_Q,
K_{\mathrm{gap}}^-,
J,
I,E,G,V
).
}
$$

---

# 27. Proof–Refutation Asymmetry

定義：

$$
\boxed{
\Delta T
=
T^+-T^-.
}
$$

但實務上建議不用單一精確數字。

而是使用：

$$
\boxed{
\Delta T
\in
\{
+++,++,+,0,-,--,---
\}.
}
$$

或 confidence interval。

避免虛假精密。

---

# 28. 為什麼不能只看 $\Delta T$ ？

因為：

$$
T^-=3,
\qquad
T^+=5
$$

與：

$$
T^-=8,
\qquad
T^+=10
$$

都有：

$$
\Delta T=2,
$$

但完全不是同一情況。

所以必須同時保存：

$$
\boxed{
(T^+,T^-,\Delta T).
}
$$

---

# 29. Quantifier Closure Criterion

由第三篇引入：

$$
\boxed{
QCC.
}
$$

若 candidate proof：

$$
\Pi
$$

真的覆蓋目標 theorem 的所有必要量詞，

則：

$$
\boxed{
QCC(\Pi,C)=1.
}
$$

否則：

$$
QCC<1.
$$

---

# 30. QCC 不是正確性驗證

必須區分：

$$
\boxed{
QCC=1
}
$$

與：

$$
\boxed{
\Pi\text{ is correct}.
}
$$

 $QCC=1$ 只表示：

> 這條論證至少「有資格」覆蓋完整命題。

它仍可能：

- 有推導錯誤；
- 引理錯誤；
- 隱藏 oracle；
- 公理使用錯誤；
- formalization mismatch。

所以：

$$
\boxed{
QCC
\neq
Proof Verification.
}
$$

---

# 31. Quantifier Coverage

對未完成研究：

$$
\Pi_t
$$

定義：

$$
\boxed{
QCov(\Pi_t,C)
}
$$

描述已經閉合多少量詞域。

例如：

$$
\forall x\in D
$$

目前只證：

$$
\forall x\in D'
$$

其中：

$$
D'\subsetneq D.
$$

那：

$$
QCov<1.
$$

---

# 32. QCov 可以比「測試到多少」更有意義

例如：

$$
10^{15}
$$

個點全部成功，

但只是有限枚舉：

$$
QCov_{\mathrm{structural}}
$$

可能仍接近零。

反之，一個 theorem 控制：

$$
D'
$$

整個 infinite subclass，

即使從未枚舉很多案例，

其：

$$
QCov
$$

可能大幅增加。

所以：

$$
\boxed{
\text{Structural Coverage}
>
\text{Raw Sample Count}
}
$$

在猜想閉合進度評估中更有意義。

---

# 33. Layer 3：Research Routing

現在進入 MCDM v0.2 最實用的部分。

定義 solver：

$$
S
$$

可以是：

- 個別數學家；
- 研究團隊；
- AI model；
- multi-agent system；
- theorem prover；
- hybrid human-AI system。

則：

$$
\boxed{
\mathfrak R(C\mid S,t)
}
$$

決定目前最適合的研究路線。

---

# 34. 原 AI 可攀爬性仍保留

v0.1 已定義：

$$
A_0-A_5,
$$

從現有模型直接可完成，到目前缺乏可信攻擊接口。

原文也特別指出 AI 擅長大量分支探索、有限反例搜尋、形式證明嘗試、證書生成與重複性計算。

v0.2 不刪除：

$$
A.
$$

而是投影成：

$$
\boxed{
A^+,
\qquad
A^-.
}
$$

---

# 35. 正向 AI 可攀爬性 $A^+$

回答：

> solver $S$ 現在有多適合尋找 $C$ 的證明？

例如 AI 可能：

$$
A^+=A4
$$

因為正證需要新的 global invariant。

---

# 36. 反向 AI 可攀爬性 $A^-$

同一猜想卻可能：

$$
A^-=A1
$$

因為反例若存在可以直接用 SAT/SMT 或 finite search 搜索。

所以：

$$
\boxed{
A^+\neq A^-.
}
$$

應成為 v0.2 的常態。

---

# 37. Verifiability 雙向投影

原 MCDM 已觀察到：

> 有些猜想很難求解，但一個有限反例可能很容易驗證；另一些長證明則需要大量審查。

因此：

$$
\boxed{
V^+
}
$$

表示正向證明 certificate 的驗證成本。

$$
\boxed{
V^-
}
$$

表示反向 certificate 的驗證成本。

---

# 38. 這與現代 AI 數學 benchmark 已經直接相關

FrontierMath 的 Tiers 1–4 已將 Background、Creativity 與 Execution 分開衡量，而 Tier 4 被設計成教授或博士後規模的短期研究任務。

其 Open Problems 更明確要求候選結果具有高度可程式驗證性；官方甚至直接指出，一個猜想的反例可能容易驗證但未必存在，而 proof 可能較可能存在、卻難以驗證。

這正是：

$$
\boxed{
V^+
\neq
V^-.
}
$$

的實際 benchmark 設計證據。

---

# 39. Formal Conjectures 也支持「問題陳述本身需要審計」

Formal Conjectures 將研究級猜想形式化為 Lean statements，其官方 repository 明確指出，形式化能澄清猜想含義、暴露缺失定義，但形式化本身也可能出現 subtle inaccuracies，因此需要人工審查與版本化修正。

這與 MCDM v0.1 原本對：

$$
F
$$

與：

$$
V
$$

需要 semantic audit 的警告一致。

因此 v0.2 再增加：

$$
\boxed{
Q\text{-audit}
}
$$

而不是用量詞形式化取代語義審計。

---

# 40. 研究進展累積性雙向化

原 MCDM：

$$
P_0-P_5
$$

描述：

> 每輪研究能否讓下一輪站得更高？

最高：

$$
P_5
$$

是每輪都能單調縮小剩餘判定域。

現在定義：

$$
\boxed{
P^+,
\qquad
P^-.
}
$$

---

# 41. $P^+$

正向研究是否累積。

例如：

- 新引理是否可重用？
- global invariant 是否逐步強化？
- theorem dependency graph 是否逐漸閉合？
- 剩餘 proof obligations 是否減少？

---

# 42. $P^-$

反向研究是否累積。

例如：

- 是否永久排除一段參數域？
- 是否淘汰整類算法？
- 是否建立 obstruction family？
- 是否逐步擴大 restricted lower bound？

---

# 43. 大規模測試不一定有高 $P^-$

若：

$$
\forall xP(x)
$$

已驗證：

$$
10^{20}
$$

個案例，

卻沒有產生：

- 新不變量；
- 新 exclusion theorem；
- 新 structural bound；

則：

$$
P^-
$$

未必高。

因為：

$$
\boxed{
N\uparrow
}
$$

不一定使：

$$
\boxed{
Q_{\mathrm{eff}}^-\downarrow.
}
$$

---

# 44. 定義 Directional Progress Rate

令：

$$
\alpha_N^+
$$

為前 $N$ 輪正向研究的有效累積率。

$$
\alpha_N^-
$$

為反向。

則：

$$
\boxed{
\alpha_N^\sigma
=
\frac{
\text{新增且可重用的 structural progress in direction }\sigma
}{
N
}.
}
$$

其中：

$$
\sigma\in\{+,-\}.
$$

---

# 45. Research Route Score 不應是固定總分

我們可以建立：

$$
\boxed{
\mathcal R^\sigma
=
F(
T^\sigma,
A^\sigma,
P^\sigma,
V^\sigma,
K_{\mathrm{gap}}^\sigma,
\text{cost},
\text{information gain}
).
}
$$

但本文不固定：

$$
F
$$

的權重。

因為：

$$
\boxed{
\text{研究政策不同，最佳路由不同。}
}
$$

---

# 46. 例如「最快得到結果」與「最可能解掉猜想」不是同一策略

研究目標：

$$
O_1
=
\text{publishable partial result}
$$

可能偏好：

$$
P^\sigma
$$

高的路線。

而：

$$
O_2
=
\text{maximize final closure probability}
$$

可能願意投入：

$$
T^\sigma
$$

更高但資訊價值更大的路線。

所以：

$$
\boxed{
\text{Routing}
=
\text{goal-relative}.
}
$$

---

# 47. Solver-Relative Difficulty

原 MCDM 已經指出：

$$
\mathfrak D_t
(
C
\mid
\mathcal K_t,\mathcal T_t
)
$$

隨知識與工具改變。

v0.2 進一步寫：

$$
\boxed{
\mathfrak D_t
(
C
\mid
S,\mathcal K_t,\mathcal T_t
).
}
$$

因此：

$$
\boxed{
\text{Difficulty}
}
$$

應理解為：

$$
\boxed{
\text{Problem–Solver Relative Difficulty}.
}
$$

---

# 48. 不同 AI 可以選不同的「難」

例如 solver：

$$
S_1
$$

特別強於：

- Lean；
- symbolic proof；
- lemma synthesis。

則適合：

$$
\boxed{
F^+\text{ 高成熟度}
+
P^+\text{ 高}
}
$$

的猜想。

---

# 49. 搜尋型 AI

若：

$$
S_2
$$

特別擅長：

- SAT；
- SMT；
- brute-force；
- program search；
- combinatorial enumeration；

則適合：

$$
\boxed{
V^-\text{ 低}
+
A^-\text{ 高}
}
$$

的反例友善猜想。

---

# 50. 結構發現型 AI

如果：

$$
S_3
$$

擅長：

- representation discovery；
- invariant mining；
- cross-domain analogy；
- symbolic regression；

則可能優先挑：

$$
\boxed{
K_{\mathrm{gap}}\text{ 高}
}
$$

但有大量 partial structure 的問題。

它的任務不是直接 proof search。

而是：

$$
\boxed{
\text{GQCM discovery}.
}
$$

---

# 51. 從「挑題」升級成「挑難法」

所以 MCDM v0.2 最重要的實際改變之一是：

以前：

> 選哪一道題？

現在：

$$
\boxed{
\text{選哪一道題的哪一個方向、哪一種困難？}
}
$$

例如同一猜想：

$$
C
$$

可以同時建立：

```text
Route A:
positive proof
global invariant discovery

Route B:
negative proof
finite counterexample search

Route C:
representation refactoring

Route D:
independence / axiom sensitivity
```

---

# 52. Research Routing Matrix

因此可以建立：

$$
\boxed{
\mathbf R(C)
=
\begin{pmatrix}
R_{\mathrm{proof}}\\
R_{\mathrm{disproof}}\\
R_{\mathrm{counterexample}}\\
R_{\mathrm{reformulation}}\\
R_{\mathrm{decomposition}}\\
R_{\mathrm{independence}}\\
R_{\mathrm{formalization}}
\end{pmatrix}.
}
$$

每條 route 分別具有自己的：

$$
T,
A,
P,
V,
K_{\mathrm{gap}}.
$$

---

# 53. MCDM 不再只是 Difficulty Matrix

因此名稱仍保留：

$$
\boxed{
\mathrm{MCDM}
}
$$

以保持歷史連續性。

但 v0.2 的實際功能已接近：

$$
\boxed{
\text{Mathematical Conjecture Difficulty
\& Research Routing Matrix}.
}
$$

---

# 54. 新版猜想卡

本文建議：

```yaml
mcdm_version: "0.2"

conjecture:
  id:
  title:
  formal_statement:
  informal_statement:
  status:
  domains:
  axiom_system:

core_difficulty:
  B:
  I:
  E:
  F:
  V:
  R:
  G:
  U:

summary:
  human_level:
  ai_climbability_legacy:
  progress_accumulability_legacy:

representations:
  - id:
    statement:
    equivalence_status:

quantifier_profile:

  positive:
    signature:
    blocks:
    dependency_graph:
    raw_burden:
    effective_burden:
    witness_type:
    global_compressors:
    compressor_gap:
    uniformity_gap:
    quantifier_swap_risk:
    proof_tension:
    discovery_difficulty:
    verification_difficulty:
    ai_climbability:
    progress_accumulability:

  negative:
    signature:
    blocks:
    dependency_graph:
    raw_burden:
    effective_burden:
    witness_type:
    global_compressors:
    compressor_gap:
    uniformity_gap:
    quantifier_swap_risk:
    refutation_tension:
    discovery_difficulty:
    verification_difficulty:
    ai_climbability:
    progress_accumulability:

asymmetry:
  delta_tension:
  preferred_direction:
  confidence:

closure:
  QCC:
  QCov:
  covered_domains:
  unresolved_domains:

research_routes:
  - route:
    expected_information_gain:
    estimated_compute_cost:
    estimated_human_cost:
    solver_fit:
    next_action:

known_results:
  partial:
  equivalences:
  counterexamples:
  failed_approaches:
  method_barriers:

audit:
  semantic_fidelity:
  formalization_version:
  toolchain:
  solver:
  last_reviewed:
  evidence:
```

---

# 55. Backward Compatibility

舊 MCDM v0.1 card 可以直接升級。

只需：

$$
\boxed{
\mathfrak D_0
}
$$

原封不動保留。

新增：

$$
\mathfrak Q
$$

與：

$$
\mathfrak R.
$$

所以資料遷移：

$$
\boxed{
v0.1
\rightarrow
v0.2
}
$$

不需要重新評所有舊欄位。

---

# 56. 缺資料可以明確留 Unknown

不允許為填滿 schema 而猜。

例如：

```yaml
global_compressors:
  status: unknown
```

而不是：

```yaml
global_compressors:
  status: none
```

因為：

$$
\boxed{
\text{不知道存在}
\neq
\text{知道不存在}.
}
$$

這與原 MCDM 對 $U$ 的精神一致。

---

# 57. 不可把路由建議當成真值預測

若系統輸出：

```text
preferred_direction: disproof
```

其意思只是：

> 目前證偽路線的 research interface 較好。

不能翻譯成：

> 猜想很可能是假的。

因此：

$$
\boxed{
\text{Research Route}
\neq
\text{Truth Probability}.
}
$$

這是一條必要安全線。

---

# 58. 「反例好找」也不能變成 Bayesian 真值結論

若：

$$
T^-<T^+,
$$

只代表：

$$
\boxed{
\text{證偽 certificate architecture 更友善}.
}
$$

不代表：

$$
P(\neg C)
>
P(C).
$$

除非另有真正 probabilistic model。

MCDM 不做此假設。

---

# 59. 不把難度等同學術價值

原 MCDM 已明確指出：

$$
\boxed{
\text{困難}
\neq
\text{重要}.
}
$$

MCDM 評估研究障礙，不評估美學、重要性或歷史地位。

v0.2 完全保留此原則。

因此：

$$
\boxed{
\text{容易被 AI 攻擊}
}
$$

不表示：

$$
\boxed{
\text{沒有學術價值}.
}
$$

---

# 60. 研究選題的 Pareto 原則仍然保留

v0.1 已主張：

$$
C_1\prec C_2
$$

只有當 $C_1$ 在所有比較維度都不差，且至少一項更低時才成立；若瓶頸不同，應視為不可直接排序。

v0.2 更應保持：

$$
\boxed{
\text{Pareto comparison}.
}
$$

不能重新退回單一：

$$
\text{Difficulty Score}=93.
$$

---

# 61. 可以做「研究菜單」，不能做絕對排行榜

例如平台可以顯示：

### Counterexample-Friendly

$$
T^-\ll T^+,
\qquad
V^-\text{ low}.
$$

### Proof-Construction-Friendly

$$
T^+<T^-,
\qquad
F^+,P^+\text{ high}.
$$

### Global-Invariant Needed

$$
K_{\mathrm{gap}}^+\text{ high},
\qquad
G\text{ high}.
$$

### Formalization-First

$$
F\text{ low},
\qquad
V\text{ uncertain}.
$$

### Currently Poor AI Interface

$$
A^+\approx A^-\approx A5.
$$

這比全球猜想「Top 100 hardest」更實用。

---

# 62. 自主 AI 數學平台的 scheduler

假設有：

$$
C_1,\ldots,C_N
$$

和：

$$
S_1,\ldots,S_M.
$$

則 scheduler 可以計算：

$$
\boxed{
\operatorname{Fit}
(
C_i,
r,
S_j,t
)
}
$$

其中：

$$
r
$$

是一條 research route。

不是只計算：

$$
\operatorname{Difficulty}(C_i).
$$

---

# 63. 任務分配可以變成

$$
\boxed{
(S_j,C_i,r)
}
$$

三元組。

例如：

$$
(S_{\mathrm{search}},
C_{17},
\mathrm{counterexample})
$$

和：

$$
(S_{\mathrm{Lean}},
C_{42},
\mathrm{formal\ proof})
$$

是兩個不同任務。

---

# 64. 算力分配

令：

$$
b_{ijr}
$$

為 solver $j$ 對猜想 $i$ 的 route $r$ 所分配算力。

則可以研究：

$$
\boxed{
\max
\sum_{i,j,r}
b_{ijr}
\cdot
\mathbb E[
\operatorname{InformationGain}_{ijr}
]
}
$$

subject to：

$$
\sum b_{ijr}\le B_{\mathrm{total}}.
$$

這把 MCDM 從分類表變成真正研究資源配置接口。

---

# 65. Information Gain 比「有沒有解掉」更適合長期研究

一輪研究即使沒有得到：

$$
C
$$

或：

$$
\neg C,
$$

但若：

- 淘汰一整類 proof route；
- 降低 $Q_{\mathrm{eff}}$ ；
- 增加 $QCov$ ；
- 找到新的 GQCM；
- 降低 $K_{\mathrm{gap}}$ ；

則：

$$
\boxed{
\operatorname{InformationGain}>0.
}
$$

---

# 66. Quantifier Progress

定義：

$$
\boxed{
\Delta_Q(t)
=
Q_{\mathrm{eff}}(t)
-
Q_{\mathrm{eff}}(t+1)
}
$$

在偏序／結構意義上。

若：

$$
\Delta_Q>0,
$$

表示有效量詞負擔下降。

這可以成為新的研究進展指標。

---

# 67. Compressor Progress

同樣：

$$
\boxed{
\Delta_K
=
K_{\mathrm{gap}}(t)
-
K_{\mathrm{gap}}(t+1).
}
$$

若找到：

$$
\mathfrak G
$$

能控制以前完全無法控制的一整個 domain，

即使猜想沒解，

也可能是巨大進展。

---

# 68. Uniformity Progress

如果原本只有：

$$
\forall x\exists W_x,
$$

後來發現 parametric：

$$
W_\theta
$$

再發展成：

$$
W=f(x),
$$

那可以表示：

$$
\boxed{
\text{instance}
\rightarrow
\text{family}
\rightarrow
\text{uniform generator}.
}
$$

這是一條非常具體的 progress ladder。

---

# 69. Barrier Progress

若證明某方法族：

$$
\mathcal M
$$

不能解：

$$
C,
$$

則：

$$
\boxed{
\mathcal R_{\mathrm{search}}
\leftarrow
\mathcal R_{\mathrm{search}}\setminus\mathcal M.
}
$$

所以：

$$
\boxed{
\text{method failure theorem}
}
$$

本身也是結構性研究成果。

---

# 70. MCDM v0.2 不假定所有猜想都能如此形式化

有些猜想：

- 自然語言尚不精確；
- 使用高階幾何概念；
- 等價形式極多；
- proof architecture 不適合 prenex normalization；
- 量詞提取可能造成巨大語義損失。

因此：

$$
\boxed{
\mathfrak Q(C)
}
$$

可以是 partial。

---

# 71. Quantifier Formalization Confidence

新增：

$$
\boxed{
C_Q\in[0,1]
}
$$

表示：

> 目前量詞剖面對原數學命題的忠實程度。

如果：

$$
C_Q
$$

低，

就不能過度使用 routing 結論。

---

# 72. 語義先於 routing

因此：

$$
\boxed{
\text{Formal Quantifier Profile}
}
$$

必須經：

$$
\boxed{
\text{Semantic Fidelity Audit}.
}
$$

Formal Conjectures 官方 repository 同樣明確提醒，形式化 conjecture statement 本身可能存在 subtle inaccuracies，需要持續人工審查與版本修正。

---

# 73. Benchmark 不應只看 final success

TheoremBench 的設計已經開始從單一 theorem success 擴張到 supporting subtheorems、coverage 與 token efficiency，以觀察 proof structure 中的部分進展，而不只看最終 theorem 是否完成。

這與 MCDM v0.2 的：

$$
QCov,
\quad
P^\pm,
\quad
\alpha_N^\pm
$$

在方法論上具有相近方向。

本文不是聲稱兩者等價，而是指出：

$$
\boxed{
\text{研究級 AI 評估正在從 final-answer binary score
走向 structural progress metrics}.
}
$$

---

# 74. Formal Conjectures 的 evolving benchmark 也說明版本化必要

Formal Conjectures 被設計為持續演進的 Lean 研究級猜想庫，並使用 frozen benchmark snapshots 與版本化管理；其論文亦將 verified discovery 與 climbable signal 作為重要目標。

因此 MCDM card 也不應是：

$$
\boxed{
\text{永久固定標籤}.
}
$$

---

# 75. 難度版本歷史

原 MCDM 已提出：

```text
2026:
B5 I6 E4 F2 V5 R6 G5 U3

2028:
B5 I5 E4 F4 V3 R6 G4 U2
```

這種版本化難度。

v0.2 再增加：

```text
2026:
T+ high
T- medium
Kgap+ 5
Kgap- 3
QCov 0.12

2028:
T+ medium
T- medium
Kgap+ 3
Kgap- 3
QCov 0.46
```

---

# 76. 猜想可以「變容易」，即使還沒被解掉

如果：

$$
K_{\mathrm{gap}}:5\rightarrow2,
$$

或者：

$$
Q_{\mathrm{eff}}
$$

大幅縮小，

那就是：

$$
\boxed{
\text{Difficulty Collapse Without Final Solution}.
}
$$

這是 MCDM 最值得長期追蹤的東西之一。

---

# 77. MCDM v0.2 的最小實作版本

若不想一開始填全部字段，可以先只加六項：

$$
\boxed{
Q^+,\;
Q^-,\;
T^+,\;
T^-,\;
K_{\mathrm{gap}}^+,\;
K_{\mathrm{gap}}^-.
}
$$

以及：

$$
\boxed{
A^+,\;A^-.
}
$$

八個字段已足以大幅改善 AI 選題。

---

# 78. 第二階段再加入

$$
\boxed{
QCov,
QCC,
J_{\mathrm{swap}},
P^+,
P^-,
V^+,
V^-.
}
$$

---

# 79. 第三階段才做自動 routing

當數據足夠之後再訓練／建立：

$$
\boxed{
\operatorname{Router}
(
C,S,t
).
}
$$

不要一開始假設人工設計權重就是正確的。

---

# 80. Router 應從歷史結果校準

未來可以收集：

- 哪些 route 最終成功；
- 每條 route 使用多少算力；
- 哪些 barrier 被發現；
- 哪些 $K_{\mathrm{gap}}$ 下降；
- 哪些 AI 對哪些量詞型態較強；
- 哪些錯誤最常來自 quantifier swap。

再更新：

$$
\boxed{
\operatorname{Router}_{t+1}.
}
$$

---

# 81. 這使 MCDM 成為動態系統

最終：

$$
\boxed{
\mathrm{MCDM}_t
}
$$

不是一張表。

而是：

$$
\boxed{
\text{Problem State}
+
\text{Solver State}
+
\text{Knowledge State}
+
\text{Research History}.
}
$$

---

# 82. MCDM 與真理保持分離

即使：

$$
\mathrm{Router}
$$

說：

> 90% 算力投入 disproof route。

也不能寫：

$$
P(\neg C)=0.9.
$$

MCDM 是：

$$
\boxed{
\text{Research Decision Model}.
}
$$

不是：

$$
\boxed{
\text{Truth Oracle}.
}
$$

---

# 83. MCDM 與證明助理保持分離

Lean／Coq 可以驗證：

$$
\Pi
$$

在形式系統中是否合法。

MCDM 則回答：

> 這條 theorem 是否覆蓋原猜想需要的量詞？
>  
> 這條路對 solver 是否值得投資？
>  
> 還剩哪個全域障礙？

因此：

$$
\boxed{
\text{Proof Assistant}
\neq
\text{Research Router}.
}
$$

兩者是互補關係。

---

# 84. MCDM 與 benchmark 也保持分離

benchmark 通常問：

$$
\boxed{
\text{model solved task?}
}
$$

MCDM 則問：

$$
\boxed{
\text{task structure is what, and why was it solved or unsolved?}
}
$$

FrontierMath 已使用 Background、Creativity、Execution 等維度而不是單看答案長度；Open Problems 又增加 verifiability 等選題條件。

MCDM v0.2 往更長期 research-planning 層前進。

---

# 85. MCDM v0.2 的核心輸出不應是一個數字

理想輸出例如：

```text
Core:
B3 I5 E3 F4 V2 R5 G5 U2

Positive route:
Q = ∀∃∀
T+ = very high
Kgap+ = 4
A+ = A4
P+ = P3

Negative route:
Q = ∃∀∃
T- = high
Kgap- = 3
A- = A2
P- = P4

Primary recommendation:
negative obstruction mining

Secondary:
positive strategy-function synthesis

Do not:
interpret finite search success as universal proof
```

這才真正具有研究用途。

---

# 86. 第一個新核心原則：方向條件難度

$$
\boxed{
\operatorname{Difficulty}(C)
}
$$

應展開為：

$$
\boxed{
\operatorname{Difficulty}^+(C),
\qquad
\operatorname{Difficulty}^-(C).
}
$$

再加其他 resolution modes。

---

# 87. 第二個核心原則：量詞優先審計

在大規模 proof search 前，

先問：

$$
\boxed{
Q^+?
\qquad
Q^-?
}
$$

以及：

$$
\boxed{
Q_{\mathrm{eff}}^\pm?
}
$$

---

# 88. 第三個核心原則：量詞交換禁令

$$
\boxed{
\forall x\exists W_x
\centernot\Rightarrow
\exists W\forall x.
}
$$

所有 AI-generated proof 必須對這類交換做自動審計。

---

# 89. 第四個核心原則：全域壓縮器優先

對高：

$$
G
$$

且高：

$$
K_{\mathrm{gap}}
$$

問題，

繼續增加 finite samples 可能不是最佳資源使用。

應轉向：

$$
\boxed{
\mathrm{GQCM\ discovery}.
}
$$

---

# 90. 第五個核心原則：search 與 verification 分離

$$
\boxed{
D_{\mathrm{discover}}
\neq
D_{\mathrm{verify}}.
}
$$

尤其不要因反例短，就認為反例容易找到。

---

# 91. 第六個核心原則：研究可累積性優先

兩條同樣難的 route，

若：

$$
P_1=P5,
$$

而：

$$
P_2=P0,
$$

長期自主 AI 系統通常應優先考慮第一條，

除非存在其他高價值因素。

---

# 92. 第七個核心原則：solver 相對性

真正要估計的是：

$$
\boxed{
D(C\mid S,t)
}
$$

而不是：

$$
D(C)
$$

的永恆絕對值。

---

# 93. 第八個核心原則：難度不是價值

MCDM 永遠禁止：

$$
\boxed{
\text{higher difficulty}
\Rightarrow
\text{higher mathematical value}.
}
$$

---

# 94. 第九個核心原則：路由不是預言

$$
\boxed{
\text{preferred proof route}
\neq
\text{predicted truth value}.
}
$$

---

# 95. 第十個核心原則：失敗也可以是成果

如果一輪研究證明：

$$
K_i
$$

不可能閉合，

或者：

$$
QCov
$$

擴大，

或者：

$$
J_{\mathrm{swap}}
$$

被消除，

即使猜想仍 open：

$$
\boxed{
\text{research progress}>0.
}
$$

---

# 96. 完整架構

因此 MCDM v0.2 最終寫為：

$$
\boxed{
\mathrm{MCDM}_{0.2}
(C\mid S,t)
=
\left[
\underbrace{
(B,I,E,F,V,R,G,U)
}_{\text{Core Obstruction}},
\;
\underbrace{
\mathfrak Q(C)
}_{\text{Quantifier/Proof Architecture}},
\;
\underbrace{
\mathfrak R(C\mid S,t)
}_{\text{Research Routing}}
\right].
}
$$

---

# 97. 其中量詞層為

$$
\boxed{
\mathfrak Q(C)
=
(
Q^\pm,
A_Q,
D_Q,
Q_{\mathrm{eff}}^\pm,
K^\pm,
K_{\mathrm{gap}}^\pm,
W^\pm,
J,
T^\pm,
\Delta T,
QCC,
QCov
).
}
$$

---

# 98. 路由層為

$$
\boxed{
\mathfrak R(C\mid S,t)
=
(
A^\pm,
P^\pm,
V^\pm,
C_{\mathrm{compute}}^\pm,
C_{\mathrm{human}}^\pm,
IG^\pm,
\Pi_{\mathrm{route}}
).
}
$$

其中：

$$
IG
=
\text{Expected Information Gain}.
$$

---

# 99. 從 Difficulty Matrix 到 Research Infrastructure

MCDM v0.1 的最終目標已不是排行榜，而是讓數學猜想難度表成為可版本化、可審計、人類與 AI 共用的研究基礎設施。

v0.2 將這個目標再推一步：

$$
\boxed{
\text{Difficulty Description}
\rightarrow
\text{Research Routing}.
}
$$

---

# 100. 最終結論

數學猜想的困難不只是：

$$
\boxed{
\text{它有多深？}
}
$$

也不只是：

$$
\boxed{
\text{它有多大？}
}
$$

甚至不只是：

$$
\boxed{
\text{它有多少全域耦合？}
}
$$

真正完整的研究問題還包括：

$$
\boxed{
\text{它的正向與反向量詞到底長什麼樣？}
}
$$

$$
\boxed{
\text{兩條方向各自需要什麼 certificate？}
}
$$

$$
\boxed{
\text{哪一個 }\forall
\text{ 尚未被壓縮？}
}
$$

$$
\boxed{
\text{哪一個 }\exists
\text{ 尚未找到 uniform witness？}
}
$$

以及：

$$
\boxed{
\text{目前這個 solver 到底應該攻哪一邊？}
}
$$

MCDM v0.2 因此將原：

$$
\mathfrak D(C)
=
(B,I,E,F,V,R,G,U)
$$

保留為基礎，

但在其上加入：

$$
\boxed{
\mathfrak Q(C)
}
$$

與：

$$
\boxed{
\mathfrak R(C\mid S,t).
}
$$

從此同一猜想可以同時具有：

$$
\boxed{
T^+\gg T^-,
}
$$

也可以：

$$
\boxed{
A^-\gg A^+,
}
$$

甚至：

$$
\boxed{
P^+\ll P^-.
}
$$

因此不再存在一個足以描述研究決策的單一：

$$
\boxed{
\text{「難度」}.
}
$$

真正應保存的是：

$$
\boxed{
\text{Difficulty Profile}
+
\text{Proof Architecture}
+
\text{Solver Fit}
+
\text{Research History}.
}
$$

最終，數學研究選題可以從：

> 哪一道猜想比較容易？

提升成：

$$
\boxed{
\text{對現在的我／AI，
哪一道猜想的哪一個方向，
具有最適合的證明張力？}
}
$$

再提升成：

$$
\boxed{
\text{投入下一單位研究資源，
哪一條路最可能降低有效未知域？}
}
$$

這才是 MCDM v0.2 真正想建立的東西。

它不是：

$$
\boxed{
\text{數學難題排行榜}.
}
$$

而是：

$$
\boxed{
\text{數學研究導航系統}.
}
$$

---

# 系列封頂

本系列至此形成四層：

$$
\boxed{
\begin{aligned}
\text{Paper I}
&:
\text{Global Quantifier Compression},
\\
\text{Paper II}
&:
\text{Proof–Refutation Quantifier Asymmetry},
\\
\text{Paper III}
&:
\text{P/NP Quantifier Interfaces},
\\
\text{Paper IV}
&:
\text{MCDM v0.2 Research Routing}.
\end{aligned}
}
$$

其依賴關係為：

$$
\boxed{
\mathrm{GQCM}
\rightarrow
\mathrm{PRQA}
\rightarrow
\begin{cases}
\mathrm{P/NP\ realization},\\
\mathrm{MCDM\ generalization}.
\end{cases}
}
$$

本系列在此停止橫向理論擴張。

若未來重新啟動，下一階段不應立即增加第五篇理論文章，而應進入：

$$
\boxed{
\text{MCDM v0.2 Conjecture Card Schema}
}
$$

$$
\boxed{
\text{Conjecture Dataset}
}
$$

與：

$$
\boxed{
\text{AI Research Router MVP}.
}
$$

也就是開始實際測試：

> 這套分類到底能不能比「題目難度分數」更好地幫助人類與 AI 選擇研究路線？