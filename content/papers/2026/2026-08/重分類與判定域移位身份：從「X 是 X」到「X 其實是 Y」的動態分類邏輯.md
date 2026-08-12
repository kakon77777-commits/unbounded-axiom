# 重分類與判定域移位身份：從「X 是 X」到「X 其實是 Y」的動態分類邏輯

**English Title:** Reclassification and Domain-Shifted Identity: A Dynamic Classification Logic from “X Is X” to “X Is Actually Y”  
**Series:** Domain-Transition Information Logic, Paper III  
**Author:** Neo.K  
**Collaborator:** Aletheia (GPT-5.6 Sol)  
**Institution:** EveMissLab / 一言諾科技有限公司  
**Version:** v0.1  
**Date:** 2026-08-10  
**Status:** Series II — Reclassification Paper

## 摘要

Series II 前兩篇分別建立了 Domain-Transition Information Logic（DTIL）的局部四態、判定域、歷史信息狀態，以及 Once / Still / Again 等 path-sensitive operators。然而，「看 X 是 X → 看 X 其實是 Y → 看 Y 又其實是 X」仍包含一種不能由單一 Q4 transition 完整描述的變化：**對象的分類身份發生了變動。**

對固定命題 \(P\)，Q4 處理：

\[
\nu_t(P)
\in
\{
\mathbf Y,\mathbf N,\mathbf B,\mathbf U
\}.
\]

但「X 其實是 Y」通常不是單純：

\[
\nu_t(P_X):
\mathbf Y\rightarrow\mathbf N.
\]

它同時涉及另一個 predicate：

\[
P_Y,
\]

以及一個較高階的分類映射：

\[
\Gamma_{\mathcal J,t}:
\Omega
\rightarrow
2^{\mathcal L_{\mathcal J}},
\]

其中 \(\Omega\) 是對象空間，\(\mathcal L_{\mathcal J}\) 是判定域 \(\mathcal J\) 下可用的分類標籤集合。對象 \(\omega\) 的重分類因此應表示為：

\[
\boxed{
\Gamma_{\mathcal J_0,t_0}(\omega)
\rightsquigarrow
\Gamma_{\mathcal J_1,t_1}(\omega),
}
\]

而不是只記某個真值由 Y 變 N。

本文提出 **Reclassification Operator**、**Classification Identity Vector** 與 **Domain-Shifted Identity**。重分類至少可分成：replacement、refinement、co-classification、evidence correction、judgment-domain remapping、ontic change、semantic retargeting 七類。本文並建立三個核心身份層：

\[
\boxed{
I_O,\quad I_C,\quad I_S
}
\]

分別代表 object identity、classification identity 與 semantic identity。由此可以出現：

\[
I_O=1,\quad I_C=0,\quad I_S=1,
\]

即「還是同一個對象、語義指涉仍相同，但分類改了」；也可以：

\[
I_O\ ? ,\quad I_C=0,\quad I_S=0,
\]

表示所謂重分類其實已經伴隨被指或對象身份改變。

本文特別區分 **belief revision / evidence revision**、**ontology/classification revision** 與 **world/object change**。Dynamic Epistemic Logic 與 belief revision 已長期研究信念如何因新資訊或模型轉換而改變；concept drift 與 ontology evolution 則研究資料分布、概念或本體如何隨時間變化。本文不宣稱首次處理動態信念、concept drift 或 ontology versioning。本文較窄的工作是：把「固定命題的 Q4 狀態變化」與「對象在不同判定域下的分類映射變化」拆成兩種不同 transition，並將其接入 Series II 的 Semantic Identity、Again、history 與 transition-cause framework。

本文的核心命題是：

\[
\boxed{
\text{Changing whether }X(\omega)\text{ is supported}
\neq
\text{changing what }\omega\text{ is classified as}.
}
\]

而：

\[
\boxed{
\text{same object}
\neq
\text{same classification}
\neq
\text{same semantic identity}.
}
\]

**關鍵詞：** Reclassification；判定域；Domain-Shifted Identity；Q4；DTIL；ontology evolution；concept drift；semantic identity；classification；Actually Operator

---

# 1. 第一個問題：\(\mathbf Y\rightarrow\mathbf N\) 到底在改什麼？

假設命題：

\[
P_X(\omega)
=
\text{“}\omega\text{ 是 }X\text{”}.
\]

若：

\[
\nu_{t_0}(P_X)=\mathbf Y
\]

後來：

\[
\nu_{t_1}(P_X)=\mathbf N,
\]

我們只知道：

\[
\boxed{
\text{對 }P_X\text{ 的局部資訊狀態改變了。}
}
\]

這還不能推出：

\[
\omega\text{ 是 }Y.
\]

因為：

\[
\neg X
\]

不等於：

\[
Y.
\]

所以：

\[
\boxed{
\mathbf Y_X\rightarrow\mathbf N_X
}
\]

和：

\[
\boxed{
X\Rightarrow Y
}
\]

是兩種不同操作。

---

# 2. 否定分類不等於新分類

若：

\[
\omega\notin X,
\]

只表示：

\[
X(\omega)=0
\]

或至少 X-membership 未成立。

它不指定：

\[
\omega\in Y
\]

對哪個 \(Y\) 成立。

例如類別空間：

\[
\mathcal L
=
\{
X,Y,Z,W
\}.
\]

從：

\[
X
\]

被排除後，

可能剩：

\[
Y,Z,W.
\]

因此：

\[
\boxed{
\text{declassification}
\neq
\text{reclassification}.
}
\]

---

# 3. 對象空間與分類空間

定義：

\[
\Omega
\]

為對象空間。

令：

\[
\mathcal J
\]

為判定域。

每個判定域有其分類語彙：

