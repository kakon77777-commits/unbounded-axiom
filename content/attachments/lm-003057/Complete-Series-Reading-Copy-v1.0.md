# 邏輯空間積分與證明空間動力學

## Logic-Space Integration and Proof-Space Dynamics

**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

## 系列定位

本系列研究長程 AI 數學研究如何從單次證明搜尋，轉化為可觀察、可去重、可積分、可路由的 proof-space dynamics。核心並不是宣稱任何未解問題已被解決，而是建立一個能保存研究軌跡、負證明資訊、障礙匯流、局部飽和與高階再採樣的研究科學框架。

全系列的認識論底線是：

$$
\boxed{
\text{Saturation is evidence about a search regime, not a verdict on mathematical reality.}
}
$$

## 十二篇

1. **LSI-PSD-01 — 證明空間不是證明：AI 長程數學研究的基本框架**  
   Proof Space Is Not Proof  
   檔案：`papers/LSI-PSD-01_證明空間不是證明_AI_長程數學研究的基本框架.md`

2. **LSI-PSD-02 — 邏輯空間積分：從單次證明搜尋到研究空間覆蓋**  
   Logic-Space Integration  
   檔案：`papers/LSI-PSD-02_邏輯空間積分_從單次證明搜尋到研究空間覆蓋.md`

3. **LSI-PSD-03 — 語義商空間：為什麼一萬篇論文不等於一萬條證明路徑**  
   Semantic Quotient Space  
   檔案：`papers/LSI-PSD-03_語義商空間_為什麼一萬篇論文不等於一萬條證明路徑.md`

4. **LSI-PSD-04 — 高階證明空間採樣：從狀態、路徑到路徑之間的關係**  
   Higher-Order Proof-Space Sampling  
   檔案：`papers/LSI-PSD-04_高階證明空間採樣_從狀態、路徑到路徑之間的關係.md`

5. **LSI-PSD-05 — 局部飽和與全域開放：證明空間的多盆地結構**  
   Local Saturation and Global Openness  
   檔案：`papers/LSI-PSD-05_局部飽和與全域開放_證明空間的多盆地結構.md`

6. **LSI-PSD-06 — 障礙匯流與研究路由：當不同方法反覆撞上同一堵牆**  
   Obstruction Confluence and Research Routing  
   檔案：`papers/LSI-PSD-06_障礙匯流與研究路由_當不同方法反覆撞上同一堵牆.md`

7. **LSI-PSD-07 — 真理—生成性反轉：為什麼更精確不一定產生更多理論**  
   Truth--Generativity Inversion  
   檔案：`papers/LSI-PSD-07_真理-生成性反轉_為什麼更精確不一定產生更多理論.md`

8. **LSI-PSD-08 — 生產性錯置：錯誤問題如何生成正確的後代理論**  
   Productive Mis-specification  
   檔案：`papers/LSI-PSD-08_生產性錯置_錯誤問題如何生成正確的後代理論.md`

9. **LSI-PSD-09 — 生產性錯置窗口：真理、錯誤與知識肥沃性的非單調曲線**  
   The Productive Mis-specification Window  
   檔案：`papers/LSI-PSD-09_生產性錯置窗口_真理、錯誤與知識肥沃性的非單調曲線.md`

10. **LSI-PSD-10 — 飽和不是判決：證明空間非結論原則**  
   Saturation Is Not a Verdict  
   檔案：`papers/LSI-PSD-10_飽和不是判決_證明空間非結論原則.md`

11. **LSI-PSD-11 — 從 Carnot 到 AI：結構性錯誤的科學史與模型論**  
   From Carnot to AI  
   檔案：`papers/LSI-PSD-11_從_Carnot_到_AI_結構性錯誤的科學史與模型論.md`

12. **LSI-PSD-12 — AI 證明空間觀測站：從 NS-203 到文明級研究記憶**  
   AI Proof-Space Observatory  
   檔案：`papers/LSI-PSD-12_AI_證明空間觀測站_從_NS-203_到文明級研究記憶.md`

## 閱讀順序

建議依編號閱讀。第 01 至 06 篇建立 proof-space measurement；第 07 至 09 篇建立 truth / generativity / mis-specification 軸；第 10 篇是全系列的認識論防火牆；第 11 篇提供科學史與模型論案例；第 12 篇把理論落成 AI Proof-Space Observatory。

## Case Study

本 release 內含 `case_study/NS_Proof_Space_Sampling_Observatory_v0.1.zip`，作為第 04、05、06、12 篇的初步 corpus instrumentation。其資料只能支持 corpus-level observation，不構成 Navier--Stokes proof。


---

# FULL SERIES

# LSI-PSD-01 — 證明空間不是證明：AI 長程數學研究的基本框架

## Proof Space Is Not Proof: A Framework for Long-Horizon AI Mathematical Research

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

大型語言模型與形式證明工具正在把數學研究從單次問答推向可持續的長程搜尋。當研究系統能連續生成數百、數千乃至更多候選論證時，新的核心問題不再只是「下一篇是否證明了目標命題」，而是「整個研究過程究竟探索了什麼、排除了什麼、反覆撞上什麼，以及哪些失敗其實是同一失敗的不同表示」。本文建立本系列的最小框架，明確區分目標命題、形式語言、證明狀態、證明路徑、研究產物、障礙類與搜尋制度。本文提出「證明空間非同一原則」：被觀察到的搜尋空間不等於數學上所有可能證明的集合；因此，任何有限或可計算的 AI 研究紀錄都不能僅由搜尋失敗推出命題為假、原問題定義錯誤、不可證或不可判定。另一方面，長程研究紀錄仍具有正面價值：它可以形成可審計的負證明資訊、路徑匯流資訊與表示敏感性資訊，並成為研究制度本身的經驗資料。

本文的目的不是把數學研究降格成搜尋，而是將「搜尋制度」本身提升為可研究對象。這使我們能同時維持兩個立場：一方面拒絕「AI 證不出來所以問題有錯」的過度結論；另一方面拒絕把數百次有結構的失敗當成零資訊。

**關鍵詞：** 證明空間、長程 AI 研究、搜尋制度、負證明資訊、形式證明、表示敏感性、認識論防火牆

---

## 1. 問題的改變：從一次答案到研究軌跡

傳統自動定理證明通常可被描述為：給定目標 $Q$，在某個形式系統中尋找一個可被檢查器接受的證明物件 $\pi$。最簡化地寫成：

$$
\operatorname{Find}\ \pi
\quad\text{such that}\quad
\mathcal V(\pi,Q)=1,
$$

其中 $\mathcal V$ 是驗證器。

當 AI 系統只能做短程推理時，這個描述已經足夠。但當系統能夠：

- 生成新的中間引理；
- 切換表示；
- 搜尋文獻；
- 執行程式與數值實驗；
- 建立反例候選；
- 記錄失敗；
- 在之後的研究輪次重新使用舊結果；

研究對象便不再只有最終證明 $\pi$，而是整個軌跡：

$$
\mathcal H_N
=
(a_1,a_2,\ldots,a_N),
$$

其中每個 $a_i$ 都可能是一個證明步、候選引理、反例、程式實驗、表示變換、失敗診斷或研究決策。

2026 年的形式數學研究已清楚顯示這種轉變。HERMES 類系統把非形式推理與 Lean 驗證交錯；Stepwise 把證明視為 proof-state tree search；TheoremGraph 則把形式與非形式數學整理成圖結構。這些工作共同提示：研究軌跡本身已經開始成為第一級資料，而不只是通往答案的暫時副產品。

---

## 2. 五個必須分開的對象

為避免把「研究過程」和「數學實在」混為一談，本文定義五個層次。

### 2.1 目標命題

$$
Q.
$$

$Q$ 是欲證、欲反證或欲分類的命題。

### 2.2 背景制度

$$
R
=
(\mathcal A,\mathcal L,\mathcal M,B,\mathcal K).
$$

其中：

- $\mathcal A$：公理、邏輯與背景理論；
- $\mathcal L$：可使用的表示與符號語言；
- $\mathcal M$：方法族與可調用工具；
- $B$：時間、算力、上下文、證明長度等資源界；
- $\mathcal K$：研究開始前已知的知識、文獻與形式庫。

本文把 $R$ 稱為 **search regime**，即搜尋制度。

### 2.3 可觀察證明狀態空間

$$
\Omega_R(Q).
$$

這不是「所有可能證明」的宇宙，而是制度 $R$ 能表示、生成、到達或區分的研究狀態集合。

### 2.4 研究產物

第 $i$ 個產物寫成：

$$
g_i=(s_i,p_i,r_i,e_i),
$$

其中 $s_i$ 是表示，$p_i$ 是推導或研究路徑，$r_i$ 是結果狀態，$e_i$ 是驗證與證據。

### 2.5 數學上的證明性結論

真正可改變命題地位的，是例如：

$$
\mathcal A\vdash Q,
$$

$$
\mathcal A\vdash \neg Q,
$$

或某個明確的獨立性結果：

$$
\mathcal A\nvdash Q
\quad\text{and}\quad
\mathcal A\nvdash\neg Q.
$$

這一層不能由前四層的統計現象自動取代。

---

## 3. 證明空間非同一原則

本文提出本系列第一個基本原則。

### 原則 1：證明空間非同一原則

$$
\boxed{
\Omega_R(Q)
\neq
\Omega_{\mathrm{all}}(Q)
}
$$

一般而言，被某個研究制度觀察到的搜尋空間不等於所有可能表示、所有可能公理擴充、所有未來方法與所有可能智能可觸及的證明空間。

因此：

$$
\operatorname{FailSearch}(Q\mid R)
\not\Rightarrow
\neg Q,
$$

$$
\operatorname{FailSearch}(Q\mid R)
\not\Rightarrow
\operatorname{Misframed}(Q),
$$

$$
\operatorname{FailSearch}(Q\mid R)
\not\Rightarrow
\operatorname{Independent}(Q).
$$

這不是保守修辭，而是邏輯上的必要區分。真正的不可證或獨立性需要元數學證明；單純未找到證明，只能描述搜尋制度的結果。

Goedel 型不可完備性尤其提醒我們：「不可證」不是「找得不夠久」的同義詞，而是相對明確形式系統的形式性敘述。反過來說，大量失敗也不能被廉價地包裝成 Goedel 式不可判定。

---

## 4. 失敗為什麼仍然不是零資訊

拒絕過度結論，不代表所有失敗都相同。

假設每次研究都留下：

$$
F_i
=
(\text{assumptions},
\text{route},
\text{failed step},
\text{obstruction},
\text{verification}).
$$

若不同路徑反覆導向同一個可驗證障礙 $O$：

$$
T_1(Q)\leadsto O,
$$

$$
T_2(Q)\leadsto O,
$$

$$
T_3(Q)\leadsto O,
$$

那麼我們至少得到一個關於制度 $R$ 的事實：

$$
P(O\mid T_1,T_2,T_3,R)
$$

具有高重現性。

這種資料可以用來：

1. 排除已知失敗模板；
2. 找出 proof-route confluence；
3. 發現表示變換是否只是改名；
4. 建立新的中間問題；
5. 判斷下一輪應改變方法、表示、資源還是問題表述。

因此本文把這類資料稱為：

$$
\boxed{
\text{negative proof information}.
}
$$

它不是「反證」，而是「關於搜尋制度中哪些路徑已被審計」的負資訊。

---

## 5. 表示敏感性使搜尋失敗更難解讀

2026 年 Olejniczak 等人的研究顯示，當形式命題經過語義保持的改寫後，先進 LLM theorem prover 的成功率仍可能大幅改變。這說明：

$$
Q_1\equiv Q_2
$$

在數學內容上等價，卻可能有：

$$
P(\operatorname{prove}Q_1\mid R)
\neq
P(\operatorname{prove}Q_2\mid R).
$$

所以 AI 搜尋的失敗不只是「方法不夠強」，也可能是表示空間沒有被適當 quotient。這直接支持本系列後續的語義商空間與表示對稱性研究。

它也提供一個重要警告：如果同一個數學命題可以因表面表示而呈現不同 proof success，則任何「搜尋已耗盡」主張都必須先回答：

$$
\text{是否真的耗盡了語義類，還是只耗盡了一組表面寫法？}
$$

---

## 6. 長程 AI 數學研究的最小資料結構

本文建議每個長程研究產物至少保存：

```text
artifact_id
target_claim
assumptions
representation
dependencies
new_lemmas
proof_route
obstruction
verification_status
counterexample_status
formalization_status
revisit_of
supersedes
transfer_targets
```

這不是行政紀錄，而是之後進行 proof-space science 的必要資料。

如果只保存「第 218 篇論文」，我們無法知道它是否真的增加新邏輯狀態。若保存上列結構，才能建立：

$$
\text{artifact graph}
\longrightarrow
\text{route graph}
\longrightarrow
\text{obstruction graph}.
$$

---

## 7. 與 Navier--Stokes 及 P vs NP 的關係

Navier--Stokes existence and smoothness 與 P vs NP 目前仍是 Clay Mathematics Institute 列出的未解 Millennium Prize Problems。本文不對其真值、可證性或 framing 做結論。

它們在本系列中的角色只是高難度案例：

$$
\boxed{
\text{hard open problem}
\Rightarrow
\text{useful stress test for research-space instrumentation}.
}
$$

即使未來某個 AI corpus 在其中呈現強烈 recurrence、confluence 或 local saturation，也只能先得到：

$$
\text{current regime saturated in some regions}.
$$

不能直接得到：

$$
\text{the problem is wrong}.
$$

---

## 8. 本系列的核心研究轉向

本系列不再只問：

$$
\text{Can AI prove }Q?
$$

而增加第二個問題：

$$
\boxed{
\text{What structure does AI reveal about its own search regime while trying?}
}
$$

這個轉向使「沒有證明」不再等於「沒有研究成果」，同時也阻止研究者把「很多成果」誤寫成「已經證明」。

---

## 9. 符號表

| 符號 | 意義 |
|---|---|
| $Q$ | 目標命題 |
| $R$ | 搜尋制度 |
| $\mathcal A$ | 公理與背景理論 |
| $\mathcal L$ | 表示語言 |
| $\mathcal M$ | 方法族 |
| $B$ | 資源界 |
| $\mathcal K$ | 已有知識 |
| $\Omega_R(Q)$ | 制度 $R$ 下可觀察研究空間 |
| $g_i$ | 第 $i$ 個研究產物 |
| $\mathcal V$ | 驗證器 |
| $O$ | 障礙或 obstruction |

---

## 10. 依賴與後續

**前置依賴：** 無，本篇為系列 Charter。  

**後續直接依賴：**

- LSI-PSD-02：邏輯空間積分；
- LSI-PSD-03：語義商空間；
- LSI-PSD-04：高階證明空間採樣；
- LSI-PSD-10：飽和不是判決。

---

## 結論

長程 AI 數學研究真正新增的，不只是更多文字，而是可被保存、比較、重放與驗證的研究軌跡。當研究規模變大，最危險的兩種錯誤恰好相反：一種把所有失敗都視為零資訊；另一種把大量失敗誤解成對數學實在的終局判決。

本文建立的底線是：

$$
\boxed{
\text{Proof-space observations are evidence about a search regime, not proof about all mathematics.}
}
$$

在這條底線之上，proof-space coverage、局部飽和、高階採樣與生產性錯置才有資格成為可研究的對象。

---

## 參考文獻

1. Krzysztof Olejniczak, Radoslav Dimitrov, Xingyue Huang, Bernardo Cuenca Grau, Jinwoo Kim, Ismail Ilkan Ceylan. *What are the Right Symmetries for Formal Theorem Proving?* arXiv:2605.22257, 2026.
2. S. Kurgan et al. *TheoremGraph: Bridging Formal and Informal Mathematics*. arXiv:2606.25363, 2026.
3. HERMES authors. *HERMES: Towards Efficient and Verifiable Mathematical Reasoning*. arXiv:2511.18760, revised 2026.
4. Baoding He et al. *Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification*. arXiv:2603.19715, 2026.
5. Stanford Encyclopedia of Philosophy. *Goedel's Incompleteness Theorems*. Current online archive consulted 2026-08-17.
6. Clay Mathematics Institute. *Navier--Stokes Equation: Existence and Smoothness*. Official Millennium Prize Problem page and Charles L. Fefferman problem description, accessed 2026-08-17. https://www.claymath.org/millennium/navier-stokes-equation/
7. Clay Mathematics Institute. *P vs NP*. Official Millennium Prize Problem page, accessed 2026-08-17. https://www.claymath.org/millennium/p-vs-np/


