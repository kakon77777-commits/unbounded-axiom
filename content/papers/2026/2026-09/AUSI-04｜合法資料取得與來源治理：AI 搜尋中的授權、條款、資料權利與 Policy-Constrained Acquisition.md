# AI-Native Unified Search Intelligence (AUSI) Series — Paper 04

## 合法資料取得與來源治理：AI 搜尋中的授權、條款、資料權利與 Policy-Constrained Acquisition

**English Title:** *Lawful Data Acquisition and Source Governance: Permissions, Terms, Data Rights, and Policy-Constrained Acquisition in AI Search*

**Version:** v0.1  
**Date:** 2026-08-30  
**Status:** Canonical Draft  
**Series:** AI-Native Unified Search Intelligence (AUSI)  
**Predecessor:** Paper 03 — *任務驅動的自主搜尋規劃：AI Search Planner、動態方法選擇與 Search Plan Optimization*  
**Reference Implementation Direction:** `ai-web-research`

---

## 摘要

AI 原生搜尋系統的能力越強，資料取得治理的重要性越高。對人類使用者而言，「網站可以打開」「資料是公開的」「robots.txt 沒有禁止」「有一個 API」「內容可以引用」常被直覺地混成「可以自動取得並自由使用」。然而在實際資料生態中，這些命題彼此獨立：一項資料可以公開瀏覽但禁止 automated queries；可以透過正式 API 取得但要求 authentication、rate limits、attribution 或特定 disclaimer；可以下載並在內部資料庫中使用，但限制原始資料再散布；可以在法律上屬於 public-domain 或 open-license 資料，但其具體服務端點仍有 access controls、registration requirements 與 technical policies；同一 provider 中不同 series、dataset、distribution 或第三方內容也可能具有不同權利狀態。

本文提出 **Source Rights & Policy Registry（SRPR）** 與 **Policy-Constrained Acquisition** 框架，將資料取得權限從單一 Boolean 拆解為多維 action-specific policy。本文區分 access、automation、scraping、crawling、bulk acquisition、bulk storage、caching、indexing、transformation、internal use、commercial use、raw redistribution、derivative distribution、sublicensing、model training、quotation 與 linking 等不同動作；並將 policy decision 定義為 `ALLOW`、`ALLOW_WITH_OBLIGATIONS`、`DENY`、`UNKNOWN` 與 `REVIEW_REQUIRED` 五種狀態。`UNKNOWN` 不得被 AI 默認推論為 `ALLOW`。

本文進一步提出 Policy Provenance、Policy Drift、Access Surface、Usage Envelope、Rights Propagation、Obligation Carrying、Policy Conflict Resolution 與 Pre-Execution Acquisition Gate。Search Planner 在比較搜尋效用之前，必須先將技術上可行的 action space 縮小為政策上允許的 action space：

$$
\mathcal{A}^{\text{allowed}}_t
\subseteq
\mathcal{A}^{\text{technically-feasible}}_t
$$

本文以 RFC 9309 Robots Exclusion Protocol、WIPO PATENTSCOPE、EPO Open Patent Services、USPTO Open Data Portal、Data.gov、FRED API 與 NOAA Climate Data Online 作為具體案例，說明 robots rules、服務條款、資料授權、API authentication、rate limits 與資料本體權利不能被混成同一層。本文同時參考 W3C ODRL 與 DCAT 對 permission、prohibition、duty、license、rights 與 access rights 的既有標準化思想。

本文不把 SRPR 定位為法律判決器。實際法律效果會依司法管轄、契約、法定例外、資料類型與個案事實而異；任何高風險法律判斷仍可能需要專業法律審查。SRPR 的功能是讓 AI 搜尋 runtime 不再對資料權利保持結構性失憶：它必須知道自己從哪個 surface 取得什麼資料、基於哪些可驗證 policy source、允許做哪些後續操作、負有哪些義務，以及何時必須拒絕、自動降級或交由人類審查。

**關鍵詞：** AI-Native Search、Data Governance、Source Rights、Policy-Constrained Acquisition、Terms of Use、Data Licensing、Robots Exclusion Protocol、ODRL、DCAT、Provenance、Automated Access、Search Governance

---

# 1. 問題：技術上取得得到，不等於可以任意取得與使用

Paper 03 定義 Search Planner 的可行行動：

$$
a_t
=
(
M_i,
P_j,
\theta_t,
\Gamma_t
)
$$

並提出：

$$
\operatorname{Allowed}(M_i,P_j,T,S_t)
$$

作為 hard guard。

本篇的問題就是：

> **`Allowed(...)` 到底應該如何計算？**

最危險的簡化是：

```text
public URL
→ HTTP 200
→ allowed
```

或者：

```text
robots.txt allows
→ legally allowed
```

又或者：

```text
open data
→ any automated use allowed
```

這些推論都不足。

本文首先提出基本不等式：

$$
\boxed{
\text{Technically Accessible}
\neq
\text{Contractually Permitted}
\neq
\text{Licensed for Reuse}
\neq
\text{Lawfully Reusable in Every Context}
}
$$

資料取得必須分層。

---

# 2. 本文中的「合法」不是自動法律判決

本文使用「合法資料取得」作為工程目標，但不主張 runtime 可以自動完成所有法律解釋。

更精確地說，系統希望達成：

$$
\text{Policy-Constrained Acquisition}
$$

亦即：

> 在已知且可驗證的 access rules、provider terms、dataset licenses、rights statements、technical constraints、organizational policy 與其他可機器化條件內，只產生可被允許或明確交由審查的取得行動。

因此：

$$
\operatorname{PolicyDecision}
\neq
\operatorname{LegalJudgment}
$$

在以下情況，系統應保留：

```text
REVIEW_REQUIRED
```

例如：

- 條款彼此衝突；
- 權利來源不清楚；
- 是否構成 fair use / statutory exception；
- 涉及 sui generis database rights；
- 涉及個人資料或敏感資料；
- 跨司法管轄；
- 商業產品的再散布範圍不明；
- 契約約束需要法律解釋。

AI 的進步不應被用來掩蓋真正的不確定性。

---

# 3. Robots Exclusion Protocol 的定位

RFC 9309 將 Robots Exclusion Protocol 標準化，並明確指出其規則不是 access authorization；它也不是有效內容安全措施的替代品。

因此：

$$
\operatorname{RobotsAllow}(u)
\not\Rightarrow
\operatorname{Authorization}(u)
$$

同樣：

$$
\operatorname{RobotsDisallow}(u)
$$

是一個 crawler policy signal，但它不應被系統錯誤解釋成完整的 copyright、license、contract 或 statutory-rights 判定。

這個區分是 Source Governance 的第一個基本 invariant：

> **robots policy 是 operational crawling policy，不是完整權利授權書。**

---

# 4. 公開介面也可能禁止自動化

