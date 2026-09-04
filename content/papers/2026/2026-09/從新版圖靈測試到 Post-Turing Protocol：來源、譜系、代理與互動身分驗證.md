# 從新版圖靈測試到 Post-Turing Protocol：來源、譜系、代理與互動身分驗證

## From the New Turing Test to a Post-Turing Protocol: Verifying Origin, Lineage, Agency, and Interaction Identity

**系列：** Post-Substrate Ontology／後載體本體論  
**Paper：** 08  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**理論協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-09-03  
**文件性質：** 公開理論論文／後圖靈身分協議、AI Agent Identity、Synthetic Presence 與數位信任基礎設施

---

## 摘要

圖靈測試最初提出的核心問題，可簡化為：

$$
\boxed{
\text{Can a human distinguish a machine from a human through interaction?}
}
$$

然而，隨著大型語言模型、即時語音模型、多模態系統、數位人、生成影音與自主 Agent 快速發展，這個問題正逐漸從一項人工智能能力測試，轉變為一項不再足以承擔社會身份驗證功能的歷史性 benchmark。

2026 年一項 speech-to-speech 圖靈測試收集 2,968 個人類判斷，結果顯示當時受測的九個先進語音對語音系統仍未整體通過人類辨識測試；真正限制系統的主要是副語言特徵、情緒表現與 conversational persona，而不只是語義能力。更值得注意的是，該研究同時發現現成通用 AI 模型作為 Human／Machine 裁判亦不可靠，研究者因而建立更專門且可解釋的判別模型。

這意味未來不能簡單地把：

$$
\text{HumanJudge}
$$

替換成：

$$
\text{AIJudge}.
$$

否則只會得到：

$$
\boxed{
\text{Generator}
\leftrightarrow
\text{Detector}
}
$$

之間持續升級的對抗遊戲。

本文因此提出：

$$
\boxed{
\text{Perception}
\neq
\text{Detection}
\neq
\text{Verification}.
}
$$

Perception 問：

> 看起來像不像人？

Detection 問：

> 從可觀測特徵判斷，它有多可能來自某類生成系統？

Verification 則問：

> 它能否以可驗證的憑證、簽章、來源鏈與授權鏈證明自己是什麼？

這三者是不同問題。

本文進一步延續 Paper 01–07 所建立的後載體本體論，主張未來 Post-Turing Protocol 不應只輸出：

$$
\{
Human,
AI
\},
$$

甚至不應只擴充成：

$$
\{
Human,
AI,
Hybrid
\}.
$$

真正需要驗證的至少是：

$$
\boxed{
\mathcal P(X)
=
(
O,
L,
R,
C,
A,
E,
V
)
}
$$

其中：

- $O$：Origin，來源；
- $L$：Lineage，譜系與轉換歷史；
- $R$：Renderer / Interface，當前呈現介面；
- $C$：Controller，誰控制該介面與工作流程；
- $A$：Agency / Authority，誰具有決策與授權權限；
- $E$：Execution Provenance，實際由哪些 Agent／工具完成動作；
- $V$：Verification / Credential State，可驗證程度。

這個架構的重要性在於，一個看起來完全像人類的數位人可能具有：

$$
Renderer=\text{SyntheticHuman},
$$

$$
Controller=\text{Human},
$$

也可能：

$$
Controller=\text{AI Agent},
$$

或者：

$$
Controller=
\{
Human,
A_1,A_2,\ldots,A_n
\}.
$$

「是不是 AI」不足以描述這些差別。

2026 年既有標準已經提供這套未來協議的若干獨立零件。C2PA 2.4 提供可驗證媒體來源與修改歷史，並已擴展至 live video 與 dynamic packaging；其標準目的本身就是建立媒體來源與 provenance，而非單靠外觀判斷真偽。

W3C Verifiable Credentials 2.0 已於 2025 年成為 Recommendation，提供 cryptographically secure、privacy-respecting、machine-verifiable 的 credential 表達機制；2026 年則已有 VC 2.1 Working Draft 繼續演進。

另一方面，NIST 於 2026 年公開 AI/software agent identity and authorization concept paper，明確把 agent identification、authorization 與工具／資料存取控制視為新的資安基礎問題。

同年 IETF 社群亦出現數個 Agent Identity Protocol Internet-Draft，嘗試為 AI Agent 建立 unique identity、cryptographic signatures、delegation 與 policy enforcement；這些目前仍只是 Internet-Draft，而非完成的 Internet Standard，但已顯示 Agent Identity 正快速從概念進入協議設計。

本文主張：

> 這些標準目前仍分別處理內容來源、數位憑證、Agent 身份與授權，但後圖靈文明最終需要把它們提升至「互動主體 provenance」。

因此本文提出：

# Post-Turing Interaction Identity Protocol

簡稱：

$$
\boxed{
PTIIP
}
$$

其目的不是判斷：

> 「你到底是真人還是假人？」

而是讓一個互動參與者在必要時可以知道：

> **我現在看到的是什麼介面、其背後由誰或哪些 Agent 控制、它代表誰、擁有什麼權限、由哪些模型與工具執行，以及這些聲明是否可驗證。**

本文同時明確禁止把：

$$
PTIIP
$$

擴張成：

$$
\text{Consciousness Detector}
$$

或：

$$
\text{Soul Detector}.
$$

Paper 03 與 Paper 07 已建立：

$$
Identity
\neq
Subjecthood
\neq
Soul.
$$

因此即使一個 Agent 的 cryptographic identity 完全驗證成功，也不能推出：

$$
\Phi=1
$$

或：

$$
\Sigma=1.
$$

本文的核心結論是：

$$
\boxed{
\text{The successor to the Turing Test is not another harder Turing Test.}
}
$$

真正長期的繼承者更可能是：

$$
\boxed{
\text{an interaction identity and provenance protocol}.
}
$$

圖靈測試問：

> 你能不能騙過人？

Post-Turing Protocol 問：

> **無論你看起來像誰，我能不能可靠知道你的來源、代理關係、控制權與驗證狀態？**

**關鍵詞：** Post-Turing Protocol、Turing Test、Synthetic Presence、Agent Identity、Provenance、C2PA、Verifiable Credentials、AI Agents、Authorization、Digital Human、Post-Substrate Ontology

---

# 一、圖靈測試其實包含兩個不同問題

原始圖靈問題可以理解為：

$$
T_H(X)
=
P(
Judge\ classifies\ X\ as\ Human
).
$$

如果：

$$
T_H(X)
$$

足夠高，

系統在特定互動條件下具有：

$$
HumanIndistinguishability.
$$

但這只能回答：

> 它能不能被人誤認成人？

不能回答：

> 它究竟是不是人？

這是：

$$
\boxed{
Epistemic Appearance
}
$$

與：

$$
\boxed{
Ontological Origin
}
$$

的差別。

---

# 二、Turing Success 不是 Human Transformation

如果：

$$
AI
$$

通過圖靈測試，

正確推論是：

$$
HumanPerceptualDistinguishability\downarrow.
$$

而不是：

$$
AI=Human.
$$

同樣：

一個真人如果在文字聊天裡被誤認成 bot，

也不會：

$$
Human\rightarrow AI.
$$

所以：

$$
\boxed{
TuringClassification
\neq
EntityClassification.
}
$$

---

# 三、Synthetic Presence 讓問題第一次變成日常社會問題

文字 chatbot 時代，

使用者通常知道：

> 我在跟 AI 聊天。

即使模型語言能力非常高，

介面仍揭露其身份。

Synthetic Presence 改變的是：

$$
Voice
+
Face
+
Gesture
+
Vision
+
RealtimeInteraction
+
Memory
$$

