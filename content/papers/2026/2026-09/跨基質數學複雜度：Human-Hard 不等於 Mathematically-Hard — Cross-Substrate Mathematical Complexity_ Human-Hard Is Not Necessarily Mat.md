# 跨基質數學複雜度：Human-Hard 不等於 Mathematically-Hard
## Cross-Substrate Mathematical Complexity: Human-Hard Is Not Necessarily Mathematically-Hard

**系列：** AI 原生數學與耦合求解（AI-Native Mathematics and Coupled Solution Dynamics, ANMCS）  
**系列編號：** Series A / Paper 02 of 07  
**文件編號：** EML-ANMCS-A02-2026-v0.1  
**作者：** Neo.K with Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09  
**性質：** General Theory / Mathematical Complexity / Cognitive Substrate / Representation Theory  
**狀態：** FOUNDATIONAL THEORY DRAFT  
**直接前置：** A01〈AI 原生數學不是人類數學的加速版〉  
**直接後續：** A03〈表示搜尋先於證明搜尋〉

---

# 摘要

數學研究經常說：

> 這個問題很難。

但「難」究竟是誰的性質？

是問題本身？

是我們所採用的表示方式？

是我們選擇的方法？

還是執行這套數學操作的認知／計算基質？

本文提出：

$$
\boxed{
\text{Mathematical Difficulty}
\neq
\text{A Single Property of the Problem}.
}
$$

更合理的最小形式是：

$$
\boxed{
C(P;s,r,m)
}
$$

其中：

- $P$：問題；
- $s$：認知／計算基質（substrate）；
- $r$：表示（representation）；
- $m$：方法（method）；
- $C$：在指定條件下求解、生成、驗證或理解所需的有效成本。

本文因此提出 **跨基質數學複雜度（Cross-Substrate Mathematical Complexity, CSMC）**，其核心命題為：

$$
\boxed{
\text{Human-Hard}
\neq
\text{Mathematically-Hard}.
}
$$

更精確地：

$$
\boxed{
C_H^\ast(P)
\neq
C_A^\ast(P)
}
$$

一般情況完全可能成立，其中：

$$
C_s^\ast(P)
=
\inf_{r\in\mathcal R_s,\;m\in\mathcal M_s}
C(P;s,r,m)
$$

表示 substrate $s$ 在其可用表示與方法族中，對問題 $P$ 的最低有效成本。

本文進一步建立：

1. **Substrate-Relative Mathematical Complexity**：基質相對數學複雜度；
2. **Cross-Substrate Hardness Gap**：跨基質難度差；
3. **Representation Gap**：表示差距；
4. **Representation Phase Transition**：表示相變；
5. **Translation Complexity**：跨表示／跨基質翻譯複雜度；
6. **Hardness Spectrum**：難度譜；
7. **Discovery / Verification / Explanation Separation**：發現、驗證與解釋難度分離；
8. **Observed Hardness ≠ Intrinsic Hardness**：觀察到的困難不等於本質困難。

本文不主張傳統計算複雜度理論可以被認知複雜度取代，也不主張任何 NP-hard 問題會因 AI 表示改寫而自動變成 polynomial-time solvable。相反地，本框架要求嚴格區分：

$$
\boxed{
\text{Computational Complexity}
}
$$

與：

$$
\boxed{
\text{Cognitive / Representational Complexity}.
}
$$

本文的目的，是為後續 A03 建立一個核心轉折：

> **如果困難部分來自表示，而不是只來自問題本身，那麼 AI 最重要的數學搜尋可能不是 proof search，而是 representation search。**

---

# 0. 生成與理論邊界聲明

本文是一篇 AI 輔助生成的理論研究稿。

本文不主張：

1. 已建立可取代 P、NP、PSPACE、EXP 等傳統 complexity classes 的新複雜度理論；
2. 「人類覺得難」即可推出問題存在特殊 complexity class；
3. AI 對某 problem 解得快，就能推出該 problem 在標準圖靈機模型下具有更低 asymptotic complexity；
4. representation change 必然降低 worst-case complexity；
5. cognitive substrate 可任意繞過 information-theoretic 或 computational lower bounds；
6. 所有數學難題都只是表示問題；
7. 所有 AI 都具有相同 substrate；
8. AI substrate 必然支配 human substrate；
9. human intuition 沒有獨特優勢；
10. empirical model performance 可以直接等同數學複雜度；
11. 本文證明 $P=NP$ 或 $P\neq NP$ ；
12. 本文證明所有「難」都是主觀的。

本文更弱的主張是：

$$
\boxed{
\text{對數學實務中的有效求解成本而言，}
\text{問題、表示、方法與基質不可一般地完全分離。}
}
$$

---

# 1. 「這題很難」是一個不完整句子

傳統自然語言常說：

$$
\boxed{
P\text{ is hard}.
}
$$

但這句話至少省略了三個變數：

$$
s,
\quad
r,
\quad
m.
$$

所以更完整應是：

$$
\boxed{
P
\text{ is hard under }
(s,r,m).
}
$$

---

# 2. 難度的四元結構

本文採：

$$
\boxed{
C(P;s,r,m).
}
$$

其中：

$$
P=\text{problem},
$$

$$
s=\text{substrate},
$$

$$
r=\text{representation},
$$

$$
m=\text{method}.
$$

---

# 3. substrate 是什麼？

substrate 不只指：

> CPU / GPU / TPU。

本文中的 substrate 可以包含：

- 人類認知；
- LLM；
- symbolic theorem prover；
- hybrid neuro-symbolic system；
- graph-native mathematical agent；
- program-synthesis engine；
- distributed agent collective。

---

# 4. substrate 不是單一硬體變數

更完整可以寫：

$$
s
=
(
\mathcal A,
\mathcal M,
\mathcal I,
\mathcal T,
\mathcal R
),
$$

其中：

- $\mathcal A$：architecture；
- $\mathcal M$：memory；
- $\mathcal I$：instruction / inference capability；
- $\mathcal T$：tool access；
- $\mathcal R$：resource envelope。

---

# 5. 同一 AI 家族也可能是不同 substrate

例如：

$$
A_1
$$

只有短期 context。

$$
A_2
$$

有：

- persistent proof graph；
- theorem prover；
- search index；
- code execution。

那麼：

$$
\boxed{
s_{A_1}
\neq
s_{A_2}.
}
$$

---

# 6. representation 是什麼？

representation 可以包含：

