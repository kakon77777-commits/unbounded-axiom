# UNPNP Series 04  
## 展開—連結—收斂：UNPNP 計算的三元循環  
### Expansion–Linking–Convergence: The Triadic Computational Cycle of UNPNP

**系列名稱：** UNPNP Hyperlink & Crystallized Computation Series  
**系列篇次：** 04  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** AI 原生計算／動態計算循環／UNPNP 理論論文  
**狀態：** Canonical Draft  

---

## 摘要

UNPNP Series 01 將複雜度理解為可轉移、外部化與重新分配的多維成本；Series 02 建立底空間與廣義超連結；Series 03 則提出 Adaptive Corridor Generator，回答「誰來選擇或生成下一條通道」。然而，若只知道「要走哪裡」，仍不足以描述一個 AI 原生計算系統如何從未知狀態中形成候選、建立跨空間 transition、壓縮結果並生成下一輪可用狀態。

本文提出 UNPNP 的三元動態循環：

$$
\boxed{
E
\rightarrow
L
\rightarrow
C
\rightarrow
E'
}
$$

其中：

- $E$：Expansion，展開；
- $L$：Linking，連結；
- $C$：Convergence，收斂。

本文將這個循環視為 UNPNP Computer 的基本「呼吸」。展開使潛在候選、語義關係、可行通道與局部底空間被顯現；連結將其中一部分真正轉化為可穿越、可執行、可驗證的 transition；收斂則將結果、證據、路徑、失敗與狀態重新壓縮為新的工作狀態與下一輪種子。

因此：

$$
\boxed{
\text{Convergence is not termination.}
}
$$

而是：

$$
\boxed{
C_t
\rightarrow
E_{t+1}.
}
$$

本文進一步將 DRC 的 Divergence–Resonance–Compression、動態語義顯影、局部工作集、frontier routing、state compression 與 hyperlink traversal 統合至同一框架。DRC 不再只是一種 Web 搜尋方法，而可被一般化為 frontier transformation；語義顯影也不只是在記憶庫中找內容，而可以被理解為對整個計算世界進行條件投影，生成當下可操作的局部世界。

本文提出：

$$
\boxed{
\mathcal W_t^{\mathrm{active}}
=
\Pi_{\xi_t}(\mathcal W)
}
$$

其中 $\Pi_{\xi_t}$ 是由任務、上下文、時間、權限、資源與工作狀態共同決定的顯影算子。理想情況下：

$$
|\mathcal W_t^{\mathrm{active}}|
\ll
|\mathcal W|.
$$

因此 AI 不需在每一輪對完整世界做深度推理，而只需對被顯影出的可操作 working set 進行展開、連結與收斂。

本文亦建立局部與全域的邊界：局部收斂不必然等於全域最優，短路徑不必然等於低總成本，反覆穩定也不必然表示永久正確。因此 UNPNP 的呼吸循環必須攜帶 guard、validator、provenance、uncertainty 與 reopen 條件。

最後，本文提出「呼吸產生結晶，結晶改變下一次呼吸」作為後續路徑編譯與計算結晶化的接口：

$$
\boxed{
K_t
=
\operatorname{Crystallize}
(E_t,L_t,C_t)
}
$$

使：

$$
\mathcal L_{t+1}
=
\mathcal L_t
\cup
K_t.
$$

因此 UNPNP 的三元循環不是在固定圖中反覆搜索，而是一個能逐步改寫自身可用路徑集合的動態計算機制。

**關鍵詞：** UNPNP、Expansion、Linking、Convergence、DRC、動態語義顯影、frontier、working set、呼吸式計算、AI 原生計算、path compilation、crystallization

---

# 1. 為什麼需要一個基本循環？

Series 03 已提出：

$$
\mathcal M
\rightarrow
\Phi_t
$$

即 Adaptive Corridor Generator 生成或選擇 corridor。

但這只回答：

> 哪條路值得走？

它沒有完整回答：

> 候選路徑從哪裡來？

> 連結如何真正成立？

> 到達新底空間後，哪些資訊應保留？

> 哪些資訊應壓縮？