\[
\mathcal L_{\mathcal J}.
\]

定義分類映射：

\[
\boxed{
\Gamma_{\mathcal J,t}:
\Omega
\rightarrow
2^{\mathcal L_{\mathcal J}}.
}
\]

使用冪集：

\[
2^{\mathcal L_{\mathcal J}}
\]

是因為一個 object 可以同時屬於多個 class。

因此：

\[
\Gamma_{\mathcal J,t}(\omega)
=
\{X_1,X_2,\ldots\}.
\]

---

# 4. 為什麼分類必須允許多標籤？

對象可能同時是：

\[
\text{人},
\]

\[
\text{研究者},
\]

\[
\text{公司負責人}.
\]

因此：

\[
\omega\in X
\]

與：

\[
\omega\in Y
\]

未必衝突。

所以看到：

\[
Y
\]

被加入分類集合，

不能自動解讀為：

\[
X
\]

被刪除。

這將導向不同的 reclassification types。

---

# 5. OWL 提供一個清楚的工程類比

在 OWL 2 中：

\[
\text{ClassAssertion}(C,I)
\]

就是「individual \(I\) 是 class \(C\) 的 instance」的形式表達。

因此一個 object 的 class membership 與 proposition truth 可以被明確建模成不同層：individual 本身是一個 entity，而 class assertion 是作用於該 entity 的分類敘述。

這與 DTIL 的分類層非常相容：

\[
\boxed{
\omega
\neq
X(\omega).
}
\]

對象不是它的分類斷言本身。

---

# 6. 最小重分類

令：

\[
\Gamma_0(\omega)=\{X\},
\]

後來：

\[
\Gamma_1(\omega)=\{Y\}.
\]

則定義：

\[
\boxed{
\mathsf{Reclass}_{X\Rightarrow Y}(\omega)
}
\]

成立。

這表示：

\[
X
\]

作為主要分類被：

\[
Y
\]

取代。

---

# 7. Replacement Reclassification

定義：

\[
\boxed{
\mathsf{ReplaceClass}_{X\Rightarrow Y}
}
\]

當：

\[
X\in\Gamma_{t^-}(\omega),
\]

\[
X\notin\Gamma_{t^+}(\omega),
\]

\[
Y\notin\Gamma_{t^-}(\omega),
\]

\[
Y\in\Gamma_{t^+}(\omega).
\]

這是最接近：

> X 其實不是 X，而是 Y。

的純 replacement 型。

---

# 8. Refinement 不等於 Replacement

假設：

\[
Y\subseteq X.
\]

原先：

\[
\Gamma_0(\omega)=\{X\},
\]

後來發現更精細：

\[
\Gamma_1(\omega)=\{X,Y\}.
\]

這不是：

\[
X\rightarrow Y
\]

的排他替換。

而是：

\[
\boxed{
\mathsf{Refine}_{X\leadsto Y}.
}
\]

即：

> 原分類仍成立，但現在知道它屬於更具體的子類。

---

# 9. Co-Classification

如果：

\[
X
\]

和：

\[
Y
\]

不是上下位關係，

但 object 同時符合兩者：

\[
\Gamma_0(\omega)=\{X\},
\]

\[
\Gamma_1(\omega)=\{X,Y\},
\]

則：

\[
\boxed{
\mathsf{AddClass}_Y.
}
\]

這叫 co-classification。

它也不是：

\[
X\Rightarrow Y.
\]

---

# 10. Reclassification Type

因此第一版：

\[
\boxed{
\mathcal R_C
=
\{
REPLACE,
REFINE,
GENERALIZE,
ADD,
REMOVE,
REMAP,
RETARGET
\}.
}
\]

其中：

- `REPLACE`：X 被 Y 取代；
- `REFINE`：進入更細類；
- `GENERALIZE`：退到更上位類；
- `ADD`：增加非排他分類；
- `REMOVE`：移除分類但未指定替代；
- `REMAP`：判定域改變後映射到新標籤；
- `RETARGET`：語義／被指本身改變。

---

# 11. 「X 其實是 Y」的技術讀法

自然語言「其實」具有多種語用。

本文不宣稱把所有「其實」統一形式化。

在 DTIL 中暫定一個技術 operator：

\[
\boxed{
\mathsf{Actually}_{X\Rightarrow Y}(\omega)
}
\]

表示：

1. 歷史中 \(X\) 曾是有效或主導 classification；
2. 當前分類機制將 \(Y\) 視為較合適 classification；
3. 這個轉換具有 correction / supersession 關係，而不是單純新增 label。

因此：

\[
\mathsf{Actually}
\]

是一個帶歷史對比的 reclassification operator。

---

# 12. Actually 不等於現在 Y

如果：

\[
Now_Y(\omega)=1,
\]

只說：

> 現在分類為 Y。

但：

\[
\mathsf{Actually}_{X\Rightarrow Y}
\]

還要求：

\[
\boxed{
\text{prior competing classification }X.
}
\]

所以：

\[
\boxed{
\mathsf{Actually}_{X\Rightarrow Y}
\Rightarrow
Now_Y,
}
\]

但：

\[
Now_Y
\not\Rightarrow
\mathsf{Actually}_{X\Rightarrow Y}.
\]

---

# 13. Reclassification Record

每次 reclassification 保存：

\[
\boxed{
\mathcal R_t(\omega)
=
(
\omega,
\Gamma^-,
\Gamma^+,
\mathcal J^-,
\mathcal J^+,
\Psi^-,
\Psi^+,
\chi_t
).
}
\]

其中：

- \(\Gamma^-\)：前分類；
- \(\Gamma^+\)：後分類；
- \(\mathcal J^-,\mathcal J^+\)：判定域；
- \(\Psi^-,\Psi^+\)：語義身份；
- \(\chi_t\)：transition cause。

