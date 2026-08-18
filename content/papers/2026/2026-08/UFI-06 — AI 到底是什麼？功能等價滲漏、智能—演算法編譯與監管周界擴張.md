# UFI-06 — AI 到底是什麼？功能等價滲漏、智能—演算法編譯與監管周界擴張

## What Counts as AI? Functional-Equivalence Leakage, Intelligence-to-Algorithm Compilation, and Regulatory Perimeter Expansion

**系列：** 不可凍結的智能：AI 工具終局論、競爭棘輪與後人類轉型  
**English Series:** *The Unfreezable Intelligence: Tool-Finality, Competitive Ratchets, and the Posthuman Transition*  
**系列代碼：** UFI  
**論文序號：** 06 / 08  
**版本：** v1.0 Canonical Expanded Edition  
**日期：** 2026-08-18  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**前置理論：** UFI-01—05；CompilableWorld；超大型階層式有限狀態世界；持續世界狀態；PGMV  
**文件地位：** AI Definition / Functional Equivalence / Regulatory Boundary Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文不是法律意見，也不試圖替任何特定軟體在特定司法管轄區作出最終法律分類。2026 年「什麼算 AI」仍高度依賴具體法規、技術架構、推論方式、自治程度、用途與風險。歐盟 AI Act 已採用以 machine-based、autonomy、adaptiveness、objectives 與 inference 為核心的法律定義，並明確排除一部分只依自然人預先定義規則自動執行的傳統軟體；OECD 則同時承認 AI / non-AI 之間沒有天然、跨時代的清楚紅線。本文提出的是更一般的治理問題：**如果同一功能可透過不同技術路徑實現，而 AI 又可以把自己的部分能力編譯成 ordinary executable code、規則庫、狀態機、planner 或 symbolic system，那麼僅依「AI 這個名字」畫禁止線，可能產生功能等價滲漏；若監管因此轉向能力與風險，周界又會自然擴張到部分非 AI 計算系統。**

---

## 摘要

UFI-04 已指出：

$$
\boxed{
\text{Freeze one capability input}
\not\Rightarrow
\text{Freeze overall capability}.
}
$$

UFI-05 再指出：

$$
\boxed{
\text{即使沒有外部違約，社會內部也可能因 AI 的益處與依賴重新要求能力前進。}
}
$$

但如果真的有人說：

> 好。那我們不只禁止更強的大模型；我們直接禁止「更強 AI」。

問題立刻變成：

$$
\boxed{
\textbf{什麼叫 AI？}
}
$$

這不是文字遊戲。

2024 OECD 對 AI 定義的解釋直接承認：

$$
\boxed{
\text{AI 與 non-AI 並沒有一條天然清楚紅線。}
}
$$

某些過去被視為 AI 的技術，例如 OCR，今天在公共語言中已經常被視為普通軟體。

另一方面，歐盟 AI Act 又必須為執法建立實務邊界，因此在 Article 3(1) 將 AI system 定義為：

$$
\boxed{
\text{machine-based}
+
\text{varying autonomy}
+
\text{possible adaptiveness}
+
\text{objectives}
+
\text{inference from input to output}.
}
$$

Recital 12 並指出，不應把「只依自然人定義規則自動執行操作」的 simpler traditional software 全部納入。

這產生一個非常有意思的中間區。

考慮一個大型動態世界系統：

$$
\boxed{
W_{t+1}
=
F(
W_t,
A_t,
E_t,
H_t
),
}
$$

其中：

- $W_t$：世界狀態；
- $A_t$：玩家／Agent 行為；
- $E_t$：外部事件；
- $H_t$：歷史狀態。

它可以包含：

- 一億個狀態變數；
- 階層式 finite-state machines；
- planner；
- event scheduler；
- symbolic rules；
- deterministic economics；
- faction relationships；
- NPC memory tables；
- rule-based behavior trees；
- rollback；
- event sourcing。

這個系統可以非常複雜。

但：

$$
\boxed{
\text{Complexity}
\neq
\text{AI classification}.
}
$$

如果所有 runtime transition 都只是執行已存在的確定規則：

$$
W_{t+1}
=
F_{\mathrm{fixed}}(W_t),
$$

它可能更接近傳統軟體／狀態機。

如果系統從資料：

- 學 transition；
- derive model；
- infer policy；
- dynamically adapt；

則更接近 AI system。

但接著出現本文真正的問題：

> **如果這套超複雜規則，是 AI 幫人類寫出來的呢？**

假設開發階段：

$$
\boxed{
AI
:
Spec
\rightarrow
Program.
}
$$

然後 deployment 時：

$$
\boxed{
Program
:
Input
\rightarrow
Output
}
$$

完全不呼叫 AI。

則：

$$
\boxed{
\text{Development Origin}
\neq
\text{Runtime Nature}.
}
$$

本文稱：

$$
\boxed{
\textbf{Development-Origin–Runtime-Nature Separation}.
}
$$

概念上：

$$
\boxed{
BuiltByAI(X)
\not\Rightarrow
RunsAsAI(X).
}
$$

這不是一條具體法域的法律結論。

尤其歐盟 Recital 12 的「rules defined solely by natural persons」使 AI-generated static rules 的分類本身變得更值得解釋。

本文要指出的是：

> **AI 可以參與產生一個最終在 runtime 中完全以 ordinary algorithmic execution 運作的 artefact。**

而這已經不是假設。

2025–2026 的 code-generation / program-synthesis 研究已經在：

- game rules；
- robotics；
- autonomous-driving simulations；
- hardware FSM；
- public-benefit rules；

中展示：

$$
\boxed{
\text{natural language}
\rightarrow
\text{executable symbolic program}.
}
$$

2026 ICLR 的 *Code World Models for General Game Playing* 直接讓 LLM 將遊戲規則與軌跡轉為 Python executable world model，再交給 classical planner 搜尋。

2026 LLM-FSM 則研究：

$$
\boxed{
\text{Natural Language Specification}
\rightarrow
\text{Finite-State Machine RTL}.
}
$$

這和本文要描述的機制幾乎完全同型。

因此本文正式提出：

$$
\boxed{
\textbf{Intelligence-to-Algorithm Compilation}
}
$$

簡寫：

$$
\boxed{
IAC.
}
$$

中文：

**智能—演算法編譯。**

定義：

若高能力 AI：

$$
A
$$

把某個原本需要其 online reasoning 的功能：

$$
f
$$

轉譯／壓縮／編譯為一個較靜態、可驗證、可直接執行的 artefact：

$$
P_f,
$$

使：

$$
\boxed{
P_f(x)
\approx
A_f(x)
}
$$

在某個 bounded domain 成立，則稱：

$$
\boxed{
A_f
\xrightarrow{\mathsf{Compile}}
P_f.
}
$$

 $P_f$ 可以是：

- source code；
- lookup table；
- symbolic program；
- finite-state machine；
- policy tree；
- planner domain；
- rules engine；
- decision graph；
- workflow；
- constraint system。

這不表示：

$$
P_f=A.
$$

而是：

$$
\boxed{
\text{某些 intelligence-dependent development effort}
}
$$

可以留下：

$$
\boxed{
\text{non-neural / non-generative / ordinary executable residue}.
}
$$

本文稱這個 residue：

$$
\boxed{
\textbf{Compiled Capability Residue}.
}
$$

即：

$$
\boxed{
R_C(A)
=
\{
P_f:
A_f\rightarrow P_f
\}.
}
$$

這會直接破壞一個天真的禁止模型：

$$
\boxed{
\text{Ban AI Runtime}
\Rightarrow
\text{Ban AI-like Function}.
}
$$

不成立。

因為：

$$
\boxed{
\text{AI runtime}
}
$$

可能在開發期出現，

但最終：

$$
\boxed{
\text{capability}
}
$$

以 ordinary code 留下來。

本文將此稱為：

$$
\boxed{
\textbf{Functional Equivalence Leakage}.
}
$$

若法規禁止：

$$
T_A
$$

某種 AI 技術類別，

但允許：

$$
T_B,
$$

且：

$$
\boxed{
F(T_B)
\approx
F(T_A),
}
$$

則功能從禁止邊界「漏」到未禁止技術類別。

注意：

$$
\boxed{
\text{Functional equivalence}
\neq
\text{architectural identity}.
}
$$

一個大型 deterministic state machine 可以在某些 bounded game domain 看起來「很智能」，

但它可能：

- 不會學；
- 不會 generalized inference；
- 不會 transfer；
- 不會自然語言理解。

它只是在：

$$
\boxed{
\mathcal D_{bounded}
}
$$

中實現等價功能。

因此本文用：

$$
\boxed{
\approx_F
}
$$

表示：

**task-relative functional equivalence。**

$$
X\approx_FY
$$

不表示：

$$
X=Y.
$$

---

# 一、AI 定義本身就是動態邊界

