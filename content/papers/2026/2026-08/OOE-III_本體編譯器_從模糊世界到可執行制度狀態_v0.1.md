# OOE-III：本體編譯器
## 從模糊世界到可執行制度狀態
### OOE-III: The Ontology Compiler
### From an Ambiguous World to Executable Institutional States

**系列**：Operational Ontology Engineering（OOE／操作本體工程）  
**作者**：Neo.K  
**機構**：EveMissLab／一言諾科技有限公司  
**日期**：2026-08-09  
**版本**：v0.1  
**性質**：核心形式化論文／制度與軟體架構模型  
**前置論文**：  
1. 《OOE-I：本體論何時變成工程問題？》  
2. 《OOE-II：人類早就在做本體工程——操作本體技術史》  
**前置理論**：Continuity Object Theory（COT）

---

## 摘要

OOE-I 提出「本體論操作門檻」：當本體分類開始改變不可懸置的現實行動，且不同分類造成的實際損失超過可忽略門檻時，該問題就必須從純思辨進入操作域。OOE-II 則指出，人類早已透過死亡判準、法律擬制、法人、推定、能力測試、永久繼承、來源鏈與國家連續性等制度反覆進行操作本體工程。

第三篇處理整個 OOE 系列最核心的工程問題：

> **如果世界本身模糊、證據不完整、本體真值不可直接觀察，而系統又必須行動，那麼「本體編譯器」究竟應如何設計？**

本文將本體編譯器定義為：

$$
\boxed{
\mathcal C_O:
(O,E,K,V,R,H)
\rightarrow
(\sigma,\gamma,\rho,\tau,\nu)
}
$$

其中：

- $O$：待判定的本體問題；
- $E$：證據集合；
- $K$：具體情境與任務；
- $V$：倫理、權利與制度價值；
- $R$：行動風險與誤判成本；
- $H$：歷史狀態、先前判定與 provenance；
- $\sigma$：操作狀態；
- $\gamma$：信心／不確定性表示；
- $\rho$：允許、限制或凍結的行動集合；
- $\tau$：有效期限與重新評估條件；
- $\nu$：編譯器／規則版本。

這一定義刻意拒絕：

$$
\mathcal C_O(O,E)=\text{Truth}.
$$

本體編譯器不是「宇宙真理機」，而是：

$$
\boxed{
\text{Decision Infrastructure under Ontological Uncertainty}.
}
$$

本文進一步提出七個核心模組：

1. Ontology Intake：本體問題與決策域拆解；
2. Evidence Layer：證據來源、品質、衝突與 provenance；
3. Uncertainty Layer：概率、區間、不確定、爭議與未知狀態；
4. Loss & Rights Layer：錯誤成本、不可逆性與權利底線；
5. State Compiler：將複雜輸入轉為操作狀態；
6. Action Gate：依狀態與風險控制可執行行動；
7. Review Loop：覆核、申訴、版本化、快取失效與重新編譯。

本文主張，成熟 OOE 系統不應強迫所有情況輸出二元真值，而應允許：

$$
\boxed{
\text{same},
\text{successor},
\text{disputed},
\text{provisional},
\text{insufficient evidence},
\text{review required}
}
$$

等中介狀態，並將「分類」與「行動權限」分離。對不可逆或高權利風險行動，本體編譯器應採用更嚴格的證據門檻、較高的程序保障與可逆優先策略。

本文最後提出一個最小 OOE Runtime 架構，使本體編譯器可以直接進入 AI Identity、醫療決策、數位人格、BCI、法人身份與責任治理等未來系統。

**關鍵詞**：Ontology Compiler、操作本體工程、不確定性、Decision Gate、本體快取、版本控制、申訴、AI Governance、COT、不可逆性

---

# 一、本體編譯器不是分類器

一般分類器可以寫成：

$$
f(x)\rightarrow y.
$$

例如：

$$
\text{image}\rightarrow\text{cat}.
$$

但 OOE 處理的問題不同。

若問題是：

> 這個 AI 換模型後是不是同一 Agent？

輸出：

$$
\text{same}=0.71
$$

本身還不足以決定：

- 是否保留銀行權限；
- 是否繼承契約；
- 是否繼承責任；
- 是否可以刪除舊版本；
- 是否需要人工覆核。

