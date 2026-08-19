# T 為什麼是 T？
## 身份根據、不變量、來源鏈與 Identity Certificate 的符號學框架

**英文題名：** *Why Is T T? Identity Grounding, Invariants, Provenance, and the Semiotics of Identity Certificates*  
**系列：**《T 的九問：符號身份、生成、命名與持續》Paper 03  
**版本：** v0.1 理論草稿  
**日期：** 2026-08-12  
**作者：** Neo.K、Aletheia（AI 協作）  
**機構：** EveMissLab／一言諾科技有限公司

---

## 摘要

Paper 01 提出多重同一性符號學（Multi-Identity Semiotics, MIS）與符號身份動力學（Symbolic Identity Dynamics, SID），將「T 是 T／T 不是 T」改寫為多種身份關係下的相同與不同。Paper 02 進一步將「T 是不是 T？」形式化為身份查詢與判定問題。

本文繼續向下追問：

> **即使系統已經判定 \(T_i\) 與 \(T_j\) 是同一個 T，這個判定憑什麼成立？**

本文主張，「T 為什麼是 T？」至少包含兩個不同問題：

\[
\boxed{
\text{What makes T T?}
}
\]

與：

\[
\boxed{
\text{What warrants us to judge T as T?}
}
\]

前者稱為**構成性身份根據**（Constitutive Identity Grounding），研究哪些不變量、關係與持續條件使某個存在構成為該身份；後者稱為**證據性身份根據**（Evidential Identity Grounding），研究觀察者依靠什麼 provenance、紀錄、簽章、命名鏈與可驗證證據，才有資格做出同一性判定。

本文因此定義身份根據物件：

\[
\boxed{
\mathcal G_\alpha(T)
=
(
\mathcal I_\alpha,
\mathcal R_\alpha,
\mathcal H_\alpha,
\mathcal P_\alpha,
\mathcal N_\alpha,
\mathcal O_\alpha,
\mathcal E_\alpha,
\mathcal V_\alpha
)
}
\]

其中：

- \(\mathcal I_\alpha\)：身份不變量；
- \(\mathcal R_\alpha\)：必要關係；
- \(\mathcal H_\alpha\)：歷史連續；
- \(\mathcal P_\alpha\)：provenance；
- \(\mathcal N_\alpha\)：命名與 namespace；
- \(\mathcal O_\alpha\)：功能／算子條件；
- \(\mathcal E_\alpha\)：證據；
- \(\mathcal V_\alpha\)：驗證程序。

本文進一步提出 **Identity Grounding Certificate（IGC）**：一個身份判定不只輸出 Same／Different，而應附帶一個可追溯、可重播、可版本化的 grounding certificate。

核心命題為：

\[
\boxed{
\text{Identity Certificate}
\neq
\text{Identity Itself}
}
\]

以及：

\[
\boxed{
\text{Evidence of Identity}
\neq
\text{Constitutive Ground of Identity}.
}
\]

因此，一個 hash、名稱、序號、簽章或 provenance chain 都可能是強身份證據，卻不必單獨構成身份本身；反之，一個對象可能在構成上保持同一身份，但由於證據鏈斷裂，系統只能輸出 Underdetermined。

---

## 關鍵詞

身份根據、Identity Grounding、身份不變量、provenance、Identity Certificate、構成性條件、證據性條件、命名鏈、歷史連續、符號身份

---

# 0. 研究邊界

本文不主張：

1. 所有身份都有單一形上「本質」；
2. 每一種身份都必須存在不可變核心；
3. provenance 本身等於身份；
4. 名稱、序號或 hash 可以單獨創造身份；
5. Identity Certificate 具有神秘的本體生成力；
6. 沒有證據就代表對象一定不是同一個；
7. 所有身份都必須以密碼簽章驗證；
8. 構成性身份條件與證據性身份條件永遠完全分離；
9. 本文已解決所有跨時間 identity persistence 問題。

本文研究的是：

> **當一個身份判定被提出時，如何要求系統說清楚：究竟是哪一些結構使它成為 T，又是哪一些證據使我們有資格知道它是 T？**

---

# 1. 「為什麼是 T？」其實有兩個問題

考慮：

\[
T_i\equiv_\alpha T_j.
\]

Paper 02 可以輸出：