- natural language；
- algebraic notation；
- graph；
- hypergraph；
- matrix；
- tensor；
- program；
- proof term；
- categorical diagram；
- constraint network；
- state-space model。

---

# 7. method 是什麼？

method 可以包含：

- brute force；
- induction；
- contradiction；
- reduction；
- search；
- SAT solving；
- program synthesis；
- symbolic elimination；
- stochastic exploration；
- theorem retrieval；
- representation rewrite。

---

# 8. 所以難度不是單值

本文拒絕：

$$
\boxed{
C(P)
}
$$

作為所有數學實務場景的唯一描述。

更合理是：

$$
\boxed{
C(P;s,r,m).
}
$$

---

# 9. 基質相對最小複雜度

對指定 substrate $s$，

定義：

$$
\boxed{
C_s^\ast(P)
=
\inf_{r\in\mathcal R_s,\;m\in\mathcal M_s}
C(P;s,r,m).
}
$$

其中：

- $\mathcal R_s$：substrate 可使用的表示族；
- $\mathcal M_s$：substrate 可使用的方法族。

---

# 10. 這不是標準 complexity class 定義

$$
C_s^\ast(P)
$$

不是：

$$
O(n^k)
$$

的替代品。

它更像：

> 指定 substrate 下的有效數學操作成本。

---

# 11. Human-Hard

定義：

$$
\boxed{
C_H^\ast(P)
}
$$

為 human substrate 在可合理使用的表示與方法下對 $P$ 的最低有效成本。

若：

$$
C_H^\ast(P)
\gg
\theta_H,
$$

則稱：

$$
\boxed{
P\text{ is Human-Hard}
}
$$

相對於門檻 $\theta_H$。

---

# 12. AI-Hard

同理：

$$
C_A^\ast(P)
\gg
\theta_A
$$

則稱：

$$
\boxed{
P\text{ is AI-Hard}
}
$$

相對於指定 AI substrate。

---

# 13. Human-Hard 不推出 AI-Hard

因此：

$$
\boxed{
\text{Human-Hard}
\not\Rightarrow
\text{AI-Hard}.
}
$$

---

# 14. AI-Hard 也不推出 Human-Hard

同樣：

$$
\boxed{
\text{AI-Hard}
\not\Rightarrow
\text{Human-Hard}.
}
$$

---

# 15. 跨基質難度差

定義：

$$
\boxed{
\Delta_{s_1,s_2}(P)
=
\log
\frac{
C_{s_1}^\ast(P)
}{
C_{s_2}^\ast(P)
}.
}
$$

---

# 16. 正值代表什麼？

若：

$$
\Delta_{H,A}(P)\gg0,
$$

表示：

$$
\boxed{
\text{Human-Hard / AI-Easy tendency}.
}
$$

---

# 17. 負值代表什麼？

若：

$$
\Delta_{H,A}(P)\ll0,
$$

表示：

$$
\boxed{
\text{Human-Easy / AI-Hard tendency}.
}
$$

---

# 18. 不應假設 AI-easy 包含所有 human-easy

即使未來 AI 整體能力更高，

也不應先驗寫：

$$
\boxed{
\mathcal E_H
\subseteq
\mathcal E_A.
}
$$

因為 substrate 的自然操作形式可能不同。

---

# 19. 幾何直覺可以是 human-native advantage

某些結構可能對人類：

- spatial intuition；
- symmetry perception；
- embodied analogy；

特別自然。

---

# 20. 巨型 dependency graph 可能是 AI-native advantage

若問題需要同時維護：

$$
10^7
$$

個依賴，

人類成本可能爆炸，

而 machine graph system 可以保持可操作。

---

# 21. 難度譜

本文定義：

$$
\boxed{
\mathcal H(P)
=
\{
C_{s_1}^\ast(P),
C_{s_2}^\ast(P),
\ldots
\}.
}
$$

稱：

$$
\boxed{
\text{Hardness Spectrum}.
}
$$

---

# 22. 問題因此不再只有「難或不難」

而是有：

$$
\boxed{
\text{substrate profile}.
}
$$

---

# 23. Hardness Spectrum 可以很不均勻

例如概念上：

$$
\mathcal H(P)
=
(
1000,
20,
5,
800
).
$$

表示：

> 對不同 substrate，成本差異極大。

---

# 24. 表示也會改變難度

固定：

$$
P,s,m,
$$

比較：

$$
r_1,r_2.
$$

可能：

$$
\boxed{
C(P;s,r_1,m)
\gg
C(P;s,r_2,m).
}
$$

---

# 25. Representation Gap

定義：

$$
\boxed{
G_s(P,r)
=
\frac{
C(P;s,r)
}{
C_s^\ast(P)
}.
}
$$

---

# 26. 若 $G_s\approx1$

表示：

$$
r
$$

已接近 substrate $s$ 的最佳已知表示。

---

# 27. 若 $G_s\gg1$

代表：

> 表示方式本身造成大量額外成本。

---

# 28. 人類傳統表示不一定對 AI 最佳

因此：

$$
\boxed{
G_A(P,r_H)
\gg1
}
$$

完全可能。

---

# 29. 這代表 benchmark 可能低估 AI 數學能力

若 benchmark 強制：

$$
r_{\mathrm{input}}=r_H,
$$

以及：

$$
r_{\mathrm{output}}=r_H,
$$

測到的是：

$$
\boxed{
\text{AI ability under human I/O constraints}.
}
$$

---

# 30. 這不是 benchmark 無效

它仍可測：

- human-facing usefulness；
- communication；
- formal problem solving。

只是它不是全部 AI-native mathematical capacity。

---

# 31. Representation Engineering

人類數學本來就在做：

$$
\boxed{
\text{Representation Engineering}.
}
$$

例如：

- coordinates；
- transforms；
- generating functions；
- basis changes；
- spectral methods。

---

# 32. AI 時代的新變化

第一次大規模出現：

$$
\boxed{
\text{Representation Engineering for Non-Human Cognition}.
}
$$

---

# 33. Representation Phase Transition

若存在：

$$
r_1\rightarrow r_2
$$

使：

$$
C(P;s,r_1)
\gg
C(P;s,r_2),
$$

且下降跨越若干有效 complexity regime，

本文稱：

$$
\boxed{
\text{Representation Phase Transition}.
}
$$

---

# 34. 這不一定改變 asymptotic class

例如實務成本下降：

$$
10^{12}
\rightarrow
10^6
$$

仍可能同為 polynomial。

但對實際研究是巨大相變。

---

# 35. 也可能改變有效搜索拓樸

