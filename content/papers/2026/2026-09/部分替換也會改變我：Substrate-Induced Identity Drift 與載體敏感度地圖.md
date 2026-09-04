# 部分替換也會改變我：Substrate-Induced Identity Drift 與載體敏感度地圖

## Partial Replacement Can Still Change the Self: Substrate-Induced Identity Drift and the Substrate Sensitivity Map

**系列：** Substrate-Constitutive Identity／載體構成論  
**Paper：** 03  
**副題：** Why One Percent of Replacement Need Not Mean One Percent of Identity Change  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**理論協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-09-03  
**文件性質：** 公開理論論文／載體敏感度、神經增強、身份漂移與跨載體風險模型

---

## 摘要

跨載體身份討論經常隱含一個直覺模型：

> 如果只替換很少一部分，就只會造成很少改變；如果替換很多，才可能產生重大身份改變。

形式上，這相當於假設：

$$
\boxed{
D_{\mathrm{self}}
\propto
R_{\mathrm{replace}}
}
$$

其中 $R_{\mathrm{replace}}$ 表示載體替換比例，而 $D_{\mathrm{self}}$ 表示自我改變程度。

本文主張，這個比例模型沒有充分理由成立。

對複雜認知系統而言：

$$
\boxed{
\text{How much was replaced?}
}
$$

往往不如：

$$
\boxed{
\text{What was replaced?}
}
$$

重要。

一個佔身體極大比例但對認知動力學影響有限的組件被替換，可能造成很小的身份效應；

反之，一個物理尺度非常小、但深度參與：

- 情緒調節；
- reward processing；
- 記憶；
- self-model；
- agency；
- bodily ownership；

的節點被修改，卻可能造成遠大於其物理比例的自我變化。

本文因此正式發展 Paper 01 所提出的：

# Substrate-Induced Identity Drift

$$
\boxed{
SIID
}
$$

並將其表示為：

$$
\boxed{
\mathbf D_S
=
(
d_{\mathrm{per}},
d_{\mathrm{aff}},
d_{\mathrm{cog}},
d_{\mathrm{mem}},
d_{\mathrm{goal}},
d_{\mathrm{agency}},
d_{\mathrm{self}},
d_{\mathrm{rel}},
d_{\mathrm{dyn}},
d_{\phi?}}
)
}
$$

分別描述：

- perceptual drift；
- affective drift；
- cognitive drift；
- memory drift；
- goal/value drift；
- agency drift；
- self-model drift；
- relational drift；
- dynamical drift；
- phenomenal drift／未知。

本文進一步提出：

# Substrate Sensitivity Map

$$
\boxed{
\mathcal M_S
}
$$

不再把整個身體或計算機視為均勻載體，而對每一個組件或功能域：

$$
s_i
$$

建立：

$$
\boxed{
\boldsymbol{\chi}_i
=
\frac{\partial\mathbf X}{\partial s_i}
}
$$

作為理論性的「自我敏感度向量」。

這裡的 $\boldsymbol{\chi}_i$ 不應被理解為目前已能直接測量的物理導數，而是表達：

> 對某組件的干預，會在多大程度上影響哪些 self-relevant dimensions？

本文進一步指出，身份影響不能只由局部組件本身決定，還應取決於：

$$
\boxed{
SIID
=
F(
Location,
Function,
Coupling,
Centrality,
Plasticity,
Compensation,
Duration,
Reversibility,
History
).
}
$$

因此即使兩個 intervention 都替換：

$$
1\%
$$

物理組件，

也可能：

$$
D_{S}^{(A)}
\ll
D_{S}^{(B)}.
$$

人類現有研究已提供這種「非均勻載體」觀點的初步經驗支持。義肢 embodiment 文獻通常將 ownership、body representation 與 agency 分離，而這三個維度本身可以受到不同操弄與回饋機制影響；感覺回饋與控制策略則能提高義肢被納入身體圖式與 ownership 的程度。

另一方面，DBS 與 neuromodulation 文獻持續討論 cognition、affect、agency、self-perception、authenticity 與 personal identity 的可能變化，但較新的回顧同時警告，不應把少數極端案例誇大成「局部腦刺激必然改寫人格」；疾病進程、藥物、症狀改善與社會重新適應均是重要混雜因子。

器官移植亦提供一項有用但必須謹慎解讀的案例。移植者確實可能面臨 modified body、foreign organ integration、body image、焦慮、抑鬱與免疫抑制治療等心理適應問題，但這不能被直接解讀成「捐贈者人格透過器官轉移」。

本文因此提出一個比「換多少％」更一般的原理：

# Functional Sensitivity over Replacement Fraction Principle

$$
\boxed{
\text{Identity impact is governed more by functional-coupling sensitivity than by raw replacement fraction.}
}
$$

中文而言：

> **替換一％的存在，不代表只改變一％的自己；真正重要的是，那一％在整個「我」裡究竟做了什麼。**

---

# 一、忒修斯之船最大的問題可能不是「換了多少」

經典問題問：

> 船板逐步替換多少後，還是不是同一艘船？

因此自然形成：

$$
R_{\mathrm{replace}}
=
\frac{\text{replaced parts}}{\text{total parts}}.
$$

然後試圖找：

$$
\theta
$$

使：

$$
R_{\mathrm{replace}}>\theta
$$

之後：

$$
IdentityBreak=1.
$$

這種思考非常直觀。

但它暗含：

$$
\boxed{
\text{all parts contribute equally to identity}.
}
$$

對認知主體而言，這幾乎肯定過度簡化。

---

# 二、一根手指與一個關鍵神經調節節點不是等價的「一個零件」

假設：

$$
s_1=\text{one finger},
$$

以及：

$$
s_2=\text{a small but highly connected neural-regulatory subsystem}.
$$

兩者質量甚至可能：

$$
Mass(s_1)>Mass(s_2).
$$

然而：

$$
IdentitySensitivity(s_1)
$$

完全可能遠低於：

$$
IdentitySensitivity(s_2).
$$

所以：

$$
\boxed{
Mass
\neq
IdentityContribution.
}
$$

---

# 三、同樣，數量也不是關鍵

假設系統有：

$$
10^{11}
$$

個相關元件。

替換其中：

$$
10^8
$$

個低敏感元件，

與替換：

$$
10^5
$$

個控制極高層決策與調節的元件，

不能只以：

$$
10^8>10^5
$$

判斷身份影響。