\[
J_\alpha(T_i,T_j)=\mathrm{Same}.
\]

但現在追問：

> 為什麼？

至少存在兩種回答。

第一種：

> 因為它們保留同一個身份構成條件。

形式：

\[
\operatorname{Ground}^{C}_\alpha(T_i,T_j).
\]

第二種：

> 因為我們有足夠證據證明它們保留同一身份。

形式：

\[
\operatorname{Ground}^{E}_\alpha(T_i,T_j).
\]

因此：

\[
\boxed{
\text{Constitutive Ground}
\neq
\text{Evidential Ground}.
}
\]

身份哲學中，尤其在跨時間身份討論裡，本來就會區分 constitutive criterion 與 evidence question：某種關係「使」一個對象保持同一，和我們用來判斷該關係存在的證據，不是同一問題。

MIS/SID 將這個區分擴展到所有符號身份關係。

---

# 2. 構成性身份根據

定義：

\[
\boxed{
\mathcal G^C_\alpha(T)
}
\]

為身份關係 \(\alpha\) 下，使 \(T\) 構成為該身份的條件集合。

例如：

### Glyph identity

可能只要求：

\[
\mathcal G_G^C(T)=\{G(T)\}.
\]

### Content identity

可能要求：

\[
\mathcal G_X^C(T)=\{\operatorname{CanonicalBytes}(T)\}.
\]

### Historical identity

則不能只看當前 state，而可能要求：

\[
\mathcal G_H^C(T)
=
\{
\text{continuity},
\text{derivation},
\text{authorized transition}
\}.
\]

所以：

\[
\boxed{
\mathcal G_\alpha^C
}
\]

本身是 identity-relation specific 的。

---

# 3. 證據性身份根據

定義：

\[
\boxed{
\mathcal G^E_\alpha(T_i,T_j)
}
\]

為支持身份判定所使用的證據與驗證程序。

它可能包含：

- hash；
- digital signature；
- timestamp；
- database primary key；
- file history；
- migration record；
- naming record；
- chain of custody；
- witness；
- log；
- model state snapshot；
- version record；
- provenance graph。

因此：

\[
\boxed{
\mathcal G^E
\rightarrow
\text{Warrant}
}
\]

而不是：

\[
\mathcal G^E
\rightarrow
\text{Create Identity}.
\]

---

# 4. 身份本身與身份證據的第一個分離

考慮兩份完全相同的檔案：

\[
Hash(f_1)=Hash(f_2).
\]

這可以強力支持：

\[
f_1\equiv_{\mathrm{content}}f_2.
\]

但不能單獨推出：

\[
f_1\equiv_{\mathrm{artifact}}f_2.
\]

因為它們可能：

- 由不同作者建立；
- 產生於不同時間；
- 屬於不同法律文件；
- 位於不同 provenance chain；
- 有不同簽章；
- 被不同制度承認。

所以：

\[
\boxed{
\text{Strong Evidence for One Identity Relation}
\not\Rightarrow
\text{Strong Evidence for Every Identity Relation}.
}
\]

---

# 5. Identity Grounding Object

本文將一個身份根據寫成：

\[
\boxed{
\mathcal G_\alpha(T)
=
(
\mathcal I_\alpha,
\mathcal R_\alpha,
\mathcal H_\alpha,
\mathcal P_\alpha,
\mathcal N_\alpha,
\mathcal O_\alpha,
\mathcal E_\alpha,
\mathcal V_\alpha
)
}
\]

其中：

## \(\mathcal I_\alpha\)：Identity Invariants

哪些結構必須保持。

## \(\mathcal R_\alpha\)：Required Relations

身份是否依賴其他對象、制度或關係。

## \(\mathcal H_\alpha\)：Historical Continuity

跨時間 transition 是否構成一條可接受的持續鏈。

## \(\mathcal P_\alpha\)：Provenance

誰、何時、透過何種活動生成、修改或導出它。

## \(\mathcal N_\alpha\)：Naming / Namespace

名稱與 stable identifier 如何被分配與持續。

## \(\mathcal O_\alpha\)：Operational Conditions

是否必須維持某種功能、能力或算子。

## \(\mathcal E_\alpha\)：Evidence

支持判定的具體資料。

## \(\mathcal V_\alpha\)：Verification

如何重播並驗證以上資料。

