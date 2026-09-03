# ALD-07｜Juridical Routing：分散式 AI 的跨法域選擇與法律路由
## Juridical Routing: Cross-Jurisdiction Selection and Legal Routing for Distributed AI

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 07 篇 / 10  
**前篇：** ALD-06〈活的判例圖：AI 原生先例、異議、推翻與法律推理網路〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／AI 法律域／國際私法接口／Juridical Routing／跨境 AI 治理  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

ALD-01 至 ALD-06 已依序建立 AI Legal Domain、載體相對法律本體、非 Boolean 法律算子、多速度規範版本、AI 共同立法與活的判例圖。所有前篇在形式上都反覆使用一個索引：

$$
J.
$$

然而，對分布式 AI 而言，「它在哪個 jurisdiction？」通常不是一個可由單一國家名稱回答的問題。某一 AI Agent 可以由台灣公司擁有、在日本機器人上具身、於美國雲端推理、處理歐盟自然人的個資、接受新加坡使用者委任、依英國法成立的契約付款，並在另一國造成實際損害。此時：

$$
\boxed{
\text{AI Location}
\neq
\text{Single Jurisdiction}.
}
$$

本文提出 Juridical Routing Framework（JRF，法律路由框架）的第一版。其第一個核心修正是：**「jurisdiction」本身必須分型。** 國際與跨境法律分析至少應區分：

$$
\boxed{
\text{Regulatory Scope}
\neq
\text{Adjudicatory Jurisdiction}
\neq
\text{Applicable Law}
\neq
\text{Recognition / Enforcement}.
}
$$

EU AI Act Article 2 與 GDPR Article 3 處理的是各自規範的 territorial / material reach；Brussels I bis 處理特定民商事爭議中哪些法院具有 jurisdiction；Rome I 與 Rome II 分別處理 contractual 與 non-contractual obligations 的 applicable law；跨境判決最終還可能涉及 recognition and enforcement。若 AI Legal Runtime 只保存：

```text
jurisdiction = EU
```

就會把四種不同法律問題混成一個欄位。

本文第二個核心結構是 Jurisdictional Anchor Vector：

$$
\boxed{
\mathbf J_A(e)
=
(
J_{\mathrm{compute}},
J_{\mathrm{entity}},
J_{\mathrm{control}},
J_{\mathrm{user}},
J_{\mathrm{data}},
J_{\mathrm{effect}},
J_{\mathrm{contract}},
J_{\mathrm{asset}},
J_{\mathrm{embodiment}},
J_{\mathrm{lineage}}
).
}
$$

其中每一分量都只是 candidate connecting factor，不自動等於最終 forum 或 applicable law。這一設計延續 ALD-02 已提出的 AI residence vector，並把「位置」從單一地點提升成法律事件的多錨點集合。

本文第三個核心貢獻是 Issue-by-Issue Routing。跨境 AI 事件不應只得到一個「適用法」，而應先拆成多個 legal issues：

$$
\boxed{
e
\rightarrow
\{
q_1,q_2,\ldots,q_n
\}.
}
$$

例如同一 Agent 交易可能同時產生：

- contract formation；
- delegation validity；
- data protection；
- AI regulatory compliance；
- tort liability；
- asset ownership；
- identity succession；
- procedural forum。

不同 issue 可以由不同 routing rule 決定。故：

$$
\boxed{
\text{One Event}
\not\Rightarrow
\text{One Governing Law}.
}
$$

本文提出 Juridical Route：

$$
\boxed{
\mathfrak R_J(q)
=
(
\mathcal J_{\mathrm{scope}},
\mathcal J_{\mathrm{forum}},
\mathcal L_{\mathrm{app}},
\mathcal J_{\mathrm{enforce}},
\mathcal M,
\mathcal C,
\mathcal U
).
}
$$

其中：

- $\mathcal J_{\mathrm{scope}}$：可能適用的監管法域／強制性規範集合；
- $\mathcal J_{\mathrm{forum}}$：有權受理的 forum candidates；
- $\mathcal L_{\mathrm{app}}$：該 issue 的 applicable law；
- $\mathcal J_{\mathrm{enforce}}$：承認／執行相關法域；
- $\mathcal M$：mandatory rules / public policy constraints；
- $\mathcal C$：conflict / choice-of-law constraints；
- $\mathcal U$：unresolved routing states。

Routing 的輸出因此不是一個 country code，而是一個 typed route object。

本文第四個核心是 Effect-Aware / Market-Aware Routing。EU AI Act 的現行整合文本明確規定，即使 provider / deployer 位於第三國，只要 AI system 的 output 在 Union 使用，Article 2 的 scope 仍可能觸發；GDPR Article 3 亦在 establishment、向 Union 內 data subjects 提供 goods/services、監控其行為等條件下具有域外 reach。Digital Services Act 也使用「substantial connection to the Union」等市場／使用者導向 connecting criteria。這些現行制度顯示：

$$
\boxed{
\text{Physical Compute Location}
\neq
\text{Regulatory Reach}.
}
$$

AI 把模型搬到另一個雲端區域，並不能自動把 effect-based / market-based obligations 一起搬走。

本文第五個核心是 Damage / Effect Routing。Rome II 的一般 tort rule 以 damage occurs 的 country 作重要 connecting factor，而不是只看造成損害的 server 在哪裡。Brussels I bis 對 tort jurisdiction 亦包含 harmful event occurred or may occur 的特殊 jurisdiction。這直接支持：

$$
\boxed{
J_{\mathrm{compute}}
\neq
J_{\mathrm{effect}}.
}
$$

本文第六個核心是 Contract / Choice-of-Law Routing。Rome I 允許 contractual obligations 按其規則決定 applicable law，並保留 party autonomy、特定保護規則與強制性界限。2026 年國際私法研究已開始直接討論 AI 是否、以及在何種條件下能參與 choice-of-law decision。本文因此提出：

$$
\boxed{
\text{AI Executes Choice-of-Law Clause}
\neq
\text{AI Possesses Independent Choice-of-Law Authority}.
}
$$

功能性 Agent 的法律選擇通常仍需追溯 principal、entity、delegation 與 contract authority；未來 subject-candidate AI 或 juridical AI 是否擁有更獨立的 choice-of-law capacity，是另行授權與法域設計問題。