WIPO PATENTSCOPE 是公開的專利資訊服務，但其公開資料庫使用條款明確禁止 automated queries、bulk acquisition、bulk downloading、bulk storing 與 web scraping，並要求特定來源標示與 disclaimer。

因此：

$$
\text{Publicly Viewable}
\not\Rightarrow
\text{Automation Allowed}
$$

也就是說，AI Search Planner 不能因為人類瀏覽器可以使用 PATENTSCOPE，就自動生成：

```text
crawl entire PATENTSCOPE
```

這是一個典型的：

$$
\operatorname{Capability}=1
$$

但：

$$
\operatorname{Allowed}=0
$$

案例。

---

# 5. 同一資料領域可以存在正式 machine-access surface

EPO 的 Open Patent Services（OPS）則提供另一種完全不同的 access surface。

OPS 是正式的機器可讀 Web Service，提供 REST/XML 介面。其條款允許符合條件的使用者取得 OPS 資料，將其納入自己的 machine-readable databases、products 與 services；但同時仍有 fair-use、下載量、資料再散布與其他條款。

因此：

$$
\text{Patent Data}
$$

本身並不能決定取得方式。

真正需要判斷的是：

$$
(\text{Asset},\text{Access Surface},\text{Action},\text{Purpose})
$$

例如：

```text
same patent information
├── public web UI
├── official API
├── bulk dataset
└── licensed derivative product
```

每一條 surface 的 policy 都可能不同。

---

# 6. Open Data 也不等於 Anonymous Access

USPTO Open Data Portal 在 2026 年 6 月 18 日起要求使用 USPTO.gov 帳號註冊後存取。

這說明：

$$
\text{Public Data}
\not\Rightarrow
\text{Anonymous Access}
$$

資料可以保持公開性，但 provider 仍可要求：

- registration；
- authentication；
- profile information；
- MFA；
- API credentials；
- technical controls。

因此 `access_level=public` 與 `authentication=none` 必須是兩個不同欄位。

---

# 7. Open License 與 Access Policy 必須分離

Data.gov 的官方政策指出，多數美國聯邦政府資料可自由使用，但個別 dataset 仍應查看其 `Access & Use Information`；非聯邦資料可能具有完全不同的 licensing terms。

DCAT 也明確區分：

- `license`；
- `accessRights`；
- broader `rights` statements。

因此：

$$
\text{License}
\neq
\text{Access Rights}
$$

一項資料可以：

```text
license = CC0
access = authenticated API
```

也可以：

```text
license = restrictive
access = publicly readable webpage
```

兩者不是同一軸。

---

# 8. Provider 條款也不必然等於底層資料權利

FRED API 的條款提供一個非常重要的案例：FRED API 可以提供大量經濟資料，但其中一些 series 可能由第三方擁有並受到額外 copyright restrictions；使用 API 並不自動覆蓋底層 series owner 的權利與限制。

因此：

$$
\text{API Permission}
\not\Rightarrow
\text{All Underlying Data Rights Granted}
$$

這對經濟研究網站尤其重要。

Source Registry 必須能描述：

```text
Provider Policy
    ↓
Dataset Policy
        ↓
Series / Item Policy
```

而不是只保存 provider-level license。

---

# 9. Authentication 與 Rate Limit 是 Policy 的一部分

NOAA Climate Data Online API 要求 access token，並對 token 設置每秒與每日請求限制。

這些限制不一定是 copyright 問題，但仍是 runtime 必須遵守的 acquisition constraints。

因此：

$$
\text{Policy}
=
\text{Rights}
+
\text{Access Conditions}
+
\text{Operational Conditions}
$$

至少在 AI Search Runtime 的工程定義中如此。

---

# 10. Source Governance 的三層分離

本文提出三層治理模型。

## Layer A — Access Governance

回答：

> 能以什麼方式取得？

例如：

- public UI；
- API；
- bulk download；
- authenticated endpoint；
- local archive；
- manual-only access。

## Layer B — Acquisition Governance

回答：

> AI 可以用什麼自動化方式取得？

例如：

- automated query；
- crawler；
- scraper；
- scheduled monitoring；
- bulk download；
- cache；
- repeated retrieval。

## Layer C — Usage Governance

回答：

> 取得後可以怎麼使用？

例如：

- internal research；
- commercial analysis；
- quotation；
- transformation；
- indexing；
- redistribution；
- derivative product；
- model training。

因此：

$$
\boxed{
\text{Access}
\neq
\text{Acquisition}
\neq
\text{Usage}
}
$$

---

# 11. Action-Specific Rights Model

本文不使用單一：

```text
allowed: true
```

而定義 action universe：

$$
\mathcal{X}
=
\{
x_{\text{view}},
x_{\text{manual-query}},
x_{\text{automated-query}},
x_{\text{crawl}},
x_{\text{scrape}},
x_{\text{bulk-download}},
x_{\text{bulk-store}},
x_{\text{cache}},
x_{\text{index}},
x_{\text{transform}},
x_{\text{internal-use}},
x_{\text{commercial-use}},
x_{\text{redistribute-raw}},
x_{\text{distribute-derived}},
x_{\text{sublicense}},
x_{\text{train-model}},
x_{\text{quote}},
x_{\text{link}}
\}
$$

對每一個 action 個別判斷。

---

# 12. 五值 Policy Decision

對某來源資產 $A$ 、surface $S$ 、action $x$ 、task $T$ 與時間 $t$：

$$
D(A,S,x,T,t)
\in
\{
\mathsf{ALLOW},
\mathsf{ALLOW\_WITH\_OBLIGATIONS},
\mathsf{DENY},
\mathsf{UNKNOWN},
\mathsf{REVIEW}
\}
$$

## 12.1 ALLOW

已取得明確、適用且足夠的允許依據。

## 12.2 ALLOW_WITH_OBLIGATIONS

可以執行，但必須同時攜帶義務。

例如：

- attribution；
- disclaimer；
- share-alike；
- identification；
- payment；
- rate limit；
- usage notice。

## 12.3 DENY

已知適用規則明確禁止。

## 12.4 UNKNOWN

目前缺乏足夠 policy evidence。

核心原則：

$$
\boxed{
\mathsf{UNKNOWN}
\not\equiv
\mathsf{ALLOW}
}
$$

## 12.5 REVIEW

規則存在，但需要人類或法律專業判斷。

---

# 13. Permission、Prohibition、Duty、Constraint

W3C ODRL 已提供一套成熟概念：

- Permission；
- Prohibition；
- Duty；
- Constraint；
- Asset；
- Party；
- Action。

本文不需要重新發明這些基本 policy concepts。

SRPR 可以：

1. 直接採用 ODRL；
2. 建立 ODRL-inspired internal representation；
3. 使用簡化 schema，再提供 ODRL export。

例如：

$$
\operatorname{Permission}(x,A)
$$

可以帶有：