---

# LSI-PSD-02 — 邏輯空間積分：從單次證明搜尋到研究空間覆蓋

## Logic-Space Integration: From Single-Proof Search to Research-Space Coverage

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

若 AI 能在同一數學問題上持續生成、驗證、排除與重組研究路徑，單純用「生成篇數」衡量進展會快速失效。本文提出「邏輯空間積分」作為研究空間覆蓋的操作性框架。核心思想是：不把每篇文本當成一個獨立點，而先建立語義與路徑等價類，再衡量某個搜尋制度對這些類的覆蓋、重訪、排除與未決狀態。本文定義局部覆蓋函數、累積積分、邊際增量與負資訊積分，並強調這些量都必須相對於明確的 domain、representation、method family 與 resource budget 才有意義。本文同時證明一個方法論上的非等價：生成量增加不必然推出覆蓋量增加；覆蓋量增加也不必然推出更接近目標證明。邏輯空間積分因此不是「證明機率」的替代，而是一個研究觀測層。

**關鍵詞：** 邏輯空間積分、覆蓋度、邊際新穎度、負資訊、研究空間、proof-space observatory

---

## 1. 為什麼篇數不是尺度

設 AI 已經生成 $N$ 個研究產物：

$$
G_N=\{g_1,\ldots,g_N\}.
$$

最直覺的進度指標是 $N$。但這個指標有三個立即問題。

第一，兩篇文字不同的論文可能只是在重新命名同一個 lemma。  
第二，一篇短文可能真正開出新的 proof route，而十篇長文可能只是在同一 obstruction 附近重寫。  
第三，負結果、反例與 no-go 也可能大幅縮小有效搜尋區域，即使沒有產生任何「正向定理」。

因此我們需要一個不以文本數量為核心的尺度。

---

## 2. 從 raw artifacts 到有效狀態

先定義研究產物空間：

$$
\mathcal G_R(Q).
$$

再定義等價關係 $\sim$。若兩個產物在目標、必要假設、主要推理骨架與結論狀態上等價，只存在可逆或語義保持的表面改寫，則視為同一有效研究類：

$$
[g]
=
\{h\in\mathcal G_R(Q):h\sim g\}.
$$

有效空間因此不是 $\mathcal G_R(Q)$ 本身，而是：

$$
\widetilde\Omega_R(Q)
=
\mathcal G_R(Q)/\sim.
$$

本系列第三篇將專門討論 $\sim$ 的設計；本篇先假定它已由可審計程序給出。

---

## 3. 局部覆蓋函數

對每個有效狀態 $x\in\widetilde\Omega_R(Q)$，定義：

$$
c_N(x)\in[0,1].
$$

$c_N(x)$ 不是「真值」，而是第 $N$ 輪研究後該狀態被探索與審計的程度。

可以把它分解為：

$$
c_N(x)
=
w_g g_N(x)
+
w_v v_N(x)
+
w_r r_N(x)
+
w_f f_N(x),
$$

其中：

- $g_N(x)$：是否生成過；
- $v_N(x)$：是否被獨立驗證；
- $r_N(x)$：是否被不同路徑重訪；
- $f_N(x)$：是否有明確失敗或排除證書；
- 權重滿足 $w_g+w_v+w_r+w_f=1$。

重要的是，$c_N$ 衡量的是 epistemic handling，而不是 mathematical truth。

---

## 4. 邏輯空間積分

給定一個研究區域 $A\subseteq\widetilde\Omega_R(Q)$ 與測度 $\mu_R$，定義：

$$
I_N(A)
=
\int_A c_N(x)\,d\mu_R(x).
$$

這就是本文所稱的邏輯空間積分。

若 $A$ 是離散的有限商空間，可簡化為：

$$
I_N(A)
=
\sum_{x\in A}
c_N(x)\mu_R(x).
$$

最值得觀察的不是絕對值，而是邊際增量：

$$
\Delta I_N(A)
=
I_{N+1}(A)-I_N(A).
$$

如果持續增加生成量，而：

$$
\Delta I_N(A)\to0,
$$

則代表該區域的邊際覆蓋正在下降。

但這只支持：

$$
\text{local effective saturation in }A,
$$

不支持全域耗盡。

---

## 5. 測度不能偷偷假定均勻

$\mu_R$ 是整個框架最容易被濫用的地方。

如果把所有 syntactic strings 等權處理，則無限多無意義改寫會讓空間失去可解釋性。若把所有 theorem-like documents 等權處理，長文本又會被錯當成高資訊。

因此本文要求 $\mu_R$ 至少滿足：

### 5.1 表示不變性要求

對語義保持變換 $\tau$：

$$
x\sim\tau(x)
\Rightarrow
\mu_R([x])=\mu_R([\tau(x)]).
$$

### 5.2 審計可解釋要求

權重來源必須可追溯，例如：

- 新假設數；
- 新 obstruction family；
- 新 proof dependency；
- 形式驗證狀態；
- 跨系列可遷移性。

### 5.3 任務條件化要求

不存在一個天然適用所有問題的唯一 $\mu$。應寫成：

$$
\mu_{R,Q,\tau},
$$

其中 $\tau$ 表示當前研究任務，例如「找證明」「找反例」「找可遷移 lemma」或「找表示錯置」。

---

## 6. 正資訊積分與負資訊積分

傳統研究評價偏向正結果：

$$
I_N^+.
$$

但對高難度問題，負資訊同樣重要。定義：

$$
I_N^-
=
\int_{\widetilde\Omega_R(Q)}
f_N(x)\,d\mu_R(x),
$$

其中 $f_N(x)$ 表示被審計排除、證明不可由特定假設閉合、或已確認落入既知 no-go family 的程度。

因此總研究處理量可寫成：

$$
I_N^{\mathrm{handled}}
=
I_N^+ + \lambda I_N^-,
$$

其中 $\lambda$ 不是「負結果折價」，而是依任務決定的權重。

這一設計使「失敗」可以被保存，但不會被誤認成反證。

---

## 7. 生成量與覆蓋量的非等價

定義生成量：

$$
N.
$$

定義有效類數：

$$
K_N
=
\left|
\{[g_1],\ldots,[g_N]\}
\right|.
$$

若大量生成只重訪既有類：

$$
N\to\infty
\quad\text{while}\quad
K_N=O(1),
$$

則：

$$
\frac{K_N}{N}\to0.
$$

這就是「文字仍增加，但有效邏輯新狀態幾乎不增加」。

反之，也可能一篇新研究產生一個高中心性的中間 lemma，使大量舊路徑被重新連接。這時 $N$ 只增加 $1$，但圖結構資訊可能劇烈增加。

因此：

$$
\boxed{
\Delta N
\not\propto
\Delta I_N.
}
$$

---

## 8. 覆蓋增加也不等於更接近證明

假設目標證明位於未知區域 $P^\star$。一個研究制度可能高效率地覆蓋與 $P^\star$ 無關的區域：

$$
I_N(A)\uparrow,
\qquad
P^\star\notin A.
$$

因此：

$$
I_N\uparrow
\not\Rightarrow
P(\text{proof found})\uparrow.
$$

這是邏輯空間積分的第二個重要限制。它測量「研究了多少被定義的空間」，不是「距離真理還有幾公尺」。

---

## 9. 實務估計：不要求先知道整個空間

有人可能反駁：若不知道 $\widetilde\Omega_R(Q)$，怎麼積分？

答案是使用逐步估計，而不是宣稱已知母空間。

可建立可觀察子空間：

$$
\widetilde\Omega_N
=
\bigcup_{i\le N}[g_i]
$$

與局部鄰域邊界 $\partial\widetilde\Omega_N$。研究指標只針對：

$$
A_N
\subseteq
\widetilde\Omega_N
\cup
\partial\widetilde\Omega_N.
$$

這和科學中用有限樣本估計未知分佈類似，但本文不假定 IID，也不把 proof states 當成自然概率樣本。

---

## 10. 與現代 theorem proving 的接口

現代 proof agents 已普遍使用：

- proof states；
- tactic transitions；
- library retrieval；
- search trees；
- decomposition；
- verification feedback。

這些正好提供實作 $c_N$ 的原始資料。TheoremGraph 類工作則表明 theorem dependency graph 與 informal citation graph 可以被對齊；Semantic Search over 9 Million Mathematical Theorems 顯示大規模 theorem-level retrieval 已經具有工程可行性。

因此邏輯空間積分不要求發明一種完全不同的 theorem prover，而是在既有 proof infrastructure 上增加一層 observability。

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $\mathcal G_R(Q)$ | 原始研究產物空間 |
| $\sim$ | 有效等價關係 |
| $\widetilde\Omega_R(Q)$ | 商後有效研究空間 |
| $c_N(x)$ | 第 $N$ 輪覆蓋函數 |
| $\mu_R$ | 任務條件化測度 |
| $I_N(A)$ | 區域 $A$ 的邏輯空間積分 |
| $\Delta I_N$ | 邊際積分增量 |
| $I_N^+$ | 正資訊積分 |
| $I_N^-$ | 負資訊積分 |
| $K_N$ | 已觀察有效類數 |

---

## 12. 依賴與可檢驗預測

**依賴：** LSI-PSD-01。  

本文給出三個可檢驗預測：

1. 在長程 corpus 中，$N$ 與 $K_N$ 會逐漸脫鉤；
2. 某些局部 basin 的 $\Delta I_N(A)$ 會先下降，而全域 novelty 不必同步下降；
3. 經過 semantic quotient 後，表面重複率與結構重複率會顯著不同。

---

## 結論

邏輯空間積分不是宣稱數學可被一個有限 measure 完整包住，而是把長程研究的「覆蓋、重訪、排除、匯流」轉成可審計量。

其最小形式是：

$$
\boxed{
I_N(A)
=
\int_A c_N(x)\,d\mu_R(x).
}
$$

真正重要的是：

$$
\boxed{
\Delta I_N(A)
}
$$

如何隨研究持續而改變。當它下降，我們得到的是一個關於研究區域與搜尋制度的訊號，而不是對數學真值的判決。

---

## 參考文獻

1. S. Kurgan et al. *TheoremGraph: Bridging Formal and Informal Mathematics*. arXiv:2606.25363, 2026.
2. Authors. *Semantic Search over 9 Million Mathematical Theorems*. arXiv:2602.05216, 2026.
3. Authors. *A Minimal Agent for Automated Theorem Proving*. arXiv:2602.24273, 2026.
4. Baoding He et al. *Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification*. arXiv:2603.19715, 2026.
5. Krzysztof Olejniczak, Radoslav Dimitrov, Xingyue Huang, Bernardo Cuenca Grau, Jinwoo Kim, Ismail Ilkan Ceylan. *What are the Right Symmetries for Formal Theorem Proving?* arXiv:2605.22257, 2026.


---

# LSI-PSD-03 — 語義商空間：為什麼一萬篇論文不等於一萬條證明路徑

## Semantic Quotient Space: Why Ten Thousand Papers Do Not Equal Ten Thousand Proof Routes

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

AI 大規模生成數學文本後，最先出現的統計陷阱是把文本差異誤認成數學差異。相同定理可以改變變數名、引理順序、參數化、座標系、形式庫與 tactic surface；不同文本也可能共享同一 proof skeleton。反過來，兩個字面極相似的敘述也可能因假設、量詞、domain 或 library semantics 不同而不是同一命題。本文提出語義商空間作為 proof-space measurement 的必要前置層。本文將等價判定分成表示等價、命題等價、路徑骨架等價與障礙等價四層，並提出「不可過早商化原則」：在尚未保留依賴、假設、量詞與驗證證據前，不應僅依 embedding 或詞彙相似度把研究產物合併。2026 年形式 theorem proving 的表示敏感性研究顯示，語義等價敘述仍可造成大幅 proof-success 差異，這使「表示」同時具有兩種身份：它在數學上可能是冗餘，在演算法上卻可能是因果變數。本文因此主張使用雙層商空間：數學語義 quotient 與搜尋制度 quotient 必須分開。

**關鍵詞：** 語義商空間、等價類、representation sensitivity、proof skeleton、形式化、embedding、symmetry

---

## 1. 重複不是一個單一概念

考慮兩個表面不同的敘述：

$$
a+b=b+a
$$

與：

$$
x+y=y+x.
$$

對適當型別與假設而言，它們可能只是變數重命名。

但在真正研究 corpus 中，「重複」可能至少有四種：

1. 字符重複；
2. 語義等價；
3. 證明路徑骨架等價；
4. 最終障礙等價。

若沒有區分，任何 saturation 統計都可能被表面文字污染。

---

## 2. 四層等價關係

令研究產物為 $g_i$。

### 2.1 表示等價

$$
g_i\sim_{\mathrm{repr}}g_j
$$

若差異僅由變數改名、可逆符號變換、段落排序或不改變語義的格式操作造成。

### 2.2 命題等價

$$
g_i\sim_{\mathrm{prop}}g_j
$$

若它們的核心命題在背景理論 $\mathcal A$ 中互相推出：

$$
\mathcal A\vdash Q_i\leftrightarrow Q_j.
$$

### 2.3 路徑骨架等價

$$
g_i\sim_{\mathrm{route}}g_j
$$

若兩者雖使用不同 notation 或局部 lemma，但依賴圖在去除低階差異後同構或近似同構。

可以用圖表示：

$$
\Gamma_i=(V_i,E_i),
\qquad
\Gamma_j=(V_j,E_j).
$$

若存在保留關鍵角色的映射 $\phi$，使主要 assumption、bridge lemma、closure step 和 obstruction 對應，則可把它們視為同 route family。

### 2.4 障礙等價

$$
g_i\sim_{\mathrm{obs}}g_j
$$

若不同路徑最後失敗於同一個可形式化 obstruction family。

這層是後續 confluence analysis 的核心。

---

## 3. 一個商空間不夠

最自然的做法是：

$$
\Omega/\sim.
$$

但 2026 年的 theorem-proving representation research 顯示，這可能過度簡化。Olejniczak 等人展示：語義保持的 rewrite 仍可讓 LLM prover 的成功率顯著變動。

因此同一語義類中：

$$
Q_i\sim_{\mathrm{prop}}Q_j
$$

仍可能有：

$$
P(\operatorname{success}\mid Q_i,R)
\neq
P(\operatorname{success}\mid Q_j,R).
$$

這表示 representation 在「數學內容」層可能應該被 quotient，在「搜尋動力」層卻不能被 quotient。

本文因此定義雙層結構。

### 數學語義商空間

$$
\Omega^{\mathrm{math}}
=
\Omega/\sim_{\mathrm{prop}}.
$$

### 搜尋制度狀態空間

$$
\Omega^{\mathrm{search}}
=
\{(Q,\rho):\rho\in\operatorname{Rep}(Q)\}.
$$

其中 $\rho$ 是命題 $Q$ 的具體表示。

這樣我們可以同時問：

$$
\text{這是不是同一個數學命題？}
$$

以及：

$$
\text{這兩種表示對 AI 搜尋是不是同一個狀態？}
$$

答案不必相同。

---

## 4. 不可過早商化原則

本文提出：

$$
\boxed{
\text{Never quotient away information before preserving the evidence needed to reconstruct it.}
}
$$

中文稱為「不可過早商化原則」。

如果 corpus 只有一個 embedding vector，而沒有：

- 原始命題；
- 量詞；
- domain；
- assumptions；
- theorem dependencies；
- formal proof status；
- counterexample status；

那麼兩篇論文被 cluster 到一起時，我們無法判斷是：

$$
\text{semantic equivalence}
$$

還是：

$$
\text{semantic collision}.
$$

