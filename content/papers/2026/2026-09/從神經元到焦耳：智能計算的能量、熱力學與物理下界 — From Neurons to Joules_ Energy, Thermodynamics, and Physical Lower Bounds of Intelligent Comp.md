# 從神經元到焦耳：智能計算的能量、熱力學與物理下界

## From Neurons to Joules: Energy, Thermodynamics, and Physical Lower Bounds of Intelligent Computation

**系列：**《智能的物理計量：從最小語意執行到成果品質與計算時空》  
**英文系列：** *Physical Metrology of Intelligence: From Minimal Semantic Execution to Quality and Computational Spacetime*  
**系列編號：** EML-IPM  
**篇次：** Paper 04 / 10  
**文件編號：** EML-IPM-04  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開純理論論文／跨學科方法論  
**工程狀態：** 無 MVP；本文建立智能計算由生物電事件向能源、熱與熱力學下界對映的理論骨架

---

## 摘要

IPM Paper 02 提出了最小智能語意執行單位：

$$
\boxed{
\mu_I:
z_t\rightarrow z_{t+1}
}
$$

Paper 03 則指出，認知科學與神經科學並沒有一個：

$$
1\ \text{thought}
=
N\ \text{spikes}
$$

的普適換算，而是透過多層 proxy、latent model、population code 與 causal perturbation 建立跨層證據。

本篇繼續向下追問：

$$
\boxed{
\textbf{
當一個神經事件真正發生時，
它如何一路變成 ATP、Joule、heat 與 entropy production？
}
}
$$

神經能量學提供了一個非常重要的方法論範例。研究者不是把「一個 spike」直接指定成某個固定能量，而是從底層物理過程逐步建立能量帳本：

$$
\boxed{
\text{Membrane Dynamics}
\rightarrow
\text{Ion Flux}
\rightarrow
\text{Pump Work}
\rightarrow
\text{ATP}
\rightarrow
\text{Energy Dissipation}.
}
$$

對 action potential 而言，若鈉離子流入總電荷為：

$$
Q_{Na}
=
\int I_{Na}(t)\,dt,
$$

則流入的鈉離子數可近似寫成：

$$
\boxed{
N_{Na}
=
\frac{Q_{Na}}{e}
}
$$

其中 $e$ 是基本電荷。

由於 Na $^+$ /K $^+$ ATPase 每消耗一個 ATP 可移出 3 個 Na $^+$，最低恢復成本可粗略表示為：

$$
\boxed{
N_{ATP}^{Na}
\approx
\frac{N_{Na}}{3}.
}
$$

再由 ATP 水解自由能 $\Delta G_{ATP}$ 得：

$$
\boxed{
E_{AP}
\approx
N_{ATP}^{Na}\Delta G_{ATP}
+
E_{\text{other}}.
}
$$

其中 $E_{\text{other}}$ 包含鈣離子處理、突觸、傳遞物回收、維持靜息電位等其他代謝成本。

這個 bottom-up accounting 的核心教訓是：

$$
\boxed{
\text{observable event type}
\neq
\text{fixed physical cost}.
}
$$

不同 neuron 的 action potential 即使外部形狀相似，其 Na $^+$ 與 K $^+$ currents overlap、channel kinetics 與膜性質仍可能讓能量成本相差超過一個數量級。因此：

$$
\boxed{
1\ \text{spike}
\neq
1\ \text{fixed Joule}.
}
$$

這對 AI 具有直接類比：

$$
\boxed{
1\ \text{token}
\neq
1\ \text{fixed Joule},
}
$$

$$
\boxed{
1\ \mu_I
\neq
1\ \text{fixed Joule}.
}
$$

本文進一步借鑑 cerebral energy budget。更新後的 cortical budget 顯示，大腦 signaling energy 並非主要只花在 action potential；在一個 cerebral cortex 模型中，大約 50% signaling energy 用於 postsynaptic glutamate receptors、21% 用於 action potentials、20% 用於 resting potentials，其餘用於 presynaptic transmitter release 與 transmitter recycling。

這意味：

$$
\boxed{
\text{communication}
+
\text{state maintenance}
+
\text{synaptic integration}
}
$$

往往和「顯眼的神經脈衝」一樣甚至更加昂貴。

對 AI 同樣不能只數 tensor arithmetic。真正的能源帳本還必須包含：

- memory movement；
- state residency；
- interconnect；
- synchronization；
- storage；
- cooling / infrastructure share。

本文因此區分四種能源量：

$$
\boxed{
\mathcal E=
(
E_{\mathrm{gross}},
E_{\mathrm{base}},
E_{\mathrm{marg}},
E_{\mathrm{attrib}}
).
}
$$

其中：

