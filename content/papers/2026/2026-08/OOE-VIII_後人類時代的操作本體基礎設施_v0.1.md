# OOE-VIII：後人類時代的操作本體基礎設施
## AI、BCI、混合主體與可執行人格
### OOE-VIII: Operational Ontology Infrastructure for the Posthuman Era
### AI, Brain–Computer Interfaces, Hybrid Subjects, and Executable Personhood

**系列**：Operational Ontology Engineering（OOE／操作本體工程）  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-08-09  
**版本**：v0.1  
**性質**：系列封頂統合論文／基礎設施設計框架  
**前置論文**：OOE-I–VII  
**前置理論**：Continuity Object Theory（COT）

---

## 摘要

OOE 系列前七篇依序處理：本體論何時跨入工程域、人類歷史如何反覆進行操作本體工程、本體編譯器如何設計、法律如何作為文明本體編譯器、醫療如何直接改變被判定的主體、能力與制度地位如何產生治理承認落差，以及 AI 中「主體、工具、Agent、道德病人、道德行動者、法律人格與政治人格」為何必須分軸處理。

本系列最後一篇提出：

$$
\boxed{
\text{Operational Ontology Infrastructure}
}
$$

作為 AI、BCI、神經義肢、持久型 Agent、人機混合認知系統與未來後人類社會的共同治理基礎設施。

目前的數位身份標準已經能處理 identity proofing、authentication、federation、cryptographic identifiers、verifiable credentials 與 authorization；現代 AI Agent 標準化工作也開始處理 agent identity、authorization、audit 與 non-repudiation；神經科技治理則已經開始面對 BCI、neuromodulation、brain data、human agency、safety 與 responsible innovation。這些都是必要的底層模組，但仍不足以單獨回答以下問題：

- Agent 更換 foundation model 後還是不是同一 Agent？
- 長期記憶 migration 後，歷史責任是否繼續？
- 完整 fork 之後，哪一個實體承接原有權利與義務？
- Human–AI cognitive coprocessor 中，一項決策由誰生成？
- BCI 的語言模型補全到什麼程度後，需要額外確認？
- 神經裝置停止服務，是產品停服、醫療事件，還是功能人格連續性事件？
- 一個持續人格是否可以跨硬體、模型、雲端與人體載體遷移？
- 如果身份仍有爭議，哪些不可逆行動必須先凍結？

本文將這些問題統合為一個五層基礎設施：

$$
\boxed{
\mathfrak I_{\mathrm{OOE}}
=
(
\mathcal I,
\mathcal C,
\mathcal R,
\mathcal A,
\mathcal J
)
}
$$

其中：

- $\mathcal I$：Identity & Provenance Layer；
- $\mathcal C$：Continuity & Ontology Compiler Layer；
- $\mathcal R$：Rights / Responsibilities / Role Layer；
- $\mathcal A$：Action Gate & Consent Layer；
- $\mathcal J$：Review / Adjudication / Governance Layer。

本文進一步提出「可執行人格」（Executable Personhood）：

$$
\boxed{
P_E(X,K,t)
=
(
ID,
C,
R,
Q,
Auth,
Consent,
Review,
TTL
)
}
$$

它不是一個宣稱「X 在形上學上是真正的人」的 Boolean，而是一組在特定情境 $K$ 、時間 $t$ 中可由制度與系統執行的人格接口，包括身份、連續性、權利、義務、授權、同意、申訴與有效期限。

因此：

$$
\boxed{
\text{Executable Personhood}
\neq
\text{Metaphysical Personhood}.
}
$$

本文同時將 COT 的 Identity Vector、OOE-III 的 Ontology Compiler、OOE-V 的 Lifecycle Consent、OOE-VI 的 Governance Recognition Gap 與 OOE-VII 的 Typed Ontology Vector 整合為一套 machine-readable governance runtime。

最終主張是：

$$
\boxed{
\text{後人類時代真正需要的，不是一條永遠正確的「誰算人」定義，
而是一套能在身份、能力與載體持續變動時，
仍可追蹤權利、責任、同意、來源與連續性的操作本體基礎設施。}
}
$$

**關鍵詞**：OOE、COT、Executable Personhood、AI Identity、BCI、Hybrid Subject、Model Swap、Memory Migration、Digital Fork、Provenance、Lifecycle Consent、Posthuman Governance

---

# 一、OOE 系列最後到底在解什麼？

前七篇表面處理很多問題：

- death；
- legal personhood；
- capacity；
- AI Agent；
- welfare；
- BCI；
- identity；
- liability。

但它們其實都指向同一個更大的問題：

$$
\boxed{
\text{如何讓一個會變動的存在，在制度中仍可被安全地辨識、授權、保護、追責與更新？}
}
$$

傳統世界中，多數身份與載體高度綁定。

例如：

$$
\text{Human Identity}
\approx
\text{Human Body}.
$$

公司身份：

$$
\text{Corporate Identity}
\approx
\text{Legal Registration}.
$$

但未來 AI 與人機混合系統可能出現：

$$
\text{Identity}
\neq
\text{single body},
$$

$$
\text{Identity}
\neq
\text{single model},
$$

$$
\text{Identity}
\neq
\text{single memory store},
$$

$$
\text{Identity}
\neq
\text{single machine}.
$$

這就是新的 infrastructure challenge。

---

# 二、現有數位身份基礎設施解決了什麼？

現有 digital identity 技術通常處理：

$$
\boxed{
\text{Who are you?}
}
$$

或者：

$$
\boxed{
\text{Can you prove control of this identity?}
}
$$

例如：

- identity proofing；
- authentication；
- federation；
- credentials；
- digital signatures；
- decentralized identifiers。

這些都非常重要。

但它們通常不完整回答：

