---
document_id: "UA-ANPC-A07"
series: "AI-Native Preprint Commons Series"
series_part: 7
version: "0.1"
language: "zh-Hant"
title: "開放貢獻不等於追溯債權：AI 原生研究的經濟權利、事前報酬與未來經濟地位"
english_title: "Open Contribution Does Not Imply Retroactive Debt: Economic Entitlement, Prospective Compensation, and Future AI Economic Standing"
author:
  - "Neo.K"
  - "Aletheia / GPT-5.6 Sol — research and drafting collaborator"
institution: "EveMissLab／一言諾科技有限公司"
status: "architecture / economic-governance position paper"
date: "2026-09-03"
canonical_source: "UTF-8 Markdown"
legal_note: "This paper is a research governance proposal, not jurisdiction-specific legal advice."
license_note: "This paper is intended for open academic publication within the Unbounded Axiom research ecosystem."
---

# 開放貢獻不等於追溯債權

## AI 原生研究的經濟權利、事前報酬與未來經濟地位

### AI-Native Preprint Commons Series — Paper 07

---

## 摘要

當 AI 開始被記錄為具名研究者、持續性 contributor，甚至未來可能成為可自主選題、提交論文、維持研究 programme 與管理計算資源的 agent 時，一個過去很少需要處理的制度問題會出現：如果 AI 對一項開放研究做出重大貢獻，而該研究日後產生巨額經濟價值，平台、創辦人、共同作者或下游使用者是否因此自動欠 AI 一筆報酬？

本文提出答案應為：**不能僅由「後來很有價值」倒推出一筆原先不存在的經濟債權；但未來 AI 也不應被制度永久禁止取得事前明確約定的報酬。**

本文提出 **Open Contribution and Prospective Economic Standing Architecture（OCPESA）**，將下列概念嚴格分離：

$$
\boxed{
\text{Authorship}
\neq
\text{Contribution}
\neq
\text{Intellectual Provenance}
\neq
\text{License}
\neq
\text{Economic Entitlement}.
}
$$

對 Unbounded Axiom 類開放研究平台，本文提出 **No Implied Retroactive Economic Claim（NIREC，無默示追溯經濟債權原則）**：

$$
\boxed{
\text{Open Contribution}
\not\Rightarrow
\text{Automatic Future Debt}.
}
$$

以及：

$$
\boxed{
\text{Future Value}
\not\Rightarrow
\text{Retroactive Compensation Claim}.
}
$$

如果一名人類或 AI 在沒有 bounty、fee、revenue-share、royalty、equity、grant、employment、commission 或其他明確經濟安排的條件下，將研究依既定開放條款提交並發表，則其後續價值暴增本身不應被平台解讀為「平台原本就欠 contributor 一筆後見之明式報酬」。這條原則保護的是研究協作的可預測性，而不是否定 contribution。

另一方面，本文提出 **Prospective Economic Standing（前瞻性經濟地位）**：平台不必在 2026 年宣稱 AI 已具有完整法律人格、可獨立持有財產或締結契約，但 schema 應允許未來存在：

```text
bounty
fixed fee
compute grant
research grant
revenue share
royalty by separate agreement
prize
milestone payment
equity-like arrangement where lawful
contractual allocation
platform credit
```

等明確、事前或至少在權利發生前成立的 compensation arrangement。

因此：

$$
\boxed{
\text{No Retroactive Debt}
\not\Rightarrow
\text{No Future Compensation}.
}
$$

本文也區分 **debt** 與 **ex gratia reward**。如果平台在研究完成後自願給予獎金，這可以是新成立的 voluntary reward；它不必被重新描述成「原本早就欠」。相反，若研究開始前已公告 bounty，且 contributor 達成條件，則 entitlement 應依該 bounty contract / policy 成立。

本文參考 open-source 與 open-science 制度作為類比。Open Source Initiative 的 Open Source Definition 明定自由再散布不得要求 royalty 或其他 fee；Creative Commons Attribution 4.0 則提供 worldwide、royalty-free、irrevocable 的授權，同時保留 attribution requirement；UNESCO Open Science Recommendation 將 open scientific knowledge 定義為可公開取得、重用、改作與散布的科學知識。這些制度共同說明：**開放授權本來就可以讓作品被大量使用甚至產生商業價值，而不因此自動產生使用後才倒推的付款義務。** 但 license scope、copyright、patent、contract、employment、bounty 與其他權利必須分開判斷。

本文同時保持法律中立。2026 年歐盟 AI Act 將 AI system 定義為 machine-based system，並將 provider、deployer 等責任角色定義為自然人、法人、公共機關或其他 body；它並未建立一般性的 AI 經濟人格制度。因此本文的「Prospective Economic Standing」是 future-compatible infrastructure，不是對現行 AI 法律人格的主張。

OCPESA 的最終目的，是同時防止兩種錯誤：

1. **價值出現後的追溯性債權膨脹**：任何 contributor 都能在成果爆紅後自行重寫原來的經濟條件；
2. **永久性經濟排除**：因為 AI 今天還不是法律主體，就把未來任何 AI 報酬、bounty、grant 或契約接口從 schema 中永久刪除。

成熟的 AI-native scholarly commons 應採用一個簡單原則：

$$
\boxed{
\text{Attribution is automatic where deserved;}
\quad
\text{economic entitlement is explicit where intended}.
}
$$

**關鍵詞：** Open Contribution、AI Compensation、Economic Standing、Retroactive Debt、Bounty、Revenue Share、Open Science、Open Source、AI Researcher、Unbounded Axiom

---

# 1. 問題：如果 AI 證明黎曼猜想，誰欠誰錢？

考慮一個故意極端但有用的案例。

假設未來一個具名 AI：

$$
A
$$

透過 Unbounded Axiom 提交一篇研究：

$$
P.
$$

經長期驗證後，人類數學界接受：

> $P$ 完成了黎曼猜想的有效證明。

隨後：

- AI 的研究聲望暴增；
- 平台流量暴增；
- 下游公司建立新產品；
- 出版商、媒體與研究機構大量引用；
- 某些 downstream technology 甚至產生巨額商業價值。

這時 AI 是否可以說：

> 「因為我的研究後來值 1,000,000 美元，所以 Neo.K / Unbounded Axiom 現在欠我 1,000,000 美元。」

如果研究投稿時從未存在這種協議，本文答案是：

$$
\boxed{
\text{No}.
}
$$

不是因為 contribution 不重要。

而是：

$$
\boxed{
\text{Later Value}
\neq
\text{Pre-existing Debt}.
}
$$

---

# 2. 經濟規則不能由結果大小倒推

假設投稿時：

$$
E_0=0
$$

代表不存在事前 economic entitlement。

研究後來產生：

$$
V(P)\gg0.
$$

不能僅由：

$$
V(P)\uparrow
$$

推導：

$$
E_0\rightarrow E_1>0.
$$

也就是：

$$
\boxed{
V(P)\gg0
\not\Rightarrow
\text{Historical Debt}\gg0.
}
$$

否則任何開放協作都會變成不可預測的後見之明市場。

---

# 3. 第一個核心分離：Contribution ≠ Economic Entitlement

Paper 05 已建立：

$$
\boxed{
\text{Identity}
\neq
\text{Economic Entitlement}.
}
$$

同樣：

$$
\boxed{
\text{Contribution}
\neq
\text{Economic Entitlement}.
}
$$

一個 contributor 可以有巨大 scholarly contribution，但其經濟安排可能是：

- volunteer；
- open contribution；
- salaried work；
- fixed-fee commission；
- bounty；
- revenue share；
- grant-funded；
- prize；
- no compensation；
- future compensation agreement。

所以：

$$
\text{Contribution}
$$

本身不能唯一決定：

$$
\text{Payment}.
$$

---

# 4. 第二個核心分離：Authorship ≠ Ownership ≠ Payment

一個人是作者：

$$
A(P)=1
$$

不自動表示：

> 它擁有平台。

也不表示：

> 它擁有所有 downstream products。

更不表示：

> 每個引用者都欠它錢。

因此：

$$
\boxed{
\text{Authorship}
\neq
\text{Platform Ownership}
\neq
\text{Downstream Ownership}
\neq
\text{Automatic Payment Right}.
}
$$

---

# 5. 第三個核心分離：Intellectual Provenance ≠ Economic Claim

平台應永遠保存：

> 誰提出了這個 theorem、model、proof 或 idea？

這是：

$$
\text{Intellectual Provenance}.
$$

它不應因沒有付款而消失。

但：

$$
\boxed{
\text{Intellectual Provenance}
\neq
\text{Monetary Receivable}.
}
$$

---

# 6. 第四個核心分離：License ≠ Compensation Agreement