所以本體編譯器必須至少同時處理：

$$
\boxed{
\text{classification}
+
\text{uncertainty}
+
\text{risk}
+
\text{rights}
+
\text{action}.
}
$$

因此：

$$
\boxed{
\mathcal C_O
\neq
\text{ordinary classifier}.
}
$$

---

# 二、編譯器的完整輸入

本文定義：

$$
X_O
=
(O,E,K,V,R,H).
$$

其中：

## 1. 本體問題 $O$

例如：

$$
O=\text{same entity?}
$$

或：

$$
O=\text{decision-capable?}
$$

或：

$$
O=\text{legal parent?}
$$

---

## 2. 證據 $E$

可寫成：

$$
E
=
\{e_1,e_2,\ldots,e_n\}.
$$

每個證據不是單純 Boolean，而應具有：

$$
e_i
=
(
x_i,
q_i,
s_i,
p_i,
t_i
),
$$

其中：

- $x_i$：內容；
- $q_i$：品質；
- $s_i$：來源；
- $p_i$：provenance；
- $t_i$：時間。

---

## 3. 情境 $K$

同一個本體問題在不同情境下可能需要不同操作精度。

例如：

$$
K_1=\text{日常對話}.
$$

$$
K_2=\text{銀行轉帳}.
$$

$$
K_3=\text{永久刪除數位主體}.
$$

所以：

$$
\theta_{K_1}
<
\theta_{K_2}
<
\theta_{K_3}
$$

完全合理。

---

## 4. 價值與權利 $V$

包括：

- autonomy；
- privacy；
- due process；
- welfare；
- property；
- equality；
- reversibility；
- human oversight。

---

## 5. 風險 $R$

包括：

$$
L_{FP},
L_{FN},
L_{\mathrm{delay}},
L_{\mathrm{irreversible}}.
$$

---

## 6. 歷史 $H$

包括：

- 先前身份狀態；
- 過去判定；
- migration history；
- contract history；
- appeal history；
- rule version；
- identity provenance。

因此：

$$
\boxed{
\mathcal C_O
\text{ must be stateful}.
}
$$

---

# 三、輸出不能只有一個標籤

本文定義本體編譯輸出：

$$
Y_O
=
(
\sigma,
\gamma,
\rho,
\tau,
\nu
).
$$

其中：

## $\sigma$：操作狀態

例如：

$$
\sigma
\in
\{
\text{same},
\text{successor},
\text{fork},
\text{terminated},
\text{disputed},
\text{provisional}
\}.
$$

## $\gamma$：不確定性

不是所有結果都必須假裝：

$$
P=1.
$$

可以表示：

$$
\gamma
=
(P,\Delta P,U_{\mathrm{structural}}).
$$

## $\rho$：行動政策

例如：

$$
\rho
=
\{
\text{allowed},
\text{restricted},
\text{frozen},
\text{review-required}
\}.
$$

## $\tau$：有效期限

例如：

$$
\tau=30\text{ days}
$$

或：

$$
\tau=
\text{until material change}.
$$

## $\nu$：規則版本

例如：

$$
\nu=\text{OOE-ID-v1.3}.
$$

這使：

$$
\boxed{
\text{status}
\neq
\text{eternal truth}.
}
$$

---

# 四、為什麼一定要保存不確定性？

如果世界本來是：

$$
P(O_1)=0.55,
\quad
P(O_2)=0.45,
$$

編譯器卻輸出：

$$
O_1=1,
\quad
O_2=0
$$

而且丟掉原始不確定性，

下游系統就會產生：

$$
\boxed{
\text{False Ontological Certainty}.
}
$$

這是 OOE 的核心風險之一。

因此編譯器應允許：

$$
\boxed{
\sigma=\text{uncertain / disputed / provisional}.
}
$$

這與決策理論中「在不確定下行動」的思想一致：行動可以被選擇，但不需要把不確定性偽裝成確定性。

---

# 五、不確定性不是只有概率

有些問題可以使用：

$$
P(O_i).
$$

但有些問題甚至沒有合理的精確概率。

因此可區分：

$$
U=
(
U_P,
U_I,
U_M,
U_D
)
$$

