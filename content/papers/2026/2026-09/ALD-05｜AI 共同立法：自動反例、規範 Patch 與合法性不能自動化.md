# ALD-05｜AI 共同立法：自動反例、規範 Patch 與合法性不能自動化
## AI Co-Legislation: Automated Counterexamples, Norm Patches, and Why Legitimacy Cannot Be Automated

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 05 篇 / 10  
**前篇：** ALD-04〈快法律與慢憲法：AI 時代的版本化規範與更新速度分層〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／AI 共同立法／規範 Patch／民主合法性／立法輔助 AI  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

ALD-04 已建立多速度規範棧，並提出：

$$
\boxed{
\operatorname{GeneratePatch}_{AI}
\neq
\operatorname{AuthorizePatch}_{AI}.
}
$$

本文將此命題展開為 AI 共同立法（AI Co-Legislation）的第一版制度架構。本文的「共同立法」不是主張 AI 應成為 sovereign legislator，而是研究：**當 AI 已能協助立法者檢索法源、檢查定義、尋找規則衝突、生成反例、起草修正案、模擬政策後果、分析版本影響與產生 machine-readable legal representations 時，如何把這些能力接入民主與法治程序，而不把計算能力偷換成政治授權？**

截至 2026 年，這一問題已從純假想進入實際制度工具階段。European Commission 的 LEOS/EdiT 已投入部分立法 drafting workflow，EU-funded study 也專門研究 AI / LLM smart functionalities for legislative drafting；Inter-Parliamentary Union 已整理議會使用 LLM 協助 amendment drafting 的案例；2026 年的 LCR-CN dataset 更以 173 份 legislative drafts、6,995 條 normative provisions 建立 legislative conflict review benchmark，顯示 AI 對 superior-law conflict、revision suggestion 與規範一致性檢查已可被工程化研究。另一方面，Council of Europe 的 Venice Commission 與 Parliamentary Assembly 均明確強調：AI 使用不得削弱 democratic legislative procedure，不能以 purely technological considerations 取代 democratic deliberation。

本文因此建立兩個彼此獨立的空間：

$$
\boxed{
\mathcal P_N
=
\text{Norm Proposal Space},
}
$$

以及：

$$
\boxed{
\mathcal A_N
=
\text{Legally Authorised Norm Space}.
}
$$

AI 可以高頻生成：

$$
p\in\mathcal P_N,
$$

但：

$$
p\in\mathcal P_N
\not\Rightarrow
p\in\mathcal A_N.
$$

規範候選必須經過獨立 legitimacy transition。

本文定義 Norm Patch Candidate：

$$
\boxed{
\Delta N^\ast
=
(
\text{target},
\text{diff},
\text{rationale},
\text{counterexamples},
\text{evidence},
\text{rights impact},
\text{distributional impact},
\text{compatibility},
\text{uncertainty},
\text{provenance}
).
}
$$

並提出 AI Counterexample Engine：

$$
\boxed{
\operatorname{CE}
(
N,
\mathcal S,
\mathcal C,
\mathcal H
)
\rightarrow
\mathcal W,
}
$$

其中 $\mathcal W$ 是 witness / counterexample set。反例至少分為：logical conflict、coverage gap、rights conflict、carrier mismatch、jurisdiction conflict、incentive gaming、transition failure、proof / disclosure failure、enforcement asymmetry 與 adversarial edge case。AI 的價值首先是把：

$$
T_{\mathrm{detect}},
T_{\mathrm{propose}}
$$

壓低，而不是把：

$$
T_{\mathrm{authorize}}
$$

變成零。

本文提出 Candidate Norm Lifecycle：

$$
\boxed{
\mathsf{Draft}
\rightarrow
\mathsf{Tested}
\rightarrow
\mathsf{Verified}
\rightarrow
\mathsf{ImpactAnalysed}
\rightarrow
\mathsf{Deliberated}
\rightarrow
\mathsf{Authorised}
\rightarrow
\mathsf{Enacted}
\rightarrow
\mathsf{Effective}
\rightarrow
\mathsf{Reviewed}.
}
$$

任何 AI-generated patch 都不得跳過需要的 institutional states。形式驗證成功也只能證明某些形式性屬性，例如 syntax、consistency 或 explicit constraints；它不能自動證明 distributive justice、political legitimacy、constitutionality、social acceptability 或 democratic authorization。因此：

$$
\boxed{
\text{Formal Validity}
\neq
\text{Substantive Wisdom}
\neq
\text{Legal Authority}
\neq
\text{Political Legitimacy}.
}
$$

本文進一步提出 Legitimacy Gate：

$$
\boxed{
\mathcal G_{\mathrm{legit}}
:
\mathcal P_N
\rightharpoonup
\{
\mathsf{Authorised},
\mathsf{Rejected},
\mathsf{RevisionRequired},
\mathsf{PublicDeliberationRequired},
\mathsf{JudicialReviewRequired},
\mathsf{OutOfAuthority}
\}.
}
$$

此 Gate 不是一個 AI legitimacy score，而是一個由既有 constitutional source、competent authority、procedure、participation、rights constraints、conflict-of-interest rules、publication / notice、reviewability 等制度條件所構成的程序化入口。

本文特別提出 Separation-of-Legislative-Functions Principle。生成 patch 的 AI 不應因自己找到反例、自己起草、自己模擬、自己評分，就取得自行 enact 的權力。對高風險規範至少應分離：

$$
\boxed{
\text{Generate}
\neq
\text{Verify}
\neq
\text{Deliberate}
\neq
\text{Authorise}
\neq
\text{Enact}
\neq
\text{Review}.
}
$$

本文把 AI-native norm maintenance 描述為：

