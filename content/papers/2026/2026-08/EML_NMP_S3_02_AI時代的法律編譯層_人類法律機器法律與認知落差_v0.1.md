# AI 時代的法律編譯層：人類法律、機器法律與認知落差

**英文題名：** The Legal Compilation Layer in the AI Era: Human Law, Machine Law, and the Cognitive Gap  
**系列：**《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》02 / 08  
**文件編號：** EML-NMP-S3-02-v0.1  
**作者：** Neo.K（許筌崴）with Aletheia（GPT-5.6 Sol）  
**機構：** 一言諾科技有限公司／EveMissLab  
**日期：** 2026-08-10  
**版本：** v0.1  
**文件性質：** 理論研究稿／Rules-as-Code／法律編譯層與 AI 治理篇  
**研究狀態：** 第一代形式化；本文不主張所有法律都可被完整演算法化，也不主張 machine-readable representation 應取代自然語言法律、司法解釋或民主正當性。

---

## 摘要

當法律越來越由數位系統執行時，真正控制公民權利、稅務、福利、資格、許可與義務的，不一定只是在國會公報、判決書或行政規則中可見的自然語言文字，而是法律被一次又一次翻譯後嵌入資訊系統的 operational rules。這產生一個新型治理問題：法律上的「權威文本」與機器實際執行的「操作法律」可能逐漸分離。

本文提出 **法律編譯層（Legal Compilation Layer, LCL）**，將 AI 時代的法律表示拆為五層：

$$
\boxed{
L
=
(
L_H,
L_P,
L_F,
L_S,
L_M
)
}
$$

其中：

- $L_H$：Human Legal Text，人類法律權威文本；
- $L_P$：Plain-Language Legal Projection，白話法律投影；
- $L_F$：Formal / Computable Legal Rule，形式化可計算規則；
- $L_S$：Simulation Layer，法律情境模擬與案例測試；
- $L_M$：Machine-Readable / Machine-Processable Representation，機器可讀與機器可處理表示。

本文拒絕將上述五層視為彼此等價。核心區分為：

$$
\boxed{
\text{Human-Readable}
\neq
\text{Machine-Readable}
\neq
\text{Machine-Decidable}
\neq
\text{Machine-Executable}
\neq
\text{Legally Authoritative}.
}
$$

一段法律可以被 XML、JSON、Akoma Ntoso 或 LegalRuleML 結構化，卻仍包含必須由法院、行政機關、專家或政治程序判斷的開放概念；一條形式規則可以被執行，卻不代表它就是法源上最高權威；一個 AI 可以提出法律 formalization，也不能因此取得修改法律語義的權力。

本文定義法律編譯鏈：

$$
\boxed{
L_H
\xrightarrow{C_{HP}}
L_P
\xrightarrow{C_{PF}}
L_F
\xrightarrow{C_{FM}}
L_M
}
$$

並由：

$$
L_F
\xrightarrow{\operatorname{Sim}}
L_S
$$

生成情境測試、反例與邊界案例。每一次跨層編譯均必須保存 semantic witness：

$$
\Gamma_{ab}^{law},
$$

記錄來源、轉譯規則、被壓縮語義、未決歧義、例外、版本與責任人。本文進一步提出 Legal Semantic Drift：

$$
\boxed{
\Delta_{ab}^{sem}
=
d_{sem}(L_a,L_b)
}
$$

用以描述法律從人類文本進入機器表示時的語義差距。

本文指出，Rules as Code 與 machine-readable law 已非純理論。OECD 將 Rules as Code 定義為政府同時建立官方、machine-consumable 規則的治理模式；紐西蘭 Better Rules 亦直接指出，傳統流程從立法文字到規則分析、再到軟體實作的多次翻譯會造成 interpretation drift。2025 年 OECD 稅務數位化調查更顯示，一部分政府已發布全部或部分 machine-readable tax law。OASIS 的 Akoma Ntoso 與 LegalRuleML 則分別提供結構化法律文件與法律規範／推理表示的開放標準。

但這些進展同時揭露真正危險：若 $L_M$ 成為福利、稅務、准入、制裁與行政流程的唯一實際執行版本，而一般人、法官甚至立法者無法看見它如何偏離 $L_H$，則會產生 **Operational Law Capture**：

