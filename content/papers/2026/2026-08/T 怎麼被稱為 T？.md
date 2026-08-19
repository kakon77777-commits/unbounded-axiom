# T 怎麼被稱為 T？
## 命名事件、指涉鏈、權威與 Namespace 下的符號身份

**英文題名：** *How Does T Come to Be Called T? Naming Events, Referential Chains, Authority, and Symbolic Identity across Namespaces*  
**系列：**《T 的九問：符號身份、生成、命名與持續》Paper 05  
**版本：** v0.1 理論草稿  
**日期：** 2026-08-12  
**作者：** Neo.K、Aletheia（AI 協作）  
**機構：** EveMissLab／一言諾科技有限公司

---

## 摘要

Paper 01 將「T 是 T／T 不是 T」拆解為多重身份關係；Paper 02 將「T 是不是 T？」形式化為身份判定；Paper 03 研究「T 為什麼是 T？」並提出 Identity Grounding Certificate；Paper 04 則將「T 怎麼變成 T？」展開為 Discovery、Transformation、Relational Acquisition、Institutional Conferment、Emergence 與 Criterion Shift 等身份生成機制。

本文進一步處理：

> **T 怎麼被稱為 T？**

本文主張：

\[
\boxed{
\text{Name}
\neq
\text{Object}
\neq
\text{Identity}
\neq
\text{Reference Relation}.
}
\]

一個名稱 \(n\) 與對象 \(x\) 之間的關係，不能只寫成：

\[
n=x.
\]

更完整的命名結構應至少包含：

\[
\boxed{
\mathcal N
=
(
A,
x,
n,
c,
t,
\Gamma_N,
Auth,
E,
P
)
}
\]

其中：

- \(A\)：命名者／名稱使用者；
- \(x\)：被命名或被指涉對象；
- \(n\)：名稱形式；
- \(c\)：語境與 namespace；
- \(t\)：時間；
- \(\Gamma_N\)：命名機制；
- \(Auth\)：命名權威；
- \(E\)：支持指涉的證據；
- \(P\)：naming provenance。

本文進一步區分：

1. **Naming Event**：第一次或重新授予名稱；
2. **Reference Fixing**：名稱如何首次鎖定對象；
3. **Name Transmission**：後續使用者如何繼承名稱—對象關係；
4. **Name-Use Practice**：同一字形名稱在不同使用鏈中可能具有不同指涉；
5. **Alias / Renaming**：同一身份可對應多個名稱；
6. **Homonymy / Collision**：同一名稱可對應多個對象；
7. **Translation / Transliteration**：跨語言名稱形式改變但指涉可能持續；
8. **Namespace Resolution**：只有 local name 時不足以唯一決定身份；
9. **Authority and Contestation**：誰有權指定 canonical name；
10. **Reference Drift / Hijack**：名稱使用鏈可能偏離原始 referent。

因此：

\[
\boxed{
\text{Same Name}
\not\Rightarrow
\text{Same Referent}
}
\]

以及：

\[
\boxed{
\text{Different Name}
\not\Rightarrow
\text{Different Referent}.
}
\]

本文定義 Naming Event Certificate（NEC）、Naming Chain（NC）、Referential Continuity Certificate（RCC）與 Namespace-Qualified Name（NQN），並提出：

\[
\boxed{
\text{Name Identity}
=
\text{Name Form}
+
\text{Name-Use Practice}
+
\text{Namespace}
+
\text{Referential Provenance}.
}
\]

最後，本文指出「T 被稱為 T」與「T 是 T」只有在某些身份關係與命名制度下重合。名稱可以是身份證據、身份入口、身份治理介面，甚至是制度身份的一部分，但不能被默認為身份本體本身。

---

## 關鍵詞

命名、指涉、proper names、Naming Event、Reference Fixing、causal-historical chain、rigid designation、alias、rename、namespace、referential continuity、符號身份

---

# 0. 研究邊界

本文不主張：