因此商化必須可逆到足以進行 audit 的表示層。

---

## 5. 自然語言 embedding 只能是候選生成器

2026 年 theorem semantic search 已經可以在數百萬級 theorem statement 上工作；TheoremGraph 也使用自然語言 slogan 與 embedding 連接 informal/formal nodes。這對大規模 corpus 很重要，但 embedding 的角色應該是：

$$
\text{candidate generation},
$$

不是：

$$
\text{equivalence proof}.
$$

本文建議流程：

```text
raw artifacts
    |
    v
cheap lexical / embedding retrieval
    |
    v
candidate pair set
    |
    v
assumption + quantifier comparison
    |
    v
dependency-graph comparison
    |
    v
formal mutual implication when possible
    |
    v
audited equivalence class
```

若形式化可行，可參考 mutual provability 類指標；若不可形式化，則保留 uncertain edge，而不是強行合併。

---

## 6. 語義不變量與 proof-search 對稱

如果某個 rewrite $\tau$ 真正保持數學內容：

$$
Q\sim_{\mathrm{prop}}\tau(Q),
$$

那麼理想 prover 應至少追求某種 success invariance：

$$
P(\operatorname{success}\mid Q)
\approx
P(\operatorname{success}\mid\tau(Q)).
$$

現實系統做不到，反而提供一種研究工具：我們可以用同一命題的等價 rewrite 當作 probe，測量搜尋制度的 representation bias。

定義：

$$
\operatorname{RSI}(Q)
=
\operatorname{Var}_{\rho\in\operatorname{Rep}(Q)}
P(\operatorname{success}\mid Q,\rho,R).
$$

稱為 Representation Sensitivity Index。

若 $\operatorname{RSI}(Q)$ 很高，則任何「此命題在目前制度下很難」的結論都必須加上表示條件。

---

## 7. 路徑 quotient 比文本 quotient 更重要

長程研究真正需要壓縮的是 proof route。

設第 $i$ 篇論文抽取：

$$
\Gamma_i
=
(A_i,L_i,B_i,O_i),
$$

其中：

- $A_i$：assumption nodes；
- $L_i$：lemma nodes；
- $B_i$：bridge / closure nodes；
- $O_i$：obstruction nodes。

兩篇文本即使 cosine similarity 很低，也可能具有：

$$
\Gamma_i\simeq\Gamma_j.
$$

若只用文本相似度，這種結構性重訪會被漏掉。

因此 proof-space saturation 的可靠版本必須逐步從：

$$
\text{text similarity}
$$

升級到：

$$
\text{claim-dependency-obstruction similarity}.
$$

---

## 8. 商空間與新穎度

定義 raw novelty：

$$
\nu_i^{\mathrm{raw}}
=
1-\max_{j<i}\operatorname{sim}_{\mathrm{text}}(g_i,g_j).
$$

定義 quotient novelty：

$$
\nu_i^{\mathrm{quot}}
=
\mathbf 1
\left(
[g_i]\notin
\{[g_1],\ldots,[g_{i-1}]\}
\right).
$$

兩者可能完全不同。

最值得研究的是：

$$
\nu_i^{\mathrm{raw}}>0
\quad\text{but}\quad
\nu_i^{\mathrm{quot}}=0.
$$

這就是表面新穎、結構重訪。

反過來：

$$
\nu_i^{\mathrm{raw}}\approx0
\quad\text{but}\quad
\nu_i^{\mathrm{quot}}=1
$$

則表示一個小修改真正改變了假設、量詞或 closure condition。

---

## 9. 符號表

| 符號 | 意義 |
|---|---|
| $\sim_{\mathrm{repr}}$ | 表示等價 |
| $\sim_{\mathrm{prop}}$ | 命題等價 |
| $\sim_{\mathrm{route}}$ | 路徑骨架等價 |
| $\sim_{\mathrm{obs}}$ | 障礙等價 |
| $\Omega^{\mathrm{math}}$ | 數學語義商空間 |
| $\Omega^{\mathrm{search}}$ | 保留表示的搜尋空間 |
| $\Gamma_i$ | 第 $i$ 個 proof-route graph |
| $\operatorname{RSI}$ | 表示敏感性指標 |
| $\nu^{\mathrm{raw}}$ | 原始文本新穎度 |
| $\nu^{\mathrm{quot}}$ | 商空間新穎度 |

---

## 10. 依賴與後續

**依賴：** LSI-PSD-01、LSI-PSD-02。  

**後續：** LSI-PSD-04、05、06、12。

---

## 結論

大規模 AI 數學研究的第一個瓶頸不是生成，而是去除「假的新穎性」同時不刪掉「真的表示效應」。

因此本篇的核心不是一句「把重複去掉」，而是雙重要求：

$$
\boxed{
\text{Quotient mathematical redundancy, preserve search-relevant representation.}
}
$$

只有做到這一點，後續的高階採樣、局部飽和與 proof-space integration 才有可靠的最小單位。

---

## 參考文獻

1. Krzysztof Olejniczak, Radoslav Dimitrov, Xingyue Huang, Bernardo Cuenca Grau, Jinwoo Kim, Ismail Ilkan Ceylan. *What are the Right Symmetries for Formal Theorem Proving?* arXiv:2605.22257, 2026.
2. X. Liu et al. *ASSESS: A Semantic and Structural Evaluation Framework for Autoformalization*. arXiv:2509.22246, 2025.
3. S. Kurgan et al. *TheoremGraph: Bridging Formal and Informal Mathematics*. arXiv:2606.25363, 2026.
4. Authors. *Semantic Search over 9 Million Mathematical Theorems*. arXiv:2602.05216, 2026.
5. Authors. *From Solvers to Research: Large Language Model-Driven Mathematical Discovery*. arXiv:2607.07779, 2026.


---

# LSI-PSD-04 — 高階證明空間採樣：從狀態、路徑到路徑之間的關係

## Higher-Order Proof-Space Sampling: From States to Routes to Relations Among Routes

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

當同一問題被長時間研究，研究對象可能發生階層轉移：最初採樣的是候選證明狀態；之後採樣的是狀態之間的轉換路徑；再之後研究的是不同路徑為何匯流、哪些 obstruction family 彼此等價、哪些高階重訪只是既有結構的再包裝。本文把這個現象形式化為高階證明空間採樣。為避免集合論上的含糊，本文不把第 $k+1$ 階簡單定義成第 $k$ 階的 power set，而使用 typed research layers：狀態層、轉換層、關係層與 meta-relation 層。本文提出 sampling-order registry、order-specific novelty 與 order-specific saturation。核心假說是：長程研究可能先出現低階 novelty 衰減，而高階 novelty 仍保持正值；因此「開始重複」不一定代表研究已失效，而可能代表研究對象從 proof state 轉移到 proof-process geometry。

**關鍵詞：** 高階採樣、proof trajectory、meta-reasoning、confluence、order-specific novelty、研究階數

---

## 1. 一階研究與高階研究不是篇數差異

設最基礎的研究狀態集合為：

$$
\Omega^{(0)}.
$$

其中的元素可能是：

- 某個中間命題；
- 某個 candidate estimate；
- 某個 regularity criterion；
- 某個 counterexample candidate；
- 某個 proof state。

如果 AI 只是在 $\Omega^{(0)}$ 中找新的元素，這是狀態採樣。

但當研究開始問：

> 從這個狀態到那個狀態有哪些方法？

研究對象變成 transition。

---

## 2. Typed research layers

本文定義：

### 第零層：狀態層

$$
\mathcal S_0
=
\Omega^{(0)}.
$$

### 第一層：轉換層

$$
\mathcal S_1
=
\{T:x\mapsto y\mid x,y\in\mathcal S_0\}.
$$

$T$ 可以是 rescaling、compactness、energy estimate、contradiction route、formal tactic sequence 等。

### 第二層：關係層

$$
\mathcal S_2
=
\{R(T_i,T_j,\ldots)\}.
$$

例如：

- 兩條路徑是否等價；
- 是否匯流到同一 obstruction；
- 是否共享同一 hidden assumption；
- 是否可相互轉換；
- 是否在某個 quotient 後相同。

### 第三層以上：meta-relation 層

$$
\mathcal S_{k+1}
=
\mathcal R_k(\mathcal S_k),
$$

其中 $\mathcal R_k$ 是明確指定的關係生成器，而不是無限制 power set。

這樣可以避免一句含糊的：

$$
\Omega^{(k+1)}=\mathcal F(\Omega^{(k)})
$$

把所有可能關係混在一起。

---

## 3. 什麼才算二階、三階或 X 階證據

本文拒絕用字面詞彙直接判定研究階數。

例如正文出現：

$$
\text{second-order derivative}
$$

並不代表二階 proof-space sampling。

真正的二階證據應該包含：

1. 明確引用多條既有路徑；
2. 研究對象是 route relation，而不是原始 PDE quantity；
3. 產出的是 route equivalence、route incompatibility、shared obstruction 或 confluence statement；
4. 能在 dependency graph 上被重建。

類似地，三階證據要求研究對象已經是：

$$
R_1,R_2,\ldots
$$

之間的結構。

因此「X 階」在本系列中不是神秘階數，而是：

$$
\boxed{
\text{auditable meta-level above the currently enumerated route-relation layers}.
}
$$

---

## 4. Order-specific novelty

對第 $k$ 階研究產物，定義：

$$
\nu_k(n)
=
\frac{
\#\text{new audited classes at order }k
}{
\#\text{artifacts classified at order }k
}.
$$

若出現：

$$
\nu_0(n)\to0,
$$

而：

$$
\nu_1(n),\nu_2(n)>0,
$$

代表低階狀態發現趨於飽和，但方法關係與高階結構仍有新資訊。

這是一個非常重要的區別。它使我們可以把：

$$
\text{repetition}
$$

分成兩種：

### 無結構退化

$$
\nu_0\to0,
\quad
\nu_1\to0,
\quad
\nu_2\to0,
$$

且沒有新的可驗證關係。

### 高階轉移

$$
\nu_0\to0,
\quad
\nu_1\approx0,
\quad
\nu_2>0.
$$

後者不是「AI 只會重複」，而是研究對象本身上移。

---

## 5. Proof trajectory 作為二階資料

現代 theorem proving 已大量把 proof state 與 tactic transition 當作基本訓練或搜尋單位。Stepwise 類框架明確在 proof state tree 中進行 best-first search；segment-level learning 也開始把 proof trajectory 的局部連續結構當作訓練單位。

這提供一個自然接口：

$$
s_0
\xrightarrow{T_1}
s_1
\xrightarrow{T_2}
\cdots
\xrightarrow{T_m}
s_m.
$$

傳統 prover 關心 $s_m$ 是否 closed。高階 proof-space science 還會問：

- 哪些 trajectory prefix 反覆出現？
- 哪些 transition family 永遠導向 dead state？
- 哪些 route 在不同 representation 下同構？
- 哪些 subgoal decomposition 是真正新結構？

---

## 6. Confluence 是高階採樣的第一個可見訊號

設三條路徑：

$$
T_a,\quad T_b,\quad T_c.
$$

若：

$$
T_a(Q)\leadsto O,
$$

$$
T_b(Q)\leadsto O,
$$

$$
T_c(Q)\leadsto O,
$$

新的研究問題不再只是「如何突破 $O$」，而是：

$$
\boxed{
\text{Why do distinct routes converge to }O?
}
$$

這個問題本身屬於 $\mathcal S_2$。

如果之後又發現不同 confluence families：

$$
C_1,C_2,C_3
$$

其實共享某個更高階 defect：

$$
C_1,C_2,C_3\leadsto D,
$$

則進入更高 meta-level。

---

## 7. X 階採樣與 all-order 語言

在研究實務中，有些 corpus 會出現「all-order」、「higher-order」、「closure family」等語言。但本文要求把它們分為：

$$
\text{mathematical order}
$$

與：

$$
\text{research-order}.
$$

只有當文本同時具備：

- 對既有 route families 的顯式回顧；
- 對 family-level recurrence 的分析；
- 對多階 route pattern 的壓縮；
- 可重建的 dependency evidence；

才可暫時標成 $T_X$。

所以：

$$
T_X
$$

是一個研究分類標籤，不是一個已證明的無限階定理。

---

## 8. 高階採樣可能先於證明，也可能永遠不導向證明

高階資訊具有價值，但不能過度解讀。

可能出現：

$$
\mathcal S_0
\to
\mathcal S_1
\to
\mathcal S_2
\to
\cdots
$$

持續產生漂亮結構，卻仍沒有：

$$
\mathcal A\vdash Q.
$$

原因可能是：

- 真正 proof route 不在目前表示域；
- 高階結構只描述 failure geometry；
- 問題需要外部新理論；
- 搜尋制度仍有 blind spot；
- 目標命題可能為假；
- 或只是尚未到達關鍵 route。

因此高階採樣是一種 observability gain，不是 proof guarantee。

---

## 9. 與 NS-203 corpus 的操作性連結

EveMissLab 的 NS Proof-Space Sampling Observatory v0.1 對 203 份保守分類的 NS paper-like artifacts 建立了初步 route graph。第一版 heuristic 得到：

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

這些數字只代表 corpus classifier 的估計，不代表真正數學階數。其價值在於提出下一個可驗證任務：

$$
\boxed{
\text{把 paper-level tier 降解成 claim-lemma-obstruction-level tier。}
}
$$

只有完成這一步，才能判斷局部高階採樣究竟是研究結構，還是文本組織風格。

---

## 10. 符號表

| 符號 | 意義 |
|---|---|
| $\mathcal S_0$ | 狀態層 |
| $\mathcal S_1$ | 轉換層 |
| $\mathcal S_2$ | 路徑關係層 |
| $\mathcal S_k$ | 第 $k$ 階研究層 |
| $T$ | proof transition / research move |
| $R$ | route relation |
| $O$ | obstruction |
| $\nu_k$ | 第 $k$ 階新穎度 |
| $T_1,T_2,T_3,T_X$ | corpus 估計採樣層級標籤 |

---

## 11. 依賴與後續

**依賴：** LSI-PSD-01 至 03。  

**後續：** LSI-PSD-05、06、12。

---

## 結論

當研究進入長程狀態，真正值得觀察的不是「還有沒有新文章」，而是：

$$
\boxed{
\text{the order at which novelty still survives}.
}
$$

低階 novelty 消失而高階 novelty 出現，代表研究可能從「找新點」轉向「理解點之間的幾何」。這是 proof-space dynamics 與普通文本生成最重要的分界之一。

---

## 參考文獻

1. Baoding He et al. *Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification*. arXiv:2603.19715, 2026.
2. Authors. *From Solvers to Research: Large Language Model-Driven Mathematical Discovery*. arXiv:2607.07779, 2026.
3. Authors. *A Minimal Agent for Automated Theorem Proving*. arXiv:2602.24273, 2026.
4. S. Kurgan et al. *TheoremGraph: Bridging Formal and Informal Mathematics*. arXiv:2606.25363, 2026.
5. EveMissLab internal research artifact. *NS Proof-Space Sampling Observatory v0.1*. 2026-08-17. Corpus instrumentation over the supplied NS archive; not a Navier--Stokes proof.


---

# LSI-PSD-05 — 局部飽和與全域開放：證明空間的多盆地結構

## Local Saturation and Global Openness: A Multi-Basin Model of Proof Space

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

長程 AI 數學研究最容易產生的誤判之一，是把某條支線的高重複率或 novelty decay 外推為「整個問題的證明空間已耗盡」。本文提出多盆地 proof-space 模型，將可觀察研究空間分解為若干由表示、方法、尺度、假設與 obstruction 結構形成的局部 basin。局部 basin 可以在全域仍高度開放時先進入飽和，也可以因 representation shift 或 method expansion 再次打開。本文定義局部覆蓋、局部邊際增量、basin escape、cross-basin transfer 與 reopening event，並說明為何 global nearest-neighbor novelty 天然受 corpus size 偏差影響。NS Proof-Space Sampling Observatory v0.1 的初步結果正提供一個例子：203 份 NS paper-like artifacts 中可以看見局部高階再採樣與 confluence，但固定回看窗的 novelty 並未支持全 corpus 單調崩塌。本文將此現象提升為一般方法論：proof-space saturation 應預設為 local、conditional、order-dependent，而不是 global、absolute、final。