---

# 6. 身份不變量不一定是「完全不變」

「不變量」這個詞容易造成誤解。

它不一定意味：

\[
x_t=x_{t+1}.
\]

更常見的是：

\[
\boxed{
I(F(x))=I(x)
}
\]

其中 \(F\) 是允許的 transformation。

因此：

\[
\mathcal I_\alpha
\]

真正描述的是：

> **在身份仍被保留的變換集合下，什麼必須保持不變？**

定義：

\[
\mathcal F_\alpha^{\mathrm{allow}}
\]

為 identity-preserving transformations。

則：

\[
\forall F\in\mathcal F_\alpha^{\mathrm{allow}},
\qquad
I_\alpha(F(T))=I_\alpha(T).
\]

---

# 7. 不變量與變量的分工

一個身份系統不應只列：

> 哪些不能改。

還要列：

> 哪些可以改。

定義：

\[
\mathcal I_\alpha
\]

為身份必要不變量；

\[
\mathcal M_\alpha
\]

為 mutable dimensions。

因此：

\[
\boxed{
Identity_\alpha
=
\text{Invariant Core}
+
\text{Allowed Variation}.
}
\]

例如軟體：

- source code 可以更新；
- UI 可以改；
- dependency 可以改；
- build artifact 可以改；

但若某任務下的 project identity 要持續，可能要求：

- repository history 持續；
- authority 持續；
- project identifier 持續；
- release lineage 可追溯。

---

# 8. 必要條件與充分條件

身份根據需要區分：

\[
N_\alpha
\]

必要條件；

與：

\[
S_\alpha
\]

充分條件。

例如：

\[
\text{same name}
\]

往往不是充分條件。

甚至未必是必要條件。

一個人改名後仍然可能保持身份。

所以：

\[
Name(T_i)=Name(T_j)
\]

不是：

\[
T_i\equiv_H T_j
\]

的必要或充分普遍條件。

身份理論應明確記錄：

\[
\boxed{
N_\alpha,
S_\alpha,
N_\alpha\cap S_\alpha
}
\]

而不是把所有「看起來重要」的欄位都當成等價條件。

---

# 9. 最小充分身份根據

本文定義：

\[
\boxed{
\mathcal G_\alpha^*
}
\]

為 Minimal Sufficient Identity Ground。

若：

\[
\operatorname{Sufficient}(\mathcal G_\alpha^*)=1
\]

且對任一真子集：

\[
\mathcal B\subsetneq\mathcal G_\alpha^*
\]

都有：

\[
\operatorname{Sufficient}(\mathcal B)=0,
\]

則：

\[
\mathcal G_\alpha^*
\]

是最小充分身份根據。

它對工程非常重要。

因為身份判定不能：

- 少到錯誤合併；
- 多到任何變化都被判成新身份。

---

# 10. Provenance 不是附錄，而可能是身份的一部分

對某些身份問題，history/provenance 不是額外 metadata。

它本身可能是 constitutive。

例如：

- 法律原件；
- 藝術品；
- 研究資料；
- 軟體 release；
- 模型 checkpoint；
- Agent 的長期身份。

W3C PROV 將 provenance 建模為 Entity、Activity、Agent 及其 generated、used、derived relations，使來源鏈可以被表示成有向關係結構。

本文將這種思想抽象成：

\[
\boxed{
\mathcal P(T)
=
(V_P,E_P)
}
\]

其中節點可能包括：

\[
\{\mathrm{Entity},\mathrm{Activity},\mathrm{Agent},\mathrm{Event}\}.
\]

---

# 11. 身份來源圖

定義：

\[
\boxed{
P_T
=
\operatorname{ProvGraph}(T).
}
\]

例如：

\[
T_0
\xrightarrow{\mathrm{generatedBy}}
A_1
\xrightarrow{\mathrm{derived}}
T_1
\xrightarrow{\mathrm{migrated}}
T_2.
\]

若 transition 均屬：

\[
\mathcal F_H^{\mathrm{allow}},
\]

則可以支持：

\[
T_0\equiv_HT_2.
\]

因此歷史身份不是：

\[
State(T_0)=State(T_2).
\]

而可能是：

\[
\boxed{
\operatorname{ValidPath}
(
T_0\leadsto T_2
)
=1.
}
\]

