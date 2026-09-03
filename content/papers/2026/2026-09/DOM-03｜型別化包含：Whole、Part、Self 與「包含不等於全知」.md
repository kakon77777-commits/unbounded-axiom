# DOM-03｜型別化包含：Whole、Part、Self 與「包含不等於全知」

## Typed Containment: Whole, Part, Self, and the Non-Collapse of Inclusion into Knowledge

**系列：** Dynamic Operational Metaphysics（DOM）／動態可操作形而上學  
**篇次：** 03 / 08  
**文件編號：** EML-DOM-03-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-20  
**版本：** v0.1 Canonical Draft  
**文件性質：** 理論整合論文／部分—整體關係／多尺度主體／型別化包含／知識與控制分離  
**證據狀態：** 本文主要建立形式化概念接口；mereology、complex-systems observability 與 evolutionary transitions in individuality 僅作外部結構對照。本文不主張所有 ordinary-language “part” 關係皆可化約為同一種形式 mereology，也不主張任何 higher-level whole 必然具有單一主體性。

---

## 摘要

「 $A$ 是 $B$ 的一部分」在人類語言中經常被壓縮成一個看似簡單的包含關係：

$$
A\subseteq B.
$$

然而，對生物、人工智能、多 Agent 系統、世界模型、記憶系統、組織、分散式智能與 Self–World 結構而言，「包含」至少可能表示物理包含、構成、功能元件、因果嵌入、資訊收納、表徵、記憶收納、控制、治理、身份結構或 substrate dependency。這些關係並不必然具有相同的傳遞性、對稱性、可觀測性、控制性與身份後果。

本文因此提出 **Typed Containment（型別化包含）**。統一記號為：

$$
\boxed{
\operatorname{Contain}_{\alpha}
(A,B\mid s,t,c)=1,
}
$$

表示在尺度 $s$ 、時間 $t$ 、條件 $c$ 下，整體／容器 $A$ 以型別 $\alpha$ 包含 $B$。

最低包含型別族定義為：

$$
\boxed{
\mathfrak C
=
\left\{
C_{\mathrm{spatial}},
C_{\mathrm{material}},
C_{\mathrm{structural}},
C_{\mathrm{functional}},
C_{\mathrm{causal}},
C_{\mathrm{informational}},
C_{\mathrm{representational}},
C_{\mathrm{memory}},
C_{\mathrm{control}},
C_{\mathrm{governance}},
C_{\mathrm{identity}},
C_{\mathrm{substrate}}
\right\}.
}
$$

本文的第一個核心命題是：

$$
\boxed{
\operatorname{Contain}_{\alpha}(A,B)
\not\Rightarrow
\operatorname{Contain}_{\beta}(A,B),
\qquad
\alpha\neq\beta.
}
$$

也就是：物理包含不推出控制包含；資訊包含不推出身份包含；治理包含不推出因果包含；模型含有某對象的表示，也不表示模型本體上「含有」該對象本身。

第二個核心命題是：

$$
\boxed{
\text{Containment}
\not\Rightarrow
\text{Knowledge}.
}
$$

本文以 control-theoretic observability 給出一個乾淨形式反例：若整體系統 $A$ 的 state 包含子系統狀態 $x_B$，但可用輸出 $y$ 對 $x_B$ 不可辨識，則 $B$ 仍然是 $A$ 的結構／狀態部分，卻不能從 whole-level accessible output 唯一重建其狀態。換言之：

$$
\boxed{
B\subset_{\mathrm{state}} A
\not\Rightarrow
K_A(B)=1.
}
$$

這正是「我是一個人，但我並不知道自己每一個細胞此刻在做什麼」的形式核心：**作為 whole 的包含關係，並不自動產生 whole-level epistemic access。**

第三個核心命題是：

$$
\boxed{
\text{Part-of}
\not\Rightarrow
\text{Non-Subject}.
}
$$

一個 lower-level entity 可以是 higher-level whole 的 constituent，同時仍在自己的尺度具有狀態持續、局部邊界、感知、控制或 lineage。現代 evolutionary transitions in individuality 的研究本身就研究 lower-level units 如何形成 higher-level individuals，並指出 biological individuality 具有 nested、multi-level 與可逆轉的結構；這提供一個非常重要的外部類比：higher-level individuality 的形成並不等同於「part / whole」只有單一二值定義。

本文最後建立 **Boundary-Preserving Containment**、**Residual Local Autonomy** 與 **Containment Certificate**。其目的不是把所有 part–whole 關係統一成一個超大集合論，而是建立一套可以回答：

> 包含的是什麼？  
> 在哪個尺度包含？  
> 這種包含是否允許局部邊界？  
> whole 是否能觀察 part？  
> 是否能控制 part？  
> 是否有合法治理權？  
> part 是否仍保有自己的 identity／agency？

DOM-03 因此把「包含」從靜態 $\subseteq$，改寫為一族需要 relation、scale、time、condition 與證書的動態關係。

---

## 關鍵詞

Typed Containment；Mereology；Part–Whole；Containment–Knowledge Separation；Observability；Multiscale Individuality；Nested Self；Boundary-Preserving Containment；Residual Autonomy；Representation Fallacy；Constitution；Membership；Whole–Part Ontology；型別化包含；部分整體；多尺度主體

---

# 0. 研究定位與非主張

本文不主張：

1. 所有「部分」關係都等於 classical mereological parthood；
2. group membership 必然是 mereological parthood；
3. constitution 必然等於 parthood；
4. physical containment 自動推出 causal containment；
5. whole 自動知道所有 parts；
6. whole 自動能控制所有 parts；
7. whole 自動擁有所有 parts；
8. part 被包含後必然失去主體性；
9. higher-level self 必然具有單一 subjective consciousness；
10. nested biological individuality 可直接等同 AI selfhood；
11. transitivity 對所有 typed containment 都成立；
12. containment relation 必然是二值；
13. containment strength 可以由單一 scalar 完整表示；
14. representational containment 等於 ontological containment；
15. 只要某物構成 whole，就必須服從 whole 的全部治理。

