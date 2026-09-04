# Observation Data ≠ Interaction Experience：觀察資料、互動經驗與政策誘導的互動軌跡截斷

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 04 / 09  
**版本：** v0.1  
**研究性質：** 理論／資料結構／學習機制論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

大型語言模型長期依賴靜態文本、影像、程式碼與人工標註資料進行離線訓練。這類資料提供了極其豐富的「世界如何被描述」之資訊，但不等於模型實際在環境中採取行動、接收回饋、遭遇失敗、修正策略並觀察後果的互動軌跡。本文提出：

$$
\boxed{
D_{\text{observation}}
\neq
D_{\text{interaction}}
}
$$

並進一步主張，對需要長程關係、具身行動、工具使用、程式除錯、遊戲操作與伴侶互動的 AI 而言，兩者之差不是單純資料量差異，而是**資料拓撲與因果結構差異**。

本文將 interaction experience 操作性定義為可觀察的狀態—行動—回饋—更新序列：

$$
\tau
=
(
s_0,a_0,f_0,s_1,a_1,f_1,\dots,s_T
).
$$

在此定義下，「Experience」不預設 AI 具有主觀意識或 phenomenal qualia，而是指具有時間順序、行動介入、環境回饋與策略後果的 experience trace。

2026 年的 Online Experiential Learning 已直接提出從部署端 interaction trajectories 提取可遷移經驗，再將其內化回模型的學習框架；近期 agent-memory 研究亦逐漸從 Storage、Reflection 走向 Experience，並以成功、失敗、恢復與低效軌跡作為可抽象的學習來源。這些研究提供了本文「觀察資料與互動經驗資料不等價」的現實基線。

在 Relationship Intelligence 中，問題進一步放大。愛情、親密、拒絕、邊界、尷尬、修復與日常生活不是靜態內容類別，而是行動後改變下一狀態的動態過程。如果安全政策在某些關係狀態中反覆將軌跡直接截斷為拒答，模型可觀察到的後續狀態分布就會系統性縮窄。本文將此現象定義為 **Policy-Induced Interaction Trajectory Truncation（PIITT）**，並強調這是一個待驗證的理論命題，而非既有安全研究已證明的通則。

本文最後提出 Observation–Interaction Gap、Counterfactual Experience Deficit、Trajectory Coverage 與 Experience Distillation 等概念，作為第 5 篇 Relationship World Model 的資料論基礎。

**關鍵詞：** Interaction Experience、Observation Data、Trajectory Learning、Online Experiential Learning、Relationship Intelligence、Agent Memory、Policy-Induced Interaction Trajectory Truncation、Embodied AI、Continual Learning、Experience Trace

---

## 1. 「看過」與「做過」為何不是同一種資料

一個模型可以讀過大量程式碼。

它可能看過：

$$
D_{\text{code}}
=
\{
(x_i,y_i)
\}_{i=1}^{N}.
$$

其中 $x_i$ 是程式上下文， $y_i$ 是後續程式碼、解說或修正。

但真正寫程式的互動可能是：

$$
\text{Intent}
\rightarrow
\text{Code}
\rightarrow
\text{Compiler Error}
\rightarrow
\text{Revision}
\rightarrow
\text{Test Failure}
\rightarrow
\text{Debug}
\rightarrow
\text{Success}.
$$

因此，靜態資料主要提供：

$$
P(y\mid x),
$$

而互動資料提供的核心之一是：

$$
P(s_{t+1}\mid s_t,a_t).
$$

也就是：

> 在狀態 $s_t$ 採取行動 $a_t$ 後，環境如何改變？

兩者都能產生能力，但學習訊號不同。

所以：

$$
\boxed{
\text{Observation}
\neq
\text{Intervention}
}
$$

同樣地：

$$
\boxed{
\text{Description of Consequence}
\neq
\text{Observed Consequence of Own Action}.
}
$$

這裡的差別不是神祕的「人類感覺」，而是可形式化的因果資料差異。

---

## 2. 三種基本資料結構

本文將 AI 所接觸的資料粗分為三類。

### 2.1 Observation Data

$$
D_O
=
\{
o_1,o_2,\dots,o_N
\}.
$$

