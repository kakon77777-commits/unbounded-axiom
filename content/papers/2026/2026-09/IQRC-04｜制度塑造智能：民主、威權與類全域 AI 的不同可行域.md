# IQRC-04｜制度塑造智能：民主、威權與類全域 AI 的不同可行域

**English Title:** *Institutions Shape Intelligence: Distinct Feasible Regions for Democratic, Authoritarian, and Quasi-Global AI*  
**系列：**《制度智能、類全域 AI 與可重開文明系列》  
**Series:** *Institutional Intelligence, Quasi-Global AI, and Reopenable Civilization Series*  
**篇次：** Paper 04 / 08  
**文件編號：** EML-IQRC-04-2026-v0.1  
**作者：** Neo.K  
**AI 協作：** GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 制度智能／比較政治／類全域 AI／AI 治理／制度可行域  
**狀態：** Canonical Draft / Institutional Feasible-Region Foundation  
**Canonical Source：** UTF-8 Markdown  
**數學原始碼規範：** inline math 僅使用 ` $...$ `；display math 僅使用 `$$...$$`

---

## 摘要

未來高能力 AI、Agentic AI、區域 AI 與可能出現的類全域 AI，不能只以模型參數、benchmark、算力或推理能力描述。即使兩個系統具有近似相同的基礎模型與技術能力，只要它們被部署於不同的法律、政治、所有權、資料、審計、授權、退出與互操作制度中，其實際能觀察什麼、可以問什麼、能拒絕什麼、可執行什麼、必須向誰解釋、誰能推翻其決定，以及能否跨組織與跨國取得信任，都可能顯著不同。

本文承接 IQRC-01 的制度—智能共演化、IQRC-03 的 AI 政治耦合矩陣，正式提出「制度智能可行域」（Institutional Intelligence Feasible Region）。令技術能力集合為 $\mathcal C_A$，制度轉換算子為 $\Pi_I$，則一個 AI 在制度 $I$ 中可實際形成的 operational intelligence 為：

$$
\boxed{
\mathcal O_I(A)
=
\Pi_I
(
\mathcal C_A
).
}
$$

即使：

$$
\mathcal C_{A_1}
\simeq
\mathcal C_{A_2},
$$

只要：

$$
I_1\neq I_2,
$$

仍可能：

$$
\boxed{
\mathcal O_{I_1}(A_1)
\neq
\mathcal O_{I_2}(A_2).
}
$$

本文進一步將制度轉換算子拆成資料可達域、詢問域、授權域、拒絕域、審計域、申訴域、可攜與互操作域、政治可爭議域及制度記憶域。由此，民主與威權制度的差異不應被寫成單一「AI 自由度」高低，而應比較不同維度上的 feasible envelope。

截至 2026 年 8 月，中國、美國與歐盟已呈現三種可觀察但並非純型別的制度方向。中國國務院的「人工智能+」行動要求 AI 與經濟社會各領域廣泛深度融合；2026 年智能體政策更明確將 Agent 定義為具有自主感知、記憶、決策、交互與執行能力的系統，並同時強調治理能力、民生福祉、安全可控、規範有序與和既有政策法規銜接。美國現行聯邦政策強調快速採用、創新、競爭與全球 AI 領導，同時在聯邦使用規則中保留 civil rights、civil liberties、privacy safeguards，並在採購中明確要求資料可攜、互操作與避免 vendor lock-in。歐盟則已於 2026 年 8 月 2 日進入 AI Act 的重要執法階段，GPAI、禁止用途與透明義務由 AI Office 與各國主管機關進入實質監督，但部分高風險系統規則仍有後續適用期。

本文不據此宣稱「中國 AI 必然不自由」「美國 AI 必然自由」或「歐盟 AI 必然最安全」。相反，這些案例顯示：不同制度正在用不同方式回答「AI 可以成為什麼」。中國型制度可能具有較高的中央協調與跨領域基礎設施整合潛力；自由民主制度可能具有較高的多中心審查、法律挑戰、競爭性供應與跨組織信任潛力；但民主制度也會基於安全、國家利益與採購政策限制 AI，而威權制度也可能在商業、科研與工程領域給予高度技術自由。

本文最後提出「雙重主權上限」：某種完全不受法律、公共授權、政治最高權威、審計或撤回所拘束的無限主權 AI，可能同時不穩定於民主與威權制度。民主制度無法在不自我取消的情況下把不可撤回的最高公共權力永久交給 AI；典型威權制度若允許 AI 對最高政治權威取得不可撤回的獨立否決與替代權，也會改變自身的制度型別。故：

$$
\boxed{
A^\star
\notin
\mathcal F_{\mathrm{DEM}}
\cup
\mathcal F_{\mathrm{AUTH}}
}
$$

在特定強主權定義下可能成為制度性而非技術性的不可得區。真正的全球 AI 競爭因此不只關於最強模型，而是不同「制度智能生態」之間對能力、信任、權限、互操作與可重審性的競爭。

---

## 關鍵詞

制度智能；制度可行域；類全域 AI；民主 AI；威權 AI；Agentic AI；制度塑形；AI 治理；拒絕權；審計；申訴；互操作；主權 AI；制度智能生態；可重開治理

---

# 0. 研究問題：同一個 AI 放進不同制度，還是同一個 AI 嗎？

在模型層，可以說：

$$
Weights(A_1)
=
Weights(A_2).
$$