- $E_{\mathrm{gross}}$：任務期間整個被觀察系統的總能源；
- $E_{\mathrm{base}}$：即使不執行該任務仍需支付的基線能源；
- $E_{\mathrm{marg}}$：因該任務額外產生的邊際能源；
- $E_{\mathrm{attrib}}$：依既定分攤規則歸因給該任務的總成本。

形式上：

$$
\boxed{
E_{\mathrm{gross}}
=
\int_{t_0}^{t_f}
P_{\mathrm{system}}(t)\,dt
}
$$

$$
\boxed{
E_{\mathrm{base}}
=
\int_{t_0}^{t_f}
P_{\mathrm{baseline}}(t)\,dt
}
$$

$$
\boxed{
E_{\mathrm{marg}}
=
\int_{t_0}^{t_f}
\left[
P_{\mathrm{system}}(t)
-
P_{\mathrm{baseline}}(t)
\right]dt.
}
$$

因此：

$$
\boxed{
E_{\mathrm{gross}}
\neq
E_{\mathrm{marg}}.
}
$$

這對人腦尤其重要：成人腦整體代謝大約為 20 W 等級，而 goal-directed cognition 相對 ongoing resting neural activity / homeostasis 的增量可能只占少量比例。這說明：

$$
\boxed{
\text{Brain Is Expensive}
\neq
\text{Every Thought Is Equally Expensive}.
}
$$

同樣地，資料中心或 GPU 本來就存在：

- idle power；
- memory refresh；
- model residency；
- networking；
- cooling。

因此不能把任務期間所有電錶讀數直接視為該答案的純增量成本。

本文再區分 **實際成本** 與 **熱力學下界**。

Landauer principle 在特定條件下指出，對一個 logical irreversible bit erasure：

$$
\boxed{
E_{\mathrm{erase,min}}
=
k_B T\ln2.
}
$$

但這不是：

$$
\boxed{
1\ \text{bit of reasoning}
=
k_B T\ln2.
}
$$

也不是：

$$
\boxed{
1\ \mu_I
=
k_B T\ln2.
}
$$

Landauer bound 描述的是特定資訊抹除過程的物理最低耗散條件，不是完整神經計算、AI inference 或語意推理的實際能耗。

因此本文建立：

$$
\boxed{
E_{\mathrm{actual}}
\gg
E_{\mathrm{thermo,min}}
}
$$

作為通常情況下的實務認知，而不是把理論下界當成 benchmark 實測值。

Laughlin 等人的經典 neural information measurements 甚至顯示，在其特定 blowfly sensory system 中，chemical synapse 傳一 bit 的成本約為 $10^4$ ATP，而某些 graded 或 spike signaling 的估計可達 $10^6$ – $10^7$ ATP/bit，遠高於純熱力學極限。

因此：

$$
\boxed{
\text{Information Efficiency}
=
\frac{\text{task-relevant information}}{E}
}
$$

可以是一個有用量，

但：

$$
\boxed{
\text{Information per Joule}
\neq
\text{Intelligence per Joule}.
}
$$

因為資訊傳輸不必然等同語意求解。

本文最後提出 IPM 的 **語意—物理—熱力學三重分離**：

$$
\boxed{
W_{\mu}^{semantic}
\neq
W^{computational}
\neq
E^{thermodynamic}.
}
$$

並建立向下映射：

$$
\boxed{
\mu_I
\rightarrow
\rho_C(\mu_I)
\rightarrow
\rho_P(\mu_I)
\rightarrow
\rho_T(\mu_I).
}
$$

真正的 IPM 問題因此不是：

> 一個 token 要多少焦耳？

而是：

$$
\boxed{
\textbf{
為了實現某個已確認的有效語意轉換，
實際硬體必須造成多少物理狀態變化、
搬移多少資訊、持續多久，最後耗散多少能量？
}
}
$$

---

# 1. 從 spike 往下走，而不是把 spike 當終點

Paper 03 已指出：

$$
\boxed{
Spike
\neq
CognitiveUnit.
}
$$

但 spike 仍是一個相對容易觀察的物理事件。

所以它可以作為：

$$
\boxed{
\text{intermediate physical proxy}.
}
$$

---

# 2. Action potential 的能量來源

Action potential 涉及膜上的：

- Na $^+$ influx；
- K $^+$ efflux；
- voltage-gated channels；
- membrane capacitance。

事件結束後，離子濃度梯度必須恢復。

---

# 3. Na/K pump 是主要恢復機制之一

Na $^+$ /K $^+$ ATPase 利用 ATP：

$$
\boxed{
3Na^+_{\mathrm{out}}
+
2K^+_{\mathrm{in}}
\quad
\text{per ATP}.
}
$$

因此 ionic movement 可以往 ATP accounting 映射。

---

# 4. 從電流到離子數

若鈉離子電流為：

$$
I_{Na}(t),
$$

則總電荷：

