# 大模型不應控制一切：狀態機、行為樹與 LLM 的分工

**系列：狀態驅動的本地具身 AI｜第 3 篇**  
**版本：v0.1**  
**日期：2026-08-01**

---

## 摘要

大型語言模型、視覺語言模型與 Vision-Language-Action（VLA）模型正在快速進入機器人系統。PaLM-E 展示了把視覺、連續狀態估計與文字一起送入大型模型以完成具身推理的可能；RT-2 更進一步把機器人動作表示為 token，使模型能直接從視覺與語言映射到動作。這些成果證明了大型模型能夠進入具身控制鏈，但並不等於「整個機器人都應交由大型模型控制」。

本文提出一個相反而更工程化的命題：**高階生成模型應提供語義、規劃、未知情境求解與策略候選；而安全、即時反射、裝置生命週期、任務執行狀態與行動仲裁，應由可驗證、可調試、可持續運行的控制結構負責。**

本文把具身 AI 的控制權拆為五層：安全監督層、物理反射層、狀態機層、行為樹／任務編排層，以及 LLM／VLM 高階推理層。LLM 的輸出不是 actuator command，而是 proposal。Proposal 必須經過結構化解析、世界狀態一致性檢查、權限檢查、前置條件檢查、安全約束與動作仲裁，才能被轉化為真正的物理行動。

本文進一步比較有限狀態機（FSM）與行為樹（BT）的角色：FSM 適合描述生命週期、裝置模式與明確互斥狀態；BT 則更適合大型任務中可重用、可中斷、可回退的行為組合。2025 年發表於 IEEE Transactions on Automation Science and Engineering 的實證比較指出，在任務複雜度上升時，BT 的維護性相較 FSM 更好，但兩者不是互斥替代，而可以形成分層混合系統。

本文最後提出「受約束智能控制堆疊」：

$$
\text{LLM Proposal}
\rightarrow
\text{Policy Validation}
\rightarrow
\text{State/BT Arbitration}
\rightarrow
\text{Safety Gate}
\rightarrow
\text{Controller}
\rightarrow
\text{Actuator}.
$$

它是下一篇「世界狀態機」的直接前置基礎。

**關鍵詞：** 大語言模型、具身智能、有限狀態機、行為樹、VLA、機器人安全、行動仲裁、世界狀態、LLM Planner、分層控制

---

# 1. 問題的真正形式：誰擁有行動權？

當大型模型只產生文字時，模型犯錯的主要後果通常停留在資訊層。

但當模型接入輪子、手臂、夾爪、門鎖、家電、車輛或工業設備，錯誤便會從：

$$
\text{semantic error}
$$

轉化為：

$$
\text{physical effect}.
$$

因此，真正的問題不再只是：

> 模型能不能理解命令？

而是：

> **模型是否有權直接讓世界發生變化？**

這裡需要區分兩個概念：

$$
\text{Reasoning Authority}
$$

與

$$
\text{Execution Authority}.
$$

模型可以擁有很高的推理能力，卻不必同時擁有不受約束的執行權。

本文主張：

$$
\boxed{
\text{High Reasoning Authority}
\not\Rightarrow
\text{Unrestricted Execution Authority}
}
$$

這是具身 AI 與純聊天 AI 最重要的架構分界之一。

---

# 2. VLA 證明「可以直接控制」，但不等於「應全部直接控制」

2023 年的 RT-2 把機器人動作轉換為與文字相同形式的 token，讓 Vision-Language 模型能夠直接輸出機器人行動。其測試顯示，從網路視覺—語言資料得到的語義能力可以轉移到機器人控制上。

PaLM-E 則把文字、視覺與連續狀態估計一起輸入大型具身模型，用於機器人操作規劃、視覺問答與其他具身任務。

這些研究的重要性在於：

$$
\text{Perception}
+
\text{Language}
+
\text{Action}
$$

可以進一步被統一學習。

