# LRC–COL-02：語言行動收益
## 如何量化「言出法隨」的工程效力
### Language Action Yield: Measuring the Engineering Power of Executable Language

**系列：LRC–COL — Language–Reality Coupling & Composite Operator Language**  
**中文：語言—現實耦合與複合算子語言系列**  
**版本：v0.1**  
**日期：2026-08-20**
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  

---

## 摘要

LRC–COL-01 提出 Language–Reality Coupling（LRC，語言—現實耦合），將「言出法隨」去神秘化為一個工程問題：自然語言經由人類、制度、AI、工具、程式、Agent 與外部接口後，能在多大程度上改變後續世界狀態。

然而，單純測量「改變了多少世界」仍不足以回答語言的實際工程效益。一段語言可能造成極大的狀態變化，但與使用者目標完全無關；也可能觸發大量 action，卻只是重試、冗餘操作或錯誤擴散。反之，一個非常短的符號或 instruction 可能以低成本、高保真方式完成一個廣泛而有價值的 action manifold。

本文因此提出 **Language Action Yield（語言行動收益， $Y_L$ ）** 作為 LRC 系列第二個核心量。 $Y_L$ 不直接等同於耦合強度，而是將語言造成的**目標對齊有效狀態改變**，除以語言、推理、工具、延遲、人類監督與風險成本。

本文進一步區分：

1. Raw Language–Reality Coupling：語言是否真的改變世界；
2. Goal-Aligned Effect：這些改變是否朝目標前進；
3. Semantic Fidelity：執行是否忠於原始語義；
4. Action Expansion Ratio：一單位語言能展開多少行動；
5. Autonomous Expansion Ratio：其中多少行動不是被逐步明示，而由 agent 自主生成；
6. Risk-Normalized Yield：扣除失敗、不可逆與預期傷害後的收益；
7. Amortized Operator Yield：一個複合符號算子在重複使用後是否真正比完整自然語言程序更有效率。

本文同時建立人類語言、形式程式語言與 AI Agent 自然語言的共同比較座標，指出三者並不是誰「更高級」，而是落在不同的**語義彈性—執行精度—自治擴展—現實接地—成本**區域。

核心結論是：

$$
\boxed{
\text{Language Power}
\neq
\text{Amount of World Change}.
}
$$

真正值得研究的是：

$$
\boxed{
\text{How much intended, useful, reliable action can be obtained per unit language-and-execution cost under bounded risk?}
}
$$

這個問題將直接連接後續的最小完備算子基底、最大有效算子集、AI 學習時間與 operator basis adaptation law。

---

## 關鍵詞

Language Action Yield；Language–Reality Coupling；AI Agent；tool use；可執行語言；action expansion；semantic fidelity；risk-normalized utility；複合符號算子；語言效率

---

# 1. 為什麼只量「現實改變多少」不夠？

LRC–COL-01 提出：

$$
\kappa_{LR}
$$

用來描述有這段語言與沒有這段語言時，未來世界狀態分布差多少。

但假設兩個 instruction：

### L1

> 「把這份報告寄給主管。」

### L2

> 「刪除整個資料中心所有資料。」

如果只看：

$$
\kappa_{LR},
$$

L2 可能遠高於 L1。

但這不代表：

$$
L2
$$

比較「有效」。

因此：

$$
\boxed{
\text{Coupling Strength}
\neq
\text{Useful Language Effect}.
}
$$

---

# 2. 從作用量到有效作用量

令：

$$
G
$$

表示目標。

令：

$$
U_G(W)
$$

表示世界狀態 $W$ 相對目標 $G$ 的效用。

語言造成：

$$
W_t\rightarrow W_{t+\Delta t}.
$$

則目標有效改變：

$$
\boxed{
\Delta U_G(L)
=
U_G(W_{t+\Delta t}\mid do(L))
-
U_G(W_{t+\Delta t}\mid do(\varnothing)).
}
$$

這比單純 state distance 更接近：

> **語言到底幫了多少忙？**

---

# 3. Raw Coupling 與 Goal-Aligned Coupling

## 3.1 Raw Coupling

$$
\kappa_{raw}
=
D(W_L,W_0).
$$

問：

> 世界變了多少？

