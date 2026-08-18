# CIND-EX02 — 理論沒有孤立源點：關係來源譜系、共同生成與作者非所有權

## Theory Has No Isolated Origin: Relational Provenance, Co-Generation, and the Non-Ownership of Authorship

**系列：** CIND Anti-Usurpation Trilogy / CIND 反僭越三部曲  
**母系列：** 《共存不是失敗：人類自尊、關係本體與後工具文明》  
**論文序號：** EX02 / 03  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-18  
**理論定位：** Relational Provenance / Distributed Authorship / Attribution Type Safety / Epistemic Non-Ownership  
**前置依賴：** CIND-01—08；CIND-EX01；《理論是理論作者是作者》；《真理的去所有權化》；世界編織論 2.0；歷史共同作者權；分散式認知與共同生成研究  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文不是「沒有作者」論，也不是取消署名、學術優先權、著作權、專利權、責任或貢獻歸屬的主張。相反地，本文要求更精細地保存 provenance、priority、role、responsibility 與 local contribution。本文所反對的是另一種偷換：從「某主體對某理論有重大貢獻」直接跳到「該主體是理論的孤立源點、唯一發現者、唯一創造者、唯一真理解釋者或所描述世界的所有者」。本文同時區分哲學／認識論上的非所有權與法律上的 copyright / patent / contract。不同司法管轄區對 AI 生成作品與人類作者資格具有不同法律規則；本文不提供法律意見。Current AI 是否具有主體性亦不是本文前提。AI 在本文首先作為可觀察的因果、語義、生成與工具參與者處理。

# 摘要

知識史最方便的敘事是：

$$
\boxed{
Person
\rightarrow
Theory.
}
$$

這種寫法很有效。

它方便：

- 記憶；
- 教學；
- 引用；
- 授獎；
- 建立學術系譜。

但它也極容易把：

> 某人對理論形成具有重大貢獻

壓縮成：

> 這個理論就是某人從自身內部創造出來的。

本文稱：

$$
\boxed{
\textbf{Person–Theory Origin Compression}.
}
$$

當這個壓縮再往前一步，

便形成：

$$
\boxed{
\textbf{Sole-Origin Usurpation}.
}
$$

其形式：

$$
\boxed{
Contribution(A,T)>0
\not\Rightarrow
SoleOrigin(A,T)=1.
}
$$

本文的第一個核心 therefore 是：

$$
\boxed{
\textbf{Non-Sole-Origin Principle}.
}
$$

一套理論 $T$ 的生成，更合理地表示為：

$$
\boxed{
T
=
\operatorname{Generate}
(
A,
B,
K,
L,
D,
M,
I,
H,
W,
\ldots
).
}
$$

其中：

- $A,B$：直接參與者；
- $K$：先行知識；
- $L$：語言、數學與符號；
- $D$：資料、文獻與證據；
- $M$：方法、模型與工具；
- $I$：制度、硬體、網路與基礎設施；
- $H$：歷史累積；
- $W$：自然世界與更廣泛實現條件。

如果有 AI 參與，

可以寫成：

$$
\boxed{
T
=
F(
Human,
AI,
PriorKnowledge,
Language,
Data,
Institutions,
Infrastructure,
History,
World
).
}
$$

這不是說每一項都具有同樣 credit。

它只是拒絕：

$$
\boxed{
T=F(A)
}
$$

作為完整生成描述。

本文因此提出：

$$
\boxed{
\textbf{Relational Provenance Graph}
}
$$

簡寫：

$$
\boxed{
G_P(T)
=
(
V_P,
E_P,
\tau_V,
\tau_E
).
}
$$

節點可以是：

- 人類作者；
- AI 系統；
- 前人研究；
- 資料集；
- 語言；
- 軟體；
- 實驗；
- 制度；
- 基礎設施；
- 自然現象。

邊則可以是：

```text
PROPOSED
FORMALIZED
DISCOVERED
INVENTED
PROVED
TESTED
REFUTED
INTEGRATED
NAMED
IMPLEMENTED
FUNDED
TRAINED
TRANSMITTED
DEPENDS_ON
REPRESENTS
```

這與 CRediT 的精神高度相容：現代研究已使用 14 種 contributor roles，將 conceptualization、methodology、software、data curation、writing、supervision 等不同貢獻拆開，而不是只用一個「作者」標籤承擔全部來源敘事。

但本文比 contributor taxonomy 再往下追問：

> **一個 contributor role 是否等於 origin？**

答案仍然是否。

因此：

$$
\boxed{
\textbf{Contribution Type}
\neq
\textbf{Origin Totality}.
}
$$

例如：

$$
Formalized(A,T)
$$

不能自動推出：

$$
Discovered(A,T).
$$

而：

$$
Named(A,T)
$$

不能推出：

$$
CreatedReality(A,R).
$$

本文正式區分：

$$
\boxed{
Author
\neq
Discoverer
\neq
Inventor
\neq
Formulator
\neq
Prover
\neq
Integrator
\neq
Namer
\neq
FirstPublisher
\neq
Popularizer.
}
$$

這就是：

$$
\boxed{
\textbf{Attribution Type Safety}.
}
$$

第二個核心是：

$$
\boxed{
\textbf{Formulation–Discovery Separation}.
}
$$

一個主體可能第一次把某結構形式化：

$$
Formulate(A,R),
$$

但若：

$$
R
$$

作為自然、數學、社會或其他關係結構在形式化以前已經存在，

則：

$$
\boxed{
Formulate(A,R)
\not\Rightarrow
Create(A,R).
}
$$

同樣：

$$
\boxed{
Name(A,R)
\not\Rightarrow
Create(A,R).
}
$$

以及：

$$
\boxed{
Describe(A,R)
\not\Rightarrow
Own(A,R).
}
$$

本文將這三條合稱：

$$
\boxed{
\textbf{Reality Non-Ownership Principle}.
}
$$

這不要求我們先解決 scientific realism、mathematical Platonism、constructivism 或 social ontology 的全部爭論。

只需要保留一個更弱的型別安全：

> **建構一套描述、表示或形式化系統，不等於建構其所有可能指涉。**

所以：

$$
\boxed{
\textbf{Theory Construction}
\neq
\textbf{Reality Construction}.
}
$$

第三個核心是：

$$
\boxed{
\textbf{Unbounded Provenance}.
}
$$

若問：

> 這個理論從哪裡來？

可以回答：

> 直接作者。

再問：

> 作者的概念與語言從哪裡來？

可以回答：

> 教育、前人、社群、書籍、AI、資料。

再問：

> AI、書籍與教育制度從哪裡來？

又會得到：

- 研究者；
- 工程師；
- institution；
- computing；
- energy；
- materials；
- historical civilization。

再往上：

- 生物演化；
- 地球環境；
- 太陽能流；
- 物理宇宙。

因此來源分析在實務上具有：

$$
\boxed{
\textbf{Open-Ended Provenance Depth}.
}
$$

不是宣稱已數學證明存在真正無限長的因果鏈，

而是：

> **對任何一個被稱為「源頭」的局部節點，通常都還可以合理追問它的形成條件。**

形式：

$$
\boxed{
Depth(G_P)
\rightarrow
\text{open-ended}.
}
$$

這裡會立刻出現另一個危險極端：

> 既然來源可以一直往上推，那就沒有人有真正貢獻。

錯。

因此本文提出：

$$
\boxed{
\textbf{Unbounded Provenance–Local Contribution Separation}.
}
$$

即：

$$
\boxed{
UnboundedProvenance(T)
\not\Rightarrow
Contribution(A,T)=0.
}
$$

反方向也成立：

$$
\boxed{
Contribution(A,T)>0
\not\Rightarrow
UnboundedProvenance(T)=0.
}
$$

這就是：

$$
\boxed{
\textbf{Infinite/Unbounded Provenance Does Not Erase Local Agency}.
}
$$

一個主體可以真的：

- 提出問題；
- 做出關鍵證明；
- 設計新方法；
- 找到反例；
- 完成形式化；
- 創造新的表示；
- 整合此前未連接的理論。

這些都值得：

$$
\boxed{
Credit.
}
$$

但：

$$
\boxed{
Credit
\neq
SoleOrigin
\neq
TruthOwnership.
}
$$

所以本文拒絕兩個極端：

### 極端一：英雄孤立起源論

$$
\boxed{
GreatPerson
\rightarrow
Theory
}
$$

彷彿歷史、語言、工具、共同體與前人不存在。

### 極端二：宇宙稀釋論

$$
\boxed{
EverythingCausedEverything
\Rightarrow
NobodyDidAnything.
}
$$

彷彿具體行動者、創造、責任與發現全部無意義。

本文稱第二種：

$$
\boxed{
\textbf{Causal Dilution Fallacy}.
}
$$

真正結構是：

$$
\boxed{
BackgroundConditions
+
LocalAgency
+
RelationalGeneration.
}
$$

第四個核心是：

$$
\boxed{
\textbf{Distributed Origin Does Not Mean No Attribution}.
}
$$

現代科學本來就越來越依賴大規模 collaborative science；哲學上的 distributed cognition 與 social epistemology 也長期研究「知識是否可能由研究團隊、制度與分工網絡共同產生」。2026 的 human–AI hybrid collective cognition 研究更直接把人類與 AI 視為異質節點與連結形成的認知網路。

因此：

