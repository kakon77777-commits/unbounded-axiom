---
title: "GACEI-03｜局部攻擊抽象論：從一次性反例到可重用 Attack Operator"
title_en: "GACEI-03 | Theory of Local Attack Abstraction: From One-Off Counterexamples to Reusable Attack Operators"
series: "全域對抗計算與 AI 工程智能系列"
series_en: "Global Adversarial Computation and AI Engineering Intelligence Series"
series_id: "GACEI-2026"
paper_id: "GACEI-03"
version: "v0.1"
date: "2026-09-08"
language: "zh-Hant"
author: "Neo.K"
organization: "EveMissLab / 一言諾科技有限公司"
document_type: "研究論文 / 攻擊抽象 / 軟體工程記憶 / AI 工程智能"
status: "Canonical Draft"
canonical_source: "UTF-8 Markdown"
math_source_rule: "inline math only $...$ ; display math only $$...$$"
security_scope: "Authorized, isolated, recoverable software testing and simulation only"
depends_on:
  - "GACEI-01 全域對抗計算總論 v0.1"
  - "GACEI-02 MSSP 的對偶 v0.1"
---

# GACEI-03｜局部攻擊抽象論
## 從一次性反例到可重用 Attack Operator

**英文題名：** Theory of Local Attack Abstraction: From One-Off Counterexamples to Reusable Attack Operators

---

## 摘要

GACEI-01 提出全域對抗計算，GACEI-02 進一步將 MSSP 的局部責任結構與全域擾動結構連接起來。但若每次專案開始時，AI 都必須重新閱讀歷史、重新想出曾經使用過的局部反例、重新寫測試並重新判斷其意義，那麼即使全域 campaign 能降低重複執行成本，昂貴的認知成本仍然會重複支付。

本文提出「局部攻擊抽象論」（Theory of Local Attack Abstraction），研究如何把一次具體、專案綁定、版本綁定的失敗 witness，轉換成可跨專案、跨版本、跨命名與跨實作細節重用的 typed attack operator。其核心命題是：

$$
\boxed{
\text{A successful attack is not yet reusable knowledge.}
}
$$

以及：

$$
\boxed{
\text{Reusability requires abstraction, typing, applicability conditions, evidence, and transfer validation.}
}
$$

本文把攻擊知識的成熟度拆成五層：

$$
W_0
\rightarrow
W_1
\rightarrow
W_2
\rightarrow
W_3
\rightarrow
W_4,
$$

其中：

- $W_0$：Concrete Witness；
- $W_1$：Typed Attack Instance；
- $W_2$：Parameterized Attack Template；
- $W_3$：Attack Family；
- $W_4$：Transfer-Validated Reusable Operator。

具體 witness 不應只保存「哪一個檔案哪一行曾經壞掉」，而應至少抽出：

$$
a
=
\left(
P,
T,
I,
O,
V,
R,
C,
K,
H
\right),
$$

其中 $P$ 為適用前提， $T$ 為擾動算子， $I$ 為目標不變量， $O$ 為觀測計畫， $V$ 為 validator / alarm contract， $R$ 為恢復與清理條件， $C$ 為覆蓋與影響描述， $K$ 為成本， $H$ 為 provenance 與歷史證據。

本文進一步區分「具體化」與「抽象化」兩個方向。令具體 witness 空間為 $\mathcal W$，抽象 attack 空間為 $\mathcal A$，則定義：

$$
\alpha:
\mathcal W
\rightarrow
\mathcal A
$$

為抽象算子，並以：

$$
\gamma:
\mathcal A
\times
\mathcal S
\rightarrow
\mathcal P(\mathcal W)
$$

表示在新系統 $\mathcal S$ 上將抽象 attack 具體化成候選 witness 的過程。本文借用「抽象／具體化」的結構語彙，但不宣稱這裡必然滿足 abstract interpretation 的 Galois connection、完備性或單調性條件；是否能形成更強數學結構留待後續研究。

局部攻擊抽象的真正難點不是「把名稱換成變數」，而是判定哪些性質應被保留、哪些只是偶然實作細節。若抽象過窄，attack 無法遷移；若抽象過廣，則會產生大量 false applicability、false positive 與無意義的 attack spam。因此本文引入最小充分攻擊骨架、結構匹配、反例保持、正例保持、負控制與 transfer validation，要求一個 attack template 至少在不同具體實例上保留相同 failure mechanism，而不是只保留表面相似的 red signal。

本文特別以「兄弟 TMS」類歷史反例說明：具體事件「TMS-A 直接依賴 TMS-B」不應被永久保存為只針對兩個名字的測試，而應逐步抽象為：

$$
\text{Forbidden Peer Coupling}
$$

並將其適用前提寫成：

$$
\operatorname{Peer}(u,v)=1
\land
\operatorname{DirectCouplingAllowed}(u,v)=0.
$$