1. 名稱的指涉只能由單一 causal-historical theory 解釋；
2. 描述理論、直接指稱理論或 rigid designation 中任何一派已被本文最終裁定；
3. 所有名稱都有唯一 referent；
4. 每個名稱都必須由正式命名儀式產生；
5. 名稱一旦被賦予就永遠不能改變；
6. 同名必然同物；
7. 異名必然異物；
8. namespace 是自然語言命名的完整模型；
9. 制度有權任意改寫所有層級的身份；
10. 命名本身就能創造任何自然或本體身份。

本文研究的是：

> **一個符號形式如何進入穩定的名稱使用實踐，並在特定語境、歷史與制度下持續指向某個對象。**

---

# 1. 「T 是 T」與「它叫 T」是兩個命題

考慮：

\[
Be(x,T).
\]

它可以表示：

> \(x\) 在某種身份關係下是 T。

而：

\[
Name_A(x)=T
\]

表示：

> 主體 \(A\) 使用名稱 T 指稱 \(x\)。

兩者沒有普遍等價：

\[
\boxed{
Be(x,T)
\not\Leftrightarrow
Name_A(x)=T.
}
\]

可能：

\[
Be(x,T)=1
\]

但：

\[
Name_A(x)\neq T.
\]

也可能：

\[
Name_A(x)=T
\]

但：

\[
Be(x,T)=0.
\]

因此：

\[
\boxed{
\text{Being T}
\neq
\text{Being Called T}.
}
\]

---

# 2. 名稱不是對象

設：

\[
n
\]

為一個名稱。

它本身是符號存在，可以具有：

- glyph；
- phonology；
- token；
- type；
- language；
- namespace；
- usage history。

而：

\[
x
\]

是名稱所指向的對象。

所以：

\[
\boxed{
n\neq x.
}
\]

名稱與對象之間真正重要的是：

\[
\boxed{
Ref(n,u,c,t)=x,
}
\]

其中：

- \(u\)：一次具體 name use；
- \(c\)：語境；
- \(t\)：時間。

因此：

\[
\boxed{
\text{Name–Object Identity}
}
\]

應被替換為：

\[
\boxed{
\text{Name–Object Referential Relation}.
}
\]

---

# 3. 名稱哲學的外部定位

名稱與指涉的哲學研究並沒有單一公認機制。

至少存在多種重要路線：

- 將名稱指涉與某些描述內容連結的 descriptivist approaches；
- 將名稱理解為直接或較直接指向對象的路線；
- causal / historical approaches；
- rigid designation；
- predicativist 或 name-practice 類分析。

本文不在此裁決哪一派完整正確。

MIS/SID 的目的，是建立更高一層的 machine-readable naming framework：

\[
\boxed{
\text{Whatever fixes reference must become explicit metadata in the identity system.}
}
\]

---

# 4. Naming Event

定義：

\[
\boxed{
NE
=
(
A,
x,
n,
c,
t,
\Gamma_N,
Auth,
E,
P
)
}
\]

為 Naming Event。

其中：

- \(A\)：執行命名的 agent；
- \(x\)：被命名對象；
- \(n\)：名稱；
- \(c\)：命名語境；
- \(t\)：命名時間；
- \(\Gamma_N\)：命名機制；
- \(Auth\)：權威條件；
- \(E\)：支持資料；
- \(P\)：命名 provenance。

命名因此不是：

\[
n=x,
\]

而是事件：

\[
\boxed{
A
\xrightarrow{\operatorname{Name}}
x
\mapsto n.
}
\]

---

# 5. Naming Mechanism

本文暫定：

\[
\boxed{
\Gamma_N
\in
\{
Baptism,
DescriptionFixing,
InstitutionalAssignment,
Inheritance,
SelfNaming,
CommunityEmergence,
AliasCreation,
Renaming,
Translation,
Transliteration
\}.
}
\]

不同 naming mechanism 不能默認成同一種指涉生成。

---

# 6. Baptism / Initial Naming

一個名稱可能透過某次初始命名事件：

\[
NE_0
\]

被配給對象：

\[
x.
\]

簡化：

\[
\boxed{
NE_0:
n\mapsto x.
}
\]

後續名稱使用者未必重新執行同樣的命名。