---

# 12. Provenance Path Principle

本文提出：

## 原理 1：Provenance Path Principle

對歷史身份而言：

\[
\boxed{
\text{Identity may be grounded by a valid path, not by equal endpoints.}
}
\]

即：

\[
T_0\neq_XT_n
\]

仍可能：

\[
T_0\equiv_HT_n
\]

只要存在：

\[
T_0
\xrightarrow{F_1}
T_1
\xrightarrow{F_2}
\cdots
\xrightarrow{F_n}
T_n
\]

且：

\[
\forall F_i,
\quad
F_i\in\mathcal F_H^{\mathrm{allow}}.
\]

這是跨時間身份研究的重要入口。

---

# 13. 來源鏈斷裂

若：

\[
T_0\leadsto T_1\leadsto ?
\leadsto T_3,
\]

其中 provenance 中間缺失，系統不應自動推：

\[
T_0\equiv_HT_3.
\]

此時可以輸出：

\[
J_H=\mathrm{Unknown}
\]

或：

\[
J_H=\mathrm{Underdetermined}.
\]

這說明：

\[
\boxed{
\text{Identity May Persist}
\land
\text{Identity May Be Unprovable}.
}
\]

即：

> 對象可能真的還是它，但我們已經失去足夠證據證明這件事。

---

# 14. Grounding 與 Warrant 的非對稱

如果：

\[
\mathcal G^C_\alpha
\]

成立，但：

\[
\mathcal G^E_\alpha
\]

缺失，則：

\[
\text{identity may hold}
\]

但：

\[
J_\alpha=\mathrm{Unknown}.
\]

反之，如果：

\[
\mathcal G^E_\alpha
\]

看起來完整，但證據是偽造的，則：

\[
J_\alpha
\]

可能誤判 Same，而 constitutive identity 實際不成立。

所以：

\[
\boxed{
\text{Grounding Failure}
\neq
\text{Evidence Failure}.
}
\]

---

# 15. Identity Grounding Certificate

本文定義：

\[
\boxed{
IGC_\alpha(T_i,T_j)
}
\]

為 Identity Grounding Certificate。

其結構：

\[
\boxed{
IGC
=
(
Q_I,
\alpha,
\mathcal G^C,
\mathcal G^E,
\mathbf I,
P,
N,
E,
V,
S
)
}
\]

其中：

- \(Q_I\)：身份查詢；
- \(\alpha\)：身份判準；
- \(\mathcal G^C\)：構成性根據；
- \(\mathcal G^E\)：證據性根據；
- \(\mathbf I\)：不變量狀態；
- \(P\)：provenance；
- \(N\)：命名／namespace；
- \(E\)：證據；
- \(V\)：驗證規則版本；
- \(S\)：certificate status。

---

# 16. Identity Certificate 不創造身份

這是本文最重要的邊界之一：

\[
\boxed{
IGC(T)
\neq
T.
}
\]

以及：

\[
\boxed{
\operatorname{IssueCertificate}(T)
\not\Rightarrow
\operatorname{CreateIdentity}(T).
}
\]

證書的作用是：

\[
\boxed{
\text{compress + expose + verify identity grounds}.
}
\]

而不是讓一個原本不同的對象因為拿到證書就神奇地變成同一個對象。

---

# 17. Certificate Forgery

如果攻擊者偽造：

\[
IGC^*
\]

使：

\[
IGC^*\models
T_i\equiv_\alpha T_j,
\]

但實際：

\[
T_i\not\equiv_\alpha T_j,
\]

則是：

# Identity Forgery

所以身份治理需要區分：

\[
\boxed{
\text{Identity Security}
}
\]

與：

\[
\boxed{
\text{Object Security}.
}
\]

錯誤身份證書可能讓系統：

- 接受錯的人；
- 接受錯的檔案；
- 接受錯的 Agent；
- 接受偽造歷史；
- 錯誤合併兩個理論版本。

---

# 18. Identity Certificate 的狀態

本文不使用簡單：

\[
\{\mathrm{valid},\mathrm{invalid}\}
\]

處理所有身份證書。

定義：

\[
S_{IGC}
\in
\{
\mathrm{Grounded},
\mathrm{PartiallyGrounded},
\mathrm{Unsupported},
\mathrm{Contradicted},
\mathrm{Expired},
\mathrm{Revoked}
\}.
\]

