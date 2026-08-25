# MWT-02：Global Legality Calculus
## 跨 Presentation 合法作用、四態判定、約束合成、非交換排程與證書化執行

**英文題名：** *MWT-02: Global Legality Calculus — Cross-Presentation Admissibility, Four-State Judgments, Constraint Composition, Noncommutative Scheduling, and Certified Execution*  
**系列：** Mathematical World Theory（MWT）  
**篇次：** 02  
**文件編號：** EML-MWT-02-2026-v0.1  
**作者：** Neo.K  
**協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-18  
**版本：** v0.1  
**文件性質：** 數學世界論第二篇形式母稿／Global Legality Calculus／AI-native mathematical runtime foundation  
**前置文件：** 《MWT-01：World Primitive 與 Presentation Theory》  
**狀態：** 可使用研究稿；尚非完備決定程序；不宣稱所有合法性問題皆可判定  

---

## 摘要

MWT-01 建立了 World primitive 與 Presentation Theory，將可操作數學重新定位為帶有 context、observer、identity、history、semantics 與 certificate 的 presentations，並以動態 presentation graph 作為 AI-native 全域數學運行的第一層 substrate。由此立即產生下一個無法迴避的問題：

> **當多個合法 presentations 被放入同一數學世界後，什麼條件下它們之中的對象、算子、證明、資料與狀態有資格彼此作用？**

若只因兩個節點都存在於 registry 就允許交互，MWT 將退化成「萬物可以任意互算」的完全圖；若只允許同一 presentation 內部運算，MWT 又退回傳統局部數學，失去全域跨表示交互的核心目標。

本文提出 **Global Legality Calculus（GLC）**，將「合法」從單一布林標籤提升為一組可版本化、可證書化、可分層、可合成、可衝突且可保留未知的判定結構。對一個候選交互 episode：

$$
\alpha
=
\left\langle
o;
(P_1,x_1,b_1),
\ldots,
(P_k,x_k,b_k);
P_o;
\Gamma;
h
\right\rangle,
$$

其中 $o$ 是在 native presentation $P_o$ 中定義的作用， $x_i$ 來自不同 presentations $P_i$， $b_i$ 是必要的跨 presentation bridge， $\Gamma$ 是形式與運行 context， $h$ 是歷史／先後資訊。GLC 不直接問「要不要算」，而先形成 judgment：

$$
\boxed{
\Gamma
\vdash
\alpha
\Downarrow_{\Lambda}
\ell.
}
$$

其中：

$$
\boxed{
\ell
\in
\mathbb L
=
\{
\mathsf{Legal},
\mathsf{Illegal},
\mathsf{Undetermined},
\mathsf{Conflicted}
\}.
}
$$

本文強調：這四態首先是 **legality evidence states**，不是命題真值。為每個判定保留兩個證據方向：

$$
\nu_{\Lambda}(\alpha)
=
(s_{\alpha},r_{\alpha})
\in
\{0,1\}^2,
$$

其中 $s_{\alpha}$ 表示是否已形成足夠的允許證書鏈， $r_{\alpha}$ 表示是否存在有效阻斷證書。由此：

$$
\mathsf{Legal}=(1,0),
$$

$$
\mathsf{Illegal}=(0,1),
$$

$$
\mathsf{Conflicted}=(1,1),
$$

$$
\mathsf{Undetermined}=(0,0).
$$

此結構吸收四態／相容矛盾推理的非爆炸精神，但不把 Belnap-Dunn/FDE 直接等同於 MWT 的合法性語義。MWT 的 `Conflicted` 只表示「允許鏈與阻斷鏈同時存在且皆未被合法消解」，不是宣稱某個數學命題本體上同時真與假。

GLC 將一個 candidate interaction 拆成一族可配置的 hard gates，包括：

- well-formedness；
- presentation/version validity；
- source-domain membership；
- bridge validity；
- type compatibility；
- identity compatibility；
- semantic compatibility；
- context admissibility；
- constraint satisfiability；
- invariant preservation；
- history/order admissibility；
- observer/governance permission；
- resource admissibility；
- certificate availability；
- realizability。

其中 hard constraints 不允許用其他高分補償。本文因此延續 X 約束算子論的核心區分：

$$
\boxed{
\text{算子合法性}
\neq
\text{合成合法性}
\neq
\text{共同約束可滿足性}.
}
$$

甚至再增加：

$$
\boxed{
\text{可作用性}
\neq
\text{可執行性}
\neq
\text{已實現性}
\neq
\text{結果真實性}.
}
$$

一個 interaction 可以在形式上合法執行，但其輸出命題仍然可能是假的；合法性只表示「依目前明示規則有資格執行／推導／轉譯」，不等於結果自動具有 World-level 真實性。

本文進一步處理非交換排程。若兩個操作：

$$
A\circ B
\neq
B\circ A,
$$

則不能把「都合法」簡化成「可任意平行執行」。GLC 將 legality 擴張到 path：

$$
\Gamma
\vdash
\gamma
\Downarrow_{\Lambda}
\ell_{\gamma},
$$

並要求每一步在前一步更新後的 state/context 上重新判定。因此：

$$
\mathsf{Legal}(A)
\land
\mathsf{Legal}(B)
$$

不推出：

$$
\mathsf{Legal}(A\circ B)
$$

或：

$$
\mathsf{Legal}(B\circ A).
$$

本文由此建立 strict、exploratory 與 simulation 三種 runtime mode。Strict mode 只有 $\mathsf{Legal}$ 可 commit； $\mathsf{Undetermined}$ 與 $\mathsf{Conflicted}$ 可進 sandbox、研究或人工複核，但不得偽裝成正式合法結果； $\mathsf{Illegal}$ 預設拒絕，除非經顯式 theory revision 或 exception rule 產生新版本規則。

最後，本文提出 Legality Engine、Gate Registry、Constraint Registry、Certificate Ledger、Conflict Ledger、History Ledger、Execution Queue 與 Commit/Rollback Layer 等最低運行模組，並提供一個可執行 reference evaluator。GLC 的目標不是成為能判定一切數學活動的全知 oracle，而是建立一個**可以明確說「不知道」「衝突」「不允許」的全域數學控制平面**。正因為它拒絕強迫所有 candidate interaction 得到二值答案，MWT 才能在 AI/AGI 時代安全地進行大規模異質、非交換、跨基礎與跨觀察者計算。

**關鍵詞：** Mathematical World Theory、Global Legality Calculus、合法作用、四態判定、partial operators、constraint composition、refinement types、effect systems、paraconsistency、noncommutativity、certificate、AI-native mathematics、global scheduler

---

# 0. 本文的責任：MWT 不能只會「把東西放進世界」

MWT-01 解決：

$$
\boxed{
\text{World}
\quad\text{與}\quad
\text{Presentation}
}
$$

的分離。

但如果下一步只做：

$$
\mathcal P_t
=
\{
P_1,\ldots,P_n
\}
$$

然後宣稱：

> 既然它們都在 World Registry 裡，就讓它們全部互相作用。

那麼 MWT 會立即崩潰。

因為：

- 一個微分算子未必能作用於任意 graph；
- 一個群作用未必對任意 object 有定義；
- 一個 proof term 未必能送入 numerical solver；
- 一個 probability distribution 未必具有另一個 presentation 所要求的 identity semantics；
- 一個 coarse-grained state 未必能恢復被操作需要的 microscopic degree of freedom；
- 一個 bridge 可以存在，但只在真子域上合法；
- 一個 action 今天合法，執行第一步後第二步可能不再合法；
- 一個局部 contradiction 不應授權全世界所有結論。

因此 MWT 必須有第二層：

$$
\boxed{
\text{Legality before interaction}.
}
$$

本文建立的就是這一層。

---

# 1. 「合法」不是法律詞，而是 admissibility

本文中的「合法」首先不是：

- 合法律；
- 合倫理；
- 合政策；
- 合社會規範。

它的最低數學意義是：

> **在一組已明示的 domain、type、identity、semantics、constraint、history、permission 與 certificate 規則下，一個候選構造、作用、合成、翻譯或執行是否具有被接受進下一層運行的資格。**

英文核心詞採：

$$
\boxed{
\text{admissibility}
}
$$

與：

$$
\boxed{
\text{legality}
}
$$

交替使用。

若某個應用真的涉及法律、倫理、權限或治理，這些只是 legality gates 的特定類型，而不是本文全部含義。

---

# 2. 從作用對象改成 Interaction Episode

如果只寫：

$$
o(x),
$$

資訊太少。

因為 MWT 必須知道：

- $x$ 來自哪個 presentation；
- $o$ 的 native presentation 是什麼；
- 是否需要 bridge；
- bridge 哪一版；
- identity contract 是什麼；
- context 是什麼；
- 之前發生過什麼；
- resource budget 是什麼；
- 哪個 observer / agent 在執行。

因此定義 interaction episode：

$$
\boxed{
\alpha
=
\left\langle
o;
\mathbf I;
P_o;
\Gamma;
h
\right\rangle.
}
$$

其中：

$$
\mathbf I
=
\left(
(P_1,x_1,b_1),
\ldots,
(P_k,x_k,b_k)
\right).
$$

---

# 3. Native Presentation 與 Partiality

每個 operator：

$$
o
$$

至少在某個 presentation：

$$
P_o
$$

中具有 native meaning。

寫：

$$
\boxed{
o
:
D_o
\rightharpoonup
C_o.
}
$$

使用 partial arrow 表示：

