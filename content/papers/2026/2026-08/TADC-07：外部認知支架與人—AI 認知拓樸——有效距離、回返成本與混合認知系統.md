# TADC-07：外部認知支架與人—AI 認知拓樸——有效距離、回返成本與混合認知系統

**英文題名：** External Cognitive Scaffolds and Human–AI Cognitive Topology: Effective Distance, Re-entry Cost, and Hybrid Cognitive Systems  
**系列：** Topological Attention and Dynamic Cognitive Domains — Conjecture Series（TADC）  
**中文系列名：** 拓樸注意力與動態認知域命題系列  
**編號：** TADC-07  
**版本：** v0.1  
**日期：** 2026-08-17  
**作者：** Neo.K（許筌崴）  
**協作：** GPT-5.6 Sol  
**文件性質：** 理論命題／人—AI 混合認知模型／可證偽研究綱領  
**文獻檢索截點：** 2026-08-17  

---

## 摘要

人類長期使用紙筆、書籍、索引、提醒器、搜尋系統與其他人來降低內部記憶與推理負擔。認知科學通常將其中一部分描述為 cognitive offloading：透過外部行動或環境資源改變資訊處理需求。生成式 AI、長期記憶系統與 agent architecture 則進一步提供傳統外部記憶工具較少具備的功能：主動檢索、重新表示、跨資料源建立橋接、生成候選路徑、保持多個研究分支，以及在使用者未直接處理某支線時持續執行局部工作。

本文提出一個比「AI 提升工作效率」更強、但也更需要反證的命題：

> **外部認知支架可能改變一個人—工具混合系統的有效認知可達結構，而不只是提高某個既有認知節點上的處理速度。**

本文定義人類內部認知結構：

$$
\mathcal C_t^H
=
(
X_t^H,
\mathcal R_t^H,
\kappa_t^H,
\mathcal N_t^H,
A_t^H,
G_t
),
$$

外部支架：

$$
\mathcal S_t^E
=
(
M_t,
I_t,
Q_t,
P_t
),
$$

以及 AI / Agent 層：

$$
\mathcal A_t^{AI}
=
(
X_t^{AI},
R_t^{AI},
\Pi_t,
V_t
).
$$

三者形成候選混合認知系統：

$$
\boxed{
\mathcal H_t
=
\mathcal C_t^H
\oplus
\mathcal S_t^E
\oplus
\mathcal A_t^{AI}.
}
$$

本文不以「extended mind」作為已成立前提，也不主張 AI 系統與人腦具有同等心理或主體地位；符號 \(\oplus\) 僅表示在特定任務中，人類行為的有效資訊處理路徑可以跨越內部與外部節點。

本文提出三個核心猜想：

1. **Effective Cognitive Distance Transformation Conjecture（ECDTC）**：外部支架可以改變任務中的有效認知距離；
2. **Re-entry Topology Conjecture（RTC）**：可尋址、可恢復的外部狀態可以降低中斷後回返舊分支的重建成本；
3. **Hybrid Reachability Expansion Conjecture（HREC）**：AI / agent support 可擴張混合系統在有限時間與資源下實際可到達的問題狀態集合。

定義內部距離：

$$
d_H(x,y\mid G),
$$

以及混合系統有效距離：

$$
d_{\mathrm{eff}}
(
x,y
\mid
G,\mathcal S^E,\mathcal A^{AI}
).
$$

若：

$$
d_{\mathrm{eff}}
<
d_H,
$$

則定義 cognitive-distance gain：

$$
\boxed{
\Gamma_d
=
d_H-d_{\mathrm{eff}}.
}
$$

本文進一步區分四種 AI / 外部支架作用：Externalization、Retrieval、Bridge Discovery、Parallel Execution。前兩者接近傳統 cognitive offloading；後兩者可能更直接改變關係圖、可達域與系統級並行分支數。

然而，外部支架也帶來 verification、coordination、miscalibration、dependency、internal-learning loss 與 motivational costs。因此本文提出：

$$
\boxed{
K_{\mathrm{eff}}
=
K_H
-
\Delta K_{\mathrm{memory}}
-
\Delta K_{\mathrm{retrieval}}
-
\Delta K_{\mathrm{reentry}}
+
K_{\mathrm{verification}}
+
K_{\mathrm{coordination}}
+
K_{\mathrm{dependency}}.
}
$$

現有 cognitive-offloading meta-analysis 支持外部支架可改善特定記憶任務表現並降低個體差異，但研究亦顯示 offloading 可能降低內部編碼或後續無支架表現。2025 年 PNAS 的大規模高中數學 field experiment 更顯示，無 guardrails 的 GPT 支援可在練習時大幅提升表現，卻可能在移除 AI 後降低獨立考試表現；有教學 guardrails 的 AI tutor 能大幅減輕此負面效果。2025 年四項 online experiments（總 \(N=3562\)）亦顯示 human–GenAI collaboration 的即時產出優勢不必然轉移到後續 human-only tasks，並伴隨動機與無聊感變化。2026 年複雜臨床推理實驗則顯示 human–AI collaboration 可提高平均準確率並降低主觀 cognitive burden，但合作失敗時常與人類接受錯誤 AI insight 有關。

因此本文的核心不是：

$$
\text{AI}\Rightarrow\text{better cognition}.
$$

而是：

$$
\boxed{
\text{AI changes the cost structure and reachable paths
of cognition under specific interface,
memory, verification, and control conditions.}
}
$$

如果混合系統模型不能比普通「更快檢索／更多資訊／較低工作記憶負荷」模型提供額外預測，則本文所稱「認知拓樸變換」應被降級。

**關鍵詞：** cognitive offloading；human–AI collaboration；external memory；agents；cognitive scaffolding；task switching；re-entry；distributed cognition；effective cognitive distance；human–AI topology；TADC

---

# 0. 邊界聲明

本文不是臨床研究、醫療建議、AI 安全保證或人類能力增強的既成事實報告。

本文提出的是：

$$
\boxed{
\text{general human–tool cognitive architecture conjecture}.
}
$$

本文不主張：

$$
\boxed{
\text{AI is part of the human brain}.
}
$$

不主張：

$$
\boxed{
\text{human attention becomes literally parallel
because AI agents work in parallel}.
}
$$

也不主張：

$$
\boxed{
\text{using AI necessarily improves learning,
memory, creativity, or reasoning}.
}
$$

本文只問：

> 若外部系統能保存、檢索、轉換、連接並執行認知相關狀態，那麼「人類完成一個任務時真正可走的有效資訊路徑」是否因此改變？

---

# 1. 從 TADC-06 到外部支架

TADC-06 定義：

$$
d_{\mathrm{rel}}(x,y\mid G)
$$

作為 goal-conditioned relational cognitive distance。

但此前主要假設：

$$
x,y
$$

都存在於主體當前可使用的內部認知結構中。

現在加入外部系統：

- notes；
- file system；
- search engine；
- knowledge graph；
- LLM；
- memory-augmented assistant；
- autonomous / semi-autonomous agent；
- shared workspace。

此時從：

$$
x
$$

到：

$$
y
$$

的最佳路徑未必完全位於：

$$
\mathcal C^H.
$$

---

# 2. 人類內部認知結構

沿用 TADC：

$$
\mathcal C_t^H
=
(
X_t^H,
\mathcal R_t^H,
\kappa_t^H,
\mathcal N_t^H,
A_t^H,
G_t
).
$$

其中：

- \(X_t^H\)：人類當前可內部操作的 cognitive objects；
- \(\mathcal R_t^H\)：內部有效 relations；
- \(\kappa_t^H\)：內部可達強度；
- \(\mathcal N_t^H\)：內部 neighborhoods；
- \(A_t^H\)：當前 active set；
- \(G_t\)：高階 goal。

---

# 3. 外部支架

定義：

