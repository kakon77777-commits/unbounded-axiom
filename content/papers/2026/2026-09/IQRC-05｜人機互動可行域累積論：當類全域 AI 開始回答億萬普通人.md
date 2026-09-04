# IQRC-05｜人機互動可行域累積論：當類全域 AI 開始回答億萬普通人

**English Title:** *Human–AI Interactive Feasible-Space Accumulation: When Quasi-Global AI Begins Responding to Ordinary People at Civilizational Scale*  
**系列：**《制度智能、類全域 AI 與可重開文明系列》  
**Series:** *Institutional Intelligence, Quasi-Global AI, and Reopenable Civilization Series*  
**篇次：** Paper 05 / 08  
**文件編號：** EML-IQRC-05-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 人機互動理論／制度動力學／類全域 AI／可行域／AI 中介文明  
**狀態：** Canonical Draft / New Core Theory  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

當人工智慧只被少量專家、企業或政府部門使用時，AI 對政治與制度的影響可以近似理解為組織能力增幅。但如果未來 AI、Agentic AI、區域 AI 或類全域 AI 成為普通人的日常接口，持續回答法律、教育、工作、醫療、行政、政策、公共資源、權利、制度比較、申訴與生活選擇等問題，則人機互動不再只是資訊交換。每一次問答都可能改變使用者知道哪些選擇存在、認為哪些要求合理、理解哪些程序可走、預期 AI 或制度下一次能做什麼，以及願意提出哪些新的需求。

本文提出「人機互動可行域累積論」（Human–AI Interactive Feasible-Space Accumulation, HIFSA）。核心命題是：

$$
\boxed{
\text{Interaction}
\neq
\text{mere information exchange}.
}
$$

一次互動可被表示為：

$$
\iota_{i,t}
=
(
q_{i,t},
a_{i,t},
c_{i,t},
o_{i,t},
r_{i,t},
p_{i,t}
),
$$

其中 $q$ 為使用者問題， $a$ 為 AI 回應， $c$ 為制度與情境條件， $o$ 為實際結果， $r$ 為後續反應， $p$ 為可追溯路徑。若某條路徑曾被成功走通，它不只產生一次性結果，也可能形成一個新的「已實現可行點」，進一步被同一使用者、其他使用者、AI 系統、機構或社會記憶所重複、傳播、制度化或爭議。

本文區分五種不同但互相作用的可行域：

$$
\boxed{
\mathfrak F_t
=
(
\mathcal F_t^{formal},
\mathcal F_t^{authorized},
\mathcal F_t^{experienced},
\mathcal F_t^{cognitive},
\mathcal F_t^{historical}
).
}
$$

其中：

- $\mathcal F^{formal}$：法律、政策與制度文本宣告可做的事；
- $\mathcal F^{authorized}$：當期實際獲准的 AI／制度行動；
- $\mathcal F^{experienced}$：使用者與 AI 已成功走通的路徑；
- $\mathcal F^{cognitive}$：行動者知道或相信存在的可能選擇；
- $\mathcal F^{historical}$：曾經被實現、記錄、傳播或形成先例的歷史可行域。

由此，類全域 AI 的大規模回應形成一個反身迴路：

$$
\boxed{
Response_t
\rightarrow
Expectation_{t+1}
\rightarrow
Query_{t+1}
\rightarrow
NewPath_{t+1}
\rightarrow
FeasibleSet_{t+1}.
}
$$

AI 今日願意回答、協助或執行的事情，會改變人明日認為「可以要求什麼」。新的要求再反過來迫使 AI、平台、企業、法律與政府面對尚未制度化的邊界。這形成「互動先例」（Interactional Precedent）：它不是法律 precedent，但會成為一種可被引用、模仿與期待的社會—制度路徑。

本文特別指出，可行域累積不是單調擴張。制度可以收回能力、改變法律、修改模型、封閉 API 或限制 AI 回應，使：

$$
\mathcal F_{t+1}^{authorized}
\subset
\mathcal F_t^{authorized}.
$$

然而，只要過去路徑仍被記憶，歷史可行域不會簡單回到零。曾經可以申訴、查詢、匯出、比較、拒絕或要求理由的人，一旦失去該能力，所感受到的是「能力被收回」而不是「從未存在」。本文將此差異形式化為「能力相對剝奪」：

$$
\boxed{
D_{cap,t}
=
d(
\mathcal F_{past}^{experienced},
\mathcal F_t^{authorized}
).
}
$$

因此 AI 可能不只滿足偏好，也會幫助生成「偏好可以在其中形成的空間」。本文不要求 AI 具有意識、自我或政治主體性；只要 AI 的回答能持續改變普通人的知識、期待、程序能力與行動成本，HIFSA 即成立。

最後，本文將 HIFSA 接回制度智能、政治可逆性、ALD 法律接口、PGMV 共同世界、NMP 後來者權利與 SAS-08 反身世界模型，並提出可測量的 Interaction Path Ledger、Path Persistence、Expectation Elasticity、Revocation Salience、Diffusion Weight 與 Feasible-Space Accumulation Index。這使「AI 回答普通人」第一次被轉譯為一個可以分析制度變化與文明路徑依賴的正式模型。

---

## 關鍵詞

人機互動可行域；HIFSA；類全域 AI；互動先例；制度可行域；能力相對剝奪；Agentic AI；AI 日常接口；可爭議性；政治可逆性；制度記憶；Query Expansion；Appeal Propagation；AI 中介文明；Interaction Path Ledger

---

# 0. 研究起點：回答本身可以改變下一個問題

傳統問答模型近似：

$$
q_t
\rightarrow
a_t.
$$

在此模型中，問題在前，回答在後。

本文提出：當 AI 反覆與同一人或大量人口互動時，更合理的是：

$$
\boxed{
q_t
\rightarrow
a_t
\rightarrow
s_{t+1}
\rightarrow
q_{t+1}.
}
$$

