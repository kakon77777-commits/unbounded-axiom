# 政治符號學 2.0——共享政治世界、關係耦合與動態契約
## Paper 04：權力越大為何責任越大
### 公眾人物、治理作用域與因果責任的形式化分析

**Political Semiotics 2.0 — Shared Political Worlds, Relational Coupling, and Dynamic Contract**  
**Paper 04: Why Greater Power Implies Greater Responsibility — A Formal Analysis of Public Figures, Governance Scope, and Causal Responsibility**

**作者：Neo.K × Aletheia**  
**機構：EveMissLab／一言諾科技有限公司**  
**版本：v0.1**  
**日期：2026-08-30**  
**性質：內部研究論文／系列政治責任基礎篇**

---

## 摘要

「權力越大，責任越大」是政治倫理中極常見的直覺，但若缺乏形式化，它很容易退化成一句模糊口號。政治人物是否應為某一結果負責，不能只看其職稱，也不能只看結果是否糟糕；必須分析其對結果的實際控制能力、作用半徑、資訊可得性、可行替代方案、決策參與程度、可逆性，以及其行動相對其他因素的因果貢獻。

本文提出「政治因果責任模型」（Political Causal Responsibility Model, PCRM）。對政治行動者 $A_j$ 、受影響主體集合 $\mathcal{S}$ 、政策或事件 $Y$，定義責任函數：

$$
\mathcal{R}_j(Y)
=
F
\left(
C_j,
I_j,
K_j,
A_j,
V_j,
D_j,
Q_j,
T_j
\right),
$$

其中：

- $C_j$：控制能力 Control；
- $I_j$：作用範圍 Impact Scope；
- $K_j$：資訊可得性 Knowledge Access；
- $A_j$：可行替代方案 Alternatives；
- $V_j$：可逆性與修復能力 Reversibility；
- $D_j$：決策參與度 Decision Share；
- $Q_j$：因果貢獻 Causal Contribution；
- $T_j$：時間持續與累積 Temporal Persistence。

本文主張，責任既不能被簡化為「誰在位誰負全責」，也不能被無限稀釋為「系統太複雜，所以沒人負責」。政治責任應是多因子、可分解、可比較的光譜量。

本文特別處理三個政治責任中的常見錯誤。第一，結果論錯誤：把壞結果直接等同於壞決策。第二，職位論錯誤：把最高職位自動等同於全部因果。第三，系統逃責錯誤：因為存在官僚、制度、歷史與外部衝擊，就宣稱任何個體都不應承擔責任。

本文進一步指出，民主治理具有「部分授權—全體作用」結構，因此政治人物一旦取得公權力，其責任對象並不只限於支持者，而是整個治理作用域中的受影響主體。這與本系列 Paper 02 的 standing 理論直接銜接：若權力能改變某一主體的選擇底空間，該主體取得 standing；相對地，施加該政治算子的行動者也取得相應的回答、說明與修復責任。

本文最後將責任問題接回政治符號學 2.0：責任不是抽象人格評分，而是「誰以什麼算子，在何種資訊與選項條件下，改變了誰的什麼選擇底空間」。下一篇將由此推進到人民與國家的雙生動力學：當責任不再被理解為單次決策，而是長期雙向耦合中的累積作用，政治關係就必須從靜態授權模型升級為動態系統。

**關鍵詞：** 政治責任、因果責任、權力、公眾人物、治理作用域、控制力、資訊優勢、可行替代方案、可逆性、政治符號學

---

# 第一部　問題：權力越大，為什麼責任越大？

## 1. 這句話不能只是一句道德口號

政治語言常說：

> 權力越大，責任越大。

這句話直覺上合理，但若不拆開，就會產生很多問題。

例如：