擾動則為：

$$
T_{\mathrm{peer}}(u,v)
=
\operatorname{IntroduceDirectCoupling}(u,v),
$$

目標不變量為：

$$
I_{\mathrm{peer-separation}}.
$$

如此，同一 attack family 才能在不同專案、不同模組名稱、不同語言甚至不同實作方式中重新實例化。

本文最後提出「用過就學會」的正式化版本：

$$
\boxed{
\text{Observed}
\rightarrow
\text{Reproduced}
\rightarrow
\text{Typed}
\rightarrow
\text{Abstracted}
\rightarrow
\text{Transferred}
\rightarrow
\text{Promoted}.
}
$$

只有通過 promotion gate 的 attack 才進入長期可重用對抗記憶。未來高階 AI 不應把昂貴算力浪費在重新發明已知 attack，而應優先處理：

$$
\boxed{
\text{Residual Unknown Failure Mechanisms}.
}
$$

因此，局部攻擊不是一次性測試消耗品，而可以被轉化為持續增值的工程知識資本。

**關鍵詞：** Attack Abstraction、Attack Operator、Concrete Witness、Attack Template、Attack Family、SEDB、對抗記憶、軟體免疫、結構匹配、Transfer Validation、MSSP、全域對抗計算、AI 工程智能

---

# 0. 研究定位與安全範圍

本文中的 attack 只作用於：

- 已授權軟體；
- synthetic fixture；
- sandbox；
- isolated copy；
- 可恢復測試環境；
- 研究用模擬系統。

本文研究的是：

$$
\boxed{
\text{Software Failure Mechanism Abstraction}.
}
$$

不是未授權入侵技巧的抽象化。

本文關心：

> 一個已知軟體失敗反例如何被轉換成可重用測試知識？

而不是：

> 如何把真實第三方系統的攻擊方法保存成可重複入侵工具？

兩者不可混淆。

---

# 1. 為什麼「找到一次」還不等於「學會」？

## 1.1 一次成功可以只是偶然

假設：

$$
w_1
$$

是某次具體失敗 witness。

若：

$$
V(w_1)=\text{Fail},
$$

只能說：

> 這個具體 witness 在這個 baseline、版本、環境與 validator 下造成了可觀測失敗。

不能直接推出：

$$
\boxed{
w_1
=
\text{General Attack Knowledge}.
}
$$

---

## 1.2 專案綁定問題

一個一次性 test 可能綁死：

- file path；
- class name；
- variable name；
- platform；
- exact fixture；
- implementation detail；
- timestamp；
- commit；
- test harness。

如果換一個專案：

$$
S_1
\rightarrow
S_2,
$$

attack 就完全失效。

這表示：

$$
\boxed{
\text{Historical Test}
\neq
\text{Transferable Operator}.
}
$$

---

## 1.3 認知成本會被重複支付

假設第一次 AI 花：

$$
C_{\mathrm{discover}}
$$

發現一個 failure mechanism。

若下一個專案仍必須重新花：

$$
C_{\mathrm{discover}},
$$

則總成本：

$$
C_n
\approx
nC_{\mathrm{discover}}.
$$

若可抽象並重用：

$$
C_n
\approx
C_{\mathrm{discover}}
+
C_{\mathrm{abstract}}
+
(n-1)C_{\mathrm{match}},
$$

若：

$$
C_{\mathrm{match}}
\ll
C_{\mathrm{discover}},
$$

則長期收益明顯。

---

# 2. 五層攻擊知識成熟度

本文定義：

$$
\boxed{
W_0<W_1<W_2<W_3<W_4
}
$$

作為操作性成熟度，而不是價值高低的絕對序。

---

## 2.1 $W_0$：Concrete Witness

定義：

$$
w
\in
\mathcal W.
$$

內容包含：

- exact baseline；
- exact input；
- exact mutation；
- exact output；
- exact validator；
- exact environment；
- exact provenance。

它回答：

> 這件事真的發生過嗎？

---

## 2.2 $W_1$：Typed Attack Instance

把 witness 從「一段歷史」轉成具有型別的 attack instance：

$$
a^{(1)}
=
(P,T,I,O,V,R,C,K,H).
$$

它回答：

> 這次失敗究竟屬於哪一種攻擊語義？

---

## 2.3 $W_2$：Parameterized Attack Template

把具體值替換成具結構意義的參數：

$$
t(\theta).
$$

例如：

$$
\theta
=
(u,v,b,s)
$$

可以代表：

- source role；
- target role；
- boundary；
- state condition。

它回答：

> 在哪些結構條件下，可以重新生成同類 failure test？

---

## 2.4 $W_3$：Attack Family

多個 template 若共享較高階 failure mechanism，可以歸入：

$$
F_j.
$$

例如：

$$
F_{\mathrm{boundary}}
$$