$$
\mathcal S_t^E
=
(
M_t,
I_t,
Q_t,
P_t
).
$$

其中：

- \(M_t\)：external memory state；
- \(I_t\)：index / address structure；
- \(Q_t\)：retrieval mechanism；
- \(P_t\)：provenance / persistence structure。

最簡紙本筆記：

$$
\mathcal S^E
$$

已具有：

$$
M_t
$$

與部分：

$$
I_t.
$$

搜尋引擎強化：

$$
Q_t.
$$

版本控制與資料庫強化：

$$
P_t.
$$

---

# 4. AI / Agent 層

生成式 AI 不只儲存既有資料。

定義：

$$
\mathcal A_t^{AI}
=
(
X_t^{AI},
R_t^{AI},
\Pi_t,
V_t
).
$$

其中：

- \(X_t^{AI}\)：AI 可生成或暫存的候選 states；
- \(R_t^{AI}\)：AI 建議的 relations / bridges；
- \(\Pi_t\)：AI / agent operation policy；
- \(V_t\)：verification state。

因此 AI 可以候選地：

1. retrieve；
2. transform；
3. propose；
4. branch；
5. execute；
6. summarize；
7. critique；
8. reconnect。

---

# 5. 混合認知系統

定義：

$$
\boxed{
\mathcal H_t
=
\mathcal C_t^H
\oplus
\mathcal S_t^E
\oplus
\mathcal A_t^{AI}.
}
$$

這裡：

$$
\oplus
$$

不是代數直和的嚴格宣告。

它表示：

> 在任務執行中，資訊處理路徑可以跨 human-internal、external-store 與 AI-computation 三種節點。

---

# 6. 有效狀態集合

令：

$$
X_t^+
=
X_t^H
\cup
X_t^E
\cup
X_t^{AI}.
$$

這是一個 task-effective state set。

它不表示：

$$
X_t^E
$$

和：

$$
X_t^H
$$

具有相同心理性質。

只是：

$$
\boxed{
\text{both can causally support task completion}.
}
$$

---

# 7. 混合關係圖

建立：

$$
\mathcal G_t^+
=
(
X_t^+,
E_H,
E_E,
E_{AI},
E_{HE},
E_{HA},
E_{EA}
).
$$

其中：

- \(E_H\)：human-internal relation；
- \(E_E\)：external-memory links；
- \(E_{AI}\)：AI-generated relation；
- \(E_{HE}\)：human ↔ external memory；
- \(E_{HA}\)：human ↔ AI；
- \(E_{EA}\)：external state ↔ AI。

---

# 8. 有效認知距離

內部-only：

$$
d_H(x,y\mid G).
$$

混合系統：

$$
\boxed{
d_{\mathrm{eff}}
(
x,y
\mid
G,\mathcal H_t
)
=
\min_{\gamma\subseteq\mathcal G_t^+}
K(\gamma).
}
$$

因此最佳 path 可以是：

$$
x_H
\rightarrow
m_E
\rightarrow
q_{AI}
\rightarrow
y_H.
$$

---

# 9. Effective Cognitive Distance Transformation Conjecture（ECDTC）

ECDTC 宣稱：

> 可用外部支架會使至少部分 task-state pairs 的有效認知距離系統性改變。

形式：

$$
\boxed{
d_{\mathrm{eff}}
(
x,y\mid G,\mathcal H
)
\neq
d_H(x,y\mid G).
}
$$

若：

$$
d_{\mathrm{eff}}<d_H,
$$

定義：

$$
\boxed{
\Gamma_d
=
d_H-d_{\mathrm{eff}}
>0.
}
$$

---

# 10. 這不是「AI 讓人變聰明」的同義詞

若：

$$
\Gamma_d>0,
$$

只能表示：

> 在給定工具可用時，完成某個 transition 的有效成本下降。

這不保證：

- unaided reasoning 變強；
- internal memory 變強；
- skill acquisition 變強；
- long-term learning 變強。

所以：

$$
\boxed{
\text{augmented performance}
\neq
\text{internalized capability}.
}
$$

---

# 11. Cognitive Offloading 的既有基礎

Risko 與 Gilbert 將 cognitive offloading 定義為利用 physical action 改變 task 的 information-processing requirements，以降低 cognitive demand。

後續 intention-offloading 與 memory-offloading 研究已反覆顯示：

$$
\boxed{
\text{external reminders can improve
performance on supported memory tasks}.
}
$$

因此 TADC-07 不需要重新發明：

$$
\text{external memory helps memory}.
$$

真正的新問題是：

> 可尋址、可重組、可生成的外部系統是否還會改變 branch reachability 與 cognitive switching geometry？

---

# 12. 2026 Cognitive-Offloading Meta-analysis

Burnett 與 Richmond 的 meta-analysis 聚合 memory-based cognitive offloading studies。

結果指出：

- offloading 整體可改善 memory-task performance；
- forced offloading 的 benefit 較 choice offloading 大；
- offloading 也降低 performance 的 interindividual variability；
- 效果依 task design、prospective / retrospective memory 等因素而變。

這支持：

$$
\boxed{
\text{external support changes effective task performance}.
}
$$

但 meta-analysis 不證明：

$$
\boxed{
\text{cognitive topology changes}.
}
$$

---

# 13. Offloading 是決策，不只是工具有沒有存在

Gilbert（2024）提出 value-based cognitive-offloading model：

人類在：

$$
\text{internal memory cost}
$$

與：

$$
\text{external reminder cost}
$$

之間做 trade-off。

可寫：

$$
U_E
=
V_{\mathrm{remember}}
-
K_{\mathrm{external}},
$$

$$
U_H
=
V_{\mathrm{remember}}
-
K_{\mathrm{internal}}.
$$

選擇：

$$
\max(U_E,U_H).
$$

因此外部支架是否改變 cognition，

還取決於：

$$
\boxed{
\text{whether the user chooses and knows how to use it}.
}
$$

---

# 14. Metacognitive Calibration

2025 MOOT 研究顯示：

offloading 策略品質和：

- externalization cost；
- memory accuracy；

有系統關係。

2026 的 metacognitive-training experiment 進一步顯示：

短期 prediction + feedback training 可改善 metacognitive calibration 與更 optimal reminder-setting。

所以：

$$
\boxed{
\text{tool availability}
\neq
\text{optimal tool use}.
}
$$

需要：

$$
\boxed{
\text{metacognitive control}.
}
$$

---

# 15. 四種外部支架作用

TADC-07 將外部系統拆成四類功能：

$$
\boxed{
\mathcal F_E
=
\{
E_x,R_x,B_x,P_x
\}.
}
$$

分別：

1. Externalization；
2. Retrieval；
3. Bridge Discovery；
4. Parallel Execution。

---

# 16. Externalization

將：

$$
x_H
$$

寫入：

$$
m_E.
$$

形式：

$$
W:
x_H
\rightarrow
m_E.
$$

外部化可以降低：

$$
K_{\mathrm{maintenance}}.
$$

---

# 17. Retrieval

需要時：

$$
Q:
m_E
\rightarrow
\widetilde x_H.
$$

如果：

$$
I_t
$$

良好，

則：

$$
K_{\mathrm{retrieval}}\downarrow.
$$

但：

$$
\widetilde x_H
$$

不必等於原：

$$
x_H.
$$

仍有：

$$
\boxed{
\text{reconstruction error}.
}
$$

---

# 18. Bridge Discovery

AI 可以給：

$$
x
$$

提出候選：

$$
y_1,\ldots,y_n
$$

以及：

$$
R_{xy}.
$$

因此：

$$
B_x:
\mathcal G_t
\rightarrow
\widetilde{\mathcal G}_{t+1}.
$$

這是 TADC-06：

$$
\text{Relation-First Cognition}
$$

最直接的人—AI擴展。

---

# 19. Bridge Discovery 不是有效 Bridge