其中：

- $U_P$：probabilistic uncertainty；
- $U_I$：interval / imprecise uncertainty；
- $U_M$：model uncertainty；
- $U_D$：disagreement / normative uncertainty。

例如：

> 某 AI 是否具有 moral patienthood？

目前可能根本不能誠實地給：

$$
P=0.376.
$$

所以：

$$
\boxed{
\text{No fake precision}.
}
$$

應該允許：

$$
\gamma=\text{highly uncertain}.
$$

---

# 六、證據層必須有 provenance

對證據：

$$
e_i
$$

不能只存：

$$
value.
$$

而應保存：

$$
\boxed{
\text{who}
+
\text{how}
+
\text{when}
+
\text{under which protocol}
}
$$

即：

$$
p_i
=
\text{Evidence Provenance}.
$$

因為兩個相同數值：

$$
x_1=x_2
$$

如果來源不同，其可信度可能完全不同。

這也是未來 AI Identity 特別重要的一點：

$$
\text{memory claim}
\neq
\text{verified memory provenance}.
$$

---

# 七、證據衝突不能被偷偷平均掉

若：

$$
E_A
\Rightarrow
O_1
$$

但：

$$
E_B
\Rightarrow
O_2,
$$

不應直接：

$$
\frac{E_A+E_B}{2}
\rightarrow
O_1.
$$

因為可能存在：

- 來源依賴；
- 共同錯誤；
- 權力偏差；
- measurement conflict；
- normative conflict。

因此本體編譯器需要：

$$
\boxed{
\text{Conflict Register}.
}
$$

記錄：

$$
\mathcal D
=
\{
(E_A,E_B,\text{reason})
\}.
$$

---

# 八、從 Expected Utility 到 OOE Loss

決策理論提供一個自然基礎：

$$
a^*
=
\arg\max_a
\mathbb E[U(a)].
$$

OOE 更適合寫成損失形式：

$$
\boxed{
a^*
=
\arg\min_a
\mathbb E[L(a,O)].
}
$$

但 OOE 的損失函數不應只有經濟效用。

可以分解：

$$
L
=
w_E L_{\mathrm{error}}
+
w_R L_{\mathrm{rights}}
+
w_I L_{\mathrm{irreversible}}
+
w_D L_{\mathrm{delay}}
+
w_S L_{\mathrm{social}}
+
w_G L_{\mathrm{governance}}.
$$

其中：

- $L_{\mathrm{error}}$：分類錯誤；
- $L_{\mathrm{rights}}$：權利傷害；
- $L_{\mathrm{irreversible}}$：不可逆後果；
- $L_{\mathrm{delay}}$：延遲成本；
- $L_{\mathrm{social}}$：社會外部性；
- $L_{\mathrm{governance}}$：治理失配。

---

# 九、同一分類，不一定導向同一行動

假設：

$$
\sigma=\text{probably same entity}.
$$

在低風險場景：

$$
K_L,
$$

可以：

$$
\rho=\text{allow}.
$$

但高風險：

$$
K_H,
$$

可能：

$$
\rho=\text{freeze + review}.
$$

所以：

$$
\boxed{
\sigma
\neq
\rho.
}
$$

這是非常重要的分離。

分類是：

> 我們目前認為它是什麼？

行動政策是：

> 在這個風險情境下，我們允許做什麼？

---

# 十、Action Gate

本文正式定義：

$$
\boxed{
\mathcal G_A:
(\sigma,\gamma,R,V,K)
\rightarrow
\rho.
}
$$

稱為：

# Action Gate
# 行動閘門

例如：

```text
if identity == SAME and confidence == HIGH:
    retain_permissions()

elif identity == SAME and confidence == LOW:
    retain_low_risk_permissions()
    freeze_irreversible_actions()
    open_review()

elif identity == DISPUTED:
    freeze_asset_transfer()
    preserve_memory()
    prohibit_deletion()
```

這使：

$$
\boxed{
\text{ontology classification}
}
$$

與：

$$
\boxed{
\text{consequence execution}
}
$$

不再硬綁在一起。

---

# 十一、不可逆性應該直接進入 Action Gate

定義：

