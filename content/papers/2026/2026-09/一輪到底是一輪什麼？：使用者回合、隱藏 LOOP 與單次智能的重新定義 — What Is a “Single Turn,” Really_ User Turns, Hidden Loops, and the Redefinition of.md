# 一輪到底是一輪什麼？：使用者回合、隱藏 LOOP 與單次智能的重新定義

## What Is a “Single Turn,” Really? User Turns, Hidden Loops, and the Redefinition of Single-Pass Intelligence

**系列：**《智能的物理計量：從最小語意執行到成果品質與計算時空》  
**英文系列：** *Physical Metrology of Intelligence: From Minimal Semantic Execution to Quality and Computational Spacetime*  
**系列編號：** EML-IPM  
**篇次：** Paper 01 / 10  
**文件編號：** EML-IPM-01  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開純理論論文

---

## 摘要

當代 AI 評測與產品敘事經常使用「一輪完成」「one-shot」「single turn」描述能力，但這些詞在介面、Agent、模型推理與物理計算層面不是同一件事。

使用者只輸入一次：

$$
U_1\rightarrow A_1
$$

背後仍可能實際展開為：

$$
M_1\rightarrow Tool_1\rightarrow M_2\rightarrow Verifier_1
\rightarrow M_3\rightarrow\cdots\rightarrow M_n.
$$

因此：

$$
\boxed{
\text{One User Turn}
\neq
\text{One Model Invocation}
\neq
\text{One Generation Trajectory}
\neq
\text{One Agent Loop}
\neq
\text{One Physical Computation}.
}
$$

本文提出 **AI 回合分解框架（Turn Decomposition Framework）**：

$$
\boxed{
\mathcal T=(U,G,I,L,R,S,P)
}
$$

其中：

- $U$：User Interaction Turns；
- $G$：Generation Trajectories；
- $I$：Model Invocations；
- $L$：External Feedback Loops；
- $R$：Retries / Rollouts；
- $S$：Selection / Verification；
- $P$：Physical Execution Trace。

本文認為「一輪」最大的概念錯誤，是把：

$$
\boxed{
\text{Interaction Compression}
}
$$

誤認為：

$$
\boxed{
\text{Computation Compression}.
}
$$

當 300 次內部 Agent 互動被藏進一個聊天泡泡裡，使用者確實只互動一次，但物理世界並沒有只計算一次。

本文進一步定義 **Externally Loopless Intelligence（ELI，外部無迴圈智能）**：在一個任務執行期間，系統不能根據外部世界、工具輸出、獨立 verifier、另一候選答案或 retry 結果重新修正求解方向。

這不表示模型內部沒有時間序列。自回歸模型仍然：

$$
y_1\rightarrow y_2\rightarrow\cdots\rightarrow y_n.
$$

所以：

$$
\boxed{
\text{No External Loop}
\neq
\text{No Sequential Computation}.
}
$$

真正被排除的是：

$$
\boxed{
\text{Action}
\rightarrow
\text{New Evidence}
\rightarrow
\text{Replanning}.
}
$$

本文將最乾淨的單次成果記為：

$$
\boxed{
\mathcal X_{SP}:x
\xrightarrow[\text{no external feedback}]{\tau}
y.
}
$$

最後建立後續 IPM 系列共用事件向量：

$$
\boxed{
\mathfrak E=
(Q,U,G,I,L,R,S,T,E,V_{CST})
}
$$

其中 $Q$ 是成果品質， $T$ 是實際時間， $E$ 是能源， $V_{CST}$ 是 Computational Spacetime Volume。

因此，真正值得問的已不再是：

> AI 是否「一輪」完成？

而是：

$$
\boxed{
\textbf{
這個成果是在幾次互動、幾條生成軌跡、幾層 LOOP、
多少計算時空與多少物理能源下產生的？
}
}
$$

---

# 1. User Turn 是介面單位，不是智能單位

最表面的「一輪」是：

$$
U=1.
$$

它只代表使用者：

- 輸入一次；
- submit 一次；
- 接收一次結果。

因此 User Turn 本質上是：

$$
\boxed{
\text{UX event}.
}
$$

它沒有告訴我們背後到底發生多少計算。

---

# 2. 一個 User Turn 可以包含大量 Model Invocation

定義：

$$
I=\text{Model Invocation Count}.
$$

可能：

$$
U=1,\quad I=1,
$$

也可能：

$$
U=1,\quad I=300.
$$

所以：

$$
\boxed{
U=1\not\Rightarrow I=1.
}
$$

---

# 3. Model Invocation 也不是物理計算原子

即使：

$$
I=1,
$$

仍可能有：

