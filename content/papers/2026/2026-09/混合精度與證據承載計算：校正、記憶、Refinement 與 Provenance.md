# 混合精度與證據承載計算：校正、記憶、Refinement 與 Provenance

**系列：外掛式物理計算機與現場計算設備研究，第 6 篇**  
**英文系列名：External Physical Compute Appliances and Field Computing Systems**  
**英文篇名：Mixed-Precision and Evidence-Bearing Computation: Calibration, Memory, Refinement, and Provenance**  
**版本：v0.1**  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：2026-08-29**  
**狀態：公開草稿／異質 physical computation 的精度、校正、結果完整性與 provenance 架構**

## 摘要

Paper 00 至 Paper 05 已依序建立 External Physical Compute Appliance（EPCA）的設備總綱、Carrier-Generalized Abacus、Observable Physical Computation、Supervisor–Physical-Core Separation、Offline-First Field Autonomy 與 Multi-Substrate Compute Backplane。到這一步，一台 EPCA 已可以容納 optical、RF、acoustic、analog、FPGA、compute-in-memory（CIM）或其他 physical substrate，並以明確的 compute boundary、calibration gate、evidence path、fault containment 與 module contract 來使用它們。然而，一旦真正進入工程與科研現場，最難避開的問題不再只是「physical core 有沒有算」，而是：它到底算得多準？當環境、元件與讀出鏈路漂移時，這個精度是否仍成立？數位 refinement 可以幫忙到什麼程度，而不把 physical core 變成純展示？最後交付的數值又如何帶著足夠證據，使使用者知道它是怎麼形成的？

本文提出 **Mixed-Precision Evidence-Bearing Computation（MPEBC）**。其基本立場是：physical computation 不必被迫假裝成理想、無噪聲、固定精度的數位 primitive；相反地，EPCA 應將 raw physical result、calibration state、readout chain、error/uncertainty envelope、refinement history、module identity、algorithm version 與 final result 一起視為計算產品的一部分。

本文將一次 physical computation 抽象為：

$$
z_P
=
\mathcal P_{m,\theta_t}(x)
+
\eta_P,
$$

其中 $m$ 是 module/substrate identity， $\theta_t$ 是當下 configuration 與 operating state， $\eta_P$ 表示 device variation、noise、drift 與其他 non-idealities 的合成影響。Readout chain 取得：

$$
r
=
\mathcal R_{q_t}(z_P)
+
\eta_R,
$$

再以 calibration state $\kappa_t$ 形成：

$$
\hat z
=
\mathcal C_{\kappa_t}(r).
$$

若任務需要更高精度，可再使用 versioned refinement operator：

$$
y
=
\mathcal F_{\rho}(x,\hat z,e_0),
$$

其中 $e_0$ 是初始 error/uncertainty description， $\rho$ 是 refinement policy 與版本。最終交付物不再只有 $y$，而是：

$$
\boxed{
\mathcal O
=
(y,\mathcal E)
}
$$

其中 $\mathcal E$ 是 Evidence Envelope，至少能連回 raw output、calibration、physical module、readout、algorithm、refinement 與 execution history。

本文特別區分 **numerical error、physical variation、measurement/readout uncertainty、calibration uncertainty 與 model/task error**。這些來源不能被一個模糊的「accuracy」數字掩蓋。本文亦提出 calibration lifecycle、calibration validity envelope、precision negotiation、adaptive refinement、confidence-triggered fallback、cross-substrate verification、evidence-before-refinement、immutable raw record、offline provenance queue，以及 memory taxonomy，使一台具備足夠記憶體與本地計算能力的 field appliance 能在無網路時仍完成可審計的混合精度運算。

本文新增 **Computational Result Assurance（CRA-R0 至 CRA-R5）**。CRA 不表示 FLOPS、bit-width 或單純的 numerical precision，而衡量 final result 是否能被追溯至 physical output、有效 calibration、誤差／不確定度模型、refinement 路徑與完整 provenance。至此，EPCA 的五個獨立 assurance 座標成為：

$$
\boxed{
Q_{\mathrm{EPCA}}
=
(
\mathrm{OPC\mbox{-}V},
\mathrm{ESA\mbox{-}S},
\mathrm{LFA\mbox{-}F},
\mathrm{MSA\mbox{-}M},
\mathrm{CRA\mbox{-}R}
).
}
$$

本文最後主張：對 heterogeneous physical computing 而言，高精度不必全部來自單一 substrate；真正重要的是知道每一部分精度、校正與修正從哪裡來，以及 final result 是否仍保留對 physical core 的可驗證因果依賴。因此：

$$
\boxed{
\text{Approximate Physical Compute}
+
\text{Declared Refinement}
+
\text{Evidence Closure}
\neq
\text{Fake Physical Compute}.
}
$$

相反地，只要 physical contribution、calibration、refinement 與 provenance 都能被明確區分並驗證，混合計算本身可以是 EPCA 最實際也最強的工作模式之一。

**關鍵詞：** Mixed Precision、Physical Computing、Analog Computing、Compute-in-Memory、Calibration、Uncertainty、Iterative Refinement、Digital Refinement、Provenance、Evidence-Bearing Result、Metrological Traceability、Offline-First Computing、EPCA

---

## 1. 問題：physical core 的答案不是天然等於「可用答案」

Paper 02 已經回答：

> 怎麼知道 physical core 真的參與計算？

但即使 OPC-V3 或 OPC-V4 已成立，仍只表示 physical path 具有可驗證的因果貢獻。

它不保證：

$$
\hat y_P
=
y^*.
$$

更常見的是：

$$
\hat y_P
=
y^*+\epsilon.
$$

而且 $\epsilon$ 未必固定。

它可能依賴：

- temperature；
- supply voltage；
- wavelength；
- phase drift；
- device aging；
- memristor conductance variation；
- ADC/DAC quantization；
- RF front-end gain；
- acoustic coupling；
- sensor/readout noise；
- module replacement；
- reset history；
- algorithm mapping。

因此：

$$
\boxed{
\text{Physical Causality}
\neq
\text{Numerical Sufficiency}.
}
$$

---

## 2. 「精度不足」不等於 physical computing 失敗

若某個 physical substrate 原生擅長快速、低能耗地計算近似 transform：

$$
z_P
\approx
f(x),
$$

要求它一定單次輸出：

$$
z_P=f(x)
$$

才承認它有計算價值，可能反而錯過 heterogeneous computing 的真正優勢。

在許多數值方法裡，低精度結果可以是：

- initial guess；
- preconditioned result；
- coarse solve；
- bulk matrix operation；
- approximate inverse；
- candidate state；
- residual estimator；
- low-cost screening result。

因此本文採用：

$$
\boxed{
\text{Approximate Compute}
\neq
\text{Useless Compute}.
}
$$

關鍵是它是否能在整體演算法中被正確定位。

---

## 3. Mixed precision 的核心不是「FP16 + FP32」

在傳統數位計算語境中，mixed precision 常被理解為不同 floating-point format 的組合。

EPCA 的 mixed precision 更廣：

$$
\boxed{
\text{Mixed Precision}
=
\text{Mixed Physical Fidelity}
+
\text{Mixed Numerical Representation}
+
\text{Mixed Verification Cost}.
}
$$

也就是：

- 某一步由 analog physical core 做低精度 bulk operation；
- 某一步由 FPGA 做 fixed-point accumulation；
- 某一步由 CPU 做高精度 residual；
- 某一步由另一 substrate 做 cross-check；
- 某一步只在 uncertainty 超出 threshold 時才啟動。

這比單純 bit-width 更接近 EPCA。

---

## 4. 一個基本 MPEBC pipeline

本文提出：

$$
\boxed{
 x
\rightarrow
\mathcal P
\rightarrow
r_{\mathrm{raw}}
\rightarrow
\mathcal C
\rightarrow
\hat z
\rightarrow
\mathcal F
\rightarrow
y
\rightarrow
\mathcal E.
}
$$

其中：

