# LSI-PSD-05 — 局部飽和與全域開放：證明空間的多盆地結構

## Local Saturation and Global Openness: A Multi-Basin Structure of Proof Space

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**論文序號：** 05  
**版本：** v2.0 Expanded Edition  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件地位：** 方法論核心論文 / Local Saturation and Basin-Dynamics Paper  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** ` $...$ ` 與 `$$...$$`

> **研究地位聲明**：本文提出「證明空間多盆地結構」作為長程 AI 數學研究的操作性模型。本文中的 basin、boundary、escape、conductance、frontier 等詞首先是 proof-space observatory 的研究語言；除非另有嚴格數學構造，不應把它們直接等同於傳統動力系統中的吸引盆、拓撲邊界、勢能井或測地結構。本文不主張目前任何有限 AI corpus 已證明 Navier--Stokes、P/NP 或其他未解問題的完整證明空間局部／全域幾何，更不主張某個局部研究盆地的飽和能推出原命題錯誤、不可證、獨立、無法判定或定義失敗。

---

## 摘要

當長程 AI 數學研究持續數百、數千乃至更多輪後，「新資訊是否變少」不再是一個單純的全域問題。研究可能在某一組表示、方法、引理依賴與障礙結構中反覆深化，呈現高度 recurrence、route confluence、higher-order resampling 與 audited yield decline；同一時間，其他表示、其他方法族、其他 premise 組合或其他局部區域仍可能持續產生大量新資訊。若把這兩種現象混在一起，便容易犯下一個關鍵錯誤：

$$
\boxed{
\text{local saturation}
\not\Rightarrow
\text{global exhaustion}.
}
$$

本文在 LSI-PSD-01 至 04 的基礎上，建立「證明空間多盆地結構」的操作性框架。固定研究問題 $Q$ 與搜尋制度 $R$，在語義 quotient 後的可觀測證明空間上建立加權圖：

$$
\mathcal G_R(Q)
=
(V_R,E_R,w_R),
$$

其中節點可為 canonical proof states、route states、obstruction states 或高階 relation states，邊則表示已驗證或已稽核的可達、依賴、轉換、重訪、匯流或再進入關係。對任意候選區域 $B\subseteq V_R$，本文以內部 recurrence、邊界流量、局部 novelty、跨界 escape rate 與 order-conditioned audited yield 定義一個**操作性 basin**。一個 basin 可以被高度探索而近似局部飽和，卻仍然只是整體可觀測研究空間中的一個低傳導、高 recurrence 區域。

本文進一步定義：

$$
\phi(B),
$$

表示 basin conductance；

$$
\rho_k(B;N,W),
$$

表示第 $k$ 階、固定時間窗內的 audited novelty yield；

$$
S_K(B),
$$

表示 $K$ 階局部飽和標記；

$$
\Gamma_{\mathrm{esc}}(B,a),
$$

表示某個 escape action $a$ 離開 basin 後帶來的新增資訊增益；

以及：

$$
\mathfrak F_R(N),
$$

表示在既有 corpus 與制度下仍具有可達性但尚未充分展開的觀測 frontier。

本文的重要限制是：**frontier 的存在可以支持「目前觀測制度仍開放」，但 frontier 的不可見不能支持「數學全域已封閉」。** 因為真正的證明空間可能超出目前表示語言、方法族、retrieval 系統、verifier、模型能力與計算預算。因此本文區分：

$$
\text{observed local saturation},
$$

$$
\text{regime-bounded global saturation},
$$

與不可從有限研究直接主張的：

$$
\text{mathematical global exhaustion}.
$$

2025--2026 年 formal theorem proving 的發展提供了工程上的相鄰證據。LeanNavigator 將 formal proof exploration 表示成 state-transition graph；LeanProgress 顯示局部 tactic 正確性不等於全局 proof progress；BFS-Prover 透過 length normalization 鼓勵更深路徑探索；FETCH 直接辨識語義重複造成的 over-exploration 與評分波動造成的 under-exploration；FormalEvolve 把固定預算下的 candidate repertoire diversity 與 cross-problem coverage uniformity 視為核心目標；LeanSearch v2 指出單一 premise 的局部檢索與完整定理所需的 global premise set 是不同問題；Goedel-Architect 以全局 blueprint refinement 避免對 dead-end strategy 的遞歸打轉；TreeThink 則顯示同一 formal environment 可以被不同 search policy、evaluator 與 tree strategy 重新探索。這些工作並不證明本文的 basin ontology，但共同顯示：**proof search 的局部深度、全局覆蓋、多樣性與可達性必須被分開測量。**

本文最後重新分析 NS-203 corpus。既有 v0.1 observatory 在保守分類下得到 203 份 NS paper-like artifacts，其中 $T_1=84$ 、 $T_2=107$ 、 $T_3=10$ 、 $T_X=2$ ；大量 recurrence、no-go 與跨系列 confluence 出現在特定研究支線，但固定窗口 novelty 測試並未支持整個 corpus 的單調全域崩塌。因此，NS-203 目前最合理的解讀不是「Navier--Stokes 證明空間被耗盡」，而是：

$$
\boxed{
\text{some proof basins show higher-order resampling while the corpus remains globally open at the observed level.}
}
$$

本文由此提出一個更一般的研究原則：長程 AI 研究的成熟標誌，不是讓同一 basin 變得越來越密，而是能辨識自己何時正在重採樣局部結構、何時需要改變 representation／premise／method family／resource regime，並把每次 basin escape 的成功或失敗保存為下一輪研究資料。

**關鍵詞：** 局部飽和、全域開放、proof basin、proof-space conductance、frontier、basin escape、route recurrence、confluence、audited novelty、global premise retrieval、proof search、AI 數學研究、Navier--Stokes corpus

---

# 1. 問題的提出：為什麼「整體新奇度」是一個危險的單一指標

## 1.1 長程研究不會均勻覆蓋證明空間

設一個研究系統在固定問題 $Q$ 上持續生成：

$$
g_1,g_2,\ldots,g_N.
$$

如果只看文本數量，最自然的直覺是：

$$
N\uparrow
\Rightarrow
\text{coverage}\uparrow.
$$

但 LSI-PSD-02 與 03 已指出，這個箭頭至少需要經過兩次修正：

第一，生成 artifact 不等於新增有效研究狀態；

第二，表面不同的 artifact 經語義 quotient 後可能落入同一個等價類。

因此真正的計量對象不是：

$$
N,
$$

而是：

$$
\left|
\Omega^{\mathrm{obs}}_R(Q)/\sim
\right|.
$$

然而，即使已經做了 quotient，仍有第三個問題：研究採樣通常不是均勻的。

LLM、retriever、verifier、prompt、既有 corpus 與研究者偏好會形成路徑依賴，使系統較容易反覆進入某些區域。

## 1.2 同一個區域可以很深，但旁邊仍然很空

考慮一個簡化圖：

```text
             B3
            /  \
           /    \
      B1=======B2
      |||       \
      |||        \
   dense core     frontier
```

假設 $B_1$ 內已經存在大量：

- lemma variants；
- proof routes；
- obstruction IDs；
- second-order revisits；
- confluence relations；
- all-order no-go candidates。

則 $B_1$ 可以非常「密」。

但這個密度不能直接推出：

$$
B_2,\ B_3
$$

也同樣被探索。

更不能推出：

$$
V_R=B_1.
$$

所以長程研究必須回答兩個不同問題：

$$
\text{How saturated is this region?}
$$

與：

$$
\text{How much of the reachable space is this region?}
$$

## 1.3 研究越成功，越容易被自己的成功困住

一個早期有效的方法族可能帶來大量成果：

$$
M_1
\rightarrow
L_1,L_2,\ldots,L_m.
$$

這會形成強烈的內部 reinforcement：

- retriever 更常抓回 $M_1$ 的相關 lemma；
- prompt 更常引用 $M_1$ 的語言；
- evaluator 更熟悉 $M_1$ 的成功模式；
- knowledge graph 的高中心度節點越來越偏向 $M_1$ ；
- 後續模型在 context 中看到更多 $M_1$ 的成功歷史。

於是：

$$
P(\text{return to }B_1)\uparrow.
$$

這個現象並不表示 $B_1$ 是錯的。

恰恰相反，它可能是因為 $B_1$ 曾經非常成功。

問題在於：

$$
\text{successful basin}
\neq
\text{complete proof space}.
$$

---

# 2. 從單一空間改成加權研究圖

## 2.1 可觀測證明空間

固定：

$$
Q=\text{研究問題},
$$

$$
R=(\mathcal A,\mathcal L,\mathcal M,\mathcal V,\mathcal B,\mathcal H),
$$

其中：