---

# 14. 三種身份先分開

本文引入：

\[
\boxed{
I_O,
I_C,
I_S.
}
\]

### \(I_O\)：Object Identity

是否仍然追蹤同一 object anchor：

\[
\omega^- \equiv_O \omega^+.
\]

### \(I_C\)：Classification Identity

分類集合是否相同：

\[
\Gamma^-(\omega)
\equiv_C
\Gamma^+(\omega).
\]

### \(I_S\)：Semantic Identity

被指／所指／語義身份是否相同：

\[
\Psi^-
\equiv_S
\Psi^+.
\]

三者不可混成一個「是不是同一個」。

---

# 15. 同一對象、不同分類

可能：

\[
I_O=1,
\]

\[
I_S=1,
\]

但：

\[
I_C=0.
\]

這是最純粹的 reclassification：

\[
\boxed{
\text{same object}
+
\text{same referent}
+
\text{different class}.
}
\]

例如分類規則更精確、證據更新或先前標記被修正。

---

# 16. 同一分類、不同語義對象

也可能：

\[
I_C=1
\]

但：

\[
I_S=0.
\]

例如同一 label：

\[
X
\]

被偷偷用來指不同 referent。

這是：

\[
\boxed{
\text{classification-label persistence with semantic drift}.
}
\]

它不是 identity preservation。

---

# 17. 同一 object anchor 也不必然代表 object 狀態沒變

假設我們持續追蹤同一 entity：

\[
\omega.
\]

其世界狀態：

\[
W_t(\omega)
\]

可能改變。

所以：

\[
I_O=1
\]

只表示：

> 我們還把它視為同一個被追蹤 entity。

不代表：

\[
W_t(\omega)=W_{t+1}(\omega).
\]

---

# 18. 四種重分類來源

至少可區分：

\[
\boxed{
\mathcal C_R
=
\{
E,
J,
W,
\Psi
\}.
}
\]

### Evidence-driven

\[
\Delta E\neq0.
\]

### Judgment-domain-driven

\[
\Delta\mathcal J\neq0.
\]

### World/object-driven

\[
\Delta W\neq0.
\]

### Semantic-driven

\[
\Delta\Psi\neq0.
\]

實際也可能：

\[
MIXED.
\]

---

# 19. Evidence-Driven Reclassification

假設：

\[
W^- = W^+,
\]

\[
\mathcal J^-=\mathcal J^+,
\]

\[
\Psi^-=\Psi^+,
\]

但：

\[
E^-\neq E^+.
\]

因此：

\[
\Gamma^-(\omega)=\{X\},
\]

\[
\Gamma^+(\omega)=\{Y\}.
\]

這是：

\[
\boxed{
\text{classification correction due to new evidence}.
}
\]

---

# 20. Belief Revision 與此有直接鄰近

Dynamic Epistemic Logic 與 belief revision 已長期研究：

\[
\text{new information}
\rightarrow
\text{belief/model change}.
\]

其核心是 agent 接收資訊後，belief state 或 epistemic model 如何改變。

DTIL 的 evidence-driven reclassification 可以使用這些工作作為上游理論資源。

但本文還額外保存：

\[
\boxed{
\Gamma(\omega)
}
\]

作為 object-classification state，而不是只保存 agent belief set。

---

# 21. Judgment-Domain-Driven Reclassification

可能：

\[
E^- = E^+,
\]

\[
W^-=W^+,
\]

\[
\Psi^-=\Psi^+,
\]

但：

\[
\mathcal J^-\neq\mathcal J^+.
\]

因此：

\[
\Gamma_{\mathcal J^-}(\omega)=\{X\},
\]

\[
\Gamma_{\mathcal J^+}(\omega)=\{Y\}.
\]

這是：

\[
\boxed{
\text{Domain-Shifted Reclassification}.
}
\]

不是因為 evidence 新增，

也不是 object 改變，

而是分類系統本身換了。

---

# 22. 這種情況不是矛盾

若：

\[
X@J_A
\]

而：

\[
Y@J_B,
\]

且：

\[
J_A\neq J_B,
\]

不能直接推出：

\[
X\land Y
\]

在單一 domain 中矛盾。

因此：

\[
\boxed{
\text{cross-domain class change}
\neq
\text{local inconsistency}.
}
\]

---

# 23. Ontology Versioning 提供清楚近鄰

OWL 2 允許 ontology IRI 與 version IRI 區分一個 ontology series 的不同版本。

因此同一 individual 的 class assertions 可以在不同 ontology versions 下被不同的 axioms 推導或解釋。

Ontology versioning / evolution 的研究正是處理：

\[
\boxed{
\text{classification framework itself changes over time}.
}
\]

這與 DTIL 的：

\[
\mathcal J_t
\]

非常接近。

---

# 24. 但 Ontology Version 不等於 Judgment Domain

DTIL 的：

\[
\mathcal J
\]

可以包含：

- ontology；
- definitions；
- thresholds；
- evaluation goals；
- admissible distinctions；
- local rules。

所以：

\[
\boxed{
\text{ontology}
\subseteq
\text{possible components of a judgment domain}.
}
\]

Judgment Domain 是更寬的工作概念。

---

# 25. Ontology Inseparability 的啟發

Description-logic ontology research 已研究：

> 一個 ontology 是否能被另一個安全替換？

但「安全」取決於用途。

例如：

- 若關心 query answers，要求 query inseparability；
- 若關心 concept reasoning，則可能要求 concept inseparability。

這提供一個非常重要的啟示：

\[
\boxed{
\text{domain identity is task-relative}.
}
\]

兩個 Judgment Domains 不需要逐字相同，

只需要對指定判定任務保持不可區分。

---