- 長 context；
- 大模型；
- MoE routing；
- 多 GPU；
- 大量 memory traffic；
- 很長的自回歸生成。

因此：

$$
\boxed{
I=1\not\Rightarrow P=1.
}
$$

---

# 4. Generation Trajectory 必須獨立計數

定義：

$$
G=\text{Generation Trajectory Count}.
$$

如果同一題生成：

$$
\tau_1,\tau_2,\ldots,\tau_{16}
$$

再選一個最好結果，那：

$$
G=16.
$$

即使最後只顯示一個回答。

所以：

$$
\boxed{
\text{One Visible Answer}
\neq
\text{One Generated Candidate}.
}
$$

---

# 5. Rollout 與 Pass@k 不能混入 Pass@1

若單次成功率為：

$$
p,
$$

允許 $k$ 次獨立 rollout，至少成功一次的機率為：

$$
\boxed{
1-(1-p)^k.
}
$$

例如：

$$
p=0.2,\quad k=16,
$$

則至少成功一次約為：

$$
1-(0.8)^{16}\approx0.972.
$$

因此：

$$
\boxed{
Pass@1\neq Pass@16.
}
$$

以及：

$$
\boxed{
BestOfN\neq MedianUserExperience.
}
$$

---

# 6. Selection 本身就是額外能力來源

若先生成：

$$
Y_1,\ldots,Y_n
$$

再透過 judge / verifier 選出：

$$
Y^\ast,
$$

那最終品質是：

$$
\boxed{
Q_{\text{final}}
=
F(
Q_{\text{generation distribution}},
Q_{\text{selection}}
).
}
$$

它不是單一生成軌跡的能力。

---

# 7. LOOP 的真正定義不是「多講幾次」

本文把 External Feedback Loop 定義為：

$$
\boxed{
State_t
\rightarrow
Action_t
\rightarrow
NewEvidence_{t+1}
\rightarrow
State_{t+1}.
}
$$

核心是：

$$
\boxed{
\text{新資訊重新進入求解狀態}.
}
$$

---

# 8. Tool Loop

例如：

$$
Model
\rightarrow
Search
\rightarrow
Evidence
\rightarrow
Model.
$$

或：

$$
Code
\rightarrow
Run
\rightarrow
Error
\rightarrow
Fix.
$$

都屬於外部 LOOP。

---

# 9. Verifier Loop

$$
Draft
\rightarrow
Verifier
\rightarrow
Critique
\rightarrow
Revision.
$$

這也不是 single-pass。

---

# 10. Retry Loop

$$
Failure
\rightarrow
Restart.
$$

新的 trajectory 從頭再來，也是一種外部鷹架增益。

---

# 11. Candidate Loop

$$
GenerateMany
\rightarrow
Compare
\rightarrow
Choose.
$$

即使沒有修改候選，也已經增加了系統層能力。

---

# 12. LOOP Taxonomy

本文第一版分類：

$$
\boxed{
\mathbf L=
(L_T,L_E,L_V,L_R,L_C)
}
$$

其中：

- $L_T$：Tool Loop；
- $L_E$：Environment Loop；
- $L_V$：Verifier Loop；
- $L_R$：Retry Loop；
- $L_C$：Candidate / Selection Loop。

它們之後都應獨立計價。

---

# 13. 自回歸生成本身不是本文要排除的 LOOP

Transformer 仍然逐步產生：

$$
P(y_t\mid x,y_{<t}).
$$

所以物理上當然有時間序列。

但若沒有新的外部證據進入：

$$
\boxed{
\text{Internal Sequential Generation}
\neq
\text{External Feedback Loop}.
}
$$

否則「No-Loop」會荒謬地變成「只准做一次矩陣乘法」。

---

# 14. Externally Loopless Intelligence

本文因此使用：

$$
\boxed{
ELI=
\text{Externally Loopless Intelligence}.
}
$$

ELI 禁止：

1. tool 回傳新證據；
2. environment re-observation；
3. retry；
4. parallel rollout；
5. independent verifier critique；
6. best-of-N；
7. 完整候選產生後再重新生成。

但允許同一 trajectory 內部的自回歸與 latent computation。

---

# 15. 最乾淨的 Single-Pass 條件

本文暫定：

$$
\boxed{
U=1,\quad
G=1,\quad
R=1,\quad
L=0,\quad
S=0.
}
$$

這才接近日常語言真正想表達的：

> 一次直接生成。

---

# 16. Interaction Compression

Agent 產品可以把大量內部工作壓縮成一次使用者互動。

定義：

$$
\boxed{
C_U=
\frac{N_{\text{internal interactions}}}{U}.
}
$$

若：

$$
C_U\gg1,
$$

代表產品替使用者吸收了大量操作負擔。

這是很好的 UX。