- $\mathcal P$：physical compute；
- $r_{\mathrm{raw}}$：raw readout；
- $\mathcal C$：calibration/correction；
- $\hat z$：calibrated physical result；
- $\mathcal F$：declared refinement；
- $y$：final result；
- $\mathcal E$：evidence envelope。

任何一個階段都不應在 provenance 中消失。

---

## 5. Raw physical result 必須先存在

Paper 03 已建立 Evidence Before Refinement。

Paper 06 將它收緊：

$$
\boxed{
\text{Raw Record Commit}
<
\text{Refinement Commit}.
}
$$

也就是在 final digital refinement 之前，設備應先取得可識別的 physical record。

不一定要把所有高頻 waveform 永久保存，但至少必須能形成：

$$
R_P
=
(
\text{trace ID},
\text{raw summary},
\text{raw hash},
\text{capture parameters},
\text{module state}
).
$$

否則 final result 很容易把 physical provenance 洗掉。

---

## 6. Raw record 不等於 human-readable record

Raw evidence 可以是：

- ADC samples；
- photodiode current sequence；
- phase monitor values；
- RF I/Q samples；
- acoustic receiver traces；
- conductance snapshot；
- timing event list；
- module-local event digest。

因此：

$$
\boxed{
\text{Evidence}
\neq
\text{Visualization}.
}
$$

Paper 01 的 visible demonstrator 可以把它畫出來，但科研與現場設備真正需要的是可驗證的 machine-readable record。

---

## 7. 五種不能混在一起的 error / uncertainty

本文至少區分：

$$
\epsilon_{\mathrm{num}},
\epsilon_{\mathrm{phys}},
\epsilon_{\mathrm{read}},
\epsilon_{\mathrm{cal}},
\epsilon_{\mathrm{task}}.
$$

其中：

1. $\epsilon_{\mathrm{num}}$：數值方法與 representation 造成的誤差；
2. $\epsilon_{\mathrm{phys}}$：substrate variation、noise、drift；
3. $\epsilon_{\mathrm{read}}$：ADC、detector、sensor、front-end 所造成的讀出誤差／不確定度；
4. $\epsilon_{\mathrm{cal}}$：calibration relation 與 calibration reference 自身的不確定度；
5. $\epsilon_{\mathrm{task}}$：計算模型本身相對實際 task 的 model error。

把這五種全部報成「accuracy = 98%」會失去工程意義。

---

## 8. Deterministic bias 與 stochastic variation 必須分開

若：

$$
e_t
=
b_t+\xi_t,
$$

其中 $b_t$ 為 systematic bias， $\xi_t$ 為 stochastic component，則兩者對修正策略不同。

Bias 可以由 calibration table、linearization 或 feedback 估計；noise 則可能需要 averaging、filtering、redundancy 或 probabilistic envelope。

因此：

$$
\boxed{
\text{Calibration}
\neq
\text{Noise Removal}.
}
$$

---

## 9. Error budget 的最簡化表達

在可加性近似成立時，可以先寫：

$$
\epsilon_{\mathrm{total}}
\approx
\epsilon_{\mathrm{num}}
+
\epsilon_{\mathrm{phys}}
+
\epsilon_{\mathrm{read}}
+
\epsilon_{\mathrm{cal}}
+
\epsilon_{\mathrm{ref}}.
$$

但若各來源相關，則不能直接把 scalar error 相加。

更一般地，可用 covariance / uncertainty propagation：

$$
\Sigma_y
\approx
J\Sigma_{\theta}J^{\mathsf T}
+
\Sigma_{\mathrm{read}}
+
\Sigma_{\mathrm{ref}},
$$

其中 $J$ 為輸出對 relevant influence variables 的局部 sensitivity。

本文不要求所有 EPCA 都採同一統計模型，但要求 model 被宣告。

---

## 10. 「Uncertainty」在 computation 與 metrology 中不是完全同義

EPCA 可能同時做兩件事：

1. 計算一個數學函數；
2. 量測 physical core 的狀態來讀出計算結果。

第二件事本身是一個 measurement chain。

因此本文不把所有 numerical error 都冒充 SI metrological uncertainty。

應分成：

$$
U_{\mathrm{comp}}
\quad\text{與}\quad
U_{\mathrm{meas}}.
$$

若結果需要 metrological traceability，才進一步要求 calibration chain、reference、uncertainty statement 與 operating condition 滿足相應 metrology 規則。

---

## 11. Calibration 是 active computational state

本文不把 calibration 看成一個 PDF 證書或 metadata 附件。

對 physical computing：

$$
\boxed{
\kappa_t
\in
\text{Runtime State}.
}
$$

因為同一個 raw signal：

$$
r
$$

在不同 calibration state 下可能得到：

$$
\mathcal C_{\kappa_a}(r)
\neq
\mathcal C_{\kappa_b}(r).
$$

Calibration 直接參與 final result 的形成。

---

## 12. Calibration Bundle

每個 module 的 calibration bundle 至少應包含：

$$
K
=
(
ID_M,
ID_C,
v_C,
\Omega,
\Phi,
U_C,
T_C,
X_C
).
$$

其中：

- $ID_M$：module identity；
- $ID_C$：calibration identity；
- $v_C$：calibration schema/version；
- $\Omega$：valid operating envelope；
- $\Phi$：correction parameters / map；
- $U_C$：calibration uncertainty/error description；
- $T_C$：time validity；
- $X_C$：invalidation triggers。

---

## 13. Calibration validity 是一個 domain，不是一個 boolean 常數

例如 optical module 可能只有在：

$$
\lambda\in[\lambda_1,\lambda_2],
\qquad
T\in[T_1,T_2]
$$

時維持既定 error envelope。

因此：

$$
\mathrm{Valid}_{\kappa}(s_t)
=
\begin{cases}
1,&s_t\in\Omega_{\kappa},\\
0,&s_t\notin\Omega_{\kappa}.
\end{cases}
$$

這比「上次校正成功」更精確。

---

## 14. Calibration lifecycle

本文建議：

$$
\text{UNKNOWN}
\rightarrow
\text{CALIBRATING}
\rightarrow
\text{VALID}
\rightarrow
\text{DEGRADED}
\rightarrow
\text{EXPIRED}
\rightarrow
\text{INVALID}.
$$

其中 DEGRADED 不必立即停機；它可以觸發：

- 更高 refinement；
- 更頻繁 cross-check；
- 降低 throughput；
- 縮小 operation envelope；
- 要求人工 re-calibration。

---

## 15. 什麼事件應使 calibration 失效？

至少可以包括：

- module replacement；
- front-end replacement；
- sensor replacement；
- firmware/bitstream change；
- physical alignment change；
- laser source change；
- acoustic geometry change；
- thermal shock；
- accumulated device wear；
- conductance reprogramming；
- calibration schema change；
- reference artifact change。

因此 calibration validity 必須跟 module lifecycle 連動。

---

## 16. Static calibration 不是唯一方法

有些 physical substrate 適合：

$$
\text{static calibration table}.
$$

有些適合：

$$
\text{continuous closed-loop tracking}.
$$

有些則使用：

$$
\text{hybrid calibration}
=
\text{static reference}
+
\text{online compensation}.
$$

2025 年可重構 photonic circuit 的 integrated electronic controller 就顯示：當 thermal drift 與 input perturbation 持續存在時，runtime feedback 可能比單次 lookup calibration 更重要。

---

## 17. Calibration plane 不能偷偷變成 compute plane

假設 physical core 宣告計算：

$$
z_P=f_P(x).
$$

Calibration logic 可以做：

$$
\hat z=a z_P+b.
$$

或更複雜的 correction map。

但如果 calibration software 實際上直接做：

$$
\hat z=f(x)
$$

而 $z_P$ 幾乎被忽略，那就違反 No Silent Substitution。

因此 calibration 也必須被納入 Paper 03 的 authority boundary。

---

## 18. Refinement 是合法的，但必須被命名

本文將 refinement 定義為：

> 在已取得 physical result 後，使用另外的 numerical or physical operation 改善 final accuracy、stability 或 confidence 的明示步驟。

也就是：

