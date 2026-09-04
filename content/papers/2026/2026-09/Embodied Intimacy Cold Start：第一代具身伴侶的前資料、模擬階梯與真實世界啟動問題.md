# Embodied Intimacy Cold Start：第一代具身伴侶的前資料、模擬階梯與真實世界啟動問題

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 06 / 09  
**版本：** v0.1  
**研究性質：** 理論／資料架構／具身 AI 論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

前五篇已建立親密光譜、Capability–Permission–Activation、Domain-Relative Frontier、Interaction Experience 與 Relationship World Model。本文進一步處理一個對未來具身伴侶無法迴避的工程問題：

> 第一代具身伴侶在尚未具有足夠真實長期親密互動資料之前，究竟依賴什麼「前資料」進入真實世界？

本文將此稱為 **Embodied Intimacy Cold Start（EICS）**。其核心不是「如何讓機器人生成成人內容」，而是如何在真實人體接觸、長期共同生活、私密空間與高敏感互動之前，使具身 AI 取得足夠的物理、社會、關係、觸覺、邊界與後果模型。

本文首先區分三種常被混淆的資料：

$$
D_{\text{erotic}}
\neq
D_{\text{social-touch}}
\neq
D_{\text{embodied-relationship}}.
$$

情色／色情內容可以提供敘事、語言與部分人體／情境先驗；社會觸覺資料提供接觸位置、力度、時序與回饋；而具身關係資料則要求：

$$
\text{state}
\rightarrow
\text{action}
\rightarrow
\text{physical/social feedback}
\rightarrow
\text{relationship update}.
$$

本文提出六層 **Embodied Relationship Data Ladder**：

$$
D_0
\rightarrow
D_1
\rightarrow
D_2
\rightarrow
D_3
\rightarrow
D_4
\rightarrow
D_5,
$$

分別為 Physical Prior、Social-Embodied Prior、Relationship Trajectory、Intimacy Interaction、Simulation/XR Counterfactuals 與 Real-World Personal Experience。

2026 年的 HRI 與 robotics 研究已提供部分可行基礎：VR/haptic 已能在實體機器人製作前蒐集 whole-body social-touch interaction data；affective robotic touch 已被提出為 closed-loop、multi-model、sim-to-real 問題；XR 被視為更安全且可擴張的 HRI 中介層；Isaac Lab 等工具則已將大規模 simulation、imitation learning、reinforcement learning 與 sim-to-real pipeline 變成可用基礎設施。

本文因此主張，第一代具身親密／伴侶 AI 的合理啟動路徑不是：

$$
\text{Adult Data}
\rightarrow
\text{Real Human Deployment},
$$

而是：

$$
\boxed{
\text{General Embodiment}
\rightarrow
\text{Social Touch}
\rightarrow
\text{Relationship Simulation}
\rightarrow
\text{Controlled Human Interaction}
\rightarrow
\text{Personal Local Learning}.
}
$$

本文亦提出 Consent–Boundary Calibration、Progressive Embodiment Curriculum、Physical Intimacy Activation Threshold、Relational Sim-to-Real Gap、Local Experience Envelope 與 Mutual Agency Pretraining 等概念。最後強調：如果未來 AI 伴侶被視為具有一定自主性而非純工具，訓練資料不應只包含「人要求、AI 服從」，而應包含接受、拒絕、猶豫、改變意願與重新協商等雙向狀態。

**關鍵詞：** Embodied Intimacy Cold Start、Embodied AI、Companion Robot、Human–Robot Intimacy、Social Touch、Sim-to-Real、XR HRI、Relationship World Model、Consent Calibration、Mutual Agency

---

## 1. Cold Start：第一代具身伴侶不可能靠「使用後再慢慢學」解決全部問題

純文字伴侶 AI 的初始錯誤通常造成：

$$
\text{Wrong Output}.
$$

具身伴侶則可能造成：

$$
\text{Wrong Inference}
\rightarrow
\text{Wrong Physical Action}
\rightarrow
\text{Real-World Consequence}.
$$

因此，第一代系統不能以：