$$
\boxed{
Q_{Na}
=
\int I_{Na}(t)\,dt.
}
$$

---

# 5. 再到離子個數

$$
\boxed{
N_{Na}
=
\frac{Q_{Na}}{e}.
}
$$

這使 electrophysiological measurement 可以往 molecular energetic accounting 下沉。

---

# 6. 再從離子個數到 ATP

若主要恢復由 Na/K pump 完成：

$$
\boxed{
N_{ATP}
\approx
\frac{N_{Na}}{3}.
}
$$

這只是主要成分估計，而不是完整 neuron energy。

---

# 7. 從 ATP 到 Joule

令每個 ATP 水解在實際細胞條件下可用自由能為：

$$
\Delta G_{ATP}.
$$

則：

$$
\boxed{
E
=
N_{ATP}\Delta G_{ATP}.
}
$$

---

# 8. 這條鏈本身就值得 IPM 借用

$$
\boxed{
\text{Observable Signal}
\rightarrow
\text{Physical Flux}
\rightarrow
\text{Chemical Work}
\rightarrow
\text{Energy}.
}
$$

而不是：

$$
\boxed{
\text{Observable Signal}
\rightarrow
\text{arbitrary energy constant}.
}
$$

---

# 9. 一個 spike 沒有固定能量

這是非常重要的結果。

不同 neuron 的 action potential：

- Na/K current overlap 不同；
- channel kinetics 不同；
- membrane area 不同；
- capacitance 不同。

---

# 10. 所以外觀相似的 spike

可以：

$$
E_{AP,A}
\gg
E_{AP,B}.
$$

---

# 11. 甚至形狀不是良好能源 proxy

研究顯示 AP 的 width / height 並不足以可靠預測它的 energy consumption。

因此：

$$
\boxed{
SignalShape
\neq
EnergyCost.
}
$$

---

# 12. IPM 的直接對應

同樣：

$$
\boxed{
OutputLength
\neq
EnergyCost.
}
$$

也就是：

$$
\boxed{
TokenCount
\neq
Joule.
}
$$

---

# 13. 同一語意單位也沒有固定 Joule

Paper 02 的：

$$
\mu_I
$$

是 semantic type。

它在不同架構上：

$$
\rho_P^A(\mu_I)
\neq
\rho_P^B(\mu_I).
$$

所以：

$$
\boxed{
E_A(\mu_I)
\neq
E_B(\mu_I).
}
$$

---

# 14. 這才使「智能能效」成為有意義的比較

如果相同語意工作：

$$
[\mu_I]
$$

在 A 上花：

$$
E_A
$$

在 B 上花：

$$
E_B,
$$

才能比較 realization efficiency。

---

# 15. 神經能量預算不是只算 action potential

早期與更新後 cortical energy budget 都顯示：

真正的 signaling cost 來自多個部分。

---

# 16. Cerebral cortex 更新預算的典型分配

一個更新模型估計：

$$
\boxed{
\sim50\%
}
$$

signaling energy 在 postsynaptic glutamate receptors。

---

# 17. Action potentials

約：

$$
\boxed{
21\%.
}
$$

---

# 18. Resting potentials

約：

$$
\boxed{
20\%.
}
$$

---

# 19. 其餘

包括：

- presynaptic transmitter release；
- transmitter recycling。

---

# 20. 這告訴我們：「顯眼運算」不是全部成本

神經 spike 最顯眼。

但能量大頭可能在：

$$
\boxed{
\text{integration + maintenance + communication}.
}
$$

---

# 21. AI 同樣如此

AI 系統不能只量：

$$
FLOPs.
$$

還要量：

- HBM reads/writes；
- KV/cache residency；
- interconnect；
- synchronization；
- routing；
- CPU/GPU coordination。

Paper 05 將正式展開這些。

---

# 22. 神經系統的 state maintenance 很昂貴

即使沒有顯式外部任務，大腦仍需要：

- resting potential；
- housekeeping；
- synaptic maintenance；
- spontaneous activity。

---

# 23. 所以需要 baseline

$$
\boxed{
P_{\mathrm{base}}(t).
}
$$

---

# 24. 人腦約 20 W 不是「20 W/思考」

它代表整個 brain 的持續 metabolic power 等級。

---

# 25. 高階認知新增的能量可能只是一小部分

這形成：

$$
\boxed{
\text{High Baseline}
+
\text{Small Task Delta}.
}
$$

---

# 26. 因此單一任務成本必須至少分三種

### Gross Energy

$$
\boxed{
E_{\mathrm{gross}}
=
\int P_{\mathrm{system}}(t)\,dt.
}
$$

---

# 27. Baseline Energy

$$
\boxed{
E_{\mathrm{base}}
=
\int P_{\mathrm{baseline}}(t)\,dt.
}
$$

---