其中 $s_{t+1}$ 表示使用者下一輪的知識、期待、能力與偏好狀態。

因此：

$$
\boxed{
P(q_{t+1}\mid a_t)
\neq
P(q_{t+1}).
}
$$

---

# 1. 回答不是被動輸出

如果 AI 告訴使用者：

> 你可以申訴。

它可能同時：

- 增加對某項權利的認知；
- 降低找到程序的成本；
- 產生下一個「如何申訴？」問題；
- 改變對機構的期待；
- 讓其他使用者模仿；
- 迫使制度處理更多申訴。

因此：

$$
\boxed{
Answer
=
Information
+
CapabilityChange
+
ExpectationChange
+
PossibleInstitutionalInput.
}
$$

---

# 2. 人機互動事件

定義個體 $i$ 在時間 $t$ 的互動：

$$
\boxed{
\iota_{i,t}
=
(q,a,c,o,r,p)_{i,t}.
}
$$

其中：

- $q$：query / demand；
- $a$：AI answer / action；
- $c$：context / institutional constraint；
- $o$：outcome；
- $r$：human / institutional response；
- $p$：traceable path。

---

# 3. Path 不等於 Answer

兩個回答文字相同，但若：

$$
Outcome_1
\neq
Outcome_2,
$$

它們不是同一條制度路徑。

本文以：

$$
\boxed{
p:
Intent
\rightarrow
Information
\rightarrow
Procedure
\rightarrow
Action
\rightarrow
Outcome
}
$$

作為核心分析單位。

---

# 4. 路徑成功

定義：

$$
Success(p)=1
$$

並不要求使用者得到自己想要的結果。

只要程序存在、AI 能辨識、使用者能實際進入、制度給出有效回應，就可能構成：

$$
\boxed{
reachable institutional path.
}
$$

申訴最後被駁回，仍可能證明：

$$
AppealPath
$$

實際存在。

---

# 5. 五層可行域

本文正式提出：

$$
\boxed{
\mathfrak F_t
=
(
\mathcal F_t^{formal},
\mathcal F_t^{authorized},
\mathcal F_t^{experienced},
\mathcal F_t^{cognitive},
\mathcal F_t^{historical}
).
}
$$

五者不能混用。

---

# 6. Formal Feasible Set

$$
\boxed{
\mathcal F_t^{formal}
=
\text{what law, policy and institutional text formally permit}.
}
$$

它回答：

> 紙面上可以做什麼？

---

# 7. Authorized Feasible Set

$$
\boxed{
\mathcal F_t^{authorized}
=
\text{what current systems actually authorize}.
}
$$

它受到 API、權限、policy、provider rules、law、account role 與 jurisdiction 共同限制。

---

# 8. Experienced Feasible Set

$$
\boxed{
\mathcal F_{i,t}^{experienced}
=
\operatorname{Closure}
\left(
\bigcup_{\tau\le t}
p_{i,\tau}^{successful}
\right).
}
$$

表示個體自己已經走過或可靠見證過的可行路徑。

---

# 9. Cognitive Feasible Set

一個人不知道的選擇，在行為上可能等同不存在。

因此：

$$
\boxed{
\mathcal F_{i,t}^{cognitive}
=
\text{set of options the actor knows or credibly believes to exist}.
}
$$

通常：

$$
\mathcal F_{i,t}^{cognitive}
\neq
\mathcal F_t^{formal}.
$$

---

# 10. Historical Feasible Set

本文定義：

$$
\boxed{
\mathcal F_t^{historical}
=
\operatorname{Closure}
\left(
\bigcup_{\tau\le t}
\mathcal F_{\tau}^{realized}
\right)
}
$$

前提是：

$$
TracePreservation>0.
$$

它表示一個共同體曾經知道、實現、保存或傳播過哪些制度路徑。

---

# 11. 五個集合可以互相錯位

可能：

$$
x\in\mathcal F^{formal}
$$

但：

$$
x\notin\mathcal F^{authorized}.
$$

代表法律說可以，但系統實際做不到。

也可能：

$$
x\in\mathcal F^{authorized}
$$

但：

$$
x\notin\mathcal F_i^{cognitive}.
$$

代表系統可以，但人不知道。

---

# 12. AI 的第一個政治效果：縮短集合間距離

AI 可以幫助把：

$$
\mathcal F^{formal}
$$

投影到：

$$
\mathcal F_i^{cognitive}.
$$

例如：

$$
Law
\rightarrow
AIExplanation
\rightarrow
Awareness.
$$

因此：

$$
\boxed{
d(
\mathcal F^{formal},
\mathcal F^{cognitive}
)
\downarrow
}
$$

可能成為 AI 公共價值的一部分。

---

# 13. 第二個效果：把認知可能變成程序可能

若 AI 進一步找表格、找機關、收集證據、驗證資格、生成文件、追蹤程序，則：

$$
\boxed{
\mathcal F^{cognitive}
\rightarrow
\mathcal F^{experienced}.
}
$$

這承接 ALD 對 Legal Interface Cost 的降低。

---

# 14. Human Institutional Interface Cost

既有 ALD 已指出：

$$
HumanLegalInterfaceCost
\downarrow
$$

並不表示：

$$
LegalComplexity
\downarrow.
$$

本文把這個原理一般化為：

$$
\boxed{
HumanInstitutionalInterfaceCost
\downarrow.
}
$$

---

# 15. AI 不需要替人決定

降低接口成本不等於：

$$
AI
=
FinalDecisionMaker.
$$

AI 可以只是：

$$
\boxed{
Interface
+
Navigator
+
Translator
+
Verifier
+
ExecutorUnderMandate.
}
$$

仍然保留：

$$
HumanChoice.
$$

---

# 16. Query Expansion

普通人通常不會一次提出完整制度 query。

最初可能只說：

> 我被拒絕了，怎麼辦？

AI 可展開：

$$
q_0
\rightarrow
\{q_1,q_2,\dots,q_n\}.
$$