- 總統是否要為所有經濟衰退負責？
- 市長是否要為所有地方犯罪負責？
- 部長是否要為每一個基層行政錯誤負責？
- 一個政策失敗，究竟是首長、官僚、立法者、執行機關還是外部環境造成？
- 若政治人物已經提出最好可行方案，但仍因不可控因素失敗，責任是否與結果同樣大？

因此：

$$
\text{Bad Outcome}
\neq
\text{Maximum Responsibility}.
$$

政治責任必須回到因果結構。

---

## 2. 責任至少包含四種不同語義

政治討論中的「負責」常混合：

### 2.1 因果責任

誰實際造成了結果：

$$
R^{causal}.
$$

### 2.2 職務責任

誰依制度角色應對某領域負責：

$$
R^{role}.
$$

### 2.3 回答責任

誰必須向受影響者說明：

$$
R^{answer}.
$$

### 2.4 修復責任

誰有義務採取補救：

$$
R^{repair}.
$$

這四者不必完全重合。

例如一個部長可能不是某事故的直接因果來源，但因職務位置仍需回答與修復。

因此：

$$
\boxed{
\text{Responsibility}
\neq
\text{Single Quantity}.
}
$$

---

# 第二部　政治因果責任的八個核心變量

## 3. 控制能力

令行動者 $A_j$ 對政策變量 $X$ 的控制能力為：

$$
C_j(X)
\in[0,1].
$$

若：

$$
C_j(X)\approx0,
$$

則要求其對 $X$ 的全部結果負責並不合理。

若：

$$
C_j(X)\approx1,
$$

其責任通常提高。

因此：

$$
\frac{\partial \mathcal{R}_j}{\partial C_j}>0.
$$

但控制力不是唯一因素。

---

## 4. 作用範圍

政治人物的權力不只取決於能不能改變某個變量，也取決於改變多少人。

令其作用域為：

$$
\mathcal{J}_j.
$$

作用人口或受影響主體數量為：

$$
N_j
=
|\mathcal{J}_j|.
$$

一般而言：

$$
N_j\uparrow
\Rightarrow
\mathcal{R}_j^{answer}\uparrow.
$$

這不是說每個人都受到同等影響，而是說作用半徑越大，需要回答的 standing 主體越多。

---

## 5. 資訊可得性

政治責任不能完全脫離當時可知資訊。

令行動者在決策時間 $t$ 可合理取得的資訊集合為：

$$
\mathcal{K}_j(t).
$$

若風險在當時不可合理預見：

$$
H
\notin
\mathcal{K}_j(t),
$$

其責任與明知風險仍故意行動的情況不同。

因此：

$$
\text{Foreseeable Harm}
>
\text{Unforeseeable Harm}
$$

在責任權重上通常應成立。

---

## 6. 可行替代方案

責任還取決於：

> 他是否其實有其他路可以走？

令當時可達方案集合為：

$$
\Omega_j^{reachable}(t).
$$

如果：

$$
|\Omega_j^{reachable}(t)|=1,
$$

則行動自由極低。

如果：

$$
|\Omega_j^{reachable}(t)|\gg1
$$

且存在明顯更低傷害方案，責任可能增加。

因此：

$$
A_j^{alt}
=
Quality
\left(
\Omega_j^{reachable}
\right)
$$

應進入責任函數。

---

## 7. 可逆性與修復能力

一項決策若可快速撤回：

$$
V_j\approx1,
$$

和不可逆決策：

$$
V_j\approx0
$$

的責任結構不同。

特別是當政治人物在高不確定性下採取不可逆政策，其說明與審慎義務應提高。

因此：

$$
Irreversibility\uparrow
\Rightarrow
DutyOfCare\uparrow.
$$

---

## 8. 決策參與度

大型政治決策往往不是單一個體完成。

令：

$$
D_j\in[0,1]
$$

表示行動者對最終決策的參與權重。

例如：

- 提案者；
- 核准者；
- 執行者；
- 監督者；
- 否決者；
- 資源提供者；

都可能具有不同 $D_j$。