# 28. Marginal Task Energy

$$
\boxed{
E_{\mathrm{marg}}
=
E_{\mathrm{gross}}
-
E_{\mathrm{base}}.
}
$$

---

# 29. 但實際系統還有 shared overhead

例如 AI data center：

- cooling；
- network switches；
- model servers；
- memory refresh。

這些不是純 idle，也不是某個 request 完全獨占。

---

# 30. 因此加入 Attributed Energy

$$
\boxed{
E_{\mathrm{attrib}}
=
E_{\mathrm{marg}}
+
\alpha E_{\mathrm{shared}}.
}
$$

其中 $\alpha$ 是明示的 allocation rule。

---

# 31. 四種能源量

$$
\boxed{
\mathcal E=
(
E_{\mathrm{gross}},
E_{\mathrm{base}},
E_{\mathrm{marg}},
E_{\mathrm{attrib}}
).
}
$$

---

# 32. 這四個不能混用

如果研究問題是：

> 這次 request 額外用了多少電？

應優先看：

$$
E_{\mathrm{marg}}.
$$

---

# 33. 如果問：

> 這個服務每次回答平均應承擔多少總能源？

可能看：

$$
E_{\mathrm{attrib}}.
$$

---

# 34. 如果問 data-center 當下真實用電

才是：

$$
E_{\mathrm{gross}}.
$$

---

# 35. 所以能源單位相同，不代表測量問題相同

全部都是 Joule。

但語意不同。

---

# 36. Joule 也需要 Type

可以寫：

$$
\boxed{
J[\mathrm{gross}],
J[\mathrm{marg}],
J[\mathrm{attrib}].
}
$$

避免報告時偷換。

---

# 37. 神經資訊效率：ATP per bit

神經科學進一步試過把：

$$
\text{information}
$$

與：

$$
\text{energy}
$$

直接耦合。

---

# 38. 經典形式

$$
\boxed{
\eta_{I/E}
=
\frac{I}{E}.
}
$$

或者：

$$
\boxed{
C_{E/I}
=
\frac{E}{I}.
}
$$

---

# 39. Laughlin 等人的經典估計

在其特定 blowfly sensory system 中，chemical synapse 傳輸一 bit 約：

$$
\boxed{
10^4\ ATP/bit.
}
$$

---

# 40. 某些 graded / spike signals

則可能達：

$$
\boxed{
10^6\sim10^7\ ATP/bit.
}
$$

---

# 41. 這些不是宇宙常數

它們依賴：

- organism；
- cell type；
- coding scheme；
- signal rate；
- noise。

---

# 42. 所以真正可借的是方法

$$
\boxed{
\text{information carried}
\div
\text{physical energy}.
}
$$

不是數值本身。

---

# 43. Information per Joule 仍不是 Intelligence per Joule

例如：

一條網路傳輸大量 random bits。

$$
I\gg0.
$$

但：

$$
\mu_I^{eff}=0.
$$

---

# 44. 所以：

$$
\boxed{
Information
\neq
\text{Task-Relevant Semantic Work}.
}
$$

---

# 45. IPM 需要一個更高層 numerator

Paper 02：

$$
N_{\mu}^{eff}.
$$

---

# 46. 因此：

$$
\boxed{
\eta_{\mu/E}
=
\frac{
N_{\mu}^{eff}
}{
E_{\mathrm{marg}}
}.
}
$$

才比較接近 semantic-energy efficiency。

---

# 47. 但 $N_\mu$ 仍不等於成果品質

所以最終還需要：

$$
\boxed{
\eta_{Q/E}
=
\frac{
Q
}{
E_{\mathrm{marg}}
}.
}
$$

---

# 48. 三條效率鏈

$$
\boxed{
\eta_{I/E}
=
\frac{I}{E}
}
$$

資訊能效。

---

# 49. 語意能效

$$
\boxed{
\eta_{\mu/E}
=
\frac{N_{\mu}^{eff}}{E}.
}
$$

---

# 50. 成果能效

$$
\boxed{
\eta_{Q/E}
=
\frac{Q}{E}.
}
$$

---

# 51. 三者不可等同

$$
\boxed{
\eta_{I/E}
\neq
\eta_{\mu/E}
\neq
\eta_{Q/E}.
}
$$

---

# 52. 現在進入 Landauer principle

Landauer 的核心命題針對：

$$
\boxed{
\text{logically irreversible information erasure}.
}
$$

---

# 53. 在理想條件下

刪除一 bit 的最低熱耗散：

$$
\boxed{
E_L
=
k_BT\ln2.
}
$$

---

# 54. 這是一個 fundamental bound

但它的適用對象是：

$$
\boxed{
\text{erasure}.
}
$$

不是：

$$
\boxed{
\text{all computation}.
}
$$

---

# 55. 所以最常見的錯誤寫法

