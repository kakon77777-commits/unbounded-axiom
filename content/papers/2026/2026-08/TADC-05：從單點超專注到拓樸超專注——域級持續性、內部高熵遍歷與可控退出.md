# TADC-05：從單點超專注到拓樸超專注——域級持續性、內部高熵遍歷與可控退出

**英文題名：** From Pointwise Hyperfocus to Topological Hyperfocus: Domain Persistence, High-Entropy Internal Traversal, and Controllable Exit  
**系列：** Topological Attention and Dynamic Cognitive Domains — Conjecture Series（TADC）  
**中文系列名：** 拓樸注意力與動態認知域命題系列  
**編號：** TADC-05  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論命題／注意力狀態模型／可證偽研究綱領  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

Hyperfocus 通常被描述為一種強烈、深度、持久，且常帶有狹窄化特徵的注意狀態。近年量表與實證研究已使 hyperfocus 從日常語言逐漸成為可操作測量的心理構念；同時，研究也顯示它與 ADHD traits、executive-function difficulties、cognitive-affective flexibility、emotion reactivity、flow、gaming motivation 與 burnout 等變項具有複雜關聯。

本文不提出新的臨床診斷，也不主張現有 hyperfocus 定義錯誤，而提出一個上位形式問題：

> **長時間高度專注是否一定意味著「長時間停留在單一認知點」？**

在 TADC-01 至 TADC-04 的動態認知空間、多尺度認知域、六算子與 object–domain duality 基礎上，本文提出三個互相包含但可分離的 hyperfocus 模型：

1. **Pointwise Hyperfocus（PHF）**：注意概率長時間集中於單一 object / task state；
2. **Domain Hyperfocus（DHF）**：注意長時間留在同一有效認知域，但域內可以存在高頻 switching；
3. **Topological Hyperfocus（THF）**：注意軌跡長期留在一個保持功能連續性的動態認知複體中，即使該複體本身持續 Expansion、Contraction、Traversal、Gluing、Detachment 與 Re-indexing。

本文提出：

$$
\boxed{
\text{high focus intensity}
\not\Rightarrow
\text{low internal mobility}.
}
$$

以及更強的：

$$
\boxed{
\text{domain persistence}
+
\text{high intra-domain entropy}
}
$$

可以共同存在。

為使「拓樸超專注」不是修辭，本文定義 domain-retention ratio、exit hazard、intra-domain transition rate、conditional entropy、goal continuity、connected-component persistence、re-indexing rate、voluntary exit controllability 與 cost load 等可測指標。本文並將 productive persistence 與 maladaptive lock-in 分開：高輸出、高投入或長時間工作本身都不足以證明健康、適應性或可控性。

本文進一步提出 **Topic Rotation as Focus Maintenance Conjecture（TRFMC）**：在部分認知型態中，低成本的域內切換可能不是專注的中斷，反而是維持高階目標長期投入的一種調節機制。其最小條件為：

$$
\nu_{\mathrm{intra}}\uparrow
$$

不導致：

$$
P_{\mathrm{domain}}\downarrow,
$$

並且在適當範圍內可能延長：

$$
T_{\mathrm{domain}}.
$$

本文建立 point-lock、flow-only、reward-only、executive-dyscontrol、random-switching 與 ordinary task-switching 等競爭模型，並提出 long-horizon behavioral logging、semantic transition graph、forced-stability、forced-switch、exit-control、re-entry 與 multi-resolution experiments。

本文的核心並非將所有長時間投入重新命名為 topological hyperfocus，而是提出一個可被資料否定的區分：

$$
\boxed{
\text{focus on a point}
\neq
\text{persistence within a dynamically evolving connected domain}.
}
$$

**關鍵詞：** hyperfocus；attention；domain persistence；topological attention；task switching；cognitive flexibility；attention entropy；flow；ADHD；multiscale cognition；TADC

---

# 0. 邊界聲明

本文不是臨床研究、診斷工具、治療建議或 ADHD 新診斷標準。

本文不主張：

$$
\boxed{
\text{hyperfocus is unique to ADHD}.
}
$$

也不主張：

$$
\boxed{
\text{hyperfocus is inherently beneficial}.
}
$$

或：

$$
\boxed{
\text{hyperfocus is inherently pathological}.
}
$$

本文提出的是一般性認知架構猜想。

ADHD 只是現有 hyperfocus literature 中的重要研究情境之一。

此外，「Topological Hyperfocus」是本文提出的理論術語，**不是現有正式臨床術語**。

---

# 1. 現有 hyperfocus 研究已經到哪裡？

Hupfeld、Abagis 與 Shah（2019）以 Adult Hyperfocus Questionnaire 系統性研究成人 hyperfocus，並發現較高 ADHD symptomology 與較高 hyperfocus frequency 相關。

2024 年 Hupfeld 等人進一步驗證 12-item Dispositional Adult Hyperfocus Questionnaire（AHQ-D）。該研究：

- \(n=347\)；
- AHQ-D 呈現單一主要 hyperfocus factor；
- Cronbach's \(\alpha=0.93\)；
- AHQ-D 與 ADHD trait measure 呈正相關；
- 與 flow 亦有正相關，但幅度較弱；
- 與 mind wandering 也存在正相關。

這代表 hyperfocus 已經具有可量化的心理計量工具。

但目前量表仍主要從：

$$
\boxed{
\text{intense / deep / prolonged task concentration}
}
$$

出發。

TADC-05 要問的是：

> 如果「task」本身其實只是 coarse-grained domain object，量表可能把哪些內部動態壓掉？

---

# 2. Hyperfocus 並不只是「注意力比較多」

Pimenta 等人（2024）在 380 名大學生中發現：

- ADHD symptom severity 與 hyperfocus frequency 正相關；
- executive-function difficulties 與 hyperfocus 正相關；
- EF difficulties 部分中介 ADHD symptoms 與 hyperfocus 的關聯。

這表示：

$$
\boxed{
\text{hyperfocus}
\neq
\text{simple high attention capacity}.
}
$$

至少在該樣本中，hyperfocus 也和 attention regulation / executive control difficulties 有關。