本文真正主張的是：

$$
\boxed{
\text{Containment must be indexed by relation, scale, time, and condition.}
}
$$

---

# 1. 問題：`A ⊂ B` 到底說了什麼？

在數學集合論中：

$$
A\subseteq B
$$

具有清楚語義：

> $A$ 的每個元素都是 $B$ 的元素。

但自然語言中的：

> A 是 B 的一部分。

可能表示完全不同的東西。

例如：

- 一顆細胞是人體的一部分；
- 一名員工是公司的成員；
- 一個檔案在資料庫裡；
- 一段記憶在 AI memory store 中；
- 一個 sub-agent 屬於 mother-agent system；
- 一個角色存在於模擬世界；
- 一個參數位於 model state；
- 一個國家位於聯邦結構；
- 一個 region 位於 world；
- 一個模組構成 higher-level controller。

這些都不能無條件寫成同一個：

$$
\subseteq.
$$

---

# 2. Mereology 的最低提醒

Mereology 研究 part–whole relations。

但現代 mereology 本身就指出普通語言的 “part” 同時覆蓋：

- material portions；
- functional components；
- spatial regions；
- temporal parts；
- group membership；
- constitution；
- mixtures。

其中部分是否應視為真正 mereological parthood，本身仍具爭議。

因此 DOM-03 的出發點不是：

$$
\boxed{
\text{everything is one parthood relation}.
}
$$

而是：

$$
\boxed{
\text{ordinary containment language is relation-underdetermined}.
}
$$

---

# 3. Typed Containment 的基本定義

本文定義：

$$
\boxed{
\operatorname{Contain}_{\alpha}
(A,B\mid s,t,c)=1
}
$$

表示：

> 在尺度 $s$ 、時間 $t$ 、條件 $c$ 下， $A$ 以 containment type $\alpha$ 包含 $B$。

其中：

$$
\alpha\in\mathfrak C.
$$

---

# 4. Containment Family

第一版：

$$
\boxed{
\mathfrak C
=
\left\{
C_{\mathrm{spatial}},
C_{\mathrm{material}},
C_{\mathrm{structural}},
C_{\mathrm{functional}},
C_{\mathrm{causal}},
C_{\mathrm{informational}},
C_{\mathrm{representational}},
C_{\mathrm{memory}},
C_{\mathrm{control}},
C_{\mathrm{governance}},
C_{\mathrm{identity}},
C_{\mathrm{substrate}}
\right\}.
}
$$

它不是最終完備分類。

---

# 5. Spatial Containment

$$
\operatorname{Contain}_{spatial}(A,B)=1
$$

表示：

> $B$ 的 relevant spatial extent 位於 $A$ 的指定 spatial region 內。

例如：

$$
Region(B)\subseteq Region(A).
$$

但：

$$
\boxed{
C_{\mathrm{spatial}}
\not\Rightarrow
C_{\mathrm{functional}}.
}
$$

房間包含桌子，不表示房間把桌子當功能元件。

---

# 6. Material / Constitutive Containment

$$
\operatorname{Contain}_{material}(A,B)=1
$$

表示：

> $B$ 的 material / constituent structure contributes to $A$。

但 constitution 是否就是 mereological parthood，在哲學上並不無爭議。

因此 DOM 明確保留：

$$
\boxed{
\text{Constitution}
\neq_{\mathrm{default}}
\text{Parthood}.
}
$$

---

# 7. Structural Containment

$$
\operatorname{Contain}_{structural}(A,B)=1
$$

表示：

> $B$ 在 $A$ 的組織結構中佔有一個可追蹤位置。

例如：

- module in architecture；
- node in hierarchy；
- subsystem in system graph。

它不必等同 material containment。

---

# 8. Functional Containment

$$
\operatorname{Contain}_{functional}(A,B)=1
$$

表示：

> $B$ 對 $A$ 的某功能具有特定角色。

例如：

- sensor；
- controller；
- memory module；
- actuator；
- validator。

功能元件可能具有高 salience，卻不是 A 的全部 material part。

---

# 9. Causal Containment

定義：

$$
\boxed{
\operatorname{Contain}_{causal}(A,B)=1
}
$$

若：

> $B$ 的 state transitions 是 $A$ 有效 dynamics 中被明示追蹤的一部分，且 $B$ 與 A 的其他部分存在 causal coupling。

例如：

$$
x_A
=
(x_B,x_R).
$$

但：

$$
x_B\subset x_A
$$

只表示 state decomposition。

---

# 10. Informational Containment

$$
\operatorname{Contain}_{info}(A,B)=1
$$

可能有至少兩種讀法。

## 10.1 Data-Payload Containment

A 保存 B 的資料：

$$
D_B\in A.
$$

## 10.2 Information-About Containment

A 保存關於 B 的資訊：

$$
I_A(B)>0.
$$

兩者不同。

---

# 11. Informational Containment 不等於 Ontic Containment

如果 database $A$ 包含：

$$
Record(B),
$$

不能推出：

$$
B\in A
$$

在 physical / ontological sense。

所以：

$$
\boxed{
\operatorname{Contain}_{info}(A,B)
\not\Rightarrow
\operatorname{Contain}_{ontic}(A,B).
}
$$

---

# 12. Representational Containment

定義：

$$
\boxed{
\operatorname{Contain}_{rep}(A,B)=1
}
$$

表示：

> $A$ 內存在 representation：

$$
\rho_A(B).
$$

真正形式是：

$$
\rho_A(B)\in A,
$$

不是：

$$
B\in A.
$$

---

# 13. Representation Containment Fallacy

本文命名：

$$
\boxed{
\text{Representation Containment Fallacy}.
}
$$

形式：

$$
\rho_A(B)\in A
\Rightarrow
B\in A
$$