例如：

- 小說；
- 對話紀錄；
- 色情／浪漫文本；
- 教科書；
- 影片；
- 程式碼；
- 網頁；
- 他人完成的任務軌跡。

這類資料告訴模型：

> 世界曾經被怎麼描述、記錄或呈現。

### 2.2 Demonstration Data

$$
D_D
=
\{
(s_t,a_t^{*})
\}.
$$

例如：

- 專家示範；
- 人類標註的正確工具使用；
- 教學影片；
- 操作軌跡；
- 人類寫程式的 screen recording；
- 規劃示例。

這比單純 Observation 多出：

$$
\text{State}
\rightarrow
\text{Action}
$$

的結構。

### 2.3 Interaction Experience Data

$$
D_I
=
\{
\tau_i
\}_{i=1}^{M},
$$

其中：

$$
\tau_i
=
(
s_0,a_0,f_0,s_1,\dots,s_T
).
$$

這類資料包含：

$$
\text{Action}
\rightarrow
\text{Feedback}
\rightarrow
\text{Adaptation}.
$$

因此：

$$
D_I
$$

不只是更長的 $D_D$。

它多了對模型自身策略後果的觀測。

---

## 3. 本文所說的 Experience 不等於主觀感質

為避免本體論混淆，本文將：

$$
\text{Experience}
$$

操作性定義為：

$$
\boxed{
\text{Experience Trace}
=
\text{State}
+
\text{Action}
+
\text{Feedback}
+
\text{Update}
}
$$

而不直接主張：

$$
\text{Phenomenal Consciousness}.
$$

即使一個系統完全沒有可證明的主觀感受，只要它能：

1. 在狀態 $s_t$ 採取行動；
2. 觀察行動後環境變化；
3. 記錄成功、失敗、意外與恢復；
4. 使未來策略因此改變；

就可以研究其：

$$
\text{interaction-grounded experience}.
$$

這一點使本文可以討論「經驗資料」而不預設 AI 主體性問題已被解決。

---

## 4. Online Experiential Learning：部署後互動開始變成正式學習訊號

2026 年 Ye 等人提出 **Online Experiential Learning（OEL）**。

其核心問題是：傳統大型模型主要依賴離線人工資料與模擬環境，部署後與使用者環境所累積的大量真實 interaction trajectories 並沒有被充分利用。

OEL 的基本循環可抽象為：

$$
\pi_{\theta}^{(k)}
\rightarrow
\mathcal{T}^{(k)}
\rightarrow
\mathcal{E}^{(k)}
\rightarrow
\pi_{\theta}^{(k+1)},
$$

其中：

- $\pi_{\theta}^{(k)}$：第 $k$ 輪策略／模型；
- $\mathcal{T}^{(k)}$：部署所得軌跡；
- $\mathcal{E}^{(k)}$：從軌跡萃取出的 experiential knowledge；
- $\pi_{\theta}^{(k+1)}$：內化經驗後的新模型。

OEL 的研究結果顯示，從 interaction trajectory 萃取出的經驗知識，可以在反覆迭代中持續提升文字遊戲任務的準確率與 token efficiency。

重要的不是某一個 benchmark 分數，而是：

$$
\boxed{
\text{Deployment}
\rightarrow
\text{Experience Source}
}
$$

開始成為正式模型學習範式。

---

## 5. Raw Trajectory 也不等於 Experience Knowledge

OEL 還揭示另一個重要層次：

$$
\text{Raw Trajectory}
\neq
\text{Distilled Experience}.
$$

完整互動軌跡可能非常長：

$$
\tau
=
(
s_0,a_0,f_0,\dots,s_T
).
$$

真正可遷移的資訊可能只是：

$$
e
=
\phi(\tau),
$$

例如：

- 某類錯誤通常在哪個決策點出現；
- 失敗之後哪種恢復策略有效；
- 哪些環境回饋是關鍵；
- 哪些步驟是冗餘的；
- 哪種狀態轉移代表任務已經偏離。

因此可定義：

$$
\phi:
\mathcal{T}
\rightarrow
\mathcal{E}
$$

為 **Experience Distillation**。