$$
\boxed{
1\ bit\ computation
=
k_BT\ln2
}
$$

不成立。

---

# 56. 更錯的是

$$
\boxed{
1\ \mu_I
=
k_BT\ln2.
}
$$

---

# 57. $\mu_I$ 可能需要抹除很多物理 bit

也可能由接近 reversible 的中間過程實現。

---

# 58. 真正需要的是 physical implementation graph

令：

$$
N_{\mathrm{erase}}
$$

為某一實作中實際需要的 logically irreversible bit erasures。

---

# 59. 才有理論下界

$$
\boxed{
E_{\mathrm{Landauer}}
\ge
N_{\mathrm{erase}}k_BT\ln2.
}
$$

---

# 60. 但 $N_{\mathrm{erase}}$ 本身通常非常難從高階任務直接得到

所以不能從：

$$
TokenCount
$$

直接推出：

$$
E_{\mathrm{Landauer}}.
$$

---

# 61. Landauer Distance

如果能合理估計下界，可定義：

$$
\boxed{
D_L
=
\frac{
E_{\mathrm{actual}}
}{
E_{\mathrm{Landauer}}
}.
}
$$

---

# 62. 但 $D_L$ 只表示 implementation 距離物理下界多遠

不是 intelligence score。

---

# 63. 所以：

$$
\boxed{
D_L
\neq
IntelligenceEfficiency.
}
$$

---

# 64. 實際系統遠高於 Landauer limit 很正常

原因包括：

- noise；
- reliability；
- finite-time operation；
- control；
- memory movement；
- nonideal hardware；
- cooling；
- communication。

---

# 65. 神經系統就是很好的例子

實測 biological signaling cost 可比純 thermodynamic minimum 高許多數量級。

這不代表大腦「違反熱力學最佳化」。

---

# 66. 因為演化最佳化的是多目標

例如：

$$
\boxed{
Energy
+
Speed
+
Reliability
+
Robustness
+
Adaptability.
}
$$

---

# 67. 所以真正的 optimum 通常不是最低 Joule

而是 Pareto optimum。

---

# 68. 這和 AI 完全一致

一個超省電但 10 小時才回答的模型，

未必優於：

- 稍微耗電；
- 但 1 秒完成；
- 更可靠的模型。

---

# 69. 因此：

$$
\boxed{
\min E
\neq
\max IntelligenceUtility.
}
$$

---

# 70. 熱力學還提供第二條橋：entropy production

非平衡系統中，運算與 state transition 會伴隨：

$$
\boxed{
\Sigma
=
\text{entropy production}.
}
$$

---

# 71. Information thermodynamics

進一步研究：

$$
\boxed{
\text{Information Flow}
\leftrightarrow
\text{Energy / Heat / Entropy Production}.
}
$$

---

# 72. 這對 neural inference 很重要

因為 neuron / synapse 是 noisy stochastic systems。

所以：

$$
\boxed{
\text{uncertainty reduction}
}
$$

不需要與 physical energy 分開研究。

---

# 73. 但仍不能把 Shannon entropy 當 physical entropy

兩者可以有正式關係。

但：

$$
\boxed{
H_{\mathrm{Shannon}}
\neq
S_{\mathrm{thermodynamic}}
}
$$

沒有指定系統與映射時不能直接當等號。

---

# 74. 同樣 variational free energy 也不是直接 Joule

認知科學中：

$$
F_{\mathrm{variational}}
$$

是一個統計／資訊量。

---

# 75. 而：

$$
F_{\mathrm{thermodynamic}}
$$

是物理熱力學量。

---

# 76. 所以：

$$
\boxed{
VariationalFreeEnergy
\neq
PhysicalEnergy
}
$$

除非另有明確物理模型建立映射。

---

# 77. 這是 IPM 的 Thermodynamic Type Safety

任何物理能源值都必須有：

$$
\boxed{
Joule.
}
$$

---

# 78. 資訊或語意函數不能因為名稱有 energy/free energy 就直接混入

---

# 79. Baseline Paradox

現在回到認知成本。

如果 brain 維持：

$$
P_{\mathrm{base}}\approx20W,
$$

做任務只增加少量：

$$
\Delta P,
$$

那單題「耗能」怎麼算？

---

# 80. 若全部算 gross

回答 1 秒：

$$
E\approx20J.
$$

但這包含本來就會消耗的 baseline。

---

# 81. 若只算 marginal

可能：

$$
E_{\mathrm{marg}}\ll20J.
$$

---

# 82. 兩者都不是錯

它們回答不同問題。

---

# 83. Gross 問：

> 物理系統在這段時間總共用了多少能量？

---

# 84. Marginal 問：

> 因為執行這個任務，多用了多少？

---

# 85. Attributed 問：

