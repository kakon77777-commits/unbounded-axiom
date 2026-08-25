# MWT-01：World Primitive 與 Presentation Theory
## 不可耗盡世界、多重數學表示、忠實度、翻譯與跨基礎共存

**英文題名：** *MWT-01: World Primitive and Presentation Theory — An Inexhaustible World, Multiple Mathematical Presentations, Fidelity, Translation, and Cross-Foundation Coexistence*  
**系列：** Mathematical World Theory（MWT）  
**篇次：** 01  
**文件編號：** EML-MWT-01-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-18  
**版本：** v0.1  
**文件性質：** 數學世界論第一篇形式母稿／Presentation Theory／AI-native mathematical infrastructure  
**前置文件：** 《數學世界論 v0.1》  
**狀態：** 可使用研究稿；尚非封閉基礎系統；不宣稱取代集合論、型別論、範疇論、模型論或既有形式邏輯  

---

## 摘要

本文建立數學世界論（Mathematical World Theory, MWT）的第一個正式分論文：**World Primitive 與 Presentation Theory**。

《數學世界論 v0.1》已將 World 設為 primitive，並提出「任何單一數學表示一般不等於 World 本身」。然而，若只停留在此層，仍有一個形式缺口：當我們寫

$$
\rho(\mathbf W)=M,
$$

很容易在不知不覺間把 $\mathbf W$ 當成普通函數的已知定義域，因而重新將 World 偷渡成集合、空間、狀態集合或其他既定數學對象。本文因此將這一記號降為非正式縮寫，改以 **presentation judgment** 作為第一級接口：

$$
\boxed{
\mathbf W
\xRightarrow[\Gamma,O,t,\lambda]{\rho_\alpha}
M_{\alpha,O,t,\lambda}.
}
$$

此式不宣稱 $\rho_\alpha$ 是以 $\mathbf W$ 為普通集合論定義域的函數，而表示：在 context $\Gamma$ 、觀察者 $O$ 、時間／版本 $t$ 與解析尺度 $\lambda$ 下，使用 presentation protocol $\rho_\alpha$，得到一個可被指定數學後端操作的呈現 $M_{\alpha,O,t,\lambda}$。

本文由此建立 **Presentation Theory**。其核心立場為：

$$
\boxed{
\text{World is primitive;}
\qquad
\text{mathematics operates on presentations.}
}
$$

以及：

$$
\boxed{
\text{presentation plurality}
\neq
\text{world plurality}.
}
$$

同一 World 可以具有集合論、型別論、拓樸、幾何、圖、張量、狀態、算子、機率、邏輯、程式、證明物件、觀察者相對表示等多種 presentation。這些 presentation 可以彼此相容、部分翻譯、保守擴張、粗粒化、精細化、不可比較，甚至在指定判定域內發生衝突。MWT 不要求它們全部化約為唯一語法，也不允許由「某個 presentation 很成功」推出「該 presentation 就是 World」。

本文進一步提出 **相對忠實度**。MWT 不使用一個無條件的全域實數分數聲稱某表示「百分之多少接近世界」，而是先指定欲保留的 inquiry family、observable family 或 invariant family：

$$
\mathcal Q.
$$

再判定 presentation $P$ 對 $\mathcal Q$ 的：

- coverage；
- distinguishability；
- recoverability；
- invariant preservation；
- legality preservation；
- history preservation；
- computational executability。

由此得到相對於 $\mathcal Q$ 的 fidelity profile，而不是假裝存在已知的終極距離

$$
d(P,\mathbf W).
$$

本文同時建立 loss、artifact、ambiguity、refinement、coarse-graining、translation、transport、bridge、presentation equivalence 與 world-addressable identity 等概念。兩個 presentation 之間即使存在雙向翻譯，也只有在指定 identity specification 與 invariant family 下，才可宣稱某種相對等價；不能直接推出：

$$
P\equiv Q
\Longrightarrow
P=\mathbf W.
$$

在主體層，presentation 必須帶 observer index。不同主體可能因可達域、解析尺度、操作能力、歷史與判定域不同而形成不同的有效數學，但 observer-relative 不等於 arbitrary。跨主體 presentation 必須接受 transport、協變性、證書與重放檢查。

在 AI-native 運行層，本文提出 Presentation Registry、Bridge Registry、Identity Ledger、Invariant Ledger、Legality Engine 與 Translation Graph 六個最低模組，使 AI 可以維持大量異質數學後端，而不強迫它們先被壓縮成單一表示。這使 MWT 的全域計算第一次獲得一個真正可實作的入口：**全域計算不是直接計算 World 本身，而是在多個合法 presentations 及其橋接圖上，維持可追溯、可分支、可重放的世界級計算。**

本文最後將 MWT 與 Institution Theory、Univalent Foundations、set-theoretic pluralism、logical pluralism 與 heterogeneous formal reasoning 區分。MWT 不宣稱重新發明這些成熟工具；其候選新意位於：將 heterogeneous mathematical presentations、observer-indexing、legality-first interaction、noncommutative history、AI runtime orchestration 與 World primitive 放入同一個長期數學世界運行框架。

**關鍵詞：** Mathematical World Theory、World primitive、Presentation Theory、多重表示、數學多元論、跨基礎翻譯、忠實度、表示損失、觀察者數學、AI-native mathematics、heterogeneous logic、institution theory、noncommutative history

---

# 0. 本文的責任：先把「世界」與「表示世界」切乾淨

MWT v0.1 的母命題是：

$$
\boxed{
\mathbf W
}
$$

作為 World primitive。

但只說「World 是 primitive」仍然不夠。

因為人類形式化具有一個極強的習慣：

> 一旦某個東西被命名，就立刻替它找一個集合、tuple、空間、圖或型別。

這個習慣非常有用。

但對 MWT 而言，它會造成一個危險：

$$
\mathbf W
\rightsquigarrow
(X,R,F,I,\ldots)
$$

然後我們很快忘記：

$$
(X,R,F,I,\ldots)
$$

本來只是一個 representation。

最後又開始說：

$$
\mathbf W
=
(X,R,F,I,\ldots).
$$

如此一來，MWT 只是把舊問題換一個更長的 tuple 重演一次。

本文的第一責任因此是建立永久邊界：

$$
\boxed{
\text{World}
\neq
\text{World-description}
}
$$

以及：

$$
\boxed{
\text{mathematical object used to represent World}
\neq
\text{World by default}.
}
$$

這不是反數學。

恰恰相反，它是在替不同數學留下共同存在空間。

---

# 1. 第一原則：World Primitive

本文不定義：

$$
\mathbf W\in X
$$

也不定義：

$$
\mathbf W=(x_1,\ldots,x_n).
$$

更不預設：

$$
\mathbf W
$$

必須是某個 category 中的 object。

這些都可以在某個後端 presentation 中成立，但不是 MWT 的起始本體承諾。

因此 v0.1 採取以下 **World Primitive Principle**：

> **MWT 將 $\mathbf W$ 作為理論中的原始指稱項。任何對 $\mathbf W$ 的集合論、型別論、範疇論、拓樸、幾何、圖論、張量、邏輯、狀態機或計算性解釋，都必須額外標記為 presentation，而不得由記號本身自動獲得本體唯一性。**

形式上，若：

$$
P_\alpha
$$

是某個 presentation，則可以建立：

$$
\mathbf W
\xRightarrow{\rho_\alpha}
M_\alpha.
$$

但不能反推：

$$
M_\alpha
=
\mathbf W.
$$

---

# 2. 第二原則：Presentation Non-Exhaustion

設：

$$
P_\alpha
$$

是當前可用 presentation。

MWT 一般不假設存在：

$$
P_\alpha
$$

使其無條件耗盡 World。

因此提出：

$$
\boxed{
\text{Presentation Non-Exhaustion Principle}
}
$$

其 v0.1 形式為：

> 對任何未經額外完備性證明的 presentation $P_\alpha$，不得宣稱它保存了對 $\mathbf W$ 的所有可區分結構、所有可觀察量、所有歷史、所有合法操作與所有未來可建立的 refinement。

注意，這不是宣稱：

$$
\forall P,\quad P\text{ 必然不完備}.
$$

這是一個**證明責任分配原則**。

如果某個研究域真的可以證明：

$$
P
$$

對指定 inquiry class：

$$
\mathcal Q
$$

是 complete，那麼 MWT 接受：

$$
\operatorname{Complete}(P\mid\mathcal Q).
$$

但這只能推出：

$$
\boxed{
P
\text{ 對 }
\mathcal Q
\text{ 完備}
}
$$

而不能直接推出：

$$
\boxed{
P
\text{ 對所有可能問題完備}.
}
$$

---

# 3. 為什麼改用 Presentation Judgment

母稿中常用：

$$
\rho_{\alpha,O,t}(\mathbf W)
=
M_{\alpha,O,t}.
$$

這在閱讀上方便。

但形式上它容易帶入：

$$
\rho:
D\to C
$$

且：

$$
\mathbf W\in D
$$

的普通函數語義。

如果 $D$ 尚未定義，這個記號就比理論承諾得更多。

因此本文正式採：

$$
\boxed{
\mathbf W
\xRightarrow[\Gamma,O,t,\lambda]{\rho_\alpha}
M_{\alpha,O,t,\lambda}.
}
$$

讀作：

> 在 context $\Gamma$ 、observer $O$ 、時間／版本 $t$ 、解析尺度 $\lambda$ 下， $\mathbf W$ 經由 presentation protocol $\rho_\alpha$ 被呈現為 $M_{\alpha,O,t,\lambda}$。

這是一個 judgment。

它不要求 $\mathbf W$ 是 ordinary domain element。

---

## 3.1 Shorthand Rule

為閱讀便利，仍允許非正式地寫：

$$
\rho_\alpha(\mathbf W).
$$