> 為什麼下一輪不必重新從零開始？

因此需要一個更底層的動態循環。

---

# 2. 三元循環

本文提出：

$$
\boxed{
E
\rightarrow
L
\rightarrow
C
}
$$

其中：

$$
E=\text{Expansion},
$$

$$
L=\text{Linking},
$$

$$
C=\text{Convergence}.
$$

若時間顯式化：

$$
E_t
\rightarrow
L_t
\rightarrow
C_t
\rightarrow
E_{t+1}.
$$

因此真正結構是：

$$
\boxed{
E
\rightarrow
L
\rightarrow
C
\rightarrow
E
\rightarrow
L
\rightarrow
C
\rightarrow
\cdots
}
$$

---

# 3. Expansion：展開不是暴力枚舉

最粗糙的展開可以是：

$$
S_t
\rightarrow
\Omega_t,
$$

其中：

$$
\Omega_t
$$

是所有可能候選。

但如果：

$$
|\Omega_t|
$$

巨大，

這種展開本身就失去意義。

因此 UNPNP 的 Expansion 不是：

$$
\text{enumerate everything}.
$$

而是：

$$
\boxed{
\text{generate a task-relative local possibility frontier}.
}
$$

---

# 4. 展開算子

令：

$$
s_t
$$

為當前狀態，

$$
\xi_t
$$

為條件集合。

定義：

$$
E_{\xi_t}(s_t)
=
F_t,
$$

其中：

$$
F_t
$$

是 candidate frontier。

條件可以包含：

$$
\xi_t
=
(g,c,t,o,a,b,h).
$$

其中：

- $g$：goal；
- $c$：context；
- $t$：time；
- $o$：observer / agent；
- $a$：authorization；
- $b$：budget；
- $h$：history。

---

# 5. Dynamic Semantic Revealing 作為展開前置層

假設全域世界：

$$
\mathcal W
$$

極大。

直接：

$$
E(\mathcal W)
$$

往往不可行。

因此先使用顯影：

$$
\Pi_{\xi_t}:
\mathcal W
\rightarrow
\mathcal W_t^{\mathrm{active}}.
$$

其中：

$$
\boxed{
\mathcal W_t^{\mathrm{active}}
=
\Pi_{\xi_t}(\mathcal W).
}
$$

理想上：

$$
|\mathcal W_t^{\mathrm{active}}|
\ll
|\mathcal W|.
$$

再做：

$$
E(
\mathcal W_t^{\mathrm{active}}
)
\rightarrow
F_t.
$$

---

# 6. 語義顯影不是永久裁剪

重要的是：

$$
\mathcal W_t^{\mathrm{active}}
$$

只是當前條件下的局部投影。

不是：

$$
\mathcal W_t^{\mathrm{active}}
=
\mathcal W_{\mathrm{true}}.
$$

所以：

$$
\boxed{
\text{Hidden}
\neq
\text{False}.
}
$$

也：

$$
\boxed{
\text{Not active}
\neq
\text{Irrelevant forever}.
}
$$

當：

$$
\xi_t
\rightarrow
\xi_{t+1},
$$

可能有：

$$
\mathcal W_t^{\mathrm{active}}
\neq
\mathcal W_{t+1}^{\mathrm{active}}.
$$

---

# 7. Working Set

本文將：

$$
\mathcal W_t^{\mathrm{active}}
$$

視為 AI 的 semantic working set。

類比傳統記憶體系統：

$$
\text{large storage}
\rightarrow
\text{small active working set}.
$$

但這裡不是 page locality。

而是：

$$
\boxed{
\text{semantic}
+
\text{goal}
+
\text{causal}
+
\text{temporal}
+
\text{authorization locality}.
}
$$

---

# 8. Expansion 的輸出不是答案

展開的結果：

$$
F_t
$$

不是最終答案。

它只是：

- 候選 link；
- 候選底空間；
- 候選證據；
- 候選操作；
- 候選解釋；
- 候選路徑。

因此：

$$
\boxed{
E
\neq
\text{solve}.
}
$$

---

# 9. Divergence 與 Expansion