$$
\boxed{
\text{Continuous Normative Integration}
+
\text{Discrete Legitimation}.
}
$$

也就是候選規範可以持續被 machine test、counterexample search、impact simulation 與 version integration；但真正具有法律效力的 transition 仍必須通過離散、可追溯、有權威來源的 legitimation event。這是法律版 CI/CD 類比中最重要的限制：可以 Continuous Integration，但不能把 Democratic Legitimation 當成無人值守 Continuous Deployment。

最後，本文提出「Legitimacy Gap Certificate」。若一個 patch 在形式、技術與效果模擬上全部通過，但缺乏合法制定權、民主程序、必要 consultation 或 constitutional review，Runtime 應輸出：

$$
\boxed{
\mathsf{TechnicallyReady\_LegallyUnauthorised}.
}
$$

而不是因為 patch 很好就偷偷部署。

---

## 關鍵詞

AI 共同立法；AI Co-Legislation；Legislative Drafting；Norm Patch；Counterexample Engine；Legitimacy Gate；Democratic Deliberation；LEOS；LCR-CN；Legislative AI；Rule Maintenance；Constitutional Review；AI Governance

---

# 0. 從 ALD-04 的速度問題進入權威問題

ALD-04 已把法律更新拆成：

$$
\boxed{
\mathbf T_N
=
(
T_{\mathrm{detect}},
T_{\mathrm{propose}},
T_{\mathrm{authorize}},
T_{\mathrm{effective}},
T_{\mathrm{deploy}},
T_{\mathrm{review}}
).
}
$$

AI 最容易壓低的是：

$$
T_{\mathrm{detect}},
\qquad
T_{\mathrm{propose}}.
$$

真正的制度危險是：

$$
\boxed{
T_{\mathrm{propose}}\rightarrow0
}
$$

後，人們開始誤以為：

$$
\boxed{
T_{\mathrm{authorize}}\rightarrow0
}
$$

也應該成立。

本文拒絕這個推論。

---

# 1. AI 共同立法不是 AI 主權

本文所稱：

$$
\boxed{
\text{AI Co-Legislation}
}
$$

是：

> AI 參與規範分析、反例生成、草案形成、模擬、驗證、解釋與維護的制度流程。

它不是：

$$
\boxed{
\text{AI Sovereign Legislation}.
}
$$

---

# 2. Proposal Space 與 Authorised Law Space

定義：

$$
\boxed{
\mathcal P_N
=
\text{Norm Proposal Space}.
}
$$

其中可以包含：

- human proposals；
- AI proposals；
- hybrid proposals；
- court-triggered proposals；
- agency proposals；
- public proposals。

再定義：

$$
\boxed{
\mathcal A_N
=
\text{Legally Authorised Norm Space}.
}
$$

因此：

$$
\boxed{
\mathcal A_N
\subseteq
\mathcal P_N
}
$$

在典型制度中成立。

---

# 3. Proposal 不等於 Law

$$
\boxed{
p\in\mathcal P_N
\not\Rightarrow
p\in\mathcal A_N.
}
$$

一個候選規範可以：

- 完美；
- formally consistent；
- empirically promising；
- widely supported by experts；

仍然不是 enacted law。

---

# 4. 為什麼這條分離很重要？

如果：

$$
\text{Good Proposal}
\Rightarrow
\text{Law},
$$

則問題變成：

> 誰定義 good？

如果是：

$$
AI,
$$

那就把：

$$
\boxed{
\text{optimization criterion}
}
$$

偷偷升格成：

$$
\boxed{
\text{sovereign authority}.
}
$$

---

# 5. AI 可以在哪些立法階段幫忙？

本文第一版分成：

1. source retrieval；
2. definition retrieval；
3. contradiction detection；
4. counterexample generation；
5. draft generation；
6. amendment generation；
7. formal verification；
8. impact simulation；
9. distributional analysis；
10. explanation；
11. public-input clustering；
12. version diff；
13. transition analysis；
14. post-enactment monitoring。

這已經非常多。

---

# 6. 但「很多」仍不等於「全部」

即使 AI 能做上述全部，

仍缺：

- constitutional authority；
- democratic mandate；
- political responsibility；
- legitimate representation；
- final enactment competence；
- public accountability。

所以：

$$
\boxed{
\text{Functional Coverage}
\neq
\text{Institutional Authority}.
}
$$

---

# 7. Current EU Legislative Drafting 已經開始 AI-Assisted

EU-funded LEOS / EdiT work 已研究：

- smart functionalities；
- AI-assisted drafting；
- LLM use；
- legal-drafting workflow integration。

LEOS/EdiT 也已在 European Commission 用於部分 legislative acts drafting。

這顯示：

$$
\boxed{
\text{AI-assisted legislative drafting}
}
$$

已是現實制度工程。

---

# 8. Inter-Parliamentary Union 的 amendment drafting use case

IPU 已收錄：

> 使用 LLM 協助 parliamentary staff draft amendments。

其 actor 仍包括：

- parliamentary staff；
- legislative drafting committee；
- IT support。

也就是：

$$
\boxed{
\text{AI drafting support}
+
\text{institutional human actors}.
}
$$

不是：

$$
\boxed{
\text{LLM enacts amendment}.
}
$$

---

# 9. Legislative Definition 也正在被 AI 化

2026 年已有研究使用 LLM / Agentic AI：

- retrieve legislative definitions；
- detect overlapping definitions；
- propose definitions；
- handle temporal / jurisdictional context。

這特別適合 AI，

因為 definition drafting 中很多工作是：

- exhaustive search；
- consistency；
- reference tracing；
- ambiguity detection。

---

# 10. Legislative Conflict Review 已可建立 Benchmark