但該研究為 self-report、非臨床大學生樣本，不能證明單一因果機制。

---

# 3. 2026 年結果讓「靜態 hyperfocus」模型更不夠

Samson 等人（2026）比較：

$$
N=48
$$

成人 ADHD 與：

$$
N=48
$$

controls，

研究 cognitive-affective switching、emotion reactivity 與 hyperfocus。

其結果顯示：

- ADHD group 從 cognitive 切換到 affective stimuli 較慢；
- ADHD group 內，較快從 affective 切回 cognitive content 與較高 emotion reactivity 相關；
- emotion reactivity 在特定 switching index 與 dispositional hyperfocus 關係中呈現 mediation。

這些結果不證明 TADC。

但它至少提醒：

$$
\boxed{
\text{hyperfocus may coexist with
nontrivial switching dynamics}.
}
$$

所以只用：

$$
\text{focus intensity}
$$

單一維度描述可能過度簡化。

---

# 4. Hyperfocus 與 Flow 不能直接等同

2024 AHQ-D validation 中：

$$
r_{\mathrm{HF,flow}}
\approx0.12,
$$

呈弱正相關。

2026 adult gaming 研究也特別將：

$$
\text{hyperfocus}
$$

與：

$$
\text{flow}
$$

分開處理，並研究其對 burnout、self-efficacy、escapism 等不同 outcome / predictor patterns。

因此：

$$
\boxed{
\text{Hyperfocus}
\neq
\text{Flow}
}
$$

至少不能視為已證明同一構念。

TADC-05 也不以 flow 作為 THF 的同義詞。

---

# 5. 最簡單的 hyperfocus 模型

令注意狀態：

$$
x_t\in X.
$$

若存在：

$$
x^*
$$

使長時間：

$$
P(x_t=x^*)\rightarrow1,
$$

則可定義：

$$
\boxed{
\text{Pointwise Hyperfocus（PHF）}.
}
$$

它的直覺是：

> 一個人長時間停在同一個 task / object。

這是最接近一般 hyperfocus 語言的形式。

---

# 6. Pointwise Hyperfocus 指標

定義：

$$
L_x(T)
=
\frac{1}{T}
\int_0^T
\mathbf 1[x_t=x^*]
\,dt.
$$

若：

$$
L_x(T)\geq\theta_P,
$$

且：

$$
T\geq T_{\min},
$$

則候選 PHF。

也可以定義 point-exit hazard：

$$
h_x(t)
=
P(
x_{t+\Delta}\neq x^*
\mid
x_t=x^*
).
$$

PHF 預測：

$$
h_x\downarrow.
$$

---

# 7. 但「task」可能不是一個點

TADC-04 已提出：

$$
U^{(\lambda_f)}
\leftrightarrow
z_U^{(\lambda_c)}.
$$

在 coarse scale：

$$
z_U
$$

看起來是一個 task。

但 fine scale：

$$
U
=
\{x_1,x_2,\ldots,x_n\}
$$

可能是一個大型 relational domain。

因此一個 participant 報告：

> 我連續六小時都在做同一件事。

可能有至少兩種內部型態。

---

# 8. 型態 A：真正 point-lock

$$
x_1
\rightarrow
x_1
\rightarrow
x_1
\rightarrow
x_1.
$$

域內 mobility：

$$
\nu_{\mathrm{intra}}\approx0.
$$

---

# 9. 型態 B：domain persistence

$$
x_1
\rightarrow
x_7
\rightarrow
x_3
\rightarrow
x_{15}
\rightarrow
x_8
\rightarrow\cdots
$$

但：

$$
\forall i,\quad x_i\in U^*.
$$

在 coarse scale：

$$
P(U^*)\rightarrow1.
$$

因此：

$$
\boxed{
\text{high internal switching}
}
$$

與：

$$
\boxed{
\text{high domain persistence}
}
$$

可以同時成立。

---

# 10. Domain Hyperfocus（DHF）

定義一個有效 domain：

$$
U^*\subseteq X.
$$

domain-retention ratio：

$$
L_U(T)
=
\frac{1}{T}
\int_0^T
\mathbf 1[x_t\in U^*]
\,dt.
$$

若：

$$
L_U(T)\geq\theta_D,
$$

且：

$$
T\geq T_{\min},
$$

則為候選：

$$
\boxed{
\text{Domain Hyperfocus（DHF）}.
}
$$

---

# 11. DHF 不要求域內低 entropy

域內狀態分布：

$$
p_i
=
P(
x_t=x_i
\mid
x_t\in U^*
).
$$

定義 conditional entropy：

$$
H_{\mathrm{intra}}
=
-\sum_i
p_i\log p_i.
$$

PHF 通常預期：

$$
H_{\mathrm{intra}}\downarrow.
$$

但 DHF 可以：

$$
H_{\mathrm{intra}}\uparrow.
$$

所以：

$$
\boxed{
L_U\uparrow
\quad\land\quad
H_{\mathrm{intra}}\uparrow
}
$$

並不矛盾。

---

# 12. 域內切換率

定義：

$$
\nu_{\mathrm{intra}}
=
\frac{
N(
x_t\rightarrow x_{t+1};
x_t,x_{t+1}\in U^*
)
}{
T_U
}.
$$

domain exit rate：

$$
\nu_{\mathrm{exit}}
=
\frac{
N(
x_t\in U^*,
x_{t+1}\notin U^*
)
}{
T_U
}.
$$

因此最關鍵的可區分類型是：

### Point Lock

$$
\nu_{\mathrm{intra}}\downarrow,
\qquad
\nu_{\mathrm{exit}}\downarrow.
$$

### Domain Hyperfocus

$$
\nu_{\mathrm{intra}}\uparrow
\quad\text{or moderate},
$$

$$
\nu_{\mathrm{exit}}\downarrow.
$$

### Distractible Switching

$$
\nu_{\mathrm{intra}}\uparrow,
\qquad
\nu_{\mathrm{exit}}\uparrow.
$$

這三者不應混在一起。

---

# 13. Macro Persistence / Micro Mobility

若 coarse-scale domain variable：

$$
D_t
=
P_{\lambda_f\rightarrow\lambda_c}(x_t),
$$