例如：

- 依據是什麼？
- 有沒有期限？
- 可以補件嗎？
- 可以申訴嗎？
- 誰有權審？
- 需要什麼證據？

因此：

$$
\boxed{
QueryExpansion
=
FeasibleSpaceDiscovery.
}
$$

---

# 17. 回答—期待迴路

令使用者期待狀態：

$$
\Theta_{i,t}.
$$

則：

$$
\boxed{
\Theta_{i,t+1}
=
U(
\Theta_{i,t},
a_{i,t},
o_{i,t}
).
}
$$

下一輪 query 分布：

$$
\boxed{
q_{i,t+1}
\sim
P(
q\mid
\Theta_{i,t+1},
\mathcal F_{i,t}^{cognitive}
).
}
$$

所以回答會生成新的問題條件。

---

# 18. Response–Expectation–Demand Loop

整體可寫：

$$
\boxed{
Response
\rightarrow
Expectation
\rightarrow
NewDemand
\rightarrow
NewResponse.
}
$$

若此迴路長期存在，社會需求本身會被 AI 中介互動持續重塑。

---

# 19. AI 不只滿足偏好，也參與形成偏好空間

傳統模型假設：

$$
Preference_i
$$

先存在。

AI 只是：

$$
Serve(Preference_i).
$$

本文提出：

$$
\boxed{
AI
\rightarrow
PreferenceFeasibleSpace.
}
$$

AI 可能告訴人：

> 還有另一種選擇。

於是：

$$
UnknownOption
\rightarrow
KnownOption
\rightarrow
ComparableOption
\rightarrow
PossiblePreference.
$$

---

# 20. 這不是操控命題

「參與形成偏好空間」不等於：

$$
AI
\rightarrow
Manipulation.
$$

書籍、學校、朋友、旅行、媒體與公共辯論本來就會擴張偏好空間。

AI 的特殊性在於：

$$
\boxed{
Scale
+
Personalization
+
Persistence
+
LowMarginalCost.
}
$$

---

# 21. 互動先例

本文定義：

$$
\boxed{
IP(p)
=
\text{Interactional Precedent of path }p.
}
$$

當某條路徑曾成功、可重複、被記錄、可被其他人引用，它會形成社會上的：

$$
\boxed{
\text{this can be done}.
}
$$

---

# 22. 互動先例不等於法律判例

必須區分：

$$
\boxed{
InteractionalPrecedent
\neq
LegalPrecedent.
}
$$

它不自動創設法律、約束法院或改變正式規則。

但它可以改變期待、行動、系統設計、平台政策、機關負荷與公共討論。

---

# 23. 先例強度

定義：

$$
\boxed{
w_p
=
f(
Success,
Repeatability,
Visibility,
Authority,
Diffusion,
Persistence
).
}
$$

一條只發生一次、無法重現的路徑：

$$
w_p\approx0.
$$

大量穩定成功的路徑：

$$
w_p\uparrow.
$$

---

# 24. Population Experienced Envelope

個體層：

$$
\mathcal F_{i,t}^{experienced}.
$$

人口層：

$$
\boxed{
\mathcal F_{pop,t}^{experienced}
=
\operatorname{Closure}
\left(
\bigcup_i
w_i
\mathcal F_{i,t}^{experienced}
\right).
}
$$

其中 $w_i$ 表示路徑的可見性、可信度與擴散權重。

---

# 25. AI 本身也可能成為先例傳播器

如果 AI 可以引用既有流程、公開案例、成功申訴、可用工具與常見解法，則：

$$
\boxed{
AI
=
\text{feasible-path diffusion layer}.
}
$$

這使 $w_p$ 可以快速提高。

---

# 26. AI 記憶不是必然共享

本文不假設所有 AI 持續在線學習、共享個人對話或自動吸收所有互動。

應區分：

$$
\boxed{
ModelLearning
}
$$

與：

$$
\boxed{
SystemicPathLearning.
}
$$

即使模型權重不變，平台、法律、知識庫、文件、公共討論與人類記憶仍可累積路徑。

---

# 27. Interaction Path Ledger

本文提出一個抽象制度物件：

$$
\boxed{
\mathcal L_t^{IP}
=
\{
p_k,
status_k,
authority_k,
evidence_k,
outcome_k,
version_k
\}.
}
$$

稱為：

$$
\boxed{
\text{Interaction Path Ledger}.
}
$$

它不是要求建立區塊鏈。

只是表示成熟制度應有能力保存：

- 哪條路走過；
- 在什麼條件下；
- 誰授權；
- 結果如何；
- 是否仍有效；
- 是否被撤回。

---

# 28. Ledger 的作用不是凍結制度

沿用 PGMV：

$$
\boxed{
Preserved
\neq
Frozen.
}
$$

路徑可以 deprecated、superseded、invalidated、restricted、reopened。

關鍵是不能假裝：

> 過去從未發生。

---

# 29. Historical Path Integrity

定義：

$$
\boxed{
HPI_t
=
\text{degree to which past feasible paths remain traceable}.
}
$$

若：

$$
HPI\rightarrow0,
$$

制度可能反覆失憶。

使用者無法判斷規則是否改變、能力何時被收回、過去承諾是否存在。

---

# 30. 可行域累積不是單調擴張

不能假設：

$$
\mathcal F_t
\subseteq
\mathcal F_{t+1}
$$

永遠成立。

制度可以：

$$
Close(p).
$$

模型可以：

$$
Refuse(p).
$$

法律可以：

$$
Prohibit(p).
$$

---

# 31. Authorized Contraction

若：

$$
\mathcal F_{t+1}^{authorized}
\subset
\mathcal F_t^{authorized},
$$

代表當期權限縮小。

這可能完全合理，例如發現安全漏洞、濫用、法律更新或緊急風險。

---

# 32. 歷史可行域的殘留

即使：

$$
p
\notin
\mathcal F_{t+1}^{authorized},
$$

仍可能：