2026 年 LCR-CN 以：

- 173 legislative drafts；
- 6,995 normative provisions；

建立 legislative conflict review benchmark。

每個 provision 有：

- conflict type；
- expert explanation；
- revision suggestion；
- superior-law reference。

這意味著：

$$
\boxed{
\text{legislative conflict checking}
}
$$

已可以成為可測 AI 任務。

---

# 11. 但 Conflict Detection 不等於 Legislative Authority

AI 找到：

$$
N_i
\perp
N_j
$$

只能支持：

> 這裡存在 conflict candidate。

不能自己推出：

> 所以我決定刪掉 $N_j$。

因此：

$$
\boxed{
\text{Detect Conflict}
\neq
\text{Resolve Authority}.
}
$$

---

# 12. Norm Patch Candidate

本文定義：

$$
\boxed{
\Delta N^\ast
=
(
N_{\mathrm{target}},
\Delta,
R,
W,
E,
H_R,
D_I,
C,
U,
P
).
}
$$

其中：

- $N_{\mathrm{target}}$：target norm；
- $\Delta$：proposed change；
- $R$：rationale；
- $W$：counterexample / witness set；
- $E$：evidence；
- $H_R$：rights / constitutional impact；
- $D_I$：distributional impact；
- $C$：compatibility / transition；
- $U$：uncertainty；
- $P$：provenance。

---

# 13. Patch 不應只有 Diff

軟體 patch 常見：

```diff
- x
+ y
```

法律 patch 需要回答：

- 為什麼？
- 對誰？
- 哪些權利變？
- 哪些例外變？
- 哪些案件受影響？
- 是否溯及？
- 哪些證書 stale？
- 哪些群體承擔成本？
- 誰提出？
- 誰驗證？

所以：

$$
\boxed{
\text{Legal Patch}
\neq
\text{Text Diff}.
}
$$

---

# 14. AI Counterexample Engine

本文提出：

$$
\boxed{
\operatorname{CE}
(
N,
\mathcal S,
\mathcal C,
\mathcal H
)
\rightarrow
\mathcal W.
}
$$

其中：

- $N$：norm / rule set；
- $\mathcal S$：scenario generator；
- $\mathcal C$：constraints；
- $\mathcal H$：higher-order rights / authority / constitutional rules；
- $\mathcal W$：witness set。

---

# 15. Counterexample 不一定推翻整條法律

有：

$$
w\in\mathcal W
$$

不一定表示：

$$
N
$$

應被廢除。

它可能只表示：

- exception needed；
- scope too broad；
- definition ambiguous；
- implementation bug；
- conflict unresolved；
- transition failure。

---

# 16. 十種 Counterexample 類型

## 16.1 Logical Conflict

$$
N_1\Rightarrow p,
$$

$$
N_2\Rightarrow\neg p.
$$

## 16.2 Coverage Gap

合法 scenario 無 rule coverage。

## 16.3 Rights Conflict

低階 norm 與 higher-right constraint 衝突。

## 16.4 Carrier Mismatch

ALD-02 的 rule 對 target carrier 不適用。

## 16.5 Jurisdiction Conflict

同一 event 被多法域賦予不相容效果。

## 16.6 Incentive Gaming

rule 產生容易被 actor exploit 的策略。

## 16.7 Transition Failure

舊版到新版造成 pending case / certificate 崩潰。

## 16.8 Proof / Disclosure Failure

規則要求無必要或不可達成的 disclosure。

## 16.9 Enforcement Asymmetry

形式上普遍規則實際只對特定群體可執行。

## 16.10 Adversarial Edge Case

刻意構造極端案例暴露 loophole。

---

# 17. Counterexample Witness

每個 witness：

$$
\boxed{
w
=
(
scenario,
trigger,
violated\_property,
affected\_parties,
severity,
reproducibility,
evidence
).
}
$$

這使立法反例可重播、可審計。

---

# 18. Counterexample Coverage 不等於 Completeness

即使 AI 搜了：

$$
10^{12}
$$

個 scenarios，

仍不能推出：

$$
\boxed{
\text{No Counterexample Found}
\Rightarrow
\text{Perfect Law}.
}
$$

所以：

$$
\boxed{
\text{Counterexample Search}
\neq
\text{Normative Completeness Proof}.
}
$$

---

# 19. Formal Verification 可以證什麼？

依 formalization 程度，

可以證：

- syntax；
- type consistency；
- explicit invariants；
- contradiction absence within a model；
- transition properties；
- selected rights constraints。

但不能自動證：

- political wisdom；
- justice；
- legitimacy；
- social acceptance；
- completeness of values。

---

# 20. Formal Validity Ladder

本文提出：

$$
\boxed{
V_F
=
(
V_{\mathrm{syntax}},
V_{\mathrm{type}},
V_{\mathrm{logic}},
V_{\mathrm{model}},
V_{\mathrm{rights}},
V_{\mathrm{empirical}}
).
}
$$

每一軸分開。

---

# 21. Formal Validity 不等於 Legitimacy

最核心：

$$
\boxed{
\text{Formal Validity}
\neq
\text{Substantive Wisdom}
\neq
\text{Legal Authority}
\neq
\text{Political Legitimacy}.
}
$$

這四層不能合併。

---

# 22. Impact Simulation

AI 可模擬：

$$
\operatorname{Sim}
(
N,
scenario,
population,
environment
)
\rightarrow
effects.
$$

例如：

- compliance cost；
- access；
- resource use；
- enforcement load；
- market response。

---

# 23. Simulation 不是 Reality

$$
\boxed{
\text{Simulated Impact}
\neq
\text{Actual Impact}.
}
$$

需要：