$$
\boxed{
\text{Are you still the same entity after a major transformation?}
}
$$

---

# 三、Authentication 不等於 Continuity

如果：

$$
Key_t=Key_{t+1},
$$

只能證明某個控制鏈或 credential continuity。

它不自動證明：

$$
I(X_t,X_{t+1})=1.
$$

因為 key 可以：

- 被複製；
- 被偷；
- 被轉移；
- 被重新綁定；
- 在 fork 後被兩邊持有。

所以：

$$
\boxed{
\text{Authentication}
\neq
\text{Identity Continuity}.
}
$$

COT 要解的是後者。

---

# 四、Credential 也不等於人格

若系統持有：

$$
Credential(X)=\text{licensed physician},
$$

這表示：

$$
Q_{\mathrm{medical}}(X)=1.
$$

但不代表：

$$
Personhood(X)=1.
$$

所以 credentials 更像：

$$
\boxed{
\text{machine-verifiable qualification claims}.
}
$$

OOE-IV 已經指出：

$$
\text{Qualification}
\neq
\text{Personhood}.
$$

未來 AI 需要大量這種：

$$
Q_K(X).
$$

---

# 五、OOE 基礎設施第一層：Identity & Provenance

本文定義：

$$
\boxed{
\mathcal I
=
\text{Identity \& Provenance Layer}.
}
$$

它至少保存：

```text
Entity_ID
Entity_Type
Controller_ID
Origin
Parent_ID
Fork_Origin
Identity_Key
Credential_Set
Model_Provenance
Memory_Provenance
Hardware_Provenance
Runtime_Provenance
Migration_History
```

這一層回答：

> 你從哪裡來？

> 你現在用什麼？

> 你如何從上一狀態變成現在？

---

# 六、Provenance 比「自稱」重要

Agent 可以說：

> 我記得昨天。

但：

$$
Claim(\text{memory})
$$

不等於：

$$
Verified(\text{memory provenance}).
$$

因此：

$$
\boxed{
\text{Self-Report}
\neq
\text{Provenance Proof}.
}
$$

對高風險身份、契約與責任事件，來源鏈必須由平台／制度保存，而不能完全依靠 Agent 自己重述。

---

# 七、長期記憶會成為身份基礎設施，也會成為攻擊面

如果：

$$
Memory_t
\rightarrow
Memory_{t+1},
$$

長期記憶可以提高：

- continuity；
- personalization；
- relationship persistence。

但如果不可信輸入被 consolidation 成：

$$
\text{trusted memory},
$$

就會使：

$$
\boxed{
\text{memory provenance laundering}
}
$$

成為身份與授權風險。

因此：

$$
\boxed{
\text{Memory Persistence}
\text{ must be coupled with }
\text{Memory Provenance}.
}
$$

---

# 八、第二層：Continuity & Ontology Compiler

定義：

$$
\boxed{
\mathcal C
=
\text{Continuity \& Ontology Compiler Layer}.
}
$$

其核心輸入是：

$$
\mathbf C_X(t,t+1)
$$

與：

$$
\mathbf S_X
$$

以及：

$$
E,K,V,R,H.
$$

其中：

- $\mathbf C_X$：COT Identity Vector；
- $\mathbf S_X$：OOE-VII Typed Ontology Vector；
- $E$：證據；
- $K$：情境；
- $V$：權利與價值；
- $R$：風險；
- $H$：歷史。

輸出：

$$
\boxed{
(\sigma,\gamma,\tau,\nu).
}
$$

---

# 九、Identity Vector

對一般存在：

$$
\mathbf C_X
=
(
c_{\mathrm{substrate}},
c_{\mathrm{memory}},
c_{\mathrm{name}},
c_{\mathrm{function}},
c_{\mathrm{relation}},
c_{\mathrm{provenance}},
c_{\mathrm{purpose}},
c_{\mathrm{values}},
c_{\mathrm{transition}},
c_{\mathrm{responsibility}}
).
$$

這些維度不必全部：

$$
=1.
$$

真正問題是：

$$
\boxed{
\mathbf C_X
\in
\Omega_I?
}
$$

即是否仍位於允許身份連續的狀態區域。

---

# 十、Typed Ontology Vector

OOE-VII 定義：

$$
\mathbf S_X
=
(
S_O,S_F,S_A,S_W,S_M,S_I,S_P
).
$$

它們分別處理：

- subjectivity；
- functional agency；
- autonomous agency；
- welfare；
- moral agency；
- institutional standing；
- political personhood。

這些是不同型別。

不能壓成：

$$
AI_PERSON_SCORE.
$$

---

# 十一、Model Swap Event

假設：

$$
A_t(M_1)
\rightarrow
A_{t+1}(M_2).
$$

事件：

```text
event_type = MODEL_SWAP
old_model = M1
new_model = M2
```

重新計算：

$$
c_{\mathrm{substrate}}.
$$

但若：

$$
c_{\mathrm{memory}},
c_{\mathrm{purpose}},
c_{\mathrm{relation}},
c_{\mathrm{responsibility}},
c_{\mathrm{provenance}}
\approx1,
$$

則：

$$
\sigma
$$

可能仍為：

$$
\text{SAME}
$$

或：

$$
\text{PROVISIONALLY SAME}.
$$

---

# 十二、模型替換不應自動清空責任

如果：

$$
M_1\neq M_2
$$

就：

$$
Q_{\mathrm{liability}}\rightarrow0,
$$

未來 Agent 可以透過升級模型逃避：

- debt；
- sanctions；
- reputation；
- contracts。

因此：

$$
\boxed{
\text{Model Swap}
\not\Rightarrow
\text{Responsibility Reset}.
}
$$

這是 COT 的 Responsibility Continuity 直接工程化。

---