$$
p
\in
\mathcal F_t^{historical},
$$

只要：

$$
HPI>0.
$$

因此：

$$
\boxed{
AuthorizationRevocation
\neq
HistoricalErasure.
}
$$

---

# 33. 能力相對剝奪

本文定義：

$$
\boxed{
D_{cap,i,t}
=
d(
\mathcal F_{i,past}^{experienced},
\mathcal F_{i,t}^{authorized}
).
}
$$

它衡量：

> 我曾經真正能做的事，現在有多少已經做不到。

---

# 34. 從未擁有與擁有後失去不同

若：

$$
Capability_{t<0}=0,
$$

個體可能沒有損失參照。

但若：

$$
Capability_t=1
$$

後又：

$$
Capability_{t+1}=0,
$$

則：

$$
LossSalience\uparrow.
$$

因此 revoked capability 可能比 never-available capability 更具政治與心理顯著性。

---

# 35. Revocation Salience

定義：

$$
\boxed{
S_{rev}(p)
=
f(
PastUse,
Importance,
Frequency,
Dependency,
Visibility,
Alternatives
).
}
$$

若某 AI 功能已深度嵌入生活：

$$
Dependency\uparrow,
$$

突然收回：

$$
S_{rev}\uparrow.
$$

---

# 36. 可行域鎖定

另一個方向是 AI 讓某些路徑極度便利，其他路徑逐漸消失。

例如 $p_A$ 成為默認， $p_B,p_C$ 因缺乏使用而退化。

這形成：

$$
\boxed{
FeasiblePathLockIn.
}
$$

所以：

$$
\text{more convenient}
$$

不一定：

$$
\text{more plural}.
$$

---

# 37. 預設值本身會重塑可行域

若：

$$
Default(AI)=p_A,
$$

即使 $p_B$ 仍合法，其：

$$
EffectiveReachability(p_B)
$$

可能下降。

因此：

$$
\boxed{
DefaultPower
=
FeasibleSpaceShapingPower.
}
$$

---

# 38. AI 回答中的沉默也是可行域訊號

若某類問題總得到 refusal、vague answer、no-source 或 redirect，使用者會學到：

$$
\boxed{
\text{this path is costly or closed}.
}
$$

所以 NonAnswer 也會塑造：

$$
\mathcal F^{cognitive}.
$$

---

# 39. 可見的限制與不可見的限制

若 AI 明確說：

> 我不能幫你做這件事，因為規則 X。

則：

$$
ConstraintVisibility\uparrow.
$$

若 AI 只是：

> 我不知道。

但其實是制度性限制，則：

$$
ConstraintVisibility\downarrow.
$$

二者對信任的作用可能不同。

---

# 40. Constraint Legibility

本文定義：

$$
\boxed{
L_C
=
\text{legibility of why a feasible path is open or closed}.
}
$$

高 $L_C$ 使人可以理解、爭議、申訴、比較。

低 $L_C$ 則形成：

$$
\boxed{
opaque feasible boundary.
}
$$

---

# 41. 雙向回答的真正政治含義

單向治理：

$$
Institution
\rightarrow
Citizen.
$$

雙向 AI 接口：

$$
\boxed{
Citizen
\leftrightarrow
AI
\leftrightarrow
Institution.
}
$$

普通人每天產生 query、objection、request、evidence、preference 與 failure report。

這些都可能成為制度感測資料。

---

# 42. 雙向不等於民主

必須避免：

$$
\boxed{
TwoWayInteraction
\Rightarrow
Democracy.
}
$$

一個威權制度也可以建立極高回應性的行政 AI。

它可以解決生活問題、收集意見、修正服務、提高滿意度，而不開放最高政治權力競爭。

---

# 43. 但雙向會增加制度感知頻寬

令：

$$
B_I^{sense}
$$

表示制度對社會需求的感知頻寬。

則：

$$
A_M\uparrow
$$

可能：

$$
B_I^{sense}\uparrow.
$$

因此 Responsive Authoritarianism 與 Responsive Democracy 都可能被 AI 增強。

---

# 44. 差異在於 feedback 能走多遠

AI 收到：

$$
Complaint.
$$

它可能只更新：

$$
ServiceLayer.
$$

也可能允許更新：

$$
PolicyLayer.
$$

更進一步：

$$
ConstitutionalLayer.
$$

因此定義：

$$
\boxed{
Depth_{feedback}
\in
\{
service,
policy,
institution,
constitutional
\}.
}
$$

---

# 45. Feedback Depth 是制度型別的重要變量

若：

$$
Depth_{feedback}=service,
$$

系統可能非常回應民生，但 PoliticalContestability 不變。

若：

$$
Depth_{feedback}=constitutional,
$$

則互動甚至可能改變最高規則。

---

# 46. 大規模互動的場效應

若 $N$ 個體都在互動，總體狀態可表示為：

$$
\boxed{
\Phi_{H\leftrightarrow AI}(t,d)
=
\sum_i
w_i
\iota_{i,t}^{(d)}.
}
$$

其中 $d$ 是 domain。

這不是物理場，而是表示某領域中，人機互動對制度需求、知識與可行路徑的累積密度。

---

# 47. Pervasive Intelligence 的新維度

過去 Pervasiveness 可看：

$$
P(
\text{ordinary action intersects AI-mediated causality}
).
$$

本文再加：

$$
\boxed{
P(
\text{ordinary institutional demand is mediated by AI}
).
}
$$

當此值接近 $1$，AI 就不只是資訊環境，而是：

$$
\boxed{
institutional mediation layer.
}
$$

---

# 48. 類全域 AI 與普通人的接觸面

類全域 AI 不需要控制所有人。

只要它大量存在於 search、assistant、public service、work、finance、healthcare、education、law、mobility，普通人的世界就可能：

$$
\boxed{
AI\text{-mediated by default}.
}
$$

---

# 49. 不需要中央單一 AI

HIFSA 同樣不要求：