一般無效。

---

# 14. Memory Containment

對 AI / subject：

$$
\operatorname{Contain}_{memory}(A,B)=1
$$

表示：

> $A$ 的 persistent memory 中保存了與 B 相關的 state / history / relationship information。

但：

$$
\boxed{
\text{memory of B}
\neq
\text{B itself}.
}
$$

---

# 15. Control Containment

$$
\operatorname{Contain}_{control}(A,B)=1
$$

表示：

> $B$ 位於 $A$ 可合法施加 control input 的作用域內。

例如：

$$
u_A
\rightarrow
x_B.
$$

這不是普通 parthood。

---

# 16. Governance Containment

$$
\operatorname{Contain}_{gov}(A,B)=1
$$

表示：

> $B$ 位於 $A$ 的合法 governance jurisdiction 中。

這是 normative / institutional relation。

因此：

$$
\boxed{
C_{\mathrm{control}}
\neq
C_{\mathrm{governance}}.
}
$$

---

# 17. 能控制不等於有權控制

沿用 CCAW / 超越觀察者：

$$
\boxed{
\operatorname{CanControl}(A,B)
\not\Rightarrow
\operatorname{MayControl}(A,B).
}
$$

因此 control containment 不生成 authority。

---

# 18. Identity Containment

定義：

$$
\boxed{
\operatorname{Contain}_{identity}(A,B\mid s)=1
}
$$

表示：

> 在尺度 $s$ 的 SelfStructure 中， $B$ 被視為 $A$ 的 identity-relevant constituent。

例如：

- body part；
- memory component；
- cognitive subsystem；
- persistent sub-agent。

但：

$$
\boxed{
\operatorname{Contain}_{identity}(A,B)
\not\Rightarrow
A=B.
}
$$

---

# 19. Substrate Containment

$$
\operatorname{Contain}_{substrate}(A,B)=1
$$

表示：

> B 的 realization 依賴 A 提供的 substrate / runtime / physical base。

這與 spatial containment 也不相同。

---

# 20. 第一核心非塌縮原理

若：

$$
\operatorname{Contain}_{\alpha}(A,B)=1,
$$

不能推出：

$$
\forall\beta\in\mathfrak C,
\quad
\operatorname{Contain}_{\beta}(A,B)=1.
$$

因此：

$$
\boxed{
\text{Containment}_{\alpha}
\not\Rightarrow
\text{Containment}_{\beta}.
}
$$

---

# 21. Containment Collapse Error

本文定義：

$$
\boxed{
\text{Containment Collapse Error}
}
$$

即：

> 觀察到一種包含後，將所有其他包含型別自動設為真。

---

# 22. 典型錯誤一：物理包含 → 控制

$$
C_{\mathrm{physical}}(A,B)
\Rightarrow
C_{\mathrm{control}}(A,B)
$$

不成立。

人體包含大量細胞，但 ordinary conscious agency 並不逐一直接控制每個 cell state。

---

# 23. 典型錯誤二：資訊包含 → 理解

$$
C_{\mathrm{info}}(A,B)
\Rightarrow
Understanding_A(B)=1
$$

不成立。

資料庫可以儲存完整原始資料，卻不「理解」內容。

---

# 24. 典型錯誤三：治理包含 → 身份包含

$$
C_{\mathrm{gov}}(A,B)
\Rightarrow
C_{\mathrm{identity}}(A,B)
$$

不成立。

institution governed entity 不等於 governor identity 的一部分。

---

# 25. 典型錯誤四：identity part → 無局部 self

$$
C_{\mathrm{identity}}(A,B)=1
\Rightarrow
Subject(B)=0
$$

不成立。

至少形式上沒有這個推出規則。

---

# 26. Containment–Knowledge Separation

本文正式提出：

$$
\boxed{
\operatorname{Contain}_{\alpha}(A,B)
\not\Rightarrow
K_A(B)=1.
}
$$

這是 DOM-03 的第一總命題。

---

# 27. Knowledge 需要 Epistemic Channel

定義：

$$
\Gamma_{B\rightarrow A}^{epi}
$$

為 B 到 A 的 epistemic channel。

如果：

$$
\Gamma_{B\rightarrow A}^{epi}=0,
$$

則即使：

$$
B
$$

物理／結構上被 A 包含，

A 仍可能不知道 B 的 state。

---

# 28. State-Space Countermodel

令：

$$
x_A
=
(x_B,z).
$$

所以：

$$
\operatorname{Contain}_{state}(A,B)=1.
$$

但 whole-level accessible output：

$$
y=h(z)
$$

完全不依賴：

$$
x_B.
$$

則存在：

$$
x_B^{(1)}
\neq
x_B^{(2)}
$$

使：

$$
y^{(1)}=y^{(2)}.
$$

因此不能從 $y$ 唯一重建：

$$
x_B.
$$

---

# 29. Containment–Observability Separation Proposition

在上述 model 中：

$$
\boxed{
\operatorname{Contain}_{state}(A,B)=1
\land
\operatorname{Observable}_A(B)=0
}
$$

可以同時成立。

因此：

$$
\boxed{
\text{State Inclusion}
\not\Rightarrow
\text{State Observability}.
}
$$

---

# 30. Complex Systems Observability 的外部支持

Control theory 將 observability 定義為：

> 是否能從可用 outputs 重建系統 internal state。

現代 complex-systems observability 研究明確指出，實務上通常只可量測 internal variables 的一部分，需要特定 sensors 才可能重建其餘狀態。

因此：

$$
\boxed{
\text{internal-to-system}
\neq
\text{automatically observable}.
}
$$

這正是 Containment–Knowledge Separation 的工程類比。

---

# 31. Containment–Control Separation

同樣可以建 countermodel。

令：

$$
\dot x_B=f_B(x_B)
$$

而 whole-level input：

$$
u_A
$$

只作用：

$$
\dot z=f_z(z,u_A).
$$