### Grounded

必要 grounds 與證據均完整。

### PartiallyGrounded

部分構成條件已支持，但仍缺證據。

### Unsupported

沒有足夠 grounds。

### Contradicted

存在高品質反證。

### Expired

certificate 的有效時間或規則版本已過期。

### Revoked

原授權／制度已撤銷該證書。

---

# 19. WhySame 算子

Paper 02 定義判定：

\[
\mathfrak J_I.
\]

本文增加：

\[
\boxed{
\operatorname{WhySame}_\alpha(T_i,T_j)
}
\]

輸出：

\[
(
\mathcal G^C,
\mathcal G^E,
IGC
).
\]

所以成熟系統面對：

> 為什麼這兩個 T 被視為同一個？

不應回答：

> 因為資料庫說是。

而應回答：

> 它們在 history identity 下共享一條合法 provenance path；必要 stable ID 沒有改變；所有 migration 均符合規則 v3；且證據 hash、簽章與遷移紀錄都能驗證。

---

# 20. WhyDifferent 算子

同樣需要：

\[
\boxed{
\operatorname{WhyDifferent}_\alpha(T_i,T_j).
}
\]

因為 Different 也需要 grounds。

可能是：

- 必要 invariant 改變；
- provenance chain 斷裂；
- namespace 不同；
- referent 不同；
- authority 不同；
- impossible transition；
- evidence contradicts continuity。

所以：

\[
\boxed{
\text{Difference Judgment Also Requires Grounding}.
}
\]

---

# 21. Identity Rupture Certificate

如果身份從：

\[
T_t
\equiv_\alpha
T_{t+1}
\]

變成：

\[
T_{t+1}
\not\equiv_\alpha
T_{t+2},
\]

系統可以產生：

\[
\boxed{
IRC_\alpha
=
\operatorname{IdentityRuptureCertificate}.
}
\]

其中記錄：

- 哪個 invariant 失效；
- 哪一個 transition 非法；
- 何時發生；
- 由誰判定；
- 是否可恢復。

Paper 07 將進一步研究這件事。

---

# 22. Identity Grounding Graph

一個 identity certificate 不一定是列表。

更自然的形式是圖：

\[
\boxed{
\mathcal G_I=(V_I,E_I).
}
\]

節點可能包含：

- Object；
- State；
- Identifier；
- Name；
- Agent；
- Event；
- Activity；
- Evidence；
- Signature；
- Rule；
- Time。

邊可能包含：

- derived-from；
- generated-by；
- named-by；
- verified-by；
- authorized-by；
- transformed-by；
- same-under；
- preserves；
- contradicts。

因此：

\[
\boxed{
\text{Identity Grounding}
}
\]

本身可以成為可查詢 graph。

---

# 23. Grounding Graph 的最短證明路徑

若系統要回答：

> 為什麼是同一個？

可以尋找：

\[
\boxed{
p^*
=
\arg\min_{p\in\mathcal P_G}
Cost(p)
}
\]

其中 \(p\) 是 grounding graph 中足以支持身份判定的證明路徑。

這形成：

# Minimal Identity Explanation

也就是：

> 用最少、但足夠的證據解釋身份。

---

# 24. 身份根據與解釋成本

過度完整的 Identity Certificate 也可能造成問題。

例如為了證明一個文字檔相同，不需要附：

- 作者出生證明；
- 電腦序號；
- 所有編輯紀錄；
- 地理位置；
- 網路封包。

因此 Identity Grounding 應具有：

\[
\boxed{
\text{Task-Relative Sufficiency}.
}
\]

對任務 \(\mathcal T\)：

\[
\mathcal G_\alpha^*(\mathcal T)
\]

應是最小充分 grounds，而不是整個宇宙的 provenance。

---

# 25. T 為什麼被叫作 T，仍然不是本文全部

命名是身份根據的一部分，但不是全部。

如果：

\[
N(x)=T,
\]

只說明：

> 某命名事件將 \(T\) 配給 \(x\)。

它不自動推出：

\[
x\in\mathcal T
\]

或：

\[
x\equiv_R T_{\mathrm{old}}.
\]

所以：

\[
\boxed{
\text{Naming Ground}
\neq
\text{Total Identity Ground}.
}
\]

