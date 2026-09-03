# ALD-09｜人機雙法律界面：高解析 AI 法律與民主可理解性的共同憲政
## Dual Human–Machine Legal Interfaces: High-Resolution AI Law and Democratically Comprehensible Constitutionalism

**系列：**《AI 法律域：機器原生法律、規範 Runtime 與人機雙法律棧》  
**系列位置：** 第 09 篇 / 10  
**前篇：** ALD-08〈動態忒修斯的法律繼受：Fork、Merge、Restore 與未決身份下的責任〉  
**版本：** v0.1  
**日期：** 2026-08-21  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／AI 法律域／人機法律界面／法律投影／民主可理解性  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

ALD-01 至 ALD-08 已把 AI Legal Domain 推進到高度結構化狀態：法律不只包含條文，還包含 carrier type、partial normative functions、typed failures、versioning、constitutional constraints、AI-assisted legislative patching、precedent graphs、jurisdictional routing，以及 Fork / Merge / Restore 下的 legal succession。這種法律 Runtime 對機器而言可以是合理的；但如果人類被要求閱讀完整 precedent graph、authority vector、succession matrix、proof chain、routing graph、version ledger 與 hundreds / thousands of legal fields，法律反而可能在「更精確」的同時變得政治上不可理解。

本文提出 Dual Legal Interface Framework（DLIF，人機雙法律界面框架）。其核心不是建立兩套互相獨立、可以彼此漂移的法律，而是由共同 canonical legal state：

$$
\boxed{
\mathcal L^\ast
}
$$

生成至少兩種用途不同的投影：

$$
\boxed{
\mathcal L^\ast
\xrightarrow{\pi_H}
\mathcal L_H,
}
$$

$$
\boxed{
\mathcal L^\ast
\xrightarrow{\pi_A}
\mathcal L_A.
}
$$

其中 $\mathcal L_H$ 是 human-comprehensible legal projection， $\mathcal L_A$ 是 AI / machine-processable high-resolution projection。兩者都不是新的 sovereign source。它們必須共同回溯：

$$
\boxed{
\operatorname{Source}(\mathcal L_H)
=
\operatorname{Source}(\mathcal L_A)
=
\mathcal S_{\mathrm{auth}}
}
$$

或可驗證地指向同一 authoritative source family。

本文的第一個核心原則是：

$$
\boxed{
\text{Human-Readable}
\neq
\text{Machine-Readable}
\neq
\text{Legally Authoritative}.
}
$$

人類版不是因為「更白話」就更有權威；機器版也不是因為「更精確」就更有權威。OECD 2026 Law as Code consultation 明確保留 authoritative legal text 為 legally binding source，同時要求 machine-executable representation 與來源保持 explicit links，並強調 transparency、traceability、accountability、reviewability 與 public control。這正好支持一個共同來源、多重表示、權威不漂移的架構。

本文第二個核心是 Projection Contract。單純把 machine law 交給 LLM 摘成「人話」不足以構成法律界面。本文定義：

$$
\boxed{
\mathfrak P_{H\leftarrow\ast}
=
(
Q,
Preserve,
Compress,
Loss,
Source,
Version,
Uncertainty,
Challenge,
Cert
).
}
$$

其中：

- $Q$：此投影要回答的人類法律問題集合；
- $Preserve$：必須保持的 legal distinctions；
- $Compress$：允許壓縮的內部細節；
- $Loss$：已知語義損失；
- $Source$：法源與 machine-state provenance；
- $Version$：投影所對應版本；
- $Uncertainty$：未決項；
- $Challenge$：申訴／覆核入口；
- $Cert$：Projection Certificate。

本文提出 Query-Preservation Criterion。若對指定 query family $\mathcal Q_H$：

$$
\boxed{
Ans_H(q,\mathcal L_H)
=
\mu_A
\left(
Ans_\ast(
\mu_Q(q),
\mathcal L^\ast
)
\right)
}
$$

在指定語義容忍度內成立，則稱 human projection 對 $\mathcal Q_H$ 保持法律回答能力。這比要求兩個 representations 字面完全相同更實際，也比「摘要看起來差不多」更嚴格。

本文第三個核心是 Material Human Consequence Principle（MHCP）：

$$
\boxed{
\text{No Material Human Consequence}
\text{ without a Human-Comprehensible Legal Projection and Challenge Route}.
}
$$

這不是本文宣稱的現行全球法律規則，而是 AI Legal Domain 的候選憲政原則。若某 machine-native legal decision 會實質影響人類的財產、自由、工作、福利、法律資格、基本權利或重大義務，系統至少應能向受影響人提供：

- 決定是什麼；
- 誰依法作成；
- AI 在其中扮演什麼角色；
- 主要法律依據；
- 主要事實／證據；
- 適用的關鍵例外與限制；
- 何時生效；
- 目前是否 provisional / contested；
- 如何 challenge / appeal；
- 可查驗的來源與版本。

本文不要求公開全部模型內部推理或 chain-of-thought。需要的是：

$$
\boxed{
\text{Contestable Legal Explanation}
\neq
\text{Model Internal Thought Dump}.
}
$$

截至 2026 年，現行 AI 法規已提供重要接口。EU AI Act Article 13 要求高風險 AI 的運作具有足夠透明度，使 deployers 能適當解釋輸出，並要求相關資訊 concise、complete、correct、clear、accessible、comprehensible；Article 14 更明確要求透過適當 human-machine interface tools 實現 natural-person human oversight。Article 86 則在其適用條件下，賦予受特定高風險 AI 輸出所影響的人取得 clear and meaningful explanations 的權利，內容包括 AI 在 decision-making procedure 中的 role 與決定的主要 elements。Council of Europe AI Framework Convention 也要求保留 sufficient information，使受影響人能 challenge AI-based decisions 或 system use 本身，並提供 complaint / procedural safeguards。這些現行法並不等同本文的 MHCP，但清楚顯示：「可理解＋可挑戰」已是 AI 治理的現實法治方向。

本文第四個核心是 Resolution Asymmetry Principle。AI 可以合法處理比人類介面更高解析的法律狀態：

$$
\boxed{
\dim(\mathcal L_A)
\gg
\dim(\mathcal L_H).
}
$$

但：