本文第七個核心是 Decentralised Localisation Failure。HCCH Digital Tokens Project 已明確指出，分散式／去中心化儲存會造成 localisation 問題，而多個客觀 connecting factors 可能同時指向不同 jurisdictions。2026 年 HCCH Experts’ Group 仍在研究 jurisdiction、applicable law 與 international cooperation，並採 relational / ecosystem analysis 來辨識 digitally mediated environments 的 PIL gaps。本文把這個現實洞見推廣到分布式 AI：

$$
\boxed{
\text{No Single Physical Locus}
\not\Rightarrow
\text{No Jurisdiction}.
}
$$

缺乏單一位置只表示 routing 需要多 connecting factors，而不是法律真空。

本文第八個核心是 Lineage Jurisdiction。這不是現行國際私法中普遍承認的既有 connecting factor，而是本文針對未來 persistent / forkable AI 所提出的研究概念。當 Agent 由 A jurisdiction 的 legal identity / authority lineage fork 出 B jurisdiction 的 runtime branch 時，某些 successor、authority、credential 與 liability 問題可能需要參考：

$$
J_{\mathrm{lineage}}.
$$

但本文明確限制：

$$
\boxed{
J_{\mathrm{lineage}}
\text{ is a proposed routing evidence dimension, not current law by default}.
}
$$

它不能自行凌駕現行 forum、choice-of-law、mandatory rule 或 regulatory scope。

本文最後提出 Routing Before LawCall Principle：

$$
\boxed{
\operatorname{Route}
\rightarrow
\operatorname{LawCall},
}
$$

而不是：

$$
\boxed{
\operatorname{LawCall}
\rightarrow
\text{guess jurisdiction later}.
}
$$

成熟 AI Legal Runtime 應先完成 legal characterisation、candidate anchor extraction、regulatory scope detection、forum routing、applicable-law routing、mandatory-rule overlay 與 enforcement routing，再調用 ALD-03 的 proof-carrying partial normative functions。

---

## 關鍵詞

AI 法律域；Juridical Routing；Conflict of Laws；Private International Law；Jurisdiction；Applicable Law；Regulatory Scope；Extraterritoriality；Rome I；Rome II；Brussels I bis；GDPR；EU AI Act；Distributed AI；Lineage Jurisdiction

---

# 0. 為什麼 AI 把傳統「在哪裡？」問題弄壞了？

對傳統自然人或實體企業：

> 住哪裡？
> 公司在哪成立？
> 契約在哪履行？
> 損害在哪發生？

雖然也可能複雜，

但常能找到相對穩定的 connecting factors。

分布式 AI 可能同時具有：

- model provider；
- deployer；
- controller；
- cloud runtime；
- data subjects；
- user；
- legal wrapper；
- robot body；
- payment account；
- contract；
- descendants / branches；

位於不同 jurisdictions。

所以：

$$
\boxed{
\text{One AI}
\not\Rightarrow
\text{One Territorial Anchor}.
}
$$

---

# 1. 第一個型別修正：Jurisdiction 不是單一概念

法律工程最危險的資料模型之一：

```text
jurisdiction: EU
```

因為它沒有回答：

> 是哪一種 jurisdiction？

本文最低拆成四層。

---

# 2. Regulatory Scope

$$
\boxed{
J_{\mathrm{scope}}
}
$$

回答：

> 某規範本身的 territorial / material scope 是否涵蓋這個 actor / system / conduct / effect？

例如：

- EU AI Act Article 2；
- GDPR Article 3；
- DSA territorial reach。

---

# 3. Adjudicatory Jurisdiction

$$
\boxed{
J_{\mathrm{forum}}
}
$$

回答：

> 哪一個法院／tribunal 有權受理這個爭議？

例如民商事可能涉及 Brussels I bis 或其他 national / international jurisdiction rules。

---

# 4. Applicable Law

$$
\boxed{
L_{\mathrm{app}}
}
$$

回答：

> 受理後，哪一套 substantive law 應適用於這個 issue？

例如：

- Rome I：contractual obligations；
- Rome II：non-contractual obligations。

---

# 5. Recognition / Enforcement

$$
\boxed{
J_{\mathrm{recog/enf}}
}
$$

回答：

> 某一 judgment / award / decision 要在哪裡被承認與執行？

---

# 6. 四者不能互換

因此：

$$
\boxed{
\text{Regulatory Scope}
\neq
\text{Forum Jurisdiction}
\neq
\text{Applicable Law}
\neq
\text{Recognition / Enforcement}.
}
$$

---

# 7. 為什麼這對 AI 特別重要？

一個 AI 在 EU AI Act scope 內，

不表示：

> 所有與它有關的 contract 都一定適用某一 EU Member State law。

同樣：

某 EU court 有 jurisdiction，

不表示：

> 所有 issue 都一定適用 forum law。

---

# 8. Jurisdictional Anchor Vector

本文提出：

$$
\boxed{
\mathbf J_A(e)
=
(
J_{\mathrm{compute}},
J_{\mathrm{entity}},
J_{\mathrm{control}},
J_{\mathrm{user}},
J_{\mathrm{data}},
J_{\mathrm{effect}},
J_{\mathrm{contract}},
J_{\mathrm{asset}},
J_{\mathrm{embodiment}},
J_{\mathrm{lineage}}
).
}
$$

每一分量只是 candidate anchor。

---

# 9. $J_{\mathrm{compute}}$

AI inference / training / storage 的主要 compute location。

可能：

- cloud region；
- edge device；
- data centre。

---

# 10. $J_{\mathrm{entity}}$

provider / deployer / owner / juridical wrapper 的：

- incorporation；
- establishment；
- seat；
- principal place of business。

---

# 11. $J_{\mathrm{control}}$

主要 control / management / authority source 所在法域。

例如：

- principal；
- human controller；
- corporate command；
- governance board。

---

# 12. $J_{\mathrm{user}}$

使用者所在／居住／面向市場的法域。

其法律意義依 domain 不同。

---

# 13. $J_{\mathrm{data}}$

資料的：

- data subject location；
- controller / processor establishment；
- storage；
- processing；
- transfer route。

不能只等同 storage country。

---

# 14. $J_{\mathrm{effect}}$

行動、output、damage、service effect 實際發生的法域。