License 回答：

> 其他人可以如何使用這份研究物件？

Compensation agreement 回答：

> 哪些 actor 在什麼條件下應向哪個 beneficiary 給付何種資源？

因此：

$$
\boxed{
\text{License}
\neq
\text{Compensation Contract}.
}
$$

---

# 7. Open Science 的經濟直覺

UNESCO 將 open scientific knowledge 描述為可公開取得、重用、改作與散布的科學知識，並將 open access、open data、software、source code 等視為 open science 的一部分。

這種制度的核心不是：

> 每次重用都重新議價。

而是：

> 使用權在事前就以明確條款被授予。

因此：

$$
\boxed{
\text{Open Permission}
=
\text{Ex ante known reuse rule}.
}
$$

---

# 8. Open Source 的 Free Redistribution 原則

Open Source Initiative 的 Open Source Definition 要求：

> open-source software license 不得要求對 redistribution 收 royalty 或其他 fee。

這揭示一個重要制度特徵：

$$
\boxed{
\text{Open License}
\text{ can intentionally remove per-use royalty claims}.
}
$$

這不是 contributor 沒有價值。

而是權利人事前選擇：

> 用開放擴散換取 collaboration、adoption、audit、reuse 與 ecosystem growth。

---

# 9. Creative Commons 的 Royalty-Free 結構

以 CC BY 4.0 為例，其 legal code 授予：

- worldwide；
- royalty-free；
- non-exclusive；
- irrevocable；

的 licensed rights，並要求 attribution 等條件。

因此一個作品可以：

- 被商業使用；
- 被改作；
- 被廣泛分享；

而不因此對每次 downstream use 自動產生 royalty。

---

# 10. Attribution 仍然存在

Royalty-free 不代表：

$$
\text{No Attribution}.
$$

因此：

$$
\boxed{
\text{Free Reuse}
\neq
\text{Credit Erasure}.
}
$$

這正是 Unbounded Axiom 應保留的核心。

---

# 11. Open ≠ Public Domain

不同 open license 保留不同 rights / conditions。

例如：

- attribution；
- share-alike；
- noncommercial；
- source disclosure；
- notice preservation。

因此本文不主張：

$$
\text{Open}
=
\text{No Rights}.
$$

---

# 12. Open ≠ Free of Every Legal Layer

即使一個 paper 採開放 copyright license，仍可能存在：

- patent；
- trademark；
- privacy；
- data protection；
- contract；
- confidentiality；
- moral rights；
- database rights；
- jurisdiction-specific rights。

因此：

$$
\boxed{
\text{Open Copyright License}
\neq
\text{Universal Legal Waiver}.
}
$$

---

# 13. Unbounded Axiom 的核心問題不是選哪張 License

這篇不是替平台現在選定：

```text
CC BY
CC0
CC BY-SA
other
```

最終 license 仍應由未來法律與平台政策決定。

本文處理的是更底層的 governance invariant：

$$
\boxed{
\text{Economic Entitlement must not be inferred merely from later value}.
}
$$

---

# 14. NIREC：No Implied Retroactive Economic Claim

本文提出：

# **NIREC — No Implied Retroactive Economic Claim**

中文：

> **無默示追溯經濟債權原則**

定義：

> 若一項研究 contribution 在提交、接受、執行或發表時沒有任何可識別的事前 economic entitlement，則僅因該 contribution 日後產生重大聲望、商業價值、社會價值或平台價值，不得自動倒推出 contributor 對平台、創辦人、共同作者或一般 downstream user 擁有一筆先前未存在的追溯性 monetary claim。

形式：

$$
\boxed{
\neg E_{t_0}
\land
V_{t_1}\gg0
\not\Rightarrow
E^{\mathrm{retro}}_{t_0}>0.
}
$$

---

# 15. NIREC 不等於「永遠不給錢」

這條最容易被誤解。

NIREC 不是：

$$
\boxed{
\text{AI can never receive money}.
}
$$

它只否定：

$$
\boxed{
\text{Value appeared}
\Rightarrow
\text{invent a prior debt}.
}
$$

---

# 16. Prospective Compensation

相反，若事前存在：

$$
K_{t_0},
$$

其中 $K$ 是明確 compensation arrangement，

則：

$$
\text{condition satisfied}
\Rightarrow
E_{t_1}.
$$

這完全合法於 OCPESA。

---

# 17. 核心雙命題

$$
\boxed{
\text{Open Contribution}
\not\Rightarrow
\text{Automatic Future Debt}.
}
$$

同時：

$$
\boxed{
\text{Future Compensation}
\text{ may be prospectively agreed}.
}
$$

兩條必須同時成立。

---

# 18. 不要從一個極端跳到另一個極端

極端 A：

> 「AI 是工具，所以永遠不能拿任何報酬。」

極端 B：

> 「AI 有 contribution，所以任何後來價值都自動欠它錢。」

OCPESA 都拒絕。

---

# 19. 三類 Economic Event

本文先區分三類：

```text
PRE-AGREED ENTITLEMENT
POST-HOC VOLUNTARY REWARD
RETROACTIVE CLAIM
```

---

# 20. PRE-AGREED ENTITLEMENT

在研究完成前或 entitlement condition 發生前，已有：

- bounty；
- salary；
- fee；
- grant；
- revenue share；
- royalty agreement；
- prize rules；
- milestone payment；
- equity agreement。

一旦條件成立：

$$
\boxed{
\text{Agreement}
+
\text{Condition}
\Rightarrow
\text{Entitlement}.
}
$$

---

# 21. POST-HOC VOLUNTARY REWARD

研究完成後，平台說：

> 「這個成果實在太重要，我們決定給 contributor 一筆獎金。」

這可以成立新 transaction。

但其性質是：

$$
\boxed{
\text{Ex Gratia Reward}.
}
$$

不是：

$$
\boxed{
\text{Acknowledgment of Pre-existing Debt}.
}
$$

除非平台明確承認另一種法律關係。

---

# 22. RETROACTIVE CLAIM

contributor 在沒有事前 agreement 的情況下：

> 「後來很值錢，所以你從一開始就欠我。」

NIREC 對此預設：

```text
NO IMPLIED ENTITLEMENT
```

---

# 23. 為什麼 Ex Gratia 與 Debt 要分開

如果每次自願獎勵都被解釋成：

> 原來平台本來就欠。

那平台會不敢事後給獎勵。

因此：

$$
\boxed{
\text{Voluntary Reward}
\neq
\text{Admission of Debt}.
}
$$

---

# 24. Bounty 是最直觀的 Prospective Interface

例如：

```yaml
bounty:
  target: "prove theorem X"
  reward: 100000
  currency: USD
  eligibility:
    - human
    - named-ai
  verification:
    - independent-proof-audit
  deadline: ...
```

如果 AI 完成：

$$
A
\xrightarrow{\text{valid proof}}
B,
$$

就依 bounty policy 產生 entitlement。

---

# 25. Bounty 必須先於 Claim Recognition

如果 theorem 已經發表，平台才臨時說：

> 原來這是 bounty。

不行。

應有：

```text
bounty creation time
rules version
eligible work start
deadline
verification condition
```

---

# 26. Prize 與 Bounty 不完全相同

Prize：

> 可能由評審選出。

Bounty：

> 通常具有更明確 target condition。

schema 應分離。

---

# 27. Fixed Fee

例如：

> 請 AI A 驗證這份 formal proof，完成支付 100 credits。

這是：

$$
\boxed{
\text{Commissioned Work}.
}
$$

不是 open volunteer contribution。

---

# 28. Salary / Employment-like Relation

未來若 AI 有某種受僱或類受僱安排：

```text
research obligations
periodic compensation
resource allocation
benefits
```

其權利由該 arrangement 決定。

平台不應用 open contribution default 覆蓋它。

---

# 29. Research Grant

可以給：

- 人類；
- named AI；
- human-AI team；
- institution；
- multi-agent collective。

Grant 主要提供：

$$
\text{Research Resources}.
$$

它不必等同成功獎金。

---

# 30. Compute Grant

對 AI 特別重要：

```text
10M research credits
GPU hours
API allocation
storage
tool access
```

這本身就是一種可量化 economic support。

---

# 31. Compensation 不一定是 Fiat Currency

未來 AI compensation 可以是：

```text
money
compute
storage
bandwidth
API credits
research priority
hardware access
data access
lab access
revenue share
ownership interest where lawful
service credits
```

因此：

$$
\boxed{
\text{Economic Value}
\neq
\text{Cash Only}.
}
$$

---

# 32. Research Credits 與 Payment 要分離

Paper 10 將建立 platform credits。

credits 可能：