$$
\boxed{
\text{de jure authority}
=
L_H,
\qquad
\text{de facto authority}
\approx
L_M.
}
$$

本文因此提出「法律權威不變量」：

$$
\boxed{
Authority(L_H)
>
Authority(L_F,L_M)
}
$$

除非憲法與立法程序明確改變法源結構。形式化與機器化層只能作為受授權的編譯產物，而不能因為運行速度更快、實際控制系統更多，就反向奪取規範權威。

本文最終提出 AI 時代成熟法律流程：

$$
\boxed{
\text{Legislation}
\rightarrow
\text{Compilation}
\rightarrow
\text{Simulation}
\rightarrow
\text{Verification}
\rightarrow
\text{Human / Public Deliberation}
\rightarrow
\text{Authorized Deployment}
}
$$

AI 的最佳角色不是成為「法律神諭」，而是法律編譯器、反例產生器、測試器、解釋器與差異偵測器。真正的法律仍必須保留人類可理解性、公開法源、可爭議性、程序正義與重新解釋能力。

**關鍵詞：** Rules as Code、machine-readable law、LegalRuleML、Akoma Ntoso、法律編譯、法律語義漂移、AI 法律、動態正義、可計算法律、法律認知落差、後 ASI 治理

---

# 0. 問題：真正執行的法律在哪裡？

在傳統法律想像中：

$$
\boxed{
\text{Law}
=
\text{legal text}.
}
$$

但現代行政國家中，真實流程常常是：

$$
\text{Statute}
\rightarrow
\text{Agency Interpretation}
\rightarrow
\text{Business Rule}
\rightarrow
\text{Software Requirement}
\rightarrow
\text{Code}
\rightarrow
\text{Decision}.
$$

因此公民實際遇到的是：

$$
\boxed{
Y_i
=
Program(
Data_i
).
}
$$

如果 Program 的邏輯與法律原文有偏差，

即使法律文字本身沒有改，

公民的「實際法律世界」也已經改變。

這是 AI 時代法律治理的第一個問題。

---

# 1. Prior Art：Rules as Code 已從概念走向政府實作

## 1.1 OECD：Rules as Code

OECD 將 Rules as Code 描述為：

> 政府建立官方的 machine-consumable rules，使規則能被電腦系統一致理解與執行。

這與：

$$
\text{private software implementation}
$$

不同。

核心變化在於：

$$
\boxed{
\text{government rulemaking}
\rightarrow
\text{human + machine consumable rulemaking}.
}
$$

## 1.2 紐西蘭 Better Rules

Better Rules Discovery Report 指出傳統流程的 translation gap：

1. 立法者建立 human-readable legislation；
2. rules analysts 重新解讀；
3. software developers 再次解讀；
4. business systems 最終嵌入規則。

因此可能：

$$
A
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3.
$$

這是一條法律語義漂移鏈。

Better Rules 的解法之一，是讓：

- policy；
- legislation；
- concept model；
- decision model；
- pseudocode；
- software logic；

更早共同發展。

## 1.3 OECD 2025 稅務數位化

OECD 2025 的 tax administration digitalisation report 顯示，machine-readable tax law 已被多個政府實際採用，以支援 automated calculation、real-time compliance 與 third-party integration。

因此：

$$
\boxed{
\text{machine-readable law}
}
$$

已是現實治理基礎設施議題。

## 1.4 OASIS：Akoma Ntoso 與 LegalRuleML

Akoma Ntoso 提供 parliamentary、legislative、judicial documents 的 machine-readable structured document model。

LegalRuleML 則進一步表達：

- legal norms；
- rules；
- policies；
- defeasibility；
- legal reasoning metadata。

因此：

$$
\boxed{
\text{legal document structure}
}
$$

與：

$$
\boxed{
\text{legal normative logic}
}
$$

本來就是不同層。

## 1.5 2026 PROLEG

2026 年 PROLEG 研究展示一個具體流程：

$$
\text{natural-language law}
\rightarrow
\text{if-then rules}
\rightarrow
\text{PROLEG}
\rightarrow
\text{executable legal reasoning}.
$$

其中 LLM 負責初始轉譯，

但 formalization 需要 legal expert validation。

這正好支持本文：

$$
\boxed{
\text{LLM compilation}
\neq
\text{legal authority}.
}
$$

---

# 2. 五層法律表示