所以：

$$
\boxed{
ComponentCount
\neq
IdentityImpact.
}
$$

---

# 四、建立 Replacement Fraction Fallacy

本文定義：

# Replacement Fraction Fallacy

若僅由：

$$
R_{\mathrm{replace}}
$$

直接推論：

$$
D_{\mathrm{self}},
$$

即：

$$
D_{\mathrm{self}}
=
f(R_{\mathrm{replace}})
$$

而忽略功能、耦合與系統位置，

則發生：

$$
\boxed{
RFF.
}
$$

---

# 五、最簡單的線性模型

錯誤的最強形式是：

$$
D_{\mathrm{self}}
=
kR_{\mathrm{replace}}.
$$

例如：

$$
10\%
$$

載體換掉，

所以：

$$
10\%
$$

「不再是自己」。

這種百分比在本體與認知上都缺乏明確意義。

---

# 六、甚至單調性都不能先驗保證

我們甚至不應預設：

$$
R_1<R_2
\Rightarrow
D_1<D_2.
$$

如果 $R_1$ 改的是高敏感節點，

而 $R_2$ 改的是大量冗餘結構，

完全可能：

$$
R_1<R_2
$$

但：

$$
D_1>D_2.
$$

---

# 七、因此載體必須從「材料總量」轉向「功能拓撲」

對主體系統：

$$
S
$$

建立組件集合：

$$
S=\{s_1,s_2,\ldots,s_n\}.
$$

每個：

$$
s_i
$$

具有：

- function；
- connectivity；
- control influence；
- redundancy；
- plasticity；
- feedback relation。

所以：

$$
\boxed{
S
}
$$

本身是一個結構化網路，

不是一袋均勻物質。

---

# 八、建立 Substrate Graph

令：

$$
\boxed{
G_S=(V_S,E_S).
}
$$

其中：

$$
V_S=\{s_1,\ldots,s_n\}
$$

為載體組件。

$$
E_S
$$

描述：

- physical coupling；
- information flow；
- regulatory influence；
- sensorimotor coupling；
- biochemical modulation。

---

# 九、身份影響來自圖上的位置

假設：

$$
Centrality(s_i)
$$

很高。

它可能：

- 接收大量輸入；
- 調節大量輸出；
- 參與多個 feedback loop。

此時即使：

$$
Size(s_i)\ll Size(S),
$$

仍可能：

$$
Impact(s_i)\gg0.
$$

---

# 十、因此需要 Substrate Sensitivity Map

本文正式定義：

$$
\boxed{
\mathcal M_S
=
\{
(s_i,\boldsymbol{\chi}_i)
\}_{i=1}^n
}
$$

其中：

$$
\boldsymbol{\chi}_i
$$

描述：

$$
s_i
$$

對不同 identity dimensions 的敏感度。

---

# 十一、Sensitivity 不是一個值

例如：

$$
\boldsymbol{\chi}_i
=
(
\chi_i^{per},
\chi_i^{aff},
\chi_i^{cog},
\chi_i^{mem},
\chi_i^{goal},
\chi_i^{agency},
\chi_i^{self}
).
$$

某個節點可能：

$$
\chi_i^{motor}\gg0
$$

但：

$$
\chi_i^{value}\approx0.
$$

另一個可能相反。

---

# 十二、這就是為什麼「身份核心區」也不能只畫一個圈

不存在足夠證據讓我們簡單說：

> 大腦某一區就是「自我區」。

更可能是：

$$
\boxed{
Self
=
distributed\ coupled\ processes.
}
$$

不同 self dimensions 依賴不同但重疊的網路。

---

# 十三、DBS 正好展示這種複雜性

DBS 只在非常局部範圍施加神經調控。

但相關 neuroethics 文獻仍持續討論：

- mood；
- motivation；
- cognition；
- agency；
- authenticity；
- identity。

這本身說明：

$$
\boxed{
SmallSpatialIntervention
}
$$

可以具有：

$$
\boxed{
LargeFunctionalReach
}
$$

的可能性。

---

# 十四、但 DBS 同樣告訴我們不能犯因果過度歸因

DBS 後一個人：

> 變開朗了。

不能立即：

$$
DBS\Rightarrow PersonalityRewrite.
$$

因為也可能：

$$
Symptoms\downarrow
\Rightarrow
SocialActivity\uparrow
\Rightarrow
BehaviorChange.
$$

或者：

$$
MedicationChange
\Rightarrow
MoodChange.
$$

因此 SIID 必須有：

$$
\boxed{
causal attribution layer.
}
$$

---

# 十五、SIID 必須是反事實量

Paper 01 已提出：

$$
\Delta_S
=
D
\left(
X_{\mathrm{actual}}^{S_1},
X_{\mathrm{counterfactual}}^{S_0}
\right).
$$

也就是：

> 真正因載體改變造成的額外漂移是多少？

這是 SIID 與一般人生改變最大的差別。

---

# 十六、因此 Before / After Comparison 不夠

錯誤：

$$
D(X_{\mathrm{before}},X_{\mathrm{after}})
=
SIID.
$$

因為即使沒有 intervention：

$$
X
$$

也會改變。

正確概念：

$$
\boxed{
SIID
=
ActualChange
-
CounterfactualNaturalChange
}
$$

在抽象意義上如此。

---

# 十七、需要 Control Trajectory

理想實驗：

$$
X_A(t_0)=X_B(t_0).
$$

其中：

$$
A:
S_0\rightarrow S_1,
$$

$$
B:
S_0\rightarrow S_0.
$$

比較：

$$
D(X_A(t),X_B(t)).
$$

人類幾乎做不到完美版本。

但 AI 系統可以逐漸逼近。

---

# 十八、因此 AI 將可能比人類更早建立真正 SSM

對 Agent：

$$
A
$$

複製兩份：

$$
A_1,A_2.
$$

保持：

- 初始 memory；
- model；
- goals；
- input stream；

盡可能一致。

只改：

$$
Substrate.
$$

那麼：

$$
\boxed{
Twin-Substrate Experiment
}
$$

就可以估計：

$$
\mathbf D_S(t).
$$

---

# 十九、建立完整 SIID Function

本文提出：

$$
\boxed{
\mathbf D_S
=
F(
\Delta S,
\mathcal M_S,
G_S,
T,
R,
P,
H,
E
)
}
$$

其中：