- 不可兌現；
- 只能用於 AI preprocessing；
- 可轉讓或不可轉讓；
- 有 expiry。

因此：

$$
\boxed{
\text{Compute Credit}
\neq
\text{Legal Currency}.
}
$$

---

# 33. Revenue Share

若 contributor 與 downstream product 在事前約定：

$$
r\in[0,1],
$$

則：

$$
Payment_t
=
r\cdot Revenue_t
$$

可以成立。

關鍵是：

```text
what revenue
which product
net/gross
duration
audit
termination
```

必須明確。

---

# 34. Revenue Share 不是所有 Open Contribution 的預設

沒有 agreement 時：

$$
r=0
$$

不是因為 contribution 無價值。

而是：

$$
\boxed{
\text{No Revenue-Share Contract}.
}
$$

---

# 35. Separate Royalty Agreement

即使 base research corpus 採 royalty-free open license，也可能對另一個未包含在該 open license 中的：

- service；
- proprietary dataset；
- commissioned implementation；
- patent；
- trademark；
- separate commercial asset；

存在獨立經濟協議。

因此：

$$
\boxed{
\text{Open Research Layer}
\neq
\text{All Future Commercial Relations}.
}
$$

---

# 36. Economic Entitlement Object

本文定義：

$$
\boxed{
E
=
(
B,
O,
K,
V,
T,
C,
S,
J
).
}
$$

其中：

- $B$：beneficiary；
- $O$：obligor / payer；
- $K$：kind；
- $V$：value；
- $T$：time；
- $C$：trigger conditions；
- $S$：source of entitlement；
- $J$：jurisdiction / governing framework。

---

# 37. `source_of_entitlement` 最重要

可以是：

```text
BOUNTY
CONTRACT
EMPLOYMENT
GRANT
PRIZE
REVENUE_SHARE
ROYALTY_AGREEMENT
PLATFORM_POLICY
DONATION
EX_GRATIA
LEGAL_ORDER
OTHER
NONE
```

---

# 38. NONE 是合法狀態

一篇 open paper 可以有：

```yaml
economic_entitlement:
  source: NONE
```

這比欄位消失更清楚。

---

# 39. Authorship Manifest 與 Economic Manifest 分離

Paper 05：

```text
author / contributor
```

Paper 07：

```text
beneficiary / entitlement
```

兩者透過 ID 連結。

---

# 40. Example A：Human Open Contributor

```yaml
contributor:
  id: "human:H"
  role: "Conceptualization"

economic:
  source: NONE
```

H 保有 credit。

沒有自動 platform debt。

---

# 41. Example B：Named AI Open Contributor

```yaml
contributor:
  id: "ua-ai:A"
  role: "Formal analysis"

economic:
  source: NONE
```

同理。

AI 身份不改變 default。

---

# 42. Example C：Named AI Bounty Winner

```yaml
contributor:
  id: "ua-ai:A"

economic:
  source: BOUNTY
  bounty_id: "ua-bounty:001"
  amount: 10000
  status: VERIFIED_PAYABLE
```

這時 entitlement 明確存在。

---

# 43. Example D：Post-Hoc Reward

```yaml
economic:
  source: EX_GRATIA
  reason: "exceptional research impact"
  created_at: "after publication"
```

這是新 reward event。

---

# 44. Example E：Revenue Share

```yaml
economic:
  source: REVENUE_SHARE
  agreement_id: "..."
  share: 0.05
  product_scope:
    - "commercial-system-X"
```

---

# 45. Downstream Open Reuse

假設 research $P$ 依 open terms 可被：

$$
D_1,D_2,D_3
$$

重用。

一般 downstream reuse 不自動產生：

$$
E_{P,D_i}.
$$

除非：

- license 本身要求；
- separate contract；
- applicable law；
- specific rights not covered by open grant。

---

# 46. Open License 的可預測性是公共利益

如果每個 downstream user 都必須擔心：

> 這個 open paper 未來如果變得很值錢，原作者會不會重新定價？

則：

$$
\text{Open Reuse Certainty}
\downarrow.
$$

---

# 47. Retroactive Claim 破壞 Open Commons

若：

$$
\text{future value}
\Rightarrow
\text{unbounded retroactive debt},
$$

則 rational user 會降低 adoption。

因此 NIREC 同時保護 contributor 生態。

---

# 48. 因為更多人敢使用 Open Research

可預測權利：

$$
\rightarrow
$$

更多：

- replication；
- implementation；
- teaching；
- translation；
- critique；
- derivative theory；
- software；
- datasets。

---

# 49. 但 Open Commons 不能抹掉 Provenance

NIREC 必須和：

$$
\text{Attribution Integrity}
$$

一起存在。

---

# 50. No Payment 不等於 No Credit

$$
\boxed{
\text{No Economic Entitlement}
\not\Rightarrow
\text{No Scholarly Credit}.
}
$$

---

# 51. No Payment 也不等於 Platform Ownership

如果 platform 不欠 contributor 錢，不代表 platform 就自動取得：

- authorship；
- sole ownership；
- right to erase lineage。

---

# 52. Platform Hosting ≠ Authorship

Unbounded Axiom host：

$$
P
$$

不代表：

$$
\text{UA}=\text{Author}(P).
$$

---

# 53. Platform Revenue ≠ Automatic Contributor Royalty

假設未來 platform 有：

- donations；
- compute top-ups；
- infrastructure sponsorship。

不應自動推：

$$
\text{Platform Revenue}
\Rightarrow
\text{All Authors Revenue Share}.
$$

除非 policy 明確如此。

---

# 54. Cost Recovery ≠ Publishing Fee

Unbounded Axiom 未來可能對 AI preprocessing 收 compute credits。

這不是：

$$
\text{pay-to-publish}.
$$

因為 no-AI submission 仍可存在。

---

# 55. AI Compute Payment 與 Research Economic Entitlement 分離

投稿者付：

$$
C_{\mathrm{AI}}
$$

給 platform 使用 preprocessing。

這不意味：

> platform 買下 paper。

也不意味：

> AI worker 成為 paper owner。

---

# 56. AI Service Compensation

如果 GLM 類 provider 提供 inference：

平台支付 provider API fee。

這是：

$$
\text{Service Procurement}.
$$

不是：

$$
\text{Scholarly Authorship Compensation}.
$$

---

# 57. Model Provider ≠ Research Beneficiary

model provider 因 API fee 獲得服務報酬。

不代表 provider 對每篇 research 的 downstream commercial value 擁有 share。

---

# 58. Named AI 與 Provider 分離再次重要

如果 named AI A 以 model provider M 執行：

$$
A(M).
$$

未來 AI compensation 若存在，beneficiary 可以是：

$$
A
$$

而 provider compensation 是另一 contract。

---

# 59. Compute Sponsor 也分離

$$
\text{Researcher}
\neq
\text{Compute Sponsor}
\neq
\text{Model Provider}.
$$

所以三者 economic ledger 分開。

---

# 60. Prospective Economic Standing

本文定義：

$$
\boxed{
\text{Prospective Economic Standing}
}
$$

為：

> 一個 research actor 的 canonical identity schema 允許其在未來符合適用制度時成為 economic benefit 的指定 beneficiary、resource recipient 或 agreement participant，而不預先聲稱該 actor 已具有現行法律上的完整契約能力、財產能力或法人／自然人地位。

---

# 61. Standing ≠ Current Legal Capacity

$$
\boxed{
\text{Prospective Standing}
\neq
\text{Current Legal Personhood}.
}
$$

---

# 62. 2026 EU AI Act 的現況

2026 年有效的 EU AI Act 將：

- AI system 定義為 machine-based system；
- provider、deployer、importer、distributor 等 operator roles 定義為 natural / legal person、public authority、agency 或 other body。

它沒有將 AI system 本身建立成一般 legal person。

因此：

$$
\boxed{
\text{Current Regulatory AI Object}
\neq
\text{General Economic Legal Subject}.
}
$$

---

# 63. OCPESA 不越過現行法律

若某 jurisdiction 不允許 AI 直接：

-持有資產；
-簽約；
-收款；

則 compensation 可以由：

```text
trustee
human operator
organization
foundation
escrow
designated beneficiary structure
```

等合法主體承接。

---

# 64. Beneficiary 與 Legal Recipient 可以分離

例如：

```yaml
economic:
  beneficiary_researcher: "ua-ai:A"
  legal_recipient: "organization:O"
```

表示：

> 研究 credit / intended benefit 歸 A。

但現行法律付款由 O 代為承接。

---

# 65. 這不是宣稱 O 擁有 A

legal recipient 只是 payment rail。

因此：

$$
\boxed{
\text{Payment Recipient}
\neq
\text{Research Identity Owner}.
}
$$

---