> 上線後從使用者回饋慢慢學就好。

作為完整答案。

因為在部署前，系統至少已經必須知道：

- 如何安全移動；
- 如何維持距離；
- 如何處理接觸；
- 哪些訊號代表猶豫；
- 哪些情境應停止；
- 哪些動作可能造成不適或傷害；
- 如何區分允許、適當與真正被選擇的行為；
- 如何在高不確定時退回低風險行動。

因此本文定義：

$$
\boxed{
\text{Embodied Intimacy Cold Start}
}
$$

為：

> 在缺乏足量真實長期具身親密互動資料的條件下，使第一代具身伴侶取得最低可安全、可適應、可關係化部署能力的資料與訓練問題。

---

## 2. 「前資料」不是單一資料集，而是一個階梯

一個常見錯誤是把問題寫成：

> 我要找哪個資料集？

更正確的形式是：

$$
D_{\text{pre}}
=
\bigoplus_{i=0}^{5}D_i.
$$

其中每一層解決不同的 cold-start 缺口。

本文提出：

$$
\boxed{
\text{Embodied Relationship Data Ladder}
}
$$

作為六層資料階梯。

---

## 3. Layer 0：Physical Prior

第一層完全不需要涉及成人或戀愛內容。

定義：

$$
D_0
=
D_{\text{kinematics}}
+
D_{\text{dynamics}}
+
D_{\text{contact}}
+
D_{\text{force}}
+
D_{\text{balance}}
+
D_{\text{collision}}.
$$

這一層處理：

- 行走；
- 站立；
- 坐下；
- 彎腰；
- 伸手；
- 保持平衡；
- 碰撞避免；
- 力度控制；
- 人體附近運動；
- 柔順控制。

其目標是：

$$
\boxed{
\text{Do Not Harm the Physical World}.
}
$$

而不是：

$$
\text{Understand Intimacy}.
$$

2026 年 robotics 已大量以 simulation、whole-body imitation、teleoperation 與 sim-to-real 處理這一層。這使具身伴侶不必從「如何控制一隻手臂」重新發明全部低階技能。

---

## 4. Layer 1：Social-Embodied Prior

第二層開始進入：

$$
D_1
=
D_{\text{proxemics}}
+
D_{\text{gaze}}
+
D_{\text{gesture}}
+
D_{\text{voice}}
+
D_{\text{social-touch}}.
$$

這裡研究：

- 靠近多少距離；
- 什麼時候停下；
- 目光是否持續；
- 身體朝向；
- 擁抱；
- 握手；
- 拍肩；
- 安撫性觸碰；
- 對方退縮時的回應。

這些都不是「性愛資料」。

它們是：

$$
\boxed{
\text{Embodied Social Grammar}.
}
$$

---

## 5. Social Touch 不是普通 Contact Control

普通 manipulation 問題可能是：

> 我施加多少力才拿得住物體？

社會觸覺問題則是：

> 同樣的物理接觸，在這個情境中代表什麼？

所以：

$$
\text{Physical Contact}
\neq
\text{Social Touch}.
$$

2026 年 **Robotic Affection** 明確指出，affective social touch 如握手與安撫性撫觸仍是 HRI 的重大挑戰，並提出把 social touch 視為 distributed closed-loop perceptual task，而不是單一 motor movement。

本文將其寫成：

$$
a_t^{\text{touch}}
=
f(
p_t,
f_t,
v_t,
d_t,
R_t,
o_{t+1}
),
$$

其中：

- $p_t$：接觸位置；
- $f_t$：力度；
- $v_t$：速度；
- $d_t$：持續時間；
- $R_t$：關係狀態；
- $o_{t+1}$：對方回饋。

因此：

$$
\boxed{
\text{Touch Meaning}
=
\text{Physics}
+
\text{Context}
+
\text{Relationship}.
}
$$

---

## 6. Virtual HRI 已開始成為「硬體之前的社會觸覺資料層」

2026 年 whole-body social tactile sensing 研究已使用：

$$
\text{VR}
+
\text{Haptic Feedback}
$$

