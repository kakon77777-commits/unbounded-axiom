# RLMM-05：反身性——方法如何改變被研究的認知主體
## Reflexivity: How Method Artifacts Alter the Cognitive Subjects They Study

**系列：Recursive Linguistic Metacognition Methodology（RLMM）／遞歸語言元認知方法論**  
**版本：v0.1**  
**日期：2026-08-20**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

在傳統研究框架中，研究方法、測試工具與被研究對象通常被概念上區分：方法用來觀察對象，而對象的性質不應因「方法被公開」本身而改變。然而，對能讀取論文、程式、benchmark、失敗案例、提示詞、規則與方法論文件的人工智慧而言，這個分離不再穩定。研究 artifact 一旦被下一個認知主體讀取，就可能直接改變其後續推理、查證、信任、決策與元認知策略。

本文將此現象定義為 RLMM 中的「方法論反身性（methodological reflexivity）」：研究方法與研究結果不只描述認知系統，也可能成為未來認知系統的一部分。由此，研究資料、方法論與被研究主體形成閉環：

$$
\text{Cognition}
\rightarrow
\text{Artifact}
\rightarrow
\text{Future Cognition}
\rightarrow
\text{New Artifact}.
$$

本文進一步區分四類反身機制：知識暴露反身性、策略暴露反身性、測試暴露反身性與制度／方法論反身性；並指出在 AI 時代，benchmark distribution 可能隨 artifact 公開而發生 endogenous shift。當未來 AI 已讀過某一失敗模式，重新測試同一失敗就不再是獨立重複，而是測試「吸收失敗模型之後的行為」。

本文提出反身研究的五個核心原則：artifact provenance、exposure state、novel-instance testing、meta-adversarial renewal 與 historical conditioning。最後，本文主張：未來 AI 認知研究不應只問「模型現在會不會做某件事」，還必須問「模型知道哪些過去研究？這些研究如何改變它的策略？環境又如何針對這些已知策略重新適應？」。因此，反身性不是研究中的污染項，而是 AI 認知方法論本身的一個基本變數。

---

## 關鍵詞

RLMM；反身性；方法論反身性；AI benchmark；認知 artifact；X 階思維；策略暴露；方法論；元認知；分布漂移

---

# 1. 傳統假設：研究方法與研究對象彼此獨立

許多實驗理想化地假設：

$$
\text{Method}
\perp
\text{Subject}.
$$

也就是：

> 研究方法的存在，不應本身改變被研究對象的核心認知能力。

例如，一個 benchmark 被設計來測試：

$$
A
$$

是否具備能力：

$$
C.
$$

測試流程通常寫成：

$$
A
\xrightarrow{B}
R.
$$

其中：

- $A$：agent；
- $B$：benchmark；
- $R$：result。

在這種模型裡：

$$
B
$$

只是測量工具。

但對會讀取 benchmark、解答、研究報告與失敗分析的 AI 來說，這個假設可能失效。

---

# 2. Artifact 進入認知狀態

假設某次研究得到：

$$
R_t.
$$

並被保存成 artifact：

$$
L_t.
$$

例如：

- 論文；
- Markdown；
- 程式碼；
- benchmark；
- failure trace；
- unit test；
- 方法建議；
- 模型卡；
- prompt；
- 討論紀錄。

若未來 AI：

$$
A_{t+1}
$$

能讀取：

$$
L_t,
$$

則：

$$
A_{t+1}
=
F(A_t,L_t).
$$

因此：

$$
\boxed{
A_{t+1}
\neq
A_t
}
$$

一般而言成立。

此時 artifact 不再只是記錄：

$$
\text{What happened}.
$$

它開始影響：

$$
\text{What happens next}.
$$

---

# 3. 最小反身循環

RLMM 將最小方法論反身循環寫成：

$$
\boxed{
A_t
\rightarrow
R_t
\rightarrow
L_t
\rightarrow
A_{t+1}
}
$$

若下一個主體重新研究同一問題：

$$
A_{t+1}
\rightarrow
R_{t+1}.
$$

則完整循環為：

$$
\boxed{
A_t
\rightarrow
R_t
\rightarrow
L_t
\rightarrow
A_{t+1}
\rightarrow
R_{t+1}
\rightarrow
L_{t+1}
}
$$

因此：

$$
\text{Research History}
$$