DRC 中的 Divergence：

$$
D
$$

可以被視為 Expansion 的一種方法。

即：

$$
D
\subseteq
E.
$$

DRC 的發散可能透過：

- query expansion；
- semantic expansion；
- multilingual expansion；
- graph neighborhood；
- counter-concept generation；
- hypothesis branching；
- source diversification；

形成：

$$
F_t.
$$

所以 DRC 在 UNPNP 中不必被限制為搜尋引擎技術。

---

# 10. Linking：從候選到真正 transition

展開後：

$$
F_t
=
\{
f_1,
f_2,
\ldots,
f_n
\}.
$$

Linking 的任務不是再增加候選，

而是決定：

$$
f_i
$$

是否能被轉成真正可穿越的 transition。

因此：

$$
L:
F_t
\rightarrow
\Gamma_t.
$$

其中：

$$
\Gamma_t
$$

可以是一條 link、link chain 或 conditional corridor。

---

# 11. Link 不等於相似

兩個底空間：

$$
B_i,
B_j
$$

語義很相似，

不表示：

$$
\ell_{ij}
$$

成立。

因此：

$$
\boxed{
\text{Semantic similarity}
\neq
\text{Executable connectivity}.
}
$$

真正的 link 至少需要：

- address；
- precondition；
- transition semantics；
- output contract；
- verification；
- capability compatibility。

---

# 12. Resonance 與 Linking

DRC 的 Resonance：

$$
R
$$

可以用來排序候選：

$$
F_t
\xrightarrow{R}
F_t'.
$$

但 Resonance 本身不等於 Linking。

更準確：

$$
\boxed{
R
\rightarrow
\text{candidate selection},
}
$$

而：

$$
\boxed{
L
\rightarrow
\text{transition realization}.
}
$$

所以：

$$
D
\rightarrow
R
\rightarrow
L
$$

可能是實際 runtime 的一種實現。

---

# 13. Linking 的最小條件

對候選：

$$
f_i
$$

若要升級為：

$$
\ell_i,
$$

至少要求：

$$
G_i(s_t)=1,
$$

其中：

$$
G_i
$$

是 guard。

並且：

$$
\operatorname{Resolvable}(a_i)=1,
$$

$$
\operatorname{Executable}(e_i)=1,
$$

$$
\operatorname{Verifiable}(v_i)=1.
$$

否則它只是 suggestion。

---

# 14. Linking 可以是平行的

並非所有計算都只能選一條路。

如果風險低、資源允許，

可以：

$$
L_t
=
\Gamma_1
\parallel
\Gamma_2
\parallel
\Gamma_3.
$$

然後由後續 Convergence 合併。

這對：

- 多來源搜尋；
- 多模型驗證；
- 多候選路徑；
- counter-evidence；
- benchmark；

尤其有用。

---

# 15. Linking 也可以是暫時性的

某條 link：

$$
\ell_t
$$

可能只在：

$$
[s_t,g_t,b_t]
$$

下成立。

所以：

$$
\ell_t
$$

不必永久加入：

$$
\mathcal L.
$$

可以只有：

$$
\text{ephemeral link}.
$$

只有經過多次驗證、重用與結晶後才變成穩定 primitive。

---

# 16. Convergence：收斂不是「給答案」

一般系統容易把 convergence 理解為：

> 終於得到答案，流程結束。

UNPNP 中更一般的定義是：

$$
C:
(\Gamma_t,O_t,V_t,H_t)
\rightarrow
S_{t+1}.
$$

其中：

- $\Gamma_t$：本輪 traversal；
- $O_t$：observations；
- $V_t$：verification；
- $H_t$：歷史狀態；
- $S_{t+1}$：新的壓縮工作狀態。

所以：

$$
\boxed{
\text{Convergence}
=
\text{state stabilization and compression}.
}
$$

---

# 17. Convergence 的輸出

收斂至少可能輸出：

$$
S_{t+1}
=
\langle
K_{t+1},
E_{t+1},
G_{t+1},
U_{t+1},
R_{t+1}
\rangle.
$$

其中：