因此不能把所有責任全部壓到單一可見人物。

---

## 9. 因果貢獻

對結果 $Y$，令行動者的因果貢獻為：

$$
Q_j(Y).
$$

若系統結果由：

$$
Y
=
F
\left(
A_1,
A_2,
\ldots,
A_n,
E
\right),
$$

其中 $E$ 是外部環境，則每個行動者只佔部分因果。

因此：

$$
\sum_jQ_j(Y)
\leq1
$$

其餘部分可能屬於外部衝擊與結構條件。

---

## 10. 時間持續與累積

短暫失誤與長期持續性失敗不同。

令：

$$
T_j
=
\int_{t_0}^{t_1}
\omega(t)\,dt
$$

表示其控制、知情與不修正狀態的持續。

若政治人物在發現問題後仍長期維持：

$$
\Pi^{harm}
$$

則：

$$
\mathcal{R}_j
\uparrow
$$

因為責任包含「未修正」本身。

---

# 第三部　統一責任函數

## 11. 政治因果責任模型

本文定義：

$$
\mathcal{R}_j(Y)
=
F
\left(
C_j,
I_j,
K_j,
A_j,
V_j,
D_j,
Q_j,
T_j
\right).
$$

其中：

- $C_j$：控制能力；
- $I_j$：作用規模；
- $K_j$：知情程度；
- $A_j$：替代方案品質；
- $V_j$：可逆性；
- $D_j$：決策份額；
- $Q_j$：因果貢獻；
- $T_j$：持續時間。

可使用一個簡化乘積模型：

$$
\mathcal{R}_j
=
Q_j
\cdot
D_j
\cdot
\left(
\alpha C_j
+
\beta K_j
+
\gamma A_j
+
\delta I_j
+
\epsilon(1-V_j)
+
\zeta T_j
\right).
$$

本文不主張此函數是唯一正確形式，而是用來展示：

> 責任不是「有／無」，而是由多個條件共同構成的光譜。

---

# 第四部　三種常見責任錯誤

## 12. 結果論錯誤

結果論錯誤是：

$$
Y_{bad}
\Rightarrow
Decision_{bad}.
$$

這不成立。

因為：

$$
\text{Good Decision}
+
\text{Bad Luck}
\rightarrow
\text{Bad Outcome}
$$

可能成立。

同樣：

$$
\text{Bad Decision}
+
\text{Good Luck}
\rightarrow
\text{Good Outcome}
$$

也可能成立。

所以政治責任必須分析當時可知條件與可行方案。

---

## 13. 職位論錯誤

職位論錯誤是：

$$
\text{Highest Office}
\Rightarrow
\text{Total Causal Responsibility}.
$$

最高領導人通常具有較大：

$$
C_j,
I_j,
K_j
$$

所以責任可能較高。

但不代表：

$$
Q_j=1.
$$

在複雜政治系統中，責任需要分層。

---

## 14. 系統逃責錯誤

另一極端是：

> 系統太複雜，所以沒有人真正負責。

這同樣錯誤。

即使：

$$
Y
=
F(A_1,\ldots,A_n,E),
$$

仍可以估計各節點的：

$$
Q_j,
D_j,
C_j.
$$

複雜性不能自動取消責任，只要求責任分配更精細。

---

# 第五部　公共權力與加強責任

## 15. 公權力不是普通私人選擇

私人個體通常只能改變有限範圍。

但公職可能具有：

- 法律強制；
- 預算控制；
- 任命權；
- 警察與軍事權；
- 公共資訊權；
- 制度設計權；
- 規則制定權。

因此：

$$
C_j^{public}
\gg
C_i^{ordinary}
$$

在許多領域成立。

這就是：

$$
\boxed{
\text{Greater Power}
\Rightarrow
\text{Greater Responsibility}
}
$$

的第一個結構基礎。

---

## 16. 作用半徑與受影響者 Standing 對偶

Paper 02 已建立：