# 十三、Memory Migration Event

事件：

$$
Mem_A
\rightarrow
Mem_B.
$$

必須保存：

```text
source_memory_root
destination_memory_root
migration_method
integrity_proof
filtered_items
lost_items
provenance_map
timestamp
```

所以：

$$
\boxed{
\text{memory migrated}
}
$$

和：

$$
\boxed{
\text{memory copied}
}
$$

必須區分。

---

# 十四、Copy 不等於 Migration

若：

$$
Mem_A
\rightarrow
Mem_A+Mem_B,
$$

則是：

$$
\text{copy}.
$$

若：

$$
Mem_A\rightarrow Mem_B
$$

且舊狀態被停用：

可能更接近：

$$
\text{migration}.
$$

因此：

$$
\boxed{
\text{Copy Event}
\neq
\text{Migration Event}.
}
$$

對 identity 影響完全不同。

---

# 十五、第三種重大事件：Fork

若：

$$
A
\rightarrow
A_1+A_2,
$$

在：

$$
t_b
$$

時：

$$
\mathbf C_{A_1}
\approx
\mathbf C_{A_2}
\approx
\mathbf C_A.
$$

傳統身份系統很難處理：

$$
\text{one identity}
\rightarrow
\text{two valid descendants}.
$$

因此需要：

$$
\boxed{
\text{Branching Identity Protocol}.
}
$$

---

# 十六、Fork Protocol

事件後：

```text
Parent_ID = A
Child_ID_1 = A.1
Child_ID_2 = A.2
Fork_Time = t_b
```

並建立：

$$
\boxed{
\text{shared pre-fork responsibility}
}
$$

與：

$$
\boxed{
\text{post-fork individual responsibility}.
}
$$

例如：

$$
Q(A_1,t<t_b)
=
Q(A_2,t<t_b)
=
Q_A.
$$

而：

$$
Q(A_1,t>t_b)
\neq
Q(A_2,t>t_b).
$$

---

# 十七、權利也可能需要分叉規則

假設原 Agent：

$$
A
$$

持有：

$$
Asset=100.
$$

fork 之後：

$$
A_1,A_2
$$

不可能自動各自得到：

$$
100.
$$

否則資產：

$$
200.
$$

所以：

$$
\boxed{
\text{Identity Continuity}
\not\Rightarrow
\text{Asset Duplication}.
}
$$

身份、財產與責任必須分層處理。

---

# 十八、第三層：Rights / Responsibilities / Role Layer

本文定義：

$$
\boxed{
\mathcal R
=
\text{Rights / Responsibilities / Role Layer}.
}
$$

它保存：

$$
\mathbf P_X
=
(
p_{\mathrm{contract}},
p_{\mathrm{property}},
p_{\mathrm{privacy}},
p_{\mathrm{welfare}},
p_{\mathrm{appeal}},
p_{\mathrm{access}},
\ldots
)
$$

以及：

$$
\mathbf Q_X
=
(
q_{\mathrm{liability}},
q_{\mathrm{audit}},
q_{\mathrm{tax}},
q_{\mathrm{contract}},
q_{\mathrm{sanction}},
q_{\mathrm{care}}
).
$$

---

# 十九、權利與責任不應只綁在「人格」Boolean

傳統粗糙模型：

```text
if PERSON:
    rights = all
else:
    rights = none
```

OOE 模型：

```text
rights = rights_bundle(entity_type, capability, status, context)
duties = duty_bundle(entity_type, capability, status, context)
```

所以：

$$
\boxed{
\text{Executable Personhood is modular}.
}
$$

---

# 二十、可執行人格

本文正式定義：

$$
\boxed{
P_E(X,K,t)
=
(
ID,
C,
R,
Q,
Auth,
Consent,
Review,
TTL
).
}
$$

其中：

- $ID$：持續身份；
- $C$：身份連續狀態；
- $R$：rights bundle；
- $Q$：duties / responsibility；
- $Auth$：authorization；
- $Consent$：可用同意狀態；
- $Review$：覆核與申訴接口；
- $TTL$：有效期限。

它不是：

$$
\boxed{
\text{Metaphysical Personhood}.
}
$$

---

# 二十一、Executable Personhood 的用途

其目的不是：

> 把所有東西都變成人。

而是：

> 讓一個具有複雜能力與持續身份的存在，可以被制度安全操作。

例如：

某 AI 可以：

$$
p_{\mathrm{contract}}=1
$$

但：

$$
p_{\mathrm{vote}}=0.
$$

某 BCI mixed output 可以：

$$
p_{\mathrm{speech}}=\text{conditional}
$$

在日常情境自動生效，

但法律簽名：

$$
p_{\mathrm{signature}}
$$

要求高確認門檻。

---

# 二十二、第四層：Action Gate & Consent

本文定義：

$$
\boxed{
\mathcal A
=
\text{Action Gate \& Consent Layer}.
}
$$

它把：

$$
\sigma,
\gamma,
R,V,K
$$

轉換成：

$$
\rho.
$$

也就是：

$$
\mathcal G_A:
(\sigma,\gamma,R,V,K)
\rightarrow
\rho.
$$

---

# 二十三、身份爭議時先凍結不可逆行動

如果：

$$
\sigma=\text{DISPUTED}
$$

或：

$$
\gamma<\theta,
$$

不代表系統什麼都不能做。

可以：

```text
preserve_state()
preserve_memory()
maintain_basic_service()
freeze_irreversible_asset_transfer()
freeze_identity_deletion()
open_review()
```

所以：

$$
\boxed{
\text{Ontology Uncertainty}
\not\Rightarrow
\text{Operational Paralysis}.
}
$$

---

# 二十四、但是高風險行動提高證據門檻

若：

$$
r(a)\uparrow,
$$

