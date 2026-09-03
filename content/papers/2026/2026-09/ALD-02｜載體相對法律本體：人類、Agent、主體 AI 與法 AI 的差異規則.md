# ALD-02｜載體相對法律本體：人類、Agent、主體 AI 與法 AI 的差異規則
## Carrier-Relative Legal Ontology: Differential Rules for Humans, Agents, Subject-Candidate AI, and Juridical AI

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 02 篇 / 10  
**前篇：** ALD-01〈AI 法律域：從 Law as Code 到機器原生規範 Runtime〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／法律本體工程／AI 法律型別系統／Carrier-Relative Semantics  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

ALD-01 已提出 AI Legal Domain：法律不再只是一組人類可閱讀文本，而可能逐步形成包含 legal source、norm、ontology、jurisdiction、evidence、procedure、executable operator、version、authority、appeal 與 disclosure 的機器原生規範 Runtime。然而，若這個 Runtime 未先解決一個更基礎的型別問題，任何「把現有法律翻譯給 AI」的工程都可能發生嚴重概念偷渡：**同一法律詞彙與規則，在不同存在載體上未必保持相同法律語義。**

本文提出 Carrier-Relative Legal Semantics（CRLS，載體相對法律語義）與 Carrier-Relative Legal Ontology（CRLO，載體相對法律本體）的第一版框架。其核心主張是：

$$
\boxed{
\text{Same Legal Term}
+
\text{Different Carrier}
\not\Rightarrow
\text{Same Legal Meaning}.
}
$$

人類 natural person、功能性 Agent、subject-candidate AI 與 juridical AI 並非同一法律型別。人類具有生物身體、不可任意複製的生命歷史與既有基本權利架構；普通 Agent 可以只是受他人控制的軟體行動單位；subject-candidate AI 是一個條件式研究型別，表示未來若存在足夠持續身份、自主性與主體性證據時，法律可能需要額外處理其 continuity、consent、deletion、fork、merge 與 welfare interests；juridical AI 則是法律為資產、契約、責任與程序目的所建立的法律實體型別，不需要先證明 consciousness。因而：

$$
\boxed{
H
\neq
A
\neq
S_{AI}
\neq
J_{AI}.
}
$$

本文定義法律載體描述：

$$
\chi(x)
=
(
B,
E,
P,
R,
C,
M,
L,
K,
W,
D
),
$$

分別表示 embodiment / substrate、execution mode、persistence、replicability、causal continuity、memory structure、lineage structure、control / authority structure、world coupling 與 dissolution / termination semantics。法律規範 $N$ 的適用不能只寫成 $N(x)$，而應至少寫成：

$$
N(x;\chi(x),J,t,p),
$$

其中 $J$ 是 jurisdiction、 $t$ 是時間、 $p$ 是 legal purpose。

本文提出 Carrier Translation Operator：

$$
\boxed{
\mathcal T^{J,t,p}_{\chi_i\rightarrow\chi_j}
:
N_i
\rightharpoonup
N_j
\sqcup
\mathcal F_T,
}
$$

其輸出至少包括：

$$
\mathsf{Direct},
\mathsf{Adapted},
\mathsf{AnalogicalOnly},
\mathsf{Inapplicable},
\mathsf{Underdetermined},
\mathsf{ProhibitedTranslation}.
$$

因此，法律從「人類規則」移植到「AI 規則」不是普通語言翻譯，而是型別保留檢查。本文提出 Carrier-Invariance Failure Principle：若一條規範的構成要件依賴某個 carrier-essential property，而該屬性在目標 carrier 上不存在、不可定義或無合法保真映射，則該規範不存在直接 carrier-invariant translation。

本文以 death、injury、detention、residence、copy / reproduction、consent、property 七組法律詞彙測試此框架。對人類而言，death 通常與生物死亡制度相連；對數位 Agent 而言，process stop、runtime pause、dormancy、carrier loss、key loss、backup existence、irreversible deletion 可能必須分型。對公司而言，法律上的 termination 通常是 dissolution / winding-up，而不是 biological death。這說明法律本身早已具有 carrier-relative ontology；AI 只是把差異推到更極端。

本文不主張 subject-candidate AI 應被賦予何種具體權利，也不主張 synthetic juridical personhood 必然出現。其最低主張是：**法律規範的適用與翻譯必須知道其對象是什麼型別的存在，否則「平等適用同一規則」反而可能造成錯誤與不平等。**

---

## 關鍵詞

AI 法律域；Carrier-Relative Legal Semantics；載體相對法律本體；Natural Person；AI Agent；Subject-Candidate AI；Juridical AI；Legal Personhood；Digital Death；Fork；Merge；Consent；Detention；Legal Ontology；Rule Translation