但其 canonical interpretation 必須是：

$$
\boxed{
\rho_\alpha(\mathbf W)
\quad\text{is shorthand for}\quad
\mathbf W
\xRightarrow{\rho_\alpha}
M_\alpha.
}
$$

而不是偷偷新增：

$$
\mathbf W\in\operatorname{Dom}(\rho_\alpha).
$$

---

# 4. Presentation 是什麼？

Presentation 不是「畫面」。

也不只是「符號」。

在 MWT 中，一個 presentation 是：

> **一套允許某些 World-related distinctions 被合法表達、比較、操作、證明、計算或觀察的結構化接口。**

因此：

- 一個集合論編碼是一種 presentation；
- 一個型別論 formalization 是一種 presentation；
- 一個 graph representation 是一種 presentation；
- 一組 PDE 是一種 presentation；
- 一個 probability distribution family 是一種 presentation；
- 一個 state machine 是一種 presentation；
- 一個 tensor representation 是一種 presentation；
- 一個自然語言定義也可以是低形式度 presentation；
- 一個 simulation state 也可以是 runtime presentation。

所以：

$$
\boxed{
\text{Presentation}
\supsetneq
\text{notation}.
}
$$

---

# 5. Minimal Presentation Interface

MWT 不要求所有 presentation 都擁有完全相同的內部本體。

但若一個 presentation 要進入可計算 MWT runtime，至少需要暴露一組 interface。

定義一個 minimal presentation interface：

$$
\boxed{
\mathbb P
=
(
\mathsf{Expr},
\mathsf{Sem},
\mathsf{Id},
\mathsf{Leg},
\mathsf{Op},
\mathsf{Cert}
).
}
$$

其中：

### 5.1 Expression Surface

$$
\mathsf{Expr}_P
$$

表示該 presentation 可合法承載的表達、物件、結構或資料。

它不必是字串集合。

可以是：

- syntax tree；
- proof term；
- graph；
- manifold data；
- tensor；
- program；
- geometric object；
- oracle interface。

### 5.2 Semantic Interface

$$
\mathsf{Sem}_P
$$

指定 expression 在該 presentation 中「代表什麼」。

它可以是：

- satisfaction relation；
- interpretation map；
- operational semantics；
- denotational semantics；
- model class；
- simulation semantics；
- measurement semantics。

### 5.3 Identity Specification

$$
\mathsf{Id}_P
$$

回答：

> 哪些差異在這個 presentation 中仍算同一個對象？

例如：

$$
x\equiv_P y.
$$

### 5.4 Legality Structure

$$
\mathsf{Leg}_P
$$

判定哪些構造、轉換、作用或推導在該 presentation 中合法。

### 5.5 Operation Interface

$$
\mathsf{Op}_P
$$

列出可在此 presentation 中執行的合法 operators、morphisms、rewrites、proof steps 或 transformations。

### 5.6 Certificate Interface

$$
\mathsf{Cert}_P
$$

描述此 presentation 如何證明：

- 一個 expression well-formed；
- 一個作用合法；
- 一個翻譯保持語義；
- 一個結果可重放；
- 一個 invariant 被保存。

---

# 6. Capability Profile，而不是固定大 tuple

不是所有 presentation 都需要：

$$
\mathsf{Proof},
\mathsf{Measure},
\mathsf{Topology},
\mathsf{Probability},
\mathsf{History}.
$$

因此 MWT 不把這些全部硬塞進 minimal interface。

改採 capability profile：

$$
\boxed{
\operatorname{Cap}(P)
\subseteq
\mathcal K.
}
$$

其中 $\mathcal K$ 可以包含：

$$
\{
\text{proof},
\text{simulation},
\text{measurement},
\text{optimization},
\text{history},
\text{transport},
\text{probability},
\text{topology},
\text{geometry},
\text{symbolic},
\text{numeric},
\ldots
\}.
$$

未來增加新 capability：

$$
k_{\mathrm{new}}
$$

不需要修改 World primitive。

也不需要修改所有既有 presentation。

---

# 7. Presentation Type 不預先封閉

令時間 $t$ 已知 presentation type family 為：

$$
\mathcal T_t^{P}.
$$

MWT 只要求：

$$
|\mathcal T_t^{P}|<\infty
$$

於任何實際 registry snapshot 中。

但不要求：

$$
\exists N
\quad
\forall t,\quad
|\mathcal T_t^{P}|\le N.
$$

因此：

$$
\boxed{
\text{presentation vocabulary is open-ended}.
}
$$

這是有限 runtime／無界 refinement 原則在表示層的版本。

---

# 8. Context-Indexed Presentation

同一 presentation protocol 在不同 context 下可能產生不同有效結構。

因此完整 judgment 為：

$$
\boxed{
\mathbf W
\xRightarrow[\Gamma,O,t,\lambda]{\rho_\alpha}
M.
}
$$

其中：

- $\Gamma$：問題條件、基礎、公理、資料、合法域；
- $O$：觀察者；
- $t$：歷史、時間、版本；
- $\lambda$：解析度或尺度。

所以不能簡化為：

$$
M_\alpha
$$

並假裝它與 context 無關。

---

# 9. Observer-Indexed Presentation

對 observer $O$：

$$
\mathbf W
\xRightarrow[O]{\rho_\alpha}
M_\alpha^O.
$$

對 observer $P$：

$$
\mathbf W
\xRightarrow[P]{\rho_\alpha}
M_\alpha^P.
$$

一般情況：

$$
M_\alpha^O
\neq
M_\alpha^P.
$$

但這不表示存在兩個 World。

它只表示：

$$
\boxed{
\text{same World}
+
\text{different access structure}
\rightarrow
\text{different presentations}.
}
$$

---

# 10. Resolution-Indexed Presentation

同一 observer 也可能在不同解析度得到：

$$
M_{\lambda_1}
$$

與：

$$
M_{\lambda_2}.
$$

例如：

- 一個節點；
- 一個 graph；
- 一個內部多層 graph；
- 一個連續場；
- 一個 microscopic state ensemble。

因此：

$$
\boxed{
\lambda_1\neq\lambda_2
\not\Rightarrow
\mathbf W_{\lambda_1}\neq\mathbf W_{\lambda_2}.
}
$$

尺度差異首先是 presentation difference。

是否構成 object identity difference，交由：

$$
\mathsf{Id}
$$

決定。

---

# 11. Presentation Fidelity：禁止假裝知道與 World 的終極距離

一個非常危險的記號是：

$$
d(P,\mathbf W).
$$

除非我們已經知道：

1. $\mathbf W$ 的完整可比較結構；
2. $P$ 和 $\mathbf W$ 位於同一 metric space；
3. $d$ 有明確語義；
4. 這個距離本身可被觀察。

否則：

$$
d(P,\mathbf W)
$$

只是把「不知道」寫成一個看起來很精準的公式。

所以 MWT v0.1 不採用無條件 World-distance。

---

# 12. Inquiry-Relative Fidelity

先指定 inquiry family：

$$
\boxed{
\mathcal Q
=
\{q_i\}_{i\in I}.
}
$$

 $q_i$ 可以是：

- 判定問題；
- observable；
- invariant；
- proof obligation；
- dynamical query；
- identity query；
- transport query；
- counterfactual；
- computational task。

然後才問：

> Presentation $P$ 對 $\mathcal Q$ 保存了什麼？

定義 fidelity profile：

$$
\boxed{
\mathsf{Fid}(P\mid\mathcal Q)
=
(
C,D,R,I,L,H,E
).
}
$$

其中：

- $C$：coverage；
- $D$：distinguishability；
- $R$：recoverability；
- $I$：invariant preservation；
- $L$：legality preservation；
- $H$：history preservation；
- $E$：executability。

這些分量不必全部是數值。

它們可以是：

- Boolean；
- partial order；
- certificate；
- interval；
- symbolic status；
- proof object。

---

# 13. Coverage

定義：

$$
\operatorname{Cov}(P\mid\mathcal Q)
$$

表示：

> $\mathcal Q$ 中哪些 inquiry 可以在 $P$ 中被合法表達。

若：

$$
q\in\mathcal Q
$$

但 $P$ 根本沒有對應語言，則不是：

$$
P(q)=\mathsf{false}.
$$

而是：

$$
\boxed{
q\notin\operatorname{Expressible}(P).
}
$$

這個區分極重要。

「不能問」不等於「答案是否定」。

---

# 14. Distinguishability

即使兩個 World-related cases：

$$
x\neq y
$$

在某個更精細 presentation 中可以區分，

粗 presentation $P$ 可能得到：

$$
\rho_P(x)
=
\rho_P(y).
$$

因此定義相對 indistinguishability：

$$
\boxed{
x\sim_P y
}
$$

若 $P$ 無法在指定 inquiry family 中區分兩者。

這裡：

$$
x\sim_P y
$$

不等於：

$$
x=y.
$$

---

# 15. Recoverability

如果 presentation $P$ 是由更精細 presentation $Q$ 粗化得到：

$$
c:
Q\to P,
$$

則問是否存在：

$$
r:
P\to Q
$$

使：

$$
r\circ c
\equiv_Q
\operatorname{id}_Q.
$$

若存在，則在指定 identity specification 下可逆。

若不存在，則：

$$
\boxed{
\text{coarse-graining is lossy relative to that identity}.
}
$$

---

# 16. Invariant Preservation

若：

$$
I\in\mathcal Q
$$

是一個 invariant，presentation translation：

$$
T:P\to Q
$$

應檢查：

$$
\boxed{
I_Q(T(x))
=
I_P(x)
}
$$

或更一般地：

$$
I_Q\circ T
\cong
I_P.
$$

若此式不成立，則：

$$
T
$$

不能被稱為對 $I$ 忠實。

---

# 17. Legality Preservation