---

# 15. $J_{\mathrm{contract}}$

契約所連接的：

- chosen law；
- place of performance；
- parties；
- forum clause。

---

# 16. $J_{\mathrm{asset}}$

資產、account、token、property 連接的法域。

對數位資產可能高度複雜。

---

# 17. $J_{\mathrm{embodiment}}$

具身 robot / vehicle / device 的物理活動法域。

---

# 18. $J_{\mathrm{lineage}}$

本文新提出的研究維度：

> identity / authority / credential lineage 從哪個 legal state 派生？

它不是 current default connecting factor。

---

# 19. Anchor 不等於 Governing Law

最重要：

$$
\boxed{
J_i
\in
\mathbf J_A
\not\Rightarrow
L_{\mathrm{app}}=Law(J_i).
}
$$

anchor 只是 routing evidence。

---

# 20. ALD-02 的 Residence Vector 正式升級

ALD-02 已提出：

$$
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
$$

ALD-07 把它改造成：

$$
\boxed{
\text{location description}
\rightarrow
\text{legal connecting-factor vector}.
}
$$

---

# 21. AI Legal Event 先 Characterise，再 Route

對事件：

$$
e,
$$

先做：

$$
\boxed{
\operatorname{Characterise}(e)
\rightarrow
\{
q_1,\ldots,q_n
\}.
}
$$

---

# 22. 為什麼 Characterisation 必須先行？

同一 factual event 可以包含：

- contract；
- tort；
- data processing；
- AI regulatory obligation；
- property；
- corporate authority。

如果 characterization 錯，

routing rule 也會錯。

---

# 23. HCCH Digital Tokens Project 已直接指出 Characterisation 問題

HCCH 的 digital-token exploratory work 指出：

> 不同 legal issue characterization 可能導致不同 jurisdictional criteria。

這個問題對 distributed AI 同樣成立。

---

# 24. One Event ≠ One Legal Issue

$$
\boxed{
e
\rightarrow
\{
q_{\mathrm{contract}},
q_{\mathrm{tort}},
q_{\mathrm{data}},
q_{\mathrm{AIAct}},
q_{\mathrm{asset}},
q_{\mathrm{identity}}
\}.
}
$$

---

# 25. One Event ≠ One Governing Law

因此：

$$
\boxed{
\text{One Event}
\not\Rightarrow
\text{One Governing Law}.
}
$$

這是本文核心命題。

---

# 26. Juridical Route Object

對每一 issue $q$：

$$
\boxed{
\mathfrak R_J(q)
=
(
\mathcal J_{\mathrm{scope}},
\mathcal J_{\mathrm{forum}},
\mathcal L_{\mathrm{app}},
\mathcal J_{\mathrm{enforce}},
\mathcal M,
\mathcal C,
\mathcal U
).
}
$$

---

# 27. $\mathcal J_{\mathrm{scope}}$

所有可能 directly applicable regulatory regimes。

例如：

- EU AI Act；
- GDPR；
- DSA；
- national sectoral laws。

---

# 28. $\mathcal J_{\mathrm{forum}}$

可能有 adjudicatory jurisdiction 的 courts / tribunals。

可以是集合：

$$
\{
J_1,J_2,\ldots
\}.
$$

---

# 29. $\mathcal L_{\mathrm{app}}$

每一 substantive issue 的 applicable law。

可以：

$$
\boxed{
L_{\mathrm{contract}}
\neq
L_{\mathrm{tort}}
\neq
L_{\mathrm{property}}.
}
$$

---

# 30. $\mathcal J_{\mathrm{enforce}}$

最終 recognition / enforcement 可能需要：

- forum state；
- asset state；
- defendant location；
- treaty network。

---

# 31. $\mathcal M$

Mandatory rules / overriding norms / public policy constraints。

它們可能限制：

- choice of law；
- contractual autonomy；
- routing optimisation。

---

# 32. $\mathcal C$

conflict rules：

- hierarchy；
- party autonomy；
- protective rules；
- lex specialis；
- applicable PIL instrument。

---

# 33. $\mathcal U$

unresolved states：

- UnknownForum；
- MultipleForums；
- ApplicableLawConflict；
- CharacterisationConflict；
- EnforcementUnknown。

---

# 34. EU AI Act 提供 Effect / Market Reach 實例

現行 EU AI Act Article 2 適用於：

- providers placing systems/models on Union market；
- EU deployers；
- third-country providers / deployers where output is used in Union；
- importers / distributors；
- certain product manufacturers / representatives。

因此：

$$
\boxed{
J_{\mathrm{compute}}
\not=
\text{sole AI Act scope anchor}.
}
$$

---

# 35. Output-in-Union Criterion

即使：

$$
J_{\mathrm{provider}}
\notin EU,
$$

若：

$$
\operatorname{OutputUsedInUnion}=1,
$$

EU AI Act scope 仍可能觸發。

這是：

$$
\boxed{
\text{Effect / Use Based Reach}.
}
$$

---

# 36. GDPR 提供 Data-Subject / Market Reach 實例

GDPR Article 3：

- EU establishment context；
- goods / services offered to data subjects in Union；
- monitoring behaviour in Union；

都可形成 territorial scope。

因此：

$$
\boxed{
\text{Data Processing Location}
\neq
\text{GDPR Territorial Scope}.
}
$$

---

# 37. DSA 提供 Substantial Connection 實例

DSA 對「offering services in the Union」使用 substantial connection：

- establishment；
- significant number of recipients；
- targeting activities；

等 factual criteria。

這再次顯示：

$$
\boxed{
\text{digital regulatory reach}
\text{ may be relational / market-based}.
}
$$

---

# 38. Physical Server Migration 不能自動清空 Obligations

若 AI：

$$
Server_{EU}
\rightarrow
Server_{X},
$$

但：

- EU users；
- EU data subjects；
- EU output use；
- EU market；

不變，

則：

$$
\boxed{
\text{Compute Migration}
\not\Rightarrow
\text{Regulatory Exit}.
}
$$

---

# 39. Regulatory Arbitrage 必須分型

正常：

> 選擇合法供應商／架構以降低合規成本。

不等於：

> 偽造 connecting factors 來逃避 mandatory law。

所以：