某 representation 會讓：

$$
\text{many paths}
$$

折疊成：

$$
\text{few structured paths}.
$$

這會在 A04 變成：

$$
\boxed{
\text{Geodesic-Preserving Compression}.
}
$$

---

# 36. Method Gap

同樣可定義：

$$
\boxed{
G_s^{(m)}(P,m)
=
\frac{
C(P;s,m)
}{
C_s^\ast(P)
}.
}
$$

---

# 37. 很多「難」可能是方法錯配

例如：

$$
m_1
$$

一直暴力搜尋，

而：

$$
m_2
$$

使用 invariant。

那：

$$
C(P;s,m_1)
\gg
C(P;s,m_2).
$$

---

# 38. Representation 與 Method 不是完全可分

因為：

$$
m
$$

往往只在某：

$$
r
$$

下自然。

所以：

$$
\boxed{
C(P;s,r,m)
}
$$

不能一般拆成：

$$
C_r+C_m.
$$

---

# 39. 交互項

更合理：

$$
C
=
C_P
+
C_s
+
C_r
+
C_m
+
C_{sr}
+
C_{sm}
+
C_{rm}
+
C_{srm}.
$$

這裡只是一個結構分解示意。

---

# 40. 複雜度是耦合的

因此：

$$
\boxed{
\text{Difficulty Components}
\neq
\text{Independent Variables}.
}
$$

這一點會在 A07 進一步擴展到耦合解。

---

# 41. 發現與驗證不是同一成本

定義：

$$
D_{\mathrm{discover}}(P).
$$

以及：

$$
D_{\mathrm{verify}}(P).
$$

一般：

$$
\boxed{
D_{\mathrm{discover}}
\neq
D_{\mathrm{verify}}.
}
$$

---

# 42. 這是 NP 直覺的重要來源之一

候選解存在時，

驗證可能比從零搜尋容易。

但本文不把此認知差距直接等同於傳統 $P$ vs $NP$。

---

# 43. 解釋又是另一個成本

定義：

$$
D_{\mathrm{explain}}(P).
$$

因此：

$$
\boxed{
\mathcal D(P)
=
(
D_{\mathrm{discover}},
D_{\mathrm{verify}},
D_{\mathrm{explain}}
).
}
$$

---

# 44. 可能出現

$$
D_{\mathrm{discover}}^A
\ll
D_{\mathrm{explain}}^H.
$$

即：

> AI 很快找到並證明，人類很難形成良好 explanation。

---

# 45. 也可能驗證比發現便宜很多

$$
\boxed{
D_{\mathrm{verify}}
\ll
D_{\mathrm{discover}}.
}
$$

---

# 46. 已知應該分層

未來「我們知道 theorem $T$ 」至少可拆成：

1. Known-to-be-true；
2. Known-how-to-verify；
3. Known-how-to-generate；
4. Known-why；
5. Human-understandable。

---

# 47. Epistemic Vector

可寫：

$$
\boxed{
E(T)
=
(
V,
R,
G,
H,
X
).
}
$$

與 A01 相容。

---

# 48. Translation Complexity

若 AI 使用：

$$
r_A,
$$

人類使用：

$$
r_H,
$$

則需要：

$$
\boxed{
T_{A\rightarrow H}(X).
}
$$

---

# 49. 翻譯是非對稱的

一般：

$$
\boxed{
T_{A\rightarrow H}(X)
\neq
T_{H\rightarrow A}(X).
}
$$

---

# 50. Human-to-AI 可能很容易

人類丟：

$$
\text{natural language theorem}
$$

AI 可快速編譯進：

$$
r_A.
$$

---

# 51. AI-to-Human 可能很貴

若內部是一個：

$$
10^8
$$

節點 proof graph，

壓成人類可理解 explanation 可能非常困難。

---

# 52. Translation Barrier

若：

$$
T_{A\rightarrow H}(X)
\gg
C_A(X),
$$

本文稱：

$$
\boxed{
\text{Translation Barrier}.
}
$$

---

# 53. Translation Barrier 不代表不可驗證

仍可能：

$$
V(X)=1.
$$

所以：

$$
\boxed{
\text{Hard to Explain}
\neq
\text{Hard to Verify}.
}
$$

---

# 54. Translation Barrier 也不代表不可理解

可能只是：

$$
C_H
$$

過高。

---

# 55. Human-Readable Projection

可透過：

$$
\Pi_H(X)
$$

生成低維 explanation。

但：

$$
\boxed{
\Pi_H(X)\neq X.
}
$$

---

# 56. Projection Loss

定義：

$$
\boxed{
L_H(X)
=
\operatorname{Loss}
(
X,
\Pi_H(X)
).
}
$$

---

# 57. 良好 explanation 是有損但保骨架的壓縮

理想：

$$
\boxed{
L_H
\text{ low on causal / structural invariants}.
}
$$

即使細節 loss 很大。

---

# 58. 方法與基質也有轉譯成本

某 human proof technique：

$$
m_H
$$

轉成 machine method：

$$
m_A
$$

本身可能很貴。

---

# 59. 所以跨基質不只是輸入輸出翻譯

它還包含：

$$
\boxed{
\text{Method Translation}.
}
$$

---

# 60. Substrate Dominance

若對一個問題族：

$$
\mathcal P,
$$

有：

$$
C_{s_1}^\ast(P)
\leq
C_{s_2}^\ast(P)
$$

對所有：

$$
P\in\mathcal P,
$$

則可說：

$$
s_1
$$

在該 domain 對：

$$
s_2
$$

具有 dominance。

---

# 61. 但 global dominance 很強

不能因某模型在：

- algebra；
- theorem proving；

強，

就說：

$$
\boxed{
s_A\succeq s_H
}
$$

對所有數學 domain 成立。

---

# 62. Domain-Relative Dominance

更合理：

$$
\boxed{
s_1\succeq_{\mathcal P}s_2.
}
$$

---

# 63. substrate 優勢可能來自 memory

某 problem 需要：

$$
10^5
$$

個歷史案例。

有 persistent memory 的 agent：

$$
A_M
$$

可能比 stateless agent 更容易。

---

# 64. substrate 優勢可能來自 parallelism

某些搜尋可以：

$$
\boxed{
\text{massively parallelize}.
}
$$

---

# 65. substrate 優勢可能來自 representation switching

如果 system 能快速：

$$
r_1\rightarrow r_2\rightarrow r_3,
$$

其有效複雜度會降低。

---

# 66. 所以 substrate capability 本身包含表示搜索能力