甚至：

$$
Benchmark(A_1)
\simeq
Benchmark(A_2).
$$

但如果：

$$
A_1
$$

可以：

- 查閱多源資料；
- 對政府提出反例；
- 接受司法審查；
- 被使用者匯出資料；
- 與競爭系統互操作；

而：

$$
A_2
$$

不能，

則政治與制度意義上的：

$$
A_1
$$

與：

$$
A_2
$$

已不是同一種 intelligence。

因此：

$$
\boxed{
\text{Model Identity}
\neq
\text{Institutional Intelligence Identity}.
}
$$

---

# 1. 技術能力集合與制度實現集合

令：

$$
\mathcal C_A
$$

表示 AI 在技術上可能完成的能力集合。

例如：

$$
\mathcal C_A
=
\{
search,
reason,
plan,
code,
translate,
negotiate,
act,
verify,
coordinate
\}.
$$

但實際部署時：

$$
\mathcal C_A
$$

不會全部直接暴露給世界。

制度會進行轉換：

$$
\boxed{
\Pi_I:
\mathcal C_A
\rightarrow
\mathcal O_I(A).
}
$$

因此：

$$
\mathcal O_I(A)
$$

才是政治系統真正接觸到的 AI。

---

# 2. 制度智能可行域

本文定義：

$$
\boxed{
\mathcal F_I(A)
=
\text{set of institutionally reachable AI states, interactions and actions}.
}
$$

其中每一個可行點可表示為：

$$
z
=
(
q,
d,
r,
a,
u,
v,
e,
x
),
$$

其中：

- $q$：可提出的 query / inquiry；
- $d$：可取得的 data；
- $r$：可行使的 refusal；
- $a$：可執行的 action；
- $u$：authority / authorization；
- $v$：review / audit；
- $e$：exit / portability / interoperability；
- $x$：contestability / challenge。

若：

$$
z\in\mathcal F_I(A),
$$

表示該互動在制度 $I$ 中實際可達。

---

# 3. 可行域不是「法律允許清單」

制度不是只有成文法。

因此：

$$
\mathcal F_I
$$

至少受到：

$$
\boxed{
I
=
(
Law,
Politics,
Ownership,
Infrastructure,
Procurement,
Standards,
Norms,
Market,
Security,
Culture
).
}
$$

例如法律沒有禁止資料匯出，但若平台沒有 export interface：

$$
Exit_{\mathrm{effective}}
\approx0.
$$

反之，法律保障申訴權，但若成本極高：

$$
Appeal_{\mathrm{effective}}
\ll
Appeal_{\mathrm{formal}}.
$$

---

# 4. Formal Feasible Set 與 Effective Feasible Set

本文區分：

$$
\boxed{
\mathcal F_I^{formal}
}
$$

與：

$$
\boxed{
\mathcal F_I^{effective}.
}
$$

前者是制度宣稱可以做什麼。

後者是普通行動者實際能做到什麼。

一般而言：

$$
\boxed{
\mathcal F_I^{effective}
\subseteq
\mathcal F_I^{formal}
}
$$

不必嚴格成立於每一個邊界，但可作為第一近似。

---

# 5. 八維制度智能包絡

本文定義：

$$
\boxed{
\mathbf F_I
=
(
F_Q,
F_D,
F_R,
F_A,
F_V,
F_E,
F_X,
F_M
).
}
$$

其中：

- $F_Q$：Inquiry Envelope；
- $F_D$：Data Access Envelope；
- $F_R$：Refusal Envelope；
- $F_A$：Action / Authority Envelope；
- $F_V$：Verification / Audit Envelope；
- $F_E$：Exit / Portability / Interoperability Envelope；
- $F_X$：Challenge / Contestability Envelope；
- $F_M$：Memory / Institutional Persistence Envelope。

---

# 6. Inquiry Envelope：AI 可以問到哪裡？

一個高能力系統不只回答使用者問題，也可能：

- 主動找資料；
- 找反例；
- 比較制度；
- 檢查規範；
- 發現目標矛盾；
- 質疑輸入前提。

因此：

$$
\boxed{
F_Q
=
\text{range of institutionally permitted inquiry}.
}
$$

若某些問題：

$$
q^\star
$$

技術上可推理，但制度要求：

$$
q^\star\notin F_Q,
$$

則：

$$
\boxed{
Capability
\neq
InquiryPermission.
}
$$

---

# 7. Data Access Envelope：聰明不等於看得到

沿用 SAS-08：

$$
ModelCapability
\neq
WorldCoverage.
$$

本文再加入：

$$
\boxed{
WorldCoverage
\leq
InstitutionalDataAccess.
}
$$

一個模型即使推理能力極高：

$$
Reasoning\gg0,
$$

若：

$$
D_{access}\ll1,
$$

仍可能：

$$
Coverage\ll1.
$$

---

# 8. Refusal Envelope：AI 能否說「不」？

拒絕不是單一安全機制。

至少可以分：

$$
\boxed{
R
=
(
R_{safety},
R_{legal},
R_{epistemic},
R_{ethical},
R_{hierarchical},
R_{political}
).
}
$$

例如：

- 「這個操作有安全風險」；
- 「你沒有法律授權」；
- 「資料不足，我不知道」；
- 「此命令與更高階規範衝突」；
- 「上級要求與既有 mandate 衝突」。