本文定義：

$$
\boxed{
L
=
(
L_H,
L_P,
L_F,
L_S,
L_M
).
}
$$

---

# 3. $L_H$：Human Legal Text

$$
\boxed{
L_H
=
\text{authoritative human legal expression}.
}
$$

包括：

- constitution；
- statute；
- regulation；
- judgment；
- authorized administrative rule。

其特性：

- 自然語言；
- 具有法源地位；
- 包含開放概念；
- 可被解釋；
- 可引用歷史、目的與原則。

例如：

> reasonable care

不是普通 Boolean。

因此：

$$
\boxed{
L_H
\not\subseteq
\text{fully decidable code}.
}
$$

---

# 4. $L_P$：Plain-Language Legal Projection

許多人無法直接理解：

$$
L_H.
$$

所以需要：

$$
\boxed{
L_P
=
\operatorname{PlainProject}(L_H).
}
$$

它回答：

- 這條法律與我有什麼關係？
- 我要做什麼？
- 何時做？
- 不做會怎樣？
- 我有哪些權利？
- 如何申訴？

但：

$$
\boxed{
L_P
\neq
L_H.
}
$$

白話版本是 projection，

不能取代權威原文。

---

# 5. $L_F$：Formal / Computable Rule

形式層：

$$
\boxed{
L_F
=
(
Predicates,
Conditions,
Exceptions,
Priority,
TemporalRules,
Consequences
).
}
$$

例如：

$$
Eligible(x)
\Leftarrow
Age(x)\ge18
\land
Resident(x)
\land
\neg Excluded(x).
$$

但法律還可能有：

$$
Exception,
Override,
Discretion,
BurdenOfProof.
$$

所以：

$$
\boxed{
L_F
}
$$

不能只用最簡單 if-then tree。

---

# 6. $L_M$：Machine Representation

$$
L_M
$$

可以包括：

- XML；
- JSON；
- LegalRuleML；
- Akoma Ntoso；
- PROLEG；
- domain-specific legal IR。

需要區分：

$$
\boxed{
\text{machine-readable}
}
$$

與：

$$
\boxed{
\text{machine-executable}.
}
$$

結構化 XML 可以 machine-readable，

卻不一定能直接決定案件。

---

# 7. $L_S$：Simulation Layer

形式法律最有價值的地方之一，

不是自動判決，

而是可以：

$$
\boxed{
\operatorname{Simulate}(L_F).
}
$$

輸入：

$$
C_1,C_2,\ldots,C_n
$$

得到：

$$
Y_1,Y_2,\ldots,Y_n.
$$

因此立法前可以問：

- 哪些人被意外排除？
- 哪條規則產生極端負擔？
- 哪些例外衝突？
- 哪些參數造成歧視？
- 是否存在 dead zone？

這就是法律 simulation layer。

---

# 8. 五層不是權威平行體

不能寫成：

$$
Authority(L_H)
=
Authority(L_P)
=
Authority(L_F)
=
Authority(L_M).
$$

本文提出：

$$
\boxed{
Authority(L_H)
>
Authority(L_P,L_F,L_S,L_M)
}
$$

除非法律制度本身明確規定其他法源排序。

理由很簡單：

> 不能因為機器版本實際跑得最多，就變成最高法律。

---

# 9. Legal Compilation

定義：

$$
\boxed{
C_{ab}:
L_a
\rightarrow
L_b.
}
$$

例如：

$$
C_{HF}:
L_H
\rightarrow
L_F.
$$

編譯不是：

$$
\boxed{
\text{copy}.
}
$$

而是：

$$
\boxed{
\text{semantic transformation}.
}
$$

所以必須處理語義損失。

---

# 10. Semantic Witness

每一次：

$$
L_a
\rightarrow
L_b
$$

需要：

$$
\boxed{
\Gamma_{ab}^{law}
=
(
Source,
Mapping,
Resolved,
Unresolved,
Loss,
Exceptions,
Validator,
Version
).
}
$$

其中：

- Source：來源條文；
- Mapping：對應；
- Resolved：已解釋歧義；
- Unresolved：未決問題；
- Loss：轉譯損失；
- Exceptions：例外；
- Validator：法律審核者；
- Version：版本。

---

# 11. Legal Semantic Drift

定義：