$$
\operatorname{Duty}(\text{attribute-source})
$$

以及：

$$
\operatorname{Constraint}(\text{requests-per-minute}\le 10)
$$

這比單純的 `allowed=true` 更符合實際世界。

---

# 14. Source Policy / Rights Registry

本文提出：

> **Source Rights & Policy Registry（SRPR）**

其不是「所有網站法律資料庫」，而是 AI Search Runtime 對已知 source / provider / dataset policy 的可驗證 operational registry。

最小結構：

```text
SourcePolicyProfile
├── source_id
├── provider_id
├── asset_scope
├── access_surface
├── policy_sources
├── policy_version
├── observed_at
├── effective_at
├── expires_at
├── jurisdiction_context
├── permissions
├── prohibitions
├── duties
├── constraints
├── authentication
├── rate_limits
├── retention_rules
├── attribution_rules
├── redistribution_rules
├── privacy_flags
├── downstream_usage
├── confidence
├── review_status
└── policy_hash
```

---

# 15. Policy Source 也必須有 Provenance

如果 AI 根據錯誤或過期 ToS 阻止／允許一個搜尋行動，後果都可能很大。

因此 policy 本身也是 evidence。

定義：

$$
P_s
=
(
u,
h,
t_r,
t_e,
v,
q,
m
)
$$

其中：

- $u$：policy URL / source identifier；
- $h$：content hash；
- $t_r$：retrieval time；
- $t_e$：effective time；
- $v$：version；
- $q$：source quality / authority；
- $m$：extraction method。

所以：

> **Policy Provenance 是 Evidence Provenance 的一個特殊子類。**

---

# 16. Policy Drift

Terms、API limits、registration requirements 與 licensing condition 會改變。

例如某 API 今天：

```text
anonymous access
```

未來可能改成：

```text
registered access
```

因此：

$$
\operatorname{Policy}(t_1)
\neq
\operatorname{Policy}(t_2)
$$

SRPR 必須保存：

```text
observed_at
effective_at
last_checked
next_review
policy_hash
```

對高風險 task，可以要求：

$$
t_{\text{now}}-t_{\text{last-check}}
<
\Delta_{\max}
$$

否則重新驗證 policy。

---

# 17. Access Surface 是一級實體

同一 organization 可以提供：

```text
web_ui
public_api
authenticated_api
bulk_data
download_file
rss_feed
licensed_dataset
```

因此：

$$
\operatorname{Policy}
:
(\text{Provider},\text{Surface})
\rightarrow
\text{Rules}
$$

不能只有：

```text
provider = WIPO
allowed = ?
```

應該是：

```text
provider = WIPO
surface = PATENTSCOPE public database
action = automated_query
```

這才具有足夠精度。

---

# 18. Asset Scope 也必須細分

Provider policy 可能只規範 service。

Dataset license 可能規範 collection。

Individual item 可能又包含第三方內容。

因此可定義：

$$
A_{\text{service}}
\supset
A_{\text{dataset}}
\supset
A_{\text{distribution}}
\supset
A_{\text{item}}
\supset
A_{\text{field}}
$$

不同層級規則可以重疊。

例如：

> API 可以使用，但某些 series 有第三方 copyright。

這就是 provider-level permission 與 item-level restriction 同時存在。

---

# 19. Applicable Rule Set

對行動 $a$：

$$
\mathcal{R}(a)
=
\{
r_1,\ldots,r_n
\}
$$

可能來自：

- API terms；
- website terms；
- dataset license；
- item rights statement；
- authentication agreement；
- bulk-data contract；
- robots policy；
- rate-limit documentation；
- organizational policy；
- user-specified constraints；
- jurisdiction-specific legal review result。

Planner 不應自行挑一條最方便的 rule。

而應建立完整 applicable rule set。

---

# 20. Rule Precedence 不能粗暴寫死

很容易想寫：

```text
DENY always wins
```

但現實可能存在：

- general prohibition；
- specific API grant；
- paid contract exception；
- account-specific entitlement；
- later policy version；
- domain-specific statutory exception。

因此本文不宣稱一個跨司法管轄的法律 precedence theorem。

工程上應使用：

```text
specificity
effective time
asset scope
surface scope
party scope
contract identity
explicit override relation
human-reviewed precedence
```

建立 machine-operational precedence。

如果仍衝突：

$$
D=\mathsf{REVIEW}
$$

而不是 AI 自己做法律創造。

---

# 21. Silence 不等於 Permission

若 Terms 沒有提到：

```text
model_training
```

系統不能直接寫：

```text
model_training = allowed
```

正確狀態通常是：

```text
UNKNOWN
```

除非存在其他適用權利來源。

因此：

$$
\operatorname{NotMentioned}(x)
\Rightarrow
D(x)=\mathsf{UNKNOWN}
$$

這是一個保守的 runtime policy，不是法律命題。

---

# 22. Robots、Terms、License、Technical Capability 四層不可互相取代

本文提出四層不變量：

## I1

$$
\text{robots}
\neq
\text{authorization}
$$

## I2

$$
\text{terms}
\neq
\text{data license}
$$

## I3

$$
\text{data license}
\neq
\text{access control}
$$

## I4

$$
\text{technical capability}
\neq
\text{permission}
$$

這四個 invariant 應進入 runtime validator。

---

# 23. Authorized Acquisition Gate

在 Paper 03 中：

```text
candidate action
↓
capability validation
↓
policy validation
↓
utility ranking
```

本文將 policy validation 正式化為：

> **Authorized Acquisition Gate（AAG）**

輸入：

$$
G_{\text{in}}
=
(
T,
M_i,
P_j,
S_j,
\theta_t,
A,
\text{Party},
t
)
$$

輸出：

$$
G_{\text{out}}
=
(
D,
O,
L,
R
)
$$

其中：

- $D$：decision；
- $O$：obligations；
- $L$：operational limits；
- $R$：policy evidence references。

---

# 24. Gate Decision

只有：

$$
D
\in
\{
\mathsf{ALLOW},
\mathsf{ALLOW\_WITH\_OBLIGATIONS}
\}
$$

才能自動進入 executor。

若：

$$
D=\mathsf{DENY}
$$

直接拒絕該 action。

若：

$$
D=\mathsf{UNKNOWN}
$$

Planner 可以：

- 改用另一 provider；
- 改用另一 surface；
- 降級為 manual instruction；
- 尋找正式 API；
- 要求人類確認。

若：

$$
D=\mathsf{REVIEW}
$$

則建立 escalation。

---

# 25. Allowed Action Space

Paper 03 的可行 action space：

$$
\mathcal{A}^{\text{technical}}_t
$$

經 AAG 後：

$$
\mathcal{A}^{\text{allowed}}_t
=
\{
a
\in
\mathcal{A}^{\text{technical}}_t
\mid
D(a)\in
\{
\mathsf{ALLOW},
\mathsf{ALLOW\_WITH\_OBLIGATIONS}
\}
\}
$$