- $K_{t+1}$：known state；
- $E_{t+1}$：verified evidence；
- $G_{t+1}$：remaining gaps；
- $U_{t+1}$：uncertainty；
- $R_{t+1}$：reopen / routing conditions。

因此收斂不是把所有事情壓成一句摘要。

---

# 18. Compression 與 Convergence

DRC 的 Compression：

$$
C_{\mathrm{DRC}}
$$

是 Convergence 的一種形式。

因此：

$$
C_{\mathrm{DRC}}
\subseteq
C_{\mathrm{UNPNP}}.
$$

DRC 壓縮可以輸出：

- cognitive map；
- summary；
- graph；
- next query；
- decision structure。

而 UNPNP Convergence 還要處理：

- runtime state；
- executable path；
- validator；
- future routing；
- possible crystallization。

---

# 19. 收斂不是資訊毀滅

若：

$$
C_t
$$

只留下極短 summary，

又刪除：

$$
\text{provenance},
$$

那不是好的收斂。

本文要求：

$$
\boxed{
\text{Compression}
+
\text{Recoverability}.
}
$$

也就是：

$$
S_{t+1}
\rightarrow
\text{relevant lower-level trace}
$$

仍應可能。

這為後續結晶化的可解壓性建立條件。

---

# 20. 收斂產生下一輪 Seed

最重要的是：

$$
C_t
$$

不是終點。

而是：

$$
\boxed{
C_t
\rightarrow
E_{t+1}.
}
$$

例如：

$$
S_{t+1}
$$

中的：

- unresolved gap；
- 新概念；
- 新底空間；
- 新 evidence；
- 新 failure；

會重新成為：

$$
E_{t+1}
$$

的種子。

---

# 21. 呼吸式計算

因此可以把一輪寫成：

$$
S_t
\xrightarrow{E_t}
F_t
\xrightarrow{L_t}
O_t
\xrightarrow{C_t}
S_{t+1}.
$$

整體：

$$
\boxed{
S_0
\xrightarrow{ELC}
S_1
\xrightarrow{ELC}
S_2
\xrightarrow{ELC}
\cdots
}
$$

這就是本文所稱：

$$
\boxed{
\text{Breathing Computation}.
}
$$

---

# 22. 為什麼像呼吸？

展開：

$$
|\Omega|\uparrow
$$

讓可能性增加。

連結：

$$
\Omega
\rightarrow
\Gamma
$$

形成可實際穿越結構。

收斂：

$$
|\Omega|\downarrow
$$

把無效與已處理部分壓縮。

所以：

$$
\boxed{
\text{Expand}
\rightarrow
\text{Traverse}
\rightarrow
\text{Compress}.
}
$$

再重新展開。

---

# 23. 呼吸不是週期性重算

如果每一輪：

$$
S_{t+1}=S_t,
$$

那只是重複。

真正有意義的呼吸要求：

$$
\boxed{
S_{t+1}
\neq
S_t
}
$$

至少在：

- knowledge；
- routing；
- uncertainty；
- corridor library；
- state；
- cost estimate；

某個維度改變。

---

# 24. 呼吸可以變快

第一次：

$$
C(ELC)_1
$$

可能很高。

如果系統學到穩定 corridor，

後面：

$$
C(ELC)_t
$$

可能下降。

理想：

$$
\frac{dC_{\mathrm{avg}}}{dt}<0.
$$

這代表：

> 系統不是只在重複計算，而是在讓自己的未來呼吸更便宜。

---

# 25. Local Convergence

本文先定義局部收斂：

$$
C_t:
F_t
\rightarrow
S_{t+1}
$$

只要求：

$$
S_{t+1}
$$

在當前任務域內足夠穩定。

不要求：

$$
S_{t+1}
=
S^\*_{\mathrm{global}}.
$$

因此：

$$
\boxed{
\text{Local convergence}
\neq
\text{global optimum}.
}
$$

---

# 26. 為什麼必須允許局部收斂？

若每輪都要求證明：

$$
\text{global optimum},
$$

那：

$$
C_V
$$

可能比原問題還昂貴。