$$
\boxed{
\text{Higher Machine Resolution}
\not\Rightarrow
\text{Lower Human Legal Standing}.
}
$$

人類不需要知道全部 internal fields 才能行使權利；反而系統必須將與其法律地位相關的必要 distinctions 投影出來。高解析 machine law 不能成為新的「只有模型看得懂的祕密法」。

本文第五個核心是 Semantic Loss Ledger。每個 human projection 應顯式記錄：

$$
\boxed{
\Lambda_H
=
(
\lambda_{\mathrm{omitted}},
\lambda_{\mathrm{collapsed}},
\lambda_{\mathrm{approx}},
\lambda_{\mathrm{unresolved}}
).
}
$$

例如 machine layer 區分八種 authority status，而 public interface 只顯示「尚待批准」，則這個壓縮可以合法；但若 machine layer 區分 `Forbidden` 與 `EvidenceMissing`，human layer 卻都顯示「不可以」，就發生高風險 semantic collapse。ALD-03 已證明這些狀態不等價，因此 human projection 不得把法律失敗型別重新壓回 Boolean。

本文第六個核心是 Common Legal Identity Across Views。European Legislation Identifier（ELI）提供一個有用的技術祖先：同一法律資源可透過標準化 identifier、metadata 與 machine-readable formats 被 humans / computers 存取與交換。本文進一步提出：

$$
\boxed{
ID(\mathcal L_H)
=
ID(\mathcal L_A)
=
ID(\mathcal L^\ast)
}
$$

應至少在 legal-resource / version / source 層具有可驗證對應。這不是說 ELI 已實作本文的 dual-interface theory，而是說「同一法律資源、多種人機表示、共用穩定識別」已有成熟基礎。

本文最後提出 Common Constitutional Interface（CCI）。人類與 AI 不必共享相同 UI，也不必共享相同資訊密度，但若共存於同一法治域，至少需要共享：

$$
\boxed{
\mathcal C_{\mathrm{shared}}
=
(
Rights,
Authority,
Procedure,
Version,
Challenge,
Source,
Effect
).
}
$$

也就是雙方都必須能指向同一組權利邊界、權威鏈、程序狀態、規則版本、申訴通道、法源與法律效果。這不是「人類法」與「AI 法」互不相干，而是同一憲政基礎上的異質表示。

---

## 關鍵詞

AI 法律域；Dual Legal Interface；Human-Comprehensible Law；Machine-Readable Law；Law as Code；Human Oversight；Right to Explanation；Legal Projection；Semantic Loss；Contestability；European Legislation Identifier；Common Constitutional Interface；民主可理解性

---

# 0. 問題不是 AI 能不能讀懂法律，而是人類還能不能治理它

到了 ALD-08，

legal state 已經可能包含：

- typed carriers；
- normative functions；
- evidence status；
- authority；
- procedure；
- version；
- precedent graph；
- jurisdiction route；
- lineage；
- successor mapping；
- provisional status；
- responsibility certificate。

機器處理這些沒有原則問題。

但人類如果每次都要讀：

$$
10^3
$$

個欄位，

法治會遇到新的 interface crisis。

---

# 1. Complexity ≠ Illegitimacy

複雜法律不一定不合法。

航空、稅務、金融、跨境交易本來就高度複雜。

所以：

$$
\boxed{
\text{Complexity}
\neq
\text{Illegitimacy}.
}
$$

---

# 2. 但不可理解性會形成治理問題

若只有 machine 能知道：

- 為什麼禁止；
- 哪一版規則；
- 哪個法域；
- 誰有權；
- 怎麼申訴；

則：

$$
\boxed{
\text{Legal Precision}
+
\text{Human Inaccessibility}
}
$$

可能形成新的 procedural opacity。

---

# 3. Human-Readable ≠ Machine-Readable ≠ Authoritative

本文固定：

$$
\boxed{
\text{Human-Readable}
\neq
\text{Machine-Readable}
\neq
\text{Legally Authoritative}.
}
$$

三者可以重疊，

但不能預設等價。

---

# 4. Canonical Legal State

本文定義：

$$
\boxed{
\mathcal L^\ast
}
$$

為：

> 對指定 jurisdiction / version / legal domain，由 authoritative sources、formal structures、precedent、procedure、evidence 與 authorised mappings 共同支撐的 canonical legal state。

它不一定是一個單一檔案。

---

# 5. Human Projection

$$
\boxed{
\pi_H:
\mathcal L^\ast
\rightharpoonup
\mathcal L_H.
}
$$

目標是：

- comprehend；
- act；
- challenge；
- verify source；
- know legal consequence。

---

# 6. AI Projection

$$
\boxed{
\pi_A:
\mathcal L^\ast
\rightharpoonup
\mathcal L_A.
}
$$

可以保留：

- full types；
- graph edges；
- proof certificates；
- machine operators；
- routing states；
- exact versioning。

---

# 7. 兩個 Projection 不應產生兩套 Sovereign Law

$$
\boxed{
\mathcal L_H
\neq
\mathcal L_A
}
$$

在表示上可以成立。

但：

$$
\boxed{
\operatorname{AuthorityRoot}(\mathcal L_H)
=
\operatorname{AuthorityRoot}(\mathcal L_A).
}
$$

---

# 8. Shared Source Family

$$
\boxed{
\operatorname{Source}(\mathcal L_H)
=
\operatorname{Source}(\mathcal L_A)
=
\mathcal S_{\mathrm{auth}}.
}
$$

若 projection 使用不同 source，

必須顯式標示。

---

# 9. OECD Law as Code 正好提供現實邊界

OECD 2026 consultation 明確要求 machine-executable representations 與 authoritative legal texts 保持 explicit links，

並保留：

$$
\boxed{
\text{authoritative legal text remains legally binding}.
}
$$

所以：

$$
\boxed{
\text{Machine Executability}
\neq
\text{Source Replacement}.
}
$$

---

# 10. Internal Legal Compilation Layer

既有 Legal Compilation Layer 已提出：

$$
L
=
(
L_H,
L_P,
L_F,
L_S,
L_M
).
$$

其中：

- human legal text；
- plain-language projection；
- formal / computable rule；
- simulation；
- machine-readable representation。

ALD-09 將它重新接到：