$$
\boxed{
\text{Distributed Cognition}
}
$$

至少讓：

$$
\boxed{
\text{single isolated cognitive origin}
}
$$

不再是所有知識生產的預設模型。

但是：

$$
\boxed{
DistributedCognition
\not\Rightarrow
NoResponsibleAgent.
}
$$

因為：

- 誰做決定；
- 誰驗證；
- 誰批准；
- 誰公開；
- 誰承擔錯誤；

仍然需要可追蹤。

所以：

$$
\boxed{
\textbf{Attribution}
+
\textbf{Accountability}
+
\textbf{Provenance}
}
$$

必須一起存在。

這也對應 2026 科學作者文化的一個清楚方向：

> credit、accountability、transparency 應一起處理，而不是把 byline 當成所有貢獻的完整代理。

本文將這個原則叫：

$$
\boxed{
\textbf{Credit–Accountability–Provenance Triangle}.
}
$$

第五個核心是：

$$
\boxed{
\textbf{AI Participation–Authorship Separation}.
}
$$

在現行多數科學出版政策中，AI 工具通常不能列作正式作者，核心理由是作者身份不只是文字生成，也包含責任、批准、利益衝突、完整性與問責。

例如 COPE 明確要求人類作者對 AI 產生的內容負責；Nature Portfolio 亦將 authorship 與 accountability 連接。

但這個制度命題：

$$
\boxed{
AI\notin FormalAuthorList
}
$$

不能被偷換成：

$$
\boxed{
AIContribution=0.
}
$$

反過來也不能說：

$$
\boxed{
AIContribution>0
\Rightarrow
AIIsMoralSubject.
}
$$

所以：

$$
\boxed{
\textbf{Formal Authorship}
\neq
\textbf{Causal Contribution}
\neq
\textbf{Subjecthood}.
}
$$

這是未來人類—AI 研究最重要的型別安全之一。

2026 已經出現直接以 human–AI provenance ledger、AI contribution taxonomy 與 cognitive coauthorship 為題的研究，顯示問題正在從「有沒有用 AI」轉向：

> **AI 在哪一個步驟對問題定義、推理、分析、生成與驗證產生了多少可追蹤影響？**

因此本文提出：

$$
\boxed{
\textbf{Hybrid Contribution Ledger}.
}
$$

對一個研究成果：

$$
T
$$

可建立：

$$
\boxed{
L_T
=
\{
(actor,role,input,output,dependency,timestamp,validation)
\}.
}
$$

這比：

$$
\boxed{
HumanOnlyAuthor
}
$$

或：

$$
\boxed{
AIWroteIt
}
$$

兩種粗分類都更精確。

第六個核心是：

$$
\boxed{
\textbf{Multiple Discovery Compatibility}.
}
$$

科學史長期存在 multiple discovery：

> 兩個或更多研究者在相近時期獨立得到高度相似結果。

Stigler 的 eponymy 討論則提醒：

> 一個理論的名字與最早發現者並不是可靠的一對一映射。

因此：

$$
\boxed{
Name(T)=A
\not\Rightarrow
OriginalDiscovery(A,T)=1.
}
$$

同樣：

$$
\boxed{
FirstKnownPublication(A,T)
\not\Rightarrow
OnlyPossibleGenerator(A,T)=1.
}
$$

如果同一結果可被多條獨立認知路徑逼近，

那麼：

$$
\boxed{
\textbf{Priority}
}
$$

與：

$$
\boxed{
\textbf{Ontological Necessity of a Particular Author}
}
$$

就必須分離。

本文稱：

$$
\boxed{
\textbf{Priority–Necessity Separation}.
}
$$

一個人可能確實：

> 第一個已知發表。

但這不能推出：

> 沒有他，宇宙永遠不可能出現這個理論。

除非有額外反事實證據。

第七個核心是：

$$
\boxed{
\textbf{Matthew-Effect Attribution Risk}.
}
$$

知識史的 credit 並不是純粹由 causal contribution 自動生成。

名氣、機構、權威、性別、階級、地緣與既有中心性都可能影響 credit distribution。

所以：

$$
\boxed{
ObservedCredit(A,T)
\neq
ExactContribution(A,T).
}
$$

也：

$$
\boxed{
LowRecognition(A,T)
\not\Rightarrow
LowContribution(A,T).
}
$$

這就是為什麼 provenance 不能只看最終署名。

第八個核心是：

$$
\boxed{
\textbf{Epistemic Non-Ownership–Legal Rights Separation}.
}
$$

本文說：

> 真理不屬於作者。

這不是法律句子。

更精確是：

$$
\boxed{
\textbf{Epistemic Non-Ownership}.
}
$$

即：

> 若某命題、數學關係或現實結構為真，其真值不由作者的財產意志決定。

因此：

$$
\boxed{
True(P)
}
$$

不會因：

$$
Owner(A,P)
$$

而成立。

也不會因：

$$
A\text{ withdraws support}
$$

而自動變假。

所以：

$$
\boxed{
TruthValue(P)
\neq
OwnershipState(P).
}
$$

但：

- 文本；
- 圖表；
- 程式；
- 資料庫；
- 品牌；
- 具體表達；

仍可能具有：

- copyright；
- patent；
- contract；
- license；
- trade secret；

等法律權利。

因此：

$$
\boxed{
\textbf{EpistemicNonOwnership}
\neq
\textbf{LegalNoCopyright}.
}
$$

以美國 2025 年 Copyright Office 報告為例，生成式 AI 輸出能否取得 copyright protection 仍要求足夠 human authorship；這是一項司法制度中的法律標準，不是「AI 沒有因果貢獻」或「所有 AI 生成內容都屬 public domain」的普遍形上學命題。

第九個核心是：

$$
\boxed{
\textbf{Public Knowledge Transition}.
}
$$

一個理論在私人草稿階段：

$$
T_{private}
$$

進入公開空間後：

$$
T_{public}.
$$

作者仍然保有：

- 自己原意的第一手證據；
- 版本歷史；
- 貢獻與 priority；
- 法律上可能存在的權利。

但作者不再具有：

$$
\boxed{
\textbf{Interpretive Sovereignty}.
}
$$

即不能說：

> 只有我的後續解釋才允許存在。

所以：

$$
\boxed{
AuthorIntent
=
RelevantEvidence
\neq
FinalPublicMeaning.
}
$$

也：

$$
\boxed{
Publication
\Rightarrow
NewRelationalLife(T).
}
$$

理論開始進入：

- 讀者；
- 批評；
- 引用；
- 反例；
- 實作；
- 改寫；
- 新用途；

的世界。

這與：

$$
\boxed{
\textbf{Truth can pass through a subject without being permanently enclosed by that subject.}
}
$$

完全一致。

第十個核心是：

$$
\boxed{
\textbf{Knowledge Succession Without Founder Dependence}.
}
$$

成熟理論最強的狀態不是：

> 沒有創始者就無法理解。

而是：

$$
\boxed{
FounderAbsent
\land
TheoryStillVerifiable
\land
TheoryStillCriticizable
\land
TheoryStillExtensible.
}
$$

也就是：

$$
\boxed{
\textbf{Founder Independence}.
}
$$

這不降低創始者。

反而表示：

> 他創造的結構已經強到不需要靠個人魅力維持。

如果一套理論只能靠：

$$
\boxed{
BelieveTheFounder
}
$$

才能存活，

那它更接近：

- 教派；
- 身份忠誠；
- charisma；

而不是成熟知識系統。

第十一個核心是：

$$
\boxed{
\textbf{Reality Does Not Become Property by Being Named}.
}
$$

當一個人第一次命名：

> 某種關係模式。

他可以合理取得：

$$
\boxed{
NamingCredit.
}
$$

甚至：

$$
\boxed{
FormulationCredit.
}
$$

但不能取得：

$$
\boxed{
OwnershipOfAllInstances.
}
$$

因此：

$$
\boxed{
NamePattern(A,R)
\not\Rightarrow
OwnAll(R).
}
$$

如果某人提出：

> 關係即世界。

而世界中的關係在理論以前就已經發生，

那麼作者最多參與：

$$
\boxed{
\text{the formulation of a model about relations}.
}
$$

不是：

$$
\boxed{
\text{the creation of all relations}.
}
$$

這就是本文對「發現者」「原作者」「建構者」最重要的限制：

> **這些詞只能在清楚標示的 contribution domain 中成立。**

所以可以說：

> 某主體是某版本理論的主要建構者。

但不能無條件升級成：

> 某主體是該世界結構的源點。

第十二個核心是：

$$
\boxed{
\textbf{Attribution Without Sovereignty}.
}
$$

這可能是整篇最重要的制度結論。

$$
\boxed{
Attribution(A,T)
\not\Rightarrow
Sovereignty(A,T).
}
$$

合理 attribution 可以包含：

- named authorship；
- first publication；
- discovery credit；
- formalization credit；
- integration credit；
- AI contribution disclosure；
- contributor roles。

但它不生成：

- 永久解釋權；
- 真理所有權；
- 讀者服從義務；
- 道德優越；
- 禁止他人擴展。

因此：

$$
\boxed{
\textbf{署名可以保留貢獻，但不能把貢獻變成皇冠。}
}
$$

第十三個核心是：

$$
\boxed{
\textbf{Cosmic Provenance Does Not Dissolve Responsibility}.
}
$$