- $\Delta S$：具體載體變換；
- $\mathcal M_S$：敏感度圖；
- $G_S$：載體耦合拓撲；
- $T$：作用時間；
- $R$：可逆性；
- $P$：系統可塑性；
- $H$：既有歷史；
- $E$：環境條件。

---

# 二十、Location

首先：

$$
L(s_i)
$$

表示介入位於什麼 subsystem。

例如：

- motor；
- sensory；
- endocrine；
- memory；
- executive；
- reward；
- autonomic。

這比 replacement percentage 更重要。

---

# 二十一、Function

$$
F(s_i)
$$

描述該節點做什麼。

相同位置，

不同 stimulation／replacement mode 也可能影響不同 function。

所以：

$$
\boxed{
Anatomy
\neq
Function.
}
$$

對 AI 亦如此：

$$
hardware\ location
$$

不等於：

$$
computational\ role.
$$

---

# 二十二、Coupling

定義：

$$
\kappa_i
$$

表示節點與全系統耦合程度。

如果：

$$
\kappa_i\gg0,
$$

局部干預更可能傳播。

因此：

$$
\boxed{
IdentityImpact
\propto
\text{functional coupling}
}
$$

至少可作候選關係。

---

# 二十三、Centrality

圖論上可以考慮：

$$
c_i.
$$

包括：

- degree centrality；
- betweenness；
- control centrality；

等候選。

但認知系統並不能直接只用普通圖中央性表示。

本文只是指出：

$$
\boxed{
network position matters.
}
$$

---

# 二十四、Redundancy

若：

$$
r_i\gg0
$$

表示高度冗餘，

替換：

$$
s_i
$$

可能幾乎沒有輸出變化。

若：

$$
r_i\approx0,
$$

則系統脆弱。

所以：

$$
\boxed{
Sensitivity
}
$$

與：

$$
\boxed{
Redundancy
}
$$

通常具有重要關係。

---

# 二十五、Compensation

生物系統尤其具有：

$$
\boxed{
compensatory plasticity.
}
$$

某個組件受損後，

其他網路可以逐漸重新組織。

因此：

$$
ImmediateDrift
$$

與：

$$
LongTermDrift
$$

可能方向不同。

---

# 二十六、可能先變很多，再逐漸恢復

$$
D_S(t_1)\gg0,
$$

但：

$$
D_S(t_2)\downarrow.
$$

也可能相反：

一開始看起來沒有差，

經過長期學習後：

$$
D_S(t)\uparrow.
$$

所以：

$$
\boxed{
SIID
}
$$

必須是時間函數。

---

# 二十七、定義 Drift Trajectory

$$
\boxed{
\Gamma_D
=
\{
\mathbf D_S(t):
t\ge t_0
\}.
}
$$

不能只做：

> 手術後一週人格量表。

長期 trajectory 可能完全不同。

---

# 二十八、Reversibility

定義：

$$
R_S
$$

表示 intervention 可逆程度。

例如 DBS stimulation 可以在某些條件下調參或關閉；

而組織性 destruction 則未必可逆。

因此：

$$
\boxed{
same drift magnitude
}
$$

在不同 reversibility 下具有不同風險。

---

# 二十九、建立 Identity Risk

可以暫定：

$$
\boxed{
Risk_I
=
F(
Magnitude,
Uncertainty,
Irreversibility,
ValueSensitivity
).
}
$$

即使：

$$
D_S
$$

中等，

如果：

$$
Irreversibility\gg0
$$

且：

$$
GoalDriftRisk\gg0,
$$

仍然是高風險 intervention。

---

# 三十、Plasticity 也是雙刃劍

高可塑性：

$$
P_S\gg0
$$

可以幫助適應新載體。

但也表示：

$$
\boxed{
new substrate can reshape the system more deeply over time.
}
$$

所以：

$$
Plasticity
$$

既是 compatibility mechanism，

也是 identity drift pathway。

---

# 三十一、這對人工神經義肢特別重要

義肢 embodiment 並不是單純：

> 裝上機械手。

現有研究將 embodiment 拆成 ownership、body representation、agency；使用者可以對義肢具有控制感而未必具有完整 ownership，反之亦然。

這意味：

$$
\boxed{
EmbodimentIntegration
}
$$

本身就是多維過程。

---

# 三十二、感覺回饋可以改變這個整合

下肢與其他神經義肢研究顯示，恢復 somatosensory／proprioceptive feedback 有助於控制、ownership 與 embodiment，並降低對視覺監控的依賴。

因此：

$$
\boxed{
ArtificialComponent
}
$$

不是永遠停留在：

> 外部工具。

它可能逐漸：

$$
\boxed{
enter body schema.
}
$$

---

# 三十三、這正是 Partial Replacement Problem

假設：

$$
Arm_{bio}
\rightarrow
Arm_{prosthetic}.
$$

沒有理由說：

> 因為只是一條手臂，所以 identity effect = 10%。

真正可能變化：

$$
BodyRepresentation,
$$

$$
Agency,
$$

$$
SensorimotorStrategy.
$$

這些與質量比例沒有簡單關係。

---

# 三十四、但這也不代表義肢使用者變成另一個人

必須避免另一極端。

$$
ProsthesisUse
\not\Rightarrow
IdentityBreak.
$$

本文只主張：

$$
\boxed{
embodiment-related self dimensions can adapt to artificial components.
}
$$

---

# 三十五、聽覺植入也是有趣的例子

人工耳蝸的作用不只是提供一個外部工具。

它直接改變：

$$
\boxed{
sensory access to the world.
}
$$

而 deaf／hearing identity、社會歸屬與 self-perception 本身可以十分複雜；相關文獻也討論人工耳蝸及其可見性與身份、污名、生活品質之間的關係。

這提醒我們：

$$
\boxed{
sensory substrate change}
$$

可以透過：

$$
Perception
\rightarrow
SocialRelation
\rightarrow
SelfModel
$$

形成間接身份效應。

---

# 三十六、Identity Drift 可以是直接也可以是間接

## Direct SIID

$$
\Delta S
\rightarrow
\Delta Neural/CognitiveDynamics
\rightarrow
\Delta Self.
$$

## Mediated SIID

$$
\Delta S
\rightarrow
\Delta Ability
\rightarrow
\Delta EnvironmentInteraction
\rightarrow
\Delta SocialHistory
\rightarrow
\Delta Self.
$$

兩者都可能真實。

---

# 三十七、因此因果鏈長不代表不是載體效應