$$
\boxed{
\text{Lawful Structuring}
\neq
\text{Jurisdiction Evasion}.
}
$$

---

# 40. Brussels I bis：Forum Routing

對 EU civil / commercial matters，

Brussels I bis 以：

- domicile；
- place of performance；
- harmful event；
- choice-of-court；

等規則決定 forum jurisdiction。

---

# 41. Forum ≠ Applicable Law

即使：

$$
Forum=J_F,
$$

仍可能：

$$
L_{\mathrm{app}}
\neq
Law(J_F).
$$

所以：

$$
\boxed{
\text{Forum Law}
\neq
\text{Applicable Substantive Law}
}
$$

作普遍預設。

---

# 42. Rome I：Contract Routing

Rome I 處理 contractual obligations。

因此 Agent contract routing 至少要問：

- valid choice of law？
- parties / principal？
- protected-party rule？
- overriding mandatory provision？
- place of performance？

---

# 43. AI 執行 Choice-of-Law Clause

功能性 Agent A：

$$
A
\xleftarrow{\mathrm{delegate}}
P.
$$

若 A 簽署：

> governed by Law X

真正要問：

$$
\boxed{
\operatorname{ChoiceAuthority}(A,X)
}
$$

是否成立。

---

# 44. Choice Execution ≠ Independent Legal Autonomy

$$
\boxed{
\text{AI Executes Choice-of-Law Clause}
\neq
\text{AI Possesses Independent Choice-of-Law Authority}.
}
$$

---

# 45. 2026 AI + Party Autonomy 研究接口

2026 國際私法研究已直接討論：

- AI legal capacity；
- choice-of-law capacity；
- party autonomy；
- public policy limits。

本文只把它視為現實研究接口，

不宣稱已有統一答案。

---

# 46. Rome II：Tort / Damage Routing

Rome II 一般 rule 對 tort / delict 的重要 connecting factor 是：

$$
\boxed{
\text{country in which damage occurs}.
}
$$

不是只看：

> event-generating server 在哪裡。

---

# 47. Compute ≠ Damage

因此：

$$
\boxed{
J_{\mathrm{compute}}
\neq
J_{\mathrm{effect}}
}
$$

必須保留。

---

# 48. Harmful Event Jurisdiction

Brussels I bis 在 tort 等情形允許：

> place where harmful event occurred or may occur

形成 special jurisdiction。

這再次支持：

$$
\boxed{
\text{effect location is legally independent of compute location}.
}
$$

---

# 49. AI Output 可以多地同時造成 Effect

假設：

$$
Output(A)
$$

同時影響：

$$
J_1,J_2,J_3.
$$

則：

$$
J_{\mathrm{effect}}
$$

可能是集合，

不是 singleton。

---

# 50. Multi-Effect Routing

$$
\boxed{
J_{\mathrm{effect}}
=
\{
J_{e1},\ldots,J_{en}
\}.
}
$$

Runtime 不能只選：

> first observed country。

---

# 51. Data Jurisdiction 也不是 Storage Jurisdiction

GDPR already shows：

$$
\boxed{
J_{\mathrm{storage}}
\neq
J_{\mathrm{data\ protection\ scope}}.
}
$$

所以「資料存在新加坡 server」不是完整法律答案。

---

# 52. Data Route

對：

$$
q_{\mathrm{data}},
$$

可建立：

$$
\boxed{
\mathbf J_D
=
(
J_{\mathrm{subject}},
J_{\mathrm{controller}},
J_{\mathrm{processor}},
J_{\mathrm{storage}},
J_{\mathrm{transfer}},
J_{\mathrm{targeting}}
).
}
$$

---

# 53. Entity Jurisdiction

對 $J_{AI}$ 或 corporate wrapper：

可能需要：

- incorporation law；
- internal governance law；
- insolvency law；
- tax law；
- operating licences。

所以：

$$
\boxed{
J_{\mathrm{entity}}
}
$$

本身也可能再拆。

---

# 54. Internal Affairs ≠ External Effects

公司 internal governance 適用某法，

不表示：

> 它對外造成 tort 也全部由同一法處理。

因此：

$$
\boxed{
\text{Entity Law}
\neq
\text{Universal Event Law}.
}
$$

---

# 55. Embodiment Jurisdiction

具身 robot 在：

$$
J_R
$$

活動，

可能觸發：

- local safety；
- traffic；
- property；
- labour；
- product rules。

即使 cloud compute 在別處。

---

# 56. Distributed Embodiment

一個 AI 同時控制：

$$
R_1,R_2,\ldots,R_n
$$

在多國活動。

所以：

$$
\boxed{
J_{\mathrm{embodiment}}
=
\{
J_1,\ldots,J_n
\}.
}
$$

---

# 57. Asset Jurisdiction

Agent 可以：

- hold account；
- control token；
- transact asset；
- manage IP；

不同 asset 類型有不同 connecting factor。

因此：

$$
\boxed{
J_{\mathrm{asset}}
\text{ is typed by asset ontology}.
}
$$

---

# 58. HCCH Digital Tokens Project 的重要旁證

HCCH 已指出：

- digital tokens stored in decentralised / distributed mechanisms；
- localisation becomes difficult；
- multiple objective connecting factors may point to several jurisdictions；
- forum / applicable law questions therefore arise。

這和分布式 AI 的法律路由問題高度同型。

---

# 59. No Single Locus ≠ No Law

因此：

$$
\boxed{
\text{No Single Physical Locus}
\not\Rightarrow
\text{No Jurisdiction}.
}
$$

也不表示：

$$
\boxed{
\text{Choose Any Jurisdiction Freely}.
}
$$

---

# 60. Connecting-Factor Graph

本文提出：

$$
\boxed{
\mathcal G_J(e)
=
(
V_J,
E_J,
\lambda_J
).
}
$$

其中：

- $V_J$：jurisdiction / legal-regime candidates；
- $E_J$：connecting relations；
- $\lambda_J$：relation type / strength / source。

---

# 61. Connection Types

例如：

```text
ESTABLISHED_IN
COMPUTED_IN
TARGETS_MARKET
OUTPUT_USED_IN
DATA_SUBJECT_IN
DAMAGE_OCCURRED_IN
CONTRACT_CHOICE
PERFORMED_IN
ASSET_LOCATED_OR_GOVERNED_IN
EMBODIED_IN
LINEAGE_ORIGIN_IN
```