可以包含：

- forbidden peer coupling；
- hidden backchannel；
- state ownership bypass；
- direct authority bypass。

Attack family 回答：

> 這些不同 attack 背後是否存在同一類失敗機制？

---

## 2.5 $W_4$：Transfer-Validated Reusable Operator

只有在不同：

- project；
- version；
- naming；
- implementation；
- fixture；

上成功具體化，並維持低 false applicability 的 attack，才升格：

$$
W_4.
$$

它回答：

> 這個抽象真的具有跨場景重用價值嗎？

---

# 3. 攻擊算子的完整資料型態

本文提出：

$$
\boxed{
a
=
\left(
P,
T,
I,
O,
V,
R,
C,
K,
H
\right).
}
$$

---

## 3.1 前提 $P$

$$
P(S,\theta)=1
$$

表示：

> attack 在目前系統與條件下有語義。

如果：

$$
P=0,
$$

則 attack 不應執行。

因此：

$$
\boxed{
\text{Not Applicable}
\neq
\text{Pass}.
}
$$

---

## 3.2 擾動 $T$

$$
T:
S
\rightarrow
S'.
$$

它描述：

> 我們故意改變什麼？

但 $T$ 必須被約束在授權 sandbox 中。

---

## 3.3 目標不變量 $I$

attack 必須知道自己在測：

$$
I_a
\subseteq
I_S.
$$

如果沒有 target invariant，只知道：

> 我想看看會不會壞。

那只是 exploration，不是成熟 attack operator。

---

## 3.4 觀測 $O$

$$
O:
S'
\rightarrow
Z.
$$

它規定：

> 哪些狀態、輸出、trace 或指標與本 attack 有關？

---

## 3.5 驗證器 $V$

$$
V(Z)
\in
\{
\text{Accept},
\text{Reject},
\text{Unknown},
\text{NotMeasured}
\}.
$$

不應把所有非 Accept 壓成同一 Failure，也不應把 Unknown 壓成 Pass。

---

## 3.6 恢復 $R$

$$
R:
S'
\rightarrow
S^\ast
$$

或：

$$
R:
S'
\rightarrow
\text{DiscardSandbox}.
$$

如果 attack 沒有安全恢復方案，就不應默認進入一般自動化 campaign。

---

## 3.7 覆蓋 $C$

$$
C(a)
=
\left(
C_N,C_R,C_\Theta,C_P,C_V,C_T
\right).
$$

表示此 attack 預期覆蓋的結構維度。

---

## 3.8 成本 $K$

$$
K(a)
=
\left(
k_{\mathrm{compute}},
k_{\mathrm{runtime}},
k_{\mathrm{tool}},
k_{\mathrm{human}},
k_{\mathrm{risk}}
\right).
$$

---

## 3.9 歷史與 provenance $H$

至少保存：

- first discovery；
- source project；
- source version；
- reproductions；
- failures；
- false positives；
- superseded forms；
- transfer history；
- validator history。

---

# 4. 抽象算子與具體化算子

## 4.1 抽象

令：

$$
\alpha:
\mathcal W
\rightarrow
\mathcal A
$$

把具體 witness 轉成 abstract attack。

---

## 4.2 具體化

令：

$$
\gamma:
\mathcal A
\times
\mathcal S
\rightarrow
\mathcal P(\mathcal W)
$$

表示：

> 給定一個 abstract attack 與新系統，產生所有可行或候選的具體 attack instances。

---

## 4.3 本文不主張 Galois connection

雖然：

$$
\alpha
$$

與：

$$
\gamma
$$

在語義上類似 abstraction / concretization，但本文不宣稱：

$$
\alpha
\dashv
\gamma
$$

或存在任何自動 Galois connection。

若未來某些 attack domain 能滿足：

- 偏序；
- 單調性；
- closure；
- sound abstraction；

才可建立更強形式化。

---

# 5. 什麼應保留，什麼應丟掉？

## 5.1 偶然細節

通常應被候選移除：

- 臨時變數名；
- 測試資料的無關字串；
- 一次性路徑；
- UI 顏色；
- 無關 timestamp；
- 不影響 failure mechanism 的命名。

---

## 5.2 結構必要資訊

通常應保留：

- role；
- type；
- topology；
- ownership；
- ordering；
- authority；
- lifecycle；
- invariant；
- state relation；
- observation condition。

---

## 5.3 最小充分攻擊骨架

本文定義：

$$
\boxed{
\operatorname{MSAS}(w)
}
$$

為 Minimal Sufficient Attack Skeleton。

它要求找到一個最小候選結構：

$$
q
$$

使：

$$
q
$$

仍能在多個合法具體化中重建相同 failure mechanism。

若刪除某條件：

$$
c_i,
$$

會導致：

$$
\text{failure mechanism lost},
$$

則：

$$
c_i
$$