# 26. Judgment-Domain Equivalence

因此定義：

\[
\boxed{
\mathcal J_1
\equiv_{\mathcal Q}
\mathcal J_2
}
\]

表示對 query / classification family：

\[
\mathcal Q
\]

而言，

兩個判定域給出等價結果。

這比：

\[
\mathcal J_1=\mathcal J_2
\]

更實用。

---

# 27. Domain-Shifted Identity

如果：

\[
\mathcal J_0
\not\equiv
\mathcal J_1,
\]

但 object anchor：

\[
I_O=1
\]

且 semantic identity：

\[
I_S=1,
\]

則：

\[
\boxed{
\Gamma_{\mathcal J_0}(\omega)=X,
\qquad
\Gamma_{\mathcal J_1}(\omega)=Y
}
\]

稱為：

\[
\boxed{
\text{Domain-Shifted Identity}.
}
\]

它表示：

> 同一對象在不同判定域下具有不同 classification identity。

---

# 28. Domain-Shifted Identity 不等於 Relative Truth 的全部

本文不主張所有 truth 都只是相對的。

Domain-Shifted Identity 只表示：

\[
\boxed{
\text{classification is indexed by a judgment domain}.
}
\]

這是型別／分類架構的索引問題，

不是一般形而上相對主義論證。

---

# 29. World-Driven Reclassification

可能：

\[
\mathcal J^-=\mathcal J^+,
\]

\[
E
\]

足以反映真實改變，

但 object state：

\[
W^-(\omega)\neq W^+(\omega).
\]

例如 object 本身真的從狀態 A 進入狀態 B。

因此：

\[
\Gamma^-(\omega)=X,
\]

\[
\Gamma^+(\omega)=Y.
\]

這叫：

\[
\boxed{
\text{Ontic Reclassification}.
}
\]

---

# 30. Ontic Reclassification 不是修正舊錯誤

在 evidence correction 中：

> 原先 X 可能就是判錯。

在 ontic change 中：

> 原先 X 在當時可以完全正確，而現在 Y 也完全正確。

所以：

\[
\boxed{
X_{t_0}\rightarrow Y_{t_1}
}
\]

不必含：

\[
\text{prior error}.
\]

---

# 31. Semantic Retargeting

最危險的情況：

\[
\Psi^-\neq\Psi^+.
\]

這可能表示：

> 所謂同一 object / concept，其實已經換了被指。

例如符號：

\[
s=X
\]

沒變，

但：

\[
\rho^-\neq\rho^+.
\]

此時：

\[
\boxed{
\text{apparent reclassification}
}
\]

可能根本不是對同一東西的分類更新。

---

# 32. Retargeting 需要先停下 Identity Claim

若：

\[
I_S=0,
\]

則系統不應直接說：

\[
X\Rightarrow Y
\]

是同一 object 的 reclassification。

更安全是：

\[
\boxed{
\text{SemanticBranch}.
}
\]

也就是：

> 先建立兩個語義身份分支，再判定能否恢復同一性。

---

# 33. Reclassification 與 Q4 如何接上？

對每個 class：

\[
X\in\mathcal L_J,
\]

建立 membership proposition：

\[
P_X(\omega)
=
X(\omega).
\]

因此：

\[
\nu_t(P_X)
\in Q4.
\]

若重分類：

\[
X\Rightarrow Y,
\]

可能同時看到：

\[
\nu(P_X):
\mathbf Y\rightarrow\mathbf N,
\]

和：

\[
\nu(P_Y):
\mathbf N/\mathbf U\rightarrow\mathbf Y.
\]

但 reclassification 本身是：

\[
\boxed{
\text{relation between two membership predicates}.
}
\]

不是其中任一 predicate 的 Q4 transition。

---

# 34. Classification Transition Matrix

若只看兩類：

\[
X,Y,
\]

可建立：

\[
\boxed{
M_C(\omega,t)
=
\begin{pmatrix}
\nu_t(P_X)\\
\nu_t(P_Y)
\end{pmatrix}.
}
\]

例如：

\[
M_C(t_0)
=
\begin{pmatrix}
\mathbf Y\\
\mathbf U
\end{pmatrix},
\]

後來：

\[
M_C(t_1)
=
\begin{pmatrix}
\mathbf N\\
\mathbf Y
\end{pmatrix}.
\]

這才比較接近：

> X 其實是 Y。

---

# 35. Multi-Class Reclassification

一般情況：

\[
\mathcal L
=
\{
X_1,\ldots,X_n
\}.
\]

定義：

\[
\boxed{
\mathbf C_t(\omega)
=
(
\nu_t(P_{X_1}),
\ldots,
\nu_t(P_{X_n})
).
}
\]

因此 object classification 本身是一個 Q4-valued class vector。

Reclassification：

\[
\boxed{
\mathbf C_t(\omega)
\rightarrow
\mathbf C_{t+1}(\omega).
}
\]

---

# 36. 為什麼這比單一 Label 更好？

因為：

\[
X
\]

失效時，

Y 可能：

- 已經成立；
- 尚未知；
- 同時有支持與反證；
- 後來才成立。

Q4-valued class vector 可以保存：

\[
\boxed{
\text{classification uncertainty}.
}
\]

---

# 37. Reclassification Confidence 不應壓成單一概率

對：

\[
X\Rightarrow Y
\]

系統可以分別保存：

```text
X_membership = N
Y_membership = Y
domain_relation = SAME
semantic_identity = ALIGNED
cause = EVIDENCE_UPDATE
```

比：

```text
reclassification_confidence = 0.93
```

更有結構資訊。

---

# 38. 「Y 其實又是 X」

現在處理反向。

歷史：

\[
\Gamma_0(\omega)=\{X\},
\]