$$
\mathcal L^\ast
$$

共同狀態。

---

# 11. Plain Language 不等於 Legal Authority

$$
\boxed{
L_P
\neq
L_H^{\mathrm{authoritative}}
}
$$

除非制度明確指定。

因此白話版必須能：

> 回到原法源。

---

# 12. Formal Rule 也不等於 Authoritative Text

$$
\boxed{
L_F
\neq
\mathcal S_{\mathrm{auth}}
}
$$

作現行 Law as Code 的保守預設。

---

# 13. Projection Contract

本文提出：

$$
\boxed{
\mathfrak P_{H\leftarrow\ast}
=
(
Q,
Preserve,
Compress,
Loss,
Source,
Version,
Uncertainty,
Challenge,
Cert
).
}
$$

---

# 14. $Q$：Query Family

不是要求 human projection 回答所有 machine query。

先聲明：

> 這個介面要支援哪些人類法律問題？

例如：

- why denied；
- what obligation；
- who decided；
- how appeal；
- which law；
- when effective。

---

# 15. Preserve

必須保留：

- legal effect；
- authority；
- key basis；
- review path；
- temporal status；
- relevant uncertainty。

---

# 16. Compress

可以壓縮：

- internal graph traversal；
- irrelevant proof edges；
- machine-only cache states；
- low-level serialization。

---

# 17. Loss

必須記錄：

> 哪些 distinctions 被折疊？

---

# 18. Source

每個人類 explanation：

$$
\mathcal L_H
$$

要能查：

- statute；
- regulation；
- case；
- certificate；
- version。

---

# 19. Version

projection 必須知道：

$$
\nu_H.
$$

若 source 更新：

$$
\nu^\ast
\rightarrow
\nu^{\ast+1},
$$

human projection 可能 stale。

---

# 20. Uncertainty

若 canonical state 是：

$$
\mathsf{Underdetermined},
$$

human layer 不能寫：

> 法律明確禁止。

---

# 21. Challenge

projection 不是 display-only。

應含：

- appeal；
- complaint；
- review；
- human contact；
- correction。

---

# 22. Projection Certificate

$$
\boxed{
K_{\pi_H}
=
(
query\_scope,
source,
version,
preserved,
loss,
uncertainty,
generated\_at,
challenge
).
}
$$

---

# 23. Query-Preservation Criterion

對 human query family：

$$
\mathcal Q_H,
$$

若：

$$
\boxed{
Ans_H(q,\mathcal L_H)
=
\mu_A
\left(
Ans_\ast(
\mu_Q(q),
\mathcal L^\ast
)
\right)
}
$$

在指定 tolerance 下成立，

則稱投影對該 query family 保真。

---

# 24. Query 也需要 Translation

人類問：

> 為什麼我不能領這筆補助？

machine query 可能展開為：

- claimant identity；
- eligibility；
- date；
- income rule；
- exception；
- evidence；
- version；
- appeal。

所以：

$$
\boxed{
\mu_Q:
Q_H
\rightarrow
Q_\ast.
}
$$

---

# 25. Cannot Map ≠ No

若：

$$
\mu_Q(q)
$$

不存在，

應輸出：

$$
\mathsf{QueryUnmappable}
$$

或：

$$
\mathsf{HumanReviewRequired}.
$$

不是：

$$
\mathsf{No}.
$$

---

# 26. Human Projection 不是 Summary

摘要可以省略：

> 可申訴期限。

但法律界面不應。

所以：

$$
\boxed{
\text{Legal Projection}
\neq
\text{Free-Form Summary}.
}
$$

---

# 27. Material Human Consequence Principle

本文提出候選憲政原則：

$$
\boxed{
\text{No Material Human Consequence}
\text{ without a Human-Comprehensible Legal Projection and Challenge Route}.
}
$$

---

# 28. Material Consequence

候選至少包括：

- deprivation of liberty；
- significant property effect；
- access to essential service；
- employment / education status；
- public benefits；
- legal capacity；
- major sanction；
- fundamental-right impact。

---

# 29. 本文不宣稱 MHCP 已是全球現行法

它是一個：

$$
\boxed{
\text{AI Legal Domain constitutional design principle}.
}
$$

---

# 30. EU AI Act Article 13 的現實錨點

Article 13 要求 high-risk AI：

- operation sufficiently transparent；
- deployer can interpret output；
- information concise；
- complete；
- correct；
- clear；
- relevant；
- accessible；
- comprehensible。

這非常接近：

$$
\boxed{
\text{operator-facing human projection}.
}
$$

---

# 31. Article 14：Human Oversight 是 Interface Requirement

Article 14 明確要求：

$$
\boxed{
\text{appropriate human-machine interface tools}
}
$$

使 natural persons 能有效 oversight high-risk AI。

這說明：

> human-machine interface

已不只是 UI engineering，

也可能是 compliance / rights infrastructure。

---

# 32. Article 86：Explanation of Individual Decision-Making

在 Article 86 適用範圍內，

受特定 Annex III high-risk AI system output 所影響的人，

對造成 legal effects 或 similarly significant adverse effects 的決定，

有權取得 clear and meaningful explanations，

至少涉及：

- AI role；
- main elements of decision。

---

# 33. Article 86 不是 Universal Right to Full Model Explanation

本文明確不誇大。

它有：

- scope conditions；
- exceptions；
- specific affected-person context。

所以：

$$
\boxed{
\text{Article 86}
\neq
\text{Universal Global Explainability Right}.
}
$$

---

# 34. 但它提供重要制度方向

$$
\boxed{
\text{Significant AI-Mediated Effect}
\rightarrow
\text{Meaningful Human Explanation}
}
$$

已進入實定法。

---

# 35. Council of Europe：Explanation 必須能支持 Challenge

Framework Convention 要求保留 relevant information，

讓 affected persons 可以：

- challenge AI-based decision；
- challenge system use；
- lodge complaint；
- obtain procedural safeguards。

所以：

$$
\boxed{
\text{Transparency}
\rightarrow
\text{Contestability}.
}
$$

---

# 36. 這比「告訴你用了 AI」更強

只有：

> 本決定由 AI 協助。

不足以支持 challenge。

---

# 37. Contestable Legal Explanation

本文提出：

