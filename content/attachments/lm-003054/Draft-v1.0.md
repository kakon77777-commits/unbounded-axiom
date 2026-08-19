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