\[
\Gamma_1(\omega)=\{Y\},
\]

\[
\Gamma_2(\omega)=\{X\}.
\]

這形成 classification return：

\[
\boxed{
X
\Rightarrow
Y
\Rightarrow
X.
}
\]

但正如 Paper II：

\[
\boxed{
\text{return}
\neq
\text{reset}.
}
\]

---

# 39. Classification Again

定義：

\[
\boxed{
\mathsf{AgainClass}_X(\omega,H)=1
}
\]

如果：

1. 現在 \(X\) 為有效分類；
2. 歷史中曾有 \(X\)；
3. 中間存在一段 \(X\) 不再是有效主分類。

因此：

\[
X\Rightarrow Y\Rightarrow X
\]

可滿足：

\[
\mathsf{AgainClass}_X.
\]

---

# 40. Classification Again 與 Q4 Again 不完全相同

可能：

\[
X
\]

在中間仍是 secondary class，

只是主分類改成 Y。

那麼：

\[
\mathsf{AgainClass}^{primary}_X=1
\]

但 membership proposition：

\[
P_X(\omega)
\]

未必曾離開 \(\mathbf Y\)。

所以：

\[
\boxed{
\text{primary-class return}
\neq
\text{membership-state return}.
}
\]

這再次證明 classification layer 必須獨立存在。

---

# 41. 主分類函數

可選擇性定義：

\[
\boxed{
\gamma_{\mathcal J,t}:
\Omega
\rightarrow
\mathcal L_{\mathcal J}\cup\{\bot\}
}
\]

表示當前主要分類。

其中：

\[
\bot
\]

表示沒有單一主分類。

因此：

\[
\gamma_0(\omega)=X,
\]

\[
\gamma_1(\omega)=Y,
\]

\[
\gamma_2(\omega)=X
\]

就是最乾淨的主分類 Again。

---

# 42. Primary Classification 不是完整 Classification

仍需同時保留：

\[
\Gamma
\]

與：

\[
\gamma.
\]

其中：

\[
\Gamma
\]

是所有有效 class，

\[
\gamma
\]

是主導／當前 focal classification。

否則會把：

\[
\text{主分類改變}
\]

誤解為：

\[
\text{所有舊類別都失效}.
\]

---

# 43. 重分類的歷史身份層級

與 Paper II ReturnIdentity 類似，

定義：

\[
\boxed{
\operatorname{ReclassIdentity}
=
(
I_O,
I_J,
I_S,
I_W
).
}
\]

其中：

- \(I_O\)：same object anchor；
- \(I_J\)：same/equivalent judgment domain；
- \(I_S\)：same semantic identity；
- \(I_W\)：same world/object state。

這四位可以描述「到底變了什麼」。

---

# 44. 純認識重分類

若：

\[
I_O=1,
\]

\[
I_J=1,
\]

\[
I_S=1,
\]

\[
I_W=1,
\]

而：

\[
I_C=0,
\]

則：

\[
\boxed{
\text{Pure Epistemic Reclassification}.
}
\]

即：

> object 沒變、domain 沒變、語義沒變，只是我們的分類判斷改了。

---

# 45. 純判定域重分類

若：

\[
I_O=1,
\]

\[
I_S=1,
\]

\[
I_W=1,
\]

但：

\[
I_J=0,
\]

則：

\[
\boxed{
\text{Pure Domain-Shifted Reclassification}.
}
\]

---

# 46. 純世界狀態重分類

若：

\[
I_O=1,
\]

\[
I_J=1,
\]

\[
I_S=1,
\]

但：

\[
I_W=0,
\]

則：

\[
\boxed{
\text{Ontic State Reclassification}.
}
\]

---

# 47. Semantic Reclassification

若：

\[
I_S=0,
\]

則必須提高風險標記。

因為這可能不是同一對象的分類變動。

定義：

\[
\boxed{
\text{SEMANTIC\_RETARGET}
}
\]

而不是普通：

\[
RECLASS.
\]

---

# 48. Concept Drift 與 DTIL 的關係

Machine-learning concept drift 通常描述：

\[
P_t(X,Y)
\]

或相關 data-generating distribution 隨時間改變。

這可能導致：

\[
\text{classifier decision boundary}
\]

需要更新。

Ontology-stream research 也已研究「semantic concept drift」，將 ontology 所表示的語義結構納入 drift detection。

這些與 DTIL 有交集。

但 DTIL 目前研究的是：

\[
\boxed{
\text{explicit object-level reclassification record}
}
\]

及其：

- judgment domain；
- semantic identity；
- world state；
- Q4 membership history。

---

# 49. Concept Drift 不等於單一 Object Reclassification

Concept drift 可以發生於整體分布：

\[
P_t(X,Y)\neq P_{t+1}(X,Y),
\]

但某個具體 object：

\[
\omega
\]

不一定改分類。

反之，

單一 object 因新證據被修正分類，

也不一定代表整個 population distribution 發生 concept drift。

所以：

\[
\boxed{
\text{population drift}
\neq
\text{object reclassification}.
}
\]

---

# 50. Recurring Concept 與 Classification Again

Concept-drift literature 也會研究 recurring concepts：

> 先前出現過的 concept pattern 後來重新出現。

這與：

\[
\mathsf{Again}
\]

在結構上有相似性。

但仍要區分：

\[
\boxed{
\text{concept recurrence at population level}
}
\]

和：

\[
\boxed{
\text{classification return for one tracked object}.
}
\]

---

# 51. Reclassification Friction

定義：

\[
\boxed{
\mathfrak F_C
=
\Delta
(
\Gamma^-,
\Gamma^+,
\mathcal J^-,
\mathcal J^+,
\Psi^-,
\Psi^+,
W^-,
W^+
).
}
\]

其分量可寫：