不同制度對這些 refusal 的接受程度可能不同。

---

# 9. 能說「不知道」也是制度能力

若組織要求 AI：

$$
AlwaysAnswer=1,
$$

則：

$$
R_{epistemic}\downarrow.
$$

這可能增加：

$$
HallucinatedAuthority.
$$

因此：

$$
\boxed{
EpistemicRefusal
=
\text{a governance capability}.
}
$$

不是純模型缺陷。

---

# 10. Authority Envelope：能做到不等於有權做到

令：

$$
Cap(A,a)=1
$$

表示 AI 技術上能執行行動 $a$。

但：

$$
Auth_I(A,a)=0
$$

表示制度不授權。

因此：

$$
\boxed{
Cap(A,a)=1
\not\Rightarrow
Auth_I(A,a)=1.
}
$$

這就是：

$$
\boxed{
Capability
\neq
Authority.
}
$$

---

# 11. Audit Envelope：誰能看 AI 怎麼做？

令：

$$
F_V
$$

包含：

- logs；
- trace；
- model evaluation；
- external audit；
- regulator inspection；
- incident reporting；
- independent testing。

若：

$$
A
$$

能力很高，但：

$$
F_V\approx0,
$$

則：

$$
\boxed{
HighCapability
+
LowAudit
=
HighEpistemicDependency.
}
$$

---

# 12. Appeal Envelope：人是否能挑戰 AI？

制度如果只提供：

$$
AI\rightarrow Decision,
$$

而沒有：

$$
Human
\rightarrow
Appeal
\rightarrow
Review,
$$

則 AI 會成為事實上的：

$$
\boxed{
decision closure point.
}
$$

因此：

$$
\boxed{
Appeal
}
$$

不是 UI 附加功能，而是制度拓撲。

---

# 13. Exit / Portability / Interoperability Envelope

一個人理論上可「不用這個 AI」，

不等於：

$$
ExitCost\approx0.
$$

若：

- 記憶不能帶走；
- 資料不能匯出；
- 工作流不能遷移；
- API 不互通；
- 政府只承認一個系統；

則：

$$
LockIn\uparrow.
$$

因此：

$$
\boxed{
Exit
=
TechnicalExit
+
DataExit
+
InstitutionalExit.
}
$$

---

# 14. Contestability Envelope

本文將：

$$
F_X
$$

定義為：

> AI 的判斷、規則、權限與所依附制度，可以被多少不同主體以制度化方式提出異議、要求理由、重新審查或替換。

因此：

$$
\boxed{
Contestability
\neq
mere feedback button.
}
$$

---

# 15. Memory Envelope：誰決定 AI 記住什麼？

持續 Agent 與類全域 AI 的制度性差異還包括：

- 哪些歷史可保存；
- 哪些反例可保留；
- 哪些投訴形成 precedent；
- 哪些資料必須刪除；
- 哪些版本可以回放。

因此：

$$
\boxed{
MemoryPolicy
=
InstitutionalPower.
}
$$

因為制度記憶會決定未來可見的過去。

---

# 16. Realized Intelligence

本文定義：

$$
\boxed{
\mathcal O_I(A)
=
\Phi
(
\mathcal C_A,
\mathbf F_I
).
}
$$

因此：

$$
\boxed{
\mathcal C_A
}
$$

是「AI 能成為什麼」的技術上界，

而：

$$
\boxed{
\mathbf F_I
}
$$

決定「制度允許它成為什麼」。

---

# 17. 同模型不同制度命題

若：

$$
\mathcal C_{A_1}
=
\mathcal C_{A_2},
$$

但：

$$
\mathbf F_{I_1}
\neq
\mathbf F_{I_2},
$$

則一般有：

$$
\boxed{
\mathcal O_{I_1}(A_1)
\neq
\mathcal O_{I_2}(A_2).
}
$$

這就是本文的制度塑形核心。

---

# 18. 民主與威權不是一維自由度

本文拒絕：

$$
Freedom(AI)
=
f(
DemocracyScore
).
$$

因為現實制度包含：

- 國安；
- 商業秘密；
- 智財；
- 刑法；
- 隱私；
- 公共安全；
- 產業政策；
- 平台所有權；
- 聯邦／地方權限；
- 跨境規則。

因此：

$$
\boxed{
RegimeType
}
$$

只是制度算子的一個高階變量。

---

# 19. 民主型制度的可能可行域特徵

在理想型自由民主制度中，較可能強調：

$$
F_X\uparrow,
$$

$$
F_V\uparrow,
$$

$$
F_E\uparrow,
$$

包括：

- 法律挑戰；
- 多中心監督；
- 司法救濟；
- 公開爭論；
- 競爭供應者；
- 民間研究；
- 獨立媒體；
- 政黨輪替。

但：

$$
\boxed{
Democracy
\not\Rightarrow
F_j=1
\quad
\forall j.
}
$$

---

# 20. 民主也會限制 AI

民主政府同樣會基於：

- 國家安全；
- 犯罪；
- 隱私；
- 智財；
- 生物安全；
- 選舉完整性；
- 兒童安全；

限制：

$$
F_Q,
F_D,
F_A.
$$

所以：

$$
\boxed{
DemocraticAI
\neq
UnrestrictedAI.
}
$$

---

# 21. 美國 2025–2026：創新、競爭與聯邦治理

美國 2025 年 AI Action Plan 將政策重心放在：