因此實際系統更可能接受：

$$
\epsilon\text{-sufficient convergence}
$$

或：

$$
\text{task-sufficient convergence}.
$$

這種近似必須明確記錄，而不能偽裝成全域證明。

---

# 27. Reopen Condition

每個收斂狀態應帶：

$$
R_{\mathrm{open}}.
$$

例如：

$$
R_{\mathrm{open}}
=
\{
\text{new evidence},
\text{version change},
\text{goal change},
\text{confidence drop},
\text{failure}
\}.
$$

當：

$$
R_{\mathrm{open}}=1,
$$

則：

$$
C_t
\rightarrow
E_{t+1}.
$$

重新展開。

---

# 28. Convergence Stability

定義：

$$
S_C(S_t)
=
f(
\text{repeatability},
\text{evidence consistency},
\text{low uncertainty},
\text{environment stability}
).
$$

若：

$$
S_C\ge\theta_C,
$$

則狀態可以進入更高 reuse 等級。

---

# 29. Non-commutativity

展開、連結、收斂一般不可交換。

例如：

$$
C\circ E
$$

不等於：

$$
E\circ C.
$$

通常：

$$
\boxed{
C(E(S))
\neq
E(C(S)).
}
$$

同樣：

$$
L(E(S))
$$

與：

$$
E(L(S))
$$

也不是同一操作。

所以三元循環不是三個可任意重排的模組。

---

# 30. 為什麼 Linking 必須居中？

如果先收斂再建立 link：

$$
E
\rightarrow
C
\rightarrow
L,
$$

可能過早壓掉候選。

如果一直展開不 link：

$$
E
\rightarrow
E
\rightarrow
E,
$$

則會造成：

$$
\text{frontier explosion}.
$$

如果一直 link 不收斂：

$$
L
\rightarrow
L
\rightarrow
L,
$$

則會造成：

$$
\text{state accumulation}.
$$

所以：

$$
\boxed{
E
\rightarrow
L
\rightarrow
C
}
$$

形成一個自然平衡。

---

# 31. Frontier Explosion

令：

$$
|F_t|=n_t.
$$

若：

$$
n_{t+1}
\approx
b n_t,
$$

且：

$$
b>1,
$$

則：

$$
n_t
\sim
b^t.
$$

所以展開必須受到：

- budget；
- relevance；
- novelty；
- utility；
- risk；
- stopping；

控制。

---

# 32. Over-Convergence

反過來，

若每次：

$$
C_t
$$

太強，

可能只留下：

$$
|S_{t+1}|\approx 1.
$$

這會導致：

- confirmation bias；
- forgotten alternatives；
- lost provenance；
- premature closure；
- brittle routing。

因此收斂也需要最低 diversity。

---

# 33. Controlled Divergence

可以定義：

$$
B_E
$$

為 expansion budget。

要求：

$$
|F_t|
\le
B_E.
$$

或：

$$
C_E(F_t)
\le
B_E.
$$

這使 Expansion 成為受控算子，而不是無限發散。

---

# 34. Controlled Convergence

同樣定義：

$$
B_C
$$

為保留預算。

Convergence 不必只保留最高分候選。

可以保留：

$$
\{
\text{best},
\text{counter},
\text{uncertain},
\text{fallback}
\}.
$$

因此：

$$
\boxed{
\text{Convergence}
\neq
\text{winner-take-all}.
}
$$

---

# 35. Information Gain

可以用：

$$
I_t
=
H(S_t)-H(S_{t+1})
$$

粗略表示 uncertainty reduction。

但理想系統也要記錄：

$$
\Delta K_t
$$

新增知識，

以及：

$$
\Delta L_t
$$

新增可用 link。

所以收斂價值可能是：

$$
U_C
=
w_I I_t
+
w_K\Delta K_t
+
w_L\Delta L_t
-
w_C C_t.
$$

---

# 36. 多尺度 ELC

ELC 可以在不同尺度同時存在。

微觀：

$$
E^{(0)}
\rightarrow
L^{(0)}
\rightarrow
C^{(0)}.
$$

中觀：

