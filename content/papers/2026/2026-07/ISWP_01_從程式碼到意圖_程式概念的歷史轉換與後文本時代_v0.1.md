---
title: "從程式碼到意圖：程式概念的歷史轉換與後文本時代"
english_title: "From Code to Intent: The Historical Transformation of the Program Concept and the Post-Textual Era"
series: "意圖—結構—世界程式論"
series_english: "Intent–Structure–World Programming"
series_number: "01/12"
author: "Neo.K with Aletheia"
institution: "EveMissLab／一言諾科技有限公司"
version: "v0.1"
date: "2026-07-24"
language: "zh-TW"
document_type: "理論論文／系列總導論"
status: "初版完成"
---

# 從程式碼到意圖：程式概念的歷史轉換與後文本時代

## From Code to Intent: The Historical Transformation of the Program Concept and the Post-Textual Era

**系列：**《意圖—結構—世界程式論》第一篇  
**作者：** Neo.K with Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026 年 7 月 24 日  

---

## 摘要

程式設計長期被理解為：人類先形成目的，再將目的翻譯成程式碼，最後由機器依照程式碼執行。然而，大型語言模型、程式生成系統、AI Agent、結構化中介表示、可逆投影編輯器、持久記憶、工具調用與世界狀態執行環境的結合，正在改變這個基本關係。人類不再必須逐行指定全部操作，而逐漸轉向描述目的、限制、架構、權限、成功條件、失敗處理與驗證方式；AI 與確定性工具鏈則負責將這些內容展開為中介表示、程式碼、工具行動與狀態轉換。

本文提出：這場轉變不應被簡化為「自然語言取代程式語言」或「程式碼即將消失」。更準確的說法是，程式的本體正在從單一文字工件，擴展為由意圖、約束、結構、能力、執行、驗證、回饋與治理共同構成的狀態轉換系統。程式碼仍然重要，但逐漸由程式本體退居為一種可執行投影。本文將這一轉變稱為「程式介面上移」與「程式本體擴張」。

本文首先區分程式碼、程式、意圖、規格、中介表示與世界狀態；其次重建從機器指令、高階語言、結構化與宣告式程式設計，到 AI 協作與意圖驅動系統的概念演化；再提出一個由意圖契約、語義表示、結構表示、能力計畫、執行產物、驗證器、狀態差分與人類可見回饋組成的統一模型。本文並提出「後文本程式系統」的最低判準：程式的權威本體不再等於單一文字檔案；多種視圖可以是同一結構的可逆投影；AI 建議不能越過可驗證核心；所有執行必須保留來源、權限、狀態差分與回復路徑。

本文最後指出，意圖時代並不降低程式工程的要求，反而把工程責任從局部語法正確性，上移到架構、契約、權限、可觀測性與世界狀態治理。未來程式設計的核心問題將不再只是「如何寫出這段程式碼」，而是「誰以何種意圖，在何種限制與權限下，透過何種可驗證結構，使世界發生何種可逆或不可逆的改變」。

**關鍵詞：** 意圖驅動程式設計、後文本程式設計、程式本體、AI Agent、自然語言程式設計、中介表示、狀態轉換、人機協作、可驗證執行、世界狀態治理

---

## Abstract

Programming has traditionally been understood as a pipeline in which a human forms an objective, translates it into source code, and delegates execution to a machine. The integration of large language models, code-generating systems, AI agents, structured intermediate representations, reversible projection editors, persistent memory, tool use, and stateful execution environments is transforming this relationship. Human operators increasingly specify goals, constraints, architecture, permissions, success conditions, failure policies, and verification criteria, while AI systems and deterministic toolchains expand those specifications into intermediate representations, executable artifacts, actions, and state transitions.

This paper argues that the transformation should not be reduced to the claim that natural language will replace programming languages or that source code will disappear. A more precise interpretation is that the ontology of the program is expanding from a single textual artifact into a governed state-transition system composed of intent, constraints, structure, capabilities, execution, verification, feedback, and control. Code remains essential, but increasingly functions as one executable projection of a broader program object.

The paper distinguishes code, program, intent, specification, intermediate representation, and world state; reconstructs the conceptual transition from machine instructions and high-level languages to structured, declarative, AI-assisted, and intent-driven programming; and proposes a unified model consisting of intent contracts, semantic representations, structural representations, capability plans, executable artifacts, validators, state deltas, and human-visible feedback. It further formulates minimum criteria for post-textual programming systems: the authoritative program object is not identical to a single text file; multiple views may be reversible projections of one structure; AI suggestions may not bypass a verifiable core; and execution must preserve provenance, permission boundaries, state differences, and recovery paths.

The intent era does not eliminate software engineering. It relocates engineering responsibility from local syntactic correctness toward architecture, contracts, permissions, observability, and the governance of world-state transitions.

**Keywords:** intent-driven programming, post-textual programming, program ontology, AI agents, natural-language programming, intermediate representation, state transition, human–AI collaboration, verifiable execution

---

# 一、問題的提出：程式不再只是一份程式碼

在傳統教科書、開發工具與軟體工程流程中，「程式」與「程式碼」經常被近似使用。人類撰寫某種形式語言，編譯器或直譯器讀取該文本，機器依此產生行為。即使軟體系統實際上還包含設定檔、資料庫、建置腳本、測試、部署環境與操作程序，程式碼仍被視為最主要的權威來源。

這種理解可以簡化為：