他們可能只是繼承：

\[
n
\]

的既有使用鏈。

這使名稱具有：

\[
\boxed{
\text{Naming Provenance}.
}
\]

---

# 7. Reference Fixing 與名稱意義必須分離

某個描述：

\[
D(x)
\]

可以用來幫助首次鎖定 referent：

\[
D
\xrightarrow{\operatorname{fix}}
n\mapsto x.
\]

但即使描述參與 reference fixing，也不必推出：

\[
Meaning(n)=D.
\]

因此：

\[
\boxed{
\text{Reference-Fixing Description}
\neq
\text{Necessary Semantic Content of the Name}.
}
\]

這個區分對 machine identity 很重要。

例如：

> 「第一個完成某事件的 Agent」

可以用來首次找到一個 stable agent ID。

但之後即使該 Agent 不再滿足該描述，名稱仍可能持續指向它。

---

# 8. Naming Chain

定義：

\[
\boxed{
NC(n)
=
(
u_0,u_1,\ldots,u_k
)
}
\]

其中：

\[
u_i
\]

表示一次 name-use event。

如果：

\[
u_0
\]

指向：

\[
x,
\]

而後續使用透過合法傳承維持 referent，則：

\[
\boxed{
Ref(u_i)=x.
}
\]

Naming Chain 因而是 reference persistence 的候選機制之一。

---

# 9. Name-Use Practice

同一 name form：

\[
n
\]

不必只有一條 naming chain。

例如：

\[
NC_1(n)
\]

與：

\[
NC_2(n)
\]

可以獨立形成。

所以：

\[
\boxed{
NameForm(n)
}
\]

不足以唯一決定：

\[
Ref(n).
\]

更完整的名稱身份是：

\[
\boxed{
n^*
=
(
Form,
Practice,
Namespace,
History
).
}
\]

---

# 10. Same Name 不等於 Same Referent

如果：

\[
Form(n_1)=Form(n_2)=T,
\]

仍可能：

\[
Ref(n_1)\neq Ref(n_2).
\]

所以：

\[
\boxed{
\text{Same Name Form}
\not\Rightarrow
\text{Same Referent}.
}
\]

這是：

# Naming Collision

最普通的例子就是不同的人可以共享相同名字。

在程式系統裡，同一 local identifier 也可能在不同 scope 指向不同 object。

---

# 11. Different Name 不等於 Different Referent

反方向也不成立。

可能：

\[
n_1\neq n_2
\]

但：

\[
Ref(n_1)=Ref(n_2)=x.
\]

例如：

- alias；
- stage name；
- translated name；
- former name；
- code name；
- technical identifier；
- multiple historical names。

因此：

\[
\boxed{
\text{Different Names}
\not\Rightarrow
\text{Different Referents}.
}
\]

---

# 12. Hesperus–Phosphorus 型結構

一個經典名稱哲學結構是：

\[
n_1\neq n_2
\]

但：

\[
Ref(n_1)=Ref(n_2).
\]

也就是兩個不同命名／發現路徑最後指向同一 object。

MIS/SID 將它表示為：

\[
\boxed{
NC(n_1)\neq NC(n_2),
\qquad
R(n_1)=R(n_2).
}
\]

因此：

\[
\boxed{
\text{Referential Convergence}
}
\]

本身是一種身份事件。

---

# 13. Referential Convergence Event

定義：

\[
\boxed{
RCE
=
(
n_1,
n_2,
x,
E,
t
)
}
\]

表示原本被視為指向不同對象的兩個 naming chain，被新證據證明：

\[
Ref(n_1)=Ref(n_2)=x.
\]

此時改變的是：

\[
\Delta Knowledge
\]

與名稱關係圖，而不是對象突然融合。

---

# 14. Referential Divergence Event

反過來，也可能原本以為：

\[
Ref(n_1)=Ref(n_2),
\]

後來證明：

\[
Ref(n_1)\neq Ref(n_2).
\]

定義：

\[
\boxed{
RDE
=
Referential\ Divergence\ Event.
}
\]

因此：

