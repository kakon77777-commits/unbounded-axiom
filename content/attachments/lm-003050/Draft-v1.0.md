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