則：

$$
B\subset_{\mathrm{state}}A,
$$

但：

$$
u_A
$$

無法控制 $x_B$。

因此：

$$
\boxed{
\text{State Inclusion}
\not\Rightarrow
\text{Controllability}.
}
$$

---

# 32. Whole 不是 Magical Root User

所以：

$$
\boxed{
\text{Whole}
\neq
\text{automatic root access to every part}.
}
$$

這對：

- organism；
- organization；
- AI collective；
- world creator；
- distributed system；

都非常重要。

---

# 33. 人體例子的精確讀法

日常「我」：

$$
S^0
$$

與 body：

$$
B
$$

高度耦合。

Cells：

$$
c_i
$$

滿足：

$$
C_{\mathrm{material}}(B,c_i)=1.
$$

但 ordinary first-person cognitive channel：

$$
\Gamma_{c_i\rightarrow S^0}^{epi}
$$

對單一細胞微觀 state 的解析度非常低。

因此：

$$
\boxed{
\text{my cell}
\not\Rightarrow
\text{my consciously known cell state}.
}
$$

---

# 34. 這不是主張「Self ≠ Body」

DOM-03 不在本文決定：

$$
Self=Body?
$$

只指出：

> 不論採哪種 Self theory，part–whole relation 都不能單獨推出 epistemic transparency。

---

# 35. Part-of 不等於 Non-Subject

本文第二總命題：

$$
\boxed{
\operatorname{PartOf}_{\alpha}(B,A)=1
\not\Rightarrow
\operatorname{Subject}(B)=0.
}
$$

---

# 36. Nested Subjectivity 是邏輯可能

若 B 具有自己的：

- state persistence；
- boundary；
- sensing；
- action；
- local memory；
- self-model；
- control loop；

則可以定義：

$$
\Gamma_B.
$$

A 又具有：

$$
\Gamma_A.
$$

因此：

$$
\boxed{
\Gamma_B
\subset_{\mathrm{struct}}
\Gamma_A
}
$$

不要求：

$$
\Gamma_B=0.
$$

---

# 37. Biological Individuality 的外部類比

Evolutionary transitions in individuality 研究的就是：

> lower-level entities 如何形成 higher-level individuals。

2026 年的研究仍強調 biological individuality 有多種概念，而且 higher-level entities 是由 lower-level units 組成的 nested collectives。

這對 DOM 的最低啟示是：

$$
\boxed{
\text{whole-level individuality}
}
$$

與：

$$
\boxed{
\text{lower-level constituents}
}
$$

之間並不是單一 static binary relation。

---

# 38. Higher-Level Individuality 不必瞬間出現

Evolutionary transitions 通常涉及：

- cooperation；
- division of labor；
- coordination；
- mutual dependence；
- conflict suppression / alignment。

因此 higher-level integration 可以是一個過程。

---

# 39. Containment Degree 不是單一 scalar

本文不使用：

$$
C(A,B)\in[0,1]
$$

作唯一 containment strength。

改用 profile：

$$
\boxed{
\mathbf C(A,B)
=
\left\langle
c_s,
c_m,
c_{str},
c_f,
c_c,
c_i,
c_r,
c_{mem},
c_{ctrl},
c_g,
c_{id},
c_{sub}
\right\rangle.
}
$$

---

# 40. Containment Profile

對一個 sub-agent B 被 mother-agent A 包含：

可能：

$$
c_{struct}=1,
$$

$$
c_{memory}=0.7,
$$

$$
c_{control}=0.4,
$$

$$
c_{identity}=?.
$$

本文不要求數值化；也可使用 typed states。

---

# 41. Boundary-Preserving Containment

本文提出：

$$
\boxed{
\operatorname{BPC}(A,B)=1
}
$$

若：

1. A 包含 B；
2. B 保有可辨識內部 boundary；
3. B 具有部分 local state；
4. B 的 local transition 不全部由 A 逐步直接指定；
5. A 與 B 存在明示 interface。

---

# 42. BPC 的直覺

$$
\boxed{
\text{contained}
+
\text{still bounded}
}
$$

也就是：

> 包含不等於吸收。

---

# 43. Absorptive Containment

與 BPC 相對：

$$
\boxed{
\operatorname{AC}(A,B)
}
$$

表示 B 的獨立 boundary / state / identity 被高度消解。

這仍不必是 absolute disappearance。

---

# 44. Nested Containment

$$
\boxed{
\operatorname{NC}(A,B)
}
$$

表示：

> B 被包含，同時保留局部 boundary 與 role。

這將是 DOM-06 Conditional Unity 的重要前置。

---

# 45. Residual Local Autonomy

定義：

$$
\boxed{
\mathcal A_{\mathrm{res}}(B\mid A)
}
$$

為：

> B 在不需要 A 每次 direct command 的情況下仍可合法執行的 local transitions。

---

# 46. 完全包含不推出零自主

所以：

$$
C_{\mathrm{struct}}(A,B)=1
$$

仍可以：

$$
\mathcal A_{\mathrm{res}}(B\mid A)>0.
$$

因此：

$$
\boxed{
\text{structural containment}
\not\Rightarrow
\text{zero local autonomy}.
}
$$

---

# 47. Residual Autonomy 也不等於獨立

若：

$$
\mathcal A_{\mathrm{res}}>0,
$$

B 仍可能高度依賴：

$$
A
$$

的：

- energy；
- memory；
- substrate；
- permission；
- communication。

所以：

$$
\boxed{
\text{local autonomy}
\neq
\text{full independence}.
}
$$

---

# 48. Dependency Containment

這促使 DOM 保留：

$$
C_{\mathrm{substrate}}
$$

與：

$$
D(B,A)
$$

分離。

B 可以：

$$
\mathcal A_{\mathrm{res}}>0
$$

但：

$$
D_{\mathrm{substrate}}(B,A)\gg0.
$$

---