- $\mathcal A$：公理與背景理論；
- $\mathcal L$：表示與符號語言；
- $\mathcal M$：方法族；
- $\mathcal V$：驗證／稽核制度；
- $\mathcal B$：算力、時間、token、模型調用等預算；
- $\mathcal H$：已保存的研究歷史。

本文把在 $R$ 下被實際建構、保留或稽核的研究對象寫成：

$$
\Omega_R^{\mathrm{obs}}(Q).
$$

它不是所有數學上可能證明的集合。

它只是：

$$
\boxed{
\text{under regime }R,\ \text{what the research system has made observable}.
}
$$

## 2.2 語義 quotient 後的節點

依 LSI-PSD-03，先建立語義等價關係：

$$
x\sim y.
$$

例如：

- $\alpha$ -renaming；
- 純記號替換；
- 同一 lemma skeleton；
- 同一 normalized hypothesis set；
- 同一 obstruction under audited equivalence；
- 經證明可逆的 representation change。

令：

$$
V_R
=
\Omega_R^{\mathrm{obs}}(Q)/\sim.
$$

此後的 basin 分析原則上作用於 $V_R$，不是原始文本。

## 2.3 邊的型別

建立 typed edge：

$$
e=(u,\tau,v),
$$

其中：

$$
\tau
\in
\{
\text{derive},
\text{depend},
\text{rewrite},
\text{revisit},
\text{contradict},
\text{converge},
\text{generalize},
\text{specialize},
\text{transfer},
\text{escape}
\}.
$$

對每條邊給予權重：

$$
w(e)\ge0.
$$

權重可以綜合：

- formal verification；
- manual audit；
- independent replication；
- semantic-equivalence confidence；
- chronology confidence；
- citation／dependency evidence。

因此：

$$
\mathcal G_R(Q)
=
(V_R,E_R,w_R).
$$

## 2.4 不把圖本身當作本體

必須保持：

$$
\boxed{
\mathcal G_R(Q)
\neq
\Omega^{\mathrm{math}}(Q).
}
$$

圖是觀測儀器。

它和氣象雷達、粒子探測器、醫學影像一樣，只是在特定解析度下重建一個可操作結構。

若圖沒有看到某個區域，只能說：

$$
\text{not observed}.
$$

不能說：

$$
\text{does not exist}.
$$

---

# 3. 操作性 basin：什麼叫「研究被困在一個局部區域」

## 3.1 Basin 不應只靠 embedding cluster 定義

如果把相似文本聚類後直接命名為 proof basin，會立刻出現錯誤。

同一個詞：

$$
\text{criticality}
$$

可能出現在完全不同的數學機制。

反過來，真正等價的兩條路可能使用不同詞彙。

因此本文要求 basin 至少同時參考：

$$
\text{semantic similarity},
$$

$$
\text{route connectivity},
$$

$$
\text{obstruction identity},
$$

$$
\text{dependency structure}.
$$

## 3.2 操作性 basin 定義

對：

$$
B\subseteq V_R,
$$

定義內部邊總重：

$$
W_{\mathrm{in}}(B)
=
\sum_{u,v\in B}
w(u,v).
$$

跨界邊總重：

$$
W_{\mathrm{out}}(B)
=
\sum_{\substack{u\in B\\v\notin B}}
w(u,v).
$$

若：

$$
W_{\mathrm{in}}(B)
\gg
W_{\mathrm{out}}(B),
$$

而且固定時間窗中研究軌跡反覆回到 $B$，則 $B$ 是一個候選 basin。

本文把這稱為：

$$
\boxed{
\text{Operational Proof Basin}.
}
$$

## 3.3 Conductance

借用圖論中的 conductance 形式，但不把它宣稱為 proof-space 的自然測度。

定義節點 volume：

$$
\operatorname{vol}(B)
=
\sum_{u\in B}
\deg_w(u).
$$

則：

$$
\phi(B)
=
\frac{
W_{\mathrm{out}}(B)
}{
\min(
\operatorname{vol}(B),
\operatorname{vol}(V_R\setminus B)
)
}.
$$

直覺上：

$$
\phi(B)\downarrow
$$

表示 basin 內部連結強、外部通道相對少。

但低 $\phi(B)$ 仍可能有三種不同解釋：

1. 真正存在結構性分區；
2. retriever／prompt 導致的人工作業偏差；
3. corpus 尚未建立跨區邊。

因此 conductance 是診斷量，不是本體結論。

## 3.4 Recurrence density

令時間窗：

$$
I_{N,W}
=
\{N-W+1,\ldots,N\}.
$$

令：

$$
r_t(B)
=
\mathbf 1[x_t\in B].
$$

定義：

$$
R_W(B)
=
\frac{1}{W}
\sum_{t\in I_{N,W}}
r_t(B).
$$

若：

$$
R_W(B)\rightarrow1,
$$

表示近期研究高度集中於 $B$。

如果此時 novelty 又下降，才開始形成局部飽和候選。

---

# 4. 局部飽和必須是多條件，而不是「最近看起來都一樣」

## 4.1 單一 novelty 不足

定義局部 novelty：

$$
\nu(B,t).
$$

若：

$$
\nu(B,t)\downarrow,
$$

可能只是：

- 模型變弱；
- prompt 固化；
- 資源不足；
- summarization 損失；
- retriever 重複；
- quotient 太粗；
- 真正研究空間局部收斂。

所以：

$$
\nu\downarrow
$$

本身不能定義 saturation。

## 4.2 第 $k$ 階 audited yield

沿用 LSI-PSD-04，令：

$$
A_k(B;N,W)
$$

是固定窗口內進入 basin $B$ 的第 $k$ 階新 artifact 數。

令：

$$
U_k(B;N,W)
$$

是人工或形式稽核後，仍被判為新的有效等價類數。

定義：

$$
\rho_k(B;N,W)
=
\frac{
U_k(B;N,W)
}{
\max(1,A_k(B;N,W))
}.
$$

當：

$$
\rho_k(B;N,W)\rightarrow0,
$$

表示該階 artifact 增加，但有效新類別很少增加。

## 4.3 多階局部飽和

對指定 $K$：

$$
\mathbf \rho_{0:K}(B)
=
(
\rho_0(B),
\rho_1(B),
\ldots,
\rho_K(B)
).
$$

本文定義 basin $B$ 在窗口 $(N,W)$ 下的操作性 $K$ 階局部飽和標記：

$$
S_K(B;N,W)=1
$$

當且僅當至少同時滿足：

$$
\rho_k(B;N,W)<\varepsilon_k
\qquad
\forall k\le K,
$$

$$
R_W(B)>\tau_R,
$$

$$
\phi(B)<\tau_\phi,
$$

且：

$$
A_k(B;N,W)\ge m_k,
$$

以避免「根本沒採樣」被誤判成飽和。

## 4.4 低產量和飽和是不同的

如果：

$$
A_k(B;N,W)=0,
$$

則：

$$
\rho_k=0
$$

沒有任何意義。

因為這可能只是：

$$
\text{no sampling}.
$$

所以局部飽和必須要求：

$$
\text{sufficient attempt density}.
$$

這是整個方法論最重要的防偽條件之一。

---

# 5. 局部飽和非傳播原則

## 5.1 核心命題

本文提出：

$$
\boxed{
S_K(B)=1
\not\Rightarrow
S_K(V_R)=1.
}
$$

這稱為：

**局部飽和非傳播原則**
（Local Saturation Non-Propagation Principle）。

它不是深奧定理。

它是一個對研究語言的約束：只要 $B$ 不是已證明等於整個可觀測空間，就不能把局部判定提升成全域判定。

## 5.2 更強的防誤推論形式

即使：

$$
S_K(B_i)=1
$$

對多個已知 basin：

$$
B_1,\ldots,B_m
$$

全部成立，仍只能得到：

$$
\text{known-basin saturation}.
$$

不能直接推出：

$$
\text{mathematical global exhaustion}.
$$

因為仍可能有：

$$
B_{m+1}
$$

尚未被表示。

甚至可能有新的表示語言：

$$
\mathcal L'
$$

使原本不可見的區域突然出現。

## 5.3 Regime-bounded global saturation

若在固定 $R$ 下，研究系統已建立一個 audited cover：

$$
\mathcal C_R
=
\{B_1,\ldots,B_m,F\},
$$

其中 $F$ 是 frontier pool。

若：

$$
S_K(B_i)=1
$$

對所有 $i$ 成立，且：

$$
F
$$

在足夠多次有意識的 escape intervention 後仍沒有穩定新增 audited class，則可以標記：

$$
\boxed{
\operatorname{Sat}^{R,K}_{\mathrm{global,obs}}=1.
}
$$

這個量的名稱中必須保留：

$$
R
$$

與：