> $o$ 不必對所有可能輸入有定義。

MWT-02 正式保留：

$$
\boxed{
\operatorname{Operatorhood}(o)
\not\Rightarrow
\forall x,\ o(x)\downarrow.
}
$$

這也是本文與「既然都在同一世界就都能相互作用」之間最重要的第一道牆。

---

# 4. Cross-Presentation Input

若：

$$
x_i
$$

已經位於：

$$
P_o,
$$

可以有：

$$
b_i
=
\operatorname{id}.
$$

若：

$$
x_i
\in P_i,
\qquad
P_i\neq P_o,
$$

則需要 bridge：

$$
\boxed{
b_i:
P_i
\to
P_o.
}
$$

但 bridge existence 仍然不夠。

還要判定：

$$
x_i
\in
\operatorname{Dom}(b_i)
$$

以及：

$$
b_i(x_i)
\in
D_o.
$$

所以：

$$
\boxed{
\text{可以翻譯}
\neq
\text{翻譯後可以作用}.
}
$$

---

# 5. Global Legality Judgment

MWT-02 的基本 judgment：

$$
\boxed{
\Gamma
\vdash
\alpha
\Downarrow_{\Lambda}
\ell.
}
$$

其中：

- $\Gamma$：完整 legality context；
- $\alpha$：candidate interaction；
- $\Lambda$：當前 legality ruleset；
- $\ell$：合法性狀態。

注意：

$$
\Lambda
$$

不等於單一 total function。

它可以包含：

- decidable rules；
- theorem prover；
- type checker；
- constraint solver；
- external evidence verifier；
- bounded search；
- human decision；
- versioned policy。

所以此式是一個 judgment interface，而不是宣稱已擁有 universal decision procedure。

---

# 6. 四態合法性狀態

定義：

$$
\boxed{
\mathbb L
=
\{
\mathsf{Legal},
\mathsf{Illegal},
\mathsf{Undetermined},
\mathsf{Conflicted}
\}.
}
$$

## 6.1 Legal

$$
\boxed{
\mathsf{Legal}
}
$$

表示：

> 對當前 run 所要求的全部 hard gates，已形成足夠的正向合法性證書，且目前沒有有效 blocking certificate。

它不是：

$$
\boxed{
\text{結果必然為真}.
}
$$

## 6.2 Illegal

$$
\boxed{
\mathsf{Illegal}
}
$$

表示：

> 至少存在一個有效 blocking certificate，且尚未同時形成完整正向允許鏈。

## 6.3 Undetermined

$$
\boxed{
\mathsf{Undetermined}
}
$$

表示：

> 尚未形成完整正向證書鏈，也沒有足夠 blocking certificate。

可能原因包括 proof 尚未完成、solver timeout、缺資料、bridge 未知、不可判片段、resource budget 不足或 observer 不可辨識。

MWT 明確禁止：

$$
\boxed{
\mathsf{Undetermined}
=
\mathsf{Illegal}.
}
$$

也禁止：

$$
\boxed{
\mathsf{Undetermined}
=
\mathsf{Legal}.
}
$$

## 6.4 Conflicted

$$
\boxed{
\mathsf{Conflicted}
}
$$

表示：

> 已形成完整正向合法性支持鏈，同時存在一個或多個仍有效的阻斷證書。

`Conflicted` 必須保存，而不是被 majority vote 靜默覆蓋。

---

# 7. 四態是合法性證據狀態，不是真值

本文使用雙軸形式：

$$
\boxed{
\nu_{\Lambda}(\alpha)
=
(s_{\alpha},r_{\alpha})
\in
\{0,1\}^2.
}
$$

其中：

$$
s_{\alpha}=1
$$

表示已存在完整正向 admissibility support；

$$
r_{\alpha}=1
$$

表示存在有效 rejection / blocking support。

因此：

$$
\mathsf{Legal}
=
(1,0),
$$

$$
\mathsf{Illegal}
=
(0,1),
$$

$$
\mathsf{Conflicted}
=
(1,1),
$$

$$
\mathsf{Undetermined}
=
(0,0).
$$

但：

$$
\boxed{
\nu_{\Lambda}
\neq
\nu_{\mathrm{truth}}.
}
$$

合法性只處理「有資格執行／推導／翻譯」，不是一般真值。

---

# 8. 與 Belnap-Dunn 四值的關係

Belnap 的四值邏輯與 First-Degree Entailment 提供成熟參照：positive information、negative information、both 與 neither。

MWT-02 吸收的主要工程精神是：

$$
\boxed{
\text{局部不一致不應自動導出無關任意結論}.
}
$$

但不宣稱：

$$
\boxed{
\mathbb L
=
\text{FDE truth values}.
}
$$

因為 MWT legality 處理的是可作用性、合成、型別、版本、證書與執行資格，而不是一般命題的 truth semantics。

---

# 9. Non-Explosion Principle

如果：

$$
\nu_{\Lambda}(\alpha)
=
(1,1),
$$

MWT 不允許由此推出：

$$
\forall \beta,\quad
\mathsf{Legal}(\beta).
$$

即：

$$
\boxed{
\mathsf{Conflicted}(\alpha)
\not\Rightarrow
\forall\beta\
\mathsf{Legal}(\beta).
}
$$

衝突必須被限制在相關 gate、context、dependency descendants 與顯式允許的 propagation edges。

---

# 10. Gate Decomposition

令：

$$
\mathcal G(\alpha)
=
\{
g_1,\ldots,g_n
\}
$$

為 $\alpha$ 的 required hard gates。

v0.1 提供十五類候選 gate：

$$
\boxed{
\begin{aligned}
g_1&=\mathsf{WellFormed},\\
g_2&=\mathsf{Version},\\
g_3&=\mathsf{SourceDomain},\\
g_4&=\mathsf{Bridge},\\
g_5&=\mathsf{Type},\\
g_6&=\mathsf{Identity},\\
g_7&=\mathsf{Semantic},\\
g_8&=\mathsf{Context},\\
g_9&=\mathsf{Constraint},\\
g_{10}&=\mathsf{Invariant},\\
g_{11}&=\mathsf{HistoryOrder},\\
g_{12}&=\mathsf{Permission},\\
g_{13}&=\mathsf{Resource},\\
g_{14}&=\mathsf{Certificate},\\
g_{15}&=\mathsf{Realization}.
\end{aligned}
}
$$

不是每個 interaction 都需要十五個。

required subset 由 operator、presentation capability 與 execution mode 共同決定。

---

# 11. Gate Result

每個 gate：

$$
g_i
$$

返回：

$$
\boxed{
\nu_i(\alpha)
=
(s_i,r_i).
}
$$

並附正向或阻斷證書：

$$
C_i^+,
\qquad
C_i^-.
$$

最低 gate record：

$$
\boxed{
R_i
=
(
s_i,
r_i,
C_i^+,
C_i^-,
v_i,
h_i
).
}
$$

其中 $v_i$ 是 ruleset/version， $h_i$ 是 validity horizon。

---

# 12. Full Positive Certificate

一個 candidate interaction 要形成完整正向合法性證書：

$$
C_{\alpha}^{+},
$$

要求所有 required hard gates 都有正向支持：

$$
\boxed{
s_{\alpha}
=
\bigwedge_{g_i\in\mathcal G_{\mathrm{req}}(\alpha)}
s_i.
}
$$

並組成：

$$
\boxed{
C_{\alpha}^{+}
=
\left\langle
C_1^+,\ldots,C_n^+
\right\rangle.
}
$$

certificate 不必全部同格式，可以是 proof term、type-check result、solver certificate、hash、test evidence、human authorization 或 measurement record。

---

# 13. Blocking Certificate

只要存在 required hard gate：

$$
g_j
$$

具有有效 blocking support：

$$
r_j=1,
$$

則：

$$
\boxed{
r_{\alpha}
=
\bigvee_{g_i\in\mathcal G_{\mathrm{req}}(\alpha)}
r_i.
}
$$

並至少保存：

$$
\boxed{
C_{\alpha}^{-}
=
\{
(g_j,C_j^-)
\}.
}
$$

因此 hard failure 可以 early reject，而不需要等所有 gate 都完成。

---

# 14. Default Aggregation Rule

strict default：

$$
\boxed{
\nu_{\Lambda}(\alpha)
=
\left(
\bigwedge_i s_i,
\bigvee_i r_i
\right).
}
$$

得到：

$$
(1,0)
\Rightarrow
\mathsf{Legal},
$$

$$
(0,1)
\Rightarrow
\mathsf{Illegal},
$$

$$
(1,1)
\Rightarrow
\mathsf{Conflicted},
$$

$$
(0,0)
\Rightarrow
\mathsf{Undetermined}.
$$

特定 domain 可以覆寫 aggregation policy，但必須版本化並產生新的 rule identity。

---

# 15. 為什麼不是 Majority Vote？

若十五個 gate 中十四個通過，一個 hard type gate 明確失敗，不能做：

$$
\frac{14}{15}
$$

然後宣稱「93.3% 合法」。

如果失敗的是硬條件，作用仍然：

$$
\mathsf{Illegal}.
$$

因此：

$$
\boxed{
\text{hard legality is non-compensatory}.
}
$$

---

# 16. Soft Preferences 不屬於 Legality Core

例如比較快、比較便宜、比較漂亮、比較容易讀或 GPU utilization 較佳，都可進：

$$
\mathsf{Preference}
$$

或：

$$
\mathsf{Cost}
$$

層。

但不應把：