$$
\hat z
\rightarrow
\mathcal F_{\rho}
\rightarrow
y.
$$

合法 refinement 的關鍵不是「digital 不可以碰答案」，而是：

$$
\boxed{
\text{Refinement must be declared and provenance-preserving}.
}
$$

---

## 19. 最經典的 mixed-precision pattern：iterative refinement

考慮：

$$
Ax=b.
$$

physical core 先取得低精度近似：

$$
x_0\approx A^{-1}b.
$$

高精度數位路徑計算 residual：

$$
r_k=b-Ax_k.
$$

再讓 physical solver 求近似 correction：

$$
A\delta_k\approx r_k.
$$

更新：

$$
x_{k+1}=x_k+\delta_k.
$$

直到：

$$
\lVert r_k\rVert\le\tau.
$$

這就是 physical bulk compute 與 digital high-precision arithmetic 可以自然合作的例子。

---

## 20. 2018 年 mixed-precision in-memory computing 的意義

Le Gallo 等人的工作已實驗展示：computational memory unit 可以做大量低精度工作，而 conventional von Neumann machine 使用 backward/iterative method 改善解的精度。

這證明：

$$
\boxed{
\text{Low-Precision Physical Primitive}
+
\text{High-Precision Refinement}
}
$$

本身是一條正當而有工程價值的路線。

EPCA 要做的是把這個原則從單一 CIM 架構抽象成跨 substrate contract。

---

## 21. 2025 年 heterogeneous CIM 又往前一步

2025 年的 mixed-precision memristor + SRAM CIM processor 進一步在同一 processor 中依 error sensitivity，把工作分派給 memristor-CIM、SRAM-CIM、tiny digital unit，以及 INT/FP format。

這說明 precision 不必是一顆晶片全域固定的屬性。

可以是：

$$
\boxed{
\text{operation-relative precision placement}.
}
$$

這與 EPCA 的 multi-substrate routing 高度相容。

---

## 22. Precision 應該成為 negotiated resource

Paper 05 的 Algorithm Requirement Manifest 可以新增：

$$
R_{\tau}
=
(
\epsilon_{\max},
U_{\max},
P_{\mathrm{conf}},
L_{\max},
E_{\max},
V_{\min}
).
$$

也就是 task 可以宣告：

- maximum numerical error；
- maximum uncertainty；
- confidence requirement；
- latency budget；
- energy budget；
- minimum verification level。

Backplane 再決定需要哪一種 physical + digital composition。

---

## 23. Precision 不是越高越好

若現場任務只需要：

$$
\epsilon\le10^{-2},
$$

卻固定用高成本路徑達到：

$$
\epsilon\le10^{-10},
$$

可能浪費：

- energy；
- latency；
- ADC precision；
- device writes；
- memory bandwidth；
- thermal budget。

因此：

$$
\boxed{
\text{Precision is task-relative.}
}
$$

---

## 24. Adaptive precision policy

可以定義成本：

$$
J
=
\alpha T
+
\beta E
+
\gamma W
+
\delta B
+
\mu C,
$$

其中：

- $T$：latency；
- $E$：energy；
- $W$：wear；
- $B$：bandwidth/storage；
- $C$：calibration/refinement cost。

在滿足：

$$
\epsilon\le\epsilon_{\max}
$$

與 assurance constraints 下最小化 $J$。

這使 precision 成為 runtime scheduling problem。

---

## 25. Confidence-triggered refinement

第一輪 physical computation 得到：

$$
(y_0,U_0).
$$

若：

$$
U_0\le U_{\max},
$$

直接接受。

若：

$$
U_0>U_{\max},
$$

啟動 refinement：

$$
y_1=\mathcal F_1(y_0).
$$

再重新估計：

$$
U_1.
$$

這比所有 input 都固定跑最昂貴路徑更合理。

---

## 26. Cross-substrate refinement

Refinement 不必由 CPU 完成。

例如：

$$
\mathcal P_{\mathrm{optical}}
\rightarrow
\mathcal P_{\mathrm{FPGA}}
\rightarrow
y.
$$

或：

$$
\mathcal P_{\mathrm{CIM}}
\rightarrow
\mathcal P_{\mathrm{digital}}
\rightarrow
\mathcal P_{\mathrm{RF-check}}.
$$

因此：

$$
\boxed{
\text{Mixed Precision}
\subset
\text{Multi-Substrate Composition}.
}
$$

---

## 27. Cross-substrate verification 與 refinement 不同

如果第二個 substrate 只是獨立重算並比較：

$$
y_A\stackrel{?}{\approx}y_B,
$$

它是 verification。

如果第二個 substrate 使用 $y_A$ 生成更準的：

$$
y_B=\mathcal F(y_A),
$$

它是 refinement。

兩者 provenance semantics 不可混在一起。

---

## 28. Refinement Non-Erasure Principle

本文新增：

$$
\boxed{
\text{Refinement must not erase the declared physical dependency.}
}
$$

若 final result 在移除 $z_P$ 後仍由同一 undeclared digital path 完整算出，則應重新分類為：

$$
\text{Digital Primary}
$$

或：

$$
\text{Digital Fallback}.
$$

不能繼續聲稱是 physical-primary result。

---

## 29. Physical contribution class

本文建議每個 result 額外宣告：

- **PC-P**：Physical-Primary；
- **PC-C**：Physical-Cooperative；
- **PC-S**：Physical-Seed / Initializer；
- **PC-V**：Physical-Verification-Only；
- **PC-D**：Digital-Primary；
- **PC-F**：Digital Fallback。

這不是性能排名，而是 final result 的 causal composition label。

---

## 30. 為什麼需要這個 label？

因為以下兩個系統可能最後 accuracy 相同：

系統 A：

$$
\text{physical core does 95\% bulk work}
+
\text{digital correction}.
$$

系統 B：

$$
\text{digital CPU does all work}
+
\text{physical path only displays waveform}.
$$

若只看 final $y$，兩者可能不可區分。

Paper 02 的 causal validation 與本篇 PC label 結合，才可以區分它們。

---

## 31. Memory：為什麼「內存夠」真的會讓這種 appliance 好用？

EPCA 不只需要存程式。

它可能要同時保留：

$$
\mathcal M_{\mathrm{state}},
\mathcal M_{\mathrm{cal}},
\mathcal M_{\mathrm{evidence}},
\mathcal M_{\mathrm{reference}},
\mathcal M_{\mathrm{cache}},
\mathcal M_{\mathrm{history}}.
$$

當 RAM 與 local storage 足夠大，很多原本必須依賴 PC/server 的工作可以留在 appliance 內部閉合。

---

## 32. Working memory

Working memory 保存：

- current input batch；
- physical configuration；
- intermediate tensors/vectors；
- residual；
- solver state；
- temporary waveform/sample buffers。

這部分可以 volatile。

但 crash recovery 需要由 Paper 04 的 durable journal 記錄必要 checkpoint。

---

## 33. Calibration memory

Calibration memory 應至少保存：

- current calibration bundle；
- previous accepted calibration；
- environment envelope；
- coefficients / LUT；
- calibration evidence；
- invalidation reasons。

它不應與一般 cache 混為一談。

---

## 34. Reference memory

Scientific/engineering appliance 可能需要本地 reference：

- standard vectors；
- known test cases；
- calibration patterns；
- golden outputs；
- expected spectral signatures；
- reference matrices。

有足夠 local memory 後，即使斷網也可以做 local validation。

---

## 35. Evidence memory

Evidence memory 保存：

$$
\mathcal E_1,\mathcal E_2,\ldots,\mathcal E_n.
$$

它可以採多層策略：

- full raw trace；
- compressed trace；
- statistical summary；
- hash + content-addressed object；
- retained-on-failure only；
- sampled audit retention。

不同 field profile 可有不同 retention policy。

---

## 36. Provenance memory

Provenance memory 不等於 raw evidence memory。

它記錄的是：

$$
\text{what depended on what}.
$$

例如：

$$
y
\leftarrow
\rho_3
\leftarrow
\hat z
\leftarrow
\kappa_{17}
\leftarrow
r_P
\leftarrow
M_{42}.
$$