$$
\mathrm{obs}.
$$

因為它只代表：

> 在目前制度與觀測器下，已知可達空間呈現全域操作性飽和。

它仍不代表：

$$
\Omega^{\mathrm{math}}
$$

已耗盡。

---

# 6. 全域開放：什麼情況下可以說「還有地方沒走」

## 6.1 Frontier

令：

$$
\mathfrak F_R(N)
$$

是目前觀測到、具有某種可達證據，但尚未充分展開的節點／候選集合。

候選 frontier 可以來自：

- unresolved dependency；
- unused premise cluster；
- new representation；
- unexplored counterexample regime；
- cross-domain transfer；
- independent model proposal；
- human-supplied conjectural bridge；
- external theorem library；
- failed route 的 alternative branch。

## 6.2 Frontier 不是「未知的全部」

應明確區分：

$$
\mathfrak F_R(N)
$$

與：

$$
V_R^{\mathrm{unknown}}.
$$

前者是：

$$
\text{known unknowns}.
$$

後者甚至沒有被表示。

因此：

$$
|\mathfrak F_R(N)|=0
$$

不能推出：

$$
V_R^{\mathrm{unknown}}=\varnothing.
$$

## 6.3 觀測性開放證書

如果存在：

$$
f\in\mathfrak F_R(N)
$$

以及至少一條 auditable transition：

$$
u\in B
\longrightarrow
f,
$$

且展開 $f$ 後產生：

$$
U_k(f)>0,
$$

則可說：

$$
\boxed{
\operatorname{Open}^{R,K}_{\mathrm{obs}}(N)=1.
}
$$

即在目前 regime 下，已直接觀察到 proof-space renewal。

這是一個很強但有限的結論：

> 我們知道目前還沒飽和。

它不需要知道完整空間有多大。

---

# 7. Basin escape：研究不只是繼續走，也要知道何時換區域

## 7.1 Escape action

定義 escape action：

$$
a
\in
\mathcal A_{\mathrm{esc}}.
$$

例如：

- 換 representation；
- 換座標系；
- 換 invariant；
- 換 scale；
- 換 proof assistant；
- 換 theorem library；
- 換 premise retriever；
- 換模型；
- 換 prompt policy；
- 換 method family；
- 引入反例搜尋；
- 強制跨域 transfer；
- 暫時移除高中心度 lemma；
- 從 final theorem 倒推必要條件；
- 從失敗 obstruction 反向生成新問題。

## 7.2 Escape gain

令：

$$
\bar\rho_k^{\mathrm{in}}(B)
$$

是 basin 內近期平均 audited yield。

執行 escape action $a$ 後，在窗口 $W'$ 內得到：

$$
\bar\rho_k^{\mathrm{out}}(B,a).
$$

定義：

$$
\Gamma_{\mathrm{esc},k}(B,a)
=
\bar\rho_k^{\mathrm{out}}(B,a)
-
\bar\rho_k^{\mathrm{in}}(B).
$$

若：

$$
\Gamma_{\mathrm{esc},k}>0,
$$

則 escape 至少在第 $k$ 階提高了新增有效資訊率。

## 7.3 Escape 可以失敗，而且失敗也有資訊

若：

$$
\Gamma_{\mathrm{esc},k}\le0,
$$

不能立刻說新 representation 沒價值。

可能原因包括：

- 新 representation 尚未學會；
- verifier 不支援；
- retriever 尚未索引；
- translation loss；
- budget 太小；
- 新 basin 本身也飽和；
- 原 basin 與新 basin 其實 quotient-equivalent。

因此每次 escape 都應保存：

$$
(
a,
B_{\mathrm{src}},
B_{\mathrm{dst}},
\Delta\rho,
\Delta\nu,
\Delta\phi,
\text{failure trace}
).
$$

這些資料會形成下一階 proof-space science 的 corpus。

---

# 8. 多盆地結構：證明空間更像 cover，而不是單一區塊

## 8.1 不要求 basin 互斥

真實研究中：

$$
B_i\cap B_j
\neq
\varnothing
$$

是常態。

例如：

- compactness route；
- recurrence route；
- energy route；

可能共享：

$$
\text{critical scaling}.
$$

所以本文不要求：

$$
V_R
=
\bigsqcup_i B_i.
$$

而採用 cover：

$$
V_R
\approx
\bigcup_{i=1}^{m}B_i
\cup
\mathfrak F_R.
$$

## 8.2 Overlap 是重要資訊

對：

$$
B_i,B_j,
$$

定義 overlap：

$$
O_{ij}
=
\frac{
\operatorname{vol}(B_i\cap B_j)
}{
\operatorname{vol}(B_i\cup B_j)
}.
$$

高 overlap 可能意味：

- 方法族實際上共享同一核心；
- obstruction 是跨 basin 的；
- basin 切分太細；
- 一個 bridge lemma 形成共同通道。

## 8.3 Cross-basin traffic

定義：

$$
T_{ij}
=
\sum_{\substack{u\in B_i\\v\in B_j}}
w(u,v).
$$

形成 basin traffic matrix：

$$
\mathbf T
=
[T_{ij}].
$$

若：

$$
T_{ij}\gg0,
$$

表示兩個 basin 之間有實際研究通道。

若：

$$
T_{ij}\approx0,
$$

則需要判斷：

- 真正結構分離；
- corpus 缺邊；
- retriever 沒找到；
- 研究者根本沒試過。

## 8.4 Basin-level entropy

令近期研究在 basin 上的分布為：

$$
p_i(N,W).
$$

定義：

$$
H_B(N,W)
=
-
\sum_i
p_i\log p_i.
$$

低 entropy：

$$
H_B\downarrow
$$

表示研究高度集中。

但低 entropy 不一定壞。

若某 basin 正在產生高 audited yield：

$$
\rho_k\gg0,
$$

集中可能是合理 exploit。

只有當：

$$
H_B\downarrow
$$

與：

$$
\rho_k\downarrow
$$

長期同時成立，才更像「被困」。

---

# 9. Exploration--Exploitation 不能簡化成「多試幾條」

## 9.1 大搜尋空間中的經典困境

formal theorem proving 的 action space 很大。

在 proof state：

$$
s_t,
$$

模型可以產生大量 tactic：

$$
a_t^{(1)},a_t^{(2)},\ldots.
$$

若每個 tactic 再分支，搜尋樹快速膨脹。

因此所有 prover 都必須在：

$$
\text{exploration}
$$

與：

$$
\text{exploitation}
$$

間取捨。

## 9.2 BFS-Prover：深路徑也需要被刻意鼓勵

BFS-Prover 顯示，簡單 best-first tree search 若配合適當的 expert iteration、compiler feedback 與 length normalization，可以有效提升大型 Lean proof search。

對本文而言，重要的不是其 benchmark 排名，而是：

$$
\boxed{
\text{search policy itself changes which region becomes reachable}.
}
$$

如果一個 policy 系統性偏好短 proof，則某些需要先繞遠的 basin 會被壓低。

因此：

$$
\text{unvisited}
$$

不等於：

$$
\text{unproductive}.
$$

## 9.3 FETCH：過度探索和探索不足可以同時存在

FETCH 的分析尤其重要。

它區分：

$$
\text{over-exploration}
$$

來自大量語義等價／重複狀態；

以及：

$$
\text{under-exploration}
$$

來自 verifier score 高 variance 導致軌跡頻繁切換。

這兩者可以同時發生：

> 系統花很多算力，但既重複走舊路，又沒有把真正的新路走深。

因此「生成量巨大」不能直接當 coverage 指標。

## 9.4 FormalEvolve：固定預算下，多樣性本身是可優化量

FormalEvolve 把 autoformalization 設計成：

$$
\text{budgeted repertoire search}.
$$

它不只追求一個可編譯候選，而是維持 diverse candidate repertoire，並測量 cross-problem coverage concentration。

這為本文提供直接啟發：

$$
\boxed{
\text{proof-space observatory should track diversity distribution, not only success count}.
}
$$

---

# 10. 局部 premise 和全域 premise：另一種 basin 盲點

## 10.1 單步最相關不等於整體最必要

LeanSearch v2 提出 global premise retrieval：

> 一個研究級 theorem 往往需要一組分散在 library 各處、聯合起來才足夠的 lemma。

因此：

$$
\operatorname{TopK}(s_t)
$$

的局部 premise selection 不必等於：

$$
P^\star(Q)
$$

這個完整 proof 所需的 premise set。

## 10.2 Premise basin

如果 retriever 長期只回傳同一高相關 cluster：

$$
P_1,
$$

研究系統會形成：

$$
B_{\mathrm{premise}}(P_1).
$$

即使該 cluster 內搜尋非常深入，也可能一直缺：