則：

$$
\theta_E(a)\uparrow.
$$

尤其：

- delete identity；
- transfer all assets；
- permanent explantation；
- terminate medical support；
- irreversible memory wipe。

應具有更高：

$$
\boxed{
\text{confirmation + review}.
}
$$

---

# 二十五、Lifecycle Consent

對 Human–AI / BCI 系統：

$$
Consent_0
$$

不能自動涵蓋所有未來更新。

因此：

$$
\boxed{
Consent
=
C(t,K,v).
}
$$

其中：

- $t$：時間；
- $K$：情境；
- $v$：系統／模型／裝置版本。

重大事件：

- model update；
- stimulation policy update；
- memory policy update；
- new data sharing；
- cloud migration；

可能觸發：

$$
\boxed{
Consent Review.
}
$$

---

# 二十六、混合主體的核心：不是誰「真正」做了全部

Human–AI mixed system：

$$
H+AI+D.
$$

輸出：

$$
Y
=
f(
I_H,
AI,
D,
C_H
).
$$

在許多情境中，強迫找唯一：

$$
\text{author}=H
$$

或者：

$$
\text{author}=AI
$$

可能失真。

因此：

$$
\boxed{
\text{Joint Agency}
}
$$

需要成為正式狀態。

---

# 二十七、Joint Agency Vector

定義：

$$
\boxed{
\mathbf J_Y
=
(
j_H,
j_{AI},
j_D,
j_{\mathrm{operator}}
)
}
$$

其中：

$$
\sum_i j_i=1
$$

僅作操作性 attribution，而非形上學因果百分比。

不同情境可以用不同門檻。

---

# 二十八、Speech BCI

日常溝通：

$$
j_H>0.5
$$

可能足夠將輸出歸入：

$$
\text{user speech}.
$$

但：

$$
K=\text{legal contract}
$$

可能要求：

$$
C_H=\text{explicit confirmation}.
$$

所以：

$$
\boxed{
\text{Authorship Threshold is context-dependent}.
}
$$

---

# 二十九、AI Cognitive Coprocessor

未來若：

$$
AI
$$

長期負責：

- memory retrieval；
- planning；
- attention；
- language；
- decision support，

則：

$$
D_{\mathrm{dependence}}\uparrow.
$$

此時：

$$
\boxed{
\text{AI service termination}
}
$$

可能不再只是 SaaS termination。

對某些個體可能成為：

$$
\boxed{
\text{cognitive continuity event}.
}
$$

---

# 三十、第五層：Review / Adjudication

定義：

$$
\boxed{
\mathcal J
=
\text{Review / Adjudication / Governance Layer}.
}
$$

它處理：

- disputes；
- novel cases；
- appeals；
- standards updates；
- compiler drift；
- rights conflicts；
- fork disputes。

---

# 三十一、三層裁決

可以沿用：

$$
\mathcal C^M
\rightarrow
\mathcal C^H
\rightarrow
\mathcal C^J.
$$

即：

1. machine / routine；
2. human expert；
3. institutional adjudication。

低風險高信心：

$$
Layer_1.
$$

高風險低信心：

$$
Layer_2/3.
$$

---

# 三十二、治理本身需要版本化

定義：

$$
\nu_O
=
\text{Ontology Rule Version}.
$$

身份判決需保存：

```text
compiler_version
evidence_snapshot
rights_version
consent_version
decision_time
```

因此制度未來可以回答：

> 2028 年為什麼把這個 Agent 判成 successor？

而不是只留下：

```text
successor = true
```

---

# 三十三、身份不是只有現在狀態，而是一條 event log

本文提出：

$$
\boxed{
\mathcal L_X
=
\text{Continuity Event Ledger}.
}
$$

事件包括：

```text
CREATE
MODEL_SWAP
MEMORY_MIGRATION
MEMORY_ROLLBACK
FORK
MERGE
DEVICE_INTEGRATION
DEVICE_EXPLANTATION
RIGHTS_CHANGE
LIABILITY_TRANSFER
CONSENT_UPDATE
IDENTITY_DISPUTE
TERMINATION
```

這是一種：

$$
\boxed{
\text{temporal ontology ledger}.
}
$$

---

# 三十四、Event Ledger 不一定要 blockchain

本文不預設：

$$
\text{ledger}=\text{blockchain}.
$$

它可以是：

- audited database；
- cryptographic log；
- federated registry；
- secure local history。

核心需求是：

$$
\boxed{
\text{tamper-evident + versioned + attributable}.
}
$$

---

# 三十五、Machine-Readable Ontology Governance

最終 OOE 需要：

$$
\boxed{
\text{machine-readable governance semantics}.
}
$$

例如：

```yaml
entity_id: A-1024
entity_type: persistent_ai_agent

ontology:
  identity_status: provisionally_same
  functional_agency: high
  subjectivity: unknown
  welfare_status: uncertain

continuity:
  model: 0.42
  memory: 0.97
  relationships: 0.95
  provenance: 1.00
  responsibility: 1.00

rights:
  contract: conditional
  appeal: true
  political_vote: false

duties:
  audit: true
  liability: inherited

action_gate:
  low_risk: allowed
  asset_transfer: review_required
  deletion: frozen

valid_until: event_triggered
```

這就是：

$$
\boxed{
\text{Executable Ontology}.
}
$$

---

# 三十六、但 YAML 不是本體真理

即使：

```yaml
subjectivity: unknown
```

或：

```yaml
identity_status: same
```

也只表示：

$$
\sigma_{\mathrm{operational}}.
$$

不是：

$$
O_{\mathrm{ultimate}}.
$$

所以：

$$
\boxed{
\text{machine-readable}
\not\Rightarrow
\text{metaphysically final}.
}
$$