\[
\mathfrak F_C
=
(
\Delta_\Gamma,
\Delta_J,
\Delta_\Psi,
\Delta_W
).
\]

如果再加 evidence：

\[
\Delta_E.
\]

它表示：

> 這一次重分類到底改了哪些層？

---

# 52. Minimal Reclassification Delta

定義：

\[
\boxed{
\Delta_C^\ast
=
\arg\min_\Delta \|\Delta\|
}
\]

使：

\[
\gamma(\omega)
\]

由：

\[
X
\]

轉為：

\[
Y.
\]

這回答：

> 最小改變哪個條件，就足以讓 object 從 X 被分類成 Y？

可能是：

- 一條 evidence；
- 一個 threshold；
- 一個 definition；
- 一個 ontology axiom；
- 一個 semantic target。

---

# 53. 這可以用於反事實分類

如果：

\[
\gamma(\omega)=X,
\]

尋找最小：

\[
\Delta
\]

使：

\[
\gamma_{\Delta}(\omega)=Y.
\]

這與 counterfactual explanation 有工程關聯，

但 DTIL 還要求保存：

\[
\boxed{
\text{which layer was changed}.
}
\]

所以：

\[
\Delta E
\]

和：

\[
\Delta J
\]

不能混在同一個黑箱 perturbation。

---

# 54. Reclassification Certificate

每次重分類建立：

```text
object_id
from_classes
to_classes
from_primary
to_primary
from_judgment_domain
to_judgment_domain
object_identity
semantic_identity
world_state_relation
evidence_relation
reclassification_type
cause
q4_membership_changes
history_link
verification
```

這是：

\[
\boxed{
\text{Reclassification Certificate}.
}
\]

---

# 55. False Reclassification

系統可能錯誤地宣稱：

\[
X\Rightarrow Y.
\]

常見失敗：

1. 其實只是新增 Y；
2. X 仍然成立；
3. domain 偷換；
4. referent 偷換；
5. object 偷換；
6. Y 只有 weak evidence；
7. 只是 classifier confidence 改變；
8. ontology labels 其實等價。

因此 reclassification 本身需要 verifier。

---

# 56. Domain Mapping

如果：

\[
\mathcal L_{\mathcal J_0}
\]

和：

\[
\mathcal L_{\mathcal J_1}
\]

使用不同 label set，

需要 mapping：

\[
\boxed{
\mu_{\mathcal J_0\to\mathcal J_1}:
\mathcal L_{\mathcal J_0}
\rightharpoonup
2^{\mathcal L_{\mathcal J_1}}.
}
\]

它可以是 partial mapping。

例如：

\[
X
\mapsto
\{Y_1,Y_2\}.
\]

所以：

\[
\boxed{
\text{domain shift may split one class into several classes}.
}
\]

---

# 57. Merge Mapping

也可能：

\[
X_1,X_2
\]

在新 domain 中合成：

\[
Y.
\]

因此 mapping 不必一對一。

這與 ontology matching / version alignment 的工程問題直接相鄰。

---

# 58. 無 Mapping 時不能聲稱「同一分類」

若：

\[
\mu
\]

不存在或未驗證，

就不能說：

\[
X@J_0
=
Y@J_1.
\]

最多：

```text
POSSIBLE_DOMAIN_CORRESPONDENCE
```

所以：

\[
\boxed{
\text{cross-domain identity requires an explicit bridge}.
}
\]

---

# 59. Domain Bridge Certificate

建立：

```text
source_domain
target_domain
source_class
target_class
mapping_type
preserved_queries
lost_distinctions
gained_distinctions
evidence
status
```

這與 Bridge Paper 的 Semantic Preservation Certificate 是互補的。

---

# 60. 「Y 又其實是 X」的四種可能

歷史：

\[
X\Rightarrow Y\Rightarrow X.
\]

可能至少有：

### A. Error Correction Loop

第一次 X 判錯 → 修成 Y → 後來又證明原 X 才對。

### B. Domain Loop

\[
J_0\to J_1\to J_0.
\]

分類隨 domain 返回。

### C. World Loop

object 本身：

\[
W_X\to W_Y\to W_X.
\]

### D. Semantic Pseudo-Loop

label 回 X，

但 referent 已不同。

四者不能混成同一個：

\[
X\to Y\to X.
\]

---

# 61. Reclassification Cause Path

因此每條 classification loop 應保存：

\[
\boxed{
\Lambda_C
=
(
c_1,c_2,\ldots
).
}
\]

例如：

\[
X
\xRightarrow{E}
Y
\xRightarrow{E}
X
\]

與：

\[
X
\xRightarrow{J}
Y
\xRightarrow{J}
X
\]

不同。

---

# 62. Classification Return Identity

定義：

\[
\boxed{
R_C
=
(
R_{\gamma},
R_J,
R_\Psi,
R_W
).
}
\]

其中：

- \(R_\gamma\)：主分類返回；
- \(R_J\)：判定域返回；
- \(R_\Psi\)：語義身份返回；
- \(R_W\)：world state 返回。

所以：

\[
\boxed{
\text{X 又是 X}
}
\]

可以被解壓成一個 return vector。

---

# 63. 「同一個 X」需要指定同一在哪裡

可能：

\[
X_0
=
_{\text{label}}
X_2,
\]

但：

\[
X_0
\neq_{\text{domain}}
X_2.
\]

也可能：

\[
X_0
=
_{\text{domain}}
X_2,
\]

但：

\[
X_0
\neq_{\text{semantic}}
X_2.
\]

因此：

\[
\boxed{
\text{identity must always be indexed by criterion}.
}
\]

---

# 64. 與 Theseus 類問題的界線

本文不是要解決一般形而上的「這還是不是同一個東西」。

