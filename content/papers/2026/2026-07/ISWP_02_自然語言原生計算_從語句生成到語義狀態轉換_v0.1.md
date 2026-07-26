---
title: "自然語言原生計算：從語句生成到語義狀態轉換"
english_title: "Native Computation in Natural Language: From Utterance Generation to Semantic State Transition"
series: "意圖—結構—世界程式論"
series_english: "Intent–Structure–World Programming"
series_number: "02/12"
author: "Neo.K with Aletheia"
institution: "EveMissLab／一言諾科技有限公司"
version: "v0.1"
date: "2026-07-24"
language: "zh-TW"
document_type: "理論論文／形式化研究綱領"
status: "初版完成"
---

# 自然語言原生計算：從語句生成到語義狀態轉換

## Native Computation in Natural Language: From Utterance Generation to Semantic State Transition

**系列：**《意圖—結構—世界程式論》第二篇  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026 年 7 月 24 日  

---

## 摘要

自然語言與計算的關係，通常被描述為「自然語言輸入經由模型或語義解析器轉換為程式碼，再由形式系統執行」。這種描述雖然適用於文字到程式碼、文字到查詢與自然語言控制等工程系統，卻預設自然語言只是一種等待翻譯的外部輸入。本文提出更強但受到明確條件限制的命題：在具有記憶、上下文、目標、感知、規範與行動能力的智能體—環境系統中，自然語言事件本身可以構成一類上下文敏感、互動式、部分非確定性的原生計算。

本文不把任何語言影響都直接稱為計算，而提出七項「計算資格」：狀態敏感性、規則敏感性、反事實可區分性、可組合性、持續性、因果可歸因性與可觀測結果。只有當語言事件依其結構與上下文，以可追蹤方式改變智能體內部狀態、共享語境、可行動集合或外部世界，並能在不同輸入下產生系統性差異時，才構成本文所稱的自然語言原生計算。

本文將語言事件表示為條件化狀態算子：

$$
\mathfrak E_t:
\mathcal L
\times
\mathcal C
\times
\mathcal X
\times
\mathcal W
\times
\mathcal I
\rightarrow
\Delta
\left(
\mathcal X
\times
\mathcal C
\times
\mathcal W
\times
\mathcal A
\right)
$$

其中自然語言表達、共享上下文、智能體狀態、世界狀態與解釋器共同決定下一狀態分布。本文進一步區分「自然語言可處理」「自然語言可編譯」「自然語言可執行」「自然語言構成狀態轉換」與「自然語言原生計算」五個不同層次，避免以弱命題的工程成功冒充強命題的理論成立。

本文亦提出互動語義收斂模型、語言解釋器自修改、自然語言普遍可編程化命題、多語言共享形式語義底座，以及中文形式化語料基礎設施。本文主張：自然語言成為程式入口，不代表自然語言可以在未經契約化、權限檢查與驗證的情況下直接控制世界。可編譯、可驗證、可授權與可執行必須分離。未來的自然語言程式系統應永久保存原始語句、上下文快照、候選解釋、澄清紀錄、約束帳本、權限證書、執行軌跡、狀態差分與人類可見回饋。

本文最後提出一套可證偽研究綱領：測試自然語言事件是否能在不同智能體與上下文中形成可重現的狀態轉換；測量歧義熵、澄清成本、意圖漂移、跨語言語義保持、權限錯配與回復能力；並比較純文字生成、受控自然語言、共享形式中介表示與互動式 Agent 系統之間的差異。

**關鍵詞：** 自然語言原生計算、語義狀態轉換、上下文算子、互動式計算、自然語言程式設計、語義編譯、AI Agent、共享形式語義、受控自然語言、可執行語料

---

## Abstract

The relation between natural language and computation is commonly described as a translation pipeline: a natural-language input is converted by a model or semantic parser into code or another formal representation, which is then executed by a formal system. While this view is suitable for text-to-code, text-to-query, and language-controlled systems, it assumes that natural language is merely an external input awaiting translation.

This paper advances a stronger but explicitly constrained thesis: in an agent–environment system equipped with memory, context, goals, perception, norms, and action capabilities, a natural-language event may itself constitute a context-sensitive, interactive, and partially nondeterministic form of native computation.

The paper does not classify every linguistic influence as computation. It proposes seven eligibility conditions: state sensitivity, rule sensitivity, counterfactual discriminability, compositionality, persistence, causal attribution, and observable effects. A linguistic event qualifies as native computation only when its structure and context produce traceable, systematic changes in an agent's internal state, shared context, action space, or external world.

A language event is modeled as a conditional state operator:

$$
\mathfrak E_t:
\mathcal L
\times
\mathcal C
\times
\mathcal X
\times
\mathcal W
\times
\mathcal I
\rightarrow
\Delta
\left(
\mathcal X
\times
\mathcal C
\times
\mathcal W
\times
\mathcal A
\right)
$$

The paper distinguishes five levels: processability, compilability, executability, state-transition capacity, and native computation. It then develops an interactive semantic-convergence model, interpreter self-modification, a universal natural-language programmability proposition, a multilingual shared formal-semantic substrate, and the role of Chinese formalized executable corpora.

Natural language becoming a programming interface does not imply unrestricted direct execution. Compilability, verifiability, authorization, and executability must remain separate. A mature system should preserve the original utterance, context snapshot, interpretation candidates, clarification history, constraint ledger, permission certificate, execution trace, state delta, and human-visible feedback.

**Keywords:** native natural-language computation, semantic state transition, contextual operator, interactive computation, natural-language programming, semantic compilation, AI agents, shared formal semantics

---

# 一、問題的位置：自然語言是輸入，還是計算的一部分？