$$
\mathsf{Illegal}
$$

靠高 performance 分數補回：

$$
\mathsf{Legal}.
$$

所以：

$$
\boxed{
\text{admissibility}
\prec
\text{optimization}.
}
$$

先合法，再比較優劣。

---

# 17. Operator Legality、Applicability、Executability、Realization

一個 operator：

$$
o
$$

本身在 presentation $P_o$ 中可以：

$$
\operatorname{OpLegal}(o\mid P_o,\Gamma).
$$

這不推出：

$$
\operatorname{Legal}(o(x)).
$$

若：

$$
o:
D_o
\rightharpoonup
C_o
$$

且：

$$
x\in D_o,
$$

可稱：

$$
\operatorname{Applicable}(o,x).
$$

但 applicability 仍不包含 permission、resource、history 與 global invariant。

再進一步，若當前 runtime 資源與執行條件滿足：

$$
\operatorname{Executable}_{\Gamma,t}(o,x).
$$

如果結果還需要對外部／物理 backend 有效，另問：

$$
\operatorname{Realized}(o(x)\mid\mathcal R).
$$

因此完整階層：

$$
\boxed{
\text{Operatorhood}
\neq
\text{Applicability}
\neq
\text{Executability}
\neq
\text{Realization}.
}
$$

---

# 18. Truth 再額外分離

如果 interaction 是推導命題：

$$
\varphi,
$$

即使：

$$
\mathsf{Legal}(\text{derive }\varphi),
$$

仍然不直接推出：

$$
\operatorname{True}_{\mathbf W}(\varphi).
$$

最多先得到：

$$
T
\vdash
\varphi
$$

或：

$$
M
\models
\varphi
$$

相對指定 foundation/model。

因此：

$$
\boxed{
\text{legally derivable}
\neq
\text{world-level true by default}.
}
$$

---

# 19. 五種不能混同的合法性

延續 X 約束算子論，至少區分：

$$
\boxed{
\text{算子合法性}
\neq
\text{合成合法性}
\neq
\text{共同約束可滿足性}
\neq
\text{bridge 合法性}
\neq
\text{path 合法性}.
}
$$

這五個層級共同構成 GLC 的基本骨架。

---

# 20. Composition Legality

即使：

$$
\operatorname{Legal}(A)
$$

且：

$$
\operatorname{Legal}(B),
$$

也不能推出：

$$
\operatorname{Legal}(B\circ A).
$$

因為可能：

$$
\operatorname{Cod}(A)
\not\subseteq
\operatorname{Dom}(B),
$$

或者 $A$ 改變某個 invariant，使 $B$ 的 precondition 失效。

---

# 21. Constraint Satisfiability

設 hard constraints：

$$
X_1,\ldots,X_n
$$

各自都合法。

仍可能：

$$
\bigcap_{i=1}^{n}
D_{X_i}
=
\varnothing.
$$

這表示：

$$
\boxed{
\text{合法 constraints}
+
\text{合法 composition syntax}
\not\Rightarrow
\text{存在共同可行解}.
}
$$

此時應輸出 constraint diagnosis，例如：

$$
\mathsf{Unsatisfiable},
$$

而不是說每個 constraint 本身非法。

---

# 22. Unsatisfiable 不等於 Illegal Rule

例如：

$$
x>0
$$

與：

$$
x<0
$$

兩個約束各自完全合法。

共同 system：

$$
x>0
\land
x<0
$$

在實數域不可滿足。

所以：

$$
\boxed{
\text{rule validity}
\neq
\text{joint satisfiability}.
}
$$

---

# 23. Bridge Legality

MWT-01 定義：

$$
b:
P_i\to P_o.
$$

MWT-02 要求 bridge 至少檢查：

$$
\boxed{
\mathsf{BridgeGate}
=
(
D_b,
\mathcal Q_b,
\mathfrak I_b,
\mathcal L_b,
C_b
).
}
$$

其中：

- $D_b$：source domain；
- $\mathcal Q_b$：preserved inquiries；
- $\mathfrak I_b$：identity contract；
- $\mathcal L_b$：declared loss；
- $C_b$：bridge certificate。

即使 bridge 存在，若：

$$
x\notin D_b,
$$

則本次使用仍不合法。

---

# 24. Type Gate 與 Refinement Gate

若：

$$
o:
A\to B,
$$

而 bridge 後輸入：

$$
x':C,
$$

需要：

$$
C
\leq
A
$$

或相應 subtype/coercion relation。

若沒有合法 coercion：

$$
g_{\mathrm{type}}
=
\mathsf{Illegal}.
$$

普通 type：

$$
x:\mathbb Z
$$

也可能不夠。

若 operator 要求：

$$
x:
\{
v:\mathbb Z
\mid
v>0
\},
$$

則：

$$
x=0
$$

即使 base type 正確仍不合法。

因此：

$$
\boxed{
\text{type compatibility}
\neq
\text{refinement compatibility}.
}
$$

---

# 25. Effect Gate

某 operation $o$ 可能 type-correct，但具有 effect：

$$
\epsilon_o.
$$

若當前 context 禁止 write、network、mutation、nondeterminism 或 external call，則：

$$
g_{\mathrm{effect}}
=
\mathsf{Illegal}
$$

或在 effect inference 未完成時為：

$$
\mathsf{Undetermined}.
$$

effect system 因而可以成為 GLC 後端之一。

---

# 26. Semantic Gate

兩個 presentations 的資料型別相同不表示語義相同。

例如：

$$
x=1
$$

可以表示 probability、count、boolean encoding、physical unit 或 category label。

因此 bridge 必須確認：

$$
\boxed{
\mathsf{Sem}_P(x)
\rightsquigarrow
\mathsf{Sem}_Q(b(x))
}
$$

符合 translation contract。

---

# 27. Unit / Dimension Gate

在物理或工程 presentation 中：

$$
1\ \mathrm{m}
$$

不能直接與：

$$
1\ \mathrm{s}
$$

進行任意加法。

即使兩者底層都使用：

$$
\mathbb R.
$$

所以 numeric base type 相同不保證 legal action。

---

# 28. Identity Gate

如果 operator 假定 $x$ 在 path 中保持某種 identity，但 bridge 只保留 coarse equivalence，則不能直接使用。

例如：

$$
x\equiv_{\mathrm{macro}} y
$$

不表示：

$$
x\equiv_{\mathrm{history}} y.
$$

因此 operator identity requirement 必須被 bridge identity contract 覆蓋。

---

# 29. Context Gate

同一作用：

$$
o(x)
$$

在不同：

$$
\Gamma_1,
\Gamma_2
$$

可以有不同 legality。

例如不同 assumptions、foundation、time horizon、permission 或 error tolerance。

因此：

$$
\mathsf{Legal}(o,x)
$$

若沒有 context index，只是 shorthand。

canonical 形式仍是：

$$
\boxed{
\Gamma
\vdash
o(x)
\Downarrow_{\Lambda}
\ell.
}
$$

---

# 30. Invariant Gate

若：

$$
I
$$

被標記為 hard invariant，

則 action $o$ 需要證明：

$$
\boxed{
I(x)
\Rightarrow
I(o(x)).
}
$$

若已證明：

$$
I(o(x))=0,
$$

則：

$$
\mathsf{Illegal}.
$$

若尚未證明保持或破壞：

$$
\mathsf{Undetermined}.
$$

---

# 31. History Gate

如果 operator legality 依賴之前發生的 path：

$$
h
=
(r_1,\ldots,r_n),
$$

則：

$$
\boxed{
\mathsf{Legal}(o,x\mid h)
}
$$

不能縮成：

$$
\mathsf{Legal}(o,x).
$$

例如 token 已被消耗、theorem dependency 已撤回、resource 已被前一步占用、state 曾經通過 irreversible transition，或 previous bridge 已產生 lossy coarse-graining。

---

# 32. Noncommutative Legality

若：

$$
A\circ B
\neq
B\circ A,
$$

則可能：

$$
\boxed{
\mathsf{Legal}(B\circ A)
\neq
\mathsf{Legal}(A\circ B).
}
$$

甚至：

$$
\mathsf{Legal}(A)
=
\mathsf{Legal}(B)
=
\mathsf{Legal},
$$

但：

$$
\mathsf{Illegal}(B\circ A).
$$

所以非交換不只是結果差異，也可能改變「是否還有資格繼續作用」。

---

# 33. Path Legality

對 path：

$$
\gamma
=
(o_1,\ldots,o_n),
$$

定義：

$$
x_0=x,
$$

$$
x_i=o_i(x_{i-1}),
$$

並要求：

$$
\boxed{
\Gamma_{i-1}
\vdash
o_i(x_{i-1})
\Downarrow_{\Lambda}
\mathsf{Legal}
}
$$

對所有：

$$
i=1,\ldots,n.
$$

其中：

$$
\Gamma_i
=
\operatorname{Update}
(
\Gamma_{i-1},
x_i,
o_i
).
$$

---

# 34. Path Legal 不等於所有節點預先 Legal

第二步 legality 必須在第一步之後重算。

所以不能只在：

$$
t_0
$$

檢查：

$$
o_1,\ldots,o_n
$$

然後永久授權整條鏈。

需要：

$$
\boxed{
\text{check}
\rightarrow
\text{execute}
\rightarrow
\text{update}
\rightarrow
\text{recheck}.
}
$$

---

# 35. Legality Is Stateful

定義：

$$
\Lambda_t(\alpha)
$$

與：

$$
\Lambda_{t+1}(\alpha)
$$