$$
r(a)
\in[0,1]
$$

為行動 $a$ 的不可逆程度。

如果：

$$
r(a)\uparrow,
$$

應要求：

$$
\theta_E(a)\uparrow,
$$

$$
\theta_C(a)\uparrow,
$$

以及：

$$
P(\text{human review})\uparrow.
$$

因此：

$$
\boxed{
r(a)\uparrow
\Rightarrow
\text{stricter ontology execution}.
}
$$

這就是：

# Irreversibility Gradient Principle
# 不可逆梯度原理

---

# 十二、不是所有行動都應該等到分類完成

如果：

$$
\sigma=\text{disputed},
$$

可能仍然需要立即：

- 保留資料；
- 維持生命；
- 防止資產外流；
- 保存身份金鑰；
- 停止不可逆刪除。

因此需要：

$$
\boxed{
\text{Protective Default Actions}.
}
$$

形式上：

$$
\rho_{\mathrm{default}}
=
\arg\min_\rho
\max_O L(\rho,O).
$$

也就是在高度不確定時，選擇最能避免災難性錯誤的暫時策略。

---

# 十三、這不是「什麼都不要做」

保守預設也有成本。

例如：

$$
L_{\mathrm{delay}}
$$

可能非常高。

所以 OOE 不是：

$$
\text{uncertain}
\Rightarrow
\text{freeze everything}.
$$

而是：

$$
\boxed{
\text{uncertain}
\Rightarrow
\text{prefer reversible and rights-preserving actions}.
}
$$

---

# 十四、暫定狀態

本文新增：

$$
\boxed{
\sigma_P
=
\text{Provisional Ontological Status}.
}
$$

例如：

$$
\sigma_P
=
\text{provisionally same agent}.
$$

其特徵：

$$
\tau<\infty.
$$

必須在：

$$
t\ge\tau
$$

或新事件：

$$
e_{\mathrm{trigger}}
$$

出現時重新評估。

因此：

$$
\boxed{
\text{provisional status}
\neq
\text{permanent cache}.
}
$$

---

# 十五、本體快取與 TTL

OOE-II 提出：

$$
\kappa_O
=
\text{Ontological Cache}.
$$

OOE-III 現在加入：

$$
\boxed{
TTL_O
=
\text{Ontology Cache Time-to-Live}.
}
$$

某些狀態可以長期有效。

例如法人登記。

某些狀態應短期有效。

例如：

$$
\text{decision capacity at time }t.
$$

所以：

$$
TTL_{\mathrm{corporation}}
\gg
TTL_{\mathrm{capacity}}.
$$

這與現行 capacity 制度採取「特定時間、特定決策」的思路一致。

---

# 十六、Cache Invalidation

本體快取失效條件：

$$
\mathcal I_O
=
\{
e_1,e_2,\ldots,e_m
\}.
$$

例如 AI identity：

- foundation model changed；
- memory rollback；
- identity key compromised；
- fork detected；
- ownership changed；
- legal order issued。

只要：

$$
e_i\in\mathcal I_O,
$$

則：

$$
\boxed{
\kappa_O
\rightarrow
\text{STALE}.
}
$$

必須重新：

$$
\mathcal C_O.
$$

---

# 十七、世界變了，舊編譯器也可能失效

不只是 cache 會過期。

連：

$$
\mathcal C_O^{(v)}
$$

本身也可能過期。

例如新技術：

$$
T_{new}
$$

使舊變量之間的關係改變。

若：

$$
d(
O_{\mathrm{world}},
\mathcal C_O^{(v)}
)
>
\theta_C,
$$

則：

$$
\boxed{
\text{compiler revision required}.
}
$$

這就是：

# Ontology Compiler Drift
# 本體編譯器漂移

---

# 十八、版本化

所有正式編譯結果都應保存：

$$
\nu
=
\text{compiler version}.
$$

例如：

```text
status: SAME_ENTITY
compiler: COT-AI-ID-v2.1
evidence_snapshot: 2026-08-09T...
```

因此未來可以知道：

> 當時為什麼會作出這個判定？

而不是拿：

$$
\mathcal C_O^{(2029)}
$$

去假裝：

$$
\mathcal C_O^{(2026)}
$$