\[
\boxed{
\Delta Reference Judgment
\not\Rightarrow
\Delta Object.
}
\]

---

# 15. Alias

若：

\[
n_1,n_2,\ldots,n_k
\]

都合法指向：

\[
x,
\]

則定義 Alias Set：

\[
\boxed{
Alias(x)
=
\{
n_1,n_2,\ldots,n_k
\}.
}
\]

但 alias set 不代表這些名稱在所有語境都完全可互換。

因為它們可能：

- 語體不同；
- 權威不同；
- 歷史不同；
- 隱私級別不同；
- 法律效力不同。

所以：

\[
\boxed{
\text{Co-reference}
\neq
\text{Full Pragmatic Equivalence}.
}
\]

---

# 16. Canonical Name

制度可能指定：

\[
\boxed{
CanonicalName_c(x)=n^*.
}
\]

但 canonical name 只是：

> 在制度 \(c\) 下被選定為標準名稱的符號。

它不等於：

\[
\boxed{
\text{The One Metaphysically True Name}.
}
\]

因此：

\[
\boxed{
Canonical
\neq
Ontologically Unique.
}
\]

---

# 17. Renaming

定義：

\[
\boxed{
RE
=
(
x,
n_{old},
n_{new},
t,
Auth,
P
)
}
\]

為 Renaming Event。

若：

\[
Ref(n_{old})=x
\]

且事件後：

\[
Ref(n_{new})=x,
\]

則：

\[
\boxed{
\Delta Name
\not\Rightarrow
\Delta Referential Identity.
}
\]

所以：

\[
\boxed{
\text{Renamed T}
}
\]

仍可能是同一個 historical T。

---

# 18. Renaming 的三種模式

## 18.1 Replacement

\[
n_{old}
\rightarrow
n_{new}
\]

舊名正式退出。

## 18.2 Alias Addition

\[
Alias(x)
\rightarrow
Alias(x)\cup\{n_{new}\}.
\]

## 18.3 Forked Naming

不同社群：

\[
C_1,C_2
\]

各自使用：

\[
n_1,n_2.
\]

沒有單一 globally canonical name。

---

# 19. Name Persistence 與 Object Persistence

如果名稱：

\[
n
\]

持續存在一百年，不代表 referent 一百年完全不變。

反之，referent 保持歷史身份，也不要求名稱不變。

因此：

\[
\boxed{
\text{Name Persistence}
\neq
\text{Object Persistence}.
}
\]

Paper 06 將專門研究後者。

---

# 20. Empty Name / Failed Reference

若：

\[
Ref(n)=\varnothing,
\]

名稱仍可能作為符號與 name-use practice 存在。

所以：

\[
\boxed{
\text{Name Exists}
\not\Rightarrow
\text{Referent Exists}.
}
\]

身份系統因此需要：

\[
ReferenceStatus(n)
\in
\{
Resolved,
Ambiguous,
Empty,
Contested,
Historical,
Unknown
\}.
\]

---

# 21. Ambiguous Name

若：

\[
Ref(n)
=
\{
x_1,x_2,\ldots,x_k
\},
\qquad
k>1,
\]

而語境不足以解析：

\[
x_i,
\]

則：

\[
\boxed{
ReferenceStatus(n)=Ambiguous.
}
\]

此時系統不能將 name form 自動當作 unique key。

---

# 22. 名稱不是 Primary Key

因此在工程上：

```text
name = "T"
```

不應被預設等於：

```text
identity_id = "T"
```

成熟系統應分開：

\[
\boxed{
DisplayName
}
\]

與：

\[
\boxed{
StableIdentifier.
}
\]

甚至 stable identifier 也只是某制度下的身份介面，不必是本體身份本身。

---

# 23. Namespace

定義 namespace：

\[
\boxed{
\mathcal N_s
}
\]

為名稱解析域。

同一 local name：

\[
T
\]

可以有：

\[
T@\mathcal N_1
\]

以及：

\[
T@\mathcal N_2.
\]

而：

\[
Ref(T@\mathcal N_1)
\neq
Ref(T@\mathcal N_2).
\]

因此：

