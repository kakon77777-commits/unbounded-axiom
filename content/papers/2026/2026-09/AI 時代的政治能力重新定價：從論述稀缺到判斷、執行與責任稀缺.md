---
title: "AI 時代的政治能力重新定價：從論述稀缺到判斷、執行與責任稀缺"
english_title: "The Repricing of Political Competence in the AI Era: From Scarce Rhetoric to Scarce Judgment, Execution, and Accountability"
series: "AI-Native Longitudinal Actor Intelligence"
author: "Neo.K"
institution: "EveMissLab／一言諾科技有限公司"
paper: "05"
version: "v0.1"
date: "2026-08-28"
language: "zh-TW"
status: "Working Paper / Canonical UTF-8 Source"
scope_note: "本文分析的是政治能力的相對稀缺性與任務重新配置，不主張 AI 將整體取代政治人物。"
---

# AI 時代的政治能力重新定價：從論述稀缺到判斷、執行與責任稀缺

**The Repricing of Political Competence in the AI Era: From Scarce Rhetoric to Scarce Judgment, Execution, and Accountability**

**AI-Native Longitudinal Actor Intelligence Series — Paper 05**

## 摘要

民主政治長期高度獎勵若干可見且稀缺的認知與語言能力：快速理解複雜議題、記憶大量政策細節、跨領域整合資訊、形成有說服力的論證、在媒體壓力下即時反駁，以及把專家知識轉換成一般選民可以理解的語言。這些能力在前生成式 AI 時代具有顯著政治溢價，因為其人力取得成本高、複製速度慢、專業幕僚稀缺，而且選民與媒體通常缺乏低成本手段檢查長時序一致性。

本文提出「政治能力重新定價」（Repricing of Political Competence, RPC）框架，分析生成式 AI、代理式 AI、長時序政治資料庫與 AI-native government tools 如何改變不同政治能力的相對稀缺性。核心主張不是「AI 讓口才不重要」，而是：當資訊檢索、政策摘要、跨領域 briefing、草稿生成、反方論證、媒體訊息適配、語言翻譯與部分說服任務的邊際成本下降後，這些能力作為政治人物個人稀缺資產的相對價值將下降。相對地，難以由 AI 單獨承擔的 judgment、authority、priority setting、coalition building、organizational coupling、execution、trust、legitimacy 與 outcome ownership 將成為更重要的政治稀缺品。

本文以 task-based approach 建立能力暴露矩陣，區分可被 AI substitute、augment、commoditize 與 revalue 的政治任務。近年研究已證明 LLM 可以快速、大規模產生具政治說服力的訊息；多輪人機對話甚至可在選舉情境中對候選人偏好產生顯著影響。2026 年政治與民主研究開始直接以勞動經濟學的 task-based framework 分析 AI 對競選、選務、社會運動與公民審議的替代與增強效果。與此同時，OECD 2025–2026 的政府 AI 研究指出，AI 已廣泛進入公共部門內部流程、服務與決策支援，但治理、採購、資料、透明、責任與組織能力仍是能否真正擴張的主要瓶頸。

本文因此提出「能力價格」的操作性概念：一項政治能力的相對價值取決於其稀缺性、可替代性、互補性、可驗證性、責任強度與治理影響。本文並預測，AI 時代將產生三種政治人物分化：第一，語言型明星的相對溢價下降；第二，能將 AI、專家、官僚與公民回饋整合成閉環治理的 AI-augmented executive 升值；第三，政治可信度與責任所有權因長時序 AI 稽核而成為更昂貴的資產。

本文最終提出：

$$
Political\ Advantage_{AI}
\neq
Who\ speaks\ fastest
$$

而更接近：

$$
Political\ Advantage_{AI}
=
Judgment
+
Execution
+
Coordination
+
Trust
+
Accountability
+
AI\ Integration
$$

AI 並未終結政治領導，而是改變政治領導中什麼東西值得稀缺溢價。

**關鍵詞：** 人工智慧、政治能力、政治領導、能力重新定價、生成式 AI、政治說服、task-based approach、行政執行、政治責任、AI-native governance

---

## Abstract

Democratic politics has historically rewarded several visible and scarce cognitive-linguistic capacities: rapid comprehension of complex issues, memory for policy details, cross-domain synthesis, persuasive argumentation, real-time rebuttal, and translation of expert knowledge into accessible public language. Before generative AI, these capabilities carried substantial political premiums because they were expensive to acquire, difficult to replicate, and dependent on scarce human staff.

This paper introduces the Repricing of Political Competence (RPC) framework. Rather than asking whether AI will replace politicians, RPC asks how AI changes the relative scarcity and political value of specific tasks and capabilities. As information retrieval, policy summarization, briefing synthesis, drafting, counterargument preparation, message adaptation, translation, and parts of persuasion become cheaper and more scalable, their value as uniquely human political assets may decline. In contrast, judgment, authority, prioritization, coalition building, organizational coupling, execution, trust, legitimacy, and outcome ownership become relatively more valuable because AI cannot independently supply democratic authority or bear political responsibility.