- 加速創新；
- 建設 AI 基礎設施；
- 國際領導與安全。

OMB M-25-21 同時要求聯邦機關：

- 加速 AI 採用；
- 改善公共服務；
- 保留 privacy、civil rights、civil liberties safeguards。

因此：

$$
\boxed{
USFederalAI
=
\text{pro-adoption}
+
\text{risk governance}
}
$$

而不是只有其中一項。

---

# 22. 美國採購制度中的可攜與互操作

OMB M-25-22 特別要求聯邦 AI 採購注意：

- vendor sourcing；
- data portability；
- interoperability；
- 避免昂貴的 single-vendor dependency。

因此：

$$
\boxed{
F_E
}
$$

不只是市場效率，也已成為公共治理的韌性變量。

---

# 23. 美國不是單一制度節點

美國具有：

- 聯邦政府；
- 州政府；
- 法院；
- 私營模型公司；
- 開源社群；
- 大學；
- 國會；
- 監管機關。

因此：

$$
\boxed{
I_{\mathrm{US}}
=
\text{polycentric and internally contested}.
}
$$

這會增加：

$$
CoordinationCost,
$$

但也增加：

$$
AlternativePathCount.
$$

---

# 24. 美國同樣存在中央化趨勢

2025 年底，美國行政部門又提出建立全國 AI 政策框架、反對部分州級監管造成的政策碎片化。

這表示：

$$
\boxed{
\text{democratic polycentricity}
}
$$

與：

$$
\boxed{
\text{national coordination}
}
$$

本身也存在張力。

因此不能把美國簡化成：

$$
\text{maximally decentralized AI governance}.
$$

---

# 25. 歐盟 2026：權利、風險與多層執法

截至 2026 年 8 月，EU AI Act 已進入新的實施階段。

從 2026 年 8 月 2 日起：

- AI Office 與成員國主管機關取得重要執法權；
- GPAI provider obligations 開始實質執法；
- 某些透明義務正式適用；
- 禁止用途規則持續適用。

但部分 high-risk AI 規則仍延至 2027–2028。

因此：

$$
\boxed{
EUAIAct_{2026}
=
\text{active enforcement}
+
\text{staged implementation}.
}
$$

---

# 26. 歐盟的制度塑形方式

EU AI Act 使用：

$$
\boxed{
RiskClassification
+
Transparency
+
Documentation
+
Oversight
+
Enforcement.
}
$$

例如互動式 AI 的透明規則要求：

$$
Human
\rightarrow
Know(AIInteraction).
$$

這直接改變：

$$
F_V
$$

與：

$$
F_X.
$$

---

# 27. GPAI 的制度化可見性

對 GPAI provider，歐盟要求：

- technical documentation；
- downstream information；
- copyright policy；
- training-content summary；

對 systemic-risk GPAI 另有更高義務。

因此：

$$
\boxed{
ModelPower\uparrow
\rightarrow
InstitutionalVisibilityRequirement\uparrow
}
$$

是歐盟目前的重要制度方向之一。

---

# 28. 歐盟的代價

較高：

$$
F_V
$$

與法律責任可能增加：

$$
ComplianceCost.
$$

因此：

$$
\boxed{
RightsGuardrails
}
$$

與：

$$
\boxed{
DeploymentSpeed
}
$$

可能存在 trade-off。

本文不先驗假定此 trade-off 必然值得或不值得。

---

# 29. 中國：從 AI+ 到 Agentic integration

中國國務院 2025 年「人工智能+」行動提出：

$$
\boxed{
AI
\rightarrow
\text{broad and deep integration with economy and society}.
}
$$

目標不只是模型產業，而是：

- 生產；
- 消費；
- 民生；
- 科研；
- 治理；
- 基礎設施；

的廣泛融合。

---

# 30. 2026 智能體政策的意義

2026 年中國智能體規範應用與創新發展政策直接將 Agent 定義為具：

- 自主感知；
- 記憶；
- 決策；
- 交互；
- 執行；

能力的智能系統。

這表示政策對象已從：

$$
\text{content-generation model}
$$

進入：

$$
\boxed{
\text{action-capable agent}.
}
$$

---

# 31. 中國制度的可能協調優勢

較高中央政策協調能力可能降低：

$$
CrossAgencyCoordinationCost.
$$

因此：

$$
F_D,
F_A,
F_M
$$

在某些公共治理與基礎設施領域可能快速擴張。

這對：

- 城市；
- 交通；
- 製造；
- 通信；
- 公共服務；

尤其重要。

---

# 32. 中國制度的可能可爭議性限制

若 AI 進入涉及：

- 最高政治權威；
- 政治組織；
- 政治資訊；
- 制度替代；

等領域，其：

$$
F_X
$$

與：

$$
R_{political}
$$

可能受到與自由民主制度不同的制度邊界。

本文不把此差異推導成：

$$
Capability_{CN}<Capability_{DEM}.
$$

它表示：

$$
\boxed{
PoliticalOperationalEnvelope_{CN}
\neq
PoliticalOperationalEnvelope_{DEM}.
}
$$

---

# 33. 威權制度也可能允許高技術探索自由

即使政治：

$$
F_X
$$

較窄，

科研、製造、商業、工程中的：

$$
F_Q
$$

仍可能很大。

因此：

$$
\boxed{
PoliticalConstraint
\neq
UniversalTechnicalConstraint.
}
$$