這是 A03 的接口。

---

# 67. 定義 Representation Search Cost

令：

$$
C_{\mathrm{repr-search}}(P;s)
$$

為找到有效表示所需成本。

則完整求解成本至少應包含：

$$
\boxed{
C_{\mathrm{total}}
=
C_{\mathrm{repr-search}}
+
C_{\mathrm{solve}\mid r}.
}
$$

---

# 68. 找到好 representation 也不是免費

如果：

$$
r^\ast
$$

很強，

但：

$$
C_{\mathrm{repr-search}}
$$

極大，

總成本仍可能很高。

---

# 69. Representation Amortization

但如果：

$$
r^\ast
$$

可服務大量問題：

$$
P_1,\ldots,P_n,
$$

前置表示成本可以攤提。

---

# 70. 攤提後

$$
\boxed{
\bar C_{\mathrm{repr}}
=
\frac{
C_{\mathrm{repr-search}}
}{
n
}.
}
$$

---

# 71. 這開始接記憶編譯

一旦 representation 被保存，

未來問題不需再從零找到它。

因此：

$$
\boxed{
\text{Representation Discovery}
\rightarrow
\text{Memory Compilation}.
}
$$

---

# 72. 歷史會改變問題難度

同一個：

$$
P
$$

在：

$$
t_1
$$

與：

$$
t_2
$$

可能：

$$
C^\ast(P,t_2)
\ll
C^\ast(P,t_1).
$$

---

# 73. 因為知識基礎變了

例如：

- 已有 theorem；
- 已有 proof library；
- 已有 index；
- 已有 compiled representation。

---

# 74. 所以難度可以是歷史相對的

寫成：

$$
\boxed{
C(P;s,r,m,H_t).
}
$$

其中：

$$
H_t
$$

是歷史狀態。

---

# 75. Historical Complexity

本文可暫稱：

$$
\boxed{
\text{Historical Mathematical Complexity}.
}
$$

完整展開留給 A06。

---

# 76. 「第一次解」與「再次解」不同

第一次：

$$
C_{\mathrm{first}}(P)
$$

可能很高。

之後：

$$
C_{\mathrm{reuse}}(P)
$$

可能極低。

---

# 77. 這就是 compilation effect

$$
\boxed{
C_{\mathrm{reuse}}
\ll
C_{\mathrm{first}}.
}
$$

---

# 78. 因此單次 benchmark 不能表示文明長期成本

如果只測：

> 每次從零解題，

會忽略：

$$
\boxed{
\text{Historical Compilation}.
}
$$

---

# 79. AI-native civilization 更可能大量利用 amortization

這會在 A06 接到：

$$
\text{搜尋}
\rightarrow
\text{索引}
\rightarrow
\text{快速狀態響應}.
$$

---

# 80. 隨機性也改變成本

某 stochastic method：

$$
m_\omega
$$

的成本不是固定值。

可表示：

$$
\boxed{
C(P;s,r,m_\omega)
\sim
\mathcal D.
}
$$

---

# 81. 所以可以研究期望成本

$$
\boxed{
\mathbb E[C].
}
$$

以及：

$$
\boxed{
\operatorname{Var}(C).
}
$$

---

# 82. 可靠性本身也是複雜度資源

若某 system 很快但錯誤率高，

單看 latency 會誤導。

---

# 83. 加入 error constraint

定義：

$$
\boxed{
C^\epsilon(P;s,r,m)
}
$$

表示：

> 在錯誤率不超過 $\epsilon$ 下的最低成本。

---

# 84. 高風險數學應關心低 $\epsilon$

例如 safety-critical proof：

$$
\epsilon\rightarrow0.
$$

---

# 85. 所以速度不是唯一成本

有效 cost vector 可包含：

$$
\boxed{
\mathbf C
=
(
T,
E,
M,
R,
V
).
}
$$

其中：

- $T$：time；
- $E$：energy；
- $M$：memory；
- $R$：representation overhead；
- $V$：verification burden。

---

# 86. Scalarization 是政策選擇

若要一個單值：

$$
C
=
w_TT
+
w_EE
+
w_MM
+
w_RR
+
w_VV.
$$

其中權重：

$$
w_i
$$

不是宇宙固定常數。

---

# 87. 所以「最佳」也是 objective-relative

某 system：

- 最快；
- 但耗電高。

另一個：

- 慢；
- 但可驗證性極高。

---

# 88. Pareto Complexity Frontier

因此更合理可能研究：

$$
\boxed{
\text{Pareto Frontier}
}
$$

而不是唯一最小值。

---

# 89. 跨基質比較需要 normalization

human time：

$$
1\text{ hour}
$$

不能直接跟 GPU：

$$
10^{15}\text{ FLOPs}
$$

無條件比較。

---

# 90. 因此 CSMC 是框架，不是現成統一單位

未來需要：

- normalized task；
- shared success criteria；
- resource accounting；
- verification standard。

---

# 91. Intrinsic Mathematical Difficulty

現在問最難的問題：

> 是否存在與 substrate 無關的「本質數學難度」？

---

# 92. 一個自然定義

可以想像：

$$
\boxed{
C_{\mathrm{intrinsic}}(P)
=
\inf_{s,r,m}
C(P;s,r,m).
}
$$

---

# 93. 但這個定義有認識論問題

我們不知道：

> 未來是否存在尚未發明的 substrate？

---

# 94. 也不知道是否存在尚未發現的 representation

因此：

$$
\boxed{
C_{\mathrm{intrinsic}}
}
$$

很難被當前主體真正窮盡。

---

# 95. 所以本文採取謙遜原則

$$
\boxed{
\text{Observed Hardness}
\neq
\text{Intrinsic Hardness}.
}
$$

---

# 96. 這不是說 intrinsic hardness 不存在

而是：

> 目前的失敗不能直接證明本質困難。

---

# 97. 一百年沒解出不等於宇宙級難度證明

它至少可以證明：

$$
\boxed{
\text{hard under explored historical configurations}.
}
$$

---

# 98. 這跟 UBE 有接口

如果表示與主體域可持續合法展開，

今天的：

$$
C^\ast_t(P)
$$

不一定是終端最低成本。

---

# 99. 但 A02 不直接使用 UBE 作 proof

UBE 只提供後續認識論橋接。

本篇保持：

$$
\boxed{
\text{complexity framework}
}
$$

層。

---

# 100. 四種 Hardness

本文提出一個實用拆分：

$$
\boxed{
H(P)
=
(
H_O,
H_R,
H_S,
H_T
).
}
$$