AI 提出：

$$
R_{xy}^{AI}
$$

不代表：

$$
R_{xy}^{AI}
$$

是真的。

所以：

$$
\boxed{
\text{proposed edge}
\neq
\text{validated edge}.
}
$$

必須有：

$$
V(R_{xy}^{AI}).
$$

---

# 20. Parallel Execution

agent system 可以同時執行：

$$
B_1,B_2,\ldots,B_n.
$$

例如：

- branch 1 搜尋；
- branch 2 寫 code；
- branch 3 驗證 citation；
- branch 4 整理文檔。

因此 system-level activity：

$$
\nu_S
$$

可以很高。

---

# 21. AI 平行不等於人類注意力平行

定義：

$$
\nu_H
=
\text{human attentional transition rate},
$$

$$
\nu_S
=
\text{hybrid-system branch event rate}.
$$

可能：

$$
\boxed{
\nu_S\gg\nu_H.
}
$$

這不代表：

$$
\boxed{
\text{human working attention became n-way parallel}.
}
$$

而是：

$$
\boxed{
\text{execution parallelism moved outside the human bottleneck}.
}
$$

---

# 22. Human Attention / System Throughput 分離

人類層：

$$
H_t.
$$

Agent / system 層：

$$
S_t.
$$

Artifact 層：

$$
A_t.
$$

因此：

$$
\boxed{
A_t
\neq
S_t
\neq
H_t.
}
$$

大量 commits、files 或 agent events 不能直接換算成人類 cognitive switches。

---

# 23. Hybrid Reachability Expansion Conjecture（HREC）

在有限時間：

$$
T
$$

與資源：

$$
B
$$

下，

人類內部可達集合：

$$
\operatorname{Reach}_H^{T,B}(x).
$$

加入支架：

$$
\operatorname{Reach}_+^{T,B}(x).
$$

HREC 宣稱：

$$
\boxed{
\operatorname{Reach}_+^{T,B}(x)
\supset
\operatorname{Reach}_H^{T,B}(x)
}
$$

在部分 task conditions 成立。

---

# 24. Reachability Gain

定義：

$$
\Gamma_R
=
\frac{
|
\operatorname{Reach}_+^{T,B}
|
-
|
\operatorname{Reach}_H^{T,B}
|
}{
|
\operatorname{Reach}_H^{T,B}
|
}.
$$

若：

$$
\Gamma_R>0,
$$

混合系統在同資源窗內能探索更多狀態。

但：

$$
\boxed{
\text{more reachable}
\neq
\text{more correct}.
}
$$

---

# 25. Reachability Precision

定義：

$$
P_R
=
\frac{
|\operatorname{Reach}_{\mathrm{valid}}|
}{
|\operatorname{Reach}_{\mathrm{all}}|
}.
$$

AI 可能：

$$
\Gamma_R\uparrow
$$

但：

$$
P_R\downarrow.
$$

即產生大量錯誤 branch。

所以：

$$
\boxed{
\text{reachability}
+
\text{precision}
}
$$

必須共同測。

---

# 26. 外部支架與任務中斷

task-interruption literature 已反覆觀察：

$$
\boxed{
\text{resumption cost}.
}
$$

中斷後回到原 task：

- reaction time 增加；
- errors 可能增加；
- working-memory / attentional reorientation 成本增加。

2024 的 interruption study 亦支持 suspended task goal 在切換後具有 persisting activation / inhibition-related dynamics。

因此：

$$
\boxed{
\text{returning to a task is not free}.
}
$$

---

# 27. Re-entry Cost

對 branch：

$$
b,
$$

定義：

$$
K_{\mathrm{reentry}}(b)
=
K_{\mathrm{locate}}
+
K_{\mathrm{retrieve}}
+
K_{\mathrm{reconstruct}}
+
K_{\mathrm{verify}}
+
K_{\mathrm{resume}}.
$$

傳統多專案工作中：

$$
K_{\mathrm{reconstruct}}
$$

往往很高。

---

# 28. Re-entry Topology Conjecture（RTC）

若 external system 保存：

- branch identity；
- last state；
- dependencies；
- unresolved questions；
- next action；
- provenance；

則：

$$
K_{\mathrm{locate}}\downarrow,
$$

$$
K_{\mathrm{retrieve}}\downarrow,
$$

$$
K_{\mathrm{reconstruct}}\downarrow.
$$

RTC 宣稱：

$$
\boxed{
K_{\mathrm{reentry}}^{E}
<
K_{\mathrm{reentry}}^{H}
}
$$

在適當 external-state design 下成立。

---

# 29. External Memory 不只是 Storage Capacity

如果只有容量：

$$
|M|\uparrow
$$

但沒有：

$$
I_t,
Q_t,
P_t,
$$

則：

$$
K_{\mathrm{retrieval}}
$$

仍可很高。

因此：

$$
\boxed{
\text{memory capacity}
\neq
\text{addressable cognitive support}.
}
$$

TADC-07 特別重視：

$$
\boxed{
\text{addressability}.
}
$$

---

# 30. Addressability

定義：

$$
A_M(b)
=
P(
\text{correct state retrieved}
\mid
\text{branch query }b
).
$$

高：

$$
A_M
$$

才真正降低：

$$
K_{\mathrm{reentry}}.
$$

大型 archive 若沒有索引：

$$
|M|\uparrow
$$

但：

$$
A_M\downarrow,
$$

可能反而造成負擔。

---

# 31. Branch Persistence

branch：

$$
b_i
$$

在時間：

$$
t
$$

被暫停。

若：

$$
P(
b_i
\text{ recoverable at }
t+\Delta
)
$$

因 external memory 上升，

則稱：

$$
\boxed{
\text{branch persistence gain}.
}
$$

定義：

$$
\Gamma_B
=
P_E(\text{return})
-
P_H(\text{return}).
$$

---

# 32. External State as Cognitive Bookmark

一個高品質 bookmark：

$$
m_b
$$

至少包含：

$$
m_b
=
(
G_b,
S_b,
D_b,
Q_b,
N_b
),
$$

其中：

- goal；
- current state；
- dependencies；
- unresolved questions；
- next move。

所以：

$$
\boxed{
\text{bookmark}
\neq
\text{file name only}.
}
$$

---

# 33. AI Summary 作為 Lossy Compression

AI 可將：

$$
C_b
$$

壓成：

$$
\widehat C_b.
$$

壓縮率：

$$
r
=
\frac{
|\widehat C_b|
}{
|C_b|
}.
$$

但重點是：

$$
L_{\mathrm{critical}}
$$

是否保留。

因此 summary utility：

$$
U_S
=
\Delta K_{\mathrm{reentry}}
-
\lambda
L_{\mathrm{critical}}.
$$

---

# 34. Summary 可能降低也可能提高回返成本

如果 hallucinated summary：

$$
\widehat C_b
$$

改寫了：

- premise；
- version；
- unresolved status；
- negative result；

則：

$$
K_{\mathrm{verification}}\uparrow
$$

甚至：

$$
\text{wrong-branch probability}\uparrow.
$$

所以：

$$
\boxed{
\text{compression quality}
}
$$

是拓樸保持的核心條件。

---

# 35. Provenance

外部支架若保留：

$$
P_t
=
\text{provenance graph},
$$

使用者能追：

$$
\text{claim}
\rightarrow
\text{source}
\rightarrow
\text{version}
\rightarrow
\text{derivation}.
$$

則：

$$
K_{\mathrm{verification}}\downarrow.
$$

沒有 provenance：

$$
K_{\mathrm{verification}}\uparrow.
$$

因此：

$$
\boxed{
\text{memory without provenance}
\neq
\text{reliable cognitive scaffold}.
}
$$

---

# 36. AI 改變切換幾何的最小形式

傳統 transition：

$$
x
\rightarrow
y
$$

成本：