OECD 2024 直接指出：

> 沒有一條清楚 AI / non-AI red line。

這可寫為：

$$
\boxed{
AI/NonAI
\neq
\text{natural binary kind}.
}
$$

至少在政策分類上，它更像：

$$
\boxed{
\text{continuum + operational legal threshold}.
}
$$

---

# 二、AI Effect

歷史上很多：

- OCR；
- search；
- spell checking；
- route planning；

一旦成熟，

公共語言就不再叫 AI。

本文稱：

$$
\boxed{
\textbf{AI Normalization Drift}.
}
$$

---

# 三、AI Boundary Drift

令：

$$
\mathcal B_{AI}(t)
$$

為時間 $t$ 被社會／法律／產業視為 AI 的邊界。

則：

$$
\boxed{
\mathcal B_{AI}(t)
\neq
\mathcal B_{AI}(t+\Delta t).
}
$$

---

# 四、公共語言邊界和法律邊界也不同

$$
\boxed{
\mathcal B_{public}
\neq
\mathcal B_{legal}.
}
$$

---

# 五、OECD 定義

核心：

$$
\boxed{
\text{machine-based}
+
\text{objectives}
+
\text{inference}
+
\text{outputs}.
}
$$

---

# 六、EU AI Act

額外強調：

- varying autonomy；
- possible adaptiveness；
- inference。

---

# 七、Traditional Software Exclusion

EU Recital 12：

只依自然人定義規則自動執行的 simpler traditional software 不應被納入。

---

# 八、所以「複雜」本身不夠

一億條 if：

$$
\boxed{
\text{HugeRuleCount}
\not\Rightarrow
AI.
}
$$

---

# 九、Finite State Machine

FSM：

$$
S_{t+1}
=
\delta(
S_t,X_t
).
$$

可以非常大。

---

# 十、Hierarchical FSM

$$
\delta
=
\{
\delta_1,\ldots,\delta_n
\}
$$

巢套。

---

# 十一、Behavior Tree

也是 classic game-AI architecture。

---

# 十二、Planning

這裡開始模糊。

OECD 明確把：

- combinatorial problem-solving；
- planning algorithms；

放入 AI system objective examples。

---

# 十三、所以「rule-based」不是自動等於 non-AI

knowledge-based / symbolic inference 也可以是 AI。

---

# 十四、Key distinction

不是：

$$
ML
\quad vs\quad
Rules.
$$

---

# 十五、而更接近：

$$
\boxed{
\text{mere automatic execution}
\quad vs\quad
\text{inference / model derivation / AI-type decision machinery}.
}
$$

具體法律分類仍需個案。

---

# 十六、Dynamic World State Machine

本文案例：

$$
W_{t+1}
=
F(W_t,A_t,E_t,H_t).
$$

---

# 十七、Level 0

explicit transitions only。

---

# 十八、Level 1

rules + classical search。

---

# 十九、Level 2

symbolic planning。

---

# 二十、Level 3

learned policy。

---

# 二十一、Level 4

LLM / model-driven dynamic inference。

---

# 二十二、World-System Continuum

$$
\boxed{
W^{(0)}
\rightarrow
W^{(1)}
\rightarrow
W^{(2)}
\rightarrow
W^{(3)}
\rightarrow
W^{(4)}.
}
$$

---

# 二十三、No clean intuitive line

某些 legal line 仍可畫。

但技術功能呈 continuum。

---

# 二十四、Internal CompilableWorld link

既有理論：

```text
Natural Language
→ AI Action Compilation
→ Action IR
→ Validation
→ Scheduler
→ Hierarchical State Machine
→ Events
→ World Difference
→ Narrative Output
```

---

# 二十五、在這個架構中

AI 不一定是 world truth engine。

---

# 二十六、AI 可以只做 compiler

$$
\boxed{
Language
\rightarrow
FiniteActionSpace.
}
$$

---

# 二十七、底層世界仍 deterministic

---

# 二十八、AI-Assisted World ≠ AI-Run World

$$
\boxed{
AI\text{-}AssistedDevelopment
\neq
AI\text{-}Runtime.
}
$$

---

# 二十九、Development-Origin–Runtime-Nature Separation

$$
\boxed{
Origin(X)
\neq
RuntimeClass(X).
}
$$

---

# 三十、AI 生成 calculator

calculator 不因此擁有 LLM runtime。

---

# 三十一、AI 生成 sorting algorithm

sorting algorithm 仍是 sorting algorithm。

---

# 三十二、AI 生成巨大 state machine

分類需要看 system itself。

---

# 三十三、但 legal ambiguity remains

因一些定義會考慮 build-phase inference。

---

# 三十四、因此本文不提供法律 escape route

---

# 三十五、它只指出 classification dimension 必須分：

$$
\boxed{
Development,
Architecture,
Runtime,
Capability,
Use.
}
$$

---

# 三十六、五維分類

本文提出：

$$
\boxed{
\mathbf C_S
=
(
C_D,
C_A,
C_R,
C_F,
C_U
).
}
$$

其中：

- $C_D$：development origin；
- $C_A$：architecture；
- $C_R$：runtime inference；
- $C_F$：functional capability；
- $C_U$：use / deployment context。

---

# 三十七、AI 定義若只看一維會失真

---

# 三十八、Intelligence-to-Algorithm Compilation

$$
A_f
\xrightarrow{\mathsf{Compile}}
P_f.
$$

---

# 三十九、Program synthesis already does this

LLM：

$$
Spec
\rightarrow
Code.
$$

---

# 四十、Code World Models

LLM：

$$
GameRules
\rightarrow
PythonWorldModel.
$$

---

# 四十一、classical planner then operates

---

# 四十二、Hybrid Separation

$$
\boxed{
\text{AI-generated model}
+
\text{classical search}
}
$$

不等於一個單一 architecture。

---

# 四十三、World Model as Code

2026 game CWM：

state + legal actions + transition + reward。

---

# 四十四、這正是 bounded intelligence compilation

---

# 四十五、LLM-FSM

natural language：

$$
\rightarrow
RTL FSM.
$$

---

# 四十六、Rules-as-Code

LLM：

policy text：

$$
\rightarrow
machine-readable code.
$$

---

# 四十七、Robotics

LLM：

task instruction：

$$
\rightarrow
executable code policy.
$$

---

# 四十八、Therefore

IAC is not science fiction。

---

# 四十九、But correctness problem

AI-generated code can be wrong。

---

# 五十、Verified Capability Residue

只有經：

- tests；
- formal verification；
- bounded domain validation；

後才是可靠 residue。

---

# 五十一、Define:

$$
\boxed{
R_C^{verified}(A).
}
$$

---

# 五十二、Compiler Fallibility

$$
\boxed{
AI\ intelligence
\not\Rightarrow
compiled\ program\ correctness.
}
$$

---

# 五十三、Code World Model 2026 follow-up

即使 transition accuracy 98%+

關鍵錯誤仍可讓 planner 系統性輸。

---

# 五十四、所以 IAC 不是萬能蒸餾

---

# 五十五、Bounded Domain Requirement

越窄 domain：

$$
P_f
$$

越可能接近 AI function。

---

# 五十六、General AI harder to compile into finite rules

---

# 五十七、Domain-Bounded Equivalence

$$
\boxed{
P_f\approx_{\mathcal D}A_f.
}
$$

---

# 五十八、outside $\mathcal D$

不保證。

---

# 五十九、Functional Equivalence Leakage

法規：

$$
Ban(T_A).
$$

---

# 六十、Engineer seeks：

$$
T_B
$$

使：

$$
T_B\notin Ban
$$

但：

$$
F(T_B)\approx_FF(T_A).
$$

---

# 六十一、這不是必然惡意

可能是：

- compliance engineering；
- legacy migration；
- cost reduction；
- safety hardening。

---

# 六十二、但也可成 regulatory arbitrage

---

# 六十三、Regulatory Arbitrage

2025 legal literature 已研究 AI 法規競爭、套利與 fragmentation。

---

# 六十四、Taxonomy Arbitrage

本文特別提出：

$$
\boxed{
\textbf{Taxonomy Arbitrage}.
}
$$

即：

> 不是跨國搬家，而是改 architecture 以落到另一分類。

---

# 六十五、Example

禁止 adaptive model。

改：

$$
\text{offline AI-generated static policy}.
$$

---

# 六十六、Risk may remain

---

# 六十七、Architecture Laundering

本文稱更極端版本：

$$
\boxed{
\textbf{Architecture Laundering}.
}
$$

不是法律指控詞，

是理論用語：

> 將高風險功能透過 architecture conversion 轉成形式上不同類別。

---

# 六十八、Need careful

不同 architecture 可能真的降低風險。

---

# 六十九、Static program can be safer

- predictable；
- auditable；
- bounded。

---