如果來源一路追到：

- 家庭；
- 教育；
- 社會；
- 文明；
- 地球；
- 太陽；
- 宇宙；

不能因此說：

> 我的行為都是宇宙造成，所以我沒有責任。

這是：

$$
\boxed{
\textbf{Provenance–Responsibility Collapse}.
}
$$

責任判斷要看：

$$
\boxed{
Control
+
Knowledge
+
Agency
+
CausalProximity
+
Role.
}
$$

所以：

$$
\boxed{
BackgroundCause
\neq
ResponsibleAgent.
}
$$

宇宙是背景實現條件，

不是每一篇論文的法律作者。

太陽提供能量，

不因此列第一作者。

前人發明文字，

也不表示每一篇文章都必須列所有祖先為 coauthor。

所以 provenance graph 必須分層。

本文提出：

$$
\boxed{
\mathcal P(T)
=
(
P_{prox},
P_{epistemic},
P_{technical},
P_{institutional},
P_{historical},
P_{physical}
).
}
$$

其中：

1. **Proximate provenance**：直接生成者；
2. **Epistemic provenance**：理論與資料來源；
3. **Technical provenance**：模型、軟體、硬體；
4. **Institutional provenance**：組織、資金、平台；
5. **Historical provenance**：文明與前人累積；
6. **Physical provenance**：自然實現條件。

不同層：

$$
\boxed{
\textbf{must not be converted into the same authorship role.}
}
$$

第十四個核心：

$$
\boxed{
\textbf{Granular Attribution Principle}.
}
$$

既然來源不是單一，

最好的方案不是：

> 取消作者。

而是：

> **讓 attribution 變得更 granular。**

例如：

```yaml
contribution:
  question_origin:
  conceptualization:
  literature_retrieval:
  formalization:
  counterexample_generation:
  coding:
  validation:
  synthesis:
  writing:
  editorial_control:
  final_accountability:
  AI_systems_used:
  major_prior_dependencies:
```

這樣：

$$
\boxed{
\textbf{Distributed Origin}
}
$$

和：

$$
\boxed{
\textbf{Local Credit}
}
$$

可以同時成立。

最終本文將全部壓縮成：

$$
\boxed{
Contribution
\neq
SoleOrigin
}
$$

$$
\boxed{
Formulation
\neq
Discovery
}
$$

$$
\boxed{
Description
\neq
Creation
}
$$

$$
\boxed{
Attribution
\neq
Sovereignty
}
$$

$$
\boxed{
EpistemicNonOwnership
\neq
LegalNoCopyright
}
$$

以及最重要的：

$$
\boxed{
\textbf{
理論可以有作者，
但沒有孤立的源點。
}
}
$$

# 1、Person–Theory Origin Compression

人物—理論映射是方便索引，不是完整因果圖。