則可以同時：

$$
H(D_t)\downarrow
$$

與：

$$
H(x_t\mid D_t)\uparrow.
$$

也就是：

$$
\boxed{
H_{\mathrm{macro}}\downarrow
\quad\land\quad
H_{\mathrm{micro}}\uparrow.
}
$$

中文：

> **宏觀高度集中，域內高度展開。**

這是 TADC-05 的核心 signature 之一。

---

# 14. Topological Hyperfocus（THF）

Domain Hyperfocus 仍假定：

$$
U^*
$$

大致固定。

但 TADC-01 至 TADC-03 已允許：

$$
U_t
\rightarrow
U_{t+1}.
$$

如果一個人長期投入某一認知複體，

而該複體自身持續：

$$
E,
C,
G,
D,
R,
T,
$$

則固定 domain 也不夠。

因此定義：

$$
\boxed{
\text{Topological Hyperfocus（THF）}.
}
$$

---

# 15. THF 的最小直覺

不是：

$$
x_t=x^*
$$

長期成立。

也不必要求：

$$
U_t=U^*
$$

長期固定。

而是存在一條 evolving domain sequence：

$$
U_0,U_1,\ldots,U_T
$$

使：

1. attention trajectory 長期位於：
   $$
   x_t\in U_t;
   $$
2. \(U_t\) 與 \(U_{t+1}\) 具有可追蹤結構連續性；
3. 高階 goal / invariant 保持；
4. exit probability 長期低；
5. domain 內允許大量局部 transition 與 re-indexing。

---

# 16. Connected Cognitive Complex

定義時間 \(t\) 的：

$$
\mathcal K_t
=
(
U_t,
\mathcal R_t,
\kappa_t
).
$$

若：

$$
\mathcal K_t
$$

隨時間改變，

但存在一組 correspondence：

$$
M_t:
\mathcal K_t
\rightsquigarrow
\mathcal K_{t+1}
$$

保留關鍵功能關係，

則稱：

$$
\{
\mathcal K_t
\}_{t=0}^T
$$

為一條 candidate connected cognitive complex trajectory。

THF 的鎖定對象不是單一：

$$
x,
$$

而是：

$$
\boxed{
\{\mathcal K_t\}_{0:T}.
}
$$

---

# 17. 結構連續性

定義：

$$
S_t
=
S(
\mathcal K_t,
\mathcal K_{t+1}
).
$$

候選可以由：

- node overlap；
- relational overlap；
- goal identity；
- bridge preservation；
- invariant preservation；

構成。

例如：

$$
S_t
=
\alpha J_X
+
\beta J_R
+
\gamma I_G
+
\delta I_{\mathrm{inv}}.
$$

若：

$$
S_t\geq\theta_S
$$

長期成立，

則即使：

$$
U_t\neq U_{t+1},
$$

仍可以說 trajectory 沒有完全離開原 cognitive complex。

---

# 18. THF 的候選形式

定義：

$$
\Theta_{\mathrm{THF}}
=
(
L_K,
\nu_{\mathrm{intra}},
H_{\mathrm{intra}},
\nu_R,
h_{\mathrm{exit}},
S,
G_C,
E_C
).
$$

其中：

- \(L_K\)：complex retention；
- \(\nu_{\mathrm{intra}}\)：域內切換率；
- \(H_{\mathrm{intra}}\)：域內熵；
- \(\nu_R\)：re-indexing rate；
- \(h_{\mathrm{exit}}\)：domain exit hazard；
- \(S\)：structural continuity；
- \(G_C\)：goal continuity；
- \(E_C\)：exit controllability。

因此 hyperfocus 不再是一個單一 scalar。

---

# 19. Goal Continuity

定義高階 goal：

$$
G_t.
$$

如果：

$$
G_t
$$

具有語義／功能連續性：

$$
\operatorname{Sim}(G_t,G_{t+1})\geq\theta_G,
$$

則：

$$
G_C
=
\frac1T
\sum_t
\operatorname{Sim}
(
G_t,G_{t+1}
).
$$

THF 強版本要求：

$$
G_C\uparrow.
$$

否則「一直換題」可能只是 random wandering。

---

# 20. Switching 不能只算次數

假設：

$$
x_i\rightarrow x_j.
$$

至少要問：

### Semantic distance

$$
d_S(x_i,x_j).
$$

### Causal distance

$$
d_C(x_i,x_j).
$$

### Goal distance

$$
d_G(x_i,x_j).
$$

### Domain-exit status

$$
I_{\mathrm{exit}}.
$$

因此：

$$
\boxed{
\text{switch count alone is insufficient}.
}
$$

---

# 21. 三種 switching

## Distractor Switching

$$
x_i\in U_G
\rightarrow
y\notin U_G,
$$

且：

$$
\rho(y,G)\approx0.
$$

---

## Exploratory Switching

$$
x_i\rightarrow x_j,
$$

$$
x_i,x_j\in U_G,
$$

並增加：

$$
\operatorname{Reach}^{(k)}.
$$

---

## Regulatory Switching

當局部 engagement：

$$
E_i(t)
$$

下降，

主體切到：

$$
x_j\in U_G
$$

以維持整體 domain engagement。

第三種正是本文最有風險的新命題。

---

# 22. Topic Rotation as Focus Maintenance Conjecture（TRFMC）

假設每個局部 topic：

$$
T_i
$$

具有 engagement：

$$
e_i(t).
$$

若持續停留：

$$
e_i(t)
=
e_{i,0}
e^{-\lambda_i t}.
$$

當：

$$
e_i(t)<\theta,
$$

切到同域內：

$$
T_j
$$

使：

$$
e_j(0)>\theta.
$$

若如此循環：

$$
T_1\rightarrow T_2\rightarrow T_3\rightarrow T_1,
$$

整體 domain engagement：

$$
E_U(t)
=
\max_i e_i(t)
$$

可能長期：

$$
E_U(t)>\theta.
$$

因此：

$$
\boxed{
\text{micro-switching}
\rightarrow
\text{macro-focus maintenance}
}
$$

在部分條件可能成立。

---

# 23. TRFMC 的必要條件