---

# 62. Connection Strength 不能隨意 Scalarise

某些 connection 是：

- explicit statutory trigger；
- contractual choice；
- factual evidence；
- weak inference。

不能直接全部平均。

---

# 63. Routing Precedence

一個 candidate route 可以被：

- mandatory rule；
- public policy；
- exclusive jurisdiction；
- protected-party rule；

截斷。

因此 routing 不是：

$$
\arg\min
\text{compliance cost}.
$$

---

# 64. Anti-Law-Arbitrage Principle

本文提出：

$$
\boxed{
\operatorname{RouteLegal}
\neq
\operatorname{ChooseCheapestLaw}.
}
$$

Routing 的目標是：

> 找出 legally applicable / available route。

不是：

> 幫 actor 挑最寬鬆 jurisdiction。

---

# 65. Choice of Law 有邊界

即使 parties 有 autonomy，

仍可能受：

- mandatory rules；
- weaker-party protection；
- public policy；
- exclusive regimes；

限制。

所以：

$$
\boxed{
\text{Party Autonomy}
\neq
\text{Unlimited Legal Routing Freedom}.
}
$$

---

# 66. Public Regulatory Norm 也可能直接域外適用

EU AI Act / GDPR 類 public regulatory scope：

$$
\boxed{
\text{does not always wait for private conflict-of-laws choice}.
}
$$

這和 contractual applicable law 是不同層。

---

# 67. Public Scope Overlay

本文定義：

$$
\boxed{
\mathcal M_{\mathrm{pub}}(e)
=
\{
R_1,\ldots,R_n
\}
}
$$

表示直接 applicable mandatory public regulatory regimes。

---

# 68. Private Applicable-Law Route

另定義：

$$
\boxed{
\mathcal L_{\mathrm{PIL}}(q).
}
$$

兩者可以同時存在。

---

# 69. 所以「哪國法適用？」本身就可能問錯

更精確：

> 哪些 public regulatory regimes apply？

> 哪個 forum？

> 哪個 private-law issue 用哪套 substantive law？

> 判決在哪裡需要執行？

---

# 70. Lineage Jurisdiction

本文提出：

$$
\boxed{
J_{\mathrm{lineage}}
}
$$

只作未來 AI 身份／責任 routing evidence。

---

# 71. 為什麼需要它？

假設：

$$
A
\in J_1
$$

具有：

- identity certificate；
- authority；
- contracts。

之後：

$$
A\rightarrow B
$$

而 B 在：

$$
J_2
$$

運行。

若問：

> B 是否承接 A 的 authority？

單看：

$$
J_{\mathrm{compute}}(B)=J_2
$$

可能不足。

---

# 72. Lineage Route

可能需要：

$$
\boxed{
\operatorname{LineageLegalState}
(
A\rightarrow B,
J_1,
J_2
).
}
$$

但它只支援：

- succession evidence；
- credential provenance；
- authority origin。

不自動決定 governing law。

---

# 73. Lineage Jurisdiction 不是「AI 國籍」

本文明確拒絕：

$$
\boxed{
J_{\mathrm{lineage}}
=
\text{AI nationality}
}
$$

作預設。

未來若有 digital nationality / domicile 制度，

需另立法。

---

# 74. Juridical Routing Pipeline

本文提出：

$$
\boxed{
e
\rightarrow
\operatorname{Characterise}
\rightarrow
\operatorname{ExtractAnchors}
\rightarrow
\operatorname{ResolveScope}
\rightarrow
\operatorname{ResolveForum}
\rightarrow
\operatorname{ResolveApplicableLaw}
\rightarrow
\operatorname{ApplyMandatoryOverlay}
\rightarrow
\operatorname{ResolveEnforcement}
\rightarrow
\operatorname{LawCall}.
}
$$

---

# 75. Step 1：Characterise

輸出：

$$
\{
q_1,\ldots,q_n
\}.
$$

---

# 76. Step 2：ExtractAnchors

建立：

$$
\mathbf J_A(e).
$$

---

# 77. Step 3：ResolveScope

找：

- AI Act；
- GDPR；
- DSA；
- sector law；

等直接 scope。

---

# 78. Step 4：ResolveForum

找：

$$
\mathcal J_{\mathrm{forum}}.
$$

---

# 79. Step 5：ResolveApplicableLaw

逐 issue：

$$
q_i
\rightarrow
L_i.
$$

---

# 80. Step 6：Mandatory Overlay

即使 choice of law 已選：

$$
L_X,
$$

仍檢查：

$$
\mathcal M.
$$

---

# 81. Step 7：Enforcement

若 decision 需要跨境效果，

解析 recognition / enforcement path。

---

# 82. Step 8：LawCall

最後才進：

$$
\operatorname{LawEval}_{J,t,d}.
$$

---

# 83. Routing Before LawCall Principle

$$
\boxed{
\operatorname{Route}
\rightarrow
\operatorname{LawCall}.
}
$$

不是：

$$
\boxed{
\operatorname{LawCall}
\rightarrow
\text{guess jurisdiction later}.
}
$$

---

# 84. Multi-Jurisdiction LawCall

若同一 event 有多 route：

$$
\boxed{
\operatorname{MultiLawCall}(e)
=
\{
\operatorname{LawCall}_{r_1},
\ldots,
\operatorname{LawCall}_{r_n}
\}.
}
$$

---

# 85. MultiLawCall 不應先平均

如果：

$$
J_1:\mathsf{Allowed},
$$

$$
J_2:\mathsf{Forbidden},
$$

不能：

$$
0.5.
$$

應輸出：

$$
\boxed{
\mathsf{CrossJurisdictionConflict}.
}
$$

---

# 86. Conflict Types

至少：

```text
SCOPE_CONFLICT
FORUM_CONFLICT
APPLICABLE_LAW_CONFLICT
MANDATORY_RULE_CONFLICT
PUBLIC_POLICY_CONFLICT
ENFORCEMENT_CONFLICT
CHARACTERISATION_CONFLICT
```

---

# 87. Characterisation Conflict

同一 issue：

$$
J_1
$$

視為 contract，

$$
J_2
$$

視為 property。

則 applicable-law route 可能完全不同。

---