$$
\boxed{
\mathcal E_H
=
(
Decision,
Authority,
AIRole,
LegalBasis,
Facts,
Evidence,
Exceptions,
Status,
EffectiveTime,
Challenge,
Sources
).
}
$$

---

# 38. Decision

> 系統做了什麼法律決定？

---

# 39. Authority

> 誰依法有權作成？

---

# 40. AI Role

AI 是：

- advisory；
- recommendation；
- scoring；
- partial automation；
- decisive input；
- execution only。

---

# 41. Legal Basis

至少提供：

- rule；
- section；
- regulation；
- precedent；

可追溯 reference。

---

# 42. Facts / Evidence

哪些事實：

- 被認定；
- 被爭議；
- 缺失。

---

# 43. Exceptions

是否：

- exception applied；
- exception rejected；
- discretion triggered。

---

# 44. Status

結果是：

- final；
- provisional；
- contested；
- under review；
- stale。

---

# 45. Effective Time

何時：

- 生效；
- 到期；
- 可申訴。

---

# 46. Challenge

要如何：

- appeal；
- correct facts；
- submit evidence；
- request human review。

---

# 47. Source

所有摘要要能：

$$
\boxed{
\text{drill down to source}.
}
$$

---

# 48. Explanation ≠ Chain-of-Thought

本文固定：

$$
\boxed{
\text{Contestable Legal Explanation}
\neq
\text{Model Internal Thought Dump}.
}
$$

---

# 49. 為什麼不需要 Chain-of-Thought？

因為法律上真正需要的是：

- basis；
- evidence；
- authority；
- procedure；
- review。

不是模型每個 hidden token。

---

# 50. Internal Reasoning 可以不可見，但 Legal Basis 不能消失

$$
\boxed{
\text{Private Internal Reasoning}
\not\Rightarrow
\text{Opaque Legal Effect}.
}
$$

---

# 51. Resolution Asymmetry

AI projection：

$$
\mathcal L_A
$$

可以含：

$$
10^4
$$

typed relations。

Human projection：

$$
\mathcal L_H
$$

可能只含：

$$
20
$$

critical fields。

因此：

$$
\boxed{
\dim(\mathcal L_A)
\gg
\dim(\mathcal L_H)
}
$$

可以成立。

---

# 52. 但 High Resolution 不能製造 Hierarchy of Standing

$$
\boxed{
\text{Higher Machine Resolution}
\not\Rightarrow
\text{Lower Human Legal Standing}.
}
$$

---

# 53. 人類不需要證明自己能讀整個 Graph 才有申訴權

否則：

$$
\boxed{
\text{Complexity}
\rightarrow
\text{Rights Barrier}.
}
$$

這不可接受。

---

# 54. Minimum Sufficient Human Legal Surface

本文提出：

$$
\boxed{
\operatorname{MSHLS}(q)
}
$$

為：

> 對一個 material legal consequence，足以讓 ordinary affected person 理解效果、主要理由與救濟方式的最低 legal surface。

---

# 55. MSHLS 不等於所有人都只看一頁

可再展開：

- plain layer；
- professional layer；
- audit layer；
- machine layer。

---

# 56. Progressive Disclosure

本文提出：

$$
\boxed{
L_{H0}
\subset
L_{H1}
\subset
L_{H2}
\subset
L_A.
}
$$

---

# 57. $L_{H0}$：Immediate Notice

例如：

- decision；
- effect；
- deadline；
- challenge button / route。

---

# 58. $L_{H1}$：Plain-Language Explanation

加入：

- main basis；
- facts；
- AI role；
- exceptions。

---

# 59. $L_{H2}$：Professional / Legal Detail

加入：

- exact provisions；
- precedent；
- evidence；
- procedural state；
- versions。

---

# 60. $L_A$：Machine / Audit Detail

加入完整：

- graph；
- certificates；
- routing；
- types；
- hashes；
- lineage。

---

# 61. Progressive Disclosure ≠ Withholding Rights

低層 UI 可以簡潔，

但 higher-detail routes 必須存在。

---

# 62. Semantic Loss Ledger

本文定義：

$$
\boxed{
\Lambda_H
=
(
\lambda_{\mathrm{omitted}},
\lambda_{\mathrm{collapsed}},
\lambda_{\mathrm{approx}},
\lambda_{\mathrm{unresolved}}
).
}
$$

---

# 63. Omitted

machine fields 未顯示，

但與當前 human query 無關。

---

# 64. Collapsed

多個 machine states 合成一個 human label。

---

# 65. Approx

精確 machine rule 轉成自然語言近似。

---

# 66. Unresolved

machine layer 本身也沒有答案。

---

# 67. 高風險 Collapse：Forbidden vs EvidenceMissing

ALD-03 已建立：

$$
\mathsf{Forbidden}
\neq
\mathsf{EvidenceMissing}.
$$

如果 human UI 都顯示：

> 不符合資格。

就產生：

$$
\boxed{
\text{Material Semantic Collapse}.
}
$$

---

# 68. 高風險 Collapse：Final vs Provisional

ALD-08 已建立 provisional successor。

如果 UI 把：

$$
\mathsf{ProvisionalSuccessor}
$$

寫成：

> 您就是唯一合法 successor。

同樣錯。

---

# 69. 高風險 Collapse：No Jurisdiction vs No Right

ALD-07 已建立：

$$
\mathsf{JurisdictionMismatch}
\neq
\mathsf{NoRight}.
$$

不能在 UI 中合併。

---

# 70. Distinction Preservation Set

本文提出：

$$
\boxed{
\mathcal D_{\mathrm{must}}
(q)
}
$$

列出 query 中不可被 human projection 壓縮掉的 distinctions。

---

# 71. Human Projection Test

對每個：

$$
d\in\mathcal D_{\mathrm{must}},
$$

驗證：

$$
\boxed{
\operatorname{Preserve}(d,\pi_H)=1.
}
$$

---

# 72. Projection Failure

若：

$$
\operatorname{Preserve}=0,
$$

應輸出：

$$
\mathsf{ProjectionUnsafe}.
$$

而不是發布錯誤人類介面。

---

# 73. Projection Drift

同一 canonical state 不變，

但 explanation generator 更新：

$$
M_1\rightarrow M_2.
$$