$$
\Pi_{ji}
\Rightarrow
\Sigma_{ij}^{standing}.
$$

也就是政治算子作用於主體時，會生成主體對權力的 standing。

反過來，對施加權力者而言：

$$
\Sigma_{ij}^{standing}
\Rightarrow
\mathcal{R}_j^{answer}.
$$

因此：

$$
\boxed{
\text{Standing of the affected}
\leftrightarrow
\text{Answerability of the powerful}.
}
$$

二者是同一政治關係的兩面。

---

# 第六部　部分授權與全體責任

## 17. 選你的人不是你唯一的責任對象

政治人物可能只得到部分選民支持：

$$
A_{support}
\subset P.
$$

但其治理作用域：

$$
J(O)
$$

往往包含：

$$
P_{jurisdiction}.
$$

因此：

$$
Responsibility(O)
\neq
Responsibility(A_{support}).
$$

更合理的是：

$$
Responsibility(O)
=
Responsibility(P_{affected}).
$$

---

## 18. 反對者不是治理外部人

一個沒有投票給執政者的人：

$$
S_i\notin A_{support}
$$

仍然可能：

$$
S_i\in J(O).
$$

他仍受：

- 稅法；
- 刑法；
- 預算；
- 外交；
- 國防；
- 行政；
- 公共服務；

作用。

因此：

$$
\boxed{
\text{Political Opposition}
\neq
\text{Exemption from Government Responsibility}.
}
$$

---

# 第七部　責任與資訊優勢

## 19. 權力常伴隨資訊優勢

政治人物與高階官僚常能取得一般公民無法取得的：

- 國安資訊；
- 專業簡報；
- 部會資料；
- 財政預測；
- 法律意見；
- 風險評估。

因此：

$$
K_j^{official}
>
K_i^{ordinary}
$$

在特定領域可能成立。

資訊優勢會提高：

$$
DutyOfCare_j.
$$

因為：

> 知道得更多，卻仍忽略已知風險，責任通常更高。

---

## 20. 但資訊優勢不能變成免責符號

政治人物也常說：

> 你不知道我們掌握的全部資訊。

這有時是真的。

但不能因此推出：

$$
\text{Secret Information}
\Rightarrow
\text{No Public Accountability}.
$$

更合理的是：

$$
\text{Confidentiality}
+
\text{Independent Oversight}
+
\text{Ex Post Review}.
$$

也就是必要保密可以存在，但不能取消責任結構。

---

# 第八部　責任與可逆性

## 21. 高不可逆政策需要更高審慎

若政策：

$$
V\approx0
$$

且影響：

- 戰爭；
- 國土；
- 憲政；
- 大規模債務；
- 核設施；
- 人口結構；
- 長期環境；

則應提高：

$$
PreDecisionBurden.
$$

因為決策後：

$$
RestoreCost\gg0.
$$

---

## 22. 及時修正會改變責任

若政策發現問題後：

$$
\Pi^{repair}
$$

快速啟動，責任可以被部分降低。

若：

$$
KnownFailure
+
NoCorrection
$$

長期存在，則：

$$
\mathcal{R}_j
\uparrow.
$$

因此責任是動態的，不是只在決策瞬間固定。

---

# 第九部　責任與多人治理

## 23. 政治責任圖

令治理系統為：

$$
G=(V,E).
$$

節點包括：

- 民選首長；
- 立法者；
- 部長；
- 官僚；
- 地方政府；
- 法院；
- 顧問；
- 承包商。

每個節點具有：

$$
\mathcal{R}_j.
$$

因此：

$$
\mathbf{R}
=
(\mathcal{R}_1,\ldots,\mathcal{R}_n).
$$

政治責任應是一張分布圖，而不是只找一個「替罪羊」。

---

## 24. 元責任

某些角色即使沒有直接做出錯誤決策，也可能具有：

$$
R^{meta}.
$$

例如：