然而，「端到端可學習」與「所有控制權都應由單一模型掌握」是兩個不同命題。

例如，一個 VLA 可以學會：

> 「把紅杯子放到桌子右側。」

但以下能力仍具有不同的工程要求：

- 馬達電流保護；
- 夾爪力矩限制；
- 避免碰撞人類；
- 急停；
- 電量不足時回充；
- 裝置故障後禁止再次執行；
- 任務取消；
- 權限不足時拒絕開門。

這些條件往往需要：

$$
\text{determinism}
+
\text{bounded latency}
+
\text{auditable transitions}
$$

而不只是平均成功率很高。

---

# 3. 將 LLM 視為「提案者」而不是「皇帝」

最簡化、也最危險的一種架構是：

```text
Sensor
  ↓
LLM / VLM / VLA
  ↓
Motor Command
```

也就是：

$$
a_t=M(o_t,c_t),
$$

其中模型 $M$ 直接將觀測 $o_t$ 與上下文 $c_t$ 轉換成物理行動 $a_t$ 。

本文建議加入一個權力分離。

模型先輸出：

$$
p_t=M(S_t,e_t,K_t),
$$

其中 $p_t$ 不是最終動作，而是 proposal。

接著：

$$
a_t=G(p_t,S_t,C_t,P_t),
$$

其中：

- $S_t$ ：當前世界狀態；
- $C_t$ ：硬性約束；
- $P_t$ ：權限與優先級；
- $G$ ：執行仲裁器；
- $a_t$ ：最終允許行動。

所以：

$$
\boxed{
\text{LLM says what may be useful;}
\quad
\text{runtime decides what may actually happen.}
}
$$

這個差異看似很小，卻改變了整個安全模型。

---

# 4. 五層控制架構

本文提出一個最小五層模型。

## 4.1 第一層：Safety Supervisor

這是最高優先級。

負責：

- 急停；
- 防碰撞；
- 防跌落；
- 力矩／速度上限；
- 地理圍欄；
- 危險區域；
- 人類接近保護；
- 硬體故障；
- 禁止動作。

其規則可以表示為：

$$
C_{\mathrm{safe}}(S_t,a_t)\in\{0,1\}.
$$

只有：

$$
C_{\mathrm{safe}}(S_t,a_t)=1
$$

的候選行動才可繼續。

對安全關鍵系統而言，更高級的版本還可以採用：

- Control Barrier Functions；
- formally verified safety functions；
- 獨立安全 PLC／MCU；
- 硬體 interlock。

2025 年 SAFER 研究即將 LLM 任務規劃與安全代理、Control Barrier Functions 結合，而不是假定 LLM 自身就足以提供物理安全保證。

## 4.2 第二層：Physical Reflex

這一層處理：

- 馬達控制；
- 姿態；
- 碰撞反射；
- 聲源轉向；
- 簡單追蹤；
- 立即停止；
- 基本 locomotion。

它的核心要求是：

$$
\tau_{\mathrm{reflex}}
\ll
\tau_{\mathrm{LLM}}.
$$

LLM 不應阻塞此層。

## 4.3 第三層：Finite State Machine

FSM 很適合表示清楚、互斥、可列舉的系統狀態。

例如機器人生命週期：

$$
Q=
\{
\text{Boot},
\text{Idle},
\text{Active},
\text{Charging},
\text{Fault},
\text{EmergencyStop}
\}.
$$

狀態轉移：

$$
\delta:Q\times E\rightarrow Q.
$$

例如：

$$
\text{Active}
\xrightarrow{\text{BatteryLow}}
\text{Charging},
$$

或：

$$
\text{AnyState}
\xrightarrow{\text{CriticalFault}}
\text{Fault}.
$$

這種狀態不應由 LLM 自由「生成」。

原因很簡單：

> 如果裝置現在處於 Fault，就應該真的處於 Fault，而不是模型認為「也許可以忽略這個 Fault」。