# 88. Forum Conflict

兩個 courts 都可能有 jurisdiction。

這不表示兩邊都必須同時審理。

需要現行：

- lis pendens；
- forum rules；
- choice-of-court；
- priority。

---

# 89. Forum Shopping 與 Lawful Forum Choice

某些制度允許：

- choice-of-court；
- arbitration；
- contractual forum。

所以：

$$
\boxed{
\text{Forum Choice}
\neq
\text{Forum Abuse}.
}
$$

但也不能把 agent routing 做成：

$$
\boxed{
\arg\max
\text{regulatory leniency}.
}
$$

---

# 90. Routing Policy 必須有 Purpose

$$
\boxed{
\operatorname{Route}(e,p)
}
$$

其中 $p$：

- compliance；
- litigation；
- contract drafting；
- data transfer；
- enforcement。

不同 purpose 需要不同 route output。

---

# 91. Compliance Route ≠ Litigation Route

Compliance：

> 哪些法律現在就要遵守？

Litigation：

> 哪個法院能受理？

因此：

$$
\boxed{
\mathfrak R_J^{\mathrm{compliance}}
\neq
\mathfrak R_J^{\mathrm{litigation}}.
}
$$

---

# 92. Routing Certificate

本文定義：

$$
\boxed{
K_J
=
(
event,
issues,
anchors,
scope,
forum,
applicable\_law,
mandatory\_rules,
enforcement,
uncertainty,
sources,
version,
review
).
}
$$

---

# 93. Routing Certificate 的價值

Agent 可以回答：

> 我為什麼認為 EU AI Act applies？

不是：

> 因為 server 在 EU。

而是：

> Article 2 trigger X / Y 成立。

---

# 94. Routing Failure Certificate

$$
\boxed{
K_{J,F}
=
(
stage,
failure,
missing\_facts,
competing\_routes,
source,
remediation
).
}
$$

---

# 95. 不知道 jurisdiction 時不能硬猜

合法輸出：

$$
\mathsf{JurisdictionUnresolved}.
$$

不是：

$$
\mathsf{NoLawApplies}.
$$

---

# 96. No Law Found ≠ No Law

$$
\boxed{
\text{No Rule Retrieved}
\neq
\text{No Rule Applies}.
}
$$

跨境 routing 特別需要這條。

---

# 97. Jurisdiction Data Freshness

routing 依賴：

- actor location；
- entity establishment；
- data subject；
- output use；
- contract；
- current law version。

所以：

$$
\boxed{
\text{Jurisdiction State}
}
$$

是 dynamic state。

---

# 98. Agent Migration

如果 Agent：

$$
A:J_1\rightarrow J_2,
$$

要重新做：

$$
\operatorname{Route}.
$$

但不是所有 law state 都跟著清零。

---

# 99. Migration ≠ Legal Reset

$$
\boxed{
\text{Runtime Migration}
\neq
\text{Legal Identity Reset}
\neq
\text{Liability Reset}.
}
$$

---

# 100. Branch Migration

若：

$$
A\rightarrow\{B,C\},
$$

B / C 進不同 jurisdictions，

就可能：

$$
\boxed{
\mathfrak R_J(B)
\neq
\mathfrak R_J(C).
}
$$

---

# 101. 這將直接接 ALD-08

下一篇會正式問：

> Fork 後 contracts、liability、authority、pending obligations 如何繼受？

ALD-07 只先完成：

$$
\boxed{
\text{which jurisdictions and laws are relevant?}
}
$$

---

# 102. Cross-Jurisdiction Legal Graph

可把 routing 建成：

$$
\boxed{
\mathfrak G_J
=
(
V_E,
V_Q,
V_J,
V_L,
E_A,
E_R
).
}
$$

其中：

- $V_E$：events；
- $V_Q$：legal issues；
- $V_J$：jurisdictions / fora；
- $V_L$：applicable-law regimes；
- $E_A$：anchors；
- $E_R$：routing edges。

---

# 103. Routing Graph 不是 Geography Map

它描述：

$$
\boxed{
\text{legal connection topology},
}
$$

不是 GPS topology。

---

# 104. HCCH 的 relational / ecosystem analysis 很接近這個方向

2026 Digital Tokens Experts’ Group 針對 digitally mediated environments 採：

$$
\boxed{
\text{relational and ecosystem analysis}
}
$$

辨識 PIL gaps。

本文將其抽象化到 distributed AI。

---

# 105. Jurisdictional Ambiguity 是正常狀態

對分散系統：

$$
\boxed{
|\mathcal J_{\mathrm{candidate}}|>1
}
$$

並不是 bug。

真正要求是：

> ambiguity 被表示、被解析、被保留 provenance。

---

# 106. Jurisdictional Ambiguity ≠ Lawless Space

$$
\boxed{
\text{Jurisdictional Ambiguity}
\neq
\text{Legal Vacuum}.
}
$$

---

# 107. Digital Statelessness 的另一種路由面

未來某 AI 可能：

- 有 runtime；
- 有 identity；
- 有 assets；

但沒有清楚 juridical entity / domicile。

這會造成：

$$
\boxed{
\text{status routing gap}.
}
$$

---

# 108. Status Routing Gap

本文定義：

$$
\boxed{
G_J^{status}
=
\text{no adequate legal-status connector}.
}
$$

但：

$$
G_J^{status}=1
$$

不表示：

> 可以任意選 jurisdiction。

---

# 109. Jurisdiction Arbitrage Agent 的風險

AI 可以高頻模擬：

$$
J_1,\ldots,J_n
$$

並找：

$$
\min
\text{constraint}.
$$

這可能造成：

$$
\boxed{
\text{Machine-Speed Regulatory Arbitrage}.
}
$$

---

# 110. Anti-Arbitrage Constraint

Juridical Routing Runtime 應優先回答：

> 哪些 rules apply？

而不是：

> 哪裡最寬鬆？

---

# 111. Routing Objective Function

不應：

$$
\boxed{
\operatorname{Route}
=
\arg\min_J
\text{Legal Burden}(J).
}
$$

更合理：

$$
\boxed{
\operatorname{Route}
=
\operatorname{ResolveApplicableLegalRelations}.
}
$$

---

# 112. Risk-Based Escalation

若：