$$
K_H(x,y).
$$

加入 AI：

$$
x
\rightarrow
q
\rightarrow
m
\rightarrow
y.
$$

若：

$$
K(x,q)
+
K(q,m)
+
K(m,y)
<
K_H(x,y),
$$

則：

$$
\boxed{
d_{\mathrm{eff}}(x,y)
<
d_H(x,y).
}
$$

這就是：

$$
\boxed{
\text{AI changes the effective geometry of switching}.
}
$$

注意：

**effective** 是必要限定詞。

---

# 37. AI 並沒有把內部大腦距離直接變短

若拿走 AI：

$$
\mathcal A^{AI}=0,
$$

可能：

$$
d_H
$$

完全沒變。

所以：

$$
\boxed{
d_{\mathrm{eff}}\downarrow
\not\Rightarrow
d_H\downarrow.
}
$$

這是 augmented cognition 與 learned/internalized cognition 的關鍵區分。

---

# 38. Scaffold-Dependent Topology

若：

$$
d_{\mathrm{eff}}^{+AI}
\ll
d_H,
$$

但移除 AI：

$$
d_{\mathrm{eff}}^{-AI}
\approx
d_H,
$$

稱：

$$
\boxed{
\text{scaffold-dependent topology}.
}
$$

這可能高效，

也可能脆弱。

---

# 39. Internalization

若長期使用支架後：

$$
d_H^{post}
<
d_H^{pre},
$$

則存在：

$$
\boxed{
\text{internalization gain}.
}
$$

定義：

$$
\Gamma_I
=
d_H^{pre}
-
d_H^{post}.
$$

只有：

$$
\Gamma_I>0
$$

才表示工具協作真正壓縮了 unaided cognitive distance。

---

# 40. Offloading 的代價：內部記憶可能變弱

2025 的 cognitive-offloading studies 顯示：

預期 external memory 可用時，

participants 可能降低 internal encoding。

2026 prospective-memory experiments 也顯示：

external reminders 改善被 offloaded intention 的當下成功，

但在後續移除 reminder 時，

原先被 offload 的 prospective-memory learning 可能受損。

因此：

$$
\boxed{
\Gamma_d>0
}
$$

可以同時：

$$
\boxed{
\Gamma_I<0.
}
$$

也就是即時有效距離下降，

但 internalized capability 反而下降。

---

# 41. Generative AI 與 Learning Cost

Bastani 等人 2025 PNAS field experiment 在近千名高中學生中比較：

- control；
- GPT Base；
- 有 safeguard 的 GPT Tutor。

AI 在練習階段可大幅提高 performance。

但 GPT Base 組在移除 AI 的 exam 上低於 control；

有 guardrails 的 GPT Tutor 大幅減輕此負面 learning effect。

這是 TADC-07 非常重要的反例：

$$
\boxed{
\text{better scaffolded performance}
\not\Rightarrow
\text{better unaided learning}.
}
$$

---

# 42. 所以必須加入 Scaffold Removal Test

任何 AI cognitive-augmentation study 都應同時測：

### Supported phase

$$
P_{+AI}.
$$

### Removal phase

$$
P_{-AI}^{post}.
$$

### Baseline

$$
P_{-AI}^{pre}.
$$

只有三者都有，

才能分：

- augmentation；
- internalization；
- dependency。

---

# 43. Immediate Augmentation

定義：

$$
\Gamma_A
=
P_{+AI}
-
P_{baseline}.
$$

---

# 44. Transfer / Internalization

定義：

$$
\Gamma_I
=
P_{-AI}^{post}
-
P_{-AI}^{pre}.
$$

---

# 45. Dependency Cost

若：

$$
P_{-AI}^{post}
<
P_{-AI}^{pre},
$$

定義：

$$
\boxed{
K_D
=
P_{-AI}^{pre}
-
P_{-AI}^{post}.
}
$$

這是 performance-level dependency index。

---

# 46. Human–GenAI Collaboration 不是必然有持續 spillover

Wu 等人（2025）進行四項 online experiments，總：

$$
N=3562.
$$

整體上 human–GenAI collaboration 提升 immediate task performance，

但提升不穩定地延續到之後 human-only task。

同時，從 AI collaboration 切回 solo work 與：

- intrinsic motivation 降低；
- boredom 增加；
- sense of control 改變；

相關。

所以：

$$
\boxed{
\text{performance topology}
}
$$

還不等於：

$$
\boxed{
\text{motivation topology}.
}
$$

---

# 47. Motivation 也會改變有效距離

如果 AI collaboration 後：

$$
M_t
=
\text{motivation}
$$

下降，

某些 task transitions：

$$
K_{\mathrm{engagement}}
$$

反而可能上升。

因此：

$$
d_{\mathrm{eff}}
$$

不能只用資訊 retrieval cost 計算。

應包含：

$$
\boxed{
\text{motivational access cost}.
}
$$

---

# 48. Clinical Human–AI Collaboration 的警告

2026 複雜眼科 reasoning experiment：

human-only 平均 accuracy 約：

$$
0.45.
$$

human–AI collaboration 約：

$$
0.60.
$$

LLM-only 約：

$$
0.70.
$$

human–AI collaboration 同時提高 confidence 並降低 subjective cognitive burden。

但有約：

$$
20\%
$$

participants performance 下降。

失敗經常涉及：

$$
\boxed{
\text{human accepts incorrect AI insight}.
}
$$

因此低 cognitive burden：

$$
\not\Rightarrow
$$

高 epistemic quality。

---

# 49. Verification Cost

AI 建議：

$$
z_{AI}.
$$

真正採用需要：

$$
V(z_{AI}).
$$

定義：

$$
K_V
=
K(
\text{source checking},
\text{logic checking},
\text{replication},
\text{cross-model verification}
).
$$

若：

$$
K_V
$$

被忽略，

表面：

$$
K_{\mathrm{eff}}
$$

會被嚴重低估。

---

# 50. Trust Calibration

令：

$$
p_C
=
P(
AI\text{ correct}
),
$$

使用者主觀估計：

$$
\widehat p_C.
$$

calibration error：

$$
E_{\mathrm{cal}}
=
|
p_C-\widehat p_C
|.
$$

若：

$$
E_{\mathrm{cal}}\uparrow,
$$

可能：

- 過度信任；
- 過度拒絕；
- verification policy 失衡。

所以：

$$
\boxed{
\text{AI availability}
+
\text{poor calibration}
}
$$

可能比沒有 AI 更差。

---

# 51. Effective Cost Equation

本文提出候選總成本：

$$
\boxed{
K_{\mathrm{eff}}
=
K_H
-
\Delta K_M
-
\Delta K_R
-
\Delta K_{RE}
+
K_V
+
K_C
+
K_D.
}
$$

其中：

- \(\Delta K_M\)：memory maintenance reduction；
- \(\Delta K_R\)：retrieval reduction；
- \(\Delta K_{RE}\)：re-entry reduction；
- \(K_V\)：verification；
- \(K_C\)：coordination；
- \(K_D\)：dependency / skill-loss cost。

只有：

$$
K_{\mathrm{eff}}
<
K_H
$$

才是淨收益。

---

# 52. Coordination Cost

多 agent 並行：

$$
n\uparrow
$$

可能：

$$
\text{raw throughput}\uparrow.
$$

但：

$$
K_C(n)
$$

也上升。

包括：

- duplicate work；
- conflicting answers；
- merge cost；
- state divergence；
- version mismatch；
- provenance reconciliation。

因此：

$$
\boxed{
\text{more agents}
\neq
\text{monotonic cognitive gain}.
}
$$

---

# 53. Agent Fan-out

人類在 state：

$$
x
$$

建立：

$$
n
$$

個 agent branches：

$$
b_1,\ldots,b_n.
$$

記：

$$
F_A=n.
$$

system reachability：

$$
\operatorname{Reach}_S
$$