是必要條件。

---

# 6. 過度抽象與抽象不足

## 6.1 抽象不足

如果 template：

$$
t_1
$$

只對：

$$
\text{ModuleName}=\text{TMS-A}
$$

成立，

則 transferability 幾乎為零。

---

## 6.2 過度抽象

如果 template 寫成：

> 任意兩個模組互相互動都可能是錯。

則：

$$
P
$$

過廣。

結果：

$$
\operatorname{FalseApplicability}
\uparrow.
$$

---

## 6.3 抽象品質

可定義：

$$
Q_{\mathrm{abs}}
=
f
(
T_{\mathrm{transfer}},
P_{\mathrm{precision}},
F_{\mathrm{mechanism}},
C_{\mathrm{compression}}
).
$$

其中：

- $T_{\mathrm{transfer}}$：transfer success；
- $P_{\mathrm{precision}}$：applicability precision；
- $F_{\mathrm{mechanism}}$：failure mechanism fidelity；
- $C_{\mathrm{compression}}$：描述壓縮。

---

# 7. 結構匹配

## 7.1 名稱相似不等於 attack 可用

$$
\operatorname{NameSim}(x,y)
\approx1
$$

不能推出：

$$
\operatorname{AttackApplicable}(x,y)=1.
$$

---

## 7.2 Structural Predicate

attack template 應攜帶：

$$
P_t
=
P_{\mathrm{role}}
\land
P_{\mathrm{relation}}
\land
P_{\mathrm{state}}
\land
P_{\mathrm{condition}}.
$$

只有：

$$
P_t(S)=1
$$

才具體化。

---

## 7.3 Typed matching

例如 forbidden peer coupling：

$$
P_{\mathrm{peer}}(u,v)
=
\operatorname{Peer}(u,v)
\land
\neg
\operatorname{DirectCouplingAllowed}(u,v).
$$

這比：

> 兩個檔案都在同一資料夾。

具有更強語義。

---

# 8. 兄弟 TMS：從事故到 Attack Operator

## 8.1 $W_0$ witness

歷史具體 witness：

$$
TMS_A
\rightarrow
TMS_B.
$$

---

## 8.2 $W_1$ typed instance

型別化後：

$$
\text{PeerBoundaryViolation}.
$$

---

## 8.3 $W_2$ template

定義：

$$
t_{\mathrm{peer}}
=
(P_{\mathrm{peer}},
T_{\mathrm{couple}},
I_{\mathrm{separation}},
O_{\mathrm{dep}},
V_{\mathrm{boundary}}).
$$

---

## 8.4 $W_3$ family

再向上抽象：

$$
t_{\mathrm{peer}}
\in
F_{\mathrm{boundary-coupling}}.
$$

---

## 8.5 $W_4$ transfer

如果在：

- 不同 MSSP App；
- 不同模組名稱；
- 不同實作語言；
- 不同 dependency mechanism；

都可以建立同一 failure mechanism，則升格成 reusable operator。

---

# 9. 正例保持與反例保持

一個好 attack abstraction 不只要保留 failure。

還要避免把正常行為誤判成 failure。

---

## 9.1 反例保持

對應具體化：

$$
w^{-}
\in
\gamma(a,S),
$$

應有：

$$
V(w^{-})=\text{Reject}.
$$

---

## 9.2 正例保持

對合法 counterpart：

$$
w^{+},
$$

應有：

$$
V(w^{+})=\text{Accept}.
$$

---

## 9.3 雙保持

因此：

$$
\boxed{
\text{Attack Abstraction Quality}
=
\text{Negative Preservation}
+
\text{Positive Preservation}.
}
$$

只會把東西弄紅，不代表 template 有辨識力。

---

# 10. Negative Control

每個 promoted attack template 應至少保留：

$$
c^{-}
$$

與：

$$
c^{+}.
$$

其中：

$$
c^{-}
=
\text{known bad control},
$$

$$
c^{+}
=
\text{authorized equivalent / known good control}.
$$

若：

$$
V(c^{-})=\text{Reject}
$$

且：

$$
V(c^{+})=\text{Accept},
$$

才有最低 discriminative evidence。

---

# 11. Transfer Validation

## 11.1 單專案成功不夠

若：

$$
a
$$

只在：

$$
S_1
$$

成功，

不能直接說：

$$
a
\in
W_4.
$$

---

## 11.2 Transfer set

定義：

$$
\mathcal S_T
=
\{
S_1,S_2,\ldots,S_m
\}.
$$

Transfer success：

$$
R_T(a)
=
\frac{
\sum_i
\mathbf 1[
\operatorname{Applicable}(a,S_i)
\land
\operatorname{MechanismPreserved}(a,S_i)
]
}{
\sum_i
\mathbf 1[
\operatorname{Applicable}(a,S_i)
]
}.
$$

---