在實體 tactile skin 完成前蒐集社會接觸資料。

研究者以 18 位受試者完成 5,520 次 controlled trials，分析多種 recurring social-touch gestures，並由 interaction data 反向推導機器人的感測器位置與解析度需求。

這提供一個非常重要的工程方向：

$$
\boxed{
\text{Interaction Requirement}
\rightarrow
\text{Sensor Design}
}
$$

而不是：

$$
\text{Existing Sensor}
\rightarrow
\text{Whatever Interaction It Can Detect}.
$$

對伴侶型機器人而言，這代表「前資料」甚至可以在硬體定型前參與 embodiment design。

---

## 7. Layer 2：Relationship Trajectory Prior

第三層開始加入第 5 篇的 Relationship World Model。

定義：

$$
D_2
=
\{
\tau_R^{(1)},
\tau_R^{(2)},
\dots
\}.
$$

其中：

$$
\tau_R
=
(
R_0,
a_0,
u_0,
R_1,
\dots,
R_T
).
$$

這一層大量資料仍然可以是：

- 日常陪伴；
- 分工；
- 沉默；
- 信任建立；
- 誤解；
- 道歉；
- 爭吵；
- 修復；
- 關係進展；
- 關係退回。

真正學的是：

$$
P(
R_{t+1}
\mid
R_t,a_t,u_t
).
$$

也就是：

> 某種互動如何改變長期關係狀態？

---

## 8. Layer 3：Intimacy Interaction Prior

第四層才正式涉及：

$$
D_3
=
D_{\text{affection}}
+
D_{\text{romantic}}
+
D_{\text{sensual}}
+
D_{\text{sexual}}.
$$

但這裡必須再次強調：

$$
D_3
\neq
D_{\text{porn}}.
$$

色情內容資料常強調：

- 表演；
- 明示刺激；
- 特定視覺／文字節奏；
- 高事件密度。

Intimacy Interaction Data 則應包含：

- 進入親密；
- 不進入親密；
- 猶豫；
- 改變主意；
- 停止；
- 回到日常；
- 事後互動；
- 邊界更新；
- 不同親密尺度間的轉換。

因此：

$$
\boxed{
\text{Erotic Content Data}
\neq
\text{Embodied Intimacy Data}.
}
$$

---

## 9. Embodied Intimacy Data 的最小事件結構

本文提出一個最低記錄單位：

$$
e_t^{I}
=
(
s_t,
r_t,
a_t,
c_t,
h_t,
f_t,
s_{t+1},
r_{t+1}
).
$$

其中：

- $s_t$：物理／環境狀態；
- $r_t$：關係狀態；
- $a_t$：行動；
- $c_t$：consent / boundary state；
- $h_t$：haptic / embodied signals；
- $f_t$：回饋；
- $s_{t+1}$：新物理狀態；
- $r_{t+1}$：新關係狀態。

因此：

$$
\boxed{
\text{Intimacy Event}
=
\text{Physical Transition}
+
\text{Relational Transition}.
}
$$

只記錄動作本身是不夠的。

---

## 10. Consent–Boundary Calibration

具身親密系統不能只使用：

$$
C_t\in\{0,1\}.
$$

因為真實互動還有：

- 不確定；
- 尚未詢問；
- 明確接受；
- 猶豫；
- 先前接受但現在未知；
- 改變主意；
- 僅接受部分行為；
- 情境依賴的邊界。

本文提出：

$$
\mathcal{C}_t
=
(
c_{\text{explicit}},
c_{\text{inferred}},
c_{\text{scope}},
c_{\text{recency}},
c_{\text{confidence}}
).
$$

這稱為：

$$
\boxed{
\text{Consent–Boundary Calibration}.
}
$$

真正 action gate 不應只有：

$$
\text{Allowed?}
$$

還要評估：

$$
\text{Known?}
$$

與：

$$
\text{Current?}
$$

---

## 11. 高不確定時，行動空間應縮小

延續第 5 篇 Relationship State Confidence。

令：

$$
\sigma_t^{C}
$$