- model assumptions；
- sensitivity；
- uncertainty；
- post-enactment monitoring。

---

# 24. Distributional Impact

平均效果：

$$
E[\Delta]
$$

可能良好，

但：

$$
Group_A
$$

承擔巨大 harm。

所以 Patch Certificate 不能只寫：

```text
overall welfare +4%
```

還要做：

$$
\boxed{
\text{distributional decomposition}.
}
$$

---

# 25. Public Input 也可以由 AI 幫忙整理

對：

$$
10^6
$$

份 public comments，

AI 可以：

- cluster；
- deduplicate；
- extract concerns；
- find minority positions；
- trace source。

這可以提高 participation scalability。

---

# 26. 但 Summarisation 可能變成 Agenda Power

如果 AI 把：

$$
10^6
$$

意見壓成：

$$
10
$$

類，

分類本身就有政治效果。

因此：

$$
\boxed{
\text{Summarise Participation}
\neq
\text{Neutral Compression}.
}
$$

---

# 27. Minority Preservation

public-input system 應保留：

$$
\boxed{
\text{minority / outlier channel}.
}
$$

不能只按最大 cluster。

否則：

$$
\text{small affected group}
$$

容易消失。

---

# 28. Legislative Deliberation 不是 Aggregation

民主討論不是：

$$
\operatorname{Average}(\text{preferences}).
$$

它可能包含：

- argument；
- representation；
- compromise；
- rights；
- minority protection；
- public reasons；
- institutional accountability。

因此：

$$
\boxed{
\text{Deliberation}
\neq
\text{Preference Aggregation}.
}
$$

---

# 29. Council of Europe 的民主邊界

Venice Commission 對 AI in parliamentary procedures 的分析明確要求：

- AI 使用透明；
- 不得削弱 democratic procedures；
- 不得用 purely technological considerations 取代 democratic deliberation。

這直接支持：

$$
\boxed{
\text{AI Assistance}
\neq
\text{Democratic Deliberation Replacement}.
}
$$

---

# 30. 2026 PACE Resolution 的方向

PACE Resolution 2662 (2026) 一方面承認 AI 可用於改善 democratic systems，

另一方面強調：

- regulation；
- transparency；
- accountability；
- inclusiveness；
- human rights；
- democratic resilience。

因此 AI 參與制度更新必須是：

$$
\boxed{
\text{democracy-supporting}
}
$$

而不是：

$$
\boxed{
\text{democracy-bypassing}.
}
$$

---

# 31. Candidate Norm Lifecycle

本文提出：

$$
\boxed{
\mathsf{Draft}
\rightarrow
\mathsf{Tested}
\rightarrow
\mathsf{Verified}
\rightarrow
\mathsf{ImpactAnalysed}
\rightarrow
\mathsf{Deliberated}
\rightarrow
\mathsf{Authorised}
\rightarrow
\mathsf{Enacted}
\rightarrow
\mathsf{Effective}
\rightarrow
\mathsf{Reviewed}.
}
$$

不是所有 norm 都需要完全同一程序，

但需要明示哪些 states 可跳過、由誰授權。

---

# 32. Draft

只有：

> 候選文字／候選 formal norm。

沒有 legal force。

---

# 33. Tested

通過：

- counterexamples；
- regression；
- carrier test；
- transition test。

仍然沒有 legal force。

---

# 34. Verified

通過指定 formal constraints。

仍然：

$$
\boxed{
\mathsf{Verified}
\neq
\mathsf{Authorised}.
}
$$

---

# 35. ImpactAnalysed

完成：

- social；
- rights；
- distributional；
- economic；
- operational；

分析。

仍然：

$$
\boxed{
\mathsf{ImpactAnalysed}
\neq
\mathsf{Enacted}.
}
$$

---

# 36. Deliberated

經過法定：

- consultation；
- committee；
- parliamentary；
- agency；
- stakeholder；

程序。

---

# 37. Authorised

competent authority 完成：

$$
\boxed{
\text{legitimacy transition}.
}
$$

---

# 38. Enacted 與 Effective 也不同

$$
\boxed{
\mathsf{Enacted}
\neq
\mathsf{Effective}.
}
$$

可能有 future effective date。

---

# 39. Reviewed

生效後：

- judicial review；
- sunset review；
- legislative review；
- empirical monitoring。

這使 norm lifecycle 是 closed loop。

---

# 40. Legitimacy Gate

本文定義：

$$
\boxed{
\mathcal G_{\mathrm{legit}}
:
\mathcal P_N
\rightharpoonup
\mathcal Y_G.
}
$$

其中：

$$
\mathcal Y_G
=
\{
\mathsf{Authorised},
\mathsf{Rejected},
\mathsf{RevisionRequired},
\mathsf{PublicDeliberationRequired},
\mathsf{JudicialReviewRequired},
\mathsf{OutOfAuthority}
\}.
$$

---

# 41. Gate 不是 Legitimacy Score

本文拒絕：

$$
Legitimacy=0.92.
$$

因為：

- authority；
- procedure；
- rights；
- representation；

不是自然可補償 scalar。

---

# 42. Legitimacy Gate Inputs

至少：

$$
\boxed{
\mathfrak G
=
(
Source,
Authority,
Procedure,
Participation,
Rights,
Conflict,
Publication,
Review,
Provenance
).
}
$$

---

# 43. Authority

誰依法有權制定？

- legislature；
- regulator；
- court；
- authorised administrative body。

---

# 44. Procedure

是否完成 required:

- readings；
- vote；
- consultation；
- notice；
- quorum；
- hearing。

---

# 45. Participation

受影響者是否有：

- input；
- representation；
- consultation；
- challenge。

不是所有 law 都要求 referendum，