The paper develops a task-based competence exposure matrix distinguishing substitution, augmentation, commoditization, and revaluation. Evidence from recent research shows that LLM-generated political messages can persuade humans at scale, and interactive AI dialogue can shift candidate preferences in real election contexts. Research on AI and democracy is increasingly applying task-based labor-economic frameworks to campaigns, election administration, movements, and deliberation. OECD work on AI in government likewise shows growing use of AI in internal operations, public services, forecasting, and decision support, while organizational capacity, governance, transparency, procurement, and accountability remain major constraints on scaling.

The central claim is that AI does not eliminate political leadership. It alters which competencies receive scarcity premiums. In an AI-rich environment, political advantage is increasingly expected to depend on judgment, execution, coordination, trust, accountability, and the capacity to integrate AI into legitimate governing systems.

---

# 1. 問題不是「AI 會不會取代政治人物」

這個問題太粗。

政治人物不是一個單一 task。

一名政治人物同時進行：

- 閱讀；
- 聽取幕僚報告；
- 形成政策判斷；
- 公開演說；
- 接受採訪；
- 募款；
- 組織政黨；
- 聯盟協商；
- 任命；
- 預算排序；
- 危機決策；
- 行政監督；
- 承擔責任；
- 代表國家或城市。

因此：

$$
Politician
\neq
Single\ Occupation\ Task
$$

真正有意義的問題是：

$$
Which\ political\ tasks\ become\ cheaper?
$$

以及：

$$
Which\ political\ tasks\ become\ more\ valuable\ because\ other\ tasks\ become\ cheaper?
$$

這就是本文的 repricing 問題。

---

# 2. 能力價格不是薪資，而是相對政治稀缺性

本文定義某一政治能力 $k$ 在時間 $t$ 的相對能力價格：

$$
\Pi_k(t)
$$

它不是市場薪資，而是：

> 該能力對取得政治優勢、治理成果、選民信任與組織控制所帶來的相對邊際價值。

可粗略寫為：

$$
\Pi_k=
f(
Scarcity,
Substitutability,
Complementarity,
Visibility,
Verifiability,
Impact,
Responsibility
)
$$

其中：

- Scarcity：有多少競爭者擁有；
- Substitutability：AI 或組織能否低成本替代；
- Complementarity：AI 是否反而提高該能力回報；
- Visibility：選民與媒體是否能觀察；
- Verifiability：能否被長時序資料驗證；
- Impact：對治理結果影響；
- Responsibility：該能力是否伴隨不可轉移的權責。

---

# 3. 前 AI 時代的政治明星為什麼值錢？

過去政治人物若可以：

$$
Complex\ Issue
\rightarrow
Immediate\ Structured\ Answer
$$

本身就是能力訊號。

因為這代表他可能具有：

$$
Memory
+
Knowledge
+
Synthesis
+
Language
+
Confidence
$$

同時還意味其背後可能有：

$$
Staff\ Capacity
$$

在傳統媒體時代，選民缺乏能力快速驗證每個細節。

因此「能即時說得完整」容易成為：

$$
Competence\ Signal
$$

並被進一步投影為：

$$
Leadership\ Signal
$$

Paper 02 已指出，這個投影可能造成 Discourse–Execution Gap。

Paper 05 的問題是：

> 當 AI 使 discourse production 變得普及後，這個 signal 還值多少？

---

# 4. AI 首先降低的是資訊加工成本

生成式 AI 對政治最直接的影響不是自動當總統，而是降低：

$$
C_{retrieval}
$$

$$
C_{summarization}
$$

$$
C_{translation}
$$

$$
C_{drafting}
$$

$$
C_{comparison}
$$

$$
C_{counterargument}
$$

$$
C_{briefing}
$$

這些成本。

因此，原先需要：

$$
Large\ Staff
+
Time
+
Expertise
$$

才能完成的工作，逐漸可以由：

$$
Small\ Team
+
AI
$$

完成。

這不等於品質自動相同。

但意味：

$$
Marginal\ Cost\downarrow
$$

。

當供給增加，稀缺溢價就可能下降。

---

# 5. AI 已經具備政治說服能力

政治語言不能被當成 AI 完全不會的高階人類專屬領域。

Bai 等人在 2025 年的三個預註冊實驗、總樣本 $N=4829$ 中發現，LLM 生成的政策說服訊息能顯著改變受試者態度，其整體效果與一般人類撰寫訊息相近。研究特別指出，AI 訊息的說服力與受試者感受到的 facts、evidence、logic 與 dispassionate voice 有關。

更進一步，Lin 等人 2025 年在美國、加拿大與波蘭選舉情境中測試人類與 AI 的多輪政治對話，發現 AI 對話能顯著改變候選人偏好，效果甚至高於傳統政治影片廣告常見效果。