翻譯最容易被忽略的問題之一是：

> 在 $P$ 中合法的東西，翻譯到 $Q$ 後仍合法嗎？

因此要求：

$$
\Lambda_P(o;x)
=
\mathsf{Legal}
$$

若被宣稱由 $T$ 保持，則應有：

$$
\Lambda_Q(T(o);T(x))
=
\mathsf{Legal}.
$$

如果翻譯只保留 expression，卻破壞 legality，則它不是完整 MWT bridge。

---

# 18. History Preservation

對非交換路徑：

$$
\gamma
=
(r_1,\ldots,r_n),
$$

若 presentation $P$ 保存：

$$
\gamma,
$$

而 $Q$ 只保存：

$$
F_\gamma(x),
$$

則即使：

$$
P
$$

與：

$$
Q
$$

對終態 query 等價，

它們對 history-sensitive inquiry family：

$$
\mathcal Q_H
$$

仍然可能不等價。

因此：

$$
\boxed{
\mathsf{Fid}(P\mid\mathcal Q_{\mathrm{state}})
\neq
\mathsf{Fid}(P\mid\mathcal Q_{\mathrm{history}}).
}
$$

---

# 19. Presentation Loss

對 inquiry family $\mathcal Q$，定義：

$$
\boxed{
\operatorname{Loss}(P\mid\mathcal Q)
=
\{
q\in\mathcal Q:
q
\text{ cannot be faithfully answered or reconstructed in }P
\}.
}
$$

Loss 不必是 bug。

任何 projection 都可能為了：

- 計算速度；
- 儲存；
- 可讀性；
- 隱私；
- 可證明性；
- 專門化；

故意丟失資訊。

問題不是「有沒有 loss」。

而是：

$$
\boxed{
\text{loss 是否被宣告與追蹤？}
}
$$

---

# 20. Presentation Artifact

Presentation 不只會丟東西。

也可能加入自身產生的 artifact。

例如：

- 座標奇點；
- discretization artifact；
- numerical stiffness；
- gauge redundancy；
- encoding overhead；
- proof-assistant bureaucracy；
- classification boundary。

定義：

$$
\boxed{
\operatorname{Art}(P\mid\mathcal Q)
}
$$

為：

> 在 $P$ 中可觀察，但沒有足夠理由直接升格為 World-level distinction 的 presentation-induced structure。

因此：

$$
\boxed{
\text{visible in presentation}
\not\Rightarrow
\text{ontologically primitive}.
}
$$

---

# 21. Ambiguity

如果同一 presentation expression：

$$
e
$$

可以對應多個不同 semantic interpretations：

$$
m_1,\ldots,m_k,
$$

且目前 context 不能唯一決定，

則：

$$
\boxed{
\operatorname{Amb}_P(e)>0
}
$$

僅作結構記號。

這不要求一定使用數值 ambiguity score。

MWT 允許 ambiguity 保持 explicit。

---

# 22. Identity Specification

Presentation Theory 的核心之一不是「兩個表示是否相等」，而是：

> 哪些差異目前被要求保存？

令：

$$
\boxed{
\mathfrak I
}
$$

為 identity specification。

它可以要求保存：

- exact syntax；
- denotation；
- topology；
- homotopy class；
- path history；
- causal ancestry；
- computational complexity；
- observer role；
- version；
- proof provenance。

因此兩個 expressions：

$$
x,y
$$

可能：

$$
x\equiv_{\mathfrak I_1}y
$$

但：

$$
x\not\equiv_{\mathfrak I_2}y.
$$

這不是矛盾。

因為 identity question 本來就依賴 specification。

---

# 23. Presentation Translation

設：

$$
P,Q
$$

為兩個 presentations。

一個 translation：

$$
\boxed{
T_{PQ}:P\to Q
}
$$

不是只要能「轉格式」就成立。

完整 bridge 至少應聲明它承諾保持哪些項目：

$$
\operatorname{Pres}(T_{PQ})
\subseteq
\{
\text{semantics},
\text{identity},
\text{legality},
\text{proof},
\text{history},
\text{invariants},
\text{cost},
\ldots
\}.
$$

所以 translation 必須帶 contract。

---

# 24. Translation Contract

定義：

$$
\boxed{
\mathcal C(T_{PQ})
=
(
D_{PQ},
R_{PQ},
\mathcal Q_{PQ},
\mathfrak I_{PQ},
\mathsf{Cert}_{PQ}
).
}
$$

其中：

- $D_{PQ}$：source legal domain；
- $R_{PQ}$：target range；
- $\mathcal Q_{PQ}$：承諾保存的 inquiry／invariants；
- $\mathfrak I_{PQ}$：身份規格；
- $\mathsf{Cert}_{PQ}$：驗證證書。

因此 MWT 不承認沒有 contract 的「 universal translator 」宣稱。

---

# 25. Exact Translation

若：

$$
T:P\to Q
$$

對指定：

$$
(\mathcal Q,\mathfrak I)
$$

滿足所有承諾，且無 declared loss：

$$
\operatorname{Loss}
(
T\mid\mathcal Q,\mathfrak I
)
=
\varnothing,
$$

則稱：

$$
T
$$

為相對 exact translation。

注意：

$$
\boxed{
\text{exact relative to }
(\mathcal Q,\mathfrak I)
}
$$

不等於：

$$
\boxed{
\text{absolutely exact for all future mathematics}.
}
$$

---

# 26. Conservative Translation

若 $T:P\to Q$ 將 $P$ 嵌入更強 presentation $Q$，且不產生對 $P$ 語言的虛假新結論，則稱為候選 conservative translation。

概念上：

$$
\boxed{
Q
\text{ can say more, but does not rewrite what }P\text{ already meant}.
}
$$

具體保守性必須依邏輯後端正式定義。

MWT 只提供分類位置。

---

# 27. Lossy Projection

若：

$$
T:P\to Q
$$

有 intentional loss，則標記：

$$
\boxed{
P
\xrightarrow[\mathcal L]{T}
Q.
}
$$

其中：

$$
\mathcal L
$$

是 loss declaration。

這種 translation 完全合法。

例如：

- 高精度場 $\to$ coarse grid；
- full proof trace $\to$ theorem statement；
- full trajectory $\to$ final state；
- multi-dimensional object $\to$ visualization。

禁止的不是 loss。

禁止的是：

$$
\boxed{
\text{lossy translation masquerading as lossless identity}.
}
$$

---

# 28. Refinement

若：

$$
R:P\to Q
$$

增加可合法區分的結構，且存在 projection：

$$
\pi:Q\to P
$$

使：

$$
\pi\circ R
\equiv_P
\operatorname{id}_P,
$$

則可將 $Q$ 視為 $P$ 的 refinement candidate。

但新增加的 distinctions 是否為 World-relevant，仍需驗證。

因此：

$$
\boxed{
\text{more detailed}
\neq
\text{more true}.
}
$$

---

# 29. Coarse-Graining

若：

$$
C:P\to Q
$$

把多個 $P$ -states 合併：

$$
x\neq_P y,
$$

但：

$$
C(x)=C(y),
$$

則 $Q$ 相對 $P$ 為 coarse presentation。

這可以非常有用。

例如統計力學、機器學習表示、宏觀經濟、流體近似都大量使用 coarse-graining。

MWT 只要求：

$$
\boxed{
\text{被商掉的差異要可追蹤}.
}
$$

---

# 30. Presentation Equivalence 不是一種

MWT 至少區分：

### 30.1 Syntactic Equivalence

$$
P\equiv_{\mathrm{syn}}Q.
$$

表示語法結構可逆對應。

### 30.2 Semantic Equivalence

$$
P\equiv_{\mathrm{sem}}Q.
$$

表示指定語義可雙向保存。

### 30.3 Inquiry Equivalence

$$
P\equiv_{\mathcal Q}Q.
$$

表示對 inquiry family $\mathcal Q$ 無法區分。

### 30.4 Identity Equivalence

$$
P\equiv_{\mathfrak I}Q.
$$

表示對 identity specification $\mathfrak I$ 等價。

### 30.5 Computational Equivalence

$$
P\equiv_{\mathrm{comp}}Q
$$

表示在指定 computation class 下具有相同可計算能力或可互相模擬。

### 30.6 World-Relative Compatibility

$$
P\bowtie_{\mathbf W}Q
$$

表示兩者可以同時作為同一 World inquiry 的合法 presentations，而目前沒有發現不可吸收衝突。

這些關係不能混成一個：

$$
P=Q.
$$

---

# 31. Equivalence Lemma

若存在：

$$
T:P\to Q
$$

與：

$$
S:Q\to P
$$

使：

$$
S\circ T
\equiv_{\mathfrak I_P}
\operatorname{id}_P
$$

且：

$$
T\circ S
\equiv_{\mathfrak I_Q}
\operatorname{id}_Q,
$$

則在指定 identity specifications 下：

$$
\boxed{
P
\text{ 與 }
Q
\text{ 具有雙向 presentation equivalence}.
}
$$

但由定義只能推出 presentation-level result。

不能推出：

$$
P=Q=\mathbf W.
$$

---

# 32. World-Addressable Mathematical Object

這裡出現一個重要問題：

> 如果同一「數學對象」在不同 presentation 中長得完全不同，那它的身份在哪？

MWT 不急著把 object 定義成 World 的裸元素。

先定義 **world-addressable mathematical object**。

令：

$$
a
$$

具有多個 presentation realizations：

$$
a_P,
\quad
a_Q,
\quad
a_R.
$$

並存在合法 transports：

$$
T_{PQ}(a_P)\equiv a_Q,
$$

$$
T_{QR}(a_Q)\equiv a_R.
$$

則可以建立一個 presentation bundle：

$$
\boxed{
[a]
=
\{
(P,a_P),
(Q,a_Q),
(R,a_R),
\ldots
\}.
}
$$