---

# 17. 但 Interaction Compression 不是 Computation Compression

若 300 次工作被藏在一個 UI turn：

$$
U=1,
$$

仍不能推出：

$$
Computation=1.
$$

所以：

$$
\boxed{
\text{Interaction Compression}
\neq
\text{Computation Compression}.
}
$$

這是 IPM 系列第一條核心原則。

---

# 18. Scaffolding Separation Principle

系統成果可以表示為：

$$
\boxed{
Q_{\text{system}}
=
F(
M,
L,
Tool,
R,
S,
Env
).
}
$$

其中 $M$ 是模型本身能力。

因此：

$$
\boxed{
Q_{\text{system}}
\neq
Q_M.
}
$$

高品質 Agent 系統不等於底層模型 single-pass 也同樣強。

---

# 19. 四種能力層必須分開

本文區分：

$$
\boxed{
C_{\text{intrinsic}}
}
$$

模型在最小鷹架下的能力；

$$
\boxed{
C_{\text{elicited}}
}
$$

透過 prompt、context、reasoning budget 被引出的能力；

$$
\boxed{
C_{\text{system}}
}
$$

加入 tool、memory、loop、verifier 後的能力；

$$
\boxed{
C_{\text{product}}
}
$$

最終受到 UI、policy、quota、latency 等限制後的使用者能力。

所以：

$$
\boxed{
C_{\text{benchmark}}
\neq
C_{\text{user}}.
}
$$

---

# 20. LOOP 不是作弊

本文並不反對 LOOP。

有些問題本體就需要：

$$
Action
\rightarrow
World
\rightarrow
Observation
\rightarrow
Replan.
$$

例如：

- debugging；
- 科學實驗；
- 機器人控制；
- 即時搜尋；
- 動態決策。

真正的錯誤只是：

$$
\boxed{
\text{Loop-Assisted Capability}
}
$$

被描述成：

$$
\boxed{
\text{Single-Pass Capability}.
}
$$

---

# 21. Single-Pass Intelligence 與 Loop Intelligence

因此至少需要兩條軸：

$$
\boxed{
I_{SP}
=
\text{Single-Pass Intelligence}
}
$$

以及：

$$
\boxed{
I_L
=
\text{Loop Intelligence}.
}
$$

 $I_{SP}$ 問：

> 沒有外部重新餵答案時，第一條求解軌跡能直接做多好？

 $I_L$ 問：

> 得到新證據之後，系統能不能有效修正？

真正強大的系統可能：

$$
\boxed{
I_{SP}\uparrow+I_L\uparrow.
}
$$

但兩者不能被一個 benchmark 分數混掉。

---

# 22. 物理世界還有第三種「一輪」

從任務開始 $t_0$ 到結果完成 $t_f$，所有被此任務因果占用的物理計算資源形成：

$$
\boxed{
\mathcal P_{\text{task}}
=
\{resource(t)\mid t_0\le t\le t_f\}.
}
$$

這可以叫：

$$
\boxed{
\text{Physical Execution Episode}.
}
$$

它才接近物理世界真正付出的「一輪」。

---

# 23. Physical Execution 至少包含

$$
\boxed{
P=
(
Ops,
Memory,
Interconnect,
Device,
Time,
Energy
).
}
$$

因此：

$$
\boxed{
\text{Physical Turn}
\neq
\text{UI Turn}.
}
$$

---

# 24. Computational Spacetime Volume

若一個任務使用：

$$
8\ GPU\times10s,
$$

粗略 hardware-time volume 為：

$$
80\ GPU\cdot s.
$$

另一任務使用：

$$
1\ GPU\times80s
$$

也可能是：

$$
80\ GPU\cdot s.
$$

但 latency 不同。

因此 $V_{CST}$ 與 $T$ 必須同時保留。

---

# 25. 不要太早壓成單一分數

智能計量更應先保留 Pareto 結構：

$$
\boxed{
Q\uparrow,
\qquad
E\downarrow,
\qquad
T\downarrow,
\qquad
V_{CST}\downarrow,
\qquad
L,R,S\downarrow.
}
$$

如果 A 在所有軸都更好，才有明確 dominance。

若各有優劣，就保留 trade-off。

---

# 26. 統一事件向量

本文最終定義：

$$
\boxed{
\mathfrak E=
(
Q,
U,
G,
I,
\mathbf L,
R,
S,
T,
E,
V_{CST}
).
}
$$

未來任何聲稱「一輪完成」的系統，至少都可以投影到這個事件向量。

---

# 27. 一個簡單比較

假設：

### System A

$$
\mathfrak E_A=
(
0.95,
1,
1,
1,
0,
1,
0,
5s,
E_A,
V_A
).
$$