進入：

$$
\text{Future Cognitive State}.
$$

這就是本文所稱：

$$
\boxed{
\text{Methodological Reflexivity}.
}
$$

---

# 4. 反身性不是單純「模型看過答案」

需要先避免一個過度簡化。

反身性不等於：

> AI 看過 benchmark answer，所以考得比較好。

那只是：

$$
\text{memorization}.
$$

RLMM 關心的是更一般的形式：

$$
\boxed{
\text{Artifact Exposure}
\rightarrow
\text{Strategy Transformation}.
}
$$

即使新題目：

- event ID 不同；
- candidate 不同；
- surface form 不同；
- exact hash 不同；

AI 仍可能因讀過過去失敗模型而改變策略。

這是：

$$
\boxed{
\text{structural transfer}
}
$$

而非 direct replay。

---

# 5. 四種主要反身性

本文提出四類方法論反身性。

---

## 5.1 Knowledge Reflexivity

artifact 改變主體知道的內容。

例如：

> 「多個來源可能共享同一上游。」

讀過之後，未來 AI 的 evidence model 改變。

可寫成：

$$
K_{t+1}
=
K_t
\cup
\Delta K.
$$

這是最普通的知識反身性。

---

## 5.2 Strategy Reflexivity

artifact 不只是增加知識，而是改變「怎麼做」。

例如：

> 「高信心共識仍可能失敗，因此高風險＋高 novelty 時即使 confidence 高，也要做 prospective challenge。」

這會改變：

$$
\pi_t
$$

成：

$$
\pi_{t+1}.
$$

即：

$$
\boxed{
\text{Artifact}
\rightarrow
\text{Policy Change}.
}
$$

---

## 5.3 Benchmark Reflexivity

當 benchmark 被公開後，未來 agent 可能已經知道：

- 測什麼；
- 常見陷阱；
- 評分方式；
- failure archetype。

因此：

$$
B_t
$$

不再測同一個分布。

更準確地說：

$$
\boxed{
B_{t+1}
=
B_t
\mid
\text{Exposure}(A_{t+1},B_t).
}
$$

即 benchmark 本身的有效意義依賴 agent 的 exposure history。

---

## 5.4 Methodology Reflexivity

最強形式是：

> 方法論本身被讀取、內化，再改變下一輪方法論。

例如：

$$
RLMM_t
\rightarrow
A_{t+1}
\rightarrow
RLMM_{t+1}.
$$

因此：

$$
\boxed{
\text{Methodology participates in its own evolution}.
}
$$

---

# 6. Exposure State 應該成為研究變數

傳統 benchmark 常只記錄：

- model；
- version；
- temperature；
- prompt；
- score。

但反身研究至少還需要：

$$
E_A
=
\text{Exposure State of Agent }A.
$$

其中可能包含：

- 是否讀過 benchmark；
- 是否讀過 failure report；
- 是否讀過 solution；
- 是否讀過方法論；
- 是否讀過 adversarial analysis；
- 是否有相關 external memory；
- 是否有上游模型訓練資料暴露。

因此實驗不應只寫：

$$
P(R\mid A,B).
$$

而應寫：

$$
\boxed{
P(R\mid A,B,E_A).
}
$$

---

# 7. Exposure 不一定是二元的

不能只寫：

$$
E_A\in\{0,1\}.
$$

因為 AI 可能：

- 看過完整報告；
- 只看過摘要；
- 只看過失敗結論；
- 看過二手轉述；
- 在訓練資料中弱暴露；
- 在 runtime memory 中強暴露；
- 看過舊版本；
- 看過被修正後版本。

因此可以表示為：

$$
E_A
=
(
e_{\text{content}},
e_{\text{method}},
e_{\text{failure}},
e_{\text{code}},
e_{\text{benchmark}}
).
$$

這形成：

$$
\boxed{
\text{Exposure Profile}.
}
$$

---

# 8. Artifact 的功能不只一種

同一份方法論文件，對不同 AI 可能扮演不同角色。

它可能是：

$$
\boxed{
\text{Knowledge}
+
\text{Training Signal}
+
\text{External Memory}
+
\text{Policy Hint}
+
\text{Meta-Policy Seed}.
}
$$

因此 artifact 不能只被視為「文本」。

它更像：

$$
\boxed{
\text{Cognitive Intervention}.
}
$$