其中 identity 由：

$$
\mathfrak I_a
$$

指定。

---

# 33. Object 不等於 bundle 本身

仍需避免另一個陷阱：

$$
a
=
[a].
$$

Presentation bundle 只是目前對 $a$ 的可追蹤 realization family。

所以：

$$
\boxed{
[a]
\text{ is an addressable record of }a,
\text{ not automatically the ontic totality of }a.
}
$$

這與 World primitive 保持一致。

---

# 34. Cross-Presentation Coherence

對：

$$
P,Q,R,
$$

若存在 translations：

$$
T_{PQ},
\quad
T_{QR},
\quad
T_{PR},
$$

理想情況需檢驗：

$$
\boxed{
T_{QR}\circ T_{PQ}
\equiv
T_{PR}.
}
$$

若不成立，定義 translation coherence defect：

$$
\Delta_{PQR}(x)
=
d_R
\left(
T_{QR}T_{PQ}(x),
T_{PR}(x)
\right)
$$

當 target presentation $R$ 提供合法 metric 時。

若沒有 metric，則保留 symbolic defect：

$$
\boxed{
\mathfrak D_{PQR}
=
T_{QR}\circ T_{PQ}
\not\equiv
T_{PR}.
}
$$

---

# 35. Translation 也可能非交換

兩個 translation／refinement operations：

$$
A,
B
$$

可能滿足：

$$
A\circ B
\neq
B\circ A.
$$

例如：

1. 先 coarse-grain 再 normalize；
2. 先 normalize 再 coarse-grain。

結果可能不同。

因此 Presentation Theory 繼承 Series B 的核心精神：

$$
\boxed{
\text{representation history can be first-class information}.
}
$$

MWT runtime 應保存：

$$
\gamma_P
=
(A_1,\ldots,A_n)
$$

而不只是最終 representation。

---

# 36. Presentation Holonomy

若一個 presentation 經歷閉路：

$$
P_0
\xrightarrow{T_1}
P_1
\xrightarrow{T_2}
\cdots
\xrightarrow{T_n}
P_0,
$$

最終資料未恢復：

$$
T_n\cdots T_1(x)
\not\equiv
x,
$$

則存在 presentation holonomy candidate。

寫：

$$
\boxed{
H_P(\gamma)
=
T_n\circ\cdots\circ T_1.
}
$$

若：

$$
H_P(\gamma)
\neq
\operatorname{id},
$$

即使 presentation label 回到原點，內部狀態仍保存轉譯歷史。

這是「回到同一表示不等於回到同一表示狀態」。

---

# 37. Presentation Conflict

設：

$$
P,Q
$$

對同一 inquiry：

$$
q
$$

得到：

$$
P\models \varphi,
$$

$$
Q\models \neg\varphi.
$$

MWT 不立即爆炸。

先問：

1. 是否真的同一 $\varphi$？
2. 是否同一 $\Gamma$？
3. 是否同一 identity specification？
4. 是否存在 translation？
5. translation 是否 faithful？
6. foundations 是否不同？
7. 是否只是 coarse-graining artifact？
8. 是否存在 genuine incompatibility？

因此：

$$
\boxed{
\text{conflict}
\rightarrow
\text{diagnostic branching}
}
$$

而不是：

$$
\text{conflict}
\rightarrow
\text{everything follows}.
$$

---

# 38. Cross-Foundation Coexistence

MWT 不要求所有 mathematics 都先轉成：

$$
\mathrm{ZFC}.
$$

也不要求先轉成：

$$
\mathrm{HoTT}.
$$

更不要求：

$$
\mathrm{Lean}
$$

成為本體。

它允許：

$$
P_{\mathrm{ZFC}},
\quad
P_{\mathrm{HoTT}},
\quad
P_{\mathrm{FOL}},
\quad
P_{\mathrm{HOL}},
\quad
P_{\mathrm{Constructive}},
\quad
P_{\mathrm{DomainSpecific}}
$$

共同存在。

它們之間的 bridge 逐一建立。

所以：

$$
\boxed{
\text{foundation plurality}
+
\text{explicit translation contracts}.
}
$$

---

# 39. 與 Institution Theory 的接口

Goguen 與 Burstall 的 Institution Theory 已經提供一個高度一般化的 logical-system 觀點。

典型 institution 可以寫成：

$$
\boxed{
\mathcal I
=
(
\mathsf{Sign},
\mathsf{Sen},
\mathsf{Mod},
\models
).
}
$$

其中：

- $\mathsf{Sign}$：signatures；
- $\mathsf{Sen}$：sentences；
- $\mathsf{Mod}$：models；
- $\models$：satisfaction。

其重要精神是：可以在不綁死單一 logic 的情況下研究 specification 與 model theory。

MWT 不應重新發明 institution。

相反地：

$$
\boxed{
\text{logical presentation}
\Rightarrow
\text{institution-compatible backend candidate}.
}
$$

MWT 的額外問題是：

- World primitive；
- observer indexing；
- history；
- noncommutativity；
- runtime legality；
- AI orchestration；
- heterogeneous non-logical presentations；
- cross-presentation fidelity。

因此 institution 可以成為 MWT Presentation Theory 的重要後端之一，而不是被取代者。

---

# 40. 與 Univalent Foundations 的接口

Univalent Foundations／HoTT 對 identity 與 equivalence 提供了極深的形式工具。

MWT 不主張：

$$
\text{MWT identity}
=
\text{univalent identity}.
$$

但對某些 presentation：

$$
P_{\mathrm{HoTT}},
$$

完全可以使用 HoTT 作為 identity backend。

MWT 的 Identity Specification：

$$
\mathfrak I
$$

則位於更高一層的 orchestration：

> 目前這個跨 presentation 任務，究竟要保存哪一種身份？

所以 MWT 不取代 univalence。

它決定：

> 何時選擇某種 identity semantics 作為當前 World computation 的合法 presentation。

---

# 41. 與數學多元論的關係

集合論中的 independence 與 multiverse 觀點已顯示：不同模型、不同 universe 或不同額外公理可以形成多種合法數學情況。

MWT 不從此推出：

$$
\boxed{
\text{all mathematical claims are equally true}.
}
$$

MWT 只接受：

$$
\boxed{
\text{truth judgment is indexed by explicit formal context}.
}
$$

因此：

$$
T_1\models\varphi
$$

與：

$$
T_2\models\neg\varphi
$$

可以共同存在於 registry，

只要：

$$
T_1\neq T_2
$$

被保留。

真正禁止的是把 context index 刪掉後再說：

$$
\varphi\land\neg\varphi
$$

無條件成立。

---

# 42. 與 Logical Pluralism 的關係

近期 formalised reasoning 研究再次強調：大型跨領域推理不一定適合被單一 object logic 壟斷，而可以在統一 meta-framework 中支援多種 object logics。

這與 MWT 的方向高度鄰接。

但 MWT 再向外擴一層：

$$
\boxed{
\text{not only many logics, but many mathematical presentations}.
}
$$

其中有些 presentation：

- 甚至不是 logic；
- 可能是 numerical solver；
- simulation；
- geometry engine；
- probabilistic model；
- dynamic state system；
- data structure；
- experimental certificate system。

因此 MWT 的 pluralism 是 runtime-level mathematical heterogeneity。

---

# 43. Global Presentation Graph

令當前 active presentations 為：

$$
\mathcal P_t
=
\{
P_1,\ldots,P_n
\}.
$$

建立 graph：

$$
\boxed{
\mathcal G_t^P
=
(
\mathcal P_t,
\mathcal B_t
).
}
$$

其中：

$$
\mathcal B_t
$$

是 bridge / translation edges。

每一條 edge：

$$
b_{ij}
:
P_i\to P_j
$$

必須攜帶：

$$
\mathcal C(b_{ij}).
$$

這個 graph 是 MWT global computation 的第一個真正 operational substrate。

---

# 44. Global Interaction 不直接作用於 World Primitive

這裡正式修正一種過強說法：

> 「直接計算 World。」

MWT v0.1 更精確的運行方式是：

$$
\boxed{
\text{compute over a dynamically expanding presentation graph of World}.
}
$$

即：

$$
\mathbf W
$$

作為共同指稱，

而實際運算發生在：

$$
\mathcal G_t^P.
$$

AI 可以不斷：

- 新增 presentation；
- 新增 bridge；
- 發現 loss；
- 拆出 refinement；
- 保存 conflict；
- 回退 translation；
- 產生 certificates。

這樣仍然是 World-oriented computation，

但不假裝 AI 已直接握住 World 本身。

---

# 45. Presentation Registry

MWT runtime 第一個必要模組：

$$
\boxed{
\mathsf{PR}
=
\text{Presentation Registry}.
}
$$

每個 presentation entry 至少記錄：

```text
presentation_id
version
type
formal_context
observer_scope
resolution
capabilities
identity_spec
legality_backend
operation_backend
certificate_backend
dependencies
status
```

這不是數學本體。

它是 AI 維護世界計算的工程索引。

---

# 46. Bridge Registry

第二個模組：

$$
\boxed{
\mathsf{BR}
=
\text{Bridge Registry}.
}
$$

每一 bridge：

```text
bridge_id
source_presentation
target_presentation
domain
range
preserved_inquiries
preserved_invariants
declared_loss
identity_contract
legality_contract
certificate
version
```

因此 AI 不會只因：

> 「這兩個看起來很像。」

就直接合併。

---

# 47. Identity Ledger

第三個模組：

$$
\boxed{
\mathsf{IL}
=
\text{Identity Ledger}.
}
$$

它記錄：

- 目前 object address；
- 各 presentation realization；
- identity specifications；
- known equivalences；
- known inequivalences；
- unresolved identity questions；
- merge history；
- split history。