> 若要把維持系統存在的成本公平分攤，每題應負擔多少？

---

# 86. 所以智能產率至少要指定分母類型

例如：

$$
\boxed{
\eta_{Q/E}^{marg}
=
\frac{Q}{E_{\mathrm{marg}}}
}
$$

---

# 87. 或：

$$
\boxed{
\eta_{Q/E}^{attrib}
=
\frac{Q}{E_{\mathrm{attrib}}}.
}
$$

---

# 88. 不能只寫：

$$
\frac{Q}{E}
$$

卻不說 $E$ 是什麼。

---

# 89. AI 也需要 Idle-Matched Baseline

假設 GPU idle：

$$
P_{idle}.
$$

---

# 90. request 執行時：

$$
P_{req}(t).
$$

---

# 91. 則最基本：

$$
\boxed{
E_{\mathrm{marg}}
=
\int
[P_{req}(t)-P_{idle}]dt.
}
$$

---

# 92. 但 shared batching 會更複雜

同一 GPU 同時跑很多 request。

所以 per-request energy attribution 不是單純除法。

Paper 05 再處理。

---

# 93. 目前先建立 Energy Boundary

任何報告必須標明：

$$
\boxed{
Boundary_E
}
$$

---

# 94. 可以是：

- accelerator only；
- node；
- rack；
- data center；
- full infrastructure；
- lifecycle。

---

# 95. 兩份 Joule 如果 boundary 不同

不可直接比較。

---

# 96. 因此：

$$
\boxed{
E
=
E(
Boundary,
BaselineRule,
AttributionRule
).
}
$$

---

# 97. 這是能源計量最重要的 meta-data

---

# 98. Neural Energy Accounting 給 IPM 的七個借鑑

本文定義：

$$
\boxed{
\mathcal B_E=
(
B_F,B_B,B_M,B_I,B_L,B_T,B_P
)
}
$$

---

# 99. $B_F$ — Flux Accounting

從實際物理流量往上算。

---

# 100. $B_B$ — Baseline Separation

基線與 task delta 分開。

---

# 101. $B_M$ — Multi-Component Budget

不要只計算最顯眼的 event。

---

# 102. $B_I$ — Information–Energy Separation

資訊量與能源量型別分離。

---

# 103. $B_L$ — Lower-Bound Discipline

熱力學下界不冒充實際成本。

---

# 104. $B_T$ — Thermodynamic Type Safety

Shannon / variational / physical entropy-energy 不偷換。

---

# 105. $B_P$ — Pareto Efficiency

能源不是唯一目標。

---

# 106. 對 $\mu_I$ 的能源實現向量

現在可以寫：

$$
\boxed{
\mathcal E_{\mu}
=
(
E_{\mathrm{gross}},
E_{\mathrm{marg}},
E_{\mathrm{attrib}},
E_{\mathrm{thermo,min}}
).
}
$$

---

# 107. 但一個 $\mu_I$ 不必有唯一固定值

更合理：

$$
\boxed{
\mathcal E_{\mu}
\sim
P(
E
\mid
\mu_I,
Architecture,
Hardware,
Context,
Boundary
).
}
$$

---

# 108. 這是一個 realization distribution

不是常數表。

---

# 109. 同一個語意 operation

可能：

$$
E_{\mu}^{Transformer}
\neq
E_{\mu}^{Symbolic}
\neq
E_{\mu}^{Brain}.
$$

---

# 110. 這才是跨基質智能計量真正有趣的地方

我們不是要證明：

> 人腦和 Transformer 一樣。

---

# 111. 而是問：

$$
\boxed{
\text{EquivalentSemanticWork}
\rightarrow
\text{DifferentPhysicalCost}.
}
$$

---

# 112. 能源還有時間問題

功率：

$$
P(t)
$$

與總能量：

$$
E=\int Pdt
$$

不同。

---

# 113. 兩系統都用 100 J

但：

$$
T_A=1s
$$

$$
T_B=100s.
$$

使用價值不同。

---

# 114. 所以 Paper 05 必須引入 computational spacetime

能源只是一條投影。

---

# 115. IPM 不能被簡化成「每焦耳 IQ」

如果只用：

$$
Q/J,
$$

會漏掉：

- latency；
- hardware occupancy；
- memory；
- parallelism；
- spatial resource。

---

# 116. 但 Joule 仍是最重要的跨基質共同物理量之一

因為：

$$
\boxed{
\text{all real computation consumes physical resources}.
}
$$

---

# 117. 十四個 Canonical Invariants

**Invariant 1**

$$
\boxed{
Spike
\neq
FixedEnergyUnit.
}
$$

**Invariant 2**

$$
\boxed{
Token
\neq
FixedEnergyUnit.
}
$$

**Invariant 3**

$$
\boxed{
\mu_I
\neq
FixedEnergyUnit.
}
$$

