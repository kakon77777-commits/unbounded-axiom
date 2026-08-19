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
