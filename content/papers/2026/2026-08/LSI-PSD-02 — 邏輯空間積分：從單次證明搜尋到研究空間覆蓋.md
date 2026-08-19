# LSI-PSD-02 — 邏輯空間積分：從單次證明搜尋到研究空間覆蓋

## Logic-Space Integration: From Single Proof Search to Research-Space Coverage

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 02  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Coverage Formalization Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文建立「邏輯空間積分」的操作性數學框架，用來描述長程 AI 數學研究中已探索、已驗證、已排除、已回訪與仍未知的研究區域。本文所稱的 coverage、integration、saturation、basin、obstruction coverage 等量，首先是對特定搜尋制度之可觀測研究狀態的度量，不等於對所有可能證明、所有可能表示、所有可能公理擴張或數學真理本身的完整測度。本文不主張已能計算任何公開未解問題的「真實總證明空間百分比」，更不把 coverage 高、novelty 下降或局部飽和視為原命題錯誤、不可證、不可判定或已被反證的證據。

---

## 摘要

當 AI 數學研究從單次輸出擴張到數百、數千甚至更長的持續研究輪次時，「是否找到最終證明」不再足以描述研究系統的進度。大量中間引理、失敗路徑、表示切換、反例候選、形式驗證、數值實驗與跨路線匯流會形成一個具有歷史、局部性與重訪結構的研究空間。若這些資料只以最後成功或失敗二分，則研究系統無法回答一個更基礎的問題：**我們究竟探索了什麼，以及新增一輪研究到底增加了多少可審計的新資訊？**

本文提出「邏輯空間積分」的第一個完整形式化框架。承接 LSI-PSD-01 所定義的搜尋制度

$$
R=(\mathcal A,\mathcal L,\mathcal M,\mathcal V,B,\mathcal K,\Sigma),
$$

本文把研究空間區分為形式可證域、制度可達域、觀測域、驗證域與暫存研究記憶，並在適當的語義商空間上定義 coverage function：

$$
c_N:\bar\Omega_R(Q)\rightarrow[0,1].
$$

由此定義理想化的邏輯空間積分：

$$
I_N
=
\int_{\bar\Omega_R(Q)}
c_N(\omega)\,d\mu(\omega),
$$

以及增量：

$$
\Delta I_N
=
I_{N+1}-I_N.
$$

但本文特別指出：在真正未解數學問題中，分母 $\bar\Omega_R(Q)$ 通常未知，測度 $\mu$ 也不存在天然唯一選擇。因此， $I_N$ 首先是一個**理論極限量**，不能被輕率轉譯為「已探索了 $73\%$ 的證明空間」。可操作實驗應改用一組不假裝知道總空間大小的相對量，包括 state coverage、route coverage、obstruction coverage、method-family coverage、representation coverage、verification coverage 與 local-basin coverage。本文因此主張使用 coverage vector：

$$
\mathbf C_N
=
(
C_N^{state},
C_N^{route},
C_N^{obs},
C_N^{method},
C_N^{repr},
C_N^{ver}
),
$$

而不是過早把所有研究歷史壓縮成一個單一百分比。

本文進一步定義負資訊的積分效應：一條經審計的 no-go route 雖然沒有提供最終證明，卻可以合法縮小制度內的候選區域：

$$
\Omega_{N+1}^{surv}
=
\Omega_N^{surv}\setminus E_N,
$$

其中 $E_N$ 必須有明確條件、適用域與可重現證據。這使「失敗」第一次能被區分為零資訊失敗與正向 coverage gain。本文也定義 marginal research yield：

$$
\eta_N
=
\frac{\Delta \widetilde I_N}{\operatorname{Cost}(N,N+1)},
$$

用來衡量每單位算力、人工審計或生成成本所換得的新增可驗證研究區域。

近年的自動定理證明工作已顯示 proof search 應被視為軌跡與圖搜尋問題。LeanProgress 直接估計 proof trajectory 的剩餘步數；BFS-Prover、AlphaProof、TreeThink 等系統以搜尋樹與 verifier feedback 導航 proof space；Aristotle 將正式 proof search 與非正式推理、lemma generation 結合；AlphaProof Nexus 在公開未解問題上以多代理正式搜尋與 Lean 驗證工作；2026 年的 theorem testing benchmark 則顯示 theorem statement 能成功編譯，不代表其語義已被充分保存，後續 dependent theorems 可提供更強測試。這些結果共同說明，單一 pass/fail 指標不足以表示長程研究進度。

本文最後以 NS-203 長程 Navier--Stokes 語料作為原型案例。該案例已出現 route revisit、cross-series dependency、obstruction confluence 與局部 higher-order sampling，但固定窗口 novelty 統計並不支持「全域 novelty 已崩潰」的結論。這個結果用來示範本文最重要的原則：**coverage 可以局部增加，飽和可以局部成立，而全域證明空間仍然保持未知。**

**關鍵詞：** 邏輯空間積分、證明空間覆蓋、proof search、研究空間、coverage vector、局部飽和、negative information、obstruction、route graph、驗證權重、AI 數學研究、Navier--Stokes

---

# 1. 從「有沒有證明」轉向「研究空間增加了什麼」

## 1.1 單次 theorem proving 的成功函數

最簡單的自動定理證明評估可以寫為：

$$
S(Q)
=
\begin{cases}
1,&\exists \pi:\mathcal V(\pi,Q)=1,\\
0,&\text{otherwise}.
\end{cases}
$$

這個成功函數對 benchmark 很有用。

它回答：

> 這個系統是否找到一個 verifier 接受的證明？

但它刻意忽略：

- 嘗試過多少條路；
- 哪些中間引理已被證明；
- 哪些表示被證明難以處理；
- 哪些方法族反覆撞上同一障礙；
- 哪些失敗其實排除了大區域候選；
- 哪些路徑只是假重複；
- 哪些新結果沒有進入最終 proof term，卻能被其他研究重用。

因此：

$$
S(Q)
$$

是一個**終點指標**，不是研究歷史指標。

## 1.2 長程研究需要另一種進度概念

假設 AI 在固定問題 $Q$ 上持續工作 $N$ 輪。

每一輪產生研究事件：

$$
e_i
=
(
q_i,
s_i,
a_i,
r_i,
v_i,
t_i
),
$$

其中可以分別表示：

- $q_i$：當輪局部目標；
- $s_i$：進入時研究狀態；
- $a_i$：採取的方法或 action；
- $r_i$：輸出的候選結果；
- $v_i$：驗證狀態；
- $t_i$：時間、版本或 provenance。

完整歷史為：

$$
\mathcal H_N
=
(e_1,e_2,\ldots,e_N).
$$

如果最後仍沒有證明，傳統成功函數仍然只有：

$$
S(Q)=0.
$$

但這不代表：

$$
\mathcal H_N
=
\varnothing.
$$

反而可能：

$$
|\mathcal H_N|
\gg1.
$$

因此長程研究需要回答另一個問題：

$$
\boxed{
\text{How much structured research space has been traversed, tested, or ruled out?}
}
$$

本文把這個問題稱為：

$$
\boxed{
\textbf{Logic-Space Integration}
}
$$

即「邏輯空間積分」。

---

# 2. 邏輯空間不是字串空間

## 2.1 最粗糙的錯誤：把 token 數當探索量

如果把每一段生成文字都視為一個新研究點，則只要修改：

- 符號名稱；
- 句子順序；
- lemma 名稱；
- Markdown 排版；
- 變數字母；
- 同義詞；
- proof sketch 的自然語言表述；

就可以無限增加「探索量」。

這顯然不合理。

因此：

$$
\text{Text Space}
\neq
\text{Logic Space}.
$$

甚至：

$$
\text{Syntactic Novelty}
\neq
\text{Proof Novelty}.
$$

## 2.2 一階研究單元

本文暫時把一個研究單元表示為：

$$
x
=
(
P,
A,
M,
R,
O,
V
),
$$

其中：

- $P$：proposition / subgoal；
- $A$：assumptions；
- $M$：method / transformation；
- $R$：result；
- $O$：obstruction / failure mode；
- $V$：verification status。

兩段文字若表面不同，但經 canonicalization 後得到相同：

$$
(P,A,M,R,O,V),
$$

則應視為同一或高度等價研究狀態。

## 2.3 語義等價關係

定義暫定等價關係：

$$
x\sim y
$$

若 $x,y$ 在研究任務所關心的結構上不可區分。

例如：

$$
\begin{aligned}
&\text{rename}(x)=y,\\
&\text{reorder}(x)=y,\\
&\text{parameter-normalize}(x)=y,\\
&\text{same-proof-skeleton}(x,y)=1.
\end{aligned}
$$

真正要積分的空間不應是 $\Omega$，而至少是：

$$
\bar\Omega
=
\Omega/\sim.
$$

這裡的 $\sim$ 不可能一次完美定義。

因此 LSI-PSD-03 將專門處理：

$$
\boxed{
\text{Semantic Quotient Space}
}
$$

問題。

本文先使用「任務相對等價」作為操作性前提。

---

# 3. 搜尋制度與五種不同的空間

## 3.1 搜尋制度回顧

承接第一篇，定義搜尋制度：

$$
R
=
(
\mathcal A,
\mathcal L,
\mathcal M,
\mathcal V,
B,
\mathcal K,
\Sigma
).
$$

其中：

- $\mathcal A$：公理與背景理論；
- $\mathcal L$：表示語言；
- $\mathcal M$：方法族；
- $\mathcal V$：驗證系統；
- $B$：資源界；
- $\mathcal K$：既有知識與資料；
- $\Sigma$：調度、搜索與 agent 策略。