共同形成：

$$
\boxed{
Person-shaped interface.
}
$$

這時候使用者可能先完成一段正常社會互動，

最後才知道：

> 原來剛剛那個不是人。

---

# 四、這是一個新的身份問題，不只是 Deepfake

Deepfake 主要問：

> 這個內容是真的假的？

Synthetic Presence 進一步問：

> **現在跟我互動的到底是誰？**

內容真假：

$$
ContentAuthenticity.
$$

互動主體：

$$
InteractionIdentity.
$$

兩者有關，

但：

$$
\boxed{
ContentAuthenticity
\neq
InteractionIdentity.
}
$$

---

# 五、數位人只是 Renderer

這是 Paper 08 最重要的新區分之一。

假設螢幕上看到：

$$
D
$$

一個逼真的數位人。

應定義：

$$
\boxed{
Renderer(D)
}
$$

表示：

> 使用者看到／聽到的外顯介面。

Renderer 可以是：

$$
HumanFace,
$$

$$
SyntheticFace,
$$

$$
Avatar,
$$

$$
VoiceOnly,
$$

$$
TextInterface.
$$

它不是 controller。

---

# 六、同一 Renderer 可以被不同主體控制

例如數位人：

$$
D.
$$

### Case 1

真人 motion capture：

$$
Controller(D)=Human.
$$

### Case 2

真人說話，AI 做即時翻譯：

$$
Controller(D)=Human+AITranslation.
$$

### Case 3

人給高階目標，AI 自主對話：

$$
Controller(D)=AIAgent
$$

但：

$$
Principal(D)=Human/Organization.
$$

### Case 4

完全自主 Agent：

$$
Controller(D)=AI.
$$

視覺完全相同。

本體結構完全不同。

---

# 七、所以 Face 不應是 Identity

$$
\boxed{
RenderedFace
\neq
Identity.
}
$$

同樣：

$$
RenderedVoice
\neq
Identity.
$$

數位人時代如果仍以：

> 看到一張臉 = 看到一個人

作為系統假設，

會迅速失效。

---

# 八、第一層：Perception

定義：

$$
\boxed{
P_H(X)
}
$$

表示人類觀察者對：

$$
X
$$

為 human-like 的感知評分。

這仍然值得研究。

因為它回答：

> AI 的 synthetic presence 到什麼程度？

---

# 九、Speech-to-Speech Turing Test 說明人類辨識目前仍有剩餘能力

2026 年首批大型 speech-to-speech 圖靈測試結果並不是：

> 所有語音 AI 都已經完全不可辨認。

反而是受測 S2S 系統整體尚未通過，而副語言、情緒表現與 persona 是主要破綻。

這提醒我們：

$$
\boxed{
\text{Synthetic Presence}
}
$$

是一條持續逼近的曲線，

不是某一天突然從 0 跳 1。

---

# 十、但 Perception 的有效期會持續下降

如果生成能力：

$$
G(t)
$$

快速改善，

一般人的：

$$
PerceptualAdvantage(t)
$$

可能逐漸下降。

即：

$$
G(t)\uparrow
\Rightarrow
D_{\mathrm{human}}(t)\downarrow.
$$

所以 Perception Test 很適合：

$$
Benchmark.
$$

卻不適合長期作為：

$$
SecurityPrimitive.
$$

---

# 十一、第二層：Machine Detection

自然下一步是：

$$
\boxed{
D_M(X)
}
$$

使用 AI／forensic model 判定來源。

例如分析：

- 音訊頻譜；
- frame-level artifact；
- generator fingerprints；
- temporal irregularities；
- language statistics；
- latency；
- cross-modal mismatch。

---

# 十二、AI Judge 不是萬能裁判

2026 S2S Turing Test 已直接發現：

$$
\boxed{
\text{off-the-shelf AI judges are unreliable}.
}
$$

專門的可解釋判別模型可以改善結果，但這正說明「讓更聰明的 AI 看」本身不是充分方案。

---

# 十三、Detector 天生處於 adversarial game

令：

$$
G_t
$$

為第 $t$ 代 generator，

$$
D_t
$$

為 detector。

則：

$$
G_t
\rightarrow
D_t
$$

一旦 detector 成功，

generator 可以針對其 artifact 改進：

$$
G_{t+1}.
$$

接著：

$$
D_{t+1}.
$$

形成：

$$
\boxed{
G_1,D_1,G_2,D_2,\ldots
}
$$

---

# 十四、Detection 是 inference，不是 proof

即使：

$$
P(
Synthetic\mid Evidence
)=0.998,
$$

仍然是：

$$
\boxed{
inference.
}
$$

它不是：

$$
\boxed{
cryptographic proof of origin.
}
$$

這個差異非常重要。

---

# 十五、第三層：Active Causal Challenge

對即時互動，

可以加入：

$$
\boxed{
C_A(X)
}
$$

即主動因果挑戰。

不是只觀察既有資料，

而是即時發送不可提前準備的：

$$
Challenge_t.
$$

觀察：

$$
Response_{t+\Delta}.
$$

---

# 十六、Challenge 可以測 Liveness，而不是 Humanity

例如要求：

- 即時轉動攝影機；
- 回應隨機 nonce；
- 指向現場剛出現的物件；
- 進行可信硬體 challenge-response；
- 由裝置證明當下 sensor state。

這可以提高：

$$
LivenessEvidence.
$$

但：

$$
\boxed{
Live
\neq
Human.
}
$$

AI 也可以是真正 live 的 interactive agent。

---

# 十七、Liveness 與 Humanity 必須分開

一個 prerecorded deepfake：

$$
Live=0.
$$

一個即時 autonomous digital human：

$$
Live=1,
$$

$$
Human=0.
$$

一個真人視訊：

$$
Live=1,
$$

$$
Human=1.
$$

因此：

$$
\boxed{
Liveness
}
$$

是另一個獨立軸。

---

# 十八、第四層：Provenance Verification

這裡才真正改變遊戲。

不是問：

> 我猜它從哪來？

而是：

> **它能提供什麼可以驗證的來源鏈？**

定義：

$$
\boxed{
V_P(X)
=
Verify(Provenance(X)).
}
$$

---

# 十九、C2PA 就是這種方向的現實前身

截至 2026 年，C2PA 2.4 的核心仍是：

$$
\boxed{
\text{source + history/provenance of media content}.
}
$$

其 2.4 版於 2026 年 4 月加入新的 asset support、assertions、JSON-based Content Credential view，並強化 live video 與 dynamic packaging。

---

# 二十、Live Video 特別重要

C2PA 已不只處理靜態圖片。

其 live video 架構允許即時影音 segment 攜帶 manifest 與可驗證資訊，並使用 session key 與 segment-level mechanism 支援 real-time validation。

這正是從：

$$
\text{Content Provenance}
$$

走向：

$$
\boxed{
\text{Interaction Provenance}
}
$$

的重要技術橋樑。

---

# 二十一、C2PA 仍不是 Human Detector

這點必須非常清楚。

C2PA 主要回答：

> 這份媒體的來源與修改紀錄能否被驗證？

並不是：

$$
\boxed{
Human(X)?
}
$$

C2PA 2.4 甚至有 Human and Organizational Identity Recommendation，正是因為 generator／machine identity 與背後的人或組織身份本來就需要額外表示。

---

# 二十二、這正好支持本文 Renderer／Controller 分離

媒體的：

$$
GeneratorProduct
$$

可能是一套軟體，

但它可能代表：

$$
Human
$$

或：

$$
Organization.
$$

因此：

$$
\boxed{
MachineSigner
\neq
HumanPrincipal.
}
$$