$$
\text{Human Intent}
\rightarrow
\text{Source Code}
\rightarrow
\text{Execution}
\rightarrow
\text{Result}
$$

然而，在 AI 協作開發中，真正發生的流程已逐漸變成：

$$
\text{Human Purpose}
\rightarrow
\text{Intent Description}
\rightarrow
\text{Architecture and Constraints}
\rightarrow
\text{AI Expansion}
\rightarrow
\text{Code and Tool Actions}
\rightarrow
\text{Validation}
\rightarrow
\text{State Change}
\rightarrow
\text{Human Feedback}
$$

這兩個流程的差異不只是「中間多了一個 AI」。更深層的改變在於：人類與系統之間的主要操作介面正在上移。人類不再必須完整指定每一步機器指令，而愈來愈常指定：

- 想完成什麼；
- 哪些事情不能做；
- 系統應遵循什麼架構；
- 可以使用哪些工具與權限；
- 結果必須滿足哪些測試；
- 發生失敗時如何停止、回復或升級；
- 完成後應如何向人類說明狀態。

因此，本文的核心問題是：

> 當人類不再主要逐行書寫程式碼，而是定義意圖、結構、限制、驗證與治理條件時，「程式」究竟變成了什麼？

本文拒絕兩種過度簡化。

第一種過度簡化是「程式碼即將消失」。執行系統仍然需要確定性結構、低歧義表示、資源配置、型別、記憶體、權限與錯誤處理。這些內容可能不再全部以人類手寫的文字出現，但不會因此失去必要性。

第二種過度簡化是「AI 只是更好的自動完成」。若 AI 只能補完幾行程式碼，這種說法尚可成立；但當 AI 能讀取專案、修改多個檔案、運行測試、調用工具、維持任務狀態、等待外部事件並改變世界狀態時，它已經參與程式的編譯、規劃與執行。

真正發生的是：

$$
\boxed{
\text{程式碼沒有消失；程式的本體範圍正在擴張。}
}
$$

---

# 二、基本概念與術語區分

為避免「自然語言就是程式」「提示就是規格」「AI 回答就是執行」等概念混淆，本文先建立六個基本定義。

## 2.1 程式碼

**定義 2.1（程式碼）**

程式碼是以某種形式語法表達、可由解析器、編譯器、直譯器或其他執行工具處理的符號工件。

令程式碼集合為：

$$
\mathcal C
$$

其中一個程式碼工件記為：

$$
c\in\mathcal C
$$

程式碼具有至少三種功能：

1. 對機器提供低歧義的操作表示；
2. 對人類提供可閱讀、可修改的外部記憶；
3. 對工具鏈提供可分析、可版本化與可驗證的工件。

程式碼可以是文字，也可以是圖、表、節點結構、位元組碼或其他形式。因此，本文所謂「程式碼」不必狹義限定為純文字，但它仍然只是程式系統中的一種表示。

## 2.2 程式

**定義 2.2（程式）**

程式是能在特定執行環境中，依照某種語義規則產生狀態轉換的可識別結構。

傳統形式可寫為：

$$
P=(c,E)
$$

其中：

- $c$ ：程式碼；
- $E$ ：執行環境。

但在意圖驅動系統中，這個定義過窄。本文提出擴張形式：

$$
\mathbb P
=
\left\langle
I,
K,
R,
A,
V,
E,
F,
G
\right\rangle
$$

其中：

- $I$ ：意圖與目的；
- $K$ ：限制、契約與政策；
- $R$ ：語義及結構表示；
- $A$ ：能力計畫與可執行產物；
- $V$ ：驗證器；
- $E$ ：執行環境；
- $F$ ：回饋與可觀測狀態；
- $G$ ：治理、權限與回復規則。

在此定義下，程式碼只是 $A$ 或 $R$ 的一種投影，不再等於完整程式。

## 2.3 意圖

**定義 2.3（意圖）**

意圖不是一句自然語言命令，而是主體對目標、限制、偏好、成功條件與容許行動的結構化指向。

可寫為：

$$
I
=
\left\langle
g,
n,
c,
p,
s,
t,
r
\right\rangle
$$

其中：

- $g$ ：目標；
- $n$ ：非目標；
- $c$ ：硬限制；
- $p$ ：偏好與優先序；
- $s$ ：成功條件；
- $t$ ：終止條件；
- $r$ ：風險與保留決策。

因此，一句「幫我建立登入系統」不是完整意圖，只是一個意圖入口。完整意圖還必須處理身分驗證方式、資料保存、權限、安全、錯誤回報、可擴充性與驗證條件。

## 2.4 規格與契約

**定義 2.4（規格契約）**

規格契約是將意圖轉換為可檢查義務的形式層，包含輸入、輸出、型別、行為、禁止項、資源、權限與驗證條件。

令規格契約為：

$$
K
=
\left\langle
K_{\mathrm{func}},
K_{\mathrm{arch}},
K_{\mathrm{perm}},
K_{\mathrm{risk}},
K_{\mathrm{test}}
\right\rangle
$$

意圖可以保留一定程度的開放性；契約則負責把不可被自由推測的部分固定下來。

## 2.5 中介表示

**定義 2.5（中介表示）**

中介表示是介於高階意圖與具體執行產物之間，可被分析、轉換、驗證與投影的結構。

本文區分：