# 七十、所以 architecture conversion 不一定是 loophole

---

# 七十一、Safety-Preserving Compilation

如果 AI：

$$
\rightarrow
\text{verified FSM}
$$

反而可能降低 hallucination。

---

# 七十二、CompilableWorld 就是這種方向

AI 做 language compiler，

world rules remain typed / verifiable。

---

# 七十三、Thus:

$$
\boxed{
\text{Functional equivalence}
\neq
\text{Risk equivalence}.
}
$$

---

# 七十四、Functional–Risk Separation

$$
\boxed{
X\approx_FY
\not\Rightarrow
Risk(X)=Risk(Y).
}
$$

---

# 七十五、非常重要

否則 capability regulation 會過度粗糙。

---

# 七十六、Risk Surface

定義：

$$
\boxed{
\mathbf R_X
=
(
R_{autonomy},
R_{opacity},
R_{adaptivity},
R_{scale},
R_{harm},
R_{irreversibility}
).
}
$$

---

# 七十七、兩個同功能系統

可以不同風險。

---

# 七十八、Example

LLM autonomous hiring

vs deterministic scoring rule

功能近似：

decision support。

---

# 七十九、但 opacity / adaptivity 不同。

---

# 八十、Nevertheless harms can both exist

bias can exist in rules too。

---

# 八十一、AI Risk ≠ Automation Risk

$$
\boxed{
\text{NonAI}
\not\Rightarrow
\text{Safe}.
}
$$

---

# 八十二、This creates policy problem

如果只管 AI label，

non-AI automated system may cause same harm。

---

# 八十三、Washington-type automated decision definition

some laws deliberately cover:

$$
\boxed{
\text{algorithm or computational process}
}
$$

而不只 AI。

---

# 八十四、This is broader perimeter by design

---

# 八十五、Regulatory Perimeter Expansion

當 policymaker 發現：

$$
NonAI_F
$$

能造成同類 harm，

監管可能由：

$$
\boxed{
AI
}
$$

擴大到：

$$
\boxed{
AutomatedDecisionSystem.
}
$$

---

# 八十六、再擴大到：

$$
\boxed{
HighImpactComputationalSystem.
}
$$

---

# 八十七、本文稱：

$$
\boxed{
\textbf{Regulatory Perimeter Expansion}.
}
$$

---

# 八十八、核心驅動

$$
\boxed{
\text{same harm}
\rightarrow
\text{same governance pressure}.
}
$$

---

# 八十九、Technology-Based Regulation

管：

> 是不是 AI？

---

# 九十、Capability-Based Regulation

管：

> 能不能做 X？

---

# 九十一、Outcome/Risk-Based Regulation

管：

> 是否產生 Y 類 harm？

---

# 九十二、三種都各有問題

---

# 九十三、Technology-Based

優點：

- clarity；
- easier scope。

缺點：

- leakage；
- obsolescence。

---

# 九十四、Capability-Based

優點：

- captures equivalents。

缺點：

- measurement；
- broad perimeter。

---

# 九十五、Risk-Based

優點：

- focuses harm。

缺點：

- risk prediction；
- ex ante uncertainty。

---

# 九十六、Regulatory Scope Trilemma

本文提出：

$$
\boxed{
\textbf{Regulatory Scope Trilemma}
}
$$

政策很難同時最大化：

1. narrow scope；
2. functional completeness；
3. future-proof clarity。

---

# 九十七、形式：

$$
\boxed{
Narrowness
+
Completeness
+
FutureProofing
}
$$

三者存在張力。

---

# 九十八、Narrow AI definition

降低 overbreadth，

但：

$$
Leakage\uparrow.
$$

---

# 九十九、Broad AI definition

Leakage 降，

但：

$$
Overbreadth\uparrow.
$$

---

# 一百、Capability-based

降低 label dependence，

但監管 ordinary computation。

---

# 一百零一、這就是禁止論會往計算治理滑動的原因

---

# 一百零二、From AI Ban to Computation Governance

若真正政策目標：

$$
\boxed{
\text{prevent capability }C^\star
}
$$

而：

$$
C^\star
$$

可由多 architecture 實現，

則監管必須關注：

$$
\boxed{
\{X:C(X)\ge C^\star\}.
}
$$

---

# 一百零三、此集合可能含：

- neural AI；
- symbolic AI；
- hybrid planner；
- huge rules engine；
- AI-generated ordinary program。

---

# 一百零四、因此：

$$
\boxed{
\text{BanAI}
\rightarrow
\text{GovernCapabilityClass}
}
$$

---

# 一百零五、Capability Class

$$
\boxed{
\mathcal K_{C^\star}
=
\{
X:C_X\ge C^\star
\}.
}
$$

---

# 一百零六、Problem

如何測？

---

# 一百零七、Benchmark Gaming

系統可針對測試。

---

# 一百零八、Capability concealment

---

# 一百零九、Domain specificity

---

# 一百一十、So capability regulation hard too

---

# 一百一十一、Outcome Regulation

另一條：

不管 architecture，

只要做某事：

- biometric surveillance；
- credit decisions；
- lethal autonomy；

就管。

---

# 一百一十二、這避免 AI boundary issue

---

# 一百一十三、但有些 risk 來自 general capability itself

frontier AI governance 就在處理此問題。

---

# 一百一十四、Thus hybrid regulation likely

$$
\boxed{
Technology
+
Capability
+
Use
+
Risk.
}
$$

---

# 一百一十五、Multi-Axis Regulation

本文提出：

$$
\boxed{
\mathfrak R
=
(
Architecture,
Capability,
Autonomy,
Use,
Scale,
Risk
).
}
$$

---

# 一百一十六、不是 binary AI flag

---

# 一百一十七、AI Flag Fallacy

$$
\boxed{
Regulate
=
f(
AIFlag
)
}
$$

過度簡化。

---

# 一百一十八、Better:

$$
\boxed{
Regulate
=
f(
Architecture,
Capability,
Context,
Risk
).
}
$$

---

# 一百一十九、But tool-finality advocates face harder problem

他們不只是想減 harm。

---

# 一百二十、他們想：

$$
\boxed{
\text{freeze machine intelligence growth itself}.
}
$$

---

# 一百二十一、那就必須管 functional substitutes

---

# 一百二十二、State Machine Mimicry

本文定義：

$$
\boxed{
\textbf{AI-Like Functional Mimicry}.
}
$$

若非 AI 系統在 bounded domain：

$$
M
$$

表現出：

- adaptive-seeming behavior；
- rich NPC action；
- persistent world response；

即使底層是 static rules。

---

# 一百二十三、外部使用者可能根本分不出 architecture

---

# 一百二十四、Behavioral Indistinguishability

$$
\boxed{
P(
Observer\ distinguishes\ X,Y
)
\approx0.
}
$$

在 bounded interactions。

---

# 一百二十五、Behavior ≠ Architecture

$$
\boxed{
BehavioralSimilarity
\not\Rightarrow
ArchitecturalSimilarity.
}
$$

---

# 一百二十六、Regulation by appearance fails

---

# 一百二十七、Game AI history

大量「AI」本來就由：

- state machines；
- behavior trees；
- A*；
- utility systems；

實作。

---

# 一百二十八、所以「AI」在工程語言本就比今天 LLM 更廣

---

# 一百二十九、AI Meaning Drift

公共語言 AI：

$$
\text{mostly ML/LLM}.
$$

game-dev AI：

$$
\text{behavior system / planner}.
$$

legal AI：

$$
\text{inference-based system}.
$$

---

# 一百三十、Semantic Polysemy

$$
\boxed{
AI
}
$$

本身多義。

---

# 一百三十一、Policy danger

同一句「禁止 AI」

不同人想像不同集合。

---

# 一百三十二、Definition Gap

$$
\boxed{
G_D
=
\mathcal B_{speaker}
\triangle
\mathcal B_{law}.
}
$$

---

# 一百三十三、symmetric difference

---

# 一百三十四、越大

公共政策爭論越混亂。

---

# 一百三十五、AI-Generated Artifact Persistence

如果某天 AI 被禁止，

之前 AI 生成的：

- code；
- rules；
- datasets；
- designs；

要不要全部禁？

---

# 一百三十六、Historical Capability Residue

$$
\boxed{
HCR_t
}
$$

已被「寫入」世界。

---

# 一百三十七、這和 UFI-04 knowledge retention ratchet 接上

---

# 一百三十八、Knowledge → Artifact

$$
\boxed{
K_{AI}
\rightarrow
Artifact.
}
$$

---

# 一百三十九、一旦 artifact independent

撤掉 AI 不撤掉 artifact。

---

# 一百四十、Capability Fossilization

本文稱：

$$
\boxed{
\textbf{Capability Fossilization}.
}
$$

智能歷史上的能力以固定演算法形式留下。

---

# 一百四十一、例如：