同一個 $Q$ 在不同 $R$ 下，具有完全不同的可達區域。

所以：

$$
\Omega_R(Q)
$$

不是數學宇宙本身。

它只是：

> 在目前制度下，可被產生、表示、調用、驗證或探索的研究狀態集合。

## 3.2 形式可證空間

令：

$$
\Omega_{formal}(Q;\mathcal A)
$$

表示在背景形式系統 $\mathcal A$ 中與 $Q$ 有關的合法 proof states、proof objects 與中間命題空間。

這已經可能極大，甚至根本不可實際枚舉。

## 3.3 制度可達空間

加入語言、方法、工具與資源限制：

$$
\Omega_R^{reach}(Q)
\subseteq
\Omega_{formal}(Q;\mathcal A).
$$

它表示：

> 理論上此搜尋制度有機會走到的區域。

這個集合仍然通常未知。

## 3.4 實際觀測空間

經過 $N$ 輪後真正走過：

$$
\Omega_N^{obs}(Q;R)
\subseteq
\Omega_R^{reach}(Q).
$$

這是我們最容易從 logs、artifact、proof state、tool execution 與版本紀錄重建的部分。

## 3.5 已驗證空間

只有通過指定驗證門檻的部分進入：

$$
\Omega_N^{ver}
\subseteq
\Omega_N^{obs}.
$$

可再分級：

$$
\Omega_N^{ver}
=
\Omega_N^{formal}
\cup
\Omega_N^{checked}
\cup
\Omega_N^{empirical},
$$

但不同級別不可混稱為相同強度。

## 3.6 研究記憶空間

研究系統還可能保存：

$$
\Omega_N^{mem}.
$$

其中包含：

- 未完成 proof sketch；
- speculative conjecture；
- failed branch；
- counterexample candidate；
- heuristic；
- literature lead；
- unresolved obstruction。

所以：

$$
\Omega_N^{mem}
\not\subseteq
\Omega_N^{ver}.
$$

但：

$$
\Omega_N^{mem}
$$

仍然可能具有高 routing value。

## 3.7 五空間不能混在一起

因此至少要維持：

$$
\boxed{
\Omega_{formal},
\Omega_R^{reach},
\Omega_N^{obs},
\Omega_N^{ver},
\Omega_N^{mem}
}
$$

五者分離。

尤其不能從：

$$
\Omega_N^{obs}
\approx
\Omega_R^{reach}
$$

就推成：

$$
\Omega_N^{obs}
\approx
\Omega_{formal}.
$$

更不能推成：

$$
\Omega_N^{obs}
\approx
\text{all mathematical possibilities}.
$$

---

# 4. 邏輯空間積分的理想定義

## 4.1 coverage function

在語義商空間：

$$
\bar\Omega_R(Q)
=
\Omega_R(Q)/\sim
$$

上，定義 coverage function：

$$
c_N:
\bar\Omega_R(Q)
\rightarrow
[0,1].
$$

直觀上：

$$
c_N(\omega)=0
$$

表示尚未觀察；

$$
c_N(\omega)=1
$$

表示在指定研究標準下已充分探索；

中間值表示：

- 僅生成；
- 僅局部驗證；
- 僅一種表示採樣；
- 缺乏獨立重現；
- 仍有重要子路徑未處理。

## 4.2 理想積分

若 $\bar\Omega_R(Q)$ 上存在適當測度 $\mu$，定義：

$$
I_N
=
\int_{\bar\Omega_R(Q)}
c_N(\omega)\,d\mu(\omega).
$$

這是本文名稱「邏輯空間積分」最直接的形式。

如果：

$$
\mu(\bar\Omega_R)=1,
$$

則形式上：

$$
0\le I_N\le1.
$$

但這個 normalization 只在 $\mu$ 已被合理定義時有意義。

## 4.3 為什麼不能隨便說「已探索 80%」

對真正困難數學問題，我們通常不知道：

$$
|\bar\Omega_R|.
$$

甚至不知道：

$$
\mu.
$$

更不知道不同 proof state 是否應該等權。

例如：

一千個同類參數變體：

$$
\omega_1,\ldots,\omega_{1000}
$$

可能比不上一次表示變換：

$$
T:\mathcal L_1\rightarrow\mathcal L_2
$$

所帶來的新研究區域。

因此：

$$
\boxed{
I_N\text{ 是理論極限量，不是天然可觀測百分比。}
}
$$

## 4.4 不完整測度仍然有用

即使無法得到全域 $\mu$，仍可在局部 chart：

$$
U\subset\bar\Omega_R
$$

上定義：

$$
I_N(U)
=
\int_U c_N(\omega)\,d\mu_U(\omega).
$$

這意味著：

> 全域 coverage 不可知，不妨礙局部 coverage 可測。

這一點對後續「局部飽和」至關重要。

---

# 5. 從單一積分改成 Coverage Vector

## 5.1 為什麼單一 scalar 太粗

假設兩個研究系統：

系統 A：

- 嘗試很多 states；
- 幾乎沒有驗證；
- route 很重複。

系統 B：

- states 較少；
- route 多樣；
- 每條都高度驗證；
- obstruction catalog 完整。

如果都壓成一個 $I_N$，可能失去最重要差別。

因此本文定義 coverage vector：

$$
\mathbf C_N
=
(
C_N^{state},
C_N^{route},
C_N^{obs},
C_N^{method},
C_N^{repr},
C_N^{ver}
).
$$

## 5.2 State Coverage

$$
C_N^{state}
$$

衡量已到訪 canonical research state 的範圍。

操作代理量可寫成：

$$
\widetilde C_N^{state}
=
|V_N^{uniq}|,
$$

其中 $V_N^{uniq}$ 是 canonicalized node set。

注意：

$$
|V_N^{uniq}|
$$

是絕對數，不是假裝知道全域分母的比例。

## 5.3 Route Coverage

令 proof-route graph：

$$
G_N=(V_N,E_N).
$$

route coverage 可觀察：

$$
\widetilde C_N^{route}
=
|E_N^{uniq}|.
$$

或考慮 route family：

$$
\mathcal R_N
=
\{[r_1],[r_2],\ldots,[r_m]\},
$$

其中：

$$
r_i\sim_r r_j
$$

表示兩條路在 transformation skeleton 上等價。

則：

$$
\widetilde C_N^{route-family}
=
|\mathcal R_N|.
$$

## 5.4 Obstruction Coverage

定義 canonical obstruction set：

$$
\mathcal O_N
=
\{O_1,O_2,\ldots,O_k\}.
$$

每個 $O_i$ 必須至少包含：

$$
O_i
=
(
\text{trigger},
\text{scope},
\text{failure mechanism},
\text{evidence},
\text{status}
).
$$

因此：

$$
\widetilde C_N^{obs}
=
|\mathcal O_N|.
$$

更重要的是重訪 multiplicity：

$$
m_N(O_i)
=
\#\{r:r\rightarrow O_i\}.
$$

以及跨方法匯流度：

$$
\kappa_N(O_i)
=
\#\{M_j: M_j\rightarrow O_i\}.
$$

## 5.5 Method-Family Coverage

若方法族為：

$$
\mathcal M
=
\{M_1,M_2,\ldots\},
$$

定義：

$$
\widetilde C_N^{method}
=
|\{M_i:\text{sampled by time }N\}|.
$$

但必須區分「叫了方法名稱」和「真的執行到能產生判定資訊」。

所以引入 method engagement weight：

$$
e_N(M_i)\in[0,1].
$$

則：

$$
C_N^{method,w}
=
\sum_i e_N(M_i).
$$

## 5.6 Representation Coverage

表示空間可能包含：

$$
\mathcal L
=
\{L_1,L_2,\ldots,L_s\}.
$$

例如同一問題可能使用：

- physical variables；
- vorticity form；
- Fourier representation；
- geometric formulation；
- weak formulation；
- functional-analytic representation；
- formal proof assistant encoding。

定義：

$$
C_N^{repr}
$$

衡量真正被採樣的 representation family。

這裡非常重要，因為：

$$
\text{route saturation in }L_1
$$

不代表：

$$
\text{route saturation in }L_2.
$$

## 5.7 Verification Coverage

定義驗證權重：

$$
w_v(x)
\in
[0,1].
$$

例如可以建立分級：

$$
0
<
w_{spec}
<
w_{crosscheck}
<
w_{formal}
\le1.
$$

這不是宣稱形式驗證涵蓋所有語義問題，而是表示：

> 在指定 statement 與形式系統內，其 deductive correctness 的驗證強度更高。

可定義：

$$
C_N^{ver}
=
\sum_{x\in V_N}w_v(x).
$$

---

# 6. 驗證不是一個 bit：Verification Lattice

## 6.1 binary verifier 的優點與限制

Lean 等 proof assistant 對已形式化 statement 可以給出非常強的：

$$
\mathcal V(\pi,Q)=1.
$$

但這仍然不能自動回答：

- $Q$ 是否忠實表達原始自然語言命題；
- 定義是否偷換；
- theorem statement 是否過弱；
- formalization 是否漏掉假設；
- 生成的 theorem 是否保留原 repository 的語義接口。

因此：

$$
\text{formal validity}
\neq
\text{complete semantic fidelity}.
$$

## 6.2 2026 theorem testing 的啟示

2026 年的 automated theorem proving testing 工作提出類似 integration testing 的概念：

生成的 theorem 不只要 compile，還要讓依賴它的 successor theorems 繼續成功。

形式化表示為：

$$
\operatorname{Compile}(T)=1
$$

仍不足；

還要求：

$$
\forall S_j\in Succ(T),
\quad
\operatorname{Compile}(S_j\mid T)=1.
$$