因此：

$$
Political\ Persuasion
\notin
Purely\ Human\ Domain
$$

。

---

# 6. 「會說理」正在從人格資產變成基礎設施

如果每個候選人都可以使用 AI：

$$
Question
\rightarrow
Issue\ Map
\rightarrow
Evidence
\rightarrow
Counterargument
\rightarrow
Talking\ Points
$$

那麼：

$$
Can\ Generate\ Structured\ Argument
$$

本身就不再具有原先那麼高的訊號價值。

這不是說選民不在乎口才。

而是：

$$
Scarcity(Rhetorical\ Preparation)\downarrow
$$

。

政治人物真正的差別會逐漸變成：

> 這套論述是不是他真正理解？

> 他能不能在不確定資訊下做選擇？

> 他會不會被自己的 AI briefing 誤導？

> 他是否能在利益衝突下維持原則？

---

# 7. AI 對政治能力有四種不同作用

本文區分：

$$
Substitute
$$

$$
Augment
$$

$$
Commoditize
$$

$$
Revalue
$$

。

## 7.1 Substitute

AI 可以直接完成大部分 task。

例如：

$$
Speech\ Drafting
$$

## 7.2 Augment

AI 提高人的產出。

例如：

$$
Policy\ Analysis
+
AI
\rightarrow
Faster\ Scenario\ Comparison
$$

## 7.3 Commoditize

能力仍重要，但幾乎人人取得。

例如：

$$
Basic\ CrossDomain\ Briefing
$$

## 7.4 Revalue

因為其他能力被商品化，某些能力相對更值錢。

例如：

$$
Judgment
$$

$$
Trust
$$

$$
Execution
$$

。

---

# 8. Task-Based Political Competence Matrix

令政治任務集合：

$$
T=
\{
t_1,\ldots,t_n
\}
$$

對每個 task 定義：

$$
X_t=
(
AIExposure,
Substitution,
Complementarity,
AuthorityNeed,
HumanTrustNeed,
AccountabilityLoad
)
$$

例如：

| 任務 | AI 暴露 | 可替代 | 可增強 | 權威需求 | 責任負荷 |
|---|---:|---:|---:|---:|---:|
| 政策摘要 | 高 | 高 | 高 | 低 | 低 |
| 演說草稿 | 高 | 高 | 高 | 低 | 低 |
| 即時反駁 | 高 | 中高 | 高 | 低 | 低 |
| 民調／輿情分析 | 高 | 中高 | 高 | 低 | 中 |
| 政策方案比較 | 高 | 中 | 高 | 中 | 中 |
| 任命高階官員 | 中 | 低 | 中 | 高 | 高 |
| 預算優先順序 | 中 | 低 | 高 | 高 | 高 |
| 聯盟協商 | 中 | 低 | 高 | 高 | 高 |
| 危機決策 | 中高 | 低 | 高 | 高 | 極高 |
| 承擔失敗 | 低 | 極低 | 低 | 極高 | 極高 |

這張矩陣就是 repricing 的起點。

---

# 9. AI 時代的「知道很多」會重新定義

以前：

$$
Knowledge_{person}
$$

是重要資產。

未來更可能是：

$$
KnowledgeAccess_{person+AI}
$$

。

因此真正稀缺的能力會變成：

$$
Question\ Formation
$$

$$
Evidence\ Discrimination
$$

$$
Model\ Selection
$$

$$
Uncertainty\ Handling
$$

$$
Decision\ Commitment
$$

而不是純粹：

$$
Fact\ Recall
$$

。

---

# 10. Policy Briefing 的政治溢價下降

候選人能在短時間談：

- 能源；
- 財政；
- 國防；
- 教育；
- 房價；
- 科技；

過去會被認為是 rare generalist。

但如果幕僚能以 AI 在十分鐘內準備：

$$
Issue\ Summary
+
History
+
Budget
+
Opposition
+
International\ Comparison
$$

則：

$$
Surface\ Generalism
$$

變得更容易生產。

所以：

$$
Briefing\ Assimilation
$$

仍然重要，

但：

$$
Briefing\ Generation
$$

的稀缺性下降。

---

# 11. 媒體即時戰的能力也會商品化

傳統政治人物常因：

$$
Fast\ Response
$$

而形成明星效果。

AI 可以：

$$
Opponent\ Statement
\rightarrow
Claim\ Extraction
\rightarrow
Fact\ Retrieval
\rightarrow
Counterframe
\rightarrow
Response\ Draft
$$

政治組織未來甚至可以在對手發言完成前後幾分鐘內準備多版本反擊。

因此：

$$
Response\ Latency\downarrow
$$

當所有人都很快，「快」本身的競爭優勢下降。

---

# 12. 競選活動正在 AI 化

Flanigan、Foos、Fung 與 Stewart 在 2026 年以 task-based framework 分析 AI 與民主，指出生成式 AI 已能加速競選內容生產，並具有高度政治說服潛力；其影響取決於組織整合、競爭動態、監管與政治領導，而不是模型能力本身。

