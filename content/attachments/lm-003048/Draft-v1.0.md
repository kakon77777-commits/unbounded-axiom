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