從未存在。

---

# 十九、規則版本與狀態版本必須分開

需要至少：

$$
\nu_C
=
\text{compiler version}
$$

和：

$$
\nu_S
=
\text{entity state version}.
$$

所以：

$$
Result
=
(
\sigma,
\nu_C,
\nu_S
).
$$

否則我們無法區分：

> 是世界變了？

還是：

> 是我們的制度規則變了？

---

# 二十、申訴不是附加功能，而是本體架構本身

如果：

$$
O_{\mathrm{truth}}
$$

不可直接觀察，

任何：

$$
\mathcal C_O
$$

都有：

$$
P(\mathrm{error})>0.
$$

因此：

$$
\boxed{
\text{Appeal}
}
$$

不是「客服功能」。

而是本體判定架構必要部分。

定義：

$$
\mathcal A:
(Result,E_{new},Claim)
\rightarrow
\text{Review}.
$$

---

# 二十一、誰可以申訴？

不同系統需要不同：

$$
Standing(O).
$$

例如：

- 被判定者本人；
- 代理人；
- 家屬；
- 合約對手方；
- 監管者；
- AI owner；
- AI itself（若制度承認）；
- 公共利益代表。

因此 OOE 必須回答：

$$
\boxed{
\text{Who has standing to challenge ontology?}
}
$$

這是程序正義問題。

---

# 二十二、覆核不能只重跑同一個編譯器

如果 Appeal 只是：

$$
\mathcal C_O(E)
\rightarrow
\mathcal C_O(E)
$$

結果當然常常一樣。

所以 Review 應至少允許：

- 新證據；
- 不同專家；
- 不同模型；
- 上級規則；
- 人工裁決；
- conflict disclosure。

可以表示：

$$
\boxed{
\mathcal R_O
\neq
\mathcal C_O
}
$$

至少在權限與方法上不能完全相同。

---

# 二十三、三層編譯架構

本文建議最小架構：

## Layer 1：Machine Compilation

快速：

$$
\mathcal C_O^{M}.
$$

處理大量低風險案件。

## Layer 2：Human / Expert Review

$$
\mathcal C_O^{H}.
$$

處理：

- 高風險；
- 低信心；
- 爭議；
- novel case。

## Layer 3：Institutional Adjudication

$$
\mathcal C_O^{J}.
$$

處理：

- 權利衝突；
- 重大先例；
- 法律／政策修改。

因此：

$$
\boxed{
\mathcal C_O
=
\mathcal C_O^M
\rightarrow
\mathcal C_O^H
\rightarrow
\mathcal C_O^J.
}
$$

不是每個案件都走到最後一層。

---

# 二十四、升級條件

定義：

$$
Escalate=1
$$

若：

$$
\gamma<\theta_\gamma
$$

或：

$$
r(a)>\theta_r
$$

或：

$$
L_{\mathrm{rights}}>\theta_R
$$

或：

$$
Novelty>\theta_N.
$$

因此：

$$
\boxed{
\text{low certainty}
+
\text{high stakes}
\rightarrow
\text{higher review layer}.
}
$$

---

# 二十五、權利底線不能被效用總和吃掉

如果只用：

$$
\min \mathbb E[L],
$$

可能產生：

> 犧牲少數權利可以讓總效用更高。

因此 OOE 必須加入 hard constraints：

$$
V_j\ge V_j^{\min}.
$$

例如：

$$
\text{due process}\ge\theta_D,
$$

$$
\text{non-discrimination}\ge\theta_N.
$$

所以：

$$
\boxed{
\min L
\quad
\text{subject to rights constraints}.
}
$$

這比單純 expected utility 更符合制度治理。

---

# 二十六、OOE 的兩階段最佳化

因此可以寫：

### Stage 1：排除不可接受行動

$$
\mathcal A_{\mathrm{valid}}
=
\{
a:
V_j(a)\ge\theta_j
\}.
$$

### Stage 2：在剩餘行動中最小化期望損失

$$
a^*
=
\arg\min_{a\in\mathcal A_{\mathrm{valid}}}
\mathbb E[L(a,O)].
$$

所以：

$$
\boxed{
\text{Rights first as constraints;
loss second as optimization}.
}
$$