DTIL 只建立工程層：

\[
\boxed{
\text{which identity dimensions are being held fixed?}
}
\]

例如：

- object ID；
- world-state continuity；
- semantic referent；
- classification；
- judgment domain。

這可以避免把所有 identity 問題壓成單一布林值。

---

# 65. Minimal Runtime Schema

```text
TrackedObject:
    object_id
    semantic_state_id
    world_state_id

ClassificationState:
    object_id
    judgment_domain_id
    valid_classes
    primary_class
    class_q4_vector
    timestamp

Reclassification:
    from_state
    to_state
    type
    cause
    domain_bridge
    semantic_identity
    object_identity
    verification
```

---

# 66. 最小判定演算法

```text
classify(object, context):
    psi = resolve_semantic_identity(object, context)
    W   = resolve_world_state(object, context)
    J   = resolve_judgment_domain(context)

    class_vector = evaluate_memberships(object, J, psi, W)
    primary      = choose_primary_class(class_vector, J)

    current = ClassificationState(
        object,
        J,
        class_vector,
        primary
    )

    previous = load_previous_classification(object)

    if previous:
        diff = compare_classification(previous, current)
        cause = classify_reclassification_cause(
            previous, current
        )
        identity = audit_identity(previous, current)

        append_reclassification(
            previous,
            current,
            diff,
            cause,
            identity
        )

    return current
```

---

# 67. Unit Test 1：否定 X 不等於 Y

輸入：

\[
\nu(P_X):
Y\rightarrow N.
\]

但：

\[
\nu(P_Y)=U.
\]

要求：

```text
X_removed = true
Y_assigned = false
RECLASS_X_TO_Y = false
```

---

# 68. Unit Test 2：Refinement

\[
\Gamma_0=\{X\},
\]

\[
\Gamma_1=\{X,Y\},
\]

且：

\[
Y\subseteq X.
\]

要求：

```text
type = REFINE
replacement = false
```

---

# 69. Unit Test 3：Evidence Correction

固定：

\[
J,\Psi,W.
\]

只改：

\[
E_0\neq E_1.
\]

分類：

\[
X\rightarrow Y.
\]

要求：

```text
type = REPLACE
cause = EVIDENCE_UPDATE
object_identity = SAME
semantic_identity = SAME
```

---

# 70. Unit Test 4：Domain Shift

固定：

\[
\omega,\Psi,W,E.
\]

但：

\[
J_0\neq J_1.
\]

且：

\[
\Gamma_{J_0}(\omega)=X,
\]

\[
\Gamma_{J_1}(\omega)=Y.
\]

要求：

```text
cause = JUDGMENT_DOMAIN_SHIFT
local_contradiction = false
```

---

# 71. Unit Test 5：World Change

固定：

\[
J,\Psi.
\]

但：

\[
W_0\neq W_1.
\]

分類：

\[
X\rightarrow Y.
\]

要求：

```text
cause = WORLD_CHANGE
prior_classification_may_have_been_correct = true
```

---

# 72. Unit Test 6：Semantic Retarget

符號與 object label 看似相同，

但：

\[
\Psi_0\neq\Psi_1.
\]

要求：

```text
type = RETARGET
ordinary_reclassification = false
semantic_review_required = true
```

---

# 73. Unit Test 7：Classification Again

\[
\gamma_0=X,
\]

\[
\gamma_1=Y,
\]

\[
\gamma_2=X.
\]

要求：

\[
AgainClass_X=1.
\]

同時記：

\[
R_{\gamma}=1.
\]

---

# 74. Unit Test 8：Pseudo-Classification Return

同樣：

\[
\gamma_0=X,
\qquad
\gamma_2=X,
\]

但：

\[
\Psi_0\neq\Psi_2.
\]

要求：

```text
primary_class_return = true
semantic_return = false
pseudo_return = true
```

---

# 75. Unit Test 9：Ontology Mapping Split

若：

\[
\mu(X)=\{Y_1,Y_2\},
\]

則不能強迫：

\[
X=Y_1
\]

或：

\[
X=Y_2.
\]

要求：

```text
mapping = SPLIT
one_to_one_identity = false
```

---

# 76. Unit Test 10：Same Label, Different Domain Meaning

\[
X@J_0,
\]

\[
X@J_1,
\]

但：

\[
\mu_{J_0\to J_1}(X)\neq X.
\]

要求：

```text
surface_label_same = true
domain_class_identity = false
```

這是高語義資料中特別危險的一種情況。

---

# 77. 與 Dynamic Epistemic Logic 的學術位置

Dynamic Epistemic Logic 已成熟研究 epistemic model change、public announcements、belief revision 與 probabilistic update等問題。

因此本文不能把：

\[
\text{belief state changes after new information}
\]

當成新穎性。

本文較窄的工作是：

\[
\boxed{
\text{separating proposition-state revision from object-classification revision}.
}
\]

也就是把：

\[
\nu_t(P_X)
\]

與：

\[
\Gamma_t(\omega)
\]

分成兩層。

---

# 78. 與 Concept Drift 的學術位置

Concept-drift research 已研究 data distribution 與 learned concept 隨時間改變，也已有 ontology-stream semantic drift 方法。

因此本文不能宣稱首次描述：

\[
\text{concepts change over time}.
\]

本文的工作單位是：

\[
\boxed{
\text{one tracked object across changing judgment / semantic / world states}.
}
\]

並要求把 reclassification 的 cause 與 identity layer 顯式記錄。

---

# 79. 與 Ontology Evolution 的學術位置

Ontology versioning、ontology matching、conservative extension 與 inseparability 已建立大量「不同 ontology 如何比較、更新與安全替換」的理論與工程工作。

OWL 2 本身也提供 ontology IRI / version IRI，以及 class assertions 等形式結構。