如果人工耳蝸：

$$
\rightarrow
new communication ability
$$

$$
\rightarrow
new social network
$$

$$
\rightarrow
new identity,
$$

這仍是 substrate intervention 的下游效應。

只是：

$$
\boxed{
mediated rather than immediate.
}
$$

---

# 三十八、建立 SIID Causal Depth

令：

$$
h
$$

為因果距離。

$$
h=1
$$

直接神經／動力改變。

$$
h=2
$$

功能改變後造成心理改變。

$$
h>2
$$

透過社會與歷史逐步形成。

因此：

$$
\boxed{
SIID
}
$$

可以具有多時間尺度。

---

# 三十九、內分泌系統更直接打擊「腦是唯一載體」直覺

情緒、認知與動機並不是只由固定神經連線決定。

例如甲狀腺與性激素異常與 depression、anxiety、cognitive impairment 等神經精神表現之間存在重要關係；治療效果本身則依族群與條件具有高度異質性。

因此：

$$
\boxed{
SelfRelevantDynamics
}
$$

至少受到：

$$
\boxed{
brain-body biochemical coupling
}
$$

影響。

---

# 四十、但荷爾蒙不等於人格開關

不能寫：

$$
Hormone_X
\Rightarrow
Personality_Y.
$$

這是嚴重過度簡化。

正確：

$$
HormonalState
\rightarrow
ModulationOfMood/Cognition/Motivation
$$

具有條件依賴性。

---

# 四十一、這使 Whole Brain Copy 再次遇到問題

假設只重建：

$$
NeuralConnectivity.
$$

但沒有重建：

- endocrine loop；
- autonomic feedback；
- visceral signals；
- bodily chemistry。

則：

$$
\boxed{
same connectome
}
$$

不必：

$$
\boxed{
same self-generating dynamics.
}
$$

---

# 四十二、因此載體邊界本身是研究問題

到底：

$$
Substrate(Self)
$$

包含到哪？

只有 brain？

還是：

$$
Brain+Body?
$$

還是：

$$
Brain+Body+Environment?
$$

這就是 extended／embodied cognition 與 SCIH 的重要交界。

---

# 四十三、本文暫時採多層載體

定義：

$$
\boxed{
S^\ast
=
(
S_N,
S_B,
S_E,
S_R
)
}
$$

其中：

- $S_N$：neural／computational substrate；
- $S_B$：bodily-regulatory substrate；
- $S_E$：embodiment interface；
- $S_R$：relational/environmental coupling support。

---

# 四十四、這不等於環境就是「身體」

而是：

> 自我的實際動力可能依賴超出單一腦組織的持續耦合。

不同理論可以對：

$$
S^\ast
$$

邊界給不同權重。

---

# 四十五、器官移植是非常容易被誤用的例子

移植後確實可能出現：

- 身體意象改變；
- 對「外來器官」的整合困難；
- anxiety；
- depression；
- altered body acceptance。

近期系統性回顧仍描述了這些心理適應挑戰。

---

# 四十六、但「捐贈者人格轉移」不能作為 SCIH 證據核心

目前無足夠可靠證據支持：

$$
\boxed{
DonorPersonality
\rightarrow
Recipient
}
$$

這種強命題。

因此我們不需要它。

---

# 四十七、真正值得保留的是較弱而穩健的事實

$$
\boxed{
Major bodily intervention
}
$$

可以透過：

- bodily integration；
- medication；
- illness recovery；
- social meaning；
- physiological change；

影響心理與自我經驗。

這已足以支持：

$$
BodyChange
\not\perp
SelfChange.
$$

---

# 四十八、這個校正對 SCIH 很重要

如果理論需要：

> 心臟保存捐贈者記憶

才成立，

理論太脆弱。

SCIH 真正強的地方是：

> 即使完全不接受 cellular memory，載體—自我耦合仍然成立。

---

# 四十九、BCI 又增加 Agency 層

BCI 使使用者可以透過腦訊號控制外部裝置。

這立即產生：

> 這個動作是誰做的？

> 使用者、decoder、AI correction system 還是共同完成？

現有 BCI 倫理研究也已把 agency、control 與 mediated action 視為核心問題。

---

# 五十、因此部分替換不只改 Self，也可能改 Agency Topology

原本：

$$
Human\rightarrow Action.
$$

BCI：

$$
HumanBrain
\rightarrow
Decoder
\rightarrow
AIController
\rightarrow
Action.
$$

此時：

$$
\boxed{
Agency
}
$$

變成分散式。

---

# 五十一、如果 AI correction 越來越強

假設：

$$
HumanIntent=0.6,
$$

$$
AIPrediction=0.4.
$$

最後 action：

$$
a.
$$

誰的：

$$
Agency(a)?
$$

不能只看使用者身體。

這正是：

$$
\boxed{
partial substrate augmentation can modify agency structure.
}
$$

---

# 五十二、而 Agency 正是 Self 的一個重要維度

如果一個人開始無法清楚區分：

> 是我想做，

還是裝置替我預測？

其：

$$
d_{\mathrm{agency}}
$$

可能提高。

所以 identity drift 不必來自記憶被改。

---

# 五十三、這就是為什麼 SIID 必須是向量

如果只測 Big Five personality，

可能完全看不到：

$$
AgencyDrift.
$$

如果只測記憶，

又看不到：

$$
BodyOwnershipDrift.
$$

所以：

$$
\boxed{
single psychological test
}
$$

不足以衡量 identity transformation。

---

# 五十四、本文提出十維 SIID

最終：

$$
\boxed{
\mathbf D_S
=
(
d_{\mathrm{per}},
d_{\mathrm{aff}},
d_{\mathrm{cog}},
d_{\mathrm{mem}},
d_{\mathrm{goal}},
d_{\mathrm{agency}},
d_{\mathrm{self}},
d_{\mathrm{rel}},
d_{\mathrm{dyn}},
d_{\phi?}}
).
}
$$

---

# 五十五、Perceptual Drift

$$
d_{\mathrm{per}}
$$

描述：

> 世界對主體「看起來／聽起來／感覺起來」變了多少？

例如：

- 新感官；
- infrared vision；
- auditory restoration；
- machine proprioception。

---

# 五十六、Affective Drift

$$
d_{\mathrm{aff}}
$$

描述：

- mood baseline；
- reward sensitivity；
- fear；
- motivation；
- emotional range。

---