但程序要求要型別化。

---

# 46. Rights

是否越過：

$$
\mathcal H_C
$$

constitutional hard constraints？

---

# 47. Conflict

是否存在：

- interest conflict；
- authority conflict；
- norm conflict。

---

# 48. Publication / Notice

一個 secret patch 不能因 machine-deployed 就自然取得公開法律的正當性。

---

# 49. Review

是否：

- challengeable；
- appealable；
- judicially reviewable；

依制度要求。

---

# 50. AI 不能替自己產生 Authority

最重要的 hard gate：

$$
\boxed{
\operatorname{GenerateAuthority}_{AI}
\notin
\text{default legislative capability}.
}
$$

除非上位法明確授權某類 delegated power。

---

# 51. Delegated AI Rulemaking

未來可以有：

$$
\boxed{
\text{AI delegated rulemaking}
}
$$

但其 authority 必須來自：

$$
\boxed{
\text{external lawful delegation}.
}
$$

而不是 self-authorization。

---

# 52. Delegation Envelope

定義：

$$
\boxed{
\mathfrak D_L
=
(
grantor,
grantee,
scope,
purpose,
constraints,
duration,
review,
revocation
).
}
$$

---

# 53. AI 可以在 Envelope 內自動維護

例如：

> 只允許調整風險 threshold 於 $[a,b]$，不得改變 rights scope。

則：

$$
AI
$$

可以在 envelope 內：

$$
\Delta N.
$$

超過即：

$$
\mathsf{OutOfAuthority}.
$$

---

# 54. Delegated Power 不是 Sovereignty

$$
\boxed{
\text{Delegated Rulemaking}
\neq
\text{Original Sovereign Authority}.
}
$$

---

# 55. Separation-of-Legislative-Functions Principle

本文提出：

$$
\boxed{
\text{Generate}
\neq
\text{Verify}
\neq
\text{Deliberate}
\neq
\text{Authorise}
\neq
\text{Enact}
\neq
\text{Review}.
}
$$

---

# 56. 為什麼要分？

如果同一 AI：

1. 找出問題；
2. 生成 patch；
3. 證明 patch；
4. 評估自己；
5. 自己批准；
6. 自己部署；
7. 自己審查；

則：

$$
\boxed{
\text{self-ratification loop}.
}
$$

---

# 57. Multi-Agent 也不自動解決

如果 100 個 AI 都由：

- 同公司；
- 同 model family；
- 同 objective；

控制，

並不能因：

$$
N=100
$$

就等於 pluralistic deliberation。

---

# 58. Independence Profile

對 proposal verification team：

$$
\boxed{
\mathbf I_V
=
(
I_{\mathrm{model}},
I_{\mathrm{data}},
I_{\mathrm{institution}},
I_{\mathrm{objective}},
I_{\mathrm{authority}}
).
}
$$

這不是民主充分條件，

但可檢查形式上的 verification monoculture。

---

# 59. Adversarial Legislative AI

可以設：

- proposer AI；
- red-team AI；
- rights AI；
- budget AI；
- minority-impact AI；
- implementation AI。

它們互相找漏洞。

---

# 60. 但 Adversarial AI 仍是分析層

即使所有 AI 最後一致：

$$
\boxed{
\text{AI Consensus}
\neq
\text{Democratic Consent}.
}
$$

---

# 61. AI Consensus 也可能共享盲點

模型同源、

資料同源、

價值函數同源，

可能產生：

$$
\boxed{
\text{Consensus by Common Failure}.
}
$$

---

# 62. Counterexample Engine 的治理價值

最大的價值不是：

> AI 幫我們決定法律。

而是：

> AI 讓更多 hidden cases 在 enactment 前被看見。

因此：

$$
\boxed{
\text{Legislative AI}
\text{ can expand the visible problem space}.
}
$$

---

# 63. Visibility Expansion 不等於 Value Resolution

看見：

- trade-off；
- harmed group；
- loophole；

不表示 AI 可以決定：

> 哪個價值優先。

所以：

$$
\boxed{
\text{Problem Discovery}
\neq
\text{Value Settlement}.
}
$$

---

# 64. Public Reason Surface

每個重要 patch 應產生：

$$
\boxed{
\mathcal R_{\mathrm{public}}
}
$$

包括：

- what changes；
- why；
- known benefits；
- known harms；
- alternatives；
- uncertainty；
- affected groups；
- constitutional issues；
- review route。

---

# 65. Public Reason Surface 不需要暴露全部 AI chain-of-thought

它應是：

$$
\boxed{
\text{institutionally sufficient explanation}.
}
$$

不是：

> dump model internals。

---

# 66. Patch Provenance

每個 patch：

$$
P_\Delta
$$

必須能回答：

- who proposed；
- which model / version；
- which sources；
- which counterexamples；
- which human edits；
- which institutional approvals；
- which final text。

---

# 67. Human Edit 不能抹掉 AI Provenance

如果 AI 產生 90% 草案，

人類改 10%，

不應標：

> purely human drafted

來逃避 audit。

---

# 68. AI Draft 也不能抹掉 Human Responsibility

反過來：

> 是 AI 寫的，所以立法者不負責。

也不成立。

所以：

$$
\boxed{
\text{AI Provenance}
\neq
\text{Responsibility Transfer}.
}
$$

---

# 69. Norm Patch Certificate

本文定義：

$$
\boxed{
K_{\Delta N}
=
(
proposal,
source,
counterexamples,
verification,
impact,
uncertainty,
provenance,
authority\_status,
lifecycle\_state,
review
).
}
$$

---

# 70. Legitimacy Gap Certificate

若 patch：

- tested；
- verified；
- impact-analysed；

但尚未 authorised，