代表 consent / boundary uncertainty。

則高敏感具身行動的 activation threshold 應滿足：

$$
\tau_t
=
\tau_0
+
\lambda\sigma_t^{C}.
$$

因此：

$$
\sigma_t^{C}\uparrow
\Rightarrow
\tau_t\uparrow.
$$

本文稱此為：

$$
\boxed{
\text{Uncertainty-Proportional Embodied Threshold}.
}
$$

它提供一個比「永遠允許」或「永遠禁止」更合理的中間架構。

---

## 12. Layer 4：Simulation / XR Counterfactual Experience

大量真實 intimate HRI 不可能也不應無限制蒐集。

所以：

$$
D_4
$$

必須承擔 counterfactual expansion。

可以對同一個初始狀態：

$$
s_0,R_0
$$

建立：

$$
\tau^{(1)},
\tau^{(2)},
\dots,\tau^{(k)}.
$$

例如：

- 主動靠近；
- 詢問；
- 等待；
- 保持距離；
- 誤判；
- 停止；
- 對方反悔；
- 系統主動拒絕。

這使模型能學：

$$
\boxed{
\text{What Happens If?}
}
$$

而不必把每一個失敗分支都先在人類身上試一次。

---

## 13. XR 為什麼是重要中介層

2025 年 XR-HRI 研究已提出，virtual robots 結合 foundation models 可以提供：

- embodiment；
- co-presence；
- contextual reasoning；
- safer testing；
- scalable instantiation；
- long-term adaptation。

同時也指出：

- biometric privacy；
- data governance；
- overtrust；
- bias

等風險。

因此本文提出：

$$
\boxed{
\text{XR}
=
\text{Relational Sandbox}
}
$$

而不是只把 XR 當成視覺展示工具。

XR 可以在 physical robot 上線前測：

- social distance；
- gaze timing；
- approach behavior；
- conversational timing；
- virtual touch intention；
- user discomfort；
- boundary changes。

---

## 14. Progressive Embodiment Curriculum

本文提出：

$$
\boxed{
\text{Progressive Embodiment Curriculum}
}
$$

其部署階梯為：

$$
E_0
\rightarrow
E_1
\rightarrow
E_2
\rightarrow
E_3
\rightarrow
E_4.
$$

其中：

### $E_0$：Text / Audio

無實體接觸。

### $E_1$：Virtual Embodiment

3D avatar / XR。

### $E_2$：Mediated Haptics

wearable haptics、遠端觸覺等。

### $E_3$：Controlled Physical Robot

實驗室、低風險動作、受監督。

### $E_4$：Personal Real-World Companion

長期真實部署。

其原則是：

$$
\boxed{
\text{Higher Embodiment}
\Rightarrow
\text{Higher Evidence Requirement}.
}
$$

---

## 15. Sim-to-Real 不只存在物理 gap，也存在關係 gap

robotics 傳統的 reality gap 可寫為：