Paper 05 將專門研究命名事件與 naming authority。

---

# 26. Symbol Identity 的 Grounding

若研究的是單符號：

\[
T,
\]

至少可以拆出：

### Glyph Ground

\[
G(T)=\texttt{"T"}.
\]

### Type Ground

\[
T\in\mathcal T_{\mathrm{LatinCapitalT}}.
\]

### State Ground

\[
X(T)=x_i.
\]

### Referential Ground

\[
R(T)=r_i.
\]

### Historical Ground

\[
P(T)=p_i.
\]

因此同一個可見：

\[
T
\]

可以擁有完全不同的：

\[
\mathcal G(T).
\]

---

# 27. TTTTT 的 Grounding Collapse

考慮：

\[
T_1T_2T_3T_4T_5.
\]

如果只保存 glyph：

\[
G(T_i)=T,
\quad
\forall i,
\]

則所有身份 grounding 被壓成同一表面證據。

這形成：

# Grounding Collapse

即：

\[
\boxed{
\Pi_G(\mathcal G(T_i))
=
\Pi_G(\mathcal G(T_j))
}
\]

但：

\[
\mathcal G(T_i)\neq\mathcal G(T_j).
\]

所以表面相同並不只是 state information loss。

還可能是：

\[
\boxed{
\text{Grounding Information Loss}.
}
\]

---

# 28. 身份可驗證性不是身份存在性的必要條件

存在：

\[
T
\]

卻沒有任何外部 observer 能驗證：

\[
IGC(T).
\]

這不必推出：

\[
T
\]

沒有身份。

因此：

\[
\boxed{
\text{Identity Existence}
\not\Rightarrow
\text{Identity Verifiability}.
}
\]

反之：

\[
\boxed{
\text{Identity Verifiability}
\not\Rightarrow
\text{Absolute Ontological Identity}.
}
\]

驗證永遠依賴某個 \(\alpha\)、規則與證據域。

---

# 29. 身份治理的三層

本文因此區分：

## Ontic Layer

\[
\mathcal G^C
\]

什麼使身份成立。

## Epistemic Layer

\[
\mathcal G^E
\]

我們如何知道。

## Institutional Layer

\[
\mathcal G^I
\]

制度允許誰、依什麼規則承認身份。

三者可能一致，也可能不同。

例如：

\[
\text{Ontically Same}
\]

但：

\[
\text{Institutionally Different}.
\]

或：

\[
\text{Institutionally Same}
\]

但：

\[
\text{Evidence Later Reveals Different}.
\]

---

# 30. AI Agent 的身份根據

若一個 Agent 更換模型：

\[
M_1\rightarrow M_2,
\]

但保留：

- stable agent ID；
- memory graph；
- goal history；
- relationship history；
- ownership／authorization；
- migration provenance；

則在某種 Agent historical identity 下：

\[
\mathcal G_H^C
\]

可能仍成立。

但如果只有：

> 名稱仍叫 Aletheia。

則：

\[
N(A_t)=N(A_{t+1})
\]

遠遠不足以證明：

\[
A_t\equiv_HA_{t+1}.
\]

所以：

\[
\boxed{
\text{Same Persona Name}
\not\Rightarrow
\text{Same Agent Identity}.
}
\]

---

# 31. AI Agent 的 Identity Certificate

可以定義：

\[
\boxed{
IGC_{\mathrm{agent}}
=
(
ID,
MemoryLineage,
GoalLineage,
ModelHistory,
Authority,
MigrationProof,
RelationshipHistory,
Version
)
}
\]

這不表示 Agent 身份只能由這些欄位定義。

而是提供一個工程上可驗證的 candidate certificate。

若未來 AI 能跨模型、跨設備、跨平台持續，這類 identity grounding 將比「當前 model name」更重要。

---

# 32. 理論文件本身也需要 Identity Grounding

這套框架也適用於研究文件。

假設：

\[
Paper_{v0.1}
\rightarrow
Paper_{v0.2}
\rightarrow
Paper_{v1.0}.
\]

三份文件 bytes 不同：

\[
X_1\neq X_2\neq X_3.
\]

但若：

- title lineage 持續；
- claim genealogy 可追；
- author lineage 持續；
- version transition 有紀錄；
- revision relation 明確；