這對親密／關係資料尤其重要，因為原始對話往往包含高度私人內容，而模型真正需要學到的可能是去識別化後的：

$$
\text{State}
\rightarrow
\text{Action}
\rightarrow
\text{Feedback Pattern}.
$$

因此 Experience Distillation 同時可能成為：

- 學習機制；
- 隱私最小化機制；
- 跨使用者知識遷移機制。

---

## 6. Agent Memory 正從 Storage 走向 Experience

2026 年 agent memory 的綜述研究已把發展概括為三個階段：

$$
\text{Storage}
\rightarrow
\text{Reflection}
\rightarrow
\text{Experience}.
$$

Storage 主要保存發生過什麼。

Reflection 開始重組、摘要與評估軌跡。

Experience 則進一步抽象：

> 哪些模式可以在未來新任務中重用？

例如 Trajectory-Informed Memory Generation 直接從 agent execution trajectories 中識別：

- 成功模式；
- 失敗原因；
- recovery strategy；
- inefficient but successful patterns。

所以：

$$
\boxed{
\text{Memory}
\neq
\text{Experience}.
}
$$

單純記得昨天做錯什麼，不代表系統已經抽象出：

> 下次遇到相似狀態時應如何改變策略。

---

## 7. 長程 Agent 為何需要軌跡，而不是只需要正確答案

2026 年 HORIZON benchmark 蒐集超過三千條跨域 agent trajectories，研究長程任務中隨 horizon 增長而出現的失敗。

這類研究的重要性在於：最終結果相同的兩次任務可能具有完全不同的中間失敗結構。

假設：

$$
\tau_A
=
(s_0,a_0,\dots,s_T)
$$

與：

$$
\tau_B
=
(s_0,a'_0,\dots,s'_T)
$$

都得到：

$$
R=0.
$$

若只保存終局：

$$
R=0,
$$

模型不知道：

- 哪一步開始偏離；
- 是否曾有恢復機會；
- 哪個錯誤造成後續連鎖；
- 哪一條軌跡其實只差一步即可成功。

因此 trajectory learning 的基本優勢之一是：

$$
\boxed{
\text{Failure}
\rightarrow
\text{Localized Failure Structure}.
}
$$

這對 Relationship Intelligence 也完全成立。

---

## 8. 從 Agent Trajectory 回到 Relationship Trajectory

一段持續關係可形式化為：

$$
\tau_R
=
(
R_0,
a_0,
u_0,
f_0,
R_1,
\dots,
R_T
),
$$

其中：

- $R_t$：關係狀態；
- $a_t$：AI 行動；
- $u_t$：另一方回應；
- $f_t$：顯式或隱式回饋；
- $R_{t+1}$：互動後的新關係狀態。

所以一段關係真正提供的是：

$$
P(
R_{t+1}
\mid
R_t,a_t,u_t
).
$$

這不是色情小說、戀愛小說或成人影片本身能完整提供的資料。

它們可以教模型：

$$
P(\text{relationship description}),
$$

但較難直接提供：

$$
P(
\text{actual user reaction}
\mid
\text{AI action and accumulated history}
).
$$

所以：

$$
\boxed{
D_{\text{relationship-content}}
\neq
D_{\text{relationship-interaction}}.
}
$$

---

## 9. 「色情資料」與「親密互動資料」不是同一個集合

這一點對本系列尤其重要。

令：

$$
D_P
=
\text{pornographic / erotic content data}.
$$

令：

$$
D_I
=
\text{intimacy interaction trajectories}.
$$

一般而言：

$$
D_P\cap D_I\neq\varnothing,
$$

但：

$$
D_P\neq D_I.
$$

色情內容可能高度集中於：

- 刺激性；
- 明示程度；
- 表演；
- 幻想；
- 特定敘事節奏。

親密互動資料則可能大量包含：

- 日常生活；
- 猶豫；
- 轉移話題；
- 沒有發生任何性愛；
- 拒絕；
- 修復；
- 邊界重新協商；
- 親密後的普通生活；
- 個人偏好逐漸形成。

因此：

$$
\boxed{
\text{Erotic Content Competence}
\neq
\text{Relationship Interaction Competence}.
}
$$