可以不同，即使 ruleset 版本不變。

因為 state、resource、history、evidence 或 certificate horizon 可以改變。

所以：

$$
\boxed{
\text{fixed rules}
\neq
\text{fixed verdict}.
}
$$

---

# 36. Validity Horizon

每個 certificate：

$$
C
$$

可以帶：

$$
\boxed{
H(C)
=
[t_0,t_1]
}
$$

或其他有效條件。

過期後不能自動 reuse。

若無法重新驗證：

$$
\mathsf{Undetermined}.
$$

---

# 37. Permission Gate

純數學 theorem proving 通常不需要人類權限。

但 MWT runtime 可能連接 databases、external tools、private sources、robots 或 deployment systems。

因此 action 可以有：

$$
\mathsf{PermissionGate}.
$$

它不是數學真理 gate，而是 execution governance gate。

---

# 38. Resource Gate

action 理論上可計算，但在 budget：

$$
B
$$

下不一定可執行。

令：

$$
\kappa(\alpha)
$$

為成本估計。

若有硬上界且：

$$
\kappa(\alpha)>B,
$$

strict runtime 可判：

$$
\mathsf{Illegal}
[
\mathsf{Resource}
].
$$

這個阻斷原因不能被誤讀成 mathematical impossibility。

---

# 39. Certificate Gate

有些高風險 interaction 要求 proof-carrying execution。

例如：

$$
C_{\mathrm{type}},
\quad
C_{\mathrm{invariant}},
\quad
C_{\mathrm{bridge}}.
$$

若 policy 要求 certificate，但目前只有 heuristic evidence：

$$
\boxed{
\mathsf{Undetermined}
}
$$

而不是 Legal。

---

# 40. Evidence Gate 與 Realization Gate

對 empirical action，可能存在：

$$
E^+,
\quad
E^-.
$$

如果正反 evidence 同時充分，可出現：

$$
\mathsf{Conflicted}.
$$

這與 formal contradiction 不完全相同。

形式模型也可能：

$$
\operatorname{FormalLegal}=1,
$$

但其 physical realization：

$$
\mathsf{Undetermined}.
$$

MWT 禁止把兩層混成一個 verdict。

---

# 41. Layered Legality Profile

更完整地：

$$
\boxed{
\mathsf{LegProfile}(\alpha)
=
(
L_{\mathrm{formal}},
L_{\mathrm{semantic}},
L_{\mathrm{runtime}},
L_{\mathrm{empirical}},
L_{\mathrm{governance}}
).
}
$$

Global verdict 是相對 execution policy 的投影：

$$
\boxed{
\ell_{\mathrm{global}}
=
\Pi_{\mathrm{exec}}
(
\mathsf{LegProfile}(\alpha)
).
}
$$

---

# 42. Strict Mode

Strict mode：

$$
\boxed{
\operatorname{Commit}_{\mathrm{strict}}(\alpha)
=
1
\iff
\ell_{\mathrm{global}}
=
\mathsf{Legal}.
}
$$

其餘三態：

$$
\mathsf{Illegal},
\mathsf{Undetermined},
\mathsf{Conflicted}
$$

都不 commit。

---

# 43. Exploratory Mode

Exploratory mode 可以允許：

$$
\mathsf{Undetermined}
$$

進 sandbox。

但結果必須帶：

$$
\mathsf{NonCommit}
$$

與：

$$
\mathsf{ResearchOnly}.
$$

`Conflicted` 也可進 isolated branch，但不得污染 stable core。

---

# 44. Simulation Mode

如果某 action：

$$
\mathsf{Illegal}_{\mathrm{physical}}
$$

但：

$$
\mathsf{Legal}_{\mathrm{simulation}},
$$

可以在 simulation sandbox 執行。

因此：

$$
\boxed{
\text{not deployable}
\neq
\text{not simulatable}.
}
$$

---

# 45. Commit Semantics 與 Transactional Legality

一次正式 interaction 建議分：

$$
\boxed{
\text{Prepare}
\rightarrow
\text{Validate}
\rightarrow
\text{Execute}
\rightarrow
\text{PostCheck}
\rightarrow
\text{Commit}.
}
$$

令：

$$
S_t
$$

為 stable state。

candidate action 先在 staging state：

$$
\widetilde S_{t+1}
$$

執行。

只有：

$$
\boxed{
\operatorname{PostLegal}
(
\widetilde S_{t+1}
)
=
\mathsf{Legal}
}
$$

才：

$$
S_{t+1}
=
\widetilde S_{t+1}.
$$

否則 stable state 不被污染，系統進 rollback、failure branch 或 repair queue。


# 46. Repair Obligation

若：

$$
\ell
=
\mathsf{Illegal}
$$

或：

$$
\mathsf{Undetermined},
$$

GLC 可以產生：

$$
\boxed{
\mathcal R_{\alpha}
}
$$

作為 repair obligations。

例如：

- find bridge；
- add proof；
- refine type；
- collect data；
- reorder path；
- relax soft constraint；
- choose new presentation；
- request theory revision。

這使 failure 不只是停止訊號，而成為下一步研究資料。

---

# 47. Illegal 不能靠重新命名變 Legal

若：

$$
x
$$

type mismatch，

不能只建立新名稱：

$$
x'
$$

就假裝通過。

任何 repair 必須產生：

$$
\boxed{
\text{explicit transformation}
+
\text{certificate}.
}
$$

因此 MWT 對「語言包裝」與「真正轉換」做明確區分。

---

# 48. Exception Rule

某些系統需要 exception。

但 exception 不能是：

> 管理員說可以，所以原規則不存在。

正確形式是產生新 rule context：

$$
\boxed{
\Gamma'
=
\Gamma
+
e_{\mathrm{exception}}.
}
$$

並重新判定：

$$
\Gamma'
\vdash
\alpha
\Downarrow_{\Lambda}
\ell'.
$$

所以 exception 是規則的一部分，不是規則外的黑洞。

---

# 49. Rule Versioning

legality ruleset：

$$
\Lambda^{(v)}
$$

必須固定版本。

同一 action：

$$
\alpha
$$

可能：

$$
\Lambda^{(v)}
\vdash
\alpha
\Downarrow
\mathsf{Illegal},
$$

而：

$$
\Lambda^{(v+1)}
\vdash
\alpha
\Downarrow
\mathsf{Legal}.
$$

這不是 contradiction，除非版本 index 被刪掉。

---

# 50. Run-Level Foundation Freeze

延續 MWT 母稿，對 formal run：

$$
\boxed{
\Lambda^{(v)}
=
\text{fixed}.
}
$$

AI 不得因 candidate action 不合法就自動：

$$
\Lambda^{(v)}
\to
\Lambda^{(v+1)}
$$

並繼續假裝是同一 run。

ruleset revision 必須是：

$$
\boxed{
\mathsf{ExplicitRevisionEvent}.
}
$$

且留下 migration、invalidation 與 rollback 資訊。

---

# 51. Conflict Ledger

所有：

$$
\mathsf{Conflicted}
$$

interaction 應進：

$$
\boxed{
\mathsf{CL}
=
\text{Conflict Ledger}.
}
$$

至少保存：

```text
interaction_id
positive_certificate_chain
blocking_certificate_chain
contexts
rule_versions
observer_sources
affected_dependencies
resolution_status
```

---

# 52. Conflict Propagation Guard

衝突只能沿：

$$
\boxed{
E_{\mathrm{conflict}}
\subseteq
E_{\mathrm{dependency}}
}
$$

中的合法 propagation edges 傳播。

不能：

$$
\mathsf{Conflict}(x)
\Rightarrow
\mathsf{Conflict}(y)
$$

對任意 $y$。

---

# 53. Dependency-Scoped Non-Explosion

若：

$$
\beta
$$

不依賴：

$$
\alpha,
$$

且沒有 conflict propagation path：

$$
\alpha
\leadsto
\beta,
$$

則：

$$
\boxed{
\mathsf{Conflicted}(\alpha)
\not\Rightarrow
\neg\mathsf{Legal}(\beta).
}
$$

局部衝突不應停掉整個世界。

---

# 54. Global Interaction Graph

令 candidate interactions：

$$
\mathcal I_t
$$

形成：

$$
\boxed{
\mathcal G_t^I
=
(
V_t,
E_t
).
}
$$

其中 nodes 可以是：

- presentations；
- objects；
- operators；
- gates；
- certificates；
- results。

edges 包含：

- dependency；
- bridge；
- order；
- conflict；
- invariant；
- certificate；
- resource。

---

# 55. 四個 Legality 子圖

定義 strict legal interaction set：

$$
\boxed{
\mathcal I_t^+
=
\{
\alpha\in\mathcal I_t:
\ell_{\alpha}
=
\mathsf{Legal}
\}.
}
$$

只有：

$$
\mathcal I_t^+
$$

進 commit-capable scheduler。

定義未知集合：

$$
\boxed{
\mathcal I_t^?
=
\{
\alpha:
\ell_{\alpha}
=
\mathsf{Undetermined}
\}.
}
$$

它進 research queue、proof search、bridge discovery、evidence acquisition 或 human review。

定義衝突集合：

$$
\boxed{
\mathcal I_t^{\pm}
=
\{
\alpha:
\ell_{\alpha}
=
\mathsf{Conflicted}
\}.
}
$$

它採：

$$
\boxed{
\text{isolate}
+
\text{diagnose}
+
\text{branch}.
}
$$

定義非法集合：

