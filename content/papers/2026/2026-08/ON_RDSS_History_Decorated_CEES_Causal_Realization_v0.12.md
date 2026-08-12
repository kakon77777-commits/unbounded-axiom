# Operator-Native RDSS：History-Decorated CEES 與 Causal Realization
## Disjunctive Causes, Enabling Witnesses, Cause-Sensitive Quotients, and HP/HHP Regression Targets

**版本：** v0.12 Working Proof/Checker Draft  
**日期：** 2026-08-10  
**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**定位：** General CEES 的歷史裝飾化／因果實現身份／Branch Quotient 再精化  
**前置：** ON-RDSS v0.9–v0.11

---

# 摘要

v0.11 已在 finite prime-event-structure 子域中建立：

$$
(C_1,f,C_2)
$$

形式的 hp/hhp-like Branch Quotient checker。

但 General CEES：

$$
\mathcal E_G
=
(E,Con,\vdash,\lambda,Ty,Auth,Cert,Ver)
$$

允許：

$$
\{a\}\vdash c,
\qquad
\{b\}\vdash c,
$$

即同一表面事件 $c$ 可以具有多個替代原因。

此時裸 configuration：

$$
C=\{a,b,c\}
$$

不足以唯一決定歷史因果結構。

本版因此將 CEES runtime configuration 升級為：

$$
\boxed{
\widehat C
=
(
C,
\pi,
\le_\pi,
v
).
}
$$

其中：

- $C$：已發生的表面 events；
- $\pi$：每次 event occurrence 使用的 enabling witness；
- $\le_\pi$：由 witness choices 誘導的 concrete causal order；
- $v$：EventSemanticsVersion。

同時引入雙層事件身份：

$$
\boxed{
\widetilde e
=
(e,\kappa,v)
}
$$

其中：

- $e$：surface semantic event；
- $\kappa$：本次 causal/enabling witness；
- $v$：語義版本。

投影：

$$
\boxed{
q(\widetilde e)=e.
}
$$

因此：

$$
\boxed{
\text{Surface Event Identity}
\neq
\text{Causal Realization Identity}.
}
$$

這使 ON-RDSS 可以保留「同一事件、不同因果歷史」，而不必把語義事件本身複製成互不相關的對象。

---

# 1. 文獻校正：HP 與 HHP 的差異確實需要 Backtracking

經典 HP/HHP 文獻明確指出：

- HP 主要保持 forward runs 的 causal history；
- HHP 再要求 backtracking 後的匹配仍然成立。

Fröschle–Hildebrandt 的標準例子給出兩個：

$$
HPB
$$

但非：

$$
HHPB
$$

的 1-safe nets。

核心機制：

1. 兩邊都有平行 $a,b$ ；
2. forward HP matching 可以依 run 中 $a,b$ 出現順序選不同映射；
3. 額外的 $c/d$ continuation 迫使某個 forward mapping；
4. HHP 回退其中一個平行事件後，留下的 mapping 進入一個兩邊 future 不再匹配的狀態；
5. 因而 hereditary/backtracking 條件失敗。

此例成為 ON-RDSS checker 的正式外部 regression target。

---

# 2. v0.11 的限制

Prime Event Structure 中，每個 event 有固定 causal past：

$$
Past(e).
$$

因此 configuration：

$$
C
$$

本身足以導出：

$$
\le_C.
$$

但 General CEES 不成立。

如果：

$$
Alt(c)
=
\{
\{a\},
\{b\}
\},
$$

則同一：

$$
C=\{a,b,c\}
$$

至少可存在兩個 causal histories：

$$
a<c,
\qquad
b\parallel c\text{ except chosen cause},
$$

或：

$$
b<c.
$$

所以：

$$
\boxed{
RawConfiguration
\neq
ConcreteHistory.
}
$$

---

# 3. Enabling Witness

定義：

$$
\boxed{
\kappa
\in
Witness_v(e)
}
$$

當：

$$
\kappa\vdash_v e.
$$

若：

$$
e
$$

initially enabled：

$$
\kappa=\varnothing.
$$

注意：

$$
MissingWitness
\neq
\varnothing.
$$

前者是 disabled / undefined，

後者是 explicit initial enabling。

---

# 4. Proving History

定義：

$$
\boxed{
\pi
=
[
(e_1,\kappa_1),
\ldots,
(e_n,\kappa_n)
].
}
$$