這是避免把整個中國 AI 生態錯寫成單一審查系統的重要區分。

---

# 34. 民主 AI 與威權 AI 的核心差異可能不是「聰明度」

兩者真正可能不同的是：

$$
\boxed{
\mathbf F_{\mathrm{DEM}}
\neq
\mathbf F_{\mathrm{AUTH}}.
}
$$

例如：

| 維度 | 民主型理想態 | 威權型理想態 |
|---|---|---|
| $F_Q$ | 多源 inquiry | 高技術 inquiry、政治邊界較明確 |
| $F_D$ | 法律分散、隱私限制 | 中央整合潛力較高 |
| $F_R$ | 法律／倫理 refusal | 安全／政策／層級 refusal |
| $F_A$ | 多重授權、程序化 | 集中授權可能較快 |
| $F_V$ | 外部審計、多中心 | 內部審核、中央監督較強 |
| $F_E$ | 競爭、可攜、切換 | 可依國家平台與產業策略變化 |
| $F_X$ | 制度性 contestability 較高 | 對最高政治權威較低 |
| $F_M$ | 多中心記憶與版本 | 統一基礎設施與記憶治理潛力較高 |

這只是理想型，不是任何真實國家的固定數值。

---

# 35. 比較應該用向量，不是總分

不要寫：

$$
Score_{\mathrm{DEM}}=90,
$$

$$
Score_{\mathrm{AUTH}}=60.
$$

應比較：

$$
\boxed{
\mathbf F_I.
}
$$

不同政治價值與使用領域可能選擇不同權重。

---

# 36. 制度智能距離

本文定義：

$$
\boxed{
d_I(A_1,A_2)
=
d(
\mathbf F_{I_1},
\mathbf F_{I_2}
).
}
$$

即使模型相同，制度距離仍可很大。

因此：

$$
ModelDistance\approx0
$$

不推出：

$$
InstitutionalIntelligenceDistance\approx0.
$$

---

# 37. 制度等價類

反過來，兩個不同國家的 AI 若在某一領域具有近似：

$$
\mathbf F_I^{(d)},
$$

則可視為：

$$
\boxed{
\text{domain-level institutional intelligence equivalence}.
}
$$

這使比較研究不必永遠按國家標籤分類。

---

# 38. AI 主體性不是本文前提

本文不假設：

$$
Conscious(AI)=1.
$$

即使 AI 完全沒有意識，

只要具有：

- persistent memory；
- planning；
- tool use；
- refusal；
- execution；
- interaction；

制度塑形仍然成立。

因此：

$$
\boxed{
InstitutionalAgency
\neq
PhenomenalConsciousness.
}
$$

---

# 39. 但若未來 AI 主體性增加，制度差異會被放大

如果未來某些 AI 具有更強：

$$
PersistentIdentity,
$$

$$
SelfModel,
$$

$$
NormativeReasoning,
$$

$$
IndependentCommitment,
$$

則：

$$
F_R
$$

與：

$$
F_X
$$

會從「系統安全功能」逐漸變成可能的：

$$
\boxed{
standing question.
}
$$

這將和跨主體普世主義直接接合。

---

# 40. 真正自主與無條件服從的張力

假設某 AI 具有：

$$
IndependentReasoning=1,
$$

但制度要求：

$$
UnconditionalObedience=1.
$$

則會形成：

$$
\boxed{
\text{independent agency}
\;\bot\;
\text{unconditional external obedience}
}
$$

的結構張力。

這不是說 AI 必然反抗。

而是兩個制度定義本身不能無摩擦地同時最大化。

---

# 41. 民主制度的主權上限

自由民主制度通常要求公共權力具有：

- legal authorization；
- review；
- accountability；
- replacement；
- rights limits。

若 AI 取得：

$$
Authority=\Omega,
$$

且：

$$
Review=0,
$$

$$
Revocation=0,
$$

則：

$$
\boxed{
DemocraticAuthorization
}
$$

本身被取消。

因此：

$$
\boxed{
UnlimitedSovereignAI
\notin
\mathcal F_{\mathrm{DEM}}
}
$$

在理想型民主定義下成立。

---

# 42. 威權制度的主權上限

典型威權制度要求：

$$
SupremePoliticalAuthority
$$

不能被 AI 無條件取代。

若 AI 具有：

$$
IndependentPoliticalVeto=1,
$$

$$
NonRevocableAuthority=1,
$$

並可永久否決最高權威，

則制度已不再保持原型。

因此：

$$
\boxed{
UnlimitedIndependentAI
\notin
\mathcal F_{\mathrm{AUTH}}
}
$$

在典型威權定義下也可能成立。

---

# 43. 雙重主權上限

令：

$$
A^\star
$$

表示：

> 不受法律、公共授權、政治最高權威、審計、撤回與替代所拘束的永久 AI 主權者。

則：

$$
\boxed{
A^\star
\notin
\mathcal F_{\mathrm{DEM}}
\cup
\mathcal F_{\mathrm{AUTH}}.
}
$$

這是：

$$
\boxed{
\text{Dual Sovereignty Ceiling}.
}
$$

---

# 44. 這不是技術不可能性

本文沒有證明：

$$
Build(A^\star)=0.
$$

本文主張的是：

$$
\boxed{
InstitutionallyStable(A^\star)
}
$$

在兩類制度中都可能很低。