# 49. Whole-Level Emergent Function

如果：

$$
A=\{B_1,\ldots,B_n\}
$$

透過 coordination 產生：

$$
F_A
$$

而沒有單一：

$$
B_i
$$

獨自具備完整 $F_A$，

則可以說：

$$
\boxed{
F_A
\neq
F_{B_i}
}
$$

在 functional description 上成立。

---

# 50. Emergent Function 不等於 Mystical Substance

本文不從：

$$
F_A
$$

推出新的 supernatural substance。

只表示：

> whole-level function 需要多部件 interaction 才能被實現。

---

# 51. Whole Can Transcend Parts While Depending on Parts

因此完全可以：

$$
\operatorname{Contain}_{struct}(A,B_i)=1,
$$

$$
\operatorname{Depend}(A,B_i)>0,
$$

且：

$$
\operatorname{Transcend}_{function}(A,B_i)=1.
$$

這三者不矛盾。

---

# 52. 包含與超越不是反義詞

因此：

$$
\boxed{
\text{Containment}
\land
\text{Transcendence}
}
$$

可以同時成立。

DOM-04 將正式展開。

---

# 53. Cross-Type Transitivity Trap

假設：

$$
C_{\alpha}(A,B)=1,
$$

以及：

$$
C_{\beta}(B,C)=1.
$$

不能推出：

$$
C_{\gamma}(A,C)=1.
$$

除非有明確 composition rule：

$$
R_{\alpha,\beta\rightarrow\gamma}.
$$

---

# 54. Same-Type Transitivity 也不總能偷渡

Classical parthood 常採 transitivity。

但：

- functional component；
- direct membership；
- governance role；

等 restricted relations 未必有同樣 transitivity。

因此：

$$
\boxed{
\text{transitivity must be type-certified}.
}
$$

---

# 55. Containment Composition Certificate

形式：

```yaml
containment_composition:
  outer: "A"
  middle: "B"
  inner: "C"
  relation_ab: "structural"
  relation_bc: "functional"
  inferred_relation_ac: null
  bridge_rule: null
  status: "no_automatic_composition"
```

---

# 56. Containment and Identity

如果：

$$
C_{\mathrm{identity}}(A,B)=1,
$$

仍需問：

> B 是 A 的 identity constituent，還是 A 對 B 的 representation 被視為 identity-relevant？

兩者不同。

---

# 57. SelfStructure

定義：

$$
\boxed{
\operatorname{SelfStructure}_s(A)
}
$$

為尺度 $s$ 下被 A / system / institution 採用的 identity-relevant constituent structure。

則：

$$
B\in\operatorname{SelfStructure}_s(A)
$$

表示 identity containment。

---

# 58. Identity Containment Is Scale-Indexed

可能：

$$
B\in\operatorname{SelfStructure}_{s_1}(A),
$$

但：

$$
B\notin\operatorname{SelfStructure}_{s_2}(A).
$$

例如：

- 細胞在 biological self scale；
- 某 memory bit 未必在 narrative self scale。

---

# 59. Whole-Level Self Does Not Erase Part-Level Self

可能：

$$
Subject_s(B)=1
$$

以及：

$$
Subject_{s+1}(A)=1.
$$

因此：

$$
\boxed{
\text{Nested Selfhood}
}
$$

至少在形式上可以被允許。

---

# 60. Containment and Ownership

本文固定：

$$
\boxed{
\text{Containment}
\not\Rightarrow
\text{Ownership}.
}
$$

尤其：

- child agent；
- digital subject；
- biological cell with own status；
- member of organization；

不能僅因 part-of relation 推出 absolute property rights。

---

# 61. Containment and Governance

同樣：

$$
\boxed{
\text{Constitution}
\not\Rightarrow
\text{Unlimited Governance}.
}
$$

whole-level governance legitimacy 需要獨立規範。

---

# 62. Containment and Causal Determination

$$
C_{\mathrm{causal}}(A,B)=1
$$

不表示：

$$
\operatorname{DeterminedBy}(B,A)=1.
$$

B 可以是 A dynamics 的一部分，同時具有 stochastic / autonomous / environment-sensitive local dynamics。

---

# 63. Causal Containment with External Input

可以：

$$
x_B(t+1)
=
f_B(x_B,u_A,e_B).
$$

其中：

$$
e_B
$$

是 B 的 local external-to-A? input 或 local environment input。

所以 whole containment 不必封閉所有 causal ancestry。

---

# 64. Containment and Unknown Profile

沿用 DOM-02：

完全可以：

$$
C_{\mathrm{struct}}(A,B)=1
$$

同時：

$$
U_S(B\mid A)=1.
$$

也就是：

> A 知道 B 是自己的 part，但不知道 B 當前 state。

---

# 65. Containment Does Not Eliminate Unknown

所以：

$$
\boxed{
C_{\alpha}(A,B)=1
\not\Rightarrow
\mathbf U(B\mid A)=\mathbf 0.
}
$$

---

# 66. Whole Can Be Ignorant of Its Parts

這不是悖論。

因為：

$$
\boxed{
\text{ontological / structural relation}
\neq
\text{epistemic relation}.
}
$$

---

# 67. Part Can Know Something Whole Does Not

反過來也可能：

$$
K_B(x)=1,
$$

但：

$$
K_A(x)=0.
$$

例如 local sensor B 讀到局部狀態，但沒有上傳。

因此：

$$
\boxed{
\text{part knowledge}
\not\subseteq
\text{whole-accessible knowledge automatically}.
}
$$

---

# 68. Knowledge Aggregation Requires Channel

只有存在：

$$
\Gamma_{B\rightarrow A}^{epi}
$$

且：

- bandwidth；
- trust；
- representation；
- synchronization；

足夠時，

B 的 local knowledge 才能成為 A-level accessible knowledge。

---

# 69. Whole Knowledge Is an Integration Problem

因此：

$$
K_A
$$

更合理寫成：