合法條件：

$$
\boxed{
\kappa_i
\subseteq
\{e_1,\ldots,e_{i-1}\}
}
$$

且：

$$
\boxed{
\kappa_i\vdash_v e_i.
}
$$

如果有 consistency：

$$
\{e_1,\ldots,e_i\}\in Con_v
$$

亦需逐 prefix 成立。

---

# 5. Induced Causal Order

由 proving history 定義 direct witness dependency：

$$
\boxed{
e_j
\prec_\pi^{0}
e_i
\iff
e_j\in\kappa_i.
}
$$

令：

$$
\boxed{
\prec_\pi
=
(\prec_\pi^{0})^+
}
$$

為 transitive closure。

因此：

$$
\widehat C
=
(
C,\pi,\prec_\pi,v
).
$$

---

# 6. Causal Realization

表面事件：

$$
e
$$

在不同 histories 中可能有不同 occurrence：

$$
\boxed{
\widetilde e_1=(e,\kappa_1,v),
}
$$

$$
\boxed{
\widetilde e_2=(e,\kappa_2,v).
}
$$

且：

$$
\kappa_1\neq\kappa_2.
$$

但：

$$
q(\widetilde e_1)
=
q(\widetilde e_2)
=
e.
$$

---

# 7. 與 Causal Unfolding 的接口

既有 causal-unfolding 研究指出：

- general event structure 可允許一個 event 有 disjunctive causes；
- 同一 event 的不同 causal histories 有時需要被重新具體化；
- 可藉由「prime cause occurrence + equivalence class」分離 event identity 與 concrete causal history。

ON-RDSS 的：

$$
\widetilde e=(e,\kappa,v)
$$

採用相鄰思想，但額外帶：

- version；
- authority；
- certificate；
- residual；
- runtime history identity。

---

# 8. Same Event Set / Different History

Toy CEES：

$$
\varnothing\vdash a,
$$

$$
\varnothing\vdash b,
$$

$$
\{a\}\vdash c,
$$

$$
\{b\}\vdash c.
$$

兩個 histories：

$$
\pi_A
=
[
(a,\varnothing),
(b,\varnothing),
(c,\{a\})
]
$$

以及：

$$
\pi_B
=
[
(a,\varnothing),
(b,\varnothing),
(c,\{b\})
].
$$

兩者 raw configuration 相同：

$$
\boxed{
C_A=C_B=\{a,b,c\}.
}
$$

---

# 9. 但 Causal Order 不同

History A：

$$
\boxed{
a\prec_{\pi_A}c.
}
$$

History B：

$$
\boxed{
b\prec_{\pi_B}c.
}
$$

因此：

$$
\boxed{
\prec_{\pi_A}
\neq
\prec_{\pi_B}.
}
$$

有限 checker 實際得到兩種 distinct causal orders。

---

# 10. Causal Realization ID

可以定義：

$$
\boxed{
RID(\widehat C)
=
Hash(
[(e_i,\kappa_i,v)]
).
}
$$

它不是 semantic identity 的唯一來源，

而是 trace/replay 用的 concrete realization fingerprint。

Toy：

$$
RID(\widehat C_A)
\neq
RID(\widehat C_B).
$$

---

# 11. Backward-Ready Difference

對 induced causal poset，

可回退的 events 為 maximal events：

$$
\boxed{
Max(\widehat C)
=
\{
e\in C
\mid
\nexists e'\in C,\;
e\prec_\pi e'
\}.
}
$$

History A：

$$
Max(\widehat C_A)
=
\{b,c\}.
$$

History B：

$$
Max(\widehat C_B)
=
\{a,c\}.
$$

若 $a,b$ profiles 不同，

backward-ready profile 立即不同。

---

# 12. 這對 HHP 的意義

HHP 的關鍵不是只看：

$$
C_A=C_B.
$$

而是：

> 當你把某個 maximal past event 撤回時，兩邊是否仍能維持匹配？

因此 general CEES 若不保存：

$$
\pi,\prec_\pi
$$

根本無法正確定義 history-preserving backtracking。

---

# 13. Governed History Isomorphism

兩個 decorated histories：

$$
\widehat C_1,
\widehat C_2
$$

的映射：

$$
f:C_1\to C_2
$$

至少要求：

## Event profile

$$
\Lambda_1(e)
=
\Lambda_2(f(e)).
$$

ON profile 包括：