## 11.3 False applicability

定義：

$$
F_A(a)
=
\frac{
N_{\mathrm{incorrect\ applicability}}
}{
N_{\mathrm{applicability\ predictions}}
}.
$$

若：

$$
F_A
$$

過高，template 應降級或拆分。

---

# 12. Attack Family 的一般化偏序

## 12.1 不是所有 family 都形成 lattice

本文定義：

$$
a_i
\preceq_G
a_j
$$

表示：

> $a_j$ 的適用域比 $a_i$ 更一般，且 $a_i$ 可視為 $a_j$ 的特例。

但本文不宣稱所有 attack families 都具有：

- unique join；
- unique meet；
- complete lattice。

---

## 12.2 Family graph

較安全的第一版：

$$
G_F
=
(F,E_G),
$$

其中關係可包含：

- GENERALIZES；
- SPECIALIZES；
- OVERLAPS；
- REQUIRES；
- CONFLICTS；
- SUPERSEDES；
- ANALOGOUS_TO；
- NOT_EQUIVALENT_TO。

---

# 13. Macro：把重複程序壓成知識

如果一組 attack sequence：

$$
a_1
\rightarrow
a_2
\rightarrow
a_3
$$

在多個專案反覆出現，

可提出：

$$
m
=
\operatorname{Macro}(a_1,a_2,a_3).
$$

但：

$$
m
$$

不應只保存「順序」。

還要保存：

- sequence precondition；
- intermediate state requirements；
- stop conditions；
- validator chain；
- recovery semantics。

因此：

$$
\boxed{
\text{Attack Macro}
\neq
\text{Recorded Script}.
}
$$

---

# 14. Deduplication 與攻擊知識膨脹

## 14.1 不去重會變成另一個地獄

如果每次：

$$
a_i
$$

略有不同就存一份，

則：

$$
|K_A|
\rightarrow
\infty
$$

會造成：

- retrieval noise；
- match duplication；
- campaign inflation；
- false diversity。

---

## 14.2 Dedup key

可以建立：

$$
D(a)
=
\operatorname{Hash}
(
\operatorname{Canonical}
(
P,I,T_{\mathrm{abstract}},V_{\mathrm{semantics}}
)
).
$$

不能只 hash 原始 script。

---

## 14.3 Similar 不等於 Equivalent

即使：

$$
\operatorname{sim}(a_i,a_j)\approx1,
$$

也不能自動：

$$
a_i=a_j.
$$

只能生成：

$$
\operatorname{MergeCandidate}(a_i,a_j).
$$

再經 structural comparison。

---

# 15. 攻擊知識的生命週期

本文提出：

```text
OBSERVED
-> REPRODUCED
-> TYPED
-> ABSTRACTED
-> TRANSFER_TESTED
-> PROMOTED
-> ACTIVE
-> SUPERSEDED / DEPRECATED / RETIRED
```

---

## 15.1 OBSERVED

只代表一次事件被記錄。

---

## 15.2 REPRODUCED

在同 baseline 可重現。

---

## 15.3 TYPED

已知道 attack kind、target invariant 與 observation semantics。

---

## 15.4 ABSTRACTED

已形成 parameterized template。

---

## 15.5 TRANSFER_TESTED

已在不同合法實例測試。

---

## 15.6 PROMOTED

符合進入 reusable memory 的門檻。

---

## 15.7 SUPERSEDED / DEPRECATED

若新架構改變：

$$
P
$$

或：

$$
I,
$$

舊 attack 不應假裝永久有效。

---

# 16. Promotion Gate

不是所有 attack 都值得進長期記憶。

本文提出第一版 promotion gate：

$$
\boxed{
G_{\mathrm{promote}}
=
R
\land
T
\land
D
\land
S
\land
P.
}
$$

其中：

- $R$：Reproduced；
- $T$：Typed；
- $D$：Discriminative；
- $S$：Structurally abstracted；
- $P$：Provenance complete。

若要升到 $W_4$，再要求：

$$
X
=
\text{Transfer validated}.
$$

---

# 17. 對抗記憶需要保存失敗歷史

## 17.1 只存成功命中會造成 survivor bias

如果 attack：

$$
a
$$

曾：

- 命中 4 次；
- false positive 12 次；

但資料庫只記 4 次命中，

未來 AI 會高估：

$$
\operatorname{Utility}(a).
$$

---

## 17.2 必須記錄

至少保存：

$$
H_a
=
\left(
N_{\mathrm{hit}},
N_{\mathrm{miss}},
N_{\mathrm{false+}},
N_{\mathrm{not-applicable}},
N_{\mathrm{unknown}}
\right).
$$

---

# 18. 攻擊價值不是命中率

一個 attack 即使命中率低，也可能：

- 成本極低；
- 覆蓋極關鍵 invariant；
- 能發現 catastrophic blind spot。