$$
p^\star
\notin
P_1.
$$

這時候局部 proof search 會呈現：

- 高 recurrence；
- 高 lemma reuse；
- 高 internal connectivity；
- 長期無 closure。

但問題不一定是 proof strategy。

可能只是：

$$
\boxed{
\text{premise basin lock-in}.
}
$$

## 10.3 Global retrieval 作為 basin escape

LeanSearch v2 的 sketch--retrieve--reflect 類型流程，可被重新解讀為：

$$
B_i
\rightarrow
\text{global premise query}
\rightarrow
B_j.
$$

這不是說 LeanSearch v2 在研究 basin theory。

而是它提供一個工程案例：

> 改變 retrieval level 本身可以改變可達 proof space。

---

# 11. Blueprint、DAG 與 dead-end basin

## 11.1 Goedel-Architect 的全局視角

Goedel-Architect 不是只逐步遞歸拆 lemma。

它先建立 definitions / lemmas 的 dependency blueprint：

$$
\mathcal B_Q.
$$

若某些 lemma proof 失敗，失敗會回饋到 blueprint refinement。

這件事對 proof-space dynamics 很重要。

因為：

$$
\text{failure}
$$

不只是葉節點錯誤。

它可以改變：

$$
\text{global route architecture}.
$$

## 11.2 Dead-end strategy

若一個 route family：

$$
R_a
$$

反覆產生：

$$
O_a
$$

而 blueprint 層知道：

$$
R_a\rightarrow O_a
$$

已經多次重現，系統就不必無限在低階 tactic 層重跑。

這正是：

$$
\boxed{
\text{basin-level memory}.
}
$$

它把：

$$
\text{this tactic failed}
$$

提升成：

$$
\text{this strategy family has a known recurrent obstruction under these assumptions}.
$$

## 11.3 Basin memory 是避免計算浪費的必要條件

如果沒有 basin memory：

$$
\text{failure}_1,
\text{failure}_2,
\ldots
$$

只會變成大量局部 log。

如果有：

$$
O_{\mathrm{ID}},
$$

則可以建立：

$$
\operatorname{Avoid}(B,O_{\mathrm{ID}},\mathcal H).
$$

或：

$$
\operatorname{Escape}(B,O_{\mathrm{ID}}).
$$

這是從 theorem prover 走向 research observatory 的關鍵差異。

---

# 12. TreeThink 與「搜尋方法本身」的可交換性

## 12.1 不同 search algorithm 會看到不同空間切片

TreeThink 將：

- BFS；
- beam；
- MCTS；

等 search strategy 模組化，並可搭配不同 evaluator。

這提醒我們：

$$
\Omega^{\mathrm{obs}}_R
$$

其實高度依賴：

$$
R.
$$

如果：

$$
R_1
\neq
R_2,
$$

則：

$$
\Omega^{\mathrm{obs}}_{R_1}
\neq
\Omega^{\mathrm{obs}}_{R_2}
$$

完全合理。

## 12.2 因此飽和必須帶 regime index

本文拒絕寫：

$$
\operatorname{Sat}(Q).
$$

更合理的是：

$$
\operatorname{Sat}(Q\mid R).
$$

進一步：

$$
S_K(B\mid R,N,W).
$$

只要模型、retriever、方法族或 verifier 改變：

$$
R\rightarrow R',
$$

舊的 saturation label 就必須重新評估。

---

# 13. Representation basin：換句話說，有時候你不是卡在證明，而是卡在語言

## 13.1 同一命題的 representation 不一定等難

LSI-PSD-03 已討論：

$$
x\sim y
$$

在數學語義上等價，不代表：

$$
\operatorname{Cost}_{\mathrm{search}}(x)
=
\operatorname{Cost}_{\mathrm{search}}(y).
$$

因此一個 proof basin 可能其實是 representation basin。

## 13.2 Representation lock-in

若長程 corpus 形成固定語言：

$$
\mathcal L_1,
$$

retriever、prompt、lemma naming、obstruction taxonomy 都會逐漸適應：

$$
\mathcal L_1.
$$

這會降低換到：

$$
\mathcal L_2
$$

的短期效率。

於是研究系統可能錯誤得出：

> $\mathcal L_2$ 沒用。

實際上只是：

$$
\text{switching cost}>0.
$$

## 13.3 Escape intervention 必須給新 representation 成熟時間

因此測：

$$
\Gamma_{\mathrm{esc}}
$$

時不能只看一次生成。

應設：

$$
W_{\mathrm{adapt}}>0.
$$

先允許：

- vocabulary adaptation；
- premise re-indexing；
- theorem translation；
- verifier bridge；
- agent memory migration。

然後再比較長期 yield。

---

# 14. Method basin：同一套成功方法可以把自己變成盲點

## 14.1 方法族的自我強化

設：

$$
\mathcal M_1
$$

曾經產生大量有效結果。

系統會自然提高：

$$
P(\mathcal M_1\mid Q,\mathcal H).
$$

這在貝氏意義上不是不合理。

但是如果 posterior 太快坍縮：

$$
P(\mathcal M_j)\rightarrow0
\qquad
j\neq1,
$$

則研究失去探索能力。

## 14.2 方法多樣性

定義近期 method-family distribution：

$$
p_m.
$$

方法 entropy：

$$
H_M
=
-
\sum_m
p_m\log p_m.
$$

若：

$$
H_M\downarrow
$$

且：

$$
\rho_k\downarrow,
$$

應啟動 method diversification。

若：

$$
H_M\downarrow
$$

但：

$$
\rho_k\gg0,
$$

則可能只是合理集中。

所以 entropy 不能獨立判讀。

## 14.3 Forced ablation

一個強測試是暫時禁用高中心度方法：

$$
\mathcal M_{\max}.
$$

比較：

$$
\rho_k^{(-\mathcal M_{\max})}
$$

與：

$$
\rho_k^{(\mathrm{full})}.
$$

如果禁用後 novelty 上升，說明原系統可能有 method lock-in。

如果禁用後全面崩潰，則高中心度方法可能真的承擔重要結構。

---

# 15. Resource basin：資源不足也會偽裝成局部飽和

## 15.1 固定 budget 會截斷深路徑

對一個 proof route：

$$
r,
$$

若所需成本：

$$
C(r)>\mathcal B,
$$

則在目前制度下：

$$
r
$$

永遠無法完整展開。

長期看起來會像：

$$
\text{recurrent partial progress}
\rightarrow
\text{same obstruction}.
$$

但真正原因可能只是：

$$
\boxed{
\text{budget ceiling}.
}
$$

## 15.2 Resource escalation test

令：

$$
\mathcal B_1<\mathcal B_2<\cdots.
$$

測：

$$
\rho_k(B\mid\mathcal B_j).
$$

如果：

$$
\rho_k
$$

隨 budget 增加顯著恢復，則原飽和標記應被撤回或降級。

若在大幅 resource escalation 後仍沒有變化，才增加「方法／表示瓶頸」的相對可信度。

但仍不能推出原命題錯誤。

---

# 16. Evaluator basin：評分器可能把搜尋困在自己的偏好中

## 16.1 Proof search 不只由 generator 決定

搜尋決策通常依賴：

$$
V(s),
$$

或：

$$
P(a\mid s).
$$

若 evaluator 偏好某類短、熟悉、局部可驗證的狀態，可能壓低長期高價值 route。

## 16.2 Evaluator ensemble

一個實驗方法是建立：

$$
V_1,V_2,\ldots,V_m.
$$

比較不同 evaluator 下：

$$
\mathcal G_R^{(i)}.
$$

若 basin 結構對 evaluator 高度敏感：

$$
B^{(1)}
\neq
B^{(2)},
$$

則「局部飽和」很可能有 instrument dependence。

## 16.3 Instrument dependence 不等於沒有真結構

科學觀測本來就有儀器依賴。

重點不是要求：

$$
\mathcal G_R
$$

完全客觀。

而是要求：

$$
\boxed{
\text{instrument dependence be measured and declared}.
}
$$

---

# 17. 時間、順序與研究歷史本身會塑造 basin

## 17.1 Path dependence

令研究歷史：

$$
\mathcal H_N
=
(g_1,\ldots,g_N).
$$

下一輪策略：

$$
\pi_{N+1}
=
\Pi(Q,\mathcal H_N).
$$

所以：

$$
\mathcal H_N
$$

不只是紀錄。

它是搜尋動力的一部分。

## 17.2 重排實驗

可對 corpus 做 random permutation：

$$
\sigma(\mathcal H_N).
$$

但必須注意：

> 真實研究不能真的把歷史重排。

Permutation test 只能回答統計問題，例如：

$$
\text{observed novelty trend}
$$

是否超過順序隨機化的基線。