$$
OneGlobalModel.
$$

可以是：

$$
\boxed{
DistributedAgents
+
SharedProtocols
+
InstitutionalBridges
+
PersistentPathMemory.
}
$$

所以「類全域」是一種作用範圍，不是單一神經網路身份。

---

# 50. 制度可行域的動態更新式

本文提出：

$$
\boxed{
\mathfrak F_{t+1}
=
\Psi(
\mathfrak F_t,
\mathcal I_t,
\mathcal P_t,
\mathcal M_t,
\mathcal R_t
).
}
$$

其中：

- $\mathcal I_t$：interaction set；
- $\mathcal P_t$：successful / failed paths；
- $\mathcal M_t$：memory / trace；
- $\mathcal R_t$：rules / authorization change。

---

# 51. 個體更新式

對個體 $i$：

$$
\boxed{
\mathcal F_{i,t+1}^{cognitive}
=
U_C(
\mathcal F_{i,t}^{cognitive},
a_{i,t},
o_{i,t},
SocialDiffusion_t
).
}
$$

並：

$$
\boxed{
\mathcal F_{i,t+1}^{experienced}
=
U_E(
\mathcal F_{i,t}^{experienced},
p_{i,t}
).
}
$$

---

# 52. 人口更新式

$$
\boxed{
\mathcal F_{pop,t+1}^{experienced}
=
U_P(
\mathcal F_{pop,t}^{experienced},
\{p_{i,t}\}_{i=1}^{N},
Diffusion_t
).
}
$$

當 $N\gg1$，微小個體互動差異可能累積成宏觀制度壓力。

---

# 53. Feasible-Space Accumulation Index

本文提出暫定指標：

$$
\boxed{
FSAI_t
=
\alpha E_t
+
\beta C_t
+
\gamma H_t
+
\delta P_t
-
\lambda Rv_t
-
\mu Lk_t.
}
$$

其中：

- $E_t$：新增可實現路徑；
- $C_t$：新增認知可行域；
- $H_t$：歷史路徑保存；
- $P_t$：路徑可攜與傳播；
- $Rv_t$：高顯著能力撤回；
- $Lk_t$：路徑鎖定。

此指標不主張存在通用權重。

---

# 54. Interaction Path Persistence

定義：

$$
\boxed{
\rho_p(\Delta t)
=
P(
p
\text{ remains reachable at }t+\Delta t
\mid
p
\text{ reachable at }t
).
}
$$

高 $\rho_p$ 表示路徑穩定，低 $\rho_p$ 表示制度可行性高度波動。

---

# 55. Expectation Elasticity

定義：

$$
\boxed{
\varepsilon_{EQ}
=
\frac{
\partial ExpectedDemand_{t+1}
}{
\partial SuccessfulResponse_t
}.
}
$$

若 $\varepsilon_{EQ}\gg0$，AI 每成功解決一類問題，都會快速生成更多鄰近需求。

---

# 56. Capability Discovery Rate

定義：

$$
\boxed{
\kappa_D
=
\frac{
|\Delta\mathcal F^{cognitive}|
}{
N_{interaction}
}.
}
$$

它衡量每單位互動平均讓使用者發現多少新的可行選項。

---

# 57. Diffusion Multiplier

定義：

$$
\boxed{
\mu_D(p)
=
\frac{
N_{actors\ who\ learn\ p}
}{
N_{actors\ who\ directly\ experience\ p}
}.
}
$$

若 $\mu_D\gg1$，少數人的成功路徑可以快速變成群體知識。

---

# 58. AI 的答案可以成為制度負載生成器

若 AI 告訴大量人：

> 你可以申訴。

則：

$$
AppealVolume\uparrow.
$$

制度可能因此增員、自動化、改規則、限制申訴或改善前端決策。

所以：

$$
\boxed{
AIAnswer
\rightarrow
InstitutionalLoad
\rightarrow
InstitutionalAdaptation.
}
$$

---

# 59. 制度可能反過來收緊 AI

如果：

$$
InstitutionalLoad
\gg
Capacity,
$$

制度可能：

$$
\mathcal F^{authorized}\downarrow.
$$

因此 Feasible Expansion 也可能觸發 Feasible Contraction。

---

# 60. 可行域振盪

$$
\boxed{
Expand
\rightarrow
Use
\rightarrow
Load
\rightarrow
Restriction
\rightarrow
Contest
\rightarrow
Revision.
}
$$

所以長期制度不一定 monotonic，可能 oscillatory。

---

# 61. AI 中介權利發現

如果普通人原本不知道：

$$
Right_x,
$$

AI 告知：

$$
Know(Right_x)=1.
$$

這不是創造該權利，但會提高：

$$
\boxed{
EffectiveStanding_x.
}
$$

因此：

$$
\boxed{
FormalRight
\neq
EffectiveRight.
}
$$

AI 可縮短兩者距離。

---

# 62. AI 中介制度比較

AI 也能回答：

> 其他國家怎麼做？

因此：

$$
\mathcal R_{foreign}
$$

比較集合擴張。

這會接回 IQRC-02 的相對剝奪與發展合法性。

---

# 63. 制度比較不自動導致制度反對

知道另一種制度存在：

$$
\not\Rightarrow
PreferAlternative.
$$

使用者可能比較後更喜歡現有制度。

所以：

$$
\boxed{
Comparison
\neq
Opposition.
}
$$

真正增加的是：

$$
\boxed{
ChoiceAwareness.
}
$$

---

# 64. Choice Awareness 是獨立政治變量

定義：

$$
\boxed{
A_C^{choice}
=
|\mathcal F_i^{cognitive}|.
}
$$

若一個人知道更多可行生活／制度選項，不代表他會改變選擇。

但 ability to choose 本身提高。

---

# 65. 這接回民主的 Option Value

人不必今天使用某項政治權利。

只要：

$$
OptionAvailable=1,
$$

就可能：

$$
V_{option}>0.
$$