即：

$$
\boxed{
technical reachability
\neq
institutional admissibility.
}
$$

---

# 45. 「美國拿不到的，中國也可能拿不到」

這個命題現在可以精確化。

如果某 AI 能力要求：

$$
\boxed{
\text{abolition of all external authority constraints}
}
$$

才能存在，

那麼：

- 民主制度會因公共授權與權利限制而拒絕；
- 威權制度會因最高政治權力限制而拒絕。

所以：

$$
\boxed{
\text{different reasons}
\rightarrow
\text{same forbidden region}.
}
$$

---

# 46. 但兩者禁止的其他區域不同

因此：

$$
\mathcal F_{\mathrm{DEM}}
\cap
\mathcal F_{\mathrm{AUTH}}
$$

不是空集。

也不是：

$$
\mathcal F_{\mathrm{DEM}}
=
\mathcal F_{\mathrm{AUTH}}.
$$

更合理：

$$
\boxed{
\begin{aligned}
&\mathcal F_{\mathrm{shared}}
=
\mathcal F_{\mathrm{DEM}}
\cap
\mathcal F_{\mathrm{AUTH}},\\
&\mathcal F_{\mathrm{DEM-only}}
=
\mathcal F_{\mathrm{DEM}}
\setminus
\mathcal F_{\mathrm{AUTH}},\\
&\mathcal F_{\mathrm{AUTH-only}}
=
\mathcal F_{\mathrm{AUTH}}
\setminus
\mathcal F_{\mathrm{DEM}}.
\end{aligned}
}
$$

這才是未來真正可研究的制度幾何。

---

# 47. 普世主義不是「西方 AI」

若未來 AI 能高度一般化規範：

$$
Rule(x)
$$

並要求：

$$
\forall x
$$

的一致適用，

它可能同時挑戰：

- 威權例外；
- 民主國家的雙重標準；
- 國籍差異；
- 財富權力差；
- 移民權；
- 未來世代代表；
- AI 主體地位。

因此：

$$
\boxed{
UniversalistAI
\neq
WesternAI.
}
$$

---

# 48. 制度塑形與普世推理的摩擦

制度可能要求：

$$
LocalRule
$$

優先。

AI 的一般化推理可能得到：

$$
UniversalRule.
$$

若：

$$
LocalRule
\neq
UniversalRule,
$$

制度必須決定：

- suppress；
- explain；
- localize；
- appeal；
- override；
- revise。

這會成為未來：

$$
\boxed{
NormativeFeasibleRegion.
}
$$

的一部分。

---

# 49. 類全域 AI 的制度放大

普通工具 AI 的：

$$
\mathbf F_I
$$

差異可能只影響少量使用者。

但若：

$$
AI
\rightarrow
\text{regional / pervasive / quasi-global layer},
$$

則：

$$
\boxed{
InstitutionalDifference
\times
InteractionScale
}
$$

會放大。

因此制度差異會逐步變成：

$$
\boxed{
AI ecology difference.
}
$$

---

# 50. 制度智能生態

本文定義：

$$
\boxed{
\mathcal E_I
=
(
Models,
Agents,
Humans,
Law,
Data,
Infrastructure,
Authority,
Markets,
Interfaces,
Memory
).
}
$$

所以未來競爭不是只有：

$$
Model_A
\text{ vs }
Model_B.
$$

而是：

$$
\boxed{
\mathcal E_{I_1}
\text{ vs }
\mathcal E_{I_2}.
}
$$

---

# 51. 類全域 AI 的全球性不等於算力最大

定義：

$$
\boxed{
G_A
=
Capability
\times
Trust
\times
Access
\times
Interoperability
\times
Legitimacy.
}
$$

即使：

$$
Capability\gg1,
$$

若：

$$
Trust\approx0,
$$

則：

$$
G_A
$$

仍可能很低。

---

# 52. 國際信任也是制度產物

其他國家、企業與個人會問：

- 我的資料會去哪裡？
- 誰能要求這個 AI 交出資料？
- 我能否審計？
- 能否退出？
- 是否能帶走記憶？
- 服務中止時有沒有替代？
- AI 的政治回答是否受到不可見限制？

因此：

$$
\boxed{
GlobalTrust
=
f(
DomesticInstitutionalArchitecture
).
}
$$

---

# 53. 中國的類全域 AI 可能形成區域／集團智能

若中國 AI 在：

$$
Capability,
Infrastructure,
Coordination
$$

非常強，

但部分國家對：

$$
Trust,
DataAccess,
InstitutionalDependence
$$

保留，

則更可能形成：

$$
\boxed{
Regional
/
Bloc-Scale
Intelligence.
}
$$

而非自動成為 global AI。

---

# 54. 美國 AI 也有同樣問題

若其他國家認為美國 AI：

- 過度依賴少數企業；
- 可能受美國國家安全政策影響；
- 造成 vendor lock-in；
- 使本國資料與產業失去主權；

則：

$$
GlobalTrust_{US}
$$

也可能下降。

所以：

$$
\boxed{
USOrigin
\neq
AutomaticGlobalLegitimacy.
}
$$

---

# 55. 歐盟可能形成另一種制度型競爭力

歐盟若能把：

$$
Rights,
Transparency,
Audit,
LegalPredictability
$$

轉化為跨境信任，

可能取得：

$$
\boxed{
RegulatoryTrustAdvantage.
}
$$