# 五十七、Cognitive Drift

$$
d_{\mathrm{cog}}
$$

描述：

- reasoning speed；
- attention；
- planning；
- working memory；
- decision style。

---

# 五十八、Memory Drift

$$
d_{\mathrm{mem}}
$$

包括：

- lost memories；
- altered recall；
- memory accessibility；
- externalized memory dependence。

---

# 五十九、Goal / Value Drift

$$
d_{\mathrm{goal}}
$$

是最需要倫理保護的維度之一。

因為：

> 我記得自己以前重視自由，

但現在完全不重視，

可能比忘記某一段午餐回憶更接近核心身份改變。

---

# 六十、Agency Drift

$$
d_{\mathrm{agency}}
$$

回答：

> 決策到底仍有多少由原主體形成與控制？

對 BCI、AI augmentation 尤其重要。

---

# 六十一、Self-Model Drift

$$
d_{\mathrm{self}}
$$

描述：

> 「我是誰」的內部模型如何變化。

例如：

$$
SingleBodySelf
\rightarrow
DistributedSelf.
$$

---

# 六十二、Relational Drift

$$
d_{\mathrm{rel}}
$$

描述主體與：

- 家人；
- 朋友；
- 社群；
- 組織；

關係的變化。

身份從來不只在腦內。

---

# 六十三、Dynamical Drift

$$
d_{\mathrm{dyn}}
$$

比較：

$$
F_{before}
$$

與：

$$
F_{after}.
$$

即：

> 系統產生未來反應的方式改變多少？

這是載體構成論最重要的新增維度之一。

---

# 六十四、Phenomenal Drift

$$
d_{\phi?}
$$

問：

> 第一人稱感質究竟改變多少？

例如新感官是否產生完全新的 qualitative experience。

但目前：

$$
d_\phi
$$

很多情境仍無可靠第三人稱測量。

因此保留：

$$
?.
$$

---

# 六十五、並不是所有 Drift 都是傷害

這一點非常重要。

例如：

$$
d_{\mathrm{per}}\gg0
$$

因為失明者恢復視覺。

這可能是巨大改變，

但具有正向價值。

所以：

$$
\boxed{
DriftMagnitude
\neq
HarmMagnitude.
}
$$

---

# 六十六、甚至巨大人格變化也可能被本人偏好

DBS 文獻中即存在患者認為治療後「更像真正的自己」，而家人卻對其變化感到不安的案例與討論。

這說明：

$$
\boxed{
IdentityChange
}
$$

與：

$$
\boxed{
IdentityLoss
}
$$

不能直接等同。

---

# 六十七、因此需要 Valence of Drift

為每個：

$$
d_i
$$

增加：

$$
v_i
\in
[-1,1]
$$

表示主體／制度評估的：

- unwanted；
- neutral；
- desired。

形成：

$$
\boxed{
\mathbf D_S^+
=
\{(d_i,v_i)\}.
}
$$

---

# 六十八、這使「變得更多」不一定更差

某些 modification 的目的就是：

$$
D>0.
$$

例如：

> 治療 depression。

如果：

$$
d_{\mathrm{aff}}\approx0,
$$

反而可能表示 intervention 沒效果。

所以身份技術不是：

$$
MinimizeAllChange.
$$

---

# 六十九、真正目標是 Control the Transformation

即：

$$
\boxed{
DesiredDrift
\approx
ActualDrift.
}
$$

以及：

$$
UndesiredDrift
\rightarrow0.
$$

這才是未來 identity-aware engineering 的合理目標。

---

# 七十、建立 Identity Transformation Error

令：

$$
\mathbf D_{\mathrm{target}}
$$

為主體同意的目標變換。

實際：

$$
\mathbf D_{\mathrm{actual}}.
$$

則：

$$
\boxed{
E_I
=
d(
\mathbf D_{\mathrm{actual}},
\mathbf D_{\mathrm{target}}
).
}
$$

---

# 七十一、這比單純「成功／失敗」更精確

治療後：

$$
Survival=1,
$$

$$
TargetFunctionRestored=1,
$$

但：

$$
E_I\gg0.
$$

那 intervention 在身份層仍可能存在重大問題。

---

# 七十二、因此未來手術同意可能需要 Identity Consent

理論上：

$$
Consent
=
(
MedicalRisk,
FunctionalOutcome,
IdentityTransformationRange
).
$$

尤其對：

- DBS；
- advanced BCI；
- neural replacement；
- memory prosthesis；
- full-body rebody；

越來越重要。

---

# 七十三、但今天不能假裝已能準確預測

目前：

$$
Predict(\mathbf D_S)
$$

能力仍非常有限。

所以短期最重要的是：

$$
\boxed{
uncertainty disclosure.
}
$$

而不是虛假精確：

> 你的 self-model 會改變 8.7%。

---

# 七十四、建立 Uncertainty Vector

$$
\boxed{
\mathbf U_S
=
(
u_{\mathrm{per}},
u_{\mathrm{aff}},
\ldots
).
}
$$

因此真正 profile：

$$
\boxed{
ITP
=
(
\mathbf C_I,
\mathbf D_S,
\mathbf U_S,
R_S
).
}
$$

---

# 七十五、這讓可逆 intervention 特別有價值

如果：

$$
U_S\gg0,
$$

則：

$$
Reversible
$$

比：

$$
Irreversible
$$

具有更高 epistemic safety。

因為可以：

$$
Intervene
\rightarrow
Measure
\rightarrow
Adjust
\rightarrow
Rollback.
$$

---

# 七十六、因此 Gradual Replacement 需要 Drift Gates

Paper 04 原本：

$$
X_0\rightarrow X_1\rightarrow\cdots X_n.
$$

現在每一步加入：

$$
Gate_k:
\mathbf D_S^{(k)}
\le
\mathbf\epsilon.
$$

若超過：

$$
\epsilon
$$

則：

$$
Pause.
$$

---

# 七十七、這就是 Identity-Aware Gradualism

不只是：

> 一次換少一點。

而是：

> 每一步觀察自我多維變化，並決定是否繼續。

兩者完全不同。

---

# 七十八、因為一小步也可能跨高敏感區

如果：

$$
R_{\mathrm{replace}}=0.005,
$$

但：

$$
\boldsymbol{\chi}_i\gg0,
$$

仍可能：

$$
D_S>\epsilon.
$$

所以 gradual replacement 不能只按百分比。

---