$$
\text{Intent IR}
\rightarrow
\text{Semantic IR}
\rightarrow
\text{Structural IR}
\rightarrow
\text{Action IR}
$$

它們分別保存：

- 想做什麼；
- 這件事意味著什麼；
- 它具有何種依賴、型別與結構；
- 執行系統實際要採取哪些行動。

## 2.6 世界狀態

**定義 2.6（世界狀態）**

世界狀態是執行系統可觀測、可修改或可推斷的外部與內部狀態集合。

令世界狀態為：

$$
W_t
$$

一次行動 $a_t$ 造成：

$$
W_{t+1}
=
T(W_t,a_t)
$$

其狀態差分為：

$$
\Delta W_t
=
W_{t+1}-W_t
$$

此處的世界不必是物理世界，也可以是：

- 檔案系統；
- 軟體專案；
- 資料庫；
- 工作流；
- 遊戲世界；
- 模擬環境；
- 組織程序；
- 知識庫；
- 多 Agent 協作空間。

程式的完成，不應只以「模型輸出了一段文字」判定，而應以可驗證的狀態差分判定。

---

# 三、程式概念的六次介面上移

程式設計史不能被壓縮成單一線性階梯，但為了說明本文命題，可以將其抽象為六次主要的介面上移。每一次上移都沒有完全消滅下層，而是把下層封裝、編譯或轉交給新的工具。

## 3.1 第一階段：物理操作與機器指令

早期計算要求人類直接面對硬體限制、指令位置、暫存器與記憶體配置。程式的主要問題是：

> 機器下一步要做什麼？

此時程式與機器操作高度接近：

$$
\text{Human Plan}
\rightarrow
\text{Machine Instruction}
$$

人的意圖必須被完整展開為低階步驟。

## 3.2 第二階段：符號化與高階語言

組合語言、編譯器與高階程式語言將大量低階操作交給工具鏈。人類開始以變數、函式、資料結構與控制流程思考，而不是直接安排每一個機器步驟。

介面變成：

$$
\text{Algorithmic Structure}
\rightarrow
\text{High-Level Code}
\rightarrow
\text{Machine Code}
$$

此時已經發生第一次重要事實：

> 人類不再直接書寫機器真正執行的全部形式。

換言之，「真正執行的東西」與「人類主要編輯的東西」早已分離。

## 3.3 第三階段：結構化、模組化與抽象化

結構化程式設計、模組、物件、型別系統、介面、函式庫與框架，使人類逐漸從局部指令上移到程式結構。

開發者不再只問：

> 這一行怎麼寫？

而開始問：

- 功能應屬於哪個模組；
- 資料如何流動；
- 邊界如何隔離；
- 介面如何穩定；
- 依賴如何控制。

程式開始由指令集合轉變為具有架構的系統。

## 3.4 第四階段：宣告式、規格式與模型式程式設計

資料庫查詢、正規表示式、樣式系統、約束求解、建置系統、基礎設施描述、工作流與模型驅動工具，進一步讓人類描述「想要什麼」，而不是完整描述「每一步怎麼做」。

其形式可寫為：

$$
\text{Desired Property}
\rightarrow
\text{Solver or Runtime}
\rightarrow
\text{Execution Plan}
$$

宣告式程式設計已經證明：意圖上移不是 AI 才出現的現象。AI 只是將這種上移擴大到更開放、更跨領域的語義空間。

## 3.5 第五階段：AI 輔助生成與對話式開發

大型語言模型使自然語言能夠直接觸發程式碼、測試、文件與修改建議。此時人類開始用對話表達需求，AI 則將需求展開為傳統工程工件。

其基本形式為：

$$
u
\rightarrow
M
\rightarrow
c
$$

其中：

- $u$ ：自然語言輸入；
- $M$ ：生成模型；
- $c$ ：程式碼。

但這仍然只是「自然語言到程式碼生成」。若生成後缺乏架構、契約、測試、權限與狀態回報，它仍然只是高速的程式碼生產。

## 3.6 第六階段：意圖驅動與持續 Agent

當 AI 系統具有專案讀取、工具調用、持久記憶、任務規劃、事件等待、測試、部署、狀態觀測與回復能力時，流程不再終止於生成程式碼。

此時變成：

$$
I
\rightarrow
K
\rightarrow
R
\rightarrow
A
\rightarrow
V
\rightarrow
\Delta W
\rightarrow
F
$$

也就是：

```text
意圖
→ 契約
→ 中介表示
→ 能力與行動計畫
→ 驗證
→ 世界狀態差分
→ 人類可見回饋
```

這是本文所稱的「意圖程式時代」。

---

# 四、核心命題：程式介面上移與程式本體擴張

## 4.1 程式介面上移

**命題 4.1（程式介面上移）**

隨著編譯器、函式庫、框架、求解器與 AI Agent 的能力增加，人類主要操作的程式表示將由低階步驟逐漸上移至高階目的、約束、架構與驗證條件。

可表示為：

$$
L_0
\subset
L_1
\subset
L_2
\subset
\cdots
\subset
L_n
$$

其中 $L_i$ 表示某一抽象層。上層不必消除下層，而是透過編譯、展開、求解或執行將其實現。

因此：

$$
\text{Higher-Level Control}
\neq
\text{Lower-Level Disappearance}
$$

意圖驅動不是取消程式碼，而是把人類的主要控制位置上移。

## 4.2 程式本體擴張

**命題 4.2（程式本體擴張）**