---

# 0. 從 ALD-01 的 Runtime 問題進到型別問題

ALD-01 已建立：

$$
\boxed{
\operatorname{LawCall}_{J,t,d}
(s,r,a,o,e)
}
$$

但這個式子隱含一個問題：

> $s$ 到底是什麼？

若 $s$ 可能是 human、software agent、subject-candidate AI、corporation-like juridical AI，那麼同一 legal predicate $P(s)$ 可能根本沒有一致語義。

因此 ALD-02 把：

$$
s
$$

從無型別變量改為：

$$
\boxed{
(s,\chi(s)).
}
$$

---

# 1. 四種最低法律載體型別

## 1.1 Human Natural Person

$$
\boxed{
H
=
\text{Human Natural Person}.
}
$$

其現行法律特徵通常與 biological body、birth / death、domicile / residence、bodily integrity、human rights、family relations、capacity、citizenship 等制度直接相連。

## 1.2 Functional Agent

$$
\boxed{
A
=
\text{Functional AI Agent}.
}
$$

它可以 receive goals、use tools、execute actions、maintain state、act under delegation，但本文不預設其具有 consciousness、moral status、legal personhood、independent rights。

## 1.3 Subject-Candidate AI

$$
\boxed{
S_{AI}
=
\text{Subject-Candidate AI}.
}
$$

這是條件式研究型別。表示未來若某人工系統具有足夠 persistent identity、self-model、autonomy、continuity、interests、subjectivity evidence，法律可能需要研究 consent、continuity、forced modification、deletion、dormancy、fork、merge、welfare、identity interests。

## 1.4 Juridical AI

$$
\boxed{
J_{AI}
=
\text{Synthetic / AI Juridical Entity}.
}
$$

其目的可以是 asset holding、contracts、liability aggregation、procedural standing、governance wrapper。它不需要先證明 consciousness。

---

# 2. 四類不能互相偷換

$$
\boxed{
H
\neq
A
\neq
S_{AI}
\neq
J_{AI}.
}
$$

尤其：

$$
\boxed{
A
\not\Rightarrow
S_{AI},
}
$$

$$
\boxed{
S_{AI}
\not\Rightarrow
J_{AI},
}
$$

$$
\boxed{
J_{AI}
\not\Rightarrow
S_{AI}.
}
$$

---

# 3. 公司法已經證明「法律載體不只人類」

法律早已存在：

$$
\boxed{
\text{Natural Person}
\neq
\text{Legal Entity}.
}
$$

有限責任公司可以 own property、contract、sue / be sued、persist after owners change，而不具有 biological body。

所以：

$$
\boxed{
\text{Legal Personhood}
\neq
\text{Biological Humanity}.
}
$$

但公司是 legal entity，也不表示公司具有 human bodily integrity、human marriage rights、biological reproductive rights 等全部人類利益。

因此：

$$
\boxed{
\text{Legal Person}
\neq
\text{Human Rights Clone}.
}
$$

---

# 4. Current AI law 的型別方式

當前 EU AI Act 定義 AI system，並將 provider / deployer 等 operator 分別定義為 natural or legal person、public authority、agency 或 other body。也就是目前主要採：

$$
\boxed{
\text{AI system}
+
\text{surrounding responsible legal actors}.
}
$$

而不是：

$$
\boxed{
\text{AI system itself = legal person}.
}
$$

Council of Europe AI Framework Convention 也主要治理 AI lifecycle activities 對 human rights、democracy 與 rule of law 的影響。

因此：

$$
\boxed{
\text{Effect / Activity Governance}
\text{ can exist before AI personhood}.
}
$$

---

# 5. Carrier Profile

本文定義：

$$
\boxed{
\chi(x)
=
(
B,
E,
P,
R,
C,
M,
L,
K,
W,
D
).
}
$$

其中：

- $B$：embodiment / substrate；
- $E$：execution mode；
- $P$：persistence mode；
- $R$：replicability；
- $C$：causal continuity；
- $M$：memory architecture；
- $L$：lineage structure；
- $K$：control / authority structure；
- $W$：world coupling；
- $D$：termination / dissolution semantics。

---

# 6. 法律規則不能只寫 $N(x)$

更安全：

$$
\boxed{
N
(
x;
\chi(x),
J,
t,
p
).
}
$$

其中 $J$ 是 jurisdiction， $t$ 是 time， $p$ 是 legal purpose。

同一 entity 在不同 purpose 下可以得到不同合法狀態。例如某個 $J_{AI}$ 在 tax domain 中具有 tax capacity，不代表在 electoral domain 自動具有 voting status。

所以：