\[
\boxed{
\text{Local Name}
+
\text{Namespace}
\rightarrow
\text{Qualified Name}.
}
\]

---

# 24. Namespace-Qualified Name

定義：

\[
\boxed{
NQN
=
(
NamespaceID,
LocalName
).
}
\]

因此：

\[
NQN_1=(N_1,T),
\]

\[
NQN_2=(N_2,T)
\]

即使 local name 完全相同：

\[
LocalName_1=LocalName_2=T,
\]

也可以：

\[
NQN_1\neq NQN_2.
\]

---

# 25. Namespace Collision

如果兩套系統 merge：

\[
N_1\cup N_2,
\]

而都有 local identifier：

\[
T,
\]

則產生：

# Namespace Collision

必須進行：

- qualify；
- rename；
- alias；
- merge；
- conflict resolution。

所以：

\[
\boxed{
\text{Same String}
\not\Rightarrow
\text{Same Global Identifier}.
}
\]

---

# 26. Namespace Migration

一個對象：

\[
x@N_1
\]

移動到：

\[
N_2,
\]

可以有多種語義：

### Preserve

保留 global identity，只換 local identifier。

### Clone

在 \(N_2\) 建立新 object。

### Alias

兩個 identifier 指向同一 global identity。

### Fork

從共同來源形成兩個後續身份。

所以 migration 必須保存：

\[
\boxed{
MigrationSemantics.
}
\]

---

# 27. Translation

名稱從語言：

\[
L_1
\]

進入：

\[
L_2
\]

時，可以：

- 翻譯語義；
- 音譯；
- transliteration；
- 保留原文；
- 重新命名。

因此：

\[
\boxed{
n_{L_1}
\rightarrow
n_{L_2}
}
\]

不只有一種 transformation。

---

# 28. Transliteration

若主要保持音韻／文字轉寫關係：

\[
n_{L_1}
\xrightarrow{\operatorname{Translit}}
n_{L_2},
\]

則：

\[
Form(n_{L_1})
\neq
Form(n_{L_2})
\]

但可以：

\[
Ref(n_{L_1})=Ref(n_{L_2}).
\]

所以：

\[
\boxed{
\text{Cross-Script Difference}
\not\Rightarrow
\text{Referential Difference}.
}
\]

---

# 29. Translation Drift

跨語言名稱可能逐漸出現：

\[
Ref(n_{L_2})
\neq
Ref(n_{L_1})
\]

或 semantic scope 改變。

這稱為：

# Referential / Semantic Drift

所以 translation mapping 必須版本化。

---

# 30. Naming Authority

不是所有命名都需要 authority。

私人暱稱可以完全不需要法律權威。

但某些名稱狀態需要：

\[
Auth(A,c,n).
\]

例如：

- legal registered name；
- scientific designation；
- domain name；
- official product identifier；
- standard symbol；
- institutional title。

所以：

\[
\boxed{
AuthorityRequirement
=
F(
NameType,
Context
).
}
\]

---

# 31. 命名權不等於身份創造權

即使：

\[
Auth(A)=1,
\]

A 有權更改 official name，也不表示 A 能改變所有 identity dimensions。

所以：

\[
\boxed{
NamingAuthority
\not\Rightarrow
TotalIdentityAuthority.
}
\]

例如改檔名不自動改變檔案內容身份。

---

# 32. Contested Naming

若：

\[
A
\]

主張：

\[
CanonicalName(x)=n_1,
\]

而：

\[
B
\]

主張：

\[
CanonicalName(x)=n_2,
\]

則產生：

\[
\boxed{
NamingContest(x).
}
\]

成熟系統應保存：

- claimant；
- authority；
- jurisdiction；
- time；
- evidence；
- current status。

而不是把一方名稱靜默覆蓋。

---

# 33. Naming as Power

命名可能影響：

- 可見度；
- 搜尋性；
- 法律分類；
- 社會地位；
- 平台處理方式；
- 後續分類。

所以：

\[
\boxed{
Name
}
\]

雖然不等於 Identity，

卻可能：

\[
Name
\rightarrow
InstitutionalConsequences.
\]