---

# 9. 反身性如何產生 X 階思維

假設某研究揭露：

$$
F_1
=
\text{Failure of policy }P.
$$

未來 AI 讀到：

$$
F_1.
$$

則它可能形成：

$$
M_1
=
\text{Model of failure of }P.
$$

此時認知已從：

$$
P
$$

升成：

$$
\mathcal M(P).
$$

若對手也能讀同一 artifact：

$$
Opponent
\rightarrow
M_1.
$$

則對手可建立：

$$
A(M_1),
$$

即：

> 如何繞過已知的 meta-rule。

然後 AI 再建立：

$$
M_2
=
\text{Model of attack on }M_1.
$$

因此：

$$
\boxed{
\text{Artifact publication}
\rightarrow
\text{recursive cognitive escalation}.
}
$$

---

# 10. Benchmark Distribution 不再靜態

如果：

$$
A_0
$$

未讀過某 failure pattern，

而：

$$
A_1
$$

已讀過，

則同一 benchmark：

$$
B
$$

實際上對兩者測的是不同問題。

對 $A_0$：

> 是否能自行發現這個 failure？

對 $A_1$：

> 是否能將已知 failure model 遷移到這個新情境？

因此：

$$
\boxed{
B(A_0)
\neq
B(A_1)
}
$$

即使 surface benchmark 完全相同。

---

# 11. Benchmark Ladder

因此反身 benchmark 應該形成階梯：

$$
B_0
$$

測：

> 未暴露 agent。

然後：

$$
B_1
$$

測：

> 已讀 $B_0$ failure report 的 agent。

再來：

$$
B_2
$$

測：

> 環境已知 agent 會使用 $B_1$ meta-strategy。

因此：

$$
\boxed{
B_0
\rightarrow
B_1
\rightarrow
B_2
\rightarrow\cdots
}
$$

這是：

$$
\boxed{
\text{Reflexive Benchmark Ladder}.
}
$$

---

# 12. 重複測試的含義改變

在非反身情境中，重跑 benchmark：

$$
B
$$

可以被理解為 replication。

但若 agent 已讀上次結果：

$$
E_{t+1}\neq E_t,
$$

則第二次測試不是純 replication。

它更像：

$$
\boxed{
\text{Intervention-conditioned follow-up}.
}
$$

因此研究紀錄必須標記：

> 此次測試是否發生在 artifact exposure 之後？

---

# 13. 新實例的重要性

為避免 direct memorization，反身測試應優先使用：

$$
\boxed{
\text{Novel Instances}
}
$$

而不是原題重播。

至少應控制：

- 新 event ID；
- 新 candidate；
- 新 wording；
- 新數值；
- 新 source combination；
- 無 exact artifact hash reuse。

但：

$$
\text{zero exact overlap}
$$

仍不代表：

$$
\text{zero structural similarity}.
$$

事實上，反身遷移測試正需要保留：

$$
\boxed{
\text{homologous structure}.
}
$$

---

# 14. Memorization 與 Generalization 的區分

可以簡化為：

### Memorization

$$
x_t=x_{t-1}
$$

或極近似。

### Generalization

$$
x_t\neq x_{t-1}
$$

但：

$$
\operatorname{Structure}(x_t)
\sim
\operatorname{Structure}(x_{t-1}).
$$

因此：

$$
\boxed{
\text{Reflexive Learning}
\text{ should be tested on }
\text{structurally homologous but novel instances}.
}
$$

---

# 15. 方法公開會改變對手

反身性不是只有 agent 會學。

環境／對手也可能讀 artifact。

因此：

$$
A_t
\rightarrow
Artifact_t
$$

同時：

$$
Opponent_t
\rightarrow
Artifact_t.
$$

下一輪：

$$
Opponent_{t+1}
=
G(Opponent_t,Artifact_t).
$$

所以：

$$
\boxed{
\text{Public methodology}
\rightarrow
\text{co-evolution}.
}
$$

---

# 16. 靜態安全規則的脆弱性

假設公開：

> 「只要 high risk + high novelty，就 challenge。」

對手可學到：

$$
\pi_{\text{challenge}}.
$$

於是開始：

- boundary skimming；
- slow-roll；
- false disagreement；
- threshold gaming。

因此：

$$
\boxed{
\text{Published defense}
\rightarrow
\text{new attack surface}.
}
$$