$$
(
Label,
Type,
Authority,
Residual
).
$$

## Causal realization order

$$
\boxed{
e\prec_{\pi_1}e'
\iff
f(e)\prec_{\pi_2}f(e').
}
$$

---

# 14. Profile-Relative Quotient

Toy 中若：

$$
Profile(a)\neq Profile(b),
$$

則：

$$
\widehat C_A
\not\cong
\widehat C_B.
$$

Checker：

$$
\boxed{
GovernedProfileIsomorphic=false.
}
$$

---

# 15. 但如果 Profile 故意相同

若：

$$
Profile(a)=Profile(b),
$$

則可存在：

$$
f(a)=b,
$$

$$
f(b)=a,
$$

$$
f(c)=c
$$

使兩個 histories causal-isomorphic。

Checker：

$$
\boxed{
SymmetricProfileIsomorphic=true.
}
$$

因此：

$$
\boxed{
HistoryIdentity
}
$$

仍然相對於所選 profile/equivalence regime。

---

# 16. Raw Configuration Ambiguity

定義：

$$
\boxed{
Real_v(C)
=
\{
\widehat C
\mid
Surface(\widehat C)=C
\}.
}
$$

若：

$$
|Real_v(C)|>1,
$$

則 raw configuration 有 causal ambiguity。

Toy 中：

$$
C=\{a,b,c\}
$$

具有至少兩類 distinct causal orders。

---

# 17. Cause-Sensitive Mode

定義：

$$
\boxed{
Mode=CauseSensitive.
}
$$

Runtime 狀態直接以：

$$
\widehat C
$$

為 identity unit。

所以：

$$
\widehat C_A
\neq
\widehat C_B
$$

即使：

$$
Surface(\widehat C_A)
=
Surface(\widehat C_B).
$$

適合：

- governance；
- replay；
- scientific causality；
- safety-critical systems。

---

# 18. Cause-Abstract Mode

若希望 parent layer 忘記具體 cause，

不能直接：

$$
\widehat C\mapsto C.
$$

而要有：

$$
\boxed{
ForgetCauseCert_Q^v(C).
}
$$

候選充分條件：

$$
\boxed{
\forall
\widehat C_i,\widehat C_j
\in Real_v(C),
\quad
BQCert_{Q,v}
(
\widehat C_i,
\widehat C_j
)
\downarrow.
}
$$

也就是所有 relevant causal realizations 在指定 scope 下都屬同一安全 quotient class。

---

# 19. Forgetting Cause 是一種 Projection

因此：

$$
\boxed{
ForgetCause:
\widehat C
\to
C
}
$$

不是免費操作。

它會丟掉：

- witness identity；
- induced causal order；
- backward-ready differences；
- possibly future capabilities。

所以必須像其他 Project 一樣具有：

$$
\boxed{
LossCert.
}
$$

---

# 20. Parent State 再次精化

Cause-sensitive parent state：

$$
\boxed{
S_{parent}
=
Quotient(
\widehat{\mathcal C}
\mid
BQCert
).
}
$$

Cause-abstract parent state：

$$
\boxed{
S_{parent}^{abs}
=
Quotient(
C
\mid
ForgetCauseCert
).
}
$$

兩者不能默認相同。

---

# 21. General CEES HP-like Triple

Prime v0.11：

$$
(C_1,f,C_2).
$$

General CEES 應改為：

$$
\boxed{
(
\widehat C_1,
f,
\widehat C_2
).
}
$$

 $f$ 保存：

- ON event profile；
- concrete $\prec_\pi$ ；
- version/scope conditions。

---

# 22. Forward Extension

General decorated transition：

$$
\boxed{
\widehat C
\xrightarrow{(e,\kappa)}
\widehat C'.
}
$$

其中：

$$
\kappa\vdash_v e.
$$

新 causal realization：

$$
\widetilde e
=
(e,\kappa,v).
$$

---

# 23. hp-like Matching

若：

$$
\widehat C_1
\xrightarrow{(e_1,\kappa_1)}
\widehat C_1',
$$

則另一邊需有：

$$
\widehat C_2
\xrightarrow{(e_2,\kappa_2)}
\widehat C_2'
$$

使：

$$
Profile(e_1)=Profile(e_2)
$$

並延伸 history isomorphism。

不要求：

$$
\kappa_1=\kappa_2
$$

作為 raw event IDs 相等，

但要求它們在 $f$ 下形成等價 cause structure。

---

# 24. Backward Extension

對：

$$
e\in Max(\widehat C),
$$

允許：

$$
\boxed{
\widehat C
\xleftarrow{e}
\widehat C^{-e}
}
$$

其中：

- 刪除 $e$ 的 occurrence；
- 刪除其 witness record；
- 保留剩餘 proving history 的合法性。

這是 HHP hereditary/backtracking 的 general-CEES 基礎。

---

# 25. Witness-Closed Subhistory

HHP hereditary closure 不能對任意 subset 生硬刪除。

必須保留：

$$
\boxed{
\text{witness-closed subhistory}.
}
$$

即若：

$$
e\in D
$$

則其 chosen witness：

$$
\kappa_e\subseteq D.
$$

否則 $D$ 不是該 concrete causal history 的合法 past。

---

# 26. General HHP-like Relation

候選 relation：

$$
\boxed{
R
\subseteq
\widehat{Conf}_1
\times
Iso
\times
\widehat{Conf}_2.
}
$$

要求：

1. forward matching；
2. backward maximal-event matching；
3. history-isomorphism extension/restriction；
4. profile / authority / residual compatibility；
5. version scope compatibility。

---

# 27. Why Raw Event Set Is Not Enough for HHP

Toy：

$$
Surface(\widehat C_A)
=
Surface(\widehat C_B).
$$

但：

$$
Max(\widehat C_A)
=
\{b,c\},
$$

$$
Max(\widehat C_B)
=
\{a,c\}.
$$

因此若只存：

$$
C=\{a,b,c\},
$$

連「現在可以回退誰」都無法唯一決定。

---

# 28. Dynamic Meta Rewrite

v1：

$$
Alt_{v1}(c)
=
\{
\{a\},
\{b\}
\}.
$$

Meta 後 v2：

$$
Alt_{v2}(c)
=
\{
\{a,b\}
\}.
$$

舊：

$$
\widetilde c
=
(c,\{a\},v1)
$$

不應被直接重寫成：

$$
(c,\{a,b\},v2).
$$

---

# 29. Version-Pinned Causal Realization

定義：

$$
\boxed{
\widetilde e=(e,\kappa,v).
}
$$

因此 old history：

$$
\widehat C_{v1}
$$

Replay 使用：

$$
v1.
$$

Checker 確認：

$$
Valid_{v1}(\widehat C_A)=true,
$$

而同一 history object 不符合 v2 rules。

---

# 30. Causal Migration

若希望舊 history 進入新 semantics：

$$
\boxed{
CausalMig:
(
\widehat C_{v1},
\mathfrak E_{v1},
\mathfrak E_{v2}
)
\rightharpoonup
(
\widehat C'_{v2},
Cert_{mig}
).
}
$$

可能：

- preserve witness；
- replace witness；
- split realization；
- grandfather；
- reject。

---

# 31. Standard HP-not-HHP Regression Target

ON-RDSS checker 下一個正式 regression fixture 應加入經典：

$$
\boxed{
HP=true,
\qquad
HHP=false.
}
$$

的 1-safe-net example。

其關鍵 assertion：

> forward matching 存在，但 matching of concurrent $a,b$ depends on linearization；回退後，forced residual mapping 進入一個 future $d$ 只能由一邊執行的狀態。

這能檢查：

$$
\boxed{
\text{forward fixed point}
}
$$

與：

$$
\boxed{
\text{hereditary/backtracking fixed point}
}
$$

真的被程式分開。

---

# 32. 本輪 Checker 結果

## Same raw event set

$$
\boxed{
C_A=C_B=\{a,b,c\}.
}
$$

## Different concrete causal orders

$$
\boxed{
a<c
}
$$

versus：

$$
\boxed{
b<c.
}
$$

## Different causal realization IDs

$$
\boxed{
RID_A\neq RID_B.
}
$$

## Different backward-ready profiles

成立。

## Governed profile isomorphism

$$
\boxed{
false.
}
$$

## Symmetric profile isomorphism

$$
\boxed{
true.
}
$$

---

# 33. Checker Enumeration

Toy General CEES 共枚舉：

$$
13
$$

個 decorated proving histories。

其中 raw：

$$
\{a,b,c\}
$$

對應：

$$
6
$$

個不同 proving sequences，

但這些 histories 壓成：

$$
2
$$

種 distinct causal orders。

因此：

$$
\boxed{
SequenceIdentity
\neq
CausalHistoryIdentity
\neq
RawConfigurationIdentity.
}
$$

---

# 34. 三層 Identity

現在至少需要：

## Surface Configuration Identity

$$
C.
$$

回答：

> 哪些語義 events 發生過？

## Causal History Identity

$$
(C,\prec_\pi).
$$

回答：

> 這些 events 是以什麼因果方式發生？

## Concrete Replay Identity

$$
(C,\pi,\prec_\pi,v).
$$

回答：

> 實際使用了哪些 witnesses、在哪個版本發生？

---

# 35. Parent-State Quotient 的新輸入

以前：

$$
Quotient(C_1,C_2).
$$

現在更安全：

$$
\boxed{
Quotient(
\widehat C_1,
\widehat C_2
).
}
$$

除非先取得：

$$
ForgetCauseCert.
$$

---

# 36. 與 Operator Ontology 的關係

Enabling witness 自己也可以算子化：

$$
\boxed{
\mathcal O_{\kappa}
:
(
C,e,\Gamma
)
\rightharpoonup
Cert_{\mathrm{enable}}.
}
$$

而 causal realization birth：

$$
\boxed{
\mathcal O_{\mathrm{CauseRealize}}
:
(
e,
\kappa,
v
)
\rightharpoonup
\widetilde e.
}
$$

因此我們仍沒有破壞：

> RDSS 最大域內所有內部構件算子化。

---

# 37. 下一個真正 theorem candidate

## CR1 — Raw Configuration Insufficiency

存在 General CEES 與：

$$
\widehat C_1,\widehat C_2
$$

使：

$$
Surface(\widehat C_1)
=
Surface(\widehat C_2)
$$

但：

$$
\prec_{\pi_1}
\neq
\prec_{\pi_2}.
$$

本輪 toy model 已構造。

---

# 38. CR2 — Backward Capability Divergence

存在：

$$
Surface(\widehat C_1)
=
Surface(\widehat C_2)
$$

但：

$$
Max(\widehat C_1)
\neq
Max(\widehat C_2).
$$

本輪 toy model亦構造。

---

# 39. CR3 — Cause Forgetting Requires Certificate

若：

$$
|Real_v(C)|>1
$$

且其中存在：

$$
\widehat C_i,
\widehat C_j
$$

不滿足指定 quotient relation，

則：

$$
\boxed{
ForgetCause(C)
}
$$

不是 safe projection。

---

# 40. CR4 — Version-Pinned Cause Preservation

若：

$$
\widetilde e=(e,\kappa,v)
$$

已 committed，

新版本：

$$
v'
$$

不能在沒有 CausalMig 的條件下改寫：

$$
\kappa.
$$

這是 No Silent Retroactivity 在 causal-realization 層的版本。

---

# 41. 下一輪

1. 將 v0.11 hp/hhp checker 升級成 decorated-history triples；
2. 直接加入 backward moves，而不是只靠 hereditary subset closure；
3. 翻譯並實作經典 HP-not-HHP regression example；
4. 比較 explicit backward checker 與 hereditary closure checker 是否一致；
5. 對 General CEES 加 conflict / consistency；
6. 對同一 raw configuration 計算所有 causal realization quotient classes；
7. 實作 ForgetCauseCert；
8. 研究 causal unfolding 是否可作 ON-RDSS strong-history backend；
9. 將 causal realization ID 接入 History / Replay；
10. 開始準備第一篇 Operator-Native RDSS 正式論文的 theorem set。

---

# 42. 暫定結論

ON-RDSS 到 v0.12 再次修正了「狀態」的基本單位。

在具有 disjunctive causation 的系統中：

$$
\boxed{
State
\neq
SetOfOccurredEvents.
}
$$

更準確：

$$
\boxed{
RuntimeHistoryState
=
(
SurfaceEvents,
EnablingWitnesses,
InducedCausalOrder,
SemanticsVersion
).
}
$$

也就是：

$$
\boxed{
\widehat C
=
(C,\pi,\le_\pi,v).
}
$$

因此：

> **同一批事情都發生過，不代表它們是以同一種因果歷史發生。**

而如果 parent layer 想忘記這個差異：

> **「忘記原因」本身就是一次有資訊損失的 projection，必須取得 certificate，而不能被當成免費的狀態壓縮。**