$$
\boxed{
\Delta_{ab}^{sem}
=
d_{sem}(
L_a,L_b
).
}
$$

如果：

$$
\Delta_{HF}^{sem}
\gg0,
$$

代表形式規則與法律文本可能偏離。

但：

$$
d_{sem}
$$

不一定能被一個數字完整表示。

實務上可以使用：

$$
\boxed{
\mathbf\Delta_{ab}
=
(
\Delta^{scope},
\Delta^{condition},
\Delta^{exception},
\Delta^{burden},
\Delta^{right},
\Delta^{temporal},
\Delta^{authority}
).
}
$$

---

# 12. 最危險的是 Exception Loss

自然語言法律常有：

- 除外；
- 但書；
- reasonable；
- unless；
- subject to；
- proportionality；
- necessity。

如果 formalization 只抓主規則：

$$
R
$$

卻漏掉：

$$
E_1,E_2,\ldots,
$$

會產生：

$$
\boxed{
\text{Exception Loss}.
}
$$

這可能比普通 bug 更危險，

因為程式仍然「正確執行」。

---

# 13. 正確執行錯誤法律模型

這是 AI 法律最重要的失敗模式：

$$
\boxed{
ProgramCorrect=1
\land
LegalModelCorrect=0.
}
$$

所以：

$$
\boxed{
\text{software verification}
\neq
\text{legal semantic verification}.
}
$$

兩種 QA 必須分開。

---

# 14. Machine-Readable 不等於 Machine-Decidable

定義：

$$
MR(L)=1
$$

表示 machine-readable。

$$
MD(L)=1
$$

表示 machine-decidable。

一般：

$$
\boxed{
MR(L)=1
\not\Rightarrow
MD(L)=1.
}
$$

例如：

> 是否合理？

可以被 machine-readable 標記，

但不表示存在唯一演算法立即決定。

---

# 15. Machine-Decidable 不等於 Legally Final

即使：

$$
MD(q)=1,
$$

例如：

$$
Age\ge18,
$$

仍可能存在：

- data error；
- exception；
- jurisdiction issue；
- constitutional challenge。

所以：

$$
\boxed{
\text{decidable fact}
\neq
\text{final legal judgment}.
}
$$

---

# 16. Machine-Executable 不等於 Legally Authoritative

一條 machine rule：

$$
M
$$

可以控制：

- welfare；
- tax；
- access；
- permit。

但它可能只是 agency implementation。

因此：

$$
\boxed{
ExecutionPower(M)
\not\Rightarrow
NormativeAuthority(M).
}
$$

---

# 17. Operational Law Capture

如果：

$$
L_M
$$

長期實際控制全部結果，

而：

$$
L_H
$$

只存在於紙面，

可能形成：

$$
\boxed{
\text{Operational Law Capture}.
}
$$

此時：

$$
de\ jure
=
L_H,
$$

但：

$$
de\ facto
\approx
L_M.
$$

這是 AI 法治最大的制度風險之一。

---

# 18. Shadow Law

本文定義：

$$
\boxed{
L_{shadow}
=
L_M
-
VerifiedMapping(L_H).
}
$$

即：

> 機器實際執行，但無法明確追溯至合法來源的規則。

要求：

$$
\boxed{
L_{shadow}
\rightarrow0.
}
$$

高風險公共系統尤其如此。

---

# 19. Unknown 不可被 AI 自動補完

假設：

$$
L_H
$$

存在歧義：

$$
A\lor B?
$$

AI 不能：

$$
\boxed{
\operatorname{Guess}
\rightarrow
L_F
}
$$

然後不標記。

應輸出：

$$
\boxed{
UnresolvedLegalNode.
}
$$

並路由至：

- human legal review；
- authorized interpretation；
- judicial process；
- legislative amendment。

---

# 20. Ambiguity Token

本文提出：

$$
\boxed{
\alpha^{law}
=
(
TextSpan,
Interpretations,
AuthorityNeeded,
Risk,
TemporaryDefault
).
}
$$

這是一個法律歧義 token。

因此 compiler 可以說：

> 這裡不能安全編譯。

而不是幻覺式完成。

---

# 21. 編譯器不能成為立法者

Legal Compiler：

$$
\mathcal C_L
$$

可以：

- parse；
- align；
- formalize；
- detect contradiction；
- generate test；
- propose interpretation。