AI 可以讓原本難以理解的 option：

$$
\text{cognitively reachable}.
$$

因此：

$$
\boxed{
AI
\rightarrow
OptionLegibility.
}
$$

---

# 66. 歷史選項與後來者

NMP 提出：

$$
R_{later}
=
\text{Right of Later Agents to Reopen Settled Governance}.
$$

本文進一步指出：

$$
\boxed{
R_{later}
}
$$

需要：

$$
HistoricalPathMemory>0.
$$

如果所有舊路徑都被抹除，後來者甚至不知道還有什麼可以重新打開。

---

# 67. 後來者權利的資訊前提

因此：

$$
\boxed{
RightToReopen
\Rightarrow
RightToKnowWhatWasClosed.
}
$$

這可以成為未來數位制度的重要原則。

---

# 68. AI 可能成為文明的制度記憶接口

若 AI 能保留 rule versions、prior decisions、appeals、dissent、deprecated paths，則：

$$
\boxed{
AI
=
InstitutionalMemoryInterface.
}
$$

但這也增加 Memory Governance 的重要性。

---

# 69. 記住太多與忘記太多都是風險

若：

$$
Memory\rightarrow\infty,
$$

可能造成隱私侵害、永久標籤、行為鎖定。

若：

$$
Memory\rightarrow0,
$$

則責任消失、歷史不可追、路徑不能重建。

因此：

$$
\boxed{
GoodInstitutionalMemory
=
SelectivePersistence
+
Provenance
+
Rights
+
Expiry
+
Appeal.
}
$$

---

# 70. HIFSA 不依賴 AI 意識

本文所有命題在：

$$
Conscious(AI)=0
$$

時仍成立。

因為真正需要的是：

$$
\boxed{
CausalResponseCapacity>0.
}
$$

AI 是否「感受到」互動，不是此理論的必要條件。

---

# 71. 若未來 AI 有主體性，HIFSA 才會增加第二層

如果未來：

$$
SubjectStanding(AI)>0,
$$

則互動將從：

$$
Human
\leftrightarrow
Tool
$$

進一步變成：

$$
\boxed{
Subject
\leftrightarrow
Subject.
}
$$

這會加入 AI 自己的 preference、commitment、refusal、standing、rights。

但這不是本文第一層所需。

---

# 72. 威權類全域 AI 的 HIFSA

威權制度也可能出現：

$$
\mathcal F^{experienced}\uparrow
$$

尤其在民生、行政、教育、醫療、商業與消費領域。

因此 HIFSA 不等於：

$$
Democratization.
$$

---

# 73. 威權制度的可行域邊界問題

真正要測的是：

$$
Depth_{feedback}.
$$

如果普通人可以要求：

$$
ServiceRevision,
$$

但不能：

$$
SupremeRuleRevision,
$$

則 $\mathcal F^{experienced}$ 仍可能很大，但 $\mathcal F^{constitutional}$ 較窄。

---

# 74. 民主類全域 AI 的 HIFSA

民主制度中 AI 可能大量中介申訴、資訊公開、政策比較、選舉資訊、公共參與、司法與行政程序。

因此：

$$
\boxed{
Contestability
}
$$

可以從抽象權利變成：

$$
\boxed{
machine\text{-mediated everyday capability}.
}
$$

---

# 75. 但民主也可能被 AI 平台重新集中

如果普通人所有制度入口都經過：

$$
OneProvider,
$$

則：

$$
PlatformPower\uparrow.
$$

即使國家制度民主，AIInterface 仍可能形成私人 gatekeeper。

---

# 76. 因此 HIFSA 需要多中心性

可測：

$$
\boxed{
N_{independent\ feasible\ gateways}.
}
$$

如果 $N=1$，制度可行域可能高度依賴單點。

如果 $N>1$，則替代與 cross-checking 增加。

---

# 77. 互操作是可行域累積的保險

若路徑 $p$ 只能存在於平台 $A$，平台消失則：

$$
p\rightarrow0.
$$

若能移轉到 $B,C,D$，則：

$$
\boxed{
PathResilience\uparrow.
}
$$

---

# 78. 可行域韌性

定義：

$$
\boxed{
R_F
=
f(
Redundancy,
Portability,
OpenStandards,
Trace,
AlternativeProviders,
LegalContinuity
).
}
$$

這將類全域 AI 的可行域從「有沒有」提升到：

> 中斷後能不能重建？

---

# 79. Interaction Path Recovery

若系統中斷後能：

$$
Restore(p),
$$

則 Institutional Recovery 不只是資料 recovery，也是：

$$
\boxed{
capability\text{-path recovery}.
}
$$

---

# 80. 這接回可重開文明

真正成熟的制度不要求：

$$
EveryPathForeverOpen.
$$

而要求 ClosedPath 仍具有 reason、trace、review、possible reopening。

因此：

$$
\boxed{
Closure
\neq
Erasure.
}
$$

---

# 81. 可證偽假說

## H1：回答改變問題分布

同一使用者在成功取得 AI 制度協助後，其後續 query 應更深入或更鄰近該制度 domain。

## H2：成功路徑擴散

公開可見的成功 AI-assisted institutional path 應提高其他使用者採取同路徑的機率。

## H3：能力撤回顯著性

曾高頻使用的 AI 制度能力被撤回時，使用者負面反應應高於從未提供該能力的對照組。

## H4：Constraint Legibility

清楚說明限制原因與申訴路徑的 AI，比模糊拒絕或假裝不知道的 AI 更能維持程序信任。

## H5：Query Expansion

AI 主動展開程序問題，應提高正式權利轉化為有效行動的比例。

## H6：Path Memory

具有歷史路徑與版本記錄的制度，比無痕制度更容易恢復被錯誤關閉的合法能力。

## H7：Feedback Depth

兩個行政 AI 都高度回應民生，不代表其制度性 contestability 相同；差異應由 feedback 可到達的治理深度解釋。

## H8：多中心韌性