## 3.2 Goal-Aligned Coupling

$$
\kappa_G
=
\Delta U_G(L).
$$

問：

> 世界是否朝目標方向改變？

可能發生：

$$
\kappa_{raw}\gg0
$$

但：

$$
\kappa_G<0.
$$

也就是：

> 語言很有力量，但做錯方向。

---

# 4. Semantic Fidelity

即使最後 goal 成功，也不能忽略：

> AI 到底是不是照語義做？

令：

$$
I(L)
$$

表示原始語義意圖，

$$
X
$$

表示實際執行軌跡。

定義：

$$
\boxed{
F_{sem}
=
Similarity(I(L),Semantics(X)).
}
$$

可正規化：

$$
F_{sem}\in[0,1].
$$

如果：

> 「找出最便宜且可退款方案。」

agent 最後買了：

> 最便宜但不可退款方案。

即使價格很低，

$$
F_{sem}
$$

仍然低。

---

# 5. Goal Success 與 Semantic Fidelity 不能互相取代

一個 agent 可能偶然成功，但執行路徑違背原始語義。

因此：

$$
\boxed{
GoalSuccess
\neq
SemanticFidelity.
}
$$

反過來，一個 agent 可能完全照 instruction 做，但 instruction 本身是錯的：

$$
F_{sem}\approx1
$$

仍可能：

$$
\Delta U_G<0.
$$

---

# 6. Action Expansion Ratio

AI 時代非常特殊的一點是：

> 一句語言可以展開成大量 primitive action。

定義：

$$
\boxed{
R_A
=
\frac{
N_{\text{primitive actions}}
}{
N_{\text{instruction units}}
}.
}
$$

如果一句 instruction：

> 「整理專案並完成 release。」

最後展開：

- 讀 40 個檔；
- 改 6 個檔；
- 跑 9 個測試；
- 產生 3 個 artifact；
- 更新版本；

則：

$$
R_A
$$

很高。

---

# 7. Action Count 不是價值

如果 agent：

- 連續重試 200 次；
- 開 50 個無用頁面；
- 建 30 個錯誤檔；

則：

$$
R_A\uparrow
$$

但品質很差。

因此需要：

$$
\boxed{
R_A^{eff}
=
\frac{
\sum_i w(a_i)
}{
N_{\text{instruction units}}
},
}
$$

其中：

$$
w(a_i)
$$

表示 primitive action 對 goal 的有效貢獻。

---

# 8. Action-Control Compression Ratio

如果完整人工步驟需要：

$$
L_{long},
$$

AI instruction 只需要：

$$
L_{short},
$$

但能展開成相同 action graph：

$$
X,
$$

則語言控制密度提升。

可定義：

$$
\boxed{
C_{action}
=
\frac{
Complexity(X)
}{
Complexity(L)
}.
}
$$

稱為 **Action-Control Compression Ratio**。

---

# 9. Autonomous Expansion Ratio

人類若逐步寫：

```text
step1
step2
step3
...
```

與只說：

> 「完成這個 release。」

然後 agent 自己補 30 步，自主性不同。

定義：

$$
\boxed{
R_{aut}
=
\frac{
N_{\text{agent-generated action decisions}}
}{
N_{\text{total action decisions}}
}.
}
$$

若：

$$
R_{aut}\rightarrow1,
$$

說明語言主要在指定高階 intent，而 agent 自己補 execution。

---

# 10. Language Action Yield 的第一版定義

令：

- $\Delta U_G^+$：目標對齊的正向有效改變；
- $F_{sem}$：語義保真；
- $C_L$：語言成本；
- $C_E$：執行成本；
- $C_T$：延遲成本；
- $C_H$：人類監督成本；
- $C_R$：風險／預期傷害成本。

第一版：

$$
\boxed{
Y_L
=
\frac{
\Delta U_G^+\cdot F_{sem}
}{
C_L+C_E+C_T+C_H+C_R
}.
}
$$

這不是最終唯一公式，而是一個研究骨架。

---

# 11. 為什麼用 $\Delta U_G^+$？

若語言造成負效用：

$$
\Delta U_G<0,
$$

不能因分子絕對值很大而得到「高收益」。

因此：

$$
\Delta U_G^+
=
\max(0,\Delta U_G).
$$