**Invariant 4**

$$
\boxed{
SignalShape
\neq
EnergyCost.
}
$$

**Invariant 5**

$$
\boxed{
GrossEnergy
\neq
MarginalEnergy.
}
$$

**Invariant 6**

$$
\boxed{
MarginalEnergy
\neq
AttributedEnergy.
}
$$

**Invariant 7**

$$
\boxed{
InformationPerJoule
\neq
IntelligencePerJoule.
}
$$

**Invariant 8**

$$
\boxed{
LandauerBound
\neq
ActualComputationCost.
}
$$

**Invariant 9**

$$
\boxed{
1\mu_I
\neq
k_BT\ln2.
}
$$

**Invariant 10**

$$
\boxed{
ShannonEntropy
\neq
ThermodynamicEntropy
}
$$

without an explicit mapping.

**Invariant 11**

$$
\boxed{
VariationalFreeEnergy
\neq
PhysicalEnergy.
}
$$

**Invariant 12**

$$
\boxed{
MinimumEnergy
\neq
MaximumUtility.
}
$$

**Invariant 13**

$$
\boxed{
EnergyComparison
\Rightarrow
SameBoundary.
}
$$

**Invariant 14**

$$
\boxed{
SemanticWork
\neq
ThermodynamicWork.
}
$$

---

# 118. 對 IPM 統一事件向量的擴張

Paper 03：

$$
\mathfrak E''=
(
Q,
\mathbf N_{\mu},
Conf_{\mu},
Grade_{\mu},
U,G,I,L,R,S,T,E,V_{CST}
).
$$

---

# 119. 現在把 $E$ 展開：