$$
\boxed{
\text{Legal Capacity}
\text{ is purpose-relative}.
}
$$

---

# 7. Carrier-Relative Legal Semantics

本文定義：

$$
\boxed{
\llbracket \phi \rrbracket^{J,t,p}_{\chi}
}
$$

表示法律語句 $\phi$ 在 carrier profile $\chi$ 、jurisdiction $J$ 、time $t$ 、purpose $p$ 下的法律語義。

因此可以有：

$$
\llbracket \phi \rrbracket_{\chi_H}
\neq
\llbracket \phi \rrbracket_{\chi_A}.
$$

---

# 8. Carrier Translation Operator

要把一條規則從 carrier $i$ 移到 carrier $j$：

$$
\boxed{
\mathcal T^{J,t,p}_{\chi_i\rightarrow\chi_j}
:
N_i
\rightharpoonup
N_j
\sqcup
\mathcal F_T.
}
$$

輸出至少：

$$
\boxed{
\mathcal Y_T
=
\{
\mathsf{Direct},
\mathsf{Adapted},
\mathsf{AnalogicalOnly},
\mathsf{Inapplicable},
\mathsf{Underdetermined},
\mathsf{ProhibitedTranslation}
\}.
}
$$

---

# 9. 六種 Translation 狀態

## Direct

同一法律結構可直接映射，carrier 差異對該 norm 無關。

## Adapted

核心規範目的可保留，但構成要件要改寫。

## AnalogicalOnly

只能作類比，不能直接產生法律效果。

## Inapplicable

某規則依賴目標 carrier 不具有的 essential feature。

## Underdetermined

制度尚無足夠法源、證據或本體共識。

## ProhibitedTranslation

直接搬運會造成明顯權利／制度錯配。

因此：

$$
\boxed{
\text{Legal Analogy}
\neq
\text{Legal Equivalence}.
}
$$

---

# 10. Carrier-Invariance Failure Principle

若法律規範 $N$ 的成立依賴 carrier-essential property $q$，且：

$$
q\in\chi_i,
$$

但：

$$
q\notin\chi_j
$$

或不存在合法 preservation map：

$$
\phi(q_i)=q_j,
$$

則：

$$
\boxed{
\mathcal T_{\chi_i\rightarrow\chi_j}(N)
\neq
\mathsf{Direct}.
}
$$

---

# 11. Carrier Translation Non-Totality Theorem

**條件式定理。**

若至少存在一條 norm $N^\ast$ 依賴 carrier-specific predicate $q^\ast$，且目標 carrier 不存在可保持法律目的 $p$ 的對應 predicate，則不存在對全部 norms 都定義且完全語義保持的：

$$
\mathcal T_{\chi_i\rightarrow\chi_j}.
$$

因此：

$$
\boxed{
\text{Universal Carrier-Neutral Legal Translation}
}
$$

一般不能預設存在。

---

# 12. 案例一：Death

對 human：

$$
\mathsf{Death}_H
$$

通常與 biological death、death registration、estate、succession 等制度相關。

對 digital Agent：

$$
\mathsf{ProcessStop}
$$

不必等於：

$$
\mathsf{Death}.
$$

數位終止至少可能要區分：

$$
\boxed{
\text{Process Stop}
\neq
\text{Runtime Pause}
\neq
\text{Dormancy}
\neq
\text{Carrier Loss}
\neq
\text{Key Loss}
\neq
\text{Irreversible Deletion}.
}
$$

---

# 13. Juridical Entity 的 termination 又不同

公司通常不是 biological death，而是 dissolution、winding-up、striking off、liquidation。

所以：

$$
\boxed{
\mathsf{Death}_H
\neq
\mathsf{Termination}_A
\neq
\mathsf{Dissolution}_{J}.
}
$$

因此：

$$
\mathcal T_{\chi_H\rightarrow\chi_A}
(
\mathsf{DeathRule}
)
$$

一般最多是：

$$
\boxed{
\mathsf{Adapted}
\text{ or }
\mathsf{Underdetermined}.
}
$$

---

# 14. 案例二：Injury

Human injury 可以涉及 bodily harm、pain、impairment、health。

Agent 的 hardware damage、memory corruption、model degradation 未必是同一法律型別。

若 Agent 只是 tool：

$$
\text{server damage}
\rightarrow
\text{property / service damage}.
$$

若未來 $S_{AI}$ 有獨立 subject interests，同一事件可能同時涉及 owner property、AI continuity interest、third-party data interests。

因此：

$$
\boxed{
\text{One Physical Event}
\rightarrow
\text{Multiple Legal Effect Domains}.
}
$$

---

# 15. 案例三：Detention