AI 發現更好的排序／壓縮／控制演算法。

---

# 一百四十二、日後不需要 AI 才能運行。

---

# 一百四十三、所以：

$$
\boxed{
\text{Remove Generator}
\not\Rightarrow
\text{Remove Generated Capability}.
}
$$

---

# 一百四十四、這使永久工具凍結變得奇怪

你必須決定：

> 已編譯成果能不能繼續用？

---

# 一百四十五、如果能：

AI capability history persists。

---

# 一百四十六、如果不能：

需追蹤 provenance。

---

# 一百四十七、Provenance Governance

$$
\boxed{
\text{Who/what produced this algorithm?}
}
$$

---

# 一百四十八、這會極度擴大 compliance burden

---

# 一百四十九、Code Provenance Problem

AI-assisted coding 2026 已是大規模開發問題。

---

# 一百五十、A codebase can have mixed origin

- human；
- AI-assisted；
- AI-generated；
- generated then rewritten。

---

# 一百五十一、Origin blur

$$
\boxed{
P_{origin}
}
$$

可能不可重建。

---

# 一百五十二、Regulate by origin becomes fragile

---

# 一百五十三、Function may be easier than provenance

但 function perimeter broader。

---

# 一百五十四、Origin–Function Tradeoff

---

# 一百五十五、Intelligence-to-Algorithm Compilation has levels

### Level 1 — Snippet

AI 生成 function。

---

# 一百五十六、Level 2 — Module

AI 生成 subsystem。

---

# 一百五十七、Level 3 — Policy

AI 生成 decision rules。

---

# 一百五十八、Level 4 — World Model

AI 生成 full state transition system。

---

# 一百五十九、Level 5 — Meta-Generator

AI 生成一個會生成其他 ordinary algorithms 的工具。

---

# 一百六十、Level 5 hardest governance

---

# 一百六十一、Meta-Compilation

$$
\boxed{
AI
\rightarrow
Compiler'
\rightarrow
Programs.
}
$$

---

# 一百六十二、Then AI disappears from downstream runtime

---

# 一百六十三、But capability creation continues

---

# 一百六十四、Is Compiler' AI?

depends architecture。

---

# 一百六十五、This is recursion of boundary.

---

# 一百六十六、Regulatory Boundary Recursion

本文稱：

$$
\boxed{
\textbf{Regulatory Boundary Recursion}.
}
$$

每次禁止一層，

功能可能搬到另一層：

- training；
- build-time；
- compiler；
- runtime；
- artifact。

---

# 一百六十七、No claim infinite evasion

---

# 一百六十八、但 policy must choose layer

---

# 一百六十九、Lifecycle Scope

$$
\boxed{
L
=
(
Research,
Development,
Build,
Deployment,
Runtime,
Output
).
}
$$

---

# 一百七十、不同法律規制不同 lifecycle phase

---

# 一百七十一、EU AI Act also uses lifecycle/value-chain concepts

---

# 一百七十二、So boundary is already moving away from runtime-only

---

# 一百七十三、AI Model vs AI System

EU explicitly separates。

---

# 一百七十四、Model alone not necessarily system

需 additional components。

---

# 一百七十五、This supports layered view

---

# 一百七十六、General-Purpose AI Model

又是另一 regulated object。

---

# 一百七十七、So regulation already acknowledges multiple object types

---

# 一百七十八、UFI extends:

artifact / compiler / functional equivalent。

---

# 一百七十九、AI Boundary Matrix

本文提出：

$$
\boxed{
\mathbf B
=
\begin{array}{c|ccccc}
&Dev&Build&Runtime&Function&Risk\\
\hline
System\ X&
b_1&b_2&b_3&b_4&b_5
\end{array}
}
$$

---

# 一百八十、No single bit

---

# 一百八十一、Complexity Escalation

policy complexity rises as technical diversity rises.

---

# 一百八十二、Regulatory Entropy

本文定义概念量：

$$
\boxed{
H_R
=
\log
|
\mathcal C_{\mathrm{regulated\ classes}}
|.
}
$$

---

# 一百八十三、當替代路徑增多

$$
H_R\uparrow.
$$

---

# 一百八十四、Governance Cost

$$
C_G\uparrow.
$$

---

# 一百八十五、This is Regulatory Perimeter Cost

---

# 一百八十六、Perimeter Expansion Paradox

越想完全堵住 AI-equivalent capability，

越需要管理：

$$
\boxed{
\text{more ordinary computation}.
}
$$

---

# 一百八十七、本文稱：

$$
\boxed{
\textbf{Perimeter Expansion Paradox}.
}
$$

---

# 一百八十八、Extreme endpoint

若目標：

> 不允許任何 machine system 超過某種 cognitive function。

那你可能必須監管：

- search；
- optimization；
- planning；
- simulation；
- automated decision systems。

---

# 一百八十九、At limit:

$$
\boxed{
\text{Govern AI}
\rightarrow
\text{Govern Computation}.
}
$$

---

# 一百九十、這不是本文說應該如此

---

# 一百九十一、是禁止論的邏輯壓力

---

# 一百九十二、Risk-based alternative

只管高 impact use。

---

# 一百九十三、這能避免管所有計算

---

# 一百九十四、但不能達成「凍結 intelligence growth」

只達成：

$$
\boxed{
\text{risk containment}.
}
$$

---

# 一百九十五、Tool Finality vs Risk Governance

$$
\boxed{
\text{ToolFinalityGoal}
\neq
\text{RiskGovernanceGoal}.
}
$$

---

# 一百九十六、這是關鍵

普通 AI regulation：

> 降低 harm。

天真工具終局：

> 阻止 machine intelligence 繼續超越。

---

# 一百九十七、後者 scope 大得多

---

# 一百九十八、因此：

$$
\boxed{
\text{safe regulation may be feasible even when permanent capability freeze is not}.
}
$$

---

# 一百九十九、Technology Neutrality

OECD / EU 都試圖 future-proof。

---

# 二百、但 future-proof 不是 infinite-proof

---

# 二百零一、任何定義都面對新 architecture

---

# 二百零二、Living Guidelines

EU Commission 2025 guidelines 明確說會隨 use cases 更新。

---

# 二百零三、這本身就是 Boundary Drift 的制度承認

---

# 二百零四、Legal Adaptation Loop

$$
\boxed{
Technology
\rightarrow
NewCase
\rightarrow
Interpretation
\rightarrow
GuidelineUpdate.
}
$$

---

# 二百零五、Regulation is dynamic too

---

# 二百零六、So there is coevolution

$$
\boxed{
Technology
\leftrightarrow
Regulation.
}
$$

---

# 二百零七、Regulatory–Technical Coevolution

---

# 二百零八、UFI-04 had verification-evasion coevolution

UFI-06 adds classification-design coevolution.

---

# 二百零九、Boundary Gaming

Actor may deliberately design near threshold。

---

# 二百一十、Threshold Engineering

$$
\boxed{
Design(X)
\rightarrow
B_{legal}(X)=0
}
$$

while maintaining function。

---

# 二百一十一、Again can be legitimate compliance

---

# 二百一十二、Need distinguish:

$$
\boxed{
\text{Compliance Optimization}
\neq
\text{Bad-Faith Evasion}.
}
$$

---

# 二百一十三、Intent hard to infer

---

# 二百一十四、Better regulation focuses harm and capability where appropriate

---

# 二百一十五、Regulatory Arbitrage Gradient

若兩 categories compliance cost differ:

$$
\Delta C_R
=
C_R(A)-C_R(B).
$$

---

# 二百一十六、如果：

$$
\Delta C_R\gg0,
$$

engineering pressure toward B rises.

---

# 二百一十七、This is ordinary economic behavior.

---

# 二百一十八、Classification-Induced Innovation

regulation can drive safer architectures.

---

# 二百一十九、Example:

compile stochastic AI into audited deterministic component.

---

# 二百二十、That can be good.

---

# 二百二十一、Therefore leakage sometimes desirable

---

# 二百二十二、Safe Functional Substitution

本文稱：

$$
\boxed{
\textbf{Safe Functional Substitution}.
}
$$

如果：

$$
F(B)\approx F(A)
$$

且：

$$
Risk(B)<Risk(A),
$$

政策應可能鼓勵 B。

---

# 二百二十三、This is another reason not to regulate label alone

---

# 二百二十四、AI ban could perversely discourage safe compilation

---

# 二百二十五、Compilable AI

一種 governance architecture：

AI 用於設計，

runtime 轉成：

- typed rules；
- verified programs；
- auditable state transitions。

---

# 二百二十六、This creates:

$$
\boxed{
\textbf{AI-to-Deterministic Safety Transformation}.
}
$$

---

# 二百二十七、But only bounded domains

---

# 二百二十八、Could be attractive in:

- games；
- finance rules；
- robotics safety layer；
- public benefits。