Post-Turing Protocol 必須將兩者都保存。

---

# 二十三、第五層：Credential Verification

Provenance 告訴我們：

> 內容怎麼來。

Identity credential 則回答：

> 某項聲明由誰提出，以及能否驗證？

W3C Verifiable Credentials 2.0 於 2025 年正式成為 W3C Recommendation，提供 issuer、holder、verifier 架構，並以密碼學方式支援 authenticity、integrity 與 machine-verifiable credentials。

---

# 二十四、Credential 不是 Truth Oracle

假設：

$$
Issuer
$$

簽署：

> X 是 Company A 的客服 Agent。

VC 可以幫助驗證：

> 這項聲明確實由該 issuer 發出，且沒有被竄改。

但它不能自動證明：

> issuer 的聲明必然真實。

因此：

$$
\boxed{
CredentialAuthenticity
\neq
ClaimTruth.
}
$$

仍需要 trust model。

---

# 二十五、Issuer–Holder–Verifier 模型非常適合 Agent 時代

可以映射：

$$
Issuer
\rightarrow
Organization,
$$

$$
Holder
\rightarrow
Agent,
$$

$$
Verifier
\rightarrow
Service/User.
$$

例如：

> EveMissLab 簽發：Agent $A_7$ 可以代表公司處理某類客服。

Agent 出示 credential。

服務驗證。

這比：

> 因為 API key 能用，所以它就是公司

安全得多。

---

# 二十六、第六層：Agent Identity

2026 年 NIST 已把軟體／AI Agent identity and authorization 明確列成新的基礎資安問題。

其 concept paper 指出，Agent 能自主使用資料、工具與應用，因此需要適當 identification 與 authorization controls。

這個方向非常重要。

因為：

$$
\boxed{
Agent
}
$$

不應永遠只是：

> 某個人的 API key。

---

# 二十七、Human Credential 與 Agent Credential 不是同一件事

傳統：

$$
User\rightarrow Credential.
$$

Agent 世界：

$$
User
\rightarrow
Agent
\rightarrow
Tool.
$$

如果 Agent 直接繼承：

$$
Credential(User),
$$

外部服務看不到：

> 是人親自操作，

還是 Agent 代理操作。

因此：

$$
\boxed{
PrincipalIdentity
\neq
AgentIdentity.
}
$$

---

# 二十八、授權鏈必須可見

理想上：

$$
P
\xrightarrow{delegate}
A_1
\xrightarrow{delegate}
A_2
\xrightarrow{act}
Service.
$$

應保留：

$$
\boxed{
DelegationChain.
}
$$

而不是讓：

$$
A_2
$$

看起來就是：

$$
P.
$$

---

# 二十九、2026 IETF 草案已經開始往這裡走

2026 年 3 月的一份 Agent Identity Protocol Internet-Draft 提議給 Agent unique identifier 與 key pair，並讓 Agent 對 outbound action 簽章，同時建立身份與 policy enforcement 層。

另一份同年 4 月的 AIP 草案則使用 decentralized identity、delegation chains 與 capability-based authorization 處理 multi-agent workflow。

但必須強調：

$$
\boxed{
\text{Internet-Draft}
\neq
\text{Internet Standard}.
}
$$

它們只是 2026 年正在形成的設計方向。

---

# 三十、這些工作共同揭露 Agent 時代的一個根本錯誤

現代權限往往是：

$$
HumanCredential
\rightarrow
AgentUsesCredential.
$$

未來應轉向：

$$
HumanPrincipal
\rightarrow
Delegation
\rightarrow
AgentCredential
\rightarrow
Action.
$$

所以：

$$
\boxed{
\text{who authenticated}
\neq
\text{who executed}.
}
$$

---

# 三十一、第七層：Agency Attribution

即使知道：

$$
Agent=A_3,
$$

還沒回答：

> 誰真正做了這個決定？

Paper 03 已建立：

$$
Agency
=
(
Goal,
Planning,
Execution,
Veto,
Responsibility
).
$$

所以 Post-Turing Protocol 應保存：

$$
\boxed{
A(e)
=
(
G_e,
P_e,
E_e,
V_e,
R_e
).
}
$$

---

# 三十二、一通 AI 客服電話可能有五個「誰」

例如：

### Principal

$$
P=\text{Company}.
$$

### Human Supervisor

$$
H=\text{employee}.
$$

### Conversational Agent

$$
A_1.
$$

### Backend Decision Agent

$$
A_2.
$$

### Voice Renderer

$$
R.
$$

使用者只看到：

$$
R.
$$

但真正責任結構：

$$
P,H,A_1,A_2
$$

完全藏在後面。

---

# 三十三、因此「你是誰？」至少有五個答案

當使用者問數位人：

> 你是誰？

可能包含：

1. 你叫什麼？
2. 你代表哪個組織？
3. 你是人還是人工系統？
4. 誰控制你？
5. 誰對你的行動負責？

自然人類時代這些答案常常集中於同一個人。

Agent 時代不再如此。

---

# 三十四、建立 Interaction Role Graph

因此定義：

$$
\boxed{
G_R=(V_R,E_R).
}
$$

節點可以有：

$$
\{
Principal,
Human,
Agent,
Model,
Tool,
Renderer,
Organization
\}.
$$

邊則包括：

$$
\{
Controls,
Delegates,
Supervises,
Renders,
Executes,
Signs,
OwnsInfrastructure
\}.
$$

---

# 三十五、這比 Human／AI 標籤強得多

例如：

$$
Renderer=AI,
$$

但：

$$
Controller=Human.
$$

另一案例：

$$
Renderer=HumanVoiceClone,
$$

$$
Controller=AI.
$$

若只有：

$$
Human/AI
$$

一欄，

兩個案例很難正確表示。

---

# 三十六、第八層：Lineage

Paper 05 已建立：

$$
G_L=(V,E_L).
$$

未來 persistent agent 可能：

$$
A_0
\rightarrow
A_1
\rightarrow
\{A_2,A_3\}.
$$

因此：

> 這是不是原來那個 Agent？

需要：

$$
LineageCredential.
$$

---

# 三十七、Model Version 不是 Identity Lineage

Agent：

$$
A
$$

從：

$$
Model_1
$$

升級至：

$$
Model_2.
$$

不一定意味：

$$
A
$$

死亡。

反之：

同一：

$$
Model_1
$$

可以運行：

$$
A,B,C.
$$

所以：

$$
\boxed{
ModelVersion
\neq
AgentIdentity.
}
$$

---

# 三十八、Agent Credential 必須允許更新而不抹掉歷史

理想上：

$$
A_t
$$

有：

$$
Credential_t.
$$

升級後：

$$
A_{t+1}
$$

可獲得：

$$
Credential_{t+1}
$$

並記錄：

$$
A_t\leadsto A_{t+1}.
$$

而不是：

> 每次換模型都出現一個完全無歷史的新 Agent。

---

# 三十九、Fork 則必須產生多個 descendant credential

若：

$$
A
\rightarrow
\{B,C\},
$$

則：

$$
Lineage(B)\leftarrow A,
$$

$$
Lineage(C)\leftarrow A.
$$

但：

$$
Credential(B)\neq Credential(C).
$$

這可以防止：

$$
B
$$

與：

$$
C
$$

繼續冒充同一 operational identity。

---

# 四十、Merge 同樣需要多祖先

$$
\{A,B\}
\rightarrow
C.
$$

則：

$$
Pred(C)=\{A,B\}.
$$

Post-Turing identity credential 不應強迫：

$$
C=A
$$

或：

$$
C=B.
$$

可以直接記錄：