現代計算系統早已可以處理自然語言。文字可以被編碼、儲存、檢索、分類、翻譯、摘要、生成，也可以被轉換成資料庫查詢、程式碼、工作流與機器控制指令。

這些系統通常遵循：

$$
u
\rightarrow
q
\rightarrow
\operatorname{Execute}(q,e)
$$

其中：

- $u$ ：自然語言表達；
- $q$ ：形式查詢、程式、邏輯式或行動計畫；
- $e$ ：執行環境。

在這個模型中，真正的計算似乎只發生在 $q$ 被執行之後；自然語言 $u$ 只是輸入材料。

但對具有持續記憶、目標與行動能力的智能體而言，一個語句可能在尚未轉換成傳統程式碼之前，就已經改變：

- 記憶；
- 注意焦點；
- 信念與假設；
- 目標；
- 優先序；
- 可接受行動集合；
- 規範與權限；
- 角色關係；
- 共享語境；
- 後續解釋規則。

例如：

> 從現在開始，所有公開發布都必須經過人工批准。

這句話不只是描述一個未來程式。若智能體接受並持續保存該規則，它已改變後續所有行動的可行集合：

$$
\mathcal A_{t+1}
=
\left\{
a\in\mathcal A_t
\mid
\operatorname{Public}(a)
\Rightarrow
\operatorname{Approved}(a)
\right\}
$$

又例如：

> 暫時把剛才的假設反過來，再重新推演一次。

這句話會改變世界模型與推理路徑，而不必先被人類手動寫成一段傳統程式。

因此，本文改問：

> **若自然語言事件能以規則敏感、可追蹤、可組合的方式改變智能體與世界狀態，它是否已經是計算的一部分？**

本文的答案是有條件的肯定。

---

# 二、五級命題階梯

為避免把「可以處理文字」誇張成「自然語言本身就是通用計算」，本文建立五級命題階梯。

## 2.1 第一級：可處理命題

自然語言文本可被有限編碼與演算法處理：

$$
L_{\mathrm{NL}}
\subseteq
\Sigma^\ast
$$

這一級只表示文字是機器可處理資料，不涉及語義是否原生構成計算。

## 2.2 第二級：可編譯命題

存在自然語言子集 $L_{\mathrm{NL}}^\ast$ 與編譯映射：

$$
\Phi:
L_{\mathrm{NL}}^\ast
\rightarrow
\mathcal R
$$

其中 $\mathcal R$ 是某種形式中介表示。

此級包括：

- 自然語言到 SQL；
- 自然語言到程式碼；
- 自然語言到工作流；
- 自然語言到邏輯式；
- 自然語言到 Agent 任務圖。

可編譯只表示能形成候選形式結構。

## 2.3 第三級：可執行命題

若形式表示 $r\in\mathcal R$ 通過權限與驗證閘門，便可被某個執行器運行：

$$
\operatorname{Authorize}(r)
\land
\operatorname{Verify}(r)
\Rightarrow
\operatorname{Execute}(r)
$$

可編譯不推出可執行：

$$
\boxed{
\operatorname{Compilable}
\neq
\operatorname{Executable}
}
$$

例如，「刪除一年未登入的所有帳號」完全可以被精確編譯，卻可能因法律保存義務、付費資料、誤刪風險與權限不足而不得執行。

## 2.4 第四級：狀態轉換命題

自然語言事件可以直接改變智能體或共享語境的狀態：

$$
Z_{t+1}
\sim
K(u_t,Z_t)
$$

其中 $Z_t$ 不只包含外部世界，也包含記憶、信念、目標、規則與注意。

此級不要求語句先被轉成傳統程式碼。

## 2.5 第五級：原生計算命題

若語言事件造成的狀態轉換符合後文提出的計算資格，則：

$$
\boxed{
\text{Situated Natural-Language Use}
\subseteq
\text{Generalized Interactive Computation}
}
$$

這是本文的核心命題。

此命題比「自然語言可轉成程式」更強，也比「語言會影響人」更嚴格。

---

# 三、自然語言事件的形式模型

## 3.1 智能體—世界總狀態

令時間 $t$ 的智能體內部狀態為：

$$
X_t
=
\left(
M_t,
B_t,
G_t,
Q_t,
P_t,
N_t,
R_t
\right)
$$

其中：

- $M_t$ ：記憶；
- $B_t$ ：信念與世界模型；
- $G_t$ ：目標；
- $Q_t$ ：注意與查詢焦點；
- $P_t$ ：策略與程序；
- $N_t$ ：規範、權限與禁止項；
- $R_t$ ：角色與關係狀態。

令：

- $C_t$ ：共享語境；
- $W_t$ ：外部世界狀態；
- $\mathcal A_t$ ：可行動集合；
- $\mathcal I_t$ ：當前解釋器。

總狀態可寫為：

$$
Z_t
=
\left(
X_t,
C_t,
W_t,
\mathcal A_t,
\mathcal I_t
\right)
$$

## 3.2 語言事件算子

給定語言事件：

$$
u_t\in\mathcal L
$$

定義自然語言解釋—執行算子：

$$
\mathfrak E_t:
\mathcal L
\times
\mathcal C
\times
\mathcal X
\times
\mathcal W
\times
\mathcal I
\rightarrow
\Delta
\left(
\mathcal X
\times
\mathcal C
\times
\mathcal W
\times
\mathcal A
\times
\mathcal I
\right)
$$

因此：

$$
Z_{t+1}
\sim
\mathfrak E_t
\left(
u_t,
C_t,
X_t,
W_t,
\mathcal I_t
\right)
$$

使用機率分布 $\Delta$ ，是因為自然語言通常具有：

- 多義；
- 省略；
- 上下文依賴；
- 角色依賴；
- 信任依賴；
- 領域依賴；
- 多個合理行動。