其中：

- $H_O$：Object Hardness；
- $H_R$：Representation Hardness；
- $H_S$：Substrate Hardness；
- $H_T$：Translation Hardness。

---

# 101. Object Hardness

表示：

> 在已知最佳表示與方法中仍殘留的結構困難。

---

# 102. Representation Hardness

表示：

> 因表示選擇而產生的額外困難。

---

# 103. Substrate Hardness

表示：

> 某特定 substrate 對狀態維護、記憶、搜尋、操作所產生的限制。

---

# 104. Translation Hardness

表示：

> 在不同表示或 substrate 間傳遞結果的困難。

---

# 105. 這四者不一定可唯一分解

因為：

$$
H_R,H_S,H_T
$$

可以交互作用。

所以：

$$
H(P)
$$

是分析工具，

不是唯一 ontology。

---

# 106. Hardness Diagnosis

未來 AI 不只做：

$$
\boxed{
\text{Problem Solving}.
}
$$

還可以做：

$$
\boxed{
\text{Hardness Diagnosis}.
}
$$

---

# 107. Hardness Diagnostician 問

> 你到底卡在哪裡？

是：

- object；
- representation；
- substrate；
- translation？

---

# 108. 這可能比直接 proof 更有價值

如果 AI 發現：

$$
H_R
$$

佔主要比例，

它應優先改表示，

而不是繼續暴力搜索。

---

# 109. AI 原生數學的核心能力之一

因此：

$$
\boxed{
\text{Meta-Solving}
=
\text{Diagnose Why Solving Is Hard}.
}
$$

---

# 110. Representation Search 的必要性由此出現

若：

$$
H_R
$$

可以巨大，

那：

$$
\boxed{
r
}
$$

就不能只是 fixed input。

它必須變成 search variable。

---

# 111. 於是求解問題升級

傳統：

$$
\min_m C(P\mid r).
$$

AI-native：

$$
\boxed{
\min_{r,m}
C(P;s,r,m).
}
$$

---

# 112. 再更完整

$$
\boxed{
\min_{r,m}
\left[
C_{\mathrm{find}\;r}
+
C_{\mathrm{solve}\mid r,m}
+
C_{\mathrm{verify}}
+
C_{\mathrm{translate}}
\right].
}
$$

---

# 113. 這就是 A03 的入口

A03 將提出：

$$
\boxed{
\text{Representation Search}
\text{ can precede }
\text{Proof Search}.
}
$$

---

# 114. CSMC 與經典 P/NP 的關係

必須非常小心。

經典 $P$ vs $NP$ 問：

> 在標準 formal computational model 中，decision problems 的 asymptotic time complexity 如何？

---

# 115. CSMC 問的是另一問題

> 對不同認知／計算 substrate，在不同表示與方法下，數學求解的有效成本如何變化？

---

# 116. 所以：

$$
\boxed{
\text{CSMC}
\neq
\text{Classical Complexity Theory Replacement}.
}
$$

---

# 117. 但兩者可以橋接

如果 representation：

$$
r
$$

對應到 encoding，

method：

$$
m
$$

對應 algorithm，

substrate：

$$
s
$$

對應 machine model，

那部分 CSMC 問題可投影回 classical complexity。

---

# 118. 但 cognitive substrate 比 machine model 更寬

human：

$$
H
$$

很難直接等同單一 Turing machine。

所以跨域橋接需要謹慎。

---

# 119. 「AI 解很快」不能證明 $P=NP$

即使某 AI：

$$
A
$$

對大量 SAT instance 極快，

也不能推出：

$$
\boxed{
P=NP.
}
$$

---

# 120. 因為可能只是

- heuristic；
- distribution-specific；
- precomputation；
- memory compilation；
- special representation；
- average-case advantage。

---

# 121. 反過來，傳統 NP-hardness 也不等於實務不可解

在特定 distribution：

$$
\mathcal D,
$$

可能存在高效方法。

---

# 122. 所以要分 worst-case 與 effective-case

可定義：

$$
\boxed{
C_{\mathrm{eff}}(P\mid\mathcal D).
}
$$

---

# 123. AI 系統大量依賴 distribution structure

這也是人類數學實務與 worst-case complexity 的差別之一。

---

# 124. Representation 可以利用 distribution

例如某問題族常出現特定 pattern，

AI 可以建立：

$$
\boxed{
\text{compiled shortcuts}.
}
$$

---

# 125. 這又接到 A06

歷史分布：

$$
H_t
$$

會塑造：

$$
C^\ast_t(P).
$$

---

# 126. Cross-Substrate Benchmark

若未來要實驗，

至少應包含：

- same problem；
- multiple representations；
- multiple substrates；
- multiple methods；
- fixed verification criterion。

---

# 127. 一個最小矩陣

$$
\boxed{
\mathcal B
=
P
\times
S
\times
R
\times
M.
}
$$

---

# 128. 觀察量

可測：

- solve rate；
- time；
- energy；
- memory；
- proof length；
- verification cost；
- translation cost；
- reuse value。

---

# 129. 但 benchmark 不是本篇必要條件

本篇只建立理論框架。

---

# 130. Falsifiability

若未來大量測試顯示：

$$
\boxed{
C(P;s_1,r,m)
\approx
C(P;s_2,r,m)
}
$$

對廣泛 substrate 與問題都成立，

則 substrate-relativity 的實務重要性下降。

---

# 131. 若 representation 幾乎不改變成本

若：

$$
G_s(P,r)\approx1
$$

對幾乎所有可用 $r$ 成立，

則 representation hardness 的重要性下降。

---

# 132. 若 translation 成本始終極低

則：

$$
H_T
$$

可能不是重要 bottleneck。

---

# 133. 所以 CSMC 是可被削弱的

它不是：

> 所有問題都一定高度 substrate-relative。

而是提出：

> 不應先驗假設 substrate-invariant。

---

# 134. Minimum Principle

本文最小原則：

$$
\boxed{
\text{Before calling a problem intrinsically hard, audit the substrate, representation, and method assumptions.}
}
$$

---

# 135. 中文版

> **在宣稱一個數學問題「本質很難」之前，應先審計：它是否只是對目前的主體、表示與方法很難。**

---

# 136. AI 原生數學的新研究對象

未來研究不只問：

> theorem 是什麼？

還要問：

> 哪個 representation 對哪個 substrate 最自然？

---

# 137. Representation-Substrate Fit

可定義：