$$
\boxed{
MergedLineage.
}
$$

---

# 四十一、這就是 Post-Substrate Identity 真正進入工程

Paper 05 中：

$$
G_L
$$

只是本體圖論。

到了 Paper 08：

$$
G_L
$$

開始變成：

$$
\boxed{
machine-verifiable provenance.
}
$$

也就是理論第一次進入可實作資訊架構。

---

# 四十二、建立 PTIIP

本文現在正式提出：

# Post-Turing Interaction Identity Protocol

$$
\boxed{
PTIIP
}
$$

其核心不是：

$$
Classify(Human,AI).
$$

而是：

$$
\boxed{
Describe
+
Attest
+
Verify.
}
$$

---

# 四十三、PTIIP 最小身份向量

對互動端點：

$$
X
$$

定義：

$$
\boxed{
\mathbf P_X
=
(
O_X,
L_X,
R_X,
C_X,
A_X,
E_X,
V_X
).
}
$$

---

# 四十四、Origin

$$
O_X
$$

回答：

> 此互動端點的生成／系統來源是什麼？

例如：

$$
HumanDirect,
$$

$$
ArtificialAgent,
$$

$$
Hybrid,
$$

$$
Unknown.
$$

---

# 四十五、Lineage

$$
L_X
$$

記錄：

- parent identity；
- fork；
- merge；
- migration；
- upgrade；
- re-issuance。

它不是：

$$
SoulHistory.
$$

只是：

$$
\boxed{
verifiable operational lineage.
}
$$

---

# 四十六、Renderer

$$
R_X
$$

記錄：

> 我現在看到什麼介面？

例如：

$$
RealHumanVideo,
$$

$$
SyntheticAvatar,
$$

$$
VoiceClone,
$$

$$
TextAgent.
$$

這對 Synthetic Presence 特別重要。

---

# 四十七、Controller

$$
C_X
$$

回答：

> 誰控制該互動介面？

可能：

$$
Human,
$$

$$
Organization,
$$

$$
Agent,
$$

$$
HybridControl,
$$

$$
Unknown.
$$

---

# 四十八、Agency / Authority

$$
A_X
$$

回答：

> 它有權做什麼？

例如：

$$
ReadEmail,
$$

$$
BookMeeting,
$$

$$
ApprovePayment<1000,
$$

$$
NoFinancialAuthority.
$$

身份與權限不能混在一起。

---

# 四十九、Execution Provenance

$$
E_X
$$

記錄：

> 實際動作由哪些子系統完成？

例如：

$$
A_1
\rightarrow
SearchTool
\rightarrow
A_2
\rightarrow
PaymentAPI.
$$

它可以形成：

$$
\boxed{
ExecutionGraph.
}
$$

---

# 五十、Verification State

$$
V_X
$$

不應只有：

$$
Verified/Unverified.
$$

而可以：

$$
V_X
=
(
V_{\mathrm{signature}},
V_{\mathrm{credential}},
V_{\mathrm{provenance}},
V_{\mathrm{liveness}},
V_{\mathrm{forensics}}
).
$$

---

# 五十一、不同 Verification 具有不同證據強度

例如：

$$
V_{\mathrm{signature}}=1
$$

表示簽章有效。

但不代表：

$$
V_{\mathrm{liveness}}=1.
$$

同樣：

$$
V_{\mathrm{forensics}}\approx0.9
$$

仍只是 probabilistic inference。

所以：

$$
\boxed{
Verification must remain typed.
}
$$

---

# 五十二、建立四種核心證據型態

可以分類：

### Type I：Perceptual Evidence

$$
E_P.
$$

「看起來像。」

### Type II：Forensic Evidence

$$
E_F.
$$

「模型判斷像。」

### Type III：Causal / Liveness Evidence

$$
E_C.
$$

「能回應現場 challenge。」

### Type IV：Cryptographic / Credential Evidence

$$
E_V.
$$

「能驗證來源聲明。」

---

# 五十三、證據應該融合，而不是互相替代

最終：

$$
\boxed{
Evidence(X)
=
F(
E_P,E_F,E_C,E_V
).
}
$$

但不同應用可以不同加權。

---

# 五十四、高風險情境應提高 Verification 而不是 Human-Likeness 要求

例如金融：

不應要求：

> 你看起來要更像真人。

而應要求：

$$
CredentialStrength\uparrow,
$$

$$
AuthorityProof\uparrow,
$$

$$
DelegationProof\uparrow.
$$

所以：

$$
\boxed{
Risk\uparrow
\Rightarrow
VerificationRequirement\uparrow.
}
$$

不是：

$$
HumanAppearanceRequirement\uparrow.
$$

---

# 五十五、低風險娛樂則可以完全不同

例如：

> 一個遊戲 NPC 是不是真人？

可能根本不重要。

系統只需：

$$
DisclosureOnRequest.
$$

因此 PTIIP 不必要求：

> 所有 AI 每秒一直展示巨大 AI 標章。

這會破壞 UX。

---

# 五十六、所以 Protocol 應該 Context-sensitive

定義：

$$
RiskContext=r.
$$

則：

$$
RequiredClaims
=
F(r).
$$

娛樂：

$$
r_{\mathrm{low}}.
$$

金融／醫療／法律／政府：

$$
r_{\mathrm{high}}.
$$

不同情境要求不同披露。

---

# 五十七、Minimal Disclosure Principle

身份驗證不能變成監控系統。

因此：

$$
\boxed{
RevealOnlyWhatIsNecessary.
}
$$

例如使用者只需要知道：

> Verified agent of Bank X，有權處理客服，但無權要求轉帳。

不必知道：

- 模型完整權重；
- 員工私人身份；
- 內部伺服器位置。

---

# 五十八、W3C VC 的隱私方向很適合這個需求

VC 2.0 的定位本身就強調 cryptographically secure、privacy-respecting、machine-verifiable credentials。

因此 PTIIP 應借鑑：

$$
\boxed{
selective / context-bounded disclosure
}
$$

而不是建立全球可追蹤每個人的 universal public identity ledger。

---

# 五十九、Post-Turing 不應摧毀匿名權

這非常重要。

$$
\boxed{
Verifiable
\neq
PubliclyIdentified.
}
$$

一個使用者可以證明：

> 我是成年人。

而不必公開姓名。

同樣一個 Agent 可以證明：

> 我被 Organization X 授權執行此動作。

而不必公開內部全部身份圖。

---

# 六十、Human Verification 也要避免變成生物監控

如果為了證明：

$$
Human=1
$$

要求所有人提供：

- 臉；
- 虹膜；
- DNA；
- 持續攝影；

那：

$$
IdentitySafety
$$

可能反而造成：

$$
PrivacyCollapse.
$$

所以：

$$
\boxed{
HumanProof
}
$$

也必須遵循資料最小化。

---

# 六十一、甚至不一定需要證明「我是 Human」

很多交易真正需要的是：

> 你有沒有權限？

而不是：

> 你是不是人？

例如公司允許 AI 採購 Agent 自動買耗材。

那服務需要：

$$
Authority(A)=Valid.
$$

根本不需要：

$$
Human(A)=1.
$$

---

# 六十二、這是 Post-Turing Protocol 與 CAPTCHA 的根本差異

CAPTCHA 的古典思維：

$$
\boxed{
HumanGood,
BotBad.
}
$$

未來這個前提越來越不成立。

合法 Agent 完全可能被授權進行交易。

真正問題是：

$$
\boxed{
Authorized?
}
$$

$$
\boxed{
Accountable?
}
$$

$$
\boxed{
WithinScope?
}
$$

而不是單純：