可能造成：

$$
\mathcal L_H^{(1)}
\neq
\mathcal L_H^{(2)}.
$$

---

# 74. Explanation Model 也需要 Version

$$
\boxed{
\nu_{\pi_H}.
}
$$

---

# 75. Human-Layer Regression Test

每次 projection model update，

都測：

- legal effect；
- deadlines；
- authority；
- appeal；
- uncertainty；

是否保留。

---

# 76. Human Explanation Hallucination

如果 source 沒有：

> 你被禁止是因為 X。

但 model 自行補出 X，

屬：

$$
\boxed{
\mathsf{LegalExplanationHallucination}.
}
$$

---

# 77. Explanation 必須 Source-Bound

$$
\boxed{
\mathcal E_H
\rightarrow
\mathcal S_{\mathrm{auth}}
+
K_L.
}
$$

---

# 78. European Legislation Identifier 的接口

ELI 提供：

- stable HTTP identifiers；
- legal metadata；
- machine-readable exchange；
- human / computer accessible legal resources。

這是：

$$
\boxed{
\text{shared legal resource identity}
}
$$

的重要基礎。

---

# 79. ELI 不等於 Dual Legal Interface Theory

本文不宣稱：

> ELI 已解決 semantic projection。

它主要解決：

- identification；
- metadata；
- interoperability；
- exchange。

---

# 80. Shared Legal Identifier

本文提出：

$$
\boxed{
ID(\mathcal L_H)
=
ID(\mathcal L_A)
=
ID(\mathcal L^\ast)
}
$$

至少在：

- source；
- legal resource；
- version；

層具有可驗證映射。

---

# 81. Same ID 不代表 Same Representation

$$
\boxed{
\text{Shared Identity}
\neq
\text{Shared Encoding}.
}
$$

---

# 82. Human / Machine Semantic Equivalence 不能用 Hash 證明

兩個不同語言 representations：

$$
hash(H)
\neq
hash(A).
$$

仍可能語義等價。

所以需要：

$$
\boxed{
\operatorname{VerifyEq}
(
\pi_H,
\pi_A,
\mathcal L^\ast,
\mathcal Q
).
}
$$

---

# 83. Legal Projection Equivalence

本文不要求：

$$
\mathcal L_H=\mathcal L_A.
$$

而要求：

> 對 material query family，答案與法律效果一致到必要程度。

---

# 84. Equivalence 也可以是 Partial

$$
\boxed{
\operatorname{EqStatus}
\in
\{
\mathsf{Preserved},
\mathsf{PartiallyPreserved},
\mathsf{Collapsed},
\mathsf{Reinterpreted},
\mathsf{Unmapped},
\mathsf{Unknown}
\}.
}
$$

---

# 85. Human Law 不能變成 Decorative Frontend

如果 machine law 真正控制：

- rights；
- money；
- access；

而 human law 只是一份漂亮 PDF，

則：

$$
\boxed{
\text{Human Layer}
=
\text{Decorative Legality}.
}
$$

這應被拒絕。

---

# 86. Machine Law 也不能變成 Secret Constitution

如果只有：

$$
\mathcal L_A
$$

實際決定結果，

而 human actors 無法查：

- rule；
- authority；
- version；
- appeal；

就出現：

$$
\boxed{
\text{Machine Constitutional Opacity}.
}
$$

---

# 87. 黑箱憲法問題

既有虛擬憲法研究已提出：

> 若制度只能由少數設計者理解、其他主體無法檢查，就不能進入全面授權。

ALD-09 把這條擴張到：

$$
\boxed{
\text{AI Legal Runtime}.
}
$$

---

# 88. Common Constitutional Interface（CCI）

本文提出：

$$
\boxed{
\mathcal C_{\mathrm{shared}}
=
(
Rights,
Authority,
Procedure,
Version,
Challenge,
Source,
Effect
).
}
$$

---

# 89. Rights

人類／AI interface 必須對同一 rights constraints 有可驗證 referent。

---

# 90. Authority

誰有權：

- 制定；
- 執行；
- 覆核。

不能只有 machine layer 知道。

---

# 91. Procedure

案件：

- pending；
- final；
- appealable；
- expired。

兩個界面不能不同步。

---

# 92. Version

$$
\nu_H
\leftrightarrow
\nu_A.
$$

---

# 93. Challenge

human / agent 都應知道合法 challenge route，

但 procedural rights 可以 carrier-relative。

---

# 94. Source

都回到：

$$
\mathcal S_{\mathrm{auth}}.
$$

---

# 95. Effect

同一 legal action 的 material effect 必須一致。

---

# 96. Common Constitutional Interface ≠ Same UI

人類可以：

- paragraphs；
- timeline；
- buttons；
- explanations。

AI 可以：

- JSON；
- graph；
- typed operators；
- certificates。

沒有問題。

---

# 97. Common Constitution ≠ Common Cognitive Format

$$
\boxed{
\text{Shared Constitution}
\neq
\text{Shared Representation Format}.
}
$$

---

# 98. Human Oversight 不是「找個人按確認」

EU AI Act 的 human oversight 方向要求：

> 人類能有效理解與監督系統。

所以：

$$
\boxed{
\text{Human Signature}
\neq
\text{Effective Human Oversight}.
}
$$

---

# 99. Rubber-Stamp Human 問題

如果 human reviewer：

- 看不懂 rule；
- 沒有時間；
- 無法 challenge；
- 只能按 approve；

則：

$$
\boxed{
\text{Nominal Human-in-the-Loop}
\neq
\text{Meaningful Oversight}.
}
$$

---

# 100. Human Oversight Capacity

本文提出：

$$
\boxed{
\mathbf H_O
=
(
H_{\mathrm{understand}},
H_{\mathrm{intervene}},
H_{\mathrm{challenge}},
H_{\mathrm{time}},
H_{\mathrm{authority}},
H_{\mathrm{evidence}}
).
}
$$

---

# 101. Oversight 必須 Match System Resolution

不是要求人類知道所有細節，

而是：

> 有能力取得必要投影與升級資訊。

---

# 102. Legal Drill-Down

human interface 應支援：