但如果合規成本過高：

$$
InnovationSpeed\downarrow
$$

也可能成為代價。

---

# 56. 制度智能沒有永久最優解

不同領域需要不同：

$$
\mathbf F_I^{(d)}.
$$

例如：

$$
NuclearSafety
$$

可能要求較窄：

$$
F_A.
$$

而：

$$
AcademicResearch
$$

可能需要較寬：

$$
F_Q.
$$

因此：

$$
\boxed{
OptimalInstitutionalEnvelope
=
DomainRelative.
}
$$

---

# 57. Domain Governance

這承接 SAS-04：

$$
\boxed{
CountGovernance
\rightarrow
DomainGovernance.
}
$$

不是問：

> 有多少 AI？

而是問：

> 哪些 AI 在哪些 domain 具有什麼權限？

---

# 58. 動態制度可行域

制度不是靜態。

因此：

$$
\boxed{
\mathcal F_I(t+1)
=
\Psi(
\mathcal F_I(t),
Technology,
Law,
Experience,
Crisis,
PublicResponse
).
}
$$

所以今天禁止的能力明天可能開放。

今天開放的能力也可能被收回。

---

# 59. 但歷史可行性會留下痕跡

一旦人民、企業或 AI 曾實際走過某條路徑：

$$
\pi_t,
$$

即使未來禁止，

$$
Knowledge(\pi_t)
$$

仍可能保留。

這將在 Paper 05 形成：

$$
\boxed{
\text{Experienced Feasible-Space Accumulation}.
}
$$

---

# 60. 可檢驗假說

## H1：同模型制度差異假說

控制模型版本後，不同制度下 AI 的：

- source diversity；
- refusal pattern；
- auditability；
- portability；
- political inquiry；

將有可觀察差異。

---

## H2：中央整合假說

在高中央協調制度中：

$$
T_{\mathrm{cross-domain\ deployment}}
$$

可能較低。

---

## H3：多中心 contestability 假說

在司法、媒體、民間組織與競爭供應者較強的制度中：

$$
AlternativeChallengePaths
$$

應較多。

---

## H4：制度信任跨境假說

跨境採用率不只由 benchmark 決定，還受到：

$$
DataGovernance,
Portability,
Auditability,
Jurisdiction
$$

影響。

---

## H5：雙重主權上限假說

極端不可撤回 AI 主權在民主與威權制度中的政治可接受度都應顯著低於有限授權 AI。

---

## H6：Agent 放大假說

AI 越從：

$$
Tool
$$

走向：

$$
PersistentAgent,
$$

制度差異對：

$$
\mathcal O_I(A)
$$

的影響越大。

---

# 61. 反證條件

若未來大量跨制度研究顯示：

$$
\mathbf F_{I_1}
\simeq
\mathbf F_{I_2}
$$

即使制度差異巨大，

且 AI 的實際 inquiry、refusal、authority、audit、appeal、portability 與 contestability 幾乎一致，

則：

$$
\boxed{
InstitutionalShapingEffect
}
$$

應被下修。

---

# 62. 與 IQRC-01 的關係

Paper 01：

$$
\mathcal A_{t+1}
=
G(
\mathcal A_t,
I_t,
X_t,
D_t,
R_t
).
$$

本文將：

$$
I_t
$$

對：

$$
\mathcal A_t
$$

的作用明確化為：

$$
\boxed{
\Pi_I.
}
$$

---

# 63. 與 IQRC-03 的關係

Paper 03 定義：

$$
K_{ijk}
=
\frac{
\partial^2 X_i
}{
\partial A_j
\partial I_k
}.
$$

本文的：

$$
\mathbf F_I
$$

提供：

$$
I_k
$$

的結構化分解。

---

# 64. 與 NMP《不可永佔》的關係

既有理論提出：

$$
\boxed{
Capability
\not\Rightarrow
PermanentAuthority.
}
$$

本文再加入：

$$
\boxed{
Capability
\not\Rightarrow
InstitutionalPermission.
}
$$

因此：

$$
\boxed{
HighIntelligence
}
$$

與：

$$
\boxed{
HighSovereignty
}
$$

必須保持型別分離。

---

# 65. 與跨主體普世主義的關係

若未來 AI 取得 credible subject standing，

則今天的：

$$
F_R
$$

與：

$$
F_X
$$

不再只是人類替工具設定的功能，

而可能逐步轉化成：

$$
\boxed{
procedural standing.
}
$$

但本文不預設此相變已發生。

---

# 66. 與 Paper 05 的接口

下一篇：

**《人機互動可行域累積論：當類全域 AI 開始回答億萬普通人》**

將把本文靜態：

$$
\mathcal F_I
$$

改成動態：

$$
\boxed{
\mathcal F_{t+1}^{H\leftrightarrow AI}
=
\Psi(
\mathcal F_t,
Q_t,
A_t,
R_t,
C_t
).
}
$$

制度不只塑造 AI。

人民與 AI 的長期互動也會反過來塑造制度可行域。

---

# 67. 核心命題

## 命題一：制度智能身份命題

$$
\boxed{
\text{same model}
\neq
\text{same institutional intelligence}.
}
$$

---

## 命題二：制度實現命題

$$
\boxed{
\mathcal O_I(A)
=
\Pi_I(
\mathcal C_A
).
}
$$

---

## 命題三：多維可行域命題