不能只看到 switching 就宣稱 regulatory rotation。

至少需要：

1. switches mostly remain within same coherent domain；
2. switching 發生在 local engagement decline 後；
3. switching 後 domain-level engagement 恢復；
4. forced no-switch condition 反而縮短 domain dwell；
5. switching 不顯著降低 goal completion。

形式：

$$
\nu_{\mathrm{intra}}\uparrow
$$

同時：

$$
T_U\uparrow
$$

或至少：

$$
T_U\not\downarrow.
$$

---

# 24. Inverted-U Hypothesis

TRFMC 不預測：

> 越切越好。

更合理：

$$
T_U
=
f(
\nu_{\mathrm{intra}}
)
$$

可能是 inverted-U。

太低：

$$
\nu_{\mathrm{intra}}\approx0
$$

可能因 boredom / local saturation 離開 domain。

適中：

$$
\nu_{\mathrm{intra}}
=
\nu^*
$$

維持 novelty / information gain。

太高：

$$
\nu_{\mathrm{intra}}\gg\nu^*
$$

則：

- reconstruction cost；
- fragmentation；
- unfinished branches；

上升。

因此：

$$
\boxed{
\nu^*
=
\arg\max_\nu
T_U(\nu).
}
$$

---

# 25. Hyperfocus 的「狹窄」需要尺度參數

傳統說：

$$
\text{hyperfocus is narrow}.
$$

但 narrow 相對於什麼？

細尺度：

$$
U^*
$$

可能非常大。

粗尺度：

$$
P(U^*)=z_U
$$

卻只是一個 task。

所以：

$$
\boxed{
\text{narrowness}
=
N(\lambda).
}
$$

Hyperfocus 的 scope 不應脫離：

$$
\lambda
$$

描述。

---

# 26. Pointwise Narrowness vs Domain Narrowness

Pointwise：

$$
|\operatorname{supp}(p(x))|
\approx1.
$$

Domain-level：

$$
|\operatorname{supp}(p(D))|
\approx1,
$$

但：

$$
|\operatorname{supp}(p(x\mid D))|
\gg1.
$$

這兩種在粗糙問卷中都可能被回答：

> 我非常專注在一件事情上。

所以需要新的 measurement resolution。

---

# 27. 超專注與「可退出性」

長時間投入本身不能區分：

$$
\text{chosen persistence}
$$

與：

$$
\text{lock-in}.
$$

因此定義 voluntary exit probe。

在時間：

$$
t_i
$$

要求：

> 若現在有理由停止，你能否在短時間內安全退出並切換？

定義：

$$
\tau_{\mathrm{exit}}
$$

為 voluntary exit latency。

以及：

$$
P_{\mathrm{exit|cue}}.
$$

---

# 28. Exit Controllability

定義：

$$
E_C
=
f(
P_{\mathrm{exit|cue}},
\tau_{\mathrm{exit}},
\text{error after exit}
).
$$

高：

$$
E_C
$$

表示：

$$
\boxed{
\text{deep engagement with retained control}.
}
$$

低：

$$
E_C
$$

表示：

$$
\boxed{
\text{attention lock-in}.
}
$$

THF 不應預設：

$$
E_C
$$

高或低。

它是獨立維度。

---

# 29. Re-entry Controllability

退出後是否能回到：

$$
U^*
$$

也是重要能力。

定義：

$$
\tau_{\mathrm{reentry}}
$$

與：

$$
P_{\mathrm{return}}(\Delta t).
$$

所以完整可控注意不只：

$$
\text{Enter}
$$

與：

$$
\text{Exit}.
$$

還包括：

$$
\boxed{
\text{Enter}
+
\text{Maintain}
+
\text{Traverse}
+
\text{Exit}
+
\text{Re-enter}.
}
$$

---

# 30. 這比「最大化 hyperfocus」更重要

如果未來做 attention engineering，

最佳目標不是：

$$
\max
\text{Hyperfocus Intensity}.
$$

而更可能：

$$
\boxed{
\max
\text{Controllable Attention Allocation}.
}
$$

其中包含：

- target selection；
- depth；
- scope；
- dwell；
- internal mobility；
- monitoring；
- exit；
- re-entry。

---

# 31. Productive Persistence 與 Maladaptive Lock-in

定義 outcome vector：

$$
\mathbf O
=
(
O_{\mathrm{task}},
O_{\mathrm{health}},
O_{\mathrm{social}},
O_{\mathrm{recovery}}
).
$$

其中：

- task output；
- physical / mental cost；
- social cost；
- recovery cost。

因此：

$$
O_{\mathrm{task}}\uparrow
$$

不保證：

$$
O_{\mathrm{total}}\uparrow.
$$

所以：

$$
\boxed{
\text{high productivity}
\neq
\text{adaptive hyperfocus}.
}
$$

---

# 32. 2026 gaming literature 的提醒

2026 年 adult-gaming studies 將 hyperfocus 與：

- flow；
- escapism；
- burnout；
- self-efficacy；

放在同一模型中比較。

這些研究顯示 hyperfocus 可能同時出現在具有正向與負向 outcome 的活動中，而且它與 flow 不宜直接視為同一概念。

因此本文採：

$$
\boxed{
\text{state structure}
\neq
\text{state value}.
}
$$

THF 描述 attention dynamics，

不是直接判定它好或壞。

---

# 33. Pointwise / Domain / Topological 三層模型

整理如下。

## PHF

$$
x_t\approx x^*.
$$

核心：

$$
\text{point retention}.
$$

---

## DHF

$$
x_t\in U^*
$$

長期成立。

核心：

$$
\text{domain retention}.
$$

域內：

$$
\nu_{\mathrm{intra}}
$$

可高可低。

---

## THF

$$
x_t\in U_t
$$

且：

$$
U_t
\rightarrow
U_{t+1}
$$

持續變動，

但：

$$
S(
U_t,U_{t+1}
)
\geq\theta.
$$

核心：

$$
\text{structurally continuous evolving-domain retention}.
$$

---

# 34. 三層不是互斥疾病分類

可能：

$$
PHF\subset DHF\subset THF
$$

在某些形式化下成立。

例如固定單點可以視為 degenerate domain。