FSM 在這裡是一個物理與程序事實層。

---

# 5. FSM 的優點與極限

FSM 最大的優點是：

- 明確；
- 可視化；
- 可測試；
- 可形式驗證；
- 很容易知道「現在在哪一個狀態」。

對小型系統，若狀態數量仍然可控，它通常非常好用。

但如果所有高階行為都使用 FSM，就會出現大量交叉轉移。

例如：

- 掃地；
- 找人；
- 充電；
- 回應語音；
- 被觸摸；
- 門打開；
- 網路中斷；
- 主人叫名字；
- 低電量；
- 路被堵住。

每一個狀態都可能對每一個事件產生新的轉移，transition graph 會快速膨脹。

因此 FSM 最適合管理：

$$
\boxed{
\text{System Mode}
+
\text{Lifecycle}
+
\text{Hard Operational State}
}
$$

而不一定適合承載全部複雜任務邏輯。

---

# 6. 第四層：Behavior Tree

Behavior Tree（BT）適合把任務拆成：

- Sequence；
- Selector／Fallback；
- Condition；
- Action；
- Decorator。

例如家庭機器人的高階行為：

```text
ROOT
├─ Emergency?
│  └─ Stop
├─ BatteryLow?
│  └─ ReturnToCharger
├─ HumanCalling?
│  ├─ OrientToHuman
│  ├─ PauseCurrentTask
│  └─ Respond
└─ ContinueMission
```

它不是只問：

> 我現在是哪個唯一狀態？

而比較像持續問：

> 現在什麼行為具有最高適用性？它成功、失敗還是仍在執行？

因此 BT 天然適合：

- 可中斷任務；
- fallback；
- 行為重用；
- 任務樹；
- 局部修改；
- 多層優先級。

2025 年 IEEE T-ASE 的 FSM／BT 實證比較指出，兩者在完成任務的最終行為上可以等價，但隨任務複雜度增加，BT 的維護更容易。

這並不意味著：

$$
\text{BT}>\text{FSM}
$$

在所有情境都成立。

更合理的是：

$$
\boxed{
\text{FSM for state truth}
+
\text{BT for behavior composition}
}
$$

---

# 7. 第五層：LLM／VLM／VLA

現在才輪到大型模型。

大型模型最適合處理前四層不擅長的部分：

- 模糊自然語言；
- 未見過的組合問題；
- 高階語義判斷；
- 長期任務分解；
- 對環境的常識推理；
- 工具選擇；
- 生成新的候選計畫；
- 從人類模糊意圖推導具體目標。

例如：

> 「二白，房間有點亂，你看著辦。」

這種命令很難直接寫進 FSM。

LLM 可以把它轉換成：

```json
{
  "goal": "improve_room_order",
  "subgoals": [
    "inspect_floor",
    "identify_movable_clutter",
    "ask_for_permission_if_private_item",
    "move_safe_items_to_known_locations"
  ],
  "confidence": 0.78
}
```

接著由 Runtime 驗證每個 subgoal 是否：

- 有相應 skill；
- 符合目前權限；
- 具備前置條件；
- 沒有安全衝突；
- 可以映射到 BT 節點。

也就是：

$$
\text{LLM}
:
\text{Ambiguous Intent}
\rightarrow
\text{Structured Plan Proposal}.
$$

而不是：

$$
\text{LLM}
:
\text{Ambiguous Intent}
\rightarrow
\text{Raw Motor Torque}.
$$

---

# 8. 一個完整的權力鏈

現在可以寫出完整流程：

$$
\boxed{
\text{Human Intent}
\rightarrow
\text{LLM/VLM Interpretation}
\rightarrow
\text{Structured Proposal}
\rightarrow
\text{BT/FSM Integration}
\rightarrow
\text{Safety Validation}
\rightarrow
\text{Low-Level Controller}
\rightarrow
\text{Physical Effect}
}
$$