這使 naming governance 成為身份治理的一部分。

---

# 34. Self-Naming

某個主體：

\[
A
\]

可能宣告：

\[
Name_A(A)=n.
\]

這稱為：

\[
\boxed{
SelfNaming(A,n).
}
\]

它在不同 identity domains 的效力不同。

例如 personal display name 可以高度依賴 self-naming。

但 legal name 可能需要制度程序。

因此：

\[
\boxed{
SelfNamingValidity
=
F(
\alpha,
c,
Auth,
Procedure
).
}
\]

---

# 35. Exonym 與 Endonym

同一群體／地方／對象可能存在：

\[
n_{endo}
\]

與：

\[
n_{exo}.
\]

若：

\[
Ref(n_{endo})
=
Ref(n_{exo}),
\]

則它們共指，但 naming authority、歷史與社會意義不同。

所以：

\[
\boxed{
\text{Co-reference}
\not\Rightarrow
\text{Equal Naming Legitimacy}.
}
\]

---

# 36. Naming Chain 與 Reference Chain 必須分離

一條名稱形式可以持續：

\[
n_0\rightarrow n_1\rightarrow n_2
\]

但 referent 可能中途改變。

所以：

\[
\boxed{
NameFormContinuity
\not\Rightarrow
ReferenceContinuity.
}
\]

反之，referent 連續時名稱也可以改。

因此 Naming Chain 應同時保存：

\[
\boxed{
FormLineage
+
ReferenceLineage.
}
\]

---

# 37. Referential Continuity Certificate

本文定義：

\[
\boxed{
RCC
=
(
n,
x,
NC,
P,
E,
V
)
}
\]

為 Referential Continuity Certificate。

其目的不是證明：

\[
n=x,
\]

而是證明：

> 當前 name-use practice 合理地延續了對 \(x\) 的指涉。

---

# 38. Naming Event Certificate

定義：

\[
\boxed{
NEC
=
(
NE,
Authority,
Procedure,
Context,
Evidence,
Signature,
Version
).
}
\]

NEC 可以成為：

- IAC 的一部分；
- IGC 的 evidence；
- RCC 的起點。

因此 Paper 03–05 的 certificate 形成：

\[
\boxed{
IAC
\rightarrow
IGC
}
\]

以及：

\[
\boxed{
NEC
\rightarrow
RCC
\rightarrow
IGC.
}
\]

---

# 39. Reference Hijack

如果新的 name-use chain：

\[
NC'
\]

刻意讓：

\[
n
\]

指向不同對象：

\[
x',
\]

並冒充原：

\[
x,
\]

則形成：

# Reference Hijack

即：

\[
\boxed{
Form(n)\text{ preserved}
\quad
\text{but}
\quad
Ref(n)\text{ displaced}.
}
\]

這是身份攻擊的一種。

---

# 40. Name Squatting

若某個 actor 先取得：

\[
n
\]

的制度控制權，目的只是阻止另一預期 referent 使用該名稱，則名稱治理問題不再只是語義，而包含 allocation policy。

所以：

\[
\boxed{
\text{Name Availability}
\neq
\text{Name Legitimacy}.
}
\]

---

# 41. Dead Name / Historical Name

當：

\[
n_{old}
\]

不再是 current preferred／official name，但仍具有歷史用途時，成熟資料系統不應：

- 完全刪除；
- 永遠作為 current canonical name。

而應標記：

\[
NameStatus
=
Historical.
\]

因此：

\[
\boxed{
\text{Historical Preservation}
\neq
\text{Current Naming Authority}.
}
\]

---

# 42. Name Deletion 與歷史不可逆

刪除某個名稱資料：

\[
Delete(n)
\]

不會讓：

\[
NE(n)
\]

從歷史上沒有發生。

所以：

\[
\boxed{
\text{Remove Current Name}
\neq
\text{Erase Naming History}.
}
\]

這與 Paper 06–07 的 persistence／rupture 直接相連。

---

# 43. Name Identity

名稱本身也有 identity。

兩個名稱 token：

\[
n_1,n_2
\]