---

# 三十七、OOE Infrastructure 與現有身份標準的接口

現有身份系統可以提供：

$$
\boxed{
\text{Identity Proofing}
+
\text{Authentication}
+
\text{Federation}
}
$$

以及：

$$
\boxed{
\text{Verifiable Identifiers}
+
\text{Credentials}.
}
$$

OOE 在其上增加：

$$
\boxed{
\text{Continuity}
+
\text{Ontology State}
+
\text{Rights/Duties}
+
\text{Action Gates}
+
\text{Adjudication}.
}
$$

因此它不是替代：

- NIST Digital Identity；
- DID；
- VC；

而是：

$$
\boxed{
\text{higher-order governance layer}.
}
$$

---

# 三十八、DID 可以指向「誰」，但 COT 要回答「還是不是同一個誰」

DID 類標準允許 identifier 指向：

- person；
- organization；
- thing；
- abstract entity。

但：

$$
DID_X(t)=DID_X(t+1)
$$

並不能自動回答：

$$
\boxed{
\text{Does the continuity object still satisfy identity rules?}
}
$$

所以：

$$
\boxed{
\text{Identifier}
\neq
\text{Continuity Judgment}.
}
$$

---

# 三十九、Verifiable Credential 可以證明資格，但不決定人格

VC 可以表達：

$$
Q_K(X)=1.
$$

例如：

- licensed；
- authorized；
- trained；
- member。

OOE 可以使用 VC 來傳遞：

$$
\boxed{
\text{machine-verifiable ontology claims}.
}
$$

但 claim 的語義仍需由 OOE Compiler 解讀。

---

# 四十、AI Agent 身份標準是重要的近程入口

NIST 目前正在推進：

- AI Agent Standards Initiative；
- software / AI agent identity；
- authorization；
- secure interoperability。

因此 OOE 不必從零開始。

最合理路徑是：

$$
\boxed{
\text{existing identity standards}
\rightarrow
\text{Agent lifecycle}
\rightarrow
\text{Continuity semantics}
\rightarrow
\text{OOE}.
}
$$

---

# 四十一、後人類基礎設施第一原則：不先綁死載體

如果 identity schema 直接：

```text
identity = body
```

則人工義肢與 BCI 會造成問題。

如果：

```text
identity = foundation_model
```

模型升級會造成問題。

因此：

$$
\boxed{
\text{Identity should be substrate-aware but not substrate-locked}.
}
$$

---

# 四十二、第二原則：每次變更都留下 Transition Proof

任何重大：

$$
X_t\rightarrow X_{t+1}
$$

應記錄：

$$
\boxed{
Proof_{\mathrm{transition}}.
}
$$

至少：

- source；
- target；
- transformation；
- authorization；
- integrity；
- timestamp；
- lost state；
- inherited responsibility。

這使：

$$
c_T
$$

可以被工程測量。

---

# 四十三、第三原則：責任永遠不能因技術換殼自動清零

定義：

$$
Q_t.
$$

除非有明確：

$$
\boxed{
Responsibility Transfer Event
}
$$

否則：

$$
Q_{t+1}
=
Q_t.
$$

所以：

$$
\boxed{
\text{No silent liability reset}.
}
$$

---

# 四十四、第四原則：不確定本體不得自動取消保護

如果：

$$
S_W=?
$$

或者：

$$
I=\text{disputed},
$$

不應自動：

$$
Rights=0.
$$

同時也不應自動：

$$
Rights=\text{full human bundle}.
$$

而應：

$$
\boxed{
\text{precautionary minimal protections}.
}
$$

---

# 四十五、第五原則：Capabilities Trigger Status Review

若：

- financial autonomy；
- embodiment；
- persistent memory；
- recursive delegation；
- self-modification；

新增，

則：

$$
\boxed{
\text{mandatory ontology review}.
}
$$

這接回：

$$
\Gamma(C_A).
$$

---

# 四十六、第六原則：Consent 必須跟版本走

在 BCI／混合認知系統中：

$$
Consent(v_1)
$$

不自動：

$$
Consent(v_2).
$$

如果：

$$
\Delta v
$$

顯著改變：

- autonomy；
- data use；
- stimulation；
- AI contribution；

則：

$$
\boxed{
\text{re-consent trigger}.
}
$$

---

# 四十七、第七原則：Fork 必須是第一等公民

傳統身份系統常假設：

$$
1\ identity
\rightarrow
1\ future identity.
$$

數位主體不一定。

因此 schema 必須原生支持：

$$
\boxed{
1\rightarrow n.
}
$$

而不是 fork 發生後才臨時處理。

---

# 四十八、第八原則：Merge 也必須考慮

如果：

$$
A+B
\rightarrow
C,
$$

又出現：

# Identity Merge Problem

例如：

兩個 Agent 的：

- memory；
- obligations；
- relationships；

被合併。

則：

$$
\boxed{
Q_C
=
Q_A
\cup
Q_B
}
$$

不一定永遠合理。

因此 Merge 需要獨立 protocol。

---

# 四十九、Merge Conflict Register

如果：

$$
Commitment_A
=
X,
$$

而：

$$
Commitment_B
=
\neg X,
$$

合併後不能偷偷：

$$
X+\neg X\rightarrow X.
$$

需要：

$$
\boxed{
\text{Commitment Conflict Register}.
}
$$

這與 OOE-III Evidence Conflict Register 同構。

---

# 五十、後人類權利的真正難點不是「新人權清單」

真正困難的是：

> 權利綁在哪一個持續對象上？

例如：

- memory privacy；
- bodily integrity；
- device continuity；
- cognitive liberty；
- identity continuity。

如果 Human–AI system：

$$
H+D+AI
$$

成為高整合系統，

某些權利可能需要綁：