這提供一個重要方向：

$$
\boxed{
\text{verification strength can be relational.}
}
$$

## 6.3 驗證格

本文建議把驗證寫成 lattice-like state：

$$
V(x)
=
(
v_{syntax},
v_{formal},
v_{semantic},
v_{independent},
v_{transfer}
).
$$

其中：

- $v_{syntax}$：語法合法；
- $v_{formal}$：形式 proof checker 通過；
- $v_{semantic}$：statement 與原命題語義對齊；
- $v_{independent}$：獨立方法或獨立 agent 重現；
- $v_{transfer}$：作為上游結果時能否支援下游 theorem / computation。

因此兩個都「verified」的 artifact，仍可能驗證結構不同。

## 6.4 coverage 必須攜帶驗證資訊

因此：

$$
c_N(\omega)
$$

不應只由「曾到訪」決定。

更合理：

$$
c_N(\omega)
=
f(
visit,
repeat,
verification,
representation,
independent\_support
).
$$

例如一個簡化版本：

$$
c_N(\omega)
=
1-
\prod_{j=1}^{m}
(1-w_j e_{j,N}(\omega)),
$$

其中 $e_{j,N}$ 表示不同證據通道是否覆蓋該狀態。

這個公式不是唯一正確定義，而是說明：

> coverage 可以是多證據累積，而不是 visit counter。

---

# 7. 增量：研究真正重要的是 $\Delta I$ 而不是輸出長度

## 7.1 積分增量

定義：

$$
\Delta I_N
=
I_{N+1}-I_N.
$$

如果第 $N+1$ 輪只是重新描述已知內容：

$$
\Delta I_N
\approx0.
$$

即使輸出：

$$
10^4\text{ tokens}.
$$

相反，如果只增加一個短 lemma，但它開啟全新 route family：

$$
\Delta I_N
\gg0.
$$

即使文字非常短。

因此：

$$
\boxed{
\text{Output Volume}
\neq
\text{Research Increment}.
}
$$

## 7.2 研究邊際收益

令本輪成本：

$$
\operatorname{Cost}_N
=
\alpha C_{compute}
+
\beta C_{human}
+
\gamma C_{verification}
+
\delta C_{retrieval}.
$$

定義：

$$
\eta_N
=
\frac{\Delta\widetilde I_N}{\operatorname{Cost}_N}.
$$

其中 $\widetilde I_N$ 是可操作代理積分。

 $\eta_N$ 可稱：

$$
\boxed{
\text{Marginal Research Yield}
}
$$

即「邊際研究收益」。

## 7.3 高產出不等於高收益

可能：

$$
Tokens_N\uparrow
$$

但：

$$
\eta_N\downarrow.
$$

這就是長程 AI 研究最容易出現的假繁榮：

> 生成量很大，但新 canonical state 幾乎沒有增加。

因此監控系統不能只報：

- paper count；
- token count；
- branch count。

而要報：

$$
\Delta V_N^{uniq},
\quad
\Delta E_N^{uniq},
\quad
\Delta\mathcal O_N,
\quad
\Delta\mathcal M_N,
\quad
\Delta\mathcal L_N.
$$

---

# 8. 負結果如何增加 coverage

## 8.1 一般直覺：失敗等於沒有進展

在只看最終 proof 的評估中：

$$
\text{failed attempt}
\mapsto
0.
$$

但長程研究不應如此粗糙。

## 8.2 可審計 no-go region

假設某 route family $R_a$ 在條件：

$$
H_a
$$

下被嚴格證明無法完成某 closure。

則可定義排除區域：

$$
E_a
=
\{x\in\Omega: H_a(x)\land R_a(x)\text{ fails by mechanism }O_a\}.
$$

如果 $E_a$ 有清楚適用域，就可以更新 survivor space：

$$
\Omega_{N+1}^{surv}
=
\Omega_N^{surv}
\setminus E_a.
$$

這是：

$$
\boxed{
\text{negative result}
\rightarrow
\text{positive space reduction}
}
$$

## 8.3 什麼失敗不能算 coverage gain

以下通常不能直接算：

- 模型說「我想不到」；
- 某次 generation timeout；
- syntax error；
- prompt 沒寫清楚；
- 沒有完整跑完搜索；
- 只測了一個參數點；
- 沒有排除等價繞路；
- obstruction 沒有被重現。

這些最多是：

$$
\text{execution failure}.
$$

不是：

$$
\text{mathematical no-go}.
$$

## 8.4 負結果分級

可定義：

$$
N_0:
\text{unexplained failure},
$$

$$
N_1:
\text{reproducible local failure},
$$

$$
N_2:
\text{identified obstruction},
$$

$$
N_3:
\text{proved no-go under explicit assumptions},
$$

$$
N_4:
\text{method-family no-go over a defined class}.
$$

coverage weight 應隨級別增加，但仍只在其適用域內成立。

---

# 9. 路由圖：邏輯空間積分的離散骨架

## 9.1 proof-route graph

定義：

$$
G_N
=
(V_N,E_N).
$$

其中 node 可包括：

$$
V_N
=
V^{claim}
\cup
V^{lemma}
\cup
V^{repr}
\cup
V^{obs}
\cup
V^{status}.
$$

edge 可包括：

$$
E_N
=
E^{depends}
\cup
E^{transforms}
\cup
E^{supports}
\cup
E^{contradicts}
\cup
E^{revisits}
\cup
E^{converges}.
$$

## 9.2 Hyperedge 比普通 edge 更自然

很多 proof step 不是：

$$
x\rightarrow y.
$$

而是：

$$
(x_1,x_2,\ldots,x_k)
\Rightarrow y.
$$

因此更一般地應使用 hypergraph：

$$
\mathcal G_N
=(V_N,\mathcal E_N).
$$

其中：

$$
e
=
(
\{x_1,\ldots,x_k\},
y,
method,
verification
).
$$

## 9.3 路徑不是證明

一條 graph path：

$$
p=(v_0,e_1,v_1,\ldots,v_m)
$$

只表示研究路由。

只有當：

- 所有 required premise 合法；
- inference verified；
- statement fidelity 已確認；
- terminal node 等於 target；

才可稱為正式 proof path。

所以：

$$
\boxed{
\text{route graph}
\neq
\text{proof certificate}.
}
$$

## 9.4 Graph coverage

可以定義局部：

$$
C_G(N;U)
=
\frac{|V_N\cap U|}{|U|},
$$

前提是 $U$ 為有限已知 benchmark subgraph。

對未知開放研究空間，則只報：

$$
|V_N^{uniq}|,
\quad
|E_N^{uniq}|,
\quad
\operatorname{components}(G_N),
\quad
\operatorname{cycle}(G_N),
\quad
\operatorname{confluence}(G_N).
$$

---

# 10. 局部盆地與局部積分

## 10.1 proof basin

定義一個研究盆地：

$$
B_i
\subseteq
\bar\Omega_R
$$

若其內部 states 在：

- 方法；
- representation；
- obstruction；
- dependency；
- proof skeleton；

上具有高內部耦合。

## 10.2 basin coverage

若 $B_i$ 已有有限 canonical map：

$$
C_N(B_i)
=
\frac{|V_N\cap B_i|}{|B_i|}.
$$

若 $|B_i|$ 仍未知，可以用：

$$
\widetilde C_N(B_i)
=
(
|V_N\cap B_i|,
|E_N\cap B_i|,
|\mathcal O_N\cap B_i|,
\rho_N^{revisit}(B_i)
).
$$

## 10.3 局部飽和不等於全域飽和

可能存在：

$$
\Delta\widetilde I_N(B_1)
\rightarrow0,
$$

但是：

$$
\Delta\widetilde I_N(B_2)
>0.
$$

所以：

$$
\boxed{
\text{local saturation}
\not\Rightarrow
\text{global saturation}.
}
$$

這是本文與後續第五篇的核心橋樑。

## 10.4 Representation escape

如果：

$$
B_i\subset L_1
$$

已高度飽和，新的表示 $L_2$ 可能建立：

$$
T:L_1\rightarrow L_2
$$

並使：

$$
\Delta I_N(B_i;L_2)
\gg0.
$$

因此 saturation detector 應輸出：

> Current basin under current representation saturated.

而不是：

> Problem saturated.

---

# 11. Novelty 不是 Coverage，但可以作為增量訊號

## 11.1 textual novelty 的危險

文本向量距離：

$$
1-\operatorname{sim}_{text}(x_i,x_j)
$$

只能反映表述差異。

不能直接當：

$$
\Delta I.
$$

## 11.2 semantic route novelty

更合理：

$$
\nu_N^{route}
=
1-
\max_{j\in W_N}
\operatorname{sim}_{route}(r_N,r_j),
$$

其中 $W_N$ 是固定大小的回看窗。

固定窗口非常重要。

如果使用全部歷史：

$$
\nu_N
=
1-
\max_{j<N}\operatorname{sim}(x_N,x_j),
$$

則隨著 $N$ 增加，可比較樣本天然變多，最大相似度會機械性上升。

這會產生假 saturation。

## 11.3 fixed-window estimator

令窗口：

$$
W_N
=
\{N-w,\ldots,N-1\}.
$$

定義：

$$
\nu_N^{(w)}
=
1-
\max_{j\in W_N}
\operatorname{sim}_{sem}(x_N,x_j).
$$

再和 random permutation baseline 比較。

## 11.4 novelty decay 的弱結論

如果：

$$
\nu_N^{(w)}\downarrow
$$

只能先說：

> 在目前 representation 與 similarity metric 下，新 artifact 與最近歷史越來越相似。

不能直接說：