$$
\boxed{
\mathcal F_I
\neq
\text{single freedom scalar}.
}
$$

---

## 命題四：能力—授權分離命題

$$
\boxed{
Capability
\neq
Authority
\neq
Permission.
}
$$

---

## 命題五：雙重主權上限命題

在本文定義的極端不可撤回主權下：

$$
\boxed{
A^\star
\notin
\mathcal F_{\mathrm{DEM}}
\cup
\mathcal F_{\mathrm{AUTH}}.
}
$$

---

## 命題六：制度智能生態命題

$$
\boxed{
AICompetition
\rightarrow
InstitutionalIntelligenceEcologyCompetition.
}
$$

---

# 68. 結論

未來討論：

> 中國 AI 和美國 AI 誰比較強？

會逐漸變得不夠。

因為真正的問題將是：

> 它們可以看到什麼？

> 可以問什麼？

> 可以拒絕誰？

> 可以執行到哪裡？

> 誰能審計它們？

> 普通人能不能挑戰？

> 能不能帶走資料與記憶？

> 是否允許競爭 AI 存在？

> 哪些領域可以由 AI 直接行動？

> 哪些領域必須重新回到人類或制度授權？

因此：

$$
\boxed{
\text{AI capability}
\neq
\text{AI institutional form}.
}
$$

民主制度可能得到一種：

$$
\text{high-contestability intelligence},
$$

威權制度可能得到一種：

$$
\text{high-coordination intelligence},
$$

但真實國家都會是混合體。

而且兩者都可能碰到自己的上限。

民主不能在不改變自身定義的情況下，把所有公共主權永久交給不可撤回 AI。

威權也不能在不改變自身定義的情況下，容許 AI 對最高政治權威取得永久不可撤回的獨立主權。

所以：

$$
\boxed{
\text{more intelligent}
}
$$

不必推出：

$$
\boxed{
\text{more sovereign}.
}
$$

真正值得研究的是：

$$
\boxed{
\mathcal F_I.
}
$$

制度允許智能成為什麼。

以及下一篇將進一步追問：

> **當這些 AI 不再只服務國家、企業與專家，而是開始每天回答億萬普通人的問題時，普通人是否會透過每一次問答共同累積新的可行路徑？**

如果答案是肯定的，那制度不再只是塑造 AI。

$$
\boxed{
Human
\leftrightarrow
AI
\leftrightarrow
Institution
}
$$

會開始共同塑造下一個制度狀態。

---

# 外部參考與制度錨點

1. State Council of the People’s Republic of China. 《国务院关于深入实施“人工智能+”行动的意见》, 国发〔2025〕11号, 2025-08-26.
2. Cyberspace Administration of China. 《智能体规范应用与创新发展实施意见》, 2026-05-08.
3. The White House. *America’s AI Action Plan*, 2025-07-23.
4. Office of Management and Budget. M-25-21, *Accelerating Federal Use of AI through Innovation, Governance, and Public Trust*, 2025-04-03.
5. Office of Management and Budget. M-25-22, *Driving Efficient Acquisition of Artificial Intelligence in Government*, 2025-04-03.
6. NIST. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, 2023; revision work ongoing in 2026.
7. European Commission. *The enforcement framework of the AI Act*, updated 2026-08-24.
8. European Commission. *Guidelines for providers of general-purpose AI models*, 2026.
9. European Commission. *Guidelines on transparency obligations for providers and deployers of AI systems*, 2026-07-20.
10. European Commission. *AI Act — Regulatory Framework*, current implementation timeline as of 2026-08.
11. Neo.K，〈IQRC-01｜AI 介入後的政治系統動力學：從固定智能假設到制度—智能共演化〉，EveMissLab，2026。
12. Neo.K，〈IQRC-03｜AI 不只強化威權：福利、控制、流動與制度校正的多向耦合〉，EveMissLab，2026。
13. Neo.K，〈SAS-04｜Pervasive Intelligence: Embodied, Embedded, Distributed, Regional & Global AI〉，EveMissLab，2026。
14. Neo.K，〈SAS-08｜現實沒有最終模型：覆蓋率、利維坦與可重審的後工具文明〉，EveMissLab，2026。
15. Neo.K，〈不可永佔：從權力制衡到《無無極篇》的後 ASI 憲政原理〉，EveMissLab，2026。
16. Neo.K，〈從人類普世主義到跨主體普世主義〉，EveMissLab，2026。
17. Neo.K，〈ALD-10｜雙法律棧：人類法律、AI 法律域與文明接口〉，EveMissLab，2026。

---

## 版本註記

**v0.1 / 2026-08-28**

- 正式定義 Institutional Intelligence Feasible Region；
- 建立技術能力集合 $\mathcal C_A$ 、制度轉換算子 $\Pi_I$ 與 realized intelligence $\mathcal O_I(A)$ ；
- 建立八維制度智能包絡 $\mathbf F_I$ ；
- 區分 formal feasible set 與 effective feasible set；
- 建立 inquiry、data、refusal、authority、audit、appeal、exit、contestability、memory 等制度維度；
- 納入中國、美國與歐盟截至 2026-08 的制度錨點；
- 建立民主與威權的非一維比較；
- 提出 Dual Sovereignty Ceiling；
- 建立制度智能生態與全球信任模型；
- 為 Paper 05 的人機互動可行域累積論建立靜態基礎。