因此本文不宣稱：

\[
\text{ontology versioning}
\]

為新概念。

本文借用其啟發建立：

\[
\boxed{
\text{Judgment-Domain Bridge}
}
\]

以回答：

> 兩個判定域中的 X 與 Y 到底在什麼意義下可以視為同一分類？

---

# 80. 本篇的較窄核心貢獻

可以壓成五點。

## Result 1

\[
\boxed{
\text{Q4 state change}
\neq
\text{reclassification}.
}
\]

## Result 2

\[
\boxed{
\text{declassification}
\neq
\text{replacement}.
}
\]

## Result 3

\[
\boxed{
I_O
\neq
I_C
\neq
I_S.
}
\]

同一 object、同一 class、同一 semantic referent 是不同身份問題。

## Result 4

\[
\boxed{
\Gamma_{\mathcal J_0}(\omega)=X,
\quad
\Gamma_{\mathcal J_1}(\omega)=Y
}
\]

可表示 Domain-Shifted Identity，而不必構成局部矛盾。

## Result 5

\[
\boxed{
X\Rightarrow Y\Rightarrow X
}
\]

只表示 classification return；是否是 semantic / judgment / world return 必須另外判定。

---

# 81. 研究邊界

本文不主張：

1. 所有自然語言「其實」都等於 correction operator；
2. 每個 object 都有唯一可追蹤 identity anchor；
3. classification 一定是集合式 membership；
4. ontology 等同 Judgment Domain；
5. concept drift 等同 reclassification；
6. semantic identity 可以完全自動判定；
7. world state 可以被完美觀測；
8. domain mappings 總能建立；
9. class hierarchy 永遠固定；
10. 本文已解決一般形而上 identity 問題。

本文只建立：

\[
\boxed{
\text{a typed reclassification layer for DTIL}.
}
\]

---

# 82. 結論：先問「還是不是同一個對象」，再問「它現在是哪一類」

Series II / Paper I 告訴我們：

\[
\mathbf B
\neq
\mathbf Y\to\mathbf N.
\]

Paper II 告訴我們：

\[
\text{Again}
\neq
\text{identity}.
\]

Paper III 再加入：

\[
\boxed{
\text{classification transition}
\neq
\text{truth / information-state transition}.
}
\]

因此「X 其實是 Y」至少要拆成：

\[
\boxed{
\omega
+
\Psi
+
\mathcal J
+
\Gamma
+
\nu
+
H.
}
\]

也就是先問：

1. 還在追蹤同一個 object 嗎？
2. 被指／所指還相同嗎？
3. 判定域還相同嗎？
4. X membership 現在是什麼 Q4 狀態？
5. Y membership 現在是什麼 Q4 狀態？
6. 分類是 replacement、refinement、addition 還是 domain remap？
7. 這次改變由 evidence、world、domain 還是 semantic shift 造成？
8. 以前是否曾經有過同樣分類？

因此：

\[
\boxed{
\text{“X is actually Y”}
}
\]

不再是一句模糊的自然語言修正。

在 DTIL 中，它可以被拆成：

\[
\boxed{
\mathsf{Actually}_{X\Rightarrow Y}
(
\omega,
\mathcal J,
\Psi,
H
).
}
\]

而如果未來：

\[
Y\Rightarrow X,
\]

則也不能只說：

> 又回去了。

還必須輸出：

\[
\boxed{
\operatorname{ClassificationReturn}
=
(
R_{\gamma},
R_J,
R_\Psi,
R_W
).
}
\]

回答：

> **究竟是哪一層回去了？**

這就是 Series II 從「歷史真值」進一步走向「歷史分類身份」的第三步。

下一篇將進入 **Series II / Paper IV：Judgment Friction and Transition-Boundary Information**，正式處理本系列最初的另一個核心命題：

\[
\boxed{
\text{狀態改變的那一瞬間差異，本身就是資訊。}
}
\]

也就是研究：

\[
t^-,
\quad
t^\ast,
\quad
t^+,
\]

以及：

\[
\Delta E,
\Delta W,
\Delta J,
\Delta\Psi,
\Delta\Gamma,
\Delta\nu
\]

如何形成可保存、可比較、可壓縮的 **Judgment Friction** 與 transition-boundary information。

---

## 參考文獻

Baltag, A., Moss, L. S., & Solecki, S. (1998). *The Logic of Public Announcements, Common Knowledge, and Private Suspicions*. TARK VII.

Stanford Encyclopedia of Philosophy. *Dynamic Epistemic Logic*.

Belardinelli, G., & Zhang, S. (2026). *Belief Contraction in Dynamic Epistemic Logic*. arXiv:2606.31861.

Webb, G. I., Hyde, R., Cao, H., Nguyen, H. L., & Petitjean, F. (2016). *Characterizing Concept Drift*. Data Mining and Knowledge Discovery.

Lu, J., Liu, A., Dong, F., Gu, F., Gama, J., & Zhang, G. (2020). *Learning under Concept Drift: A Review*. IEEE Transactions on Knowledge and Data Engineering.

Lecue, F., Chen, J., Pan, J. Z., & Chen, H. (2017). *Learning from Ontology Streams with Semantic Concept Drift*. IJCAI / arXiv:1704.07466.

W3C. *OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition)*.

Qiang, Z., Taylor, K., & Wang, W. (2024). *OM4OV: Leveraging Ontology Matching for Ontology Versioning*. arXiv:2409.20302.

Botoeva, E., Konev, B., Lutz, C., Ryzhikov, V., Wolter, F., & Zakharyaschev, M. (2020). *Inseparability and Conservative Extensions of Description Logic Ontologies: A Survey*. Reasoning Web / arXiv:1804.07805.