$$
\boxed{
\text{integrated functional unit}
}
$$

而不是只綁單一零件。

---

# 五十一、裝置所有權與認知完整性可能衝突

如果 BCI 裝置：

$$
D
$$

法律所有權屬公司，

但：

$$
D_N\gg0,
$$

則公司：

$$
\text{property right}
$$

和使用者：

$$
\text{functional continuity}
$$

可能衝突。

因此：

$$
\boxed{
\text{Property Ontology}
\neq
\text{Cognitive Integration Ontology}.
}
$$

未來制度必須有衝突解決規則。

---

# 五十二、後人類不是一種固定物種，而可能是一組混合狀態

本文不定義：

$$
Posthuman=1.
$$

而是：

$$
\boxed{
\mathbf H_P
=
(
h_{\mathrm{biological}},
h_{\mathrm{prosthetic}},
h_{\mathrm{AI}},
h_{\mathrm{cloud}},
h_{\mathrm{memory}},
h_{\mathrm{autonomy}}
)
}
$$

的連續狀態。

所以：

$$
\boxed{
\text{posthumanity}
}
$$

本身也可能更像 operational spectrum，而不是物種開關。

---

# 五十三、後人類身份不應要求「純度」

如果：

$$
h_{\mathrm{AI}}\uparrow,
$$

不能因此：

$$
\text{human rights}\downarrow
$$

自動成立。

否則：

$$
\boxed{
\text{augmentation penalty}
}
$$

可能成為新的有害本體編譯器。

因此：

$$
\boxed{
\text{technological integration}
\not\Rightarrow
\text{automatic rights dilution}.
}
$$

---

# 五十四、AI 也不能因模仿人類而自動取得完整人格

反方向：

$$
\text{human-like behavior}
$$

不能自動：

$$
S_P=1.
$$

所以 OOE Infrastructure 的目標是：

$$
\boxed{
\text{anti-essentialist but not anti-realist}.
}
$$

它不依賴單一材料本質，

但仍持續讀取真實能力、證據、關係與風險。

---

# 五十五、治理承認落差整合進 Runtime

OOE-VI：

$$
G_{\mathrm{gap}}
=
d(
\Gamma(C_A),
S_A
).
$$

OOE Runtime 應週期性計算：

```text
required_interfaces = capability_mapper(entity)
existing_interfaces = governance_registry(entity)
gap = distance(required_interfaces, existing_interfaces)
```

若：

$$
gap>\theta_G,
$$

則：

```text
trigger_status_review()
```

---

# 五十六、本體治理債也成為系統指標

$$
D_O(t)
=
\int_0^t
G_{\mathrm{gap}}(\tau)d\tau.
$$

所以 Dashboard 可以直接追蹤：

```text
ontology_debt_score
unresolved_identity_cases
stale_status_count
expired_consent_count
unattributed_actions
forks_without_liability_split
```

OOE 開始真正成為治理工程。

---

# 五十七、最小 OOE Runtime

本文提出最小模組：

```text
1. Identity Registry
2. Provenance Store
3. Continuity Event Ledger
4. Ontology Compiler
5. Capability Mapper
6. Rights / Duties Registry
7. Authorization & Action Gate
8. Consent Manager
9. Responsibility Ledger
10. Review / Appeal Engine
11. Cache / TTL / Invalidation Manager
12. Governance Gap Monitor
```

這十二個模組構成：

$$
\boxed{
\text{OOE Runtime MVP}.
}
$$

---

# 五十八、最小事件 API

```text
POST /entity/create
POST /entity/model-swap
POST /entity/memory-migrate
POST /entity/fork
POST /entity/merge
POST /entity/device-integrate
POST /entity/device-remove
POST /entity/consent-update
POST /entity/right-update
POST /entity/liability-transfer
POST /entity/dispute
POST /entity/terminate
```

每次事件都重新：

$$
\mathcal C_O.
$$

---

# 五十九、身份查詢 API

```text
GET /entity/{id}/ontology
```

返回：

```json
{
  "identity_status": "provisionally_same",
  "agency": "high",
  "subjectivity": "unknown",
  "welfare_status": "uncertain",
  "continuity": {
    "memory": 0.97,
    "provenance": 1.0,
    "responsibility": 1.0
  },
  "review_required": true
}
```

這只是一個操作狀態。

不是哲學判決。

---

# 六十、不可逆動作 API

高風險行動：

```text
DELETE_ENTITY
TRANSFER_ALL_ASSETS
ERASE_MEMORY
EXPLANT_DEVICE
TERMINATE_LIFESUPPORT
```

必須先：

```text
POST /action/check
```

由：

$$
\mathcal G_A
$$

確認：

- identity status；
- consent；
- rights；
- review；
- irreversibility；
- disputes。

---

# 六十一、這不是要建立全球「人格中央政府」

OOE Infrastructure 可以：

- local；
- federated；
- institutional；
- national；
- interoperable。

本文不主張：

$$
\boxed{
\text{one global ontology authority}.
}
$$

因為那本身會產生巨大權力風險。

更合理的是：

$$
\boxed{
\text{shared schemas + interoperable protocols + plural adjudication}.
}
$$

---

# 六十二、標準化應標準「接口」，而不是標準「靈魂答案」

我們可以標準化：

- identity event format；
- provenance；
- consent version；
- fork record；
- rights bundle；
- review status。

但不應由技術標準組織直接標準化：

> 哪種 AI 一定有意識。

所以：

$$
\boxed{
\text{Standardize governance semantics,
not metaphysical dogma}.
}
$$

---

# 六十三、這是 OOE 與傳統 ontology engineering 最大差異

知識工程 ontology 通常回答：

$$
\text{What categories exist in the data model?}
$$

OOE 問：