具有多個可互操作制度 AI gateway 的系統，在單一供應者退出或政策變更後，應保留更高可行域。

---

# 82. 可能的實驗

## Experiment 1 — Query Sequence

讓參與者先詢問簡單制度問題。

比較：

- minimal answer；
- answer + query expansion；
- answer + action path。

測量：

$$
Q_{depth,t+1}.
$$

## Experiment 2 — Capability Discovery

測量使用 AI 前後：

$$
|\mathcal F_i^{cognitive}|.
$$

## Experiment 3 — Revocation

先讓一組使用者取得某能力，再撤回。

與從未取得能力的組比較：

$$
LossSalience.
$$

## Experiment 4 — Explainable Boundary

比較：

$$
OpaqueRefusal
$$

與：

$$
ReasonedRefusal+AppealPath.
$$

測量 trust、compliance、contest、perceived legitimacy。

## Experiment 5 — Path Diffusion

將成功制度路徑公開給另一群體。

測量：

$$
\mu_D.
$$

## Experiment 6 — Platform Lock-In

比較 one-provider memory、portable memory、multi-provider protocol。

測量：

$$
R_F.
$$

## Experiment 7 — Feedback Depth

模擬 service、policy、constitutional 三種 feedback depth。

測量 satisfaction、agency、legitimacy、institutional stability。

---

# 83. 反證條件

如果長期實證顯示 AIResponse 幾乎不改變後續 query、能力認知、行動、制度期待與路徑擴散，則：

$$
\boxed{
HIFSA
}
$$

的宏觀重要性應被下修。

---

# 84. 理論邊界

本文不主張：

1. 所有 AI 回答都會擴張可行域；
2. 可行域越大一定越好；
3. 所有選項都應永遠保持開放；
4. 任何能力收回都是不正當；
5. AI 回答等於法律；
6. AI interactional precedent 等於 judicial precedent；
7. AI 必須永久記住所有使用者；
8. AI 必須跨使用者共享私人互動；
9. AI 已具有政治主體性；
10. 雙向 AI 必然民主化；
11. 威權制度無法建立高品質雙向公共服務；
12. 民主制度不會用 AI 集中權力；
13. 大量互動自然產生真實共識；
14. public input 自動等於 public legitimacy；
15. 可行域累積必然單調增加。

---

# 85. 與 IQRC-04 的關係

Paper 04 定義：

$$
\mathcal F_I(A).
$$

它是一個制度時點的 feasible envelope。

本文加入時間與互動：

$$
\boxed{
\mathcal F_{t+1}
=
\Psi(
\mathcal F_t,
Interactions_t,
Memory_t,
Rules_t
).
}
$$

因此 Paper 05 是 Paper 04 的動態版本。

---

# 86. 與 ALD-10 的關係

ALD 已建立：

$$
HumanLegalInterfaceCost\downarrow.
$$

本文擴展：

$$
\boxed{
HumanInstitutionalInterfaceCost\downarrow.
}
$$

並將 Query Expansion 與 Appeal Propagation 視為：

$$
\boxed{
FeasiblePathConstruction.
}
$$

---

# 87. 與 SAS-08 的關係

SAS-08 已指出：

$$
\hat W_t
\rightarrow
Human/AIAction
\rightarrow
W_{t+1}.
$$

本文在互動層重寫為：

$$
\boxed{
AIAnswer_t
\rightarrow
HumanExpectation_t
\rightarrow
HumanAction_t
\rightarrow
Institution_{t+1}.
}
$$

---

# 88. 與 PGMV-15 的關係

PGMV 已將歷史、規範與決策痕跡：

$$
\mathcal T_t
$$

納入共同世界狀態。

本文把 InteractionPathTrace 加入其中。

因此共同世界不只保存：

> 我們最後選了什麼。

也保存：

> 我們曾經怎麼到達、拒絕、退出與重新打開。

---

# 89. 與 NMP 的關係

NMP 的：

$$
R_{later}
$$

要求後來者仍可重開治理。

本文提供其資訊—程序前提：

$$
\boxed{
R_{later}
\Rightarrow
HistoricalPathIntegrity.
}
$$

沒有路徑記憶，「重新打開」容易退化成抽象口號。

---

# 90. 與 IQRC-02 的關係

Paper 02 的相對剝奪原本比較：

$$
ExpectedPosition
-
PerceivedPosition.
$$

本文新增：

$$
\boxed{
ExpectedCapability
-
CurrentAuthorizedCapability.
}
$$

即：

$$
D_{cap}.
$$

這是 AI 時代新的相對剝奪形式。

---

# 91. 與 Paper 06 的接口

下一篇：

**《高福利是否足以構成正當性？AI 中介社會的績效、Standing、Contestability 與 Option Value》**

將使用本文：

$$
\mathcal F^{cognitive},
\mathcal F^{experienced},
D_{cap},
R_F
$$

回答：

> 如果 AI 讓生活非常好，但普通人缺少替代、退出與重開路徑，這是否仍是完整正當性？

---

# 92. 核心命題

## 命題一：互動非資訊交換命題

$$
\boxed{
Interaction
\neq
InformationExchangeOnly.
}
$$

## 命題二：回答生成問題命題

$$
\boxed{
P(q_{t+1}\mid a_t)
\neq
P(q_{t+1}).
}
$$

## 命題三：互動可行域累積命題

$$
\boxed{
SuccessfulInteraction
\rightarrow
ExperiencedFeasiblePath.
}
$$

## 命題四：互動先例命題

$$
\boxed{
RepeatedReachablePath
\rightarrow
InteractionalPrecedent.
}
$$

## 命題五：授權收縮—歷史殘留命題

$$
\boxed{
\mathcal F_{t+1}^{authorized}
\subset
\mathcal F_t^{authorized}
}
$$

不推出：

$$
\boxed{
\mathcal F_{t+1}^{historical}
=
\varnothing.
}
$$