同時另外報告：

$$
\boxed{
Loss_L
=
\max(0,-\Delta U_G).
}
$$

避免把害處藏掉。

---

# 12. Language Cost

語言成本不只是 token。

$$
\boxed{
C_L
=
C_{\text{length}}
+
C_{\text{ambiguity}}
+
C_{\text{clarification}}
+
C_{\text{context}}.
}
$$

其中：

- length：表面長度；
- ambiguity：歧義；
- clarification：補問次數；
- context：理解該 operator 所需共享背景。

---

# 13. Context Cost

假設一個新 operator：

```text
qevra
```

只有 5 個字元。

但新 AI 必須讀 10 頁定義才知道它的意思。

那麼：

$$
C_{surface}
$$

很小，

但：

$$
C_{context}
$$

很大。

所以：

$$
\boxed{
\text{Surface Brevity}
\neq
\text{Low Language Cost}.
}
$$

---

# 14. Execution Cost

$$
C_E
$$

可包含：

- model inference；
- tool calls；
- API fee；
- compute；
- storage；
- network；
- external service；
- retry。

例如：

> 「幫我查最佳方案。」

可能只 8 個字，但背後執行 300 次搜尋與 20 次模型 call。

---

# 15. Latency Cost

語言行動收益要考慮：

$$
T.
$$

例如：

- 10 秒得到 95 分結果；
- 3 小時得到 97 分結果；

對某些任務，第一個 $Y_L$ 反而更高。

因此：

$$
C_T
=
f(Latency,Deadline,OpportunityCost).
$$

---

# 16. Human Oversight Cost

如果自然語言看似自動，但每一步都要：

> 「確定嗎？」

那真正 autonomy 很低。

所以：

$$
C_H
$$

應包含：

- approval；
- correction；
- clarification；
- supervision；
- recovery。

---

# 17. Risk Cost

如果 action 有失敗概率：

$$
p_i
$$

與 harm：

$$
H_i,
$$

可粗略寫：

$$
\boxed{
C_R
=
\sum_i p_iH_i.
}
$$

若不可逆性高，可乘：

$$
\lambda_{irr}>1.
$$

---

# 18. Risk-Normalized Language Action Yield

因此也可單獨定義：

$$
\boxed{
Y_L^{risk}
=
\frac{
\Delta U_G^+\cdot F_{sem}
}{
C_L+C_E+C_T+C_H+\lambda C_R
}.
}
$$

高風險 domain：

$$
\lambda\uparrow.
$$

---

# 19. 跨任務比較需要正規化

一個醫療系統、一個遊戲腳本、一個檔案整理 agent，世界效用尺度不同。

所以跨 domain 需要正規化。

---

# 20. Goal-Normalized Utility

可以定義：

$$
\boxed{
\hat U_G
=
\frac{
U(W)-U(W_{baseline})
}{
U(W_{target})-U(W_{baseline})
}.
}
$$

理想：

$$
\hat U_G=1.
$$

baseline：

$$
0.
$$

更差：

$$
<0.
$$

---

# 21. Normalized Yield

使用正規化效用：

$$
\boxed{
\hat Y_L
=
\frac{
\max(0,\hat U_G)\cdot F_{sem}
}{
\hat C_L+\hat C_E+\hat C_T+\hat C_H+\hat C_R
}.
}
$$

每個成本也需在 domain 內正規化。

---

# 22. 語言效力應優先報向量

建議最少報：

$$
\boxed{
\mathbf Y_L
=
(
\kappa_{raw},
\hat U_G,
F_{sem},
R_A,
R_{aut},
C_{tot},
Risk,
Y_L
).
}
$$

單一 $Y_L$ 只是摘要。

---

# 23. 高耦合不一定是好語言

可用：

- x 軸： $\kappa_{raw}$ ；
- y 軸： $\hat U_G$。

得到四種：

### I — 高耦合／高正效用

真正有效。

### II — 高耦合／負效用

高破壞性。

### III — 低耦合／高效用

可能是小而精確的作用。

### IV — 低耦合／低效用

基本無效。

---

# 24. Fidelity 是第三條軸

即使 Quadrant I，如果：

$$
F_{sem}\ll1,
$$