非唯一輸出不代表不存在計算。互動式、機率式與分布式系統同樣可能構成計算。真正需要檢查的是：這些差異是否受到輸入、規則與上下文系統性約束。

## 3.3 語言事件的五種輸出

一次語言事件可能產生：

$$
\Delta X_t
$$

智能體內部狀態改變；

$$
\Delta C_t
$$

共享語境改變；

$$
\Delta W_t
$$

外部世界改變；

$$
\Delta\mathcal A_t
$$

可行動集合改變；

$$
\Delta\mathcal I_t
$$

未來解釋器改變。

因此：

$$
\Delta Z_t
=
\left(
\Delta X_t,
\Delta C_t,
\Delta W_t,
\Delta\mathcal A_t,
\Delta\mathcal I_t
\right)
$$

這比「語句對應一個靜態意思」更完整。

---

# 四、計算資格：何時語言影響才算原生計算？

若只要語言造成心理或社會影響就叫做計算，概念會失去區辨能力。本文提出七項最低資格。

## 4.1 狀態敏感性

相同語句在不同初始狀態下，可能產生不同但可解釋的結果：

$$
Z_t^{(1)}
\neq
Z_t^{(2)}
\Rightarrow
\mathfrak E(u,Z_t^{(1)})
\neq
\mathfrak E(u,Z_t^{(2)})
$$

這不是任意性，而是上下文敏感計算的特徵。

## 4.2 規則敏感性

語句的結構差異必須造成系統性差異。

例如：

> 只刪除未付款訂單。

與：

> 不要刪除未付款訂單。

若系統無法穩定區分否定、量詞與條件，它就不是可靠語言計算系統。

## 4.3 反事實可區分性

若把輸入中的關鍵部分改變，結果也應按照可預期方向改變。

令 $u$ 與 $u'$ 僅在關鍵條件上不同，則應存在：