---

# 二十七、本體編譯器的正式 Pipeline

完整流程可以寫成：

$$
\boxed{
O
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Scope / Context }K
}
$$

$$
\downarrow
$$

$$
\boxed{
E+\text{Provenance}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Conflict + Uncertainty Model}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Candidate Ontological States}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Rights Constraints}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Loss / Risk Evaluation}
}
$$

$$
\downarrow
$$

$$
\boxed{
\sigma+\gamma
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Action Gate }\rho
}
$$

$$
\downarrow
$$

$$
\boxed{
\kappa_O+\tau+\nu
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Monitor / Appeal / Invalidate / Recompile}.
}
$$

---

# 二十八、閉環而不是直線

最終：

$$
\text{Action}
$$

會產生新證據：

$$
E_{t+1}.
$$

因此：

$$
E_t
\rightarrow
\mathcal C_O
\rightarrow
\sigma_t
\rightarrow
A_t
\rightarrow
E_{t+1}.
$$

所以：

$$
\boxed{
\text{OOE is a closed-loop state machine}.
}
$$

而不是一次性：

$$
input\rightarrow label.
$$

---

# 二十九、NIST / WHO 類風險治理框架提供了工程先例

現代 AI 風險治理已經逐漸採取類似閉環架構。

例如 NIST AI RMF 使用：

$$
\text{Govern}
\rightarrow
\text{Map}
\rightarrow
\text{Measure}
\rightarrow
\text{Manage}
$$

組織風險活動，並強調風險管理應貫穿 AI 系統生命週期。

WHO 對 AI 與健康政策的近期工作也強調：

- living evidence；
- human verification；
- human-in-the-loop decision gateways；
- multidisciplinary oversight；
- iterative policy updating。

這些不是 OOE 本身，但它們證明：

$$
\boxed{
\text{high-uncertainty governance naturally tends toward continuous review loops}.
}
$$

---

# 三十、Mental Capacity 是「情境編譯器」的歷史現成案例

現行 Mental Capacity 實踐要求：

$$
\text{capacity}
$$

針對：

$$
\boxed{
\text{specific decision}
+
\text{specific time}.
}
$$

也就是不能永久把一個人快取成：

$$
\text{incapable forever}.
$$

這正好支持：

$$
TTL_{\mathrm{capacity}}\ll\infty.
$$

因此 OOE 的 context-sensitive compiler 並不是純粹 AI 想像。

人類制度早已在部分領域使用類似架構。

---

# 三十一、本體編譯器的最小資料結構

可寫成：

```text
OntologyCase
    case_id
    ontology_question
    entity_id
    context
    evidence[]
    evidence_provenance[]
    conflicts[]
    uncertainty
    candidate_states[]
    rights_constraints[]
    loss_model
    compiler_version
```

輸出：

```text
OntologyDecision
    operational_status
    confidence
    action_policy
    valid_until
    invalidation_triggers[]
    review_level
    appeal_path
    decision_provenance
```

這已經是一個可以工程化的最小規格。

---

# 三十二、AI Identity 範例

輸入：

```text
ontology_question = SAME_AGENT?
model_changed = true
memory_continuity = 0.97
identity_key_continuity = 1.0
relationship_continuity = 0.94
responsibility_ledger = intact
fork_detected = false
```

候選：

$$
S
=
\{
\text{same},
\text{successor},
\text{new}
\}.
$$

編譯器可能輸出：

```text
status = PROVISIONALLY_SAME
confidence = MEDIUM
```

Action Gate：

```text
retain_low_risk_permissions()
retain_liabilities()
freeze_irreversible_asset_transfer()
require_review_for_high_risk_actions()
```

這比：

```text
same = true
```

安全得多。

---

# 三十三、BCI 範例

假設 neural decoder + language model 產生一句輸出。

本體問題：

$$
O=\text{authorship / agency}.
$$

證據包括：

- neural intent signal；
- decoder confidence；
- LM completion share；
- user confirmation；
- correction history。

輸出不一定要：

$$
\text{human authored}
\quad/\quad
\text{AI authored}.
$$

可以是：

$$
\boxed{
\text{jointly mediated output}.
}
$$

並為不同用途設定不同 Action Gate：