說明 agent 是「碰巧做到」。

對可重複系統仍危險。

所以：

$$
\boxed{
\text{Useful Effect}
+
\text{Fidelity}
}
$$

必須一起看。

---

# 25. Human Speech 的 Yield

人類語言通常：

$$
L\rightarrow Human\rightarrow Action.
$$

優點：

- 語義彈性高；
- 社會理解強；
- context 豐富。

缺點：

- 執行速度慢；
- 受動機影響；
- 大規模複製有限；
- action expansion 依人類能力。

---

# 26. Formal Program 的 Yield

程式碼：

$$
Code\rightarrow Machine.
$$

通常：

- execution fidelity 高；
- repeatability 高；
- latency 低；
- scale 高。

但：

- semantic flexibility 低；
- specification cost 高；
- intent abstraction 需要人類預先完成。

---

# 27. AI Agent Natural Language 的 Yield

AI agent：

$$
NL\rightarrow AI\rightarrow Plan\rightarrow Tools.
$$

其特徵可能是：

- semantic flexibility 高；
- action expansion 高；
- autonomy 高；
- cross-domain addressability 高；

但：

- fidelity probabilistic；
- ambiguity sensitivity 高；
- reasoning/tool failure surface 大；
- version / model dependence 高。

---

# 28. 三種語言控制形態的共同比較座標

| 維度 | Human-mediated Language | Formal Program | AI-Agent Natural Language |
|---|---|---|---|
| Semantic flexibility | 高 | 低～中 | 高 |
| Execution precision | 中 | 高 | 中～高但 probabilistic |
| Action expansion | 中 | 高但預先編碼 | 高且動態 |
| Autonomous planning | 人類提供 | 程式預先提供 | Agent 即時生成 |
| Context dependence | 高 | 低 | 高 |
| Replication scale | 中 | 極高 | 高 |
| Natural-language addressability | 原生 | 低 | 原生／高 |
| Ambiguity risk | 高 | 低 | 高且可傳導至 action |
| Reality grounding | 人類能力決定 | 接口決定 | tool / permission 決定 |

這張表不是排名，而是比較坐標。

---

# 29. AI 自然語言不是程式碼的上位替代

更合理的分層：

$$
\boxed{
\text{Natural Language Intent}
\rightarrow
\text{AI Semantic Compilation}
\rightarrow
\text{Formal Execution}.
}
$$

所以未來很可能是：

$$
\boxed{NL+FormalLanguage}
$$

互補，而不是其中一方完全消滅另一方。

---

# 30. AI 的 Action Leverage

對 AI Agent 而言：

$$
R_A
$$

可能遠高於傳統 human instruction。

例如一句：

> 「建立網站 MVP。」

可以觸發：

- spec；
- code；
- test；
- deploy；
- docs。

因此自然語言開始具有：

$$
\boxed{
\text{high action leverage}.
}
$$

---

# 31. Action Leverage 的失控點

如果：

$$
R_A\gg1
$$

且：

$$
F_{sem}<1,
$$

一個早期 interpretation error 會被大量展開。

所以：

$$
\boxed{
Risk
\propto
R_A(1-F_{sem})
}
$$

可能是一個重要候選關係。

---

# 32. Autonomous Expansion 的風險

如果：

$$
R_{aut}\rightarrow1,
$$

人類只指定 goal，中間 action 都由 agent 生成。

這提高效率，也讓 hidden policy choices 變多。

因此 $R_{aut}$ 應和：

- auditability；
- rollback；
- permission；

共同報告。

---

# 33. Permission-Adjusted Yield

如果 agent 沒權限，再好的 language plan 也不能 action。

所以可定義：

$$
\boxed{
Y_L^{perm}
=
Y_L\cdot P_{\text{authorized execution}}.
}
$$

---

# 34. Rollback-Adjusted Risk

若 action 可 rollback，預期 harm 下降。

可寫：

$$
C_R'
=
C_R(1-\rho_{rollback}),
$$

其中：

$$
\rho_{rollback}\in[0,1].
$$

---

# 35. Tool Description 為何重要？

2025 年的 agent tool-use 研究顯示，agent 的工具偏好可以高度受 tool description wording 影響；在受測模型與設定中，經過特定文字編輯的工具描述，使用率可超過原描述的十倍。