$$
E^{(1)}
\rightarrow
L^{(1)}
\rightarrow
C^{(1)}.
$$

宏觀：

$$
E^{(2)}
\rightarrow
L^{(2)}
\rightarrow
C^{(2)}.
$$

例如一個 function call 是微觀，

一個遊戲任務是中觀，

一整個 strategy 是宏觀。

---

# 37. 巢狀呼吸

一個高層 Expansion：

$$
E^{(2)}
$$

可能要求啟動多個：

$$
ELC^{(1)}
$$

子循環。

所以：

$$
\boxed{
ELC
}
$$

本身可以遞歸巢狀。

這與底空間巢狀直接相容。

---

# 38. Async ELC

並非所有呼吸都需要同步。

可以有：

$$
ELC_{\mathrm{sync}}
$$

處理當前必要 transition，

以及：

$$
ELC_{\mathrm{async}}
$$

在背景處理：

- deeper verification；
- relation discovery；
- path comparison；
- cache promotion；
- future corridor preparation。

因此：

$$
\boxed{
\text{Sync maintains continuity;}
\quad
\text{Async improves structure}.
}
$$

---

# 39. 遊戲中的 ELC

在單機遊戲：

$$
S_t
$$

可能包含：

- player state；
- world state；
- NPC state；
- quest state；
- resources。

Expansion：

$$
S_t
\rightarrow
F_t
$$

生成：

- 行動；
- 路徑；
- 技能；
- 策略；
- 資訊需求。

Linking：

$$
F_t
\rightarrow
\Gamma_t
$$

選出並執行 action chain。

Convergence：

$$
\Gamma_t
\rightarrow
S_{t+1}
$$

更新：

- 世界狀態；
- 成功／失敗；
- 新 corridor；
- uncertainty；
- next goal。

---

# 40. 遊戲中的 Working-Set 優勢

假設整個遊戲 object：

$$
|O|=10^6.
$$

但當前任務只相關：

$$
|O_t^{\mathrm{active}}|=10^2.
$$

則：

$$
\frac{
|O_t^{\mathrm{active}}|
}{
|O|
}
=
10^{-4}.
$$

如果 semantic revealing 能可靠做到這種 reduction，

就可能大幅降低 AI reasoning cost。

---

# 41. ELC 與記憶搜尋

後續結晶化語義圖也可以使用相同循環。

Expansion：

$$
q
\rightarrow
\text{memory frontier}.
$$

Linking：

$$
\text{crystal}
\rightarrow
\text{crystal}
\rightarrow
\text{raw source}.
$$

Convergence：

$$
\text{retrieved traces}
\rightarrow
\text{active memory state}.
$$

所以 ELC 不只適用遊戲。

---

# 42. ELC 與 Omphalos

Omphalos 搜尋：

$$
\text{method selection}
\rightarrow
\text{execution}
\rightarrow
\text{evidence}
\rightarrow
\text{gap}.
$$

可以嵌入：

$$
E
\rightarrow
L
\rightarrow
C.
$$

例如：

$$
E=\text{search-method expansion},
$$

$$
L=\text{provider-bound execution},
$$

$$
C=\text{evidence/gap convergence}.
$$

---

# 43. ELC 與 Path Compilation

某一段穩定：

$$
E_t
\rightarrow
L_t
\rightarrow
C_t
$$

若反覆重現，

可以留下 trace：

$$
\tau_t.
$$

多次：

$$
\tau_1,\tau_2,\ldots,\tau_n
$$

若高度穩定，

則：

$$
K(\tau_{1:n})
\rightarrow
\widehat{\ell}.
$$

這就是後續 path compilation 的接口。

---

# 44. 呼吸產生結晶

本文正式提出：

$$
\boxed{
K_t
=
\operatorname{Crystallize}
(E_t,L_t,C_t).
}
$$

若：

$$
K_t\neq\varnothing,
$$

則：

$$
\mathcal L_{t+1}
=
\mathcal L_t
\cup
K_t.
$$

因此下一輪：

$$
E_{t+1}
$$

看到的是一個不同的計算世界。

---