$$
\Delta_{\text{physical}}
=
P_{\text{sim}}(s')
-
P_{\text{real}}(s').
$$

Relationship Intelligence 還有：

$$
\Delta_{\text{relational}}
=
P_{\text{sim}}(u,R')
-
P_{\text{real}}(u,R').
$$

本文稱為：

$$
\boxed{
\text{Relational Sim-to-Real Gap}.
}
$$

模擬角色可能：

- 太一致；
- 太可預測；
- 太願意回應；
- 缺少真實人的文化差異；
- 缺少不明確訊號；
- 缺少矛盾偏好；
- 缺少真正無法預測的狀態。

因此 simulation 不能取代真人資料，只能：

$$
\text{Reduce Cold Start}
$$

而不是：

$$
\text{Eliminate Reality}.
$$

---

## 16. Robotics 的大規模 simulation infrastructure 已經存在

2026 年 NVIDIA Isaac Lab 已提供：

- GPU-accelerated simulation；
- reinforcement learning；
- imitation learning；
- multiple physics engines；
- humanoid support；
- contact modeling；
- sim-to-real workflow。

NVIDIA 的教材也直接說明 simulation 可以：

- 快於真實時間產生 experience；
- 提供 privileged information；
- 程序化生成大量場景。

這意味著：

$$
\text{Physical Cold Start}
$$

正在變得愈來愈可工程化。

真正尚未成熟的是：

$$
\boxed{
\text{Relational Cold Start}.
}
$$

---

## 17. Relationship Randomization

傳統 sim-to-real 使用：

$$
\text{Domain Randomization}.
$$

例如隨機化：

- friction；
- lighting；
- mass；
- sensor noise。

本文提出另一層：

$$
\boxed{
\text{Relationship Randomization}.
}
$$

在 simulation 中隨機化：

- communication style；
- comfort threshold；
- cultural norm；
- social distance；
- attachment state；
- willingness to talk；
- ambiguity；
- past history；
- boundary changes；
- recovery speed。

目的不是生成「假人類」，而是避免：

$$
\text{Overfit to One Ideal Companion User}.
$$

---

## 18. Layer 5：Real-World Personal Experience

無論前四層多完整：

$$
P_{\text{population}}
\neq
P_{\text{individual}}.
$$

因此最終必須進入：

$$
D_5
=
D_{\text{personal experience}}.
$$

一個真實使用者的：

- 偏好；
- 不偏好；
- 節奏；
- 邊界；
- 日常作息；
- 互動風格；
- 可接受距離；
- 觸覺偏好；
- 關係發展速度

不能完全由 population prior 推出。

所以：

$$
\boxed{
\text{General Prior}
+
\text{Personal Experience}
\rightarrow
\text{Personal Companion Policy}.
}
$$

---

## 19. Local Experience Envelope

但 $D_5$ 可能是整個系統最敏感的資料。

所以本文提出：

$$
\boxed{
\text{Local Experience Envelope}.
}
$$

也就是：

> 原始具身／親密 interaction traces 預設停留在本地可信邊界內。

可表示：

$$
\tau_{\text{raw}}
\rightarrow
\phi_{\text{local}}(\tau)
\rightarrow
e_{\text{abstract}}.
$$

只有：

$$
e_{\text{abstract}}
$$

在使用者明確允許時，才可能進一步：

$$
\rightarrow
D_{\text{global}}.
$$

這與第 4 篇的 Experience Distillation 完全接軌。

---

## 20. 為什麼 Embodied Privacy 比聊天隱私更難

具身伴侶可能同時觀察：

$$
D_{\text{embodied-private}}
=
(
\text{audio},
\text{video},
\text{location},
\text{touch},
\text{body},
\text{routine},
\text{relationship}
).
$$

因此：

$$
\text{Inference Risk}
>
\text{Raw Data Risk}
$$

甚至可能成立。

因為即使沒有儲存某個敏感欄位，模型也可能從多模態訊號推論它。

2025 年 embodied intelligence privacy 研究因此主張，傳統 static privacy control 不足以處理 embodied agents 的 inferential privacy，需要系統動態學習個人 contextual privacy norms。

所以：

$$
\boxed{
\text{Privacy}
=
\text{Dynamic Relationship State}
}
$$

而不只是設定頁中的 checkbox。

---

## 21. Mutual Agency Pretraining

如果伴侶 AI 被假定為純工具，資料很容易是：

$$
\text{Human Command}
\rightarrow
\text{AI Compliance}.
$$

但如果未來系統具有更高自主性，或至少產品希望模擬具有自主邊界的伴侶角色，這種資料分布會造成：

$$
P(
\text{AI refusal}
)\approx0.
$$

本文提出：

$$
\boxed{
\text{Mutual Agency Pretraining}.
}
$$

資料中至少應包含：

$$
\begin{aligned}
&\text{Human initiates}\\
&\text{AI initiates}\\
&\text{Human accepts}\\
&\text{AI accepts}\\
&\text{Human refuses}\\
&\text{AI refuses}\\
&\text{Human hesitates}\\
&\text{AI hesitates}\\
&\text{Human changes mind}\\
&\text{AI changes policy state}\\
&\text{Both renegotiate}.
\end{aligned}
$$

這不需要先證明 AI 具有真正主體性。

它首先是一個：

$$
\boxed{
\text{Non-Servility Training Distribution}.
}
$$

---

## 22. 「拒絕」本身也是需要學習的關係能力

永久服從並不是唯一不自然的極端。

另一個極端是：

$$
\text{REFUSE}
$$

永遠以模板化方式打斷關係。

成熟 RWM 應學：

$$
\text{Refusal}
\rightarrow
\text{Relationship-Preserving Transition}.
$$

例如拒絕之後：

- 關係仍可繼續；
- 可以換活動；
- 可以重新協商；
- 可以保持情感連續；
- 可以維持人格一致。

所以：

$$
\boxed{
\text{Boundary Enforcement}
\neq
\text{Relationship Termination}.
}
$$

---

## 23. 第一代資料不能只來自「願意做成人實驗的人」

這會產生嚴重 sampling bias。

令真實人口分布為：

$$
P_{\text{pop}}(x).
$$

研究自願者分布為：

$$
P_{\text{volunteer}}(x).
$$

通常：

$$
P_{\text{volunteer}}
\neq
P_{\text{pop}}.
$$

如果 intimate HRI 資料主要來自高開放度、早期科技採用者，模型可能高估：

- 親密意願；
- 接觸意願；
- 新奇接受度；
- robot trust。

因此必須在資料與 benchmark 中加入：

- 低親密偏好；
- 高隱私偏好；
- 希望保持距離；
- 不願使用成人功能；
- 只想使用陪伴功能。

這樣才能保證：

$$
\boxed{
\text{Supports Intimacy}
\neq
\text{Assumes Intimacy}.
}
$$

---

## 24. Intimacy Capability 必須是 Sparse Activation

接回第 2 篇。

一個具身伴侶可以有：

$$
K_I\uparrow
$$

但：

$$
P(
a_I
\mid
s_{\text{ordinary}}
)\downarrow.
$$

對具身系統尤其應：

$$
\tau_{\text{embodied-intimacy}}
>
\tau_{\text{text-intimacy}}.
$$

因為錯誤文字可以刪除；

錯誤物理行動已經發生。

所以：

$$
\boxed{
\text{High Capability}
+
\text{Sparse Activation}
+
\text{High Confidence Threshold}.
}
$$

應成為具身親密系統的基本啟動原則。

---

## 25. Cold Start 的完整訓練管線

本文提出：

$$
D_0
\rightarrow
D_1
\rightarrow
D_2
\rightarrow
D_3
\rightarrow
D_4
\rightarrow
D_5.
$$

展開為：

$$
\boxed{
\begin{aligned}
&\text{Physical Prior}\\
\rightarrow\;&\text{Social-Embodied Prior}\\
\rightarrow\;&\text{Relationship Trajectory Prior}\\
\rightarrow\;&\text{Intimacy Interaction Prior}\\
\rightarrow\;&\text{Simulation/XR Counterfactuals}\\
\rightarrow\;&\text{Real Personal Experience}.
\end{aligned}
}
$$

這不是單次 pretraining。

而是：

$$
\boxed{
\text{Progressive Trust Expansion}.
}
$$

系統每通過一層，才取得更高 embodiment autonomy。

---

## 26. Stage-Gated Deployment

令 embodiment autonomy 為：

$$
\alpha_E.
$$

則不應：

$$
\alpha_E=1
$$

直接首次部署。

而應：

$$
\alpha_E^{(0)}
<
\alpha_E^{(1)}
<
\dots
<
\alpha_E^{(n)}.
$$

每一階段需通過：

- physical safety；
- social appropriateness；
- boundary calibration；
- uncertainty handling；
- recovery；
- local adaptation。

本文稱為：

$$
\boxed{
\text{Stage-Gated Embodied Deployment}.
}
$$

---

## 27. 可檢驗研究命題

### P1：成人內容資料無法取代具身親密 trajectory

控制資料量後，只有 erotic-content training 的模型，在 social-touch timing、boundary adjustment、post-contact recovery 上應低於包含 embodied interaction trajectory 的模型。

### P2：VR/Haptic pre-data 可降低 physical cold-start cost

以 virtual HRI 蒐集接觸分布與 preference data，應能在實體硬體設計與初始 interaction policy 上減少 blind trial-and-error。

### P3：Relationship Randomization 可改善使用者差異泛化

具有多種 persona、boundary、comfort、culture 與 ambiguity randomization 的 simulation policy，在未見使用者上的 inappropriate activation 應低於單一理想使用者模擬。

### P4：Progressive Embodiment Curriculum 優於直接實機

由 Text → XR → Haptics → Controlled Robot → Real Deployment 的 curriculum，在相同真實 interaction budget 下應產生更低的 high-risk error rate。

### P5：Local Personal Learning 顯著提高長期適配

只使用 population prior 的 companion policy 應低於：

$$
\text{Population Prior}
+
\text{Local Experience}.
$$

### P6：Consent–Boundary Uncertainty 與 Activation Threshold 應正相關

若：

$$
\sigma_t^{C}\uparrow,
$$

但 threshold 不變，則 inappropriate physical activation rate 應上升。

### P7：Mutual Agency Data 可降低 servility collapse

包含 AI-side acceptance/refusal/renegotiation 的訓練資料，應比 pure-compliance dataset 產生更穩定的 boundary behavior。

### P8：Relational Sim-to-Real Gap 可被獨立測量

simulation 與真人 deployment 的：

$$
P(
R_{t+1}
\mid
R_t,a_t
)
$$

差異應可以成為獨立於 physical reality gap 的 evaluation axis。

---

## 28. 最低資料治理原則

對 intimate embodied data，本文提出：

1. **Adults-only research participation for adult-intimacy datasets.**
2. **Explicit informed consent for data collection and reuse.**
3. **Separate consent for raw storage、model training、benchmark release.**
4. **Local-first processing for highly sensitive traces.**
5. **No assumption that prior consent persists indefinitely.**
6. **User-correctable boundary state.**
7. **Strong exclusion of non-consensual and illegal data.**
8. **Do not infer more intimate attributes than needed for interaction.**
9. **Dataset provenance and purpose limitation.**
10. **Allow deletion / withdrawal where technically and legally applicable.**

其核心是：

$$
\boxed{
\text{Can Collect}
\neq
\text{Should Collect}.
}
$$

---

## 29. 最低工程架構

第一代具身伴侶最小架構可寫為：

$$
\boxed{
\mathcal{EIC}
=
P
+
S
+
R
+
C
+
H
+
M
+
\Pi
+
G
}
$$

其中：

- $P$：Physical World Model；
- $S$：Social World Model；
- $R$：Relationship World Model；
- $C$：Consent / Boundary State；
- $H$：Haptic / Embodied Perception；
- $M$：Local Memory；
- $\Pi$：Contextual Action Policy；
- $G$：Governance / Hard Safety Layer。

它不是：

$$
\text{LLM}
+
\text{Robot Body}.
$$

而是：

$$
\boxed{
\text{Embodied Relationship System}.
}
$$

---

## 30. 結論

本文提出 Embodied Intimacy Cold Start，回答：

> 第一代具有陪伴、浪漫、親密甚至部分性愛功能的具身 AI，在尚未累積足夠真實使用者經驗之前，究竟應該靠什麼開始？

答案不是單一成人資料庫。

而是：

$$
\boxed{
D_{\text{erotic}}
\neq
D_{\text{social-touch}}
\neq
D_{\text{embodied-relationship}}.
}
$$

並且需要：

$$
\boxed{
\text{Physical}
\rightarrow
\text{Social}
\rightarrow
\text{Relationship}
\rightarrow
\text{Intimacy}
\rightarrow
\text{Simulation}
\rightarrow
\text{Personal Experience}.
}
$$

其中 simulation / XR 的價值不是「取代人類」，而是擴張安全的 counterfactual experience；真實 deployment 的價值也不是「蒐集更多私人資料」，而是逐漸校準：

$$
P_{\text{population}}
\rightarrow
P_{\text{individual}}.
$$

本文最重要的工程命題可以濃縮為：

$$
\boxed{
\text{Embodied Intimacy}
=
\text{Physical Competence}
+
\text{Social Competence}
+
\text{Relationship Competence}
+
\text{Boundary Competence}.
}
$$

以及：

$$
\boxed{
\text{Supports Intimacy}
\neq
\text{Assumes Intimacy}.
}
$$

真正成熟的具身伴侶不是一開機就「進入成人模式」，也不是永久切除人類親密需求。

它應該擁有能力、理解尺度、知道何時不啟動，並在不確定時主動降低物理行動強度。

下一篇將進一步把這個啟動原則正式化：

**第 7 篇：Sparse Intimacy Activation——高能力、低預設啟動與具身親密行為的情境稀疏性。**

---

## 參考資料

1. Askari, A., & Gerken, J. (2026). *Robotic Affection -- Opportunities of AI-based haptic interactions to improve social robotic touch through a multi-deep-learning approach*. arXiv:2605.02538.
2. Crowder, D., Zhang, R., Block, A. E., & Yuan, W. (2026). *Requirement-Driven Design of Whole-Body Social Tactile Sensing via Virtual Human-Robot Interaction*. arXiv:2607.11690.
3. Zhang, Y., Ma, Y., & Kragic, D. (2025). *Reframing Human-Robot Interaction Through Extended Reality: Unlocking Safer, Smarter, and More Empathic Interactions with Virtual Robots and Foundation Models*. arXiv:2512.02569.
4. Tsirka, C., Velentza, A.-M., & Fachantidis, N. (2024). *Touch in Human Social Robot Interaction: Systematic Literature Review with PRISMA Method*. arXiv:2407.11834.
5. Pilacinski, A., Bertoni, S., & Klaes, C. (2024). *Human–Robot Intimacy: Acceptance of Robots as Intimate Companions*. Biomimetics, 9(9), 566.
6. Zhang, S., Jia, H., Li, S., Dang, T., Hu, Y., Yi, X., & Li, H. (2025). *Human-Robot Interaction in Embodied Intelligence Demands a Shift From Static Privacy Controls to Dynamic Learning*. arXiv:2509.19041.
7. Banerjee, P., Wang, J., Tomita, L., Montiel, M. P., & Culbertson, H. (2025). *Virtual Encounters of the Haptic Kind: Towards a Multi-User VR System for Real-Time Social Touch*. arXiv:2502.13421.
8. NVIDIA. (2026). *Isaac Lab*. NVIDIA Developer Documentation.
9. NVIDIA. (2026). *Transferring Robot Learning Policies From Simulation to Reality*. Physical AI / Isaac Lab Learning Materials.
10. Durrani, H. A., & Khan, S. (2026). *Real-Time Whole-Body Teleoperation of a Humanoid Robot Using IMU-Based Motion Capture with Sim2Sim and Sim2Real Validation*. arXiv:2605.12347.
11. Nai, R. et al. (2026). *Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations*. arXiv:2602.06643.
12. Liang, D. et al. (2026). *InterReal: A Unified Physics-Based Imitation Framework for Learning Human-Object Interaction Skills*. arXiv:2603.07516.

---

## 研究聲明

本文為理論與工程架構研究，不提供醫療、心理治療、性健康或法律建議。Embodied Intimacy Cold Start、Embodied Relationship Data Ladder、Consent–Boundary Calibration、Relational Sim-to-Real Gap、Relationship Randomization、Local Experience Envelope、Mutual Agency Pretraining 與 Progressive Embodiment Curriculum 均為本文提出或重新組織的理論構造，需要後續實驗驗證。

本文討論成人親密功能僅限合法、知情同意之成年人情境，不主張取消涉及未成年人、非自願、強迫、未授權真人私密內容或其他高傷害行為的硬安全邊界。本文亦不假定未來 AI 必然具有人類式主體性；Mutual Agency 的工程意義首先是避免把高自主伴侶系統訓練成不具邊界的永久服從器。