可以：

- 同字形；
- 同 pronunciation；
- 同 name type；
- 不同 naming practice；
- 不同 referent。

因此名稱身份也應使用 Paper 01 的多重關係：

\[
\boxed{
n_i
\equiv_{\alpha}
n_j.
}
\]

所以「名字是不是同一個名字？」本身又是一層 T 問題。

---

# 44. T 被稱為 T 的第一個完整形式

現在可以把：

> x 被稱為 T。

展開成：

\[
\boxed{
\exists u:
NameUse(u,T)
\land
Ref(u)=x.
}
\]

如果還要主張：

> T 是 x 的有效 canonical name。

則需要：

\[
\boxed{
Canonical(T,x,c,t,Auth)=1.
}
\]

如果主張：

> 所有叫 T 的都指向 x。

則是更強命題，通常不成立。

---

# 45. Same Name / Same T Matrix

考慮：

\[
T_1,T_2,T_3.
\]

表面名稱都是：

\[
T.
\]

但：

| Name | Namespace | Practice | Referent |
|---|---|---|---|
| \(T_1\) | \(N_A\) | \(P_1\) | \(x\) |
| \(T_2\) | \(N_A\) | \(P_2\) | \(y\) |
| \(T_3\) | \(N_B\) | \(P_3\) | \(x\) |

所以：

\[
Form(T_1)=Form(T_2)=Form(T_3),
\]

但：

\[
Ref(T_1)=Ref(T_3)\neq Ref(T_2).
\]

由此：

\[
\boxed{
\text{Name Surface}
}
\]

與：

\[
\boxed{
\text{Referential Topology}
}
\]

完全可以分離。

---

# 46. TTTTT 與 Naming Entropy

假設可見名稱序列：

\[
TTTTTTTTTTTTTT.
\]

則：

\[
H(NameForm)=0.
\]

但如果每個 T 屬於不同 naming chain：

\[
NC(T_i)\neq NC(T_j),
\]

則：

\[
\boxed{
H(NamingPractice\mid Form=T)>0.
}
\]

若 referent 也不同：

\[
H(Referent\mid Form=T)>0.
\]

因此得到：

\[
\boxed{
\text{Surface Name Entropy}
\neq
\text{Referential Entropy}.
}
\]

---

# 47. Naming Resolver

本文定義：

\[
\boxed{
\mathfrak N_R:
(
n,
c,
t,
E
)
\longrightarrow
(
NC,
Namespace,
CandidateReferents,
RefStatus
).
}
\]

它不直接假定：

\[
n\mapsto x.
\]

而先解析：

- 哪一個 name-use practice；
- 哪個 namespace；
- 哪個時間；
- 哪些 referent candidates；
- 有沒有 collision／ambiguity。

---

# 48. Naming Authority Resolver

另外定義：

\[
\boxed{
\mathfrak N_A:
(
A,
n,
x,
c,
t
)
\longrightarrow
AuthorityStatus.
}
\]

其中：

\[
AuthorityStatus
\in
\{
Authorized,
Unauthorized,
Contested,
NotRequired,
Unknown
\}.
\]

這避免把：

> 某人曾如此稱呼

錯寫成：

> 某人有權正式重新命名。

---

# 49. Name Migration Operator

定義：

\[
\boxed{
\mathfrak N_M:
(
n_1,
N_1,
N_2,
Mode
)
\longrightarrow
(
n_2,
RCC,
Status
).
}
\]

其中：

\[
Mode
\in
\{
Rename,
Alias,
Translate,
Transliterate,
Fork,
Clone,
Preserve
\}.
\]

因此跨平台／跨語言名稱遷移成為可明確審計的 identity event。

---

# 50. 核心命題一：名稱—身份分離

\[
\boxed{
Name(x)=Name(y)
\not\Rightarrow
x\equiv y.
}
\]

---

# 51. 核心命題二：異名共指

\[
\boxed{
n_1\neq n_2
\not\Rightarrow
Ref(n_1)\neq Ref(n_2).
}
\]

---

# 52. 核心命題三：命名事件不必創造本體身份