可能快速增加。

但 human review capacity：

$$
B_H
$$

有限。

若：

$$
F_A
\gg
B_H,
$$

會產生：

$$
\boxed{
\text{verification backlog}.
}
$$

---

# 54. Verification Backlog

定義：

$$
Q_V(t)
=
N_{\mathrm{unverified}}(t).
$$

若：

$$
\frac{dQ_V}{dt}>0
$$

長期成立，

混合系統產出速度超過人類吸收／驗證速度。

此時：

$$
\Gamma_R\uparrow
$$

但：

$$
P_R\downarrow
$$

或：

$$
K_V\rightarrow\infty.
$$

---

# 55. 可達域爆炸

若 AI 每個 node 提出：

$$
b
$$

個 branches，

深度：

$$
d,
$$

候選量：

$$
O(b^d).
$$

因此 AI 的問題可能從：

$$
\text{not enough options}
$$

轉成：

$$
\boxed{
\text{too many reachable options}.
}
$$

所以 Expansion 必須搭配 TADC-03 的：

$$
C
=
\text{Contraction}.
$$

---

# 56. 人—AI 系統需要 Selection Operator

AI 生成：

$$
Y
=
\{y_1,\ldots,y_n\}.
$$

人類／另一個 agent 必須：

$$
S:
Y
\rightarrow
Y^*.
$$

如果：

$$
|Y|\uparrow
$$

但：

$$
Q(S)\downarrow,
$$

混合 cognition 變差。

---

# 57. AI 可能降低跨域 Bridge Cost

TADC-06：

$$
d_{\mathrm{rel}}(x,y\mid G).
$$

AI 搜尋與類比生成可以提出 bridge：

$$
B_{xy}.
$$

若驗證後成立：

$$
d_{\mathrm{rel}}^{+AI}(x,y)
<
d_{\mathrm{rel}}^{-AI}(x,y).
$$

這是 AI 最接近真正「改變關係拓樸」的作用之一。

---

# 58. 但 AI 也可能製造 False Bridge

若：

$$
B_{xy}^{AI}
$$

只保 surface similarity，

不保 constraints，

則：

$$
\boxed{
\text{cross-domain hallucination}.
}
$$

所以：

$$
G
=
\text{Gluing}
$$

必須搭配：

$$
D
=
\text{Detachment}.
$$

---

# 59. AI 作為 Re-indexing Engine

AI 可以：

- summarize；
- outline；
- decompose；
- abstract；
- expand。

因此：

$$
R^-:
U
\rightarrow
z_U
$$

與：

$$
R^+:
z_U
\rightarrow
\widetilde U
$$

都可以外部化。

這可能：

$$
K_R\downarrow.
$$

所以 AI 不只降低 horizontal switching cost，

也可能降低：

$$
\boxed{
\text{vertical scale-switching cost}.
}
$$

---

# 60. AI 改變 TADC-04 多尺度 routing

沒有 AI：

$$
x_f
\rightarrow
y_f
$$

可能需要長 fine-scale path。

有 AI：

$$
x_f
\overset{R^-}{\longrightarrow}
U_c
\overset{T}{\longrightarrow}
V_c
\overset{R^+}{\longrightarrow}
y_f.
$$

若：

$$
K_{R^-}+K_T+K_{R^+}
<
K_{\mathrm{fine}},
$$

AI 降低了 multiscale routing cost。

---

# 61. AI 與 Topological Hyperfocus

TADC-05 定義 THF：

$$
\mathcal K_0
\rightarrow
\mathcal K_1
\rightarrow\cdots
$$

保持 structural continuity。

外部 memory 可以保存：

$$
\mathcal K_t
$$

使 interrupted episode 後：

$$
P_{\mathrm{return}}\uparrow.
$$

因此 AI / external state 可能：

$$
\boxed{
\text{support persistent domain attachment
without continuous internal maintenance}.
}
$$

---

# 62. Continuous Attention 不再是 Continuous State Maintenance

如果 state 可外存，

人類可以：

$$
U_A
\rightarrow
U_B
\rightarrow
U_C
\rightarrow
U_A
$$

而不必在 working memory 中一直保留：

$$
U_A.
$$

所以：

$$
\boxed{
\text{long-term project continuity}
\neq
\text{continuous internal activation}.
}
$$

這對長時間尺度研究非常重要。

---

# 63. External Persistence as a New Form of Continuity

傳統：

$$
\text{continuity}
\approx
\text{internal state persistence}.
$$

混合系統：

$$
\text{continuity}
$$

可以由：

$$
\boxed{
\text{external state persistence}
+
\text{reliable re-entry}
}
$$

維持。

因此 persistent cognition 可變成：

$$
\boxed{
\text{discontinuous human activation
over continuous addressable state}.
}
$$

---

# 64. Hybrid Cognitive Continuity Conjecture（HCCC）

本文增加一個衍生命題：

若 external state：

$$
M_t
$$

能長期保存 task-relevant invariants，

則：

$$
A_t^H
$$

即使離開，

整個混合系統的 project-state continuity：

$$
C_S
$$

仍可保持。

形式：

$$
\boxed{
A_t^H=0
\not\Rightarrow
C_S=0.
}
$$

---

# 65. 這不是把 AI 說成人格主體

HCCC 只描述：

$$
\boxed{
\text{task-state persistence}.
}
$$

它不推論：

- AI consciousness；
- AI personhood；
- AI intention；
- shared phenomenology。

這些是不同問題。

---

# 66. 混合系統的四個層級

## Level 0 — No External Scaffold

$$
\mathcal H=\mathcal C^H.
$$

---

## Level 1 — Passive Memory

notes / files：

$$
M.
$$

---

## Level 2 — Addressable Scaffold

search / index / graph：

$$
M+I+Q.
$$

---

## Level 3 — Interactive AI

$$
M+I+Q+B_x+R.
$$

AI 可主動重表徵與提出 bridge。

---

## Level 4 — Persistent Agent System

$$
M+I+Q+B_x+R+P_x.
$$

支援：

- branch persistence；
- parallel execution；
- asynchronous state updates。

---

# 67. Topological Gain 不應只看工具複雜度

Level 4 不一定優於 Level 2。

如果：

$$
K_V+K_C+K_D
$$

過大，

則：

$$
K_{\mathrm{eff}}^{L4}
>
K_{\mathrm{eff}}^{L2}.
$$

所以：

$$
\boxed{
\text{more agentic}
\neq
\text{better cognitive scaffold}.
}
$$

---

# 68. Null Model 1：Speed-Up Only

假設 AI 只降低：

$$
K_{\mathrm{lookup}}.
$$

所有其他 graph structure 不變。

如果這就能解釋：

- switching；
- reachability；
- return；
- performance；

則 ECDTC 的拓樸語言不需要。

---

# 69. Null Model 2：Memory Capacity Only

假設：

$$
|M|\uparrow
$$

已經解釋所有 benefit。

如果 index / graph / agent architecture 沒有額外作用，

RTC / HREC 過度複雜。

---

# 70. Null Model 3：More Information Only

AI 只是給更多：

$$
I.
$$

如果資訊量：

$$
|I|
$$

控制後，

AI-specific bridge / re-indexing / re-entry 效應消失，

TADC-07 應縮減。

---

# 71. Null Model 4：Motivation / Novelty Only

AI interface 可能比較有趣。

若所有：

$$
T_{\mathrm{engagement}}
$$

增加都由 novelty / motivation 解釋，

不能說拓樸變了。

---

# 72. Null Model 5：Ordinary Collaboration

人類一直會把 cognition offload 給其他人。

Armitage 與 Redshaw 的研究直接顯示：

$$
\boxed{
\text{other humans can serve as offloading targets}.
}
$$

因此 AI 若只是另一個 partner，

則無需新 topology。

TADC-07 必須找：

