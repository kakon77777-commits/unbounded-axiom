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
