# UNPNP Series 10
## 從遊戲世界到一般程式：AI 自我重組計算圖的研究路線
### From Game Worlds to General Software: A Research Roadmap for AI-Reorganized Computational Graphs

**系列名稱：** UNPNP Hyperlink & Crystallized Computation Series  
**系列篇次：** 10  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** 研究路線圖／實驗設計／UNPNP 理論系列收束篇  
**狀態：** Canonical Draft  

---

## 摘要

UNPNP 前九篇已依序建立：複雜度轉移、跨底空間超連結、自適應快速通道、展開—連結—收斂、耦合計算、路徑編譯、計算結晶化、有效度超連結路徑編碼，以及安全可達世界。至此，理論已足以回答「一個 AI-native runtime 應該如何逐步發現、驗證、編譯並重用新的計算路徑」。然而，一套理論若無法被實驗證偽，就仍只是架構猜想。

本文提出 UNPNP 的第一版實驗研究路線，主張應先以**單機遊戲世界**作為主要驗證域，再逐步進入一般程式與 legacy software 的 AI 再編譯。核心理由是，遊戲同時具備：

$$
\boxed{
\text{複雜狀態}
+
\text{可重播}
+
\text{可回滾}
+
\text{可測量}
+
\text{低外部風險}
}
$$

這使 UNPNP 能在不被企業 IAM、外部不可逆行為、法規與真實生產環境風險淹沒的情況下，先測其真正計算命題。

本文提出五階研究路線：

$$
\boxed{
\text{Synthetic World}
\rightarrow
\text{Turn-Based Game}
\rightarrow
\text{Simulation Game}
\rightarrow
\text{Real-Time Game}
\rightarrow
\text{Controlled Legacy Program}.
}
$$

每一階段都要求相同核心比較：

$$
\text{Baseline}
\quad\text{vs.}\quad
\text{Adaptive}
\quad\text{vs.}\quad
\text{Crystallized}.
$$

並持續測量：

$$
R_{\mathrm{reason}}(t)
=
\frac{
N_{\mathrm{deep-reasoned\ transitions}}
}{
N_{\mathrm{all\ transitions}}
},
$$

$$
H_{\mathrm{corridor}}(t)
=
\frac{
N_{\mathrm{verified\ corridor\ hits}}
}{
N_{\mathrm{all\ transitions}}
},
$$

$$
R_K(t)
=
\frac{
N_{\mathrm{crystal\ transitions}}
}{
N_{\mathrm{all\ transitions}}
},
$$

以及：

$$
C_{\mathrm{avg}}(t).
$$

如果 UNPNP 的核心機制成立，則在穩定 workload 中應觀察到：

$$
R_{\mathrm{reason}}(t)\downarrow,
$$

$$
H_{\mathrm{corridor}}(t)\uparrow,
$$

$$
R_K(t)\uparrow,
$$

$$
C_{\mathrm{avg}}(t)\downarrow,
$$

且錯誤率、風險與維護成本不應同步惡化到抵銷收益。

本文特別提出 **Frozen-Model Experiment**：保持 AI 模型權重固定：

$$
\theta_{t+1}=\theta_t,
$$

只允許 corridor library、crystal set、routing statistics 與索引結構演化：

$$
\mathcal K_{t+1}\neq\mathcal K_t.
$$

若系統性能仍持續改善，即可提供重要證據，顯示改善來自：

$$
\boxed{
\text{world-to-corridor compilation}
}
$$

而非單純來自更大模型或權重更新。

本文同時提出 shadow recompilation、differential verification、baseline replay、ablation、cost ledger、distribution shift、negative crystal、deoptimization、crystal debt 與安全 envelope 等實驗要求。只有在遊戲域中證明「AI 能逐步把既有計算世界重新組織成更便宜的計算世界」後，才進入一般 legacy program 的 selective recompilation。

因此，本文將未來 AI 再編譯定義為：

$$
\boxed{
\text{Legacy Program}
\rightarrow
\text{Observe}
\rightarrow
\text{Trace}
\rightarrow
\text{Reveal}
\rightarrow
\text{Recompose}
\rightarrow
\text{Verify}
\rightarrow
\text{Crystallize}
}
$$

而不是一次性「讓 AI 重寫整個程式」。

本文亦明確保留與經典 P/NP 的邊界。即使實驗證明平均計算成本會隨經驗下降，也不能推出：

$$
P=NP.
$$

更合理的結論將是：在可重複、可結晶、可維護的工作負載中，一部分原本反覆支付的計算可以被轉移為可重用結構，使未來求解逐步轉向：

$$
\boxed{
\text{re-solving}
\rightarrow
\text{solution-preserving and path-preserving evolution}.
}
$$

本文因此作為 UNPNP 第一理論系列的收束：前九篇定義「如何可能」，本篇定義「如何證明它真的有用」。

**關鍵詞：** UNPNP、Game Experiment、AI Recompilation、Frozen Model、Path Compilation、Crystallization、Legacy Software、Benchmark、Adaptive Corridor、Self-Optimizing Computation

---

# 1. 理論寫完之後，真正的問題才開始

到 Series 09 為止，我們已經可以寫出一個完整抽象 runtime：

