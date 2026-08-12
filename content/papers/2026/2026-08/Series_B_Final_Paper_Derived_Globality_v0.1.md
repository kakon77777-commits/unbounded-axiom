# Series B / Final Paper

## 關係耦合、類全域狀態與觀察者網路：從局部關係數學到可工程化的 Derived Globality

**版本**：v0.1  
**日期**：2026-08-11  
**系列**：Series B — Observer, Local Relations, Noncommutativity, Globality, and Conservation

---

## 摘要

本文對 Series B 的理論與計算實驗作階段性收束。Series B 的核心問題不是證明「世界本體必然以關係先於物件」，也不是假定存在一個可被任何實體直接取得的上帝視角全域狀態，而是研究一個較弱、但可形式化且可工程化的命題：

> 多個有限、局部、嵌入式觀察者所持有的關係資訊，是否能在保留局部差異、路徑依賴、觀察者轉換、不可辨識性與不確定性的前提下，耦合成可操作的類全域狀態？

本文回答：在本文建立並測試的有限維、線性與非線性經典模型族中，答案是肯定的。類全域狀態可由局部觀察、時間歷史、觀察者通信、物理 transport、descent/coherence、robust consistency、calibration 與 active measurement 共同導出。然而，此類 globality 必須被理解為 **derived globality / network-globality**，而非 ontological global truth。

本文並提出一個收束性的工程形式：

\[
G_{\mathrm{usable}}
=
(\hat S,\mathcal U,\mathcal C,\mathcal P),
\]

其中 \(\hat S\) 是目前重建的類全域狀態，\(\mathcal U\) 是尚未消除的不確定性與等價類，\(\mathcal C\) 是跨觀察者一致性結構，\(\mathcal P\) 是證據來源與轉換鏈。若觀察網路存在不可見 gauge group \(\mathcal G_{\rm inv}\)，真正可辨識的 global object 應寫成

\[
[\hat S]_{\mathcal G_{\rm inv}}
\in
\mathcal S/\mathcal G_{\rm inv},
\]

而非唯一裸狀態 \(\hat S\)。

本文最後區分三個層次：已可工程化的 observer-runtime、已有穩定數學骨架的 Series B 方法論，以及仍屬條件性哲學／物理命題的本體論主張。

---

## 1. 問題設定

令真實或模型中的世界狀態空間為

\[
\mathcal S.
\]

觀察者集合為

\[
\mathcal O=\{O_1,\ldots,O_n\}.
\]

第 \(i\) 個觀察者不直接取得整個 \(S\in\mathcal S\)，而透過局部觀察通道

\[
A_i:\mathcal S\to\mathcal D_i
\]

取得

\[
y_i=A_i(S).
\]

在更一般的非線性與隨機情況：

\[
y_{i,t}
=
h_i(S_t)+\epsilon_{i,t}.
\]

因此單一觀察者實際可區分的不是整個 \(\mathcal S\)，而是其觀察等價類：

\[
S_a\sim_i S_b
\iff
A_i(S_a)=A_i(S_b).
\]

單體 observer 的有效狀態空間可寫成

\[
\mathcal S/\sim_i.
\]

Series B 的工程問題不是要求某個 \(O_i\) 成為全知觀察者，而是研究聯合觀察是否能縮小這些等價類：

\[
[S]_{\mathcal O}
=
\bigcap_i [S]_{\sim_i}.
\]

若新的 observer、歷史資料或 measurement 被加入，理想上有