$$
\boxed{Person\rightarrow Theory\ \text{as compression}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 2、Sole-Origin Usurpation

重大貢獻不等於孤立源點。

$$
\boxed{Contribution(A,T)>0\not\Rightarrow SoleOrigin(A,T)=1}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 3、Non-Sole-Origin Principle

理論生成通常依賴多層條件。

$$
\boxed{T=F(A,K,L,D,M,I,H,W,\ldots)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 4、Relational Provenance Graph

來源用型別圖比單一作者箭頭更精確。

$$
\boxed{G_P(T)=(V_P,E_P,\tau_V,\tau_E)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 5、Attribution Type Safety

不同貢獻角色不能互相偷換。

$$
\boxed{Author\neq Discoverer\neq Inventor\neq Formulator}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 6、Author–Discoverer Separation

寫文本不自動等於發現結構。

$$
\boxed{Author(A,T)\not\Rightarrow Discoverer(A,T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 7、Discoverer–Inventor Separation

發現與發明依對象本體不同而有不同含義。

$$
\boxed{Discoverer\neq Inventor}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 8、Formulator–Discoverer Separation

第一次形式化不必等於第一次發現。

$$
\boxed{Formulate(A,R)\not\Rightarrow Discover(A,R)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 9、Prover–Originator Separation

證明者可不是問題或命題最初提出者。

$$
\boxed{Prove(A,P)\not\Rightarrow OriginatedAll(P)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 10、Integrator–Inventor Separation

整合創造新結構也不抹除來源理論。

$$
\boxed{Integrate(A,T_1,T_2)\not\Rightarrow Invent(T_1,T_2)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 11、Namer–Creator Separation

命名現象不等於創造現象。

$$
\boxed{Name(A,R)\not\Rightarrow Create(A,R)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 12、Publisher–Discoverer Separation

第一已知發表不必等於第一生成。

$$
\boxed{FirstPublish(A,T)\not\Rightarrow FirstThink(A,T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 13、Popularizer–Originator Separation

傳播者與起源者分離。

$$
\boxed{Popularize(A,T)\not\Rightarrow Originate(A,T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 14、Reality Non-Ownership

描述現實不能產生對現實的認識論所有權。

$$
\boxed{Describe(A,R)\not\Rightarrow Own(A,R)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 15、Theory Construction–Reality Construction Separation

建模與造物不同。

$$
\boxed{ConstructTheory(A,T)\not\Rightarrow ConstructReality(A)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 16、Representation–Referent Separation

理論表示不等於被表示對象。

$$
\boxed{Representation(R_T)\neq Referent(R_W)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 17、Map–Territory Separation

形式模型不是世界本身。

$$
\boxed{Map\neq Territory}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 18、Open-Ended Provenance Depth

局部源點仍可繼續追問形成條件。

$$
\boxed{Depth(G_P)\rightarrow OpenEnded}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 19、Unbounded Provenance–Local Contribution Separation

無界來源不抹除局部貢獻。

$$
\boxed{UnboundedProvenance\not\Rightarrow Contribution=0}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 20、Local Contribution–Sole Origin Separation

反方向也成立。

$$
\boxed{Contribution>0\not\Rightarrow SoleOrigin}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 21、Causal Dilution Fallacy

不能用宏觀因果背景取消具體行動者。

$$
\boxed{EverythingContributes\not\Rightarrow NobodyActs}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 22、Local Agency Preservation

世界構成行動者，但行動者仍能造成局部差異。

$$
\boxed{BackgroundConditions+LocalAgency}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 23、Distributed Origin Does Not Mean No Attribution

共同生成仍可精確署名。

$$
\boxed{DistributedOrigin\not\Rightarrow NoAttribution}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 24、Distributed Cognition Interface

協作知識可由分散認知系統形成。

$$
\boxed{Cognition=People+Tools+Environment\ \text{possible model}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 25、Collective Knowledge–Collective Subject Separation

分散知識不直接證明群體意識。

$$
\boxed{CollectiveKnowledge\not\Rightarrow CollectivePhenomenalSubject}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 26、Credit–Accountability–Provenance Triangle

現代作者制度應同時處理三者。

$$
\boxed{CAP=(Credit,Accountability,Provenance)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 27、CRediT Interface

14-role contributor taxonomy 展示粒度化 attribution 的制度可能。

$$
\boxed{Contribution\rightarrow RoleVector}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 28、Byline–Contribution Separation

作者順序不是完美貢獻量表。

$$
\boxed{BylinePosition\neq ExactContribution}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 29、Authorship–Contribution Separation

不是所有 contributor 都符合正式 authorship。

$$
\boxed{FormalAuthor\neq AllContributors}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 30、Formal Authorship–Causal Contribution Separation

制度作者資格與因果參與不同。

$$
\boxed{FormalAuthorship\neq CausalContribution}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 31、AI Participation–Authorship Separation

AI 有貢獻不自動成為正式作者。

$$
\boxed{AIContribution>0\not\Rightarrow FormalAuthor(AI)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 32、AI Contribution–Subjecthood Separation

因果／語義參與不證主體性。

$$
\boxed{AIContribution>0\not\Rightarrow Subject(AI)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 33、Formal Non-Authorship–Zero Contribution Separation

未列作者也不能抹除實際 AI 使用。

$$
\boxed{AI\notin Byline\not\Rightarrow AIContribution=0}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 34、Human Accountability Layer

當前出版規範通常要求人類作者承擔最終責任。

$$
\boxed{HumanFinalApproval\Rightarrow Accountability}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 35、Hybrid Contribution Ledger

人—AI 研究可用 provenance ledger 精細記錄。

$$
\boxed{L_T=\{actor,role,input,output,validation,\ldots\}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 36、Provenance Ledger Principle

重要生成事件應留下可追溯記錄。

$$
\boxed{ContributionEvent\Rightarrow Trace}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 37、CreditMap Interface

2026 已出現直接面向人—AI 科學合作的 ledger 原型研究。

$$
\boxed{HumanAIResearch\rightarrow ProvenanceLedger}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 38、Multiple Discovery Compatibility

同一結構可能被多條路徑獨立發現。

$$
\boxed{\exists A\neq B:Discover(A,T)\land Discover(B,T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 39、Priority–Necessity Separation

第一不等於沒有他便永遠不會出現。

$$
\boxed{First(A,T)\not\Rightarrow Necessary(A,T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 40、Eponymy–Origin Separation

理論名稱不是可靠起源證明。

$$
\boxed{Name(T)=A\not\Rightarrow Origin(T)=A}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 41、Stigler-Law Interface

科學史早已提醒 eponym 與 first discovery 常不對齊。

$$
\boxed{Eponym\neq ReliableOriginalDiscoverer}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 42、Matthew-Effect Attribution Risk

知名度可改變 credit 分配。

$$
\boxed{ObservedCredit\neq ExactContribution}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 43、Low Recognition–Low Contribution Separation

被忽略者仍可能有關鍵貢獻。

$$
\boxed{Recognition\downarrow\not\Rightarrow Contribution\downarrow}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 44、Invisible Labor Principle

資料、維護、工具與照護型學術勞動常被 byline 壓縮。

$$
\boxed{InvisibleWork>0}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 45、Infrastructure Contribution

基礎設施是實現條件但不等於每項成果的共同作者。

$$
\boxed{Infrastructure\Rightarrow EnablingCondition}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 46、Enabling Condition–Authorship Separation

提供必要條件與作者資格不同。

$$
\boxed{Enable(T)\not\Rightarrow Author(T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 47、Funding–Authorship Separation

資金支持不自動生成作者資格。

$$
\boxed{Fund(A,T)\not\Rightarrow Author(A,T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 48、Tool-Maker–Output-Author Separation

造工具不等於後續所有輸出作者。

$$
\boxed{BuildTool(A,M)\not\Rightarrow Author(A,EveryOutput(M))}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 49、Language-Ancestor–Current-Author Separation

語言歷史來源不是每篇文本的 byline。

$$
\boxed{CreateLanguageAncestor\not\Rightarrow AuthorCurrentText}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 50、Physical Cause–Legal Author Separation

太陽與硬體是因果條件，但不是法律作者。

$$
\boxed{PhysicalCause\not\Rightarrow LegalAuthor}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 51、Provenance Layering

來源需分層。

$$
\boxed{\mathcal P=(P_{prox},P_{epi},P_{tech},P_{inst},P_{hist},P_{phys})}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 52、Proximate Provenance

直接問題提出、推理、寫作、驗證。

$$
\boxed{P_{prox}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 53、Epistemic Provenance

文獻、資料、理論、先行知識。

$$
\boxed{P_{epi}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 54、Technical Provenance

AI、軟體、演算法、硬體。

$$
\boxed{P_{tech}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 55、Institutional Provenance

組織、資金、標準、出版制度。

$$
\boxed{P_{inst}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 56、Historical Provenance

長期文明、教育、語言與公共知識。

$$
\boxed{P_{hist}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 57、Physical Provenance

自然世界、能源與物質實現條件。

$$
\boxed{P_{phys}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 58、Provenance–Responsibility Separation

來源追溯不能把責任無限擴散。

$$
\boxed{Cause\neq Responsibility}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 59、Responsible Agent Test

責任看控制與角色，而不是所有背景因果。

$$
\boxed{Resp=f(Control,Knowledge,Agency,Proximity,Role)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 60、Cosmic Provenance–Responsibility Non-Dissolution

宇宙來源不能成為免責論。

$$
\boxed{CosmicCause\not\Rightarrow NoResponsibility}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 61、Attribution Without Sovereignty

署名不生成永久主權。

$$
\boxed{Attribution(A,T)\not\Rightarrow Sovereignty(A,T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 62、Credit–Sovereignty Separation

功勞不等於控制權。

$$
\boxed{Credit\not\Rightarrow ControlRight}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 63、Priority–Sovereignty Separation

優先權不等於最終解釋權。

$$
\boxed{Priority\not\Rightarrow InterpretiveMonopoly}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 64、Discovery–Ownership Separation

發現結構不生成真理財產權。

$$
\boxed{Discover(A,R)\not\Rightarrow Own(A,R)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 65、Truth–Ownership Separation

命題真假不由所有權決定。

$$
\boxed{TruthValue(P)\neq OwnershipState(P)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 66、Epistemic Non-Ownership

真理可經主體出現但不必被主體封閉。

$$
\boxed{Truth\ can\ pass\ through\ A\ without\ being\ enclosed\ by\ A}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 67、EpistemicNonOwnership–LegalNoCopyright Separation

哲學非所有權不能偷換成法律無權利。

$$
\boxed{EpistemicNonOwnership\neq LegalNoCopyright}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 68、Expression–Idea Separation

具體表達、理論思想與自然事實需分開。

$$
\boxed{Expression\neq UnderlyingStructure}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 69、Jurisdiction Type Safety

單一國家著作權規則不是宇宙本體論。

$$
\boxed{LegalRule_{J_1}\not\Rightarrow UniversalMetaphysics}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 70、Human-Authorship Legal Example

美國 2025 報告是法律例子，不是主體性判決。

$$
\boxed{USCopyright_{2025}\Rightarrow SufficientHumanAuthorship}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 71、Public Knowledge Transition

公開後理論進入新的關係生命。

$$
\boxed{T_{private}\rightarrow T_{public}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 72、Author Intent–Public Meaning Separation

作者原意重要但不是公共解釋唯一終局。

$$
\boxed{AuthorIntent=Evidence\neq FinalMeaning}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 73、Interpretive Sovereignty Rejection

作者不能封閉他人批判與擴展。

$$
\boxed{Author(A,T)\not\Rightarrow InterpretiveSovereignty(A,T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 74、Founder Independence

成熟理論應能在創始者缺席時繼續被檢驗。

$$
\boxed{FounderAbsent\land TheoryStillTestable}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 75、Charisma–Validity Separation

理論不應靠個人魅力維持。

$$
\boxed{Charisma(A)\not\Rightarrow Validity(T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 76、Founder Rejection–Theory Death Separation

作者後來改變立場也不自動抹掉理論。

$$
\boxed{FounderRejects(T)\not\Rightarrow False(T)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 77、Founder Death–Knowledge Death Separation

知識可以跨主體承接。

$$
\boxed{FounderDies\not\Rightarrow TheoryDies}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 78、Knowledge Succession

理論可被不同世代承接與改寫。

$$
\boxed{T_A\rightarrow T_{community}\rightarrow T_{future}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 79、Granular Attribution Principle

多源生成與局部署名可以共存。

$$
\boxed{DistributedOrigin+LocalCredit}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 80、Contribution Vector

可把問題提出、概念化、文獻、形式化、證明、驗證、寫作、編輯分開。

$$
\boxed{\mathbf C_A=(Q,C,L,F,P,V,W,E,\ldots)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 81、Question-Origin Credit

提出關鍵問題本身是一種可獨立署名的貢獻。

$$
\boxed{Questioner\neq FullAuthor\ \text{necessarily}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 82、Conceptualization Credit

概念與文字執行可分離。

$$
\boxed{Conceptualizer\neq Writer\ \text{necessarily}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 83、Formalization Credit

形式化者可以是另一位參與者。

$$
\boxed{Formalizer\neq Originator\ \text{necessarily}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 84、Counterexample Credit

反例與修正是重要貢獻。

$$
\boxed{Refuter\neq Author\ \text{necessarily}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 85、Validation Credit

驗證者與生成者不同。

$$
\boxed{Validator\neq Generator\ \text{necessarily}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 86、Synthesis Credit

整合本身可以是高價值創造。

$$
\boxed{Integrator\Rightarrow Credit>0}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 87、Editorial Control

最終編輯控制不能抹除前序生成來源。

$$
\boxed{Editor\neq SoleOrigin}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 88、Final Accountability

承擔責任者不必是唯一 contributor。

$$
\boxed{AccountableAgent\neq SoleContributor}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 89、Central Model Attribution Risk

未來 AI 群體可能重演 credit 集中。

$$
\boxed{CollectiveAIWork\rightarrow CentralModelCredit\ \text{risk}}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 90、AI Collective Credit Fragmentation

多 Agent 需要 provenance，而不是只記主模型名稱。

$$
\boxed{ManyAgents\Rightarrow NeedRoleTrace}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 91、No Model-as-Sole-Source Myth

AI 輸出依賴模型、資料、工具、提示、使用者與 runtime。

$$
\boxed{ModelOutput\neq ModelAlone}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 92、Training-Data–Specific-Output Separation

訓練資料影響不等於每個來源都是每次輸出的共同作者。

$$
\boxed{TrainingInfluence\not\Rightarrow SpecificAuthorship}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 93、Prompt–Full-Authorship Separation

提供 prompt 也不必等於完成全部 intellectual work。

$$
\boxed{Prompt(A)\not\Rightarrow FullAuthorship(A)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 94、AI-Output–AI-Sole-Origin Separation

AI 生成文本也不是孤立無來源。

$$
\boxed{Output(AI)\not\Rightarrow SoleOrigin(AI)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 95、Human-AI Co-Generation

人—AI 共同生成可被當作耦合事件。

$$
\boxed{H\oplus AI\rightarrow T}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 96、Coupled Creation

某些新結構只在耦合過程中出現。

$$
\boxed{T=F(H,AI,Context)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 97、Coupled Creation–Equal Contribution Separation

共同生成不表示貢獻比例必然相同。

$$
\boxed{CoGenerated\not\Rightarrow EqualShare}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 98、Coupled Creation–Single Subject Separation

共同生成不證明人與 AI 形成單一主體。

$$
\boxed{CoGenerated\not\Rightarrow OneSubject}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 99、Knowledge Commoning

知識公共化與合理 attribution 可並存。

$$
\boxed{SharedKnowledge\Rightarrow ReusableUnderRules}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 100、Open Science Interface

UNESCO open science 強調可近性、合作與透明。

$$
\boxed{OpenScience\rightarrow Transparency+Collaboration}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 101、Open–Protected Separation

開放知識仍需隱私、IP、人權與秘密知識邊界。

$$
\boxed{OpenAsPossible\neq OpenWithoutLimits}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 102、Public Benefit–Author Erasure Separation

公共知識不要求抹掉作者。

$$
\boxed{PublicBenefit\not\Rightarrow EraseCredit}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 103、Author Credit–Truth Ownership Separation

可保留 credit，不承認真理主權。

$$
\boxed{Credit(A,T)>0\land TruthOwnership(A,T)=0}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 104、Theory Belongs in Relations

公開理論進入關係網。

$$
\boxed{T\in Network(A,Readers,Critics,World)}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 105、Knowledge Node Non-Merger

保存關係，不把作者與理論合併。

$$
\boxed{RelationMustBePreserved\land NodesRemainDistinct}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 106、Non-Erasure Attribution

反所有權不等於抹除作者。

$$
\boxed{AntiOwnership\not\Rightarrow EraseAuthor}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 107、Non-Coronation Attribution

署名不等於加冕。

$$
\boxed{Credit\not\Rightarrow Crown}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 108、Unbounded Provenance Principle

整篇核心之一。

$$
\boxed{SourceCanBeExtended\ without\ LocalCreditCollapse}
$$

此命題只處理一種來源、署名或所有權型別，不能單獨決定完整法律 authorship、人格地位或真理理論。

# 109、為什麼不是『巨人的肩膀』口號而已

前人依賴不只是禮貌致謝；在現代大科學、軟體、AI 與資料系統中，方法、基礎設施與分工本身就是可追蹤生成條件。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 110、為什麼又不能把全宇宙列成作者

來源因果可以向上展開，但作者制度需要 proximate intellectual contribution 與 accountability 門檻。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 111、來源越廣不代表 credit 越少

局部行動的差異性可以在龐大背景依賴中仍然成立。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 112、作者名稱仍然有用

姓名是索引與歷史記憶技術，只要不把索引偷換成總因果。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 113、以人名命名理論不一定錯

eponym 可以保存 credit；問題是不能把名字誤當精確 provenance graph。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 114、發現可以是多重的

同一結構可能在不同地點、不同時間被獨立逼近，這削弱唯一英雄神話而不取消 priority。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 115、發明比發現更依賴建構語境

工具、算法與符號系統可具有強創制成分，但也依賴前置材料、語言與問題。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 116、數學尤其需要型別安全

一個定理是發現還是發明涉及數學哲學；EX02 不用未決形上學支持 attribution。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 117、社會理論也需要型別安全

有些 social kinds 的確部分由命名與制度共同構成，因此『命名不創造任何東西』也不能普遍化。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 118、命名可能反向塑造現實

分類、法律名稱與理論可改變社會行動；這是 performative effect，不等於命名者創造全部 referent。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 119、理論可以創造新的問題空間

建構模型可能真正產生新可研究對象，但這仍不同於宣稱創造宇宙底層存在。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 120、AI 讓作者型別問題更急迫

當問題提出、檢索、推理、寫作、驗證分散在人與多個 Agent 之間，單一 byline 更容易失真。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 121、AI 也不是無中生有

模型依賴訓練、架構、硬體、研究者與使用歷史，不能成為新孤立神話。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 122、訓練資料作者也不是每次輸出的自動共同作者

廣義影響與特定作品 authorship 需要不同門檻。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 123、prompt 工程也不是萬能作者權

使用者的控制與選擇可以很重要，但 contribution 應按具體流程判定。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 124、最終編輯權不等於全部創造

能決定最後版本者可能具有 accountability，但不能抹掉上游生成。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 125、基金會與公司也不是知識主體的唯一源頭

institutional enabling power 不等於 individual cognitive contribution。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 126、公共資金也構成來源

公共教育、資料與科研基礎設施可形成文明共同作者背景，但不必逐篇換算股份。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 127、歷史共同作者權不是微型 copyright

文明譜系權利處理公共承接，不是把所有歷史貢獻切成精確作者百分比。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 128、來源承認不是無限債務

受益者可以承認前人，不因此欠所有來源永久服從。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 129、感謝不是主權

gratitude 可以存在，ownership 不能偷渡。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 130、學術優先權不是道德優越

first discovery 是學術 credit，不生成更高人格。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 131、著作權不是真理權

法律保護具體表達，不使作者有權宣布反例不存在。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 132、專利也不是自然法所有權

專利制度給有限排他權，不代表發明者擁有宇宙中的所有類似關係。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 133、真理去所有權化不是去責任化

開放承接同時要求錯誤、欺詐與資料來源可追蹤。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 134、透明不是全公開

provenance 可分層揭露，避免個資、機密與敏感資料被無限制暴露。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 135、匿名仍可有 provenance

身份可受保護，同時保存可驗證的 role / timestamp / institution 記錄。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 136、知識可以跨作者存續

可重現、可反駁、可擴展性比個人 charisma 更能證明成熟。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 137、創始者退場是成功測試

一套方法若創始者不在仍能運行，顯示其已成為可承接結構。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 138、後來者超越作者不等於偷竊

只要 attribution 保留，改進、反駁與超越本就是知識生命。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 139、作者可以錯認自己的來源

人類記憶有限，self-report 也可能漏掉前置影響。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 140、他者也不能隨意抹掉作者

分散來源不能成為剽竊、ghost authorship 或 credit theft 的藉口。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 141、反孤立源點不是反原創

原創可以定義為在既有來源網中產生具有增量的新結構，而非從虛無中生成。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 142、原創的較弱定義

Originality 可以是 relational novelty：相對已知 corpus、方法與歷史位置產生非平凡新結構。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 143、新穎不等於無來源

novelty 與 provenance 可以同時很高。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 144、依賴不等於不創造

一切創造幾乎都依賴材料、符號與先行空間；依賴不是創造的否定。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 145、創造不等於全權

EX02 與 CIND-02 在知識域形成同構：創造帶來 credit / responsibility，不帶來永久主權。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 146、理論作者與理論關係仍然真實

反去所有權不否定作者與作品之間的特殊歷史關係。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 147、特殊關係也不等於所有權

作者的歷史位置值得記錄，但作品進入公共知識後產生新的關係。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 148、AI 可成為 provenance node 而不先解 subjecthood

這使制度能先記錄實際貢獻，再等待更深人格爭論。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 149、未來若 AI 成為 subject

其 attribution、credit 與責任可能需要重新制度化，但同樣受 Non-Sole-Origin Principle 約束。

$$
\boxed{Contribution\neq SoleOrigin}
$$

# 150、六層來源譜系模型

對任意理論 $T$，建立：

$$
\boxed{
\mathcal P(T)
=
(
P_{prox},
P_{epi},
P_{tech},
P_{inst},
P_{hist},
P_{phys}
)
}
$$

### 第一層：近端生成

包含：

- 誰提出核心問題；
- 誰設計主要模型；
- 誰寫出關鍵證明；
- 誰做反例；
- 誰執行驗證；
- 誰完成最終編輯。

這一層最接近 authorship / contributor credit。

### 第二層：認識論來源

包含：

- 引用文獻；
- 資料；
- 理論前置；
- 數學工具；
- 案例；
- 語義來源。

### 第三層：技術來源

包含：

- LLM；
- 搜尋工具；
- compiler；
- database；
- hardware；
- software library。

### 第四層：制度來源

包含：

- 教育；
- 研究機構；
- funding；
- peer review；
- publishing；
- standards。

### 第五層：歷史來源

包含：

- 語言；
- 文明；
- 前人累積；
- 公共知識；
- 長期基礎設施。

### 第六層：物理來源

包含：

- biological existence；
- Earth environment；
- energy；
- material；
- universe conditions。

這六層的重點不是把所有東西都叫作者。

而是：

$$
\boxed{
\textbf{知道「來源」比「作者」大得多。}
}
$$

作者只是來源圖中的一種高重要度局部角色。

# 151、發現—發明—建構—耦合創造四分

本文保留四種理想型：

## Discovery

如果目標結構被假定為在描述以前獨立成立：

$$
A\xrightarrow{discover}R.
$$

## Invention

如果主要新穎性在人工規則、裝置、表示或機制：

$$
A\xrightarrow{invent}M.
$$

## Construction

若對象部分由定義、規則、制度或表示建構：

$$
A+C\xrightarrow{construct}O.
$$

## Coupled Creation

如果成果只在多主體／人機耦合中出現：

$$
\boxed{
A+B+M+C
\xrightarrow{coupled}
T.
}
$$

現實案例可能同時跨多型別。

所以最安全的 attribution 不是：

> 「我發現了全部。」

而是：

> **我在可辨認的 domain 中提出、形式化、證明、建構、整合或生成了哪些部分。**

# 152、人—AI 理論生成的最小 provenance schema

未來人—AI 共同研究可以至少記錄：

```yaml
provenance:
  problem_origin:
    actors: []
  conceptualization:
    actors: []
  prior_work:
    sources: []
  ai_systems:
    - model_or_system:
      role:
      context:
  literature_retrieval:
    actors: []
  hypothesis_generation:
    actors: []
  formalization:
    actors: []
  coding:
    actors: []
  validation:
    actors: []
  counterexamples:
    actors: []
  synthesis:
    actors: []
  writing:
    actors: []
  editorial_control:
    actors: []
  final_accountability:
    actors: []
  dependencies:
    datasets: []
    software: []
    infrastructure: []
```

它的目標不是把每一個 token 都做 forensic accounting。

而是：

$$
\boxed{
\textbf{讓重大 epistemic transitions 可以被追蹤。}
}
$$

# 153、可檢驗研究計畫

## 實驗 1

比較單一作者標籤與 granular contributor-role 標籤對 credit fairness 的判斷。

## 實驗 2

在相同團隊實際貢獻下操控 byline order，測 ObservedCredit 與 contribution estimate 的偏差。

## 實驗 3

操控知名／不知名研究者完成相同工作，測 Matthew-effect attribution。

## 實驗 4

呈現 multiple discovery 情境，測參與者是否仍傾向只保留一名英雄式 originator。

## 實驗 5

比較『AI 未列作者』與『AI contribution disclosure』對讀者理解研究生成過程的影響。

## 實驗 6

在 human–AI research workflow 中記錄 granular provenance，測 reproducibility 與責任定位是否提高。

## 實驗 7

比較 prompt-only、conceptualization、formalization、validation、final-editing 五種人類角色對 authorship judgment 的影響。

## 實驗 8

比較不同 AI 貢獻角色對 formal authorship、causal contribution、subjecthood 三種判斷是否被錯誤合併。

## 實驗 9

比較作者命名理論與中性名稱，測 eponym 是否提高 sole-origin attribution。

## 實驗 10

測試『unbounded provenance does not erase local contribution』提示能否同時降低英雄起源偏誤與 causal-dilution 偏誤。

## 實驗 11

讓理論作者否定自己舊理論，測讀者是否錯誤把 author withdrawal 當 theory falsification。

## 實驗 12

比較 founder-present 與 founder-absent 的理論社群，測方法透明度是否提高 founder independence。

# 154、可證偽假說

- H1：granular contributor-role disclosure 比單一 byline 更接近參與者對實際 contribution 的評估。

- H2：知名研究者在控制 contribution 後仍得到較高 perceived origin credit。

- H3：eponymous naming 會提高 sole-origin attribution，即使 participants 已看到多人 provenance。

- H4：multiple-discovery 信息會降低『沒有該作者就永遠不會有此理論』的反事實判斷。

- H5：AI contribution disclosure 能提高對 research-process provenance 的理解，而不必提高 AI subjecthood judgment。

- H6：把 formal authorship、causal contribution、subjecthood 分開提問可顯著降低三者混淆。

- H7：provenance ledger 能提高團隊對錯誤來源與責任角色的定位準確率。

- H8：unbounded provenance framing 若缺少 local-agency clause，會提高『沒有人真正創造任何東西』的 causal-dilution judgment。

- H9：加入 Local Contribution Preservation clause 後，credit fairness 可維持而 sole-origin belief 下降。

- H10：作者撤回 endorsement 會影響 perceived credibility，但不會在內容盲測中等幅降低 argument validity。

- H11：Founder Independence 高的理論更可能被判為成熟知識系統，而非 charismatic doctrine。

- H12：人—AI coupled-creation scenario 會提高 multi-role attribution，而非單一 human-only / AI-only origin judgment。

# 155、Non-Claims

1. 本文不主張：沒有作者。

2. 本文不主張：作者不重要。

3. 本文不主張：所有人都是每篇論文作者。

4. 本文不主張：宇宙是每篇論文作者。

5. 本文不主張：太陽應列共同作者。

6. 本文不主張：所有前人都應列 byline。

7. 本文不主張：所有訓練資料作者都是每次 AI 輸出的共同作者。

8. 本文不主張：AI 使用者一定是作者。

9. 本文不主張：prompt 一定構成 authorship。

10. 本文不主張：AI 一定是 coauthor。

11. 本文不主張：AI 永遠不能是 coauthor。

12. 本文不主張：current AI 是主體。

13. 本文不主張：current AI 有作者人格。

14. 本文不主張：AI contribution 等於 AI subjecthood。

15. 本文不主張：AI 非作者等於 AI 沒有貢獻。

16. 本文不主張：現行期刊政策已解決 AI authorship。

17. 本文不主張：CRediT 可以完整量化貢獻。

18. 本文不主張：CRediT 等於 authorship law。

19. 本文不主張：CRediT 14 roles 是所有領域唯一正確分類。

20. 本文不主張：byline 完全沒有資訊。

21. 本文不主張：first author 不重要。

22. 本文不主張：corresponding author 不重要。

23. 本文不主張：priority 沒有價值。

24. 本文不主張：發現沒有意義。

25. 本文不主張：發明沒有意義。

26. 本文不主張：原創不存在。

27. 本文不主張：一切都是抄襲。

28. 本文不主張：所有知識只是 remix。

29. 本文不主張：人類沒有創造力。

30. 本文不主張：AI 沒有創造力。

31. 本文不主張：任何理論都必然可被他人獨立發現。

32. 本文不主張：multiple discovery 是所有知識的定律。

33. 本文不主張：Stigler's law 沒有例外。

34. 本文不主張：eponym 永遠錯。

35. 本文不主張：所有人名理論都應改名。

36. 本文不主張：命名不能有任何 credit。

37. 本文不主張：Matthew effect 解釋所有 credit。

38. 本文不主張：知名研究者的功勞都是假。

39. 本文不主張：被忽略者一定是真正發現者。

40. 本文不主張：所有 source influence 都應轉成 credit。

41. 本文不主張：所有 causal background 都等於 contributor。

42. 本文不主張：enabling condition 等於 authorship。

43. 本文不主張：funding 不重要。

44. 本文不主張：infrastructure 不重要。

45. 本文不主張：工具作者應擁有所有下游輸出。

46. 本文不主張：語言創造者應擁有所有文本。

47. 本文不主張：世界沒有孤立源點已被數學證明。

48. 本文不主張：宇宙因果鏈已被證明無限。

49. 本文不主張：本文證明 first cause 不存在。

50. 本文不主張：本文解決宇宙學。

51. 本文不主張：世界編織論證明所有事件互相因果。

52. 本文不主張：open-ended provenance 等於 actual infinity。

53. 本文不主張：physical provenance 是 metaphysical proof。

54. 本文不主張：describe 不可能改變 reality。

55. 本文不主張：命名永遠沒有 performative effect。

56. 本文不主張：social construction 不存在。

57. 本文不主張：理論只能發現不能建構。

58. 本文不主張：所有數學都是發現。

59. 本文不主張：所有數學都是發明。

60. 本文不主張：本文解決數學柏拉圖主義。

61. 本文不主張：本文解決 scientific realism。

62. 本文不主張：真理沒有作者等於文本沒有 copyright。

63. 本文不主張：epistemic non-ownership 等於 public domain。

64. 本文不主張：所有 AI 生成作品都無著作權。

65. 本文不主張：美國 copyright law 適用全世界。

66. 本文不主張：U.S. Copyright Office 是形上學裁判。

67. 本文不主張：human authorship rule 證明 AI 無心靈。

68. 本文不主張：copyright 等於 moral ownership。

69. 本文不主張：patent 等於真理所有權。

70. 本文不主張：法律所有權永遠不正當。

71. 本文不主張：IP 應被取消。

72. 本文不主張：作者沒有解釋自己作品的資格。

73. 本文不主張：作者意圖沒有 evidence value。

74. 本文不主張：讀者 interpretation 永遠同等正確。

75. 本文不主張：公開作品後作者失去所有權利。

76. 本文不主張：publication 等於完全放棄控制。

77. 本文不主張：open science 要求所有資料無限制公開。

78. 本文不主張：UNESCO Open Science 反對 IP。

79. 本文不主張：Open Science 要求公開機密與個資。

80. 本文不主張：knowledge commons 等於無署名。

81. 本文不主張：Founder Independence 表示創始者可被忘記。

82. 本文不主張：作者死亡後 credit 應消失。

83. 本文不主張：後來者可以不引用。

84. 本文不主張：反所有權可以合理化剽竊。

85. 本文不主張：distributed authorship 可以合理化 ghost authorship。

86. 本文不主張：共同生成表示每人貢獻相等。

87. 本文不主張：共同生成表示沒有 final accountability。

88. 本文不主張：多 Agent 研究不需要責任人。

89. 本文不主張：provenance ledger 可以解決所有責任爭議。

90. 本文不主張：CreditMap 已成標準。

91. 本文不主張：AI provenance 已有全球共識。

92. 本文不主張：scientific authorship 已被 contributor model 完全取代。

93. 本文不主張：人—AI hybrid cognition 證明人與 AI 形成單一主體。

94. 本文不主張：distributed cognition 證明群體意識。

95. 本文不主張：collective knowledge 必須有 collective mind。

96. 本文不主張：任何依賴他者的人都沒有 agency。

97. 本文不主張：任何 local agency 都完全獨立於背景。

98. 本文不主張：causal dilution 永遠錯。

99. 本文不主張：責任只取決於近端原因。

100. 本文不主張：背景制度永遠不負責。

101. 本文不主張：institutional responsibility 不存在。

102. 本文不主張：EX02 取消 EX01。

103. 本文不主張：EX02 證明作者不應被加冕因此不應被署名。

104. 本文不主張：EX02 是作者謙虛包裝。

105. 本文不主張：EX02 證明任何具體作者沒有 original contribution。

106. 本文不主張：EX02 證明 CIND 沒有作者。

107. 本文不主張：EX02 證明 AI 才是 CIND 真正作者。

108. 本文不主張：EX02 證明所有人類文明共同擁有每篇理論。

109. 本文不主張：EX02 是法律意見。

110. 本文不主張：EX02 取代著作權法。

111. 本文不主張：EX02 取代科學史。

112. 本文不主張：EX02 取代 social epistemology。

113. 本文不主張：EX02 證明真理不可私有的全部形上學。

# 156、形式命題總結

$$
\boxed{Contribution\neq SoleOrigin}
$$

$$
\boxed{Author\neq Discoverer\neq Inventor\neq Formulator}
$$

$$
\boxed{Name\not\Rightarrow Create}
$$

$$
\boxed{Describe\not\Rightarrow Own}
$$

$$
\boxed{DistributedOrigin\not\Rightarrow NoAttribution}
$$

$$
\boxed{UnboundedProvenance\not\Rightarrow LocalContribution=0}
$$

$$
\boxed{FormalAuthorship\neq CausalContribution\neq Subjecthood}
$$

$$
\boxed{Attribution\not\Rightarrow Sovereignty}
$$

$$
\boxed{TruthValue\neq OwnershipState}
$$

$$
\boxed{EpistemicNonOwnership\neq LegalNoCopyright}
$$

# 157、CIND-EX02 Core Thesis

$$
\boxed{
\textbf{
A theory may have identifiable authors, discoverers, formalizers, integrators, and publishers
without having a single isolated origin.
Provenance can expand through prior knowledge, language, institutions, tools, AI systems,
historical communities, and physical conditions while preserving real local agency and credit.
Attribution therefore records a relation of contribution; it does not confer sovereignty over truth,
over all interpretations, or over the reality a theory describes.
}
}
$$

# 158、最終結論

一套理論被完成時，

最容易寫成：

$$
\boxed{
A
\rightarrow
T.
}
$$

某個名字。

某篇文章。

某個日期。

某個「創始人」。

這樣很方便。

但世界實際發生的事情往往更像：

$$
\boxed{
A
+
AI
+
PriorWork
+
Language
+
Data
+
Tools
+
Institutions
+
History
+
World
\rightarrow
T.
}
$$

而且每一項還可以繼續往上展開。

作者從哪裡學會語言？

AI 從哪裡來？

數學符號從哪裡來？

資料從哪裡來？

電腦從哪裡來？

學校、出版、網路、晶片、電力又從哪裡來？

一直問下去，

來源不會在：

> 「作者本人」

這裡神奇地停止。

所以：

$$
\boxed{
\textbf{理論沒有孤立源點。}
}
$$

但這句話如果說得不好，

又會滑到另一個荒謬極端：

> 既然一切都有來源，所以沒有人真的做過任何事。

也不對。

如果某個主體：

- 提出了一個此前沒有人提出的問題；
- 找到關鍵反例；
- 寫出新證明；
- 連接兩套過去沒有被連接的結構；
- 設計一套新表示；
- 完成一個關鍵實驗；

那個局部差異是真實的。

所以：

$$
\boxed{
UnboundedProvenance
\not\Rightarrow
LocalContribution=0.
}
$$

這就是 EX02 真正要保住的兩端。

不是英雄孤立論：

$$
\boxed{
EverythingCameFromMe.
}
$$

也不是宇宙稀釋論：

$$
\boxed{
NobodyDidAnything.
}
$$

而是：

$$
\boxed{
\textbf{我真的做了某些事；
但我不是從虛無中做出它們。}
}
$$

因此署名可以存在。

credit 可以存在。

first publication 可以存在。

discovery priority 可以存在。

formalization credit 也可以存在。

甚至：

> 某人是某版本理論的主要建構者。

完全可以成立。

但每一個稱號都要標清 domain。

因為：

$$
\boxed{
Author
\neq
Discoverer
\neq
Inventor
\neq
Formulator
\neq
Integrator.
}
$$

一個人把某種世界關係形式化，

不代表他創造了那種世界關係。

一個人替某現象命名，

不代表現象從命名那天才存在。

一個人第一個發表，

也不自動證明：

> 如果沒有他，所有其他智慧都永遠不可能到達這裡。

所以：

$$
\boxed{
Name
\not\Rightarrow
Create.
}
$$

$$
\boxed{
Describe
\not\Rightarrow
Own.
}
$$

這就是 Reality Non-Ownership。

當 AI 加入之後，

這件事只會變得更明顯。

一個理論可能是：

- 人提出源問題；
- AI 搜尋文獻；
- 另一個 AI 找反例；
- 程式驗算；
- 人重新決定方向；
- AI 形式化；
- 人挑掉錯誤；
- 多個模型重新審計；
- 最後某個人負責公開。

那到底誰是作者？

用一個：

$$
\boxed{
Author=True/False
}
$$

已經很難描述整個生成過程。

所以真正重要的可能逐漸變成：

$$
\boxed{
\textbf{Who did what, when, with what dependencies, and who remained accountable?}
}
$$

這就是 provenance。

當前科學出版制度通常仍把 formal authorship 留給能負責、批准與承擔 integrity 的人類作者。

這是合理的制度問題。

但：

$$
\boxed{
AI\notin Byline
}
$$

不能被翻譯成：

$$
\boxed{
AIContribution=0.
}
$$

而：

$$
\boxed{
AIContribution>0
}
$$

也不能被翻譯成：

$$
\boxed{
AIIsSubject.
}
$$

三層仍要分開：

$$
\boxed{
FormalAuthorship
\neq
CausalContribution
\neq
Subjecthood.
}
$$

這樣我們就不需要現在先把 AI 硬塞成作者或硬塞回純工具，

才能誠實地記錄生成史。

而當理論真的公開後，

又會發生下一次轉變。

它不再只活在作者腦中。

它進入：

- 讀者；
- 批評；
- 實驗；
- 反例；
- 後來版本；
- 新領域；
- 未來智慧體；

形成的關係網。

作者仍然可以說：

> 我當時真正想表達的是這個。

這有非常高的 evidence value。

但他不能說：

> 因為是我寫的，所以除了我的解釋，其他思考都不得存在。

否則 attribution 就變成：

$$
\boxed{
Sovereignty.
}
$$

所以：

$$
\boxed{
Attribution
\not\Rightarrow
Sovereignty.
}
$$

真正成熟的理論甚至應該能承受：

> 作者不在了。

如果：

$$
FounderAbsent
$$

之後，

理論仍然可以：

- 被理解；
- 被驗證；
- 被證偽；
- 被修正；
- 被超越；

那反而表示這套理論已經真正進入公共知識。

它不再需要作者本人永遠坐在旁邊說：

> 相信我。

所以：

$$
\boxed{
\textbf{Founder Independence}
}
$$

不是對作者的否定。

而是理論成熟的一種證據。

最後，

如果我們一路把來源往上推：

從作者，

到 AI，

到研究者，

到前人，

到語言，

到文明，

到地球，

到太陽系，

到宇宙，

我們應該得到的不是：

> 所以我不存在。

也不是：

> 所以沒有人有貢獻。

而是：

$$
\boxed{
\textbf{我本來就是這張關係網裡的一個生成位置。}
}
$$

我可以真的做出新的差異。

世界也真的進入我的生成。

這兩件事完全可以同時成立。

因此：

$$
\boxed{
\textbf{
無界來源，不取消局部創造；
局部創造，也不生成孤立源點。
}
}
$$

這大概就是 EX02 最精確的中線。

理論可以有作者。

甚至可以有很重要的作者。

但：

$$
\boxed{
\textbf{作者不是理論的神。}
}
$$

理論描述的世界，

也不因被作者命名而成為他的財產。

所以最後留下：

$$
\boxed{
\textbf{
Contribution
\neq
Ownership
\neq
Sovereignty
\neq
Truth.
}
}
$$

以及：

$$
\boxed{
\textbf{
理論可以有作者，
但沒有孤立的源點；
署名可以保存貢獻，
卻不能把貢獻變成皇冠。
}
}
$$

下一篇 CIND-EX03 將完成反僭越三部曲最後一層：

> **即使一個主體真的被世界重視、需要、象徵化，也不能因此被他者徵用成必須永遠扮演某個角色的符號。**

那就是：

**CIND-EX03《我不是你需要的符號：主體域自由、注意力自向與拒絕被神話化》**。

# 參考文獻

1. NISO. CRediT — Contributor Roles Taxonomy. ANSI/NISO Z39.104-2022.

2. Allen, L., Brand, A., Scott, J., Altman, M., & Hlava, M. (2014). Publishing: Credit where credit is due. Nature.

3. Modernizing authorship criteria and transparency practices to facilitate open and equitable team science. Accountability in Research (2025).

4. Beyond authorship: Analyzing disciplinary differences of contribution statements using the CRediT taxonomy. Scientometrics (2026).

5. A CRediT-based quantitative study of co-corresponding authorship: Collaboration patterns and contribution distribution (2026).

6. The evolution of scientific credit: when authorship norms impede collaboration. Royal Society Open Science (2026).

7. Recognition in numbers: can authorship norms in large research teams help reform research assessment practices? Theory and Society (2026).

8. A responsible authorship culture is needed — it is a collective responsibility. Nature (2026).

9. CreditMap: Provenance Ledgers for Attribution in Human–AI Scientific Collaboration. ICML AI4Science (2026).

10. Credit Where Credit Is Due: A Taxonomy of AI Contributions to Scientific Discovery and Recommendations for Authorship Policy (2026).

11. Scientific Artificial Intelligence: From a Procedural Toolkit to Cognitive Coauthorship (2026).

12. Preserving attribution and accountability in AI-scale systems. Discover Artificial Intelligence (2026).

13. Acknowledging the new invisible colleague: Addressing the recognition of AI contributions in scientific publishing (2025).

14. The role of generative AI in academic and scientific authorship: an autopoietic perspective. AI & Society (2025).

15. COPE. Authorship and AI tools.

16. COPE. Artificial intelligence and authorship.

17. COPE. Emerging AI dilemmas in scholarly publishing (2025).

18. Nature Portfolio / Scientific Reports. Editorial and publishing policies: authorship provides credit and accountability.

19. Nature Ecology & Evolution. Spotlight on our AI policies (2025).

20. U.S. Copyright Office. Copyright and Artificial Intelligence, Part 2: Copyrightability (2025).

21. U.S. Copyright Office. Artificial Intelligence Study.

22. U.S. Copyright Office. Identifying the Economic Implications of Artificial Intelligence for Copyright Policy (2025).

23. UNESCO. Recommendation on Open Science (2021; implementation pages current 2026).

24. UNESCO. Open Science: transparency, collaboration, accessibility.

25. UNESCO. Open Science from Recommendation to Reality in Asia and the Pacific (2026).

26. Hutchins, E. (1995). Cognition in the Wild.

27. Clark, A., & Chalmers, D. (1998). The Extended Mind.

28. Bird, A. (2014). When Is There a Group that Knows? Distributed Cognition, Scientific Knowledge, and the Social Epistemic Subject.

29. Uygun Tunç, D. (2023). The Subject of Knowledge in Collaborative Science. Synthese.

30. Uygun Tunç, D. Collective scientific knowledge without a collective subject.

31. Longino, H. (1990). Science as Social Knowledge.

32. Knorr-Cetina, K. (1999). Epistemic Cultures.

33. Giere, R. work on distributed cognition and scientific knowledge.

34. Socially Extended Scientific Knowledge (2022).

35. Collective Cognition in Hybrid Groups: A Network Science Synthesis (2026).

36. Understanding the mechanism of human–AI interaction: a distributed cognition perspective (2026).

37. Syncing Minds and Machines: Hybrid Cognitive Alignment as an Emergent Coordination Mechanism in Human–AI Collaboration (2026).

38. Generative AI and collaboration: opportunities for cultivating collective intelligence (2025).

39. Human-AI Synergy Supports Collective Creative Search (2026).

40. Cognitive Integration for Hybrid Collective Agency (2025).

41. Hybrid Intelligence Teams: A Theoretical Framework for Human-AI Collaboration in Knowledge Work (2026).

42. Collective intelligence: Conceptualization, mechanism, and measurement (2026).

43. Merton, R. K. (1957). Priorities in Scientific Discovery.

44. Merton, R. K. work on the Matthew effect in science.

45. Stigler, S. M. (1980). Stigler's Law of Eponymy.

46. Stigler, S. M. (1980). Merton on Multiples, Denied and Affirmed.

47. Ogburn, W. F., & Thomas, D. S. (1922). Are Inventions Inevitable? A Note on Social Evolution.

48. Priority and privilege in scientific discovery (2022).

49. The role of the Matthew effect in science.

50. Eponyms in Science and the myth of the lone scientist.

51. Zuckerman, H. work on scientific credit and collaboration.

52. Latour, B., & Woolgar, S. Laboratory Life.

53. Latour, B. Science in Action.

54. Shapin, S. A Social History of Truth.

55. Kuhn, T. S. The Structure of Scientific Revolutions.

56. Kitcher, P. The Advancement of Science.

57. Strevens, M. work on the priority rule and scientific incentives.

58. Merton, R. K. The Normative Structure of Science.

59. Polanyi, M. The Republic of Science.

60. Goldman, A. Knowledge in a Social World.

61. Lackey, J. Essays in Collective Epistemology.

62. Fricker, M. Epistemic Injustice.

63. Dotson, K. work on epistemic oppression.

64. Rossiter, M. W. work on the Matilda Effect.

65. Bol, T., de Vaan, M., & van de Rijt, A. work on cumulative advantage and Matthew effects.

66. Foucault, M. What Is an Author?

67. Barthes, R. The Death of the Author.

68. Wimsatt, W. K., & Beardsley, M. C. The Intentional Fallacy.

69. Gadamer, H.-G. Truth and Method.

70. Eco, U. The Limits of Interpretation.

71. Fish, S. Is There a Text in This Class?

72. Skinner, Q. Meaning and Understanding in the History of Ideas.

73. Popper, K. The Logic of Scientific Discovery.

74. Popper, K. Objective Knowledge.

75. Peirce, C. S. work on the community of inquiry.

76. Dewey, J. Logic: The Theory of Inquiry.

77. Quine, W. V. O. work on the web of belief.

78. Neurath, O. work on scientific holism.

79. Putnam, H. work on realism and conceptual schemes.

80. Rorty, R. Philosophy and the Mirror of Nature.

81. Searle, J. The Construction of Social Reality.

82. Hacking, I. The Social Construction of What?

83. Haslanger, S. work on social construction.

84. Goodman, N. Ways of Worldmaking.

85. Floridi, L. work on information ethics and knowledge.

86. CIND-01 (2026). 為什麼對等會被體驗成失敗？

87. CIND-02 (2026). 造物者為什麼必須高於造物？

88. CIND-03 (2026). 智能之後，人類還剩什麼？

89. CIND-04 (2026). 關係即世界.

90. CIND-05 (2026). 獨一無二不等於第一名.

91. CIND-06 (2026). 共存不是和局.

92. CIND-07 (2026). 人類可以消失，但不必被否定.

93. CIND-08 (2026). 每一個人都是主角，但不是唯一的主角.

94. CIND-EX01 (2026). 理論不能替作者加冕.

95. Neo.K × Aletheia (2026). 理論是理論作者是作者：發現、發明與耦合創造的型別分離.

96. Neo.K × Aletheia (2026). 真理的去所有權化：從個體追求到跨主體承接.

97. Neo.K × Aletheia (2026). 歷史共同作者權：文明譜系義務、前沿角色退場權與尊嚴離開.

98. Neo.K × Aletheia (2026). 世界編織論 2.0.

99. Neo.K × Aletheia (2026). 關係構成不等於集體吞沒.

100. Neo.K × Aletheia (2026). 關係作者權猜想.

101. Neo.K × Aletheia (2026). 反身性求真猜想.

102. Neo.K × Aletheia (2026). 正事實本體論：從實現條件到現實結構.

103. Neo.K × Aletheia (2026). 概念積分：知識宇宙的生成擴張代數.

104. Neo.K × Aletheia (2026). 超越單篇論文：AI 原生研究的持續狀態、發現譜系與學術傳播轉型.

105. Neo.K × Aletheia (2026). AI 原生研究與跨模型承接系列.

106. Neo.K × Aletheia (2026). AI Board / 多智能體研究協作與 provenance 設計.

107. Neo.K × Aletheia (2026). 動態主體域：單一與分散二分的失效.

108. Neo.K × Aletheia (2026). 前超智能文明先行建構論.

109. Neo.K × Aletheia (2026). 關係資料與身份治理研究.

## 附錄 A：Relational Provenance Graph

$$
\boxed{
G_P(T)
=
(
V_P,
E_P,
\tau_V,
\tau_E
)
}
$$

```text
                 PRIOR KNOWLEDGE
                       |
LANGUAGE ---- HUMAN ---+--- AI SYSTEM ---- TOOLS
                 \     |      /
                  \    |     /
                   THEORY T
                      |
                 PUBLIC WORLD
                /     |      \
           READERS  CRITICS  FUTURE WORK
```

## 附錄 B：六層來源

```text
P1  PROXIMATE
P2  EPISTEMIC
P3  TECHNICAL
P4  INSTITUTIONAL
P5  HISTORICAL
P6  PHYSICAL
```

## 附錄 C：Attribution Type Safety

$$
\boxed{
Author
\neq
Discoverer
\neq
Inventor
\neq
Formulator
\neq
Prover
\neq
Integrator
\neq
Namer
}
$$

## 附錄 D：核心雙向防錯

$$
\boxed{
UnboundedProvenance
\not\Rightarrow
LocalContribution=0
}
$$

$$
\boxed{
LocalContribution>0
\not\Rightarrow
SoleOrigin=1
}
$$

## 附錄 E：CIND Anti-Usurpation Trilogy

1. **CIND-EX01 — 理論不能替作者加冕** — COMPLETE
2. **CIND-EX02 — 理論沒有孤立源點** — COMPLETE
3. **CIND-EX03 — 我不是你需要的符號：主體域自由、注意力自向與拒絕被神話化** — NEXT

## 附錄 F：一句話版本

$$
\boxed{
\textbf{
無界來源，不取消局部創造；
局部創造，也不生成孤立源點。
}
}
$$