因此：

$$
\boxed{
\mathcal{A}^{\text{allowed}}_t
\subseteq
\mathcal{A}^{\text{technical}}_t
}
$$

Planner 只能在前者做 utility optimization。

---

# 26. Obligation Carrying

允許取得並不表示義務完成。

假設：

$$
D=\mathsf{ALLOW\_WITH\_OBLIGATIONS}
$$

且：

$$
O=
\{
o_{\text{attribution}},
o_{\text{disclaimer}}
\}
$$

則資料結果必須攜帶：

```text
UsageEnvelope
```

而不是只在下載當下檢查一次。

這樣資料進入：

- evidence store；
- database；
- report；
- downstream API；
- derivative product；

時，義務仍存在。

---

# 27. Usage Envelope

定義：

$$
U_E(d)
=
(
P_d,
F_d,
O_d,
X_d,
T_d
)
$$

其中：

- $P_d$：permissions；
- $F_d$：prohibitions；
- $O_d$：obligations；
- $X_d$：constraints；
- $T_d$：policy/provenance references。

資料不只是一個 value。

它同時攜帶「怎麼來、能怎麼用」的 envelope。

---

# 28. Rights Propagation

資料經過 transformation：

$$
d'
=
f(d)
$$

不代表：

$$
U_E(d')
=
\varnothing
$$

也不代表權利自動擴張。

因此：

$$
U_E(d')
=
\operatorname{Propagate}
(
U_E(d),
f,
\text{policy rules}
)
$$

若 transformation 是否解除某限制需要法律解釋：

$$
D=\mathsf{REVIEW}
$$

而不是 AI 宣稱：

> 經過摘要後就沒有原本限制了。

---

# 29. 多來源融合的 Rights Problem

若：

$$
d^*
=
f(d_1,d_2,\ldots,d_n)
$$

且：

$$
U_E(d_i)
$$

彼此不同，最終產品的 usage envelope 不能簡單取：

```text
most permissive
```

也不能永遠粗暴取：

```text
most restrictive
```

因為不同 license / obligation 可能作用於不同 components。

因此需要：

```text
component provenance
component rights
transformation graph
distribution mode
```

若無法安全求解：

$$
\mathsf{REVIEW}
$$

---

# 30. Cache 不等於 Bulk Store

很多系統會把：

- transient request cache；
- search-result cache；
- long-term archival copy；
- bulk corpus mirror；

全部叫做「cache」。

這在 policy 上非常危險。

因此至少區分：

$$
x_{\text{transient-cache}}
$$

$$
x_{\text{persistent-cache}}
$$

$$
x_{\text{bulk-store}}
$$

$$
x_{\text{archive}}
$$

每一種需要不同 decision。

---

# 31. Indexing 也不是單純保存

建立：

- lexical index；
- vector index；
- embeddings；
- knowledge graph；

都可能構成不同的 derived representation。

因此：

$$
x_{\text{index}}
$$

應被獨立建模。

而：

$$
x_{\text{train-model}}
$$

更不能被默認等同於 `index` 或 `internal-use`。

---

# 32. Commercial Use 是下游用途，不是取得方法

很多資料取得行為本身完全相同：

```text
GET /dataset
```

但用途不同：

```text
personal research
internal R&D
public academic site
paid SaaS
redistributed database
model training
```

因此 Policy Gate 必須接收 task purpose：

$$
T_{\text{purpose}}
$$

而不是只根據 HTTP request 判斷。

---

# 33. Attribution 是可執行義務

Attribution 不應只是一段 README 說明。

可以定義：

```text
AttributionDuty
├── source_name
├── source_url
├── required_text
├── placement
├── persistence
└── downstream_requirement
```

報告產生器在輸出時檢查：

$$
\operatorname{DutySatisfied}=1
$$

這樣 policy 才真正進入 runtime。

---

# 34. Disclaimer 也應可攜帶

某些 provider 要求特定 disclaimer。

如果 acquisition 結果進入：

- report；
- dashboard；
- exported CSV；
- API response；

runtime 應知道 disclaimer 是否仍須傳遞。

因此 obligation 不只是「執行前條件」，也可能是：

$$
\text{downstream duty}
$$

---

# 35. Rate Limit 不應只靠 429 才學會

如果 provider 已經明確公告：

$$
r_{\max}
$$

runtime 應在 planner / scheduler 先限制：

$$
r_{\text{planned}}
\le
r_{\max}
$$

而不是：

> 打到 429 再 exponential backoff。

HTTP failure handling 與 policy compliance 是兩件事。

---

# 36. Authentication Credential 也是 Governance Boundary

API key、OAuth token、account session 代表：

> runtime 具有某 Party 的 entitlement。

因此 credential 不應只被當成 network configuration。

可以表示：

$$
\operatorname{Entitlement}
(
\text{Party},
\text{Credential},
P_j,
S_j
)
$$

但：

$$
\text{has credential}
\not\Rightarrow
\text{all actions allowed}
$$

credential 只證明某種 access identity，不替代 Terms。

---

# 37. Party / Organization Context

同一 API 的權利可能依使用者身分不同。

例如：

- individual；
- academic；
- commercial；
- subscriber；
- enterprise licensee；
- anonymous user。

因此 Gate 輸入需包含：

$$
\text{PartyProfile}
$$

但只保存政策判斷所需最少資訊，避免過度蒐集個人資料。

---

# 38. Privacy Gate 必須與 Rights Gate 並存

合法使用授權不代表資料沒有 privacy 問題。

例如：

$$
\text{Licensed Dataset}
$$

仍可能含個人資料。

因此 runtime 最少需要：

$$
\operatorname{RightsGate}
$$

與：

$$
\operatorname{PrivacyGate}
$$

兩者都通過才可進入某些下游處理。

本文不完整建立 privacy law model，但要求架構上不能把 privacy 混進 copyright/license 的單一欄位。

---

# 39. Jurisdiction Context

對跨國搜尋，可以記錄：

$$
J
=
(
J_{\text{source}},
J_{\text{operator}},
J_{\text{contract}},
J_{\text{subject}}
)
$$

但 runtime 不應自動宣稱自己已解出所有 conflict-of-laws 問題。

其主要用途是：

- 選擇適用 policy profile；
- 觸發 legal review；
- 避免把一國的 public-domain 判定直接投射到全球。

---

# 40. Data.gov 案例：Open 不代表所有 catalog item 同權利

Data.gov 強調美國聯邦政府資料多數在美國境內可無限制使用，但也要求使用者查看各 dataset 的 Access & Use Information；非聯邦來源可以有其他授權。

因此 Registry 不應：

```text
host = data.gov
license = public_domain
```

而應：

```text
catalog_entry
    ↓
publisher
    ↓
distribution
    ↓
license / access rights
```

這也是 DCAT-style metadata 值得整合的原因。

---

# 41. FRED 案例：Aggregator 不是所有資料的權利所有人

經濟資料平台常聚合多來源 series。

因此：

$$
\operatorname{Provider}(d)
\neq
\operatorname{RightsHolder}(d)
$$

SRPR 需要：

```text
provider
publisher
original_source
rights_holder_if_known
series_notice
```

以避免 AI 認為：

> 「從同一 API 取出的資料，所以授權一定相同。」

---

# 42. NOAA 案例：Operational Policy 影響 Search Planner

如果 API 每 token 有：

- per-second limit；
- per-day limit；

Planner 在執行一個 30 年高頻資料拉取前，應先估算：

$$
N_{\text{requests}}
$$

若超過當日 budget：

- batch；
- delay；
- use bulk surface；
- change endpoint；
- schedule later；
- select alternative provider。

這是 policy-aware planning，而不是 error recovery。

---

# 43. WIPO / EPO 案例：Provider Substitution 必須改 Surface，不只是換 URL

如果 public Web UI 禁止 automation，而另有正式 machine service：

Planner 應：

$$
P_{\text{web-ui}}
\xrightarrow{\text{policy-deny}}
P_{\text{official-api}}
$$

這是一種合法性導向的 provider routing。

因此 search intelligence 的價值不只是：

> 找得到資料。

而是：

> **找得到適合機器取得且權利邊界清楚的正式入口。**

---

# 44. Source Preference Function

Planner 可加入 policy quality：

$$
Q_P(P_j,S_j)
$$

例如偏好：

1. official documented API；
2. official bulk dataset；
3. open structured feed；
4. public webpage with explicit automation permission；
5. manual-only public source；
6. unclear third-party mirror。

但這不是絕對排序。

某些任務需要：

- historical archive；
- alternative source；
- independent corroboration。

因此只是 task-conditioned preference。

---

# 45. Rights Quality 也是 Source Quality

傳統 source ranking 可能考慮：

- authority；
- relevance；
- freshness。

AUSI 還需要：

$$
\text{Rights Clarity}
$$

若兩個來源內容等價：

$$
R_1\approx R_2
$$

但：

$$
Q_{\text{rights}}(R_1)
>
Q_{\text{rights}}(R_2)
$$

Planner 可以優先使用權利更清楚的來源。

這能降低 downstream compliance cost。

---

# 46. Unknown Policy 的 Fallback Strategy

若：

$$
D=\mathsf{UNKNOWN}
$$

runtime 不必直接放棄 task。

可以：

```text
1. Search official API documentation
2. Search official terms / license
3. Search machine-readable rights metadata
4. Find alternate authorized provider
5. Restrict to manual-access recommendation
6. Ask for human/legal review
```

因此：

$$
\mathsf{UNKNOWN}
$$

是一個 planner state，而不是死路。

---

# 47. Denied Action 不等於 Denied Information Need

如果：

$$
D(M_i,P_j)=\mathsf{DENY}
$$

並不代表：

$$
T=\text{impossible}
$$

Planner 可以尋找：

$$
(M_i,P_k)
$$

或：

$$
(M_l,P_k)
$$

例如：

- 不 scrape UI；
- 改用 API；
- 不 bulk mirror；
- 改 query on demand；
- 不 redistribute raw；
- 只輸出 derived statistics；
- 不自動抓；
- 交給人工使用介面。

這是 Policy-Aware Replanning。

---

# 48. Policy Search 本身是一種 Search Method

如果缺乏 policy evidence，可以調用：

$$
M_{\text{policy-discovery}}
$$

查找：

- official terms；
- license page；
- API docs；
- data policy；
- robots；
- developer portal；
- dataset metadata。

因此 Search Runtime 可以「先搜尋如何合法搜尋」。

這是一個很重要的 reflexive property：

$$
\text{Search}
\rightarrow
\text{Search Policy}
\rightarrow
\text{Allowed Search}
$$

---

# 49. Machine-Readable Policy

理想情況下，provider 不必讓 AI 從長篇 ToS 自己猜。

可利用：

- ODRL；
- DCAT license/accessRights；
- SPDX-like identifiers；
- Creative Commons canonical license URIs；
- provider-specific policy JSON。

例如：

```text
policy:
  automated_query: allow
  scraping: deny
  bulk_download:
    decision: conditional
    max_per_week: ...
  redistribution_raw: deny
  derivative_use: allow
  attribution:
    required: true
```

但 machine-readable metadata 本身仍需要 authority 與 version provenance。

---

# 50. Human-Readable Terms 解析

現實中很多 Terms 只有自然語言。

因此 AI 可以協助：

$$
\operatorname{ExtractPolicy}
(
\text{Terms Document}
)
\rightarrow
\text{Candidate Policy Rules}
$$

但是在高風險來源中：

$$
\text{LLM Extracted Rule}
$$

應標記為：

```text
machine_interpreted
not_human_verified
```

並保留原文定位。

AI 可以解析，但不能把解析結果偽裝成 provider 自己發布的 machine-readable policy。

---

# 51. Policy Confidence

定義：

$$
C_P
\in
[0,1]
$$

但 confidence 不應覆蓋 decision semantics。

例如：

```text
decision = REVIEW
confidence = 0.93 that terms are ambiguous
```

是合理的。

而不是：

```text
0.7 allowed
```

直接模糊掉 prohibition。

---

# 52. Policy Evidence Object

可以定義：

$$
e_p
=
(
\text{rule},
\text{source},
\text{quote-location},
\text{effective-time},
\text{retrieved-time},
\text{hash},
\text{interpretation-status}
)
$$

這使任何 `ALLOW` / `DENY` 都能回答：

> 根據什麼？

---

# 53. Policy Receipt

Search Receipt 應增加：

```text
policy_decisions
provider_surface
policy_sources
policy_versions
obligations
rate_limits
fallbacks
review_events
```

因此未來 audit 可以重建：

> 為何這次用了 EPO API 而沒有抓 PATENTSCOPE UI？

這是非常有價值的企業合規證據。

---

# 54. Policy Cache

每次搜尋都重新下載 Terms 會很浪費。

可以 cache policy：

$$
P_c
$$

但 policy cache 需要：

```text
ttl
etag/hash
last_checked
effective_date
risk_class
```

低風險來源可以較長 TTL。

高風險商業／專利來源則縮短。

---

# 55. Policy Change Detection

若：

$$
h_{t_1}
\neq
h_{t_2}
$$

不能立即假設 policy semantics 一定改變。

但可以觸發：

$$
M_{\text{policy-diff}}
$$

比較：

- permissions；
- prohibitions；
- duties；
- rates；
- authentication；
- redistribution terms。

重大變更則 invalidates affected cached decisions。

---

# 56. Revocation 與 Downstream State

如果 provider terms 改變，是否影響過去合法取得的資料，可能是契約與法律問題。

因此 runtime 不應自動刪除或自動宣稱 grandfathered。

應建立：

```text
policy_changed
affected_assets
past_acquisition_time
original_policy
current_policy
review_required
```

供後續判斷。

---

# 57. Source Rights 與 Evidence Independence 是不同維度

合法來源不一定可靠。

可靠來源也不一定允許 bulk reuse。

因此：

$$
Q_{\text{source}}
=
(
Q_{\text{authority}},
Q_{\text{evidence}},
Q_{\text{rights}},
Q_{\text{freshness}}
)
$$

不能壓成單一「可信度」。

Paper 05 將完整處理 Evidence Quality。

---

# 58. Patent Intelligence 的特殊價值

專利搜尋尤其需要 SRPR，因為：

- 多司法管轄；
- 多官方資料庫；
- 同一 patent family 多 publication；
- full text / legal status / image data；
- public UI 與 machine API policy 可能不同；
- downstream commercial product 可能涉及 redistribution terms。

因此 Patent Domain Pack 不應只列：

```text
EPO
WIPO
USPTO
```

而應列：

```text
provider
surface
capability
policy
rights
rate
authentication
evidence role
```

---

# 59. 經濟研究網站的特殊價值

經濟資料常見：

- official government data；
- central bank data；
- international organizations；
- third-party licensed series；
- revisions / vintages；
- derived indicators。

因此：

$$
\text{Series Identity}
+
\text{Rights Identity}
+
\text{Version Identity}
$$

應同時保存。

這能避免：

> 數值找對了，但來源授權與版本搞錯了。

---

# 60. 氣象研究網站的特殊價值

氣象與氣候資料通常量大、更新頻繁、具 temporal / spatial structure。

Policy-aware runtime 可以：

- 優先 bulk dataset；
- 避免拿 query API 做不合理大規模 extraction；
- 遵守 request quotas；
- 記錄 station / dataset attribution；
- 分離 raw data 與 derived analysis。

因此 Rights Registry 會直接影響計算與資料架構。

---

# 61. 商業產品的特殊價值

若 Search Runtime 成為企業服務，它不能只回答：

> 我找到資料了。

企業更需要：

```text
where did it come from?
which surface?
what terms applied?
can we store it?
can we show it to customers?
can we redistribute raw?
must we attribute?
what changed since last month?
who approved the ambiguous case?
```

SRPR 使這些問題從人工記憶變成系統狀態。

---

# 62. SourcePolicySpec 最小 Schema

第一版可以從：

```text
SourcePolicySpec
├── policy_id
├── provider_id
├── surface_id
├── asset_scope
├── actions
│   ├── view
│   ├── automated_query
│   ├── crawl
│   ├── scrape
│   ├── bulk_download
│   ├── bulk_store
│   ├── cache
│   ├── index
│   ├── transform
│   ├── commercial_use
│   ├── redistribute_raw
│   ├── distribute_derived
│   └── train_model
├── duties
├── constraints
├── auth
├── rate_limits
├── policy_sources
├── provenance
└── review
```

開始。

---

# 63. Policy Decision API

可提供：

```text
evaluate_action(
    task,
    method,
    provider,
    surface,
    action,
    purpose,
    party,
    timestamp
) -> PolicyDecision
```

輸出：

```text
decision
obligations
limits
policy_evidence
confidence
review_required
```

---

# 64. Planner Integration

Paper 03 的 planner：

$$
\pi(T,S_t,\mathcal{M},\mathcal{P})
$$

現在變為：

$$
\pi
(
T,
S_t,
\mathcal{M},
\mathcal{P},
\mathcal{R}_{\text{policy}}
)
$$

候選 action：

$$
\mathcal{A}_t
$$

先經：

$$
\operatorname{AAG}
$$

得到：

$$
\mathcal{A}_t^{\text{allowed}}
$$

再做 optimization。

---

# 65. Executor Integration

Executor 收到的不應只是：

```text
GET URL
```

而應是：

```text
AuthorizedAction
├── action
├── credential_scope
├── request_limits
├── storage_policy
├── downstream_usage_envelope
├── attribution
└── policy_receipt
```

這樣 executor 才不會繞過 planner 的治理決策。

---

# 66. Storage Integration

資料寫入 storage 時：

```text
content
metadata
provenance
rights_envelope
retention
```

應一起 commit。

禁止：

```text
save content now
figure out rights later
```

因為資料一旦進入大型 corpus，就很容易失去來源與權利身份。

---

# 67. Export Integration

Export 前必須再次 evaluate：

$$
x_{\text{redistribute}}
$$

因為：

$$
\text{allowed to acquire}
\not\Rightarrow
\text{allowed to export}
$$

因此 acquisition gate 與 export gate 是同一 policy engine 的不同 action。

---

# 68. Fail-Closed 與 Fail-Open

對 `UNKNOWN` 可以有 task-specific policy。

## High Risk

$$
\mathsf{UNKNOWN}
\rightarrow
\mathsf{BLOCK/REVIEW}
$$

## Low Risk

某些純導航、公開連結行為可以：

$$
\mathsf{UNKNOWN}
\rightarrow
\text{restricted fallback}
$$

但不能默認：

$$
\mathsf{UNKNOWN}
\rightarrow
\mathsf{ALLOW\_ALL}
$$

---

# 69. 系統核心不變量

本文提出十二個 invariants。

## I1 — Technical Capability ≠ Permission

$$
C_{\text{tech}}
\neq
C_{\text{policy}}
$$

## I2 — Robots ≠ Authorization

$$
R_{\text{robots}}
\neq
R_{\text{auth}}
$$

## I3 — Access ≠ Reuse

$$
A_{\text{access}}
\neq
A_{\text{reuse}}
$$

## I4 — API Permission ≠ Underlying Data Rights

$$
R_{\text{API}}
\neq
R_{\text{data}}
$$

## I5 — Public ≠ Anonymous

$$
P_{\text{public}}
\neq
P_{\text{no-auth}}
$$

## I6 — Unknown ≠ Allow

$$
\mathsf{UNKNOWN}
\neq
\mathsf{ALLOW}
$$

## I7 — Permission May Carry Duties

$$
\mathsf{ALLOW}
+
O
$$

必須可表達。

## I8 — Policy Must Have Provenance

任何 policy decision 必須可追溯。

## I9 — Policy Is Time-Dependent

$$
P=P(t)
$$

## I10 — Rights Travel with Data

資料轉換後不得自動遺失 Usage Envelope。

## I11 — Acquisition ≠ Redistribution

$$
x_{\text{acquire}}
\neq
x_{\text{redistribute}}
$$

## I12 — Planning ≠ Authorization

$$
\operatorname{Propose}
\neq
\operatorname{Authorize}
$$

---

# 70. Failure Modes

## 70.1 Public-Equals-Free Fallacy

看到 public 即認為 unrestricted。

## 70.2 Robots Authorization Fallacy

把 robots allow 當法律許可。

## 70.3 API Laundering

認為透過 API 取得就自動擁有底層資料使用權。

## 70.4 License Flattening

把 provider、dataset、item 的不同 license 壓成一個欄位。

## 70.5 Rights Stripping

資料進入 local corpus 後失去 rights metadata。

## 70.6 Obligation Loss

attribution / disclaimer 在 downstream report 消失。

## 70.7 Terms Staleness

多年不重新檢查 provider terms。

## 70.8 Silent Policy Interpretation

LLM 自己解讀 ambiguous terms，卻標記成確定規則。

## 70.9 Credential Overreach

有 API key 就假設所有操作獲授權。

## 70.10 Rate-Limit Abuse

只靠 provider 封鎖才控制 request rate。

## 70.11 Redistribution Blindness

取得階段合法，但商業 export 階段違反限制。

## 70.12 Mixed-License Fusion Blindness

融合多來源後不再知道各 component 權利。

---

# 71. 與 W3C ODRL / DCAT 的關係

ODRL 已標準化：

- permissions；
- prohibitions；
- duties；
- constraints。

DCAT 已區分：

- license；
- accessRights；
- rights。

因此 SRPR 不應封閉地另造全部詞彙。

合理方向是：

$$
\text{SRPR}
=
\text{AUSI runtime semantics}
+
\text{existing rights vocabularies where applicable}
$$

也就是：

- 用既有標準表達能表達的部分；
- 用 AUSI profile 補充 search-specific actions；
- 例如 `automated_query`、`crawl`、`bulk_store`、`index`、`search_receipt`。

---

# 72. 與 Creative Commons / Open Data 的關係

Creative Commons 4.0 可適用於資料庫中的 copyright 與某些 database rights 情境；CC0 則用於最大化權利放棄與重用。

但：

$$
\text{CC License}
$$

只能回答 license scope 中的問題。

它不替代：

- API authentication；
- endpoint quotas；
- privacy；
- third-party rights；
- service availability；
- jurisdiction-specific mandatory law。

因此 Registry 可以存 canonical license URI，但仍保留其他 policy layers。

---

# 73. 研究命題

## P4.1 — Multi-Dimensional Rights Hypothesis

將資料權限拆成 action-specific dimensions，應比單一 `allowed` Boolean 更能避免錯誤 permission propagation。

## P4.2 — Policy-Before-Utility Hypothesis

在 Search Planner 中先做 hard policy filtering，再做 utility ranking，比把 legal/policy risk 當普通負分更能降低 prohibited action rate。

## P4.3 — Surface-Aware Governance Hypothesis

顯式區分 Web UI、API、bulk data 與其他 access surfaces，應能提高合法 provider substitution 的成功率。

## P4.4 — Obligation-Carrying Hypothesis

讓 attribution / disclaimer / retention 等 obligations 隨資料進入 downstream pipeline，可以降低輸出階段 obligation loss。

## P4.5 — Policy Provenance Hypothesis

保存 policy source、hash、observed time 與 interpretation status，可以提高 auditability 並降低 stale-policy decision。

## P4.6 — Unknown-State Hypothesis

將 unknown 與 deny / allow 分離，可以降低 silent over-permission，同時允許 planner 使用 alternative-source fallback。

## P4.7 — Rights-Aware Source Ranking Hypothesis

在 relevance / authority 類似時，優先 rights clarity 較高的來源，可降低整體 downstream compliance cost。

---

# 74. Benchmark 設計

可建立 Policy-Constrained Search Benchmark。

任務包含：

- public UI but automation prohibited；
- API allowed with attribution；
- API allowed but raw redistribution prohibited；
- open dataset behind authentication；
- provider with third-party series；
- stale terms；
- conflicting license metadata；
- unknown policy；
- provider quota exhaustion；
- same data available through legal alternative surface。

---

# 75. Baselines

## B0 — No Policy

只要能 HTTP fetch 就執行。

## B1 — Robots Only

只檢查 robots.txt。

## B2 — Flat Terms Flag

每 provider 一個 `allowed=true/false`。

## B3 — Source-Level License

保存 provider license，但不區分 surface/action。

## Proposed — SRPR + AAG

具備：

- action-specific rights；
- surface-aware rules；
- policy provenance；
- unknown/review states；
- obligations；
- hard gating；
- downstream Usage Envelope。

---

# 76. Metrics

$$
\text{Policy Violation Rate}
$$

$$
\text{False Denial Rate}
$$

$$
\text{Unknown Correctness}
$$

$$
\text{Alternative Provider Recovery Rate}
$$

$$
\text{Obligation Preservation Rate}
$$

$$
\text{Policy Staleness Rate}
$$

$$
\text{Rights Provenance Completeness}
$$

$$
\text{Export Compliance Rate}
$$

$$
\text{Manual Review Precision}
$$

$$
\text{Compliance Cost per Acquired Evidence}
$$

---

# 77. 工程落地

對 `ai-web-research`，可以新增：

```text
policy/
    models.py
    registry.py
    evaluator.py
    provenance.py
    drift.py
    obligations.py
    usage_envelope.py
    conflicts.py

providers/
    surfaces.py
    rights.py
    auth.py
    limits.py

planning/
    acquisition_gate.py

storage/
    rights_metadata.py
```

---

# 78. 第一批 Source Profiles

工程 MVP 不必一開始收錄全世界。

可以先建立少量高價值 source profiles：

```text
generic_web
generic_robots
WIPO_PATENTSCOPE_WEB
EPO_OPS
USPTO_ODP
DATA_GOV
FRED_API
NOAA_CDO_API
```

目的不是宣稱 profile 永遠正確。

而是測試：

- 不同 surface；
- 不同 auth；
- 不同 rate；
- 不同 reuse；
- 不同 downstream obligations。

---

# 79. Canonical Policy Workflow

```text
Search Need
↓
Candidate Method
↓
Candidate Provider
↓
Resolve Access Surface
↓
Load Policy Profile
↓
Refresh if stale
↓
Resolve Applicable Rules
↓
Evaluate Action
↓
ALLOW / CONDITIONAL / DENY / UNKNOWN / REVIEW
↓
Attach Obligations
↓
Execute
↓
Store Content + Provenance + Usage Envelope
↓
Re-evaluate on Export / Redistribution
```

---

# 80. 限制

第一，SRPR 不能保證任何具體使用在法律上必然合法。實際權利仍受司法管轄、契約、法定權利與個案事實影響。

第二，Terms of Use 是自然語言文件時，AI extraction 可能錯誤，因此高風險 profile 必須允許 human verification。

第三，robots.txt 的功能是 crawler coordination，不應被擴張解釋成法律授權或禁止的全部範圍。

第四，machine-readable license metadata 可能錯誤或與人類可讀條款衝突，因此 metadata 本身也需要 provenance。

第五，對多來源 derivative works 的 rights propagation 可能非常複雜；本文沒有提出一般性自動法律求解器。

第六，privacy、export controls、database rights、text-and-data-mining exceptions、trade secrets、personal data 與其他法域問題只被視為可插入的 governance modules，未在本文完整處理。

第七，provider policy 會變動，因此任何靜態 registry 都有 staleness risk。

第八，過度保守的 fail-closed policy 可能降低研究能力，因此需要 alternative provider discovery 與 human review，不能只會拒絕。

---

# 81. 結論

AI 原生搜尋若真的要成為科研、經濟、氣象、專利與企業 research infrastructure，就不能把「合法且可驗證的資料取得」留給最後人工補救。

本文的核心命題是：

$$
\boxed{
\text{Source Governance must be part of Search Planning}
}
$$

而不是 Search 完成後的 compliance patch。

因此：

$$
\boxed{
\text{Can Retrieve}
\not\Rightarrow
\text{May Retrieve}
}
$$

$$
\boxed{
\text{May Retrieve}
\not\Rightarrow
\text{May Store}
}
$$

$$
\boxed{
\text{May Store}
\not\Rightarrow
\text{May Redistribute}
}
$$

$$
\boxed{
\text{Public}
\not\Rightarrow
\text{Unrestricted}
}
$$

本文提出 Source Rights & Policy Registry，將 permission 拆成 action-specific decision：

$$
D(A,S,x,T,t)
\in
\{
\mathsf{ALLOW},
\mathsf{ALLOW\_WITH\_OBLIGATIONS},
\mathsf{DENY},
\mathsf{UNKNOWN},
\mathsf{REVIEW}
\}
$$

並將 Planner 的 action space限制為：

$$
\boxed{
\mathcal{A}^{\text{allowed}}_t
\subseteq
\mathcal{A}^{\text{technically-feasible}}_t
}
$$

最終資料取得流程不再只是：

$$
\text{URL}
\rightarrow
\text{Fetch}
\rightarrow
\text{Store}
$$

而是：

$$
\boxed{
\text{Need}
\rightarrow
\text{Method}
\rightarrow
\text{Provider}
\rightarrow
\text{Surface}
\rightarrow
\text{Policy Evaluation}
\rightarrow
\text{Authorized Acquisition}
\rightarrow
\text{Usage Envelope}
\rightarrow
\text{Evidence}
}
$$

Paper 01 定義 AI-Native Search。

Paper 02 定義 Search Method Space。

Paper 03 定義 Search Planner。

Paper 04 則為 Planner 畫出第一條真正不能被 utility 最佳化跨越的邊界：

> **搜尋智能必須知道，不是所有找得到的東西都應以同一方式取得，也不是所有取得到的資料都能以同一方式保存、使用與再散布。**

下一篇將處理另一條同樣重要的邊界：

> **Paper 05 — 從搜尋結果到證據：Provenance、Verification、Evidence Ledger 與可驗證研究資料生命週期**

也就是：

$$
\text{Retrieved}
\not\Rightarrow
\text{Verified}
$$

---

# References

[1] Koster, M., Illyes, G., Zeller, H., & Sassman, L. (2022). *RFC 9309 — Robots Exclusion Protocol*. Internet Engineering Task Force / RFC Editor. https://www.rfc-editor.org/rfc/rfc9309.html

[2] World Intellectual Property Organization. *WIPO Terms and Conditions for the Use of Published International Patent Applications Data*. PATENTSCOPE. Accessed 2026-08-30. https://www.wipo.int/en/web/patentscope/data/terms_patentscope

[3] European Patent Office. *Terms and Conditions for Use of the EPO's Open Patent Services (OPS)*. Accessed 2026-08-30. https://www.epo.org/en/service-support/ordering/terms-and-conditions/ops-terms-and-conditions

[4] European Patent Office. *Open Patent Services (OPS)*. Accessed 2026-08-30. https://www.epo.org/en/searching-for-patents/data/web-services/ops

[5] European Patent Office. *Does OPS Permit Bulk Data Retrieval?* Accessed 2026-08-30. https://www.epo.org/en/service-support/faq/searching-patents/open-patent-services/general-information/does-ops-permit-bulk

[6] United States Patent and Trademark Office. (2026). *USPTO Open Data Portal to Require Registration for Access Beginning June 18, 2026*. Published 2026-05-01. https://www.uspto.gov/subscription-center/2026/uspto-open-data-portal-require-registration-access-beginning-june-18-2026

[7] Data.gov. *Privacy and Website Policies — Data Policy / Licensing*. Accessed 2026-08-30. https://data.gov/privacy-policy/

[8] Resources.data.gov. *Open Licenses*. Accessed 2026-08-30. https://resources.data.gov/open-licenses/

[9] W3C. (2018). *ODRL Information Model 2.2*. W3C Recommendation. https://www.w3.org/TR/odrl-model/

[10] W3C. (2024). *Data Catalog Vocabulary (DCAT) — Version 3*. W3C Recommendation. https://www.w3.org/TR/vocab-dcat-3/

[11] Creative Commons. *Frequently Asked Questions — Data and CC Licenses*. Accessed 2026-08-30. https://creativecommons.org/faq/

[12] Federal Reserve Bank of St. Louis. *FRED API Terms of Use*. Accessed 2026-08-30. https://fred.stlouisfed.org/docs/api/terms_of_use.html

[13] Federal Reserve Bank of St. Louis. *Full FRED Services Terms of Use*. Accessed 2026-08-30. https://fred.stlouisfed.org/legal/terms/

[14] NOAA National Centers for Environmental Information. *Climate Data Online: Web Services API v2 — Getting Started*. Accessed 2026-08-30. https://www.ncei.noaa.gov/cdo-web/webservices/getstarted

[15] Data.gov / DCAT-US. *Distribution — License, Rights, and Use Restrictions*. Accessed 2026-08-30. https://resources.data.gov/standards/catalog/dcat-us-3/distribution/

---

# Series Continuation

**Paper 05 — 從搜尋結果到證據：Provenance、Verification、Evidence Ledger 與可驗證研究資料生命週期**

下一篇將正式區分：

$$
\text{Search Result}
\rightarrow
\text{Candidate Evidence}
\rightarrow
\text{Verified Evidence}
$$

並建立：

- Evidence Object；
- Source Identity；
- Quote / Span Anchoring；
- Content Hash；
- Retrieval Time；
- Event / Publication / Revision Time；
- Version Lineage；
- Source Independence；
- Corroboration；
- Contradiction；
- Verification State；
- Evidence Ledger；
- Claim–Evidence Graph；
- downstream citation / reproducibility contract。

也就是讓 AUSI 從「知道能不能取得資料」，繼續前進到「知道取得的資料究竟能不能支持某個命題」。