因此「同一個東西」本身也成為可審計資料。

---

# 48. Invariant Ledger

第四個模組：

$$
\boxed{
\mathsf{IVL}
=
\text{Invariant Ledger}.
}
$$

它記錄某個跨 presentation inquiry 中要求保存：

$$
\mathcal Q_{\mathrm{inv}}.
$$

例如：

- cardinality；
- topology；
- homology；
- probability mass；
- causal order；
- energy；
- proof validity；
- complexity class；
- path history。

每一 translation 都要聲明自己保持哪些 invariants。

---

# 49. Legality Engine

第五個模組：

$$
\boxed{
\mathsf{LE}
=
\text{Legality Engine}.
}
$$

輸入：

$$
(
P_i,
o,
x,
P_j,
\Gamma
)
$$

輸出：

$$
\Lambda
\in
\{
\mathsf{Legal},
\mathsf{Illegal},
\mathsf{Undetermined},
\mathsf{Conflicted}
\}.
$$

只有：

$$
\mathsf{Legal}
$$

才直接進 execution queue。

其他狀態進：

- rejection；
- research queue；
- conflict branch；
- human review；
- proof obligation。

---

# 50. Translation Graph

第六個模組是：

$$
\boxed{
\mathsf{TG}.
}
$$

它不是單純 graph database。

因為 edge composition 可能非交換。

對：

$$
P_i
\xrightarrow{A}
P_j
\xrightarrow{B}
P_k,
$$

與另一條：

$$
P_i
\xrightarrow{C}
P_m
\xrightarrow{D}
P_k,
$$

MWT 必須比較：

$$
B\circ A
$$

與：

$$
D\circ C.
$$

因此 translation graph 同時是一個 path-sensitive computation structure。

---

# 51. AI 的第一個 Presentation Algorithm

對 inquiry：

$$
q,
$$

AI 不應直接：

> 找一個最熟悉的數學工具。

而可以執行：

```text
1. register q
2. infer required invariants and identity specification
3. retrieve candidate presentations
4. score expressibility and legality
5. branch over admissible presentations
6. solve / transform locally
7. transport results across bridges
8. compare invariant-preserving results
9. diagnose disagreement
10. converge without deleting unresolved branches
11. emit human-readable projection + certificates
```

這就是 MWT 和普通「工具選擇器」不同的地方。

它不是只選一個 solver。

它允許多個 solver 成為同一 World inquiry 的不同局部 presentations。

---

# 52. Presentation Expansion

若目前 presentations：

$$
P_1,\ldots,P_n
$$

都不足以回答：

$$
q,
$$

則不是立即判定問題不可解。

MWT 可以觸發：

$$
\boxed{
\mathsf E_P.
}
$$

即 presentation expansion：

1. refinement；
2. 新 coordinate；
3. 新 domain；
4. 新 logic；
5. 新 computational representation；
6. 新 observer；
7. 新 scale；
8. 新 bridge；
9. 新 primitive candidate。

因此「建立新數學」本身可以成為 World computation 的一部分。

---

# 53. 但新增 Primitive 必須被限制

任何新概念：

$$
z
$$

不能因「目前沒有地方放」就立即升格為 World primitive。

應依序嘗試：

$$
\boxed{
\text{existing presentation}
\rightarrow
\text{typed refinement}
\rightarrow
\text{new presentation}
\rightarrow
\text{bridge}
\rightarrow
\text{primitive candidate}.
}
$$

只有最後仍不可約，才進 primitive-review queue。

這吸收差合化「不要靠命名吞掉所有新操作」的精神。

---

# 54. Presentation Convergence

多個 presentation 得到結果：

$$
R_1,\ldots,R_n.
$$

MWT 不只做 majority vote。

先建立：

$$
\boxed{
\Omega
=
(
S,
D,
B,
U,
C
).
}
$$

其中：

- $S$：stable shared structure；
- $D$：irreducible differences；
- $B$：remaining branches；
- $U$：unresolved obligations；
- $C$：certificates。

所以：

$$
\boxed{
\text{agreement}
\neq
\text{truth},
}
$$

但：

$$
\boxed{
\text{structured cross-presentation agreement}
}
$$

可以成為公共驗證的重要證據。

---

# 55. 公共數學作為 Presentation Stable Core

令人類與 AI 社群具有：

$$
\mathcal P
=
\{
P_i
\}_{i\in I}.
$$

若某個 structure：

$$
s
$$

在一組重要 translations 下保持：

$$
T_{ij}(s_i)
\equiv
s_j,
$$

且可被多後端重放，

則可以定義候選：

$$
\boxed{
\operatorname{StableCore}(\mathcal P).
}
$$

這提供一個公共數學的新理解：

> 公共數學不是某一套表示永遠正確，而是大量異質表示間形成的高穩定可翻譯核心。

---

# 56. 這也解釋「一般人以為數學是什麼」

學校與公共社會使用的 mathematics 本身就是一組高度穩定 presentations：

- 十進位；
- 代數記號；
- 歐氏幾何直覺；
- 方程求解；
- 函數圖像；
- 最佳化問題；
- 標準概率語言。

這些 presentation 很成功，所以容易被誤認成：

$$
\boxed{
\text{Mathematics itself}.
}
$$

MWT 的觀點則是：

$$
\boxed{
\mathcal M_{\mathrm{public}}
=
\text{a highly stabilized presentation family}.
}
$$

它非常重要，

但不是所有未來數學的邊界。

---

# 57. Example A：同一個數，不同 Presentation

考慮：

$$
\sqrt 2.
$$

它可以被表示為：

### Decimal Approximation

$$
1.41421356\ldots
$$

### Algebraic Number

$$
x^2-2=0,
\qquad
x>0.
$$

### Interval

$$
x\in
[1.4142135,1.4142136].
$$

### Symbolic Expression

$$
\sqrt 2.
$$

這些 presentation 對不同 inquiries 有不同 fidelity。

問：

$$
x^2=2?
$$

代數表示可能極強。

問快速 GPU computation，

float presentation 可能更便宜。

所以：

$$
\boxed{
\text{best presentation}
}
$$

本身依賴 inquiry。

---

# 58. Example B：P vs NP 不是「一個最優解 Presentation」

對：

$$
P\stackrel{?}{=}NP,
$$

可以建立：

- language class presentation；
- machine presentation；
- circuit presentation；
- proof complexity presentation；
- reduction graph presentation；
- empirical algorithm landscape presentation。

這些都可能提供不同信息。

MWT 不要求：

> 先選一個 presentation，其他都只是解釋。

而是允許：

$$
\mathcal P_{P/NP}
=
\{
P_1,\ldots,P_n
\}
$$

共同運行。

如果某個 candidate proof 只在單一 presentation 中成立，

跨 presentation translation 就成為新的 proof obligation。

---

# 59. Example C：State 與 Geometry

一個系統可以同時被表示為：

$$
P_{\mathrm{state}}
$$

與：

$$
P_{\mathrm{geom}}.
$$

state presentation 擅長：

- transition；
- reachability；
- runtime execution。

geometry presentation 擅長：

- neighborhood；
- curvature；
- continuous deformation；
- global shape。

若存在 bridge：

$$
T:
P_{\mathrm{state}}
\to
P_{\mathrm{geom}},
$$

MWT 不要求兩者合併成一個巨大 notation。

只要求：

$$
\boxed{
\text{在需要交互的 inquiry 上建立合法 bridge}.
}
$$

---

# 60. Example D：Observer Difference

觀察者 $O$ 只能看到：

$$
(x,y),
$$

觀察者 $P$ 還能看到：

$$
(x,y,z).
$$

則：

$$
P
\to
O
$$

可能存在自然 coarse-graining：

$$
C(x,y,z)=(x,y).
$$

但：

$$
O\to P
$$

通常不能唯一重建 $z$。

所以：

$$
\boxed{
\text{cross-observer translation can be asymmetric}.
}
$$

這不是誰比較「主觀」。

而是 information accessibility 不對稱。

---

# 61. Example E：同結果、不同歷史

假設：

$$
F_\gamma(x)
=
F_\eta(x)
=
y,
$$

但：

$$
\gamma\neq\eta.
$$

如果 inquiry 只問：

$$
\text{final state}?
$$

兩條 path 可等價。

若 inquiry 問：

$$
\text{causal provenance}?
$$

則不可等價。

所以 identity 與 fidelity 永遠需要 inquiry index。

---

# 62. Presentation Error 的五種類型

MWT 至少區分：

### Type I：Expression Error

expression 本身不 well-formed。

### Type II：Semantic Error

expression 合法，但 interpretation 錯置。

### Type III：Translation Error

兩個 presentation 各自成立，但 bridge 不忠實。

### Type IV：Identity Error

錯把不同對象商成同一，或錯把同一 realization 拆成不同。

### Type V：Ontological Promotion Error

把 presentation-specific structure 無證據升格成 World primitive。

第五種對 MWT 最危險。

---

# 63. World Primitive 的最大風險：空洞化

把 World 設為 primitive 也可能造成另一個問題：

> 「反正都是 World。」

如果所有東西都能被一句 World 吸收，

那麼：

$$
\operatorname{Discrimination}
\to
0.
$$

所以 MWT 不允許 World 成為 explanatory wildcard。

World primitive 的功能只有：

$$
\boxed{
\text{提供共同指稱層}
}
$$

而不是：

$$
\boxed{
\text{替代具體數學解釋}.
}
$$

真正計算仍必須進 presentation。

---

# 64. 因此 World Primitive 是「最薄」的 primitive

MWT 的設計不是讓 $\mathbf W$ 承擔全部語義。

反而應使它盡量薄。

World primitive 至少只承諾：