則：

\[
Paper_{v0.1}
\equiv_{\mathrm{work}}
Paper_{v1.0}
\]

可以成立。

這就是：

\[
\boxed{
\text{Same Work}
\neq
\text{Same File}.
}
\]

---

# 33. 理論分支與身份分裂

如果：

\[
Paper_1
\rightarrow
\begin{cases}
Paper_A\\
Paper_B
\end{cases}
\]

而兩條分支都聲稱：

> 我才是原版的延續。

則 identity grounding graph 產生 bifurcation。

這時不能只靠名稱。

需要重新指定：

\[
\alpha.
\]

例如：

- canonical branch；
- author-authorized branch；
- semantic successor；
- historical descendant；
- exact continuation。

這會產生：

\[
\boxed{
\text{One Origin}
\not\Rightarrow
\text{One Future Identity}.
}
\]

---

# 34. Identity Grounding Monotonicity 不能預設成立

加入更多證據：

\[
E_1\subset E_2
\]

不保證：

\[
Confidence_{Same}(E_2)
\geq
Confidence_{Same}(E_1).
\]

因為新證據可能揭露：

- provenance 偽造；
- identity collision；
- branch split；
- namespace mismatch。

因此：

\[
\boxed{
\text{More Evidence}
\not\Rightarrow
\text{More Sameness}.
}
\]

更多證據提高的應該是：

\[
\boxed{
\text{Resolution Quality},
}
\]

而不是預設 Same 的分數。

---

# 35. Grounding Revision

Identity Grounding Certificate 必須版本化。

定義：

\[
IGC^{(v)}.
\]

當：

- 規則改變；
- 新證據出現；
- provenance 補齊；
- 舊證據失效；
- namespace 遷移；

則：

\[
IGC^{(v)}
\rightarrow
IGC^{(v+1)}.
\]

判定也可能：

\[
Same
\rightarrow
Underdetermined
\rightarrow
Different.
\]

但：

\[
\Delta J
\]

仍不必表示對象在當下改變。

可能只是：

\[
\boxed{
\text{Grounding Knowledge Changed}.
}
\]

---

# 36. Identity Grounding 的可否證性

成熟身份理論應回答：

> 什麼證據會讓你停止稱它為同一個 T？

因此每個 \(\alpha\) 應具：

\[
\boxed{
Falsifier_\alpha.
}
\]

例如：

### Content identity

不同 canonical hash 可以是反證。

### Historical identity

證明中間 transition 是 unauthorized replacement 可以是反證。

### Referential identity

證明兩個名稱一直指向不同對象可以是反證。

因此：

\[
\boxed{
\text{Identity Grounding Without Possible Defeater}
}
\]

容易退化成不可審計的信念。

---

# 37. Defeater Set

定義：

\[
\boxed{
D_\alpha(T_i,T_j)
=
\{d_1,\ldots,d_n\}.
}
\]

若：

\[
\exists d\in D_\alpha
\]

成立，則可以：

\[
IGC_\alpha
\rightarrow
\mathrm{Contradicted}.
\]

這使身份證書成為：

\[
\boxed{
\text{Defeasible Certificate}
}
\]

而不是永恆不可推翻的神諭。

---

# 38. Identity Certificate 與密碼證書的差別

名稱相似，但兩者不是同一概念。

Cryptographic certificate 主要證明：

- key binding；
- signer／subject relation；
- trust chain。

Identity Grounding Certificate 則可能包含：

- provenance；
- state continuity；
- naming history；
- invariants；
- institutional rules；
- cryptographic evidence。

因此密碼簽章可以成為：

\[
\mathcal E_\alpha
\]

的一部分，但：

\[
\boxed{
\text{Cryptographic Certificate}
\neq
\text{Complete Identity Grounding Certificate}.
}
\]

---

# 39. Identity Grounding 與「T 是 T」

現在重新回到：

\[
T=T.
\]

形式邏輯上：

\[
T=T
\]

不需要額外證明。

但當自然語言說：

> 這個現在看到的 T，就是之前那個 T。

它其實是：

\[
T_t
\equiv_{\alpha}
T_{t+\Delta}.
\]

這時：

\[
\boxed{
\text{Reflexive Logical Identity}
\neq
\text{Re-identification Claim}.
}
\]