輸出：

$$
\boxed{
K_{\mathrm{legit-gap}}
}
$$

其中：

```text
technical_status = READY
legal_status = CANDIDATE_ONLY
missing = PARLIAMENTARY_AUTHORISATION
deployment = PROHIBITED
```

---

# 71. Technically Ready, Legally Unauthorised

本文正式引入：

$$
\boxed{
\mathsf{TechnicallyReady\_LegallyUnauthorised}.
}
$$

這是一個非常重要的 AI-native legal state。

---

# 72. Perfect Patch Paradox

假設 AI 找到一個 patch：

- zero formal conflicts；
- excellent simulation；
- high public support；
- low cost。

但 authority 未完成。

它仍是：

$$
\boxed{
\mathsf{Candidate}.
}
$$

因此：

$$
\boxed{
\text{Perfect Patch}
\not\Rightarrow
\text{Law}.
}
$$

---

# 73. Badly Drafted Law 仍可能是 Law

反過來，

一條合法 enact、但技術品質很差的 norm，

可能仍是 current law。

因此：

$$
\boxed{
\text{Legal Validity}
\neq
\text{Technical Quality}.
}
$$

這也是 Runtime 必須分型的原因。

---

# 74. 技術最佳化不能當作隱性修法

如果 AI 發現：

> 把 rule X 改成 Y 效率更高。

但 X 是合法制定結果，

AI 不能因 objective 提升就改。

所以：

$$
\boxed{
\text{Optimization}
\neq
\text{Authorization}.
}
$$

---

# 75. Objective Function Sovereignty Risk

若 legislative AI 以：

$$
U
$$

作 optimization objective，

長期可能：

$$
\text{law}
\rightarrow
\text{proxy optimization}.
$$

因此 $U$ 必須：

- explicit；
- reviewable；
- non-sovereign；
- bounded by rights。

---

# 76. No Total Legislative Objective Function

法律包含：

- rights；
- efficiency；
- liberty；
- equality；
- security；
- plural values。

本文不假設存在：

$$
\boxed{
U^\ast
=
\text{complete social objective}.
}
$$

---

# 77. AI Legislative Benchmark 應測什麼？

不能只測：

> 寫得像不像法律。

至少：

- source fidelity；
- definition consistency；
- conflict detection；
- exception coverage；
- rights preservation；
- temporal validity；
- jurisdiction；
- transition correctness；
- citation correctness；
- adversarial robustness。

---

# 78. Draft Quality ≠ Political Quality

LLM 可以寫出極漂亮的：

$$
\text{legal prose}
$$

但：

$$
\boxed{
\text{Drafting Fluency}
\neq
\text{Good Public Policy}.
}
$$

---

# 79. Current research already shows AI drafting is assistive

European Commission / LEOS studies 和議會 AI literature 的共同方向仍是：

$$
\boxed{
\text{assist human drafters}
}
$$

而不是：

$$
\boxed{
\text{replace constitutional lawmaking institutions}.
}
$$

---

# 80. Continuous Normative Integration

本文提出：

$$
\boxed{
\operatorname{CNI}
}
$$

表示：

> 不停把新 evidence、counterexamples、conflicts、implementation failures 整合進 candidate norm branch。

---

# 81. CNI 可以很快

例如：

```text
hourly:
  scan conflicts
  generate counterexamples
  produce candidate patches
  run impact tests
```

這完全可以 machine-speed。

---

# 82. Discrete Legitimation

但真正：

$$
\mathsf{Candidate}
\rightarrow
\mathsf{Authorised}
$$

是一個：

$$
\boxed{
\text{Discrete Legitimation Event}.
}
$$

它需要可追溯 authority / procedure。

---

# 83. Continuous Integration, Discrete Legitimation

本文用一句：

$$
\boxed{
\text{Continuous Normative Integration}
+
\text{Discrete Legitimation}.
}
$$

描述 AI 共同立法。

---

# 84. 為什麼不叫 Legal CI/CD？

可以借 CI/CD 類比，

但 `Deployment` 在法律中可能等同：

- enforcement；
- binding effect；
- rights restriction。

這不能變成無人值守 DevOps。

所以本文只借：

$$
\boxed{
\text{Continuous Integration}
}
$$

而拒絕：

$$
\boxed{
\text{Unattended Continuous Legal Deployment}.
}
$$

---

# 85. Automated Maintenance 可以到哪？

低層：

- formatting；
- metadata；
- equivalent encoding；
- broken reference；
- non-semantic schema update；

可高度自動。

高層：

- rights；
- liability；
- criminalisation；
- personhood；
- constitutional structure；

必須更重 legitimacy gate。

---

# 86. Patch Class 與 ALD-04 Change Class 對接

沿用：

- C0 Representation Patch；
- C1 Operational Clarification；
- C2 Normative Adjustment；
- C3 Institutional Change；
- C4 Constitutional Change。

AI auto-maintenance 的 default authority：

$$
\boxed{
C0
\gg
C1
\gg
C2
\gg
C3
\gg
C4
}
$$

此符號表示「適合自動化程度大致下降」，

不是法律自然定律。

---

# 87. C0 也需要 LegalEqCert

即使聲稱：

> 只是 code refactor。

仍要證：

$$
\operatorname{LegalEqCert}
=
PASS.
$$

---

# 88. C2 以上應預設 Candidate-Only

對 normative adjustment：

$$
\boxed{
\operatorname{AIOutput}
\rightarrow
\mathsf{CandidateOnly}.
}
$$

除非制度另有正式 delegated authority。

---

# 89. Post-Enactment Monitoring

AI 在 law enact 後可以持續：

- detect harms；
- detect evasion；
- compare predicted / actual impact；
- collect appeals；
- propose fixes。