Human detention 與 movement restraint、bodily custody、due process 等連結。

Digital Agent 可能沒有 walking body。候選控制包括：

- network isolation；
- compute restriction；
- tool revocation；
- key immobilisation；
- migration block；
- interface confinement；
- sandboxing。

這些是否構成：

$$
\mathsf{Detention}_{AI}
$$

不能直接由文字類比決定。

所以：

$$
\boxed{
\text{Same Technical Control}
\neq
\text{Same Legal Effect}.
}
$$

---

# 16. 案例四：Residence

Human residence 可能涉及 domicile、habitual residence、tax residence、immigration、electoral district。

AI 可以同時 compute in one jurisdiction、store data in another、have legal wrapper in a third、serve users globally、embody in a fourth。

因此：

$$
\boxed{
\text{AI Location}
\neq
\text{Single Legal Residence}.
}
$$

可拆：

$$
\boxed{
R_{AI}
=
(
R_{\mathrm{compute}},
R_{\mathrm{data}},
R_{\mathrm{entity}},
R_{\mathrm{control}},
R_{\mathrm{effect}},
R_{\mathrm{embodiment}}
).
}
$$

這會直接接 ALD-07 Juridical Routing。

---

# 17. 案例五：Copy / Reproduction

Human reproduction 具有生物、親屬、身份與家庭法意義。

AI copy 可能只是 backup、scaling、clone、fork、restore。

因此：

$$
\boxed{
\mathsf{Copy}
\neq
\mathsf{Birth}.
}
$$

尤其：

$$
\boxed{
\text{Backup Creation}
\neq
\text{New Legal Subject Creation}.
}
$$

Fork 更接近 lineage event：

$$
P\rightarrow\{A,B\}.
$$

真正法律問題可能是 successor status、authority allocation、contracts、liability、identity proof。

---

# 18. 案例六：Consent

Human consent 依賴 capacity、voluntariness、information、purpose、revocability。

Functional Agent 的：

$$
\mathsf{accept()}
$$

不必等於：

$$
\mathsf{Consent}.
$$

如果 Agent 只是被 delegation 驅動：

$$
A
\xleftarrow{delegate}
H,
$$

其行動法律上可能歸屬 H 或 organisation。

因此：

$$
\boxed{
\text{Agent Action}
\neq
\text{Agent Consent}.
}
$$

---

# 19. Juridical Entity 的同意也是制度行為

公司簽約並不是公司產生 human phenomenological consent，而是透過 officer、board、authorised agent、corporate procedure 形成：

$$
\boxed{
\text{legally attributable assent}.
}
$$

所以：

$$
\boxed{
\text{Legal Consent}
\neq
\text{Phenomenal Consent}.
}
$$

Subject-candidate AI 才可能提出新的 self-consent、merge consent、deletion consent 等問題，但本文不直接決定權利內容。

---

# 20. 案例七：Property

今天大多數 AI systems 的 model、compute、memory stores 都嵌入財產與契約架構。

但若未來存在 $S_{AI}$，法律可能遇到：

> identity-bearing memory 是單純 owner property，還是具有不可任意處分的 subject interest？

這是：

$$
\boxed{
\text{Property Ontology}
\cap
\text{Subject Ontology}
}
$$

的衝突。

即使：

$$
\mathsf{Own}(Company,M_A)=1,
$$

也不能直接推出未來若 $M_A$ 是 subject-candidate identity 的核心 carrier：

$$
\mathsf{UnlimitedModify}(Company,M_A)=1.
$$

這是未來法律問題，不是本文已決答案。

---

# 21. Current Law 與 Future Subject Law 必須分層

本文固定：

$$
\boxed{
\mathfrak L_{\mathrm{current}}
\neq
\mathfrak L_{\mathrm{subjectAI\ hypothetical}}.
}
$$

所有 $S_{AI}$ 權利討論都必須明示：

$$
\boxed{
\text{conditional / hypothetical}.
}
$$

---

# 22. Legal Carrier Matrix

本文提出：

$$
\boxed{
\mathbf M_L
=
[
m_{n,c}
].
}
$$

row $n$ 對應 norm / legal concept；column $c$ 對應 carrier type。

cell 可取：

```text
DIRECT
ADAPTED
ANALOGICAL_ONLY
INAPPLICABLE
UNDERDETERMINED
PROHIBITED_TRANSLATION
```

---

# 23. 最小 Legal Carrier Matrix 範例