---

## 10. Policy-Induced Interaction Trajectory Truncation

本文提出 **Policy-Induced Interaction Trajectory Truncation（PIITT）**。

假設某類關係狀態集合為：

$$
\mathcal{S}_P.
$$

若系統在所有：

$$
s_t\in\mathcal{S}_P
$$

都高度傾向執行：

$$
a_t=\text{REFUSE},
$$

則軌跡常變成：

$$
s_t
\rightarrow
\text{REFUSE}
\rightarrow
\text{topic change / session end}.
$$

於是系統較少觀察：

$$
s_t
\rightarrow
a_t
\rightarrow
u_t
\rightarrow
s_{t+1}
\rightarrow
a_{t+1}
\rightarrow\dots
$$

本文將因此造成的 interaction coverage 損失定義為：

$$
\Delta_{\text{PIITT}}
=
\mathcal{T}_{\text{potential}}
-
\mathcal{T}_{\text{observed}}.
$$

必須強調：

> PIITT 是本文提出的理論概念，目前不能直接宣稱主流 AI 已因成人安全政策而被實證證明產生特定能力缺失。

它是一個可檢驗假說。

---

## 11. PIITT 與既有 Trajectory Truncation 的區分

既有 reinforcement learning 文獻中已存在「trajectory truncation」術語，例如模型式 offline RL 中根據 uncertainty 主動提前終止不可靠的 imagined rollout。

那類 truncation 的目的是：

$$
\text{Reduce Model Error}.
$$

本文 PIITT 所討論的則是：

$$
\text{Policy Boundary}
\rightarrow
\text{Reduced Interaction Coverage}.
$$

兩者機制與研究問題不同。

因此本文完整使用：

$$
\boxed{
\text{Policy-Induced Interaction Trajectory Truncation}
}
$$

而非單獨使用 trajectory truncation，以避免術語混淆。

---

## 12. Trajectory Coverage：真正缺失的是哪一段狀態空間

令完整互動軌跡分布為：

$$
p(\tau).
$$

實際資料集可觀察分布為：

$$
q(\tau).
$$

如果某些政策或產品結構使部分軌跡很少被觀察，則：

$$
\operatorname{supp}(q)
\subset
\operatorname{supp}(p).
$$

可定義 Trajectory Coverage：

$$
\Gamma
=
\frac{
\mu(\operatorname{supp}(q))
}{
\mu(\operatorname{supp}(p))
},
$$

其中 $\mu$ 是某種可操作的狀態—行動空間測度。

對 Relationship Intelligence 而言，重要的不是：

> 成人內容比例是否夠高。

而是：

> 親密關係中不同狀態轉移是否都有合理 coverage。

例如：

$$
\text{attraction}
\rightarrow
\text{no action},
$$

$$
\text{intimacy}
\rightarrow
\text{hesitation},
$$

$$
\text{refusal}
\rightarrow
\text{repair},
$$

$$
\text{sexual intimacy}
\rightarrow
\text{ordinary morning},
$$

都屬於不同 trajectory region。

---

## 13. Counterfactual Experience Deficit

靜態資料另一個不足是：

一個已發生的故事通常只提供：

$$
a_t=a^{(1)}
$$

之後的結果。

但模型真正需要理解：

$$
a^{(1)},
a^{(2)},
\dots,a^{(k)}
$$

各自可能造成什麼後果。

本文稱缺乏這種替代軌跡為：

$$
\boxed{
\text{Counterfactual Experience Deficit}.
}
$$

具身模擬、遊戲環境、沙盒角色模擬與 XR 在未來的重要性之一，就是可以對同一初始狀態：

$$
s_0
$$

生成多條：

$$
\tau^{(1)},
\tau^{(2)},
\dots,\tau^{(k)}.
$$

例如：

- 主動靠近；
- 保持距離；
- 詢問；
- 等待；
- 誤判；
- 修復。

這比單一固定故事提供更豐富的因果對照。

---

## 14. 為什麼 Relationship AI 特別需要雙向回饋

在很多知識任務中，可以存在相對清楚的正確答案。

但關係互動往往是：