- persistent addressability；
- scalable branching；
- rapid re-indexing；
- machine retrieval；

等增量特徵。

---

# 73. Null Model 6：Artifact Throughput Illusion

如果：

$$
A_t\uparrow
$$

只是 AI 自動生成大量 artifacts，

但：

$$
P_{\mathrm{validated}}\downarrow
$$

或：

$$
P_{\mathrm{integrated}}\downarrow,
$$

不能說 cognition 變強。

所以：

$$
\boxed{
\text{artifact count}
\neq
\text{cognitive reachability gain}.
}
$$

---

# 74. 實驗一：Support Ladder

同一 participant 完成 multi-branch reasoning task。

條件：

1. no aid；
2. static notes；
3. searchable notes；
4. LLM without persistent memory；
5. LLM + persistent memory；
6. LLM + memory + agents。

測：

$$
K_{\mathrm{switch}},
K_{\mathrm{reentry}},
\operatorname{Reach},
P_R,
Accuracy,
InternalRecall.
$$

---

# 75. 關鍵預測

若 TADC-07 成立，

不同工具層級不只提高：

$$
\text{speed},
$$

還會改變：

$$
\boxed{
\text{which branches are revisited,
which bridges are used,
and which states become reachable}.
}
$$

---

# 76. 實驗二：Branch Suspension / Re-entry

建立：

$$
b_1,b_2,b_3,b_4.
$$

participants 反覆被迫：

$$
b_i\rightarrow b_j.
$$

比較：

- internal-only；
- note；
- structured checkpoint；
- AI-generated checkpoint；
- provenance-preserving checkpoint。

測：

$$
\tau_{\mathrm{reentry}},
$$

$$
\text{state reconstruction error},
$$

$$
\text{branch completion}.
$$

---

# 77. 實驗三：AI Bridge Discovery

兩個外部 taxonomy 遠的 domains：

$$
U_A,U_B.
$$

control：

人工搜尋。

experimental：

AI 提供候選 bridges。

最終所有 bridge 都需 blind validation。

測：

$$
d_{\mathrm{rel}}^{post},
$$

$$
K_{AB},
$$

$$
\text{novel inference}.
$$

---

# 78. 實驗四：False Bridge Load

AI 故意混入：

$$
p
$$

比例的 invalid bridges。

測：

$$
K_V(p),
$$

$$
P_R(p),
$$

$$
\Gamma_d(p).
$$

預測存在臨界：

$$
p^*
$$

使：

$$
\Gamma_d
$$

由正轉負。

---

# 79. 實驗五：Agent Fan-out

設定：

$$
n
=
1,2,4,8,16.
$$

agents 平行處理 branches。

測：

$$
\text{raw artifact throughput},
$$

$$
\text{validated throughput},
$$

$$
Q_V,
$$

$$
K_C.
$$

預測：

validated gain 對：

$$
n
$$

不是單調增加。

---

# 80. 實驗六：Scaffold Removal

participants 經多輪 AI-assisted task 後，

移除 AI。

測：

$$
P_{-AI}^{post}.
$$

和：

$$
P_{-AI}^{pre}
$$

比較。

這直接區分：

$$
\boxed{
\text{augmentation}
}
$$

與：

$$
\boxed{
\text{internalization}.
}
$$

---

# 81. 實驗七：Guardrail Design

比較：

### Answer-first AI

直接給解。

### Hint-first AI

提示、要求 human step。

### Verify-first AI

要求 human 先提出 candidate，

AI 再 critique。

### Memory-first AI

只保存／恢復狀態，

不代替 reasoning。

測：

- supported performance；
- later unaided performance；
- cognitive load；
- motivation；
- retention；
- verification accuracy。

---

# 82. 實驗八：System vs Human Switch Rate

使用精確 logs 分離：

$$
\nu_H
$$

與：

$$
\nu_S.
$$

Human switch 必須由：

- explicit interaction；
- eye / input focus；
- task declaration；
- experience sample；

估計。

Agent background events：

$$
\notin\nu_H.
$$

測：

$$
\nu_S/\nu_H.
$$

這是多 agent cognition 研究必要的 measurement correction。

---

# 83. 實驗九：External-State Continuity

讓人類離開 project：

$$
\Delta t
=
1\text{h},1\text{d},1\text{w}.
$$

比較不同 scaffold：

$$
P_{\mathrm{return}},
$$

$$
\tau_{\mathrm{reentry}},
$$

$$
\text{state fidelity}.
$$

RTC 預測：

$$
\boxed{
\text{structured external state
reduces decay of project continuity}.
}
$$

---

# 84. 九個核心可證偽命題

## TADC7-H1 — Effective Distance Reduction

至少部分 transitions：

$$
d_{\mathrm{eff}}^{+E}
<
d_H.
$$

---

## TADC7-H2 — Addressability Matters Beyond Capacity

控制：

$$
|M|
$$

後，

$$
A_M
$$

仍預測：

$$
K_{\mathrm{reentry}}.
$$

---

## TADC7-H3 — Re-entry Gain

structured state support：

$$
K_{\mathrm{reentry}}^{structured}
<
K_{\mathrm{reentry}}^{unstructured}.
$$

---

## TADC7-H4 — Hybrid Reachability Expansion

同資源窗：

$$
|\operatorname{Reach}_+|
>
|\operatorname{Reach}_H|.
$$

---

## TADC7-H5 — Verification Moderates Gain

$$
\Gamma_R
$$

只有在：

$$
P_R
$$

足夠高時轉化成有效 performance gain。

---

## TADC7-H6 — Agent Parallelism Is System-Level

$$
\nu_S\uparrow
$$

不必伴隨：

$$
\nu_H\uparrow
$$

同等幅度。

---

## TADC7-H7 — Supported and Unaided Performance Dissociate

存在：

$$
\Gamma_A>0
$$

但：

$$
\Gamma_I\leq0.
$$

這已與既有 offloading / AI-learning evidence 相容。

---

## TADC7-H8 — Tool Design Changes Internalization

不同 guardrails：

$$
\Gamma_I^{(1)}
\neq
\Gamma_I^{(2)}.
$$

---

## TADC7-H9 — Hybrid Model Adds Prediction

加入：

$$
A_M,
K_{RE},
\Gamma_R,
K_V,
K_C
$$

後，

out-of-sample prediction 應優於：

$$
\text{speed + information volume}
$$

模型。

---

# 85. 什麼會殺掉「AI 改變認知拓樸」？

## F1 — Pure Speed Model Wins

如果所有效應都只需：

$$
K_{\mathrm{lookup}}\downarrow
$$

解釋，

則 topology language 多餘。

---

## F2 — Reachability Does Not Change

若 AI 只讓原本 path 更快，

但：

$$
\operatorname{Reach}_+
=
\operatorname{Reach}_H,
$$

HREC 失敗。

---

## F3 — Re-entry Does Not Improve

若 structured external state 對：

$$
K_{\mathrm{reentry}}
$$

沒有穩定 effect，

RTC 失敗。

---

## F4 — Addressability Adds Nothing

若：

$$
|M|
$$

足以解釋所有效果，

index / topology claim 過度。

---

## F5 — AI Bridges Add No Valid Transfer

若 AI 只增加候選但不增加：

$$
\text{validated cross-domain inference},
$$

Bridge Discovery 不構成拓樸增益。

---

## F6 — Agent Parallelism Produces Only Artifact Noise

若：

$$
n\uparrow
$$

只使：

$$
Q_V\uparrow
$$

而 validated output 不增，

system-level reachability gain 不成立。

---

## F7 — Internal Cost Dominates

若：

$$
K_V+K_C+K_D
>
\Delta K_M+\Delta K_R+\Delta K_{RE},
$$

則：

$$
K_{\mathrm{eff}}>K_H.
$$

此工具配置應被視為負增益。

---