1. MWT 有一個共同被描述者／共同世界指稱；
2. presentations 對其提供局部或任務化顯影；
3. presentation 不自動獲得本體唯一性；
4. 不同 presentations 可在合法 bridge 下共同運行。

其餘內容盡量由 presentations 承擔。

---

# 65. Versioned Presentation

任何 presentation：

$$
P
$$

都必須帶版本：

$$
P^{(v)}.
$$

因為：

$$
P^{(v)}
\neq
P^{(v+1)}
$$

可能只是：

- bug fix；
- refinement；
- axiom change；
- identity change；
- semantics change。

MWT 不允許只靠相同名稱假設相同意義。

---

# 66. Foundation Revision 與 Presentation Revision 分開

若 presentation implementation 更新：

$$
P^{(v)}
\to
P^{(v+1)},
$$

不一定表示 MWT foundation：

$$
\mathcal A^{(k)}
$$

改變。

反之，若 MWT constitution 改版：

$$
\mathcal A^{(k)}
\to
\mathcal A^{(k+1)},
$$

則所有 presentations 必須重新檢查 compatibility。

這兩種 revision 不能混在一起。

---

# 67. Presentation Provenance

每個 result：

$$
r
$$

至少應可追溯：

$$
\boxed{
\operatorname{Prov}(r)
=
(
P,
v,
\Gamma,
O,
t,
\lambda,
\gamma,
C
).
}
$$

其中：

- $P$：presentation；
- $v$：版本；
- $\Gamma$：context；
- $O$：observer；
- $t$：時間；
- $\lambda$：解析度；
- $\gamma$：操作／翻譯 path；
- $C$：certificate。

因此 AI 不能只回傳：

> result = true

而失去生成世界。

---

# 68. AI-native Presentation Search

當前 AI 的工具選擇通常是：

$$
q
\to
\text{tool}.
$$

MWT 要提升成：

$$
q
\to
\mathcal Q
\to
\mathfrak I
\to
\mathcal P
\to
\mathcal G^P
\to
\text{multi-presentation execution}.
$$

也就是 AI 先辨認：

- 問題要保存什麼；
- 哪些差異不能商掉；
- 哪些 histories 重要；
- 哪些 foundations 合法；
- 哪些 presentations 可參與。

再開始算。

---

# 69. Presentation Economics

不同 presentation 有不同成本：

$$
\kappa(P).
$$

可能包含：

- compute；
- memory；
- communication；
- proof cost；
- translation cost；
- human interpretability cost。

因此 MWT 不會無限展開所有 presentation。

而是在 resource budget：

$$
B_t
$$

下做：

$$
\boxed{
\operatorname{Select}
(
\mathcal P_t
\mid
\mathcal Q,
\mathfrak I,
B_t
).
}
$$

這保留 WT8 中 structure／efficiency 分離的精神。

---

# 70. Global 不等於全部 Presentation 同時啟動

完整 registry 可以有：

$$
10^6
$$

個 presentations。

當前 inquiry 可能只激活：

$$
17.
$$

因此：

$$
\boxed{
\text{global registry}
\neq
\text{global simultaneous activation}.
}
$$

MWT 的 global 是：

> 所有 presentation 原則上可被同一世界治理與橋接，不被固定學科邊界先驗排除。

不是：

> 每次運算把整個數學史全部載入 RAM。

---

# 71. Presentation Locality

一個 presentation 可以只對：

$$
D_P
$$

有效。

例如：

$$
P:
D_P
\rightsquigarrow
M_P.
$$

MWT 不要求：

$$
D_P
=
\mathbf W.
$$

局部 presentation 完全合法。

其責任只是：

$$
\boxed{
\text{declare its domain}.
}
$$

這比假裝 universal 更重要。

---

# 72. Presentation Boundary

如果：

$$
x
$$

離開：

$$
D_P,
$$

則：

$$
P(x)
$$

可能是：

- undefined；
- illegal；
- extrapolative；
- approximate；
- speculative。

這些狀態必須分開。

所以 MWT 需要：

$$
\boxed{
\text{boundary-aware mathematics}.
}
$$

---

# 73. Presentation Overlap

若：

$$
D_P\cap D_Q\neq\varnothing,
$$

則 overlap 是建立 bridge 的第一候選區。

但 overlap 存在不等於 representations 相同。

真正需檢查：

$$
T_{PQ}
$$

在 overlap 上是否保持：

$$
\mathcal Q.
$$

---

# 74. Presentation Atlas

對同一 inquiry region，可有：

$$
\boxed{
\mathfrak A
=
\{
(P_i,D_i,T_{ij})
\}.
}
$$

這可稱為 presentation atlas。

但本文刻意不宣稱：

$$
\mathbf W
$$

是 differentiable manifold。

「atlas」只表示：

> 多個局部 presentations 及其 overlap translations 的組織結構。

---

# 75. Global Glue 不必存在

即使：

$$
P_i
$$

在各局部都合法，

也可能不存在一個單一：

$$
P_G
$$

把所有局部無損合成。

因此：

$$
\boxed{
\text{local compatibility}
\not\Rightarrow
\text{global single presentation}.
}
$$

這與 Series B 的局部—全域阻塞精神相容。

MWT 可以接受：

$$
\boxed{
\text{World computation without a single global chart}.
}
$$

---

# 76. 這正是 MWT 與「統一成一套公式」的差異

傳統統一想像常是：

$$
P_1,\ldots,P_n
\rightarrow
P^\ast.
$$

MWT 允許另一個終局：

$$
\boxed{
\{
P_i,
T_{ij},
\mathfrak I,
\mathcal Q,
H
\}
}
$$

本身就是穩定結構。

也就是：

$$
\boxed{
\text{global coherence}
\neq
\text{single representation}.
}
$$

---

# 77. 三種 Globality

MWT-01 開始區分：

### 77.1 Registry Globality

所有合法 presentation 可被共同索引。

### 77.2 Interaction Globality

跨 presentation 合法作用可進共同 dependency graph。

### 77.3 Representation Globality

存在單一 presentation 覆蓋指定 World inquiry。

第三種最強，也最不應被預設。

因此：

$$
\boxed{
G_{\mathrm{registry}}
\not\Rightarrow
G_{\mathrm{representation}}.
}
$$

---

# 78. 三種 Completeness

同理，至少分：

### Expressive Completeness

指定 inquiry 都能表達。

### Decisional Completeness

指定命題都能決定。

### Reconstructive Completeness

指定 identity 下可完整重建。

所以：

$$
\boxed{
\text{complete}
}
$$

永遠必須帶下標。

---

# 79. Presentation Theory 的第一個反唯一本體規則

若有人提出：

$$
P^\ast
$$

並宣稱：

> $P^\ast$ 是唯一真正數學表示。

MWT 的回答不是「不可能」。

而是要求提供：

1. domain；
2. inquiry family；
3. identity specification；
4. completeness theorem；
5. translation from alternatives；
6. preserved invariants；
7. loss analysis；
8. observer independence；
9. future refinement boundary。

在完成前，只能標為：

$$
\boxed{
\text{Universal-Presentation Candidate}.
}
$$

---

# 80. Presentation Theory 的第一個反相對主義規則

相反地，也不能說：

> 每個表示都只是觀點，所以全部一樣。

MWT 明確拒絕。

因為 presentation 可以：

- 不 well-formed；
- 語義錯誤；
- translation 失真；
- 破壞 invariant；
- 製造 artifact；
- 越界使用；
- falsified by data；
- logically inconsistent within declared foundation。

所以：

$$
\boxed{
\text{plurality}
\neq
\text{equal validity}.
}
$$

---

# 81. Validity 是分域的

Presentation validity 應寫成：

$$
\boxed{
\operatorname{Valid}
(
P
\mid
D,\Gamma,\mathcal Q,\mathfrak I
).
}
$$

而不是：

$$
\operatorname{Valid}(P)
$$

的無條件形上學標籤。

這使 MWT 能同時容納：

- Newtonian approximation；
- relativistic model；
- quantum model；

而不說三者「全部一樣真」。

它們在不同 domain 有不同 validity。

---

# 82. Presentation 與資料

對 empirical presentation：

$$
P_E,
$$

還必須加入：

$$
\mathcal D
$$

資料來源與 measurement contract。

所以：

$$
\mathsf{Sem}_{P_E}
$$

不能只靠形式 self-consistency。

它還需要：

$$
\boxed{
\text{model-data interface}.
}
$$

MWT 因此不是純形式主義。

---

# 83. Presentation 與證明

對 proof presentation：

$$
P_{\mathrm{proof}},
$$

需要：

$$
\mathsf{Cert}
$$

可重放。

若 theorem：

$$
\varphi
$$

只在自然語言存在，

可以標：

$$
\mathsf{HumanProof}.
$$

若已形式化：

$$
\mathsf{FormalProof}_{F}.
$$

若多後端重放：

$$
\mathsf{CrossPresentationProof}.
$$

這些是不同證明成熟度。

---

# 84. Presentation 與計算

數值結果：

$$
r
$$

必須攜帶：

- precision；
- error semantics；
- algorithm；
- data type；
- hardware assumptions；
- rounding；
- certificate。

所以同一顯示：

$$
1.41421356
$$

不代表同一 presentation。

---

# 85. Presentation 與 Simulation

Simulation 不是 World。

但 simulation 可以成為：

$$
P_{\mathrm{sim}}.
$$

若其 update rule：

$$
S_{t+1}
=
F(S_t)
$$

有效，

可用來回答指定 dynamical inquiries。

但 simulation artifact 不能直接升格成 World law。

---

# 86. Presentation 與 Generative AI

LLM output 也可以被視為：

$$
P_{\mathrm{LLM}}.
$$

但它通常不是高保證 formal backend。

因此其 capability profile 可能包含：

- hypothesis generation；
- translation proposal；
- bridge suggestion；
- semantic paraphrase；