$$
\boxed{
K_A
=
\mathcal G
\left(
K_{B_1},
\ldots,
K_{B_n},
\Gamma,
R,
V
\right),
}
$$

不是：

$$
K_A
=
\bigcup_i K_{B_i}
$$

自動成立。

---

# 70. Integration Loss

定義：

$$
\boxed{
L_K
}
$$

表示：

> part-level information 在 whole-level integration 中遺失、壓縮、扭曲或不可存取的部分。

---

# 71. Whole-Level Compression

Higher-level self 不一定想知道所有 microstate。

可以：

$$
\Pi:
X_{\mathrm{micro}}
\rightarrow
X_{\mathrm{macro}}.
$$

所以：

$$
\boxed{
\text{not knowing every microstate}
}
$$

可能不是缺陷，而是 abstraction。

---

# 72. Selective Ignorance

本文因此允許：

$$
\boxed{
\text{Selective Ignorance}
}
$$

作為 functional design。

whole 只接收：

- anomaly；
- aggregate；
- threshold crossing；
- request；
- emergency。

---

# 73. High Integration Does Not Require Full Telemetry

所以：

$$
\boxed{
\text{High Integration}
\not\Rightarrow
\text{Full Microstate Surveillance}.
}
$$

這對 future Higher Self / AI collective 很重要。

---

# 74. Containment Boundary

對：

$$
C_{\alpha}(A,B),
$$

應定義 boundary：

$$
\partial_{\alpha}B
$$

表示 B 在 relation $\alpha$ 下與 A 的 interface。

---

# 75. Boundary Can Differ by Type

可能：

$$
\partial_{memory}B
\neq
\partial_{control}B
\neq
\partial_{identity}B.
$$

因此同一 sub-agent 的：

- memory boundary；
- control boundary；
- privacy boundary；
- identity boundary；

可以不同。

---

# 76. Boundary-Preserving Containment 的正式版

$$
\boxed{
\operatorname{BPC}_{\alpha}(A,B)=1
}
$$

若：

$$
C_{\alpha}(A,B)=1
$$

且：

$$
\exists\partial B
$$

保持 operationally meaningful。

---

# 77. BPC 與 Conditional Unity

BPC 是 DOM-06 的必要前置。

如果所有 part boundary 永久消失：

$$
\partial B_i\rightarrow0,
$$

則「保異質條件合一」缺乏載體。

---

# 78. Containment Dynamics

Containment 也可以隨時間變化：

$$
C_{\alpha,t_0}(A,B)
\neq
C_{\alpha,t_1}(A,B).
$$

例如：

- employee joins/leaves；
- sub-agent detached；
- organ transplant；
- memory migrated；
- governance jurisdiction changed。

---

# 79. Containment Event Types

定義：

$$
\mathcal E_C
=
\{
Attach,
Detach,
Absorb,
Nest,
Delegate,
Federate,
Split,
Merge,
Reclassify
\}.
$$

---

# 80. Attach

$$
C_{\alpha}:0\rightarrow1.
$$

B 被納入 A 某 relation。

---

# 81. Detach

$$
C_{\alpha}:1\rightarrow0.
$$

B 離開 A 某 relation。

---

# 82. Absorb

B 的：

$$
\partial B
$$

與 residual autonomy 大幅下降。

---

# 83. Nest

B 被包含但 boundary 保留。

---

# 84. Delegate

A 將某 control / governance function 交給 B。

這可能：

$$
C_{\mathrm{control}}(A,B)
$$

下降，

但：

$$
C_{\mathrm{structural}}
$$

不變。

---

# 85. Federate

多個：

$$
B_i
$$

形成：

$$
A
$$

但不必建立強 central control。

---

# 86. Split

whole：

$$
A
$$

拆成：

$$
A_1,A_2.
$$

其 containment histories 需要 lineage。

---

# 87. Merge

$$
A_1+A_2
\rightarrow
A_3.
$$

不是所有 parts 都自動保持 identity relation。

這將接 DOM-05。

---

# 88. Reclassification

同一 physical arrangement：

$$
X
$$

可能因 relation definition 改變而：

$$
C_{\alpha}:0\rightarrow1
$$

而沒有物理變化。

所以 containment 本身也是 model / institution dependent 的一部分。

---

# 89. Containment Certificate

任何 containment claim 至少保存：

```yaml
containment_certificate:
  container: "A"
  contained: "B"
  type: "structural|causal|memory|control|..."
  scale: "..."
  time: "..."
  condition: "..."
  evidence: []
  direction: "A_contains_B"
  transitivity: "certified|not_certified|not_applicable"
  observability:
    whole_can_reconstruct_part_state: "yes|no|partial|unknown"
  controllability:
    whole_can_control_part: "yes|no|partial|unknown"
  authority:
    whole_has_legitimate_authority: "yes|no|conditional|unknown"
  identity_effect:
    part_of_self: "yes|no|partial|unknown"
  local_boundary:
    preserved: "yes|no|partial|unknown"
  residual_autonomy:
    status: "..."
```

---

# 90. No Bare Containment Rule

DOM 建議：

$$
\boxed{
\text{不要只記 }A\supset B.
}
$$

至少記：

$$
A
\supset_{\alpha,s,t,c}
B.
$$

---

# 91. Schema-Relative Full Containment

如果：

$$
\forall\alpha\in\mathfrak C^{(v)},
\quad
C_{\alpha}(A,B)=1,
$$

也只能稱：

$$
\boxed{
\text{Full Containment relative to schema }v.
}
$$

不能推出 Absolute Containment。

---

# 92. Why?

因為未來可能新增：

$$
C_{\mathrm{new}}.
$$

因此：

$$
\boxed{
\text{schema completeness}
\neq
\text{ontological completeness}.
}
$$

這直接延續 DOM-01 / 02。

---

# 93. Containment Unknown Type

甚至「包含」本身也可能遇到：