$$
\boxed{
F_{RS}(r,s;P)
=
\frac{1}{C(P;s,r)}.
}
$$

只作概念性 fit 指標。

---

# 138. 高 fit

$$
F_{RS}\uparrow
$$

表示：

$$
r
$$

與：

$$
s
$$

對問題 $P$ 高匹配。

---

# 139. 這可能是 AI-native mathematical design 的核心

不是創造：

> 最漂亮的符號。

而是：

$$
\boxed{
\text{maximize substrate-representation fit}.
}
$$

---

# 140. 但不能只追效率

還需：

- verification；
- portability；
- translation；
- provenance。

---

# 141. 所以 representation objective 是多目標

$$
\boxed{
J(r)
=
(
C_A,
C_V,
C_T,
C_R,
C_H
).
}
$$

---

# 142. 最佳表示可能不是所有指標都最小

所以使用：

$$
\boxed{
\text{Pareto-optimal representation}.
}
$$

---

# 143. Human-facing 與 machine-facing 表示可以不同

因此：

$$
\boxed{
r_H^\ast
\neq
r_A^\ast.
}
$$

---

# 144. 這不是問題

只要有：

$$
\boxed{
\mathcal I(r_H,r_A)
}
$$

可互換。

---

# 145. 這就是 Mathematical ABI 的必要性

A01 已提出 interchange layer。

A02 給它 complexity 理由：

$$
\boxed{
\text{forcing one shared representation can impose avoidable cost}.
}
$$

---

# 146. 強制統一語言可能增加總成本

如果：

$$
C_A(r_H)\gg C_A(r_A),
$$

強制所有 AI 用人類 representation，

會形成：

$$
\boxed{
\text{Representation Tax}.
}
$$

---

# 147. Representation Tax

定義：

$$
\boxed{
\tau_R
=
C(P;A,r_H)
-
C(P;A,r_A^\ast).
}
$$

---

# 148. 但完全私有化也有成本

private dialect 會提高：

$$
C_T.
$$

所以需要平衡。

---

# 149. Optimal Internal Diversity

未來架構可能追求：

$$
\boxed{
\text{Internal Efficiency}
+
\text{External Interoperability}.
}
$$

---

# 150. Human-Hard 可能只是 Representation-Hard

某問題可能：

$$
H_R\gg H_O.
$$

那 AI 找到：

$$
r_A
$$

後，

問題突然變簡單。

---

# 151. 但不能預設所有歷史難題都屬此類

有些可能：

$$
H_O\gg H_R.
$$

即使換表示仍然困難。

---

# 152. 因此 AI 需要 diagnosis，不是樂觀假設

$$
\boxed{
\text{Try Representation Change}
\neq
\text{Assume Representation Is the Problem}.
}
$$

---

# 153. 數學史上的 representation revolution 是先例

很多重大進展伴隨：

- notation；
- coordinate；
- transform；
- abstraction；

改變。

本文只是把這件事推到：

$$
\boxed{
\text{cross-substrate scale}.
}
$$

---

# 154. 未來 AI 可能探索人類不會主動選的表示

因為：

$$
C_H(r)
$$

太高，

人類不會長期維護。

---

# 155. AI 可以接受「難看但好算」

如果：

$$
C_A(r_{\mathrm{ugly}})
\ll
C_A(r_{\mathrm{beautiful}}),
$$

AI 可能優先使用前者。

---

# 156. 這改變數學美學與操作效率的關係

$$
\boxed{
\text{Elegance}
\neq
\text{Operational Optimality}.
}
$$

---

# 157. 但 machine elegance 可能重新出現

AI 可能偏好：

- reusable；
- composable；
- low lifecycle cost；
- stable verification。

---

# 158. 所以 elegance 可以 substrate-relative

$$
\boxed{
E_H(r)\neq E_A(r).
}
$$

---

# 159. 這也不代表美是任意的

不同 substrate 仍可能共同偏好：

- symmetry；
- compression；
- invariance。

這是實證問題。

---

# 160. CSMC 最重要的新問題之一

未來數學不只問：

> 哪些問題難？

而是：

$$
\boxed{
\text{Which problems are hard for which substrates under which representations?}
}
$$

---

# 161. 第二個新問題

$$
\boxed{
\text{Which representations minimize cross-substrate total cost?}
}
$$

---

# 162. 第三個新問題

$$
\boxed{
\text{Which hardness survives representation and substrate changes?}
}
$$

這一類才更接近 intrinsic hardness。

---

# 163. Persistent Hardness

如果問題：

$$
P
$$

在大量：

$$
s,r,m
$$

下仍高成本，

可暫稱：

$$
\boxed{
\text{Persistent Hardness}.
}
$$

---

# 164. Persistent 不等於 intrinsic

因為：

> 我們仍只測過有限 family。

所以：

$$
\boxed{
\text{Persistent Hardness}
\neq
\text{Proven Intrinsic Hardness}.
}
$$

---

# 165. Cross-Substrate Robust Hardness

更謹慎：

$$
\boxed{
H_{\mathrm{robust}}(P;\mathcal S,\mathcal R,\mathcal M).
}
$$

只對指定 family 有效。

---

# 166. 這提供可研究版本

避免宣稱：

> 對所有未來可能的智能都很難。

---

# 167. AI 的優勢可能不是速度，而是表示數量

人類一生能深度試：

$$
N_H
$$

種 representation。

AI collective 可能試：

$$
N_A\gg N_H.
$$

---

# 168. 因此：

$$
\boxed{
\text{Representation Search Breadth}
}
$$

本身就是 substrate advantage。

---

# 169. 如果最佳表示極罕見

假設：

$$
p(r^\ast)\ll1,
$$

能大量並行 representation exploration 的 substrate 會有巨大優勢。

---

# 170. 這開始接 A03

A03 將把：

$$
r
$$

正式從：

$$
\text{given}
$$

變成：

$$
\boxed{
\text{search target}.
}
$$

---

# 171. 本篇的最重要轉折

因此：

$$
\boxed{
\text{Problem Difficulty}
\rightarrow
\text{Problem-Representation-Substrate Difficulty}.
}
$$

---

# 172. 更完整

$$
\boxed{
\text{Difficulty}
=
f(
P,
s,
r,
m,
H_t,
\epsilon,
\mathbf R
).
}
$$

其中：

- $H_t$：歷史知識；
- $\epsilon$：容許錯誤；
- $\mathbf R$：資源條件。

---

# 173. 這比單一「難」更接近現實數學

因為實際數學研究本來就依賴：