這裡每一層都縮小上一層的自由度。

可以把可行行動集合表示為：

$$
A_0
\supseteq
A_{\mathrm{skill}}
\supseteq
A_{\mathrm{state}}
\supseteq
A_{\mathrm{permission}}
\supseteq
A_{\mathrm{safe}}
\supseteq
A_{\mathrm{execute}}.
$$

LLM 最初可能提出大量候選：

$$
a\in A_0.
$$

經過一層層限制後，真正能執行的是：

$$
a^*\in A_{\mathrm{execute}}.
$$

這就是「智能」與「權限」的分離。

---

# 9. 世界狀態是所有層的共同接口

如果每一層各自維護一份世界，就會產生衝突。

例如：

- LLM 認為門是開的；
- FSM 記錄門是關的；
- 視覺模型剛剛看到門正在打開；
- 馬達控制器知道機器人此刻正高速移動。

因此所有層需要共享一個至少邏輯上統一的狀態表示：

$$
S_t=
(
S_t^{\mathrm{physical}},
S_t^{\mathrm{device}},
S_t^{\mathrm{task}},
S_t^{\mathrm{social}},
S_t^{\mathrm{memory}}
).
$$

每個模組只讀取自己需要的部分。

例如：

- Safety Supervisor 主要讀 $S_t^{\mathrm{physical}}$ ；
- FSM 主要讀 $S_t^{\mathrm{device}}$ ；
- BT 主要讀 $S_t^{\mathrm{task}}$ ；
- LLM 主要讀經壓縮後的 $S_t^{\mathrm{task}}+S_t^{\mathrm{social}}+S_t^{\mathrm{memory}}$ 。

所以 LLM 根本不需要每輪讀整個程式碼與所有 sensor raw data。

它只需要讀：

$$
\phi(S_t),
$$

其中 $\phi$ 是為高階推理生成的狀態投影。

這就是下一篇世界狀態機的直接入口。

---

# 10. 為什麼不能只靠 Prompt 約束？

一種常見做法是把所有安全規則寫進 System Prompt：

```text
你不能撞人。
你不能進入危險區域。
你必須在低電量時充電。
你不能在沒有授權時開門。
```

這種做法可以作為語義層提示，但不能當成最後防線。

原因在於：

$$
\text{Prompt Constraint}
\neq
\text{Execution Constraint}.
$$

Prompt 是模型推理上下文的一部分。

Execution constraint 則是：

$$
\text{if unsafe: reject}
$$

且無論模型說什麼都成立。

真正的安全條件應存在於模型外：

$$
G_{\mathrm{safe}}(S_t,p_t)
=
\begin{cases}
\text{ALLOW}, & C_{\mathrm{safe}}=1,\\
\text{DENY}, & C_{\mathrm{safe}}=0.
\end{cases}
$$

這個 gate 不能被自然語言說服。

---

# 11. 當模型與狀態機意見不同時，誰贏？

假設：

- LLM：建議繼續陪主人玩；
- FSM：BatteryCritical；
- Safety Runtime：只剩安全回充電量。

最終結果應該是：

$$
\text{BatteryCritical}
>
\text{Social Preference}.
$$

又例如：

- LLM：為了回答問題，建議靠近使用者；
- 感知：偵測到樓梯邊緣；
- Safety：禁止前進。

則：

$$
\text{Safety Stop}
>
\text{LLM Approach Proposal}.
$$

因此「更聰明」不意味著「優先級更高」。

這裡可以建立一條一般原則：

$$
\boxed{
\text{Authority is assigned by consequence, not intelligence.}
}
$$

一個非常簡單的 emergency stop 模組，其推理能力可能近乎為零，但它對馬達的否決權可以高於一個超大型模型。

---

# 12. LLM 可以修改行為樹嗎？

這是一個更有趣的進階問題。

答案可以是：