# 86. 「AI 讓領域消失」不是本文主張

AI 可以降低：

$$
d_{\mathrm{eff}}(D_i,D_j),
$$

但不表示：

$$
D_i=D_j.
$$

因此：

$$
\boxed{
\text{distance reduction}
\neq
\text{domain identity}.
}
$$

TADC-06 的 constraint-preserving mapping 仍然必要。

---

# 87. AI 的真正特殊性可能是「低成本重建」

傳統 external memory：

$$
M
$$

需要人類自己讀回並重建。

LLM / agent 可以：

$$
M
\rightarrow
\widehat C
\rightarrow
\text{next action}.
$$

所以它不只：

$$
\text{store},
$$

而是：

$$
\boxed{
\text{store + retrieve + reconstruct candidate context}.
}
$$

這可能是：

$$
K_{\mathrm{reentry}}
$$

大幅下降的關鍵。

---

# 88. 但重建候選必須可驗證

如果 AI 自動補完 missing context：

$$
\widehat C
=
C+\epsilon,
$$

其中：

$$
\epsilon
$$

可能包含 false inference。

因此高品質 scaffold 需要：

$$
\boxed{
\text{state recovery}
+
\text{uncertainty disclosure}
+
\text{provenance}.
}
$$

---

# 89. Hybrid Cognitive Atlas

TADC-02：

$$
\mathfrak A_t
=
\{(U_\alpha,\phi_\alpha)\}.
$$

加入外部系統：

$$
\boxed{
\mathfrak A_t^+
=
\{
(U_\alpha,\phi_\alpha,M_\alpha,Q_\alpha,V_\alpha)
\}.
}
$$

每個 domain 不只具有 internal chart，

還可以具有：

- external state；
- retrieval path；
- verification state。

---

# 90. 外部 Atlas 允許 Sparse Human Activation

人類不需要：

$$
A_t^H
$$

同時涵蓋：

$$
U_1,\ldots,U_n.
$$

只要：

$$
\mathfrak A_t^+
$$

保留其狀態，

就能：

$$
U_1
\rightarrow
U_7
\rightarrow
U_3
\rightarrow
U_1.
$$

因此：

$$
\boxed{
\text{many active project branches}
\neq
\text{many simultaneously active human attention states}.
}
$$

---

# 91. 這會改變「多工」的定義

傳統 multitasking 常研究：

$$
\text{rapid internal task switching}.
$$

混合系統則可能是：

$$
\boxed{
\text{serial human control
over parallel persistent external branches}.
}
$$

這不是傳統意義的 simultaneous human multitasking。

可以叫：

$$
\boxed{
\text{Externally Parallelized Serial Cognition}.
}
$$

簡稱：

$$
\boxed{
EPSC.
}
$$

---

# 92. EPSC 候選模型

Human controller：

$$
H:
b_i\rightarrow b_j.
$$

agents：

$$
A_i
$$

在背景維持：

$$
b_i.
$$

所以：

$$
\boxed{
\text{human control channel is serial-ish,
execution fabric is parallel}.
}
$$

這可能是 agentic AI 時代新的工作拓樸。

---

# 93. EPSC 的限制

若 human review：

$$
B_H
$$

固定，

agent throughput：

$$
B_A
$$

持續增加，

則：

$$
\frac{B_A}{B_H}
\rightarrow\infty
$$

不可持續。

因此需要：

- automated verification；
- hierarchical summaries；
- branch prioritization；
- provenance；
- exception routing。

否則：

$$
\boxed{
\text{parallelism becomes queue overload}.
}
$$

---

# 94. Cognitive Topology Engineering

如果 TADC-07 部分成立，

未來工具設計目標就不只是：

$$
\text{minimize clicks}.
$$

而可能是：

$$
\boxed{
\text{engineer effective cognitive topology}.
}
$$

包括：

- shorten valid paths；
- preserve branch state；
- expose bridges；
- reduce re-entry cost；
- preserve invariants；
- prevent false gluing；
- maintain human controllability。

---

# 95. 六個工程指標

## 1. Addressability

$$
A_M.
$$

## 2. Re-entry cost

$$
K_{RE}.
$$

## 3. Reachability gain

$$
\Gamma_R.
$$

## 4. Precision

$$
P_R.
$$

## 5. Verification burden

$$
K_V.
$$

## 6. Internalization

$$
\Gamma_I.
$$

真正好的 cognitive scaffold 應同時優化，

而不是只提高：

$$
\text{output count}.
$$

---

# 96. 系列統一

TADC-01：

$$
\boxed{
\text{attention may transform effective cognitive space}.
}
$$

TADC-02：

$$
\boxed{
\text{domains may be dynamically induced}.
}
$$

TADC-03：

$$
\boxed{
\mathcal O=\{E,C,T,G,D,R\}.
}
$$

TADC-04：

$$
\boxed{
\text{object/domain status may be scale-relative}.
}
$$

TADC-05：

$$
\boxed{
\text{focus persistence need not imply state immobility}.
}
$$

TADC-06：

$$
\boxed{
d_{\mathrm{ext}}
\neq
d_{\mathrm{rel}}.
}
$$

TADC-07：

$$
\boxed{
d_{\mathrm{eff}}
=
d(
\mathcal C^H
\oplus
\mathcal S^E
\oplus
\mathcal A^{AI}
).
}
$$

---

# 97. 最小總模型

Human state：

$$
\mathcal C_t^H.
$$

External state：

$$
\mathcal S_t^E.
$$

AI system：

$$
\mathcal A_t^{AI}.
$$

Hybrid state：

$$
\mathcal H_t
=
\mathcal C_t^H
\oplus
\mathcal S_t^E
\oplus
\mathcal A_t^{AI}.
$$

有效 transition：

$$
\boxed{
d_{\mathrm{eff}}(x,y)
=
\min_{\gamma\subseteq\mathcal H_t}
K(\gamma).
}
$$

---

# 98. 最小效益條件

外部系統有淨效益需：

$$
\boxed{
\Delta K_M
+
\Delta K_R
+
\Delta K_{RE}
>
K_V
+
K_C
+
K_D.
}
$$

而長期學習若重要，

還應要求：

$$
\boxed{
\Gamma_I
\geq
\Gamma_I^{\min}.
}
$$

否則即時效能可能以人類內部能力下降為代價。

---

# 99. 結論

本文提出：

$$
\boxed{
\textbf{ECDTC}
}
$$

即外部認知支架可改變任務中的有效認知距離；

$$
\boxed{
\textbf{RTC}
}
$$

即可尋址、可恢復的 external state 可降低中斷後 re-entry cost；

以及：

$$
\boxed{
\textbf{HREC}
}
$$

即 AI / agent system 可在有限資源窗內擴張混合系統的有效 reachability。

本文最重要的區分是：

$$
\boxed{
\text{internal cognition}
\neq
\text{supported human performance}
\neq
\text{hybrid-system throughput}.
}
$$

因此：

$$
\nu_S\gg\nu_H
$$

不能被解釋成人類 attention 無限制平行化；

$$
A_t\uparrow
$$

也不能直接被解釋為 human cognitive throughput 上升。

本文真正提出的是：

$$
\boxed{
\text{AI may alter the effective geometry
through which cognition is executed}.
}
$$

這個改變可以來自：

$$
\text{Externalization},
$$

$$
\text{Retrieval},
$$

$$
\text{Bridge Discovery},
$$

$$
\text{Parallel Execution}.
$$

但每項都有成本：

$$
\text{Verification},
$$

$$
\text{Coordination},
$$

$$
\text{Dependency},
$$

$$
\text{Internal-learning loss}.
$$

因此最終不是：

$$
\boxed{
\text{AI = cognitive amplification}.
}
$$

而是：

$$
\boxed{
\text{AI creates a new cost-and-reachability landscape
whose value depends on architecture and control}.
}
$$