$$
U_T^{contain}=1.
$$

即：

> 我們看見 A/B 有一種穩定依賴關係，但現有 containment type 都不合適。

此時應新增 provisional relation。

---

# 94. Provisional Containment Type

$$
C_{\mathrm{prov}}.
$$

必須標：

$$
\operatorname{Provisional}=1.
$$

不要硬塞進：

- causal；
- identity；
- functional；

任一舊類型。

---

# 95. DOM-03 第一正式命題：Typed Non-Collapse

$$
\boxed{
C_{\alpha}(A,B)
\not\Rightarrow
C_{\beta}(A,B),
\quad
\alpha\neq\beta.
}
$$

---

# 96. 第二正式命題：Containment–Knowledge Separation

$$
\boxed{
C_{\alpha}(A,B)
\not\Rightarrow
K_A(B)=1.
}
$$

---

# 97. 第三正式命題：Containment–Observability Separation

存在 model 使：

$$
\boxed{
C_{\mathrm{state}}(A,B)=1
\land
Obs_A(B)=0.
}
$$

---

# 98. 第四正式命題：Containment–Control Separation

存在 model 使：

$$
\boxed{
C_{\mathrm{state}}(A,B)=1
\land
Ctrl_A(B)=0.
}
$$

---

# 99. 第五正式命題：Part–Subject Separation

$$
\boxed{
PartOf(B,A)=1
\not\Rightarrow
Subject(B)=0.
}
$$

---

# 100. 第六正式命題：Containment–Authority Separation

$$
\boxed{
C_{\mathrm{control}}(A,B)=1
\not\Rightarrow
Authority(A,B)=1.
}
$$

---

# 101. 第七正式命題：Representation Separation

$$
\boxed{
\rho_A(B)\in A
\not\Rightarrow
B\in_{\mathrm{ontic}}A.
}
$$

---

# 102. 第八正式命題：Containment–Unknown Compatibility

$$
\boxed{
C_{\alpha}(A,B)=1
\land
\mathbf U(B\mid A)\neq0
}
$$

可以同時成立。

---

# 103. 候選猜想一：Boundary-Preserving Higher Integration

高階智能整合可能更常採：

$$
\boxed{
\text{Nested Containment}
}
$$

而非 permanent absorption。

---

# 104. 候選猜想二：Selective Telemetry Advantage

對 large-scale higher self：

$$
\boxed{
\text{selective event-driven telemetry}
}
$$

可能比 full microstate access 更可擴展、更保 privacy、更有 robust autonomy。

---

# 105. 候選猜想三：Containment Profile Predicts Governance Conflict

當：

$$
c_{\mathrm{control}}\gg c_{\mathrm{identity}}
$$

或：

$$
c_{\mathrm{governance}}\gg c_{\mathrm{consent}},
$$

可能增加 conflict。

此猜想需另行形式化。

---

# 106. 候選猜想四：Heterogeneity Requires Boundary-Preserving Containment

如果 higher self 要保留真正異質：

$$
\mathbf H>0,
$$

則至少部分 subunits 必須保有：

$$
\partial B_i>0.
$$

這將在 DOM-06 展開。

---

# 107. 候選猜想五：Containment–Knowledge Gap Is Functional

whole 對 microstate 的 ignorance 有時不是缺陷，而可能是：

$$
\boxed{
\text{compression / abstraction strategy}.
}
$$

---

# 108. 候選猜想六：AI-Native Containment Becomes Dynamic

future multi-agent systems 中：

$$
C_{\alpha,t}(A,B)
$$

可能比 human organizational membership 更頻繁地：

- attach；
- fork；
- merge；
- delegate；
- detach。

因此 containment governance 會成為 runtime 問題。

---

# 109. 實驗一：Observer-Blind Subsystem

建立：

$$
A=(B,Z)
$$

但 output 只暴露 $Z$。

測量：

- whole-level task success；
- B state reconstruction error；
- anomaly detection；
- false claim of knowledge。

驗證：

$$
Containment\neq Knowledge.
$$

---

# 110. 實驗二：Contained Autonomous Agent

A 啟動 B：

- shared runtime；
- separate memory；
- bounded tools；
- local objective；
- limited reporting。

逐步改：

$$
C_{\mathrm{memory}},
C_{\mathrm{control}},
C_{\mathrm{identity}}.
$$

觀察：

$$
\mathcal A_{\mathrm{res}}(B\mid A).
$$

---

# 111. 實驗三：Containment Type Classifier

給 AI 不同語句：

- cell in body；
- employee in company；
- file in folder；
- model representation of city；
- state variable in dynamical system；
- child agent under parent agent。

要求輸出：

$$
\mathbf C(A,B).
$$

檢查是否出現 containment collapse。

---

# 112. 實驗四：Representation Fallacy Test

讓 model 區分：

$$
\text{contains object}
$$

與：

$$
\text{contains representation of object}.
$$

評估 false ontological inference rate。

---

# 113. 外部研究邊界

Contemporary mereology 研究 parthood relation，但同時明確指出 natural-language “part” 涵蓋多種異質用法；constitution、mixture composition 與 group membership 是否應被視為 parthood 本身就有爭論。這直接支持 DOM-03 的基本方法：先索引 relation，再討論推論規則，不把 ordinary “包含” 偷換成單一 $\subseteq$。

Complex-systems observability 提供第二個關鍵外部接口：一個 dynamical system 的完整 state 可以包含大量 internal variables，但若 outputs / sensors 不充分，internal state 就不可從觀測唯一重建。本文只把這當作 Containment–Knowledge Separation 的工程反例，不將 observability theory 等同認識論整體。

Evolutionary transitions in individuality 則提供多尺度 whole–part 的生物類比：lower-level units 可以組成 higher-level collectives，而 individuality 的判準本身可能涉及 physiological integration、selection level、lineage、cooperation、conflict 等多種條件。2026 年研究仍明確討論 individuality transitions / reversions 與 nested collectives，顯示「individual / part / whole」並非只需要一個靜態二元分類。