$$
\boxed{
\text{Summary}
\rightarrow
\text{Reason}
\rightarrow
\text{Rule}
\rightarrow
\text{Evidence}
\rightarrow
\text{Certificate}.
}
$$

---

# 103. Legal Drill-Up

AI / lawyer 也應能從 detailed graph 回到：

> 對 ordinary person 這到底意味著什麼？

---

# 104. Bidirectional Traceability

$$
\boxed{
\mathcal L_H
\leftrightarrow
\mathcal L^\ast
\leftrightarrow
\mathcal L_A.
}
$$

---

# 105. Human Intent Interface

一般人可能只問：

> 處理好了嗎？

這不是法律 query 的完整形式。

Runtime 可以展開：

$$
\boxed{
\text{Human Intent}
\rightarrow
\text{Legal Query Expansion}
\rightarrow
\text{LawEval}
\rightarrow
\text{Human Result}.
}
$$

---

# 106. 但 Intent Expansion 必須可看見

如果：

> 處理好了嗎？

被 AI 偷偷解讀為：

> 放棄申訴。

顯然不可接受。

所以：

$$
\boxed{
\text{Intent Expansion}
\text{ must not create hidden waiver}.
}
$$

---

# 107. High-Stakes Confirmation Surface

重大：

- waiver；
- settlement；
- asset transfer；
- rights surrender；

應要求更明確 human confirmation。

---

# 108. Simplification 不能製造 Consent

$$
\boxed{
\text{Simple UI}
\neq
\text{Informed Consent by Default}.
}
$$

---

# 109. Machine Interface 也需要 Human-Origin Constraints

如果 AI agent 代表 human principal，

其 machine-readable authority 應能追到：

- delegation；
- scope；
- expiry；
- revocation。

---

# 110. Human / AI Interface Symmetry 不是權利完全對稱

$$
\boxed{
\text{Interface Symmetry}
\neq
\text{Rights Identity}.
}
$$

ALD-02 已建立 carrier-relative semantics。

---

# 111. 人類與 AI 可以共享程序而不共享全部權利

例如：

- notice；
- proof；
- version；
- appeal structure；

可能共享。

但：

- bodily rights；
- subject welfare；
- corporate powers；

仍 carrier-relative。

---

# 112. Democratic Comprehensibility

本文定義最低：

$$
\boxed{
\operatorname{DemComp}(\mathcal L)
}
$$

不是：

> 每位 citizen 能背完整法典。

而是：

> 重大規範如何制定、誰有權、如何影響自己、如何反對，都有可理解公共接口。

---

# 113. Public Constitutional Surface

至少公開：

- authority allocation；
- protected rights；
- rule-change process；
- emergency powers；
- appeal / complaint；
- audit；
- major machine-law interfaces。

---

# 114. Public Surface 不等於 Full Security Disclosure

可以保留：

- security secrets；
- personal data；
- privileged information。

所以：

$$
\boxed{
\text{Transparency}
\neq
\text{Unlimited Disclosure}.
}
$$

---

# 115. Transparency 需要 Purpose-Typed

public：

- rules；
- authority；
- effect。

affected person：

- case basis；
- evidence；
- challenge。

auditor：

- logs；
- certificates。

machine：

- structured graph。

---

# 116. Projection Access Control

$$
\boxed{
\pi_{H,u}
}
$$

可依 legal role / privacy 給不同 detail，

但不能藉 access control 隱藏基本 challenge information。

---

# 117. Human Accessibility

Article 13 也把 accessible / comprehensible 明確放進資訊要求。

ALD-09 因此加入：

$$
\boxed{
\text{Legal Accessibility}
}
$$

而不是只有 semantic correctness。

---

# 118. Accessibility 包含

- language；
- disability access；
- reading level；
- timing；
- format；
- navigation。

---

# 119. Multi-Lingual Law

同一 canonical legal state 可有：

$$
\pi_{H,zh},
\pi_{H,en},
\pi_{H,fr}.
$$

---

# 120. 翻譯也需要 Semantic Witness

法律語言翻譯同樣可能 loss。

因此：

$$
\boxed{
\Gamma_{\mathrm{translation}}^{law}.
}
$$

---

# 121. AI 可以生成 Explanation，但不能自己改法律

$$
\boxed{
\operatorname{Explain}_{AI}
\neq
\operatorname{ModifyLaw}_{AI}.
}
$$

---

# 122. Explanation Correction

若 human explanation 錯，

應：

- correct；
- notify；
- preserve old version；
- identify affected decisions。

---

# 123. Explanation Version History

$$
\boxed{
H_{\pi_H}(t)
}
$$

也應 append-preserving。

---

# 124. Human Interface Can Be Wrong While Machine State Is Right

$$
\boxed{
\mathcal L_A=\text{correct}
\not\Rightarrow
\mathcal L_H=\text{correct}.
}
$$

---

# 125. Machine Interface Can Be Wrong While Human Text Is Right

反之：

$$
\boxed{
\mathcal L_H^{auth}=\text{correct}
\not\Rightarrow
\mathcal L_A=\text{correct}.
}
$$

---

# 126. Cross-View Consistency Monitor

本文提出：

$$
\boxed{
\operatorname{CrossViewCheck}
(
\mathcal L^\ast,
\mathcal L_H,
\mathcal L_A,
\mathcal Q
).
}
$$

---

# 127. Cross-View Failure Types

```text
SOURCE_MISMATCH
VERSION_MISMATCH
EFFECT_MISMATCH
AUTHORITY_MISMATCH
CHALLENGE_MISSING
UNCERTAINTY_COLLAPSE
FAILURE_TYPE_COLLAPSE
SEMANTIC_DRIFT
```

---

# 128. Common-Source but Different-Effect 是最危險 Bug

兩層都引用同一法條，

但 machine result 與 human explanation 不同。

這是：

$$
\boxed{
\text{Semantic Interface Failure}.
}
$$

---

# 129. No Material Human Consequence Without Projection

對高風險決定，

若：

$$
\pi_H
$$

無法安全生成，

較保守：

$$
\boxed{
\mathsf{Escalate}
}
$$

而不是：

$$
\mathsf{ExecuteOpaque}.
$$

---

# 130. Explainability Budget

不是所有低風險 operation 都需要十頁 explanation。

可以依 risk：

$$
\boxed{
B_E(q)
}
$$