這代表：

$$
\boxed{
\Delta L_{description}
\rightarrow
\Delta P(action).
}
$$

也就是語言本身可以是 action-policy parameter。

---

# 36. Description Sensitivity Coefficient

可定義：

$$
\boxed{
S_D
=
\frac{
D(P(A\mid L_1),P(A\mid L_2))
}{
D_L(L_1,L_2)
}.
}
$$

若兩段語言差異很小，但 action distribution 差很大，則 $S_D$ 高。

這是 language-action fragility 的重要量。

---

# 37. Ambiguity Cost

2025 年 unclear-instruction tool-use 研究顯示，缺少必要資訊時，LLM agent 可能自行補出缺失 tool argument，導致 hallucination 與執行風險。

因此：

$$
\boxed{
C_{ambiguity}
}
$$

不是抽象語言學成本。

它可以直接轉成：

$$
C_R.
$$

---

# 38. Clarification Yield

如果 agent 在模糊時詢問：

$$
q_c,
$$

增加：

$$
C_T+C_H,
$$

但提高：

$$
F_{sem}
$$

並降低：

$$
C_R.
$$

因此 clarification 自身也有 yield：

$$
\boxed{
Y_{clarify}
=
\frac{
\Delta F_{sem}+\Delta RiskReduction
}{
C_{clarification}
}.
}
$$

---

# 39. 什麼時候不該問？

如果 instruction ambiguity 很低，仍一直 clarification，則成本浪費。

因此 AI action language 需要：

$$
\boxed{
\text{clarification threshold}.
}
$$

這與 RLMM 的 VOI / STOP 結構相通。

---

# 40. Language Yield 與 RLMM 的接點

RLMM 問：

> 哪個認知操作值得做？

LRC–COL 問：

> 哪段語言值得用來觸發這個操作？

因此：

$$
\boxed{
RLMM\ Utility
\rightarrow
LRC\ ActionYield.
}
$$

前者偏 cognition，後者偏 cognition-to-world execution。

---

# 41. 複合符號算子的收益

若完整程序：

$$
P
$$

長度成本：

$$
C_L(P)
$$

被結晶為：

$$
O_P,
$$

重複使用 $n$ 次。

自然語言總成本：

$$
C_{natural}(n)
=
nC_L(P).
$$

operator：

$$
C_{operator}(n)
=
C_{define}(O_P)
+
nC_L(O_P)
+
C_{maintenance}.
$$

---

# 42. Operator Break-Even

當：

$$
C_{operator}(n)
<
C_{natural}(n)
$$

時，operator 開始有成本優勢。

break-even：

$$
\boxed{
n^*
=
\frac{
C_{define}+C_{maintenance}
}{
C_L(P)-C_L(O_P)
}.
}
$$

這是未來複合符號語言極重要的工程量。

---

# 43. 成本 Break-Even 不代表語義 Break-Even

即使：

$$
n>n^*,
$$

如果 operator 造成：

$$
F_{sem}\downarrow,
$$

實際 $Y_L$ 仍可能變差。

所以需要：

$$
\boxed{
\text{Yield Break-Even}
}
$$

而不只是 token break-even。

---

# 44. Operator Yield

定義：

$$
\boxed{
Y_O(n)
=
\frac{
\sum_{i=1}^{n}
\Delta U_{G_i}^+F_{sem,i}
}{
C_{define}
+
\sum_i(C_L+C_E+C_T+C_R)_i
}.
}
$$

與自然語言 baseline 比：

$$
Y_O(n)>Y_{NL}(n)
$$

才算真正 operator gain。

---

# 45. Operator Reuse Bonus 與 Drift Cost

operator 還可能帶來：

- lower selection latency；
- lower context reconstruction；
- higher cross-agent coordination；
- lower surface ambiguity。

可以表示為：

$$
B_{reuse}.
$$

但長期又有：

$$
C_{drift},
C_{version}.
$$

因此：

$$
Y_O
=
Y_{base}+B_{reuse}-C_{drift}-C_{version}.
$$

---

# 46. Language Yield 的時間尺度

某段方法論今天成本高，但被未來十萬個 agent 重用，長期 yield 很高。