$$
\boxed{
\mathcal I_t^-
=
\{
\alpha:
\ell_{\alpha}
=
\mathsf{Illegal}
\}.
}
$$

它可以保留作 negative knowledge、failed route、regression test 或 future revision target。

---

# 56. Scheduler 不是 Topological Sort 就結束

若 dependency graph 是 DAG，topological sort 可以提供合法先後的一部分。

但 MWT 還要處理：

- commutativity；
- shared mutable state；
- bridge loss；
- dynamic legality；
- resource；
- alternative branches。

因此 scheduler 必須是：

$$
\boxed{
\text{dependency-aware}
+
\text{legality-aware}
+
\text{noncommutativity-aware}.
}
$$

---

# 57. Commutativity Certificate

如果兩個 actions：

$$
A,B
$$

被允許交換，最好有：

$$
\boxed{
C_{AB}^{\mathrm{comm}}
}
$$

證明或驗證：

$$
B\circ A
\equiv_{\mathfrak I}
A\circ B.
$$

沒有 certificate 時，不能只因看起來互不相關就永久假設交換。

---

# 58. Conditional Commutativity

可能只有在：

$$
D\subseteq X
$$

上：

$$
A\circ B
=
B\circ A.
$$

所以 certificate 必須帶 domain：

$$
C_{AB}^{\mathrm{comm}}(D).
$$

超出 $D$ 必須重檢。

---

# 59. Branch on Order

如果：

$$
A\circ B
$$

與：

$$
B\circ A
$$

都合法且非交換，scheduler 可以產生：

$$
\boxed{
\gamma_1=(A,B),
\qquad
\gamma_2=(B,A).
}
$$

並行探索兩支。

這是 AI-native mathematics 的重要能力：人類可能因分支太多而被迫提前假設某些交換性，AI 則可以在資源允許時保留多條合法歷史。

---

# 60. Path Certificate

對完整 path：

$$
\gamma=(o_1,\ldots,o_n),
$$

建立：

$$
\boxed{
C_{\gamma}
=
(
C_{o_1},
\ldots,
C_{o_n},
C_{\mathrm{order}},
C_{\mathrm{post}}
).
}
$$

它證明的不是單一 theorem，而是：

> 這條執行歷史在當前 ruleset 下可合法重放。

---

# 61. Replay

若：

$$
C_{\gamma}
$$

仍有效，另一 runtime 應能重建：

$$
S_0
\overset{\gamma}{\longrightarrow}
S_n.
$$

若版本或 bridge 改變，replay 必須標記：

$$
\mathsf{NonEquivalentReplay}
$$

而不是靜默使用新環境。

---

# 62. Certificate Algebra

證書也需要合成。

如果：

$$
C_A
$$

證明 $A$ 合法，

$$
C_B
$$

證明 $B$ 在 $A$ 後合法，

則可形成：

$$
\boxed{
C_{B\circ A}
=
C_B
\star
C_A.
}
$$

但：

$$
\star
$$

一般不是交換操作。

通常：

$$
C_B\star C_A
\neq
C_A\star C_B.
$$

因為 preconditions 與 postconditions 不同。

---

# 63. Certificate Composition 也可能失敗

即使：

$$
C_A,
C_B
$$

各自有效，若：

$$
\operatorname{Post}(A)
$$

無法滿足：

$$
\operatorname{Pre}(B),
$$

則：

$$
C_B\star C_A
$$

未定義。

再次得到：

$$
\boxed{
\text{component validity}
\neq
\text{composition validity}.
}
$$

---

# 64. Static Legality 與 Dynamic Legality

某些 gate 可在 execution 前完成：

- syntax；
- type；
- signature；
- bridge version；
- static effect；
- theorem certificate。

形成：

$$
L_{\mathrm{static}}.
$$

另一些只能 runtime 知道：

- current state；
- resource；
- lock；
- latest data；
- dynamic permission；
- path-dependent invariant。

形成：

$$
L_{\mathrm{dynamic}}.
$$

global legality 需要兩者。

---

# 65. Static Legal 不等於 Runtime Legal

例如程式：

$$
p
$$

type checks，

但 memory：

$$
M_t
$$

不足。

則：

$$
L_{\mathrm{static}}
=
\mathsf{Legal},
$$

$$
L_{\mathrm{runtime}}
=
\mathsf{Illegal}
[
\mathsf{Resource}
].
$$

反過來，runtime 暫時有資源也不能改寫 static operator definition。

---

# 66. Monotone 與 Non-Monotone Legality

若增加證據：

$$
E\subseteq E'
$$

只可能讓：

$$
\mathsf{Undetermined}
$$

朝 definitive verdict 移動，可稱某 gate evidence-monotone。

但很多現實 legality 是 non-monotone。

新增 blocker 後：

$$
\mathsf{Legal}
\to
\mathsf{Conflicted}.
$$

規則撤回後：

$$
\mathsf{Legal}
\to
\mathsf{Undetermined}.
$$

MWT 不預設全域單調。

---

# 67. Revocation

certificate：

$$
C
$$

可以被撤銷：

$$
\boxed{
\operatorname{Revoke}(C).
}
$$

所有依賴 $C$ 的 stable results 必須進：

$$
\mathsf{RevalidationQueue}.
$$

這是世界長期運行的必要機制。

---

# 68. Legality Provenance

每個 verdict：

$$
\ell_{\alpha}
$$

必須可追溯：

$$
\boxed{
\operatorname{Prov}
(
\ell_{\alpha}
)
=
(
\Lambda^{(v)},
\Gamma,
\mathcal G_{\mathrm{req}},
C^+,
C^-,
h,
O,
t
).
}
$$

沒有 provenance 的 Legal 不進 stable core。

---

# 69. Reason Codes

Illegal、Undetermined 與 Conflicted 都應有 reason set：

$$
\boxed{
R_{\alpha}
=
\{
r_1,\ldots,r_m
\}.
}
$$

例如：

```text
TYPE_MISMATCH
BRIDGE_OUT_OF_DOMAIN
CERTIFICATE_MISSING
INVARIANT_VIOLATION
RESOURCE_LIMIT
RULE_VERSION_CONFLICT
IDENTITY_CONTRACT_MISMATCH
HISTORY_DEPENDENCY_UNRESOLVED
```

這使 AI 能自動生成 repair plan。

---

# 70. Legality Maturity

一個 legality claim 可以分成熟度：

### L0 — Claimed

只有自然語言說「可以」。

### L1 — Rule-Structured

有明確 gate 與規則。

### L2 — Machine-Checked

至少部分 gate 可機器驗證。

### L3 — Certificate-Carrying

關鍵 hard gates 有證書。

### L4 — Cross-Implementation

至少兩個獨立 verifier 重放。

### L5 — Stable Runtime

跨版本或長時間仍保持指定 invariants。

不是所有普通運算都需要 L5，依風險設定。

---

# 71. Example A：代數數到浮點 Solver

有：

$$
x
=
\sqrt 2
$$

在 algebraic presentation：

$$
P_A.
$$

numerical solver $N$ native 於：

$$
P_F.
$$

需要 bridge：

$$
b:
P_A
\to
P_F.
$$

如果 $b$ 只提供：

$$
1.4142,
$$

而 solver 要求 error：

$$
<10^{-8},
$$

則：

$$
g_{\mathrm{bridge}}
=
\mathsf{Illegal}
$$

或：

$$
\mathsf{Undetermined}
$$

取決於是否還能 refinement。

不是因為 $\sqrt2$ 非法，而是當前 bridge 不足。

---

# 72. Example B：Proof Assistant 與 Numerical Evidence

某 theorem：

$$
\varphi
$$

有大型 numerical evidence。

但 formal proof presentation：

$$
P_{\mathrm{proof}}
$$

要求完整 proof term。

則：

$$
\mathsf{EvidenceGate}
=
\mathsf{Legal}
$$

不等於：

$$
\mathsf{ProofGate}
=
\mathsf{Legal}.
$$

global verdict 可能仍是：

$$
\mathsf{Undetermined}.
$$

這保留：

$$
\boxed{
\text{evidence}
\neq
\text{proof}.
}
$$

---

# 73. Example C：P vs NP 多 Presentation

candidate argument 在：

$$
P_{\mathrm{circuit}}
$$

中得到某結論。

要輸送到：

$$
P_{\mathrm{machine}},
$$

需要 bridge：

$$
T.
$$

若 theorem 只證明 $T$ 在 restricted circuit family 上 sound，則超出 domain 的 claim：

$$
\boxed{
\mathsf{Illegal}
[
\mathsf{BridgeDomain}
].
}
$$

這可阻止「局部等價被偷換成全域等價」。

---

# 74. Example D：非交換 Constraint

兩個 constraints：

$$
X_A,
X_B
$$

各自合法。

但：

$$
X_B\circ X_A
$$

先刪除某些 states，使另一條後續路徑不可恢復。

反序：

$$
X_A\circ X_B
$$

得到不同 feasible set。

因此：

$$
\boxed{
\text{constraint order}
}
$$

本身必須進 history。

---

# 75. Example E：Observer Translation

observer $O$ 與 $P$ 各自有合法 presentation。

若：

$$
F_{OP}
$$

尚未證明保持某 invariant：

$$
I,
$$

則 cross-observer merge：

$$
\boxed{
\mathsf{Undetermined}
}
$$

而不是直接說「只是不同視角，所以等價」。

---

# 76. Example F：Conflicted Bridge

bridge：

$$
b:P\to Q
$$

有：