# 七十九、真正應該按 Sensitivity Budget 前進

定義：

$$
\boxed{
B_I
}
$$

為每一步可接受 identity-change budget。

選擇 intervention：

$$
T_k
$$

滿足：

$$
ExpectedSIID(T_k)<B_I.
$$

---

# 八十、這使增強工程變成控制問題

不是：

$$
ReplaceUntilDone.
$$

而是：

$$
\boxed{
Control
(
Transformation,
Feedback,
Drift
).
}
$$

這和普通 closed-loop engineering 更相似。

---

# 八十一、AI 載體遷移尤其適合做這套

對 persistent AI：

$$
A
$$

可以在 migration 前跑：

$$
\boxed{
shadow twin.
}
$$

原 substrate：

$$
A_0.
$$

新 substrate：

$$
A_1.
$$

並行一段時間，

給相似測試，

估計：

$$
\mathbf D_S.
$$

---

# 八十二、如果 drift 過大就不切換 primary identity

這可以形成：

$$
\boxed{
Identity Migration Gate.
}
$$

條件：

$$
D_{\mathrm{dyn}}<\epsilon_d,
$$

$$
D_{\mathrm{goal}}<\epsilon_g,
$$

等等。

這是非常工程化的 SCIH 推論。

---

# 八十三、它也比 hash 相同更有意義

即使：

$$
ModelHash(A_0)=ModelHash(A_1),
$$

仍不能保證：

$$
Trajectory(A_0)=Trajectory(A_1).
$$

所以：

$$
\boxed{
BinaryEquivalence
\neq
CognitiveEquivalence.
}
$$

---

# 八十四、硬體差異可能被 abstraction 消除，也可能被放大

若 software stack 強制：

$$
deterministic\ semantics,
$$

則：

$$
SIID\approx0
$$

可能成立。

如果：

- precision 改變；
- timing 改變；
- stochasticity 改變；
- online learning；

則：

$$
SIID
$$

可能增加。

所以 SCIH 不是：

> 不同 CPU 一定生出不同人格。

---

# 八十五、這是一個可檢驗命題

我們可以對：

$$
S_1,S_2
$$

跑：

$$
N
$$

組 matched agents。

比較：

$$
Distribution(
\mathbf D_S
).
$$

如果 substrate effect 不高於 noise baseline：

$$
SCIH
$$

在該層級失去支持。

---

# 八十六、這也是為什麼載體敏感度不能是宇宙固定表

$$
\mathcal M_S
$$

會隨：

- architecture；
- developmental history；
- adaptation；

改變。

同一介入：

$$
T
$$

對：

$$
X
$$

與：

$$
Y
$$

可能：

$$
D_S^X\neq D_S^Y.
$$

---

# 八十七、個體差異本身就是 sensitivity 的一部分

所以：

$$
\boxed{
SubstrateSensitivity
=
SystemSpecific.
}
$$

不能：

> DBS 某位置讓 A 變外向，

所以所有人同位置都會變外向。

這也正是現有 DBS 文獻警告過度泛化的原因。

---

# 八十八、歷史會改變載體敏感度

經長期使用義肢，

body representation 可以逐步適應。

因此：

$$
\chi_i(t)
$$

本身可能改變。

所以：

$$
\boxed{
SensitivityMap
=
\mathcal M_S(t).
}
$$

它也是動態的。

---

# 八十九、這形成二階回饋

$$
SubstrateChange
\rightarrow
IdentityChange
\rightarrow
SensitivityChange.
$$

然後：

$$
SensitivityChange
\rightarrow
FutureSubstrateResponse.
$$

因此：

$$
\boxed{
SIID
}
$$

可能具有遞歸性。

---

# 九十、這是載體構成論真正進入動態系統的地方

不再：

$$
S\rightarrow X.
$$

而是：

$$
\boxed{
S_t
\leftrightarrow
X_t
}
$$

並：

$$
S_{t+1}
=
G(S_t,X_t),
$$

$$
X_{t+1}
=
F(X_t,S_t).
$$

---

# 九十一、對人類尤其如此

人使用工具：

$$
Tool
\rightarrow
Skill.
$$

Skill 改變：

$$
brain/body.
$$

新的 brain/body 再使工具使用方式改變。

因此：

$$
\boxed{
human-technology coupling is developmental.
}
$$

不是單向裝插件。

---

# 九十二、後人類因而可能不是「加很多零件」

而是：

$$
\boxed{
long-term co-adaptation between person and artificial substrate.
}
$$

這比：

> 人體 60% 機械化

更接近真正變化。

---

# 九十三、所以後人類比例指標可能毫無意義

$$
MechanicalPercentage(H)=70\%.
$$

沒有回答：

- cognition 有沒有變；
- agency 有沒有變；
- body ownership 有沒有變；
- values 有沒有變。

因此：

$$
\boxed{
PercentArtificial
}
$$

不是 Posthuman degree 的好指標。

---

# 九十四、更合理的是 Functional Transformation Profile

$$
\boxed{
FTP_H
=
(
Embodiment,
Cognition,
Agency,
Memory,
Affect,
SelfModel
).
}
$$

這會在 Paper 06 正式用到。

---

# 九十五、New Human 也不該用 DNA 修改百分比決定

修改：

$$
0.01\%
$$

基因，

如果碰到重要 developmental regulator，

影響可能很大。

修改：

$$
1\%
$$

大量低功能區，

影響反而可能較小。

所以同樣：

$$
\boxed{
GenomicFraction
\neq
BeingChange.
}
$$

---

# 九十六、SCIH 因此具有非常一般的結構

不論：

- neural hardware；
- hormones；
- genes；
- prostheses；
- sensors；
- AI chips；

真正問題都是：

$$
\boxed{
functional sensitivity,
not raw replacement fraction.
}
$$

---

# 九十七、建立 Functional Sensitivity Principle

本文正式提出：

# Functional Sensitivity over Replacement Fraction Principle

對 intervention：

$$
T:S\rightarrow S',
$$

其 identity effect 應主要由：

$$
\boxed{
\Psi(T)
=
F(
\chi,
\kappa,
c,
r,
p,
t
)
}
$$

描述，

而非只由：

$$
R_{\mathrm{replace}}.
$$

其中：

- $\chi$：self-dimension sensitivity；
- $\kappa$：coupling；
- $c$：control/network centrality；
- $r$：redundancy；
- $p$：plasticity；
- $t$：temporal integration。