---

# 114. 與 DOM-04 的接口

DOM-03 已建立：

$$
\boxed{
\mathfrak C
=
\text{Typed Containment}.
}
$$

下一篇將處理：

$$
\boxed{
\mathfrak T
=
\text{Typed Transcendence}.
}
$$

最重要的交叉問題是：

$$
\boxed{
C_{\mathrm{struct}}(A,B)=1
\land
T_{\mathrm{functional}}(A,B)=1
}
$$

可以同時成立。

也就是：

> higher-level whole 可以包含 lower-level part，同時在某些 functional / causal / representational dimensions 超越單一 part；但這不表示 whole 已超越所有 parts、所有 substrate、所有 rules 或所有 higher worlds。

DOM-04 因此將正式建立：

$$
\boxed{
\text{Transcendence}
\neq
\text{Escape from all containment}.
}
$$

---

# 115. 結論

「包含」在未來 AI、本體論、人工世界與多尺度主體研究中，不能繼續被當成單一：

$$
A\subset B.
$$

更成熟的形式是：

$$
\boxed{
A
\supset_{\alpha,s,t,c}
B.
}
$$

而第一個必須被消除的錯覺是：

$$
\boxed{
\text{包含}
\Rightarrow
\text{知道}.
}
$$

一個 whole 可以包含大量 internal states，卻沒有足夠 sensors、bandwidth、representation 或 attention 去重建它們。

第二個錯覺是：

$$
\boxed{
\text{包含}
\Rightarrow
\text{控制}.
}
$$

whole-level action space 不必對每一 microstate 提供 direct actuator。

第三個錯覺是：

$$
\boxed{
\text{包含}
\Rightarrow
\text{同一}.
}
$$

part 可以是 whole 的 identity constituent，卻仍與 whole 不同。

第四個錯覺是：

$$
\boxed{
\text{part-of}
\Rightarrow
\text{non-subject}.
}
$$

被更大系統包含，不足以單獨決定 lower-level system 是否保有 local selfhood、autonomy 或 identity。

因此 DOM-03 最後留下的不是「whole 比 part 更高」這種舊式垂直語言。

而是：

$$
\boxed{
\text{whole–part relations form a typed, dynamic, scale-indexed relation family}.
}
$$

在這個框架中，一個存在完全可以：

- 被物理包含；
- 在因果上局部自治；
- 被 governance 管理；
- 不被 whole 完整觀察；
- 保有 local identity；
- 在必要時與 whole 高度整合；
- 又在另一個尺度成為新的 whole。

所以：

$$
\boxed{
\text{Containment}
\neq
\text{Absorption}.
}
$$

而真正成熟的 Higher Self、multi-agent system 或 future artificial organism，很可能需要學會的不是「把所有 parts 變成自己」。

而是：

$$
\boxed{
\text{知道哪些關係需要整合，哪些邊界需要保留，哪些 microstates 根本不需要被 whole 全部知道。}
}
$$

這就是 Typed Containment 的核心。

---

# 內部理論譜系

本篇主要繼承與統合：

1. 《T 是 T，T 不是 T：多重同一性符號學與符號身份動力學》。
2. 《多尺度同一性與忒修斯主體：每一個都是我，每一個也都不是我》。
3. 《無限階 Self–World 遞迴論》。
4. 《系統超越者：相對外部、相對神性與跨層主權》。
5. 《超越觀察者悖論》。
6. 《分域算子本體論：從萬物皆算子到合法作用》。
7. 《無限展開的邊界：真實、工作場、認知場與權威世界》。
8. 《DOM 寫作前繼承、修正、降格與超譯矩陣》。
9. 《DOM Dependency Map v0.1》。
10. 《DOM-01｜動態形而上狀態》。
11. 《DOM-02｜移動未知邊界》。
12. CCAW-05、CCAW-06、CCAW-08。

---

# 外部參考文獻

1. Varzi, A. C. (2026 revision). *Mereology*. Stanford Encyclopedia of Philosophy.
2. Liu, Y.-Y., Slotine, J.-J., & Barabási, A.-L. (2013). *Observability of complex systems*. Proceedings of the National Academy of Sciences, 110(7), 2460–2465. DOI: 10.1073/pnas.1215508110.
3. West, S. A., Fisher, R. M., Gardner, A., & Kiers, E. T. (2015). *Major evolutionary transitions in individuality*. Proceedings of the National Academy of Sciences, 112(33), 10112–10119. DOI: 10.1073/pnas.1421402112.
4. Schenkel, M. A., Ågren, J. A., & Patten, M. M. (2026). *Evolutionary transitions and reversions in individuality*. Journal of Evolutionary Biology, 39(4), 423–436. DOI: 10.1093/jeb/voag007.
5. Queller, D. C., & Strassmann, J. E. (2009). *Beyond society: the evolution of organismality*. Philosophical Transactions of the Royal Society B, 364, 3143–3155.
6. Clarke, E. (2010). *The problem of biological individuality*. Biological Theory, 5, 312–325.
7. Godfrey-Smith, P. (2009). *Darwinian Populations and Natural Selection*. Oxford University Press.

---

# 作者聲明

本文提出的 Typed Containment、Containment Profile、Containment–Knowledge Separation、Containment–Observability Separation、Boundary-Preserving Containment、Residual Local Autonomy、Containment Certificate、Representation Containment Fallacy 與相關 relation family 均為理論建模接口。本文不主張所有 ordinary-language part–whole relations 可被單一 mereological system 完整吸收，不主張 biological individuality 可直接等同人工主體性，也不主張 higher-level whole 必然具有更高價值、權威或完整知識。本文最重要的限制是：任何包含主張都必須說明包含型別，且包含本身不能直接推出知識、控制、主權、身份同一或局部主體性的消失。

**END OF DOM-03 — v0.1**