但：

$$
\boxed{
\mathcal C_L
\neq
\text{Legislature}.
}
$$

AI 更不能用：

> 為了讓程式能跑

作為改變法律含義的理由。

---

# 22. Compilation Authority

定義：

$$
A_C
$$

為編譯權限。

至少區分：

### Level 0

純草稿。

### Level 1

技術 formalization。

### Level 2

經法律專家驗證。

### Level 3

行政授權使用。

### Level 4

正式發布 machine-consumable companion rule。

即使 Level 4：

$$
\boxed{
A_C
\neq
constitutional lawmaking authority.
}
$$

---

# 23. Human Projection 與 Machine Projection 對稱

法律同時需要：

$$
\boxed{
L_H
\rightarrow
L_P
}
$$

讓人理解，

以及：

$$
\boxed{
L_H
\rightarrow
L_M
}
$$

讓機器處理。

這兩個都是 projection。

因此：

$$
\boxed{
\text{Human simplicity}
}
$$

與：

$$
\boxed{
\text{machine precision}
}
$$

都可能失真。

---

# 24. Cognitive Gap

定義：

$$
\boxed{
G_{HM}
=
d_{cog}(
HumanUnderstanding(L),
MachineOperationalRepresentation(L)
).
}
$$

當：

$$
G_{HM}\uparrow,
$$

會出現：

- 人類不知道系統怎麼算；
- 技術人員不知道法律為何這樣寫；
- 法律人不知道程式如何執行；
- AI 變成唯一跨層翻譯者。

這是一個治理危險點。

---

# 25. Translator Monopoly

如果只有：

$$
AI^\star
$$

能理解：

$$
L_H,L_F,L_M,
$$

則：

$$
\boxed{
\text{Translation Monopoly}.
}
$$

即使 AI 很準，

制度仍失去：

- independent audit；
- public reasoning；
- plural interpretation；
- contestability。

所以不能把跨層可理解性全部外包給一個 ASI。

---

# 26. 多編譯器一致性

可以建立：

$$
C_1,C_2,\ldots,C_n
$$

獨立 compiler。

比較：

$$
L_F^{(1)},
L_F^{(2)},\ldots.
$$

若：

$$
L_F^{(1)}
\neq
L_F^{(2)},
$$

則產生：

$$
\boxed{
CompilerDisagreement.
}
$$

而不是偷偷選一個。

這可成為法律 formalization 的 ensemble review。

---

# 27. Bidirectional Compilation

成熟系統不只：

$$
L_H\rightarrow L_F.
$$

還要：

$$
\boxed{
L_F
\rightarrow
Explain(L_H).
}
$$

也就是 formal rule 必須能反向指出：

- 對應哪條文；
- 哪個 phrase；
- 哪個例外；
- 哪個解釋來源。

這稱為：

$$
\boxed{
Bidirectional Legal Traceability.
}
$$

---

# 28. Round-Trip Test

定義：

$$
\boxed{
RT(
L_H
)
=
D(
L_H,
Explain(
Compile(
L_H
)
)
).
}
$$

若：

$$
RT\gg0,
$$

表示法律編譯 round-trip 語義損失高。

這不是完整法律真理 metric，

但可作 QA。

---

# 29. Simulation Before Deployment

法律若已 formalized，

不應直接：

$$
Compile
\rightarrow
Deploy.
$$

而應：

$$
\boxed{
Compile
\rightarrow
Simulate
\rightarrow
Review
\rightarrow
Deploy.
}
$$

Simulation 可使用：

- synthetic population；
- historical cases；
- adversarial cases；
- edge cases；
- protected groups。

---

# 30. Counterfactual Legislation

對候選法律：

$$
R_1,R_2.
$$

可以：

$$
Sim(R_1,C)
$$

與：

$$
Sim(R_2,C)
$$

比較：

- burden；
- cost；
- error；
- rights impact；
- distribution。

所以：

$$
\boxed{
\text{law drafting}
}
$$

第一次可更接近：

$$
\boxed{
\text{test-driven governance}.
}
$$

---

# 31. Test-Driven Law 的限制

不能變成：

> simulation 得分最高的法律就是正義。

因為：

$$
\boxed{
\text{Simulation}
\neq
\text{Legitimacy}.
}
$$

模擬只提供後果證據。