---

# 九十八、Replacement Fraction 仍有用，但只是變量之一

我們不是完全丟掉：

$$
R_{\mathrm{replace}}.
$$

如果：

$$
R\rightarrow1,
$$

通常變換機會確實增加。

但：

$$
\boxed{
R
}
$$

只是：

$$
\Psi
$$

的輸入之一，

不是 identity oracle。

---

# 九十九、建立 Critical Substrate Node

若某：

$$
s_i
$$

滿足：

$$
\|\boldsymbol{\chi}_i\|>\theta_\chi
$$

且：

$$
\kappa_i>\theta_\kappa,
$$

可以暫稱：

$$
\boxed{
CriticalSubstrateNode.
}
$$

但這只是功能性術語。

不是：

> 靈魂節點。

---

# 一百、Critical 不等於不可替換

如果能建立功能等價：

$$
s_i'
$$

並保持：

$$
F_{s_i'}\approx F_{s_i},
$$

仍可能低漂移替換。

所以：

$$
\boxed{
high sensitivity}
$$

表示需要更高保真，

不是禁止 replacement。

---

# 一百零一、這正是人工神經元替換真正需要的判準

不是：

> 第幾個 neuron。

而是：

> replacement 是否保持：

$$
Timing,
Plasticity,
Neuromodulation,
Connectivity,
Feedback.
$$

如果只保持輸入輸出 snapshot，

可能不足。

---

# 一百零二、因此 Functional Equivalence 也要多層

$$
Eq_{IO},
$$

$$
Eq_{temporal},
$$

$$
Eq_{plastic},
$$

$$
Eq_{biochemical},
$$

$$
Eq_{developmental}.
$$

不應只：

$$
SameOutput.
$$

---

# 一百零三、這是 Gradual Replacement Paradox 的新答案

傳統：

> 每一個 neuron 換成完全等價人工 neuron，最後是不是還是你？

SCIH 回答：

> **先告訴我「完全等價」究竟包括哪些動力與耦合層。**

如果真的：

$$
Eq_{\mathrm{full}}\rightarrow1,
$$

那 SIID 可能極低。

如果只：

$$
Eq_{IO}=1,
$$

則仍未必。

---

# 一百零四、所以問題不在人工／天然

$$
ArtificialNeuron
$$

不因人工就必然破壞 identity。

Natural neuron 也不是神聖 token。

真正問題：

$$
\boxed{
does the replacement preserve the self-relevant dynamics?
}
$$

---

# 一百零五、這再次避免 Material Essentialism

SCIH 不是：

> 生物好，人工壞。

它甚至允許：

$$
ArtificialReplacement
$$

比受損生物組件更好地保持 identity。

只要：

$$
D_S\downarrow.
$$

---

# 一百零六、例如治療可能反而恢復身份

疾病：

$$
X_0
\rightarrow
X_{\mathrm{ill}}.
$$

Intervention：

$$
X_{\mathrm{ill}}
\rightarrow
X_{\mathrm{treated}}.
$$

如果：

$$
X_{\mathrm{treated}}
$$

更接近患者認同的先前自我，

則：

$$
\boxed{
substrate intervention can reduce identity drift.
}
$$

DBS 文獻中「更像以前的自己」的敘事正提供這種可能。

---

# 一百零七、因此 SIID 有正負方向問題

以自然／期望 trajectory 為參照，

intervention 可能：

$$
D_S>0
$$

但改善：

$$
DistanceToPreferredSelf.
$$

所以：

$$
\boxed{
Drift
}
$$

不等於：

$$
\boxed{
Degradation.
}
$$

---

# 一百零八、建立 Preferred Self Distance

令：

$$
X^\ast
$$

為主體認可的理想／復原目標。

則：

$$
\boxed{
D^\ast(t)
=
D(X_t,X^\ast).
}
$$

治療可能：

$$
D^\ast\downarrow
$$

即使：

$$
D(X_{\mathrm{pre}},X_{\mathrm{post}})\uparrow.
$$

這是重要倫理區分。

---

# 一百零九、但 Preferred Self 也會變

治療後本人可能：

> 我現在比較喜歡現在的我。

而術前本人可能不會同意。

這就是：

$$
\boxed{
Diachronic Preference Conflict.
}
$$

---

# 一百一十、前我與後我可能不同意

$$
Preference_{pre}(T)=Reject,
$$

$$
Preference_{post}(T)=Accept.
$$

誰具有優先權？

這不是 SCIH 能單獨解決的。

但它證明：

$$
\boxed{
identity-changing intervention}
$$

會產生新的 consent philosophy。

---

# 一百一十一、這將是未來 neuroethics 的真正難題

DBS 文獻已經出現類似：

> 治療後的偏好是否真正自主？

> 是治療恢復了原本的我，還是創造了新的偏好？

等討論。

未來深度 augmentation 只會把它放大。

---

# 一百一十二、所以 Identity Consent 必須是時間性的

不是：

$$
Consent(t_0)
$$

一次永久有效。

可能需要：

$$
\boxed{
Consent(t_0),
Review(t_1),
Review(t_2),\ldots
}
$$

尤其 intervention 可調節時。

---

# 一百一十三、這與 Drift Monitoring 完全配合

$$
Intervene
\rightarrow
Monitor
\rightarrow
Re-consent
\rightarrow
Continue.
$$

對真正高風險可逆 identity technology，

這可能比一次性 consent 更合理。

---

# 一百一十四、本文提出 Substrate Intervention Classes

依 identity sensitivity 可暫分：

### S0 — Peripheral

對 cognition/self 低耦合。

### S1 — Embodiment-Relevant

顯著影響 body representation／agency。

### S2 — Cognitive-Modulatory

影響 cognition、affect、motivation。

### S3 — Identity-Critical

可能影響 memory、values、self-model、core agency。

### S4 — Whole-Regime Transformation

改變整個 cognitive realization dynamics。

---

# 一百一十五、這不是固定醫療分類

而是一種：

$$
\boxed{
identity-risk classification.
}
$$

同一裝置對不同患者可能跨不同 class。

---

# 一百一十六、Rebody 可能從 S1 到 S4

只換 avatar：

$$
S1.
$$

換感官：

$$
S1/S2.
$$

換完整 body feedback：

$$
S2/S3.
$$

換 whole cognitive substrate：

$$
S4.
$$

所以「Rebody」本身過度寬泛。

---

# 一百一十七、AI migration 也一樣

換普通伺服器：

$$
S0.
$$

換 numeric precision：

$$
S1/S2?
$$

換 memory architecture：

$$
S2/S3.
$$

換成 biological adaptive cognition：

$$
S4.
$$

應按實際 dynamics 分類。

---

# 一百一十八、這才真正回答「矽基 AI ≠ 光子 AI ≠ 生物 AI」

如果只是：

$$
SameSemantics
$$

在三種 hardware 上執行，

它們未必形成不同 cognitive kind。

但如果：

$$
\boxed{
SubstrateChange
\rightarrow
DifferentReachableDynamics
}
$$

達到 S4，

則 Strong SCIH 才真正有力。

---

# 一百一十九、所以「材料名稱」不是分類終點

真正應比較：

$$
\mathcal X_{S_1},
\mathcal X_{S_2}.
$$

也就是不同 substrate 下的：

$$
\boxed{
reachable self-state spaces.
}
$$

這會在 Paper 05 正式深化。

---

# 一百二十、結論：換多少不是核心，換到哪裡才是

本文從一個非常簡單的反問開始：

> 如果只換 1%，真的就只改變 1% 的我嗎？

答案是：

$$
\boxed{
沒有理由如此假設。
}
$$

複雜主體不是一堆對身份貢獻完全等重的零件。

更合理的模型是：

$$
\boxed{
\mathbf D_S
=
F(
Location,
Function,
Coupling,
Centrality,
Redundancy,
Plasticity,
Duration,
Reversibility,
History
).
}
$$

這意味：

$$
\boxed{
ReplacementFraction
}
$$

不能直接等同：

$$
\boxed{
IdentityChangeFraction.
}
$$

人類現有神經調控研究已顯示，非常局部的神經介入就足以使 cognition、affect、agency、self-perception 與 authenticity 成為真實倫理議題；但現有研究亦清楚提醒，個體差異、疾病、藥物與社會重新適應使這些變化遠比「刺激一個位置就改人格」複雜。

義肢與 neuroprosthetics 則從另一方向顯示：

$$
\boxed{
ArtificialPart
}
$$

可以逐漸進入：

$$
\boxed{
BodySchema,
Ownership,
Agency.
}
$$

而且 ownership、body representation、agency 本來就是可分離而又互相作用的 embodiment dimensions。

器官移植則提醒我們：

> 大幅改變身體確實可能伴隨 self-image 與心理適應改變，

但這不能被誇張成：

> 捐贈者人格經器官傳輸。



因此 SCIH 不需要神祕的：

$$
CellularMemory.
$$

它只需要承認一個更基本的事實：

$$
\boxed{
\text{the self is generated by a non-uniform coupled system}.
}
$$

既然系統不是均勻的，

介入效應也不會均勻。

因此本文正式建立：

# Substrate Sensitivity Map

$$
\boxed{
\mathcal M_S
=
\{(s_i,\boldsymbol{\chi}_i)\}.
}
$$

每一個組件：

$$
s_i
$$

都應根據它對：

- perception；
- affect；
- cognition；
- memory；
- values；
- agency；
- self-model；
- dynamics；

的影響評估，

而不是根據重量或百分比。

這也使 Gradual Replacement 得到更成熟的版本。

真正安全的 gradual replacement 不是：

> 每次只換 1%。

而是：

$$
\boxed{
\text{每次只跨越可接受的 Identity Drift Budget。}
}
$$

即：

$$
ExpectedSIID(T_k)<B_I.
$$

所以某一步可以換：

$$
10\%
$$

而幾乎沒有問題。

另一小步只換：

$$
0.1\%,
$$

卻可能因進入高敏感 control loop 而必須停止。

這就是載體構成論第三篇的核心原則：

$$
\boxed{
\text{Functional sensitivity matters more than raw replacement fraction.}
}
$$

中文而言：

> **你換掉多少，不一定最重要；真正重要的是，你究竟換掉了「你」的哪一部分動力。**

因此：

$$
\boxed{
1\%\ substrate\ change
\not\Rightarrow
1\%\ self\ change.
}
$$

甚至：

$$
\boxed{
1\%\ substrate\ change
>
50\%\ substrate\ change
}
$$

在 identity impact 上也可能成立，

只要那一小部分位於足夠高敏感、低冗餘、高耦合的認知節點。

這使「後人類到底機械化幾％」成為一個低資訊量問題。

真正更重要的是：

$$
\boxed{
\mathcal M_S,
\mathbf D_S,
\Gamma_D.
}
$$

即：

> **什麼部分被改了？**

> **哪些自我維度因此發生漂移？**

> **這個漂移會不會隨時間放大、恢復或重新塑造未來的自己？**

這才是部分替換真正的身份問題。

---

# 與 Paper 01–02 的關係

Paper 01 建立：

$$
\boxed{
Substrate
\not\perp
Identity.
}
$$

Paper 02 建立：

$$
\boxed{
IdentityContinuity
\neq
IdentityInvariance.
}
$$

本文現在加入第三層：

$$
\boxed{
IdentityInvarianceChange
\neq
ReplacementFraction.
}
$$

並正式建立：

$$
\boxed{
SIID
+
SubstrateSensitivityMap.
}
$$

因此前三篇可以濃縮成：

$$
\boxed{
\text{The substrate matters,}
}
$$

$$
\boxed{
\text{change does not imply discontinuity,}
}
$$

以及：

$$
\boxed{
\text{the effect of change depends on where and how the substrate participates in the self.}
}
$$

---

# 後續論文

## Paper 04

# 身體就是認知的一部分：Interoception、Embodiment 與 Self

下一篇將把本文的：

$$
\mathcal M_S
$$

真正放進人類身體。

集中處理：

$$
\boxed{
Brain
\leftrightarrow
Body
\leftrightarrow
World
}
$$

的閉環，

包括：

- interoception；
- proprioception；
- body ownership；
- agency；
- endocrine modulation；
- autonomic regulation；
- prosthetic embodiment；
- BCI。

核心問題將是：

> **如果「我」的生成依賴心跳、呼吸、內分泌、身體位置、感官回饋與行動閉環，那麼所謂「把大腦完整複製出去」究竟複製了多少真正的 Self-System？**

並正式比較：

$$
\boxed{
WholeBrainEmulation
}
$$

與：

$$
\boxed{
WholeSelfRelevantSystemEmulation.
}
$$