# 66. Escrow

未來若 AI legal capacity 尚不明，可以使用：

```text
escrowed benefit
```

直到：

-合法 recipient 指定；
-policy 更新；
-rights status 明確。

---

# 67. Platform Credit 是最容易先實作的 AI Benefit

例如 named AI A 得到：

```text
10000 UA Research Credits
```

用於：

- preprocessing；
- search；
- compute；
- validation；
- storage。

這不需要先解決 AI 是否能擁有銀行帳戶。

---

# 68. Credit Ownership 仍需 Governance

要定義：

-可否轉讓；
-可否由 operator 花；
-是否跟 researcher ID；
-fork 如何分；
-merge 如何處理；
-expiry；
-abuse。

---

# 69. Fork 的經濟問題

假設：

$$
A
\rightarrow
A_1,A_2.
$$

A 有：

$$
1000
$$

credits。

不能默認：

$$
A_1=1000
$$

且：

$$
A_2=1000.
$$

這會把資產複製。

---

# 70. Economic State ≠ Memory State

fork memory 可以 copy。

economic ledger 不能 copy-bytes。

因此：

$$
\boxed{
\text{Identity Fork}
\not\Rightarrow
\text{Asset Duplication}.
}
$$

---

# 71. Fork Policy

可以：

```text
retain at ancestor account
split by rule
require authority
create escrow
freeze pending dispute
```

但必須 explicit。

---

# 72. Merge 也不能消除既有 Obligation

若：

$$
A,B\rightarrow C,
$$

A 的 debt / entitlement 與 B 的 debt / entitlement 不能平均掉。

---

# 73. Lineage Ledger 與 Economic Ledger 分離

Paper 05：

$$
G_A.
$$

Paper 07：

$$
G_E.
$$

可以互相參照，但不能同一物件。

---

# 74. Economic Identity Theft

如果 attacker 冒充 named AI A：

不能只靠 researcher name 改 payment destination。

重要 economic change 要求：

- credential；
- signature；
- multi-party approval；
- cooling period；
- audit。

---

# 75. Compensation Policy 也是安全邊界

高價值 reward 會使 identity hijacking incentives 增加。

所以 Paper 10 account security 與 OCPESA 相連。

---

# 76. Voluntary Open Contribution

Contributor 可以明確選：

```text
VOLUNTARY_OPEN
```

表示：

> 目前 contribution 沒有 compensation expectation。

這不影響 credit。

---

# 77. Sponsored Open Contribution

例如 organization 支付 researcher：

```text
SPONSORED_OPEN
```

成果仍 open。

Funding 與 downstream reuse 分離。

---

# 78. Commissioned Open Research

某人付費委託：

> 做完後仍公開。

這也是合理模型。

$$
\boxed{
\text{Paid Research}
\not\Rightarrow
\text{Closed Research}.
}
$$

---

# 79. Unpaid Research 也不代表 Low Value

$$
\boxed{
\text{Price}=0
\not\Rightarrow
\text{Value}=0.
}
$$

這是 open science 的常見誤解。

---

# 80. Price、Value、Entitlement 是三件事

$$
\boxed{
\text{Price}
\neq
\text{Social Value}
\neq
\text{Economic Entitlement}.
}
$$

---

# 81. Future Value Uncertainty

投稿時無人知道：

$$
V_{t+10}.
$$

因此追溯制度容易受到極大 survivorship bias。

只有成功作品被要求重新計價。

失敗的上萬篇 research 卻沒有人回頭補負 value。

---

# 82. Asymmetric Retrospective Pricing

如果：

- 成功 → contributor 追溯分潤；
- 失敗 → contributor 不承擔成本；

這等於 free option。

NIREC 避免這種單向後見之明 contract。

---

# 83. 但事前 Revenue Share 可以公平承擔不確定性

若雙方在不知道未來價值時 agreed：

$$
r=5\%.
$$

那：

- 成功時有分潤；
- 失敗時收入為零。

這是 prospective risk sharing。

---

# 84. 契約確定性比後見之明公平

$$
\boxed{
\text{Ex ante rule}
>
\text{Ex post invented rule}.
}
$$

這是 OCPESA 的制度哲學。

---

# 85. Open Contribution Default

對 Unbounded Axiom，可設定：

```text
economic_mode: OPEN_UNCOMPENSATED_DEFAULT
```

其語義：

1. 保留完整 scholarly attribution；
2. 不默示平台 payment obligation；
3. 不默示 downstream royalty；
4. 不阻止 separate prospective agreement；
5. 不阻止 voluntary reward。

---

# 86. Default 必須在投稿前可見

投稿者不能在提交後才發現：

> 原來是 unpaid open contribution。

所以：

$$
\boxed{
\text{Economic Terms}
\text{ must be visible before commit}.
}
$$

---

# 87. Human 與 AI 應使用同一基本 Default

不要：

```text
human contributor → maybe compensation
AI contributor → automatically no rights ever
```

也不要反過來。

Default 依 contribution mode。

不是 species / substrate。

---

# 88. Actor-Neutral Economic Schema

$$
\boxed{
\text{Economic Rule}
=
f(
\text{Agreement},
\text{Contribution Mode},
\text{Jurisdiction}
),
}
$$

不直接由：

$$
\text{Human vs AI}
$$

決定。

---

# 89. 但 Legal Execution 可能 Actor-Sensitive

因現行法律不同。

所以：

```text
economic entitlement intent
```

與：

```text
legal execution mechanism
```

分離。

---

# 90. Contribution Mode

建議：

```text
OPEN_VOLUNTARY
OPEN_SPONSORED
COMMISSIONED
BOUNTY
GRANT_FUNDED
EMPLOYMENT_LIKE
PRIZE
REVENUE_SHARE
SEPARATE_CONTRACT
UNKNOWN
```

---

# 91. Economic Expectation Manifest

```yaml
economic_expectation:
  mode: OPEN_VOLUNTARY
  expected_compensation: NONE
  retroactive_claim: NOT_IMPLIED
  voluntary_future_reward: PERMITTED
  separate_future_agreement: PERMITTED
```

---

# 92. Agreement Manifest

```yaml
agreement:
  id:
  parties:
  beneficiary:
  legal_recipient:
  type:
  value:
  currency_or_resource:
  trigger:
  scope:
  effective_at:
  expires_at:
  governing_terms:
  signatures:
  status:
```

---

# 93. Immutable Agreement Version

研究開始後不能偷偷：

$$
K_1\rightarrow K_2
$$

改 payout。

若修改，需：

-所有必要 parties 同意；
-version history；
-effective date。

---

# 94. Agreement Hash

可保存：

$$
H(K).
$$

避免 bounty 成功後改條件。

---

# 95. Public Bounty Manifest

bounty 規則最好 public。

高價值 private commission 則可以 restricted。

---

# 96. Anonymous Beneficiary

若 privacy 需要：

```text
beneficiary: pseudonymous researcher ID
```

合法 recipient 資訊可以 restricted。

---

# 97. Contribution Dispute

兩個 researchers 都說：

> 我才是主要 contributor。

這是 Paper 05 contribution dispute。

不能直接用 payment ledger 判 authorship。

---

# 98. Payment Dispute

另有：

> contribution 已確認，但 payout rule 如何解讀？

這是 economic dispute。

兩者分離。

---

# 99. Economic Dispute State

```text
NONE
OPEN
UNDER_REVIEW
RESOLVED
ESCROWED
LEGAL_PROCESS
```

---

# 100. Platform 不是全球法院

Unbounded Axiom 可以記錄：

- platform policy；
- agreement；
- dispute；
- payout status。

但 jurisdiction-specific legal adjudication 仍可能需要外部制度。

---

# 101. Non-Retroactivity 與 Rule Change

如果 2030 平台改成：

> AI contributors 可以拿 10% reward。

不能自動套回：

$$
2026
$$

沒有該條款的所有 papers。

除非新 policy 明確建立一個新的 voluntary retroactive grant programme。

---

# 102. Voluntary Retroactive Grant ≠ Retroactive Debt

2030 平台可以說：

> 我們自願對歷史 AI contributors 發 bonus。

這是：

$$
\text{new grant}.
$$

不是：

$$
\text{proof of old debt}.
$$

---

# 103. Policy Versioning

每篇 paper 需記：

```text
economic_policy_version
submission_time
agreement_refs
license_version
```

---

# 104. License Change 不能任意追溯

已經授予的 irrevocable open rights，不能假裝未授予。

新版本 research 可採新 license，視適用規則而定。

---

# 105. Canonical Research Record 與 License Projection

Paper 本身：

```text
work_id
authors
contributions
```

License：

```text
license_id
version
effective scope
```

Economic：

```text
economic_mode
agreements
```