\[
[S]_{\mathcal O'}
\subseteq
[S]_{\mathcal O}.
\]

這就是本文所稱的 **derived globality**：global description 不是預先假定，而是由局部 evidence 所允許的可能世界集合逐步收斂而成。

---

## 2. 從局部順序到關係結構

Series B 最初從非交換順序開始。

對映射 \(f,g\) 定義局部非交換缺陷

\[
\delta_{f,g}(x)
=
d(f(g(x)),g(f(x))).
\]

若路徑

\[
\gamma=(r_1,\ldots,r_n),
\]

則有序組合

\[
F_\gamma
=
r_n\circ\cdots\circ r_1.
\]

兩條由相同局部關係但不同順序構成的路徑，可比較

\[
\Delta_x(\gamma,\eta)
=
d(F_\gamma(x),F_\eta(x)).
\]

因此關係不只是「有哪些 edge」，還包括：

- 可否組合；
- 組合順序；
- 路徑歷史；
- transport 後的狀態差；
- 閉路後是否留下 relational memory。

對閉路 \(\ell:x\to x\)，定義 holonomy

\[
H_x(\ell)=T_\ell.
\]

即使位置回到 \(x\)，仍可能

\[
H_x(\ell)\neq I.
\]

這說明：

\[
\text{base-state closure}
\neq
\text{relational-state closure}.
\]

---

## 3. 從局部不一致到全域阻塞

局部 residual 並不自動代表 global obstruction。

若 cover \(\{U_i\}\) 的 overlap 上有 residual

\[
c_{ij},
\]

必須先滿足適當的 cocycle compatibility，才可形成

\[
c\in Z^1.
\]

而真正的全域 obstruction 是 cohomology class

\[
[c]\in H^1,
\]

不是單純

\[
c\neq0.
\]

因為若

\[
c=db,
\]

則

\[
[c]=0.
\]

因此 Series B 的基本警告是：

\[
\boxed{
\text{local disagreement}
\not\Rightarrow
\text{global obstruction}.
}
\]

同樣：

\[
\boxed{
\text{noncommutativity}
\not\Rightarrow
\text{nonseparability}.
}
\]

這些區分避免把所有局部異常都過度解釋成新的全域物理結構。

---

## 4. Globality 的三種不同意義

Series B 必須嚴格區分：

### 4.1 Global structure

局部 observer、transition、transport 與 overlap data 可被 coherent 地黏合成某個整體 relational object。

### 4.2 Global state

存在一個完整 state

\[
S\in\mathcal S.
\]

### 4.3 Global access

某個 observer 能唯一、有效地重建該 state。

三者不能混同：

\[
\boxed{
\text{global structure}
\neq
\text{global state}
\neq
\text{global access}.
}
\]

同樣地：

\[
\boxed{
\text{不存在}
\neq
\text{不知道}
\neq
\text{算不到}.
}
\]

---

## 5. Collective Reconstruction

若每個局部 observer 在線性情況下具有

\[
y_i=A_i S,
\]

即使

\[
\operatorname{rank}(A_i)<\dim\mathcal S
\qquad\forall i,
\]

聯合觀察映射

\[
A_{\mathcal O}
=
\begin{bmatrix}
A_1\\
A_2\\
\vdots\\
A_n
\end{bmatrix}
\]

仍可能滿足

\[
\operatorname{rank}(A_{\mathcal O})
=
\dim\mathcal S.
\]

因此：

\[
\boxed{
\text{individual incompleteness}
\not\Rightarrow
\text{collective incompleteness}.
}
\]

Series B 的計算實驗已在二維諧振子模型中實現此情況：每個 observer 單獨只有部分狀態資訊，但若干 observer 聯合後可以重建完整四維 state。

---

## 6. History 作為第二種 Globality Generator

對動力系統

\[
S_t=\Phi_tS_0,
\]

單一 observer 的多時間觀察形成

\[
\mathcal O_H
=
\begin{bmatrix}
A\Phi_{t_1}\\
A\Phi_{t_2}\\
\vdots
\end{bmatrix}.
\]

即使瞬時

\[
\operatorname{rank}(A)<\dim\mathcal S,
\]

仍可能有

\[
\operatorname{rank}(\mathcal O_H)
=
\dim\mathcal S.
\]

所以：

\[
\boxed{
\text{instantaneously inaccessible}
\neq
\text{historically inaccessible}.
}
\]

通信與記憶因此成為兩種不同的 globality generator：

\[
\text{communication across observers}
\]

與

\[
\text{history across time}.
\]

---

## 7. Nonlinear、Stochastic 與 Robust Reconstruction

Series B 不依賴線性 observation。

一般情況可寫成

\[
y_{i,t}
=
h_i(\Phi_t(S_0;\theta))
+
\epsilon_{i,t}.
\]

類全域重建因此成為 robust nonlinear inverse problem：

\[
(\hat S_0,\hat\theta)
=
\arg\min_{S,\theta}
\sum_{i,t}
\rho_i
\left(
h_i(\Phi_t(S;\theta))-y_{i,t}
\right).
\]

計算實驗顯示：

1. 單一 nonlinear observer 可產生真正 many-to-one ambiguity；
2. 多 observer 與 history 可縮小甚至打破多解；
3. robust loss 可降低 corrupted channel 對 global estimate 的污染；
4. 在 shared law 已重新估計後，local residual localization 可協助找出 observer defect。

因此 anomaly 至少要分成：

\[
\Delta
=
(
\Delta_S,
\Delta_L,
\Delta_O
),
\]

分別表示：

- state mismatch；
- shared law mismatch；
- observer/channel mismatch。

---

## 8. Calibration、Gauge 與可辨識的全域物件

若 state 與 observer calibration 同時未知，可能出現精確 gauge freedom。

例如

\[
y_i=g_iq_i(S),
\]

且

\[
q_i(\lambda S)
=
\lambda^2q_i(S),
\]

則變換

\[
S\mapsto\lambda S,
\qquad
g_i\mapsto\frac{g_i}{\lambda^2}
\]

保持所有 observations 不變。

此時不存在足以從目前 evidence 唯一決定的裸狀態 \(S\)。

更一般地，令

\[
\mathcal G_{\rm inv}
=
\{
g:\,
A_i(gS)=A_i(S),\ \forall i
\}.
\]

則 observer network 真正可識別的是

\[
\boxed{
[S]_{\mathcal G_{\rm inv}}
\in
\mathcal S/\mathcal G_{\rm inv}.
}
\]

因此本文提出：

> **Globality is only uniquely meaningful modulo observer-invisible transformations.**

也即：

> **全域性只能在觀察者不可見變換的商空間上被唯一定義。**

這也說明 local Fisher/Jacobian full rank 並不保證 global uniqueness；離散 branch 或 global gauge 仍可能存在。

---

## 9. Active Observer Design

如果 ambiguity 是由 observation channel 本身造成，單純「推理得更努力」無法產生被測量抹掉的資訊。

因此應改變 observation。

若目前 global hypothesis set 為

\[
\mathcal H=\{S_1,\ldots,S_k\},
\]

對候選 measurement \(m\) 定義 separation utility

\[
U(m)
=
\operatorname{Sep}
\left(
\{h_m(S_j)\}_{j=1}^k
\right).
\]

主動選擇

\[
m^\star
=
\arg\max_m U(m)
\]

後，可望得到

\[
[S]_{\mathcal O+m^\star}
\subsetneq
[S]_{\mathcal O}.
\]

Series B 因而從 passive reconstruction 進一步成為：

\[
\text{infer}
\to
\text{identify ambiguity}
\to
\text{choose observation}
\to
\text{refine}.
\]

---

## 10. 多重嵌套 Observer Tower

更一般的系統可具有

\[
\mathcal W
\to
O_0
\to
O_1
\to
\cdots
\to
O_n
\to
G.
\]

其中 \(O_0\) 最接近實際物理 interaction；後續各層可能加入 interpretation、compression、cross-check 與 synthesis。

這裡必須區分：

- measurement authority；
- interpretation authority；
- synthesis authority。

Global AI 並不因為整合範圍最大，就自動成為 truth oracle。

相反地，Global AI 應理解為

\[
G_{\mathcal O},
\]

即相對於目前 observer network \(\mathcal O\) 的 network-global estimator。

加入新 observer 後，

\[
G_{\mathcal O\cup\{O_{n+1}\}}
\]

可以不同於

\[
G_{\mathcal O}.
\]

因此：

\[
\boxed{
\text{network-global}
\neq
\text{ontologically global}.
}
\]

---

## 11. Sandbox Truth 與真實世界的界線

所有本文計算實驗都具有一個現實世界通常沒有的特權：

\[
S_{\rm true}
\]

被 simulator 保存，可在實驗結束後用來評分 reconstruction。

這使我們能量化：

- state error；
- law error；
- observer fault detection；
- recognition delay；
- classification accuracy。

但真實科學系統通常不能直接查詢

\[
S_{\rm true}.
\]

因此 sandbox 中的「誰比較正確」只能理解為相對於已知 simulation label 的 benchmark。

真實部署時，Global AI 只能維護 provisional world model：

\[
G_t
=
(
\hat{\mathcal W}_t,
\mathcal U_t,
\mathcal A_t,
\mathcal P_t
),
\]

其中包含：

- 目前最佳世界模型；
- 未解不確定性；
- unresolved anomalies；
- provenance。

所以本文採用：

\[
\boxed{
\text{Global consensus is an epistemic state,
not an ontological certificate.}
}
\]

並進一步允許：

\[
\boxed{
\text{Frontier truth can precede global recognition.}
}
\]

即某個前線 observation 可能首先接觸到後來被證實的重要現象，但當時的 global model 合理地將它視為 sensor fault、noise 或 outlier。

此命題在現實世界中不能靠 sandbox oracle 直接證成；它在本文中被保留為 epistemic / philosophical research direction。

---

## 12. 工程化收束：Usable Global State

本文最終不要求

\[
G_{\rm true}.
\]

工程上真正需要的是

\[
\boxed{
G_{\rm usable}
=
(
\hat S,
\mathcal U,
\mathcal C,
\mathcal P
).
}
\]

其中：

### \(\hat S\)

目前的 provisional global reconstruction。

### \(\mathcal U\)

uncertainty、remaining gauge、hypothesis branches 與未解等價類。

### \(\mathcal C\)

observer consistency、transport consistency、descent/coherence、conservation residual。

### \(\mathcal P\)

每項 evidence 的來源、observer path、calibration、history 與 transformation provenance。

這個結構不需要宣稱「已取得宇宙真正全域狀態」，就足以支援：

- distributed sensing；
- scientific AI；
- multi-agent experimental systems；
- anomaly localization；
- adaptive observation；
- future quantum measurement orchestration。

---

## 13. 計算驗證摘要

Series B 已完成的 sandbox / MVP 類型包括：

1. 非交換缺陷與 adjacent-swap propagation；
2. \(H^1\)-style global obstruction；
3. global nonexistence vs observer inaccessibility；
4. holonomy 與 conserved invariant 共存；
5. observer covariance 與 relative holonomy；
6. observer-network descent/coherence；
7. conservation hierarchy；
8. classical SO(3)、sphere parallel transport、Lorentz/Wigner stress tests；
9. Global AI vs Embedded AI harmonic-oscillator MVP；
10. collective observer reconstruction；
11. noisy synchronization；
12. observer-only emergent global reconstruction；
13. nonlinear stochastic reconstruction；
14. joint state-law inference；
15. joint state-law-calibration inference；
16. exact observer-invisible gauge；
17. active measurement gauge breaking；
18. nested observer tower governance。

這些結果共同支持一個有限但足夠工程化的結論：

\[
\boxed{
\text{local relational descriptions can be coupled into a usable derived global state}
}
\]

在本文測試的模型族中成立。

它們不證明宇宙本體必然是 relational，也不證明不存在更強的 global ontology。

---

## 14. 與既有數學與工程的關係

本文不主張以下元件本身為新發明：

- noncommutativity；
- sheaf/cohomological obstruction；
- path transport / holonomy；
- distributed state estimation；
- observability；
- robust estimation；
- calibration / gauge freedom；
- adaptive experiment design；
- quantum tomography。

Series B 的主要價值是將這些成熟結構放入同一個 observer-centered diagnostic pipeline：

\[
\boxed{
\delta
\to
[c]
\to
A_O
\to
H
\to
D_{OP}
\to
K_{ijk}
\to
C
\to
[\hat S]_{\mathcal G}
\to
G_{\rm usable}.
}
\]

並將 Global AI 明確降格為 derived/network-relative synthesis layer，而非預設的 God-view observer。

---

## 15. 理論邊界

本文目前不證明：

1. 真實宇宙不存在 global state；
2. 關係在本體論上必然先於物件；
3. 任意 observer network 都可重建 global structure；
4. 任意 local consistency 都可有效 descent；
5. \(H^1=0\) 足以保證所有 contextual/global compatibility；
6. Global AI 永遠劣於 frontier observer；
7. frontier observer 的直接敘述必然是真實；
8. classical sandbox 結果可直接外推為量子定理。

這些必須維持為額外條件、開放問題或未來研究。

---

## 16. 結論

Series B 的最低成功條件可以表述為：

> 若一套關係原生的觀察者數學能在不抹除局部差異的前提下，使多個局部 observer 經由 transport、history、communication、coherence、calibration 與 active measurement 耦合出一個可更新、可追溯、可診斷的類全域狀態，則該數學已足以成為工程可用的 observer framework。

目前的理論與計算實驗已達到此最低條件。

因此 Series B 在此階段不必繼續追求無限制的概念擴張。後續工作可自然分為兩條：

\[
\boxed{\text{Formalization}}
\]

以及

\[
\boxed{\text{Application}}.
\]

Formalization 將進一步統一 category/sheaf/groupoid/gauge/descent 語言並明確給出定理條件；Application 則可把目前 classical observer channel

\[
h_i(S)
\]

逐步替換為更實際的 measurement/channel formalism，最終進入 quantum measurement、quantum control 與 AI-assisted scientific observation。

Series B 因而由「關係是否能成為世界描述的起點」收斂為一個更具體的工程命題：

\[
\boxed{
\textbf{Globality need not be assumed; it can be reconstructed from relations.}
}
\]

但這個 globality 應始終理解為：

\[
\boxed{
\textbf{derived, provisional, gauge-aware, observer-relative, and revisable.}
}
\]

---

## 參考文獻定位

[R1] Abramsky, S.; Brandenburger, A. *The Sheaf-Theoretic Structure of Non-Locality and Contextuality*. New Journal of Physics 13 (2011). arXiv:1102.0264.

[R2] Abramsky, S.; Barbosa, R. S.; Kishida, K.; Lal, R.; Mansfield, S. *Contextuality, Cohomology and Paradox*. arXiv:1502.03097.

[R3] Wang, S.; Guay, M. *Distributed State Estimation for Jointly Observable Linear Systems over Time-varying Networks*. arXiv:2302.12161.

[R4] He, X.; Xue, W.; Fang, H. *Consistent Distributed State Estimation with Global Observability over Sensor Network*. arXiv:1711.04993.

[R5] Mahler, D. H.; Rozema, L. A.; Darabi, A.; Ferrie, C.; Blume-Kohout, R.; Steinberg, A. M. *Adaptive Quantum State Tomography Improves Accuracy Quadratically*. arXiv:1303.0436.

[R6] Straupe, S. *Adaptive Quantum Tomography*. arXiv:1610.02840.

[R7] Schreiber, U.; Waldorf, K. *Connections on Non-Abelian Gerbes and Their Holonomy*. arXiv:0808.1923.

---

## 狀態

**Series B：階段性收束。**

後續若再開展，建議不再以「繼續增加概念」為主，而以：
1. formal theorem package；
2. runtime / benchmark；
3. quantum measurement mapping；
為主要研究方向。