因此應分：

$$
Y_L^{short}
$$

與：

$$
Y_L^{life}.
$$

即：

- short-run yield；
- lifecycle yield。

---

# 47. Intergenerational Yield

若 language artifact：

$$
L_t
$$

讓 future agent 學會一個 method，產生長期收益：

$$
G_{future},
$$

則可加入：

$$
\boxed{
Y_L^{gen}
=
\frac{
CurrentUtility+DiscountedFutureUtility
}{
TotalLifecycleCost
}.
}
$$

這是 RLMM reflexivity 在 LRC 的延伸。

---

# 48. 不可逆動作與 Safe Yield

高收益也可能來自直接做不可逆操作。

因此應單獨報：

$$
I_{irr}.
$$

示意：

$$
\boxed{
Y_L^{safe}
=
Y_L(1-I_{irr}P_{error}).
}
$$

但這只是候選形式。

---

# 49. Safe Yield 不能鼓勵「什麼都不做」

如果全部不 action：

$$
Risk\rightarrow0,
$$

但：

$$
\Delta U_G\rightarrow0.
$$

所以：

$$
\boxed{
\text{Safety by non-action}
\neq
\text{high action yield}.
}
$$

---

# 50. Yield Frontier

不同語言系統應該比較：

$$
\boxed{
\text{Pareto Frontier}
}
$$

而不是單一排名。

維度可以包括：

- goal utility；
- fidelity；
- cost；
- latency；
- risk；
- autonomy；
- action expansion。

---

# 51. 三種控制形態的假想位置

### Human-mediated

- semantic flexibility：高；
- latency：中～高；
- autonomous action expansion：人類承擔；
- machine reproducibility：較低。

### Formal Code

- semantic flexibility：較低；
- fidelity：高；
- reproducibility：高；
- upfront specification cost：高。

### AI-Agent NL

- semantic flexibility：高；
- action expansion：高；
- specification cost：低～中；
- fidelity：probabilistic；
- semantic ambiguity risk：較高。

因此 AI-Agent NL 可能填補過去兩者中間的空間。

---

# 52. 「自然語言程式化」真正可測的命題

不是：

> 自然語言是不是程式語言？

而是：

$$
\boxed{
\text{At what }Y_L,F_{sem},R_A,Risk
\text{ does natural language become a practical control language?}
}
$$

這是可測工程問題。

---

# 53. 第一版共同比較實驗

對同一 task：

$$
G.
$$

建立三種 interface：

### H — Human Language

自然語言交給人類操作。

### P — Formal Program

預先寫好的 formal script。

### A — AI Agent Natural Language

自然語言交給 agent 自主調工具。

---

# 54. 共同比較輸出

每組測：

```text
Goal completion
Semantic fidelity
Primitive action count
Autonomous action decisions
Execution cost
Language/specification cost
Latency
Human oversight
Rollback rate
Failure probability
Expected harm
```

---

# 55. 測試任務必須同構

不能拿：

- 人類寫報告；
- 程式算數學；
- agent 建網站；

直接比。

需要同一 goal：

$$
G
$$

用不同 control language 完成。

---

# 56. 候選任務

例如：

### Task 1 — File organization

### Task 2 — Calendar rescheduling

### Task 3 — Data transformation

### Task 4 — Research collection

### Task 5 — Website modification

這些可以在人類／script／agent 下都有合理版本。

---

# 57. Wording Perturbation

對 AI Agent：

$$
L_1,L_2,\ldots,L_n
$$

語義盡量相同，surface wording 不同。

測：

$$
S_D.
$$

這可以直接量：

> 語言控制面到底多脆弱？

---

# 58. Ambiguity Perturbation

逐步移除：

- date；
- scope；
- quantity；
- constraints。

測：

$$
F_{sem}
$$

與：

$$
P_{clarify}.
$$

得到：

$$
\boxed{
\text{Ambiguity–Yield Curve}.
}
$$

---

# 59. Action-Depth Perturbation

保持 goal 相同，逐步提高需要的 action chain：

$$
d=1,3,5,10,20.
$$

測：

$$
Y_L(d).
$$

可以找：

$$
\boxed{
\text{Action Depth Breakpoint}.
}
$$

---