固定 domain 可以視為 dynamic domain 的特殊情況。

所以：

$$
\boxed{
\text{PHF and DHF can be limiting cases of THF}.
}
$$

但 empirically 不一定需要 THF 才能解釋 PHF / DHF。

---

# 35. THF 的強判準

候選 THF 至少要求：

$$
L_K\geq\theta_L,
$$

$$
S\geq\theta_S,
$$

$$
G_C\geq\theta_G,
$$

而：

$$
\nu_{\mathrm{intra}}
$$

不限低。

更強版本要求：

$$
\nu_R>0
$$

或：

$$
N_E+N_C+N_G+N_D>0.
$$

也就是 domain 真的在演化。

---

# 36. Topological 不能只因為「很複雜」

若只是：

$$
\text{many topics}
$$

並不叫 topological hyperfocus。

若只是：

$$
\text{fast switching}
$$

也不叫。

THF 需要：

$$
\boxed{
\text{connectivity / neighborhood / structural continuity}
}
$$

有可測內容。

如果：

$$
S
$$

無法估計，

就只能叫：

$$
\text{dynamic-domain focus}.
$$

---

# 37. Null Model 1：Point-Lock Model

假設所有 hyperfocus 的關鍵都可以由：

$$
L_x
$$

與：

$$
h_x
$$

解釋。

如果：

$$
H_{\mathrm{intra}},
\nu_{\mathrm{intra}},
S,\nu_R
$$

完全沒有增量預測，

THF 沒必要。

---

# 38. Null Model 2：Reward-Only Model

假設：

$$
\text{high reward / interest}
\rightarrow
\text{long dwell}.
$$

只需：

$$
V(x)
$$

即可解釋。

若域內 switching 完全由 reward gradient 決定，

且 domain topology 不增加預測，

TRFMC / THF 被削弱。

---

# 39. Null Model 3：Executive Dyscontrol

假設 hyperfocus 主要來自：

$$
\text{difficulty disengaging}.
$$

如果：

$$
\tau_{\mathrm{exit}}
$$

與 executive control measures 已能解釋所有 long dwell，

domain model 沒有必要。

Pimenta 等人的 EF mediation 結果使這個競爭模型尤其重要。

---

# 40. Null Model 4：Flow

假設所有 adaptive-looking long engagement 都是：

$$
\text{flow}.
$$

如果 flow measures 對：

- persistence；
- outcome；
- controllability；

的預測完全吸收 THF variables，

THF 不需要。

但現有 AHQ-D 與 gaming evidence 尚不支持簡單等同。

---

# 41. Null Model 5：Random Topic Switching

一個人可以：

$$
\nu_{\mathrm{switch}}\uparrow
$$

但沒有：

$$
G_C
$$

與：

$$
S.
$$

這是：

$$
\boxed{
\text{fragmentation}
}
$$

不是 THF。

所以 semantic / causal / goal coherence 是必須測的。

---

# 42. Null Model 6：Ordinary Task Switching

若所有：

$$
x_i\rightarrow x_j
$$

都只是固定 task graph 中 ordinary switching，

則：

$$
\mathcal K_t
$$

不需要變。

那最多支持 DHF，

不支持 THF。

---

# 43. Long-Horizon Digital Phenotyping

THF 特別適合用：

$$
\text{long-horizon logs}
$$

測量。

每一個 cognitive event：

$$
e_i
$$

至少標記：

$$
(
t_i,
D_i,
T_i,
G_i,
R_{i,i-1},
O_i,
Y_i
).
$$

其中：

- timestamp；
- domain；
- topic；
- goal；
- relation to previous state；
- operator；
- output type。

---

# 44. Topic Transition Graph

建立：

$$
\mathcal G_{\mathrm{topic}}
=
(V,E).
$$

每個：

$$
v_i
$$

是 topic / cognitive state。

每條：

$$
e_{ij}
$$

具有：

- semantic weight；
- causal weight；
- temporal frequency；
- return probability；
- goal coherence。

然後找：

$$
\boxed{
\text{persistent evolving connected components}.
}
$$

---

# 45. Domain Retention vs Artifact Retention

若使用數位工作資料，

必須分開：

$$
\text{cognitive event}
$$

與：

$$
\text{artifact event}.
$$

一個 AI agent、script、auto-save 或 asynchronous job 可能產生：

$$
A_t
$$

但不代表人類：

$$
H_t
$$

在該時刻切換注意。

因此：

$$
\boxed{
\text{artifact switch}
\neq
\text{human attentional switch}.
}
$$

數位 trace 只能作為代理觀察。

---

# 46. 實驗一：Forced Stability vs Free Rotation

給同一 domain：

$$
U.
$$

Condition A：

必須連續做同一 subtopic：

$$
T_1.
$$

Condition B：

允許在：

$$
T_1,T_2,T_3
$$

間自由旋轉，

但都屬於：

$$
U.
$$

測：

$$
T_U,
$$

$$
O_{\mathrm{task}},
$$

$$
\nu_{\mathrm{exit}},
$$

$$
\text{fatigue},
$$

$$
\text{return probability}.
$$

若：

$$
T_U^{B}
>
T_U^{A}
$$

而 performance 不下降，

支持 TRFMC。

---

# 47. 實驗二：Forced Switching

反過來，

強迫 participants：

$$
T_1\rightarrow T_2\rightarrow T_3
$$

與 self-selected switching 比較。

如果 regulatory switching 的效果只在 self-selected condition 存在，

表示：

$$
\boxed{
\text{timing of switch matters}.
}
$$

而不是「切換本身」有益。

---

# 48. 實驗三：Exit-Control Probe

在 hyperfocus episode 中隨機插入：

$$
\text{exit cue}.
$$

測：

$$
\tau_{\mathrm{exit}},
$$

$$
P_{\mathrm{exit}},
$$

$$
\text{post-switch error},
$$

$$
P_{\mathrm{return}}.
$$

因此可以區分：

### Deep but controllable

$$
L_U\uparrow,
E_C\uparrow.
$$

### Locked-in

$$
L_U\uparrow,
E_C\downarrow.
$$

---

# 49. 實驗四：Resolution Probe