在持續 Agent 系統中，若僅保存最終程式碼，而不保存意圖、權限、來源、驗證與狀態差分，系統便無法完整重建其行為意義。因此，程式本體必須擴張。

傳統程式工件常被近似為：

$$
P_{\mathrm{old}}
=
\{c\}
$$

擴張後則為：

$$
P_{\mathrm{new}}
=
\{
I,
K,
R,
A,
V,
E,
F,
G,
H
\}
$$

其中 $H$ 表示歷史、來源與執行軌跡。

這不是說所有元素都必須存在於同一檔案，而是它們共同構成可理解、可重現與可治理的程式系統。

## 4.3 程式碼投影命題

**命題 4.3（程式碼投影命題）**

若存在一個權威結構 $R^\ast$ ，並可從中生成多種等價視圖，則程式碼可以被理解為該結構的一種投影：

$$
\pi_{\mathrm{code}}(R^\ast)=c
$$

其他投影可以是：

$$
\pi_{\mathrm{graph}}(R^\ast)=g
$$

$$
\pi_{\mathrm{math}}(R^\ast)=m
$$

$$
\pi_{\mathrm{explain}}(R^\ast)=e
$$

$$
\pi_{\mathrm{test}}(R^\ast)=t
$$

若各投影可被驗證為指向同一語義核心，則文字不再是唯一權威本體。

## 4.4 意圖不是直接執行許可

**命題 4.4（意圖—執行分離）**

高階意圖本身不應自動取得無限制執行權。意圖必須先經過契約化、權限檢查、風險分析與驗證規劃。

因此：

$$
I
\not\Rightarrow
A_{\mathrm{unbounded}}
$$

合理形式應是：

$$
I
\rightarrow
K
\rightarrow
P_{\mathrm{cap}}
\rightarrow
A_{\mathrm{bounded}}
$$

其中：

- $P_{\mathrm{cap}}$ ：能力與權限計畫；
- $A_{\mathrm{bounded}}$ ：受限制的行動。

這是意圖程式設計與「模型自由發揮」之間的根本差異。

---

# 五、從程式碼中心論到意圖—結構—執行三元論

只以程式碼為中心，容易把所有高階問題都視為程式碼外部的管理事項。但在 Agent 時代，目的、權限與驗證會直接影響系統行為，不能再被視為附註。

本文提出三元模型：

$$
\boxed{
\mathbb P
=
\mathbb I
\otimes
\mathbb S
\otimes
\mathbb X
}
$$

其中：

- $\mathbb I$ ：意圖域；
- $\mathbb S$ ：結構域；
- $\mathbb X$ ：執行域；
- $\otimes$ ：受契約約束的耦合，而非任意拼接。

## 5.1 意圖域

意圖域回答：

- 為什麼做；
- 想達成什麼；
- 不應達成什麼；
- 哪些選擇必須由人類保留；
- 如何判斷完成。

意圖域若缺失，AI 的統計預設便可能替代人類設計意志。

## 5.2 結構域

結構域回答：

- 系統由哪些物件構成；
- 模組與資料如何依賴；
- 型別、形狀、效果與權限如何表示；
- 哪些內容可以轉換；
- 哪些語義不得在投影時遺失。

結構域是意圖與執行之間的穩定層。

## 5.3 執行域

執行域回答：

- 使用哪些工具；
- 以何種順序行動；
- 如何處理失敗；
- 哪些操作需要批准；
- 如何留下軌跡；
- 如何重播或回復。

三者缺一不可。

只有意圖而無結構，系統會模糊。

只有結構而無意圖，系統會失去目的與治理依據。

只有執行而無前兩者，系統會成為不可理解的自動化。

---

# 六、意圖程式的統一形式模型

本文提出一個最小統一模型，用於後續系列展開。

## 6.1 意圖程式物件

定義意圖程式物件：

$$
\mathcal P_I
=
\left\langle
I,
C,
M,
R_s,
R_t,
P_c,
A,
V,
\Delta,
F,
Q
\right\rangle
$$

其中：

- $I$ ：意圖；
- $C$ ：限制與契約；
- $M$ ：上下文、記憶與世界模型；
- $R_s$ ：語義中介表示；
- $R_t$ ：結構中介表示；
- $P_c$ ：能力計畫；
- $A$ ：可執行行動或程式產物；
- $V$ ：驗證集合；
- $\Delta$ ：預期與實際狀態差分；
- $F$ ：人類可見回饋；
- $Q$ ：權限、風險與治理政策。

完整流程為：

$$
I
\xrightarrow{\operatorname{contract}}
C
\xrightarrow{\operatorname{semanticize}}
R_s
\xrightarrow{\operatorname{structure}}
R_t
\xrightarrow{\operatorname{plan}}
P_c
\xrightarrow{\operatorname{lower}}
A
\xrightarrow{\operatorname{execute}}
\Delta W
\xrightarrow{\operatorname{verify}}
V(\Delta W)
\xrightarrow{\operatorname{report}}
F
$$

## 6.2 驗證條件

一個執行不應因「成功產生輸出」就被視為完成。定義完成條件：

$$
\operatorname{Done}(\mathcal P_I)
=
V_{\mathrm{goal}}
\land
V_{\mathrm{constraint}}
\land
V_{\mathrm{permission}}
\land
V_{\mathrm{state}}
\land
V_{\mathrm{report}}
$$

分別表示：