因此：

$$
\boxed{
\text{Hit Rate}
\neq
\text{Attack Value}.
}
$$

可定義：

$$
U(a)
=
\frac{
w_rR(a)
+
w_iI(a)
+
w_cC(a)
+
w_kK_{\mathrm{learn}}(a)
}{
\operatorname{Cost}(a)+\epsilon
}.
$$

其中：

- $R(a)$：risk relevance；
- $I(a)$：information gain；
- $C(a)$：coverage；
- $K_{\mathrm{learn}}(a)$：knowledge gain。

---

# 19. Abstraction Compression Ratio

定義：

$$
ACR
=
\frac{
N_{\mathrm{concrete\ witnesses}}
}{
N_{\mathrm{reusable\ templates}}
}.
$$

若：

$$
ACR\gg1,
$$

表示很多具體案例被壓縮成少量 reusable knowledge。

但：

$$
ACR
$$

越大不代表越好。

過度壓縮可能造成：

$$
F_A\uparrow.
$$

所以必須配合 applicability precision。

---

# 20. Reuse Saving

令：

$$
C_D
=
\text{rediscovery cost},
$$

$$
C_M
=
\text{match and instantiate cost}.
$$

單次 reuse saving：

$$
S_R
=
C_D-C_M.
$$

多專案累積：

$$
S_R^{(n)}
=
\sum_{i=2}^{n}
\left(
C_D^{(i)}-C_M^{(i)}
\right)
-
C_{\mathrm{abstract}}.
$$

若：

$$
S_R^{(n)}>0,
$$

attack abstraction 開始回本。

---

# 21. 從 Retrieval 到 Creativity 的分界

Attack memory 的目的不是讓 AI 停止創造。

而是：

$$
\boxed{
\text{Known Mechanism}
\rightarrow
\text{Retrieve / Instantiate},
}
$$

$$
\boxed{
\text{Residual Gap}
\rightarrow
\text{Create / Generate}.
}
$$

若 AI 每次都重新創造已知 attack：

$$
\text{Creativity}
\rightarrow
\text{Waste}.
$$

若 AI 只會 replay：

$$
\text{Memory}
\rightarrow
\text{Stagnation}.
$$

真正理想是：

$$
\boxed{
\text{Memory frees creativity for the unknown.}
}
$$

---

# 22. 攻擊抽象與全域 campaign 的接口

GACEI-02 的 campaign compiler 需要：

$$
K_A.
$$

本文提供：

$$
K_A
=
\{
W_4\text{ operators},
W_3\text{ families},
W_2\text{ templates}
\}.
$$

其中：

- $W_4$：可優先自動具體化；
- $W_3$：提供 family-level coverage；
- $W_2$：需要較多場景判斷。

---

## 22.1 Campaign selection

對新系統：

$$
S,
$$

先：

$$
A_{\mathrm{known}}
=
\operatorname{Instantiate}(K_A,S).
$$

再計算 residual：

$$
G_{\mathrm{residual}}.
$$

高階 AI 只對：

$$
G_{\mathrm{residual}}
$$

進行新 attack synthesis。

---

# 23. SEDB 特化版的前置資料契約

下一篇會正式建立 SEDB attack memory。

本文先提出 attack record 最低欄位：

```yaml
attack_id:
maturity:
family:
template_version:
preconditions:
target_invariants:
abstract_operator:
observation_contract:
validator_contract:
recovery_contract:
coverage_signature:
cost_profile:
first_witness:
provenance:
reproduction_history:
transfer_history:
false_applicability_history:
supersedes:
superseded_by:
status:
```

---

# 24. Attack Identity

## 24.1 Script identity 不等於 attack identity

兩段完全不同的 script：

$$
s_1\neq s_2
$$

可能實現同一：

$$
a.
$$

---

## 24.2 同 script 也可能不是同 attack

同一段 script：

$$
s
$$

在不同：

- target invariant；
- role；
- condition；
- validator；

下可能具有不同語義。

因此：

$$
\boxed{
\text{Attack Identity}
\neq
\text{Code Identity}.
}
$$

---

## 24.3 第一版 semantic identity

可寫：

$$
ID(a)
=
\operatorname{Hash}
(
P,
I,
T_{\mathrm{sem}},
O_{\mathrm{sem}},
V_{\mathrm{sem}}
).
$$

實作 bytes 另存：

$$
\text{ArtifactDigest}.
$$

---

# 25. 版本與條件纖維

attack 應綁定：

$$
\theta
=
(
\text{project},
\text{version},
\text{platform},
\text{architecture},
\text{permission},
\text{resource},
\text{validator}
).
$$

因此：

$$
a\in W_4
$$

也不是「永遠通用」。

更正確：

$$
\boxed{
a
\text{ reusable under declared condition fibers.}
}
$$

---

# 26. 過期與失效