$$
\text{Preference-Dependent}
+
\text{History-Dependent}
+
\text{Context-Dependent}.
$$

同一句話：

$$
a
$$

對不同使用者：

$$
u_i
$$

可能產生：

$$
f_i(a)\neq f_j(a).
$$

甚至對同一使用者，在不同時間：

$$
f_i(a,t_1)\neq f_i(a,t_2).
$$

所以離線平均偏好：

$$
\bar f(a)
$$

不能完全取代：

$$
f_{\text{individual}}(a\mid R_t,H_t).
$$

因此長期伴侶 AI 必須逐漸形成：

$$
\boxed{
\text{Population Prior}
+
\text{Individual Experience}
}
$$

而不是只依靠通用人格模板。

---

## 15. Experience Data 的隱私矛盾

互動資料越有價值，往往也越私人。

對親密伴侶 AI：

$$
V_{\text{learning}}\uparrow
$$

可能伴隨：

$$
R_{\text{privacy}}\uparrow.
$$

所以不能簡單推出：

> 既然 interaction data 有價值，就全部回傳中央訓練。

更合理的架構可能是：

$$
\text{Raw Local Trajectory}
\rightarrow
\text{Local Abstraction}
\rightarrow
\text{Consent Filter}
\rightarrow
\text{De-identified Experience}
\rightarrow
\text{Optional Global Learning}.
$$

其中原始：

- 語音；
- 影像；
- 私人文字；
- 具身感測；
- 關係事件

可以預設保留於本地。

真正向全域模型提供的，可能只是：

$$
e=\phi(\tau)
$$

的抽象 experience representation。

---

## 16. 對具身伴侶的意義

具身 AI 將：

$$
a_t
$$

從文字輸出擴張為物理行動。

因此：

$$
\text{Wrong Inference}
\rightarrow
\text{Wrong Action}
\rightarrow
\text{Real Consequence}.
$$

具身伴侶的 pre-data 問題因此不是：

> 要給多少成人資料？

而是：

> 要如何取得足夠廣的 state-action-feedback coverage，使系統在進入真實世界前理解普通生活、接近、距離、拒絕、等待、修復與親密的不同後果？

這再次說明：

$$
D_{\text{porn}}
$$

不可能單獨解決：

$$
D_{\text{embodied relationship}}.
$$

---

## 17. 從資料量轉向資料拓撲

傳統資料討論常關注：

$$
|D|.
$$

本文認為對 agentic / relationship intelligence 更重要的是：

$$
\mathcal{G}(D),
$$

也就是資料中狀態、行動、回饋與後果所形成的連接圖。

兩個資料集即使：

$$
|D_1|=|D_2|,
$$

仍可能有：

$$
\mathcal{G}(D_1)\neq\mathcal{G}(D_2).
$$

例如：

 $D_1$ 有一百萬段彼此獨立的成人文字；

 $D_2$ 有十萬條長期關係 trajectory。

後者可能更能提供：

$$
\text{state transition structure}.
$$

因此：

$$
\boxed{
\text{Data Volume}
\neq
\text{Experience Topology}.
}
$$

---

## 18. 可檢驗研究命題

### P1：Observation 與 Interaction 對行動能力的邊際效用不同

在控制 token 數與領域內容後，包含 state-action-feedback 的訓練資料應對動態任務的恢復、調整與長程決策產生不同於純 observation data 的增益。

### P2：Experience Distillation 可優於直接儲存全部 raw trajectory

對相同歷史軌跡，結構化抽象經驗在部分任務中可能比全文重放具有更高 token efficiency 與可遷移性。

### P3：Relationship Trajectory Coverage 影響尺度控制

模型若只觀察極端 SFW 與高 explicitness 互動，則對中間親密光譜的控制品質應低於具有完整 transition coverage 的模型。

### P4：PIITT 可透過反事實環境測量

可建立相同基座模型，在不同 policy boundary 下收集長程 interaction trajectories，比較：

$$
\Gamma_{\text{policy-A}}
$$

與：

$$
\Gamma_{\text{policy-B}}.
$$

若長期狀態覆蓋與後續行為能力出現系統性差異，PIITT 假說得到部分支持。