$$
\Omega\text{ 已耗盡}.
$$

更不能說：

$$
Q\text{ 不可證}.
$$

---

# 12. 邏輯空間積分的多階結構

## 12.1 一階積分

一階採樣 states：

$$
\Omega^{(0)}.
$$

積分：

$$
I_N^{(0)}
=
\int_{\Omega^{(0)}}c_N^{(0)}(x)d\mu_0(x).
$$

## 12.2 二階積分

採樣 transitions / proof moves：

$$
\Omega^{(1)}.
$$

$$
I_N^{(1)}
=
\int_{\Omega^{(1)}}c_N^{(1)}(T)d\mu_1(T).
$$

## 12.3 三階積分

研究 route relations：

$$
\Omega^{(2)}.
$$

例如：

$$
T_a\sim T_b,
$$

或：

$$
T_a,T_b,T_c\rightarrow O.
$$

定義：

$$
I_N^{(2)}
=
\int_{\Omega^{(2)}}c_N^{(2)}(R)d\mu_2(R).
$$

## 12.4 X 階

一般：

$$
I_N^{(k)}
=
\int_{\Omega^{(k)}}c_N^{(k)}(\xi)d\mu_k(\xi).
$$

因此完整研究狀態不是單一 $I_N$，而是：

$$
\mathbf I_N
=
(
I_N^{(0)},
I_N^{(1)},
I_N^{(2)},
\ldots
).
$$

這為第四篇「高階證明空間採樣」預留正式接口。

---

# 13. Search Progress 與 Coverage：從 LeanProgress 到全域研究歷史

## 13.1 proof progress 的局部形式

LeanProgress 類工作把 theorem proving 視為狀態轉移：

$$
s_0
\xrightarrow{a_1}
s_1
\xrightarrow{a_2}
\cdots
\xrightarrow{a_T}
s_T.
$$

並估計：

$$
\hat d(s_t)
\approx
\text{remaining proof steps}.
$$

這是一種：

$$
\boxed{
\text{trajectory-aware progress}
}
$$

而不是只預測下一 tactic。

## 13.2 進度不等於覆蓋

但是：

$$
\hat d(s_t)
$$

和：

$$
I_N
$$

回答不同問題。

 $\hat d$ 問：

> 這條 route 距離 closure 還多遠？

 $I_N$ 問：

> 整個研究制度已經走過哪些區域？

因此：

$$
\boxed{
\text{distance-to-proof}
\neq
\text{coverage-of-research-space}.
}
$$

## 13.3 二者應聯合

可以建立狀態：

$$
Z_N
=
(
\hat d_N,
\mathbf C_N,
\eta_N
).
$$

這比單一 success probability 更適合長程研究管理。

---

# 14. Tree Search 文獻與「積分」觀點

## 14.1 BFS-Prover

BFS-Prover 把 formal theorem proving 明確視為大型 proof-search tree 的導航問題。

其核心工程事實是：

$$
\text{proof success}
$$

依賴：

- node expansion；
- search policy；
- preference learning；
- depth encouragement；
- compiler feedback。

這與本文一致：

> proof 不是憑空出現，而是 search regime 對 tree / graph 的取樣結果。

## 14.2 TreeThink

2026 年 TreeThink 更直接把 theorem-proving tree search 模組化，允許比較不同搜索策略。

這說明：

$$
\Sigma
$$

本身就是研究變數。

因此同一模型、同一 verifier、同一 theorem，只改：

$$
\Sigma_1\rightarrow\Sigma_2
$$

就可能得到不同 coverage。

## 14.3 AlphaProof

AlphaProof 在 Lean formal environment 中結合 reinforcement learning 與 search，最重要的方法論意義之一是：

$$
\text{verifiable environment}
$$

可以為大規模探索提供可靠回饋。

本文不把這解讀成「搜索越大就一定接近所有真理」，而是：

$$
\boxed{
\text{verification makes large search histories scientifically more usable.}
}
$$

因為一部分 branch 可以被嚴格標記為：

$$
valid / invalid.
$$

---

# 15. 從競賽證明到研究級 proof search

## 15.1 Aristotle 的混合路徑

Aristotle 將：

- Lean proof search；
- informal reasoning；
- lemma generation / formalization；
- geometry solver；

放在同一系統中。

這支持一個重要觀點：

$$
\text{Research Route}
$$

可能跨越多種 representation 與 solver。

因此 coverage 系統不能假設所有 node 都是同質 Lean state。

## 15.2 AlphaProof Nexus 與 open-problem search

2026 年 AlphaProof Nexus 對公開未解問題進行大規模正式 proof search，並使用多 subagents、Lean compiler feedback 與演化式協調。

它直接把：

$$
\text{long-horizon search}
$$

帶到 research-level problem setting。

此時「沒有證出來」的剩餘 artifacts 就更值得保存。

因為它們可能包括：

- formalized lemmas；
- failed subgoals；
- reusable constructions；
- proof search statistics；
- library dependencies。

## 15.3 FormalProofBench 與 MA-ProofBench

2026 年的 FormalProofBench、MA-ProofBench 等 benchmark 把 formal proving 推向 advanced undergraduate / graduate mathematics 與 mathematical analysis。

這些工作揭露：

$$
\text{competition success}
$$

不能直接外推成：

$$
\text{research-level coverage}.
$$

特別是在分析領域，長依賴鏈、Mathlib 熟悉度、statement formalization 與 remaining subgoal discharge 都可能成為獨立瓶頸。

所以 coverage 需要 domain-sensitive normalization。

---

# 16. Premise Retrieval 本身就是 Coverage Operator

## 16.1 知識庫不是被動背景

形式證明中，模型能不能找到合適 premise，直接影響：

$$
\Omega_R^{reach}.
$$

令 retrieval operator：

$$
\mathcal R_k(s)
=
\{p_1,\ldots,p_k\}.
$$

不同 retrieval policy：

$$
\mathcal R^{(1)}
\neq
\mathcal R^{(2)}
$$

會改變下一步可達 states。

## 16.2 LeanSearch 類系統的意義

Global premise retrieval / LeanSearch 類工作顯示，大型 Mathlib 搜索本身是 theorem proving 的核心能力。

因此：

$$
\mathcal K
$$

和：

$$
\operatorname{Access}(\mathcal K)
$$

必須分開。

知識存在，不代表 agent 可有效調用。

## 16.3 可達空間受檢索界面限制

因此：

$$
\Omega_R^{reach}
=
F(
\mathcal A,
\mathcal L,
\mathcal M,
\mathcal V,
B,
\mathcal K,
\operatorname{Access}(\mathcal K),
\Sigma
).
$$

這比單純把 $\mathcal K$ 視為「模型知道的東西」更精確。

---

# 17. Theorem Graph 與 Knowledge Graph：Coverage 的跨證明層

## 17.1 theorem dependency graph

TheoremGraph 類工作把 formal / informal mathematical objects 連成圖。

對本文而言，可把：

$$
G^{knowledge}
$$

與：

$$
G^{search}
$$

分離。

 $G^{knowledge}$ 表示已有 theorem dependency；

 $G^{search}$ 表示目前研究歷史。

## 17.2 兩張圖的交集

定義：

$$
G_N^{align}
=
G_N^{search}
\cap
G^{knowledge}.
$$

這可以觀察：

- agent 是否只在已知 theorem graph 內移動；
- 是否產生新中介節點；
- 是否重建已知結果；
- 是否開啟新的 dependency bridge。

## 17.3 新增 theorem 不等於新增知識島

一個新 theorem：

$$
T_{new}
$$

如果只是：

$$
T_{old}
$$

的弱改寫，其 graph contribution 可能很小。

反之，一個短 bridge lemma：

$$
L^\star
$$

若連接兩個長期分離 components：

$$
C_1
\leftrightarrow
C_2,
$$

其 coverage impact 可能巨大。

因此應考慮：

$$
\Delta connectivity,
$$

而不只 theorem count。

---

# 18. 自主 theorem discovery 與「搜尋本身生成知識」

## 18.1 proof search 不一定只服務單一 target

2026 年 self-supervised theorem discovery 類研究顯示，形式 proof search 可以在公理系統中產生可驗證的新 theorem。

這表示：

$$
\text{Search}(Q)
$$

可能副產生：

$$
\{T_1,T_2,\ldots,T_m\}.
$$

其中並非所有 $T_i$ 都是 $Q$ 最終 proof 的必要步驟。

## 18.2 研究積分的生成版本

因此定義：

$$
\operatorname{Gen}_N
=
\{T_i:\mathcal V(T_i)=1\}.
$$

並考察：

$$
G_N^{new}
=
|\operatorname{Gen}_N\setminus\mathcal K_0|.
$$

若能判定 theorem 不只是資料庫重複，就可能形成：

$$
\boxed{
\text{search-generated knowledge gain}.
}
$$

## 18.3 這和最終 proof 成功可分離

可能：

$$
S(Q)=0
$$

但：

$$
G_N^{new}>0.
$$

這是長程 AI 數學研究與單次 benchmark 最大差別之一。

---

# 19. NS-203：第一個長程案例的 Coverage 解讀

## 19.1 語料地位

本文使用一個內部長程 Navier--Stokes 研究 corpus 作原型案例。

在保守排除：

- README；
- CHANGELOG；
- roadmap；
- handoff；
- checkpoint；
- audit；

等非 paper-like artifacts 後，第一輪 observatory 得到：

$$
203
$$

份 NS paper-like artifacts。

注意：

$$
203
$$

不是 203 個獨立 theorem。

更不是 203 條互不等價 proof route。

## 19.2 已建立的離散圖

第一輪 extraction 得到：