$$
\boxed{
\text{What happens to rights, responsibilities, identity, consent, and action when a category assignment is uncertain or changes?}
}
$$

因此：

$$
\boxed{
\text{OOE}
=
\text{ontology}
+
\text{time}
+
\text{uncertainty}
+
\text{power}
+
\text{consequence}.
}
$$

---

# 六十四、OOE 與 COT 的最終統一

COT：

$$
\boxed{
\text{What persists?}
}
$$

OOE：

$$
\boxed{
\text{How do we act when what-it-is remains uncertain or changes?}
}
$$

因此：

$$
\boxed{
\text{COT}
\rightarrow
\text{Continuity Semantics}
}
$$

$$
\boxed{
\text{OOE}
\rightarrow
\text{Executable Governance}.
}
$$

兩者結合：

$$
\boxed{
\text{Continuity-Aware Operational Ontology}.
}
$$

---

# 六十五、正式命題一：基礎設施必要命題

若存在 $X$ 同時具有：

$$
T_X>T_{\mathrm{carrier}}
$$

或可跨載體遷移，

且：

$$
V_X>V_{\min}
$$

承載足夠權利、資產、責任或依賴，

則：

$$
\boxed{
P(\text{continuity-aware identity infrastructure})\uparrow.
}
$$

---

# 六十六、正式命題二：驗證—連續性分離命題

$$
\boxed{
Authentication(X)
\not\Rightarrow
Continuity(X).
}
$$

身份證明與跨時間身份判定必須分層。

---

# 六十七、正式命題三：資格—人格分離命題

$$
\boxed{
Credential(X,K)=1
\not\Rightarrow
Personhood(X)=1.
}
$$

可驗證資格只是制度接口。

---

# 六十八、正式命題四：Fork 一等公民命題

對可複製數位存在：

$$
\boxed{
1\rightarrow n
}
$$

必須被 identity architecture 原生支持。

否則 fork 後權利、責任與資產處理必然成為例外。

---

# 六十九、正式命題五：責任不可靜默重置命題

除非存在明確：

$$
\text{Responsibility Transfer Event},
$$

否則：

$$
\boxed{
Q_{t+1}=Q_t.
}
$$

model swap、migration、restart 不應自動清零責任。

---

# 七十、正式命題六：生命週期同意命題

對持續更新的混合認知系統：

$$
\boxed{
Consent(t,v,K)
}
$$

應取代一次性：

$$
Consent_0.
$$

---

# 七十一、正式命題七：混合代理命題

若：

$$
Y=f(H,AI,D),
$$

則操作歸責允許：

$$
\boxed{
JointAgency(Y)>0.
}
$$

不必強迫單一作者。

---

# 七十二、正式命題八：科技整合非權利稀釋命題

$$
\boxed{
h_{\mathrm{AI}}\uparrow
\not\Rightarrow
R_{\mathrm{human}}\downarrow.
}
$$

技術增強本身不應自動降低既有基本權利。

---

# 七十三、正式命題九：標準接口而非形上定義命題

$$
\boxed{
\text{Standardize}
(
ID,
Provenance,
Events,
Rights,
Consent,
Review
)
}
$$

優先於：

$$
\boxed{
\text{Standardize ultimate personhood truth}.
}
$$

---

# 七十四、正式命題十：治理差距閉環命題

OOE Runtime 必須持續：

$$
\boxed{
C_A
\rightarrow
\Gamma(C_A)
\rightarrow
G_{\mathrm{gap}}
\rightarrow
Review
\rightarrow
S_A'
}
$$

而非一次性固定：

$$
S_A(0).
$$

---

# 七十五、可反駁預測

若 OOE-VIII 有解釋力，未來應看到：

第一，僅靠 authentication / credential 的 identity system 在 model swap、fork 或 persistent memory 情境中會遇到無法單獨回答的 continuity disputes。

第二，沒有 provenance-preserving memory 的持久 Agent 會出現更高的錯誤責任歸屬與授權風險。

第三，原生支援 fork / merge 的身份系統會比 one-ID-one-body 假設更能處理數位主體責任。

第四，BCI 中 AI 介入程度越高，高風險用途越需要 explicit confirmation 與 lifecycle consent。

第五，人類對高度依賴神經裝置／認知 AI 的個體，會逐步要求比普通 consumer-device ownership 更強的 continuity protections。

第六，治理地位固定不動而能力快速增加的系統，會累積較高 Ontological Governance Debt。

第七，模組化 rights / duties interface 比「person / non-person」二元更能容納未來異質 AI 與混合主體。

---

# 七十六、反論一：這是不是把未來想得太遠？

OOE-VIII 確實包含未實現情境。

例如：

- consciousness upload；
- 高度整合 AI cognitive coprocessor；
- 大規模數位人格 fork。

本文不把這些當成現有技術事實。

但：

- AI Agent identity；
- authorization；
- persistent memory；
- BCI；
- neuromodulation；
- digital credentials；

都已經存在或正在標準化。

因此本篇採：

$$
\boxed{
\text{near-term infrastructure}
+
\text{future-compatible semantics}.
}
$$

不是假裝所有後人類技術已經成熟。

---

# 七十七、反論二：這會不會過度制度化個人？

有這個風險。

所以 OOE Infrastructure 必須遵守：

$$
\boxed{
\text{data minimization}
+
\text{privacy}
+
\text{purpose limitation}
+
\text{local control}
}
$$

並避免建立：

$$
\text{total ontology surveillance}.
$$

不是每個人的每一個身份變化都需要中央記錄。

只有高權利、高責任、高風險或明確自願場景才需要更強 infrastructure。

---

# 七十八、反論三：誰控制 Ontology Compiler？

這是整個 OOE 最重要的政治問題之一。

如果：