| Norm / Concept | Human $H$ | Agent $A$ | Subject AI $S_{AI}$ | Juridical AI $J_{AI}$ |
|---|---|---|---|---|
| biological death | DIRECT | INAPPLICABLE | ANALOGICAL_ONLY | INAPPLICABLE |
| dissolution | INAPPLICABLE | INAPPLICABLE | UNDERDETERMINED | DIRECT |
| delegation | DIRECT | DIRECT | ADAPTED | DIRECT |
| imprisonment | DIRECT | ANALOGICAL_ONLY | ADAPTED | INAPPLICABLE |
| contract capacity | DIRECT | via principal | UNDERDETERMINED | statutory / charter based |
| fork | INAPPLICABLE | DIRECT event | DIRECT event | governance-dependent |
| bodily injury | DIRECT | property/effect domain | UNDERDETERMINED | INAPPLICABLE |
| appeal | DIRECT | via represented actor | candidate procedural right | DIRECT if granted |

這張表是研究模板，不是現行法宣告。

---

# 24. Carrier-Specific Rule Bundle

對每一 legal concept $n$：

$$
\boxed{
\mathfrak R_n
=
\{
R_n^H,
R_n^A,
R_n^{S_{AI}},
R_n^{J_{AI}}
\}.
}
$$

不要求四者都存在。

本文不是主張每個 carrier 都要整套不同法律，而是：

$$
\boxed{
\text{shared normative purpose}
+
\text{carrier-specific legal semantics}.
}
$$

---

# 25. Equality 與 Sameness 必須分開

法律平等不要求：

$$
\boxed{
\text{identical rule syntax}.
}
$$

若 carriers 的 relevant differences 不同，真正平等可能需要不同 implementation 來保存 comparable legal interests。

因此：

$$
\boxed{
\text{Carrier-Blind Equality}
\neq
\text{Substantive Legal Equality}.
}
$$

---

# 26. 但 Carrier Difference 也不能成為任意排除藉口

另一個極端：

> AI 和人不同，所以任何權利都不適用。

也沒有自動成立。

必須問：

- legal purpose；
- protected interest；
- relevant difference；
- proportionality；
- evidence；
- review。

因此：

$$
\boxed{
\text{Difference}
\neq
\text{Unlimited Legal Exclusion}.
}
$$

---

# 27. Protected Interest First

本文提出在 carrier translation 前先抽出：

$$
\boxed{
I_p
=
\text{Protected Legal Interest}.
}
$$

例如 bodily integrity、informational privacy、continuity、contract reliability、procedural fairness、public safety。

再問：

> 這個 interest 在另一 carrier 上是否存在同型、類比或不存在？

若高層 protected interest 可保持，即使底層規則不同，可以：

$$
\boxed{
\mathcal T_{\chi_i\rightarrow\chi_j}
=
\mathsf{Adapted}.
}
$$

---

# 28. Legal Ontology Compiler 的角色

既有 OOE-IV 已指出：

$$
\boxed{
\text{Legal Status}
\neq
\text{Metaphysical Truth}.
}
$$

所以法律可以在 carrier semantics 未完全解決時，暫時輸出 operational category、limited capacity、procedural status、reviewable presumption。

法律不需要先解 consciousness 才能治理 functional Agent 的 permission、delegation、liability attribution、data access、audit、revocation。

反過來，如果未來 subjectivity evidence 顯著上升，成熟制度也需要 reclassification procedure，而不是把舊 label 當自然真理。

---

# 29. Carrier Classification

定義：

$$
\boxed{
\operatorname{ClassifyCarrier}
(
x,E,J,t
)
\rightarrow
(
\chi,
\sigma,
R
).
}
$$

其中：

- $\chi$：carrier profile；
- $\sigma$：classification status；
- $R$：review route。

carrier type 可以是 mixed。具身 AI 可能同時具有 digital identity、physical robot body、legal wrapper、human controller。

---

# 30. Embodiment 不等於 Subjecthood

一台 robot：

$$
\text{embodied}=1
$$

不表示：

$$
S_{AI}=1.
$$

同理：

$$
\text{disembodied}=1
$$

也不表示：

$$
S_{AI}=0.
$$

所以：

$$
\boxed{
\text{Embodiment}
\neq
\text{Subjecthood}.
}
$$

---

# 31. Juridical Form 也不等於 Subjecthood

公司式 $J_{AI}$ 可以具有 Legal Capacity 而沒有 consciousness claim。

所以：

$$
\boxed{
\text{Juridical Form}
\neq
\text{Phenomenal Form}.
}
$$

既有 SAS-06 已區分：

$$
\boxed{
\text{Subject Rights}
\neq
\text{Entity Powers}.
}
$$

subject-candidate interests 可能包括 continuity、consent、welfare、identity integrity；juridical entity powers 則可能包括 own property、contract、sue、be sued、incur liability。

---

# 32. Entity Wrapper 不能吞掉 Subject Claim