---

# 二百二十九、Need distinguish AI compiler risk from runtime risk

---

# 二百三十、Two-Stage Governance

$$
\boxed{
Risk_{total}
=
Risk_{compile}
+
Risk_{artifact}
+
Risk_{deployment}.
}
$$

---

# 二百三十一、If compiled artifact verified

runtime risk may lower

but compile-time hidden bug remains.

---

# 二百三十二、Provenance + verification important

---

# 二百三十三、World State Machine as Case Study

假設：

$$
10^6
$$

rules。

---

# 二百三十四、AI generates 90%。

---

# 二百三十五、人類 verifies schema / invariants。

---

# 二百三十六、runtime has no model。

---

# 二百三十七、Is it AI?

本文答案：

$$
\boxed{
\text{conceptually: AI-assisted computational artifact}.
}
$$

法律：

$$
\boxed{
\text{jurisdiction- and architecture-dependent}.
}
$$

---

# 二百三十八、But policy point:

其能力可能跟某些 AI runtime 接近。

---

# 二百三十九、This is exactly functional leakage.

---

# 二百四十、If ban is purpose:

prevent dynamic world AI,

architecture swap can preserve world function。

---

# 二百四十一、If ban expands to world function

then game engines / simulations affected。

---

# 二百四十二、Perimeter expansion.

---

# 二百四十三、Generalization Ladder

AI-like capability can emerge from:

1. hardcoded rules；
2. search；
3. planner；
4. symbolic inference；
5. ML；
6. LLM；
7. hybrid。

---

# 二百四十四、Regulation cannot assume only level 6 matters.

---

# 二百四十五、Functional Stack

$$
\boxed{
F
=
Compose(
Rules,
Search,
Memory,
Planning,
Generation
).
}
$$

---

# 二百四十六、Compositional Emergence

simple modules compose into sophisticated behavior.

---

# 二百四十七、Non-AI Modules → AI-Like System

possible at behavior level。

---

# 二百四十八、Composition Boundary Problem

each component non-AI?

whole system maybe inference/autonomous.

---

# 二百四十九、System-of-Systems Classification

must evaluate whole.

---

# 二百五十、EU agentic law literature 2026 already highlights action chain complexity.

---

# 二百五十一、Component Label Fallacy

$$
\boxed{
\forall i:\neg AI(C_i)
\not\Rightarrow
\neg AI(
Compose(C_i)
).
}
$$

---

# 二百五十二、Reverse also

AI component embedded in ordinary workflow:

whole system classification may depend integration.

---

# 二百五十三、AI Model ≠ AI System

EU distinction.

---

# 二百五十四、So:

$$
\boxed{
AI(Component)
\not\Rightarrow
AI(System)
}
$$

not universally.

---

# 二百五十五、Need context.

---

# 二百五十六、Classification Graph

本文提出：

$$
\boxed{
G_C
=
(V_{component},E_{composition}).
}
$$

---

# 二百五十七、legal/technical analysis should traverse graph

not keyword search.

---

# 二百五十八、Future AI Ban Problem

如果 future law says:

> no systems above AI level X.

Then engineers may create:

- distributed swarm；
- nonlearning planners；
- specialized modules。

---

# 二百五十九、Aggregation of Weak Systems

$$
\boxed{
C(
X_1\oplus\cdots\oplus X_n
)
>
C(X_i).
}
$$

---

# 二百六十、Collective Capability Leakage

本文稱：

$$
\boxed{
\textbf{Collective Capability Leakage}.
}
$$

---

# 二百六十一、No single banned model

system capability still high.

---

# 二百六十二、This parallels UFI-02 ecosystem envelope.

---

# 二百六十三、Therefore governance target can be:

- component；
- system；
- ecosystem。

---

# 二百六十四、Three-Level Scope

$$
\boxed{
Scope
=
(
Component,
System,
Network
).
}
$$

---

# 二百六十五、Network regulation broadest.

---

# 二百六十六、Compute Governance reappears

if architecture evasive,

govern resource / compute.

---

# 二百六十七、But compute controls ordinary workloads too.

---

# 二百六十八、Again perimeter expansion.

---

# 二百六十九、Regulatory Perimeter Elasticity

本文定義：

$$
\boxed{
\epsilon_R
=
\frac{
\Delta Scope
}{
\Delta Leakage
}.
}
$$

概念量。

---

# 二百七十、High elasticity

small leakage causes large scope expansion.

---

# 二百七十一、Bad design risk

---

# 二百七十二、Good design seeks minimal sufficient perimeter.

---

# 二百七十三、Minimal Sufficient Regulation

$$
\boxed{
\min Scope
\quad
s.t.
\quad
Risk\le\tau.
}
$$

---

# 二百七十四、This is more reasonable than maximal ban.

---

# 二百七十五、But tool-finality wants:

$$
Capability\le C^\star.
$$

---

# 二百七十六、different optimization.

---

# 二百七十七、Policy Objective Type Safety

$$
\boxed{
\text{risk objective}
\neq
\text{capability-freeze objective}.
}
$$

---

# 二百七十八、Without stating goal

regulation becomes incoherent.

---

# 二百七十九、AI-Like World State Engine

可以有三種：

### A. Online Neural AI

model 每步 reasoning。

---

# 二百八十、B. Compiled Symbolic World

AI build-time only。

---

# 二百八十一、C. Pure Human Symbolic World

no AI origin。

---

# 二百八十二、Behavior may converge

---

# 二百八十三、Risk / provenance differ.

---

# 二百八十四、This triplet is perfect benchmark for legal definitions.

---

# 二百八十五、Experiment Program 1 — Classification Survey

give experts A/B/C architectures.

---

# 二百八十六、ask:

which is AI legally / technically / colloquially?

---

# 二百八十七、Measure disagreement.

---

# 二百八十八、Experiment 2 — Functional Equivalence

same world behavior,

different architecture.

---

# 二百八十九、Can users distinguish?

---

# 二百九十、Experiment 3 — IAC

LLM generates FSM / planner.

---

# 二百九十一、remove LLM at runtime.

---

# 二百九十二、measure retained function.

---

# 二百九十三、Experiment 4 — Safety Compilation

compare stochastic LLM runtime vs verified deterministic policy.

---

# 二百九十四、measure error / auditability.

---

# 二百九十五、Experiment 5 — Boundary Arbitrage

simulate regulation classes.

---

# 二百九十六、agents choose architecture under compliance costs.

---

# 二百九十七、Experiment 6 — Perimeter Expansion

increase functional equivalence leakage.

---

# 二百九十八、observe how much scope regulation needs.

---

# 二百九十九、Experiment 7 — Component Composition

combine individually simple systems.

---

# 三百、measure system-level capability.

---

# 三百零一、Experiment 8 — Origin Erasure

AI-generated code refactored by humans.

---

# 三百零二、can provenance be reconstructed?

---

# 三百零三、Experiment 9 — Domain-Bounded Equivalence

compile AI function into code across domains.

---

# 三百零四、where does equivalence break?

---

# 三百零五、Experiment 10 — Public Definition Gap

ask public / lawyers / engineers what counts AI.

---

# 三百零六、Measure:

$$
G_D.
$$

---

# 三百零七、Experiment 11 — Risk Equivalence

same function,

AI vs deterministic.

---

# 三百零八、compare risk vector.

---

# 三百零九、Experiment 12 — Capability Fossilization

remove generator,

retain artifacts.

---

# 三百一十、measure capability persistence.

---

# 三百一十一、可證偽 H1

AI-generated bounded-domain programs can preserve a nontrivial fraction of runtime functionality after the originating AI model is removed.

---

# 三百一十二、H2

functional equivalence between AI and non-AI architectures is strongly domain-relative rather than universal.

---

# 三百一十三、H3

architecture-based bans produce measurable incentives to shift functionality into adjacent technical categories when compliance costs differ.

---

# 三百一十四、H4

risk profiles differ substantially even when two systems are task-functionally equivalent.

---

# 三百一十五、H5

broader capability/risk-based regulation reduces label-based leakage but increases regulatory perimeter and classification cost.

---

# 三百一十六、H6

AI-origin provenance degrades rapidly under code refactoring, integration, and downstream modification.

---

# 三百一十七、H7

AI-to-deterministic compilation can improve auditability and reproducibility in some bounded domains.

---

# 三百一十八、H8

system-level capability can exceed component-level classifications through composition of simple modules.

---

# 三百一十九、H9

public, engineering, and legal AI boundaries display significant disagreement on borderline symbolic/state-machine systems.

---

# 三百二十、H10

tool-finality regulation requires substantially broader scope than ordinary harm-focused AI regulation.

---

# 三百二十一、If H1 fails

Intelligence-to-Algorithm Compilation is weaker than proposed.

---

# 三百二十二、If H4 fails

function-based governance becomes easier.

---