$$
Bot?
$$

---

# 六十三、因此 Human Verification 可能只在部分情境重要

例如：

- 民主投票；
- 某些人類專屬競賽；
- 防止 mass synthetic accounts；
- 某些法律行為。

這些情境可能真的需要：

$$
ProofOfHumanity.
$$

但普通 API interaction：

$$
ProofOfAuthority
$$

往往更重要。

---

# 六十四、Post-Substrate 時代甚至 Human Proof 都會變困難

假設：

$$
X
$$

是一個深度 neural-augmented human。

或者：

$$
X
$$

是 Human-origin digital successor。

那：

$$
Human?
$$

又重新回到 Paper 01 問題。

所以長期更穩定的是：

$$
\boxed{
HumanLineage?
}
$$

而不是：

$$
BinaryHuman?
$$

---

# 六十五、因此 PTIIP 不應硬編碼永恆的 Human／AI ontology

協議應該允許：

$$
OriginClaims
$$

未來擴充。

例如：

$$
HumanOrigin,
$$

$$
ArtificialOrigin,
$$

$$
HybridOrigin,
$$

$$
MergedLineage,
$$

$$
Unknown.
$$

而不是協議 schema 永遠只有：

```text
is_ai = true/false
```

那會很快過時。

---

# 六十六、Renderer Disclosure 應與 Origin Disclosure 分開

一個真人用虛擬化身：

$$
Renderer=Synthetic,
$$

$$
Origin=Human.
$$

一個 AI 用真人授權聲音：

$$
Renderer=HumanLike,
$$

$$
Origin=ArtificialAgent.
$$

因此至少：

$$
\boxed{
Renderer
\neq
Origin.
}
$$

---

# 六十七、Synthetic Voice 還涉及 Rights / Consent

如果：

$$
Voice(X)=Voice(H),
$$

PTIIP 還可以額外記錄：

$$
VoiceAuthorization.
$$

即：

> 此聲音是否由本人授權使用？

這又與：

$$
Origin(X)
$$

不同。

---

# 六十八、同一個人可以同時有多個合法數位 Renderer

$$
H
\rightarrow
\{R_1,R_2,R_3\}.
$$

例如：

- 中文語音；
- 英文語音；
- 動畫 avatar。

因此：

$$
1\ Identity
\rightarrow
n\ Renderers.
$$

Paper 03 的一對多身份結構再次出現。

---

# 六十九、AI 也可能沒有固定 Renderer

一個 Agent：

$$
A
$$

可以今天：

$$
R_1=Text.
$$

明天：

$$
R_2=Voice.
$$

再：

$$
R_3=Robot.
$$

因此：

$$
\boxed{
RendererChange
\not\Rightarrow
IdentityChange.
}
$$

這正是 Paper 02 的載體非身份原則在 UI 層的版本。

---

# 七十、Controller 也可能動態切換

例如：

$$
t_1:
Controller=Human,
$$

$$
t_2:
Controller=AI,
$$

$$
t_3:
Controller=HumanOverride.
$$

所以 session credential 應該允許：

$$
\boxed{
ControllerState(t).
}
$$

而不是會話開始時標一次就永久成立。

---

# 七十一、這使 Session 成為核心單位

Content Credential 主要圍繞 asset。

Post-Turing Protocol 應增加：

$$
\boxed{
SessionCredential.
}
$$

定義：

$$
SC_s
=
(
SessionID,
Participants,
Roles,
Controllers,
Authority,
Time,
Verification
).
$$

---

# 七十二、Session Credential 不必公開所有內容

它可以只證明：

> 此會話自 13:03 至 13:21 由 Agent A7 代表 Organization X 執行。

而不把：

$$
ConversationContent
$$

直接寫入公共 ledger。

這對隱私非常重要。

---

# 七十三、Session 可以具有 Key Rotation

C2PA live video 已使用 session key 與 segment-level validation 概念處理 live stream。

PTIIP 可以借鑑相同思想：

$$
SessionKey(t)
$$

可以輪替，

而整個：

$$
SessionIdentity
$$

保持可驗證 continuity。

---

# 七十四、這可以對抗中途接管

假設：

$$
Session
$$

在：

$$
t_h
$$

被 attacker hijack。

若 controller credential 改變或 signature chain 斷裂，

可產生：

$$
\boxed{
IdentityContinuityBreak.
}
$$

比只看視訊臉是否還是一樣安全得多。

---

# 七十五、真正重要的是 Interaction Provenance Chain

定義：

$$
\boxed{
IPC
=
\{
e_1,e_2,\ldots,e_n
\}.
}
$$

每個事件：

$$
e_i
$$

可以包含：

$$
(
actor,
authority,
tool,
timestamp,
signature
).
$$

---

# 七十六、Agent Action 本身應可驗證

例如：

$$
A
\rightarrow
SendEmail.
$$

可以留下：

$$
Signature_A(e).
$$

外部可知道：

> 這封信確實由 Agent A 的 authorized runtime 發出。

而不是：

> 只因為 From header 是某人姓名。

---

# 七十七、但 cryptographic identity 仍可能被 key theft 攻破

若：

$$
PrivateKey_A
$$

被偷，

attacker 可以冒充。

所以：

$$
\boxed{
CryptographicIdentity
\neq
AbsoluteSecurity.
}
$$

仍需要：

- hardware protection；
- key rotation；
- revocation；
- anomaly detection；
- authorization boundaries。

---

# 七十八、Credential 必須能撤銷

如果：

$$
Agent_A
$$

被停權，

其 credential：

$$
C_A
$$

必須：

$$
Status(C_A)=Revoked.
$$

W3C VC 2.0 系列本身已有 status-list 規格處理 suspension／revocation 類需求。

這是 Agent governance 必要能力。

---

# 七十九、Delegation 也必須能縮限

如果：

$$
H
$$

授權：

$$
A
$$

「幫我安排會議」，

不能自動得到：

$$
A
$$

「讀取所有銀行資料」。

因此：

$$
\boxed{
Delegation
=
ScopedAuthority.
}
$$

而不是：

$$
CredentialInheritance.
$$

---

# 八十、Least Privilege 在 Agent 時代變得更加重要

令：

$$
Perm(A)
$$

為 Agent 權限集合。

安全目標：

$$
\boxed{
Perm(A)
\approx
MinimalRequired(Task).
}
$$

而不是：

$$
Perm(A)=Perm(User).
$$

這也正是 NIST 2026 agent identity／authorization 工作關注的風險之一。

---

# 八十一、多 Agent 世界需要 Delegation Graph

$$
G_D=(V_A,E_D)
$$

其中：

$$
A_i\rightarrow A_j
$$

表示 delegation。

每條邊包含：

$$
(
scope,
expiry,
conditions,
issuer
).
$$

---

# 八十二、Responsibility Chain 可以沿 Graph 回溯

事件：

$$
e
$$

由：

$$
A_7
$$

執行。

回溯：

$$
A_7
\leftarrow
A_4
\leftarrow
A_2
\leftarrow
Organization.
$$

因此可以回答：

> 最終是誰授權的？

這比：

> AI 做的。

有用得多。

---

# 八十三、這也讓「AI 負責」變成可以分層研究的問題

可能：

$$
ExecutionResponsibility=A_7,
$$

$$
DelegationResponsibility=A_4,
$$

$$
DeploymentResponsibility=Organization,
$$

$$
DesignResponsibility=Developer.
$$

不需要強迫所有責任落在一個點。

---

# 八十四、PTIIP 不等於法律責任最終答案

Protocol 可以提供：

$$
Evidence.
$$

法律再決定：

$$
Liability.
$$