$$
189
$$

條 sequence edges；

$$
390
$$

條 explicit dependency edges；

$$
258
$$

條 revisit-similarity edges。

這些數字描述的是：

$$
G_N^{search},
$$

不是 NS 數學真實證明空間。

## 19.3 局部 higher-order 訊號

語料中可觀察到：

- obstruction confluence；
- coupled confluence；
- recurrence；
- all-order route escalation；
- second-order residue；
- route feedback。

因此某些 basin 顯示：

$$
\Omega^{(0)}
\rightarrow
\Omega^{(1)}
\rightarrow
\Omega^{(2)}
$$

式的高階再採樣。

但這首先是 corpus-level classification。

不能直接變成 theorem-level 數學階數。

## 19.4 固定窗口 novelty 的重要負結果

初始 cumulative nearest-neighbor similarity 看起來像 novelty 下降。

但 cumulative estimator 有天然 bias：

$$
\max_{j<i}
\operatorname{sim}(x_i,x_j)
$$

隨歷史池增加容易上升。

改成固定窗口後，第一輪分析並未支持全 corpus 已出現顯著 global novelty collapse。

所以現在最保守結論是：

$$
\boxed{
\text{some basins show high recurrence, while global novelty remains open.}
}
$$

## 19.5 這恰好是 coverage framework 的用途

如果只有：

$$
S(NS)=0,
$$

我們只知道「沒有最終 proof」。

加入 coverage 後，可以說：

- 某些 route family 已密集採樣；
- 某些 obstruction 有高 confluence；
- 某些 representation 仍有新增資訊；
- 某些 higher-order relations 開始出現；
- global saturation 未被證成。

這是一個嚴格更豐富、但仍不越權的描述。

---

# 20. Coverage 不能回答什麼

## 20.1 不能判定命題真假

即使：

$$
\Delta I_N\rightarrow0,
$$

也不能推出：

$$
Q=\mathrm{false}.
$$

## 20.2 不能判定不可證

不能推出：

$$
\nexists\pi.
$$

因為可能只是：

$$
\pi
\notin
\Omega_R^{reach}.
$$

## 20.3 不能判定 framing 錯誤

即使所有已知 route 反覆匯流，也可能只是：

- 方法族不足；
- representation 太窄；
- intelligence 不足；
- resource bound 太小；
- proof 極長；
- 關鍵 lemma 尚不存在。

所以：

$$
\boxed{
\text{high coverage under }R
\not\Rightarrow
\text{misframed}(Q).
}
$$

## 20.4 不能把 observation denominator 當真實 denominator

若觀測到：

$$
80\%
$$

已知 route family 被採樣，最多只能說：

> 在目前 catalog 中採樣了 $80\%$。

不能說：

> 採樣了宇宙中 $80\%$ 的可能證明。

---

# 21. Relative Coverage：未知分母時真正能報什麼

## 21.1 catalog-relative coverage

假設當前建立候選 catalog：

$$
\mathcal C_t
=
\{c_1,\ldots,c_m\}.
$$

可定義：

$$
C_N^{catalog}
=
\frac{|\mathcal C_N^{sampled}|}{|\mathcal C_t|}.
$$

必須明示：

$$
\mathcal C_t
$$

是動態、可擴張 catalog。

## 21.2 window-relative coverage

對固定最近窗口：

$$
W=[N-w,N],
$$

可計算：