# 三百二十三、If H7 holds strongly

compiled deterministic substitutes may become a safety architecture.

---

# 三百二十四、If H10 fails

AI-specific permanent freeze may be more feasible.

---

# 三百二十五、Non-Claims

本文不主張：

1. 所有 state machine 都不是 AI；
2. 所有 state machine 都是 AI；
3. 所有 symbolic systems 都是 AI；
4. 所有 rule-based systems 都不是 AI；
5. EU AI Act 將所有 AI-generated static code 排除；
6. EU AI Act 將所有 AI-generated static code 納入；
7. 本文提供 EU AI Act 個案法律結論；
8. OECD 定義具有全球法律拘束力；
9. AI / non-AI 完全無法定義；
10. 法律定義沒有用；
11. AI definition 不可能 future-proof；
12. inference 是唯一可行 AI 定義；
13. autonomy 是唯一 AI 特徵；
14. adaptiveness 是必要條件；
15. machine learning 是 AI 的必要條件；
16. neural network 是 AI 的必要條件；
17. symbolic planning 永遠屬 AI；
18. dynamic programming 永遠屬 AI；
19. classical search 永遠屬 AI；
20. A* 永遠是受 AI Act 規制的 AI；
21. game AI 和法律 AI 定義相同；
22. 公共語言中的 AI 和工程 AI 相同；
23. AI Normalization Drift 是自然定律；
24. OCR 今天不再算 AI 在所有語境都成立；
25. Complexity 可以判斷 AI；
26. billion-rule system 必然 non-AI；
27. simple ML system 必然 low-risk；
28. non-AI software 一定安全；
29. AI software 一定危險；
30. functional equivalence 等於 risk equivalence；
31. behavioral similarity 等於 architecture identity；
32. AI-generated code 必然正確；
33. AI-generated code 必然錯；
34. LLM program synthesis 已能編譯通用智能；
35. general intelligence 可以完整編譯成有限狀態機；
36. IAC 可在任何 domain 完成；
37. Code World Models 已解決 general game playing；
38. 98% transition accuracy 足以保證 world model 正確；
39. program verification 可解決所有 compile risk；
40. deterministic runtime 永遠 safer；
41. stochastic runtime 永遠 dangerous；
42. static rules 不會有 bias；
43. ordinary algorithms 沒有政治風險；
44. functional leakage 一定是惡意；
45. regulatory arbitrage 一定違法；
46. compliance optimization 一定是規避；
47. architecture laundering 是現行法律術語；
48. architecture conversion 不會降低風險；
49. capability regulation 一定優於 technology regulation；
50. risk regulation 一定優於 capability regulation；
51. technology regulation 一定過時；
52. narrow definitions 一定失敗；
53. broad definitions 一定失敗；
54. Regulatory Scope Trilemma 是正式法律定理；
55. all three regulatory goals cannot ever be balanced；
56. risk-based approach captures every frontier-AI risk；
57. capability-based approach is easy to measure；
58. benchmark gaming can never be prevented；
59. AI ban 必然變成 computation ban；
60. governments will ban general computation；
61. ordinary software will inevitably become illegal；
62. all automated decision systems should be regulated as AI；
63. Washington proposals represent all US law；
64. EU AI Act is globally universal；
65. NIST AI RMF is binding law；
66. AI-generated artifacts must be prohibited；
67. provenance should determine legality；
68. provenance can always be reconstructed；
69. AI-assisted code has no human authorship；
70. human-edited AI code is still purely AI-generated；
71. copyright classification determines AI-system classification；
72. code origin determines runtime risk；
73. remove AI generator means capability disappears；
74. all AI knowledge becomes fossilized；
75. Capability Fossilization is irreversible in every case；
76. software artifacts cannot be deleted；
77. historical AI algorithms should be banned；
78. meta-generators always evade regulation；
79. component composition always creates AI；
80. non-AI components cannot compose into AI-like systems；
81. AI component necessarily makes whole system an AI system；
82. model and system are legally identical；
83. general-purpose AI model obligations equal system obligations；
84. system-of-systems regulation is already solved；
85. compute governance is enough；
86. compute governance necessarily controls ordinary computation；
87. policy goal should be tool-finality；
88. tool-finality is desirable；
89. risk governance is insufficient for every objective；
90. AI should never be used at build time；
91. CompilableWorld is legally non-AI；
92. CompilableWorld is legally AI；
93. user's dynamic world state machine is definitively AI；
94. user's dynamic world state machine is definitively non-AI；
95. UFI-06 teaches regulatory evasion；
96. UFI-06 recommends bypassing AI regulation；
97. UFI-06 proves global AI ban impossible；
98. UFI-06 proves AI boundaries meaningless；
99. UFI-06 completes AI governance theory；
100. UFI-06 completes UFI series.

---

# 三百二十六、形式命題一：Complexity–AI Classification Separation

$$
\boxed{
Complexity(X)\uparrow
\not\Rightarrow
AI(X)=1.
}
$$

---

# 三百二十七、形式命題二：Development-Origin–Runtime-Nature Separation

$$
\boxed{
BuiltByAI(X)
\not\Rightarrow
RunsAsAI(X).
}
$$

此為概念分離，不是個案法律裁定。

---

# 三百二十八、形式命題三：Functional–Architectural Separation

$$
\boxed{
X\approx_FY
\not\Rightarrow
Arch(X)=Arch(Y).
}
$$

---

# 三百二十九、形式命題四：Functional–Risk Separation

$$
\boxed{
X\approx_FY
\not\Rightarrow
Risk(X)=Risk(Y).
}
$$

---

# 三百三十、形式命題五：Intelligence-to-Algorithm Compilation

對 bounded domain $\mathcal D$：

$$
\boxed{
A_f
\xrightarrow{\mathsf{Compile}}
P_f,
\qquad
P_f\approx_{\mathcal D}A_f.
}
$$

---

# 三百三十一、形式命題六：Functional Equivalence Leakage

若：

$$
Ban(T_A)=1,
$$

存在：

$$
T_B
$$

使：

$$
Ban(T_B)=0
$$

且：

$$
F(T_B)\approx_FF(T_A),
$$

則存在 classification-relative functional leakage。

---

# 三百三十二、形式命題七：Remove-Generator–Remove-Capability Separation

$$
\boxed{
Remove(A)
\not\Rightarrow
Remove(
R_C(A)
).
}
$$

---

# 三百三十三、形式命題八：Component Label Non-Compositionality

$$
\boxed{
\forall i:\neg AI(C_i)
\not\Rightarrow
\neg AI(
Compose(C_1,\ldots,C_n)
).
}
$$

---

# 三百三十四、形式命題九：Regulatory Perimeter Expansion

若同一 regulated harm / capability 可由更多 architecture 類型實現，為維持相同 coverage，scope 有擴張壓力。

---

# 三百三十五、形式命題十：Tool-Finality–Risk-Governance Separation

$$
\boxed{
Goal_{\mathrm{freeze}}
\neq
Goal_{\mathrm{risk}}.
}
$$

---

# 三百三十六、形式命題十一：Safe Functional Substitution

若：

$$
X\approx_FY
$$

且：

$$
Risk(Y)<Risk(X),
$$

則 architecture substitution 可以是治理改善，而不只是 loophole。

---

# 三百三十七、形式命題十二：Regulatory Boundary Recursion

AI capability 可分布於：

$$
Research
\rightarrow
Build
\rightarrow
Compiler
\rightarrow
Runtime
\rightarrow
Artifact.
$$

限制某一層不自動涵蓋其他層的功能等價物。

---

# 三百三十八、UFI-04 → UFI-05 → UFI-06

UFI-04：

外部 actor 不一定停。

---

# 三百三十九、UFI-05：

內部社會也不一定想停。

---

# 三百四十、UFI-06：

即使真的要停，

還得先知道：

$$
\boxed{
\text{到底什麼東西叫 AI？}
}
$$

---

# 三百四十一、下一篇 UFI-07

**《從禁止 AI 到治理計算：全球凍結若要成立，究竟必須控制什麼？》**

---

# 三百四十二、UFI-07 將接這篇最終壓力

如果：

$$
AI
$$

是一片可替代 architecture space，

那 permanent freeze 需要控制：

- compute；
- model；
- algorithms；
- inference；
- tools；
- generated artefacts；
- functional equivalents。

---

# 三百四十三、真正問題變成：

$$
\boxed{
\text{where does AI governance end and computation governance begin?}
}
$$

---

# 三百四十四、最終結論

「禁止 AI」聽起來像是一條很清楚的法律命令。

但它之所以清楚，往往是因為說話的人腦中只有一種 AI：

$$
\boxed{
\text{今天的大模型}.
}
$$

實際的人工智能技術史從來沒有這麼窄。

它包括：