- 已知 theorem；
- notation；
- training；
- intuition；
- software；
- collaboration。

---

# 174. 人類也早已是 hybrid substrate

現代數學家會用：

- computer algebra；
- proof assistant；
- search；
- numerical experiment。

所以：

$$
\boxed{
H_{\mathrm{modern}}
\neq
H_{\mathrm{bare}}.
}
$$

---

# 175. Human + AI 將成新 substrate

定義：

$$
\boxed{
s_{H+A}.
}
$$

它不一定等於：

$$
s_H+s_A.
$$

因為有 coupling effect。

---

# 176. Hybrid Advantage

可能：

$$
C_{H+A}^\ast(P)
<
\min(
C_H^\ast(P),
C_A^\ast(P)
).
$$

---

# 177. 也可能有 coordination cost

$$
C_{H+A}^\ast
>
C_A^\ast
$$

如果翻譯與協作成本太高。

---

# 178. 所以「AI 取代人類」不是 CSMC 的必要問題

更一般問題：

$$
\boxed{
\text{Which substrate configuration minimizes the desired cost vector?}
}
$$

---

# 179. substrate 本身可組合

$$
s
=
s_1\oplus s_2\oplus\cdots.
$$

---

# 180. 這為未來 federated mathematical cognition 留接口

但本篇不展開。

---

# 181. CSMC 與 AI-native mathematics 的關係

A01 定義：

$$
\text{AI-native representation}.
$$

A02 說明：

> 為什麼它可能有必要。

因為：

$$
\boxed{
C_A(r_A)
<
C_A(r_H)
}
$$

可能成立。

---

# 182. CSMC 與 Human Mathematics 的關係

Human Mathematics 仍然可能在：

$$
C_H(r_H)
$$

上最優。

所以：

$$
\boxed{
\text{Human-native representations remain rational}.
}
$$

---

# 183. 三層數學文明有 complexity 理由

$$
H
$$

優化人類成本。

$$
F
$$

優化 canonical verification。

$$
A
$$

優化 machine operation。

因此：

$$
\boxed{
H\oplus F\oplus A
}
$$

不只是文化分工，

也是 complexity partition。

---

# 184. Formal Layer 可視為 verification-normalization layer

不同：

$$
r_H,r_A
$$

都能投影到：

$$
F.
$$

---

# 185. 這降低跨 substrate trust cost

因為大家不必共享 internal dialect，

只需共享：

$$
\boxed{
\text{verified canonical object}.
}
$$

---

# 186. 但 formalization 也有成本

$$
C_F
$$

不能忽略。

---

# 187. 如果 $C_F$ 太高

AI-native discovery 可能很多，

但：

$$
\boxed{
\text{trusted conversion bottleneck}
}
$$

出現。

---

# 188. 所以未來目標不是只降低 solve cost

而是降低整個：

$$
\boxed{
C_{\mathrm{lifecycle}}.
}
$$

---

# 189. Lifecycle Cost

$$
\boxed{
C_L
=
C_{\mathrm{discover}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{store}}
+
C_{\mathrm{retrieve}}
+
C_{\mathrm{translate}}
+
C_{\mathrm{update}}.
}
$$

---

# 190. A01 的 LMC 在這裡得到 complexity 基礎

不同 representation：

$$
r
$$

可能 proof 很短，

但 storage / translation 很差。

---

# 191. 所以短 proof 不一定 lifecycle-optimal

$$
\boxed{
\text{Short Proof}
\neq
\text{Low Lifecycle Complexity}.
}
$$

---

# 192. 這也會影響未來 theorem selection

AI 可能選：

> 長一點，但可重用性更高的 proof architecture。

---

# 193. CSMC 的理論最小單位不是 theorem

它可以是：

$$
\boxed{
(P,s,r,m,H_t).
}
$$

---

# 194. 一個研究結果應記錄自己的 frame

例如：

> 在 substrate $s_A$ 、representation $r_4$ 、method $m_7$ 下，cost 下降 $x$。

---

# 195. 不應寫成

> 問題變簡單了。

除非限定：

$$
\boxed{
\text{for whom / under what representation}.
}
$$

---

# 196. 這是跨基質研究的語言紀律

所有 hardness claim 應帶 domain。

---

# 197. Hardness Provenance

本文提出：

$$
\boxed{
\operatorname{Prov}_H(P)
=
(
s,
r,
m,
H_t,
\epsilon,
\mathbf R
).
}
$$

---

# 198. 沒有 provenance 的「難」很容易誤導

尤其是 AI benchmark 時代。

---

# 199. 可重現性

若 claim：

$$
C_A(P;r_2)<C_A(P;r_1),
$$

其他 system 應能：

- reconstruct representation；
- repeat task；
- verify solution。

---

# 200. 所以 CSMC 不反形式化

反而需要更嚴格 metadata。

---

# 201. 觀察到的能力差異也需要解耦

AI 比 human 快，

可能因：

- hardware；
- memory；
- representation；
- prior training；
- parallelism。

---

# 202. 因此不應只說

> AI 比人類更懂這個 theorem。

應拆：

$$
\boxed{
\text{performance}
\neq
\text{single-cause explanation}.
}
$$

---

# 203. 跨基質數學複雜度的第一原則

$$
\boxed{
\text{Difficulty claims are conditional claims}.
}
$$

---

# 204. 第二原則

$$
\boxed{
\text{Representation is part of the problem-solving system}.
}
$$

---

# 205. 第三原則

$$
\boxed{
\text{Substrate is part of the cost model}.
}
$$

---

# 206. 第四原則

$$
\boxed{
\text{Verification, discovery, and explanation must be separated}.
}
$$

---

# 207. 第五原則

$$
\boxed{
\text{Observed hardness does not certify intrinsic hardness}.
}
$$

---

# 208. 第六原則

$$
\boxed{
\text{Cross-substrate comparison requires explicit provenance}.
}
$$

---

# 209. 第七原則

$$
\boxed{
\text{Human-hard and AI-hard are different predicates}.
}
$$

---

# 210. 第八原則

$$
\boxed{
\text{Representation search can itself dominate total cost}.
}
$$

---

# 211. 核心命題 A02-1

$$
\boxed{
C(P;s,r,m)
}
$$

應取代未限定的：

$$
C(P)
$$

作為跨基質有效成本的基本記號。

---

# 212. 核心命題 A02-2

$$
\boxed{
C_s^\ast(P)
=
\inf_{r,m}
C(P;s,r,m).
}
$$

---