$$
C_b^+
$$

證明對 identity：

$$
\mathfrak I_1
$$

保真。

另一個 audit：

$$
C_b^-
$$

指出對：

$$
\mathfrak I_2
$$

失真。

如果 interaction 沒有聲明 identity specification，則：

$$
\boxed{
\mathsf{Conflicted}
}
$$

比強行選一方更正確。

---

# 77. Example G：合法計算得到錯誤 Conjecture

AI 可以合法執行：

$$
\mathsf{GenerateConjecture}.
$$

輸出：

$$
\varphi.
$$

這表示生成 action：

$$
\mathsf{Legal}.
$$

但：

$$
\varphi
$$

仍然是：

$$
\mathsf{Unverified}.
$$

因此：

$$
\boxed{
\text{legal generation}
\neq
\text{validated theorem}.
}
$$

---

# 78. Example H：Global Coupling

三個 presentations：

$$
P_1,
P_2,
P_3
$$

各自有 interactions：

$$
A,
B,
C.
$$

假設 $A$ 和 $B$ 可交換，但 $B$ 和 $C$ 不可交換。

scheduler 不能只建立：

$$
\{A,B,C\}
$$

的 unordered set。

需要保存 partial order，例如：

$$
B\prec C
$$

以及 $A$ 與 $B$ 的有條件 independence。

---

# 79. Global Coupling 不是一次矩陣乘法

MWT 的全域交互不能預設：

$$
\mathbf x_{t+1}
=
A\mathbf x_t
$$

已涵蓋全部 legality。

runtime 更接近：

$$
\boxed{
\mathfrak W_t
\xrightarrow{\mathsf{Candidate}}
\mathcal I_t
\xrightarrow{\Lambda}
\mathcal I_t^+
\xrightarrow{\mathsf{Schedule}}
\Gamma_t^{\mathrm{paths}}
\xrightarrow{\mathsf{Execute}}
\widetilde{\mathfrak W}_{t+1}
\xrightarrow{\mathsf{PostCheck}}
\mathfrak W_{t+1}.
}
$$

---

# 80. Candidate Generation 與 Legality 分離

AI 可以非常激進地生成：

$$
\mathcal I_t.
$$

這本身不危險。

真正危險的是 candidate 未經 legality 就直接 commit。

所以 MWT 鼓勵：

$$
\boxed{
\text{high creativity in candidate generation}
+
\text{strict legality at commit boundary}.
}
$$

---

# 81. Legality Search 也可以展開

若：

$$
\alpha
$$

是 Undetermined，AI 可以展開：

- proof search；
- bridge search；
- alternate presentation；
- counterexample search；
- constraint decomposition；
- type refinement；
- observer comparison。

因此 legality calculus 本身也參與：

$$
\mathsf E
\rightarrow
\mathsf L
\rightarrow
\mathsf C.
$$

---

# 82. Legality Convergence

多個 verifier：

$$
V_1,\ldots,V_n
$$

給：

$$
\ell_1,\ldots,\ell_n.
$$

MWT 不做單純 vote。

先分析：

- same ruleset？
- same context？
- independent implementation？
- same certificate？
- shared bug？
- foundation difference？

最後形成：

$$
\boxed{
\Omega_{\Lambda}
=
(
S,
D,
U,
C
)
}
$$

其中 $S$ 是 stable legality support， $D$ 是 disagreement， $U$ 是 unresolved， $C$ 是 certificates。

---

# 83. Cross-Implementation Legality

如果兩個獨立 verifier：

$$
V_A,
V_B
$$

都重放：

$$
C_{\alpha}^{+},
$$

可以提高 Legality Maturity。

但：

$$
\boxed{
\text{two implementations}
\neq
\text{two independent specifications}.
}
$$

共享 specification bug 仍可能存在。

---

# 84. External Theory Interface：Partial Functions

MWT-02 的：

$$
o:
D_o
\rightharpoonup
C_o
$$

與既有 partial-function / partial-algebra 傳統相容。

MWT 不重新發明 partiality。

MWT 的增量在於：把 partiality 與 presentation bridge、history、observer、certificate、runtime resource 共同納入 global interaction judgment。

---

# 85. External Theory Interface：Type Systems

type systems 已成熟處理 term formation、type safety、effect restrictions 與 subtype/refinement constraints。

MWT 不重新發明 type checking。

它把：

$$
\mathsf{TypeGate}
$$

視為 legality gate family 的一員。

---

# 86. External Theory Interface：Effect Systems

Lucassen 與 Gifford 的 polymorphic effect systems 已展示 effect information 可以用於發現 expression scheduling constraints。

這正好說明：

$$
\boxed{
\text{type-correct}
\neq
\text{order-free}.
}
$$

MWT 將此精神推廣到跨 presentation global scheduler。

---

# 87. External Theory Interface：Liquid / Refinement Types

Liquid Types 將 type inference 與 predicate abstraction 結合，用於靜態驗證 safety properties。

MWT 可以把 refinement proof 直接作為：

$$
C_{\mathrm{type}}^+
$$

或：

$$
C_{\mathrm{constraint}}^+.
$$

因此 GLC 是 meta-orchestration，不是另一個 competing refinement type system。

---

# 88. External Theory Interface：Paraconsistency

Belnap 的 four-valued logic 以及後續 paraconsistent traditions 顯示：

$$
\boxed{
\text{inconsistency}
\not\Rightarrow
\text{triviality}
}
$$

可以成為嚴格形式系統。

MWT-02 的 Conflict Isolation 接受這個成熟精神，但 legality state 仍不是一般 truth semantics。

---

# 89. External Theory Interface：Heterogeneous Reasoning

heterogeneous dynamic logic 與 logic-pluralistic formalised reasoning 已研究：

- 多 object logics；
- 不同 program logics；
- common meta-framework；
- modular combination；
- sound cross-language reasoning。

MWT 與此高度鄰接。

MWT 的進一步目標是：

$$
\boxed{
\text{many logics}
\subset
\text{many mathematical presentations}
\subset
\text{one governed mathematical world runtime}.
}
$$

這是研究方向，不是已證明的 universal reduction。

---

# 90. Global Legality 不是 Universal Decision Procedure

MWT-02 不主張存在：

$$
\Lambda_{\mathrm{total}}
$$

可以對所有未來 mathematics 的所有 $\alpha$ 在有限時間給出：

$$
\mathsf{Legal}
$$

或：

$$
\mathsf{Illegal}.
$$

正因如此：

$$
\boxed{
\mathsf{Undetermined}
}
$$

是永久第一級狀態，不是暫時 UI placeholder。

---

# 91. Bounded Runtime Semantics

實際 AI system 可以設定：

$$
B
=
(
B_{\mathrm{time}},
B_{\mathrm{memory}},
B_{\mathrm{proof}},
B_{\mathrm{search}}
).
$$

若 budget 到期且無 definitive result：

$$
\boxed{
\ell
=
\mathsf{Undetermined}
[
\mathsf{BudgetExhausted}
].
}
$$

不准偽造 verdict。

---

# 92. Legality Engine

MWT-02 第一核心 runtime 模組：

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
\alpha,
\Gamma,
\Lambda^{(v)}
)
$$

輸出：

$$
(
\ell,
C^+,
C^-,
R,
\mathcal R_{\alpha}
).
$$

---

# 93. Gate Registry

第二個模組：

$$
\boxed{
\mathsf{GR}
}
$$

記錄：

```text
gate_id
gate_type
version
required_capabilities
input_contract
positive_certificate_type
blocking_certificate_type
validity_horizon
dependencies
```

---

# 94. Constraint Registry

第三個模組：

$$
\boxed{
\mathsf{XR}
}
$$

保存 hard constraints、soft preferences、scope、exception rules 與 version。

硬／軟必須分開。

---

# 95. Certificate、Conflict、History、Execution 與 Commit 模組

第四個模組：

$$
\mathsf{CertL}
$$

保存 positive certificates、blockers、provenance、hash、verifier、expiry、revocation 與 dependency graph。

第五個模組：

$$
\mathsf{ConfL}
$$

確保：

$$
\mathsf{Conflicted}
$$

不被自動 collapse。

第六個模組：

$$
\mathsf{HL}
$$

保存每條 history：

$$
\gamma
=
(
o_1,\ldots,o_n
)
$$

以及每一步 state hash、context、legality verdict、certificate、branch 與 rollback。

第七個模組：

$$
\mathsf{EQ}
$$

至少分：

```text
STRICT_COMMIT
SANDBOX
RESEARCH
CONFLICT_REVIEW
REJECTED
REVALIDATION
```

第八個模組：

$$
\mathsf{CRL}
$$

負責 Commit / Rollback。

只有 strict legal 且 postcheck 通過的 action 才修改 canonical stable state。


# 96. First Reference Algorithm

概念 pseudocode：

```text
function judge(interaction alpha, context Gamma, rules Lambda):
    gates = required_gates(alpha, Gamma, Lambda)

    positive_chain = []
    blockers = []
    unresolved = []

    for gate in gates:
        result = evaluate(gate, alpha, Gamma)

        if result.support:
            positive_chain.append(result.positive_certificate)

        if result.block:
            blockers.append(result.blocking_certificate)

        if not result.support and not result.block:
            unresolved.append(result.reason)

    full_support = every required gate has support
    any_block = blockers is not empty

    if full_support and not any_block:
        status = LEGAL
    elif not full_support and any_block:
        status = ILLEGAL
    elif full_support and any_block:
        status = CONFLICTED
    else:
        status = UNDETERMINED

    return status, positive_chain, blockers, unresolved
```