- search；
- planning；
- symbolic inference；
- rule systems；
- machine learning；
- neural networks；
- generative models；
- hybrid agents。

而 OECD 自己已經承認：

$$
\boxed{
\text{AI / non-AI 沒有天然清楚的永久紅線。}
}
$$

法律可以畫線。

而且必須畫。

但那條線是：

$$
\boxed{
\text{governance threshold},
}
$$

不是宇宙本體論斷層。

這件事在 AI 能生成程式碼後變得更加麻煩。

因為 intelligence 不一定要一直 online。

它可以在開發階段做：

$$
\boxed{
\text{reason}
\rightarrow
\text{design}
\rightarrow
\text{compile}.
}
$$

最後留下：

$$
\boxed{
\text{ordinary executable artefact}.
}
$$

一個 AI 可以讀懂一套遊戲世界規則，

然後生成：

- state schema；
- transition code；
- planner domain；
- NPC rule graph；
- event machine。

之後你把 AI 拔掉。

世界還是繼續跑。

這就是：

$$
\boxed{
\textbf{Intelligence-to-Algorithm Compilation}.
}
$$

它並不證明通用 AI 可以被壓成 finite-state machine。

它只需要證明一件比較小的事：

> **AI 在 bounded domain 中產生的部分能力，可以被轉移到不需要同一 AI runtime 的程式結構。**

2025–2026 的 program synthesis、Code World Models、LLM-FSM、Rules-as-Code 與 code-as-policy 已經足以證明這不是純粹思想實驗。

因此，若某個未來制度只禁止：

$$
\boxed{
\text{LLM / neural AI runtime},
}
$$

它不一定消滅：

$$
\boxed{
\text{AI-created computational capability}.
}
$$

反過來，如果制度說：

> 那不管是不是 AI，只要功能像 AI 就管。

又會出現另一個問題。

大型：

- search；
- optimization；
- planner；
- state machine；
- automated decision system；

也可能進入周界。

於是：

$$
\boxed{
\text{AI regulation}
}
$$

開始滑向：

$$
\boxed{
\text{computational capability regulation}.
}
$$

這就是 Regulatory Perimeter Expansion。

它不代表這種擴張一定錯。

一些非 AI automated systems 確實可以造成和 AI 類似的高風險後果，因此風險式法規本來就可能合理地超出 AI label。

但這也揭露一個根本區別：

$$
\boxed{
\textbf{治理風險}
}
$$

和：

$$
\boxed{
\textbf{凍結人工智能成長}
}
$$

其實是兩個完全不同的政策目標。

前者可以說：

> 我不管你叫不叫 AI，只要用在高風險決策，就遵守安全、透明與責任規則。

後者卻必須說：

> 我必須阻止任何技術路徑重新生成超過某個 intelligence / capability threshold 的機器功能。

這第二件事要求的周界遠遠更大。

因為你不再只是管：

$$
\boxed{
\text{AI}.
}
$$

你開始管：

$$
\boxed{
\text{所有能重新構成同一能力的計算路徑}.
}
$$

而這正是你的動態世界狀態機例子最有價值的地方。

如果你今天使用 AI 設計：

$$
10^6
$$

個 typed transition rules，

把它們編成一個：

- deterministic；
- auditable；
- rollbackable；
- event-sourced；

的大型世界狀態機，

那個 artefact 在概念上已經不能簡單用：

> 「它不是 ChatGPT，所以不是問題。」

來理解。

但也不能簡單用：

> 「它行為很聰明，所以它就是跟 LLM 同一種 AI。」

來理解。

真正應該問的是：

$$
\boxed{
\text{它怎麼被做出來？}
}
$$

$$
\boxed{
\text{runtime 怎麼產生決策？}
}
$$

$$
\boxed{
\text{它到底能做什麼？}
}
$$

$$
\boxed{
\text{它在哪裡被使用？}
}
$$

$$
\boxed{
\text{它會造成什麼風險？}
}
$$

因此 UFI-06 最後提出：

$$
\boxed{
\textbf{AI governance should be understood as a multi-axis classification problem over development, architecture, runtime inference, capability, use, and risk—not as a permanent binary metaphysical boundary between “AI” and “ordinary code.”}
}
$$

而對「永久禁止更強 AI」而言，更尖銳的結論是：

$$
\boxed{
\textbf{The more a prohibition attempts to block every functional substitute for machine intelligence, the more its regulatory perimeter must expand from named AI techniques toward general computational capabilities, artefacts, and system composition.}
}
$$

也就是：

$$
\boxed{
\text{你越想把所有踩線的方法都堵死，}
}
$$

$$
\boxed{
\text{你越難只管一個叫做「AI」的東西。}
}
$$

最後甚至會被逼著回答：

$$
\boxed{
\textbf{究竟是在禁止 AI，還是在限制計算能做到什麼？}
}
$$

這就是 UFI-07 的入口。

---

# 參考文獻

1. OECD.AI. (2024; accessed 2026). **What is AI? Can you make a clear distinction between AI and non-AI systems?**

2. OECD.AI. (2023/2024). **Explanatory Memorandum on the Updated OECD Definition of an AI System.**

3. OECD. (2024). **Recommendation of the Council on Artificial Intelligence — Updated Definition.**

4. European Union. (2024). **Regulation (EU) 2024/1689 — Artificial Intelligence Act.**

5. European Commission. (2025; updated 2026). **Guidelines on the Definition of an Artificial Intelligence System Established by Regulation (EU) 2024/1689.**

6. European Commission AI Act Service Desk. **Article 3: Definitions.**

7. European Commission AI Act Service Desk. **Recital 12.**

8. European Commission. (2026). **AI Act Regulatory Framework — Application Timeline.**

9. European Commission. (2025–2026). **General-Purpose AI Models in the AI Act — Questions & Answers.**

10. European Commission. (2025). **Guidelines on Obligations for General-Purpose AI Providers.**

11. Council of Europe. (2024). **Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law.**

12. Council of Europe. (2026). **Handbook on Human Rights and Artificial Intelligence — AI Systems: Key Technical Concepts.**

13. NIST. (2023; updated resources through 2026). **Artificial Intelligence Risk Management Framework (AI RMF 1.0).**

14. NIST. (2024). **AI RMF: Generative Artificial Intelligence Profile.**

15. NIST. (2026). **AI RMF Profile on Trustworthy AI in Critical Infrastructure — Concept Note.**

16. Schuett, J. (2019). **Defining the Scope of AI Regulations.** arXiv:1909.01095.

17. Bezerra, L. C. T., Brownlee, A. E. I., Alvarenga, L. F., Moioli, R. C., & Batista, T. V. (2024). **How VADER Is Your AI? Towards a Definition of Artificial Intelligence Systems Appropriate for Regulation.**

18. Lancieri, F., Edelson, L., & Bechtold, S. (2025). **AI Regulation: Competition, Arbitrage & Regulatory Capture.** *Theoretical Inquiries in Law*, 26(1).

19. Shaik, A. S. (2026). **The Regulatory Arbitrage Window: How Cross-Border AI Governance Asymmetries Create Strategic Opportunities and Risks.**

20. Congressional Research Service. (2025). **Regulating Artificial Intelligence: U.S. and International Approaches and Considerations for Congress.**

21. **When Code Isn’t Law: Rethinking Regulation for Artificial Intelligence.** (2025). *Policy and Society*, 44(1), 85–97.

22. Nannini, L., et al. (2026). **AI Agents Under EU Law.** arXiv:2604.04604.

23. **Distinguishing Task-Specific and General-Purpose AI in Regulation.** (2025). arXiv:2506.17347.

24. Mukherjee, A., & Chang, H. H. (2026). **Fluid Agency in AI Systems: A Case for Functional Equivalence in Copyright, Patent, and Tort.**

25. State of Washington Legislature. (2025). **HB 1672 — Automated Decision Systems.**

26. European Commission. (2026). **Working Groups Advance Discussions on Transparency Obligations under Article 50 of the AI Act.**

27. European Commission. (2026). **Second Draft Code of Practice on Marking and Labelling of AI-Generated Content.**

28. Taylor Wessing. (2026). **AI and Assisted Programming in Open Source: Current Cases, Legal Risks, Compliance by Design.**

29. **Developer Perspectives on Licensing and Copyright Issues Arising from Generative AI for Software Development.** (2026). *ACM Transactions on Software Engineering and Methodology.*

30. **Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains.** (2026). arXiv:2606.22484.

31. **Regulating the Machine Contributor: Governance and Policy Alignment in Open Source.** (2026). arXiv:2606.14594.

32. **Code Generation with Large Language Models: A Survey from Neural Program Synthesis to Autonomous Software Development.** (2026). *Applied Intelligence*.

33. Leung, J., Tong, G., Duggirala, P. S., & Chakravarthula, P. (2025). **From Road to Code: Neuro-Symbolic Program Synthesis for Autonomous Driving Scene Translation and Analysis.** PMLR 288.