後者需要 grounds。

---

# 40. 核心命題一：構成—證據分離

\[
\boxed{
\mathcal G^C_\alpha
\neq
\mathcal G^E_\alpha.
}
\]

身份成立的條件與我們知道身份成立的證據，不應被默認為同一集合。

---

# 41. 核心命題二：證書非身份本身

\[
\boxed{
IGC_\alpha(T)
\neq
Identity_\alpha(T).
}
\]

Identity Certificate 表達身份根據，不創造身份本體。

---

# 42. 核心命題三：歷史身份可由合法路徑支持

若：

\[
T_0
\xrightarrow{F_1}
T_1
\rightarrow\cdots
\xrightarrow{F_n}
T_n
\]

且：

\[
\forall i,\quad
F_i\in\mathcal F_H^{allow},
\]

則即使：

\[
X(T_0)\neq X(T_n),
\]

仍可能：

\[
\boxed{
T_0\equiv_HT_n.
}
\]

---

# 43. 核心命題四：證據鏈斷裂不等於身份必然斷裂

\[
\boxed{
\neg\operatorname{ProvableIdentity}
\not\Rightarrow
\neg\operatorname{Identity}.
}
\]

系統可能只能輸出 Underdetermined。

---

# 44. 核心命題五：身份根據是任務相對的最小充分結構

\[
\boxed{
\mathcal G_\alpha^*(\mathcal T)
}
\]

應追求足以完成任務的最小 grounds，而不是無限制累積 metadata。

---

# 45. Paper 03 的核心算子

Paper 02：

\[
\mathfrak J_I
\]

回答：

> 是不是同一個？

Paper 03 定義：

\[
\boxed{
\mathfrak G_I:
(
T_i,T_j,\alpha,\mathcal T,c,t
)
\longrightarrow
(
\mathcal G^C,
\mathcal G^E,
IGC,
D
)
}
\]

其中：

- \(\mathcal G^C\)：構成性根據；
- \(\mathcal G^E\)：證據性根據；
- \(IGC\)：Identity Grounding Certificate；
- \(D\)：defeater set。

---

# 46. 與既有研究的邊界

身份哲學中，同步 identity criteria 與跨時間 diachronic identity criteria 本來就不是單一統一概念；個人身份文獻也明確區分 persistence condition 與 evidential criterion。這支持本文必須區分「使身份成立」與「使判定有證據」的基本方向。

另一方面，W3C PROV 將 provenance 表示為 Entity、Activity、Agent 及 wasGeneratedBy、used、wasDerivedFrom 等關係，說明來源鏈可以被做成機器可查詢的圖，而不只是敘述性註腳。

本文的新增工作是：

1. 把 provenance 與 identity invariants 放進同一 grounding object；
2. 分離 constitutive ground 與 evidential ground；
3. 定義 Identity Grounding Certificate；
4. 引入 defeater 與 certificate revision；
5. 將 grounding graph 用於符號、文件、Agent 與跨時間身份。

---

# 47. 結論

「T 為什麼是 T？」不能只回答：

> 因為它長得像 T。

也不能只回答：

> 因為它叫 T。

甚至不能只回答：

> 因為資料庫裡 ID 一樣。

真正完整的問題是：

\[
\boxed{
\text{What makes this T the same T, and what evidence warrants that judgment?}
}
\]

因此：

\[
\boxed{
Identity
=
Grounds
+
Relations
+
Allowed Transformations
+
History
}
\]

而我們對身份的知識則是：

\[
\boxed{
Identity Warrant
=
Evidence
+
Provenance
+
Verification
+
Rules.
}
\]

最後：

\[
\boxed{
\text{T 是 T}
}
\]

在形式邏輯裡可以只是反身性。

但：

> **「這個 T 為什麼仍然有資格被稱為那個 T？」**

則需要整套：

\[
\boxed{
\mathcal G_\alpha
}
\]

來回答。

下一篇 Paper 04〈T 怎麼變成 T？〉將把研究從 grounding 推進到 generation：

\[
\boxed{
x
\rightarrow
\text{candidate}
\rightarrow
\text{classified}
\rightarrow
\text{recognized}
\rightarrow
T.
}
\]

也就是：一個原本尚未是 T 的存在，究竟透過什麼過程取得 T 的身份。