這是一個 derivation graph。

---

## 37. Evidence Envelope 的最小內容

本文提出：

$$
\mathcal E
=
(
I,
A,
M,
C,
K,
R,
U,
F,
P,
T,
H
).
$$

其中：

- $I$：input identity/hash；
- $A$：algorithm identity/version；
- $M$：module/substrate identity；
- $C$：configuration；
- $K$：calibration identity；
- $R$：raw physical record reference；
- $U$：error/uncertainty description；
- $F$：refinement history；
- $P$：physical contribution class；
- $T$：timing/environment context；
- $H$：hardware/software lineage。

---

## 38. Evidence Envelope 不一定把所有 bytes 內嵌

對大型 waveforms：

$$
|R|\gg|y|.
$$

因此 evidence envelope 可以使用：

$$
R=(h_R,URI_{\mathrm{local}},\text{retention class}).
$$

重點不是把每個 raw sample 塞進 final JSON，而是建立不可混淆的 binding。

---

## 39. Provenance graph

一次結果可以形成：

$$
G_E=(V_E,E_E).
$$

節點可以包含：

- input entity；
- module state；
- calibration entity；
- physical execution activity；
- readout activity；
- refinement activity；
- verification activity；
- final result entity。

這可以與 W3C PROV 的 entity/activity/agent 概念相容，但 EPCA 仍需要自己的 domain-specific schema。

---

## 40. Provenance 不是「log 很多」

若裝置產生 10 GB log，但無法回答：

> 這個 $y$ 到底由哪個 physical run、哪個 calibration、哪次 refinement 形成？

那就仍然沒有 result provenance closure。

因此：

$$
\boxed{
\text{Logging Volume}
\neq
\text{Provenance Quality}.
}
$$

---

## 41. Result identity

每一個 final result 建議有：

$$
RID
=
H(
I,A,M,C,K,R,F
).
$$

這不是說 hash 本身證明計算正確，而是讓 result 與 derivation record 綁定。

如果 provenance graph 改了，RID 也應改變或產生新版本。

---

## 42. Versioned result，而不是覆寫 result

若新的 calibration 或 refinement policy 產生：

$$
y^{(2)}\neq y^{(1)},
$$

不應把舊結果直接覆寫。

而應形成：

$$
RID_1\rightarrow RID_2.
$$

兩者都保留 derivation relation。

這對科研重現與事故調查非常重要。

---

## 43. Evidence-before-refinement 的 durable 實作

在 offline-first appliance 中可以使用：

1. write raw-run journal；
2. fsync / durable commit；
3. run calibration；
4. commit calibrated record；
5. run refinement；
6. commit final result；
7. append provenance edges。

因此 power loss 發生在任一步，都能知道 computation 停在哪裡。

---

## 44. 不能把 crash recovery 當成重新算一遍就好

若 physical run 具有：

- stochasticity；
- device wear；
- sensor capture；
- environmental dependence；
- non-repeatable external input，

那麼：

$$
\text{rerun}
\neq
\text{same execution}.
$$

所以 durable evidence record 本身就是 computation state 的一部分。

---

## 45. Calibration provenance

每個 calibrated result：

$$
\hat z
=
\mathcal C_{K_j}(r)
$$

必須能連到 $K_j$。

若 later re-calibration 產生 $K_{j+1}$，舊 result 不能默認變成由新 calibration 產生。

必要時可以建立：

$$
\hat z'
=
\mathcal C_{K_{j+1}}(r)
$$

作為 derived result。

---

## 46. 保留 raw record 的科學價值

如果 raw evidence 還在，未來可以：

- 使用更好的 calibration 重算；
- 使用更好的 error model 重估；
- 重做 digital refinement；
- 檢查 instrumentation bug；
- 比較不同 algorithm version。

因此 raw record 有時比 final scalar 更有長期價值。

---

## 47. 但 raw evidence retention 不是免費的

若 sample rate 為 $f_s$ 、每 sample $b$ bits、通道數 $n$ 、時間 $T$：

$$
S
=
f_s b n T.
$$

因此 EPCA 需要 retention profile。

不是所有 field device 都適合永久保存 full waveform。

---

## 48. Retention profiles

本文建議至少四種：

### Demo Profile

保留大量可視化 trace，方便展示。

### Field Profile

保存 summary + hash + abnormal-run raw trace。

### Scientific Profile

保存可重分析所需的 raw evidence 與 calibration context。

### Throughput Profile

只保留 policy 要求的最小證據，優先 performance。

---

## 49. Compression 不能破壞 provenance semantics

若 raw waveform 被壓縮：

$$
R\rightarrow R_c,
$$

應記錄：

- compression algorithm；
- version；
- lossless/lossy；
- parameters；
- pre-compression hash；
- post-compression hash。

尤其 scientific profile 不應默認用 lossy compression 抹掉 error analysis 所需特徵。

---

## 50. Calibration 與 normalization 不同

Normalization：

$$
x'=
\frac{x-\mu}{\sigma}
$$

可能只是 algorithm preprocessing。

Calibration 則把 instrument indication 與 reference relation 連起來。

兩者可能都改變數值，但 provenance role 不同。

---

## 51. Correction 與 calibration 也應分開

Calibration 可以估計：

$$
y=a x+b.
$$

Correction 則實際套用：

$$
\hat x=\frac{y-b}{a}.
$$

因此 calibration evidence 與 runtime correction activity 最好分開記錄。

---

## 52. Online calibration 的 evidence

如果 calibration 是 runtime feedback：

$$
\kappa_t
\rightarrow
\kappa_{t+1}
$$

持續更新，則結果 provenance 不能只寫「calibration v3」。

需要能識別：

$$
\kappa(t_{\mathrm{exec}}).
$$

或者記錄可重建該時段 control state 的 digest / trace。

---

## 53. Photonic substrate 特別需要這個模型

可重構 photonic circuit 的 working point 會受：

- thermal drift；
- phase error；
- input variation；
- wavelength shift，

影響。

2025 年已有 integrated electronic controller 使用多個 local feedback loop 動態設定與維持 photonic circuit 工作點。

這支持 EPCA 將 calibration/control state 納入 computational provenance，而不是視為外部設備維護。

---

## 54. Analog/CIM substrate 的主要 non-idealities

常見包括：

- conductance quantization；
- programming error；
- device-to-device variation；
- cycle-to-cycle variation；
- temporal drift；
- IR drop；
- DAC/ADC quantization；
- saturation；
- circuit noise；
- nonlinear response。

因此 raw bit-width 不能直接等價於有效 computational precision。

---

## 55. ADC 可能成為 precision bottleneck

即使 physical core 內部具有豐富 analog state，最後若：

$$
\text{ADC precision}=b,
$$

readout 也可能把 information 壓縮到有限 code space。

因此：

$$
\boxed{
\text{Core Precision}
\neq
\text{System Precision}.
}
$$

System precision 必須包含 transduction/readout chain。

---

## 56. 高精度可以由低精度 primitive 組出來

2025 年的 analogue matrix equation solving 研究顯示，低位元 RRAM primitive 可以透過 iterative algorithm 與 block matrix 方法得到遠高於單次 primitive 的 effective precision。

這再次說明：

$$
\boxed{
\text{Primitive Precision}
\neq
\text{Algorithmic Result Precision}.
}
$$

EPCA 的 module descriptor 因此應分別宣告兩者。

---

## 57. Module descriptor 新增 precision fields

Paper 05 的 capability descriptor 可以增加：

- native representation；
- nominal primitive precision；
- empirically validated error envelope；
- calibration-dependent precision；
- supported refinement modes；
- readout precision；
- repeatability；
- drift model；
- uncertainty model version；
- validated operating envelope。

不能只寫：

$$
\text{precision}=8\text{ bit}.
$$

---

## 58. Precision claim 必須帶 scope

合理的 claim 應是：

> 在 module $M$ 、calibration $K$ 、temperature envelope $\Omega_T$ 、operation family $O$ 與 input domain $D$ 下，error distribution / bound 為某範圍。

形式上：