> 可以提出修改，但不應默認直接熱修改執行中的正式行為樹。

可以分為三種權限。

### Level 0：只選擇既有技能

$$
\text{LLM}
\rightarrow
\text{Skill ID}.
$$

最安全。

### Level 1：組合既有技能

$$
\text{LLM}
\rightarrow
\text{Temporary BT}.
$$

但所有節點必須來自白名單。

### Level 2：產生新技能／程式

$$
\text{LLM}
\rightarrow
\text{Code}
\rightarrow
\text{Test}
\rightarrow
\text{Sandbox}
\rightarrow
\text{Approval}
\rightarrow
\text{Deployment}.
$$

這已經不是一般即時控制，而是系統自我擴展。

因此，讓 LLM 「寫新的行為」與讓 LLM 「立刻執行新行為」必須分開。

---

# 13. 錯誤也需要分層處理

如果所有失敗都回傳給 LLM，系統會浪費大量推理。

可以建立：

$$
E=
\{
E_{\mathrm{control}},
E_{\mathrm{skill}},
E_{\mathrm{task}},
E_{\mathrm{semantic}},
E_{\mathrm{unknown}}
\}.
$$

例如：

### 控制錯誤

馬達過熱。

直接由底層處理：

$$
E_{\mathrm{control}}
\rightarrow
\text{Stop / Fault}.
$$

### 技能錯誤

抓取失敗一次。

BT 可以 fallback：

$$
\text{Grasp A Failed}
\rightarrow
\text{Try Grasp B}.
$$

### 任務錯誤

通往廚房的路被封住。

任務層重新規劃。

### 語義錯誤

「幫我收一下」到底要收什麼？

才交給 LLM 或人類 clarification。

因此：

$$
\boxed{
\text{Do not escalate every failure to the most expensive intelligence layer.}
}
$$

---

# 14. 分層控制並不否定端到端模型

這裡需要避免另一個極端。

RT-2、VLA 與端到端政策的價值非常真實：

- 可從資料學到複雜動作；
- 泛化到未見物體；
- 把高階語義與低階行為連接；
- 降低人工規則工程量。

本文不是主張：

$$
\text{Learning Control}
\rightarrow
\text{不要用}.
$$

而是主張：

$$
\boxed{
\text{Learned Policy}
\subset
\text{Governed Runtime}
}
$$

即使某個 learned policy 可以直接輸出動作，也可以讓它運行在安全 envelope、速度限制、空間限制、狀態限制、watchdog 與 emergency stop 之內。

端到端學習與分層治理並不矛盾。

---

# 15. 一個迷你陪伴機器人的實際架構

可以把整套東西壓縮成：

```text
                    ┌──────────────────┐
                    │ LLM / VLM / VLA  │
                    │ Reason / Propose │
                    └────────┬─────────┘
                             │
                      Structured Plan
                             │
                    ┌────────▼─────────┐
                    │ Behavior Tree    │
                    │ Task Arbitration │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │ State Machines   │
                    │ Mode / Lifecycle │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │ Safety Gate      │
                    │ Hard Constraints │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │ Local Controller │
                    │ MCU / Servo / PID│
                    └────────┬─────────┘
                             │
                          Actuator
```

旁邊有一個持續更新的：

```text
World State / Blackboard / Memory
```

提供各層讀寫。

這種設計有一個很實際的優點：

> 換模型，不必重寫整台機器人。

今天使用 3B 模型。

明天換 7B。

後天接雲端模型。

甚至完全離線。

只要模型輸出的 proposal schema 不變：

$$
\mathcal I_{\mathrm{LLM}}
=
\text{Stable Interface},
$$

底層具身系統仍然可以保持穩定。

---

# 16. 這也是「AI 原生狀態機」真正有價值的地方

傳統狀態機常被視為「舊式規則 AI」。

但在大型模型時代，它反而重新變得重要。

因為模型帶來的是：