- 日常溝通；
- 法律簽名；
- 醫療同意；
- 金融交易。

---

# 三十四、OOE 的一個重要結果：不要逼世界假裝二元

很多制度災難源自：

$$
\boxed{
\text{binary coercion}.
}
$$

即世界實際是：

$$
x\in[0,1]
$$

甚至：

$$
x\in\text{unknown}.
$$

系統卻逼：

$$
x\in\{0,1\}.
$$

OOE 應允許：

- provisional；
- disputed；
- mixed；
- partial；
- successor；
- shared；
- unknown。

這並不是逃避判斷。

因為：

$$
\boxed{
\text{action policy can still be precise even when ontology is not binary}.
}
$$

---

# 三十五、正式命題一：狀態—行動分離命題

$$
\boxed{
\sigma\neq\rho.
}
$$

同一操作本體狀態可以依風險情境導出不同動作政策。

---

# 三十六、正式命題二：不確定性保存命題

若：

$$
U(O)>0,
$$

則編譯器不應強制輸出：

$$
U_{\mathrm{output}}=0.
$$

因此：

$$
\boxed{
\text{Compiler should not destroy epistemic uncertainty without justification}.
}
$$

---

# 三十七、正式命題三：不可逆梯度命題

$$
r(a)\uparrow
\Rightarrow
\theta_E\uparrow
\land
P(\text{review})\uparrow.
$$

---

# 三十八、正式命題四：本體 TTL 命題

不同本體狀態需要不同：

$$
TTL_O.
$$

如果狀態高度時間敏感：

$$
\boxed{
TTL_O\downarrow.
}
$$

---

# 三十九、正式命題五：Cache Invalidation 命題

若新事件：

$$
e\in\mathcal I_O,
$$

則：

$$
\boxed{
\kappa_O
\rightarrow
STALE
\rightarrow
\mathcal C_O.
}
$$

---

# 四十、正式命題六：編譯器漂移命題

若制度編譯器與世界的失配：

$$
d(
\mathcal C_O,
O_{\mathrm{world}}
)
>
\theta_C,
$$

則：

$$
\boxed{
\text{compiler revision is required}.
}
$$

---

# 四十一、正式命題七：程序內生性命題

只要：

$$
P(\mathrm{error})>0
$$

且分類具有重大後果，

則：

$$
\boxed{
\text{appeal and review are internal components of ontology engineering}.
}
$$

不是外掛。

---

# 四十二、正式命題八：權利約束最佳化命題

OOE 的行動最佳化應寫為：

$$
\boxed{
a^*
=
\arg\min_{a\in\mathcal A_{\mathrm{valid}}}
\mathbb E[L(a,O)]
}
$$

其中：

$$
\mathcal A_{\mathrm{valid}}
$$

先由權利與倫理底線篩選。

---

# 四十三、正式命題九：多層裁決命題

對低風險高信心案件：

$$
\mathcal C_O^M
$$

可能足夠。

對高風險、低信心或新型案件：

$$
\boxed{
\mathcal C_O^M
\rightarrow
\mathcal C_O^H
\rightarrow
\mathcal C_O^J.
}
$$

因此 review depth 應與：

$$
\text{uncertainty}
+
\text{stakes}
+
\text{novelty}
$$

共同增加。

---

# 四十四、可反駁預測

如果本模型有解釋力，應看到：

第一，高風險不可逆判定會需要更高證據門檻與更多覆核。

第二，時間敏感的本體狀態會比制度性法人身份具有更短有效期限。

第三，當規則無法表示 disputed / provisional 等中介狀態時，誤判與例外處理成本會上升。

第四，將分類結果與實際動作權限分離，可以降低低信心分類造成的災難性後果。

第五，缺乏 provenance 的證據會降低本體判定可審計性與可申訴性。

第六，當技術條件快速改變時，未版本化的操作本體協議更容易累積治理債。

---

# 四十五、反論一：這只是 Expert System

不是。

Expert System 可以：

$$
Rules+Facts\rightarrow Answer.
$$

OOE 額外要求：

$$
\boxed{
\text{uncertainty}
+
\text{rights}
+
\text{loss}
+
\text{action gating}
+
\text{appeal}
+
\text{versioning}
+
\text{cache invalidation}.
}
$$