- 明知制度會失效卻不修；
- 故意關閉監督；
- 阻止資訊上報；
- 建立獎勵錯誤；
- 壓縮異議管道。

這些行為改變其他人能否做出正確決策。

因此：

$$
\boxed{
\text{Responsibility for the decision system}
}
$$

也是政治責任。

---

# 第十部　政治符號學 2.0 接口

## 25. 責任必須翻譯成算子作用

政治符號學 2.0 中：

$$
\Pi_{ji}:
\mathfrak{B}_i
\rightarrow
\mathfrak{B}_i'.
$$

因此責任問題可改寫為：

> 誰選擇、授權、維持或阻止了這個算子？

定義：

$$
\mathcal{R}_j(\Pi)
=
F
\left(
Control_j(\Pi),
Knowledge_j(\Pi),
Alternative_j(\Pi),
Persistence_j(\Pi)
\right).
$$

這比單問：

> 誰是領導人？

解析度更高。

---

## 26. 高階政治符號也會遮蔽責任

例如：

- 「國家決定」；
- 「市場要求」；
- 「體制如此」；
- 「人民選擇」；
- 「歷史必然」。

這些句子可能把具體行動者藏起來。

因此政治符號學應追問：

$$
\text{Who instantiated the operator?}
$$

即：

> 到底是誰執行了哪個政治算子？

---

# 第十一部　十項核心命題

## 27. PCRM-A1：責任非結果同一命題

$$
\boxed{
BadOutcome
\neq
MaximumResponsibility.
}
$$

---

## 28. PCRM-A2：責任控制依賴命題

$$
\frac{\partial \mathcal{R}}{\partial C}>0.
$$

控制力增加通常提高責任。

---

## 29. PCRM-A3：責任作用域命題

$$
ImpactScope\uparrow
\Rightarrow
Answerability\uparrow.
$$

---

## 30. PCRM-A4：資訊優勢命題

$$
KnowledgeAccess\uparrow
\Rightarrow
DutyOfCare\uparrow.
$$

---

## 31. PCRM-A5：替代方案命題

若存在明顯更佳可達方案：

$$
AltBetter=1,
$$

則未選擇它可能提高責任。

---

## 32. PCRM-A6：不可逆性命題

$$
Irreversibility\uparrow
\Rightarrow
PreDecisionBurden\uparrow.
$$

---

## 33. PCRM-A7：複雜性不免責命題

$$
SystemComplexity\uparrow
\not\Rightarrow
Responsibility\rightarrow0.
$$

---

## 34. PCRM-A8：職位非總因果命題

$$
HighestOffice
\not\Rightarrow
Q=1.
$$

---

## 35. PCRM-A9：持續不修正命題

$$
KnownFailure
+
Persistence
\Rightarrow
Responsibility\uparrow.
$$

---

## 36. PCRM-A10：Standing—Answerability 對偶命題

$$
\boxed{
AffectedStanding
\leftrightarrow
PowerAnswerability.
}
$$

---

# 第十二部　反例與限制

## 37. 責任不能完全量化

很多責任變量：

- 知情程度；
- 控制能力；
- 替代方案；
- 因果貢獻；

本身都需要估計。

因此本文模型不是宣稱：

$$
\mathcal{R}=0.7312
$$

就是客觀真值。

其主要用途是強迫分析者把責任來源拆開。

---

## 38. 高責任不等於刑事責任

政治責任可能包括：

- 政治辭職；
- 選舉問責；
- 行政責任；
- 道德批評；
- 公開說明；
- 民事責任；
- 刑事責任。

這些不能混為一談。

因此：

$$
PoliticalResponsibility
\neq
CriminalLiability.
$$

---

## 39. 好意不能完全免責

即使：

$$
Intentions>0,
$$

若：

$$
Negligence\gg0,
$$

責任仍可能成立。

因此：

$$
GoodIntent
\neq
NoResponsibility.
$$

---