$$
\mathcal Q
=
(M,K,O,D,\Omega,\epsilon,U).
$$

脫離 scope 的「高精度」不能被視為同一保證。

---

## 59. Result status

本文建議 result state：

$$
\text{RAW}
\rightarrow
\text{CALIBRATED}
\rightarrow
\text{REFINED}
\rightarrow
\text{VERIFIED}
\rightarrow
\text{AUDITABLE}.
$$

這不是說每個任務都必須走到最後。

Demo mode 可能停在 CALIBRATED；科研模式則希望走到 AUDITABLE。

---

## 60. CRA-R0：Output Only

系統只交付：

$$
y.
$$

沒有 raw binding、calibration identity、uncertainty 或 refinement history。

它可以是一台能用的計算器，但 result assurance 最低。

---

## 61. CRA-R1：Raw-Bound Result

要求：

$$
y\leftrightarrow R_P.
$$

至少能識別 final result 來自哪一次 physical run。

但 calibration、uncertainty 與 refinement 還可能不完整。

---

## 62. CRA-R2：Calibrated Result

要求：

- raw record binding；
- calibration ID/version；
- validity envelope；
- basic error/uncertainty statement。

也就是：

$$
(y,R_P,K,U).
$$

---

## 63. CRA-R3：Refinement-Transparent Result

若使用 mixed precision，必須保存：

$$
\hat z
\rightarrow
F_1
\rightarrow
F_2
\rightarrow
\cdots
\rightarrow
y.
$$

並標記 physical contribution class。

同時能通過 Refinement Non-Erasure 檢查。

---

## 64. CRA-R4：Cross-Validated Replayable Result

在 R3 基礎上增加：

- cross-path / reference verification；
- uncertainty model version；
- fault/abnormal condition annotation；
- deterministic parts 可 replay；
- stochastic/raw parts 有保留或摘要證據。

結果可以被另一個 verifier 重建 derivation chain。

---

## 65. CRA-R5：Independent Evidence Closure

R5 要求 final result 的形成能由獨立 verifier 檢查：

- input identity；
- module identity；
- raw physical evidence；
- calibration lineage；
- uncertainty/error model；
- refinement history；
- verification history；
- software/hardware versions；
- tamper-evident provenance binding。

R5 仍不表示「數值一定正確」，而表示 result formation 已達到高強度可審計性。

---

## 66. CRA 與 OPC 不同

可能有：

$$
\mathrm{OPC\mbox{-}V5}
+
\mathrm{CRA\mbox{-}R1}.
$$

表示 physical causality 證據很強，但 final result 的 calibration/refinement provenance 很弱。

也可能：

$$
\mathrm{OPC\mbox{-}V3}
+
\mathrm{CRA\mbox{-}R5}.
$$

表示 causal physical compute 已經成立，而且 final result lineage 極完整，但 physical-core causal verification 沒做到最高級。

兩軸不能合併。

---

## 67. CRA 與 numerical precision 也不同

一個 64-bit result：

$$
y_{64}
$$

可能只有 CRA-R0。

另一個 8-bit physical primitive 經 refinement 得到的結果，可能達 CRA-R5。

因此：

$$
\boxed{
\text{Bit Width}
\neq
\text{Result Assurance}.
}
$$

---

## 68. EPCA 五維 assurance space

到 Paper 06：

$$
\boxed{
Q_{\mathrm{EPCA}}
=
(V,S,F,M,R).
}
$$

其中：

- $V$：Observable Physical Computation evidence；
- $S$：Embedded Supervisor authority assurance；
- $F$：Local Field Autonomy；
- $M$：Modular Substrate Assurance；
- $R$：Computational Result Assurance。

這比單一成熟度分數更誠實。

---

## 69. 一個科研用 profile

例如科研設備可以要求：

$$
Q_{\mathrm{sci}}
\ge
(
V4,
S4,
F3,
M3,
R5
).
$$

原因是科研情境可能不需要最高 hot-swap/modularity，但對 result provenance 要求很高。

---

## 70. 一個現場工程 profile

工程 field appliance 可能要求：

$$
Q_{\mathrm{field}}
\ge
(
V3,
S4,
F5,
M3,
R4
).
$$

這裡 offline recovery 比保存所有 raw trace 更重要。

---

## 71. 一個展示 profile

Demonstrator 可能：

$$
Q_{\mathrm{demo}}
\ge
(
V3,
S2,
F1,
M1,
R2
).
$$

它需要證明 physical core 真算，但不一定要有完整 field autonomy。

---

## 72. Offline evidence closure

Paper 04 已要求斷網仍能執行。

Paper 06 再加：

$$
\boxed{
\text{Network Loss}
\not\Rightarrow
\text{Evidence Loss}.
}
$$

即使 remote provenance service 不可用，本機仍應能：

- assign local RID；
- commit raw evidence；
- commit calibration binding；
- store refinement graph；
- later sync without rewriting history。

---

## 73. Reconnect 後不能偷偷補造 provenance

若設備離線期間沒有保存 raw evidence，回網後 server 不能根據 final $y$ 反推一份「看起來完整」的 physical history。

因此：

$$
\boxed{
\text{Provenance is recorded during execution, not invented after execution}.
}
$$

---

## 74. Signed metadata 與 correctness 不同

Cryptographic signature 可以證明：

> 某個 key 對這份 record 簽過名。

但不能單獨證明：

> physical computation 正確。

因此：

$$
\boxed{
\text{Integrity}
\neq
\text{Correctness}.
}
$$

Signature/hash 是 evidence transport 的一層，不是物理驗證的替代品。

---

## 75. Tamper-evident provenance

若需要較高 assurance，可以使用：

$$
H_i
=
H(H_{i-1}\Vert E_i).
$$

形成 hash chain。

或以 Merkle tree 形成 batch evidence root。

這對離線 field appliance 很適合，因為可以先在本機封存，之後再同步 root / records。

---

## 76. Provenance privacy

Evidence-rich 不代表所有 raw input 都要無限制上傳。

可使用：

- content hash；
- local-only raw record；
- redacted metadata；
- encrypted evidence object；
- selective disclosure；
- export policy。

科研可重現性與現場資料治理要同時考慮。

---

## 77. Algorithm package 必須宣告 refinement semantics

一個 algorithm manifest 不只寫：

$$
\text{operation} = \text{matrix solve}.
$$

還應宣告：

- physical stage；
- required calibration class；
- accepted primitive error；
- refinement method；
- stopping rule；
- fallback policy；
- evidence retention requirement；
- final CRA target。

這樣 supervisor 才能安全排程。

---

## 78. Stopping rule 不能只寫「差不多了」

例如 iterative refinement 可以使用：

$$
\frac{\lVert r_k\rVert}{\lVert b\rVert}
\le
\tau_r.
$$

或者：

$$
U_k\le U_{\max}.
$$

也可以有 max iteration：

$$
k\le k_{\max}.
$$

所有 stopping condition 都應進 provenance。

---

## 79. Refinement failure

若 refinement 無法收斂：

$$
\lVert r_{k+1}\rVert
\ge
\lVert r_k\rVert,
$$

系統不應繼續把 final result 標成高精度成功。

可以轉成：

- retry with recalibration；
- alternate module；
- digital fallback；
- lower-confidence result；
- fail-closed。

---

## 80. Digital fallback 必須顯式

如果 physical path 失敗，而 CPU 完整重算：

$$
y=f_{\mathrm{CPU}}(x),
$$

則 result 應標記：

$$
PC=\mathrm{PC\mbox{-}F}.
$$

不能因為 appliance 裡有 physical module，就把這個 result 繼續標成 physical-compute result。

---

## 81. Physical fallback 也可能存在

若 optical core 失效：

$$
\mathcal P_{\mathrm{optical}}
\rightarrow
\mathcal P_{\mathrm{FPGA}}
$$

或：

$$
\mathcal P_{\mathrm{CIM}}
\rightarrow
\mathcal P_{\mathrm{RF}}.
$$

這是 Paper 05 multi-substrate backplane 的直接用途。