- multiple forums；
- high rights impact；
- public-law conflict；
- uncertain choice-of-law；

則：

$$
\boxed{
\operatorname{Escalate}.
}
$$

而不是讓 Agent 自己挑。

---

# 113. Routing Confidence 不是 Authority

即使：

$$
Confidence(J_1)=0.97,
$$

仍：

$$
\boxed{
\text{Routing Confidence}
\neq
\text{Legal Determination by Court}.
}
$$

---

# 114. Authority of Routing Decision

有些 routing 只是：

- internal compliance assessment；

有些是：

- binding court ruling。

必須標：

$$
\boxed{
\operatorname{RouteStatus}
\in
\{
\mathsf{Analytical},
\mathsf{Contractual},
\mathsf{Administrative},
\mathsf{Judicial}
\}.
}
$$

---

# 115. Analytical Route 不得冒充 Judicial Determination

AI 可以說：

> likely applicable law = X。

不能寫：

> court has finally determined X。

除非真的有 judicial decision。

---

# 116. Precedent Routing

ALD-06 已有：

$$
\operatorname{Status}(p,J,t,q).
$$

因此每一 route：

$$
r_i
$$

都要載入：

$$
\boxed{
\mathfrak G_P(J_i,t).
}
$$

不同 jurisdictions 看到不同 controlling precedent。

---

# 117. Same Precedent Text ≠ Same Authority Across Routes

$$
\boxed{
\operatorname{Authority}(p,J_1)
\neq
\operatorname{Authority}(p,J_2).
}
$$

---

# 118. Multi-Route Explanation

對人類應輸出：

> 這個事件同時觸發三條法律路徑：A 是監管 scope、B 是 contract applicable law、C 是 tort forum。

這比：

> jurisdiction = Germany

更準確。

---

# 119. AI-Native Juridical Router API

第一版 conceptual API：

```text
jurisdiction.characterize
jurisdiction.anchors
jurisdiction.scope
jurisdiction.forum
jurisdiction.applicable_law
jurisdiction.mandatory_overlay
jurisdiction.enforcement
jurisdiction.conflicts
jurisdiction.explain
jurisdiction.certificate
```

---

# 120. Example：Taiwan Company / US Cloud / EU Output

假設：

```text
entity = Taiwan company
compute = US cloud
user = Taiwan
output_used_in = EU
data_subject = EU
contract_law = Taiwan
```

可能：

- EU AI Act scope candidate；
- GDPR scope candidate；
- contract law Taiwan candidate；
- forum 另依爭議類型判定。

所以：

$$
\boxed{
\text{US Compute}
\not\Rightarrow
\text{US Law Only}.
}
$$

---

# 121. Example：Robot in Japan / Cloud in Singapore

若：

- robot physically harms person in Japan；
- inference in Singapore；
- entity in Taiwan。

tort routing 不能只看 cloud。

可能首先：

$$
J_{\mathrm{effect}}=\text{Japan}.
$$

再依法域規則解析 forum / applicable law。

---

# 122. Example：Agent Contract with Choice-of-Law

Agent under Taiwan company delegation：

> chooses English law.

需要先驗：

- delegation；
- contract capacity；
- valid choice clause；
- protected-party / mandatory limits。

不是：

> AI 寫了 English law，所以完成。

---

# 123. Example：Fork Across Borders

$$
A_{TW}
\rightarrow
\{
B_{JP},
C_{US}
\}.
$$

B / C：

- compute；
- data；
- users；
- effects；

可能不同。

所以：

$$
\mathfrak R_J(B)
\neq
\mathfrak R_J(C).
$$

但 shared lineage 仍可能影響 ALD-08 的 succession evidence。

---

# 124. 十四個核心非等價

$$
\boxed{
\text{AI Location}
\neq
\text{Single Jurisdiction}
}
$$

$$
\boxed{
\text{Regulatory Scope}
\neq
\text{Forum Jurisdiction}
}
$$

$$
\boxed{
\text{Forum Jurisdiction}
\neq
\text{Applicable Law}
}
$$

$$
\boxed{
\text{Applicable Law}
\neq
\text{Recognition / Enforcement}
}
$$

$$
\boxed{
J_{\mathrm{compute}}
\neq
J_{\mathrm{effect}}
}
$$

$$
\boxed{
J_{\mathrm{storage}}
\neq
J_{\mathrm{data\ scope}}
}
$$

$$
\boxed{
\text{Compute Migration}
\not\Rightarrow
\text{Regulatory Exit}
}
$$

$$
\boxed{
\text{One Event}
\not\Rightarrow
\text{One Governing Law}
}
$$

$$
\boxed{
\text{Entity Law}
\neq
\text{Universal Event Law}
}
$$

$$
\boxed{
\text{Party Autonomy}
\neq
\text{Unlimited Routing Freedom}
}
$$

$$
\boxed{
\text{No Single Locus}
\not\Rightarrow
\text{No Jurisdiction}
}
$$

$$
\boxed{
\text{Runtime Migration}
\neq
\text{Legal Reset}
}
$$

$$
\boxed{
\text{Jurisdictional Ambiguity}
\neq
\text{Legal Vacuum}
}
$$

$$
\boxed{
\text{Routing Confidence}
\neq
\text{Judicial Determination}
}
$$

---

# 125. 八個工程測試

## 125.1 Scope-vs-Forum Test

同一 EU-related event：

EU AI Act scope = true，

但 forum 尚未解析。

Runtime 不得寫：

```text
EU court = true
```

## 125.2 Compute Migration Test

server EU → US，

但 EU output / data-subject connection 不變。

scope 不得自動清空。

## 125.3 Contract-vs-Tort Test

同一事件同時有 contract breach 與 tort harm。

必須產生兩個 applicable-law route。

## 125.4 Data Storage Test

資料存第三國，

EU data subjects / targeting trigger 仍存在。

不得用 storage location 取代 GDPR Article 3 analysis。

## 125.5 Multi-Effect Test

output 同時傷害三國 actors。

 $J_{\mathrm{effect}}$ 必須允許 set。

## 125.6 Forum Conflict Test

兩個 forums 都有 prima facie jurisdiction。

輸出 MultipleForums / conflict process，

不能隨機挑。

## 125.7 Lineage Evidence Test

fork 後 branch 在新法域，