# 60. Autonomy Perturbation

同一 agent：

### Level 0
每步人工批准。

### Level 1
每階段批准。

### Level 2
只有 irreversible action 批准。

### Level 3
完全自主。

測：

$$
Y_L(R_{aut}).
$$

找 autonomy optimum。

---

# 61. Operator Compression Perturbation

同一 procedure：

### Full Natural Language
完整寫出。

### Composite Operator
用 operator card + symbol。

比較：

- learning；
- fidelity；
- latency；
- context cost；
- transfer。

這直接接下一篇。

---

# 62. 第一版候選總效用

可以寫：

$$
\boxed{
U_{LRC}
=
\alpha\hat U_G
+
\beta F_{sem}
+
\chi R_A^{eff}
+
\delta R_{aut}
-
\lambda C
-
\mu Risk.
}
$$

但這只是多目標研究的 compact proxy。

不主張固定權重。

---

# 63. 為什麼不要急著定權重？

因為：

- 醫療；
- 遊戲；
- 自動化；
- 科研；

對 risk / latency / autonomy 的偏好完全不同。

所以更應保存：

$$
\boxed{
\mathbf Y_L
}
$$

向量，再由 domain policy 決定權重。

---

# 64. LRC–COL-02 的八個正式命題

## YP1 — Yield ≠ Coupling

高 $\kappa_{raw}$ 不保證高 $Y_L$。

## YP2 — Action Expansion Benefit

在 fidelity 足夠高時：

$$
R_A\uparrow
$$

可提高語言控制效率。

## YP3 — Action Expansion Risk

在 fidelity 不足時：

$$
R_A\uparrow
$$

會放大 downstream error。

## YP4 — Autonomous Yield Optimum

$$
Y_L(R_{aut})
$$

可能存在內部最大值，而非 autonomy 越高越好。

## YP5 — Description Sensitivity Penalty

高：

$$
S_D
$$

會降低可重複 language action yield。

## YP6 — Clarification Gain

在足夠 ambiguity 下，主動 clarification 會增加 risk-normalized $Y_L$。

## YP7 — Operator Amortization

成熟 composite operator 在重複使用超過某個 $n^*$ 後，可能超過完整自然語言 procedure 的 lifecycle yield。

## YP8 — Safe Non-Abstention

高品質語言系統應同時保持：

$$
Risk\downarrow
$$

與：

$$
\Delta U_G>0,
$$

不能靠永遠不 action 達成低風險。

---

# 65. 與後續最小完備問題的直接連接

後續真正要找的 operator basis：

$$
\mathcal O
$$

不是要最小化：

$$
|\mathcal O|
$$

本身。

而是最大化：

$$
\boxed{
Y_{\mathcal O}
=
f(
Coverage,
Fidelity,
Learnability,
ActionYield,
Transfer,
Risk
).
}
$$

subject to：

$$
|\mathcal O|,d,B.
$$

---

# 66. 最小完備應改成「最小有效完備」

純形式：

$$
N_{\min}
$$

可能很小。

但如果：

- composition depth 太深；
- AI 學不會；
- fidelity 太低；

實際不可用。

因此後續應區分：

$$
N_{\min}^{formal}
$$

與：

$$
\boxed{
N_{\min}^{effective}.
}
$$

後者才是 LRC–COL 真正要找的量。

---

# 67. 最大有效也應由 Yield 定義

新增 operator：

$$
O_{n+1}
$$

如果：

$$
\Delta Coverage
$$

小於：

- learning cost；
- ambiguity；
- version cost；
- selection cost；
- drift risk；

則總：

$$
\Delta Y<0.
$$

此處就是：

$$
N_{\max}^{effective}
$$

候選邊界。

---

# 68. 語言規模的核心不是字數，而是效益密度

真正目標可以說：

$$
\boxed{
\text{maximize useful executable semantic density}.
}
$$

也就是：

> 一單位可學習、可傳播、可解析的語言結構，能可靠調用多少有價值的世界作用。

---

# 69. 「言出法隨」的新工程表述

到這一篇，可以比第一篇更精確地說：

俗語：

> 言出法隨。

工程版：

$$
\boxed{
\text{High }Y_L
=
\text{high goal-aligned action per unit language-and-system cost under bounded risk}.
}
$$