這一 reference policy 有意維持簡單。

它固定的是 v0.1 的最低語義，不宣稱所有 domain 都必須永遠使用同一 aggregation。

---

# 97. Scheduler Algorithm

```text
1. collect strict-legal actions
2. build dependency edges
3. attach noncommutativity relations
4. attach commutativity certificates
5. compute currently enabled frontier
6. execute commuting independent actions in parallel
7. branch when multiple noncommuting legal orders are intentionally explored
8. after every committed step, update state/context
9. re-run affected legality gates
10. invalidate stale certificates
11. postcheck invariants
12. commit or rollback
```

這個 algorithm 在 MWT-02 只固定接口。

真正的 scheduler theory 留給 MWT-03。

---

# 98. Why AI-Native?

人類可以理解：

$$
\mathbb L,
$$

gate、certificate、path 與 commit。

但大規模 runtime 可能需要同時維護：

- 幾十萬 gate results；
- 多個 foundations；
- 多個 observers；
- 大量 cross-presentation bridges；
- 非交換 path branches；
- certificate validity graph；
- resource / dependency frontier。

這正是 AI/AGI 比較適合承載的部分。

因此本文所稱 AI-native 不是：

$$
\boxed{
\text{人類無法理解公式}.
}
$$

而是：

$$
\boxed{
\text{完整運行狀態超出單一未增強人類可實際維護的操作頻寬}.
}
$$

---

# 99. Human Governance

Human interface 不需要顯示每個 gate 的所有微觀細節。

至少應顯示：

1. why legal；
2. why blocked；
3. what is unknown；
4. what conflicts；
5. what will change if committed；
6. what certificate supports it；
7. rollback availability；
8. 哪個 ruleset / version 正在生效。

這使 governance 建立在可追溯結構上，而不是只看 AI 的一句結論。

---

# 100. MWT-02 Minimal Constitution

v0.1 固定十六條：

### L1 — Legality Before Interaction

任何 cross-presentation interaction 在 commit 前必須經 legality judgment。

### L2 — Partiality

operator existence 不代表 universal applicability。

### L3 — Four-State Output

系統必須能表達 Legal、Illegal、Undetermined、Conflicted。

### L4 — Legality Is Not Truth

Legal 不等於 World-level true。

### L5 — Non-Explosion

Conflicted 不得無條件污染無關 interaction。

### L6 — Hard Constraints Are Non-Compensatory

硬約束失敗不能靠其他偏好分數抵銷。

### L7 — Operator Legality Is Not Composition Legality

合法元件不保證合法合成。

### L8 — Composition Legality Is Not Satisfiability

合法合成語法不保證共同解存在。

### L9 — Bridge Contract

跨 presentation 作用必須使用有 domain 與 preservation contract 的 bridge。

### L10 — Identity Must Be Declared

需要保存的 identity 不得靠名稱默認。

### L11 — History Is First-Class When Order Matters

非交換問題必須保存 path。

### L12 — Dynamic Recheck

state/context 更新後，受影響 legality 必須重判。

### L13 — Certificates Are Versioned

certificate 必須攜帶來源、版本與 validity horizon。

### L14 — Unknown Is Stable

系統允許永久保留 Undetermined。

### L15 — Conflict Is Preserved

Conflicted 必須被隔離、診斷與追蹤，而不是靜默覆蓋。

### L16 — Foundation Revision Is Explicit

AI 不得在同一 formal run 中偷偷改 legality foundation。

---

# 101. 命題：Hard Block Dominance

若：

$$
r_{\alpha}=1
$$

且：

$$
s_{\alpha}=0,
$$

則 default aggregation：

$$
\nu_{\Lambda}(\alpha)
=
(0,1),
$$

因此：

$$
\boxed{
\ell_{\alpha}
=
\mathsf{Illegal}.
}
$$

此命題直接來自四態 aggregation 定義。

---

# 102. 命題：Unknown Does Not Authorize Commit

Strict mode 定義：

$$
\operatorname{Commit}(\alpha)=1
$$

若且唯若：

$$
\ell_{\alpha}
=
\mathsf{Legal}.
$$

因此：

$$
\boxed{
\mathsf{Undetermined}
\not\Rightarrow
\operatorname{Commit}.
}
$$

這是 MWT runtime 最重要的安全邊界之一。

---

# 103. 命題：Conflict Does Not Explode

由 L5，若：

$$
\ell_{\alpha}
=
\mathsf{Conflicted},
$$

且：

$$
\beta
$$

不在其 dependency / propagation closure，

則不能單由 $\alpha$ 推出：

$$
\ell_{\beta}
\neq
\mathsf{Legal}.
$$

這保證局部 conflict 能夠與世界其餘穩定區域共存。

---

# 104. 命題：Node Legality Does Not Imply Path Legality

存在：

$$
A,B
$$

各自 Legal，

但：

$$
\operatorname{Cod}(A)
\cap
\operatorname{Dom}(B)
=
\varnothing.
$$

因此：

$$
B\circ A
$$

未定義。

所以：

$$
\boxed{
\mathsf{Legal}(A)
\land
\mathsf{Legal}(B)
\not\Rightarrow
\mathsf{Legal}(B\circ A).
}
$$

---

# 105. 命題：Order Can Change Legality

若：

$$
A
$$

改寫一個 gate precondition，使：

$$
B
$$

失效，而 $B$ 不破壞 $A$ 的 precondition，則可能：

$$
\mathsf{Illegal}(B\circ A)
$$

但：

$$
\mathsf{Legal}(A\circ B).
$$

故 path order 是 legality datum。

---

# 106. 命題：Legal Execution Does Not Imply True Output

若 action：

$$
\alpha
=
\mathsf{GenerateConjecture}
$$

合法，但輸出 conjecture：

$$
\varphi
$$

未經 proof，則 legality 定義本身不能推出：

$$
\operatorname{True}(\varphi).
$$

這將 AI 的「合法生成」與「數學證明」永久分離。

---

# 107. 條件定理：Sequential Legality Closure

設 path：

$$
\gamma
=
(o_1,\ldots,o_n),
$$

並假設：

1. 初始 $S_0$ 合法；
2. 每一步：
   $$
   \Gamma_{i-1}
   \vdash
   o_i(S_{i-1})
   \Downarrow_{\Lambda}
   \mathsf{Legal};
   $$
3. 每一步 postcheck 成功；
4. context update 正確；
5. 所有 certificate 在執行時有效。

則依定義構造：

$$
\boxed{
\gamma
}
$$

為一條可 commit 的 sequentially legal path。

這不是聲稱 path 結果為 World-level true。

它只證明執行歷史符合當前 legality calculus。

---

# 108. 條件定理：Certified Bridge Composition

若：

$$
b_1:P\to Q,
$$

$$
b_2:Q\to R
$$

各自具有相對 inquiry family：

$$
\mathcal Q
$$

的 preservation certificates，且：

$$
\operatorname{Ran}(b_1)
\subseteq
\operatorname{Dom}(b_2),
$$

並且 identity contracts compatible，則：

$$
b_2\circ b_1
$$

可形成對 $\mathcal Q$ 的候選 composite bridge certificate。

若任一條件失敗，不能由兩個局部 bridge 的存在推出 composite bridge 合法。

---

# 109. 研究猜想：Legality-Guided Globalization

對一部分目前必須手工切成多個局部 solver 的問題，若 presentation registry 與 legality engine 足夠成熟，可以先生成較大的 global interaction graph，再由 legality 與 resource gates 動態誘導有效 locality。

這個猜想若成立，代表數學工作流可以從：

$$
\boxed{
\text{先切小才能算}
}
$$

逐步轉成：

$$
\boxed{
\text{先保持較大全域，再讓合法性決定哪些局部真的需要被啟用}.
}
$$

---

# 110. 研究猜想：Conflict-Tolerant Research Acceleration

保存：

$$
\mathsf{Conflicted}
$$

與：

$$
\mathsf{Undetermined}
$$

而非強迫二值化，可能使多 AI 研究在大量局部 disagreement 存在時仍維持整體推進，降低 premature collapse。

這需要未來以實際 multi-agent research benchmark 驗證。

---

# 111. 研究猜想：Certificate-Guided AI Mathematics

當大部分高風險 interactions 都能攜帶 composable certificates 時，AI 可以將更多計算、翻譯與形式化工作從 human micromanagement 轉為 machine-maintained global runtime。

人類的角色因此可以逐步轉向：

- foundation governance；
- value / goal specification；
- high-level inquiry；
- exception approval；
- audit；
- theory revision。

---

# 112. 開放問題

### O1 — Universal Gate Vocabulary

是否存在足夠小但具有高覆蓋力的 legality gate vocabulary？

### O2 — Gate Independence

哪些 gates 可被證明彼此獨立？

### O3 — Minimal Certificate

一個跨 presentation action 的最小充分證書是什麼？

### O4 — Conflict Algebra

Conflicted gate 的 composition 是否存在有用的通用代數？

### O5 — Noncommutative Scheduling Complexity

大量 path-sensitive legality 如何避免 combinatorial explosion？

### O6 — Bridge Discovery

AI 如何自動提出並證明新 bridge？

### O7 — Legality under Theory Revision

foundation version 改變後，如何最小化 revalidation？

### O8 — Observer Disagreement

何時 observer conflict 可以由 covariance / translation 吸收？

### O9 — Empirical Legality