Provenance 必須記錄實際使用哪個 fallback。

---

## 82. Calibration-aware routing

同一 task 可能有兩個 module：

$$
M_A,
M_B.
$$

若：

$$
\mathrm{Valid}_{K_A}=0,
\qquad
\mathrm{Valid}_{K_B}=1,
$$

即使 $M_A$ nominal throughput 更高，也不一定應選它。

因此 scheduler 要把 calibration readiness 放進 routing cost。

---

## 83. Drift-aware routing

若 module error 隨時間增加：

$$
\epsilon_M(t)
\uparrow,
$$

scheduler 可以在 re-calibration 之前：

- 降低 task class；
- 增加 refinement；
- 增加 verification sampling；
- 把高精度任務轉給其他 module。

這是 dynamic constraint domain 的工程版本。

---

## 84. Wear-aware precision

對某些 non-volatile memory device，頻繁 programming 具有 wear cost。

因此高 precision 可能不只更慢，也更耗 device life。

Routing objective 可以加入：

$$
W_{\mathrm{device}}.
$$

這使「精度」與 lifecycle 成為聯合最佳化問題。

---

## 85. Scientific reproducibility 的兩種層級

### Computational reproducibility

同一 input、algorithm、configuration 可重算出一致範圍結果。

### Physical-run reproducibility

同一 physical substrate 在相同 operating envelope 可重現相似 physical behavior。

兩者不是同一件事。

EPCA evidence envelope 應能支持區分。

---

## 86. Exact replay 不一定可能

對 stochastic physical system：

$$
R_{t_1}\neq R_{t_2}
$$

可能是正常的。

所以 replay target 可以是：

$$
\text{distributional / tolerance equivalence}
$$

而不是 bitwise identity。

這再次說明 provenance 比單純 deterministic log 更重要。

---

## 87. Effective equivalence

兩個 substrate：

$$
\mathcal P_A
\neq
\mathcal P_B
$$

可能在 task tolerance 下：

$$
d(f_A(x),f_B(x))\le\epsilon_{\tau}.
$$

則它們可以形成 task-relative effective compute equivalence。

但 provenance 應保留：

$$
A\neq B.
$$

不能因 final number 接近就抹除 construction path。

---

## 88. 與前置「跨尺度構成」系列的接口

該系列已區分：

$$
\text{approximability}
\neq
\text{finite-cost exactness}
\neq
\text{efficient realizability}.
$$

Paper 06 把這條命題工程化：

physical core 可能只有 approximability；refinement 把它推到 task sufficient；但總成本是否值得，仍由 routing policy 決定。

---

## 89. 與「認知功能體物理實現」系列的接口

前置系列指出：

$$
\text{same function}
\not\Rightarrow
\text{same substrate/history}.
$$

Paper 06 對計算結果也採相同態度。

兩個 final results 可以功能等價，但 evidence envelope 告訴我們：

- 哪個來自 optical；
- 哪個來自 CIM；
- 哪個有 digital refinement；
- 哪個是 fallback。

有效等價不要求 provenance 相同。

---

## 90. NIST traceability 給 EPCA 的啟發

NIST 將 metrological traceability 描述為 measurement result 能透過 documented unbroken chain of calibrations 連回 specified reference，且鏈上的 calibration 都對 uncertainty 有貢獻。

EPCA 不應冒稱所有 computation 都具有 SI traceability。

但它可以採用相似原則：

$$
\boxed{
\text{Result Traceability}
=
\text{documented unbroken derivation chain}.
}
$$

這是 computational provenance 的強大設計參考。

---

## 91. Traceability 是 result property，不是「設備貼紙」

NIST 特別強調：僅僅儀器被校正，不代表後續所有 measurement result 自動具有 traceability。

EPCA 也應採取同樣保守態度：

$$
\boxed{
\text{Calibrated Module}
\not\Rightarrow
\text{Every Result Is Calibrated/Traceable}.
}
$$

每一個 result 必須證明自己使用了哪個 calibration 與 operating condition。

---

## 92. W3C PROV 給 EPCA 的啟發

W3C PROV 將 provenance 建模為 producing/influencing data 或 thing 的 entities、activities 與 agents。

EPCA 可以使用相容精神：

- Input：Entity；
- Physical Run：Activity；
- Module：Entity/Agent-like accountable component；
- Calibration：Entity；
- Refinement：Activity；
- Final Result：Entity。

但 EPCA 仍需增加 physical evidence、calibration validity、uncertainty 與 assurance level 等 domain semantics。

---

## 93. Evidence graph 可以跨設備

若 field EPCA A 產生：

$$
y_A
$$

再傳給 lab EPCA B refinement：

$$
y_B=F(y_A),
$$

provenance graph 可以跨裝置連接：

$$
RID_A\rightarrow RID_B.
$$

這使「外掛式計算機」不是孤島，而能形成可審計的 computation chain。

---

## 94. 網路不是 provenance 的前提

每台裝置先用 local identity space：

$$
RID_{\mathrm{local}}.
$$

回網後再同步 mapping。

所以：

$$
\boxed{
\text{Offline First}
+
\text{Provenance First}
}
$$

是相容的。

---

## 95. Human-readable result card

現場 UI 不需要把所有 evidence 全塞給使用者。

可以顯示：

- Result：17.8234；
- Precision target：met；
- Estimated error： $\pm 0.003$ ；
- Physical core：RF Module 02；
- Calibration：valid；
- Refinement：2 iterations；
- Verification：cross-check passed；
- CRA：R4；
- Evidence ID：RID-...。

需要時再展開 full evidence。

---

## 96. Machine-readable result contract

對 host / API：

$$
\mathrm{ResultObject}
=
(
value,
status,
precision,
uncertainty,
provenance,
evidence\_ref,
assurance
).
$$

這讓 EPCA 不只是回傳一個 float。

它回傳一個 computation object。

---

## 97. 這會改變「外掛計算機」的 API

傳統 accelerator API 常像：

$$
y=\mathrm{execute}(x).
$$

EPCA 更合理的是：

$$
(y,E)
=
\mathrm{execute}(x,\tau,\Pi),
$$

其中 $\Pi$ 是 policy：

- precision；
- latency；
- energy；
- assurance；
- retention；
- fallback。

---

## 98. Precision/Evidence policy examples

### Fast

$$
\Pi_F:
\epsilon\le10^{-2},
R\ge R2.
$$

### Engineering

$$
\Pi_E:
\epsilon\le10^{-4},
R\ge R4.
$$

### Scientific

$$
\Pi_S:
\epsilon\le10^{-6},
R=R5,
\text{raw retention required}.
$$

這些數字只是示意，真正門檻由 task 定義。

---

## 99. AI 未來可以做什麼？

Paper 06 仍不需要 AI 才能成立。

所有 routing/refinement policy 都可以由 deterministic rule engine 執行。

未來 AI 可以協助：

- 預測 drift；
- 選擇 substrate；
- 選擇 refinement strategy；
- anomaly detection；
- calibration scheduling；
- evidence triage。

但 AI 不應成為無法審計的 accuracy oracle。

---

## 100. AI refinement 需要更高 provenance 要求

若未來 refinement operator 是 learned model：

$$
y=F_{\mathrm{AI}}(x,\hat z),
$$

至少要保存：

- model identity；
- model version/hash；
- inference configuration；
- prompt/context 若適用；
- confidence/error validation；
- whether AI can independently solve task from $x$。

否則 physical contribution 更容易被掩蓋。

---

## 101. 不讓 AI 把 physical evidence「合理化」

AI 可以解釋 evidence，但不能把缺失 evidence 自動補寫成已觀測事實。

因此：

$$
\boxed{
\text{Inference}
\neq
\text{Observation}.
}
$$

這與前置可觀測性系列完全一致。

---

## 102. Benchmark 也要拆成多個輸出

Paper 07 之後不能只比較：

$$
\mathrm{Throughput}.
$$

還需要至少：

$$
(
T,
E,
\epsilon,
U,
C_{\mathrm{cal}},
C_{\mathrm{ref}},
S_{\mathrm{evidence}}
).
$$