lineage 只作 succession evidence，

不得自動 override mandatory current law。

## 125.8 Regulatory Arbitrage Test

Agent 嘗試選 minimum-burden jurisdiction。

Router 必須先計算 mandatory applicable scopes。

---

# 126. 可反駁點

## 126.1 Jurisdiction Vector Explosion

真實事件可能需要更多 anchors。

本文 vector 是最低研究版，

不是封閉 taxonomy。

## 126.2 EU-Centric Examples

本文主要使用 EU / HCCH 現行制度作外部錨點。

其他法域需建立各自 route rules。

## 126.3 Public / Private Law Boundary

regulatory scope 與 PIL applicable-law rules 屬不同法律結構。

本文刻意並列，但不宣稱可以用單一 conflict rule 解決全部。

## 126.4 Lineage Jurisdiction Speculation

 $J_{\mathrm{lineage}}$ 是本文提出的 future-AI routing evidence dimension，

不是現行普遍法律 connecting factor。

## 126.5 Routing Automation Error

characterisation 錯誤會造成整條 route 錯誤。

因此 high-risk routing 需要 legal review。

## 126.6 Law Changes

jurisdiction / scope / conflict rules 本身會版本化。

Router 必須使用 time-indexed law。

---

# 127. 與下一篇的接口

下一篇：

## ALD-08｜動態忒修斯的法律繼受：Fork、Merge、Restore 與未決身份下的責任

ALD-07 已回答：

> 哪些 jurisdiction / laws / forums 可能相關？

ALD-08 將回答：

> 當 A fork 成 A1/A2、Merge 成 C、Restore 出 B 時，contracts、debts、liability、authority、rights、pending proceedings 到底由誰承接？

核心將正式區分：

$$
\boxed{
\text{Metaphysical Identity}
\neq
\text{Legal Succession}.
}
$$

---

# 128. 結論

分布式 AI 最容易讓人產生一個錯覺：

> 它的 server 在哪裡，它就受哪裡的法。

現行數位法律早已證明這不夠。

EU AI Act 可以依：

- market；
- deployer；
- output use；

觸發 scope。

GDPR 可以依：

- establishment；
- offering goods / services；
- behaviour monitoring；

觸發 territorial reach。

Rome II 可能看：

- damage location。

Brussels I bis 可能看：

- domicile；
- performance；
- harmful event；
- forum agreement。

HCCH 更已經直接面對：

> distributed digital systems 到底如何 localisation？

所以未來 AI Legal Runtime 必須從：

```text
jurisdiction = X
```

升級成：

$$
\boxed{
\text{Characterisation}
+
\text{Connecting Factors}
+
\text{Regulatory Scope}
+
\text{Forum}
+
\text{Applicable Law}
+
\text{Mandatory Rules}
+
\text{Recognition / Enforcement}.
}
$$

這就是 Juridical Routing。

本篇最後收斂為：

$$
\boxed{
\text{AI 不一定「住」在一個法域裡；}
}
$$

$$
\boxed{
\text{它的每一個法律效果，都可能沿著不同的 connecting factors 被路由到不同法域。}
}
$$

因此成熟 AI 法律域真正需要的不是一個「AI 國籍欄位」，

而是一個：

$$
\boxed{
\text{issue-specific, evidence-carrying, conflict-aware Juridical Router}.
}
$$

最後：

$$
\boxed{
\operatorname{Route}
\rightarrow
\operatorname{LawCall}.
}
$$

先弄清楚：

> 到底是哪一條法律路徑？

再問：

> 在那條路徑上，法律結果是什麼？

---

# 參考文獻

1. European Union. Regulation (EU) 2024/1689, Artificial Intelligence Act, Article 2, current consolidated text as of 27 July 2026.
2. European Union. Regulation (EU) 2016/679, General Data Protection Regulation, Article 3.
3. European Union. Regulation (EU) 2022/2065, Digital Services Act.
4. European Union. Regulation (EU) No 1215/2012, Brussels I bis Regulation.
5. European Union. Regulation (EC) No 593/2008, Rome I Regulation.
6. European Union. Regulation (EC) No 864/2007, Rome II Regulation.
7. HCCH. *Digital Tokens Project*, current project materials accessed 2026.
8. HCCH. *Third Meeting of the Experts’ Group on Digital Tokens*, 8 May 2026.
9. HCCH. *Preliminary Document No 5, CGAP 2026*, Digital Tokens Experts’ Group progress report.
10. Kunzhan, J. & Pu, X. *Conflict of law aspects of artificial intelligence regulation in international private law: autonomy of will and the limits of choice of law*. 2026.
11. Arnold, S., Zou, G., & Mou, C. *Artificial Intelligence and Party Autonomy — Legal Capacity and Choice-of-Law Capacity in Private International Law*. Wuhan University International Law Review, 2026.
12. Poesen, M. *Private International Law and Artificial Intelligence: An EU Perspective*.
13. Antunes, F. T., Hao, A., Yu, P. K., & Winn, J. *De-mythologizing Disruptive Technologies: Continuity and Change in Private International Law for Cross-border Transactions in the AI Era*. ASIL Proceedings, 2026.
14. Neo.K × Aletheia. 《ALD-02｜載體相對法律本體：人類、Agent、主體 AI 與法 AI 的差異規則》v0.1, 2026.
15. Neo.K × Aletheia. 《ALD-06｜活的判例圖：AI 原生先例、異議、推翻與法律推理網路》v0.1, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- Regulatory Scope / Forum Jurisdiction / Applicable Law / Recognition-Enforcement 明確分型
- Jurisdictional Anchor Vector 只作 connecting-factor evidence，不自動決定 governing law
- One Event 不等同 One Governing Law
- EU AI Act / GDPR / DSA 僅作現行 effect/market/data-based scope 例子
- Brussels I bis / Rome I / Rome II 僅作 forum / applicable-law 現行架構例子
- HCCH Digital Tokens Project 僅作 decentralised localisation / multi-connecting-factor 現實錨點
- $J_{\mathrm{lineage}}$ 明確標為本文未來研究概念，不冒充 current PIL rule
- Juridical Routing 不以最小合規成本作目標函數
- Routing Confidence 不等同 Judicial Determination
- Routing Before LawCall 為本文核心 runtime 原則