它不能模擬「如果研究歷史真的不同，AI 會走哪裡」。

## 17.3 Forked-history experiment

更強的測試是：

從某 checkpoint：

$$
H_t
$$

建立多個 fork：

$$
H_t^{(1)},
H_t^{(2)},
\ldots,H_t^{(m)}.
$$

給不同方法政策。

比較：

$$
B^{(1)}_{t+\Delta},
\ldots,
B^{(m)}_{t+\Delta}.
$$

這能直接測：

$$
\text{basin dependence on research history}.
$$

---

# 18. NS-203：為什麼它目前更像「局部高階採樣」而不是「全域耗盡」

## 18.1 Corpus accounting

NS Proof-Space Sampling Observatory v0.1 對整包遞迴掃描後得到：

$$
1109
$$

個 file instances，

其中：

$$
593
$$

個 Markdown instances，

去除 exact duplicate 後：

$$
565
$$

個 unique Markdown artifacts。

保守排除：

- README；
- CHANGELOG；
- SOURCE_POLICY；
- checkpoint；
- roadmap；
- handoff；
- audit；

後，得到：

$$
\boxed{
203
}
$$

份 NS paper-like artifacts。

## 18.2 高階採樣 tier

v0.1 的操作性 tier 分布為：

$$
T_1=84,
$$

$$
T_2=107,
$$

$$
T_3=10,
$$

$$
T_X=2.
$$

這顯示 corpus 已存在大量：

$$
\text{route revisit}.
$$

而少數支線進入：

$$
\text{confluence / higher-order family analysis}.
$$

## 18.3 但全域 novelty collapse 沒有被建立

累積 nearest-neighbor novelty 從早期下降到後期，看似支持飽和。

但累積比較池會隨時間變大，因此有 size bias。

固定窗口：

$$
W=20
$$

後，得到：

$$
\bar\nu_{\mathrm{Q2}}=0.5425,
$$

$$
\bar\nu_{\mathrm{Q4}}=0.5781.
$$

不是後期更低。

500 次 permutation baseline 得：

$$
z\approx1.01.
$$

因此 v0.1 沒有支持：

$$
\boxed{
\text{whole-corpus monotone novelty collapse}.
}
$$

## 18.4 這反而正好支持本文的問題設定

如果 corpus 裡：

- 某些 X72 round 出現 obstruction confluence；
- 某些 DCRP 路線進入 second-order / higher-order residue；
- C5-H 出現 all-order escalation；
- 多個 series 反覆命中 carrier-supplier、rigidity-closure、obstruction-gap-defect；

同時整體固定窗 novelty 沒崩塌，

那最自然的候選模型正是：

$$
\boxed{
\text{localized basin saturation + globally open observed corpus}.
}
$$

## 18.5 不能從 NS-203 推出什麼

不能推出：

$$
\text{Navier--Stokes is misframed}.
$$

不能推出：

$$
\text{Navier--Stokes is unprovable}.
$$

不能推出：

$$
\text{the Clay problem is badly defined}.
$$

不能推出：

$$
\text{AI has exhausted known mathematics}.
$$

目前只可以說：

> 在這個特定 AI 長程研究 corpus 中，某些方法／概念／障礙區域顯示高 recurrence 與高階再採樣，而整個 corpus 尚未顯示穩健的全域 novelty collapse。

這是 observational claim。

---

# 19. 從 concept family 到 basin：第二版 observatory 應如何升級

## 19.1 v0.1 的限制

目前 concept family 如：

$$
\text{carrier-supplier},
$$

$$
\text{rigidity-closure},
$$

$$
\text{obstruction-gap-defect}
$$

仍然是 routing ontology。

它們不能直接當 basin。

因為同一 broad family 可能包含多個不等價的 theorem state。

## 19.2 Canonical obstruction ID

第二版應建立：

```text
OBSTRUCTION_ID
ASSUMPTIONS
DOMAIN
NORMALIZED_STATEMENT
TERMINAL_STATUS
PROOF_DEPENDENCIES
COUNTEREXAMPLE_STATUS
AUDIT_LEVEL
```

若兩個 artifact 只有在：

$$
\text{normalized assumptions}
$$

與：

$$
\text{terminal obstruction}
$$

都被確認等價後，才允許合併。

## 19.3 Basin graph

建立：

$$
G_O
=
(V_O,E_O),
$$

其中：

$$
V_O
=
\{\text{audited obstruction / route states}\}.
$$

再以：

- recurrence；
- shared dependencies；
- transfer；
- confluence；

建立 basin。

這會比 title embedding 強得多。

---

# 20. 一個可重現的 Basin Detection Protocol

## 20.1 Step A：建立 canonical node

對每個 artifact 抽取：

$$
x_i
=
(
A_i,
C_i,
L_i,
O_i,
S_i
),
$$

其中：

- $A_i$：assumptions；
- $C_i$：claims；
- $L_i$：lemma dependency；
- $O_i$：obstruction；
- $S_i$：status。

## 20.2 Step B：先 quotient，再聚類

建立：

$$
x_i\sim x_j.
$$

只在 audited equivalence 後合併。

避免：

$$
\text{cluster first}
\rightarrow
\text{assume equivalence later}.
$$

## 20.3 Step C：建立 typed graph

邊至少分：

$$
E_{\mathrm{derive}},
E_{\mathrm{revisit}},
E_{\mathrm{depend}},
E_{\mathrm{converge}},
E_{\mathrm{escape}}.
$$

不要把所有關係壓成單一 similarity edge。

## 20.4 Step D：候選 basin

使用多種 community / conductance 方法產生候選：

$$
B_1,\ldots,B_m.
$$

但 algorithm 只負責：

$$
\text{candidate generation}.
$$

最終 basin label 仍需 structural audit。

## 20.5 Step E：計算多階 yield

對每個 basin：

$$
\rho_0,\rho_1,\ldots,\rho_K.
$$

再配：

$$
R_W,\phi,H_B,H_M.
$$

## 20.6 Step F：主動 escape

如果：

$$
S_K(B)=1,
$$

則至少觸發數個不同類型 escape：

$$
a_1,\ldots,a_m.
$$

例如：

- representation switch；
- premise-globalization；
- method ablation；
- resource escalation；
- model-family change。

## 20.7 Step G：再判定

只有當多種 escape 都沒有帶來：

$$
\Gamma_{\mathrm{esc}}>0
$$

時，才把 saturation confidence 上調。

仍然不能上調成：

$$
\text{unprovability confidence}=1.
$$

---

# 21. Saturation Confidence：把「看起來飽和」變成分級證據

## 21.1 分數

定義：

$$
C_{\mathrm{sat}}(B)
=
f(
\rho,
R_W,
\phi,
D_{\mathrm{audit}},
E_{\mathrm{attempt}},
E_{\mathrm{escape}},
R_{\mathrm{robust}}
).
$$

其中：

- $D_{\mathrm{audit}}$：人工／形式稽核深度；
- $E_{\mathrm{attempt}}$：有效嘗試量；
- $E_{\mathrm{escape}}$：escape intervention 多樣性；
- $R_{\mathrm{robust}}$：對模型、retriever、順序、budget 的穩健度。

## 21.2 建議分級

### Level 0：未評估

資料不足。

### Level 1：表面 recurrence

文字／概念重複增加。

### Level 2：route recurrence

audited route 重訪。

### Level 3：multi-order recurrence

多階 novelty yield 同時下降。

### Level 4：escape-resistant local saturation

多種 escape intervention 後仍低 yield。

### Level 5：regime-bounded global observational saturation

固定 $R$ 的已知 basin cover 全部高度飽和，frontier expansion 反覆失敗。

即使 Level 5，也不叫：

$$
\text{mathematical exhaustion}.
$$

---

# 22. 「全域開放」也不能被浪漫化

## 22.1 新東西很多不代表研究健康

若系統不停製造：

$$
\text{new terms},
$$

$$
\text{new symbols},
$$

$$
\text{new reformulations},
$$

但：

$$
\rho_k\approx0,
$$

則「看似開放」只是語言膨脹。

因此 global openness 需要 audited novelty。

## 22.2 Frontier quality

對 frontier candidate：

$$
f
$$

定義：

$$
Q_F(f)
=
g(
\text{semantic distance},
\text{formal validity},
\text{dependency novelty},
\text{obstruction novelty},
\text{transfer potential}
).
$$

只有：

$$
Q_F(f)>\tau_F
$$

才進入高優先級 frontier。

## 22.3 Open-ended 不是無限輸出

本文不把：

$$
\text{open}
$$

等同：

$$
\text{unbounded text generation}.
$$

更合理的是：

$$
\boxed{
\text{open}
=
\text{the system can still produce audited structural renewal under intervention}.
}
$$

---