\[
\boxed{
NameEvent(A,x,n)
\not\Rightarrow
CreateOntologicalIdentity(x).
}
\]

但在某些制度身份中，合法命名／宣告事件可能參與 constitutive acquisition。

---

# 53. 核心命題四：名稱使用鏈可以是身份證據

若：

\[
NC(n)
\]

保持合法 referential continuity，則它可以支持：

\[
IGC_R.
\]

所以：

\[
\boxed{
\text{Name History}
}
\]

可能是 identity evidence，而不只是 linguistic metadata。

---

# 54. 核心命題五：namespace 是名稱身份的一部分

在可能發生名稱碰撞的系統中：

\[
\boxed{
NameIdentity
\supseteq
(
Namespace,
LocalName
).
}
\]

只保存 local form 不足以安全解析 identity。

---

# 55. 核心命題六：Canonical Name 是治理狀態，不是形上唯一名稱

\[
\boxed{
CanonicalName_c(x)
}
\]

依賴：

\[
c,t,Auth,Rule.
\]

因此 canonical status 可以改變，而 referent 不必改變。

---

# 56. Paper 05 的核心算子

將全文壓縮成：

\[
\boxed{
\mathfrak N:
(
A,
x,
n,
c,
t,
\Gamma_N,
Auth,
E
)
\longrightarrow
(
NEC,
NC,
RCC,
NameStatus
).
}
\]

其中：

- \(NEC\)：Naming Event Certificate；
- \(NC\)：Naming Chain；
- \(RCC\)：Referential Continuity Certificate；
- \(NameStatus\)：名稱當前狀態。

---

# 57. 與既有研究的邊界

proper-name 與 reference 文獻包含 descriptivist、causal-historical、direct-reference、rigidity 及其他 competing approaches。名稱條目也指出，同一 name form 可能需要透過特定 use、name-using practice 或 naming convention 才能處理其實際指涉，因此「名稱字形本身」並不足以完成完整的 reference analysis。

rigid designation 則提供另一個重要問題：一個 designator 是否在相關反事實情境中持續指定同一 object。本文不將 rigidity 直接等同 naming chain continuity，而把它們視為可以進一步對接的不同分析層。

工程上的 namespace／qualified identifier 概念則清楚展示：local name 需要配合 namespace 才能避免碰撞。本文借用這種結構作為 machine-readable identity interface，但不主張自然語言名稱完全等同 XML/RDF 名稱系統。

---

# 58. 結論

「T 怎麼被稱為 T？」真正不是：

\[
x=T.
\]

而是：

\[
\boxed{
A
\xrightarrow{\operatorname{Name}}
x
\mapsto
n
}
\]

之後還必須追蹤：

\[
\boxed{
NE
\rightarrow
NC
\rightarrow
RCC
\rightarrow
CurrentReference.
}
\]

所以：

\[
\boxed{
\text{T 被稱為 T}
}
\]

可能表示：

- 首次命名；
- 名稱繼承；
- alias；
- rename；
- translation；
- namespace qualification；
- canonical designation；
- 社群習慣；
- 制度登記；
- 誤稱；
- reference hijack。

這些完全不是同一種 naming relation。

本文最終得到：

\[
\boxed{
\text{Name}
\neq
\text{Identity}
}
\]

但同時：

\[
\boxed{
\text{Name History}
\subset
\text{Possible Identity Grounding}.
}
\]

所以名稱既不能被高估成身份本體，也不能被低估成毫無作用的標籤。

它真正的角色更接近：

\[
\boxed{
\text{Name}
=
\text{A socially and historically routed interface to identity}.
}
\]

下一篇 Paper 06〈T 為何還是 T？〉將把前五篇全部拉進時間軸：

\[
\boxed{
T_{t_0}
\stackrel{?}{\equiv}
T_{t_1}.
}
\]

真正的問題將變成：

> 名稱變了、狀態變了、材料變了、模型換了、歷史累積了，為什麼我們還說「它還是那個 T」？

這將正式進入 persistence、continuity、replacement、gradual change 與忒修斯型問題。