$$
\text{open-ended intelligence}.
$$

而具身 Runtime 需要的是：

$$
\text{bounded execution}.
$$

兩者結合：

$$
\boxed{
\text{Open Intelligence}
+
\text{Bounded Action Space}
}
$$

才可能同時得到：

- 泛化；
- 自主性；
- 可控性；
- 低延遲；
- 可測試性；
- 穩定角色；
- 可持續世界狀態。

所以未來真正高階的 AI 系統，不一定會「消滅狀態機」。

更可能是：

> AI 讓狀態機從手工寫死的唯一智能來源，轉變為大型智能之下的執行秩序層。

---

# 17. 從「控制分工」走向「世界狀態機」

完成這篇後，下一個問題幾乎不可避免。

如果 Safety Supervisor、FSM、Behavior Tree、LLM 與感知模型都需要知道「現在發生什麼」，那麼就不能讓每一層各自重新猜一次世界。

應該存在：

$$
S_t
$$

作為共同狀態。

然後：

$$
S_{t+1}=F(S_t,E_t,A_t).
$$

也就是：

> 世界不是每輪重新生成，而是持續演化。

這正是第 4 篇的核心：

**《從狀態機到世界狀態機：AI 為何不應每輪重新理解世界》**

---

# 18. 結論

大型模型進入機器人，不代表所有舊式控制架構都變得沒有必要。

恰恰相反。

模型能力越開放，越需要一個能把它的自由度安全映射到物理世界的 Runtime。

本文的核心架構可以壓縮為：

$$
\boxed{
\text{LLM Proposal}
\rightarrow
\text{Behavior Composition}
\rightarrow
\text{State Validation}
\rightarrow
\text{Safety Arbitration}
\rightarrow
\text{Physical Execution}
}
$$

其中：

- LLM 負責不知道的；
- BT 負責怎麼組合；
- FSM 負責現在是什麼狀態；
- Safety 負責什麼絕對不能做；
- Controller 負責如何準確地做。

最重要的一句是：

$$
\boxed{
\text{模型可以是最聰明的一層，
但不必是權力最大的一層。}
}
$$

這不是降低 AI 的自主性。

而是把「智能」與「執行權」從同一個概念中拆開，使自主系統真正可以長時間存在於一個會造成後果的物理世界。

---

# 參考資料

1. Driess, D. et al. (2023). *PaLM-E: An Embodied Multimodal Language Model*. ICML 2023, PMLR 202:8469–8488.  
   https://proceedings.mlr.press/v202/driess23a.html

2. Zitkovich, B. et al. (2023). *RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control*. Conference on Robot Learning 2023, PMLR 229:2165–2183.  
   https://proceedings.mlr.press/v229/zitkovich23a.html

3. Ghzouli, R. et al. (2022). *Behavior Trees and State Machines in Robotics Applications*.  
   https://arxiv.org/abs/2208.04211

4. Iovino, M. et al. (2025). *Comparison Between Behavior Trees and Finite State Machines*. IEEE Transactions on Automation Science and Engineering.  
   DOI: https://doi.org/10.1109/TASE.2025.3610090

5. Iovino, M. et al. (2022). *On the programming effort required to generate Behavior Trees and Finite State Machines for robotic applications*.  
   https://arxiv.org/abs/2209.07392

6. Khan, A. A. et al. (2025). *Safety Aware Task Planning via Large Language Models in Robotics (SAFER)*.  
   https://arxiv.org/abs/2503.15707

7. Benjumea, D. C., Farrell, M., & Dennis, L. A. (2025). *Safe-ROS: An Architecture for Autonomous Robots in Safety-Critical Domains*.  
   https://arxiv.org/abs/2511.14433

8. Mu, Y. et al. (2023). *EmbodiedGPT: Vision-Language Pre-Training via Embodied Chain of Thought*.  
   https://arxiv.org/abs/2305.15021