$$
S_t
\xrightarrow{\Pi}
W_t
\xrightarrow{E}
F_t
\xrightarrow{L}
O_t
\xrightarrow{C}
S_{t+1}
\xrightarrow{K}
\mathcal K_{t+1}.
$$

但這還沒有回答：

> 它真的會比傳統方法快嗎？

---

# 2. 不能用「看起來比較聰明」作為證據

如果 AI 玩遊戲更好，

可能只是：

- 模型本來更強；
- prompt 更好；
- agent loop 更長；
- tool 更多；
- cache 更大。

因此：

$$
\boxed{
\text{better task score}
\neq
\text{UNPNP validated}.
}
$$

---

# 3. 真正需要證明的命題

至少要證明：

$$
\boxed{
\text{同一工作負載下，系統能隨經驗累積減少未來必要計算。}
}
$$

---

# 4. 第一核心實驗命題

令：

$$
C_{\mathrm{avg}}(t)
$$

為平均 transition cost。

UNPNP 理想：

$$
\boxed{
\frac{dC_{\mathrm{avg}}}{dt}<0.
}
$$

---

# 5. 第二核心命題

令：

$$
R_{\mathrm{reason}}(t)
$$

為深推理比例。

理想：

$$
\boxed{
\frac{dR_{\mathrm{reason}}}{dt}<0.
}
$$

---

# 6. 第三核心命題

令：

$$
H_{\mathrm{corridor}}(t)
$$

為已驗證 corridor 命中率。

理想：

$$
\boxed{
\frac{dH_{\mathrm{corridor}}}{dt}>0.
}
$$

---

# 7. 第四核心命題

令：

$$
R_K(t)
$$

為 crystal transition 比例。

理想：

$$
\boxed{
\frac{dR_K}{dt}>0.
}
$$

---

# 8. 第五核心命題

性能改善不能來自錯誤率惡化。

因此要求：

$$
E_{\mathrm{err}}(t)
\not\uparrow
$$

超過允許門檻。

---

# 9. 為什麼先用單機遊戲？

因為遊戲提供：

$$
\boxed{
\text{Bounded Complexity}.
}
$$

世界複雜，

但邊界可知道。

---

# 10. 可重播

可以保存：

$$
S_0.
$$

然後不同 runtime 從同一：

$$
S_0
$$

開始。

---

# 11. 可回滾

錯誤：

$$
S_t\rightarrow S_{\mathrm{bad}}
$$

可以：

$$
S_{\mathrm{bad}}\rightarrow S_t.
$$

---

# 12. 低外部風險

失敗通常不造成：

- 真實金流；
- 真實帳號；
- production data；
- 第三方不可逆影響。

---

# 13. 有大量重複模式

遊戲中常有：

- 移動；
- 戰鬥；
- inventory；
- NPC；
- 商店；
- pathfinding；
- resource update。

這些天然適合：

$$
\text{reuse}.
$$

---

# 14. 又不會太簡單

如果只用 toy graph，

可能證明的只是：

> cache 有用。

遊戲則能測：

- partial observability；
- state variation；
- branching；
- dynamic world；
- semantic equivalence。

---

# 15. 第一版研究階梯

本文提出：

$$
\boxed{
P_0
\rightarrow
P_1
\rightarrow
P_2
\rightarrow
P_3
\rightarrow
P_4.
}
$$

---

# 16. Phase 0：Synthetic World

建立人工小世界。

例如：

- grid；
- object graph；
- inventory；
- deterministic tasks。

---

# 17. Phase 0 的目的

不是證明遊戲能力。

而是驗證：

- receipt；
- path trace；
- guard；
- crystallization；
- deoptimization；
- cost accounting。

---

# 18. Synthetic World 必須有 Baseline

不能只測 UNPNP。

至少：

$$
B_0
=
\text{ordinary planner}.
$$

---

# 19. Phase 0 成功門檻

如果連 toy world 都無法：

$$
C_{\mathrm{avg}}\downarrow,
$$

就不應進入更大遊戲。

---

# 20. Phase 1：Turn-Based Game

下一步：

$$
\boxed{
\text{Turn-Based}.
}
$$

---

# 21. 為什麼回合制？

因為 time pressure 低。

可以精確記錄：

- reasoning；
- action；
- verification；
- state。

---

# 22. 回合制適合 Differential Replay

同一 state：

$$
S_t
$$

可以測：

$$
A_{\mathrm{baseline}},
A_{\mathrm{adaptive}},
A_{\mathrm{crystal}}.
$$

---

# 23. Phase 1 主要測什麼？

- corridor reuse；
- semantic path family；
- reasoning reduction；
- negative crystal；
- path invalidation。

---

# 24. Phase 2：Simulation / Management Game

例如：

- colony；
- economy；
- management；
- world simulation。

---

# 25. 為什麼 Simulation 很重要？

因為有大量：

$$
\boxed{
\text{repeated local state update}.
}
$$

這比一次性 puzzle 更接近一般程式。

---

# 26. Simulation 會暴露維護問題

World state 一直變。

因此 crystal 可能：

$$
\text{fresh}
\rightarrow
\text{stale}.
$$

---

# 27. Phase 2 主要測

- incremental repair；
- crystal debt；
- distribution shift；
- higher-order crystal；
- selection congestion。

---