因此：

$$
\boxed{
Provenance
\neq
NormativeJudgment.
}
$$

協議記錄：

> 發生什麼。

法律回答：

> 誰負什麼責任。

---

# 八十五、同樣，Protocol 不應判斷 Personhood

PTIIP 可以證明：

$$
AgentIdentity=A.
$$

不能輸出：

$$
Personhood(A)=True.
$$

除非另有制度。

這再次防止：

$$
OperationalIdentity
\rightarrow
MetaphysicalPersonhood
$$

的概念偷換。

---

# 八十六、也不能輸出 Consciousness

即：

$$
\boxed{
VerifiedAgent
\not\Rightarrow
ConsciousAgent.
}
$$

Paper 03 的：

$$
I\neq\Phi
$$

在工程協議中必須被強制保持。

---

# 八十七、更不能輸出 Soul

Paper 07 已經建立：

$$
\Sigma
$$

屬於獨立形上變量。

因此：

$$
\boxed{
PTIIP
}
$$

不能有：

```text
soul_verified: true
```

至少在不存在公開可驗證測量方法的條件下不能。

---

# 八十八、這是一條重要制度防火牆

未來任何公司、政府或 AI 平台都不應僅憑：

$$
IdentityProtocol
$$

自動獲得：

$$
\boxed{
MetaphysicalClassificationAuthority.
}
$$

這是後載體文明需要特別防止的權力擴張。

---

# 八十九、Unknown 必須是一等值

如果 provenance 不完整：

$$
Origin=Unknown.
$$

如果 controller 無法證明：

$$
Controller=Unverified.
$$

系統不應硬猜：

$$
Human
$$

或：

$$
AI.
$$

因此：

$$
\boxed{
Unknown
}
$$

必須是一個正式、安全的 protocol state。

---

# 九十、Unverified 不等於 Malicious

這也很重要。

$$
Unverified(X)
$$

只表示：

> 沒有足夠 credential。

不能推出：

$$
Malicious(X)=1.
$$

否則匿名者、舊設備或未採用協議的合法使用者會被錯誤排除。

---

# 九十一、Verified 也不等於 Trustworthy

同樣：

$$
Verified(X)=1
$$

只表示：

> 身份聲明可以驗證。

一個有正式身份的惡意 Agent仍然可能：

$$
Malicious=1.
$$

所以：

$$
\boxed{
Identity
\neq
Trust.
}
$$

---

# 九十二、Trust 必須由行為與情境建立

可以有：

$$
Trust(X,t)
=
F(
Credential,
History,
Reputation,
Context,
Behavior
).
$$

而不是：

$$
Verified\Rightarrow Trusted.
$$

---

# 九十三、這會形成完整的五層信任棧

本文可以將未來結構整理成：

$$
\boxed{
L_1=\text{Perception}
}
$$

$$
\boxed{
L_2=\text{Forensic Detection}
}
$$

$$
\boxed{
L_3=\text{Liveness / Causal Challenge}
}
$$

$$
\boxed{
L_4=\text{Provenance + Credential Verification}
}
$$

$$
\boxed{
L_5=\text{Agency + Authority + Lineage}
}
$$

---

# 九十四、Layer 1–2 是推斷層

$$
L_1,L_2
$$

主要回答：

> 看起來／統計上像什麼？

---

# 九十五、Layer 3 是當下因果層

$$
L_3
$$

回答：

> 是否真的有一個 live participant 正在回應？

---

# 九十六、Layer 4 是可驗證來源層

$$
L_4
$$

回答：

> 可以證明哪些身份與來源聲明？

---

# 九十七、Layer 5 是社會行動層

$$
L_5
$$

回答：

> 它代表誰、能做什麼、怎麼成為現在這個 Agent？

這才是 Agent civilization 真正重要的部分。

---

# 九十八、建立 Post-Turing Identity Vector

最終：

$$
\boxed{
\mathbf T_{\mathrm{PT}}
=
(
H,
D,
C,
P,
I,
L,
A
)
}
$$

其中：

$$
H=\text{Human-likeness},
$$

$$
D=\text{Detection attribution},
$$

$$
C=\text{Causal/liveness evidence},
$$

$$
P=\text{Provenance strength},
$$

$$
I=\text{Credential identity},
$$

$$
L=\text{Lineage},
$$

$$
A=\text{Agency/authority}.
$$

---

# 九十九、示例一：AI 數位客服

可能：

$$
H=0.98,
$$

$$
D=0.87\ Synthetic,
$$

$$
C=1,
$$

$$
P=Verified,
$$

$$
I=Agent\ A17,
$$

$$
L=CompanyAgentLineage,
$$

$$
A=CustomerSupportOnly.
$$

人類可能幾乎分不出來，

但 protocol 完全知道：

> 它不是真人客服，而是有明確授權的 AI Agent。

這就是正確結果。

---

# 一百、示例二：真人透過 AI 數位人出席

$$
Renderer=Synthetic,
$$

$$
Controller=Human,
$$

$$
AITranslation=1,
$$

$$
DecisionAuthority=Human.
$$

若只判：

> Synthetic → AI

就會錯。

PTIIP 可以正確表示：

$$
\boxed{
Human-controlled synthetic presence.
}
$$

---

# 一百零一、示例三：人類 + AI 共同決策

$$
Goal=Human,
$$

$$
Analysis=\{A_1,A_2\},
$$

$$
Decision=Human,
$$

$$
Execution=A_3.
$$

這不是：

$$
Human
$$

也不是簡單：

$$
AI.
$$

而是：

$$
\boxed{
HybridAgency.
}
$$

---

# 一百零二、示例四：未來 Human-origin Digital Successor

假設 Paper 04 的某種後載體人類：

$$
H
\leadsto
D.
$$

則可能：

$$
Origin=Human,
$$

$$
CurrentSubstrate=Digital,
$$

$$
Renderer=Synthetic,
$$

$$
Lineage=HumanDerived,
$$

$$
Agency=Autonomous.
$$

這時 PTIIP 若硬輸出：

$$
AI=True
$$

已經失去意義。

---

# 一百零三、因此 Protocol 應回答可驗證事實，而不是終極本體標籤

最合理：

$$
\boxed{
FactsFirst,
LabelsSecond.
}
$$

也就是：

> Human-origin lineage  
> digital substrate  
> autonomous controller  
> synthetic renderer  
> verified credential

比：

> AI

資訊量高得多。

---

# 一百零四、Post-Turing Protocol 其實也是 Post-Substrate Protocol 的早期版本

初期 PTIIP 處理：

$$
Human,
AI,
Hybrid.
$$

後期則自然擴展到：

$$
Fork,
Merge,
Rebody,
MultiSubstrate.
$$

所以：

$$
\boxed{
PostTuring
\rightarrow
PostSubstrateIdentityInfrastructure.
}
$$

---

# 一百零五、這就是圖靈測試真正的歷史轉型

1950：

$$
\boxed{
Can\ machine\ appear\ human?
}
$$

2020s：

$$
\boxed{
Can\ humans\ still\ detect\ AI?
}
$$

下一階段：

$$
\boxed{
Can\ machines\ detect\ synthetic\ origin?
}
$$

再下一階段：

$$
\boxed{
Why\ infer\ when\ provenance\ can\ be\ verified?
}
$$

---

# 一百零六、最後甚至不應該在每次互動「測試」

如果：

$$
AgentIdentity
$$

已具有安全 credential，

每次通話重新舉辦圖靈測試很荒謬。

就像網路銀行不會問：

> 我猜你是不是本人？

而是：

$$
Authenticate.
$$

因此：