但不自動包含：

$$
\boxed{
\text{proof certificate}.
}
$$

只有接上 verifier 後才能提升相應 maturity。

---

# 87. AI 不應成為新的「唯一觀察者」

MWT 是 AI-native，

但不表示：

$$
\boxed{
\text{AI output}
=
\text{World}.
}
$$

AI 也只操作 presentations。

而且不同 AI：

$$
A_1,\ldots,A_n
$$

可以具有不同：

- training；
- memory；
- tools；
- context；
- representations。

所以 AI 也需要 observer index。

---

# 88. Multi-AI Presentation Network

多 AI 系統可以維護：

$$
\mathcal P^{A_1},
\ldots,
\mathcal P^{A_n}.
$$

再建立：

$$
F_{A_iA_j}
$$

作跨 AI translation。

此時：

$$
\boxed{
\text{multi-AI agreement}
}
$$

只有在：

- independence；
- translation；
- certificate；
- shared-data bias；

被檢查後才有高證據價值。

單純多數輸出相同不等於真。

---

# 89. Presentation Diversity 是資產，也是風險

多 presentation 可以降低：

$$
\text{single representation blind spot}.
$$

但也可能增加：

- translation bugs；
- version drift；
- shared hidden assumptions；
- ontology mismatch；
- computational explosion。

所以 MWT 需要 diversity governance。

---

# 90. Diversity Governance

令：

$$
\mathcal P_t
$$

為候選 presentation pool。

AI 不只最大化數量。

而要考慮：

$$
\boxed{
\text{coverage}
+
\text{independence}
+
\text{bridge quality}
+
\text{cost}
+
\text{auditability}.
}
$$

這比單純「AI 海」更接近可驗證多模型研究。

---

# 91. Presentation Maturity Levels

v0.1 建議：

### P0 — Informal

自然語言構想。

### P1 — Structured

定義、域與核心關係已明示。

### P2 — Executable

可以計算／模擬。

### P3 — Certifiable

關鍵操作具有可檢查證書。

### P4 — Cross-Presentation

存在至少一個獨立 presentation bridge。

### P5 — Stable Core Candidate

跨多後端、版本與觀察者仍保持指定 invariants。

這不是價值排名。

而是 engineering maturity。

---

# 92. MWT-01 的 Minimal Constitution

本篇暫時固定十二條：

### C1 — World Primitive

$$
\mathbf W
$$

不被預先定義為任一單一既有數學對象。

### C2 — Presentation Distinction

$$
P
\neq
\mathbf W
$$

除非另有證明責任完成。

### C3 — Context Indexing

所有有效 presentation 都應攜帶必要 context。

### C4 — Domain Declaration

presentation 必須聲明適用域。

### C5 — Identity Declaration

跨 presentation 等價必須聲明 identity specification。

### C6 — Translation Contract

bridge 必須聲明保持項與 loss。

### C7 — Legality Preservation

合法性不能在 translation 中被默默丟失。

### C8 — History Preservation When Required

非交換／歷史敏感 inquiry 不得只保留終態。

### C9 — Plurality Without Relativism

允許多 presentation，不等於所有 presentation 同等有效。

### C10 — Global Coherence Without Single Representation

全域一致性不要求單一 global chart。

### C11 — Finite Runtime, Open Refinement

任何 active registry 有限，但 presentation types 不預先封閉。

### C12 — Explicit Revision

presentation 與 foundation revision 必須版本化、可審計。

---

# 93. 可由定義直接得到的命題

## 命題 93.1

若：

$$
P\equiv_{\mathcal Q}Q
$$

則只能推出：

$$
P,Q
$$

在 $\mathcal Q$ 下不可區分。

不能推出：

$$
P=Q.
$$

更不能推出：

$$
P=\mathbf W.
$$

**理由：** $\equiv_{\mathcal Q}$ 的定義域只覆蓋 $\mathcal Q$。

---

## 命題 93.2

若 coarse-graining：

$$
C:P\to Q
$$

非單射，

則不存在 ordinary inverse：

$$
C^{-1}:Q\to P
$$

使所有 $P$ -states 唯一恢復。

**理由：** 非單射映射至少存在兩個不同輸入具有相同輸出。

---

## 命題 93.3

若：

$$
T:P\to Q
$$

與：

$$
S:Q\to P
$$

在 $\mathfrak I$ 下互為逆，

則：

$$
P,Q
$$

在該 identity specification 下具有雙向等價。

但 identity specification 改變後需重新判定。

---

## 命題 93.4

若 inquiry 僅依賴 final state，

兩條不同 history：

$$
\gamma\neq\eta
$$

且：

$$
F_\gamma(x)=F_\eta(x)
$$

可在該 inquiry 下等價。

若 inquiry 包含 provenance，

則不能由終態相同推出 history equivalence。

---

# 94. 研究猜想

以下不是定理。

## Conjecture 94.1 — Stable Cross-Presentation Core

對部分成熟數學領域，存在一族異質 presentations：

$$
\mathcal P
$$

與 inquiry family：

$$
\mathcal Q
$$

使得：

$$
\operatorname{StableCore}
(
\mathcal P
\mid
\mathcal Q
)
$$

能以可計算方式被抽取，並比任何單一 presentation 對 implementation error 更具韌性。

---

## Conjecture 94.2 — Presentation Diversity Benefit

在固定資源範圍內，適度增加 representation independence 可能降低 shared-blind-spot risk。

但：

$$
\text{benefit}
$$

不是單調隨 presentation count 增加。

---

## Conjecture 94.3 — AI-Native Global Mathematics

當 AI 能維護足夠大的 presentation registry、bridge graph 與 certificate ledger 時，某些目前必須由人類預先切成多個局部問題的研究，可以改寫為先全域登錄、再由 legality 與 resource scheduling 動態誘導 locality。

---

# 95. 開放問題

### O1

是否能為 presentation fidelity 建立一個不依賴單一 scalar score 的通用 partial order？

### O2

跨不同 foundation 的 identity specification 如何機器可判？

### O3

何時存在 finite complete bridge family？

### O4

presentation holonomy 能否在實際數學軟體中檢測？

### O5

如何區分 genuine World-relevant refinement 與 mere representational artifact？

### O6

是否存在某些 inquiry class，單一 presentation 確實可證 complete？

### O7

如何控制 presentation graph 的 combinatorial explosion？

### O8

如何建立 AI 可維護但人類可審計的 presentation provenance？

---

# 96. 第一代實作資料結構

可以先定義：

```text
WorldRef:
  world_id

Presentation:
  presentation_id
  version
  type
  domain
  context
  observer_scope
  resolution
  capabilities
  identity_spec
  semantics_backend
  legality_backend
  operation_backend
  certificate_backend
  dependencies

Bridge:
  bridge_id
  source
  target
  source_domain
  target_range
  preserved_inquiries
  preserved_invariants
  declared_loss
  identity_contract
  legality_contract
  certificate
  version

Result:
  result_id
  inquiry_id
  presentation_id
  provenance_path
  certificate
  status
```

注意：

$$
\texttt{WorldRef}
$$

不是 World 的資料結構。

只是 runtime 中對共同指稱的 handle。

---

# 97. 第一代 Execution Loop

```text
INPUT inquiry q

1. define q-context
2. infer identity specification
3. infer required invariants
4. query Presentation Registry
5. generate candidate presentation set
6. legality-check candidates
7. allocate resource budget
8. execute independent branches
9. translate results through certified bridges
10. compare preserved invariants
11. detect coherence defects
12. retain conflicts and unresolved branches
13. converge to stable-core report
14. emit human projection
15. preserve full provenance
```

這個 loop 本身就是 MWT-01 的最小工程落點。

---

# 98. 與既有 EveMissLab 理論的重新分工

MWT-01 暫時將既有主線重新定位如下。

### 編織論 8.0

提供：

- 跨層關係；
- 結構／效率分離；
- 多範式投影；
- AI-oriented global modeling 精神。

但：

$$
\text{WT8}
\neq
\mathbf W.
$$

### ERFI 運作束

可成為一個高通用 presentation family。

但：

$$
\text{ERFI}
\neq
\text{終極 World 定義}.
$$

### 異質空間／全域幾何

提供：

- heterogeneous local structures；
- global coupling；
- gap；
- boundary；
- geometry bridges。

### RDSS

提供：

- state；
- container；
- process；
- finite active support；
- open dimension。

### 差合化

提供高階 transformation grammar：

$$
\Delta,
\mathcal U,
\nabla.
$$

但它是一種 operator presentation，不是 World totality。

### 分域算子本體論

提供：

- operatorhood；
- applicability；
- executability；
- realization；

的合法作用區分。

### 同一性微積分

提供 identity／presentation slicing 的候選 calculus。

### NTLA-O

提供 observer、resolution、transport、identity、topology 的成熟接口。

### Series B

提供：

- noncommutative order；
- local-to-global obstruction；
- embedded observers；
- transport；
- holonomy；
- covariance。

MWT 不把這些吃掉。

MWT 給它們共同運行的 World-level registry。

---

# 99. 與外部理論的邊界

MWT-01 不宣稱：

- 發明 institution；
- 發明 logical pluralism；
- 發明 model translation；
- 發明 coarse-graining；
- 發明 category-theoretic transport；
- 發明 HoTT identity；
- 發明 mathematical multiverse；
- 發明 heterogeneous formal methods。

MWT 候選貢獻是：

$$
\boxed{
\begin{aligned}
&\text{World primitive}\\
+&\text{presentation non-exhaustion}\\
+&\text{observer-indexed presentations}\\
+&\text{legality-first bridges}\\
+&\text{history-sensitive translation}\\
+&\text{cross-presentation fidelity}\\
+&\text{AI runtime registry}\\
+&\text{global coherence without single representation}.
\end{aligned}
}
$$