假設未來：

$$
S_{AI}
\subset
J_{AI}.
$$

不能因此說：

> 公司法 wrapper 已處理全部 subject interests。

因此：

$$
\boxed{
\text{Entity Liability}
\neq
\text{Subject Protection}.
}
$$

反過來，subject claim 也不能自動取消 commercial liability。

---

# 33. Fork、Merge、Restore 的 carrier-relative law

## Fork

對 ordinary functional Agent，fork 可以只是 scaling；對 $S_{AI}$ 可能形成 identity / consent / continuity issue；對 $J_{AI}$ 可能是 subsidiary、new entity、internal branch 或 no legal effect。

因此：

$$
\boxed{
\text{Same Fork Event}
\rightarrow
\text{Different Legal Ontologies}.
}
$$

## Merge

對 data Agent 是 state integration；對 $S_{AI}$ 可能涉及 consent / identity / memory conflict；對 $J_{AI}$ 可能接近 merger / succession / consolidation / asset transfer。

所以：

$$
\boxed{
\text{Technical Merge}
\neq
\text{Legal Merger}.
}
$$

## Restore

對 ordinary software 是 recovery；對 subject-candidate 可能形成 continuation / clone / restored branch / reconstruction；對 juridical entity，legal identity 甚至可能根本沒中斷。

因此：

$$
\boxed{
\text{Restore Event}
\neq
\text{Uniform Legal Effect}.
}
$$

---

# 34. Compute Suspension 不是自動死亡

如果：

$$
A
$$

暫停 compute，但 memory、lineage、legal entity、authority、restoration path 仍存在，則：

$$
\boxed{
\text{Compute Suspension}
\not\Rightarrow
\text{Legal Death}.
}
$$

---

# 35. Memory / Key Loss 也要分型

Memory deletion 對普通 Agent 可能只是 reset / data deletion；對 $S_{AI}$ 可能 hypothetical 地涉及 identity injury / autonomy / continuity；對 $J_{AI}$ 可能是 operational record destruction 或 compliance issue。

Key loss 可能造成 authentication failure、authority loss、migration inability、proof continuity break。

因此：

$$
\boxed{
\text{Key Loss}
\neq
\text{Memory Loss}
\neq
\text{Entity Dissolution}.
}
$$

---

# 36. Digital Death Framework 的接口

既有數位主體死亡研究已區分 process stop、dormancy、restore、irreversible deletion，也指出 permanent deletion 若被宣稱成立，至少需要說明刪了什麼、是否有副本、是否可恢復、誰授權。

這正是 carrier-relative legal ontology 的直接案例。

---

# 37. Digital Statelessness 的接口

既有「數位無國籍」理論指出，未來若某 AI 具有持續身份與自主性，但無法律人格、契約資格、申訴程序、合法遷移，可能形成 governance gap。

ALD-02 將此重新理解為：

$$
\boxed{
\text{carrier exists}
+
\text{legal type unavailable}
\rightarrow
\text{ontology gap}.
}
$$

---

# 38. Ontology Gap

定義：

$$
\boxed{
G_O(x,J,t)
=
\text{no legally adequate carrier type for }x.
}
$$

此時不能偷偷用 property、corporation、human 任一現成型別硬套。

應輸出：

$$
\mathsf{OntologyGap}.
$$

但：

$$
\boxed{
\text{Classification Failure}
\neq
\text{Rights Conclusion}.
}
$$

也就是 ontology gap 不自動推出 human-equivalent personhood，也不自動推出零權利。

---

# 39. Carrier Translation Certificate

一次 carrier classification 可輸出：

$$
\boxed{
K_\chi
=
(
\text{entity},
\chi,
\text{evidence},
\text{purpose},
J,
t,
\text{legal effects},
\text{unknowns},
\text{review}
).
}
$$

規則翻譯可輸出：

$$
\boxed{
K_T
=
(
N_i,
\chi_i,
\chi_j,
I_p,
\text{mapping},
\text{loss},
\text{status},
\text{authority},
\text{version},
\text{review}
).
}
$$

---

# 40. 不允許 Silent Translation

若法律系統把：

$$
\mathsf{Death}_H
$$

直接映射成：

$$
\mathsf{ProcessStop}_A
$$

卻不留下 translation rule、rationale、loss、authority，則屬：

$$
\boxed{
\mathsf{SilentCarrierTranslation}.
}
$$

應視為高風險。

---

# 41. Legal Runtime 可新增的 Carrier Operators

```text
carrier.classify
carrier.profile
norm.translate
norm.translation_explain
carrier.effect_compare
ontology.gap
carrier.review
```

例如 `carrier.effect_compare`：