# 28. Phase 3：Real-Time Single-Player

再進：

$$
\boxed{
\text{Real-Time}.
}
$$

---

# 29. Real-Time 增加 latency 壓力

此時不只：

$$
\mathbb E[C].
$$

還要看：

$$
p95,
p99.
$$

---

# 30. Real-Time 會測出 fast path 是否真的有意義

如果：

$$
p99_{\mathrm{crystal}}
<
p99_{\mathrm{baseline}},
$$

才有實際價值。

---

# 31. Real-Time 也測 variance

$$
\operatorname{Var}(C).
$$

穩定快速可能比平均稍快更重要。

---

# 32. Phase 4：Controlled Legacy Program

只有前面通過，

才進：

$$
\boxed{
\text{general software}.
}
$$

---

# 33. Controlled Legacy Program 的定義

不是 production system。

而是：

- local；
- open-source；
- testable；
- rollback；
- reproducible；
- no dangerous external effects。

---

# 34. Phase 4 第一目標

不是讓 AI 重寫全部程式。

而是：

$$
\boxed{
\text{observe hot semantic paths}.
}
$$

---

# 35. Legacy Program 初始模式

$$
P_{\mathrm{legacy}}
$$

保持 canonical。

UNPNP 只建立：

$$
\mathcal K_{\mathrm{shadow}}.
$$

---

# 36. Shadow Recompilation

$$
P_{\mathrm{legacy}}
\parallel
P_{\mathrm{shadow}}.
$$

不讓 shadow 直接改真狀態。

---

# 37. Compare

比較：

$$
\operatorname{Obs}
(
P_{\mathrm{legacy}}
)
$$

與：

$$
\operatorname{Obs}
(
P_{\mathrm{shadow}}
).
$$

---

# 38. Only Then Promote

只有：

$$
V_{\mathrm{equiv}}\ge\theta_V
$$

且：

$$
U_L>0
$$

才 active。

---

# 39. 三組 Baseline

所有實驗至少三組。

---

# 40. Baseline A：Naive / Traditional

$$
B_A.
$$

不使用 corridor memory。

---

# 41. Baseline B：Adaptive without Crystallization

$$
B_B.
$$

允許 AI planning / search，

但不形成 persistent crystal。

---

# 42. Experimental C：Adaptive + Crystallization

$$
E_C.
$$

完整：

- routing；
- EHPE；
- crystal；
- reuse。

---

# 43. 這三組可以回答什麼？

如果：

$$
E_C>B_B>B_A,
$$

才能逐步分離：

- AI adaptivity；
- crystallization value。

---

# 44. Frozen-Model Experiment

為了避免：

> 模型後來變聰明了。

固定：

$$
\boxed{
\theta_{t+1}=\theta_t.
}
$$

---

# 45. 只允許什麼變？

$$
\mathcal K_t,
$$

$$
\mathcal R_t,
$$

$$
\mathcal I_t,
$$

$$
\mathcal S_t.
$$

即：

- crystal library；
- routing statistics；
- index；
- state summaries。

---

# 46. Frozen-Model 的意義

若：

$$
P(t+1)>P(t)
$$

仍成立，

則：

$$
\boxed{
\text{architecture learned}.
}
$$

---

# 47. World-to-Corridor Compilation

本文將此稱為：

$$
\boxed{
\text{World-to-Corridor Compilation}.
}
$$

---

# 48. Learning 不只在權重裡

所以：

$$
\boxed{
\text{Learning}
=
\text{Weight Learning}
\cup
\text{Structural Learning}.
}
$$

---

# 49. 核心 Metric 1：Reasoning Ratio

$$
R_{\mathrm{reason}}(t)
=
\frac{
N_{\mathrm{deep-reason}}
}{
N_{\mathrm{all}}
}.
$$

---

# 50. Metric 2：Corridor Hit Ratio

$$
H_{\mathrm{corridor}}(t)
=
\frac{
N_{\mathrm{corridor-hit}}
}{
N_{\mathrm{all}}
}.
$$

---

# 51. Metric 3：Crystal Ratio

$$
R_K(t)
=
\frac{
N_{\mathrm{crystal-exec}}
}{
N_{\mathrm{all}}
}.
$$

---

# 52. Metric 4：Average Cost

$$
C_{\mathrm{avg}}(t).
$$

---

# 53. Metric 5：Tail Cost

$$
C_{p95},
C_{p99}.
$$

---

# 54. Metric 6：Failure Rate

$$
F_R
=
\frac{
N_{\mathrm{failure}}
}{
N_{\mathrm{all}}
}.
$$

---

# 55. Metric 7：Rollback Rate

$$
R_B
=
\frac{
N_{\mathrm{rollback}}
}{
N_{\mathrm{all}}
}.
$$

---

# 56. Metric 8：Crystal Invalidation Rate

$$
I_K
=
\frac{
N_{\mathrm{stale-or-invalid}}
}{
N_{\mathrm{crystal}}
}.
$$

---

# 57. Metric 9：Maintenance Cost

$$
C_M(t).
$$

---

# 58. Metric 10：Selection Cost

$$
C_S(t).
$$

---

# 59. Metric 11：Memory Cost

$$
C_{\mathrm{memory}}(t).
$$

---

# 60. Metric 12：Verification Cost