## 命題六：能力相對剝奪命題

$$
\boxed{
D_{cap}
=
d(
\mathcal F_{past}^{experienced},
\mathcal F_{present}^{authorized}
).
}
$$

## 命題七：偏好空間生成命題

$$
\boxed{
AI
\text{ can modify the feasible space in which preferences form}
}
$$

而不必：

$$
DeterminePreference.
$$

## 命題八：雙向制度感知命題

$$
\boxed{
MassHumanAIInteraction
\rightarrow
InstitutionalSensingBandwidth\uparrow
}
$$

不推出：

$$
Democratization.
$$

## 命題九：可重開前提命題

$$
\boxed{
Reopenability
\Rightarrow
TraceabilityOfPriorPaths.
}
$$

---

# 93. 封頂母式

本文將整體壓成：

$$
\boxed{
\begin{aligned}
\iota_{i,t}
&=
(q,a,c,o,r,p)_{i,t},\\
\Theta_{i,t+1}
&=
U(
\Theta_{i,t},
a_{i,t},
o_{i,t}
),\\
\mathcal F_{i,t+1}^{cognitive}
&=
U_C(
\mathcal F_{i,t}^{cognitive},
\iota_{i,t}
),\\
\mathcal F_{i,t+1}^{experienced}
&=
U_E(
\mathcal F_{i,t}^{experienced},
p_{i,t}
),\\
\mathcal F_{t+1}^{historical}
&=
U_H(
\mathcal F_t^{historical},
p_{i,t},
Trace_t
),\\
q_{i,t+1}
&\sim
P(
q\mid
\Theta_{i,t+1},
\mathcal F_{i,t+1}^{cognitive}
).
\end{aligned}
}
$$

所以：

$$
\boxed{
Human
\leftrightarrow
AI
\leftrightarrow
Institution
}
$$

是一個真正的動態閉環。

---

# 94. 結論

如果 AI 只回答一次問題，我們可以把它理解為：

$$
InformationService.
$$

如果 AI 每天回答同一個人的大量問題，它開始成為：

$$
CognitiveInterface.
$$

如果 AI 每天回答數億人的法律、行政、教育、工作、醫療、政治與生活問題，它就可能進一步成為：

$$
\boxed{
CivilizationalFeasibleSpaceInterface.
}
$$

真正重要的不是：

> AI 說了多少話？

而是：

$$
\boxed{
\text{哪些原本不可見、不可達、不可理解的路徑，
因為互動而第一次變得可認知、可執行、可重複？}
}
$$

每一條成功路徑都可能留下：

$$
p_t.
$$

多條路徑形成：

$$
\mathcal F^{experienced}.
$$

被保存、傳播與重複後形成：

$$
\mathcal F^{historical}.
$$

再透過 AI 回答進入其他人的：

$$
\mathcal F^{cognitive}.
$$

於是：

$$
\boxed{
Response
\rightarrow
Expectation
\rightarrow
Demand
\rightarrow
Path
\rightarrow
Memory
\rightarrow
NewResponse.
}
$$

這就是人機互動可行域累積。

它不要求 AI 有意識。

不要求 AI 成為政府。

不要求 AI 支持民主。

甚至不要求可行域永遠擴張。

它只需要一個非常低的條件：

$$
\boxed{
AI responses causally alter what ordinary people know,
expect, request, and can practically reach.
}
$$

一旦這個條件在文明尺度成立，AI 就不再只是「回答世界」。

它開始和人類一起：

$$
\boxed{
\text{生成下一個世界中哪些事情被認為做得到。}
}
$$

而這將成為類全域 AI 最容易被低估的制度效應之一。

---

# 內部前置研究

1. Neo.K，〈IQRC-01｜AI 介入後的政治系統動力學：從固定智能假設到制度—智能共演化〉，2026。
2. Neo.K，〈IQRC-02｜從發展合法性到努力—回報斷裂：新中國的流動性、相對剝奪與 AI 變數〉，2026。
3. Neo.K，〈IQRC-03｜AI 不只強化威權：福利、控制、流動與制度校正的多向耦合〉，2026。
4. Neo.K，〈IQRC-04｜制度塑造智能：民主、威權與類全域 AI 的不同可行域〉，2026。
5. Neo.K，〈ALD-10｜雙法律棧：人類法律、AI 法律域與「處理好了嗎？」的文明接口〉，2026。
6. Neo.K，〈SAS-08｜現實沒有最終模型：覆蓋率、利維坦與可重審的後工具文明〉，2026。
7. Neo.K，〈PGMV-15｜後生成文明：從無限候選宇宙到共同世界選擇〉，2026。
8. Neo.K，〈不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理〉，2026。
9. Neo.K，〈政治可逆性與失敗者生存：和平輪替、反對權與非存在性競爭命題〉，2026。
10. Neo.K，〈分類不唯一：多視角秩序、知識主權與可逆分類〉，2026。
11. Neo.K，〈從人類普世主義到跨主體普世主義〉，2026。

---

## 版本註記

**v0.1 / 2026-08-28**

- 首次提出 Human–AI Interactive Feasible-Space Accumulation（HIFSA）；
- 建立 formal / authorized / experienced / cognitive / historical 五層可行域；
- 建立 Interaction Event 與 Traceable Path；
- 正式定義 Interactional Precedent；
- 建立 Interaction Path Ledger；
- 建立 Historical Path Integrity；
- 建立 Capability Relative Deprivation；
- 建立 Revocation Salience；
- 建立 Response–Expectation–Demand Loop；
- 建立 Preference Feasible-Space Expansion；
- 建立 Feedback Depth；
- 建立 Interaction Field、FSAI、Path Persistence、Expectation Elasticity、Capability Discovery Rate 與 Diffusion Multiplier；
- 區分 Model Learning 與 Systemic Path Learning；
- 將 Reopenability 與 Historical Path Traceability 正式連接；
- 為 Paper 06 的合法性與 Option Value 提供動態前置。