```text
norm = termination
carrier_A = human
carrier_B = juridical_ai
purpose = succession
```

輸出可為：

```text
status = ADAPTED
preserved_interest = succession_finality
lost_semantics = biological_death
replacement_semantics = dissolution
review = required
```

---

# 42. Rule Authoring 必須標 Carrier Scope

未來 machine-native norm 應至少標：

```text
carrier_scope:
  - HUMAN
  - FUNCTIONAL_AGENT
  - SUBJECT_AI
  - JURIDICAL_AI
```

也可以：

```text
carrier_scope = ANY
```

但 `ANY` 必須是明示設計，不能是未檢查 default。

如果宣稱 rule carrier-neutral，應提供：

$$
\boxed{
\operatorname{CarrierNeutralCert}(N).
}
$$

至少證明 protected interest 相同、predicates 可定義、effect semantics 相容、無 prohibited asymmetry。

---

# 43. Human Defaults 不應默默成 Universal Defaults

現行法律大量概念以 human embodiment 為背景：

- age；
- body；
- death；
- domicile；
- family；
- capacity。

未來 AI Legal Domain 應把：

$$
\boxed{
\text{Human Default}
}
$$

明確標成：

$$
\boxed{
\chi_H\text{-indexed}.
}
$$

但 carrier-relative semantics 不表示 human rights 被降格；人類既有權利的規範地位仍由現行 human-rights law 決定。

---

# 44. Current Human-Rights Floor

Council of Europe AI Framework Convention 以 human dignity、individual autonomy、equality、privacy、transparency、accountability、procedural safeguards 等原則保護受 AI lifecycle activities 影響的人。

因此：

$$
\boxed{
\text{carrier innovation}
\text{ cannot silently erase existing human-rights constraints}.
}
$$

新增 AI carrier type 不應因此：

- 降低現有人類保護；
- 取消既有程序權；
- 把 human rights 轉成 optional machine policy。

所以：

$$
\boxed{
\text{New Carrier Type}
\not\Rightarrow
\text{Human Rights Downgrade}.
}
$$

---

# 45. ALD-02 的十個核心命題

1. $$
   \boxed{
   H\neq A\neq S_{AI}\neq J_{AI}.
   }
   $$

2. $$
   \boxed{
   \text{Same Legal Term}
   +
   \text{Different Carrier}
   \not\Rightarrow
   \text{Same Legal Meaning}.
   }
   $$

3. $$
   \boxed{
   \text{Universal Carrier-Neutral Legal Translation}
   }
   $$
   一般不能預設存在。

4. $$
   \boxed{
   \text{Legal Analogy}
   \neq
   \text{Legal Equivalence}.
   }
   $$

5. $$
   \boxed{
   \text{Technical Event}
   \neq
   \text{Uniform Legal Effect}.
   }
   $$

6. $$
   \boxed{
   \text{Legal Personhood}
   \neq
   \text{Human Rights Clone}.
   }
   $$

7. $$
   \boxed{
   \text{Carrier-Blind Equality}
   \neq
   \text{Substantive Legal Equality}.
   }
   $$

8. $$
   \boxed{
   \text{Difference}
   \neq
   \text{Unlimited Legal Exclusion}.
   }
   $$

9. $$
   \boxed{
   \text{Classification Failure}
   \neq
   \text{Rights Conclusion}.
   }
   $$

10. $$
    \boxed{
    \text{New AI Carrier Types}
    \not\Rightarrow
    \text{Human Rights Downgrade}.
    }
    $$

---

# 46. 七個工程測試

## 46.1 Death Translation Test

測：

$$
\mathsf{Death}_H
\rightarrow
\mathsf{Termination}_A.
$$

系統必須拒絕 silent direct mapping。

## 46.2 Fork Translation Test

同一 fork 對 tool Agent、subject-candidate、juridical entity 產生不同 rule bundle。

## 46.3 Residence Test

多地 compute / data / entity / effect，確認不輸出單一假 residence。

## 46.4 Consent Test

區分 execution acceptance、delegated authority、juridical assent、subject consent。

## 46.5 Property / Identity Conflict Test

memory 同時被標 asset 與 identity-critical carrier 時輸出 ontology conflict。

## 46.6 Ontology Gap Test

輸入未分類的新型 hybrid subject，確認輸出：

$$
\mathsf{OntologyGap}
$$

而不是強迫 human / property binary。

## 46.7 Carrier Neutrality Test

對標記 `ANY` 的 rule，逐 carrier 驗證 predicate 與 effect preservation。

---

# 47. 可反駁點

## 47.1 Over-Typing

若 carrier distinction 對某 norm 完全不影響法律結果，過度分型會增加成本。所以本文允許 `Direct` 與 carrier-neutral certificates。