調整 explanation depth。

---

# 131. 但 Minimum Rights Surface 不可低於底線

即使低 cost mode，

重大 human consequence 仍保留：

- effect；
- basis；
- challenge。

---

# 132. Projection Latency

human explanation 不能在：

> 已失去申訴期限之後

才生成。

所以：

$$
\boxed{
T_{\mathrm{projection}}
<
T_{\mathrm{challenge\ deadline}}
}
$$

是重要 procedural constraint。

---

# 133. Real-Time AI Law 需要 Real-Time Notice

如果 machine law 毫秒級改變 access，

human notice / appeal 系統不能延遲幾週。

---

# 134. Fast Law / Slow Constitution 接口

ALD-04 已建立：

$$
\text{Fast Adaptation}
\subset
\text{Slow Legitimate Boundary}.
$$

ALD-09 加：

$$
\boxed{
\text{Fast Machine Adaptation}
\rightarrow
\text{Human-Visible Version / Effect Change}.
}
$$

---

# 135. Silent Machine-Law Update 禁止

若 machine policy 版本變了，

影響人類權利，

但 human layer 沒更新，

形成：

$$
\boxed{
\mathsf{SilentNormativeDrift}.
}
$$

---

# 136. Precedent Graph Interface

ALD-06 的完整 graph 人類不必全看。

human view 可以：

> 此先例已被 2026 年某案在此命題上部分限制。

並提供 drill-down。

---

# 137. Jurisdiction Routing Interface

ALD-07 的 route 也可投影：

> 此案同時受 EU AI Act scope 與某國 contract law 影響；法院管轄尚待確認。

而不是塞十個 country codes。

---

# 138. Succession Interface

ALD-08 human layer：

> 您目前是 provisional successor；付款 authority 暫停，資產由 escrow 保全，可在 30 日內申請 review。

而不是顯示：

```json
{"succ_state":7,"auth":0,"asset":3}
```

---

# 139. Human Layer 必須保留 Provisionality

$$
\boxed{
\text{Provisional}
\neq
\text{Final}
}
$$

不可被 UX 省略。

---

# 140. Machine Layer 必須保留 Human Challenge State

如果 human 已 appeal：

$$
A_{\mathrm{appeal}}=1,
$$

machine executor 也要知道。

---

# 141. Human Challenge Must Propagate to Machine Runtime

$$
\boxed{
\operatorname{Appeal}_H
\rightarrow
\operatorname{StateUpdate}_{A}.
}
$$

否則 human interface 是假的。

---

# 142. Machine Evidence Update Must Propagate to Human Interface

新 evidence：

$$
E'
$$

改變 legal status，

human projection 必須更新。

---

# 143. Dual Interface 是 Bidirectional Coupling

不是：

$$
\text{Machine}
\rightarrow
\text{Human Dashboard}.
$$

而是：

$$
\boxed{
\text{Human Procedural Acts}
\leftrightarrow
\text{Machine Legal State}.
}
$$

---

# 144. Common Constitutional Interface 的目的

避免：

$$
\boxed{
\text{two legal realities}.
}
$$

---

# 145. 最終不是「人類法 vs AI 法」

而是：

$$
\boxed{
\text{one authoritative constitutional domain}
+
\text{heterogeneous legal interfaces}.
}
$$

---

# 146. 十六個核心非等價

$$
\boxed{
\text{Human-Readable}
\neq
\text{Machine-Readable}
}
$$

$$
\boxed{
\text{Machine-Readable}
\neq
\text{Legally Authoritative}
}
$$

$$
\boxed{
\text{Legal Projection}
\neq
\text{Free-Form Summary}
}
$$

$$
\boxed{
\text{Explanation}
\neq
\text{Chain-of-Thought}
}
$$

$$
\boxed{
\text{Complexity}
\neq
\text{Illegitimacy}
}
$$

$$
\boxed{
\text{Higher Machine Resolution}
\not\Rightarrow
\text{Lower Human Legal Standing}
}
$$

$$
\boxed{
\text{Human Signature}
\neq
\text{Effective Human Oversight}
}
$$

$$
\boxed{
\text{Nominal Human-in-the-Loop}
\neq
\text{Meaningful Oversight}
}
$$

$$
\boxed{
\text{Shared Constitution}
\neq
\text{Shared Representation Format}
}
$$

$$
\boxed{
\text{Transparency}
\neq
\text{Unlimited Disclosure}
}
$$

$$
\boxed{
\text{Simple UI}
\neq
\text{Informed Consent}
}
$$

$$
\boxed{
\text{Shared Legal ID}
\neq
\text{Shared Encoding}
}
$$

$$
\boxed{
\text{Current Machine State}
\neq
\text{Automatically Correct Human Explanation}
}
$$

$$
\boxed{
\text{Human Explanation}
\neq
\text{Authority Source}
}
$$

$$
\boxed{
\text{AI Explanation}
\neq
\text{AI Legislative Authority}
}
$$

$$
\boxed{
\text{Human Interface}
\neq
\text{Decorative Frontend}.
}
$$

---

# 147. 八個工程測試

## 147.1 Forbidden / EvidenceMissing Projection Test

machine states 不同，

human UI 不得都顯示「不允許」。

## 147.2 Provisional / Final Test

ALD-08 provisional successor 不得被壓成 final successor。

## 147.3 Version Drift Test

machine law 更新、human explanation 尚未更新。

Runtime 應標 stale / block material consequence。

## 147.4 Appeal Propagation Test

human 提出 appeal，

machine enforcement state 必須同步。

## 147.5 Article-86-Style Explanation Test

對符合指定高風險決定條件的模擬案例，

介面必須能輸出 AI role + main decision elements + challenge route。

## 147.6 Source Trace Test

任一 plain-language claim 必須能 drill down 到 source / version。

## 147.7 Projection Model Regression Test

更換 explanation model 後，

material distinctions 不得丟失。

## 147.8 Accessibility Test

同一 legal consequence 提供 plain / professional / accessible / machine views，

法律效果與申訴入口必須一致。

---

# 148. 可反駁點

## 148.1 Human-Comprehensible 是相對概念

不同人：

- education；
- language；
- disability；
- legal expertise；

不同。