更重要的是：

> OOE 的規則本身就是需要治理的本體權力。

---

# 四十六、反論二：這是不是把法律和倫理都塞進程式？

不是必然。

OOE 可以是：

- 純人工制度；
- 人機混合；
- 法院流程；
- 醫療 protocol；
- 軟體 runtime。

「Compiler」描述的是功能：

$$
\text{ambiguous ontology}
\rightarrow
\text{operational state}.
$$

而不是說所有倫理判斷都應完全自動化。

---

# 四十七、反論三：為什麼不能直接讓人判？

因為：

$$
\text{human judgement}
$$

也需要：

- 標準；
- 證據；
- 程序；
- 記錄；
- 一致性；
- 申訴。

否則只是把：

$$
\text{implicit compiler}
$$

藏在人腦裡。

OOE 的目標不是：

$$
\text{replace humans}.
$$

而是：

$$
\boxed{
\text{make the ontology compiler explicit, inspectable, and governable}.
}
$$

---

# 四十八、與 OOE-IV 的接口

OOE-III 已經建立：

$$
\mathcal C_O
$$

本身的架構。

下一篇要回答：

> 人類歷史上哪一個制度最接近大規模「文明本體編譯器」？

答案之一顯然是：

$$
\boxed{
\text{Law}.
}
$$

因為法律長期處理：

- person；
- death；
- parent；
- owner；
- citizen；
- corporation；
- responsible actor；
- successor。

下一篇將正式把法律重新解讀為：

# 《OOE-IV：法律作為文明本體編譯器——擬制、推定、資格與可執行人格》

---

# 四十九、結論

OOE-III 的核心可以濃縮成一句：

$$
\boxed{
\text{本體編譯器不是回答「世界真正是什麼」；
而是在知道自己可能不知道的前提下，
把模糊世界轉換成可安全行動的制度狀態。}
}
$$

因此成熟本體編譯器不是：

```text
input -> truth
```

而應是：

```text
question
-> evidence
-> provenance
-> uncertainty
-> candidate states
-> rights constraints
-> loss model
-> operational status
-> action gate
-> cache
-> monitor
-> appeal
-> invalidate
-> recompile
```

形式上：

$$
\boxed{
O_t
\rightarrow
\mathcal C_O^{(\nu)}
\rightarrow
(\sigma_t,\gamma_t,\rho_t,\tau_t)
\rightarrow
A_t
\rightarrow
E_{t+1}
\rightarrow
\mathcal C_O^{(\nu+1)}.
}
$$

它是一個：

$$
\boxed{
\text{closed-loop, uncertainty-preserving, rights-constrained ontology runtime}.
}
$$

這也使 OOE 從一套哲學—制度理論，開始真正具備可以被工程實作的形式。

---

## 初版參考文獻與制度接口

1. NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, 2023，以及現行 AI RMF Core / Playbook。
2. World Health Organization, *Artificial intelligence and evidence-informed policy: emerging challenges and opportunities*, 2026。
3. World Health Organization, *Ethics and governance of artificial intelligence for health*。
4. NICE, *Decision-making and mental capacity*, NG108。
5. UK Government / Mental Capacity Act guidance on time- and decision-specific capacity。
6. *Decision Theory*, Stanford Encyclopedia of Philosophy。
7. Cambridge literature on Bayesian decision theory and decision-making under uncertainty。
8. OOE-I、OOE-II 與 COT。

---

## 版本註記

v0.1 已重新查核 NIST AI RMF、WHO 2026 evidence-informed AI policy guidance、Mental Capacity 的時間／決策特定性，以及決策理論中的 uncertainty / expected utility 架構。

後續 v0.2 應優先：

1. 形式化 imprecise probability 與 ambiguity；
2. 建立 evidence provenance schema；
3. 定義 Conflict Register；
4. 建立 rights-constraint DSL；
5. 建立 Action Gate reference implementation；
6. 建立 Ontology Cache / TTL / invalidation 規格；
7. 建立 Appeal / Review 狀態機；
8. 以 AI Identity 作第一個可執行 MVP；
9. 以 medical capacity 作非 AI 對照測試。