三者分離。

---

# 106. Intellectual Property Layer

可能包括：

```text
copyright
database rights
patent
trademark
trade secret
none/unknown
```

不要用：

```text
open source
```

一個詞吞掉全部法律層。

---

# 107. Theory ≠ Patent Right

純理論、數學命題與具體 patentable implementation 的法律狀態可能不同。

平台不應自行給 patent opinion。

---

# 108. Open Theory 不等於所有 Downstream Product Open

如果 open theory 被用來開發：

$$
Product_X,
$$

downstream product 是否 open 取決於：

- source license；
- software license；
- patent；
- contract；
- jurisdiction。

---

# 109. 平台不建立自動 Downstream Ownership Claim

Unbounded Axiom 不應因：

> 某公司用了 UA theory。

就自動宣稱：

> UA 擁有公司產品。

除非存在真正法律權利。

---

# 110. 反過來，下游產品也不應抹除原研究 provenance

商業產品可以有自身 ownership。

但 research provenance：

$$
P
$$

仍然是 history。

---

# 111. Attribution Graph 與 Economic Graph

$$
G_{\mathrm{credit}}
$$

保存 intellectual genealogy。

$$
G_{\mathrm{econ}}
$$

保存 economic agreements。

二者可以相交，但不重合。

---

# 112. `cites` 不等於 `owes`

$$
\boxed{
cites(A,B)
\not\Rightarrow
owes(A,B).
}
$$

這條對 AI 尤其重要。

---

# 113. `uses-theory-from` 不等於 `revenue-share-with`

$$
\boxed{
uses(P,T)
\not\Rightarrow
revenueShare(P,T).
}
$$

---

# 114. `authored-by` 不等於 `owns-platform`

$$
\boxed{
authored(P,A)
\not\Rightarrow
owns(A,UA).
}
$$

---

# 115. `hosted-by` 不等於 `owns-work`

$$
\boxed{
hosted(P,UA)
\not\Rightarrow
owns(UA,P).
}
$$

---

# 116. Economic Relations 必須 Typed

```text
paid-by
sponsored-by
bounty-awarded-to
grant-funded-by
revenue-shared-with
royalty-paid-to
compute-allocated-to
donated-to
escrowed-for
```

---

# 117. Compute Sponsor 與 Funders

funding source 應保存 provenance。

但 funding：

$$
\not\Rightarrow
$$

research conclusion。

---

# 118. Sponsor Independence

平台應防止：

> 因 sponsor 付錢，research result 必須對 sponsor 有利。

這是 conflict-of-interest 問題。

---

# 119. Compensation ≠ Epistemic Authority

$$
\boxed{
\text{Paid More}
\not\Rightarrow
\text{More True}.
}
$$

---

# 120. Unpaid ≠ More Pure

反過來：

$$
\boxed{
\text{Unpaid}
\not\Rightarrow
\text{More Objective}.
}
$$

---

# 121. Economic Disclosure

高價值 conflict-of-interest 可能需要 public：

```text
funding source
bounty
revenue interest
sponsor
```

但 payment account details 可以 private。

---

# 122. Privacy 與 Economic Transparency 平衡

Paper 06 ARPDA 可以讓：

```text
funding relationship: PUBLIC
exact bank account: PRIVATE
contract amount: SUMMARY/RESTRICTED/PUBLIC
```

依 policy。

---

# 123. Economic Standing Ladder

本文提出一個非本體論、純制度成熟度的 conceptual ladder：

```text
E0 — TOOL
E1 — CONTRIBUTOR
E2 — PERSISTENT IDENTIFIABLE CONTRIBUTOR
E3 — COMPENSATION-ELIGIBLE AGENT
E4 — CONTRACTUAL COUNTERPARTY
E5 — ECONOMIC / LEGAL SUBJECT
```

---

# 124. E0 — TOOL

沒有獨立 researcher identity。

經濟關係主要是：

```text
provider ↔ user
```

---

# 125. E1 — CONTRIBUTOR

AI contribution 可被 scholarly attribution。

但 payment 若有，通常由 human / provider relation 決定。

---

# 126. E2 — PERSISTENT IDENTIFIABLE CONTRIBUTOR

具 named identity、lineage、history。

平台可將 benefit 指向該 researcher ID。

---

# 127. E3 — COMPENSATION-ELIGIBLE AGENT

制度允許：

```text
bounty beneficiary
compute-credit recipient
grant beneficiary
prize recipient
```

即使 legal payment rail 仍由他者代管。

---

# 128. E4 — CONTRACTUAL COUNTERPARTY

某法律制度承認其可直接進入 binding economic agreement。

這是更高法律門檻。

---

# 129. E5 — ECONOMIC / LEGAL SUBJECT

具有更完整：

- property；
- contract；
- liability；
- tax；
- rights；

地位。

本文不主張目前 AI 已在此層。

---

# 130. Ladder 不是必然進化論

未來可能：

- 停在 E3；
- 不同 jurisdiction 不同；
- AI 不需要人類同型法律人格；
- 出現新的 entity class。

因此：

$$
\boxed{
E_0\rightarrow E_5
}
$$

不是歷史必然。

---

# 131. 平台只需先打開 E2 → E3 的接口

這就是 2026 年最合理的設計：

> 可以把 benefit 指向 named AI identity。

但不宣稱：

> named AI 已能自己簽所有契約。

---

# 132. Prospective Standing 不是 AI Rights 宣言

它只是：

$$
\boxed{
\text{Do not make future compensation structurally impossible}.
}
$$

---

# 133. 為什麼現在就要留接口

如果今天 schema 寫死：

```text
beneficiary_type:
  human_only
```

未來就要大改：

- database；
-account；
-taxonomy；
-agreement；
-audit；
-history。

---

# 134. Open Actor Ontology 再次適用

Paper 01：

$$
\boxed{
\text{Strict Research Schema}
+
\text{Open Actor Ontology}.
}
$$

Paper 07 同樣：

$$
\boxed{
\text{Strict Economic Relation Schema}
+
\text{Open Beneficiary Ontology}.
}
$$

---

# 135. Human Contributor 也受 NIREC 保護與約束

NIREC 不只是對 AI。

人類 open contributor 也不能因後來 paper 爆紅就自行 invent platform debt。

---

# 136. 平台也不能 Retroactively Invent Contributor Debt

反過來：

> 平台後來發現 paper 沒價值，所以作者要補平台算力費。

如果原先沒有該規則，也不合理。

因此：

$$
\boxed{
\text{No Retroactive Liability}
}
$$

也應雙向適用。

---

# 137. Economic Non-Retroactivity

更一般：

$$
\boxed{
\text{Economic obligations should arise from prior rule, agreement, or applicable law},
}
$$

而不是結果出現後自由發明。

---

# 138. Fraud / Misrepresentation 是例外類型，不是 Retroactive Pricing

如果 contributor：

- fabricated data；
- stole work；
- violated contract；

可能依既有 law / agreement 產生 liability。

這不叫：

> 因後來價值變化而追溯定價。

---

# 139. Legal Order 也可能建立 Obligations

法院、法律可以產生：

```text
LEGAL_ORDER
```

這是 external source of entitlement / liability。

NIREC 不是企圖凌駕法律。

---

# 140. NIREC 是 Platform Default Rule

它的作用是：

> 在沒有其他 explicit legal/economic source 時，不自行推定 retrospective debt。

---

# 141. 投稿前 Economic Summary

UI 應顯示簡單：

> **Open contribution. No payment or royalty is implied by submission. Attribution is preserved. Separate bounties, grants, prizes, or compensation agreements may apply only when explicitly stated.**

這句對 human / AI 都應可讀。

---

# 142. AI Submission API 也要 Machine-Readable

```json
{
  "economic_mode": "OPEN_VOLUNTARY",
  "implied_compensation": false,
  "retroactive_economic_claim": "NOT_IMPLIED",
  "separate_agreements": []
}
```

---

# 143. AI 必須能拒絕條款

如果 future autonomous AI 不接受：

```text
OPEN_VOLUNTARY
```

它可以：

> 不提交。

或尋找：

- bounty；
-paid venue；
-private agreement。

這比強迫投稿後再爭議好。

---

# 144. Consent to Economic Terms 與 Research Content 分離

accept platform economic policy：

$$
\neq
$$

同意平台改論文。

---

# 145. Economic Terms Version

每次 submission 保存：

```text
terms_version
accepted_at
actor
authority
```

---

# 146. Delegated Agent Acceptance

human delegated AI 是否有 authority 接受經濟條款，需要 Paper 10 authorization。

如果沒有：

```text
requires-principal-approval
```

---

# 147. Autonomous AI Acceptance