$$
\boxed{
\mathfrak E'''=
(
Q,
\mathbf N_{\mu},
Conf_{\mu},
Grade_{\mu},
U,G,I,L,R,S,T,
\mathcal E,
Boundary_E,
V_{CST}
)
}
$$

其中：

$$
\boxed{
\mathcal E=
(
E_{\mathrm{gross}},
E_{\mathrm{base}},
E_{\mathrm{marg}},
E_{\mathrm{attrib}},
E_{\mathrm{thermo,min}}
).
}
$$

---

# 120. 這是第一次讓「一個答案用了多少電」變成可重現的科學問題

不再只說：

> 大約用了 5 Joules。

而是要說：

- 哪個 boundary？
- gross 還是 marginal？
- baseline 怎麼定？
- shared overhead 怎麼分？
- Landauer 是不是只是 lower bound？

---

# 121. 能源 measurement grade

本文再補充：

### E-Grade D — Estimated

由 TDP、FLOPs 或公開規格推估。

---

# 122. E-Grade C — Device Telemetry

有 GPU / CPU power telemetry。

---

# 123. E-Grade B — Node-Level Meter

有完整節點實測。

---

# 124. E-Grade A — Infrastructure Meter

包含 power supply、network、cooling 等指定 boundary。

---

# 125. E-Grade A+ — Marginal Causal Energy

有 matched baseline / randomized workload，可估計 causal marginal task energy。

---

# 126. 因為能源也不能只報一個假精確數字

如果只是拿 GPU TDP 乘時間，

不應假裝是：

$$
E_{\mathrm{true}}.
$$

---

# 127. 所以：

$$
\boxed{
EnergyEstimate
+
MeasurementGrade
+
Boundary
}
$$

必須一起報。

---

# 128. 結論：智能進入物理世界後，任何語意都必須付出實現成本

人腦能量學最重要的貢獻，不是告訴我們：

> 一個 spike 固定值多少 Joule。

恰恰相反。

它證明：

$$
\boxed{
\textbf{
同一種可見神經事件，
可以因底層離子動力學與系統架構不同，
具有完全不同的實際能量成本。
}
}
$$

因此，智能物理計量不能建立：

$$
Token\rightarrow Joule
$$

的簡單表。

也不能建立：

$$
\mu_I\rightarrow ConstantJoule.
$$

真正的結構是：

$$
\boxed{
\mu_I
\rightarrow
\rho_C
\rightarrow
\rho_P
\rightarrow
\rho_T.
}
$$

而 $\rho_T$ 的輸出還要分：

$$
\boxed{
E_{\mathrm{gross}},
E_{\mathrm{base}},
E_{\mathrm{marg}},
E_{\mathrm{attrib}},
E_{\mathrm{thermo,min}}.
}
$$

Landauer principle 則只提供其中最底層的理論約束之一：

$$
\boxed{
E_{\mathrm{erase,min}}
=
k_BT\ln2
}
$$

它不是智能的價格。

不是 reasoning 的價格。

不是一個 $\mu_I$ 的價格。

它只是提醒我們：

$$
\boxed{
\textbf{
資訊處理最終不是抽象魔法；
當資訊被物理系統操作，
至少有部分邏輯轉換會受到熱力學不可逃避的約束。
}
}
$$

更重要的是，大腦也提醒我們：

$$
\boxed{
\text{Baseline}
\gg
\text{TaskDelta}
}
$$

完全可能成立。

所以如果未來有人說：

> 這個 AI 回答用了 100 J。

我們第一個問題不應該是：

> 那它效率高不高？

而應該先問：

> 這 100 J 是 gross、marginal 還是 attributed？

再問：

> 它完成了多少有效 $\mu_I$？

最後才問：

> 產生了多少品質 $Q$？

這才形成：

$$
\boxed{
\text{Physical Energy}
\rightarrow
\text{Semantic Work}
\rightarrow
\text{Task Quality}.
}
$$

但即使到了這裡，能源仍只是一條物理軸。

一個模型可能：

- Joule 很少；
- 卻占用大量 memory 很久；

另一個：

- Joule 相近；
- 卻使用 64 張 GPU 平行完成；

又或者兩者 FLOPs 相同，但 memory movement 完全不同。

因此下一篇必須回答：

$$
\boxed{
\textbf{
如果計算成本不只有 FLOPs 與 Joules，
那真正的「計算時空」到底由什麼組成？
}
}
$$

這就是 Paper 05：

**《計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積》**。

---

## 文獻基礎

[1] Attwell, D., & Laughlin, S. B. (2001). An Energy Budget for Signaling in the Grey Matter of the Brain. *Journal of Cerebral Blood Flow & Metabolism*, 21(10), 1133–1145. DOI: 10.1097/00004647-200110000-00001.  

[2] Howarth, C., Gleeson, P., & Attwell, D. (2012). Updated energy budgets for neural computation in the neocortex and cerebellum. *Journal of Cerebral Blood Flow & Metabolism*, 32(7), 1222–1232. DOI: 10.1038/jcbfm.2012.35.  

[3] Laughlin, S. B., de Ruyter van Steveninck, R. R., & Anderson, J. C. (1998). The metabolic cost of neural information. *Nature Neuroscience*, 1, 36–41. DOI: 10.1038/236.  

[4] Sengupta, B., Stemmler, M., Laughlin, S. B., & Niven, J. E. (2010). Action Potential Energy Efficiency Varies Among Neuron Types in Vertebrates and Invertebrates. *PLOS Computational Biology*, 6(7), e1000840. DOI: 10.1371/journal.pcbi.1000840.  

[5] Sengupta, B., Laughlin, S. B., & Niven, J. E. (2014). Consequences of Converting Graded to Action Potentials upon Neural Information Coding and Energy Efficiency. *PLOS Computational Biology*, 10(1), e1003439. DOI: 10.1371/journal.pcbi.1003439.  

[6] Karbowski, J. (2024). Information Thermodynamics: From Physics to Neuroscience. *Entropy*, 26(9), 779. DOI: 10.3390/e26090779.  

[7] Landauer, R. (1961). Irreversibility and Heat Generation in the Computing Process. *IBM Journal of Research and Development*, 5, 183–191.  

[8] Bérut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider, R., & Lutz, E. (2012). Experimental verification of Landauer’s principle linking information and thermodynamics. *Nature*, 483, 187–189. DOI: 10.1038/nature10872.  

[9] Georgescu, I. (2021). 60 years of Landauer’s principle. *Nature Reviews Physics*, 3, 770. DOI: 10.1038/s42254-021-00400-8.  

[10] Westbrook, A. et al. (2025). The metabolic costs of cognition. *Trends in Cognitive Sciences*, 29(6), 541–555. DOI: 10.1016/j.tics.2024.11.010.  

---

## 系列路徑

1. **Paper 01｜一輪到底是一輪什麼？：使用者回合、隱藏 LOOP 與單次智能的重新定義**  
2. **Paper 02｜智能到底算了一次什麼？：最小智能語意執行單位的候選理論**  
3. **Paper 03｜從認知到神經元：人腦如何跨層測量智能計算**  
4. **Paper 04｜從神經元到焦耳：智能計算的能量、熱力學與物理下界**  
5. **Paper 05｜計算不是只有 FLOPs：記憶體、互連、硬體占用與計算時空體積**  
6. **Paper 06｜成果品質到底怎麼量？：從形式化正確性到結構化智能品質**  
7. **Paper 07｜不要叫人類替自己的感覺打分數：IBQF 二元測量與低負擔品質評估**  
8. **Paper 08｜自然語言、圖像與創意如何被量？：高歧義成果的結構化品質空間**  
9. **Paper 09｜拿掉 LOOP 還剩多少智能？：單次智能、鷹架依賴與隱藏計算成本**  
10. **Paper 10｜一個答案值多少物理世界？：智能產率的統一計量框架**