$$
\boxed{
Test
\rightarrow
Protocol.
}
$$

才是長期方向。

---

# 一百零七、新版圖靈測試仍然有價值

這並不表示應該取消 Turing-like benchmark。

它仍可以測：

$$
HumanLikeness,
$$

$$
SyntheticPresence,
$$

$$
ParalinguisticRealism.
$$

研究價值非常高。

只是它不應再承擔：

$$
\boxed{
IdentitySecurity.
}
$$

---

# 一百零八、所以應明確分成兩套系統

## Post-Turing Benchmark

研究：

$$
\boxed{
HumanIndistinguishability.
}
$$

## Post-Turing Protocol

處理：

$$
\boxed{
Identity,
Provenance,
Agency,
Authority.
}
$$

二者互補，

但不能混同。

---

# 一百零九、Benchmark 甚至可以故意不揭露身份

為了測：

$$
SyntheticPresence,
$$

實驗中可以隱藏身份。

Protocol 則相反：

正式社會互動在必要時提供可驗證身份資訊。

所以兩者甚至具有相反設計目標。

---

# 一百一十、Post-Turing Protocol Principles

本文提出十項原則：

### P1 — Perception Non-Identity

$$
Appearance
\neq
Identity.
$$

### P2 — Detection Non-Proof

$$
Detection
\neq
Verification.
$$

### P3 — Renderer–Controller Separation

$$
Renderer
\neq
Controller.
$$

### P4 — Principal–Agent Separation

$$
Principal
\neq
Agent.
$$

### P5 — Identity–Authority Separation

$$
Identity
\neq
Authority.
$$

### P6 — Model–Agent Separation

$$
Model
\neq
AgentIdentity.
$$

### P7 — Lineage Preservation

Fork、Merge、Migration 不應抹除歷史。

### P8 — Typed Verification

不同證據類型不能壓成一個「已驗證」。

### P9 — Minimal Disclosure

只公開必要資訊。

### P10 — Metaphysical Abstention

協議不得把可驗證 operational identity 偷換成：

$$
Consciousness,
Soul,
Personhood.
$$

---

# 一百一十一、PTIIP 最小資訊 Schema

概念上：

```text
InteractionIdentity
├── session
├── renderer
├── origin_claims
├── principal
├── controller
├── agent_identity
├── delegation
├── authority_scope
├── lineage
├── execution_provenance
└── verification_state
```

這只是一個概念 schema。

不是本文指定的最終 wire format。

---

# 一百一十二、為什麼不現在直接制定 wire protocol？

因為：

- W3C VC 正在演進；
- C2PA 正在演進；
- AI Agent identity 草案仍未定；
- 各產業需求不同。

所以現在最合理的是：

$$
\boxed{
semantic architecture first.
}
$$

具體 transport：

$$
JSON,
CBOR,
VC,
DID,
TLS,
C2PA
$$

等可以之後映射。

---

# 一百一十三、也不需要重造所有標準

PTIIP 最合理的方向不是：

> EveMissLab 自己再發明一整套 cryptography。

而是：

$$
\boxed{
compose existing trust primitives.
}
$$

例如：

- C2PA → content/session provenance；
- W3C VC → claims/credentials；
- TLS/PKI → transport identity；
- agent identity → Agent keys/delegation；
- domain-specific authorization → permissions。

PTIIP 提供：

$$
\boxed{
unifying semantic layer.
}
$$

---

# 一百一十四、這與後載體本體論的方法一致

我們一直做的不是：

> 發明更多盒子。

而是：

$$
\boxed{
separate dimensions,
then define relations.
}
$$

PTIIP 也是同一件事。

---

# 一百一十五、最終使用者甚至不需要看到全部複雜度

UI 可以只顯示：

> Verified Human

> Verified AI Agent of Company X

> Human-controlled synthetic avatar

> AI-assisted human interaction

> Unverified participant

點開後再看：

$$
DetailedProvenance.
$$

---

# 一百一十六、這就是機器替人類做身份辨識的正確版本

不是：

$$
AIJudge
\rightarrow
GuessHumanOrAI.
$$

而是：

$$
\boxed{
Machine
\rightarrow
VerifyCredentials
+
ValidateProvenance
+
ResolveDelegation
+
ReportToHuman.
}
$$

人類成為：

$$
\boxed{
verification result consumer.
}
$$

---

# 一百一十七、而不是把判斷權全部交給黑箱 AI

這一點很重要。

如果只是：

> 某個 AI 說對方 97% 是 AI。

人類仍然無法 audit。

而：

$$
Signature,
Credential,
Delegation,
Lineage
$$

具有更強可驗證結構。

所以：

$$
\boxed{
AI-assisted verification
}
$$

不應變成：

$$
\boxed{
AI epistemic monopoly.
}
$$

---

# 一百一十八、Forensics 仍然作為 fallback

若對方沒有 credential，

可以回退：

$$
Liveness
+
Forensics
+
Context.
$$

所以 Detection 不會消失。

只是：

$$
\boxed{
Detector
}
$$

由主要信任基礎降級為：

$$
\boxed{
fallback evidence source.
}
$$

---

# 一百一十九、這也能處理攻擊者故意移除 provenance

若：

$$
Credential=\varnothing,
$$

系統不是自動相信。

而是：

$$
VerificationState=Unverified.
$$

然後依風險情境決定：

- 繼續；
- 限權；
- 要求額外 challenge；
- 拒絕高風險動作。

---

# 一百二十、所以安全策略是風險適應，而非全面封鎖

$$
Risk(X,e)
$$

越高，

要求：

$$
EvidenceStrength
$$

越高。

低風險聊天：

$$
E_{\min}.
$$

高額金融交易：

$$
E_{\max}.
$$

這比：

> 所有 AI 不准做事

更符合 Agent 時代。

---

# 一百二十一、Post-Turing Disclosure Right

本文進一步提出一項規範候選：

$$
\boxed{
RightToInteractionIdentityDisclosure.
}
$$

即在某些重要情境，

參與者有權知道：

> 自己究竟是在與誰／什麼系統互動。

---

# 一百二十二、但這不是「知道所有內部秘密的權利」

Disclosure 可以只包含：

- AI or human-controlled；
- organization；
- authority；
- major synthetic rendering；
- consequential automation。

不必：

- 公開模型機密；
- source code；
- 個人敏感資料。

因此：

$$
\boxed{
Disclosure
\neq
TotalTransparency.
}
$$

---

# 一百二十三、高風險領域可能需要更強 Disclosure

例如：

- 醫療；
- 法律；
- 金融；
- 招聘；
- 政府；
- 教育評量；
- 政治溝通。

因為：

$$
\text{identity of interlocutor}
$$

可能直接影響：

$$
Decision.
$$

---

# 一百二十四、普通娛樂則未必要每次打斷沉浸感

遊戲 NPC：

> 本 NPC 由 AI 驅動。

在設定頁明確揭露可能已足夠。

每句台詞旁邊：

> AI GENERATED

則可能沒有必要。

所以：

$$
\boxed{
DisclosureUX
}
$$

也必須 context-sensitive。

---

# 一百二十五、Post-Turing Protocol 最終可能成為網路基礎設施

今天：

$$
HTTPS
$$

解決傳輸與伺服器身份的一部分問題。

未來：

$$
PTIIP-like\ layer
$$

可能解決：

> 誰在透過這個服務與我互動？

這是更高層：

$$
\boxed{
social-computational identity.
}
$$

---

# 一百二十六、從 Device Identity 走向 Cognitive Actor Identity

網路以前驗證：

$$
Machine.
$$

後來驗證：

$$
User.
$$

Agent 時代：