# 23. 局部飽和與「越是真理越可能像廢話」的關係

## 23.1 不在本文提前證明後續命題

後續 LSI-PSD-07 將處理：

$$
\text{truth--generativity inversion}.
$$

本文只指出一個接口。

如果 basin 在不斷加入約束後：

$$
B_0\supset B_1\supset\cdots,
$$

可能出現：

$$
H(B_t)\downarrow.
$$

極端時：

$$
|B_t|\rightarrow1.
$$

那麼最後留下的核心命題可能表面非常簡單。

## 23.2 但局部簡化不等於全域真理

若某 basin 壓縮成：

$$
x^\star,
$$

只能說：

$$
\text{within this basin and regime, the survivor structure is simple}.
$$

不能推出：

$$
x^\star
=
\text{ultimate mathematical truth}.
$$

這個區分會在後續「真理—生成性反轉」與「生產性錯置」兩篇變得非常重要。

---

# 24. 局部飽和與問題範疇錯置的關係

## 24.1 Saturation 可以觸發 framing audit

如果：

$$
S_K(B)=1
$$

且多種 escape：

$$
a_1,\ldots,a_m
$$

都失敗，

系統可以提高：

$$
\operatorname{Priority}(\text{framing audit}).
$$

## 24.2 但不能直接診斷 framing error

必須保持：

$$
\boxed{
S_K(B)
\not\Rightarrow
\operatorname{Misframed}(Q).
}
$$

因為同樣現象也可能來自：

- 問題真的極難；
- 所需新理論尚未出現；
- proof 太長；
- resource 不夠；
- verifier 不夠表達；
- intelligence 不夠；
- independence；
- 命題為假但反例未找到。

## 24.3 Framing audit 是下一步，不是結論

因此流程應是：

$$
\text{local saturation}
\rightarrow
\text{audit trigger}
\rightarrow
\text{alternative hypotheses},
$$

而不是：

$$
\text{local saturation}
\rightarrow
\text{question is wrong}.
$$

---

# 25. 多模型、多方法與獨立研究線的真正作用

## 25.1 多 AI 不只是多投票

若所有 agent 使用：

$$
\text{same prompt},
$$

$$
\text{same retrieval},
$$

$$
\text{same model family},
$$

$$
\text{same proof memory},
$$

那：

$$
n\text{ agents}
$$

可能只是在同一 basin 裡並行採樣。

## 25.2 Independent basin probes

更好的設計是：

$$
R_1,\ldots,R_m
$$

有意做差異：

- model family；
- method family；
- representation；
- premise retriever；
- proof language；
- allowed tools；
- memory subset。

比較：

$$
\mathcal G_{R_1},
\ldots,
\mathcal G_{R_m}.
$$

## 25.3 交集和差集都重要

若多個 regime 都命中：

$$
O^\star,
$$

則：

$$
O^\star
$$

的 obstruction robustness 上升。

若：

$$
B^{(1)}
$$

只在某個 regime 出現，則可能是：

- 新發現；
- representation artifact；
- instrument artifact。

都值得研究。

---

# 26. 一個最小 Proof-Basin Observatory Schema

```yaml
problem:
  id: Q
  statement: ...
  formalization: ...
  domain: ...

regime:
  axioms: ...
  language: ...
  methods: ...
  verifier: ...
  model: ...
  retriever: ...
  budget: ...
  memory_version: ...

node:
  id: ...
  order: 0
  assumptions: ...
  claims: ...
  dependencies: ...
  obstruction_id: ...
  audit_status: ...
  equivalence_class: ...

edge:
  source: ...
  target: ...
  type: revisit
  audit_level: ...
  weight: ...

basin:
  id: ...
  members: ...
  conductance: ...
  recurrence_density: ...
  method_entropy: ...
  order_yield: ...
  saturation_level: ...

escape:
  id: ...
  source_basin: ...
  action_type: representation_switch
  destination: ...
  audited_gain: ...
  status: ...
```

這樣才可能讓：

$$
\text{basin}
$$

成為可重跑資料，而不是聊天中的比喻。

---

# 27. 對未來 AI 自主數學研究的架構含義

## 27.1 Agent 應該知道自己在哪個 basin

下一代數學 agent 不只需要：

> 下一步做什麼？

還要知道：

> 我現在是不是又回到過去研究過的 basin？

因此狀態應包含：

$$
b_t
=
\operatorname{BasinID}(s_t).
$$

## 27.2 Agent 應知道 basin 的歷史

例如：

```text
Basin B-17
attempts: 492
audited novel classes: 8
last 100 yield: 0.01
known obstructions: O-31, O-44
escape attempts:
  - representation switch: failed
  - premise globalization: positive
  - budget x4: neutral
```

這種記憶比單純：

> 以前試過。

強得多。

## 27.3 Meta-controller

可以建立：

$$
\Pi_{\mathrm{meta}}
$$

決定：

$$
\text{exploit},
\text{explore},
\text{escape},
\text{audit},
\text{stop}.
$$

輸入：

$$
(
C_{\mathrm{sat}},
\Gamma_{\mathrm{esc}},
H_B,
H_M,
\rho_k,
\mathfrak F_R
).
$$

## 27.4 Stop 也應該分層

不是只有：

$$
\text{proof found}
$$

或：

$$
\text{give up}.
$$

而是：

- stop this tactic；
- stop this route；
- stop this basin；
- stop this regime；
- pause this problem；
- request new definition；
- request stronger intelligence／resource；
- transfer descendants elsewhere。

這會大幅改善長程研究的計算效率。

---

# 28. 實驗一：Basin Escape Benchmark

## 28.1 目的

測試：

> 當局部 audited yield 下降時，主動換 basin 是否比繼續加算力更有效？

## 28.2 設計

選擇已知可解但證明路徑多樣的 theorem set。

對每題建立兩組：

### Control

$$
\text{continue same regime}.
$$

### Escape

當：

$$
C_{\mathrm{sat}}>\tau
$$

時，強制：

- representation switch；
- method switch；
- global premise retrieval；
- random restart。

## 28.3 指標

比較：

$$
P_{\mathrm{solve}},
$$

$$
\text{audited novel classes},
$$

$$
\text{tokens},
$$

$$
\text{verifier calls},
$$

$$
\text{time-to-new-basin}.
$$

## 28.4 可證偽性

如果 escape 組在多個資料集上：

$$
\Gamma_{\mathrm{esc}}\le0
$$

且成功率沒有改善，

則本文的 basin-control 工程價值會被削弱。

---

# 29. 實驗二：局部飽和假陽性測試

## 29.1 人工製造 retrieval lock

刻意限制 retriever：

$$
P_{\mathrm{retrieval}}
$$

只在一個子庫。

觀察是否產生：

$$
R_W\uparrow,
\quad
\rho\downarrow,
\quad
\phi\downarrow.
$$

## 29.2 解鎖

再恢復 global premise retrieval。

若 novelty 迅速恢復：

$$
\Gamma_{\mathrm{esc}}\gg0,
$$

則證明：

> 相同的飽和表面現象可以純粹由搜尋制度製造。

這是本文非常重要的 calibration experiment。

---

# 30. 實驗三：多模型 Basin Agreement

## 30.1 問題

不同模型是否會形成相同 basin？

## 30.2 定義

對 model $m$：

$$
\mathcal B^{(m)}
=
\{B_1^{(m)},\ldots\}.
$$

定義 basin alignment：

$$
A_{mn}
=
\operatorname{Match}(
\mathcal B^{(m)},
\mathcal B^{(n)}
).
$$

## 30.3 解讀

若：

$$
A_{mn}\approx1
$$

對不同架構模型都成立，

則 basin 更可能反映問題結構。

若：

$$
A_{mn}\approx0,
$$

則 basin 可能高度 model-specific。

兩種結果都重要。

---

# 31. 實驗四：NS-203 的第二輪 theorem-level basin audit

## 31.1 目標

把 v0.1：

$$
\text{title / concept family graph}
$$

提升成：

$$
\text{claim--lemma--obstruction graph}.
$$

## 31.2 抽樣

優先處理：

- NS-DCRP；
- NS-X72；
- NS-MORP；
- NS-FCBP；
- NS-C5；
- Proof Asset Map。

因為這些支線已有較高 recurrence 或 cross-series traffic。

## 31.3 手工 gold set

每條 route 至少抽取：

$$
50
$$

個 artifact pair。

雙重標註：

$$
\text{same basin?}
$$

$$
\text{same obstruction?}
$$

$$
\text{same proof skeleton?}
$$

$$
\text{mere lexical similarity?}
$$

## 31.4 成功條件

若自動 basin detector 對 gold set：

$$
F1>0.8
$$

並且 escape intervention 能穩定找出新 audited classes，