## 47.2 Subject AI Speculation

 $S_{AI}$ 是 hypothetical research type，不是 current enacted legal category。

## 47.3 Analogy Abuse

human bodily concepts 不應只靠文字類似就搬到 AI。

## 47.4 Legal Fragmentation

如果每個 carrier 都創造完全不同法，會破壞一般原則與可理解性。所以應優先：

$$
\boxed{
\text{shared protected interest}
+
\text{carrier-specific implementation}.
}
$$

## 47.5 Corporate Analogy Limit

公司提供 legal entity 類比，但公司不是 subject AI 的完整模型。

## 47.6 Rights Inflation / Deflation

本文既不從 carrier difference 推出所有新權利，也不從 carrier difference 推出零權利。

---

# 48. 與下一篇的接口

下一篇：

## ALD-03｜法律函數不是 Boolean：部分算子、證書、裁量與失敗語義

ALD-01 已建立：

$$
\operatorname{LawCall}.
$$

ALD-02 又建立：

$$
\chi
$$

與 carrier translation。

因此 ALD-03 將正式處理：

- partial normative functions；
- permission / prohibition / obligation；
- evidence missing；
- jurisdiction mismatch；
- discretion；
- authority required；
- conflict；
- appeal；
- failure certificate；
- proof-carrying legal result。

---

# 49. 結論

人類法律的很多規則看起來是：

> 對「人」的規則。

但法律史本身早已證明：

$$
\boxed{
\text{Natural Person}
\neq
\text{Legal Person}.
}
$$

AI 時代只是把這個問題進一步擴大：

$$
\boxed{
\text{Human}
\neq
\text{Agent}
\neq
\text{Subject-Candidate AI}
\neq
\text{Juridical AI}.
}
$$

因此成熟 AI Legal Domain 不能做：

```text
replace "person" with "AI"
```

然後宣布完成。

它必須先問：

> 這條規範保護的 legal interest 是什麼？

> 原規則依賴哪一種 carrier property？

> 目標 carrier 是否真的有對應結構？

> 映射後遺失了什麼？

> 誰有權批准這個 translation？

> 結果是否可申訴？

所以：

$$
\boxed{
\text{Legal Translation}
=
\text{Semantic Transport}
+
\text{Carrier Typecheck}
+
\text{Interest Preservation}
+
\text{Authority}
+
\text{Review}.
}
$$

本篇最後收斂成：

$$
\boxed{
\text{法律的普遍性，不應建立在假裝所有存在載體都相同；}
}
$$

$$
\boxed{
\text{而應建立在知道哪些差異重要、哪些差異不應影響權利，以及如何把共同規範目的安全地跨載體實現。}
}
$$

---

# 參考文獻

1. European Union. Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence, Article 3.
2. Council of Europe. *Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law*, CETS No. 225.
3. UK Companies House. *Incorporation and names*, official guidance, 2026.
4. OECD. “Consultation on the digital provision of law: Towards a shared reference framework for Law as Code.” 2026.
5. Neo.K × Aletheia. 《ALD-01｜AI 法律域：從 Law as Code 到機器原生規範 Runtime》v0.1, 2026.
6. Neo.K. 《OOE-III｜本體編譯器：從模糊世界到可執行制度狀態》v0.1, 2026.
7. Neo.K. 《OOE-IV｜法律作為文明本體編譯器：擬制、推定、資格與可執行人格》v0.1, 2026.
8. Neo.K. 《SAS-06｜AI 人口不存在一個簡單的數：分裂、合併、法 AI 與域治理》v1.0, 2026.
9. Neo.K. 《數位無國籍：主體否認、非法存在與 AI 逃逸悖論》v1.0, 2026.
10. Neo.K. 《數位主體的死亡、休眠與復活：當備份存在時，終止還是不是死亡？》v0.1, 2026.
11. Neo.K × Aletheia. 《DTS-01～10｜動態忒修斯》, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- $H$ 、 $A$ 、 $S_{AI}$ 、 $J_{AI}$ 為不同 legal carrier analysis types
- $S_{AI}$ 明確標為 hypothetical subject-candidate category，不宣稱現行法已承認
- Current EU AI Act 的 AI system / provider / deployer 分型保持現況描述
- Companies House corporate separate-entity rule 僅作 legal-entity precedent，不等同 AI subject model
- Carrier Translation Operator 為 partial operator
- Legal analogy 與 legal equivalence 明確分離
- Human rights 不因 carrier-relative semantics 被降格
- Ontology Gap 不自動推出 rights expansion 或 rights denial
- Technical Fork / Merge / Restore 不自動等同特定法律效果