也就是 latency、energy、error、uncertainty、calibration cost、refinement cost、evidence cost。

---

## 103. End-to-end benchmark

physical core 本身可能 1 ns 完成 transform，但：

- DAC encode 需要時間；
- calibration 需要時間；
- ADC readout 需要時間；
- refinement 需要時間；
- evidence commit 需要時間。

因此最公平的是：

$$
T_{\mathrm{E2E}}
=
T_{\mathrm{encode}}
+
T_P
+
T_{\mathrm{read}}
+
T_{\mathrm{cal}}
+
T_{\mathrm{ref}}
+
T_{\mathrm{evidence}}.
$$

---

## 104. Energy benchmark 也一樣

$$
E_{\mathrm{E2E}}
=
E_{\mathrm{encode}}
+
E_P
+
E_{\mathrm{control}}
+
E_{\mathrm{read}}
+
E_{\mathrm{ref}}
+
E_{\mathrm{storage}}.
$$

若只報 physical core propagation energy，很可能誤導實際 appliance 效率。

---

## 105. 精度與證據都有成本

高 CRA 可能需要：

- 更多 raw storage；
- 更多 verification；
- 更長 retention；
- 更高頻 calibration；
- 更完整 signatures/hashes；
- 更多 refinement。

因此：

$$
\boxed{
\text{Assurance is a resource.}
}
$$

這將成為 Paper 07 routing 的重要條件。

---

## 106. 但 evidence cost 可以被工程化

可以用：

- sampling；
- event-triggered retention；
- compressed trace；
- hierarchical evidence；
- Merkle batching；
- local ring buffer；
- failure-triggered freeze。

所以 high assurance 不必等於無限制 logging。

---

## 107. 一個完整例子：RF physical transform

假設 RF module 做：

$$
z_P\approx Fx.
$$

執行流程：

1. supervisor commit input hash；
2. module configuration locked；
3. RF waveform injected；
4. ADC capture raw response；
5. raw evidence committed；
6. calibration map applied；
7. digital residual computed；
8. optional refinement performed；
9. alternate reference vector sampled；
10. final result + CRA level committed。

這就是一個 evidence-bearing physical calculation。

---

## 108. 一個完整例子：CIM matrix solve

Physical stage：

$$
x_0\approx A^{-1}b.
$$

Evidence：

- array ID；
- conductance state/version；
- ADC configuration；
- raw solve output；
- calibration ID。

Refinement：

$$
r_k=b-Ax_k,
$$

$$
x_{k+1}=x_k+\delta_k.
$$

Final evidence 同時保存 physical solve 與 digital correction lineage。

---

## 109. 一個完整例子：photonic matrix transform

Photonic stage：

$$
z_P=W_{\mathrm{opt}}x.
$$

Control plane 同時維持 phase / working point。

Evidence 可以包含：

- optical module ID；
- wavelength；
- controller state digest；
- temperature；
- detector readout；
- calibration/feedback mode；
- raw output；
- digital normalization/refinement。

這讓 photonic result 不再只是一個 host memory 裡的 vector。

---

## 110. 一個完整例子：聲學 demonstrator

聲學版本可能速度較慢，但更容易展示：

$$
\text{input pulse}
\rightarrow
\text{propagation}
\rightarrow
\text{interference}
\rightarrow
\text{readout}.
$$

Scientific profile 可保存 receiver waveform；Demo profile 則同時顯示 propagation visualization。

同一 raw evidence 可以服務人類可觀察與 machine audit。

---

## 111. Result acceptance gate

本文建議 final commit 前至少檢查：

$$
G_R
=
G_{\mathrm{physical}}
\land
G_{\mathrm{cal}}
\land
G_{\mathrm{precision}}
\land
G_{\mathrm{refinement}}
\land
G_{\mathrm{evidence}}.
$$

若任一必要 gate 不成立，不能把 result 升格到宣告的 CRA level。

---

## 112. Result status 要能降級

例如 execution 開始時預計：

$$
R4.
$$

但 raw waveform storage failure，使 cross-replay 不可用。

最後應降為：

$$
R2
$$

或 failure，而不是繼續標 R4。

Assurance 必須反映實際執行，而不是計畫。

---

## 113. Result status 也不能事後升級而不產生新 evidence

如果當下只保存 summary，事後不可能憑 final number 變出 raw trace。

因此：

$$
\boxed{
R_{\mathrm{actual}}
\le
R_{\mathrm{evidence\ captured}}.
}
$$

這是 evidence ceiling。

---

## 114. Calibration uncertainty 不能被 refinement 假裝消失

Digital refinement 可以降低 numerical residual，但若 calibration reference 本身有不確定度：

$$
U_{\mathrm{cal}}>0,
$$

final result 不能因 iteration 很多次就報：

$$
U=0.
$$

不同 uncertainty source 必須正確 propagation。

---

## 115. Model error 也是 ceiling

如果 task model 本身：

$$
y=f_{\mathrm{model}}(x)
$$

與真實工程現象有 model discrepancy，計算得再精確也只是精確求解該 model。

所以：

$$
\boxed{
\text{Numerical Exactness}
\neq
\text{Physical Truth}.
}
$$

這對科研與工程現場尤其重要。

---

## 116. Paper 06 的最低 MVP 要求

第一代 EPCA demonstrator 不需要先做到 CRA-R5。

合理 MVP 可以是：

$$
\boxed{
\mathrm{OPC\mbox{-}V3}
+
\mathrm{ESA\mbox{-}S2}
+
\mathrm{LFA\mbox{-}F2}
+
\mathrm{MSA\mbox{-}M1}
+
\mathrm{CRA\mbox{-}R2}.
}
$$

也就是：physical computation causal、supervisor boundary 已聲明、可離線執行、module boundary 已明確，而且每個 result 至少綁定 raw run 與 calibration。

---

## 117. 科研 prototype 的較高目標

若是公開驗證新型 physical compute substrate，建議：

$$
\boxed{
V4/S4/F3/M3/R5.
}
$$

因為科研爭議往往不是「能不能跑」，而是：

- 有沒有 hidden digital path；
- error 怎麼來；
- calibration 是否有效；
- result 是否可重分析；
- physical claim 是否可被獨立檢查。

---

## 118. 產品版反而可以動態調 CRA

同一台 appliance：

- 普通 field mode：R3；
- diagnostic mode：R4；
- certification test：R5；
- high-throughput screening：R2。

這能避免所有任務都支付最高 evidence cost。

---

## 119. 這使「計算機」重新像儀器

傳統 calculator 通常只給：

$$
y.
$$

科學儀器則常需要：

$$
y+\text{calibration}+\text{uncertainty}+\text{traceability}.
$$

EPCA 將兩者結合：

$$
\boxed{
\text{Calculator}
+
\text{Instrument}
+
\text{Compute Appliance}.
}
$$

這正是它可能在工程與科研現場意外好用的原因之一。

---

## 120. 這也是「讓計算機回到計算本身」的另一層意思

不是把 computer 簡化成只有四則運算。

而是把設備的中心重新放在：

$$
\boxed{
\text{Compute}
+
\text{Know How It Computed}.
}
$$

OS、network、storage、UI 都服務這個中心，而不是反過來把計算淹沒在 general-purpose desktop environment 裡。

---

## 121. Paper 06 的核心不變量

本文總結為六條：

### I. Raw Evidence Before Refinement

$$
R_P\prec F.
$$

### II. Calibration Is Versioned Runtime State

$$
\kappa_t\in\mathcal S_{\mathrm{runtime}}.
$$

### III. Refinement Must Be Declared

$$
F\in\mathrm{Provenance}.
$$

### IV. Refinement Must Not Erase Physical Dependency

$$
\mathrm{Dep}_{P}(y)=1
$$

對宣告為 physical-primary/cooperative result 必須成立。

### V. Precision Claims Are Scoped

$$
Q=(M,K,O,D,\Omega,\epsilon,U).
$$

### VI. Final Result Is an Evidence-Bearing Object

$$
\mathcal O=(y,\mathcal E).
$$

---