則可以開始談更強的 empirical proof-space dynamics。

---

# 32. Basin 與 SDPE：空間域證明包圍的局部版本

## 32.1 原始 filtration

SDPE 型思路可寫成：

$$
\Omega_{t+1}
=
\Omega_t\cap H_t.
$$

每個 audited no-go：

$$
H_t
$$

切除不可能區域。

## 32.2 多 basin filtration

本文改成：

$$
B_i^{(t+1)}
=
B_i^{(t)}
\cap
H_t.
$$

不同 theorem cut 只影響部分 basin。

甚至可能：

$$
H_t
$$

同時：

- 壓縮 $B_1$ ；
- 不影響 $B_2$ ；
- 打開 $B_3$ 的新 bridge。

因此 proof enclosure 不是單調「整塊空間縮小」的唯一圖像。

更一般的是：

$$
\boxed{
\text{local contraction + basin splitting + bridge creation + frontier renewal}.
}
$$

## 32.3 研究過程可以改變空間的有效座標

如果新 theorem 建立：

$$
B_1\sim B_2,
$$

兩 basin 可以 merge。

如果反例顯示原先同一 family 其實分成：

$$
B_{1a},B_{1b},
$$

則 basin split。

因此 observatory 本身需要版本化：

$$
\mathcal G_R^{(0)}
\rightarrow
\mathcal G_R^{(1)}
\rightarrow
\cdots.
$$

---

# 33. 失敗不是垃圾：Escape Failure Atlas

## 33.1 為什麼要保存失敗 escape

如果研究者只保留：

$$
\text{successful escape},
$$

未來系統可能反覆嘗試同一失敗跨越。

因此要建立：

$$
\mathcal E_{\mathrm{fail}}.
$$

## 33.2 Failure type

建議分類：

- translation failure；
- semantic mismatch；
- verifier incompatibility；
- no new premise；
- same obstruction recurrence；
- new obstruction；
- budget failure；
- evaluator failure；
- representation degeneration；
- proof-state explosion。

## 33.3 高階價值

若多個 basin 的 escape 都反覆落在：

$$
O^\star,
$$

則：

$$
O^\star
$$

本身可能成為高階 confluence obstruction。

也就是：

$$
\text{escape failure}
\rightarrow
\text{new proof-space relation}.
$$

---

# 34. 從「局部盆地」到「研究地圖」

## 34.1 最終 observatory 應該顯示什麼

不是一張漂亮的 force-directed graph。

而至少應同時顯示：

1. basin；
2. basin saturation level；
3. frontier；
4. known obstructions；
5. escape attempts；
6. cross-basin traffic；
7. method／representation distribution；
8. confidence；
9. unresolved ambiguity。

## 34.2 地圖上的顏色不能冒充真值

視覺上：

> 紅色 = 飽和

只應表示：

$$
C_{\mathrm{sat}}>\tau.
$$

不能表示：

> 此路徑數學上已證明不可能。

因此 UI 必須直接顯示：

```text
SATURATION TYPE:
observational / local / regime-bounded

NOT A CLAIM OF:
falsehood / unprovability / independence
```

---

# 35. 形式命題總表

## 命題 1：局部飽和非傳播

$$
\boxed{
S_K(B)
\not\Rightarrow
S_K(V_R).
}
$$

## 命題 2：觀測全域飽和非數學全域耗盡

$$
\boxed{
\operatorname{Sat}^{R,K}_{\mathrm{global,obs}}
\not\Rightarrow
\Omega^{\mathrm{math}}\text{ exhausted}.
}
$$

## 命題 3：低 novelty 非充分條件

$$
\boxed{
\nu\downarrow
\not\Rightarrow
S_K(B)=1.
}
$$

## 命題 4：低採樣不能叫飽和

$$
\boxed{
A_k\approx0
\not\Rightarrow
\rho_k\approx0\text{ means saturation}.
}
$$

## 命題 5：成功 basin 不等於完整空間

$$
\boxed{
\operatorname{Success}(B)\uparrow
\not\Rightarrow
V_R=B.
}
$$

## 命題 6：搜尋制度改變可達空間

$$
\boxed{
R_1\neq R_2
\Rightarrow
\Omega^{\mathrm{obs}}_{R_1}
\text{ may differ from }
\Omega^{\mathrm{obs}}_{R_2}.
}
$$

## 命題 7：Escape gain 是局部研究續行決策的證據

$$
\boxed{
\Gamma_{\mathrm{esc}}>0
}
$$

支持從原 basin 轉向新區域，但不保證新區域最終可閉合目標 theorem。

## 命題 8：多 basin recurrence 比單一文本重複更有診斷價值

若獨立方法／表示：

$$
B_i
$$

反覆匯流至同一 audited obstruction：

$$
O^\star,
$$

則：

$$
\operatorname{Robustness}(O^\star)\uparrow.
$$

但仍：

$$
O^\star
\not\Rightarrow
\text{unprovability}.
$$

---

# 36. 非主張總表

本文**不主張**：

1. proof space 在數學本體上天然具有唯一 basin decomposition；
2. graph conductance 是證明空間的唯一正確幾何；
3. embedding community 等於數學等價類；
4. 局部 novelty 下降就是 saturation；
5. 多階 recurrence 就代表接近真理；
6. basin escape 一定比加算力有效；
7. 多模型共識等於數學真理；
8. NS-203 已耗盡 Navier--Stokes 研究空間；
9. NS-203 證明 Clay 問題 framing 有錯；
10. P/NP 或 NS 必然不可判定；
11. regime-bounded saturation 可推出 Gödel 式獨立性；
12. 目前 AI 智能足以列舉所有重要表示；
13. frontier 為空表示沒有未知區域；
14. 新 representation 一定更好；
15. 研究地圖可以取代 theorem-level verification。

---

# 37. 與前四篇的整合

LSI-PSD-01 建立：

$$
\text{search regime}
\neq
\text{mathematical reality}.
$$

LSI-PSD-02 建立：

$$
I_N
=
\text{proof-space coverage functional}.
$$

LSI-PSD-03 要求先在：

$$
\Omega/\sim
$$

上去除表面重複。

LSI-PSD-04 再把採樣分成：

$$
\Omega^{(0)},
\Omega^{(1)},
\Omega^{(2)},
\ldots.
$$

本文進一步指出：

> 即使每個階都能計量，也不能假設整個空間均勻被採樣。

因此：

$$
I_k
$$

必須分解成 basin-conditioned quantities：

$$
I_k
=
\sum_i
I_{k,i}
+
I_{k,\mathfrak F}.
$$

更一般地，若 basin overlap：

$$
I_k
$$

需要 inclusion--exclusion 或 probabilistic cover correction。

所以真正成熟的 proof-space integration 不只是：

$$
\Delta I_k(N).
$$

而是：

$$
\boxed{
\Delta I_k(B_i,N)
}
$$

與：

$$
\boxed{
\Delta I_k(\mathfrak F,N).
}
$$

---

# 38. 一個更完整的動力圖像

研究開始時：

$$
\mathfrak F
\gg
B_i.
$$

大量區域尚未展開。

中期：

$$
B_1,B_2,\ldots
$$

逐漸形成。

某些 basin：

$$
\rho_k>0
$$

仍有高產量。

後期局部：

$$
\rho_k(B_1)\rightarrow0.
$$

若系統沒有 meta-control，就會：

$$
B_1\rightarrow B_1\rightarrow B_1.
$$

如果有：

$$
\Pi_{\mathrm{meta}},
$$

則：

$$
B_1
\xrightarrow{\mathrm{escape}}
B_j
$$

或：

$$
B_1
\rightarrow
\mathfrak F.
$$

於是長程研究不再是一條：

$$
\text{linear paper sequence},
$$

而是一個：

$$
\boxed{
\text{basin formation--saturation--escape--renewal process}.
}
$$

---

# 39. 對 AI 海戰術的修正

## 39.1 單純增加 agent 數量會遇到 basin crowding

若：

$$
n\rightarrow10^4
$$

但所有 agent 都在：

$$
B_1,
$$

那麼新增算力可能主要提高：

$$
\text{sampling density},
$$

不是：

$$
\text{coverage breadth}.
$$

## 39.2 真正需要的是 basin allocation

設：

$$
n_i
$$

為分配到 basin $B_i$ 的 agent 數。

應解：

$$
\max_{\{n_i\}}
\sum_i
\mathbb E[
U_i(n_i)
]
$$

subject to：

$$
\sum_i n_i=N.
$$

其中：

$$
U_i
$$

不是 paper count，而是 audited novelty utility。

## 39.3 自適應 allocation

若：

$$
\rho(B_i)\downarrow,
$$

則：

$$
n_i\downarrow.
$$