2026 年美國期中選舉期間，已有競選團隊使用 AI 進行社群趨勢感知、選民反應模擬與內容生成。

因此未來競選團隊的差異不會只是：

$$
Has\ AI?
$$

而是：

$$
How\ deeply\ AI\ is\ integrated\ into\ decision\ loops?
$$

。

---

# 13. AI 讓小團隊取得過去大團隊的部分能力

傳統政治競選有顯著規模優勢：

$$
Money
\rightarrow
Staff
\rightarrow
Research
\rightarrow
Content
$$

AI 可能降低部分 scale barrier：

$$
Small\ Campaign
+
AI
\rightarrow
Research/Content\ Capacity\uparrow
$$

這可能：

1. 降低新政治人物進入門檻；
2. 增加訊息競爭；
3. 提高政治內容供給；
4. 同時增加低成本 manipulation。

所以：

$$
Democratization\ of\ Capacity
$$

與：

$$
Industrialization\ of\ Propaganda
$$

可以同時發生。

---

# 14. AI 不只幫政治人物，也幫對手

能力重新定價是雙向的。

政治人物可以用 AI：

$$
Generate
$$

對手與媒體也可以用 AI：

$$
Audit
$$

。

因此：

$$
Message\ Production\ Cost\downarrow
$$

同時：

$$
Contradiction\ Detection\ Cost\downarrow
$$

$$
Archive\ Search\ Cost\downarrow
$$

$$
Policy\ Outcome\ Matching\ Cost\downarrow
$$

。

Paper 04 的 Diligent AI 就是後者。

這會削弱「說完後大家會忘」的傳統政治優勢。

---

# 15. 語義自由度可能下降

前 AI 時代，政治人物可以透過：

$$
Qualification
+
Scope\ Change
+
Reframing
+
Context\ Shift
$$

維持高度語言彈性。

當長時序 AI 可以即時重建：

$$
Statement_{t_1}
\leftrightarrow
Statement_{t_2}
\leftrightarrow
Action_{t_3}
$$

語言重框仍然可行，但更容易被檢驗。

因此：

$$
Semantic\ Degrees\ of\ Freedom\downarrow
$$

不是因為語言變簡單，而是因為：

$$
Audit\ Capacity\uparrow
$$

。

---

# 16. 所以政治可信度會升值

如果所有人都能生成漂亮文稿：

$$
Beautiful\ Statement
$$

的訊號價值下降。

選民與機構會更需要：

$$
Is\ this\ actor\ reliable\ over\ time?
$$

因此：

$$
Trust
$$

從模糊人格詞彙，逐步變成可以由：

- 承諾；
- 行動；
- 結果；
- 修正；
- attribution consistency；

長期估計的資產。

Paper 03 的 CBRA 使此類估計開始可操作化。

---

# 17. Judgment 是 AI 時代政治人物的核心稀缺能力之一

AI 可以輸出：

$$
Option_A
$$

$$
Option_B
$$

$$
Option_C
$$

甚至估計：

$$
P(Outcome_i\mid Option_j)
$$

但政治首長仍需要：

$$
Choose
$$

。

這個選擇通常包含：

- 不完整資訊；
- 價值衝突；
- 分配效果；
- 法律限制；
- 政治風險；
- 不可逆性；
- 道德責任。

因此：

$$
Decision\ Support
\neq
Decision\ Authority
$$

。

---

# 18. Authority 不能由 AI 直接供給

民主政治中的權威不是：

$$
Best\ Prediction
$$

而是：

$$
Legitimate\ Mandate
$$

。

AI 可以推薦：

> 加稅 3% 是財政最優。

但真正作成決定需要：

$$
Legal\ Authority
+
Democratic\ Legitimacy
+
Political\ Responsibility
$$

因此 authority-heavy tasks 具有低 AI substitutability。

---

# 19. Accountability 是不可外包的政治稀缺品

政治人物可以說：

> AI 建議我這樣做。

但：

$$
AI\ Recommendation
\nRightarrow
AI\ Responsibility
$$

。

尤其高風險決策中：

$$
Human\ Authority
\rightarrow
Human\ Accountability
$$

仍然是民主治理核心。

OECD 2026 在討論政府 agentic AI 時特別強調 traceable decision trails、meaningful accountability、user control，以及可暫停、逆轉、挑戰自動化行動的重要性。

這表示 AI 越強：

$$
Accountability\ Design
$$

反而越重要。

---

# 20. Execution 的相對價值上升

如果政策設計變便宜，但落地仍困難：

$$
Policy\ Proposal\ Supply\uparrow
$$

而：

$$
Implementation\ Capacity
$$

沒有同比例增加，

則：

$$
Relative\ Value(Execution)\uparrow
$$

。

這就是 Paper 02 的 DEG 在 AI 時代的放大版本。