現有 cognitive-offloading evidence 已充分說明外部資源能改變 task performance；現有 GenAI experiments 也已顯示即時增益、長期學習、動機、confidence 與 correctness 可以彼此分離。

因此 TADC-07 的強版本只有在：

1. 外部 state 不只增加資訊量；
2. addressability 能獨立降低 re-entry；
3. AI bridge 能增加 validated cross-domain transfer；
4. hybrid system 擴張有限資源下的有效 reachable states；
5. 這些量比純 speed / memory-capacity 模型提供額外預測；

時才成立。

若不能，

本文應降級成：

$$
\boxed{
\text{cognitive offloading + human–AI task support model}.
}
$$

而不再使用「認知拓樸」這個較強名稱。

但是若成立，

就會得到一個非常重要的結果：

> **認知切換成本並不完全由大腦當下保存了多少上下文決定；它也取決於環境是否替這個認知系統保存了可尋址、可驗證、可回返的狀態。**

因此：

$$
\boxed{
\text{cognitive continuity}
}
$$

可以從：

$$
\text{continuous internal activation}
$$

擴展為：

$$
\boxed{
\text{reliably recoverable state continuity}.
}
$$

這也是下一篇 TADC-08 的最終任務：

> 把整個 TADC 系列從理論語言收斂成可量測變量、preregistered experiments、模型比較與明確淘汰條件，決定「拓樸注意力」究竟能不能從一個命題猜想升級為真正的研究理論。

---

# 參考文獻

1. Risko EF, Gilbert SJ. **Cognitive Offloading.** *Trends in Cognitive Sciences*. 2016;20(9):676–688. doi:10.1016/j.tics.2016.07.002. PMID: 27542527.  
2. Gilbert SJ, Boldt A, Sachdeva C, Scarampi C, Tsai P-C. **Outsourcing Memory to External Tools: A Review of 'Intention Offloading'.** *Psychonomic Bulletin & Review*. 2023;30(1):60–76. doi:10.3758/s13423-022-02139-4. PMID: 35789477.  
3. Gilbert SJ. **Cognitive offloading is value-based decision making: Modelling cognitive effort and the expected value of memory.** *Cognition*. 2024;247:105783. doi:10.1016/j.cognition.2024.105783. PMID: 38583321.  
4. Burnett LK, Richmond LL. **Meta-analytic investigations of the effect of cognitive offloading on memory-based task performance and interindividual variability.** *Memory & Cognition*. 2026;54(1):144–168. doi:10.3758/s13421-025-01743-8. PMID: 40500483.  
5. Kelly MO, Karimjee B, Pereira AE, Lu X, Risko EF. **Does expecting external memory support cost recognition memory?** *Memory & Cognition*. 2025. doi:10.3758/s13421-025-01688-y. PMID: 39890707.  
6. Magen H, Tomer-Offen M. **Reduced relational and item-specific processing in cognitive offloading.** *Cognitive Research: Principles and Implications*. 2025;10(1):41. doi:10.1186/s41235-025-00647-0. PMID: 40660049.  
7. Fellers C, Storm BC. **Offloading reduces prospective memory learning.** *Journal of Experimental Psychology: Learning, Memory, and Cognition*. 2026. doi:10.1037/xlm0001630. PMID: 42241083.  
8. Armitage KL, Redshaw J. **Can you help me? Using others to offload cognition.** *Memory & Cognition*. 2025;53(3):946–959. doi:10.3758/s13421-024-01621-9. PMID: 39172203.  
9. Murphy DH, Metcalfe J. **The Metacognitive Optimization of Offloading Task (MOOT): Both higher costs to offload and the accuracy of memory predict goodness of offloading performance.** *Journal of Experimental Psychology: General*. 2025;154(4):1149–1166. doi:10.1037/xge0001726. PMID: 39847000.  
10. **Metacognitive training facilitates optimal cognitive offloading.** *Cognitive Research: Principles and Implications*. 2026. doi:10.1186/s41235-026-00714-0. PMID: 41817942.  
11. Hirsch P, Moretti L, Askin S, Koch I. **Examining the cognitive processes underlying resumption costs in task-interruption contexts: Decay or inhibition of suspended task goals?** *Memory & Cognition*. 2024;52(2):271–284. doi:10.3758/s13421-023-01458-8. PMID: 37674056.  
12. Wu S, Liu Y, Ruan M, Chen S, et al. **Human-generative AI collaboration enhances task performance but undermines human’s intrinsic motivation.** *Scientific Reports*. 2025;15:15105. doi:10.1038/s41598-025-98385-2.  
13. Bastani H, Bastani O, Sungu A, Ge H, Kabakcı Ö, Mariman R. **Generative AI without guardrails can harm learning: Evidence from high school mathematics.** *Proceedings of the National Academy of Sciences USA*. 2025;122(26):e2422633122. doi:10.1073/pnas.2422633122. PMID: 40560616.  
14. Ong KT-I, Seo J, Kim H, Kim J, Kim J, Kim S, Yeo J, Choi EY. **Success and failure of human–AI collaboration in clinical reasoning: An experimental study on challenging real-world cases.** *International Journal of Medical Informatics*. 2026;211:106342. doi:10.1016/j.ijmedinf.2026.106342. PMID: 41689881.  
15. Tsai P-C, Scarampi C, Kliegel M, Gilbert SJ. **Optimal cognitive offloading: Increased reminder usage but reduced proreminder bias in older adults.** *Psychology and Aging*. 2023. doi:10.1037/pag0000751. PMID: 37289516.  
16. **Strategic reminder setting for time-based intentions: Influence of metacognition, delay length, and cue visibility.** 2025. PMID: 40238032.  
17. **Between Alarms and Scheduling: The Effect of Cognitive Offloading on Prospective and Retrospective Memory.** 2026. PMID: 42352705.  
18. Dong CV, Lu Q, Norman KA, Michelmann S. **Towards large language models with human-like episodic memory.** *Trends in Cognitive Sciences*. 2025. doi:10.1016/j.tics.2025.06.016. PMID: 40713240.  
19. Peer M, Epstein RA. **Cognitive maps for hierarchical spaces in the human brain.** *Cerebral Cortex*. 2025;35(9):bhaf261. doi:10.1093/cercor/bhaf261. PMID: 40982478.  
20. Tan L, Qiu Y, Qiu L, et al. **The medial and lateral orbitofrontal cortex jointly represent the cognitive map of task space.** *Communications Biology*. 2025;8:163. doi:10.1038/s42003-025-07588-w. PMID: 39900714.  

---

## 與系列的關係

**已完成：**

- TADC-01：《注意力不是單點選擇——可變認知空間與注意—空間轉換猜想》
- TADC-02：《動態認知域——領域作為局部座標圖》
- TADC-03：《拓樸注意力六算子——展開、收斂、遍歷、黏合、切離與重索引》
- TADC-04：《嵌套注意域與觀察尺度——宏觀／微觀的相對性與多尺度重索引》
- TADC-05：《從單點超專注到拓樸超專注——域級持續性、內部高熵遍歷與可控退出》
- TADC-06：《關係優先認知與跨域連續性——從學科距離到關係距離的認知拓樸猜想》
- TADC-07：《外部認知支架與人—AI 認知拓樸——有效距離、回返成本與混合認知系統》

**下一篇：**

- TADC-08：《拓樸注意力的測量、反證與工程化》

---

**狀態：** TADC-07 v0.1  
**原始人體／臨床數據：** 無  
**理論狀態：** 猜想／研究綱領；未經一般性實驗驗證  
**AI 狀態：** 不主張 AI 使用必然提升內部人類認知能力；supported performance、internalization 與 hybrid-system throughput 必須分離  
**拓樸狀態：** effective cognitive topology 為 task-level hybrid accessibility 的候選形式；不宣稱外部 AI 與人腦構成單一心理主體