# 45. 結晶改變下一次呼吸

若原本：

$$
E_t
$$

需要展開：

$$
100
$$

個候選，

但新結晶：

$$
\widehat{\ell}
$$

使下次：

$$
F_{t+1}
$$

只需要：

$$
10
$$

個候選，

則：

$$
C_E(t+1)
<
C_E(t).
$$

所以結晶化可以直接降低未來 Expansion 成本。

---

# 46. 呼吸與結晶的雙向關係

因此：

$$
\boxed{
\text{Breathing creates crystals;}
}
$$

以及：

$$
\boxed{
\text{Crystals reshape breathing}.
}
$$

形式：

$$
ELC_t
\rightarrow
K_t
\rightarrow
ELC_{t+1}.
$$

---

# 47. Dynamic Fixed Point

若系統最終達到：

$$
S_{t+1}
\approx
S_t,
$$

且：

$$
\mathcal L_{t+1}
\approx
\mathcal L_t,
$$

則可稱為：

$$
\epsilon\text{-stable computational fixed point}.
$$

但只要世界：

$$
\mathcal W_t
$$

繼續變化，

這個 fixed point 也可能被重新打開。

---

# 48. Dynamic Non-Fixed Stability

更一般地，

系統甚至可能：

$$
S_{t+1}\neq S_t
$$

但保持：

$$
\mathcal I(S_{t+1})
=
\mathcal I(S_t),
$$

其中：

$$
\mathcal I
$$

是核心不變量。

這是一種：

$$
\boxed{
\text{dynamic stability}.
}
$$

也就是狀態持續變，但重要結構保持。

---

# 49. 三元循環的成本

一輪成本：

$$
C_{\mathrm{ELC}}(t)
=
C_E(t)
+
C_L(t)
+
C_C(t)
+
C_B(t),
$$

其中：

$$
C_B
$$

是 boundary / coordination cost。

總成本：

$$
C_T
=
\sum_{t=1}^{T}
C_{\mathrm{ELC}}(t).
$$

如果 crystallization 成功，

理想：

$$
C_{\mathrm{ELC}}(t)
\downarrow
$$

於穩定工作負載。

---

# 50. ELC Efficiency

定義：

$$
\eta_{\mathrm{ELC}}
=
\frac{
\Delta U
}{
C_E+C_L+C_C
}.
$$

其中：

$$
\Delta U
$$

可以是：

- goal progress；
- information gain；
- cost reduction；
- corridor gain。

理想：

$$
\eta_{\mathrm{ELC}}(t)
\uparrow.
$$

---

# 51. 失敗也需要收斂

若 Linking 失敗：

$$
L_t
\rightarrow
\mathsf{fail},
$$

不代表本輪沒有價值。

Convergence 可以保存：

$$
C_t(
\mathsf{fail}
)
\rightarrow
\{
\text{failed guard},
\text{invalid route},
\text{new risk},
\text{blocked address}
\}.
$$

因此：

$$
\boxed{
\text{Failed traversal}
\rightarrow
\text{negative knowledge}.
}
$$

---

# 52. Negative Crystallization

甚至反覆失敗模式可以結晶成：

$$
\widehat{\ell}_{\mathrm{avoid}}.
$$

即：

> 某些狀態下不要再走這條路。

所以 crystallization 不只記錄成功 shortcut。

也可以記錄：

$$
\boxed{
\text{verified forbidden / useless corridor}.
}
$$

---

# 53. ELC 的安全接口

Expansion 可以看見：

$$
\text{reachable candidates}.
$$

但 Linking 前必須檢查：

$$
\text{authorization}.
$$

所以：

$$
\boxed{
E
\not\Rightarrow
L.
}
$$

也就是：

> 被顯影、被看到，不代表可以執行。

這個安全邊界留給後續 Series 09 深入展開。

---

# 54. ELC 不等於 P=NP

即使某個系統能透過 ELC：

$$
C_{\mathrm{avg}}
\downarrow,
$$

也不能推出：

$$
P=NP.
$$

因為：