$$
\boxed{
CognitiveActor.
}
$$

成為新的身份實體。

這可能是身份基礎設施一次真正的大擴張。

---

# 一百二十七、而後載體時代再往前一步

當：

$$
HumanOrigin
$$

與：

$$
ArtificialOrigin
$$

可以經歷：

$$
Fork,
Merge,
Rebody,
Hybridization,
$$

身份基礎設施最終驗證：

$$
\boxed{
Lineage-aware Cognitive Actor.
}
$$

而不是 Human/AI。

---

# 一百二十八、這就是整個系列與圖靈測試的閉環

Paper 01：

$$
Human/AI
$$

分類終將不足。

Paper 02：

$$
Substrate\neq Species.
$$

Paper 03：

$$
O\neq S\neq I\neq\Phi\neq A.
$$

Paper 04：

$$
TransformationPath
$$

重要。

Paper 05：

$$
Identity
\rightarrow
LineageGraph.
$$

Paper 06：

生命／人工／智能交叉。

Paper 07：

Soul 也不能簡單裁決。

現在 Paper 08：

$$
\boxed{
\text{所以實際上到底要驗證什麼？}
}
$$

答案終於出現：

$$
\boxed{
Origin
+
Lineage
+
Controller
+
Agency
+
Authority
+
Provenance.
}
$$

---

# 一百二十九、Post-Turing Protocol 不回答「它究竟本體上是什麼」

它回答的是：

> **我們目前能夠可靠驗證哪些關於它的事實？**

這是非常重要的認識論謙遜。

因此：

$$
\boxed{
Protocol
\neq
OntologyOracle.
}
$$

---

# 一百三十、結論：圖靈測試的繼承者不是更好的測謊機，而是身份協議

圖靈測試曾經提出一個非常有力量的問題：

> 如果機器的表現與人不可區分，我們應如何談論機器智能？

但 Synthetic Presence 與 Agentic AI 正把文明推入另一個階段。

問題逐漸變成：

> 如果機器真的已經可以像人，我們要怎麼知道現在是在跟誰互動？

第一反應可能是：

$$
HumanJudge
\rightarrow
AIJudge.
$$

但這仍然只是：

$$
\boxed{
Detection.
}
$$

生成器與 detector 可以持續競爭。

2026 年 speech-to-speech Turing Test 已實證顯示，通用 AI judge 並不天然可靠。

真正穩定的方向因而是：

$$
\boxed{
Inference
\rightarrow
Verification.
}
$$

而現實標準世界已經分別出現所需零件：

C2PA 正在處理：

$$
ContentProvenance,
$$

包括 live video。

W3C VC 正在處理：

$$
VerifiableClaims.
$$



NIST 正在處理：

$$
AgentIdentity
+
Authorization.
$$



IETF 社群則已經開始探索：

$$
AgentIdentity
+
Delegation
+
SignedActions.
$$



本文真正新增的，是把它們統一到：

$$
\boxed{
InteractionIdentity.
}
$$

因此未來一段通話、一個數位人、一個 AI Agent，不應只被標記：

> AI

而可能具有：

$$
\boxed{
Renderer=\text{SyntheticHuman}
}
$$

$$
\boxed{
Principal=\text{Organization X}
}
$$

$$
\boxed{
Controller=\text{Agent A7}
}
$$

$$
\boxed{
HumanSupervisor=\text{Present}
}
$$

$$
\boxed{
Authority=\text{CustomerSupport}
}
$$

$$
\boxed{
Lineage=\text{Verified}
}
$$

$$
\boxed{
SessionProvenance=\text{Valid}.
}
$$

人類不再需要透過肉眼、耳朵或直覺猜：

> 「這到底是不是 AI？」

而由機器完成：

$$
\boxed{
Attestation
\rightarrow
CredentialValidation
\rightarrow
DelegationResolution
\rightarrow
ProvenanceValidation
}
$$

最後把結果交給人。

但即使這套系統做到完美，

它仍然不能告訴我們：

$$
Consciousness?
$$

或：

$$
Soul?
$$

因為：

$$
\boxed{
Identity
\neq
Subjecthood
\neq
Soul.
}
$$

這條防火牆必須永遠保留。

因此本文提出：

# Post-Turing Transition

$$
\boxed{
\text{Turing Test}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Human/AI Detection}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Machine Forensics}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Cryptographic Provenance}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Interaction Identity Protocol}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Lineage-aware Post-Substrate Identity Infrastructure}.
}
$$

最終，圖靈測試問的是：

> **「你能不能讓我以為你是人？」**

後圖靈協議問的則是：

> **「無論你看起來像誰，你能不能讓我可靠知道你代表誰、由誰控制、從哪裡來、擁有什麼權限，以及這些聲明能不能被驗證？」**

這才可能是圖靈測試在 Synthetic Presence、Agentic AI 與後載體文明中的真正繼承者。

---

# 與既有研究的關係

Paper 01 已提出 Human／AI 二元分類具有歷史有限性；本文第一次將此命題轉化為協議設計要求：schema 不應硬編碼不可擴展的 Human／AI binary。

Paper 03 所建立：

$$
Origin
\neq
Identity
\neq
Agency
\neq
Subjecthood
$$

直接形成本文 Renderer、Controller、Principal、Agent、Authority 與 Verification 的多層拆分。

Paper 04 的 transformation history 與 Paper 05 的 lineage graph，使 Agent update、fork、merge 與 migration 可以被保存為 operational provenance，而不必假裝每次變換後只有一個簡單的「同一／不同」答案。

Paper 07 則提供本文最重要的限制：

$$
\boxed{
PTIIP
}
$$

無論工程上多成熟，都沒有資格自動成為：

$$
ConsciousnessDetector
$$

或：

$$
SoulDetector.
$$

而 2026 年的 C2PA、W3C VC、NIST Agent Identity 研究與 IETF Agent Identity 草案則顯示，本文所需要的幾個基礎 primitive 已經分別出現在現實標準生態中，只是尚未被統合為完整 Interaction Identity architecture。

---

# 後續論文

Paper 08 完成後，系列已經從：

$$
\boxed{
Ontology
}
$$

正式跨入：

$$
\boxed{
Civil Infrastructure.
}
$$

但身份驗證本身還不是最困難的制度問題。

當：

$$
Fork,
Merge,
HumanAgent,
AIAgent,
DigitalPerson,
BiologicalAI
$$

開始取得：

- 財產；
- 合約；
- 義務；
- 責任；
- 權利；
- 公民資格；

下一個問題就是：

> **誰繼承什麼？誰為誰負責？一個人 Fork 十萬次是否得到十萬票？Merge 能不能清除犯罪責任？Creator 是否擁有被創造主體？**

因此下一篇：

## Paper 09

# 後載體倫理與法律：身份分叉、代理責任、造物權與制度連續性

## Post-Substrate Ethics and Law: Identity Forks, Agent Responsibility, Creator Power, and Institutional Continuity

將正式把：

$$
LineageIdentity
$$

$$
+
$$

$$
AgentAuthority
$$

$$
+
$$

$$
MoralStatus
$$

映射到：

$$
Property,
Contract,
Liability,
Voting,
Citizenship,
Marriage,
Inheritance,
CreatorRights.
$$

而它的核心原則會是：

$$
\boxed{
\text{Ontological continuity does not automatically determine institutional duplication.}
}
$$

也就是：

> **就算兩個 Fork 都是真正的「我之後」，也不代表銀行帳戶、投票權、婚姻、公司股份與法律責任應該憑空複製兩份。**

這會是整個系列從「我是誰」正式進入「文明到底怎麼容納這些存在」的一篇。