同一 long-duration task，

要求 participant 定期回答：

> 你現在是在處理一個子問題、整個 project，還是更高階 goal？

估計：

$$
\lambda_t.
$$

再和 behavioral / neural scale signatures 比較。

若 internal report 與 objective hierarchy 一致，

支持 multiscale focus model。

---

# 50. 實驗五：Connectivity Destruction

建立 domain：

$$
U
$$

內多個 subtopics。

Experimental condition：

移除關鍵 bridge：

$$
B.
$$

如果：

$$
\nu_{\mathrm{exit}}\uparrow
$$

或：

$$
T_U\downarrow,
$$

表示：

$$
\boxed{
\text{domain connectivity contributes to persistence}.
}
$$

如果完全沒差，

topological interpretation 受損。

---

# 51. 實驗六：Novel Branch Expansion

讓 participant 在 long-focus episode 中遇到新資訊：

$$
y.
$$

若：

$$
y
$$

可被整合進：

$$
U_t
$$

而不造成 domain exit，

記：

$$
E(U_t)\rightarrow U_{t+1}.
$$

測新 branch 是否：

- 保留 goal coherence；
- 後續回返；
- 最終完成；
- 改變原 domain structure。

這是 THF 與固定 DHF 的關鍵分界。

---

# 52. 實驗七：Re-entry

在 long-focus episode 中強制離開：

$$
\Delta t.
$$

再讓 participant 回來。

測：

$$
\tau_{\mathrm{reentry}},
$$

$$
\operatorname{StateRecovery},
$$

$$
P_{\mathrm{return\ to\ branch}}.
$$

高品質 external memory / context cues 可能：

$$
\tau_{\mathrm{reentry}}\downarrow.
$$

這將在 TADC-07 與 AI cognitive scaffolding 接軌。

---

# 53. 八個核心可證偽命題

## TADC5-H1 — Domain Persistence Is Distinct from Point Persistence

存在 episodes：

$$
L_U\uparrow
$$

但：

$$
L_x\downarrow.
$$

若不存在，

DHF 無必要。

---

## TADC5-H2 — High Intra-Domain Entropy Can Coexist with Long Dwell

存在：

$$
H_{\mathrm{intra}}\uparrow
$$

且：

$$
T_U\uparrow.
$$

---

## TADC5-H3 — Intra-Domain Switching Predicts Differently from Exit Switching

$$
\nu_{\mathrm{intra}}
$$

與：

$$
\nu_{\mathrm{exit}}
$$

對 performance / dwell 的效果不同。

---

## TADC5-H4 — Regulatory Rotation

在部分 individuals / tasks：

$$
\nu_{\mathrm{intra}}
$$

存在最佳區間：

$$
\nu^*
$$

使：

$$
T_U
$$

最大。

---

## TADC5-H5 — Structural Continuity Predicts Persistence

$$
S\uparrow
$$

應預測：

$$
P_{\mathrm{return}}\uparrow
$$

與：

$$
\nu_{\mathrm{exit}}\downarrow.
$$

---

## TADC5-H6 — Exit Control Is Independent

同樣：

$$
L_U
$$

的人可以具有不同：

$$
E_C.
$$

如果完全同一維度，

exit controllability 沒必要獨立建模。

---

## TADC5-H7 — THF Adds Prediction Beyond Reward / Flow / EF

加入：

$$
S,
H_{\mathrm{intra}},
\nu_R,
G_C
$$

後，

模型應對 long-horizon focus behavior 提供增量預測。

---

## TADC5-H8 — Dynamic Domain Beats Fixed Domain

在至少部分 episodes：

$$
M_{\mathrm{dynamic-domain}}
>
M_{\mathrm{fixed-domain}}
$$

的 out-of-sample prediction。

若否，

THF 只需降級成 DHF。

---

# 54. 什麼結果會殺掉 Topological Hyperfocus？

## F1 — Point Model Suffices

如果：

$$
L_x,h_x
$$

足以預測所有 hyperfocus outcome，

THF 多餘。

---

## F2 — No High-Entropy Persistent Episodes

若：

$$
H_{\mathrm{intra}}\uparrow
$$

總是導致：

$$
T_U\downarrow,
$$

TRFMC 受否定。

---

## F3 — Switching Is Always Distracting

若控制其他變項後：

$$
\nu_{\mathrm{intra}}\uparrow
\Rightarrow
O_{\mathrm{task}}\downarrow
$$

普遍成立，

regulatory switching 假說失敗。

---

## F4 — Domain Structure Adds No Prediction

若：

$$
S
$$

與：

$$
G_C
$$

無法預測 persistence / return / performance，

「connected cognitive complex」只是漂亮語言。

---

## F5 — Dynamic Domain Is Unidentifiable

如果：

$$
U_t
$$

只能由研究者事後任意畫出，

沒有 independent measurement，

THF 不可測。

---

## F6 — Flow Absorbs THF

若 flow measure + reward + skill-demand balance 完全吸收 THF 的預測，

不需要新構念。

---

## F7 — Executive Dyscontrol Absorbs THF

若：

$$
\tau_{\mathrm{exit}}
$$

與 executive-control measures 已能完整解釋 episode dynamics，

THF 無增量。

---

# 55. Hyperfocus 不是一年不間斷的單一 episode

長時間尺度必須拆開。

一個人一年長期投入同一 broad domain，

不應寫：

$$
\text{one-year hyperfocus episode}.
$$

更合理：

$$
\boxed{
\text{recurrent focus episodes}
+
\text{persistent domain attachment}
+
\text{return dynamics}.
}
$$

因此：

$$
T_{\mathrm{episode}}
$$

與：

$$
T_{\mathrm{attachment}}
$$

必須分開。

---

# 56. Persistent Domain Attachment（PDA）

定義跨 episode：

$$
P_{\mathrm{return}}
(
U
\mid
\Delta t
).
$$

若數週、數月反覆：

$$
P_{\mathrm{return}}\uparrow,
$$

可以叫：

$$
\boxed{
\text{Persistent Domain Attachment}
}
$$

而不是把它硬算成單次 hyperfocus。

這能避免時間尺度混亂。