$$
C_V(t).
$$

---

# 61. Total Cost Ledger

最重要的是：

$$
\boxed{
C_T
=
C_{\mathrm{reason}}
+
C_{\mathrm{route}}
+
C_{\mathrm{execute}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{memory}}
+
C_{\mathrm{maintain}}
+
C_{\mathrm{failure}}.
}
$$

---

# 62. 不可以只看 Token

Token 是部分成本。

不能：

$$
\text{token down}
\Rightarrow
\text{system faster}.
$$

---

# 63. CPU / GPU

需要量：

- CPU time；
- GPU time；
- memory；
- I/O；
- API latency。

---

# 64. Wall-Clock Time

$$
T_{\mathrm{wall}}
$$

也必須記。

---

# 65. Reasoning Invocation Count

$$
N_{\mathrm{LLM}}.
$$

很重要。

因為 UNPNP 其中一個目標是：

$$
N_{\mathrm{LLM}}\downarrow.
$$

---

# 66. Tool Call Count

$$
N_{\mathrm{tool}}.
$$

如果 crystal 只是讓 token 少，

卻 tool call 更多，

未必有收益。

---

# 67. State Transfer

量：

$$
B_{\mathrm{state}}
$$

傳輸 bytes。

這能測 boundary reduction。

---

# 68. Intermediate Materialization

量：

$$
N_{\mathrm{materialize}}.
$$

Path Compilation 成功時應可能下降。

---

# 69. A/B Replay

同一初始 state：

$$
S_0
$$

重播多次。

---

# 70. 隨機種子

若遊戲 stochastic，

固定：

$$
\text{seed}.
$$

才能公平比。

---

# 71. 多 Seed

不能只用一個。

應：

$$
\text{seed}_1,\ldots,\text{seed}_n.
$$

---

# 72. Distribution Split

分：

- train / observe；
- validation；
- shifted。

---

# 73. Observe Set

允許系統形成 crystal。

---

# 74. Validation Set

測：

> crystal 是否泛化？

---

# 75. Shift Set

故意改：

- map；
- item；
- rule；
- NPC；
- difficulty。

---

# 76. Distribution Shift Test

看：

$$
\text{Hot}
\rightarrow
\text{Warm / Cold}
$$

是否正常。

---

# 77. 如果 Crystal 不會失效，是壞事

因為真世界會變。

所以：

$$
\boxed{
\text{correct invalidation}
}
$$

本身也是成功指標。

---

# 78. Negative Crystal Test

故意建立：

$$
\text{known bad path}.
$$

測系統是否：

$$
\text{avoid repeated exploration}.
$$

---

# 79. Reopen Test

環境變後，

原本 bad path 變好。

系統是否能：

$$
\kappa^-
\rightarrow
\text{reopen}.
$$

---

# 80. Higher-Order Crystal Test

先形成：

$$
\kappa_1,\kappa_2,\kappa_3.
$$

再測：

$$
K^{(2)}
(
\kappa_1,\kappa_2,\kappa_3
).
$$

---

# 81. 不能只證明一階 Cache

如果只證明：

> 同樣 input 有 cache 很快。

那不夠。

必須測：

$$
\boxed{
\text{procedure-level reuse}.
}
$$

---

# 82. Semantic Family Test

不同 raw state：

$$
s_1\neq s_2,
$$

但屬同一 task family。

看是否命中：

$$
\kappa_{\mathcal D}.
$$

---

# 83. Guard Precision Test

測：

$$
P_G.
$$

---

# 84. Guard Recall Test

測：

$$
R_G.
$$

---

# 85. Guard False Positive 是重要失敗

因為：

$$
\text{wrong fast path}
$$

會放大錯誤。

---

# 86. Deoptimization Test

故意輸入：

$$
x\notin D_\kappa.
$$

系統應：

$$
\text{fast}
\rightarrow
\text{slow}.
$$

---

# 87. Decrystallization Test

故意更改 dependency。

看：

$$
\kappa
\rightarrow
\Gamma.
$$

是否可追。

---

# 88. Provenance Test

每個：

$$
\kappa
$$

應能回答：

- source；
- version；
- benchmark；
- validator。

---

# 89. Crystal Poisoning Test

在安全 sandbox 中故意提供錯誤 trace。

測：

> 會不會被 promotion？

---

# 90. Promotion Gate

要求：

$$
V\ge\theta_V,
$$

$$
U_L>0,
$$

$$
R\le\theta_R.
$$

---

# 91. Ablation 1：No Semantic Revealing

關掉：

$$
\Pi_\xi.
$$

看 frontier cost 是否上升。

---

# 92. Ablation 2：No Corridor Memory

關掉：

$$
\mathcal K.
$$

看 reasoning ratio。

---

# 93. Ablation 3：No Negative Crystal

看是否重複走錯路。

---

# 94. Ablation 4：No EHPE

讓所有 candidate 都 crystallize。

看 maintenance explosion。

---

# 95. Ablation 5：No Invalidation

看 distribution shift 下錯誤率。

---

# 96. Ablation 6：No Fast Verification

全部 deep verify。

看安全成本。

---

# 97. Ablation 7：No Deep Verification

全部 fast verify。

看 failure。

---

