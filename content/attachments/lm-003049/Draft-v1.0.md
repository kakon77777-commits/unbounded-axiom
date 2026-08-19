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