$$
C_W^{new}
=
\frac{\#\text{new canonical classes in }W}{w}.
$$

這其實更接近 novelty rate。

## 21.3 basin-relative coverage

如果某 basin 有有限 decomposition：

$$
B_i
=
\bigsqcup_{j=1}^{m_i}b_{ij},
$$

可計算：

$$
C_N(B_i)
=
\frac{\#\{b_{ij}\text{ audited}\}}{m_i}.
$$

這種局部 coverage 比全域百分比可信得多。

## 21.4 benchmark-relative coverage

在明確 benchmark：

$$
\mathcal B
=
\{Q_1,\ldots,Q_n\}
$$

中，coverage 可合法寫為：

$$
C^{bench}
=
\frac{\#\text{solved}}{n}.
$$

但 benchmark success 不等於研究空間 coverage。

兩者應分開。

---

# 22. Coverage Density 與過度採樣

## 22.1 density

對局部區域 $U$，定義訪問密度：

$$
d_N(U)
=
\frac{\#\text{visits to }U}{\mu_U(U)}.
$$

如果 $\mu_U$ 未知，可使用 normalized local count。

## 22.2 oversampling

當：

$$
d_N(U)\gg d_N(V)
$$

但：

$$
\Delta I_N(U)\approx0,
$$

則 $U$ 可能被過度採樣。

定義 oversampling score：

$$
O_N(U)
=
\frac{Visit_N(U)}{\epsilon+\Delta\widetilde I_N(U)}.
$$

 $O_N(U)$ 高意味：

> 花很多研究成本，但新資訊很少。

## 22.3 調度策略

因此 scheduler 可以：

$$
\Sigma_{N+1}
=
\operatorname{Reweight}(
\Sigma_N,
O_N,
\eta_N,
\mathbf C_N
).
$$

即：

- 降低過度採樣 basin；
- 提高低 coverage representation；
- 啟動 independent verification；
- 尋找新的 method family。

---

# 23. Coverage Frontier

## 23.1 定義 frontier

令已觀測區域：

$$
\Omega_N^{obs}.
$$

frontier 可定義為：

$$
\partial\Omega_N^{obs}
=
\{x\in\Omega_N^{obs}:\exists y\notin\Omega_N^{obs},\ x\rightarrow y\text{ plausible}\}.
$$

它表示：

> 已知與未知的可操作邊界。

## 23.2 frontier quality

好的 frontier node 應具有：

- 高可驗證性；
- 高分支潛力；
- 與既有 obstruction 不同；
- 低 representation redundancy；
- 足夠 domain relevance。

可定義 heuristic：

$$
F_N(x)
=
\alpha Novelty(x)
+
\beta Verify(x)
+
\gamma Branch(x)
-
\delta Redundancy(x).
$$

## 23.3 frontier 比「再寫一篇」更重要

長程 AI 研究若沒有 frontier management，就容易：

$$
\text{paper generation}
\rightarrow
\text{local repetition}.
$$

因此每輪應輸出：

$$
\boxed{
\text{current frontier set}
}
$$

而不是只輸出最新 artifact。

---

# 24. Coverage 與 Compression 的對偶

## 24.1 探索後必須壓縮

若研究歷史長度：

$$
N\rightarrow10^4,
$$

不可能每次把所有原始文本重新讀一遍。

因此需要 compression：

$$
\mathcal H_N
\rightarrow
\mathcal S_N.
$$

其中 $\mathcal S_N$ 至少保存：

- canonical claims；
- proof dependencies；
- verified lemmas；
- obstruction IDs；
- unresolved frontiers；
- representation history；
- provenance。

## 24.2 壓縮不能抹掉差異

如果：

$$
Compress(x_1)=Compress(x_2)
$$

但：

$$
x_1\not\sim x_2,
$$

則 coverage estimator 會錯誤低估研究空間。

相反，如果：

$$
x_1\sim x_2
$$

卻被保存為完全不同 nodes，則會高估 coverage。

所以：

$$
\boxed{
\text{coverage quality depends on compression fidelity.}
}
$$

## 24.3 可逆 provenance

每個 compressed node 應能回指：

$$
node\_id
\rightarrow
\{artifact\_ids\}
\rightarrow
\{source\_ranges\}.
$$

否則不能 audit。

---

# 25. 動態積分：研究空間會自己改變

## 25.1 固定 $\Omega$ 是理想化

真正研究中：

- 新 theorem 出現；
- 新 tool 加入；
- 新 representation 被發明；
- 新 benchmark 被建立；
- 舊 obstruction 被修正；
- 公理背景可能改變。

因此：

$$
\Omega_R(t)
$$

是時間依賴的。

## 25.2 moving domain integral

更一般：

$$
I(t)
=
\int_{\bar\Omega_R(t)}
c(t,\omega)d\mu_t(\omega).
$$

因此：

$$
\frac{dI}{dt}
$$

同時受到：

1. coverage 增加；
2. domain 擴張；
3. measure 重新定義；
4. equivalence relation 更新；

影響。

## 25.3 coverage 下降不一定退步

如果新 representation 讓 domain 擴張：

$$
\Omega_R(t+1)
\supset
\Omega_R(t),
$$

即使已知內容不減少，normalized coverage ratio 也可能下降。

這不代表退步。

反而可能代表：

$$
\boxed{
\text{the system discovered that the search space is larger than previously modeled.}
}
$$

這本身是重要知識。

---

# 26. Logic-Space Reynolds Transport 類比

## 26.1 類比而非物理同一

為了處理 moving domain，可借用 transport theorem 的形式類比。

若：

$$
I(t)
=
\int_{\Omega(t)}c(t,\omega)d\mu_t,
$$

概念上可拆：

$$
\frac{dI}{dt}
=
\text{internal coverage gain}
+
\text{domain-boundary motion}
+
\text{measure update}.
$$

本文不宣稱 proof space 真的是物理流體。

這只是 bookkeeping analogy。

## 26.2 三種研究增長

可寫：

$$
\Delta I
=
\Delta I_{explore}
+
\Delta I_{expand}
+
\Delta I_{reclassify}.
$$

其中：

- $\Delta I_{explore}$：探索原本已定義區域；
- $\Delta I_{expand}$：發現新區域；
- $\Delta I_{reclassify}$：改進 canonicalization / equivalence 後重估。

這三者應分開報告。

---

# 27. Saturation Detector 必須是統計程序，不是感覺

## 27.1 最低要求

要宣稱某 basin 接近 saturation，至少要看到：

$$
\Delta V_N^{uniq}\downarrow,
$$

$$
\Delta E_N^{uniq}\downarrow,
$$

$$
\Delta\mathcal O_N\downarrow,
$$

同時：

$$
Revisit_N\uparrow.
$$

最好還要：

$$
CrossMethodConfluence_N\uparrow.
$$

## 27.2 不能只用文本相似度

需要至少三組特徵：

$$
F_{text},
\quad
F_{symbol},
\quad
F_{route}.
$$

更好再加入：

$$
F_{obstruction}.
$$

## 27.3 baseline

必須和：

- random permutation；
- shuffled series order；
- synthetic duplication；
- known non-saturated corpus；

比較。

如果 estimator 對所有長 corpus 都自動顯示下降，則它不能證明 saturation。

## 27.4 regime-change test

若改變：

$$
R_1\rightarrow R_2
$$

之後 novelty 重新上升：

$$
\Delta I_N(R_2)
\gg
\Delta I_N(R_1),
$$

則舊 saturation 更可能是：

$$
\text{regime-local saturation}.
$$

---

# 28. 邏輯空間積分的最小實驗協議

## 28.1 輸入

研究系統至少需要：

```text
problem_id
formal_or_informal_statement
axiom_background
representation
method_family
verification_channels
resource_budget
artifact_history
```

## 28.2 每輪輸出 schema

```text
run_id
parent_state_ids
claim_ids
assumption_ids
method_ids
representation_id
result_ids
obstruction_ids
verification_state
cost
provenance
```

## 28.3 canonicalization

每輪先做：

```text
Normalize symbols
Resolve aliases
Extract claims
Extract dependencies
Map obstruction candidates
Map method family
Compare prior canonical nodes
```

## 28.4 更新圖

$$
G_{N+1}
=
Update(G_N,e_{N+1}).
$$

## 28.5 計算相對量

至少輸出：

$$
\Delta V_N^{uniq},
$$

$$
\Delta E_N^{uniq},
$$

$$
\Delta O_N^{uniq},
$$

$$
\nu_N^{(w)},
$$

$$
\eta_N,
$$

$$
\rho_N^{revisit}.
$$

## 28.6 更新 frontier

$$
\mathcal F_{N+1}
=
Frontier(G_{N+1}).
$$

然後 scheduler 選擇下一輪：

$$
a_{N+1}
=
\Sigma(
\mathcal F_{N+1},
\mathbf C_N,
\eta_N,
O_N
).
$$

---

# 29. 可執行的 Pseudocode

```text
initialize Graph G
initialize Catalog C
initialize ObstructionRegistry O
initialize Frontier F

for run in research_runs:
    artifact = execute(run)

    parsed = extract(
        claims,
        assumptions,
        methods,
        representations,
        dependencies,
        obstructions,
        verification,
        provenance
    )

    canonical = semantic_normalize(parsed)
    matches = retrieve_equivalent_prior_nodes(canonical, G)

    if matches are high-confidence equivalent:
        update_revisit_edges(G, canonical, matches)
    else:
        add_new_nodes(G, canonical)

    add_dependency_edges(G, canonical)
    add_verification_state(G, canonical)
    update_obstruction_registry(O, canonical)

    metrics = compute(
        new_state_count,
        new_route_count,
        obstruction_gain,
        fixed_window_novelty,
        revisit_rate,
        confluence,
        verification_gain,
        marginal_research_yield
    )

    F = update_frontier(G, O, metrics)
    next_run = scheduler(F, metrics)
```

這個流程最重要的不是演算法細節，而是資料結構要求：

$$
\boxed{
\text{每一輪生成必須留下可比較、可驗證、可回指的痕跡。}
}
$$

---

# 30. Falsifiable Predictions

本文不是只提出詞彙。

它應該能產生可被反駁的觀察命題。

## 30.1 P1：固定制度下局部邊際收益可衰減

若 basin $B$ 在固定 $R$ 下長期被重複採樣，則可能觀察：

$$
E[\eta_N\mid B,R]
\downarrow.
$$

若始終沒有下降，則「局部飽和」假說受到削弱。

## 30.2 P2：制度切換可重置 novelty

若飽和主要由表示或方法限制引起，改變：

$$
R_1\rightarrow R_2
$$

後應有：

$$
E[\nu_N\mid R_2]
>
E[\nu_N\mid R_1]
$$

至少在初始窗口成立。

## 30.3 P3：真正 obstruction 應跨表述重現

若 $O$ 是結構性 obstruction，而非 wording artifact，則在語義等價表示間：

$$
L_1\sim L_2
$$

應保有某種：

$$
O(L_1)
\leftrightarrow
O(L_2).
$$

若完全消失，可能表示原 obstruction 只是 representation artifact。

## 30.4 P4：verified coverage 比 textual novelty 更穩定

真正累積的已驗證節點：

$$
C_N^{ver}
$$

應比純 textual novelty 對 prompt wording 更不敏感。

如果相反，則 canonicalization 或 verification architecture 有問題。

## 30.5 P5：高品質負結果應降低 future duplication

當 no-go registry 成熟：

$$
|\mathcal O_N|
\uparrow
$$

且 scheduler 真的使用它時，應看到：

$$
DuplicateFailedRoutes_N
\downarrow.
$$

如果沒有，代表 research memory 沒有真正進入決策閉環。

---

# 31. 三種積分不能混淆

## 31.1 探索積分

$$
I_N^{explore}
$$

表示研究到訪量。

## 31.2 驗證積分

$$
I_N^{verify}
$$

表示被足夠驗證的研究量。

## 31.3 排除積分

$$
I_N^{exclude}
$$

表示被可靠 no-go 排除的候選區域。

因此：

$$
\boxed{
I_N^{explore}
\neq
I_N^{verify}
\neq
I_N^{exclude}.
}
$$

一個成熟 observatory 應至少同時追蹤三者。

---

# 32. Coverage Conservation 不成立

## 32.1 知識不是固定體積流體

不能假設：

$$
I^{known}+I^{unknown}=1
$$

永遠有固定分母。

因為：

$$
\Omega(t)
$$

會擴張。

## 32.2 新定義可能增加未知量

當發現新的 structure：

$$
S_{new},
$$

可能同時增加：

$$
Known\uparrow
$$

與：

$$
Unknown\uparrow.
$$

這是數學研究常見現象。

因此「知道越多，未知越少」不是單調律。

## 32.3 更合理的更新

$$
K_{N+1}
=
K_N+\Delta K_N,
$$

$$
U_{N+1}
=
U_N-\Delta K_N+\Delta U_N^{new}.
$$

其中：

$$
\Delta U_N^{new}
$$

是新研究開啟的未知空間。

---

# 33. Coverage 與「越是真理越可能像廢話」的接口

## 33.1 本篇暫不證明真理—生成性反轉

後續第七篇將研究：

$$
\text{Truth / Fidelity / Generativity}
$$

是否存在非單調關係。

本篇只建立必要的測量語言。

## 33.2 極端閉合的直觀

若某局部問題被約束到：

$$
|\Omega^{surv}|
\rightarrow1,
$$

則剩餘結論可能表面非常簡單。

但是：

$$
\text{simple endpoint}
$$

不代表：

$$
\text{simple derivational history}.
$$

因此 coverage history 可以保存：

> 為什麼最後只剩這個看似「廢話」的結果。

這正是只保存最終 theorem statement 會丟失的部分。

---

# 34. Coverage 與 Productive Mis-specification 的接口

## 34.1 父問題錯誤不是本文前提

本文不假設：

$$
Q\text{ is misframed}.
$$

## 34.2 但 coverage 能觀察 descendant production

若研究 $Q$ 的過程中產生：

$$
\{T_1,T_2,\ldots,T_m\},
$$

可測：

$$
G_N(Q)
=
\#\{T_i:\text{independently reusable}\}.
$$

這和 $Q$ 最終真假可以分離。

## 34.3 後續問題

第八、九篇將問：

$$
G_N(Q)
$$

是否可能在某些定義偏差下反而增加。

本篇只提供：

$$
\boxed{
\text{generativity can be measured separately from proof success.}
}
$$

---

# 35. 研究治理：何時應繼續，何時應換空間

## 35.1 四種狀態

可建立簡化矩陣。

### A. 高 novelty、高 verification gain

$$
\nu_N\uparrow,
\quad
\Delta C_N^{ver}\uparrow.
$$

策略：

> 繼續深入。

### B. 高 novelty、低 verification gain

$$
\nu_N\uparrow,
\quad
\Delta C_N^{ver}\approx0.
$$

策略：

> 強化驗證，不要只增加生成。

### C. 低 novelty、高 verification gain

$$
\nu_N\downarrow,
\quad
\Delta C_N^{ver}>0.
$$

策略：

> 可能正在收斂與清理舊空間，不應誤判為停滯。

### D. 低 novelty、低 verification gain

$$
\nu_N\downarrow,
\quad
\Delta C_N^{ver}\approx0.
$$

策略：

> 啟動 regime audit：representation、method、retrieval、resource、problem decomposition。

## 35.2 這不是自動宣告問題錯誤

即使 D 長期成立，輸出也只能是：

$$
\boxed{
\text{Current research regime has low marginal yield.}
}
$$

不能輸出：

$$
\boxed{
Q\text{ is wrong}.
}
$$

---

# 36. Proof-Space Observatory 的最低儀表板

一個真正的研究觀測站，最低應顯示：

## 36.1 Corpus

$$
N_{artifact},
\quad
N_{canonical},
\quad
N_{verified}.
$$

## 36.2 Graph

$$
|V|,
\quad
|E|,
\quad
components,
\quad
cycles.
$$

## 36.3 Novelty

$$
\nu_N^{text},
\quad
\nu_N^{symbol},
\quad
\nu_N^{route}.
$$

## 36.4 Revisit

$$
\rho_N^{revisit}.
$$

## 36.5 Obstruction

$$
|\mathcal O_N|,
\quad
m_N(O_i),
\quad
\kappa_N(O_i).
$$

## 36.6 Verification

$$
C_N^{ver}
$$

及各級 verification breakdown。

## 36.7 Frontier

$$
|\mathcal F_N|.
$$

## 36.8 Cost

$$
\eta_N.
$$

這組儀表板比「今天又寫了幾篇 paper」更接近研究狀態。

---

# 37. 失敗模式目錄

## 37.1 Fake Coverage Inflation

大量改寫同一內容：

$$
N_{artifact}\uparrow
$$

但：

$$
N_{canonical}\approx const.
$$

## 37.2 Verification Laundering

把：

$$
\text{compiler success}
$$

冒充：

$$
\text{semantic correctness}.
$$

## 37.3 Obstruction Overgeneralization

局部 no-go：

$$
R_a\text{ fails under }H_a
$$

被錯寫成：

$$
Q\text{ impossible}.
$$

## 37.4 Basin Blindness

在 $B_1$ 飽和後一直重跑，卻沒有探索：

$$
B_2,B_3,\ldots
$$

## 37.5 Representation Lock-in

把：

$$
L_1
$$

誤認為：

$$
\text{the problem itself}.
$$

## 37.6 Unknown Denominator Fraud

在不知道 $|\Omega|$ 時仍報：

$$
93\%\text{ explored}.
$$

這在真正開放問題中通常不可接受。

## 37.7 History Erasure

只保存 final paper，不保存：

- failed routes；
- no-go assumptions；
- rejected reformulations；
- verification state。

結果未來 AI 再次重跑同一失敗。

---

# 38. 與傳統 Proof Complexity 的區別

## 38.1 Proof complexity 問什麼

傳統 proof complexity 可研究：

- proof length；
- proof system strength；
- lower bound；
- simulation between proof systems。

這些是高度嚴格的數學領域。

## 38.2 本文問什麼

本文主要問：

> 一個實際 AI research regime 如何在歷史中探索、記錄、驗證與重訪 proof-related states？

所以：

$$
\text{Logic-Space Integration}
\neq
\text{Classical Proof Complexity}.
$$

## 38.3 兩者可接合

如果某 formal domain 已知 proof complexity bound，則它可以提供：

$$
\mu
$$

或：

$$
Cost(\omega)
$$

的更嚴格結構。

但本文不假設所有研究問題都有此條件。

---

# 39. 與 Information Theory 的區別

## 39.1 不是直接把 entropy 套上去

本文使用：

$$
H(\Omega)
$$

時，只能在已定義概率或權重模型時當正式 entropy。

否則「熵」應被視為類比詞。

## 39.2 coverage measure 比 entropy 更原始

我們首先需要：

$$
\Omega,
\quad
\sim,
\quad
\mu,
\quad
c_N.
$$

然後才能討論：

$$
H.
$$

不應反過來先宣布：

> proof space entropy 下降。

卻沒有定義 sample space。

## 39.3 資訊增量的保守用法

若建立 probabilistic model：

$$
P_N(H_i),
$$

某新結果 $E$ 可定義 information gain：

$$
IG(E)
=
D_{KL}(P_{N+1}\|P_N).
$$

但這是 hypothesis-space information gain，和 coverage integral 是不同量。

---

# 40. 與 Bayesian Search 的接口

## 40.1 hypothesis weights

若候選機制：

$$
\mathcal H
=
\{H_1,\ldots,H_m\},
$$

可維持：

$$
P_N(H_i).
$$

## 40.2 coverage 和 posterior 分離

高 coverage：

$$
C_N(H_i)\uparrow
$$

只表示該 hypothesis family 被充分測試。

不表示：

$$
P_N(H_i)\uparrow.
$$

如果負證據多，反而可能：

$$
C_N(H_i)\uparrow,
\quad
P_N(H_i)\downarrow.
$$

這個分離非常重要。

## 40.3 最好的研究狀態可能是「高 coverage、低 posterior」

這代表：

> 我們非常確定這條方法族不值得繼續。

這不是浪費。

它是 routing knowledge。

---

# 41. Multi-Agent Coverage

## 41.1 多 agent 不等於多 coverage

假設：

$$
A_1,\ldots,A_m
$$

全部使用同一模型、同一 prompt、同一 retrieval、同一 temperature。

則：

$$
Coverage(A_1\cup\cdots\cup A_m)
$$

可能只比單 agent 稍高。

## 41.2 異質性

應考慮 agent diversity：

$$
D_A
=
f(
model,
prompt,
representation,
method,
retrieval,
verifier
).
$$

理想上：

$$
D_A\uparrow
$$

可增加獨立 basin 採樣機會。

但仍不保證：

$$
Truth\uparrow.
$$

## 41.3 union coverage

多 agent 聯合觀測：

$$
\Omega_N^{obs,union}
=
\bigcup_{i=1}^{m}
\Omega_{N,i}^{obs}.
$$

重疊：

$$
\Omega_{N,i}^{obs}
\cap
\Omega_{N,j}^{obs}
$$

則可用來測：

- convergence；
- reproducibility；
- redundancy。

---

# 42. Human-in-the-Loop Coverage

## 42.1 人類不只是 final judge

人類可以參與：

- 定義 basin；
- 判定 semantic equivalence；
- 確認 statement fidelity；
- 評估 method-family boundaries；
- 決定何時換 representation；
- 審計 false confluence。

## 42.2 human cost 必須記錄

如果一個系統需要巨大人工修復：

$$
C_{human}\gg0,
$$

其：

$$
\eta_N
$$

可能低於表面自動化率所暗示。

## 42.3 人類共識不是 truth oracle

即使多人同意：

$$
Consensus(Q)=1
$$

也不代表：

$$
T(Q)=1.
$$

所以 human verification 也必須記錄方法與證據，而不是只存 vote。

---

# 43. Research Memory 的兩層架構

## 43.1 Verified Fact Layer

保存：

$$
\mathcal K_N^{ver}
=
\{T_i:V(T_i)\ge\theta\}.
$$

要求：

- proof / evidence；
- provenance；
- dependencies；
- version；
- semantic statement。

## 43.2 Exploratory Memory Layer

保存：

$$
\mathcal M_N^{exp}.
$$

包括：

- failed routes；
- heuristic；
- partial proof；
- rejected idea；
- speculative bridge；
- negative experiment。

## 43.3 不可混淆

$$
\mathcal K_N^{ver}
\cap
\mathcal M_N^{exp}
$$

可以有引用關係，但 status 必須分離。

否則長期運行後最危險的事情是：

$$
\text{speculation}
\rightarrow
\text{memory}
\rightarrow
\text{recalled as fact}.
$$

---

# 44. Research Ledger：每一輪必須可追溯

## 44.1 Ledger entry

每一輪：

$$
L_i
=
(
id,
parent,
input,
transform,
output,
verify,
cost,
provenance
).
$$

## 44.2 不可靜默覆蓋

若 artifact 更新：

$$
a^{(1)}\rightarrow a^{(2)},
$$

必須保留：

$$
Diff(a^{(1)},a^{(2)}).
$$

否則 retrospective coverage analysis 不可靠。

## 44.3 Canonical source 與 rendering 分離

正式數學 source 應保存 canonical representation。

渲染畫面不是唯一來源。

這不只是出版工程問題，也直接影響：

$$
\text{semantic comparison}
$$

與：

$$
\text{route reconstruction}.
$$

---

# 45. Coverage-Aware Research Scheduler

## 45.1 傳統 scheduler

可能只最大化：

$$
P(\text{solve next}).
$$

## 45.2 coverage-aware scheduler

本文提出：

$$
Score(a)
=
\alpha P_{solve}(a)
+
\beta E[\Delta I\mid a]
+
\gamma E[\Delta C^{ver}\mid a]
-
\delta Cost(a)
-
\lambda Redundancy(a).
$$

## 45.3 這允許有意義的探索

某 action：

$$
a^\star
$$

即使短期：

$$
P_{solve}(a^\star)\approx0,
$$

但若：

$$
E[\Delta I\mid a^\star]\gg0,
$$

仍值得執行。

這就是 research 和 benchmark solving 的差異。

---

# 46. Coverage 與 Exploration--Exploitation

## 46.1 exploitation

沿已知 promising route：

$$
Exploit(B_i).
$$

## 46.2 exploration

開啟低採樣 basin：

$$
Explore(B_j).
$$

## 46.3 coverage-aware bandit 類比

可以把 basin 視為 arms：

$$
\{B_1,\ldots,B_m\}.
$$

reward 不只是 solved theorem，而可包括：

$$
r_i
=
\alpha\Delta C^{ver}
+
\beta\Delta C^{obs}
+
\gamma\Delta C^{route}
-
\delta Cost.
$$

本文不宣稱標準 bandit 理論可直接完整描述數學研究。

它只是提供 scheduler design 的可用類比。

---

# 47. Coverage 的尺度依賴

## 47.1 coarse scale

在粗粒度：

$$
\Omega^{coarse}
$$

可能只有：

- energy methods；
- compactness；
- geometric route；
- harmonic analysis。

## 47.2 fine scale

在細粒度：

$$
\Omega^{fine}
$$

可能展成成千上萬 lemma states。

## 47.3 coverage 是 resolution-relative

因此：

$$
C_N
=
C_N(\rho),
$$

其中 $\rho$ 是描述解析度。

粗尺度看：

$$
C_N(\rho_{coarse})\approx1
$$

不代表細尺度：

$$
C_N(\rho_{fine})\approx1.
$$

這將與後續 Reflexive Representation / resolution 問題產生接口。

---

# 48. Coverage 不應追求最大化到無限

## 48.1 研究不是窮舉字串

如果目標是：

$$
\max |\Omega_N^{obs}|,
$$

最容易的方法可能是生成大量低價值變體。

這沒有意義。

## 48.2 應最大化 weighted information gain

更合理：

$$
\max
\sum_{x\in\Delta\Omega_N}
w(x),
$$

其中 $w(x)$ 可依：

- verification；
- novelty；
- transferability；
- obstruction relevance；
- frontier importance；

調整。

## 48.3 最好的研究可能主動停止某 basin

如果：

$$
\eta_N(B_i)\rightarrow0,
$$

理性策略可能是：

$$
Stop(B_i).
$$

這不是證明 basin 沒有解。

只是 resource allocation decision。

---

# 49. 本文核心命題總表

## 命題一：研究量不等於 artifact 數

$$
\boxed{
N_{artifact}\not\equiv C_N.
}
$$

## 命題二：可觀測 coverage 依賴搜尋制度

$$
\boxed{
C_N=C_N(Q,R,\rho,\sim).
}
$$

## 命題三：全域積分通常不可直接觀測

$$
\boxed{
I_N
=
\int_{\bar\Omega_R}c_Nd\mu
}
$$

是理想量；真實研究常只能估局部或相對 coverage。

## 命題四：coverage 必須向量化

$$
\boxed{
\mathbf C_N
=
(C^{state},C^{route},C^{obs},C^{method},C^{repr},C^{ver}).
}
$$

## 命題五：負結果可以增加研究資訊

在明確適用域內：

$$
\boxed{
\text{proved no-go}
\Rightarrow
\text{valid survivor-space reduction}.
}
$$

## 命題六：局部飽和不推出全域飽和

$$
\boxed{
\Delta I(B_i)\rightarrow0
\not\Rightarrow
\Delta I(\Omega)\rightarrow0.
}
$$

## 命題七：低 novelty 不等於命題不可證

$$
\boxed{
\nu_N\downarrow
\not\Rightarrow
\nexists\pi.
}
$$

## 命題八：驗證具有層級與關係結構

$$
\boxed{
\text{compile success}
\not\equiv
\text{semantic fidelity}.
}
$$

## 命題九：邊際研究收益應納入成本

$$
\boxed{
\eta_N
=
\frac{\Delta\widetilde I_N}{Cost_N}.
}
$$

## 命題十：研究制度飽和只是一個制度結論

$$
\boxed{
\text{Saturation}(R)
\not\Rightarrow
\text{Verdict on mathematical reality}.
}
$$

---

# 50. 與系列後續論文的依賴關係

本文建立：

$$
\Omega,
\quad
\bar\Omega,
\quad
c_N,
\quad
I_N,
\quad
\Delta I_N,
\quad
\mathbf C_N,
\quad
\eta_N,
\quad
B_i,
\quad
\partial\Omega_N.
$$

後續：

LSI-PSD-03 將處理：

$$
\boxed{
\Omega/\sim
}
$$

的語義商空間問題。

LSI-PSD-04 將處理：

$$
\Omega^{(0)},\Omega^{(1)},\Omega^{(2)},\ldots
$$

高階採樣。

LSI-PSD-05 將處理：

$$
\boxed{
\text{local saturation / global openness}
}
$$

的盆地結構。

LSI-PSD-06 將建立 obstruction confluence 與 route equivalence。

LSI-PSD-07 至 09 才進入真理、生成性與 productive mis-specification。

LSI-PSD-10 將把本文所有防過度推論規則獨立形式化。

LSI-PSD-12 則把這些量轉成真正 Proof-Space Observatory runtime。

---

# 51. 結論：研究進度不應只問「離答案多遠」

當自動定理證明仍以單一 benchmark 為主時：

$$
\text{Solved / Unsolved}
$$

是合理的核心指標。

但在長程 AI 數學研究中，研究系統還需要知道：

$$
\boxed{
\text{What has been explored?}
}
$$

$$
\boxed{
\text{What has been verified?}
}
$$

$$
\boxed{
\text{What has been ruled out?}
}
$$

$$
\boxed{
\text{What is being revisited?}
}
$$

$$
\boxed{
\text{Where is the current frontier?}
}
$$

$$
\boxed{
\text{How much new information is each additional run producing?}
}
$$

本文將這組問題統一到：

$$
\boxed{
\textbf{Logic-Space Integration}
}
$$

框架。

最理想的形式是：

$$
I_N
=
\int_{\bar\Omega_R(Q)}
c_N(\omega)d\mu(\omega).
$$

但本文拒絕把這個漂亮公式誤用成虛假的全域百分比。

真正可操作的第一步，是建立：

$$
\boxed{
\mathbf C_N
=
(
C_N^{state},
C_N^{route},
C_N^{obs},
C_N^{method},
C_N^{repr},
C_N^{ver}
)
}
$$

以及：

$$
\boxed{
\Delta I_N,
\quad
\eta_N,
\quad
\rho_N^{revisit},
\quad
\mathcal F_N.
}
$$

這樣，一個沒有得到最終 proof 的研究系統，也不再只能回報：

> 失敗。

它可以更準確地回報：

> 我們在哪些區域投入了多少資源；哪些路線已被反覆重訪；哪些障礙已經得到可審計確認；哪些表示仍然有新增資訊；哪些 basin 的邊際研究收益已下降；哪些 frontier 尚未進入。

而這些資訊仍然必須服從本文最終的認識論限制：

$$
\boxed{
\text{Coverage is a property of an observed research regime,
not a percentage of mathematical reality.}
}
$$

這就是「邏輯空間積分」作為 AI 長程數學研究量測框架的最小成立條件。

---

# 參考文獻

1. Hubert, T. et al. **Olympiad-level formal mathematical reasoning with reinforcement learning.** *Nature* (2025). https://www.nature.com/articles/s41586-025-09833-y
2. Huang, S. et al. **Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925 (2025). https://arxiv.org/abs/2502.17925
3. Xin, R. et al. **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving.** arXiv:2502.03438 (2025). https://arxiv.org/abs/2502.03438
4. Achim, T. et al. **Aristotle: IMO-level Automated Theorem Proving.** arXiv:2510.01346 (2025). https://arxiv.org/abs/2510.01346
5. Tsoukalas, G. et al. **Advancing Mathematics Research with AI-Driven Formal Proof Search.** arXiv:2605.22763 (2026). https://arxiv.org/abs/2605.22763
6. Kim, J. et al. **Benchmarking Testing in Automated Theorem Proving.** arXiv:2604.23698 (2026). https://arxiv.org/abs/2604.23698
7. **Can Models Write Graduate Level Math Proofs That Are Formally Verifiable? FormalProofBench.** arXiv:2603.26996 (2026). https://arxiv.org/abs/2603.26996
8. Pu, L. et al. **MA-ProofBench: A Two-Tiered Evaluation of LLMs for Formal Theorem Proving in Mathematical Analysis.** arXiv:2606.13782 (2026). https://arxiv.org/abs/2606.13782
9. **TheoremGraph: Bridging Formal and Informal Mathematics.** arXiv:2606.25363 (2026). https://arxiv.org/abs/2606.25363
10. **TreeThink: A Modular Tree Search Library for Mathematical Theorem Proving.** arXiv:2607.11258 (2026). https://arxiv.org/abs/2607.11258
11. **Self-Supervised Theorem Discovery in a Formal Axiomatic System.** arXiv:2606.28747 (2026). https://arxiv.org/abs/2606.28747
12. **Global Premise Retrieval for Lean 4 Theorem Proving.** arXiv:2605.13137 (2026). https://arxiv.org/abs/2605.13137
13. Requena, B. et al. **A Minimal Agent for Automated Theorem Proving.** arXiv:2602.24273 (2026). https://arxiv.org/abs/2602.24273
14. Google DeepMind. **AI achieves silver-medal standard solving International Mathematical Olympiad problems.** 2024; methodology updated with the 2025 Nature publication. https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/

---

# 版本與非主張

## 本文主張

- 長程 AI 數學研究需要超越 solved / unsolved 的研究進度表示。
- 邏輯空間積分可作為描述研究 coverage 的理論框架。
- 真正開放問題通常不能誠實宣稱已知全域 proof-space denominator。
- coverage 應拆成 state、route、obstruction、method、representation、verification 等多個維度。
- 負結果在適用域明確、可重現、可審計時，可以增加研究資訊。
- 局部 saturation 與 global saturation 必須分離。

## 本文不主張

1. 已存在所有數學問題通用的自然測度 $\mu$ ；
2. 可直接計算 Navier--Stokes 或 P/NP 的真實 proof-space 百分比；
3. artifact 越多代表 coverage 越高；
4. AI 生成越多代表越接近真理；
5. novelty 越低代表原命題錯誤；
6. no-go 越多代表命題不可證；
7. formal verification 自動保證自然語言 statement fidelity；
8. 多 agent 自動提高真理率；
9. NS-203 已顯示 Navier--Stokes 全域證明空間飽和；
10. 本文的積分符號已構成傳統測度論意義下對所有 proof objects 的完備測度。

---

**END OF LSI-PSD-02 v2.0 Expanded Edition**