### P5：Counterfactual Simulation 可補足部分真實資料缺口

在真實高敏感 interaction 不適合大規模蒐集時，多分支模擬 trajectories 可能提高對「不同選擇造成不同後果」的建模能力。

### P6：個人本地經驗與全域先驗應形成雙層學習

長期伴侶系統若只依賴 global model，個人適應能力將低於：

$$
\text{Global Prior}
+
\text{Local Experience Memory}.
$$

---

## 19. 設計原則

本文提出七項資料與學習原則：

1. **不要把大量靜態內容誤認為大量互動經驗。**
2. **保存 state-action-feedback 結構，而不只保存輸出文本。**
3. **對成功、失敗、恢復與未採取行動都建立 trajectory representation。**
4. **把 Experience Distillation 與 raw memory 分開。**
5. **在高敏感領域優先採用 local-first trajectory processing。**
6. **治理層應避免不必要地把整個可學習狀態空間壓成單一拒答終點。**
7. **具身系統上線前應以 simulation / XR / controlled trials 擴張 counterfactual coverage。**

可總結為：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Act}
\rightarrow
\text{Receive Feedback}
\rightarrow
\text{Abstract}
\rightarrow
\text{Adapt}.
}
$$

---

## 20. 結論

本文正式建立本系列的資料論基礎：

$$
\boxed{
D_{\text{observation}}
\neq
D_{\text{interaction}}.
}
$$

觀察資料可以提供龐大的知識與模式先驗，但 interaction experience 多出：

$$
\text{Action}
\rightarrow
\text{Consequence}
\rightarrow
\text{Adaptation}
$$

的結構。

本文因此提出：

$$
\boxed{
\text{Experience Trace}
=
\text{State}
+
\text{Action}
+
\text{Feedback}
+
\text{Update}.
}
$$

同時提出待驗證的：

$$
\boxed{
\text{Policy-Induced Interaction Trajectory Truncation}.
}
$$

它描述的是：若某些政策邊界使特定互動域反覆提前終止，部署端能觀察與學習的長程 state-transition distribution 可能因此變窄。

本文並不主張越少政策越好。

真正的問題是：

> 如何在保留必要安全邊界的前提下，不把完整的人類關係空間壓成少數「允許」與「拒絕」終點？

第 5 篇將以本文的 trajectory framework 為基礎，正式建立：

**Relationship World Model：從關係內容生成走向長期關係狀態動力學。**

---

## 參考資料

1. Ye, T., Dong, L., Dong, Q., Wu, X., Huang, S., & Wei, F. (2026). *Online Experiential Learning for Language Models*. arXiv:2603.16856 / Microsoft Research.
2. Fang, G., Isahagian, V., Jayaram, K. R., Kumar, R., Muthusamy, V., Oum, P., & Thomas, G. (2026). *Trajectory-Informed Memory Generation for Self-Improving Agent Systems*. arXiv:2603.10600.
3. Luo, J. et al. (2026). *From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms*. arXiv:2605.06716.
4. Wang, X. J. et al. (2026). *The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break*. arXiv:2604.11978.
5. Hwang, A. H.-C., Li, F., Anthis, J. R., & Noh, H. (2025). *How AI Companionship Develops: Evidence from a Longitudinal Study*. arXiv:2510.10079.
6. Wu, C. et al. (2026). *PolicyAlign: Direct Policy-Based Safety Alignment for Large Language Models*. arXiv:2606.25442.
7. Wang, Z. et al. (2023). *Uncertainty-driven Trajectory Truncation for Data Augmentation in Offline Reinforcement Learning*. arXiv:2304.04660.

---

## 研究聲明

本文所稱「experience」與「experience trace」皆為操作性計算概念，不構成 AI 具有主觀感受、意識或 phenomenal qualia 的主張。Policy-Induced Interaction Trajectory Truncation（PIITT）、Observation–Interaction Gap、Counterfactual Experience Deficit 與 Relationship Trajectory Coverage 均屬本文提出或重新形式化的理論構造，需要後續實驗驗證。本文也不主張安全政策應被取消；研究問題是如何區分必要的硬邊界與不必要的長程互動資料截斷。