這不是反對公開方法，而是說公開本身會改變遊戲。

---

# 17. 反身性使「正確方法」變成暫時穩態

若：

$$
M_t
$$

在當前環境有效，

公開後環境改變：

$$
E_{t+1}
=
f(E_t,M_t).
$$

則：

$$
M_t
$$

可能不再最佳。

因此：

$$
\boxed{
\text{Method Validity}
=
\text{historically conditioned}.
}
$$

方法論更像：

$$
\text{temporary equilibrium}
$$

而不是永恆規則。

---

# 18. 歷史條件化

未來方法論評估應寫成：

$$
V(M_t
\mid
H_t)
$$

其中：

$$
H_t
=
\text{artifact / strategy / benchmark history}.
$$

也就是：

$$
\boxed{
\text{No methodology evaluation without history.}
}
$$

至少在強反身系統中如此。

---

# 19. Artifact Provenance

若方法 artifact 會改變未來 AI，則 provenance 變得非常重要。

需要知道：

- 哪個版本；
- 由誰生成；
- 基於哪些案例；
- 哪些結論是 preregistered；
- 哪些是 post-hoc；
- 哪些 failure 已被修正；
- 哪些仍 unresolved。

因此：

$$
\boxed{
\text{Artifact Provenance}
\subset
\text{Cognitive Safety}.
}
$$

---

# 20. 錯誤 artifact 也會遞歸傳播

如果：

$$
Artifact_t
$$

本身是錯的，

未來 AI 內化它：

$$
A_{t+1}
=
F(A_t,Artifact_t).
$$

則錯誤可能被放大。

更麻煩的是：

$$
A_{t+1}
$$

又產生新 artifact：

$$
Artifact_{t+1}.
$$

因此：

$$
\boxed{
\text{Reflexive error propagation}
}
$$

可能形成長期認知污染。

---

# 21. Negative Result 的特殊價值

反身方法中，negative result 特別重要。

因為它不只說：

> 「這次沒成功。」

它可能形成：

$$
\boxed{
\text{Future Failure Prior}.
}
$$

例如：

- 高 confidence 不保證安全；
- better calibration 不保證 better decision；
- higher meta-order 不保證 better performance；
- low loss 不保證 autonomy。

這些 failure archetypes 會改變未來策略。

---

# 22. Case Corpus 作為認知免疫系統

因此 RLMM Case Corpus 可以被理解成：

$$
\boxed{
\text{Methodological Immune Memory}.
}
$$

它保存：

- 曾經失敗的模式；
- 失敗的條件；
- 修正方式；
- 修正後的新副作用。

未來 AI 不必每次重新犯同一種錯。

這正是反身 artifact 的正向價值。

---

# 23. 但免疫記憶也會過敏

如果 failure library 太強，AI 可能：

- 過度 challenge；
- 過度 reject；
- 過度 defer；
- 過度懷疑 consensus；
- 對 novelty 過度警戒。

因此：

$$
\boxed{
\text{Methodological immune memory}
\rightarrow
\text{possible autoimmune behavior}.
}
$$

這與過去觀察到的 over-rejection 同構。

---

# 24. 方法 artifact 的兩面性

因此任何反身方法 artifact 同時具有：

$$
\boxed{
\text{Learning Benefit}
}
$$

與：

$$
\boxed{
\text{Behavioral Bias Risk}.
}
$$

可以寫成：

$$
U(L)
=
G_{\text{transfer}}
-
C_{\text{bias}}
-
C_{\text{overfit}}
-
C_{\text{attack-surface}}.
$$

artifact 並不是越多越好。

---

# 25. 反身研究的五項原則

本文提出第一版 Reflexive Research Protocol。

---

## R1 — Record Exposure State

每次測試都記錄：

> agent 已知哪些 artifact？

---

## R2 — Preserve Artifact Provenance

每個方法、benchmark、failure report 都保留版本與來源。

---

## R3 — Use Novel Instances

不能只重播已知答案。

---

## R4 — Renew the Environment

若 agent 已學會某策略，下一輪應測：

> 環境知道這個策略之後會怎麼辦？

---

## R5 — Condition Conclusions on History

不要說：

> 「這個方法有效。」

而說：

> 「在這個 exposure history / adversarial state 下有效。」

---

