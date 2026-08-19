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