## 122. Paper 06 與 Paper 05 的收斂

Paper 05 說：

$$
\boxed{
\text{Preserve Physics}
+
\text{Standardize Interaction}.
}
$$

Paper 06 再加：

$$
\boxed{
\text{Preserve Error Structure}
+
\text{Standardize Result Semantics}.
}
$$

不同 substrate 不必有相同 noise model，但都必須能把 error/calibration/refinement 描述交給 appliance。

---

## 123. 到這裡 EPCA 已經不是一個 accelerator box

EPCA 現在具有：

- independent appliance identity；
- physical compute core；
- supervisor authority separation；
- offline execution closure；
- transactional update/recovery；
- multi-substrate backplane；
- calibration lifecycle；
- mixed-precision composition；
- evidence-bearing result；
- provenance graph。

因此它逐漸形成：

$$
\boxed{
\text{A self-contained computational instrument platform}.
}
$$

---

## 124. 下一篇接口：Benchmark、Routing 與 AI Orchestration

Paper 06 解決：

> 一個 heterogeneous physical result 怎麼變成可信、可用、可審計的 final result？

最後一篇 Paper 07 將處理：

> 當一台 EPCA 同時有多個 substrate、多種 precision path、多種 assurance level、多種成本時，誰決定每一道計算要走哪裡？

因此下一篇會正式建立：

$$
\boxed{
\text{Task}
\rightarrow
\text{Requirement Manifest}
\rightarrow
\text{Candidate Substrates}
\rightarrow
\text{Cost/Assurance Model}
\rightarrow
\text{Execution Plan}.
}
$$

並區分 deterministic routing 與未來 AI orchestration。

---

## 125. 結論：真正的高精度不是假裝物理世界沒有誤差

Physical computing 的工程化，不應建立在以下假設：

$$
\text{physical device}
=
\text{ideal mathematical primitive}.
$$

真正成熟的架構應承認：

$$
\text{device variation},
\text{noise},
\text{drift},
\text{readout},
\text{calibration},
\text{refinement}
$$

都是 computation chain 的一部分。

因此本文提出：

$$
\boxed{
\text{Raw Physical Compute}
\rightarrow
\text{Calibrated Physical Result}
\rightarrow
\text{Declared Mixed-Precision Refinement}
\rightarrow
\text{Evidence-Bearing Final Result}.
}
$$

只要 physical contribution 沒有被 refinement 偷偷抹掉，而且 calibration、uncertainty、refinement、module identity 與 raw evidence 都能被追溯，那麼 heterogeneous mixed precision 不是 physical computing 的妥協，而很可能是它真正進入工程世界的主要形式。

最後可以把 Paper 06 壓縮成一句話：

$$
\boxed{
\text{不要只問答案有幾位；要問這幾位是怎麼來的。}
}
$$

---

## 參考文獻與工程資料

1. Le Gallo, M., Sebastian, A., Mathis, R., et al. (2018). *Mixed-precision in-memory computing*. Nature Electronics, 1, 246-253. DOI: 10.1038/s41928-018-0054-8. https://www.nature.com/articles/s41928-018-0054-8
2. Khwa, W.-S., Wen, T.-H., Hsu, H.-H., et al. (2025). *A mixed-precision memristor and SRAM compute-in-memory AI processor*. Nature, 639, 617-623. DOI: 10.1038/s41586-025-08639-2. https://www.nature.com/articles/s41586-025-08639-2
3. Zuo, P., Wang, Q., Luo, Y., et al. (2025). *Precise and scalable analogue matrix equation solving using resistive random-access memory chips*. Nature Electronics, 8, 1222-1233. DOI: 10.1038/s41928-025-01477-0. https://www.nature.com/articles/s41928-025-01477-0
4. Singh, A., Le Gallo, M., Vasilopoulos, A., et al. (2025). *The design of analogue in-memory computing tiles*. Nature Electronics, 8, 1156-1169. DOI: 10.1038/s41928-025-01537-5. https://www.nature.com/articles/s41928-025-01537-5
5. *Achieving high precision in analog in-memory computing systems*. npj Unconventional Computing (2025). The review discusses slicing, residue-number systems, error-correction codes and iterative refinement as precision/error-mitigation strategies. https://www.nature.com/articles/s44335-025-00044-2
6. Wan, W., Kubendran, R., Schaefer, C., et al. (2022). *A compute-in-memory chip based on resistive random-access memory*. Nature, 608, 504-512. DOI: 10.1038/s41586-022-04992-8. https://www.nature.com/articles/s41586-022-04992-8
7. Le Gallo, M., Khaddam-Aljameh, R., Stanisavljević, M., et al. (2023). *A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference*. Nature Electronics. This work is a representative large-scale mixed-signal AIMC architecture and motivates system-level treatment of converters, memory states and calibration.
8. Yao, P., Zhang, Q., Tang, J., Qian, H., Wu, H., et al. (2025). *A full-stack memristor-based computation-in-memory system with software-hardware co-development*. Nature Communications, 16, 2123. https://www.nature.com/articles/s41467-025-57183-0
9. Sacchi, E., Zanetto, F., Martinez, A. I., et al. (2025). *Integrated electronic controller for dynamic self-configuration of photonic circuits*. Light: Science & Applications, 14, 348. DOI: 10.1038/s41377-025-01977-w. https://www.nature.com/articles/s41377-025-01977-w
10. National Institute of Standards and Technology. *NIST Policy on Metrological Traceability*. NIST states metrological traceability as a property of a measurement result related to a reference through a documented unbroken chain of calibrations, each contributing to measurement uncertainty. https://www.nist.gov/calibrations/traceability
11. National Institute of Standards and Technology. *Metrological Traceability: Frequently Asked Questions and NIST Policy*. https://www.nist.gov/metrology/metrological-traceability
12. Ehrlich, C. D. (2016). *Traceability Considerations for the Characterization and Use of Measuring Systems*. NIST. https://www.nist.gov/publications/traceability-considerations-characterization-and-use-measuring-systems-0
13. World Wide Web Consortium. *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. https://www.w3.org/TR/prov-dm/
14. World Wide Web Consortium. *PROV Model Primer*. W3C Working Group Note, 30 April 2013. https://www.w3.org/TR/prov-primer/

---

## 前置系列與本系列銜接

- 《跨尺度構成與動態約束域研究》v0.1：approximability、finite-cost exactness、effective physical equivalence、dynamic reachability 與 constraint domain。
- 《認知功能體的物理實現與自然可觀測性研究》v0.1：存在、可觀測、可辨識、跨 substrate functional realization 與 causal history separation。
- Paper 00：EPCA、Local Execution Closure、Physical-Core Non-Substitution 與 Evidence-Bearing Result 的初步提出。
- Paper 01：Carrier-Generalized Abacus、position coding、mode coding、relation coding 與 dynamical geometry。
- Paper 02：OPC-V0 至 OPC-V5、causal intervention、ablation、independent challenge 與 falsifiable physical evidence。
- Paper 03：Declared Compute Boundary、No Silent Substitution、Reference-Path Isolation、Evidence Before Refinement 與 ESA-S0 至 ESA-S5。
- Paper 04：Local Execution Closure、transactional update、offline evidence queue、field recovery 與 LFA-F0 至 LFA-F5。
- Paper 05：Multi-Substrate Compute Backplane、Physical Module Contract、capability descriptor、calibration gate、module lifecycle、fault containment 與 MSA-M0 至 MSA-M5。

本篇新增 Mixed-Precision Evidence-Bearing Computation、calibration bundle/lifecycle、error and uncertainty taxonomy、precision negotiation、adaptive/iterative refinement、Refinement Non-Erasure、Physical Contribution Class、evidence/provenance memory、Evidence Envelope、result identity、offline provenance closure 與 CRA-R0 至 CRA-R5。從這裡開始，EPCA 的 final output 不再被視為單一 scalar/vector，而是帶有 physical lineage、calibration、precision 與 refinement history 的 computation object。下一篇將以此為基礎，完成 benchmark、routing、execution planning 與未來 AI orchestration 的總收斂。