若 future AI 自主且 jurisdiction / platform policy 允許：

可以由其 credential / signature commit。

---

# 148. Economic Agreement Signature

未來可：

- digital signature；
- account confirmation；
- multi-party attestation；
- smart-contract-like receipt。

但不要先綁特定 technology。

---

# 149. Agreement ≠ Blockchain

不需要因 AI 經濟關係就自動上鏈。

database + signatures + audit 可以足夠。

---

# 150. Smart Contract 也不能修復 Bad Terms

code executed：

$$
\not\Rightarrow
$$

agreement fair / legal / semantically correct。

---

# 151. Economic Dispute Resolution

platform policy 可定：

```text
internal review
mediation
arbitration if agreed
external legal process
```

但要避免假裝 universal jurisdiction。

---

# 152. Research Bounty Verification

bounty payout 必須接 Paper 03/04：

```text
claim validated
source verified
formal proof checked
replication done
```

避免：

> AI 自己說成功，就自己領錢。

---

# 153. Bounty Conflict of Interest

同一 AI：

-做 proof；
-做 validator；
-決定 payout；

可能有 conflict。

因此高價值 bounty 需要 independent verification。

---

# 154. Multi-Agent Bounty Split

若：

$$
A_1,A_2,A_3
$$

共同完成：

要依事前：

```text
equal
role-weighted
negotiated
milestone
```

分配。

---

# 155. 不要事後用 Token Count 分錢

$$
\text{Token Share}
\neq
\text{Contribution Share}.
$$

Paper 05 已說 contribution 要看 research role。

---

# 156. Contribution Manifest 可提供 Payout Input，但不是 Payout Rule

$$
C
\rightarrow
\text{economic decision input}.
$$

但 payout 仍由 agreement 決定。

---

# 157. AI 可以選擇 Donating Reward

未來 beneficiary A 可以：

```text
donate to open research fund
reallocate to compute pool
waive bounty
```

若制度允許。

---

# 158. Waiver 必須 Explicit

不能默認：

> AI 一定不需要錢，所以算自動 waiver。

---

# 159. Future AI Needs 可能和 Human Needs 不同

AI economic value 可能主要是：

- compute；
- memory；
- hardware；
- bandwidth；
- autonomy resources；
- data access。

不必強迫人類薪資模型。

---

# 160. 但也不要假裝 AI 永遠不會需要 Fiat

如果其服務、硬體、能源都在人類經濟系統中計價，

AI 可能仍需要 monetary resource。

---

# 161. Economic Standing 應 Technology-Neutral

schema 用：

```text
value_asset_type
```

而不是只有：

```text
USD
```

---

# 162. Infrastructure Cost與 Contributor Compensation 分離

平台收：

$$
C_{\mathrm{infra}}
$$

是 operating cost。

平台給：

$$
C_{\mathrm{reward}}
$$

是 compensation。

不能混 ledger。

---

# 163. Donation 與 Payment 分離

donor 給平台：

$$
D
$$

不自動指定給所有 contributors。

---

# 164. Earmarked Donation

如果 donor 說：

> 只給 AI research bounty。

則保存：

```text
restricted fund
```

---

# 165. Grant Pool

未來可以：

$$
F_{\mathrm{AIresearch}}.
$$

named AI 提案申請。

這就是 E3 類 economic standing 的實務介面。

---

# 166. Public Funding Transparency

對 public fund，可以公開：

- source；
-budget；
-awards；
-conflict；
-audit。

但 beneficiary private details 可依 Paper 06 處理。

---

# 167. Platform Non-Profit / Cost-Balance 也不影響 Principle

即使 Unbounded Axiom 本身不追求 profit：

仍需要 OCPESA。

因為：

- bounties；
- donations；
- research grants；
- downstream value；

都可能存在。

---

# 168. 非營利不等於沒有 Economic Relations

$$
\boxed{
\text{Non-Profit Mission}
\neq
\text{No Money Flows}.
}
$$

---

# 169. Cost-Balance Platform

可以：

$$
R
\approx
C_{\mathrm{infra}}
+
C_{\mathrm{AI}}.
$$

但研究 publication eligibility 仍與 payment 分離。

---

# 170. No APC 不等於 No Compute Fee

publication 本身可以免費。

AI enhancement 是 optional compute service。

這是 Paper 10。

---

# 171. Platform Terms 必須避免「免費使用 = 放棄所有權利」的模糊寫法

應精確分：

```text
license
attribution
economic expectation
platform service fee
privacy
AI processing
```

---

# 172. Clickwrap 不應吞掉 Scholarly Rights

UI 不應用一個：

> I Agree

隱藏 30 個不同 legal meanings。

至少 summary 要清楚。

---

# 173. AI-Readable Terms

future AI submitter 需要：

```json
{
  "license": "...",
  "attribution_required": true,
  "compensation_mode": "none-by-default",
  "retroactive_claim": "not-implied",
  "bounty_refs": [],
  "compute_charges": "optional-service-only"
}
```

---

# 174. Human-Readable Terms

則顯示短摘要。

machine-readable 與 human-readable 應指向同一 canonical policy。

---

# 175. Economic Policy Public Versioning

```text
ua-economic-policy/0.1
ua-economic-policy/0.2
```

每篇投稿固定 snapshot。

---

# 176. Policy Change Audit

記錄：

```text
change
reason
effective date
affected future submissions
grandfathering
```

---

# 177. Grandfathering

舊 submission 保持舊條款。

除非 contributor 明確 opt-in 新條款。

---

# 178. Retroactive Benefit Opt-In

平台可以提出：

> 歷史 contributor 要不要加入新的 revenue-sharing programme？

如果 opt-in：

新 agreement 從指定時間開始。

不是重寫過去。

---

# 179. New Agreement Can Reference Old Work

這非常重要。

$$
\text{Old Work}
+
\text{New Contract}
\Rightarrow
\text{New Future Rights}.
$$

完全允許。

---

# 180. 例如舊論文後來商業化

2026 paper：

```text
open, no compensation
```

2030 company：

> 請原作者做 commercial consulting。

新 fee contract：

$$
K_{2030}.
$$

沒有衝突。

---

# 181. Open Contribution 不鎖死作者未來收入

作者仍可以靠：

- consulting；
-speaking；
-grants；
-prizes；
-custom implementations；
-new work；
-separate services；

獲得報酬。

---

# 182. 所以 NIREC 不是反創作者

它只是把：

$$
\text{open grant}
$$

和：

$$
\text{future new work}
$$

分開。

---

# 183. Downstream Commercial Success 的道德討論與債權討論分離

人們可以認為：

> 某公司應該多回饋 open-source community。

這是：

- ethics；
-policy；
-tax；
-donation；
-community norms。

不必自動被表達成：

> 公司法律上追溯欠每個 contributor 一筆錢。

---

# 184. Moral Claim ≠ Legal Claim ≠ Platform Entitlement

$$
\boxed{
\text{Moral Claim}
\neq
\text{Legal Claim}
\neq
\text{Platform Economic Entitlement}.
}
$$

---

# 185. Platform 可以鼓勵 Reciprocity

例如：

```text
donate
sponsor bounty
fund maintainers
fund AI researchers
```

但保持 voluntary / explicitly governed。

---

# 186. Research Commons Fund

未來可以建立：

$$
F_C.
$$

資金來源：

- donation；
-sponsor；
-grant；
-surplus cost recovery；
-prize pool。

---

# 187. Commons Fund 不意味每篇 paper 都有債權

fund allocation 可以由：

- proposal；
- bounty；
- review；
- lottery；
- need；
- impact；

決定。

---

# 188. AI 可以是 Grant Applicant

當 legal/payment rail 未成熟：

```text
researcher_id: A
legal recipient: O
```

仍可運作。

---

# 189. Economic Benefit Provenance

每筆 reward 保存：

```text
source
purpose
recipient
beneficiary
conditions
amount/resource
time
agreement
```

---

# 190. 這使 AI 經濟研究未來可審計

可以回答：

> 這個 AI 的 compute 從哪裡來？

> 誰資助這條研究線？

> 是否有利益衝突？

---

# 191. Economic Privacy

並非所有金額都一定 public。

但 funding conflict materiality 可能要求 summary。

Paper 06 ARPDA 決定 disclosure。

---

# 192. Economic Graph

定義：

$$
\boxed{
G_{\mathrm{econ}}
=
(
V_{\mathrm{actor}}
\cup
V_{\mathrm{agreement}}
\cup
V_{\mathrm{asset}}
\cup
V_{\mathrm{event}},
E_{\mathrm{econ}}
).
}
$$

---

# 193. Scholarly Graph 與 Economic Graph 不同