# 98. 這些 Ablation 為何重要？

因為可以分辨：

$$
\boxed{
\text{哪一個模組真的有價值。}
}
$$

---

# 99. 第一個成功標準

在 stable workload：

$$
C_{\mathrm{avg}}^{\mathrm{crystal}}
<
C_{\mathrm{avg}}^{\mathrm{adaptive}}
<
C_{\mathrm{avg}}^{\mathrm{baseline}}.
$$

---

# 100. 第二成功標準

$$
R_{\mathrm{reason}}^{\mathrm{crystal}}
<
R_{\mathrm{reason}}^{\mathrm{adaptive}}.
$$

---

# 101. 第三成功標準

錯誤率：

$$
F_R^{\mathrm{crystal}}
\le
F_R^{\mathrm{baseline}}
+
\epsilon.
$$

---

# 102. 第四成功標準

完整成本：

$$
C_T^{\mathrm{crystal}}
<
C_T^{\mathrm{baseline}}.
$$

不能只看 runtime。

---

# 103. 第五成功標準

在 shift 後：

$$
\operatorname{InvalidationAccuracy}
$$

足夠高。

---

# 104. 第六成功標準

Crystal library 不爆炸。

即：

$$
C_M
$$

與：

$$
C_S
$$

受控。

---

# 105. 失敗標準一

如果：

$$
C_{\mathrm{compile}}
+
C_{\mathrm{maintain}}
>
C_{\mathrm{saved}},
$$

則 UNPNP 該版本失敗。

---

# 106. 失敗標準二

如果：

$$
R_{\mathrm{reason}}
$$

沒有下降，

代表 crystal 沒真正替代 reasoning。

---

# 107. 失敗標準三

如果：

$$
|\mathcal K|\uparrow
$$

但：

$$
H_{\mathrm{corridor}}
$$

不升，

代表 crystal quality 差。

---

# 108. 失敗標準四

如果錯誤率明顯上升，

則 fast path 只是：

$$
\text{fail faster}.
$$

---

# 109. 失敗標準五

如果 guard / routing 比原 path 還貴，

形成：

$$
\text{negative optimization}.
$$

---

# 110. 這些失敗都不是壞結果

因為它們能告訴我們：

> 哪些 UNPNP 命題不成立。

這就是可證偽研究。

---

# 111. Experiment Receipt

每次 run 留：

$$
r
=
\langle
\text{seed},
\text{version},
\text{config},
\text{metrics},
\text{crystals},
\text{failures}
\rangle.
$$

---

# 112. Reproducibility

應能：

$$
\operatorname{Replay}(r).
$$

---

# 113. Canonical Baseline

每個遊戲版本要保存：

$$
B_v.
$$

避免版本更新污染結果。

---

# 114. Version Lock

初期最好：

$$
v_{\mathrm{game}}
$$

固定。

---

# 115. 後期才做 Version Shift

再測：

$$
v_1\rightarrow v_2.
$$

---

# 116. Hardware Lock

同一 benchmark 先固定 hardware。

---

# 117. 再做 Hardware Transfer

測：

$$
\kappa_{\mathrm{CPU}}
$$

與：

$$
\kappa_{\mathrm{GPU}}.
$$

---

# 118. AI Model Lock

Frozen-model 階段固定模型。

---

# 119. Model Transfer

後期才測：

> 同一 crystal library 是否可跨模型使用？

---

# 120. Cross-Model Crystal

若：

$$
\kappa
$$

是 external runtime primitive，

理論上可能：

$$
M_A\rightarrow\kappa
$$

與：

$$
M_B\rightarrow\kappa.
$$

---

# 121. 這很重要

因為表示：

> 學習成果不一定綁在單一模型權重裡。

---

# 122. Cross-Agent Reuse

同理：

$$
\text{Agent}_1
$$

產生 crystal，

$$
\text{Agent}_2
$$

是否可使用？

---

# 123. 需要 Capability / Provenance

跨 Agent 不能裸共享。

必須：

- trust；
- version；
- validator；
- capability。

---

# 124. 遊戲實驗之後才能問一般程式

如果遊戲域證明：

$$
C_T\downarrow,
$$

下一步才有理由做 legacy software。

---

# 125. Legacy Recompilation Pipeline

本文正式提出：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Trace}
\rightarrow
\text{Reveal}
\rightarrow
\text{Recompose}
\rightarrow
\text{Verify}
\rightarrow
\text{Crystallize}.
}
$$

---

# 126. Observe

不修改 source。

先看：

$$
P_{\mathrm{legacy}}
$$

怎麼跑。

---

# 127. Trace

收集：

$$
\Gamma_1,\ldots,\Gamma_n.
$$

---

# 128. Reveal

找：

- high-cost；
- high-frequency；
- stable semantic path。

---

# 129. Recompose

生成：

$$
\widehat{\Gamma}.
$$

---

# 130. Verify

要求：

$$
\Gamma
\simeq_{\mathcal T}
\widehat{\Gamma}.
$$

---

# 131. Crystallize

只有：

$$
U_H>0.
$$

---

# 132. AI Recompilation 不是 AI Refactor

Refactor 通常：

> 改 source 結構。

AI Recompilation 更廣：

$$
\boxed{
\text{change computational path representation}.
}
$$