模型的 domain-of-validity 如何機器化？

### O10 — Physical Realization

形式合法與物理可實現之間如何建立一般接口？

---

# 113. Runtime 資料結構

建議最低 interaction record：

```text
Interaction:
  interaction_id
  operator_id
  operator_presentation
  inputs[]
  bridges[]
  context_id
  history_ref
  rule_version
  required_gates[]
  execution_mode
```

每個 input：

```text
InputRef:
  presentation_id
  object_id
  object_version
  bridge_id
  identity_spec
```

---

# 114. Gate Result Schema

```text
GateResult:
  gate_id
  required
  support
  block
  positive_certificate
  blocking_certificate
  reason_codes
  rule_version
  valid_from
  valid_until
```

---

# 115. Judgment Record

```text
LegalityJudgment:
  interaction_id
  status
  full_positive_chain
  blockers
  unresolved
  provenance
  repair_obligations
  evaluated_at
```

---

# 116. Execution Record

```text
ExecutionRecord:
  interaction_id
  pre_state
  legality_judgment
  staging_state
  postcheck
  commit_status
  rollback_ref
  resulting_state
  history_hash
```

---

# 117. Reference Evaluator 的定位

本 Source Pack 附帶：

```text
mwt02_legality_reference.py
```

它只實作：

- four-state gate aggregation；
- hard / soft gate separation；
- strict commit rule；
- basic reason tracking。

它不是 MWT-02 完整 theorem prover，更不是 universal legality oracle。

其用途是固定 v0.1 最低 operational semantics，避免未來不同 AI 對四態 aggregation 產生互不相容的隱性解讀。

---

# 118. 與內部既有理論的分工

## 分域算子本體論

提供：

$$
\boxed{
\text{Operatorhood}
\neq
\text{Applicability}
\neq
\text{Executability}
\neq
\text{Realization}.
}
$$

MWT-02 將其提升成跨 presentation gate。

## X 約束算子論

提供：

$$
\boxed{
\text{算子合法性}
\neq
\text{合成合法性}
\neq
\text{可滿足性}.
}
$$

以及：

$$
\boxed{
\text{局部有限、全局無界}.
}
$$

MWT-02 將其從應用約束中介表示擴張為數學世界控制層。

## 四態與非爆炸推理

提供：

$$
\boxed{
\text{局部衝突可保存}
}
$$

且：

$$
\boxed{
\text{衝突不授權任意推論}.
}
$$

MWT-02 將此精神轉為 legality conflict isolation。

## Series B

提供 relation order、path difference、observer transport、holonomy、covariance 與 local-global obstruction。

MWT-02 將其接到 scheduler 與 history gate。

---

# 119. MWT-02 與 MWT-01 的組合

MWT-01 問：

$$
\boxed{
\text{What presentations exist?}
}
$$

MWT-02 問：

$$
\boxed{
\text{What interactions are admissible?}
}
$$

因此：

$$
\boxed{
\mathcal G_t^P
+
\Lambda
\Rightarrow
\mathcal G_t^{I,+}.
}
$$

這是 MWT 第一次從 world representation 進入 world operation。

---

# 120. 仍然沒有完成的部分

MWT-02 尚未完整建立：

- optimal global scheduler；
- global convergence protocol；
- branch compression；
- distributed multi-agent transaction；
- world-state canonical runtime；
- proof-carrying bridge synthesis。

這些應由後續文章處理。

---

# 121. 下一篇接口

下一篇建議：

# **MWT-03：Global Interaction Graph and Noncommutative Scheduler**

正式處理：

$$
\boxed{
\text{合法 interactions 已經存在後，
它們如何被全域排程、並行、分支、重排、回滾與收斂？}
}
$$

核心將包含：

- dependency graph；
- partial order；
- commutativity certificates；
- dynamic frontier；
- branch explosion control；
- path equivalence；
- transaction；
- multi-AI execution；
- stable-state commit。

MWT-02 管：

$$
\boxed{
\text{Can it act?}
}
$$

MWT-03 管：

$$
\boxed{
\text{When and in what order should it act?}
}
$$

---

# 122. 一句話版

> **MWT-02 將「合法性」建立為數學世界的第一級控制結構：任何跨 presentation 作用都必須帶著明示的 domain、type、identity、semantics、constraint、invariant、history、resource 與 certificate 條件接受判定；判定允許 Legal、Illegal、Undetermined 與 Conflicted 四態，並以非爆炸、硬約束不可補償、動態重判、非交換 path 保存與 transactional commit 保證全域計算不退化成任意互算。它不承諾判定一切，而承諾在不知道時說不知道，在衝突時保存衝突，在不合法時拒絕 commit，只有已形成完整正向證書且無有效 blocker 的 interaction 才能進入穩定世界狀態。**

---

# 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $\alpha$ | candidate interaction episode |
| $o$ | native operator |
| $P_o$ | operator native presentation |
| $b_i$ | cross-presentation bridge |
| $\Gamma$ | legality context |
| $\Lambda^{(v)}$ | versioned legality ruleset |
| $\ell$ | legality status |
| $\mathbb L$ | four legality states |
| $\nu_{\Lambda}(\alpha)$ | legality evidence pair |
| $s_{\alpha}$ | full positive admissibility support |
| $r_{\alpha}$ | blocking support |
| $g_i$ | legality gate |
| $C_i^+$ | positive gate certificate |
| $C_i^-$ | blocking gate certificate |
| $\gamma$ | ordered interaction path |
| $C_{\gamma}$ | path legality certificate |
| $\mathcal I_t^+$ | strict legal interaction set |
| $\mathcal I_t^?$ | undetermined interaction set |
| $\mathcal I_t^{\pm}$ | conflicted interaction set |
| $\mathcal I_t^-$ | illegal interaction set |
| $\mathsf{LE}$ | Legality Engine |
| $\mathsf{GR}$ | Gate Registry |
| $\mathsf{CertL}$ | Certificate Ledger |
| $\mathsf{ConfL}$ | Conflict Ledger |
| $\mathsf{HL}$ | History Ledger |
| $\mathsf{EQ}$ | Execution Queue |
| $\mathsf{CRL}$ | Commit / Rollback Layer |

---

# 附錄 B：v0.1 非主張清單

MWT-02 不主張：

1. 所有合法性問題可決定；
2. 四態 legality 就是 Belnap-Dunn truth semantics；
3. Conflicted 表示某命題本體上真且假；
4. Legal action 的輸出必然是真的；
5. type checking 足以完成所有 legality；
6. constraint satisfiability 等於 operator legality；
7. 所有合法 actions 可以任意平行；
8. 所有非交換 path 都必須全部實際執行；
9. 所有 bridges 都能自動發現；
10. 所有 certificates 都能形式證明；
11. resource block 表示 mathematical impossibility；
12. physical unrealizability 表示 formal illegality；
13. observer disagreement 必然可消解；
14. global legality 需要一個唯一邏輯 foundation；
15. MWT-02 取代 refinement types、effect systems、partial algebras、constraint solvers 或 paraconsistent logic；
16. AI 有權在同一 run 中自動修改 foundation；
17. 多數 verifier 同意就等於 World truth；
18. Global Legality Calculus 已經是完整 AGI mathematics runtime。

---

# 附錄 C：外部研究接口與參考文獻

1. Nuel D. Belnap Jr., **A Useful Four-Valued Logic**, in J. Michael Dunn and George Epstein (eds.), *Modern Uses of Multiple-Valued Logic*, 1977, pp. 5–37. DOI: 10.1007/978-94-010-1161-7_2.  
2. John M. Lucassen and David K. Gifford, **Polymorphic Effect Systems**, POPL 1988, pp. 47–57. DOI: 10.1145/73560.73564.  
3. Patrick Maxim Rondon, Ming Kawaguchi, and Ranjit Jhala, **Liquid Types**, PLDI 2008, pp. 159–169.  
4. J. V. Tucker and J. I. Zucker, **Abstract Computability, Algebraic Specification and Initiality**, 2001, arXiv:cs/0109001.  
5. Liyi Li and Elsa Gunter, **A Method to Translate Order-Sorted Algebras to Many-Sorted Algebras**, 2018, arXiv:1802.06493.  
6. Célia Borlido and Brett McLean, **Difference-Restriction Algebras of Partial Functions with Operators: Discrete Duality and Completion**, 2020, arXiv:2012.00224.  
7. Samuel Teuber, Mattias Ulbrich, André Platzer, and Bernhard Beckert, **Heterogeneous Dynamic Logic: Provability Modulo Program Theories**, 2025, arXiv:2507.08581.  
8. Christoph Benzmüller, Daniel Kirchner, and Luca Pasetto, **Many Logics, One Methodology: A Plea for Logical Pluralism in Formalised Reasoning**, 2026, arXiv:2605.27246.  

---

# 附錄 D：內部依賴

MWT-02 主要直接吸收：

- 《MWT-01：World Primitive 與 Presentation Theory》
- 《分域算子本體論：從萬物皆算子到合法作用》
- 《X 約束算子論：局部有限、全局無界的非數值應用約束演算》
- 《四態與非爆炸推理》
- 《多維空間狀態類型論：開放維度、依賴類型與合法態射》
- 《分域憲章：結構域、概念身份與角色型別系統》
- Series B《觀察者、局部關係、非交換與全域守恆》

這些理論不被 MWT-02 廢除。

MWT-02 的責任是把它們已有的 legality、constraint、type、conflict 與 order 思想提升成 World-level cross-presentation control plane。