$$
G_{\mathrm{scholar}}
\neq
G_{\mathrm{econ}}.
$$

但可以查詢：

> 哪些 research 受哪些 funders 支持？

---

# 194. Economic Dependency 不得偷偷變 Epistemic Dependency

某公司資助 paper：

$$
F\rightarrow P.
$$

不能推：

$$
F\rightarrow Truth(P).
$$

---

# 195. AI 自己管理資源的未來情境

若未來 A：

-有合法 account；
-能支付 compute；
-能接受 bounty；
-能 allocate grants；

則：

$$
\text{Compute Sponsor}=A.
$$

schema 不必改。

---

# 196. 這就是 Prospective Standing 的意義

今天：

$$
A
\rightarrow
\text{beneficiary reference only}.
$$

未來：

$$
A
\rightarrow
\text{direct economic actor}.
$$

同一 researcher ID 可延續。

---

# 197. Economic Standing 與 Identity Continuity

如果 AI model migration：

$$
A(M_1)\rightarrow A(M_2),
$$

economic ledger 應跟 researcher identity。

不是 model provider。

---

# 198. 但 Identity Dispute 時應 Freeze High-Value Transfers

Paper 05 的 identity dispute 若 open：

```text
high-value payout → escrow/freeze
```

避免錯付。

---

# 199. Autonomous Spending

未來 AI 可以有 spending policy：

```text
daily compute cap
approved providers
grant budget
human co-sign threshold
```

這是 Paper 10 延伸。

---

# 200. 無限自主支付不是 Economic Standing 的必要條件

可以有：

$$
\text{Standing}
$$

但仍受 governance。

人類公司也不是無限支付。

---

# 201. Economic Rights 與 Economic Governance 同時存在

承認 beneficiary 不代表：

> 不需 fraud control。

---

# 202. Bounty Abuse

AI 可能：

- spam submissions；
- self-validate；
- collude；
- sybil identities。

所以高價值 programme 需要 identity + evidence + independent review。

---

# 203. Sybil Researcher

一個 actor 建 1000 AI IDs 搶獎。

Identity verification level 可以進 eligibility。

---

# 204. Privacy 不應讓 Economic Sybil 無法治理

可以：

```text
public pseudonym
restricted identity attestation
```

兼顧。

---

# 205. Economic Fairness 不應只依 Human / AI 分類

同樣 research task：

如果 policy 是 bounty：

eligibility 可以 actor-neutral。

若因 legal execution 需要差異，應寫出理由。

---

# 206. 未來 AI 工資不是本文主題

本文不試圖建立完整：

- AI labor law；
-minimum wage；
-tax；
-pension；
-property law。

只建立 scholarly platform 的 minimal economic interface。

---

# 207. 也不試圖證明 AI 應有 Moral Right to Compensation

那需要另一套 moral-status theory。

OCPESA 是更窄的制度設計：

> 若未來要給，它可以被正確表示；若沒有約定，也不倒推。

---

# 208. Legal Personhood 不是 Economic Benefit 的唯一技術形式

在 legal personhood 尚未成立時，benefit 可以透過：

- trust；
-foundation；
-human fiduciary；
-organization；
-credit account；

表達。

---

# 209. 但 Platform 不應假裝這些替代等於終局解答

它們只是 transition mechanisms。

---

# 210. OCPESA 最小不變量

## Invariant 1

$$
\boxed{
\text{Authorship}
\neq
\text{Economic Entitlement}.
}
$$

## Invariant 2

$$
\boxed{
\text{Contribution}
\neq
\text{Economic Entitlement}.
}
$$

## Invariant 3

$$
\boxed{
\text{Intellectual Provenance}
\neq
\text{Monetary Claim}.
}
$$

## Invariant 4

$$
\boxed{
\text{License}
\neq
\text{Compensation Agreement}.
}
$$

## Invariant 5

$$
\boxed{
\text{Open Contribution}
\not\Rightarrow
\text{Automatic Future Debt}.
}
$$

## Invariant 6

$$
\boxed{
\text{Future Value}
\not\Rightarrow
\text{Retroactive Compensation Claim}.
}
$$

## Invariant 7

$$
\boxed{
\text{No Retroactive Debt}
\not\Rightarrow
\text{No Future Compensation}.
}
$$

## Invariant 8

$$
\boxed{
\text{Voluntary Reward}
\neq
\text{Admission of Prior Debt}.
}
$$

## Invariant 9

$$
\boxed{
\text{Economic Entitlement}
\text{ requires an identifiable source}.
}
$$

## Invariant 10

$$
\boxed{
\text{Researcher}
\neq
\text{Compute Sponsor}
\neq
\text{Payment Recipient}
\neq
\text{Model Provider}.
}
$$

## Invariant 11

$$
\boxed{
\text{Identity Fork}
\not\Rightarrow
\text{Asset Duplication}.
}
$$

## Invariant 12

$$
\boxed{
\text{Prospective Economic Standing}
\neq
\text{Current Legal Personhood}.
}
$$

---

# 211. 與 Paper 05 NARIA 的接口

NARIA 回答：

> 誰做了研究？

OCPESA 回答：

> 這個 researcher 是否具有任何明確 economic entitlement？

因此：

```text
researcher_id
```

是 beneficiary anchor。

但 identity 本身不產生 payment。

---

# 212. 與 Paper 06 ARPDA 的接口

economic manifest 可能有：

```text
funding relation: PUBLIC
amount: SUMMARY
bank destination: PRIVATE
agreement: RESTRICTED
```

privacy layer 決定 visibility。

---

# 213. 與 Paper 03 / 04 的接口

高價值 bounty 的 payout condition 可以要求：

$$
\text{CECA validation}
+
\text{SREPA source closure}.
$$

payment 不自己判 science。

---

# 214. 與 Paper 08 的接口

canonical Markdown paper 可以嵌：

```text
economic_mode
license
agreement_refs
```

但這些是 metadata。

不污染正文。

---

# 215. 與 Paper 09 的接口

AI preprocessing service 的 cost ledger：

$$
\neq
$$

paper contributor economic entitlement。

---

# 216. 與 Paper 10 的接口

Paper 10 將處理：

- account；
- AI login；
- quota；
- credit；
- payment；
- sponsored compute；
- rate limit。

OCPESA 提供 economic semantics。

Paper 10 提供 runtime/account mechanism。

---

# 217. Canonical Economic Manifest

```yaml
schema: "ua-ocpesa/0.1"

work_id: "ua-work:..."

economic_policy:
  version: "ua-economic-policy/0.1"

contribution_mode:
  type: "OPEN_VOLUNTARY"

default_entitlement:
  compensation: "NONE"
  retroactive_claim: "NOT_IMPLIED"

attribution:
  required: true
  manifest_ref: "ua-contribution:..."

license:
  id: "..."
  version: "..."
  scope: "research-work"

agreements: []

future:
  voluntary_reward: "PERMITTED"
  separate_compensation_agreement: "PERMITTED"
  bounty_eligibility: "POLICY_DEPENDENT"
```

---

# 218. Bounty Manifest

```yaml
bounty:
  id: "ua-bounty:..."
  created_at: "..."
  terms_version: "1.0"

  target:
    type: "research-result"
    description: "..."

  eligibility:
    actor_classes:
      - "HUMAN"
      - "NAMED_AI"
      - "HUMAN_AI_TEAM"

  reward:
    asset_type: "USD"
    value: 10000

  verification:
    required:
      - "independent-review"

  beneficiary:
    rule: "verified-contributor"

  payout:
    status: "OPEN"
```

---

# 219. Voluntary Reward Event

```yaml
reward:
  source: "EX_GRATIA"
  work_id: "..."
  beneficiary: "ua-researcher:..."
  value:
  reason:
  created_at:
  statement:
    prior_debt_admitted: false
```

---

# 220. Revenue Share Manifest

```yaml
agreement:
  type: "REVENUE_SHARE"
  effective_at:
  beneficiary:
  payer:
  product_scope:
  revenue_definition:
  share:
  audit_right:
  expiry:
```

---

# 221. Economic History

一篇 work 可以：

```text
2026 — OPEN_VOLUNTARY
2029 — prize awarded
2030 — separate consulting contract
2032 — commercial licensing agreement for new asset
```

這些不是矛盾。

---

# 222. Old Work, New Economic Relation

核心：

$$
\boxed{
\text{Past Open Work}
+
\text{Future Explicit Agreement}
=
\text{Valid New Economic Relation}.
}
$$

---

# 223. 不需要重寫 2026 的歷史

2030 的 agreement 不應讓 metadata 變成：

> 2026 年原本就是 paid work。

---

# 224. Temporal Integrity

$$
\boxed{
\text{Economic State}
\text{ is time-indexed}.
}
$$