**關鍵詞：** 局部飽和、多盆地、proof-space geometry、novelty decay、basin escape、global openness

---

## 1. 為什麼「越來越像以前」不等於全域耗盡

假設研究 corpus 依序為：

$$
g_1,g_2,\ldots,g_N.
$$

一個簡單 novelty 指標可以寫成：

$$
\nu_i^{\mathrm{cum}}
=
1-\max_{j<i}\operatorname{sim}(g_i,g_j).
$$

但當 $i$ 增加，可比較的先前樣本也增加，所以最大相似度天然有上升趨勢。即使研究分佈不變，也可能觀察到：

$$
\nu_i^{\mathrm{cum}}\downarrow.
$$

因此「後期更像前期」可能只是 comparison-pool bias。

更可靠的局部檢查是固定回看窗：

$$
\nu_i^{(W)}
=
1-
\max_{i-W\le j<i}
\operatorname{sim}(g_i,g_j).
$$

但即使 $\nu_i^{(W)}$ 下降，也只能描述附近歷史，不足以推出所有可能 proof route 都已經被採樣。

---

## 2. 多盆地模型

本文把可觀察 proof space 寫成：

$$
\widetilde\Omega_R(Q)
=
\bigcup_{\alpha\in A}
B_\alpha,
$$

其中 $B_\alpha$ 是 basin。

一個 basin 可以由下列條件共同形成：

$$
B_\alpha
=
B(
\mathcal L_\alpha,
\mathcal M_\alpha,
\mathcal A_\alpha,
\mathcal S_\alpha,
\mathcal O_\alpha
).
$$

分別代表：

- 特定表示；
- 特定方法族；
- 特定附加假設；
- 特定尺度或正則度 regime；
- 特定 obstruction family。

這些 basin 不必互斥。更合理的情形是：

$$
B_\alpha\cap B_\beta\neq\varnothing.
$$

交集正是跨方法轉移與 confluence 最常發生的位置。

---

## 3. 局部飽和

對 basin $B_\alpha$，定義：

$$
I_N(B_\alpha)
=
\int_{B_\alpha}
c_N(x)\,d\mu(x).
$$

若在一段足夠長的研究期內：

$$
\Delta I_N(B_\alpha)\approx0,
$$

且新增產物主要是既有等價類的重訪：

$$
\nu_k(B_\alpha,N)\approx0
$$

對若干低階 $k$ 成立，則可暫時稱：

$$
\operatorname{Sat}(B_\alpha\mid R,N)=1.
$$

這個「1」不是絕對數學真值，而是 operational label。

---

## 4. 全域開放

即使：

$$
\operatorname{Sat}(B_\alpha)=1,
$$

也完全可能存在：

$$
B_\beta
$$

使：

$$
\Delta I_N(B_\beta)\gg0.
$$

因此：

$$
\boxed{
\operatorname{Sat}(B_\alpha)
\not\Rightarrow
\operatorname{Sat}(\widetilde\Omega_R(Q)).
}
$$

更強地，即使目前所有已知 basin 都趨於飽和，也仍可能存在尚未被表示的 basin：

$$
B_\star
\not\subseteq
\widetilde\Omega_R(Q).
$$

這就是為什麼本系列始終拒絕把 empirical search saturation 寫成 mathematical exhaustion。

---

## 5. Basin escape

當一個 basin 接近飽和，下一步不一定是「再搜尋一億次」。

可以定義 escape operator：

$$
E_\alpha:
B_\alpha
\to
B_\beta.
$$

常見 escape 包括：

### 5.1 Representation escape

更換 variables、coordinates、gauge、formal encoding 或 theorem statement form。

### 5.2 Method escape

從 energy method 切到 compactness、probabilistic、topological、algebraic 或 computational method。

### 5.3 Scale escape

從 microscopic estimate 改成 renormalized、coarse-grained 或 asymptotic representation。

### 5.4 Problem escape

把原目標改寫成 auxiliary theorem、equivalent criterion 或 weaker/stronger statement。

### 5.5 Axiom / framework escape

在明確標記的情況下更改背景 theory 或 admissible assumptions。

每個 escape 都應保留來源：

$$
\operatorname{src}(E_\alpha)=B_\alpha.
$$

否則研究者會把「換了問題」誤報成「原問題被解決」。

---

## 6. Reopening event

一個看似飽和的 basin 可能因新工具重新打開。

設在時間 $t_0$：

$$
\Delta I_t(B_\alpha)\approx0.
$$

若新增工具或表示 $u$ 之後：

$$
\Delta I_{t_0+\tau}(B_\alpha;u)\gg0,
$$

則稱為 reopening event：

$$
\operatorname{Reopen}(B_\alpha,u)=1.
$$

這個概念特別適合描述新的 theorem prover、形式庫、符號回歸工具或跨領域 theorem transfer 帶來的重新活化。

因此飽和不是「死亡」，更像：

$$
\text{conditional quiescence}.
$$

---

## 7. Local saturation 可以跨階不同步

依第四篇的高階採樣，可定義：

$$
\operatorname{Sat}_k(B_\alpha).
$$

可能發生：

$$
\operatorname{Sat}_0(B_\alpha)=1,
$$

但：

$$
\operatorname{Sat}_2(B_\alpha)=0.
$$

意義是：新的原始 proof states 幾乎沒有，但 route-relations 仍在產生新資訊。

也可能：

$$
\operatorname{Sat}_0
=
\operatorname{Sat}_1
=
\operatorname{Sat}_2
=
1,
$$

而某個新的 representation escape 重新產生：

$$
\nu_0>0.
$$

所以 proof-space dynamics 不是單向走向枯竭，而可能是：

$$
\text{explore}
\to
\text{saturate}
\to
\text{escape}
\to
\text{reopen}.
$$

---

## 8. NS-203 的第一個實證訊號

NS Proof-Space Sampling Observatory v0.1 對 203 份 paper-like artifacts 的測量沒有支持「全 corpus novelty 單調崩塌」。

固定窗 $W=20$ 時：

$$
\bar\nu_{\mathrm{Q2}}=0.5425,
$$

$$
\bar\nu_{\mathrm{Q4}}=0.5781.
$$

差值為：

$$
0.0356.
$$

相對 500 次 random reordering 的基線，觀察到的變化並沒有形成「後期 unusually less novel」的訊號。

但同一 corpus 又明顯含有局部 confluence、高階回訪與 all-order 類研究。

這正符合：

$$
\boxed{
\text{local high-order saturation}
+
\text{global openness}.
}
$$

這個結果並不證明 NS 有任何特殊 metamathematical 性質，只證明「局部飽和」比「全域耗盡」更符合目前 corpus。

---

## 9. 多盆地指標

本文建議至少保存下列量。

### Basin coverage

$$
C_\alpha(N)
=
\frac{I_N(B_\alpha)}
{\mu(B_\alpha)}
$$

若分母可合理估計。

### Basin novelty

$$
N_\alpha^{(k)}
=
\nu_k(B_\alpha).
$$

### Basin confluence

$$
K_\alpha
=
\#\{\text{distinct route families entering the same obstruction zone}\}.
$$

### Escape rate