---

# 57. Episode–Attachment 二層模型

短尺度：

$$
H_t
=
\text{hyperfocus episode state}.
$$

長尺度：

$$
A_T
=
\text{domain attachment state}.
$$

因此：

$$
P(
H_t
\mid
A_T
)
$$

可能很高，

但：

$$
H_t
$$

會中斷於：

- sleep；
- meals；
- other duties；
- recovery；
- unrelated tasks。

這是正常 time-series 分層。

---

# 58. THF 與 ADHD 的關係

現有研究支持：

$$
\boxed{
\text{higher ADHD traits}
\leftrightarrow
\text{higher reported hyperfocus}
}
$$

在多個樣本中成立。

但 TADC-05 不提出：

$$
\boxed{
\text{ADHD}
\Rightarrow
\text{THF}.
}
$$

也不提出：

$$
\boxed{
\text{THF}
\Rightarrow
\text{ADHD}.
}
$$

THF 是一般 attention-dynamics conjecture。

ADHD 可作為一個 future test population。

---

# 59. 2026 Cognitive-Affective 結果應如何使用？

Samson 等人的研究可以支持：

$$
\boxed{
\text{hyperfocus should not be modeled
without flexibility / switching dimensions}.
}
$$

但該研究：

- sample \(N=96\)；
- switching task 為 cognitive-affective flexibility；
- mediation 為統計關係；
- 不直接測 THF domain topology。

所以不能寫：

> 該研究證明 topological hyperfocus。

正確說法只到：

> 它使「hyperfocus 與 switching dynamics 完全無關」的簡單模型更不充分。

---

# 60. Hyperfocus measurement 的下一代向量

本文建議由單 scalar：

$$
HF
$$

擴展為：

$$
\boxed{
\mathbf H
=
(
I,
T,
S,
L_D,
\nu_I,
\nu_E,
H_I,
R,
E_C,
R_C,
C_L
)
}
$$

其中：

- \(I\)：intensity；
- \(T\)：episode duration；
- \(S\)：scope；
- \(L_D\)：domain retention；
- \(\nu_I\)：intra-domain switching；
- \(\nu_E\)：exit switching；
- \(H_I\)：internal entropy；
- \(R\)：re-indexing；
- \(E_C\)：exit controllability；
- \(R_C\)：re-entry controllability；
- \(C_L\)：cost load。

---

# 61. 這不是要取代 AHQ-D

AHQ-D 的目的：

$$
\boxed{
\text{measure dispositional hyperfocus tendency}.
}
$$

TADC-05 的目的：

$$
\boxed{
\text{model within-episode dynamics and multiscale structure}.
}
$$

兩者可以互補。

例如：

$$
AHQ\text{-}D
$$

測 trait，

而：

$$
\mathbf H(t)
$$

測 state dynamics。

---

# 62. Ecological Measurement

未來最適合：

- ecological momentary assessment；
- computer interaction logs；
- eye tracking；
- task event streams；
- wearables；
- neural state decoding；
- experience sampling。

但不能把：

$$
\text{screen time}
$$

直接當：

$$
\text{hyperfocus time}.
$$

也不能把：

$$
\text{keyboard activity}
$$

直接當：

$$
\text{human cognitive activity}.
$$

---

# 63. 最小 THF 判定程序

候選研究程序：

### Step 1

識別 episode：

$$
[t_0,t_1].
$$

### Step 2

建立 topic / state sequence：

$$
x_{t_0:t_1}.
$$

### Step 3

估計 effective domain：

$$
U_t.
$$

### Step 4

測：

$$
L_U,
\nu_{\mathrm{intra}},
\nu_{\mathrm{exit}},
H_{\mathrm{intra}}.
$$

### Step 5

估計：

$$
S_t,G_C.
$$

### Step 6

測：

$$
E_C,R_C.
$$

### Step 7

和：

- PHF；
- reward；
- flow；
- executive dyscontrol；
- random switching；

模型比較。

只有最後 THF 有增量：

$$
\Delta\operatorname{Prediction}>0
$$

才保留。

---

# 64. TADC-05 與前四篇的統一

TADC-01：

$$
\mathcal C_t
\rightarrow
\mathcal C_{t+1}.
$$

TADC-02：

$$
D_t
=
D(
G_t,\mathcal R_t,\kappa_t,\lambda_t
).
$$

TADC-03：

$$
\mathcal O
=
\{E,C,T,G,D,R\}.
$$

TADC-04：

$$
U^{(\lambda_f)}
\leftrightarrow
z_U^{(\lambda_c)}.
$$

TADC-05：

$$
\boxed{
\text{focus can persist on the evolving domain,
not merely on a fixed point}.
}
$$

所以：

$$
\boxed{
\mathcal K_0
\overset{O_1}{\longrightarrow}
\mathcal K_1
\overset{O_2}{\longrightarrow}
\cdots
\overset{O_n}{\longrightarrow}
\mathcal K_n
}
$$

可以整段都屬於同一 THF episode，

只要：

$$
S_t
$$

與：

$$
G_C
$$

保持足夠高。

---

# 65. 最核心的新區分

本文真正要留下的不是新名詞，

而是：

$$
\boxed{
\text{focus persistence}
\neq
\text{state immobility}.
}
$$

高 focus persistence 可以伴隨：

$$
\boxed{
\text{high state mobility}.
}
$$

只要 mobility 大多發生在：

$$
\boxed{
\text{same coherent evolving cognitive complex}.
}
$$

---

# 66. 結論

本文將 hyperfocus 的最小模型從：

$$
\boxed{
\text{long dwell on one point}
}
$$

擴展為三層：

$$
\boxed{
\textbf{PHF — Pointwise Hyperfocus}
}
$$

$$
\boxed{
\textbf{DHF — Domain Hyperfocus}
}
$$

$$
\boxed{
\textbf{THF — Topological Hyperfocus}.
}
$$

PHF 強調：

$$
L_x\uparrow.
$$

DHF 強調：

$$
L_U\uparrow
$$

但允許：

$$
\nu_{\mathrm{intra}}\uparrow.
$$

THF 更進一步允許：

$$
U_t\neq U_{t+1},
$$