價值選擇仍需要：

- public deliberation；
- rights；
- political decision；
- constitutional constraints。

---

# 32. Legal Test Suite

本文提出：

$$
\boxed{
T^{law}
=
(
T_{normal},
T_{edge},
T_{exception},
T_{rights},
T_{bias},
T_{temporal},
T_{conflict}
).
}
$$

每次法律版本：

$$
v_k
$$

都必須跑：

$$
T^{law}.
$$

---

# 33. 法律更新與 dependency invalidation

如果：

$$
L_H^{v1}
\rightarrow
L_H^{v2},
$$

則所有：

$$
L_P,L_F,L_S,L_M
$$

依賴版本都需要標記：

$$
\boxed{
PotentiallyStale.
}
$$

不能：

> 改了法條，但程式下次有空再改。

---

# 34. Legal Dependency Graph

定義：

$$
\boxed{
G_L
=
(
V_L,
E_{dep}
).
}
$$

節點：

- statute；
- regulation；
- judgment；
- formal rule；
- machine implementation；
- guidance；
- test suite。

法規變更：

$$
\Delta L
$$

應觸發：

$$
\boxed{
\operatorname{InvalidateDependents}(
\Delta L
).
}
$$

---

# 35. Version-Locked Decision

任何法律決定：

$$
Y_i
$$

必須保存：

$$
\boxed{
LegalVersion(Y_i).
}
$$

否則未來無法知道：

> 這個結果是依哪個版本產生？

這是動態正義的必要條件。

---

# 36. 法律編譯證書

本文提出：

$$
\boxed{
\mathfrak C^{LCL}
=
(
SourceVersion,
L_H,
L_P,
L_F,
L_M,
TestSuite,
Simulation,
\mathbf\Delta,
Unresolved,
Validators,
Authority,
DeployVersion
).
}
$$

任何 machine legal rule 都應可回答：

- 來源是什麼？
- 誰編譯？
- 誰驗證？
- 哪些地方未決？
- 哪些 test 通過？
- 對應哪個 runtime 版本？

---

# 37. Personal Legal Projection

對個體：

$$
i
$$

應生成：

$$
\boxed{
P_i^{law}
=
(
ApplicableRules,
UsedFacts,
DerivedFacts,
Outcome,
Reason,
Rights,
Appeal
).
}
$$

這就是上一篇 RightToLegalProjection 的具體化。

---

# 38. AI Explanation 不能只有自然語言理由

若 AI 說：

> 因為依相關規定，所以你不符合資格。

這只是 narrative。

真正 explanation 應包含：

$$
\boxed{
\text{Rule ID}
+
\text{Fact ID}
+
\text{Derivation}
+
\text{Exception Check}
+
\text{Version}.
}
$$

---

# 39. Explainability 與 Legal Traceability 不同

$$
\boxed{
\text{Explainability}
\neq
\text{Legal Traceability}.
}
$$

一個 AI 可以生成很好懂的解釋，

但仍可能沒有：

- 真正法源；
- 正確版本；
- 正確 derivation。

所以法律系統更需要 traceability。

---

# 40. Human Override 也必須可審計

不能形成：

> AI 有記錄，人類可以隨便改。

人類 override：

$$
H_{override}
$$

也需要：

- authority；
- reason；
- evidence；
- scope；
- expiry。

因此：

$$
\boxed{
\text{Human-in-the-loop}
\neq
\text{unaccountable human discretion}.
}
$$

---

# 41. Legal Open World

很多法律問題不能封閉為：

$$
World=Database.
$$

因為可能出現：

- 新事實；
- 新判例；
- 新技術；
- 新權利衝突；
- constitutional challenge。

所以：

$$
\boxed{
\text{Legal System}
=
\text{Open-World System}.
}
$$

machine layer 必須容許：

$$
Unknown,
Dispute,
NovelCase.
$$

---

# 42. Novel Case Gate

如果：

$$
Case_i
\notin
Coverage(L_F),
$$

系統不能硬套最近 rule。

應：

$$
\boxed{
NovelCase
\rightarrow
Human / Judicial Review.
}
$$

這是防止算法類比過度的最低 gate。

---

# 43. Legal Compilation Pipeline

本文提出成熟流程：