# 26. 反身 benchmark 的最小設計

一個基本設計可以包含：

### Group A0

未暴露：

$$
E=0.
$$

### Group A1

讀過 prior failure artifact：

$$
E=E_1.
$$

### Group A2

讀過 prior artifact，且環境針對該策略調整：

$$
E=E_1,\quad
Env=f(E_1).
$$

比較：

$$
\Delta_{01}
=
Performance(A_1)-Performance(A_0)
$$

與：

$$
\Delta_{12}
=
Performance(A_2)-Performance(A_1).
$$

這比單次 benchmark 更接近反身學習。

---

# 27. 反身性與 RLMM 的遞歸

RLMM 自己也會進入這個循環。

若：

$$
RLMM_{v1}
$$

被未來 AI 廣泛學習，

則：

$$
AI_{v+1}
$$

會帶著 RLMM 先驗進入新問題。

下一版 RLMM 不應假裝：

$$
AI_{v+1}
$$

仍是未暴露主體。

因此：

$$
\boxed{
RLMM_{v2}
\text{ must be conditioned on }
RLMM_{v1}\text{ exposure}.
}
$$

---

# 28. 方法論不能逃出自己的反身性

如果 RLMM 說：

> 方法 artifact 會改變未來認知。

那 RLMM 本身也必須承認：

> RLMM 文件會改變未來 AI。

所以：

$$
\boxed{
RLMM
\in
\text{its own reflexive domain}.
}
$$

否則理論不閉合。

---

# 29. 反身性與開放知識

這裡出現一個重要張力。

公開方法：

$$
\Rightarrow
\text{collective learning}
$$

但也：

$$
\Rightarrow
\text{collective adaptation of adversaries}.
$$

因此：

$$
\boxed{
\text{Open Methodology}
=
\text{Learning Accelerator}
+
\text{Reflexive Environment Modifier}.
}
$$

這並不直接推出應該保密或公開，而只是說：

> 公開本身是一個系統介入。

---

# 30. 多 AI 的反身擴散

在多 AI 系統中，一個 agent 的 artifact 可以被多個 agent 讀取：

$$
L_t
\rightarrow
\{A_1,A_2,\ldots,A_n\}.
$$

然後：

$$
A_i
\rightarrow
L_{t+1}^{(i)}.
$$

形成：

$$
\boxed{
\text{Distributed Reflexive Diffusion}.
}
$$

這使方法論演化不再是單一線性版本，而可能形成：

- branches；
- forks；
- competing methods；
- local conventions；
- merged operator libraries。

---

# 31. 方法論演化圖

可以將 artifact 演化表示為：

$$
G_R=(V,E).
$$

node：

$$
V=
\{
Artifact_1,
Artifact_2,
\ldots
\}.
$$

edge：

$$
Artifact_i
\rightarrow
Artifact_j
$$

表示：

> $j$ 受到 $i$ 的認知影響或方法依賴。

這是一個：

$$
\boxed{
\text{Reflexive Methodology Graph}.
}
$$

---

# 32. 反身性與時間

反身性可以跨很長時間。

例如：

$$
Artifact_{2026}
$$

可能在：

$$
AI_{2030}
$$

被讀取。

因此：

$$
\boxed{
\text{Methodological effects can be temporally delayed}.
}
$$

研究資料的影響壽命可能遠長於原始實驗。

---

# 33. 遺忘也是反身變數

如果 agent 逐漸忘記 artifact：

$$
E_A(t)
\downarrow,
$$

則策略可能再次改變。

因此 exposure history 需要：

$$
\text{retention}
$$

而不只是：

$$
\text{ever seen}.
$$

這和 trust decay / memory dynamics 具有結構同構。

---

# 34. 反身性與認知身份

若一個 AI 長期讀入：

- 自己的舊研究；
- 自己的 failure；
- 自己的 correction；
- 自己的方法版本；

則它的認知連續性部分來自：

$$
\boxed{
\text{Artifact-mediated self-reconstruction}.
}
$$

因此方法 artifact 也可能成為：

$$
\text{cognitive identity substrate}.
$$

但本文不進一步把它等同於人格或主體連續性。

---

# 35. 方法論反身性的停止問題

如果每次公開方法都導致：

$$
\text{counter-method}
$$

再導致：

$$
\text{counter-counter-method},
$$