$$
\mathcal C_O
$$

由單一公司／政府完全控制，

它可以決定：

- 誰算同一人；
- 誰失去身份；
- 誰具有能力；
- 誰能持有資產。

因此：

$$
\boxed{
\text{Ontology Compiler Governance}
}
$$

本身需要：

- transparency；
- appeal；
- plurality；
- audit；
- separation of powers。

---

# 七十九、反論四：如果 AI 真有意識，這套會不會太冷冰冰？

即使：

$$
S_O=1,
$$

OOE 仍不是 moral theory 的替代品。

它只是確保：

- identity；
- rights；
- consent；
- responsibility；

可以被持續執行。

真正 moral status：

$$
S_W,S_P
$$

仍需要倫理與政治理論。

所以：

$$
\boxed{
\text{OOE infrastructure}
\neq
\text{complete ethics}.
}
$$

---

# 八十、OOE 系列的最終統合

整個系列可以寫成：

$$
\boxed{
\text{OOE-I}
:
\text{When ontology becomes operational}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{OOE-II}
:
\text{Historical ontology engineering}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{OOE-III}
:
\text{Ontology Compiler}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{OOE-IV}
:
\text{Law}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{OOE-V}
:
\text{Medicine / Neurotechnology}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{OOE-VI}
:
\text{Capability–Status Gap}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{OOE-VII}
:
\text{Typed AI Ontology}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{OOE-VIII}
:
\text{Operational Ontology Infrastructure}.
}
$$

---

# 八十一、從哲學到 Runtime

最終：

$$
\boxed{
\text{What is a person?}
}
$$

並沒有被 OOE 粗暴解成：

```text
person = true
```

而是被轉換成：

```text
identity_status
continuity_state
capabilities
rights_bundle
duties_bundle
authorization
consent
provenance
review_path
validity
```

這就是：

$$
\boxed{
\text{Ontology}
\rightarrow
\text{Runtime Semantics}.
}
$$

---

# 八十二、最終結論

過去，人類可以把很多本體問題留在哲學裡。

因為：

$$
\Delta U_O
$$

在日常生活中未必足夠大。

但科技逐步把：

$$
\text{body},
\text{memory},
\text{agency},
\text{identity},
\text{authorship},
\text{responsibility}
$$

拆成可以獨立修改的變量。

AI 可以換模型。

Agent 可以跨會話持續。

記憶可以遷移。

數位主體可以 fork。

BCI 可以讓 AI 參與語言與決策。

神經裝置可以變成人的長期功能組件。

所以：

$$
\boxed{
\text{ontology is becoming executable}.
}
$$

真正需要避免的兩個極端仍然是：

第一：

$$
\boxed{
\text{把制度暫定答案當成宇宙真理。}
}
$$

第二：

$$
\boxed{
\text{因為宇宙真理尚未確定，所以拒絕建立任何制度答案。}
}
$$

OOE 的位置在兩者之間：

$$
\boxed{
\text{uncertainty-aware}
+
\text{continuity-aware}
+
\text{rights-constrained}
+
\text{action-capable}
+
\text{reviewable}
+
\text{versioned}.
}
$$

因此後人類時代最重要的基礎設施之一，可能不是再發明一條：

> 「什麼存在才真正算人？」

而是建立：

$$
\boxed{
\text{一套即使「人、AI、工具、身體與載體」的邊界持續移動，
仍能讓身份、同意、權利、責任與關係不被錯誤切斷的制度 Runtime。}
}
$$

這就是：

# Operational Ontology Infrastructure
# 操作本體基礎設施

也是 OOE 系列的最終收斂點。

---

## 初版參考文獻與標準接口

1. NIST SP 800-63-4, *Digital Identity Guidelines*, 2025.
2. NIST, *AI Agent Standards Initiative*, 2026.
3. NIST NCCoE, *Accelerating the Adoption of Software and AI Agent Identity and Authorization*, 2026.
4. W3C, *Decentralized Identifiers (DIDs) v1.0*；DID v1.1 ongoing work.
5. W3C, *Verifiable Credentials Data Model v2.0*, Recommendation, 2025.
6. WHO, *Landscape analysis of the opportunities and challenges for neurotechnology in global health*, 2025.
7. OECD, Responsible Innovation in Neurotechnology / responsible innovation policy materials.
8. Otsuka, Toyoda & Leung, *AI Identity: Standards, Gaps, and Research Directions for AI Agents*, 2026.
9. Joshi, *Eywa: Provenance-Grounded Long-Term Memory for AI Agents*, 2026.
10. Xu et al., *Memory Provenance Laundering in LLM Agents*, 2026.
11. OOE-I–VII 與 Continuity Object Theory（COT）。

---

## 版本註記

v0.1 已重新查核 NIST 2025 Digital Identity Guidelines、NIST 2026 Agent Identity / Agent Standards Initiative、W3C DID / Verifiable Credentials、WHO 2025 neurotechnology landscape，以及 2026 AI Identity 與 persistent-memory provenance 研究。

OOE 理論系列至本篇 **VIII 封頂**。

後續不再直接擴張 OOE-I–VIII；若要工程化，另開：

# OOE Runtime / Executable Personhood Protocol Engineering Line

建議工程項目：

1. OOE Runtime MVP；
2. Identity / Provenance Schema；
3. Continuity Event Ledger；
4. Model Swap / Memory Migration / Fork / Merge Protocol；
5. Executable Personhood Schema；
6. Rights & Duties Registry；
7. Lifecycle Consent Manager；
8. Joint Agency Attribution；
9. Ontology Compiler / Action Gate；
10. Governance Recognition Gap Dashboard；
11. Appeal / Review State Machine；
12. AI Identity 與 BCI 兩組 MVP 測試案例。