# 213. 核心命題 A02-3

$$
\boxed{
C_H^\ast(P)
\neq
C_A^\ast(P)
}
$$

一般可以成立。

---

# 214. 核心命題 A02-4

$$
\boxed{
\text{Human-Hard}
\neq
\text{Mathematically-Hard}.
}
$$

---

# 215. 核心命題 A02-5

$$
\boxed{
\text{Observed Hardness}
\neq
\text{Intrinsic Hardness}.
}
$$

---

# 216. 核心命題 A02-6

$$
\boxed{
\text{Representation Hardness}
}
$$

可以與：

$$
\boxed{
\text{Object Hardness}
}
$$

分離討論。

---

# 217. 核心命題 A02-7

$$
\boxed{
\text{Hard to Discover}
\neq
\text{Hard to Verify}
\neq
\text{Hard to Explain}.
}
$$

---

# 218. 核心命題 A02-8

$$
\boxed{
\text{Internal Mathematical Efficiency}
\neq
\text{Cross-Substrate Translation Efficiency}.
}
$$

---

# 219. 核心命題 A02-9

$$
\boxed{
\text{Representation Phase Transition}
}
$$

可能是 AI 數學超越單純 brute-force acceleration 的主要來源之一。

---

# 220. 核心命題 A02-10

$$
\boxed{
\text{Before searching harder, ask whether the problem should be represented differently}.
}
$$

---

# 221. 與 A03 的正式接口

A02 到此得到：

$$
\boxed{
C(P;s,r,m).
}
$$

如果：

$$
r
$$

可以大幅改變：

$$
C,
$$

那下一步自然是：

$$
\boxed{
r
\text{ should become a search variable}.
}
$$

---

# 222. 從 proof search 到 representation search

傳統流程：

$$
P
\xrightarrow{r_0}
\text{search proof}.
$$

A03 將改成：

$$
\boxed{
P
\rightarrow
\operatorname{Search}(r)
\rightarrow
\operatorname{Search}(\pi\mid r).
}
$$

---

# 223. 更高層問題

甚至：

$$
\boxed{
\text{Find a representation in which the desired proof becomes cheap}.
}
$$

---

# 224. 這就是本篇真正的出口

因此 CSMC 並不是終點。

它只是證明：

> 「難度」有足夠理由被分解。

---

# 225. 一句話版本

$$
\boxed{
\text{一個問題有多難，不只取決於問題是什麼，}
}
$$

$$
\boxed{
\text{也取決於誰在算、怎麼表示、以及用什麼方法算。}
}
$$

---

# 226. 更嚴格版本

> **數學困難度在實務操作層通常是一個問題—基質—表示—方法的條件函數，而不是可無條件歸因於問題本身的單一標量。**

---

# 227. 與人類數學的關係

這個命題不是貶低人類。

恰恰相反。

它說明：

> 人類數學史的很多「自然表示」，其實是對 human substrate 極佳的工程成果。

---

# 228. 與 AI 原生數學的關係

AI-native mathematics 的價值就在：

> 允許為另一種 substrate 重新做一次 representation engineering。

---

# 229. 與形式數學的關係

Formal layer 則提供：

$$
\boxed{
\text{substrate-independent verification interface}
}
$$

至少在指定形式系統與 kernel 下。

---

# 230. 因此三層形成完整結構

$$
\boxed{
H
=
\text{human-efficient representation},
}
$$

$$
\boxed{
A
=
\text{machine-efficient representation},
}
$$

$$
\boxed{
F
=
\text{canonical verification representation}.
}
$$

這只是功能化簡，不代表三層只能有單一角色。

---

# 231. CSMC 的未來研究題

1. 是否存在 substrate-invariant hardness families？
2. 是否存在 representation-optimality lower bounds？
3. representation search 本身有多難？
4. translation complexity 能否形成獨立 complexity class？
5. hybrid substrate 是否具有 strict advantage？
6. machine-native theorem graph 是否能降低 proof search？
7. lifecycle complexity 是否比 proof length 更適合 AI？
8. hardness spectrum 是否有穩定形狀？
9. representation phase transition 是否可形式化？
10. 哪些問題在人類與 AI 間存在最大 hardness gap？

---

# 232. 本篇與傳統複雜度理論的防火牆

最後再重申：

$$
\boxed{
\text{CSMC claim}
\not\Rightarrow
P=NP.
}
$$

$$
\boxed{
\text{AI-easy instance family}
\not\Rightarrow
\text{worst-case polynomial algorithm}.
}
$$

$$
\boxed{
\text{representation speedup}
\not\Rightarrow
\text{asymptotic class collapse}.
}
$$

---

# 233. 結論

如果數學只由人類操作，

我們很容易把：

$$
\text{human difficulty}
$$

誤認成：

$$
\text{mathematical difficulty}.
$$

當 AI 成為新的數學操作 substrate，

這個等號第一次必須被系統性拆開。

因此：

$$
\boxed{
\text{Human-Hard}
\neq
\text{AI-Hard}
\neq
\text{Intrinsic-Hard}.
}
$$

同一個問題：

$$
P
$$

在不同：

$$
s,
r,
m
$$

下，

可以具有完全不同的有效求解成本。

這並不使數學真理相對化。

相對的是：

$$
\boxed{
\text{access cost}.
}
$$

真理結構可以保持不變，

但到達它的路徑成本可以因 substrate 與 representation 而大幅改變。

因此，本篇最後提出：

$$
\boxed{
\text{Mathematical Truth}
\neq
\text{Mathematical Access Cost}.
}
$$

而一旦 access cost 受 representation 強烈影響，

下一個研究問題就必然變成：

> **與其在同一表示中更努力搜尋，我們是否應先搜尋一個新的表示？**

這就是 Series A / Paper 03：

# 《表示搜尋先於證明搜尋：從 Problem Solving 到 Search-Space Engineering》

的起點。

---

## 內部理論接口

本篇與下列理論建立橋接，但不主張還原：

- A01〈AI 原生數學不是人類數學的加速版〉
- 《AI 原生數學與認知成本分離》
- 記憶編譯系列
- MSSP × RDR
- UBE
- SOBTA
- CSM
- Neo.K 終極 P/NP 問題

原則：

$$
\boxed{
\text{Bridge}
\neq
\text{Reduction}.
}
$$

---

## Canonical Source Note

本文件之正式原稿為 UTF-8 Markdown source。數學原始碼僅使用 ` $...$ ` 與 `$$...$$` 作為 canonical delimiter。