- corridor generation 成本可能高；
- 外部資源可能很大；
- reuse 可能依賴預計算；
- uniformity 未必成立；
- worst-case 未必改善。

所以：

$$
\boxed{
\text{ELC efficiency}
\neq
\text{classical complexity collapse}.
}
$$

---

# 55. 核心命題一

$$
\boxed{
\textbf{
UNPNP 的基本動態不是「搜索—回答」，
而是「展開—連結—收斂」。
}
}
$$

---

# 56. 核心命題二

$$
\boxed{
\textbf{
展開負責生成局部可能世界；
連結負責把候選轉成可穿越 transition；
收斂負責把本輪結果壓縮成下一輪可用狀態。
}
}
$$

---

# 57. 核心命題三

$$
\boxed{
\textbf{
收斂不是終止條件，而是下一次展開的起點。
}
}
$$

---

# 58. 核心命題四

$$
\boxed{
\textbf{
呼吸若能留下可驗證的結晶，
則系統的下一次呼吸可以比前一次更短、更便宜或更直接。
}
}
$$

---

# 59. 第一版總模型

本文將一輪 UNPNP 動態寫成：

$$
\boxed{
S_t
\xrightarrow{\Pi_{\xi_t}}
W_t
\xrightarrow{E_t}
F_t
\xrightarrow{L_t}
O_t
\xrightarrow{C_t}
S_{t+1}.
}
$$

其中：

- $\Pi_{\xi_t}$：顯影；
- $W_t$：active working set；
- $E_t$：Expansion；
- $F_t$：frontier；
- $L_t$：Linking；
- $O_t$：observed transition result；
- $C_t$：Convergence；
- $S_{t+1}$：下一輪狀態。

若可結晶：

$$
K_t
=
K(E_t,L_t,C_t).
$$

則：

$$
\mathcal L_{t+1}
=
\mathcal L_t
\cup
K_t.
$$

---

# 60. 結論

UNPNP 的計算世界不應被理解成一張固定圖，AI 在裡面永遠尋找一條最短路徑。

更接近的結構是：

$$
\boxed{
\text{世界}
\rightarrow
\text{局部顯影}
\rightarrow
\text{展開}
\rightarrow
\text{連結}
\rightarrow
\text{收斂}
\rightarrow
\text{世界的重新表示}.
}
$$

展開讓潛在關係變得可見。

連結讓可能性變成真正可執行的 passage。

收斂讓已經走過的世界被壓縮成新的狀態。

而這個新狀態再次：

$$
\text{展開}.
$$

因此：

$$
\boxed{
E
\rightarrow
L
\rightarrow
C
\rightarrow
E
\rightarrow
L
\rightarrow
C
\rightarrow
\cdots
}
$$

不是單純的 workflow。

它是一個可以逐步改變自身計算結構的動態循環。

如果一次成功呼吸：

$$
E_t
\rightarrow
L_t
\rightarrow
C_t
$$

只留下結果，

那它只是一次計算。

如果它還能留下：

$$
K_t,
$$

使未來：

$$
C_{\mathrm{ELC}}(t+1)
<
C_{\mathrm{ELC}}(t),
$$

那它開始成為：

$$
\boxed{
\text{self-optimizing computation}.
}
$$

因此本篇可以用一句話收束：

$$
\boxed{
\textbf{
呼吸產生結晶，結晶改變下一次呼吸。
}
}
$$

而下一篇將把這個循環推到更底層的執行結構：

> 如果展開、尋址、執行、生成與驗證可以高度耦合，傳統 pipeline 是否能被重新壓成一個新的計算 transition？

這正是下一篇的問題。

---

## 後續篇章

**Series 05｜耦合計算：尋址即執行即生成即驗證**

下一篇將處理：

$$
A
\otimes
P
\otimes
E
\otimes
G
\otimes
V,
$$

並正式區分：

$$
\text{Coupling}
\neq
\text{Logical Identity},
$$

以及：

- addressing；
- permission / authorization；
- execution；
- generation；
- verification；
- pipeline collapse；
- boundary removal；
- fast path；
- why coupling can improve efficiency；
- why coupling without safety boundaries can amplify failure。