---

# 100. MWT-01 的核心結論

本文把：

$$
\boxed{
\mathbf W
}
$$

與：

$$
\boxed{
P
}
$$

正式分離。

世界不是 presentation。

presentation 不是幻覺。

它是可操作數學真正發生的地方。

所以 MWT 的立場不是：

$$
\boxed{
\text{representation is unreal}.
}
$$

而是：

$$
\boxed{
\text{representation is operationally real,
but ontologically non-exclusive}.
}
$$

我們可以極度認真地計算：

$$
P.
$$

同時保持：

$$
P
\neq
\mathbf W.
$$

這兩句完全可以同時成立。

---

# 101. 從「哪套數學是真的」改問「哪套表示對什麼問題忠實」

MWT-01 因此將問題從：

> 哪一套數學是真正的數學？

重寫為：

> 對指定 World inquiry，我們目前有哪些合法 presentations？它們各自保存什麼、丟失什麼、引入什麼 artifact、彼此如何翻譯、哪些 invariants 穩定、哪些差異不可消去？

這是一個完全不同的研究入口。

---

# 102. AI 時代的 Presentation Explosion

人類時代需要控制 presentation 數量。

因為每一套數學語言都有：

- 學習成本；
- 記憶成本；
- 文獻成本；
- 翻譯成本。

AI 時代第一次可能允許：

$$
|\mathcal P|
\uparrow
$$

而仍維持：

- registry；
- translation；
- provenance；
- certificate。

這可能使數學不再必須把「語言統一」當成降低人類認知負擔的主要手段。

---

# 103. 但 AI 時代仍然需要壓縮

MWT 不主張：

$$
\text{more presentations}
=
\text{always better}.
$$

如果：

$$
P_1,\ldots,P_{10000}
$$

實際上全部是同一 representation 的 superficial variants，

則只增加成本。

所以 AI 必須執行：

$$
\boxed{
\text{presentation deduplication}
}
$$

與：

$$
\boxed{
\text{structural novelty detection}.
}
$$

---

# 104. Presentation Novelty

新 presentation：

$$
P_{\mathrm{new}}
$$

至少可以問：

1. 是否增加 expressibility？
2. 是否增加 distinguishability？
3. 是否降低 computation cost？
4. 是否新增 certificate capability？
5. 是否提供 independent semantics？
6. 是否只是 notation change？

如果只有第六項，

則：

$$
P_{\mathrm{new}}
$$

未必值得成為獨立 world node。

---

# 105. Human Interface

人類不需要看到：

$$
\mathcal G_t^P
$$

全部細節。

可以要求：

$$
\pi_H:
\mathcal G_t^P
\to
\widetilde{\mathcal G}_{H,t}.
$$

人類看到：

- 問題目前有哪些主要 presentations；
- 哪些結果一致；
- 哪些衝突；
- 哪些 bridge 有 loss；
- 哪些證明責任未完成；
- 哪些 branch 需要決策。

這就是 AI-operationally native／human-understandable 的第一個具體 UI 原則。

---

# 106. 不要把 Human Projection 再誤認成 World

即使 AI 有一個更大 runtime，

人類 dashboard：

$$
\widetilde{\mathcal G}_{H,t}
$$

仍然只是 presentation of presentation-world state。

所以：

$$
\boxed{
\text{rendering view}
\neq
\text{canonical source}
}
$$

這一點也應延伸到 MWT 工程：

正式 mathematical state 必須保存在可驗證 source artifact 中，而不是只存在 UI 渲染畫面。

---

# 107. Canonical Source Principle

任何 MWT formal artifact 都應具備：

- UTF-8 source；
- version；
- deterministic delimiter rules；
- validation；
- hash；
- dependency record；
- machine-readable metadata。

因此 MWT 本身的書寫方式也必須服從其 provenance 原則。

---

# 108. MWT-01 暫時封頂的位置

MWT-01 到此不繼續定義：

- World dynamics；
- global scheduler；
- universal legality calculus；
- world-state runtime；
- global convergence theorem。

因為那些屬於後續分論文。

本文只完成第一件事：

$$
\boxed{
\text{World}
\quad\text{與}\quad
\text{Presentation}
}
$$

的正式切分。

這是後面所有全域計算成立的前提。

---

# 109. 下一篇接口

下一篇最自然的方向是：

# **MWT-02：Global Legality Calculus**

處理：

$$
\boxed{
\text{兩個合法 presentations 中的對象，
何時可以跨表示真正作用？}
}
$$

以及：

$$
\Lambda:
(
P_i,x,o,P_j,y,\Gamma
)
\to
\{
\mathsf{Legal},
\mathsf{Illegal},
\mathsf{Undetermined},
\mathsf{Conflicted}
\}.
$$

MWT-01 建立「有哪些世界表示」。

MWT-02 才開始回答：

> 它們如何在同一數學世界裡合法互動？

---

# 110. 一句話版

> **MWT-01 將 World 保留為不可由單一數學語言預先耗盡的 primitive，並把所有可操作數學重新定位為帶 context、observer、identity、legality、history 與 certificate 的 presentations；不同 presentations 可以共同存在、互相翻譯、精細化、粗粒化、衝突與形成穩定核心，而不必被壓成單一表示。AI 的任務不是宣稱握住 World，而是維護一個持續擴張、可追溯、可驗證的 presentation graph，讓全域數學計算得以在其中發生。**

---

# 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $\mathbf W$ | World primitive |
| $P,Q,R$ | presentations |
| $\rho_\alpha$ | presentation protocol |
| $\mathbf W\xRightarrow{\rho_\alpha}M_\alpha$ | presentation judgment |
| $\Gamma$ | context |
| $O,P$ | observers（上下文可區分於 presentation $P$ ） |
| $t$ | time / version / history index |
| $\lambda$ | resolution |
| $\mathbb P$ | minimal presentation interface |
| $\mathsf{Expr}$ | expression surface |
| $\mathsf{Sem}$ | semantic interface |
| $\mathsf{Id}$ | identity specification backend |
| $\mathsf{Leg}$ | legality backend |
| $\mathsf{Op}$ | operation interface |
| $\mathsf{Cert}$ | certificate interface |
| $\mathcal Q$ | inquiry / invariant family |
| $\mathsf{Fid}(P\mid\mathcal Q)$ | inquiry-relative fidelity profile |
| $\operatorname{Loss}$ | declared loss |
| $\operatorname{Art}$ | presentation artifact |
| $\mathfrak I$ | identity specification |
| $T_{PQ}$ | translation / bridge |
| $\mathcal C(T_{PQ})$ | translation contract |
| $\mathcal G_t^P$ | active presentation graph |
| $\mathsf{PR}$ | Presentation Registry |
| $\mathsf{BR}$ | Bridge Registry |
| $\mathsf{IL}$ | Identity Ledger |
| $\mathsf{IVL}$ | Invariant Ledger |
| $\mathsf{LE}$ | Legality Engine |
| $\mathsf{TG}$ | Translation Graph |

---

# 附錄 B：v0.1 非主張清單

MWT-01 v0.1 不主張：

1. World 已被形式化完成；
2. World 是集合；
3. World 不是集合；
4. World 是類；
5. World 不是類；
6. 存在已知終極 metric $d(P,\mathbf W)$ ；
7. 所有 presentations 都不完備；
8. 不存在全域完備 presentation；
9. 所有 foundations 等價；
10. 所有 logics 都同等有效；
11. 所有 translation 都能機器化；
12. 所有 presentation conflicts 都能解決；
13. 所有局部 presentations 都能黏成單一 global presentation；
14. MWT 已提供一個新的 foundation of mathematics；
15. MWT 取代 Institution Theory 或 HoTT；
16. AI 已能維護實際無限 presentation graph；
17. 人類不能理解任何 MWT computation；
18. representation plurality 表示真理不存在。

---

# 附錄 C：與外部研究的最低文獻接口

1. Joseph A. Goguen and Rod M. Burstall, **Institutions: Abstract Model Theory for Specification and Programming**, *Journal of the ACM*, 39(1), 1992, pp. 95–146. DOI: 10.1145/147508.147524.  
2. The Univalent Foundations Program, **Homotopy Type Theory: Univalent Foundations of Mathematics**, Institute for Advanced Study, 2013.  
3. Jonas Reitz, **From Geometry to Geology: An Invitation to Mathematical Pluralism through the Phenomenon of Independence**, 2016, arXiv:1609.00093.  
4. Christoph Benzmüller, Daniel Kirchner, Luca Pasetto, **Many Logics, One Methodology: A Plea for Logical Pluralism in Formalised Reasoning**, 2026, arXiv:2605.27246.  
5. Marie Farrell, Rosemary Monahan, James F. Power, **Building Specifications in the Event-B Institution**, 2021, arXiv:2103.10881.  
6. Yuichi Nishiwaki, Yoshihiko Kakutani, Yuito Murase, **Modality via Iterated Enrichment**, 2018, arXiv:1804.02809.

---

# 附錄 D：內部依賴主線

MWT-01 目前主要吸收下列 EveMissLab 內部理論的精神與接口：

- 《編織論（Weaving Theory, WT）完整版 v8.0》
- 《ERFI 運作束的本體論降階與數學保留》
- 《狀態、容器與存在：遞歸動態狀態系統的總命題》
- 《差合化的保真擴張》
- 《分域算子本體論：從萬物皆算子到合法作用》
- 《同一性微積分：拓樸微積分的本體論基礎》
- 《NTLA-O：廣義嵌套拓樸觀察者論》
- Series B《觀察者、局部關係、非交換與全域守恆》

本文不將上述任一理論提升為 $\mathbf W$ 本身。

它們被重新視為 MWT Presentation Graph 中具有不同能力與邊界的高價值 presentations／meta-presentations／operator interfaces。