未來可能出現：

$$
Many\ Excellent\ Plans
$$

但仍只有少數政治人物能做到：

$$
Plan
\rightarrow
Organization
\rightarrow
Budget
\rightarrow
Delivery
$$

。

---

# 21. OECD 的政府 AI 資料支持「瓶頸轉移」

OECD 2026 Digital Government Outlook 顯示，35/36 個受調 OECD 國家已至少在一個政府領域使用 AI。

但 AI 使用最成熟的仍主要是：

- 內部流程；
- 公共服務；

而在 policymaking 與 oversight 中較有限。

同時，跨國資料顯示：

- AI 訓練普及；
- 採購能力不足；
- 風險評估與後部署稽核仍弱；
- 影響衡量不足；
- 使用者回饋機制有限。

所以瓶頸不是：

$$
Can\ AI\ Generate?
$$

而是：

$$
Can\ Institutions\ Govern,\ Integrate,\ Measure,\ and\ Correct?
$$

。

這正是政治 executive competence 的領域。

---

# 22. 政治人物需要成為 AI-System Integrator

未來真正強的首長不需要：

$$
Know\ Everything
$$

而需要：

$$
Integrate
(
AI,
Experts,
Bureaucracy,
Citizens,
Law,
Budget
)
$$

。

可以定義 AI Governance Integration competence：

$$
AGI_A=
(
ToolSelection,
DataGovernance,
HumanReview,
WorkflowDesign,
Audit,
Escalation,
Correction
)
$$

這是一種新的政治管理能力。

---

# 23. AI-native executive 與 AI-assisted speaker 不同

## AI-assisted speaker

主要使用 AI：

$$
Research
+
Draft
+
TalkingPoints
$$

## AI-native executive

使用 AI：

$$
Signal\ Detection
\rightarrow
Policy\ Simulation
\rightarrow
Human\ Decision
\rightarrow
Execution
\rightarrow
Telemetry
\rightarrow
Audit
\rightarrow
Correction
$$

前者增加：

$$
Communication\ Productivity
$$

後者增加：

$$
Governance\ Loop\ Performance
$$

兩者政治價值不可混同。

---

# 24. 政治領導將從「答案供應者」轉向「問題與決策架構者」

前 AI 政治明星常呈現：

> 我知道答案。

未來真正高價值的領導可能呈現：

> 我知道應該問什麼、哪些答案不能信、何時需要更多資料、何時資訊已足夠、最後如何作成決定。

因此：

$$
Answer\ Production
$$

相對貶值，

而：

$$
Problem\ Formulation
+
Decision\ Architecture
$$

升值。

---

# 25. AI 時代的 generalist 不再是「什麼都能講」

新 generalist 更接近：

$$
Can\ Coordinate\ Specialists
$$

$$
Can\ Detect\ CrossDomain\ Conflict
$$

$$
Can\ Allocate\ Attention
$$

$$
Can\ Decide\ Under\ Uncertainty
$$

而不是：

$$
Can\ Recite\ CrossDomain\ Facts
$$

。

---

# 26. Charisma 不會消失，但會改變

AI 很難完全替代：

- 身體在場；
- 危機中的可信表現；
- 群眾象徵；
- 儀式；
- 身分代表；
- 情緒共鳴。

所以：

$$
Charisma
$$

不會因 AI 直接歸零。

但純語言型 charisma 可能受到：

$$
Synthetic\ Content
$$

侵蝕。

相對更重要的可能是：

$$
Embodied\ Credibility
$$

與：

$$
Repeated\ Reliability
$$

。

---

# 27. Authenticity 的價格可能上升，也可能變得更難驗證

AI 生成讓：

$$
Perfect\ Message
$$

變得廉價。

因此人們可能更重視：

$$
Authenticity
$$

。

但同時，deepfake 與 synthetic media 也讓 authenticity 本身更難驗證。

所以：

$$
Demand(Auth)\uparrow
$$

與：

$$
VerificationCost(Auth)\uparrow
$$

可能同時發生。

這會提高：

$$
Provenance
+
Identity\ Verification
+
Official\ Channels
$$

的政治價值。

---

# 28. Political Staff 的工作也會重新定價

AI 不只影響候選人。

幕僚工作中的：

- 摘要；
- 初稿；
- clipping；
- 基礎 opposition research；
- 翻譯；
- FAQ；
- 基本資料整理；

會高度 AI 化。

相對升值的幕僚能力可能是：

$$
Source\ Judgment
$$

$$
Political\ Timing
$$

$$
Coalition\ Knowledge
$$

$$
Local\ Knowledge
$$

$$
Confidential\ Context
$$

$$
Strategy
$$

$$
Execution
$$

。

---

# 29. AI 可能讓政治人物更像「組織架構設計者」

如果內容與分析供給大幅增加，首長真正的工作會更接近：

$$
Attention\ Allocation
$$

。

問題不再是：

> 有沒有資訊？