只要：

$$
S(
U_t,U_{t+1}
)
$$

與：

$$
G_C
$$

保持。

因此本文提出：

$$
\boxed{
H_{\mathrm{macro}}\downarrow
\quad\land\quad
H_{\mathrm{micro}}\uparrow
}
$$

可以是合法的 attention configuration。

這意味著：

$$
\boxed{
\text{high internal switching}
\not\Rightarrow
\text{low high-level focus}.
}
$$

本文還提出：

$$
\boxed{
\textbf{Topic Rotation as Focus Maintenance Conjecture}
}
$$

即某些低成本域內 switching 可能反而延長 domain-level engagement。

但這一命題必須接受非常強的反證：

如果：

- switching 永遠降低 persistence；
- fixed point-lock model 已充分；
- flow / reward / executive dyscontrol 完整吸收所有 effect；
- domain connectivity 沒有預測力；
- evolving-domain structure 無法被獨立識別；

則：

$$
\boxed{
\text{Topological Hyperfocus should be abandoned}.
}
$$

因此本文不是要把：

> 「任何一直做很多事的人」

都叫作 hyperfocus。

而是提出：

> **如果長時間專注可以發生在一個持續變形、展開、收斂與內部遍歷的認知域上，那麼「注意是否穩定」不能只由局部 task switch 次數判定。**

真正應測的是：

$$
\boxed{
\text{where the trajectory remains,
what structure it preserves,
how it exits,
and whether it can return}.
}
$$

也就是：

$$
\boxed{
\text{Retention}
+
\text{Mobility}
+
\text{Continuity}
+
\text{Control}.
}
$$

這四個維度共同構成 TADC-05 對 hyperfocus 的核心重寫。

---

# 參考文獻

1. Hupfeld KE, Abagis TR, Shah P. **Living "in the zone": hyperfocus in adult ADHD.** *Attention Deficit and Hyperactivity Disorders*. 2019;11(2):191–208. doi:10.1007/s12402-018-0272-y. PMID: 30267329.  
2. Hupfeld KE, Osborne JB, Tran QT, Hyatt HW, Abagis TR, Shah P. **Validation of the dispositional adult hyperfocus questionnaire (AHQ-D).** *Scientific Reports*. 2024;14:19460. doi:10.1038/s41598-024-70028-y. PMID: 39169147.  
3. Garcia Pimenta M, Gruhnert RK, Fuermaier ABM, Groen Y. **The role of executive functions in mediating the relationship between adult ADHD symptoms and hyperfocus in university students.** *Research in Developmental Disabilities*. 2024;144:104639. doi:10.1016/j.ridd.2023.104639. PMID: 38039699.  
4. Samson JL, Rochat L, Perroud N, Debbané M. **Cognitive-affective flexibility in adult ADHD: Links to emotion reactivity and hyperfocus.** *Journal of Affective Disorders Reports*. 2026;24:101047. doi:10.1016/j.jadr.2026.101047.  
5. Pyszkowska A, Nowacki A, Dziura N. **Game on but pay the price: Hyperfocus, flow, escapism, self-efficacy, and burnout among video gamers with ADHD traits.** *Research in Developmental Disabilities*. 2026;170:105241. doi:10.1016/j.ridd.2026.105241. PMID: 41650538.  
6. Pyszkowska A, Nowacki A, Dziura N. **Determinants of hyperfocus in the context of escapism and gaming motivations, flow, and ADHD symptoms among adult video gamers.** *Research in Developmental Disabilities*. 2026;174:105321. doi:10.1016/j.ridd.2026.105321. PMID: 42229071.  
7. Li Y, Chen J, Zheng X, Liu J, Peng C, Liao Y. **Functional Near-Infrared Spectroscopy Evidence of Prefrontal Regulation of Cognitive Flexibility in Adults With ADHD.** *Journal of Attention Disorders*. 2023;27(11):1196–1206. doi:10.1177/10870547231154902. PMID: 36799464.  
8. Peer M, Epstein RA. **Cognitive maps for hierarchical spaces in the human brain.** *Cerebral Cortex*. 2025;35(9):bhaf261. doi:10.1093/cercor/bhaf261. PMID: 40982478.  
9. Leach SC, Chen X, Hwang K. **Hierarchical Reconfiguration of Neurocognitive Task Set Representations Mediates Cognitive Flexibility.** *Journal of Neuroscience*. 2026. doi:10.1523/JNEUROSCI.0113-26.2026. PMID: 42276789.  
10. Qiu Y, Li H, Liao J, et al. **Forming cognitive maps for abstract spaces: the roles of the human hippocampus and orbitofrontal cortex.** *Communications Biology*. 2024;7:517. doi:10.1038/s42003-024-06214-5. PMID: 38693344.  
11. Behrens TEJ, Muller TH, Whittington JCR, et al. **What Is a Cognitive Map? Organizing Knowledge for Flexible Behavior.** *Neuron*. 2018;100(2):490–509. doi:10.1016/j.neuron.2018.10.002.  

---

## 與系列的關係

**已完成：**

- TADC-01：《注意力不是單點選擇——可變認知空間與注意—空間轉換猜想》
- TADC-02：《動態認知域——領域作為局部座標圖》
- TADC-03：《拓樸注意力六算子——展開、收斂、遍歷、黏合、切離與重索引》
- TADC-04：《嵌套注意域與觀察尺度——宏觀／微觀的相對性與多尺度重索引》
- TADC-05：《從單點超專注到拓樸超專注——域級持續性、內部高熵遍歷與可控退出》

**下一篇：**

- TADC-06：《關係優先認知與跨域連續性》

後續：

- TADC-07：《外部認知支架與人—AI 認知拓樸》
- TADC-08：《拓樸注意力的測量、反證與工程化》

---

**狀態：** TADC-05 v0.1  
**原始人體／臨床數據：** 無  
**理論狀態：** 猜想／研究綱領；未經實驗驗證  
**臨床狀態：** Topological Hyperfocus 不是正式臨床術語或診斷構念  
**拓樸狀態：** connected cognitive complex / structural continuity 為候選操作化，尚未建立嚴格拓樸分類