$$
E_\alpha(N)
=
\frac{\#\text{successful basin transitions}}
{\#\text{attempted escape operations}}.
$$

### Reopening gain

$$
R_\alpha(u)
=
I_{N+\Delta}(B_\alpha;u)-I_N(B_\alpha).
$$

---

## 10. 實務研究策略

當局部 basin 顯示飽和時，研究系統應從：

```text
generate more inside the same route
```

切換為：

```text
audit quotient classes
identify dominant obstruction
test representation sensitivity
search cross-series transfer
attempt basin escape
measure reopening
```

這是一個比「繼續讓同一模型多想幾次」更具資訊效率的策略。

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $B_\alpha$ | 局部 proof-space basin |
| $I_N(B_\alpha)$ | basin 邏輯空間積分 |
| $\operatorname{Sat}$ | operational saturation label |
| $E_\alpha$ | basin escape operator |
| $\operatorname{Reopen}$ | reopening event |
| $\nu_i^{(W)}$ | 固定窗 novelty |
| $K_\alpha$ | basin confluence measure |

---

## 12. 依賴與後續

**依賴：** LSI-PSD-01 至 04。  

**後續：** LSI-PSD-06、10、12。

---

## 結論

proof-space saturation 的預設語法不應是：

$$
\text{the space is exhausted}.
$$

而應是：

$$
\boxed{
\text{this basin, under this regime, at this order, shows low marginal novelty}.
}
$$

把這幾個條件全部保留下來，才能讓「飽和」成為研究工具，而不是新的終局神話。

---

## 參考文獻

1. EveMissLab internal research artifact. *NS Proof-Space Sampling Observatory v0.1*. 2026-08-17. Corpus instrumentation over the supplied NS archive; not a Navier--Stokes proof.
2. Krzysztof Olejniczak, Radoslav Dimitrov, Xingyue Huang, Bernardo Cuenca Grau, Jinwoo Kim, Ismail Ilkan Ceylan. *What are the Right Symmetries for Formal Theorem Proving?* arXiv:2605.22257, 2026.
3. Authors. *A Minimal Agent for Automated Theorem Proving*. arXiv:2602.24273, 2026.
4. Baoding He et al. *Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification*. arXiv:2603.19715, 2026.
5. FATE authors. *FATE: A Formal Benchmark Series for Frontier Algebra of Theorem Proving*. arXiv:2511.02872, 2026 revision.


---

# LSI-PSD-06 — 障礙匯流與研究路由：當不同方法反覆撞上同一堵牆

## Obstruction Confluence and Research Routing: When Distinct Methods Hit the Same Wall

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

當多條彼此獨立或弱相關的證明路徑反覆停在同一類障礙時，失敗本身開始產生可研究的拓撲結構。本文提出 obstruction confluence framework，把長程數學研究表示成由 claims、lemmas、routes、obstructions 與 verification states 組成的有向多重圖。本文區分 lexical convergence、semantic convergence、structural confluence 與 certified confluence，並提出 canonical obstruction ID 的建構規則。核心思想是：不同方法命中同一 obstruction 並不證明該 obstruction 是唯一真正瓶頸，但會提高其作為研究路由節點的優先度。本文定義 confluence degree、route diversity、obstruction persistence 與 escape yield，並提出一個實務準則：當 confluence 高而 escape yield 低時，研究應從「再攻一次」轉向「審計共同前提、表示與問題分解」。這一框架可將數百次失敗壓縮成少量可檢查的障礙族。

**關鍵詞：** obstruction、confluence、proof graph、research routing、negative information、canonicalization

---

## 1. 從失敗列表到障礙圖

沒有結構的失敗紀錄像：

```text
attempt 1 failed
attempt 2 failed
attempt 3 failed
...
```

這種資料幾乎不可用。

更有價值的記錄是：

$$
T_i
:
A_i
\to
L_i
\to
C_i
\to
O_j,
$$

其中：

- $A_i$ 是 route-specific assumptions；
- $L_i$ 是中間 lemmas；
- $C_i$ 是 closure attempt；
- $O_j$ 是 canonical obstruction。

當多個 $T_i$ 指向同一 $O_j$，才出現 confluence。

---

## 2. Proof-route multigraph

定義圖：

$$
\mathcal G
=
(V,E,\tau,\sigma).
$$

節點 $V$ 可以包含：

$$
V
=
V_Q
\cup
V_A
\cup
V_L
\cup
V_R
\cup
V_O
\cup
V_S.
$$

分別是：

- target claims；
- assumptions；
- lemmas；
- routes；
- obstructions；
- status nodes。

邊 $E$ 保存：

- depends-on；
- implies；
- refines；
- contradicts；
- revisits；
- fails-at；
- transfers-to。

$\tau$ 是 node type，$\sigma$ 是 evidence status。

---

## 3. 四種「匯流」不能混在一起

### 3.1 Lexical convergence

不同文本使用相同詞，例如 pressure、criticality、recurrence。

這只能形成候選：

$$
C_{\mathrm{lex}}.
$$

### 3.2 Semantic convergence

經過 assumption 與 proposition comparison 後，兩個 obstruction 描述指向相同語義缺口：

$$
O_i\sim_{\mathrm{sem}}O_j.
$$

### 3.3 Structural confluence

不同 route graph 的末端子圖可以映射到同一 failure template：

$$
\Gamma_i^{\mathrm{tail}}
\simeq
\Gamma_j^{\mathrm{tail}}.
$$

### 3.4 Certified confluence

若有 formal proof、counterexample、machine-checked incompatibility 或可重現 computation 證明兩者確實共享同一 obstruction，才標記：

$$
C_{\mathrm{cert}}.
$$

所以 confluence 應有證據等級，而不是一個二值標籤。

---

## 4. Canonical obstruction ID

每個 obstruction 應至少記錄：

```yaml
obstruction_id:
claim_scope:
required_assumptions:
failure_statement:
witness_or_counterexample:
formal_status:
first_seen:
revisited_by:
equivalent_to:
stronger_than:
weaker_than:
representation_dependence:
escape_attempts:
```

canonical ID 的目的不是命名漂亮，而是防止同一障礙被 40 篇論文取 40 個名字。

---

## 5. Confluence degree

對 obstruction $O$，定義：

$$
\kappa(O)
=
\#\{\text{distinct audited route families reaching }O\}.
$$

但單純 route count 會被同一家族複製灌水，所以增加 route diversity：

$$
d(O)
=
H(
\text{method-family distribution reaching }O
),
$$

其中 $H$ 可以是 Shannon 型 entropy，也可以是其他明示多樣性指標。

因此高價值 confluence 應同時滿足：

$$
\kappa(O)\uparrow
$$

與：

$$
d(O)\uparrow.
$$

也就是不只是很多次，而是很多不同方法都撞到它。

---

## 6. Obstruction persistence

定義 obstruction 在研究歷史中的 persistence：

$$
P_N(O)
=
\frac{
\#\text{time windows in which }O\text{ is revisited}
}{
\#\text{observed windows}
}.
$$

若：

$$
P_N(O)\to1,
$$

表示這個 obstruction 長期存在於多個研究階段。

但仍然不能推出：

$$
O=\text{fundamental mathematical barrier}.
$$

因為它可能只是當前 representation 的共同 blind spot。

因此 persistence 必須和 representation audit 一起看。

---

## 7. Escape yield

對 obstruction $O$ 的第 $m$ 次 escape attempt，記錄是否真正產生：

- 新等價類；
- 新可驗證 lemma；
- 新 basin；
- 或正式關閉 $O$。

定義：

$$
Y(O)
=
\frac{
\#\text{escape attempts producing audited novelty}
}{
\#\text{escape attempts}
}.
$$

若：

$$
\kappa(O)\gg1,
\qquad
P_N(O)\approx1,
\qquad
Y(O)\approx0,
$$

則研究策略應轉成：

$$
\boxed{
\text{audit the shared premises of the routes feeding }O.
}
$$

不是再盲目增加相同類型 attempt。

---

## 8. 匯流可以是假的

高 confluence 也可能由研究制度造成。

例如所有 agent 都讀同一 corpus、使用同一 theorem library、同一 prompt family、同一 representation，則：

$$
\kappa_{\mathrm{observed}}
$$

可能只是 shared initialization。

因此需定義 route independence score：

$$
\iota(T_i,T_j)\in[0,1].
$$

可根據：

- 不同模型；
- 不同工具；
- 不同文獻子集；
- 不同 proof language；
- 不同 initial decomposition；
- 不同 formal system；

估計。

更可靠的 confluence 是：

$$
\kappa^\star(O)
=
\sum_{T_i\to O}
w_i,
$$

其中 $w_i$ 依 route independence 調整。

---

## 9. NS corpus 的例子

NS Proof-Space Sampling Observatory v0.1 已初步偵測多個跨系列 confluence zones，例如：

- carrier-supplier；
- rigidity-closure；
- obstruction-gap-defect；
- recurrence-return；
- criticality。

這些只是 controlled concept families，不是已證明的 mathematical equivalence。

更有價值的是跨系列 traffic，例如：

$$
\text{MORP}\to\text{DCRP},
$$

$$
\text{FCBP}\to\text{DCRP},
$$

$$
\text{NS-O}\to\text{X72}.
$$

下一版若能把這些 paper-level edge 下鑽成 claim-level obstruction IDs，就能測：

$$
\kappa(O),\quad d(O),\quad P_N(O),\quad Y(O).
$$

---

## 10. Research router

基於 obstruction graph，可建立簡單路由器：

```text
if new_route:
    explore
elif same_obstruction and low_independence:
    diversify_method
elif same_obstruction and high_independence:
    audit_common_assumptions
elif high_persistence and low_escape_yield:
    attempt_basin_escape
elif certified_obstruction:
    register_no_go_region
else:
    continue_local_search
```

這使 AI 長程研究從「不斷生成」轉成「根據 proof-space 狀態分配算力」。

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $\mathcal G$ | proof-route multigraph |
| $O$ | canonical obstruction |
| $\kappa(O)$ | confluence degree |
| $d(O)$ | route diversity |
| $P_N(O)$ | obstruction persistence |
| $Y(O)$ | escape yield |
| $\iota$ | route independence score |
| $\kappa^\star$ | independence-adjusted confluence |

---

## 12. 依賴與後續

**依賴：** LSI-PSD-01 至 05。  

**後續：** LSI-PSD-10、12。

---

## 結論

當不同方法反覆撞到同一堵牆，最重要的不是替那堵牆取更華麗的名字，而是回答：

$$
\boxed{
\text{Is this one wall, many similar walls, or one artifact of our common representation?}
}
$$

obstruction confluence framework 的任務，就是把這三者分開。

---

## 參考文獻

1. EveMissLab internal research artifact. *NS Proof-Space Sampling Observatory v0.1*. 2026-08-17. Corpus instrumentation over the supplied NS archive; not a Navier--Stokes proof.
2. S. Kurgan et al. *TheoremGraph: Bridging Formal and Informal Mathematics*. arXiv:2606.25363, 2026.
3. Baoding He et al. *Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification*. arXiv:2603.19715, 2026.
4. Krzysztof Olejniczak, Radoslav Dimitrov, Xingyue Huang, Bernardo Cuenca Grau, Jinwoo Kim, Ismail Ilkan Ceylan. *What are the Right Symmetries for Formal Theorem Proving?* arXiv:2605.22257, 2026.
5. Authors. *From Solvers to Research: Large Language Model-Driven Mathematical Discovery*. arXiv:2607.07779, 2026.


---

# LSI-PSD-07 — 真理—生成性反轉：為什麼更精確不一定產生更多理論

## Truth--Generativity Inversion: Why Greater Precision Need Not Produce More Theory

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

科學與數學研究常隱含一個直覺：定義越精確、理論越接近真實，應該產生越多有價值的知識。本文指出，這個單調關係並不成立。當一個問題的約束逐漸增加，候選空間可能收縮；在極端情況下，最終閉合命題甚至表現得近似同一律或極低描述長度，而真正龐大的資訊存在於從核心到具體現象的生成過程。另一方面，較粗糙、理想化甚至局部失真的模型可能具有更高的操作生成性，因為它們保留較多自由度並暴露可研究的偏差結構。本文把這個現象稱為「真理—生成性反轉」，但明確將其定位為研究假說，而非普遍定理。本文區分 truth、fidelity、generativity、utility 與 compressibility 五個軸，並說明它們之間不存在一般單調序。科學模型、minimal models 與 effective field theories 的哲學研究提供了直接先例：更基本、更真實或更詳細，並不自動意味著更能解釋或更適合某個尺度的研究。

**關鍵詞：** 真理、生成性、精確性、理想化、minimal models、effective theory、compression、scientific understanding

---

## 1. 一個常被默認的單調函數

很多研究直覺近似假設：

$$
\text{precision}\uparrow
\Rightarrow
\text{truth-likeness}\uparrow
\Rightarrow
\text{understanding}\uparrow
\Rightarrow
\text{generativity}\uparrow.
$$

前兩個箭頭在某些條件下都已經需要辯護，最後兩個更沒有一般保證。

科學模型哲學早已指出，理想化模型會刻意簡化甚至扭曲真實系統，以換取 tractability 與 understanding。Minimal Model Explanations 更進一步主張，一個模型的解釋力有時不來自它保留了更多真實細節，而來自它揭示哪些細節對宏觀行為不重要。

這使「更接近真實」與「更能生成研究」第一次被系統性分開。

---

## 2. 五軸模型

本文定義：

$$
\mathbf Z
=
(T,F,G,U,C).
$$

其中：

- $T$：truth status 或 truth-likeness；
- $F$：fidelity，對目標系統的保真程度；
- $G$：generativity，可生成新問題、模型、推論與路徑的能力；
- $U$：utility，對任務的實用價值；
- $C$：compressibility，核心描述能否被壓縮。

這五者沒有一般全序。

可能出現：

$$
F_1>F_2
$$

但：

$$
G_1<G_2.
$$

也可能：

$$
C_1>C_2
$$

但：

$$
U_1<U_2.
$$

所以本文不再使用「越好」作單一尺度。

---

## 3. 約束增加會縮小候選空間

令問題定義為 $D$，其 admissible candidate space 為：

$$
\Omega(D).
$$

若 $D_2$ 在 $D_1$ 上增加有效限制：

$$
D_2=D_1+\Delta C,
$$

常見情況是：

$$
\Omega(D_2)\subseteq\Omega(D_1).
$$

因此候選空間的有效 entropy 可能下降：

$$
H_{\mathrm{eff}}(\Omega(D_2))
\le
H_{\mathrm{eff}}(\Omega(D_1)).
$$

如果定義逼近一個高度閉合的核心：

$$
D\to D^\star,
$$

可能得到：

$$
|\Omega(D^\star)|\approx1.
$$

此時最終命題的表面 novelty 會很低。

這正是「越逼近閉合，越像廢話」的形式版本之一。

---

## 4. 低描述長度不等於低生成性

一個核心規則可以很短，卻有巨大生成閉包。

設核心為 $K$，生成算子為 $\Phi$：

$$
\mathcal G(K)
=
\bigcup_{n\ge0}\Phi^n(K).
$$

可能有：

$$
\operatorname{DL}(K)\ll1
$$

相對於：

$$
\operatorname{DL}(\mathcal G(K)).
$$

因此：

$$
\boxed{
\text{core simplicity}
\not\Rightarrow
\text{world simplicity}.
}
$$

「核心看起來像廢話」與「從核心生成的現象非常豐富」可以同時成立。

這也說明為什麼一個成熟理論的終局表述可能越來越短，而研究與應用並不因此消失。

---

## 5. Minimal models 的反例

Batterman 與 Rice 對 minimal models 的分析提供一個典型反例。某些模型刻意忽略大量微觀細節，卻能解釋不同物理系統為何出現相同宏觀行為。

若增加所有微觀真實細節，模型可能更 faithful，但 universal structure 反而更難看見。

因此可能有：

$$
F\uparrow
\quad\text{while}\quad
U_{\mathrm{explanatory}}\downarrow.
$$

這不是鼓勵錯誤，而是提醒 fidelity 與 explanatory relevance 是不同軸。

---

## 6. Effective theories 的反例

Effective field theories 在明確能標示 validity regime 的前提下，可能對特定尺度提供比更 fundamental 描述更好的 tractability 與 understanding。

近期關於 productive idealization 與 EFT 的工作進一步強調：

$$
\text{more fundamental}
\not\Rightarrow
\text{more understanding}
$$

至少不是無條件成立。

這與 proof-space research 的關係很直接。如果一個過度 fundamental 的 formulation 對實際 proof search 不提供可操作中間量，那麼較粗糙的 effective formulation 可能具有更高 $G$ 與 $U$。

---

## 7. 真理—生成性反轉假說

本文提出弱形式：

### 假說 TG-1

存在研究域與任務，使：

$$
F(D_2)>F(D_1)
$$

但：

$$
G(D_2)<G(D_1).
$$

即更高 fidelity 不保證更高 generativity。

更強形式：

### 假說 TG-2

在接近高閉合定義 $D^\star$ 時，局部候選自由度可能下降：

$$
D\to D^\star
\Rightarrow
H_{\mathrm{eff}}(\Omega(D))\downarrow,
$$

但從 $D^\star$ 出發的 downstream generative closure 仍可很大：

$$
|\mathcal G(D^\star)|\gg1.
$$

TG-2 不是一般數學定理，而是一個可對不同研究域測量的 structural hypothesis。

---

## 8. 「越是真理越像廢話」的嚴格化

這句話如果沒有條件會過度強。

本文只保留以下版本：

$$
\boxed{
\text{When independent degrees of freedom are progressively eliminated, a closure statement may become semantically low-novelty while remaining structurally high-value.}
}
$$

也就是：

> 當獨立自由度被逐步消除，閉合命題可能在表面語義上低新穎，卻仍是整個推導結構的高價值壓縮點。

這和「所有真理都是廢話」完全不同。

---

## 9. 對 AI 數學研究的意義

如果 AI corpus 後期大量出現：

- 更短的 closure statement；
- 更少的獨立 obstruction family；
- 更高的 route confluence；
- 更低的 low-order novelty；

研究者不能立即判斷這是：

$$
\text{model collapse}
$$

還是：

$$
\text{structural compression}.
$$

需要額外檢查：

$$
\text{verification},
\text{transfer},
\text{dependency reduction},
\text{representation invariance}.
$$

只有當壓縮仍保持可重建性，才有資格叫「閉合」。

---

## 10. 符號表

| 符號 | 意義 |
|---|---|
| $T$ | truth / truth-likeness |
| $F$ | fidelity |
| $G$ | generativity |
| $U$ | utility |
| $C$ | compressibility |
| $D$ | 問題或模型定義 |
| $\Omega(D)$ | admissible candidate space |
| $D^\star$ | 高閉合參考定義 |
| $\mathcal G(K)$ | 核心 $K$ 的生成閉包 |

---

## 11. 依賴與後續

**依賴：** LSI-PSD-01 至 06。  

**後續：** LSI-PSD-08、09、11。

---

## 結論

真理、精確、詳細、基本、可解釋、可生成、可實用不是同一條軸。

本文的核心否定式是：

$$
\boxed{
\text{Greater precision does not universally imply greater generativity.}
}
$$

而正面研究問題是：

$$
\boxed{
\text{在什麼條件下，理論自由度的下降會轉化成閉合，而不是貧瘠？}
}
$$

這個問題將直接導向下一篇的生產性錯置。

---

## 參考文獻

1. Roman Frigg and Stephan Hartmann. *Models in Science*. Stanford Encyclopedia of Philosophy, current online edition, accessed 2026-08-17.
2. Robert W. Batterman and Collin C. Rice. *Minimal Model Explanations*. Philosophy of Science 81(3), 2014.
3. Karla Weingarten. *Productive Idealizations for Scientific Understanding*. PhilSci-Archive preprint, 2026.
4. Author(s). *Abstraction, Explanation, and Effective Field Theories*. arXiv:2507.03582, 2025.
5. Stanford Encyclopedia of Philosophy. *Mathematical Explanations*. Current online edition, accessed 2026-08-17.


---

# LSI-PSD-08 — 生產性錯置：錯誤問題如何生成正確的後代理論

## Productive Mis-specification: How a Wrong Parent Problem Can Generate Correct Descendants

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

科學史與現代模型研究反覆顯示：一個模型可以包含錯誤本體、理想化假設、尺度錯置或缺失機制，卻仍產生可重現、可移植甚至後來被保留的局部結構。本文把這種現象形式化為「生產性錯置」。核心區分是 parent validity 與 descendant validity：父問題、父模型或父 framing 的錯誤不會邏輯上污染所有後代理論；反之，後代中出現真實定理或有用工具，也不能倒推父 framing 正確。本文定義 mis-specification vector、descendant graph、truth retention、transfer utility 與 salvage ratio，並提出「父子真值分離原則」。2026 年 missing-physics discovery 的工作進一步顯示，模型誤差可以被局部化並轉化成缺失機制的符號發現；這提供了從「錯誤」走向「可測 discrepancy」的工程接口。本文同時設置嚴格限制：生產性錯置不等於任意錯誤，必須要求與資料、形式驗證、局部有效域或可重建機制保持接觸。

**關鍵詞：** 生產性錯置、productive mis-specification、model discrepancy、missing physics、descendant theory、structured error

---

## 1. 父問題錯，不代表子結果都錯

設父問題或父模型為：

$$
P.
$$

它在研究過程中產生 descendant set：

$$
\mathcal D(P)
=
\{D_1,D_2,\ldots,D_n\}.
$$

常見但錯誤的直覺是：

$$
P=\text{false}
\Rightarrow
D_i=\text{false for all }i.
$$

這在邏輯上並不成立。

一個錯誤模型仍可包含：

- 正確的局部關係；
- 正確的 limit；
- 正確的 invariant；
- 有效 approximation；
- 可重用的數學工具；
- 新實驗；
- 新測量技術；
- 對錯誤來源的診斷。

所以必須把 parent status 與 descendant status 分離。

---

## 2. 父子真值分離原則

本文提出：

$$
\boxed{
V(P)
\not\Rightarrow
V(D_i)
}
$$

以及：

$$
\boxed{
V(D_i)
\not\Rightarrow
V(P),
}
$$

其中 $V$ 表示適合該 domain 的 validity predicate。

更具體地：

$$
\neg V(P)
\centernot\Rightarrow
\forall i\,\neg V(D_i).
$$

這是生產性錯置的邏輯底座。

---

## 3. Mis-specification vector

「錯」不是單一軸。定義：

$$
\epsilon(P)
=
(
\epsilon_D,
\epsilon_S,
\epsilon_A,
\epsilon_M,
\epsilon_R
).
$$

其中：

- $\epsilon_D$：domain mismatch；
- $\epsilon_S$：semantic / representation mismatch；
- $\epsilon_A$：assumption mismatch；
- $\epsilon_M$：missing mechanism；
- $\epsilon_R$：resolution / scale mismatch。

兩個模型可能有相似總誤差，但錯在完全不同位置。

因此任何「錯誤越多越有生成性」的粗糙命題都應被拒絕。

---

## 4. Structured error 與 arbitrary error

本文只研究 structured error。

一個錯置若要具有研究價值，至少滿足其中數項：

1. 有明確 validity regime；
2. 能生成可檢驗預測；
3. 偏差能被測量；
4. 有可識別 residual；
5. 可對照更高 fidelity 模型；
6. 產生的子命題能獨立驗證；
7. 錯誤可以被局部化或拆分；
8. 研究路徑可重建。

反之，任意拼湊且不接受反駁的框架不屬於 productive mis-specification。

---

## 5. 後代理論圖

定義 descendant graph：

$$
\mathcal G_P
=
(V_P,E_P).
$$

節點包括：

- parent assumptions；
- intermediate lemmas；
- derived models；
- experimental designs；
- computational tools；
- transferable theorems；
- corrected formulations。

每個 descendant $D_i$ 都需要自己的 validation status：

$$
v_i
\in
\{
\text{unverified},
\text{numerically supported},
\text{formally proved},
\text{empirically confirmed},
\text{refuted}
\}.
$$

這能避免研究者把「父框架有問題」當成一次性刪庫理由。

---

## 6. Truth retention 與 salvage ratio

定義經獨立審計後仍成立的 descendants：

$$
\mathcal D^+(P).
$$

truth retention ratio：

$$
R_T(P)
=
\frac{
|\mathcal D^+(P)|
}{
|\mathcal D(P)|
}.
$$

但不同成果價值不同，所以再定義 weighted salvage ratio：

$$
R_S(P)
=
\frac{
\sum_{D_i\in\mathcal D^+(P)}w(D_i)
}{
\sum_{D_i\in\mathcal D(P)}w(D_i)
}.
$$

$w$ 可以根據：

- formal strength；
- empirical support；
- transfer count；
- downstream usage；
- reproducibility；

設定。

這兩個指標都不能評價父命題真值，只評價「錯置後留下多少可救回的知識」。

---

## 7. Missing physics 作為現代工程接口

2026 年 LISDD 的核心問題非常接近本文精神：物理模型不一定在所有 operating regimes 中同樣錯。它先找 clean regime，再定位 discrepancy region，最後從候選 symbolic library 中辨識 missing mechanism。

可抽象為：

$$
\text{trusted model}
+
\text{localized discrepancy}
\to
\text{candidate missing term}.
$$

這個流程顯示，錯誤不一定只能被整體拋棄，而可以被轉成：

$$
\text{where wrong}
+
\text{how wrong}
+
\text{what is missing}.
$$

本文把這種局部化能力視為 productive mis-specification 的必要工程條件之一。

---

## 8. 為什麼錯置會增加生成性

若原定義 $D^\star$ 已高度閉合：

$$
|\Omega(D^\star)|\ll|\Omega(D')|.
$$

當某個有限錯置 $D'$ 引入額外自由度時，研究系統會被迫處理：

- correction terms；
- boundary regimes；
- incompatibilities；
- residual dynamics；
- alternative variables；
- new limiting cases。

因此 descendant count 可以增加。

但這不是好事的保證。只有其中能通過獨立 validation 的部分才算 epistemically salvageable。

---

## 9. 對數學未解問題的限制

如果某個未解問題長期產生大量正確子理論，我們不能因此說：

$$
\text{parent problem is mis-specified}.
$$

因為任何真正困難且正確表述的問題，也可能具有巨大 descendant graph。

所以：

$$
\boxed{
G(P)\uparrow
\not\Rightarrow
\operatorname{MisSpecified}(P).
}
$$

要支持 mis-specification hypothesis，還需要：

- 明確 category inconsistency；
- semantic non-equivalence；
- proof obligation 與實際 target 不一致；
- 新 formulation 對 recurrent obstruction 有統一解釋；
- 或形式證明舊 formulation 沒有預期的 truth condition。

這條限制對 NS 與 P vs NP 尤其重要。

---

## 10. 生產性錯置與「問錯問題」

本文不使用「問錯問題」作粗糙結論。

更精確的情形至少有：

$$
\text{ill-posed},
$$

$$
\text{well-posed but unhelpful},
$$

$$
\text{well-posed but representation-poor},
$$

$$
\text{domain-misaligned},
$$

$$
\text{scale-misaligned},
$$

$$
\text{partially valid}.
$$

productive mis-specification 主要研究中間地帶，而不是把所有非最優 framing 都叫錯。

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $P$ | parent problem / model |
| $\mathcal D(P)$ | descendant set |
| $\epsilon(P)$ | mis-specification vector |
| $\mathcal G_P$ | descendant graph |
| $R_T(P)$ | truth retention ratio |
| $R_S(P)$ | weighted salvage ratio |
| $w(D_i)$ | descendant value weight |

---

## 12. 依賴與後續

**依賴：** LSI-PSD-07。  

**後續：** LSI-PSD-09、11、12。

---

## 結論

生產性錯置最重要的不是替錯誤辯護，而是拒絕兩種粗暴刪除：

$$
\text{wrong parent}
\Rightarrow
\text{all descendants worthless}
$$

與：

$$
\text{useful descendants}
\Rightarrow
\text{parent must be right}.
$$

真正成熟的研究系統應該把父問題與子成果拆開驗證，留下可以 salvage 的知識，同時允許父 framing 被修正、替換甚至放棄。

---

## 參考文獻

1. Yifan Wang. *Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy*. arXiv:2606.23215, 2026.
2. Authors. *Learning Missing Physics, Modeling Systematic Residuals*. SIAM Journal on Scientific Computing, DOI 10.1137/22M148375X.
3. Roman Frigg and Stephan Hartmann. *Models in Science*. Stanford Encyclopedia of Philosophy, current online edition, accessed 2026-08-17.
4. Karla Weingarten. *Productive Idealizations for Scientific Understanding*. PhilSci-Archive preprint, 2026.
5. Clay Mathematics Institute. *Navier--Stokes Equation: Existence and Smoothness*. Official Millennium Prize Problem page and Charles L. Fefferman problem description, accessed 2026-08-17. https://www.claymath.org/millennium/navier-stokes-equation/
6. Clay Mathematics Institute. *P vs NP*. Official Millennium Prize Problem page, accessed 2026-08-17. https://www.claymath.org/millennium/p-vs-np/


---

# LSI-PSD-09 — 生產性錯置窗口：真理、錯誤與知識肥沃性的非單調曲線

## The Productive Mis-specification Window: A Non-Monotone Relation Between Error and Epistemic Fertility

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

若完全精確的模型不必然具有最大生成性，而有限錯置又可能產生新的 correction、boundary、residual 與 descendant theories，一個自然但尚未證明的問題是：有效生成性是否對錯置程度呈非單調關係？本文提出「生產性錯置窗口」猜想。令 $\epsilon$ 表示相對參考 formulation 的結構偏差，令 $G_{\mathrm{useful}}(\epsilon)$ 表示經驗證後仍有價值的後代生成率。本文猜想某些研究域可能存在中間區間，使 $G_{\mathrm{useful}}$ 高於高度閉合區與任意失真區；幾何上可能近似 inverted-U，但本文明確拒絕把 inverted-U 視為普遍定律。本文提供可證偽的量化設計：將錯置分解為 domain、semantics、assumption、mechanism 與 resolution 五軸，使用受控 perturbation、獨立驗證與 descendant salvage rate 測試每個軸的反應曲線。本文並提出 fertility、noise、salvage、transfer 四個互相獨立的量，以避免「生成很多垃圾」被錯算成高知識肥沃性。

**關鍵詞：** productive window、non-monotonicity、mis-specification、epistemic fertility、inverted-U、controlled perturbation

---

## 1. 從定性觀察到可證偽猜想

前兩篇得到兩個相容命題：

$$
\text{precision}\uparrow
\not\Rightarrow
\text{generativity}\uparrow,
$$

以及：

$$
\text{structured error}
\not\Rightarrow
\text{zero epistemic value}.
$$

但這仍不足以推出：

$$
\text{moderate error is best}.
$$

因此本文不把「中等錯誤最肥沃」當作結論，而只提出一個待測曲線。

---

## 2. 錯置不是一維變數

令：

$$
\boldsymbol\epsilon
=
(
\epsilon_D,
\epsilon_S,
\epsilon_A,
\epsilon_M,
\epsilon_R
).
$$

五軸分別是：

- domain mismatch；
- semantic / representation mismatch；
- assumption mismatch；
- missing-mechanism mismatch；
- resolution / scale mismatch。

總距離可定義為：

$$
\|\boldsymbol\epsilon\|_W
=
\sqrt{
\boldsymbol\epsilon^\top
W
\boldsymbol\epsilon
},
$$

但 $W$ 只是任務條件化權重，不應被宣稱為自然唯一度量。

不同錯誤方向可能有完全不同的生成效果，因此應先估計：

$$
G(\epsilon_D),
\quad
G(\epsilon_S),
\quad
G(\epsilon_A),
\quad
G(\epsilon_M),
\quad
G(\epsilon_R),
$$

再討論混合效應。

---

## 3. 知識肥沃性不是生成篇數

定義 raw generation：

$$
G_{\mathrm{raw}}.
$$

定義 verified descendant count：

$$
G_{\mathrm{ver}}.
$$

定義 transferable descendant count：

$$
G_{\mathrm{tr}}.
$$

本文提出 epistemic fertility：

$$
F_E
=
\alpha G_{\mathrm{ver}}
+
\beta G_{\mathrm{tr}}
+
\gamma N_{\mathrm{new}}
-
\delta N_{\mathrm{noise}},
$$

其中：

- $N_{\mathrm{new}}$：新的 audited equivalence classes；
- $N_{\mathrm{noise}}$：無法驗證、重複或失去目標接觸的產物；
- $\alpha,\beta,\gamma,\delta$ 必須在實驗前設定。

這使一萬篇 hallucinated papers 不會自動得到高 fertility。

---

## 4. 生產性錯置窗口猜想

### PMW 弱猜想

存在某些研究任務 $\tau$ 與錯置方向 $j$，使：

$$
F_E(\epsilon_j)
$$

不是單調函數。

### PMW 中等猜想

存在區間：

$$
0<\epsilon_a<\epsilon_b
$$

使：

$$
F_E(\epsilon)
>
F_E(0)
$$

對某些 $\epsilon\in(\epsilon_a,\epsilon_b)$ 成立。

### PMW inverted-U 猜想

某些受控任務可能近似：

$$
F_E(\epsilon)
=
a\epsilon e^{-b\epsilon}
+
c,
\qquad
a,b>0.
$$

此函數在：

$$
\epsilon^\star=\frac{1}{b}
$$

附近達到局部最大。

本文強調：這只是方便測試的 parametric toy form，不是理論預言。

---

## 5. 為什麼左端可能低生成

在 $\epsilon=0$ 附近，如果參考 formulation 已高度閉合，可能出現：

$$
\operatorname{DoF}(\Omega)\downarrow.
$$

新增研究多半是：

- 更精確驗證；
- 更短證明；
- 更好實作；
- 更強應用；

而不是大量新 theory branches。

因此 raw branch count 可能下降。

但這完全不表示精確 formulation 價值低。它的價值可能轉移到：

$$
\text{reliability},
\text{compression},
\text{transfer},
\text{engineering}.
$$

---

## 6. 為什麼中段可能高生成

有限 structured perturbation 會暴露：

- failure boundaries；
- correction terms；
- hidden assumptions；
- regime transitions；
- missing variables；
- model discrepancies。

例如 missing-physics discovery 的工作正是從 residual 中搜尋缺失項。

因此中段可能增加：

$$
N_{\mathrm{new}},
\quad
G_{\mathrm{ver}},
\quad
G_{\mathrm{tr}}.
$$

---

## 7. 為什麼右端會崩潰

當錯置過大：

$$
\|\boldsymbol\epsilon\|\gg1,
$$

模型可能失去：

- empirical contact；
- formal coherence；
- stable semantics；
- reproducibility；
- meaningful descendant validation。

此時 raw generation 甚至可能繼續上升：

$$
G_{\mathrm{raw}}\uparrow,
$$

但：

$$
F_E\downarrow.
$$

這是 productive mis-specification 與任意幻想之間的邊界。

---

## 8. 實驗設計

本文建議使用已知答案或可控模型，而不是直接拿完全未知的 Millennium problem 當第一個測試場。

### 8.1 Known-theorem perturbation

選擇已有正式證明的 theorem $Q$，系統性修改：

- 量詞；
- domain；
- 假設；
- representation；
- auxiliary structure。

得到：

$$
Q^{(\epsilon_1)},
\ldots,
Q^{(\epsilon_m)}.
$$

讓多個 AI agent 在固定 budget 下研究，記錄 descendants 與 salvage。

### 8.2 Known-physics perturbation

選擇已知 governing equation，刻意移除一項或錯設尺度，再測是否：

$$
\text{residual}
\to
\text{missing mechanism discovery}.
$$

### 8.3 Blind evaluation

生成 agent 不知道正確 formulation；audit agent 使用獨立工具與資料判斷 descendant validity。

這可以減少 confirmation bias。

---

## 9. Null models

任何觀察到的 inverted-U 都必須和至少三個 null 比較：

### Random-error null

錯置只是隨機噪聲。

### Search-volume null

中段只是因 branch count 更多，所以偶然產生更多結果。

### Evaluator-bias null

audit system 對某種複雜度或文字風格偏好。

只有超過這些 null，才能說有 productive window evidence。

---

## 10. 對 NS 與 P vs NP 的態度

完全未知問題不適合用來「證明」 PMW，因為我們不知道：

$$
\epsilon=0
$$

到底在哪裡。

因此 NS 與 P vs NP 在本框架中只能用作：

$$
\text{observational case},
$$

不是 ground-truth experiment。

更好的順序是：

$$
\text{known cases}
\to
\text{controlled perturbation}
\to
\text{calibrated metrics}
\to
\text{open-problem observation}.
$$

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $\boldsymbol\epsilon$ | 錯置向量 |
| $F_E$ | epistemic fertility |
| $G_{\mathrm{raw}}$ | raw generation |
| $G_{\mathrm{ver}}$ | verified descendants |
| $G_{\mathrm{tr}}$ | transferable descendants |
| $N_{\mathrm{new}}$ | 新 audited 類 |
| $N_{\mathrm{noise}}$ | 噪聲或無效產物 |
| $\epsilon^\star$ | toy inverted-U 的局部最大位置 |

---

## 12. 依賴與後續

**依賴：** LSI-PSD-07、08。  

**後續：** LSI-PSD-11、12。

---

## 結論

「有限錯誤可能更肥沃」現在可以從哲學直覺轉成可失敗的實驗命題。

本文最重要的自我限制是：

$$
\boxed{
\text{The inverted-U is a hypothesis to test, not a law to assume.}
}
$$

如果實驗顯示所有錯置都只降低 verified fertility，那麼 PMW 應被拒絕；如果只有特定錯置方向產生局部峰值，則應把理論縮小到那些方向，而不是保留一個漂亮但空泛的普遍曲線。

---

## 參考文獻

1. Yifan Wang. *Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy*. arXiv:2606.23215, 2026.
2. Authors. *Learning Missing Physics, Modeling Systematic Residuals*. SIAM Journal on Scientific Computing, DOI 10.1137/22M148375X.
3. Karla Weingarten. *Productive Idealizations for Scientific Understanding*. PhilSci-Archive preprint, 2026.
4. Roman Frigg and Stephan Hartmann. *Models in Science*. Stanford Encyclopedia of Philosophy, current online edition, accessed 2026-08-17.
5. Robert W. Batterman and Collin C. Rice. *Minimal Model Explanations*. Philosophy of Science 81(3), 2014.


---

# LSI-PSD-10 — 飽和不是判決：證明空間非結論原則

## Saturation Is Not a Verdict: The Proof-Space Non-Conclusion Principle

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

本系列最容易被誤讀的地方，是把 proof-space saturation 當成對目標數學命題的裁決。本文專門建立認識論防火牆。即使某個 AI 研究制度已經產生數萬次研究、完成語義去重、觀察到低階與高階 novelty 衰減、不同方法匯流到相同 obstruction，仍不能僅由這些現象推出目標命題為假、問題表述錯誤、不可證、獨立或不可判定。本文將這個限制命名為「證明空間非結論原則」。本文區分至少十種可造成長期無解的候選原因，並提出 evidence ladder：搜尋失敗、局部飽和、跨方法匯流、representation robustness、formal no-go、counterexample、proof、independence proof 各自具有不同結論權限。Navier--Stokes 與 P vs NP 被用作案例說明：截至 2026-08-17，Clay Mathematics Institute 仍將兩者列為未解問題；任何私人或 AI corpus 的失敗都不能改寫其正式數學地位。本文的目的不是削弱 proof-space science，而是讓它能在不越權的情況下提供可靠診斷。

**關鍵詞：** non-conclusion principle、search saturation、independence、unprovability、epistemic firewall、open problems

---

## 1. 最危險的推論

考慮：

$$
10^4
$$

次 AI 研究都沒有找到目標證明。

直覺很容易滑向：

$$
\text{many failures}
\Rightarrow
\text{problem is wrong}.
$$

或者：

$$
\text{many failures}
\Rightarrow
\text{unprovable}.
$$

這兩個箭頭都不成立。

---

## 2. 證明空間非結論原則

本文正式提出：

$$
\boxed{
\operatorname{Sat}(\Omega_R(Q))
\not\Rightarrow
\operatorname{Verdict}(Q).
}
$$

其中 $\operatorname{Sat}$ 表示某個可觀察搜尋制度中的 operational saturation。

更完整地：

$$
\operatorname{Sat}(\Omega_R(Q))
\not\Rightarrow
\neg Q,
$$

$$
\operatorname{Sat}(\Omega_R(Q))
\not\Rightarrow
Q,
$$

$$
\operatorname{Sat}(\Omega_R(Q))
\not\Rightarrow
\operatorname{MisSpecified}(Q),
$$

$$
\operatorname{Sat}(\Omega_R(Q))
\not\Rightarrow
\operatorname{Independent}_{\mathcal A}(Q).
$$

這些結論需要各自獨立證據。

---

## 3. 十個不可由「沒找到證明」區分的原因

長期無解至少可能由下列假說造成：

$$
H_1:
Q\text{ 為真，但 proof 尚未找到},
$$

$$
H_2:
Q\text{ 為假，但 counterexample 尚未找到},
$$

$$
H_3:
\mathcal M\text{ 方法族不足},
$$

$$
H_4:
\mathcal L\text{ 表示語言不足},
$$

$$
H_5:
B\text{ 資源不足},
$$

$$
H_6:
\text{智能與規劃深度不足},
$$

$$
H_7:
\text{需要尚不存在的新中間理論},
$$

$$
H_8:
\text{framing 存在 mismatch},
$$

$$
H_9:
\text{驗證器或形式庫形成瓶頸},
$$

$$
H_{10}:
Q\text{ 相對背景理論可能獨立}.
$$

觀察：

$$
\operatorname{FailSearch}
$$

通常不能唯一識別其中任何一個。

---

## 4. Evidence ladder

本文建議使用八級證據階梯。

### E0：未成功

只有：

$$
\operatorname{FailSearch}.
$$

結論權限：幾乎只有「目前未找到」。

### E1：去重後的重訪

大量 artifacts 經 quotient 後仍集中於少數 route families。

結論權限：表示 current regime repetition。

### E2：局部飽和

固定窗 novelty、coverage increment 與 high-order metrics 顯示某 basin 邊際新資訊下降。

結論權限：local regime saturation。

### E3：跨表示 robust recurrence

對多種 semantically equivalent representation 都重現。

結論權限：降低「單一寫法」解釋。

### E4：跨方法 independent confluence

不同 method families 與 independent agents 指向相同 obstruction。

結論權限：提高 shared bottleneck hypothesis。

### E5：formal no-go under explicit assumptions

形式證明：

$$
A\Rightarrow\neg C
$$

或某 proof family 在指定條件不可能閉合。

結論權限：只排除明確 family / assumption regime。

### E6：counterexample 或 formal proof

$$
\mathcal A\vdash Q
$$

或：

$$
\mathcal A\vdash\neg Q.
$$

結論權限：直接改變 theorem status。

### E7：independence / undecidability proof

需要明確元理論結果，例如：

$$
\mathcal A\nvdash Q
\quad\text{and}\quad
\mathcal A\nvdash\neg Q.
$$

結論權限：相對指定形式系統的獨立性。

這個階梯不能跳級。

---

## 5. Goedel 不能被當成失敗解釋模板

Goedel incompleteness theorems 是對特定類形式系統的精確元數學結果。它們不是：

> 很難，所以可能不可判定。

真正的 independence claim 需要明確系統、明確句子與明確 proof。

因此本文禁止：

$$
\text{AI cannot prove }Q
\Rightarrow
\text{Goedel}.
$$

這種推論既不增加理解，也會遮蔽真正的 search-regime limitation。

---

## 6. Representation failure 也不能被忽略

2026 年 theorem-proving symmetry research 顯示，語義等價的 rewrite 仍可能造成大幅成功率差異。

因此如果某個 AI 在表示 $\rho_1$ 下失敗：

$$
\operatorname{Fail}(Q,\rho_1),
$$

不能直接推斷：

$$
\operatorname{Fail}(Q,\rho_2)
$$

對所有等價 $\rho_2$ 成立。

只有完成 representation robustness audit，才能把結論從「這個寫法不行」推進到「這個語義類在目前制度中普遍困難」。

---

## 7. Navier--Stokes 案例

Clay 的官方 Navier--Stokes problem 要求處理三維 incompressible Navier--Stokes 的 existence and smoothness 類問題。這是一個正式、公開、長期被數學界研究的問題。

即使某私人 corpus 產生：

$$
203
$$

篇或：

$$
20{,}300
$$

篇 NS 研究 artifact，仍不能由數量推出 Clay formulation 錯誤。

合理的敘述只能是：

$$
\boxed{
\text{某些 corpus-defined proof basins 出現 recurrence 或 saturation evidence。}
}
$$

如果未來真的有人提出新 formulation $Q'$，還需要：

1. 證明 $Q'$ 與原問題的關係；
2. 說明新定義修正了什麼；
3. 給出可驗證 proof / counterexample；
4. 接受獨立專家審查；
5. 若涉及 Millennium Prize，符合正式規則與共識程序。

---

## 8. P vs NP 案例

Clay 對 P vs NP 的核心敘述是：若一個解容易檢查，是否也容易求得？

即使 AI proof search 長期無法決定：

$$
P=NP
$$

或：

$$
P\neq NP,
$$

也不能由失敗推出 complexity classes 的定義錯誤。

可以合理研究的是：

- representation dependence；
- proof-complexity barriers；
- method families；
- known relativization / natural-proofs 類 barrier；
- formal reformulations；
- empirical search-space structure。

但「我找不到 proof」永遠不是「P/NP 問錯」的證明。

---

## 9. 問題 framing 何時才真的可以被批判

framing audit 當然合法，而且很重要。

但要把「值得懷疑」升級成「有錯」，至少應有：

### 9.1 Semantic inconsistency

同一 formulation 混合不相容 truth conditions。

### 9.2 Category mismatch

把某類 predicate 套到不具備該 predicate 所需結構的對象。

### 9.3 Non-equivalent target drift

研究實際證的命題和公開聲稱的命題不同。

### 9.4 Formal reformulation theorem

新 formulation $Q'$ 能嚴格描述與舊 $Q$ 的映射，並解釋舊 route 的 recurring failures。

### 9.5 Independent validation

不依賴原作者單一路徑的外部檢查。

這些都比「大量失敗」強得多。

---

## 10. 飽和訊號的正確輸出格式

一個成熟 proof-space observatory 不應輸出：

```text
The problem is wrong.
```

而應輸出：

```text
Observed:
- basin B17 has low fixed-window novelty;
- 6 independent route families converge on obstruction O4;
- representation sensitivity remains high;
- no formal no-go theorem exists.

Interpretation:
- current regime is locally saturated;
- cause unresolved.

Recommended:
- representation audit;
- method-family expansion;
- formalize O4;
- test basin escape.
```

這就是「診斷」與「判決」的差別。

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $Q$ | 目標命題 |
| $R$ | 搜尋制度 |
| $\operatorname{Sat}$ | operational saturation |
| $H_1,\ldots,H_{10}$ | 長期無解候選原因 |
| E0--E7 | evidence ladder |
| $\mathcal A$ | 明確背景形式系統 |
| $\rho$ | representation |

---

## 12. 依賴與後續

**依賴：** LSI-PSD-01、05、06。  

**後續：** LSI-PSD-12；同時作為全系列的認識論防火牆。

---

## 結論

本系列最重要的一句限制是：

$$
\boxed{
\text{Saturation is evidence about a search regime, not a verdict on mathematical reality.}
}
$$

如果未來證據真的支持「原問題 framing 有錯」，那應該由更好的定義、更清楚的映射與可驗證的數學結果完成，而不是由 AI 累積失敗替它宣判。

---

## 參考文獻

1. Stanford Encyclopedia of Philosophy. *Goedel's Incompleteness Theorems*. Current online archive consulted 2026-08-17.
2. Krzysztof Olejniczak, Radoslav Dimitrov, Xingyue Huang, Bernardo Cuenca Grau, Jinwoo Kim, Ismail Ilkan Ceylan. *What are the Right Symmetries for Formal Theorem Proving?* arXiv:2605.22257, 2026.
3. Clay Mathematics Institute. *Navier--Stokes Equation: Existence and Smoothness*. Official Millennium Prize Problem page and Charles L. Fefferman problem description, accessed 2026-08-17. https://www.claymath.org/millennium/navier-stokes-equation/
4. Clay Mathematics Institute. *P vs NP*. Official Millennium Prize Problem page, accessed 2026-08-17. https://www.claymath.org/millennium/p-vs-np/
5. FATE authors. *FATE: A Formal Benchmark Series for Frontier Algebra of Theorem Proving*. arXiv:2511.02872, 2026 revision.
6. Authors. *From Solvers to Research: Large Language Model-Driven Mathematical Discovery*. arXiv:2607.07779, 2026.


---

# LSI-PSD-11 — 從 Carnot 到 AI：結構性錯誤的科學史與模型論

## From Carnot to AI: A History and Philosophy of Structured Error

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

「錯誤理論仍可產生正確知識」不是 AI 時代才出現的現象。本文以科學史與模型哲學為案例層，檢查本系列的生產性錯置命題。核心案例包括：Carnot 在 caloric theory 背景下建立熱機效率的一般理論；Priestley 在 phlogiston framework 中發現氧氣相關現象，而 Lavoisier 後來重構燃燒理論；以太框架在相對論前史中促成對 length contraction、local time 與 Lorentz transformation 的發展；現代科學則制度化使用 idealized models、minimal models 與 effective field theories。本文不把這些案例粗暴地歸納為「錯誤越多越好」，而將它們分解成四個機制：錯誤框架保留真實局部結構、錯誤暴露可測 discrepancy、理想化移除無關細節、舊框架產生後來可遷移的數學工具。這些機制共同支持較弱但更可靠的結論：scientific fruitfulness 與 literal truth 並非單調同一。

**關鍵詞：** Carnot、caloric theory、phlogiston、ether、idealization、minimal models、effective field theory、scientific history

---

## 1. 歷史案例的用途與危險

科學史案例很容易被濫用。

我們今天知道某理論被替代，就會把它描述成：

$$
\text{wrong theory}
\to
\text{right theory}.
$$

但真正歷史往往更複雜：

- 舊理論包含部分可靠經驗結構；
- 新理論保留舊數學的一部分；
- 實驗不是一次性裁決；
- 同一概念的意義會在轉換中改變。

因此本文不用歷史案例「證明」 PMW，只用來測試：

$$
\boxed{
\text{parent error and descendant value can be separated in real science.}
}
$$

---

## 2. Carnot：錯誤熱本體與正確熱機結構

Carnot 的 1824 工作建立了熱機效率研究的基礎，但他的推理處於 caloric theory 背景中：熱被視為守恆的流體式實體。

按照現代能量觀，這個本體與部分量化推論並不正確；熱可以與功發生能量轉換。

然而 Norton 對 Carnot 的歷史與哲學分析指出，Carnot 的 waterfall analogy 與 reversible-process thinking 仍促成了極具一般性的熱機理論。

這個案例可表示為：

$$
P_{\mathrm{caloric}}
\to
\{
D_{\mathrm{reversibility}},
D_{\mathrm{efficiency}},
D_{\mathrm{cycle}},
\ldots
\}.
$$

後來：

$$
V(P_{\mathrm{caloric}})=0
$$

不妨礙部分 $D_i$ 被重新解釋、修正與保留。

Carnot 案例因此不是「錯誤神奇地變真」，而是：

$$
\boxed{
\text{a false parent ontology contained and generated salvageable structure.}
}
$$

---

## 3. Phlogiston：錯誤解釋框架中的新現象

十八世紀燃燒研究長期由 phlogiston theory 組織。Priestley 在這個框架中研究 gases，並把後來稱為 oxygen 的氣體理解為 dephlogisticated air。

American Chemical Society 的歷史資料明確記錄：Priestley 的發現發生在 phlogiston framework 中；Lavoisier 後來使用相關實驗結果建立新的氧化與燃燒理論，並反對 phlogiston。

因此：

$$
\text{wrong explanatory ontology}
$$

可以和：

$$
\text{good experimental production}
$$

共存。

這是一個重要分離：

$$
\boxed{
\text{discovery competence}
\neq
\text{correct ontology}.
}
$$

對 AI 科學尤其重要，因為 AI 可能提出錯誤 explanation，卻設計出有價值的 experiment 或 auxiliary computation。

---

## 4. Ether：被拋棄的本體與被保留的數學

十九世紀末，光與電磁理論常以 luminiferous ether 作為傳播背景。Michelson--Morley 等結果與相對論的發展使 ether 不再是特殊相對論所需的本體。

但 Lorentz 與同時代工作的數學發展，包括 local time、length contraction 與 Lorentz transformation，並沒有因 ether ontology 被放棄而消失。

歷史路徑更像：

$$
\text{ether problem}
\to
\text{mathematical compensations}
\to
\text{transformation structure}
\to
\text{new spacetime interpretation}.
$$

這是「descendant mathematical structure survives ontology replacement」的典型。

---

## 5. Idealized models：錯誤不是例外，而是方法

Stanford Encyclopedia of Philosophy 對 scientific models 的整理指出，idealization 會刻意簡化或扭曲複雜系統，使其更 tractable 或 understandable。

常見例子包括：

- frictionless plane；
- point mass；
- isolated system；
- perfectly rational agent；
- perfect equilibrium。

這些模型不按字面描述世界，卻是正常科學方法。

因此現代科學早已制度化承認：

$$
\text{literal fidelity}<1
$$

不必然使：

$$
\text{scientific utility}=0.
$$

---

## 6. Minimal models：少一點真實細節，可能多一點結構

Batterman 與 Rice 的 minimal model account 強調，某些模型的解釋力來自揭示不同系統之間的 universality，而不是最大限度重建每個微觀機制。

如果不同微觀系統都落入同一宏觀 class，增加所有細節可能反而遮蔽：

$$
\text{relevant invariant}.
$$

所以：

$$
\boxed{
\text{more detail}
\not\Rightarrow
\text{more explanation}.
}
$$

這與本系列的 semantic quotient 非常接近：研究系統必須知道哪些差異應保留，哪些只是對目標無關的自由度。

---

## 7. Effective theories：非最基本仍可最適用

Effective field theory 的核心特徵之一是明確承認尺度與適用域。它不必宣稱自己是最 fundamental 的最終理論，卻可以在特定 energy scale 提供非常有效的描述。

近期 productive idealization 與 EFT 哲學研究進一步把問題指向：

$$
\text{fundamentality},
\text{fidelity},
\text{understanding},
\text{utility}
$$

之間的非單調關係。

這使「最底層理論一定最適合所有研究任務」成為需要證明、而不是可以偷渡的前提。

---

## 8. 四種生產性機制

從上述案例，本文整理四種不同機制。

### M1：Local truth retention

父理論錯，但保留某些局部正確關係。

### M2：Discrepancy exposure

模型的失效位置本身暴露 missing mechanism。

### M3：Irrelevance stripping

理想化刪除對目標不重要的細節，使 invariant 更清楚。

### M4：Tool migration

舊框架中發展的數學、儀器、實驗設計遷移到新框架。

這四者都可能增加 descendant value，但邏輯機制不同。

---

## 9. AI 時代新增了什麼

歷史科學的 productive error 通常需要多年甚至數十年才能被重構。

AI 長程研究第一次可能讓我們保存：

$$
\text{generation}
+
\text{route}
+
\text{failure}
+
\text{revision}
+
\text{descendant transfer}
$$

的高密度縱向資料。

這意味著「錯誤如何生知識」可能從歷史重建問題，變成部分可觀測的 prospective science。

例如 LISDD 類方法已經把：

$$
\text{where model fails}
$$

轉成：

$$
\text{which symbolic mechanism is missing}.
$$

Proof-space observatory 則可以嘗試把：

$$
\text{where proof routes fail}
$$

轉成：

$$
\text{which obstruction family or representation assumption is shared}.
$$

---

## 10. 歷史案例不能證明 NS 或 P vs NP framing 錯

這是本文最重要的反濫用條款。

Carnot、phlogiston、ether 告訴我們：

$$
\exists P:
\neg V(P)
\land
R_S(P)>0.
$$

它們不告訴我們：

$$
\forall\text{ hard problem }Q,
\operatorname{Hard}(Q)
\Rightarrow
\operatorname{MisSpecified}(Q).
$$

因此科學史只能支持「可能性與機制」，不能替代對具體未解問題的數學分析。

---

## 11. 符號表

| 符號 | 意義 |
|---|---|
| $P_{\mathrm{caloric}}$ | caloric parent framework |
| $D_i$ | descendant structures |
| M1--M4 | 四種生產性機制 |
| $V(P)$ | parent validity |
| $R_S(P)$ | salvage ratio |

---

## 12. 依賴與後續

**依賴：** LSI-PSD-07 至 09。  

**後續：** LSI-PSD-12。

---

## 結論

科學史最穩健的教訓不是「錯誤是好的」，而是：

$$
\boxed{
\text{Scientific fruitfulness and literal truth are not the same variable.}
}
$$

一個成熟的 AI 科學系統因此不能只保存最後勝出的理論；它也應保存被替代框架中仍可遷移的數學、實驗、工具與 failure structure。這正是 proof-space observatory 下一步的資料任務。

---

## 參考文獻

1. John D. Norton. *How Analogy Helped Create the New Science of Thermodynamics*. Synthese 200:269, 2022. DOI: 10.1007/s11229-022-03708-9.
2. American Chemical Society. *Joseph Priestley and the Discovery of Oxygen*. National Historic Chemical Landmark.
3. American Chemical Society. *The Chemical Revolution of Antoine-Laurent Lavoisier*. National Historic Chemical Landmark.
4. Rafael Ferraro. *From aether theory to Special Relativity*. arXiv:1302.6965, 2013.
5. Roman Frigg and Stephan Hartmann. *Models in Science*. Stanford Encyclopedia of Philosophy, current online edition, accessed 2026-08-17.
6. Robert W. Batterman and Collin C. Rice. *Minimal Model Explanations*. Philosophy of Science 81(3), 2014.
7. Karla Weingarten. *Productive Idealizations for Scientific Understanding*. PhilSci-Archive preprint, 2026.
8. Yifan Wang. *Where Is My Physics Wrong? Localized and Identifiable Discovery of Model Discrepancy*. arXiv:2606.23215, 2026.


---

# LSI-PSD-12 — AI 證明空間觀測站：從 NS-203 到文明級研究記憶

## AI Proof-Space Observatory: From the NS-203 Corpus to Civilization-Scale Research Memory

**系列：** 邏輯空間積分與證明空間動力學 / Logic-Space Integration and Proof-Space Dynamics  
**系列代碼：** LSI-PSD  
**版本：** v1.0  
**日期：** 2026-08-17  
**理論發起：** Neo.K  
**協作整理：** Aletheia / GPT-5.6 Sol  
**文件狀態：** 正式研究稿 / v1.0  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** `$...$` 與 `$$...$$`

> **研究地位聲明**：本文屬方法論、數學哲學、AI 證明研究與研究工程之理論建模。除非文中明確標記為已知定理並給出來源，本文提出的「命題」「原則」「指標」「窗口」均應視為工作定義、可檢驗假說或研究設計，而不是對 Navier--Stokes、P vs NP 或其他未解問題的證明、反證或不可判定性證明。


## 摘要

前十一篇建立了 proof-space measurement 的概念層：搜尋制度、語義商空間、邏輯空間積分、高階採樣、局部飽和、obstruction confluence、真理—生成性反轉、生產性錯置與非結論原則。本文將它們整合成可實作的 AI Proof-Space Observatory 架構。觀測站的基本單位不再是「論文」，而是 Claim、Assumption、Lemma、Route、Obstruction、Evidence 與 Status。本文提出 canonical research event schema、route graph、obstruction registry、sampling-order classifier、novelty estimator、coverage estimator、epistemic firewall 與 recommendation engine。NS Proof-Space Sampling Observatory v0.1 被用作第一個原型案例：保守分類得到 203 份 NS paper-like artifacts，並觀察到 84/107/10/2 的 $T_1/T_2/T_3/T_X$ heuristic distribution，以及局部 confluence 卻沒有全 corpus novelty collapse 的情況。本文把下一版工作明確化為 claim-level extraction 與 formal evidence attachment。最終目標不是自動宣告未解問題已被解決，而是讓長程 AI 研究第一次擁有可重放、可去重、可路由、可審計的文明級研究記憶。

**關鍵詞：** proof-space observatory、research memory、claim graph、obstruction registry、NS-203、AI science、long-horizon agents

---

## 1. 為什麼需要觀測站

當研究量只有十篇時，人可以靠記憶理解：

- 哪條路試過；
- 哪個 lemma 出現過；
- 哪個 obstruction 已知；
- 哪篇只是重寫。

當研究量進入：

$$
10^2,\quad10^3,\quad10^4
$$

級別後，這種人腦索引會崩潰。

此時問題不再是「AI 能不能生成」，而是：

$$
\boxed{
\text{文明能不能記得自己已經研究過什麼。}
}
$$

Proof-Space Observatory 就是對這個問題的工程回答。

---

## 2. 最小資料單位

每個研究事件應拆成：

$$
E_i
=
(
C_i,
A_i,
L_i,
R_i,
O_i,
V_i,
S_i
).
$$

其中：

- $C_i$：Claim；
- $A_i$：Assumptions；
- $L_i$：Lemmas；
- $R_i$：Route；
- $O_i$：Obstruction；
- $V_i$：Verification / Evidence；
- $S_i$：Status。

論文、對話、程式、Lean file、實驗結果都只是 container。

真正 canonical 的研究記憶是這些結構化事件與原始 source 的雙向鏈接。

---

## 3. Canonical event schema

建議 JSON / YAML 層至少包含：

```yaml
event_id:
source_artifact:
source_hash:
target_problem:
claim:
claim_type:
domain:
quantifiers:
assumptions:
representation:
dependencies:
lemmas:
route_family:
obstruction_id:
evidence:
  formal:
  computational:
  empirical:
  literature:
status:
revisit_of:
supersedes:
equivalent_candidates:
transfer_targets:
sampling_order:
confidence:
created_at:
```

其中 source hash 是必要欄位，確保分析圖不取代 canonical source。

---

## 4. 雙層儲存

觀測站應保留：

### 4.1 Canonical source layer

原始 UTF-8 Markdown、Lean source、程式、數據、diff、checksum。

### 4.2 Derived graph layer

embedding、summary、claim graph、route graph、cluster、metric。

必須維持：

$$
\boxed{
\text{Derived Representation}
\neq
\text{Canonical Source}.
}
$$

這和語義商空間的不可過早商化原則一致。

---

## 5. 系統模組

### Module A：Source Ingest

讀入 paper、proof、code、data。

### Module B：Claim Extractor

抽取：

$$
C_i,A_i,L_i.
$$

### Module C：Semantic Quotient Engine

建立 candidate equivalence edges：

$$
\sim_{\mathrm{repr}},
\sim_{\mathrm{prop}},
\sim_{\mathrm{route}},
\sim_{\mathrm{obs}}.
$$

### Module D：Route Graph

建立 proof dependencies 與 transition history。

### Module E：Obstruction Registry

維護 canonical obstruction IDs。

### Module F：Sampling-Order Classifier

估計：

$$
T_1,T_2,T_3,T_X.
$$

### Module G：Coverage and Novelty

計算：

$$
I_N(A),
\quad
\Delta I_N(A),
\quad
\nu_k(N).
$$

### Module H：Epistemic Firewall

限制輸出結論權限。

### Module I：Research Router

根據 confluence、saturation、representation sensitivity 決定下一步算力配置。

---

## 6. NS-203 v0.1 實例

對本次提供的 NS archive，v0.1 recursive scan 得到：

$$
1109
$$

個 file instances，

$$
593
$$

個 Markdown instances，

$$
565
$$

個 exact-hash unique Markdown artifacts。

保守排除 README、CHANGELOG、checkpoint、roadmap、handoff、audit 等後，得到：

$$
\boxed{
203\ \text{NS paper-like artifacts}.
}
$$

另有：

$$
27
$$

份「空間域證明包圍」paper-like artifacts。

這是 corpus instrumentation 結果，不是數學 theorem。

---

## 7. Sampling-order prototype

v0.1 heuristic 得到：

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

這些 tier 的意義是：

$$
T_1:
\text{state / route sampling},
$$

$$
T_2:
\text{revisit / transition},
$$

$$
T_3:
\text{relation / confluence},
$$

$$
T_X:
\text{explicit family-level or higher/all-order evidence}.
$$

它們不是已證明的數學階數。

---

## 8. Novelty robustness 結果

累積 nearest-neighbor novelty 後期下降，但這個指標受到比較池增大的 bias。

固定窗 $W=20$ 後：

$$
\bar\nu_{\mathrm{Q2}}=0.5425,
$$

$$
\bar\nu_{\mathrm{Q4}}=0.5781.
$$

差值：

$$
\Delta\bar\nu=0.0356.
$$

500 次 random reorder baseline 下，該變化沒有支持 global novelty collapse。

所以 v0.1 的合理結論是：

$$
\boxed{
\text{localized higher-order resampling exists, global exhaustion is not established.}
}
$$

這個負結果非常重要，因為它證明 observatory 不應只尋找支持原始假說的數字。

---

## 9. 第一版 confluence zones

v0.1 controlled concept families 中，跨系列最明顯的區域包括：

- carrier-supplier；
- rigidity-closure；
- obstruction-gap-defect；
- recurrence-return；
- criticality；
- spectral-frequency。

這些只是 routing signals。

下一步必須把：

$$
\text{concept family}
$$

下鑽為：

$$
\text{canonical claim / obstruction ID}.
$$

否則「大家都談 criticality」不等於「大家證明中撞到同一個障礙」。

---

## 10. v0.2：Claim-Level Observatory

下一版最重要的升級是把 paper node 拆解。

### 10.1 Claim graph

$$
C_i\to C_j.
$$

記錄 implication、dependency、refinement。

### 10.2 Lemma graph

$$
L_i\to L_j.
$$

追蹤 lemma 重用與 transfer。

### 10.3 Obstruction graph

$$
R_i\to O_j.
$$

計算：

$$
\kappa(O_j),
\quad
d(O_j),
\quad
P_N(O_j),
\quad
Y(O_j).
$$

### 10.4 Formal evidence attachment

若有 Lean / Coq / Isabelle proof，直接掛到 claim node。

若只有 numerical evidence，必須標記：

$$
\text{numerical}
\neq
\text{formal proof}.
$$

---

## 11. 與現代 formal mathematics infrastructure 的整合

TheoremGraph 類工作顯示 formal theorem dependency graph 已可大規模抽取；theorem semantic search 也已進入百萬級 corpus。這意味著 observatory 可以使用既有基礎設施：

$$
\text{formal declarations}
+
\text{informal papers}
+
\text{semantic retrieval}
+
\text{proof verification}.
$$

而不是另造一個封閉知識庫。

---

## 12. Research router

觀測站最終不只是 dashboard，而應影響下一輪 research policy。

輸入：

$$
X_t
=
(
\nu_k,
I_N,
\kappa,
P_N,
Y,
\operatorname{RSI}
).
$$

路由器輸出：

$$
a_{t+1}
=
\pi(X_t).
$$

可能動作：

- continue local search；
- diversify representation；
- formalize obstruction；
- search transfer theorem；
- run counterexample search；
- increase compute；
- switch prover；
- pause basin；
- open framing audit。

重要的是：

$$
\pi
$$

不能輸出「declare theorem false」這類超越證據層級的行動。

---

## 13. 文明級研究記憶

如果多個 AI、研究者與機構長期共享：

$$
\mathcal M_t
=
\text{audited research memory at time }t,
$$

則新研究不必每次從：

$$
\emptyset
$$

開始。

更新可以寫成：

$$
\mathcal M_{t+1}
=
\operatorname{Validate}
\left(
\mathcal M_t
\cup
\Delta\mathcal R_t
\right).
$$

其中 $\Delta\mathcal R_t$ 是新 research events。

長期目標不是讓 AI「記得所有文本」，而是：

$$
\boxed{
\text{remember enough structure to avoid rediscovering the same dead ends blindly.}
}
$$

---

## 14. 成熟度階段

### Level 0：Archive

只保存文件。

### Level 1：Searchable Corpus

可全文與 semantic search。

### Level 2：Claim Graph

可看 dependencies。

### Level 3：Proof Route Graph

可看 route recurrence。

### Level 4：Obstruction Observatory

可看 confluence、saturation、escape。

### Level 5：Adaptive Research Router

研究策略由觀測資料動態調整。

### Level 6：Cross-Domain Transfer Memory

可把某問題產生的 lemmas、no-go 與 proof patterns 遷移到其他 domain。

---

## 15. 符號表

| 符號 | 意義 |
|---|---|
| $E_i$ | canonical research event |
| $C_i$ | claim |
| $A_i$ | assumption set |
| $L_i$ | lemma set |
| $R_i$ | route |
| $O_i$ | obstruction |
| $V_i$ | verification evidence |
| $S_i$ | status |
| $X_t$ | observatory state vector |
| $\pi$ | research routing policy |
| $\mathcal M_t$ | civilization-scale research memory |

---


## 16. 依賴

**依賴：** LSI-PSD-01 至 11，以及 `NS Proof-Space Sampling Observatory v0.1` corpus instrumentation。  

**後續工程：** Claim-Level Observatory v0.2、formal evidence attachment、cross-domain transfer memory。

---

## 17. 全系列總結

十二篇的核心鏈條可以壓縮為：

$$
\text{search regime}
\to
\text{semantic quotient}
\to
\text{logic-space integration}
\to
\text{higher-order sampling}
\to
\text{local saturation}
\to
\text{obstruction confluence}
\to
\text{generativity analysis}
\to
\text{productive mis-specification}
\to
\text{non-conclusion firewall}
\to
\text{proof-space observatory}.
$$

真正的目標不是讓 AI 更有自信地宣布答案，而是讓研究系統更知道：

$$
\boxed{
\text{what it has tried, what it has learned, what it has ruled out, and what it still does not know.}
}
$$

---

## 結論

NS-203 corpus 目前最重要的價值，不是它能否被包裝成 Navier--Stokes proof，而是它已經足夠大，讓「AI 長程數學研究如何形成高階重訪、局部飽和與障礙匯流」第一次具有可觀察原型。

Proof-Space Observatory 的終局不是：

$$
\text{automatic certainty}.
$$

而是：

$$
\boxed{
\text{auditable continuity of scientific reasoning at scales larger than any single conversation or paper.}
}
$$

---

## 參考文獻

1. EveMissLab internal research artifact. *NS Proof-Space Sampling Observatory v0.1*. 2026-08-17. Corpus instrumentation over the supplied NS archive; not a Navier--Stokes proof.
2. S. Kurgan et al. *TheoremGraph: Bridging Formal and Informal Mathematics*. arXiv:2606.25363, 2026.
3. Authors. *Semantic Search over 9 Million Mathematical Theorems*. arXiv:2602.05216, 2026.
4. Krzysztof Olejniczak, Radoslav Dimitrov, Xingyue Huang, Bernardo Cuenca Grau, Jinwoo Kim, Ismail Ilkan Ceylan. *What are the Right Symmetries for Formal Theorem Proving?* arXiv:2605.22257, 2026.
5. HERMES authors. *HERMES: Towards Efficient and Verifiable Mathematical Reasoning*. arXiv:2511.18760, revised 2026.
6. Authors. *A Minimal Agent for Automated Theorem Proving*. arXiv:2602.24273, 2026.
7. Authors. *From Solvers to Research: Large Language Model-Driven Mathematical Discovery*. arXiv:2607.07779, 2026.
8. Clay Mathematics Institute. *Navier--Stokes Equation: Existence and Smoothness*. Official Millennium Prize Problem page and Charles L. Fefferman problem description, accessed 2026-08-17. https://www.claymath.org/millennium/navier-stokes-equation/
9. Clay Mathematics Institute. *P vs NP*. Official Millennium Prize Problem page, accessed 2026-08-17. https://www.claymath.org/millennium/p-vs-np/


---