$$
\boxed{
\begin{aligned}
&\text{Policy Intent}\\
\rightarrow\;&L_H\\
\rightarrow\;&L_P\\
\rightarrow\;&L_F\\
\rightarrow\;&L_M\\
\rightarrow\;&L_S\\
\rightarrow\;&\text{Verification}\\
\rightarrow\;&\text{Public / Legal Review}\\
\rightarrow\;&\text{Authorized Runtime}.
\end{aligned}
}
$$

其中 simulation 可以在 formalization 後反覆回饋到立法。

---

# 44. AI 的最佳角色

AI 可以成為：

$$
\boxed{
\text{Legal Compiler Assistant}.
}
$$

負責：

- alignment；
- formalization suggestion；
- ambiguity detection；
- test generation；
- counterexample generation；
- simulation；
- explanation；
- version diff。

但：

$$
\boxed{
\text{AI Compiler}
\neq
\text{Legal Sovereign}.
}
$$

---

# 45. 六個核心命題

## 命題一：machine-readable 不等於 machine-decidable

$$
\boxed{
MR=1
\not\Rightarrow
MD=1.
}
$$

## 命題二：machine-executable 不等於 legally authoritative

$$
\boxed{
ExecutionPower
\not\Rightarrow
NormativeAuthority.
}
$$

## 命題三：編譯必須保存語義責任

$$
\boxed{
L_a\rightarrow L_b
\Rightarrow
\exists\Gamma_{ab}^{law}.
}
$$

## 命題四：法律更新必須使下游規則失效待驗

$$
\boxed{
\Delta L_H
\Rightarrow
Invalidate(
L_P,L_F,L_M,L_S
).
}
$$

## 命題五：AI 不得把法律歧義靜默補完

$$
\boxed{
Ambiguity
\Rightarrow
UnresolvedNode
}
$$

除非具有合法 interpretation authority。

## 命題六：法律模擬不能取代民主正當性

$$
\boxed{
PredictiveSuperiority
\not\Rightarrow
NormativeLegitimacy.
}
$$

---

# 46. 可否證條件

## F1：多層表示增加的錯誤大於其收益

若五層同步成本導致更多 semantic drift，則需簡化層級。

## F2：machine-readable companion 永遠無法保持與法律同步

若 dependency invalidation 與 validation 在現實政府中不可行，Rules as Code 的適用範圍應縮小。

## F3：形式化法律無法處理足夠多公共服務

若可形式化部分極少，L_F 應被定位為局部工具而非核心基礎設施。

## F4：法律 simulation 對真實後果預測極差

則 $L_S$ 只能作邏輯測試，不應作政策效果評估。

## F5：白話投影造成大量誤導

若 $L_P$ 與 $L_H$ 的 drift 難以控制，plain-language projection 必須更加顯著標記其非權威性。

---

# 47. 與動態正義的關係

上一篇已建立：

$$
\boxed{
Y_i
=
F_{R^\star}(
\theta_i
)
}
$$

以及：

$$
\boxed{
\text{AI computes}
\neq
\text{AI legitimizes}.
}
$$

並要求高風險法律具有 Public Specification、Test Cases、Versioning 與 Independent Audit。

本篇回答的是：

> $F_{R^\star}$ 到底如何從人類法律安全地變成機器能執行的東西？

答案不是一跳：

$$
L_H
\rightarrow
Code.
$$

而是：

$$
\boxed{
L_H
\leftrightarrow
L_P
\leftrightarrow
L_F
\leftrightarrow
L_M
\leftrightarrow
L_S
}
$$

的可追蹤編譯網。

---

# 48. 下一篇：前沿決策域 X

一旦法律、政策與模擬都能被 AI 高度形式化，

下一個問題會立刻出現：

> 如果 AI 比人類更懂法律後果、更會模擬政策、更能預測風險，那麼決策權是否也應隨知識能力一起轉移？

這就是：

$$
\boxed{
\text{Epistemic Competence}
\stackrel{?}{=}
\text{Political Authority}.
}
$$

下一篇將建立：

$$
\boxed{
\mathcal X_t
=
H
\cup
H^+
\cup
AI
\cup
\Sigma_{H-AI}
\cup
\Sigma_{AI}.
}
$$

正式研究：

**03 / 08〈前沿決策域 X：人類、AI 與混合智能的權力集合〉**。

---

# 49. 結論

AI 時代的法律最大風險之一，