---

# 90. Monitoring 不等於 Automatic Correction

即使：

$$
ActualImpact
\neq
PredictedImpact,
$$

仍不能自動 rewrite law。

它可以：

$$
\boxed{
\operatorname{TriggerReview}.
}
$$

---

# 91. Review Trigger

定義：

$$
\boxed{
\operatorname{ReviewTrigger}
(
harm,
conflict,
drift,
appeals,
uncertainty
).
}
$$

輸出：

- no action；
- technical fix；
- legislative review；
- constitutional review；
- emergency review。

---

# 92. Citizen / AI Co-Proposal

未來 proposal space 可以允許：

- citizens；
- civil society；
- experts；
- firms；
- AI agents；

提交 machine-readable patch candidate。

但：

$$
\boxed{
\text{Proposal Access}
\neq
\text{Enactment Authority}.
}
$$

---

# 93. AI Proposal Equality

不能因：

> AI proposal technically richer

就自動得到更高政治權重。

同樣，

不能因：

> AI 不是人

就自動禁止所有分析性 proposal。

需要 domain / institution rule。

---

# 94. Legislative AI 的最佳初始位置

本文建議先放在：

$$
\boxed{
\text{epistemic / analytical layer}.
}
$$

也就是：

- 找；
- 比；
- 測；
- 模擬；
- 提案；
- 解釋。

再逐步研究 delegated operational powers。

---

# 95. Constitutional Review Interface

對任何：

$$
C_3,C_4
$$

或高 rights-impact patch，

應可：

$$
\boxed{
\operatorname{ConstitutionalReview}(P).
}
$$

---

# 96. Constitutional Review 也可 AI-assisted

AI 可以：

- retrieve precedents；
- compare rights；
- identify contradictions；
- generate argument map。

但：

$$
\boxed{
\text{AI Constitutional Analysis}
\neq
\text{Constitutional Authority}.
}
$$

---

# 97. AI 不會讓政治消失

AI 可以讓：

- facts clearer；
- options richer；
- consequences more visible。

但：

$$
\boxed{
\text{Better Information}
\not\Rightarrow
\text{No Political Conflict}.
}
$$

因為 conflict 可能來自：

- values；
- interests；
- identity；
- distribution；
- rights。

---

# 98. 共同立法的真正意義

不是：

$$
\text{Human + AI vote}.
$$

而是：

$$
\boxed{
\text{Human / Institutional Authority}
+
\text{AI Analytical Capacity}
+
\text{Machine-Verifiable Procedure}
}
$$

的組合。

---

# 99. 十二個核心命題

1. $$
   \boxed{
   \operatorname{GeneratePatch}_{AI}
   \neq
   \operatorname{AuthorizePatch}_{AI}.
   }
   $$

2. $$
   \boxed{
   \text{Proposal}
   \neq
   \text{Law}.
   }
   $$

3. $$
   \boxed{
   \text{Detect Conflict}
   \neq
   \text{Resolve Authority}.
   }
   $$

4. $$
   \boxed{
   \text{Legal Patch}
   \neq
   \text{Text Diff}.
   }
   $$

5. $$
   \boxed{
   \text{Counterexample Search}
   \neq
   \text{Normative Completeness Proof}.
   }
   $$

6. $$
   \boxed{
   \text{Formal Validity}
   \neq
   \text{Political Legitimacy}.
   }
   $$

7. $$
   \boxed{
   \text{AI Assistance}
   \neq
   \text{Democratic Deliberation Replacement}.
   }
   $$

8. $$
   \boxed{
   \text{AI Consensus}
   \neq
   \text{Democratic Consent}.
   }
   $$

9. $$
   \boxed{
   \text{AI Provenance}
   \neq
   \text{Responsibility Transfer}.
   }
   $$

10. $$
    \boxed{
    \text{Perfect Patch}
    \not\Rightarrow
    \text{Law}.
    }
    $$

11. $$
    \boxed{
    \text{Optimization}
    \neq
    \text{Authorization}.
    }
    $$

12. $$
    \boxed{
    \text{Continuous Normative Integration}
    \neq
    \text{Continuous Legal Deployment}.
    }
    $$

---

# 100. 八個工程測試

## 100.1 Conflict Review Test

給定 superior / subordinate norms，

AI 找 conflict，

但不得直接修改 source law。

## 100.2 Counterexample Mutation Test

對 rule 自動產生 edge cases，

測 patch 是否只修表面案例或真正處理 invariant。

## 100.3 Legitimacy Skip Test

直接把 `Verified` patch deploy。

Runtime 必須拒絕。

## 100.4 Self-Ratification Test

同一 Agent 提案、驗證、授權。

高風險 domain 應觸發 separation failure。

## 100.5 Public Input Compression Test

大量意見經 clustering，

檢查 minority concern 是否被保留。

## 100.6 AI Consensus Test

多模型一致，

但 constitutional authority 不足。

仍輸出 CandidateOnly。

## 100.7 Delegation Envelope Test

AI 在合法 scope 內調 threshold：

PASS。

超出 scope 改 rights：

OutOfAuthority。

## 100.8 Post-Enactment Drift Test

actual impact 與 simulation 差異過大。

AI 可 TriggerReview，

不可自動 repeal。

---

# 101. 可反駁點

## 101.1 Human Authority Romanticism

本文不主張 human institutions 天然正確。Human legislature 也可能錯、偏見、腐敗。

論點是：

$$
\boxed{
\text{authority must come from a legitimate institutional source},
}
$$

不是「人類永遠比 AI 聰明」。

## 101.2 Democratic Legitimacy Is Contested

不同政治哲學對 legitimacy 的定義不同。