而是：

> 哪一個資訊要進入決策？

> 哪一個模型值得信？

> 哪一個風險先處理？

> 哪一個局處必須重新協調？

因此政治領導更接近：

$$
Meta\text{-}Decision\ System
$$

。

---

# 30. AI 能力越強，組織耦合越重要

Paper 02 定義 Leader-System Coupling：

$$
C_A
$$

AI 會在組織裡增加新的節點：

$$
Leader
\leftrightarrow
Staff
\leftrightarrow
AI
\leftrightarrow
Bureaucracy
\leftrightarrow
Data
$$

如果耦合差：

- AI 分析不進決策；
- 決策不進執行；
- 現場資料回不來；
- 自動化錯誤無人發現。

因此：

$$
AI\ Capacity\uparrow
$$

不保證：

$$
Governance\ Capacity\uparrow
$$

。

---

# 31. Skill Exposure 與 Skill Replacement 不能混用

OECD 2026 指出，高技能職業往往對 AI 暴露最高，包括管理者、專業人士與工程師，但因依賴非例行認知與社會能力，往往比 routine jobs 更可能呈現 AI complementarity，而不是完整自動化。

這對政治能力分析很重要。

政治人物可能：

$$
AIExposure\gg0
$$

但：

$$
ReplacementRisk\ll Exposure
$$

。

所以 Paper 05 不是「政治人物會失業」論。

而是：

$$
TaskComposition\ changes
$$

。

---

# 32. Complementarity 會製造新的政治不平等

如果某政治人物本來就具備：

$$
Judgment
+
Execution
+
Strong\ Organization
$$

再得到 AI：

$$
Performance\uparrow\uparrow
$$

。

但如果政治人物只有：

$$
Surface\ Communication
$$

AI 可能只是讓：

$$
Surface\ Communication\uparrow
$$

。

所以 AI 不一定拉平政治人才差距。

它可能：

$$
Compress\ Some\ Gaps
$$

同時：

$$
Amplify\ Other\ Gaps
$$

。

---

# 33. 「明星政治人物」模型會改變

傳統：

$$
Star_{old}
=
Rhetoric
+
Media
+
Knowledge
+
Narrative
+
Charisma
$$

AI-rich environment 中可能變成：

$$
Star_{AI}
=
Judgment
+
Execution
+
Trust
+
Coordination
+
AIIntegration
+
Charisma
$$

不是完全替換，而是權重改變。

---

# 34. 新世代政治候選人的成長路徑也會改變

以前政治人物可能靠：

$$
Media\ Performance
\rightarrow
National\ Recognition
\rightarrow
Executive\ Office
$$

未來如果選民可以低成本檢查：

$$
Speech
\leftrightarrow
Action
\leftrightarrow
Outcome
$$

則：

$$
Execution\ Evidence
$$

可能更早成為升級必要條件。

政治人才市場可能要求：

$$
Proof\ of\ Delivery
$$

而不只是：

$$
Proof\ of\ Visibility
$$

。

---

# 35. 但政治市場不一定自動變理性

AI 也可能使：

$$
Propaganda
+
Microtargeting
+
Synthetic\ Identity
+
Attention\ Manipulation
$$

更強。

所以：

$$
Better\ Audit
$$

不代表：

$$
Better\ Democracy
$$

。

AI 同時提高：

$$
Epistemic\ Defense
$$

與：

$$
Epistemic\ Attack
$$

。

最終結果取決於：

$$
Institutions
+
Platform\ Design
+
Media\ Ecology
+
Regulation
+
Political\ Culture
$$

。

---

# 36. Repricing 不是單方向歷史律

本文不主張：

$$
Rhetoric\ Value\rightarrow0
$$

。

在某些時期，AI 生成內容過度氾濫反而可能讓真正優秀的人類說服與現場表現更稀缺。

因此：

$$
\Pi_k(t)
$$

是動態變數。

Repricing 取決於：

- 技術能力；
- 普及率；
- 信任；
- 法規；
- 媒體形式；
- 選民習慣；
- 組織吸收能力。

所以這是一個 empirical research program，而不是必然論。

---

# 37. 能力價格模型

本文提出示意模型：

$$
\Pi_k=
\frac{
I_k\cdot L_k\cdot V_k\cdot R_k
}{
S_k+\lambda A_k
}
\cdot
(1+\mu C_k)
$$

其中：

- $I_k$：governance impact；
- $L_k$：legitimacy relevance；
- $V_k$：verifiability；
- $R_k$：responsibility load；
- $S_k$：human supply；
- $A_k$：AI substitutability；
- $C_k$：AI complementarity；
- $\lambda,\mu$：制度與技術調節係數。

此公式不是估計完成的經濟模型，而是概念框架。

若：

$$
A_k\uparrow
$$

且：

$$
C_k\approx0
$$

則相對價格可能下降。

若：

$$
A_k\approx0
$$

但：

$$
C_k\uparrow
$$