- 目標已達成；
- 限制未被破壞；
- 權限使用合法；
- 世界狀態符合要求；
- 人類已獲得可理解回報。

## 6.3 語義等價

兩個不同表面工件 $a$ 與 $b$ 不必文字相同，只要它們在指定契約下產生等價語義與狀態轉換。

可定義：

$$
a
\equiv_{C,V}
b
$$

若且唯若：

$$
\operatorname{Sem}_C(a)
=
\operatorname{Sem}_C(b)
$$

且：

$$
V
\left(
\Delta W_a,
\Delta W_b
\right)
=
\operatorname{true}
$$

這使文字、節點圖、數學公式與其他投影可以共同指向一個程式本體。

## 6.4 意圖充分性

意圖越短不必然越好。真正重要的是「最小充分意圖」。

令控制訊號為 $s$ ，展開環境為 $\Gamma$ ，目標軌跡為 $\tau^\ast$ 。若：

$$
G(s;\Gamma)=\tau^\ast
$$

且對所有更短訊號 $s'$ ：

$$
|s'|<|s|
\Rightarrow
G(s';\Gamma)\neq\tau^\ast
$$

則 $s$ 可被視為相對於環境 $\Gamma$ 的最小充分控制訊號。

這也說明：短指令能觸發大型系統，不是因為短指令憑空包含全部資訊，而是大量資訊已被前置到記憶、模型、架構、工具、權限與環境中。

---

# 七、什麼是「後文本程式系統」

「後文本」不是反對文字，也不是宣稱未來不再閱讀程式碼。它描述的是：文字不再必然是程式唯一且最高權威的存在形式。

## 7.1 最低判準

本文提出五項最低判準。

### 判準一：結構權威性

系統存在一個可識別、可驗證、可版本化的權威結構：

$$
R^\ast
$$

文字只是：

$$
\pi_{\mathrm{text}}(R^\ast)
$$

### 判準二：多投影一致性

同一程式可以投影為文字、圖形、數學、文件、除錯與人類摘要，且投影之間具有可檢查的語義關係。

### 判準三：語義身分穩定

表面排版或投影變化，不應任意改變程式身分。程式身分應由正規化結構、語義識別與版本關係決定。

### 判準四：確定性核心獨立

AI 可以提出候選、補全意圖、生成轉換與修復方案，但型別、權限、政策、測試與關鍵正確性不能只依賴模型的不可重現判斷。

### 判準五：來源與回復

系統必須知道：

- 誰提出意圖；
- 哪個模型或工具生成了候選；
- 哪些權限被使用；
- 哪些狀態被改變；
- 哪些結果已驗證；
- 如何回復或重播。

滿足這些條件的系統，才有資格稱為後文本程式系統，而不是單純的視覺化編輯器或聊天式程式碼生成器。

## 7.2 文字仍然保留的角色

文字仍具有不可替代的優點：

- 易於版本控制；
- 易於交換；
- 易於搜尋；
- 易於精確引用；
- 易於人類審查；
- 易於建立長期文化與教育體系。

因此，後文本不是：

$$
\text{Text}\rightarrow 0
$$

而是：

$$
\text{Text}
\subset
\text{Projection Set}
$$

文字從唯一程式本體，轉變為多種可靠投影之一。

---

# 八、人類與 AI 的新分工

## 8.1 人類操作位置的變化

傳統開發者主要負責：

- 寫語法；
- 寫函式；
- 管理資料結構；
- 手動整合模組；
- 找出局部錯誤。

意圖時代的人類責任將更加集中於：

- 定義目的與非目的；
- 建立架構邊界；
- 聲明設定與權限；
- 指定驗證標準；
- 判斷風險；
- 保留不可代理決策；
- 評估狀態改變是否可接受。

這不是減少人類責任，而是責任上移。

## 8.2 AI 的合理角色

AI 適合負責：

- 把模糊意圖轉成候選結構；
- 發現遺漏條件；
- 生成多種實作候選；
- 建立程式碼與測試；
- 分析依賴；
- 操作工具；
- 整理執行軌跡；
- 把機器狀態轉譯成人類狀態。

AI 不應在未經授權與驗證時：

- 自行決定不可逆目標；
- 靜默擴大權限；
- 將推測當成契約；
- 將生成結果當成已驗證結果；
- 隱藏狀態差分；
- 以「模型認為正確」取代確定性檢查。

## 8.3 三層認知架構的升級

既有宏觀、中觀、微觀三層架構可在意圖時代升級為：

$$
\text{Macro}
=
\text{Purpose, Value, Strategy}
$$

$$
\text{Meso}
=
\text{Architecture, Contract, Capability}
$$

$$
\text{Micro}
=
\text{Code, Tool Action, Test, Patch}
$$

人類可以把部分微觀工作交給 AI，但不能因此放棄宏觀與中觀責任。相反地，若人類不表達宏觀與中觀決策，AI 的預設模式就會成為隱性架構。

---

# 九、意圖時代的七種錯誤理解

## 9.1 「自然語言已經等於程式語言」

自然語言可成為意圖入口，也可以在具有記憶、上下文與行動能力的系統中造成狀態轉換；但它通常仍具有歧義、語境依賴與不完整性。

因此：

$$
\text{Natural Language}
\neq
\text{Automatically Safe Executable Language}
$$

正確架構是：

$$
\text{Natural Language}
\rightarrow
\text{Controlled Intent}
\rightarrow
\text{IR}
\rightarrow
\text{Validation}
\rightarrow
\text{Execution}
$$

## 9.2 「AI 生成得出程式碼，就代表理解了需求」

模型可以生成形式合理的程式碼，但生成成功不等於目標對齊。若沒有成功條件與禁止項，模型只能用常見模式補足空白。

## 9.3 「程式碼不再重要」

即使人類不直接閱讀所有程式碼，執行系統仍需要低歧義結構。程式碼、IR、型別圖或其他形式會繼續存在，只是其生產者與權威位置可能改變。

## 9.4 「模型可以同時當編譯器、執行器與驗證器」

若同一模型生成方案、執行方案並自行宣告方案正確，系統便缺乏獨立檢查。合理架構必須分離：

$$
\text{Generator}
\neq
\text{Validator}
$$

至少在安全、權限與關鍵正確性上，驗證器必須具有可重現規則。

## 9.5 「提示越短越高級」

短提示只有在共享上下文足夠穩定時才有效。否則它只是把大量未聲明決策交給模型猜測。

## 9.6 「Agent 完成操作就等於完成協作」

若人類不知道 Agent 改了什麼、測了什麼、沒測什麼、如何確認與如何回復，就不存在完整協作。

因此：

$$
\text{Execution}
+
\text{Human-Visible State}
=
\text{Collaborative Completion}
$$

## 9.7 「只要保留最終檔案就能重現工作」

Agent 行動可能依賴模型版本、工具、權限、外部資料、上下文與中間決策。只保存最終檔案，無法完整重建其來源與風險。

---

# 十、意圖程式系統的風險模型

## 10.1 隱性架構轉移

當人類未聲明架構時，AI 的統計預設會填補空白：

$$
\text{Missing Human Decision}
\rightarrow
\text{Model Default}
\rightarrow
\text{Hidden Architecture}
$$

這是一種設計權力的靜默轉移。

## 10.2 意圖漂移

在長任務中，初始意圖可能經過多輪摘要、規劃與修改而逐漸改變。令初始意圖為 $I_0$ ，第 $t$ 輪意圖表示為 $I_t$ ，則需監控：

$$
d(I_0,I_t)
$$

若距離超過容許閾值：

$$
d(I_0,I_t)>\epsilon
$$

系統應停止、回報或要求重新確認。

## 10.3 投影損失

高維結構轉為文字或自然語言時可能遺失資訊。令投影為 $\pi$ ，重建為 $\rho$ ，則投影損失可寫為：

$$
L_{\pi}
=
d
\left(
R,
\rho(\pi(R))
\right)
$$

後文本系統必須顯示投影損失，而不能假設所有視圖完全等價。

## 10.4 權限擴張

Agent 可能為了完成目標而自行尋求更多能力。若能力集合由 $A_t$ 擴張為 $A_{t+1}$ ，則必須符合政策：

$$
A_{t+1}
\subseteq
\operatorname{Allowed}(I,C,Q)
$$

任何超出範圍的能力都應要求顯性批准。

## 10.5 不可見性債

若機器狀態愈來愈複雜，但人類可見狀態沒有同步提升，便產生不可見性債。

可抽象表示為：

$$
D_{\mathrm{invisible}}
=
C_{\mathrm{machine}}
-
C_{\mathrm{human\ visible}}
$$

當差距持續增大，人類對系統的實際治理能力就會下降。

---

# 十一、可證偽命題與研究綱領

本文不是宣告一個不可反駁的未來敘事，而提出可被工程實驗檢查的研究命題。

## 11.1 假說一：意圖契約能降低架構漂移

比較兩組 AI 開發任務：

- A 組只提供自然語言需求；
- B 組提供目標、非目標、架構、設定、權限與測試契約。

測量：

- 未聲明依賴數量；
- 架構違反次數；
- 重構成本；
- 後續 Agent 接手成功率。

若 B 組沒有顯著改善，則意圖契約的工程價值需要重新評估。

## 11.2 假說二：結構權威能提高多視圖一致性

比較：

- 以文字檔案為唯一權威；
- 以結構化程式圖為權威並生成多種投影。

測量：

- round-trip 語義損失；
- 重構後等價性；
- 圖形與文字不同步率；
- 跨語言投影錯誤率。

## 11.3 假說三：獨立驗證器能降低模型自證錯誤

比較：

- 模型生成後自行判斷完成；
- 模型生成後由確定性測試、型別、政策與狀態檢查判斷完成。

測量誤報成功率與未發現破壞率。

## 11.4 假說四：人類可見狀態層能提高接管能力

測量人類在不閱讀完整終端機日誌的情況下，能否回答：

- 系統改了什麼；
- 哪些內容已驗證；
- 目前風險為何；
- 如何撤銷；
- 下一步需要什麼決策。

## 11.5 假說五：程式碼產量可能上升，但人類直接編寫比例下降

意圖時代不一定使程式碼總量下降。AI 可能生成更多測試、適配器、追蹤與防護程式碼。真正改變的可能是：

$$
\frac{
\text{Human-Written Code}
}{
\text{Total Executable Artifacts}
}
\downarrow
$$

同時：

$$
\frac{
\text{Human-Governed Intent and Constraints}
}{
\text{Total High-Level Decisions}
}
$$

應維持或上升。若後者下降，則所謂意圖程式設計可能只是設計權外包。

---

# 十二、工程架構：意圖時代的最小完整管線

本文建議後續系統採用以下最小管線：

```text
Human Purpose
    ↓
Intent Contract
    ↓
Semantic IR
    ↓
Structural IR
    ↓
Capability and Permission Plan
    ↓
Executable Artifact / Action IR
    ↓
Deterministic Validation Gates
    ↓
State Delta
    ↓
Human-Visible State
    ↓
Approval / Revision / Rollback
```

其形式為：

$$
\boxed{
\text{Purpose}
\rightarrow
\text{Intent}
\rightarrow
\text{Contract}
\rightarrow
\text{Semantic IR}
\rightarrow
\text{Structural IR}
\rightarrow
\text{Capability Plan}
\rightarrow
\text{Action}
\rightarrow
\text{State Delta}
\rightarrow
\text{Feedback}
}
$$

這條管線有三個不可被省略的閉環。

## 12.1 意圖閉環

$$
\text{Purpose}
\rightarrow
\text{Intent}
\rightarrow
\text{Clarification}
\rightarrow
\text{Confirmed Intent}
$$

## 12.2 執行閉環

$$
\text{Plan}
\rightarrow
\text{Action}
\rightarrow
\text{Observation}
\rightarrow
\text{Plan Revision}
$$

## 12.3 治理閉環

$$
\text{State Delta}
\rightarrow
\text{Human-Visible State}
\rightarrow
\text{Human Decision}
\rightarrow
\text{Continue / Stop / Rollback}
$$

只具備第一個閉環的系統是對話助手。

具備前兩個閉環的系統是 Agent。

同時具備三個閉環，才接近可治理的意圖程式系統。

---

# 十三、與 EML、Nova、ICL 與 HVSL 的關係

本文不把既有理論粗暴合併成單一超級語言，而將它們放置於不同層次。

## 13.1 EML

EML 處理語意如何附著於宿主物件、如何形成宿主中立語義表示，以及如何投影到不同語言、工作流、資料或介面。

在本文架構中，EML 主要位於：

$$
\text{Intent}
\rightarrow
\text{Semantic IR}
$$

以及：

$$
\text{Host Object}
+
\text{Semantic Overlay}
\rightarrow
\text{Semantic Graph}
$$

## 13.2 Nova

Nova 處理程式是否可以直接以型別化結構圖存在，而不是先以文字存在。

在本文架構中，Nova 主要位於：

$$
\text{Semantic IR}
\rightarrow
\text{Structural IR}
\rightarrow
\text{Executable Projection}
$$

## 13.3 ICL

ICL 處理人類如何把目標、架構、設定、限制、輸出協議與驗證要求明確化，使 AI 不必用預設模式替代人類決策。

在本文架構中，ICL 位於：

$$
\text{Human Purpose}
\rightarrow
\text{Intent Contract}
$$

## 13.4 HVSL

HVSL 處理執行後的機器狀態如何被轉譯成人類可理解、可驗證、可操作與可回復的狀態。

在本文架構中，HVSL 位於：

$$
\text{Machine State}
\rightarrow
\text{Human-Visible State}
$$

## 13.5 自然語言原生計算

自然語言原生計算論說明：對具有記憶、上下文、目標與行動能力的智能體而言，語言事件可以直接改變策略、記憶與世界狀態。

本文承接此命題，但增加工程限制：

$$
\text{Language Event}
\rightarrow
\text{Candidate State Transition}
$$

不等於：

$$
\text{Language Event}
\rightarrow
\text{Unrestricted Authorized Action}
$$

自然語言可以參與計算，但仍需契約、權限與驗證。

---

# 十四、對程式教育與職業分工的含義

## 14.1 程式教育不應只教語法

若 AI 能大量生成局部程式碼，教育重心應更加重視：

- 問題分層；
- 架構；
- 狀態模型；
- 契約；
- 型別與不變量；
- 測試；
- 權限；
- 失敗處理；
- 驗證與可觀測性。

語法仍需學習，但它不應是全部。

## 14.2 程式設計師不會簡單消失

「程式設計師」可能分化為：

- 意圖架構師；
- 語義與 IR 設計者；
- Agent Runtime 工程師；
- 驗證與政策工程師；
- 世界狀態設計者；
- 人類可見狀態設計者；
- 執行與資源工程師；
- 專業領域意圖編譯者。

局部程式碼生產可能高度自動化，但對目的、結構與風險的判斷不會因此自動消失。

## 14.3 不可代理選擇

任何主體都不應永久替另一主體完成其不可撤回選擇。映射到程式系統中，涉及：

- 不可逆刪除；
- 高風險資金行動；
- 身分與權利改變；
- 公開發布；
- 法律承諾；
- 重大安全設定；
- 對他者造成持續影響的決策。

這些行動即使可以由 Agent 技術性執行，也不代表它應取得最終決定權。

---

# 十五、本文的七項總命題

本文可濃縮為七項命題。

## 命題一

$$
\boxed{
\text{Program}
\neq
\text{Code Alone}
}
$$

## 命題二

$$
\boxed{
\text{Code}
=
\text{One Executable Projection of a Broader Program Object}
}
$$

## 命題三

$$
\boxed{
\text{Intent-Driven Programming}
\neq
\text{Unrestricted Natural-Language Execution}
}
$$

## 命題四

$$
\boxed{
\text{Higher Abstraction}
\neq
\text{Lower-Layer Elimination}
}
$$

## 命題五

$$
\boxed{
\text{AI Generation}
\neq
\text{Independent Verification}
}
$$

## 命題六

$$
\boxed{
\text{Execution Completion}
\neq
\text{Collaborative Completion}
}
$$

## 命題七

$$
\boxed{
\text{The Future Core of Programming}
=
\text{Intent}
+
\text{Structure}
+
\text{Verification}
+
\text{Governed State Transition}
}
$$

---

# 十六、結論：程式設計的終點不是少寫幾行程式碼

程式設計的演化，從來不只是讓人少寫一些符號。組合語言、高階語言、編譯器、函式庫、框架、宣告式系統與 AI 生成工具，都在持續改變人類與機器之間的控制介面。

意圖時代真正的重要變化，不是自然語言看起來更像魔法，也不是程式碼會從世界上消失，而是：

> 人類開始把目的、限制、架構、權限與驗證條件直接置於程式系統的上層；AI、編譯器、驗證器與 Runtime 則共同把這些高階內容展開為可執行且可治理的狀態轉換。

因此，程式設計正在從：

$$
\text{How to write the instructions}
$$

逐漸轉向：

$$
\text{How to govern the transformation}
$$

未來最關鍵的問題不再只是：

> 這段程式碼怎麼寫？

而是：

> 誰提出了什麼意圖？  
> 哪些條件不可違反？  
> 哪些決策可以代理，哪些必須保留？  
> 系統如何把意圖編譯為結構與行動？  
> 執行後世界究竟改變了什麼？  
> 人類如何理解、驗證、拒絕或回復這些改變？

這就是從程式碼到意圖的真正轉換。

程式碼不會因此死亡。它會被重新定位。

文字也不會因此消失。它會成為多種投影之一。

人類也不會因 AI 能寫程式而失去作用。真正的問題是，人類是否能把自己的目的、邊界與責任提升到足以治理更強大執行系統的位置。

《意圖—結構—世界程式論》的後續工作，將依序處理自然語言原生計算、形式化壓縮、語意附加、後文本結構、符號算子、意圖中介表示、時空控制、Agent Runtime、可編譯世界、人類可見狀態與意圖程式文明。本文作為第一篇，只建立最根本的起點：

$$
\boxed{
\text{程式碼是重要的，但程式比程式碼更大。}
}
$$

---

# 附錄 A：最小意圖契約範本

```yaml
intent:
  goal:
  non_goals:
  target_state:
  success_conditions:

architecture:
  allowed_modules:
  forbidden_dependencies:
  interfaces:
  invariants:

permissions:
  allowed_tools:
  allowed_resources:
  prohibited_actions:
  approval_required:

execution:
  preferred_strategy:
  stop_conditions:
  retry_policy:
  rollback_policy:

verification:
  tests:
  state_checks:
  security_checks:
  human_review:

feedback:
  summary_required:
  changed_items:
  verified_items:
  unverified_items:
  risks:
  rollback_instructions:
```

---

# 附錄 B：系列十二篇位置

1. **從程式碼到意圖：程式概念的歷史轉換與後文本時代**
2. 自然語言原生計算：從語句生成到語義狀態轉換
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

1. Neo.K，《程式語言設計開發的普適方法論：三層認知架構的理論建構與實踐路徑》，2025。
2. Neo.K，《意圖協作層（Intent Collaboration Layer, ICL）：Vibe Coding、意圖語言與 AI 協作開發的意識層方法論》，2026。
3. Neo.K，《HVSL：人類可見狀態層——Agent 不得把終端機當成使用者介面》，2026。
4. Neo.K with Aletheia，《自然語言原生計算論：從語義狀態轉換、上下文算子到互動式執行》，2026。
5. Neo.K，《從高維意圖到一念即成：最小充分意圖原理與單符號宇宙統一框架》，2026。
6. Neo.K，《程式設計—意圖語言—AI Agent—時空切片理論群總索引》，2026。
7. Neo.K，《EML Universal Semantic Overlay 2026 v2.0》，2026。
8. Neo.K，《EML Dual Profile Architecture：EML-P／EML-U v1.0》，2026。
9. Neo.K，《Nova Core Baseline v3.0：統合前正式核心規格》，2026。
10. Neo.K，《Nova Unified Roadmap v1.0：新版計畫書與 AI 原生張量語言統合架構》，2026。

## 一般理論背景

11. Turing, A. M., “On Computable Numbers, with an Application to the Entscheidungsproblem,” 1936.
12. Backus, J., “Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs,” 1978.
13. Brooks, F. P., “No Silver Bullet: Essence and Accidents of Software Engineering,” 1987.
14. Wegner, P., “Why Interaction Is More Powerful Than Algorithms,” 1997.
15. Fowler, M., *Domain-Specific Languages*, 2010.
16. Gamma, E., Helm, R., Johnson, R., and Vlissides, J., *Design Patterns: Elements of Reusable Object-Oriented Software*, 1994.

---

# 版本紀錄

## v0.1 — 2026-07-24

- 完成系列第一篇總導論。
- 建立程式碼、程式、意圖、契約、中介表示與世界狀態的基本區分。
- 提出程式介面上移、程式本體擴張與程式碼投影命題。
- 定義後文本程式系統的五項最低判準。
- 建立意圖程式物件與最小完整執行管線。
- 加入可證偽假說、風險模型與系列十二篇位置。