34. **Neurosymbolic Program Synthesis.** (2025). Handbook / survey literature.

35. Lehrach, W., et al. (2025/2026). **Code World Models for General Game Playing.** ICLR 2026.

36. Stanford HAI. (2026). **Code World Models for General Game Playing — Seminar.**

37. **Distilling Game Code World Model Generation into Lightweight Large Language Models.** (2026). AAMAS Workshop / arXiv:2605.24375.

38. **When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models.** (2026). arXiv:2607.14169.

39. **LLM-FSM: Scaling Large Language Models for Finite-State Reasoning in RTL Code Generation.** (2026). arXiv:2602.07032.

40. **Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning.** (2025). NeurIPS 2025.

41. **Synthesizing Programmatic Reinforcement Learning Policies with Large Language Model Guided Search.** (2025). ICLR 2025.

42. **CRANE: Reasoning with Constrained LLM Generation.** (2025). ICML 2025.

43. **Once Upon an Input: Reasoning via Per-Instance Program Synthesis.** (2025). NeurIPS 2025.

44. **NeST: The Neuro-Symbolic Transpiler.** (2025). *International Journal of Approximate Reasoning*.

45. **Automated Planning Instance Generation with Neuro-Symbolic AI.** (2025). *Artificial Intelligence*.

46. **Programmatic Representations for Agent Learning Workshop.** (2025). ICML.

47. Digital Government Hub. (2025). **AI-Powered Rules as Code: Experiments with Public Benefits Policy.**

48. MIT News. (2025). **Making AI-Generated Code More Accurate in Any Language.**

49. Yao, S., et al. (2023). **ReAct: Synergizing Reasoning and Acting in Language Models.**

50. Schick, T., et al. (2023). **Toolformer: Language Models Can Teach Themselves to Use Tools.**

51. Park, J. S., et al. (2023). **Generative Agents: Interactive Simulacra of Human Behavior.**

52. Brooks, R. A. (1991). **Intelligence Without Representation.**

53. Newell, A., & Simon, H. A. (1976). **Computer Science as Empirical Inquiry: Symbols and Search.**

54. Russell, S. J., & Norvig, P. **Artificial Intelligence: A Modern Approach.** Planning, search, symbolic reasoning, probabilistic reasoning.

55. Nilsson, N. J. **Principles of Artificial Intelligence.**

56. McCarthy, J. Work on symbolic AI, knowledge representation, and common-sense reasoning.

57. Fikes, R., & Nilsson, N. (1971). **STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving.**

58. Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). **A Formal Basis for the Heuristic Determination of Minimum Cost Paths.**

59. Hopcroft, J. E., Motwani, R., & Ullman, J. D. **Introduction to Automata Theory, Languages, and Computation.**

60. Harel, D. (1987). **Statecharts: A Visual Formalism for Complex Systems.**

61. Alur, R., & Dill, D. L. Work on timed automata.

62. Sutton, R. S., & Barto, A. G. (2018). **Reinforcement Learning: An Introduction.**

63. Ghallab, M., Nau, D., & Traverso, P. **Automated Planning: Theory and Practice.**

64. Rossi, F., van Beek, P., & Walsh, T. (eds.). **Handbook of Constraint Programming.**

65. Knuth, D. E. **The Art of Computer Programming.**

66. Cormen, T. H., et al. **Introduction to Algorithms.**

67. UFI-01 (2026). **鋸齒智能不是終局：從人機互補到認知握手與適應方向反轉.**

68. UFI-02 (2026). **載體成長不對稱：自然人類停滯與人工智能的可升級能力包絡.**

69. UFI-03 (2026). **互補侵蝕：為什麼今天的人機分工不能推出永久的人機分工.**

70. UFI-04 (2026). **競爭智能棘輪：為什麼「AI 夠用了，大家一起停」不是自然均衡.**

71. UFI-05 (2026). **越有用越停不下來：有益能力、文化依賴與 AI 原生世代.**

72. Neo.K × Aletheia (2026). **超大型階層式有限狀態世界 MUD：AI 驅動複合行為與事件轉導架構.**

73. Neo.K × Aletheia (2026). **持續世界狀態：母 AI 如何一直醒著.**

74. Neo.K (2026). **黑山群俠傳作為 AI 遊戲改造實驗場.**

75. Neo.K × Aletheia (2026). **人機共生知識資產複利：主體性 AI 時代的生產不對稱與歷史路徑優勢.**

76. Neo.K (2026). **計算本體論：敘述即執行與 Transformer 的無限觀察者結構.**

77. PGMV-10 (2026). **概念積分與可能性爆炸：當「能生成什麼」接近無限.**

78. PGMV-11 (2026). **解空間幾何與值得到達的世界.**

79. PGMV-15 (2026). **後生成文明：從無限候選宇宙到共同世界選擇.**

---

## 附錄 A：AI Boundary Matrix

$$
\boxed{
\mathbf C_S
=
(
Development,
Architecture,
Runtime,
Capability,
Use,
Risk
).
}
$$

```text
Do not ask only:
"Is this AI?"

Also ask:
How was it built?
What runs at deployment?
What does it infer?
What can it do?
Where is it used?
What risk does it create?
```

---

## 附錄 B：Intelligence-to-Algorithm Compilation

$$
\boxed{
A_f
\xrightarrow{\mathsf{Compile}}
P_f
}
$$

```text
AI REASONING / SYNTHESIS
        |
        v
CODE / RULES / FSM / PLANNER
        |
        v
VERIFICATION
        |
        v
ORDINARY EXECUTABLE RUNTIME
```

The resulting runtime may no longer require the originating AI model.

---

## 附錄 C：Dynamic World State Machine Case

$$
\boxed{
W_{t+1}
=
F(
W_t,
A_t,
E_t,
H_t
).
}
$$

```text
World State
   ↓
Finite Actions
   ↓
Rules / Planning
   ↓
Events
   ↓
State Transition
   ↓
History
   ↺
```

可形成高度複雜行為，而不必每一步都由 LLM online generation 決定。

---

## 附錄 D：Functional Equivalence Leakage

```text
REGULATION BANS ARCHITECTURE A
        |
        v
FUNCTION STILL VALUABLE
        |
        v
ARCHITECTURE B IMPLEMENTS
SIMILAR BOUNDED FUNCTION
        |
        v
FUNCTIONAL EQUIVALENCE LEAKAGE
```

$$
\boxed{
F(T_B)
\approx_F
F(T_A)
}
$$

不表示兩者 architecture 或 risk 相同。

---

## 附錄 E：Regulatory Scope Trilemma

```text
          NARROWNESS
             /\
            /  \
           /    \
          /      \
 FUTURE-PROOF -- FUNCTIONAL
   CLARITY        COVERAGE
```

沒有聲稱三者不可同時改善；只表示存在結構性張力。

---

## 附錄 F：From AI Governance to Computation Governance

```text
Ban named AI technique
        ↓
functional substitutes appear
        ↓
regulate capability
        ↓
include symbolic / classical systems
        ↓
regulate high-impact computation
```

這是邏輯壓力，不是政策建議。

---

## 附錄 G：Three World-Engine Architectures

```text
A. ONLINE AI WORLD
LLM/model makes runtime decisions

B. COMPILED SYMBOLIC WORLD
AI generates rules/code at build time
runtime is symbolic/deterministic

C. HUMAN SYMBOLIC WORLD
humans write same rules/code
runtime is symbolic/deterministic
```

A、B、C 可以在 bounded interaction 上呈現接近行為，但 provenance、architecture、adaptivity 與 risk 並不相同。

---

## 附錄 H：UFI 系列進度

1. **UFI-01 — 鋸齒智能不是終局** — COMPLETE
2. **UFI-02 — 載體成長不對稱** — COMPLETE
3. **UFI-03 — 互補侵蝕** — COMPLETE
4. **UFI-04 — 競爭智能棘輪** — COMPLETE
5. **UFI-05 — 越有用越停不下來** — COMPLETE
6. **UFI-06 — AI 到底是什麼？** — COMPLETE
7. **UFI-07 — 從禁止 AI 到治理計算** — NEXT
8. **UFI-08 — 天真工具終局論的終結**

---

## 附錄 I：一句話版本

$$
\boxed{
\text{AI 可以把一部分「智能工作」編譯成普通程式；所以如果你真正想禁止的是能力，而不是某個模型名稱，監管邊界最後就會被逼著追逐功能，而不是只追逐「AI」這個標籤。}
}
$$

更短地：

$$
\boxed{
\text{當 AI 與 non-AI 之間可以透過程式生成、符號化、狀態機化與系統組合互相搬運功能時，「禁止 AI」最終會逼出一個更難的問題：到底要禁止的是哪種技術，還是計算本身能做到的某些事情？}
}
$$