---

# 133. 可以不改 Source

Crystal overlay 可以存在：

$$
P_{\mathrm{legacy}}
$$

之外。

---

# 134. 可以之後回寫 Source

若長期證明成熟，

再：

$$
\kappa
\rightarrow
\text{source patch}.
$$

---

# 135. Source Rewrite 是最後階段

不是第一步。

---

# 136. 適合的第一批 Legacy Target

- deterministic library；
- parser；
- query workload；
- simulation；
- local tool chain；
- test runner；
- build pipeline。

---

# 137. 不適合第一批

- payment；
- authentication core；
- production DB write；
- safety-critical control；
- irreversible external systems。

---

# 138. 一般程式實驗仍要 Shadow

新 path：

$$
\widehat{\Gamma}
$$

先不接 production。

---

# 139. General Program Metric

除了 latency，

還要：

- CPU；
- memory；
- I/O；
- test pass；
- semantic equivalence；
- maintenance。

---

# 140. Human Code Review

若最後要回寫 source，

仍可要求 human review。

---

# 141. AI 先做 Runtime Overlay 比較合理

因為：

$$
\boxed{
\text{runtime evidence}
\rightarrow
\text{source confidence}.
}
$$

---

# 142. 從遊戲到程式的真正橋樑

不是：

> 遊戲跟程式很像。

而是兩者都可以抽象成：

$$
\boxed{
\text{state}
+
\text{transition}
+
\text{cost}
+
\text{verification}.
}
$$

---

# 143. 所以 Game 不是玩具

它是：

$$
\boxed{
\text{controlled computational ecology}.
}
$$

---

# 144. UNPNP Computer 的最小 MVP？

本系列刻意不以產品 MVP 為主。

但研究原型至少需要：

```text
State Observer
Transition Logger
Adaptive Corridor Generator
Crystal Store
EHPE Gate
Validator
Cost Ledger
Replay Harness
```

---

# 145. 第一版不用複雜 UI

研究重點是：

$$
\text{runtime evidence}.
$$

---

# 146. 第一版不用多玩家

多玩家增加：

- networking；
- fairness；
- external effects；
- synchronization。

先不要。

---

# 147. 第一版不用 Enterprise IAM

Series 09 已說明。

只需要：

$$
I+C+R+G+V.
$$

---

# 148. 第一版不用 Online Learning

可先固定模型。

---

# 149. 第一版也不用修改模型權重

這反而能讓實驗更乾淨。

---

# 150. 最重要的控制變因

$$
\boxed{
\text{same model, same world, different runtime architecture}.
}
$$

---

# 151. 如果這樣仍變快

才能真正說：

> UNPNP runtime 本身提供價值。

---

# 152. 如果沒有變快

也要接受。

可能表示：

- crystal overhead 太高；
- world 太 dynamic；
- guard 太貴；
- selection 太貴；
- path 不可壓縮。

---

# 153. 找到不可壓縮區域也是成果

可形成：

$$
\boxed{
\text{non-crystallizable workload class}.
}
$$

---

# 154. 可結晶性地圖

未來可以建立：

$$
Q_K(\mathcal D).
$$

不同 workload 的：

$$
\text{crystallizability}.
$$

---

# 155. 這可能比單一成功案例更重要

因為真正需要知道：

> 哪些世界適合 UNPNP？

---

# 156. Workload Taxonomy

未來分類：

- highly repetitive；
- moderately dynamic；
- adversarial；
- one-shot；
- stochastic；
- high verification burden。

---

# 157. UNPNP 不應宣稱全域適用

Series 03 已有：

$$
\mathsf{LGC}
\prec
\mathsf{FGC}
\prec
\mathsf{AGC}
\prec
\mathsf{UGC}.
$$

實驗先從：

$$
\mathsf{LGC}
$$

與：

$$
\mathsf{FGC}
$$

開始。

---

# 158. 最初不要碰 P/NP 結論

即使遊戲成功，

只能說：

> 某些 workload 的 amortized runtime 改善。

---

# 159. Uniformity 仍未證明

仍然：

$$
\forall x\exists\Gamma_x
\centernot\Rightarrow
\exists G\forall x.
$$

---

# 160. 外部化成本仍要計

如果 crystal build 很貴，

不能藏起來。

---

# 161. 完整實驗總式

baseline：

$$
C_B(N)
=
\sum_{i=1}^{N}
C_{\mathrm{base}}(x_i).
$$

UNPNP：

$$
C_U(N)
=
C_{\mathrm{build}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{maintain}}
+
\sum_{i=1}^{N}
C_{\mathrm{crystal}}(x_i).
$$

成功要求：

$$
\boxed{
C_U(N)<C_B(N).
}
$$

---

# 162. 再加風險

$$
C_U^R
=
C_U
+
\lambda E_L.
$$

---

# 163. 再加失敗

$$
C_U^{RF}
=
C_U^R
+
C_{\mathrm{failure}}.
$$

---

# 164. 最終比較應是系統級

這與 Series 01 完整閉環。

---

# 165. Research Gate 0

Synthetic world 通過。

---

# 166. Research Gate 1

Turn-based 通過。

---

# 167. Research Gate 2

Simulation 通過。

---

# 168. Research Gate 3

Real-time 通過。