若：

$$
\Gamma_{\mathrm{esc}}(B_i,a)>0,
$$

則增加對新 basin 的 allocation。

這才是真正的：

$$
\boxed{
\text{proof-space resource scheduling}.
}
$$

---

# 40. 與未來第 6 篇的接口：障礙匯流

本文主要回答：

> 哪裡在局部飽和？

下一篇將集中問：

> 為什麼不同 basin／route 最後會撞上同一 obstruction？

如果：

$$
B_1\rightarrow O,
$$

$$
B_2\rightarrow O,
$$

$$
B_3\rightarrow O,
$$

則：

$$
O
$$

不再只是某條 proof 的局部失敗。

它可能是：

$$
\boxed{
\text{cross-basin confluence hub}.
}
$$

因此 LSI-PSD-06 將建立：

- obstruction canonicalization；
- weighted confluence；
- route-family convergence；
- obstruction inheritance；
- no-go region；
- escape obstruction；
- confluence graph。

這會把本文的 basin map 進一步變成 obstruction map。

---

# 41. 結論

長程 AI 數學研究最容易產生的一個錯覺是：

> 我已經研究這個問題非常久，所以我大概已經看完這個問題。

本文的核心工作就是拆掉這個推論。

在一個巨大的 proof space 中，研究可以非常深入地探索某個局部區域：

$$
B.
$$

系統可以在其中生成上百篇論文、數千個 lemma、反覆形成二階、三階與更高階 relation，甚至建立 all-order no-go family。

這只足以支持：

$$
\boxed{
\text{this basin is highly explored}.
}
$$

若 audited yield 同時長期下降，可以進一步支持：

$$
\boxed{
\text{this basin is operationally locally saturated}.
}
$$

但仍不能推出：

$$
\boxed{
\text{the proof space is globally exhausted}.
}
$$

更不能推出：

$$
\boxed{
\text{the mathematical problem is wrong}.
}
$$

因此成熟的 AI 研究系統不應只追求：

$$
\text{more generations}.
$$

也不應只追求：

$$
\text{more compute}.
$$

它必須知道：

$$
\boxed{
\text{where it has been,
where it keeps returning,
where novelty is dying,
and what has never been seriously tried}.
}
$$

真正的長程研究控制迴路應是：

$$
\boxed{
\text{sample}
\rightarrow
\text{quotient}
\rightarrow
\text{map}
\rightarrow
\text{detect basin}
\rightarrow
\text{measure local yield}
\rightarrow
\text{escape}
\rightarrow
\text{audit renewal}.
}
$$

從這個角度看，proof-space saturation 不是一個「最後宣布失敗」的詞。

它是一個路由訊號。

它告訴研究系統：

> 這裡可能已經看得夠深了；下一個問題不是再多走一百次，而是確認世界是否還有別的入口。

這也構成本文最終命題：

$$
\boxed{
\textbf{A mature proof-search system must distinguish depth within a basin from breadth across proof space.}
}
$$

以及其認識論底線：

$$
\boxed{
\textbf{Local saturation is a property of an observed research region, not a verdict on mathematical reality.}
}
$$

---

# 參考文獻

1. Yin, D., & Gao, J. (2025). **Generating Millions Of Lean Theorems With Proofs By Exploring State Transition Graphs.** arXiv:2503.04772. https://arxiv.org/abs/2503.04772

2. George, R. J., Huang, S., Song, P., & Anandkumar, A. (2025; revised 2026). **LeanProgress: Guiding Search for Neural Theorem Proving via Proof Progress Prediction.** arXiv:2502.17925. https://arxiv.org/abs/2502.17925

3. Xin, R. et al. (2025). **BFS-Prover: Scalable Best-First Tree Search for LLM-based Automatic Theorem Proving.** arXiv:2502.03438. https://arxiv.org/abs/2502.03438

4. Wang, A. et al. (2025). **Don't Get Lost in the Trees: Streamlining LLM Reasoning by Overcoming Tree Search Exploration Pitfalls.** arXiv:2502.11183. https://arxiv.org/abs/2502.11183

5. Lu, H., Wang, W., & Liu, J. (2026). **FormalEvolve: Neuro-Symbolic Evolutionary Search for Diverse and Prover-Effective Autoformalization.** arXiv:2603.19828. https://arxiv.org/abs/2603.19828

6. Gao, G. et al. (2026). **LeanSearch v2: Global Premise Retrieval for Lean 4 Theorem Proving.** arXiv:2605.13137. https://arxiv.org/abs/2605.13137

7. Chung, J.-H. et al. (2026). **Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement.** arXiv:2606.06468. https://arxiv.org/abs/2606.06468

8. Akbudak, B. S., Ulusan, Z. A., Erer, C. S., & Şahin, G. G. (2026). **TreeThink: A Modular Tree Search Library for Mathematical Reasoning with LLMs.** arXiv:2607.11258. https://arxiv.org/abs/2607.11258

9. Kung, P. N. et al. (2026). **LEAP: Supercharging LLMs for Formal Mathematics with Agentic Frameworks.** arXiv:2606.03303. https://arxiv.org/abs/2606.03303

10. Zhang, Y. et al. (2026). **LeanMarathon: Toward Reliable AI Co-Mathematicians through Long-Horizon Lean Autoformalization.** arXiv:2606.05400. https://arxiv.org/abs/2606.05400

11. Kurgan, S. et al. (2026). **TheoremGraph: Bridging Formal and Informal Mathematics.** arXiv:2606.25363. https://arxiv.org/abs/2606.25363

12. EveMissLab / Neo.K × AI collaborative analysis (2026). **NS Proof-Space Sampling Observatory v0.1.** Internal reproducible corpus analysis, 2026-08-17.

---

## 附錄 A：符號表

| 符號 | 意義 |
|---|---|
| $Q$ | 研究問題 |
| $R$ | 搜尋制度 / research regime |
| $\Omega_R^{\mathrm{obs}}(Q)$ | 在 $R$ 下實際可觀測研究空間 |
| $\Omega^{\mathrm{math}}(Q)$ | 理想化的底層數學證明空間；本文不假定可直接觀測 |
| $\mathcal G_R(Q)$ | quotient 後的加權 typed research graph |
| $B$ | 操作性 proof basin |
| $\phi(B)$ | basin conductance |
| $R_W(B)$ | 固定窗口 recurrence density |
| $A_k(B;N,W)$ | 第 $k$ 階嘗試數 |
| $U_k(B;N,W)$ | 第 $k$ 階新 audited equivalence classes |
| $\rho_k(B;N,W)$ | 第 $k$ 階 audited yield |
| $S_K(B)$ | $K$ 階局部飽和標記 |
| $\mathfrak F_R(N)$ | 觀測 frontier |
| $\Gamma_{\mathrm{esc},k}$ | 第 $k$ 階 basin escape gain |
| $H_B$ | basin allocation entropy |
| $H_M$ | method-family entropy |
| $C_{\mathrm{sat}}$ | saturation confidence |
| $\mathbf T$ | cross-basin traffic matrix |
| $O_{ij}$ | basin overlap |
| $\Pi_{\mathrm{meta}}$ | meta-level research routing controller |

---

## 附錄 B：最小實驗矩陣

| 實驗 | 控制變數 | Intervention | 主要指標 |
|---|---|---|---|
| Basin Escape | model / theorem set | representation / method switch | $\Gamma_{\mathrm{esc}}$ |
| Retrieval Lock | prover / budget | local vs global premise | $\rho_k$, success |
| Resource Escalation | method / representation | budget multipliers | $\rho_k(\mathcal B)$ |
| Model Agreement | theorem set / tools | model family | basin alignment |
| Evaluator Sensitivity | generator / corpus | evaluator | basin robustness |
| History Fork | checkpoint | different route policy | basin divergence |
| NS-203 Audit | corpus | theorem-level canonicalization | precision / recall / F1 |

---

## 附錄 C：Observatory 判定流程

```text
INPUT:
  problem Q
  regime R
  research history H

1. Normalize artifacts
2. Build semantic quotient
3. Extract typed route graph
4. Generate candidate basins
5. Audit basin membership
6. Measure:
   - recurrence
   - conductance
   - order-conditioned novelty
   - audited yield
7. If local saturation candidate:
   trigger escape interventions
8. Recompute yield
9. Store success/failure trace
10. Update basin map
11. Never convert observational saturation
    into a theorem about mathematical reality
```

---

## 附錄 D：一句話版本

$$
\boxed{
\text{在一口井裡挖到一萬公尺深，不代表你已經走遍整個地表。}
}
$$

對長程 AI 數學研究而言：

$$
\boxed{
\text{depth within a proof basin}
\neq
\text{breadth across proof space}.
}
$$