### System B

$$
\mathfrak E_B=
(
0.95,
1,
16,
48,
30,
16,
1,
120s,
E_B,
V_B
).
$$

兩者：

$$
Q_A=Q_B,
\qquad
U_A=U_B=1.
$$

從聊天介面看完全可以都叫「一輪完成」。

但：

$$
\boxed{
\mathfrak E_A\neq\mathfrak E_B.
}
$$

甚至可能具有幾個數量級不同的智能物理效率。

---

# 28. 十二個 Canonical Invariants

**Invariant 1**

$$
\boxed{
UserTurn\neq PhysicalTurn.
}
$$

**Invariant 2**

$$
\boxed{
UserTurn\neq ModelInvocation.
}
$$

**Invariant 3**

$$
\boxed{
ModelInvocation\neq GenerationTrajectory.
}
$$

**Invariant 4**

$$
\boxed{
GenerationTrajectory\neq ExternalLoop.
}
$$

**Invariant 5**

$$
\boxed{
SingleInteraction\neq SinglePassIntelligence.
}
$$

**Invariant 6**

$$
\boxed{
NoExternalLoop\neq NoSequentialComputation.
}
$$

**Invariant 7**

$$
\boxed{
Pass@k\neq Pass@1.
}
$$

**Invariant 8**

$$
\boxed{
BestOfN\neq MedianExperience.
}
$$

**Invariant 9**

$$
\boxed{
SystemCapability\neq ModelNativeCapability.
}
$$

**Invariant 10**

$$
\boxed{
InteractionCompression\neq ComputationCompression.
}
$$

**Invariant 11**

$$
\boxed{
SameFinalQuality\neq SameIntelligenceEfficiency.
}
$$

**Invariant 12**

$$
\boxed{
TokenCount\neq PhysicalComputationCost.
}
$$

---

# 29. 結論：一個聊天泡泡不是智能的自然單位

「一輪」長期造成混亂，是因為同一詞被同時拿來描述：

- 使用者操作；
- Agent 執行；
- 模型呼叫；
- 自回歸生成；
- 物理資源消耗。

如果使用者只輸入一次：

$$
U=1,
$$

我們最多只能說：

> 這是 single-interaction UX。

不能直接推出：

> 這是 single-pass intelligence。

如果系統在背後搜尋、執行、驗證、重試、生成多個候選，再挑出最好的一個，那麼：

$$
\boxed{
U=1
}
$$

只是介面壓縮。

真正的：

$$
L,R,S,V_{CST},E
$$

仍然可能很大。

因此 IPM 系列從第一篇開始拒絕把聊天 UI 當成智能計量單位。

真正應被記錄的是：

$$
\boxed{
\mathfrak E=
(
Q,
U,
G,
I,
\mathbf L,
R,
S,
T,
E,
V_{CST}
).
}
$$

而如果我們想知道：

> **拿掉 LOOP 後，模型自己還剩多少智能？**

就必須先把條件壓到：

$$
\boxed{
U=1,\quad
G=1,\quad
R=1,\quad
L=0,\quad
S=0,
}
$$

再測：

$$
Q_{SP}.
$$

但這仍不是終點。

因為即使我們成功隔離出一條 single-pass trajectory，仍然沒有回答：

> 這條軌跡裡，AI 究竟「算了多少次智能」？

Token 不能回答。

FLOP 也不能回答。

所以 Paper 02 必須進入整套 IPM 最困難的問題：

$$
\boxed{
\textbf{
智能到底算了一次什麼？
}
}
$$

也就是：

$$
\boxed{
\mu_I
=
\text{Minimum Intelligent Semantic Execution Unit}.
}
$$

---

## 系列路徑

1. **Paper 01｜一輪到底是一輪什麼？：使用者回合、隱藏 LOOP 與單次智能的重新定義**  
2. **Paper 02｜智能到底算了一次什麼？：最小智能語意執行單位的候選理論**  
3. **Paper 03｜從認知到神經元：人腦如何跨層測量智能計算**  
4. **Paper 04｜從神經元到焦耳：智能計算的能量、熱力學與物理下界**  
5. **Paper 05｜計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積**  
6. **Paper 06｜成果品質到底怎麼量？：從形式化正確性到結構化智能品質**  
7. **Paper 07｜不要叫人類替自己的感覺打分數：IBQF 二元測量與低負擔品質評估**  
8. **Paper 08｜自然語言、圖像與創意如何被量？：高歧義成果的結構化品質空間**  
9. **Paper 09｜拿掉 LOOP 還剩多少智能？：單次智能、鷹架依賴與隱藏計算成本**  
10. **Paper 10｜一個答案值多少物理世界？：智能產率的統一計量框架**