若新版本：

$$
S_t
\rightarrow
S_{t+1}
$$

移除：

$$
P_a,
$$

則：

$$
a
\rightarrow
\text{Not Applicable}.
$$

不能因為歷史 attack 曾重要，就硬塞進每一版 global campaign。

---

# 27. Novelty 與 Duplicate Attack

AI 生成新 attack：

$$
a_{\mathrm{new}}
$$

後，先檢查：

$$
\operatorname{Match}(a_{\mathrm{new}},K_A).
$$

結果可以是：

- DUPLICATE；
- SPECIALIZATION；
- GENERALIZATION；
- OVERLAP；
- NOVEL；
- UNKNOWN。

只有：

$$
\text{NOVEL}
$$

才應增加 attack knowledge mass。

---

# 28. Attack Distillation

多個 attacks：

$$
a_1,\ldots,a_n
$$

可能被 distill 成：

$$
\hat a.
$$

Distillation 目標不是最短文字，而是：

$$
\boxed{
\text{Minimum Reconstructable Attack Semantics}.
}
$$

也就是：

> 新 AI 只讀 distill 後的 record，仍能正確判斷何時適用、如何生成、如何驗證、如何停止。

---

# 29. 第一版抽象演算法

```text
FUNCTION AbstractAttack(witness w):

1. VERIFY_WITNESS
   Confirm w is reproducible and belongs to the intended baseline.

2. IDENTIFY_TARGET
   Determine the violated invariant or failed contract.

3. EXTRACT_CAUSAL_CORE
   Separate structural cause from incidental implementation details.

4. TYPE
   Assign attack kind, target structure, observation, validator,
   recovery, and cost semantics.

5. PARAMETERIZE
   Replace project-specific names and values with typed parameters.

6. BUILD_PRECONDITION
   Define when the attack is semantically applicable.

7. BUILD_CONTROLS
   Preserve at least one known-bad and one known-good control.

8. ABSTRACT
   Produce template t.

9. MATCH_HISTORY
   Compare t to existing templates/families.

10. TRANSFER_TEST
    Instantiate t in independent eligible structures when available.

11. SCORE
    Measure mechanism fidelity, applicability precision,
    transfer rate, coverage, and cost.

12. PROMOTE_OR_HOLD
    Promote to reusable memory only when evidence is sufficient.

13. RECORD_FAILURES
    Persist misses, false positives, NotApplicable, and unknowns.

14. VERSION
    Bind the template to explicit condition fibers and provenance.
```

---

# 30. AI 在抽象時真正需要哪些能力？

## 30.1 理解

AI 必須知道：

$$
\text{what failed}
$$

和：

$$
\text{why it failed}
$$

不是同一件事。

---

## 30.2 解析

它必須把：

- state；
- role；
- relation；
- invariant；
- environment；

拆出來。

---

## 30.3 抽象

它必須找：

$$
\text{common mechanism}
$$

而不是做 literal rewrite。

---

## 30.4 驗證

它必須證明：

$$
t
$$

在合法具體化後仍保留 failure semantics。

---

## 30.5 生成

它必須能從：

$$
t
$$

生成新：

$$
w'.
$$

這才證明 abstraction 可用。

---

# 31. 研究假說

## H1：Attack abstraction 可降低跨專案 rediscovery cost

在同類架構專案族：

$$
\mathcal S
=
\{S_1,\ldots,S_n\},
$$

應存在：

$$
C_{\mathrm{reuse}}
<
C_{\mathrm{rediscover}}.
$$

---

## H2：Typed structural template 比 raw script 有更高 transfer rate

$$
R_T(t_{\mathrm{typed}})
>
R_T(s_{\mathrm{raw}})
$$

應在跨 naming / implementation 變體中成立。

---

## H3：過度一般化會提高 false applicability

若 template generality：

$$
G(t)
\uparrow
$$

超過某範圍，

則：

$$
F_A(t)
\uparrow.
$$

---

## H4：雙控制可降低假抽象

具有：

$$
c^{-}
+
c^{+}
$$

的 attack template，

其 false-positive rate 應低於只保存 bad witness 的 template。

---

## H5：攻擊記憶會把高階算力推向未知區

隨：

$$
|K_A|
\uparrow,
$$

前沿模型在 known attacks 上的 reasoning share 應下降，而在 residual unknowns 上的 share 應上升。

---

# 32. Benchmark

可建立：

$$
N
$$

個功能相似但表面不同的 synthetic systems。

第一個系統給 AI 完整 attack discovery 任務。

其後：

$$
S_2,\ldots,S_N
$$

只提供 architecture。

比較：

### Baseline A

每次重新發現 attack。

### Baseline B

使用 raw historical test scripts。

### Baseline C

使用 typed attack templates / families。

測：

$$
\text{Transfer Rate},
$$