# 第十三部　通往 Paper 05：從單次責任到長期耦合

## 40. 單次責任模型仍然不夠

Paper 04 處理的是：

$$
Action
\rightarrow
Outcome
\rightarrow
Responsibility.
$$

但國家與人民不是只在單次決策中相遇。

政治權力每天都在作用：

$$
\Pi_1,
\Pi_2,
\ldots,
\Pi_n.
$$

人民也每天以：

- 納稅；
- 勞動；
- 投票；
- 遵法；
- 抗議；
- 生育；
- 移動；
- 投資；

反作用於國家。

因此：

$$
State
\leftrightarrow
People
$$

不是一次性契約，而是持續動力學。

---

## 41. 從責任函數到雙生動力

令人民狀態：

$$
P(t)
$$

國家狀態：

$$
S(t).
$$

則下一篇將建立：

$$
\frac{dP}{dt}
=
F(P,S,E),
$$

以及：

$$
\frac{dS}{dt}
=
G(S,P,I).
$$

這會把政治責任從單次事件推進到長期耦合中的累積責任。

---

# 結論

「權力越大，責任越大」之所以成立，不是因為高位者在道德上天然更應被責怪，而是因為高權力位置通常具有更高的：

$$
Control,
Impact,
Knowledge,
Alternatives,
DecisionShare.
$$

因此：

$$
\boxed{
GreaterPoliticalPower
\Rightarrow
GreaterPotentialResponsibility.
}
$$

但「更大」不是自動等於「全部」。

政治責任必須拆成：

$$
\boxed{
Responsibility
=
Control
+
Impact
+
Knowledge
+
Alternatives
+
Reversibility
+
DecisionShare
+
CausalContribution
+
Time.
}
$$

政治分析因此應避免兩個極端：

$$
\text{Leader Did Everything}
$$

和：

$$
\text{System Did Everything}.
$$

真正的任務是建立責任拓撲：誰具有多大控制力、知道多少、有哪些替代方案、影響多少人、做了什麼、維持了多久，又是否有能力修正。

本文最終提出：

$$
\boxed{
\text{Power is not merely the capacity to act;}
\quad
\text{it is also the capacity to become answerable.}
}
$$

下一篇將把這種單次政治責任提升到更底層的人民—國家雙向耦合：若人民持續構成國家，而國家又持續塑造人民，那麼政治合法性與政治責任就不能只被理解成選舉日的一次授權，而必須進入長期動力系統。

---

# 內部理論接口

1. EveMissLab，《政治知識的多源性——為什麼政治學專業不等於政治全知》，本系列 Paper 01，2026。
2. EveMissLab，《公民批評的政治正當性——從專業資格到受影響者 Standing》，本系列 Paper 02，2026。
3. EveMissLab，《政治評價不是喜歡與討厭——公共判斷的高維向量、張量結構與投影模型》，本系列 Paper 03，2026。
4. EveMissLab，《政治符號學 2.0：主體、選擇底空間與不可代決政治的統一公理框架》，2026。
5. EveMissLab，《政治算子論》，政治符號學 2.0 基礎論文 III，2026。
6. EveMissLab，《權力的四維結構：控制、合法性、網絡與穩定性的動態平衡論》，2025。
7. EveMissLab，《統治者—人民同向性原理》，2026。

# 經典理論接口

- Max Weber, writings on responsibility, authority, and political vocation.
- H. L. A. Hart, writings on responsibility and legal attribution.
- Joel Feinberg, works on responsibility and harm.
- John Stuart Mill, works on liberty, public power, and harm.
- Philip Pettit, works on domination and institutional control.
- Judea Pearl, works on causal modeling and intervention.

---

**Canonical source note:** 本文件以 UTF-8 Markdown 為正式原始稿。數學原始碼只使用 ` $...$ ` 與 `$$...$$` 作為 canonical delimiters；不以渲染後公式替代原始碼。