則能力可能升值。

---

# 38. 幾個預期重新定價方向

## 下降或商品化

$$
Basic\ Drafting
$$

$$
Basic\ Research
$$

$$
Routine\ Briefing
$$

$$
Translation
$$

$$
Basic\ Counterargument
$$

$$
Message\ Variants
$$

## 高度增強

$$
Policy\ Analysis
$$

$$
Scenario\ Planning
$$

$$
Public\ Sentiment\ Analysis
$$

$$
Risk\ Detection
$$

## 相對升值

$$
Judgment
$$

$$
Authority
$$

$$
Execution
$$

$$
Coalition\ Building
$$

$$
Organizational\ Coupling
$$

$$
Trust
$$

$$
Outcome\ Ownership
$$

。

---

# 39. 如何實證 RPC？

需要 longitudinal political labor data。

可以建立：

$$
Actor
+
Task
+
AIUse
+
Outcome
$$

資料。

研究問題包括：

1. AI 採用後競選 staff composition 是否改變？
2. 候選人政策回應速度是否收斂？
3. 論述品質差距是否下降？
4. 行政成果差距是否反而擴大？
5. 選民是否降低對「知識型口才」的能力推論？
6. execution record 是否更能預測選舉支持？
7. AI-native governance 是否提高 policy feedback speed？
8. 長時序 AI audit 是否降低 inconsistent rhetoric 的收益？

---

# 40. 政治能力 repricing 的測量

本文建議建立 Political Competence Price Index：

$$
PCPI_k(t)
$$

可由：

- candidate selection；
- media attention；
- polling premium；
- campaign spending；
- staff demand；
- appointment patterns；
- executive performance；
- voter survey；

等資料估計。

例如測試：

$$
\frac{\partial VoteShare}{\partial RhetoricalScore}
$$

是否隨 AI 普及下降，

以及：

$$
\frac{\partial VoteShare}{\partial DeliveryScore}
$$

是否上升。

---

# 41. 與 Paper 01–04 的關係

Paper 01 讓政治人物成為：

$$
Temporal\ Actor
$$

Paper 02 區分：

$$
Discourse
\neq
Execution
$$

Paper 03 區分：

$$
Attribution
\neq
Ownership
$$

Paper 04 建立：

$$
Diligent\ AI
$$

Paper 05 才能問：

> 當所有人的 discourse 與 research capacity 被 AI 增強後，哪些 actor characteristics 仍然具有稀缺政治價值？

因此 RPC 不是獨立未來學，而是前四篇自然推出的能力經濟學。

---

# 42. 與 Paper 06 的關係

政治能力重新定價會影響企業風險模型。

企業不能只問：

> 候選人說什麼？

還需要問：

> 他是否具有把政策真的實作的 executive probability？

因此：

$$
PolicyIntent
\times
ExecutionProbability
$$

才接近：

$$
PolicyRealizationRisk
$$

Paper 06 將把這個問題接到企業、產業與資本配置。

---

# 43. 與 Paper 08 的關係

如果政治能力價格改變，政治菁英生成路徑也會改變。

例如過去：

$$
Law
\rightarrow
Rhetoric/Institutional\ Advantage
\rightarrow
Politics
$$

未來這種優勢是否下降？

公共行政、工程、科技管理、企業執行或 AI-system governance 經歷是否升值？

Paper 08 的教育與 career-path 模型將提供測試基礎。

---

# 44. 研究命題

**命題 1：論述商品化命題**

隨 AI 普及，基本政策摘要、演說草稿、快速反駁與跨領域 briefing 的供給增加，其作為政治人物個人稀缺能力的相對溢價下降。

**命題 2：說服能力擴散命題**

AI 使具說服力的政治訊息生產成本下降，降低大型專業傳播團隊在部分文字任務上的相對優勢。

**命題 3：判斷升值命題**

當政策選項生成與資訊整理成本下降，選擇、排序與不確定性下承諾的相對價值提高。

**命題 4：執行升值命題**

當高品質政策建議供給增加，而組織執行能力供給增長較慢時，execution competence 的相對政治價值提高。

**命題 5：責任升值命題**

當 AI 降低政治長期記憶與比對成本，可信的 decision ownership 與 outcome ownership 成為更重要的政治資產。

**命題 6：整合能力命題**

AI 對治理成果的影響受到 leader-system-AI coupling 顯著調節。

**命題 7：高技能互補命題**

政治領導屬高度 AI exposed 但不易完全自動化的工作，其主要變化將表現為 task recomposition 與 complementarity，而非職位整體消失。

**命題 8：明星政治重構命題**

政治明星的能力權重將從 knowledge/rhetoric dominant，逐步向 judgment/execution/trust/AI-integration 移動。

---

# 45. 反例與可能失敗

RPC 可能被以下證據削弱：