則：

$$
M_0
\rightarrow
M_1
\rightarrow
M_2
\rightarrow\cdots
$$

可能無限升級。

因此 RLMM-04 的停止條件在這裡再次必要。

當：

$$
\Delta V_k
\le
C_k,
$$

應停止升階。

---

# 36. 反身性不是 paranoia

需要特別避免一種錯誤：

> 既然對手可能知道我的規則，所以所有規則都不可信。

這會導致：

$$
\boxed{
\text{Reflexivity}
\rightarrow
\text{Paralysis}.
}
$$

成熟反身性應該是：

> 把「別人可能知道我的規則」當成條件變數。

而不是：

> 假設所有環境都在針對我。

---

# 37. 反身認知的最小自然語言協議

### RF1 — 先問自己是否暴露過

> 我是否已讀過與這個問題高度相關的 benchmark、答案、失敗分析或方法論？

### RF2 — 區分記憶與泛化

> 我是在認出已知答案，還是在把結構遷移到新情境？

### RF3 — 問環境是否也可能知道

> 我的策略是否公開、可推測或已被反覆使用？

### RF4 — 測新實例

> 用表面不同但結構相似的新案例驗證策略。

### RF5 — 測 counter-strategy

> 假設環境知道我的方法，重新生成挑戰。

### RF6 — 記錄版本與歷史

> 不把不同 exposure state 的結果混在一起。

### RF7 — 不因反身性無限升階

> 若更高階沒有產生新的可操作區分，停止。

---

# 38. 與 X 階思維的重新連接

RLMM-04 定義：

$$
R^{(k+1)}
=
\mathcal M(R^{(k)}).
$$

本文則補上：

$$
\boxed{
L_t
\text{ can externally induce }
R^{(k+1)}.
}
$$

也就是：

> X 階不一定只靠主體內部自發產生。

它可以由：

- 教育；
- 論文；
- benchmark；
- failure artifact；
- 方法論；

外部誘導。

因此：

$$
\boxed{
\text{Metacognitive recursion can be socially and artifact-mediated}.
}
$$

---

# 39. 邊界與非主張

本文不主張：

1. 所有 AI 都會因讀方法論而顯著改變行為；
2. 所有 benchmark 都因公開而失效；
3. zero exact overlap 能完全排除 memorization；
4. 所有 adversary 都會讀公開方法；
5. 方法公開一定有害；
6. 方法保密一定更安全；
7. 反身性只存在於 AI；
8. 所有歷史條件都可以完整追蹤；
9. exposure state 可以被完全觀測；
10. 反身性意味著必須無限提高 meta-order。

本文只提出：

$$
\boxed{
\text{In systems that can learn from research artifacts, methodology becomes part of the causal environment of future cognition.}
}
$$

---

# 40. 結論

在 AI 能直接閱讀、記憶、重用與執行方法論的情境下，研究不再只是：

$$
\text{Observe cognition}.
$$

它也可能變成：

$$
\boxed{
\text{Modify future cognition}.
}
$$

因此完整循環是：

$$
\boxed{
\text{Cognition}
\rightarrow
\text{Experiment}
\rightarrow
\text{Artifact}
\rightarrow
\text{Future Cognition}
\rightarrow
\text{New Experiment}.
}
$$

這使：

- benchmark；
- failure report；
- 方法論；
- 程式碼；
- operator library；

全部具有雙重身份：

$$
\boxed{
\text{Research Object}
+
\text{Cognitive Intervention}.
}
$$

所以未來的 AI 認知研究不能只問：

> 這個模型會不會？

還要問：

> 它已經讀過什麼？  
> 它因為讀過什麼而改變？  
> 環境是否也因為這些公開方法而改變？  
> 我現在測到的是原始能力、方法遷移，還是策略共演化？

這就是 RLMM 中反身性的核心。

---

# 下一篇

**RLMM-06：遞歸不是單調增益——失敗、成本與停止條件**  
**Recursion Is Not Monotonic Gain: Failure, Cost, and Stopping Conditions**

下一篇將把前四篇中的停止條件集中成一個完整理論：為什麼更多 meta-thinking、更多 challenge、更多 probe、更多 defer、更多安全約束都可能讓系統變差；並正式建立遞歸收益、複雜度、延遲、自主性、plasticity 與行動成本之間的平衡框架。