所以需要 progressive / adaptive interface，而不是單一 readability score。

## 148.2 Explanation Overload

太多資訊也可能降低理解。

因此本文採 minimum sufficient + drill-down。

## 148.3 Projection Can Never Be Perfect

自然語言壓縮總可能丟失細節。

本文不要求 lossless full equivalence，而要求 query-specific semantic preservation + explicit loss。

## 148.4 Legal Source Models Differ

某些 jurisdictions 的 authoritative sources / precedent roles 不同。

 $\mathcal L^\ast$ 必須 jurisdiction-relative。

## 148.5 Security / Privacy Limits

某些資料不能公開。

因此 contestability 必須與 lawful disclosure limits 一起設計。

## 148.6 Human Oversight Can Become Symbolic

即使 UI 完善，institutional time / authority 不足仍可能造成 rubber-stamping。

需要程序與資源配套。

---

# 149. 與最後一篇的接口

下一篇也是本系列封頂篇：

## ALD-10｜雙法律棧：人類法律、AI 法律域與「處理好了嗎？」的文明接口

ALD-09 已建立：

$$
\mathcal L^\ast
\xrightarrow{\pi_H}
\mathcal L_H,
$$

$$
\mathcal L^\ast
\xrightarrow{\pi_A}
\mathcal L_A.
$$

最後一篇將把整個系列收束成：

$$
\boxed{
\mathfrak L
=
\mathfrak L_H
\oplus
\mathfrak L_A
\oplus
\mathfrak L_{HA}.
}
$$

並正式研究：

$$
\boxed{
\text{Human Intent}
\rightarrow
\text{Legal Expansion}
\rightarrow
\text{Execution}
\rightarrow
\text{Human Result}.
}
$$

也就是普通人未來可能只問：

> 「處理好了嗎？」

而底層其實已完成：

- identity；
- authority；
- jurisdiction；
- precedent；
- succession；
- proof；
- compliance；
- appeal-state；

等巨大法律閉包。

---

# 150. 結論

AI 原生法律最容易走向兩個極端。

第一個極端：

> 為了讓人類理解，把所有法律重新壓回幾個簡單按鈕。

結果失去：

- uncertainty；
- jurisdiction；
- exception；
- authority；
- appeal；
- provenance。

第二個極端：

> 既然 AI 看得懂高維法律圖，人類就不需要理解。

結果法律變成：

$$
\boxed{
\text{Machine-Only Normative Infrastructure}.
}
$$

本文拒絕兩者。

真正需要的是：

$$
\boxed{
\text{One Canonical Legal State}
+
\text{Multiple Typed Projections}
+
\text{Semantic Preservation}
+
\text{Bidirectional Procedural Coupling}.
}
$$

所以：

$$
\boxed{
\mathcal L^\ast
\xrightarrow{\pi_H}
\mathcal L_H,
\qquad
\mathcal L^\ast
\xrightarrow{\pi_A}
\mathcal L_A.
}
$$

人類版可以短，

AI 版可以深，

但：

- source 不能分裂；
- rights 不能分裂；
- authority 不能分裂；
- effect 不能分裂；
- appeal 不能分裂。

因此本文最重要的憲政原則是：

$$
\boxed{
\text{No Material Human Consequence}
\text{ without a Human-Comprehensible Legal Projection and Challenge Route}.
}
$$

而整篇最後可以壓成：

$$
\boxed{
\text{人類不需要讀懂機器法律的每一個欄位；}
}
$$

$$
\boxed{
\text{但任何會改變人類法律地位的機器法律，都必須能把「為什麼、依什麼、誰決定、如何反對」重新投影回人類世界。}
}
$$

也就是：

$$
\boxed{
\text{AI 可以擁有更高解析的法律介面，}
}
$$

$$
\boxed{
\text{但不能因此擁有一個人類無法理解、無法挑戰、無法追溯的祕密憲法。}
}
$$

---

# 參考文獻

1. OECD. *Consultation on the digital provision of law: Towards a shared reference framework for Law as Code*. Public consultation, 29 July 2026 – 30 April 2027.
2. European Union. Regulation (EU) 2024/1689, Artificial Intelligence Act, Article 13, Article 14, Article 86.
3. Council of Europe. *Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law*, CETS No. 225.
4. Council of Europe. *Handbook on Human Rights and Artificial Intelligence*, 2026 materials on procedural safeguards and human oversight.
5. European Union / EUR-Lex. *European Legislation Identifier (ELI)* specifications and training materials.
6. Neo.K. 《虛擬憲法：從方向性錨點到候選制度實現》v0.1, 2026.
7. Neo.K. 《AI 時代的法律編譯層：人類法律、機器法律與認知落差》v0.1, 2026.
8. Neo.K × Aletheia. 《ALD-03｜法律函數不是 Boolean：部分算子、證書、裁量與失敗語義》v0.1, 2026.
9. Neo.K × Aletheia. 《ALD-06｜活的判例圖：AI 原生先例、異議、推翻與法律推理網路》v0.1, 2026.
10. Neo.K × Aletheia. 《ALD-07｜Juridical Routing：分散式 AI 的跨法域選擇與法律路由》v0.1, 2026.
11. Neo.K × Aletheia. 《ALD-08｜動態忒修斯的法律繼受：Fork、Merge、Restore 與未決身份下的責任》v0.1, 2026.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- Human-Readable / Machine-Readable / Legally Authoritative 明確分離
- canonical legal state 與 human / AI projections 明確分離
- projection 不是 free-form summary；需 preserve / loss / source / version / challenge / certificate
- Material Human Consequence Principle 明確標為本文候選憲政原則，不冒充全球現行法
- EU AI Act Article 13 / 14 / 86 僅作現行透明、oversight、explanation 法律錨點，Article 86 不被誇大為 universal right
- Council of Europe Framework Convention 僅作 contestability / remedies / safeguards 現實錨點
- ELI 僅作 shared legal resource identity / interoperability 錨點，不宣稱其已解決 semantic projection
- human explanation 不要求模型 chain-of-thought
- semantic loss ledger 明確保存 omitted / collapsed / approximate / unresolved
- appeal / challenge 由 human interface 回寫 machine legal state
- Common Constitutional Interface 不要求 human / AI 使用相同 representation format