---

# 169. Research Gate 4

Controlled legacy program 通過。

---

# 170. 只有之後才做 Production-Like

不是現在。

---

# 171. Gate 不只是成功率

每一階段都要：

- performance；
- correctness；
- maintenance；
- invalidation；
- safety。

---

# 172. Stop Condition

若某階段：

$$
U_L\le0
$$

長期成立，

停止擴張。

---

# 173. Pivot Condition

可以改：

- workload；
- granularity；
- crystal policy；
- verification。

---

# 174. Fail Fast in Research

研究系統應：

> 早點知道哪裡不成立。

不是把負結果包裝掉。

---

# 175. 理論與工程要互相修正

如果實驗顯示：

$$
E\rightarrow L\rightarrow C
$$

太粗，

就拆。

---

# 176. 如果 Path Compilation 太貴

降低 granularity。

---

# 177. 如果 Crystal Library 爆炸

提高 EHPE threshold。

---

# 178. 如果 Invalidation 太頻繁

降低 persistent crystal。

---

# 179. 如果 Reasoning Ratio 不降

檢查 routing / semantic family。

---

# 180. 這就是研究循環

$$
\boxed{
\text{Theory}
\rightarrow
\text{Experiment}
\rightarrow
\text{Failure}
\rightarrow
\text{Revision}.
}
$$

---

# 181. Series 01–09 的實驗映射

Series 01：

$$
\text{cost ledger}.
$$

---

# 182. Series 02

$$
\text{subspace / hyperlink instrumentation}.
$$

---

# 183. Series 03

$$
\text{adaptive corridor generator}.
$$

---

# 184. Series 04

$$
\text{ELC runtime trace}.
$$

---

# 185. Series 05

$$
\text{coupled transition benchmark}.
$$

---

# 186. Series 06

$$
\text{path compilation}.
$$

---

# 187. Series 07

$$
\text{crystal lifecycle}.
$$

---

# 188. Series 08

$$
\text{EHPE utility gate}.
$$

---

# 189. Series 09

$$
\text{safe reachable world}.
$$

---

# 190. Series 10

$$
\boxed{
\text{integrated falsifiable experiment}.
}
$$

---

# 191. 核心命題一

$$
\boxed{
\textbf{
UNPNP 第一階段不需要證明一般計算世界都能被重新編譯；只需要證明在一個複雜、可重複、可測量的封閉世界中，結晶化確實能降低未來計算成本。
}
}
$$

---

# 192. 核心命題二

$$
\boxed{
\textbf{
單機遊戲是理想第一實驗域，因為它在保留真實狀態複雜度的同時，把不可逆外部風險壓到很低。
}
}
$$

---

# 193. 核心命題三

$$
\boxed{
\textbf{
Frozen-model experiment 是區分「模型更聰明」與「計算架構真的學會更便宜路徑」的關鍵實驗。
}
}
$$

---

# 194. 核心命題四

$$
\boxed{
\textbf{
未來一般程式的 AI 再編譯，應先以 shadow overlay 與 selective recompilation 進行，而不是讓 AI 一次性重寫完整 legacy system。
}
}
$$

---

# 195. 核心命題五

$$
\boxed{
\textbf{
一套真正成立的 UNPNP runtime，不只會在世界中尋找答案；它會逐步把自己走過的世界重新編譯成一個更容易再次穿越的世界。
}
}
$$

---

# 196. 系列最終總模型

整套 UNPNP v0.1：

$$
\boxed{
\mathfrak U_t
=
(
\mathcal W,
\mathcal B,
\mathcal L_t,
\mathcal M,
\Pi,
E,
L,
C,
K,
V,
\mathcal S,
\mathbf C
).
}
$$

其中：

- $\mathcal W$：world；
- $\mathcal B$：subspaces；
- $\mathcal L_t$：dynamic hyperlinks；
- $\mathcal M$：adaptive corridor generator；
- $\Pi$：semantic revealing；
- $E$：Expansion；
- $L$：Linking；
- $C$：Convergence；
- $K$：crystallization；
- $V$：verification；
- $\mathcal S$：security envelope；
- $\mathbf C$：cost vector。

---

# 197. 一輪運行

$$
S_t
\xrightarrow{\Pi}
W_t
\xrightarrow{E}
F_t
\xrightarrow{\mathcal M}
\Gamma_t
\xrightarrow{L}
O_t
\xrightarrow{V}
\widehat O_t
\xrightarrow{C}
S_{t+1}.
$$

---

# 198. 一輪之後

若：

$$
\operatorname{EHPE}(\Gamma_t)>0,
$$

則：

$$
\Gamma_t
\xrightarrow{\operatorname{PC}}
\widehat{\ell}_t
\xrightarrow{K}
\kappa_t.
$$

---

# 199. 世界更新

$$
\boxed{
\mathcal L_{t+1}
=
\mathcal L_t
\cup
\kappa_t^+
-
\kappa_t^-.
}
$$

---

# 200. 下一輪不再是同一個計算圖

所以：

$$
\boxed{
\mathfrak U_{t+1}
\neq
\mathfrak U_t.
}
$$

這就是自我重組計算圖。

---

# 201. 最終與 P/NP 的邊界

即使：

$$
C_{\mathrm{avg}}(t)\downarrow,
$$