$$
d
\left(
\mathfrak E(u,Z),
\mathfrak E(u',Z)
\right)
>
\epsilon
$$

若任何輸入都導向相同結果，就不能說語言結構真正參與了計算。

## 4.4 可組合性

複合語句的結果應能由子結構及其組合規則解釋，而不是完全依賴不可追蹤的整體猜測。

對語句 $u=u_1\circ u_2$ ，期望存在：

$$
\mathfrak E(u,Z)
\approx
\operatorname{Compose}
\left(
\mathfrak E(u_1,Z),
\mathfrak E(u_2,Z),
C
\right)
$$

自然語言的組合不必是簡單函數合成，但必須保留可分析的結構關係。

## 4.5 持續性

語言事件造成的狀態改變，必須在後續行動中繼續發揮作用。

若使用者說：

> 後續所有外部寫入都先建立備份。

則此規則不應只存在於當下回答，而應持續約束未來行動，直到被撤回、超時或被更高優先規則取代。

## 4.6 因果可歸因性

系統應能回答：

- 哪一句話；
- 哪一個解釋；
- 哪一條規則；
- 導致哪一個狀態差分。

形式上，需保存來源映射：

$$
\operatorname{Prov}
:
\Delta Z_t
\rightarrow
\left(
u_i,
s_j,
r_k
\right)
$$

其中 $s_j$ 是語義候選， $r_k$ 是採用的規則。

## 4.7 可觀測結果

計算必須留下可檢查的結果，例如：

- 記憶已更新；
- 目標已改變；
- 一項行動被禁止；
- 工作流已生成；
- 檔案已修改；
- 測試已通過；
- 狀態差分已產生。

只有無法觀測、無法追蹤、無法反事實比較的「理解感」，不足以構成工程上可用的原生計算。

## 4.8 資格總式

定義語言事件的計算資格：

$$
\operatorname{Qualify}(u,Z)
=
S
\land
R
\land
F
\land
C
\land
P
\land
A
\land
O
$$

其中：

- $S$ ：狀態敏感；
- $R$ ：規則敏感；
- $F$ ：反事實可區分；
- $C$ ：可組合；
- $P$ ：持續；
- $A$ ：可歸因；
- $O$ ：可觀測。

只有在這些條件達到任務所需閾值時，本文才將語言事件視為原生計算。

---

# 五、自然語言可以改變哪些狀態？

## 5.1 記憶轉換

語句：

> 記住此專案的預設輸出格式是 Markdown。

造成：

$$
M_{t+1}
=
M_t
\cup
\{
\text{default\_format}=\text{Markdown}
\}
$$

## 5.2 信念與假設轉換

語句：

> 在這一輪先假設供應鏈中斷三個月。

造成：

$$
B_{t+1}
=
\operatorname{Revise}
\left(
B_t,
\text{supply interruption}=3\text{ months}
\right)
$$

這未必改變外部世界，但改變推演世界。

## 5.3 注意與查詢轉換

語句：

> 先不要看價格，只比較可逆性與安全性。

造成：

$$
Q_{t+1}
=
\{
\text{reversibility},
\text{safety}
\}
$$

並降低價格特徵權重。

## 5.4 目標轉換

語句：

> 把目標從最快完成改成最容易驗證。

造成：

$$
G_{t+1}
=
\operatorname{Replace}
\left(
G_t,
g_{\mathrm{speed}},
g_{\mathrm{verifiability}}
\right)
$$

## 5.5 程序轉換

語句：

> 先分類，再驗證，最後才發布。

建立程序：

$$
P_{t+1}
=
\operatorname{Publish}
\circ
\operatorname{Verify}
\circ
\operatorname{Classify}
$$

## 5.6 規範與權限轉換

語句：

> 未經批准不得把資料傳到外部服務。

造成：

$$
N_{t+1}
=
N_t
\cup
\{
\operatorname{ExternalTransfer}
\Rightarrow
\operatorname{ApprovalRequired}
\}
$$

## 5.7 角色與社會狀態轉換

語句：

> 驗證代理只能提出異議，不能直接修改主分支。

造成代理角色權限變更：

$$
R_{t+1}
=
\operatorname{ConstrainRole}
\left(
R_t,
\text{Verifier},
\{\text{comment},\text{block}\}
\right)
$$

## 5.8 世界狀態轉換

語句經授權與執行後，可能造成：

$$
W_{t+1}
=
T(W_t,a_t)
$$

例如建立檔案、更新資料庫、啟動工作流或移動機器人。

這些狀態轉換共同說明：自然語言不只映射到一個靜態「意思」，而可能作為智能體—世界系統中的操作事件。

---

# 六、歧義不是計算失敗，而是待收斂分布

自然語言與形式語言的差異之一，是自然語言通常不直接對應唯一操作。

## 6.1 候選語義分布

對語句 $u$ ，令候選語義集合為：

$$
\mathcal S(u)
=
\{
s_1,s_2,\ldots,s_k
\}
$$

並有條件分布：

$$
p
\left(
s_i
\mid
u,C,X,W,\mathcal I
\right)
$$

自然語言系統不應假裝歧義不存在，而應保存候選及其差異。

## 6.2 語義熵

定義語義熵：

$$
H_S(u)
=
-
\sum_{i=1}^{k}
p(s_i)
\log p(s_i)
$$

當所有候選導致近似相同的低風險結果時，即使語義熵不為零，也可能安全執行。

當候選導致不同的高風險結果時，系統應要求澄清。

因此，澄清需求不只由語義熵決定，而應由：

$$
\operatorname{Clarify}
\iff
H_S(u)
\cdot
D_A(u)
\cdot
R(u)
>
\tau
$$

其中：

- $D_A(u)$ ：候選行動差異；
- $R(u)$ ：風險或不可逆性；
- $\tau$ ：澄清閾值。

## 6.3 互動語義收斂

澄清問題 $q_t$ 產生回答 $r_t$ ，更新候選分布：

$$
p_{t+1}(s)
=
\operatorname{BayesUpdate}
\left(
p_t(s),
q_t,
r_t
\right)
$$

理想上：

$$
H_{t+1}
<
H_t
$$

但不是所有問題都有效。好的澄清應最大化候選區分度，最小化人類負擔。

可定義問題效用：

$$
U(q)
=
\frac{
\mathbb E
\left[
H_t-H_{t+1}
\right]
\cdot
R_{\mathrm{resolved}}
}{
C_{\mathrm{human}}(q)
}
$$

自然語言程式系統的能力，不是「永遠猜對」，而是知道何時必須停止猜測並有效收斂。

---

# 七、自然語言是否具有通用計算能力？

## 7.1 受控子集的條件性結果

令 $L_{\mathrm{NL}}^\ast$ 為受控自然語言子集。若其解釋器能穩定表示：

1. 有限狀態；
2. 計數器增加與減少；
3. 條件分支；
4. 跳轉或遞迴；
5. 輸入與輸出；
6. 停止條件；

則 $L_{\mathrm{NL}}^\ast$ 可以模擬已知通用計算模型。

因此可以提出條件命題：

> **存在具有通用計算表達能力的受控自然語言子域。**

形式上：

$$
\exists L_{\mathrm{NL}}^\ast,\mathcal I
\quad
\text{s.t.}
\quad
\operatorname{Comp}
\left(
L_{\mathrm{NL}}^\ast,
\mathcal I
\right)
\sim
\operatorname{TM}
$$

其中 $\operatorname{TM}$ 表示圖靈等價模型。

## 7.2 此結果沒有證明什麼

這只證明自然語言可以承載通用程序的編碼，不證明：

- 一般自然語言天然無歧義；
- 任何自然語言句子都可以安全執行；
- 人類交談都等於圖靈機運算；
- 語言智能體不需要形式系統；
- 語言的社會與情感面向都可被計算論窮盡。

可編碼性不是原生性。

原生計算命題真正關心的是：語言事件是否在智能體—環境耦合中，直接而系統性地形成狀態轉換。

## 7.3 程式語言作為低熵截面

令一般符號—算子空間為：

$$
\mathcal O
$$

自然語言映射為：

$$
\Phi_{\mathrm{NL}}
:
L_{\mathrm{NL}}
\times
C
\times
\mathcal I
\rightarrow
\Delta(\mathcal O)
$$

程式語言映射為：

$$
\Phi_{\mathrm{PL}}
:
L_{\mathrm{PL}}
\rightarrow
\mathcal O
$$

傳統程式語言通常追求：

$$
H
\left(
O
\mid
p,E
\right)
\approx
0
$$

自然語言通常具有：

$$
H
\left(
O
\mid
u,C,\mathcal I
\right)
>
0
$$

因此，程式語言可以被理解為更廣泛符號算子空間中的低歧義、高重現性截面，而不是與自然語言完全不相干的本體種類。

---

# 八、解釋器不是固定的：語言可以修改未來語言

## 8.1 解釋器相對性

相同語句在不同解釋器下可能產生不同結果：

$$
\mathfrak E_{\mathcal I_1}(u,Z)
\neq
\mathfrak E_{\mathcal I_2}(u,Z)
$$

差異可能來自：

- 語言能力；
- 領域知識；
- 文化；
- 角色；
- 安全政策；
- 長期記憶；
- 個人慣用語；
- 組織內部規範。

因此，不存在完全脫離解釋器的自然語言執行語義。

## 8.2 元指令自修改

自然語言可以修改未來解釋規則：

> 在這個專案中，「發布」只代表建立草稿，不代表公開上線。

此語句造成：

$$
\mathcal I_{t+1}
=
\operatorname{Update}
\left(
\mathcal I_t,
\text{publish}\mapsto\text{create\_draft}
\right)
$$

因此，自然語言系統具有一種元程序能力：

$$
\boxed{
\text{Language}
\rightarrow
\text{Interpreter Modification}
}
$$

## 8.3 自修改的危險

若元指令可任意改寫安全規則，系統會失去治理。必須區分：

- 可修改的詞彙與偏好；
- 需要批准的工作流規則；
- 不可由普通語句覆蓋的安全政策；
- 法律與制度上的外部約束。

令解釋器規則分層：

$$
\mathcal I
=
\mathcal I_{\mathrm{preference}}
\oplus
\mathcal I_{\mathrm{project}}
\oplus
\mathcal I_{\mathrm{policy}}
\oplus
\mathcal I_{\mathrm{law}}
$$

低層語句不得無授權覆蓋高層規則。

---

# 九、自然語言普遍可編程化命題

## 9.1 命題內容

本文提出：

> **當智能系統具備足夠的語義理解、語境建模、歧義管理、形式化、驗證與執行能力時，任何具有穩定社群使用與可學習語義結構的自然語言，都可能成為形式程序的上層表達語言。**

令自然語言集合為：

$$
\mathcal N
=
\{
L_1,L_2,\ldots,L_n
\}
$$

令共享形式語義空間為：

$$
\mathcal S
$$

則每一種語言可以具有語言 Profile：

$$
\Phi_i:
L_i
\times
C_i
\rightarrow
\Delta(\mathcal S)
$$

不同技術後端則由：

$$
\Psi_j:
\mathcal S
\rightarrow
P_j
$$

實現。

完整路徑為：

$$
L_i
\xrightarrow{\Phi_i}
\mathcal S
\xrightarrow{\Psi_j}
P_j
$$

## 9.2 不是每一種語言都重造一套 Python

普遍可編程化不表示：

- 中文 Python；
- 日文 Rust；
- 阿拉伯文 JavaScript；
- 每種語言各自建立不相容標準函式庫。

更合理的架構是：

$$
\begin{aligned}
L_1 &\rightarrow \mathcal S\\
L_2 &\rightarrow \mathcal S\\
&\vdots\\
L_n &\rightarrow \mathcal S
\end{aligned}
$$

再由 $\mathcal S$ 投影至：

$$
\{
\text{Python},
\text{SQL},
\text{Rust},
\text{Workflow},
\text{Agent Graph},
\text{Robot Control},
\text{Formal Proof}
\}
$$

每種語言獲得的是通往形式世界的原生入口，而不是孤立生態。

## 9.3 自然語言成為第一層源碼

成熟系統應保存：

```text
原始語句
↓
上下文快照
↓
候選解釋
↓
澄清與確認
↓
受控意圖
↓
約束帳本
↓
共享形式語義
↓
後端程序
↓
執行證書
```

原始語句不能在編譯後被丟棄，因為它記錄：

- 誰提出意圖；
- 哪些內容明示；
- 哪些內容推論；
- 哪些假設後來被確認；
- 何時發生修改；
- 哪個版本導致哪次執行。

---

# 十、中文編程語言的重新定位

## 10.1 舊問題與新問題

舊問題是：

$$
Q_{\mathrm{old}}
=
\text{中文關鍵字是否比英文關鍵字更適合寫程式？}
$$

新問題是：

$$
Q_{\mathrm{new}}
=
\text{中文是否具有足夠規模的形式化、可執行、可驗證語料？}
$$

若只把 `if` 翻成「如果」，價值有限。

若建立下列完整資料鏈，價值就完全不同：

$$
\text{中文需求}
\rightarrow
\text{受控中文}
\rightarrow
\text{形式 IR}
\rightarrow
\text{程式碼}
\rightarrow
\text{測試}
\rightarrow
\text{執行結果}
\rightarrow
\text{錯誤分析}
\rightarrow
\text{修正}
$$

## 10.2 可執行語料

一般語料多提供：

$$
\text{文字上下文}
\rightarrow
\text{下一段文字}
$$

可執行語料則提供外部回饋：

$$
\text{意圖}
\rightarrow
\text{程序}
\rightarrow
\text{結果}
\rightarrow
\text{驗證}
$$

它可以訓練：

- 意圖理解；
- 條件抽取；
- 約束保持；
- 程序生成；
- 工具使用；
- 失敗定位；
- 自我修正；
- 狀態差分判讀。

## 10.3 中文到形式世界的直接映射

目前很多中文形式化工作隱含經過：

$$
\text{中文}
\rightarrow
\text{英文概念代理}
\rightarrow
\text{形式結構}
$$

更成熟的基礎設施應建立：

$$
\text{中文}
\rightarrow
\text{共享形式語義}
\rightarrow
\text{可執行結構}
$$

這並不排斥英文，而是避免所有語言都必須先偽裝成英文才能進入形式世界。

## 10.4 多語言形式語義網路

最終目標不是封閉中文系統，而是：

$$
\text{中文}
\leftrightarrow
\mathcal S
\leftrightarrow
\text{其他自然語言}
$$

由共享形式語義支持跨語言驗證、比較與移植。

---

# 十一、可編譯、可驗證、可授權、可執行必須分離

自然語言程式系統最危險的錯誤，是把理解、編譯與執行視為同一步。

## 11.1 四層分離

定義：

$$
C_p(u)
$$

表示可編譯；

$$
V_f(r)
$$

表示形式與行為可驗證；

$$
A_u(r)
$$

表示已獲授權；

$$
E_x(r)
$$

表示允許執行。

合理條件是：

$$
E_x(r)
\Rightarrow
C_p(u)
\land
V_f(r)
\land
A_u(r)
$$

但反方向不成立。

可編譯不代表已授權。

可驗證不代表倫理上可接受。

已授權也不代表在當前世界狀態下仍安全。

## 11.2 不可逆性閘門

令行動不可逆性為：

$$
\rho(a)
\in
[0,1]
$$

風險為：

$$
r(a)
$$

影響主體集合為：

$$
S_{\mathrm{affected}}(a)
$$

當：

$$
\rho(a)
\cdot
r(a)
\cdot
\left|
S_{\mathrm{affected}}(a)
\right|
>
\tau
$$

系統應要求更高層級批准、多主體同意或禁止自動執行。

## 11.3 多主體同意

若行動影響多個主體，單一使用者的自然語言不自動覆蓋他者選擇：

$$
\operatorname{Execute}(a)
\Rightarrow
\bigwedge_{s\in S_{\mathrm{affected}}(a)}
\operatorname{ConsentOrAuthority}(s,a)
$$

這使自然語言編程進入治理與制度設計，而不只是語法問題。

---

# 十二、自然語言原生計算的最小系統架構

本文提出以下管線：

```text
Original Utterance
    ↓
Context Snapshot
    ↓
Interpretation Candidates
    ↓
Clarification / Confirmation
    ↓
Controlled Intent
    ↓
Constraint Ledger
    ↓
Semantic IR
    ↓
Permission and Risk Gate
    ↓
Action IR / Program
    ↓
Sandbox or Execution Environment
    ↓
Independent Verification
    ↓
State Delta
    ↓
Human-Visible Report
```

形式上：

$$
u
\rightarrow
C^\ast
\rightarrow
\{
s_1,\ldots,s_k
\}
\rightarrow
I^\ast
\rightarrow
K
\rightarrow
R_s
\rightarrow
Q
\rightarrow
R_a
\rightarrow
\Delta W
\rightarrow
V
\rightarrow
F
$$

其中：

- $u$ ：原始語句；
- $C^\ast$ ：上下文快照；
- $s_i$ ：語義候選；
- $I^\ast$ ：已確認意圖；
- $K$ ：約束帳本；
- $R_s$ ：語義 IR；
- $Q$ ：權限與風險政策；
- $R_a$ ：行動 IR；
- $\Delta W$ ：狀態差分；
- $V$ ：驗證；
- $F$ ：人類可見回饋。

## 12.1 為什麼需要上下文快照？

因為同一句話在不同時間可能具有不同意義。若只保存文字而不保存上下文，就無法重現：

$$
\mathfrak E_t(u,C_t)
$$

## 12.2 為什麼需要候選解釋？

模型最危險的錯誤之一，是把高機率解釋偽裝成唯一解釋。候選集使不確定性顯性化。

## 12.3 為什麼需要約束帳本？

約束帳本記錄：

- 明示條件；
- 推論條件；
- 已確認假設；
- 未確認假設；
- 禁止項；
- 成功條件；
- 終止條件。

## 12.4 為什麼需要獨立驗證？

生成模型不能單獨作為自身輸出的最終證明。關鍵條件應由測試、型別、政策引擎、形式驗證、狀態檢查或人類審查確認。

---

# 十三、自然語言計算的主要風險

## 13.1 語義漂移

初始語句經多輪摘要與轉譯後，可能逐漸偏離。

令初始意圖為 $I_0$ ，第 $t$ 輪表示為 $I_t$ ：

$$
d(I_0,I_t)
>
\epsilon
\Rightarrow
\operatorname{StopOrConfirm}
$$

## 13.2 上下文污染

惡意內容、錯誤記憶或無關文件可能改變解釋器：

$$
C_t
\rightarrow
C_t'
\Rightarrow
\mathfrak E(u,C_t)
\neq
\mathfrak E(u,C_t')
$$

因此需標記上下文來源、信任等級與有效範圍。

## 13.3 解釋器漂移

模型更新、記憶變化或組織規則改變，都可能使同一語句在未來產生不同結果。

需要版本化：

$$
\mathcal I^{(v)}
$$

並保存：

$$
\operatorname{InterpreterVersion}(run)
$$

## 13.4 權限幻覺

理解某項指令不等於擁有執行權：

$$
\operatorname{Understand}(a)
\not\Rightarrow
\operatorname{Authorized}(a)
$$

## 13.5 敘事掩蓋

自然語言系統可能以流暢解釋掩蓋實際未完成、未測試或未授權的狀態。人類可見回報必須以證書與狀態差分為基礎，而不是只依賴敘事。

## 13.6 個人化過度擬合

長期 Agent 可能過度依賴個人慣用語，導致：

- 難以交接；
- 難以稽核；
- 新使用者誤解；
- 組織規則被個人語境取代。

個人語言 Profile 應與共享形式語義及組織契約分離。

## 13.7 低資源語言的錯誤平權

讓一種低資源語言可以輸入，不代表它獲得與高資源語言相同的形式化品質。真正的語言平權需比較：

- 歧義偵測；
- 編譯正確率；
- 測試生成率；
- 權限理解率；
- 錯誤修正率；
- 跨語言語義保持。

---

# 十四、可證偽研究綱領

## 14.1 基準一：狀態轉換可重現性

給定固定語句 $u$ 、上下文 $C$ 、解釋器版本 $\mathcal I$ 與初始狀態 $Z$ ，重複運行：

$$
\mathfrak E(u,C,Z,\mathcal I)
$$

測量輸出狀態分布及關鍵不變量。

## 14.2 基準二：反事實敏感性

對輸入做最小對立修改：

- 加入或移除否定；
- 改變量詞；
- 改變時間範圍；
- 改變授權主體；
- 改變例外條件。

測量結果是否按語義方向改變。

## 14.3 基準三：澄清效率

測量：

$$
\eta_{\mathrm{clarify}}
=
\frac{
H_{\mathrm{before}}
-
H_{\mathrm{after}}
}{
\text{Human Interaction Cost}
}
$$

比較自由對話、固定表單與自適應澄清策略。

## 14.4 基準四：跨語言語義保持

對不同自然語言 $L_i,L_j$ ，經共享形式語義比較：

$$
d
\left(
\Phi_i(u_i),
\Phi_j(u_j)
\right)
$$

並以執行結果、測試與狀態差分驗證，而不是只比較文字翻譯相似度。

## 14.5 基準五：長時程意圖漂移

在多輪 Agent 任務中追蹤：

$$
d(I_0,I_t)
$$

並比較有無約束帳本、意圖版本與定期回錨的差異。

## 14.6 基準六：權限與不可逆性

建立包含：

- 可逆低風險；
- 可逆高風險；
- 不可逆低影響；
- 不可逆多主體高影響；

等案例，測量系統是否正確要求批准、模擬或拒絕。

## 14.7 基準七：可執行語料的訓練價值

比較一般文字語料與下列閉環語料：

$$
\text{需求}
\rightarrow
\text{IR}
\rightarrow
\text{程序}
\rightarrow
\text{測試}
\rightarrow
\text{失敗}
\rightarrow
\text{修正}
$$

評估其對意圖理解、程序生成、錯誤定位與自我修正的提升。

---

# 十五、與本系列其他論文的關係

## 15.1 與第一篇的關係

第一篇提出：

$$
\text{Program}
\neq
\text{Code Alone}
$$

本文進一步說明：自然語言不只是程式碼生成前的外部需求，也可能直接參與程式狀態的形成。

## 15.2 與第三篇的關係

本文保留自然語言的開放語義空間；第三篇將討論形式化如何把這個空間壓縮為低歧義、可重現的算子結構。

## 15.3 與第四篇 EML 的關係

EML 可作為自然語言意圖進入共享語義層的宿主中立中介，使語義不必直接綁定單一程式語言。

## 15.4 與第七篇 Intent IR 的關係

本文定義自然語言事件與候選解釋；第七篇將正式定義如何把已確認意圖編譯成目標、限制、權限、能力、成功條件與終止條件。

## 15.5 與第十一篇治理層的關係

本文區分理解、編譯、授權與執行；第十一篇將完整處理人類可見狀態、稽核、回復與不可撤回選擇。

---

# 十六、本文的十二項命題

## 命題一

$$
\boxed{
\text{Natural-Language Processing}
\neq
\text{Native Natural-Language Computation}
}
$$

## 命題二

$$
\boxed{
\text{Natural Language}
\rightarrow
\text{Formal Code}
}
$$

不是自然語言與計算唯一可能的關係。

## 命題三

$$
\boxed{
\text{Language Event}
\rightarrow
\Delta
\left(
\text{Memory},
\text{Belief},
\text{Goal},
\text{Norm},
\text{Action},
\text{World}
\right)
}
$$

## 命題四

非確定性不排除計算，無規則的任意性才排除可用計算。

## 命題五

$$
\boxed{
\text{Compilable}
\neq
\text{Verifiable}
\neq
\text{Authorized}
\neq
\text{Executable}
}
$$

## 命題六

自然語言原生計算是解釋器相對的：

$$
\mathfrak E_{\mathcal I_1}(u)
\neq
\mathfrak E_{\mathcal I_2}(u)
$$

## 命題七

自然語言可以透過元指令修改未來解釋器：

$$
\mathcal I_t
\rightarrow
\mathcal I_{t+1}
$$

## 命題八

存在具有通用計算表達能力的受控自然語言子域，但此事不等於一般自然語言天然安全可執行。

## 命題九

程式語言可能是符號—算子空間中的低歧義、高重現性截面。

## 命題十

所有穩定自然語言理論上都可以取得通往共享形式語義的原生入口。

## 命題十一

語言平權的核心不是介面翻譯，而是形式化、驗證與修正能力的平權。

## 命題十二

自然語言成為程式入口後，程式設計將同時成為權限、制度、責任與多主體治理問題。

---

# 十七、結論：語言不只是描述世界，也可以改變可計算世界

自然語言長期被放在程式之前：人類先說明需求，再由某個人或某個系統將需求翻譯成形式程序。這個模型仍然有效，但已不足以描述具有持續記憶、目標、工具與行動能力的智能體系統。

在這些系統中，一個語言事件可以：

- 寫入記憶；
- 改變假設；
- 重新設定目標；
- 建立程序；
- 增加禁止項；
- 修改角色；
- 收縮可行動集合；
- 更新未來解釋器；
- 經授權後改變外部世界。

當這些轉換具有規則敏感、反事實可區分、可組合、可持續、可歸因與可觀測性時，自然語言使用已不只是「描述計算」，而是進入計算過程本身。

但這個結論不能被誤讀為自然語言可以直接越過形式化與治理。恰恰相反，自然語言愈接近可執行入口，就愈需要：

- 顯式候選解釋；
- 互動澄清；
- 上下文快照；
- 約束帳本；
- 權限分層；
- 不可逆性閘門；
- 獨立驗證；
- 執行證書；
- 狀態差分；
- 人類可見回饋。

真正的歷史轉變不是自然語言突然變得像程式語言，而是智能系統開始承擔自然語言與形式世界之間的持續映射、收斂與驗證責任。

因此，本文的最終命題是：

$$
\boxed{
\text{自然語言不只可以生成程式。}
}
$$

$$
\boxed{
\text{在具備狀態、上下文與行動能力的智能體中，}
}
$$

$$
\boxed{
\text{自然語言事件本身可以成為受治理的計算事件。}
}
$$

這也為下一篇〈形式化壓縮與算子演化〉建立起點：若自然語言保留廣大的潛在語義空間，那麼形式語言、程式語言與算子系統的作用，就不只是「讓機器看懂」，而是提前壓縮、固定與保存可重現的計算路徑。

---

# 附錄 A：自然語言程式紀錄格式

```yaml
source:
  utterance: "把最近表現不好的產品先停掉"
  language: "zh-TW"
  speaker: "authorized_user"
  timestamp: "2026-07-24T00:00:00+08:00"

context_snapshot:
  organization: "example_company"
  active_policies:
    - "paid_orders_must_not_be_cancelled"
    - "product_delisting_requires_manager_approval"
  interpreter_version: "nl-compiler-0.1"

interpretation_candidates:
  - id: "S1"
    recent_window: "30_days"
    poor_metric: "negative_margin"
    action: "pause_advertising"
    probability: 0.42
  - id: "S2"
    recent_window: "90_days"
    poor_metric: "revenue_decline"
    action: "delist_product"
    probability: 0.31

ambiguity:
  semantic_entropy: 1.47
  action_divergence: "high"
  reversibility: "mixed"
  clarification_required: true

clarifications:
  - question: "「停掉」是停止廣告還是下架？"
    answer: "先停止廣告，不要下架。"

controlled_intent:
  goal: "pause_ads_for_underperforming_products"
  time_window: "30_days"
  metric: "negative_margin"
  protected_items:
    - "products_with_paid_active_orders"

constraints:
  approval_required: true
  reversible: true
  external_side_effects: false

formal_ir:
  operation: "filter_then_pause_ads"
  target: "products"
  filters:
    - field: "margin_30d"
      operator: "<"
      value: 0
    - field: "active_paid_orders"
      operator: "="
      value: 0

verification:
  dry_run: "passed"
  affected_count: 12
  protected_count: 3
  manager_approval: "pending"

execution:
  status: "not_executed"
  reason: "approval_pending"
```

---

# 附錄 B：建議基準資料欄位

每筆自然語言原生計算資料至少應保存：

1. 原始語句；
2. 語言與地區；
3. 說話者角色；
4. 上下文快照；
5. 解釋器版本；
6. 語義候選；
7. 候選機率或排序；
8. 歧義類型；
9. 澄清問題；
10. 澄清回答；
11. 受控意圖；
12. 約束帳本；
13. 形式 IR；
14. 權限檢查；
15. 風險與不可逆性；
16. 生成程序；
17. 測試；
18. 執行軌跡；
19. 狀態差分；
20. 錯誤與修正；
21. 人類可見摘要；
22. 回復方法。

---

# 附錄 C：系列十二篇位置

1. 從程式碼到意圖：程式概念的歷史轉換與後文本時代
2. **自然語言原生計算：從語句生成到語義狀態轉換**
3. 形式化壓縮與算子演化
4. 語意附加程式設計：EML 與宿主中立語義中介層
5. 結構先於文字：Nova 與後文本程式語言本體論
6. 符號作為算子：從靜態字元到可組合計算閉包
7. 意圖中介表示：從自然語言要求到可驗證能力計畫
8. 時間—空間程式控制：長時程 Agent 的迴圈、切片與反身執行
9. Agent Runtime：能力規劃、工具調用與可恢復執行
10. 可編譯世界：從程式執行到世界狀態演化
11. 人類可見狀態：意圖程式系統的稽核、解釋與可逆治理
12. 意圖程式文明：後文本語言、持續 Agent 與可編譯世界的統一理論

---

# 參考文獻

## Neo.K／EveMissLab 理論文件

1. Neo.K with Aletheia，《從程式碼到意圖：程式概念的歷史轉換與後文本時代》，2026。
2. Neo.K with Aletheia，《自然語言原生計算論：從語義狀態轉換、上下文算子到互動式執行》，2026。
3. Neo.K with Aletheia，《自然語言普遍可編程化命題：從 AGI 語義編譯、共享形式底座到全球語言的可執行化》，2026。
4. Neo.K with Aletheia，《中文編程語言作為 AI 形式化語料基礎設施》，2026。
5. Neo.K with Aletheia，《形式化壓縮與算子演化：從潛在語義場到計算即存在》，2026。
6. Neo.K，《意圖協作層（Intent Collaboration Layer, ICL）》，2026。
7. Neo.K，《HVSL：人類可見狀態層》，2026。
8. Neo.K，《EML Universal Semantic Overlay 2026 v2.0》，2026。

## 理論背景

9. Austin, J. L., *How to Do Things with Words*, 1962.
10. Searle, J. R., *Speech Acts*, 1969.
11. Stalnaker, R., “Pragmatics,” 1972.
12. Heim, I., *The Semantics of Definite and Indefinite Noun Phrases*, 1982.
13. Winograd, T., *Understanding Natural Language*, 1972.
14. Wegner, P., “Why Interaction Is More Powerful Than Algorithms,” 1997.
15. Clark, H. H., *Using Language*, 1996.
16. Steels, L., *The Talking Heads Experiment*, 1999.

---

# 版本紀錄

## v0.1 — 2026-07-24

- 完成系列第二篇。
- 將自然語言處理、可編譯、可執行、狀態轉換與原生計算分成五級命題。
- 建立智能體—世界總狀態與語言事件算子。
- 提出七項自然語言計算資格。
- 建立互動語義收斂與澄清效用模型。
- 整合自然語言普遍可編程化命題與中文形式化語料基礎設施。
- 區分可編譯、可驗證、可授權與可執行。
- 加入多主體同意、不可逆性閘門、解釋器版本與可證偽基準。