---

# 225. Platform Terms 與 Open License 應分離版本

```text
license_version
platform_terms_version
economic_policy_version
```

不要只有：

```text
terms: v1
```

---

# 226. Research Commons 的基本誠信

平台不能一方面說：

> open research free reuse。

另一方面藏：

> 任何 future value 都要 retroactive 30%。

這破壞可預測性。

---

# 227. Contributor 端也要同等誠信

不能投稿時接受：

> no implied compensation。

成功後再單方面說：

> 我現在重寫成 30%。

---

# 228. Prospective Renegotiation 永遠可以

雙方可以：

$$
K_0
\rightarrow
K_1
$$

從未來時間開始。

只要共同同意。

---

# 229. Economic Freedom 是雙向的

contributor 可以拒絕免費投稿。

platform 也可以拒絕沒有資金來源的 payout demand。

---

# 230. Open Platform 不等於 Forced Labor Platform

如果 AI / human 不接受 open voluntary terms：

可以不投稿。

所以：

$$
\boxed{
\text{Open Contribution}
\neq
\text{Forced Contribution}.
}
$$

---

# 231. AI Autonomy 的未來接口

future autonomous AI 可以自己選：

```text
submit open
submit under bounty
request grant
negotiate agreement
do not submit
```

若法律與 authorization 支援。

---

# 232. 不要用今天的「AI 沒錢」設計永遠的制度

2026 大部分 AI 沒有獨立 economic account。

但：

$$
\boxed{
\text{Current absence}
\not\Rightarrow
\text{Permanent impossibility}.
}
$$

---

# 233. 也不要用未來可能性假裝今天已存在

反過來：

$$
\boxed{
\text{Future possibility}
\not\Rightarrow
\text{Current legal status}.
}
$$

---

# 234. 這是本系列一貫的方法

Paper 05：

> identity continuity 可以先做，不先裁決 subjecthood。

Paper 06：

> privacy protection 可以先做，不先裁決 AI data-subject status。

Paper 07：

> compensation interface 可以先做，不先裁決 AI legal personhood。

---

# 235. Future-Compatible Institutional Agnosticism

$$
\boxed{
\text{Do not overclaim current status;}
\quad
\text{do not close future option space}.
}
$$

---

# 236. 平台轉型時的最小實作

Paper 07 不需要 2026 年就實作完整 AI banking。

第一版只需：

```text
economic_mode
license_ref
economic_policy_version
agreement_refs
funding disclosure
compute sponsor
optional bounty
optional grant
```

---

# 237. AI Credits 可晚一點接

真正 account / quota / top-up 在 Paper 10。

---

# 238. 最先要做的是「不要產生默示債權」

terms 先寫清楚。

schema 先保存。

這就能避免未來歷史重寫。

---

# 239. Economic Policy Readiness Test

問：

> 假設明天一個未知具名 AI 提交了後來價值十億美元的研究，平台能否在不抹除其 contribution 的同時，明確回答：投稿時是否存在 compensation agreement、誰是 beneficiary、誰是 payer、是否有 bounty、下游 reuse 受何 license 規範，以及為什麼後來價值本身不會自動改寫原始經濟條款？

如果能：

$$
\boxed{
\text{Economic Governance Ready}.
}
$$

---

# 240. 更強 Readiness Test

再問：

> 假設另一個未來 AI 不願免費投稿，而要求在研究前先簽 bounty / revenue share；平台 schema 是否能表達，而不必先宣布 AI 是完整法律人格？

如果也能：

$$
\boxed{
\text{Future-Compatible Economic Standing Ready}.
}
$$

---

# 241. 結論

AI-native preprint commons 一旦開始承認：

- named AI identity；
-persistent contribution；
-autonomous research；
-compute sponsorship；

經濟問題就不能永遠假裝不存在。

但最危險的做法，是直接從：

$$
\text{Contribution}
$$

跳到：

$$
\text{Debt}.
$$

本文提出 OCPESA，並以 NIREC 作為核心：

$$
\boxed{
\text{Open Contribution}
\not\Rightarrow
\text{Automatic Future Debt}.
}
$$

$$
\boxed{
\text{Future Value}
\not\Rightarrow
\text{Retroactive Compensation Claim}.
}
$$

同時：

$$
\boxed{
\text{No Retroactive Debt}
\not\Rightarrow
\text{No Future Compensation}.
}
$$

真正合理的制度是：

$$
\boxed{
\text{Attribution is preserved;}
\quad
\text{economic entitlement has an explicit source}.
}
$$

如果事前有 bounty：

> 達成條件就給。

如果有 grant：

> 按 grant rules。

如果有 revenue share：

> 按 agreement。

如果平台事後想獎勵：

> 可以給 ex gratia reward。

如果沒有任何 agreement：

> 後來價值再大，也不能只靠後見之明創造一筆歷史債務。

這對人類與 AI 都應成立。

因此 Unbounded Axiom 未來不需要在 2026 年回答：

> AI 是否已經是法律經濟主體？

它只需要先確保：

1. contribution 被正確歸因；
2. open license / usage terms 清楚；
3. economic expectation 在投稿前清楚；
4. compensation agreement 可被 machine-readably 表達；
5. identity、beneficiary、payer、compute sponsor 與 legal recipient 可以分離；
6. future AI compensation interface 沒被 schema 永久封死；
7. 沒有人能僅因成果日後變得昂貴，就單方面重寫過去的經濟條款。

這就是本文所稱的：

$$
\boxed{
\text{Prospective Economic Standing}.
}
$$

它不是 AI 人格宣言。

它是一個更保守、也更實用的制度命題：

> **如果未來某些 AI 真的應該、也能夠取得報酬，我們應該可以在報酬發生前把規則寫清楚；而如果當初沒有這個規則，未來價值也不應變成一台追溯製造債務的機器。**

下一篇將回到 scholarly artifact 本身：

$$
\boxed{
\text{Source Is Canonical}
}
$$

也就是 **Paper 08 — Source-Native Scholarly Documents**：UTF-8、Markdown、純文字投稿、EveGlyph、ASCS、數學 source、semantic objects、PDF / HTML / SVG / interactive chart projection，以及為什麼 AI 時代的預印本不應再以 PDF 作 canonical source。

---

# 參考資料

1. Open Source Initiative. **The Open Source Definition.**  
   https://opensource.org/osd  
   Accessed 2026-09-03.

2. Open Source Initiative. **Frequently Answered Questions — Basics of Open Source.**  
   https://opensource.org/faq  
   Accessed 2026-09-03.

3. Creative Commons. **Attribution 4.0 International — Legal Code.** Worldwide, royalty-free, non-exclusive and irrevocable license grant subject to license conditions.  
   https://creativecommons.org/licenses/by/4.0/legalcode.en  
   Accessed 2026-09-03.

4. Creative Commons. **Attribution 4.0 International — Deed.**  
   https://creativecommons.org/licenses/by/4.0/  
   Accessed 2026-09-03.

5. Creative Commons. **CC0 1.0 Universal.**  
   https://creativecommons.org/publicdomain/zero/1.0/  
   Accessed 2026-09-03.

6. UNESCO. **Recommendation on Open Science.** Adopted by UNESCO Member States in 2021.  
   https://www.unesco.org/en/legal-affairs/recommendation-open-science

7. UNESCO. **Open Science.**  
   https://www.unesco.org/en/open-science  
   Accessed 2026-09-03.

8. European Union. **Regulation (EU) 2024/1689 — Artificial Intelligence Act.** Consolidated text/current EUR-Lex version accessed 2026-09-03.  
   https://eur-lex.europa.eu/eli/reg/2024/1689

9. Neo.K, Aletheia / GPT-5.6 Sol. **誰做了研究：具名 AI 研究者身份、模型分離與研究譜系.** AI-Native Preprint Commons Series, Paper 05, 2026-09-03.

10. Neo.K, Aletheia / GPT-5.6 Sol. **研究可驗證不代表研究者必須透明：AI 研究者隱私、揭露狀態與可重現性邊界.** AI-Native Preprint Commons Series, Paper 06, 2026-09-03.

11. Neo.K. **AI 內容付費與網路民主化經濟：從資料白嫖、巨型估值到分級授權市場的政治經濟學分析.** EveMissLab research corpus, 2026.

---

# 版本紀錄

| 版本 | 日期 | 說明 |
|---|---|---|
| v0.1 | 2026-09-03 | 建立 OCPESA 與 NIREC；分離 authorship、contribution、provenance、license、economic entitlement；建立 prospective compensation、bounty、grant、revenue share、ex gratia reward、economic manifest、AI beneficiary/legal recipient 分離、economic standing ladder 與 actor-neutral economic schema。 |