1. AI 普及後，政治口才溢價反而持續上升；
2. 選民無法或不願使用 AI audit；
3. synthetic content 使個人品牌比實績更重要；
4. 行政能力依舊難以被外部觀察；
5. AI 成為少數大型政黨壟斷資產；
6. AI 對組織 coordination 的增強速度與語言生成一樣快；
7. 政治極化使實績資訊失去作用。

因此本文沒有宣稱：

$$
AI\Rightarrow Better\ Meritocracy
$$

。

---

# 46. 規範風險

若 AI 讓：

$$
Persuasion\ Cost\downarrow
$$

政治可能出現：

$$
Manipulation\ Scale\uparrow
$$

。

Lin 等人的研究同時提醒，政治 AI 對話具有可觀察說服力，而且模型可能提出不準確事實。

因此政治能力重新定價不能只討論效率。

還必須討論：

$$
Truth
+
Fairness
+
Transparency
+
Consent
+
Power
$$

。

---

# 47. 政府 AI 尤其不能消除人類責任

OECD 的公共部門 AI 研究已明確把：

- 透明；
- accountability；
- risk assessment；
- audit；
- user control；

放在可擴張 AI government 的核心。

因此 AI-native executive 不是：

> 把決策交給 AI。

而是：

$$
AI\ Advice
+
Human\ Authority
+
Traceable\ Decision
+
Auditable\ Execution
$$

。

這是 RPC 中 accountability 升值的制度原因。

---

# 48. 結論

AI 不需要成為政治人物，才能重新定價政治人物。

只要 AI 使原本昂貴的：

$$
Knowledge\ Retrieval
$$

$$
Policy\ Synthesis
$$

$$
Drafting
$$

$$
Counterargument
$$

$$
Translation
$$

$$
Persuasion
$$

變得更容易取得，政治市場中的相對稀缺性就已經改變。

因此，前 AI 時代的政治優勢：

$$
I\ know\ more
$$

$$
I\ speak\ faster
$$

$$
I\ explain\ better
$$

將逐步受到：

$$
AI\ assisted\ parity
$$

壓縮。

而 AI 不容易自行供給的：

$$
I\ choose
$$

$$
I\ coordinate
$$

$$
I\ execute
$$

$$
I\ accept\ responsibility
$$

$$
I\ maintain\ trust
$$

將變得相對重要。

所以本文的核心不是：

$$
AI\ replaces\ politics
$$

而是：

$$
AI\ reprices\ political\ competence
$$

。

未來政治領導的真正比較優勢可能不再是：

$$
Who\ can\ produce\ the\ best\ answer?
$$

而是：

$$
Who\ can\ build\ the\ best\ legitimate\ decision\text{-}execution\text{-}correction\ loop?
$$

最終可壓縮為：

$$
\boxed{
Political\ Advantage_{AI}
=
Judgment
+
Execution
+
Coordination
+
Trust
+
Accountability
+
AI\ Integration
}
$$

這不是對人類政治能力的貶低。

恰恰相反，它把政治重新推回最難被自動化的部分：

$$
Choosing
+
Governing
+
Owning\ the\ Consequences
$$

。

---

# References

Bai, H., Voelkel, J. G., Muldowney, S., Eichstaedt, J. C., & Willer, R. (2025). LLM-generated messages can persuade humans on policy issues. *Nature Communications, 16*, 6037. https://doi.org/10.1038/s41467-025-61345-5

Flanigan, B., Foos, F., Fung, A., & Stewart, C. (2026). Artificial Intelligence and Democracy: Campaigns, Elections, Movements, and Deliberation. *APSA Preprints*. https://doi.org/10.33774/apsa-2026-lzzlk

International Monetary Fund. (2026). *Bridging Skill Gaps for the Future: New Jobs Creation in the AI Age*. IMF Staff Discussion Note SDN/2026/001. https://doi.org/10.5089/9798229028196.006

Lin, H., Czarnek, G., Lewis, B., White, J. P., Berinsky, A. J., Costello, T., Pennycook, G., & Rand, D. G. (2025). Persuading voters using human–artificial intelligence dialogues. *Nature, 648*, 394–401. https://doi.org/10.1038/s41586-025-09771-9

OECD. (2025). *Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions*. OECD Publishing. https://doi.org/10.1787/795de142-en

OECD. (2026). *Digital Government Outlook 2026: From Foundations to Transformational Impact*. OECD Publishing. https://doi.org/10.1787/0496b2bc-en

OECD. (2026). *Skills in the AI Age*. OECD Artificial Intelligence Papers, No. 60. OECD Publishing. https://doi.org/10.1787/972bd15e-en

---

## Canonical Source Note

本檔為 Paper 05 v0.1 的 UTF-8 canonical Markdown source。正式數學 source 僅使用 ` $...$ ` 與 `$$...$$` delimiter。任何 PDF、HTML、簡報、聊天畫面或其他 rendering 均不取代本檔。本文中的能力價格公式與 task matrix 為研究框架，不應被誤讀為已完成實證估計。