$$
\text{False Applicability},
$$

$$
\text{Defect Recall},
$$

$$
\text{Reasoning Cost},
$$

$$
\text{Time-to-Campaign},
$$

$$
\text{Novel Attack Share}.
$$

---

# 33. 本文非主張

本文不主張：

1. 所有成功 attack 都值得保存；
2. 所有具體 witness 都有一般化價值；
3. attack abstraction 只靠 LLM embedding 即可完成；
4. 名稱替換就是抽象；
5. attack family 必然形成 complete lattice；
6. 抽象越一般越好；
7. template 越短越好；
8. historical hit rate 可以替代 applicability contract；
9. raw test script 沒有保存價值；
10. transfer success 一次就足以證明通用；
11. attack identity 等於 code identity；
12. 同 failure signal 代表同 failure mechanism；
13. 所有 attack 都應自動執行；
14. 所有過期 attack 都應永久保留在 active campaign；
15. attack memory 可以取代 novel reasoning；
16. attack abstraction 應用於未授權第三方入侵知識。

本文主張的是：

$$
\boxed{
\text{一次性失敗只有經過型別化、抽象化、控制、遷移與版本化，}
}
$$

才可能成為：

$$
\boxed{
\text{可重用的工程對抗知識。}
}
$$

---

# 34. 與 GACEI-01 / 02 的關係

GACEI-01：

$$
\text{Global Attack}
\rightarrow
\text{Local Diagnosis}
\rightarrow
\text{Learn Permanently}.
$$

GACEI-02：

$$
\text{MSSP Structure}
\rightarrow
\text{Global Campaign}
\rightarrow
\text{Failure Projection}.
$$

本文回答最後一段：

$$
\boxed{
\text{What does "learn permanently" operationally mean?}
}
$$

答案不是：

> 把 log 留著。

而是：

$$
\boxed{
\text{Witness}
\rightarrow
\text{Typed Attack}
\rightarrow
\text{Template}
\rightarrow
\text{Family}
\rightarrow
\text{Transfer-Validated Operator}.
}
$$

---

# 35. 下一篇：SEDB 特化對抗記憶

GACEI-04 將把本文的 attack knowledge 正式落到：

$$
\boxed{
K_A
=
\text{Persistent Adversarial Memory}.
}
$$

核心問題將包括：

- sparse schema；
- attack identity；
- provenance；
- version；
- relation graph；
- history；
- hit / miss；
- false applicability；
- promotion；
- supersession；
- retrieval；
- structural matching；
- knowledge update；
- campaign interface。

所以：

$$
\boxed{
\text{GACEI-03}
=
\text{What should be learned?}
}
$$

而：

$$
\boxed{
\text{GACEI-04}
=
\text{How should that learning be stored, governed, and retrieved?}
}
$$

---

# 36. 結論

如果每一個 AI 在每一個新專案中都重新發現：

> sibling coupling 可以破壞 separation；

重新發現：

> stale state 可以破壞 consistency；

重新發現：

> `NotMeasured` 不應被壓成 `Pass`；

重新發現：

> validator 可以產生 false green；

那麼 AI 的高推理能力被大量花費在：

$$
\boxed{
\text{Rediscovery of Known Failure Mechanisms}.
}
$$

這不是最有效的智能配置。

本文因此提出：

$$
\boxed{
\text{Attack Once}
\rightarrow
\text{Abstract Correctly}
\rightarrow
\text{Validate Transfer}
\rightarrow
\text{Reuse Permanently}.
}
$$

但「永久」不是永久有效。

它表示：

> 只要 attack 的適用條件、版本與結構契約仍成立，就不必重新支付完整發現成本。

當條件改變時：

$$
a
\rightarrow
\text{Revalidate / Specialize / Supersede / Retire}.
$$

所以真正成熟的 attack memory 不是死掉的病毒碼集合，而是：

$$
\boxed{
\text{Versioned, typed, evidence-bearing, transferable failure-mechanism knowledge}.
}
$$

它的價值在於：

$$
\text{Known Failure}
\rightarrow
\text{Cheap Recognition},
$$

並把昂貴智能留給：

$$
\boxed{
\text{Unknown Failure}
\rightarrow
\text{New Understanding}
\rightarrow
\text{New Attack}
\rightarrow
\text{New Knowledge}.
}
$$

因此，「用過就學會」的正式版本不是：

> AI 記得以前怎麼攻擊。

而是：

> **AI 能把一次具體失敗蒸餾成未來仍可被正確判斷、具體化、驗證與組合的抽象對抗算子。**

這才是全域對抗計算真正可累積的學習基礎。

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown。

所有數學原始碼僅使用：

- inline：` $...$ `
- display：`$$...$$`

不以 Unicode 數學字元替代 LaTeX source，不進行 unicode-escape round-trip，不將聊天渲染畫面視為 canonical source。