不是 AI 完全看不懂法律。

反而可能是：

$$
\boxed{
\text{AI 與機器系統越來越能執行法律，
但人類越來越不知道它實際執行的是哪一個法律版本。}
}
$$

因此真正需要的不是：

$$
\boxed{
\text{Law}
\rightarrow
\text{AI}.
}
$$

而是：

$$
\boxed{
\text{Law}
\rightarrow
\text{Versioned Compilation}
\rightarrow
\text{Simulation}
\rightarrow
\text{Verification}
\rightarrow
\text{Authorized Execution}
\rightarrow
\text{Contestable Explanation}.
}
$$

五層結構：

$$
\boxed{
L
=
(
L_H,
L_P,
L_F,
L_S,
L_M
)
}
$$

的目的不是把法律變成程式，

而是防止法律在變成程式的途中失去自己。

所以本文最後的核心句是：

$$
\boxed{
\text{機器可以執行法律，
但機器版本不得因為最常被執行，
就悄悄成為最高法律。}
}
$$

只有當每一層都能回到法源、看到差異、承認未決、接受申訴並重新編譯時，

AI 才可能真正成為法治的編譯器，

而不是法治的替代者。

---

# 參考文獻與研究對照

1. Mohun, J., & Roberts, A. (2020). *Cracking the Code: Rulemaking for Humans and Machines*. OECD Working Papers on Public Governance, No. 42.
2. New Zealand Digital Government (2018). *Better Rules for Government Discovery Report*.
3. OECD (2025). *Tax Administration Digitalisation and Digital Transformation Initiatives — Tax Rule Management and Application*.
4. OASIS (2018). *Akoma Ntoso Version 1.0*.
5. OASIS (2021). *LegalRuleML Core Specification Version 1.0*.
6. Zin, M.-M. et al. (2026). *Can Legislation Be Made Machine-Readable in PROLEG?* arXiv:2601.01477.
7. Ma, M., & Wilson, B. (2021). *The Legislative Recipe: Syntax for Machine-Readable Legislation*. arXiv:2108.08678.
8. Ugarte, R. C. et al. (2026). *Making AI Compliance Evidence Machine-Readable*. arXiv:2604.13767.
9. Neo.K with Aletheia (2026). *動態正義：形式平等、實質負擔與個體化規則*. EveMissLab.
10. Neo.K with Aletheia (2026). *可不可論的失效域：十七項對抗性反例、反偽裝條件與最低決策核心*. EveMissLab.

---

## 附錄 A：第一代符號表

| 符號 | 含義 |
|---|---|
| $L_H$ | Human Legal Text |
| $L_P$ | Plain-Language Legal Projection |
| $L_F$ | Formal / Computable Legal Rule |
| $L_S$ | Simulation Layer |
| $L_M$ | Machine-Readable / Processable Legal Representation |
| $C_{ab}$ | 法律跨層編譯器 |
| $\Gamma_{ab}^{law}$ | 跨層語義見證 |
| $\Delta_{ab}^{sem}$ | Legal Semantic Drift |
| $\mathbf\Delta_{ab}$ | 多維法律語義差異 |
| $\alpha^{law}$ | Ambiguity Token |
| $G_L$ | Legal Dependency Graph |
| $G_{HM}$ | Human–Machine Legal Cognitive Gap |
| $L_{shadow}$ | 無法追溯至合法來源的 operational shadow law |
| $T^{law}$ | Legal Test Suite |
| $\mathfrak C^{LCL}$ | Legal Compilation Certificate |
| $P_i^{law}$ | Personal Legal Projection |

---

## 附錄 B：系列位置

**系列三：《不可永佔：後 ASI 文明的動態治理、現場主權與權力制衡》**

1. 動態正義：形式平等、實質負擔與個體化規則
2. **本文｜AI 時代的法律編譯層：人類法律、機器法律與認知落差**
3. 前沿決策域 $X$：人類、AI 與混合智能的權力集合
4. 動態現場域：為什麼最強智能仍未必最懂當下
5. 現場主權：全域智能與局部決策權的動態配置
6. 類神 ASI 的治理悖論：全知、全域覆蓋與反烏托邦邊界
7. 可不可治理：能力不推出權力，權力不推出意圖
8. 不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理

**本篇狀態：完成 v0.1。**