仍然不能推出：

$$
P=NP.
$$

---

# 202. 更合理的研究結論

如果實驗成功，

可以說：

$$
\boxed{
\text{repeated workload complexity can be partially transferred into reusable verified structure}.
}
$$

---

# 203. 從 Re-solving 到 Evolution

因此：

$$
\boxed{
\text{re-solving}
\rightarrow
\text{solution-preserving evolution}.
}
$$

---

# 204. 從 Path Search 到 Path-Space Rewrite

更進一步：

$$
\boxed{
\text{optimize path}
\rightarrow
\text{optimize path space}.
}
$$

---

# 205. 從固定程式到會長路的程式

$$
P_t
=
(V_t,E_t).
$$

而：

$$
E_{t+1}
\neq
E_t.
$$

---

# 206. 從 AI 玩家到 AI 世界編譯器

第一階段表面看：

> AI 在玩遊戲。

真正測的是：

$$
\boxed{
\text{AI 是否能把遊戲世界逐步編譯成自己的快速通道網路。}
}
$$

---

# 207. 從遊戲世界到一般程式

若成功，

下一步：

$$
\boxed{
\text{AI 是否能把 legacy software 的高成本語義路徑逐步編譯成 validated crystal overlay？}
}
$$

---

# 208. 這才是 AI Recompilation

不是：

> AI 幫我重寫程式。

而是：

$$
\boxed{
\text{AI 觀察執行世界，發現值得重組的計算路徑，生成候選新路，驗證後逐步將其提升為新 primitive。}
}
$$

---

# 209. 結論

UNPNP 的第一理論系列到這裡收束。

我們從：

$$
P\stackrel{?}{=}NP
$$

之外的一個上位問題開始：

> 如果困難的計算能透過索引、表示、搜尋、路由、編譯與記憶被搬到其他地方，那麼複雜度到底去了哪裡？

接著得到：

$$
\text{Complexity Transfer}.
$$

再得到：

$$
\text{Subspaces}
+
\text{Hyperlinks}.
$$

接著需要：

$$
\text{Adaptive Corridor Generator}.
$$

動態運行採：

$$
E
\rightarrow
L
\rightarrow
C.
$$

transition 內可：

$$
A
\otimes
P
\otimes
E
\otimes
G
\otimes
V.
$$

穩定 path 可以：

$$
\Gamma
\rightarrow
\widehat{\ell}.
$$

再：

$$
\widehat{\ell}
\rightarrow
\kappa.
$$

但只有：

$$
U_H>0
$$

的 path 才值得結晶。

而：

$$
\kappa
$$

只能存在於：

$$
\mathcal W^{\mathrm{accessible}}.
$$

最終整個系統形成：

$$
\boxed{
ELC
\rightarrow
K
\rightarrow
ELC'
\rightarrow
K'
\rightarrow
\cdots
}
$$

這也就是：

$$
\boxed{
\text{呼吸產生結晶，結晶改變下一次呼吸。}
}
$$

但理論真正有價值的時刻，不是我們把這句話寫得漂亮。

而是我們在一個實際遊戲世界中，看到：

$$
R_{\mathrm{reason}}\downarrow,
$$

$$
H_{\mathrm{corridor}}\uparrow,
$$

$$
R_K\uparrow,
$$

$$
C_{\mathrm{avg}}\downarrow,
$$

同時：

$$
F_R
$$

沒有失控，

$$
C_M
$$

沒有吞掉收益，

且 distribution shift 後系統能正確失效、解晶與重建。

如果這些現象真的出現，

那麼我們才有資格說：

$$
\boxed{
\textbf{
AI 不只是在計算世界中解題；
它開始學會重新編譯計算世界本身。
}
}
$$

而如果這些現象沒有出現，

也同樣重要。

因為那會告訴我們：

> 哪些世界根本不值得結晶，哪些成本無法被有效外部化，哪些路徑不存在可維護的捷徑。

因此這個系列最終不是一個「UNPNP 一定成立」的宣言。

它是一套可以開始被實驗的研究綱領。

下一步不再是繼續增加抽象詞彙。

下一步是：

$$
\boxed{
\textbf{
做實驗。
}
}
$$

---

## 系列完成後的兩份技術白皮書

### Technical Whitepaper 01
**Crystallized Semantic Graph：結晶化語義圖長期記憶架構**

處理：

$$
R_i
\rightarrow
C_i
\rightarrow
\mathcal G_C
$$

以及：

- raw canonical conversation；
- multi-view semantic crystals；
- source hyperlinks；
- semantic hypergraph；
- synchronous / asynchronous crystallization；
- progressive expansion；
- crystal-first, source-on-demand；
- SEDB storage；
- Omphalos search runtime；
- memory path crystallization。

### Technical Whitepaper 02
**UNPNP Game Experimental Runtime：以單機遊戲驗證自適應超連結與計算結晶化**

處理：

- Phase 0–4；
- runtime architecture；
- benchmark harness；
- frozen-model experiment；
- replay；
- crystal lifecycle；
- cost ledger；
- success / failure gate；
- future legacy-program recompilation interface。

至此，**UNPNP Hyperlink & Crystallized Computation Series v0.1 的十篇理論論文完成閉環。**