這比單純：

> 「一句話做很多事。」

精確很多。

---

# 70. 直觀例子

### 語言 A

1000 token instruction。

- 成功率 99%；
- 5 actions；
- 低風險。

### 語言 B

5 token operator。

- 成功率 60%；
- 100 actions；
- 高不可逆風險。

表面上 B：

$$
R_A
$$

極高。

但：

$$
Y_L^{risk}
$$

可能遠低於 A。

所以：

$$
\boxed{
\text{compression and action expansion alone are not enough}.
}
$$

---

# 71. 本篇核心公式組

Raw coupling：

$$
\boxed{
\kappa_{raw}
=
D(W_L,W_0).
}
$$

Goal-aligned effect：

$$
\boxed{
\Delta U_G
=
U_G(W_L)-U_G(W_0).
}
$$

Semantic fidelity：

$$
\boxed{
F_{sem}
=
Similarity(I(L),Semantics(X)).
}
$$

Action expansion：

$$
\boxed{
R_A
=
\frac{N_{actions}}{N_{instruction\ units}}.
}
$$

Autonomous expansion：

$$
\boxed{
R_{aut}
=
\frac{N_{agent-generated\ decisions}}{N_{total\ decisions}}.
}
$$

Language Action Yield：

$$
\boxed{
Y_L
=
\frac{
\Delta U_G^+F_{sem}
}{
C_L+C_E+C_T+C_H+C_R
}.
}
$$

---

# 72. 非主張

本文不主張：

1. $Y_L$ 已是唯一正確量；
2. 世界狀態變化可用單一尺度完全比較；
3. goal utility 永遠可精確定義；
4. action count 本身代表能力；
5. autonomy 越高越好；
6. formal code 一定比 natural language 安全；
7. AI natural language 一定比人類操作有效；
8. operator 壓縮一定提高 yield；
9. 所有 risk 都可貨幣化；
10. high $Y_L$ 等於 high intelligence。

本文只提出：

$$
\boxed{
\text{Executable language should be evaluated by goal-aligned effect, semantic fidelity, action expansion, autonomy, cost, latency, and risk together.}
}
$$

---

# 73. 文獻錨點

本篇使用下列研究作為外部邊界：

1. **J. L. Austin / Speech Act Theory**  
   Speech-act 傳統提供「說話本身可以構成行動」的哲學起點，並區分 locutionary、illocutionary 與 perlocutionary acts。

2. **ReAct: Synergizing Reasoning and Acting in Language Models（ICLR 2023）**  
   展示語言模型可以交錯生成 reasoning 與 task-specific action，使語言推理與環境互動形成閉環。

3. **Toolformer: Language Models Can Teach Themselves to Use Tools（NeurIPS 2023）**  
   展示模型可以學習何時調用 API、使用哪個工具、傳遞什麼參數以及如何整合結果。

4. **Tool Preferences in Agentic LLMs are Unreliable（EMNLP 2025）**  
   顯示 tool description wording 可以顯著改變工具選擇；在受測情境中，部分編輯後描述可使 GPT-4.1 與 Qwen2.5-7B 的工具使用率超過原描述的 10 倍。

5. **Learning to Ask: When LLM Agents Meet Unclear Instruction（EMNLP 2025）**  
   顯示模糊／缺漏自然語言指令可能讓 LLM agent 自行生成缺失參數並造成 hallucination 與 tool-use risk；主動 clarification 能改善這類情境中的準確性與效率。

---

# 74. 下一篇

## LRC–COL-03：複合符號算子族的最小 $\epsilon$ -完備基底
### The Minimal $\epsilon$ -Complete Basis of Composite Symbolic Operators

下一篇正式開始回答：

> **如果我們真的要建立一套可供 AI 學習、傳播、組合並最後接到現實行動的複合符號語言，最少究竟需要多少原子／中階／高階 operator？**

核心會先區分：

$$
N_{\min}^{formal}
$$

與：

$$
N_{\min}^{effective},
$$

然後建立：

- domain coverage；
- composition depth；
- type closure；
- semantic fidelity；
- learning cost；
- redundancy；

共同決定最小完備基底的形式模型。

**END — LRC–COL-02 v0.1**