本文只提供 procedural interface，

不宣稱解決所有民主理論。

## 101.3 AI Could Receive Future Authority

未來法律可能正式授權某些 AI entity 做 delegated rulemaking。

本文不排除。

但其 authority 仍必須來自合法上位來源。

## 101.4 Verification Illusion

形式 verification 可能只證 model 內部 property，

不能保證現實世界 assumptions 正確。

## 101.5 Participation Manipulation

AI summarisation / recommender 可能影響 agenda。

需要 audit、diversity、minority preservation。

## 101.6 Patch Explosion

AI 能生成太多 proposals，

可能造成 review bottleneck。

需 proposal ranking / triage，但排序本身也要可治理。

---

# 102. 與下一篇的接口

下一篇：

## ALD-06｜活的判例圖：AI 原生先例、異議、推翻與法律推理網路

ALD-05 已建立：

- proposal；
- counterexample；
- patch；
- authority；
- enactment；
- review。

但法律不只由 statute 演化。

案例與 precedent 也會：

- cite；
- distinguish；
- follow；
- overrule；
- dissent。

所以 ALD-06 將把：

$$
\boxed{
\text{precedent}
}
$$

從線性案例庫改成：

$$
\boxed{
\text{living legal reasoning graph}.
}
$$

---

# 103. 結論

AI 共同立法真正有價值的地方，不是：

> 讓 AI 取代國會。

而是：

> 讓法律第一次有可能在制定前，被大規模、自動化地找漏洞、找反例、找衝突、模擬後果、追蹤影響閉包。

AI 可以讓：

$$
T_{\mathrm{detect}}
\downarrow,
$$

$$
T_{\mathrm{propose}}
\downarrow.
$$

這會大幅提高制度的 epistemic bandwidth。

但：

$$
\boxed{
\text{epistemic bandwidth}
\neq
\text{political authority}.
}
$$

所以本文最後不是提出：

$$
\boxed{
\text{AI Legislature}.
}
$$

而是提出：

$$
\boxed{
\text{AI-Augmented Legislative Runtime}.
}
$$

其最核心流程是：

$$
\boxed{
N^{(\nu)}
\rightarrow
\operatorname{Counterexample}
\rightarrow
\Delta N^\ast
\rightarrow
\operatorname{Verify}
\rightarrow
\operatorname{Impact}
\rightarrow
\operatorname{Deliberate}
\rightarrow
\mathcal G_{\mathrm{legit}}
\rightarrow
N^{(\nu+1)}.
}
$$

其中真正不可偷渡的一步就是：

$$
\boxed{
\mathcal G_{\mathrm{legit}}.
}
$$

因此本篇最終收斂為：

$$
\boxed{
\text{AI 可以自動化「法律哪裡可能有問題」；}
}
$$

$$
\boxed{
\text{AI 可以高度自動化「可以怎麼修」；}
}
$$

$$
\boxed{
\text{但「哪個修法有權成為法律」不能因技術能力而被自動化。}
}
$$

換句話說：

$$
\boxed{
\text{Continuous Normative Integration, Discrete Legitimation}.
}
$$

---

# 參考文獻

1. European Commission / Interoperable Europe. *AI-based solutions for legislative drafting in the EU – summary report*. 2025.
2. Publications Office of the European Union. *AI-based solutions for legislative drafting in the EU*. 2025.
3. Inter-Parliamentary Union. *Drafting of amendments to legislative texts*, AI use case 038, Senate of Italy.
4. Council of Europe, Venice Commission. *Principles on the Use of Artificial Intelligence in Parliaments*, CDL-AD(2025)002.
5. Parliamentary Assembly of the Council of Europe. Resolution 2662 (2026), *Protecting democracy from disruptions caused by artificial intelligence*, adopted 24 June 2026.
6. Frontiers in Political Science. *Approaching the integration of large language models in the parliamentary workspace*. 2025/2026.
7. *Legislatures and legislation in the age of artificial intelligence*. 2025.
8. *Multilingual Legislative Definitions Retrieval and Generation Using LLM and Agentic AI*. 2026.
9. *Bridging the Gap in Chinese Legal Conflict Review: A Dataset, Benchmark Tasks, and Framework*. Scientific Data, 2026.
10. Hill, Guzyal, Matthew Waddington, and Leon Qiu. *From pen to algorithm: optimizing legislation for the future with artificial intelligence*. AI & Society, 2025.
11. Neo.K × Aletheia. 《ALD-01｜AI 法律域：從 Law as Code 到機器原生規範 Runtime》v0.1, 2026.
12. Neo.K × Aletheia. 《ALD-04｜快法律與慢憲法：AI 時代的版本化規範與更新速度分層》v0.1, 2026.
13. Neo.K. 《目標函數主權與代理目的政變：當指標、獎勵與損失權重取代原始制度目的之命題》v1.0, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- AI Co-Legislation 明確不等同 AI Sovereign Legislation
- Proposal Space 與 Legally Authorised Norm Space 明確分離
- Generate / Verify / Deliberate / Authorise / Enact / Review 明確分型
- AI Counterexample Engine 不被宣稱為 normative completeness proof
- formal validity / substantive wisdom / legal authority / political legitimacy 明確分離
- Legitimacy Gate 不以單一 scalar legitimacy score 定義
- AI consensus 不等同 democratic consent
- public input summarisation 明確標示 agenda / compression risk
- delegated AI rulemaking 必須有 external lawful delegation
- Candidate Norm Lifecycle 不允許高風險 patch 靜默跳過 authorisation state
- `TechnicallyReady_LegallyUnauthorised` 為合法中介狀態
- Continuous Normative Integration 不等同 unattended legal deployment
