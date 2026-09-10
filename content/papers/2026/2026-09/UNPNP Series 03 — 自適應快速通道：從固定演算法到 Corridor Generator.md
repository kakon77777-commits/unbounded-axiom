# UNPNP Series 03  
## 自適應快速通道：從固定演算法到 Corridor Generator  
### Adaptive Fast Corridors: From Fixed Algorithms to Corridor Generators

**系列名稱：** UNPNP Hyperlink & Crystallized Computation Series  
**系列篇次：** 03  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** AI 原生計算／自適應元演算法／UNPNP 理論論文  
**狀態：** Canonical Draft  

---

## 摘要

UNPNP Series 01 將計算複雜度重新理解為可在建構、表示、搜尋、索引、驗證、執行與維護之間轉移的多維成本結構；Series 02 則將超連結重新定義為跨底空間的可尋址計算 transition。由此自然產生下一個問題：

> 如果計算世界中存在大量候選超連結，那麼究竟由誰決定「現在應該走哪一條路」？

本文提出 **Adaptive Corridor Generator** 作為 UNPNP Computer 的前端控制核心。它不是單純 Planner，也不是固定路由表，更不是每一步都呼叫大型語言模型重新思考。其基本任務是：根據當前狀態、目標、歷史、資源、風險、底空間幾何、已知路徑與新穎性，選擇、生成、驗證或重新展開當前最適合的計算通道。

本文將自適應通道生成器寫為：

$$
\boxed{
\mathcal M:
(s_t,g,h_t,B_t,R_t,\mathcal G_t,\mathcal K_t)
\mapsto
\Phi_t
}
$$

其中：

- $s_t$：當前狀態；
- $g$：任務目標；
- $h_t$：歷史；
- $B_t$：計算／時間／能源預算；
- $R_t$：風險與權限條件；
- $\mathcal G_t$：當前可見計算圖；
- $\mathcal K_t$：已結晶的快速通道集合；
- $\Phi_t$：此次生成或選擇的 corridor。

本文進一步區分五種不同強度的快速通道主張：

$$
\mathsf{LGC}
\prec
\mathsf{FGC}
\prec
\mathsf{AGC}
\prec
\mathsf{UGC}
\prec
\mathsf{EGC},
$$

即局部通道、問題族通道、自適應通道、通用通道生成與極強通用通道。本文主張，近期最具工程可驗證性的目標不是直接追求通用固定捷徑，而是研究：

$$
\boxed{
\text{能否建立一個低成本、可回退、可學習的 corridor generator。}
}
$$

本文也提出 novelty threshold、reasoning escalation、known-route fast path、corridor utility、repair versus re-solve、distribution shift 與 fail-closed 等機制，並主張：

$$
\boxed{
\text{Reasoning should be invoked when routing knowledge is insufficient, not by default.}
}
$$

因此，真正 AI-native 的計算系統不應把模型推理當成每一步必經路徑，而應把模型推理視為一種昂貴、可按需提升的 corridor-generation capability。

本文最後建立「固定程式」與「會長路的程式」之間的轉折：UNPNP Computer 的核心不是永遠沿著預先寫好的路運行，而是在可控條件下持續觀察、生成、評估、驗證與淘汰通道，使計算圖本身逐步適應其所處世界。

**關鍵詞：** UNPNP、自適應演算法、Corridor Generator、快速通道、AI 原生計算、Meta-controller、routing、novelty threshold、adaptive planning、path generation、uniformity

---

# 1. 問題：誰來決定下一條超連結？

Series 02 已建立：

$$
\ell:
(\mathcal B_i,s_i,H_t)
\rightarrow
(\mathcal B_j,s_j,H_{t+1}).
$$

如果可用 transition 只有一條，問題很簡單。

但一般情況中：

$$
|\mathcal L_t|\gg 1.
$$

甚至某些狀態下：

$$
|\mathcal L_t|
\rightarrow
\text{large}.
$$

因此真正的 runtime 問題變成：

$$
\boxed{
\text{Which transition should be selected now?}
}
$$

這不是普通搜尋排序。

因為 transition 選擇會改變：

- 下一個底空間；
- 可見狀態；
- 可用工具；
- 計算成本；
- 風險；
- 未來可走路徑；
- 是否需要重新推理；
- 是否能形成新的結晶。

所以它是一個計算路由問題。

---

# 2. Planner 不足以描述這個角色

一般 Planner 可以抽象為：

$$
\operatorname{Plan}(g,s_t)
\rightarrow
(a_1,a_2,\ldots,a_n).
$$

這通常假設：

- action space 大致已知；
- 計畫主要是選擇；
- 世界模型相對固定；
- 路由不會因運行而新增 primitive。

但 UNPNP 中：

$$
\mathcal L_{t+1}
\neq
\mathcal L_t
$$

可能成立。

也就是：

> 系統不只選擇現有路徑，也可能生成新的路徑。

所以更適合的角色不是單純 Planner，而是：

$$
\boxed{
\text{Adaptive Corridor Generator}.
}
$$

---

# 3. Corridor 的基本定義

本文將 corridor 定義為：

$$
\Phi_t
=
\langle
F_t,
\Gamma_t,
G_t,
V_t,
C_t
\rangle.
$$

其中：

- $F_t$：candidate frontier；
- $\Gamma_t$：選中的 transition chain；
- $G_t$：guard / applicability conditions；
- $V_t$：verification strategy；
- $C_t$：estimated total cost。

Corridor 不必是一條單一路徑。

它也可以是：

$$
\Phi_t
=
\Gamma_1
\parallel
\Gamma_2
$$

的平行探索，

或：

$$
\Gamma_1
\triangleright
\Gamma_2
$$

的條件序列。

---

# 4. 自適應通道生成器

本文提出：

$$
\boxed{
\mathcal M:
(s_t,g,h_t,B_t,R_t,\mathcal G_t,\mathcal K_t)
\mapsto
\Phi_t.
}
$$

其中：

$$
s_t
$$

是目前 state；

$$
g
$$

是 goal；

$$
h_t
$$

是歷史執行／搜尋／驗證記錄；

$$
B_t
$$

是剩餘資源；

$$
R_t
$$

是 risk / authorization state；

$$
\mathcal G_t
$$

是目前可見計算圖；

$$
\mathcal K_t
$$

是已知並驗證的結晶通道；

$$
\Phi_t
$$

是此次選出的 corridor。

---

# 5. 自適應不是「每次重新想」

需要避免一個常見錯誤。

所謂 adaptive 不代表：

> 每次狀態一變，都叫最強模型完整推理一次。

那會導致：

$$
C_{\mathrm{reasoning}}
$$

本身成為主要成本。

真正合理的 adaptive system 應該優先使用已知結構：

$$
\boxed{
\text{Known}
\rightarrow
\text{Reuse}.
}
$$

只有：

$$
\boxed{
\text{Unknown}
\rightarrow
\text{Reason}.
}
$$

因此：

$$
\text{adaptivity}
\neq
\text{constant deliberation}.
$$

---

# 6. Known-Route Fast Path

若目前狀態：

$$
s_t
$$

符合某個已驗證通道：

$$
\widehat{\ell}_k
$$

的 guard：

$$
G_k(s_t)=1,
$$

且：

$$
S_H(\widehat{\ell}_k)\ge\theta_H,
$$

則可以直接：

$$
s_t
\xrightarrow{\widehat{\ell}_k}
s_{t+1}.
$$

不需要完整 Planner。

所以：

$$
\boxed{
\text{Stable known route}
\Rightarrow
\text{fast path}.
}
$$

---

# 7. Novelty Threshold

需要推理的核心不是：

> 狀態有沒有變？

因為世界每一刻都可能有微小變動。

真正要問的是：

> 變化是否超出既有 corridor 的有效域？

定義 novelty：

$$
N(s_t\mid\mathcal K_t).
$$

若：

$$
N(s_t\mid\mathcal K_t)
<
\theta_N,
$$

則：

$$
\text{reuse}.
$$

若：

$$
N(s_t\mid\mathcal K_t)
\ge
\theta_N,
$$

則：

$$
\text{reveal / replan / reason}.
$$

因此：

$$
\boxed{
\text{Reasoning Escalation}
=
\mathbb I[N\ge\theta_N].
}
$$

---

# 8. 三層計算路由

第一版可以把 runtime 分成三層：

## Level 0：Deterministic Fast Path

$$
\text{known state}
+
\text{known link}
\rightarrow
\text{execute}.
$$

## Level 1：Local Adaptive Routing

若：

$$
N
$$

中等，

則只在局部 frontier 上選擇：

$$
F_t
=
\Pi_{\xi_t}(\mathcal L).
$$

## Level 2：Deep Corridor Generation

若：

$$
N
$$

高，

或者：

$$
F_t=\varnothing,
$$

才呼叫昂貴 reasoning：

$$
\mathcal M_{\mathrm{deep}}.
$$

所以：

$$
\boxed{
L_0
\rightarrow
L_1
\rightarrow
L_2
}
$$

是一個 escalation ladder。

---

# 9. 自適應不是單一模型能力

Adaptive Corridor Generator 可以由：

- deterministic rules；
- heuristic；
- graph algorithm；
- DRC；
- semantic revealing；
- search-method runtime；
- local model；
- frontier model；
- large reasoning model；
- verifier；
- learned policy；

共同組成。

因此：

$$
\boxed{
\mathcal M
\neq
\text{one LLM}.
}
$$

更接近：

$$
\mathcal M
=
\mathcal M_{\mathrm{rule}}
\cup
\mathcal M_{\mathrm{search}}
\cup
\mathcal M_{\mathrm{AI}}
\cup
\mathcal M_{\mathrm{verify}}.
$$

---

# 10. 固定演算法與自適應通道

固定演算法：

$$
A(x)
\rightarrow
y.
$$

其主要流程在設計時已固定。

自適應通道系統則是：

$$
x
\rightarrow
\mathcal M(x)
\rightarrow
\Phi_x
\rightarrow
y.
$$

也就是：

$$
\boxed{
\text{solve}
=
\text{generate corridor}
+
\text{traverse corridor}.
}
$$

所以總成本必須寫成：

$$
C_{\mathrm{total}}(x)
=
C_{\mathcal M}(x)
+
C_{\Phi_x}(x)
+
C_V(x).
$$

這防止把通道生成成本忽略。

---

# 11. 局部通道猜想

第一級：

$$
\mathsf{LGC}.
$$

形式：

$$
\exists x,\exists\Phi_x:
C_{\Phi_x}(x)
<
C_0(x).
$$

意思是：

> 對至少一個問題，存在比 baseline 更便宜的 corridor。

這是最弱也最容易驗證的層級。

---

# 12. 問題族通道猜想

第二級：

$$
\mathsf{FGC}.
$$

對一個問題族：

$$
\mathcal D
$$

存在可重用結構：

$$
\Phi_{\mathcal D}.
$$

使：

$$
\mathbb E_{x\sim\mathcal D}
[
C_{\Phi_{\mathcal D}}(x)
]
<
\mathbb E_{x\sim\mathcal D}
[
C_0(x)
].
$$

這時開始有：

$$
\text{reuse}
$$

與：

$$
\text{amortization}.
$$

---

# 13. 自適應通道猜想

第三級：

$$
\mathsf{AGC}.
$$

存在：

$$
\mathcal M
$$

可以根據新問題生成 corridor：

$$
\mathcal M(x)
\mapsto
\Phi_x.
$$

並使：

$$
C_{\mathcal M}(x)
+
C_{\Phi_x}(x)
<
C_0(x)
$$

在某一問題分布上經常成立。

這是本文最重視的層級。

---

# 14. 通用通道生成猜想

第四級：

$$
\mathsf{UGC}.
$$

主張存在某種跨多個問題族仍有效的：

$$
\mathcal M_{\mathrm{general}}.
$$

但這裡必須明確限制：

- 問題域；
- 可用表示；
- 可用外部資源；
- oracle；
- approximation；
- advice；
- memory；
- learning history；
- verifier；
- time horizon。

否則「通用」會迅速失去意義。

---

# 15. 極強通用通道

第五級：

$$
\mathsf{EGC}.
$$

如果主張：

> 所有可表述問題都存在低成本可生成通道。

那就會直接碰到：

- 不可判定性；
- 不可壓縮性；
- halting；
- adversarial instance；
- non-uniformity；
- verifier bottleneck；
- representation dependency。

所以本文不把：

$$
\mathsf{EGC}
$$

作為近期工程目標。

---

# 16. 五級偏序

正式寫成：

$$
\boxed{
\mathsf{LGC}
\prec
\mathsf{FGC}
\prec
\mathsf{AGC}
\prec
\mathsf{UGC}
\prec
\mathsf{EGC}.
}
$$

其中：

$$
A\prec B
$$

表示：

> $B$ 的主張嚴格強於 $A$。

不能因為局部遊戲實驗成功，就直接宣稱：

$$
\mathsf{UGC}
$$

成立。

---

# 17. 通道生成成本

令：

$$
C_G(x)
=
C_{\mathcal M}(x).
$$

如果：

$$
C_G(x)
\gg
C_0(x),
$$

那麼即使生成出的 corridor 很短，也沒有整體加速。

因此：

$$
\boxed{
\text{Cheap corridor}
\neq
\text{cheap corridor generation}.
}
$$

真正有效要求：

$$
C_G(x)
+
C_{\mathrm{traverse}}(\Phi_x)
+
C_V(x)
<
C_0(x).
$$

---

# 18. Corridor Utility

可以定義：

$$
U(\Phi\mid s_t)
=
w_gG
-w_cC
-w_lL
-w_rR
+w_iI
+w_hH.
$$

其中：

- $G$：goal contribution；
- $C$：compute cost；
- $L$：latency；
- $R$：risk；
- $I$：information gain；
- $H$：future reuse value。

則：

$$
\Phi_t^\*
=
\arg\max_{\Phi\in\mathcal F_t}
U(\Phi\mid s_t).
$$

注意：

$$
H
$$

非常重要。

因為某條路現在稍微昂貴，

但若可結晶並被未來大量重用，

總價值可能更高。

---

# 19. 即時最優與長期最優

若只最小化：

$$
C_t,
$$

系統可能永遠走目前最便宜路。

但這可能阻止：

$$
\text{exploration}.
$$

因此需要區分：

$$
U_{\mathrm{immediate}}
$$

與：

$$
U_{\mathrm{long-term}}.
$$

形式：

$$
U_{\mathrm{total}}
=
U_{\mathrm{immediate}}
+
\gamma
U_{\mathrm{future}}.
$$

這使 corridor generator 可以偶爾選擇：

> 現在稍微貴，但能增加未來知識的路。

---

# 20. Corridor Exploration

假設目前有：

$$
\Phi_a
$$

已知可靠，

以及：

$$
\Phi_b
$$

未知但潛在更便宜。

系統需要平衡：

$$
\text{exploit}
$$

與：

$$
\text{explore}.
$$

可寫成：

$$
\Phi_t
=
\arg\max
\left(
U(\Phi)
+
\beta
\operatorname{UncertaintyBonus}(\Phi)
\right).
$$

但高風險環境：

$$
\beta
$$

應降低。

單機遊戲 sandbox 中：

$$
\beta
$$

可以提高。

---

# 21. 遊戲為什麼是理想實驗域？

遊戲提供：

$$
\boxed{
\text{complexity}
+
\text{bounded world}
+
\text{repeatability}
+
\text{rollback}
+
\text{measurement}.
}
$$

這讓 corridor generator 可以安全探索：

$$
\text{unknown routes}.
$$

失敗通常只意味：

$$
\text{reload state}.
$$

因此可以用高 exploration policy。

---

# 22. 自適應與遊戲效率

遊戲世界經常有：

- 重複狀態；
- 局部變異；
- 高頻 transition；
- 可觀察成本；
- 低風險 rollback。

這恰好適合：

$$
\text{discover}
\rightarrow
\text{reuse}
\rightarrow
\text{compile}
\rightarrow
\text{crystallize}.
$$

如果自適應成功，理想現象是：

$$
C_{\mathrm{reasoning}}(t)\downarrow
$$

而：

$$
C_{\mathrm{reuse}}(t)\uparrow.
$$

---

# 23. Reasoning Ratio

定義：

$$
R_{\mathrm{reason}}(t)
=
\frac{
N_{\mathrm{deep-reasoned\ transitions}}
}{
N_{\mathrm{all\ transitions}}
}.
$$

若系統真的學到 corridor：

$$
\frac{dR_{\mathrm{reason}}}{dt}<0
$$

應在穩定遊戲世界中出現。

這比只看任務成功率更能測到 UNPNP 的核心。

---

# 24. Corridor Hit Ratio

定義：

$$
H_{\mathrm{corridor}}(t)
=
\frac{
N_{\mathrm{verified\ corridor\ hits}}
}{
N_{\mathrm{all\ transitions}}
}.
$$

理想：

$$
\frac{dH_{\mathrm{corridor}}}{dt}>0.
$$

如果：

$$
H_{\mathrm{corridor}}
$$

一直很低，

表示：

- 世界太不穩定；
- corridor 太狹窄；
- guard 不好；
- 結晶策略失敗；
- routing 無法泛化。

---

# 25. Adaptive Core 的 Cold／Warm／Hot

可以將 corridor 分成：

$$
\boxed{
\text{Cold}
\rightarrow
\text{Warm}
\rightarrow
\text{Hot}.
}
$$

Cold：

- 未知；
- 需要完整探索；
- 可能需要深 reasoning。

Warm：

- 曾成功；
- 已有 trace；
- 仍需較多驗證。

Hot：

- 高頻；
- 高穩定；
- 已充分驗證；
- 可直接 fast-path。

所以：

$$
\boxed{
\text{Adaptive routing}
=
\text{state-dependent temperature transition}.
}
$$

---

# 26. Promotion

令：

$$
n_{\mathrm{success}}(\Phi)
$$

為成功次數，

$$
n_{\mathrm{verify}}(\Phi)
$$

為驗證次數。

則可以有：

$$
\text{Cold}\rightarrow\text{Warm}
$$

若：

$$
n_{\mathrm{success}}\ge\theta_W.
$$

以及：

$$
\text{Warm}\rightarrow\text{Hot}
$$

若：

$$
n_{\mathrm{verify}}\ge\theta_H
$$

且：

$$
S_H(\Phi)\ge\theta_S.
$$

---

# 27. Demotion

反之，如果：

$$
\operatorname{FailRate}(\Phi)
>
\theta_F,
$$

或環境版本：

$$
v_{t+1}\neq v_t,
$$

則：

$$
\text{Hot}\rightarrow\text{Warm}
$$

甚至：

$$
\text{Warm}\rightarrow\text{Cold}.
$$

因此 corridor temperature 不是永久資格。

---

# 28. Repair versus Re-solve

當通道失效時，有兩個策略：

$$
\text{Repair}(\Phi)
$$

或：

$$
\text{ReSolve}(s_t).
$$

若：

$$
C_{\mathrm{repair}}(\Phi)
<
C_{\mathrm{resolve}}(s_t),
$$

則修 corridor。

反之：

$$
\text{discard and regenerate}.
$$

因此：

$$
\boxed{
\text{Repairability}
}
$$

本身也是 corridor utility 的一部分。

---

# 29. Distribution Shift

若系統原本在：

$$
\mathcal D_1
$$

上學到 corridor，

後來世界變成：

$$
\mathcal D_2,
$$

則：

$$
\Phi_{\mathcal D_1}
$$

可能不再有效。

所以必須測：

$$
D(
\mathcal D_t,
\mathcal D_{t+1}
).
$$

若：

$$
D>\theta_D,
$$

提高：

$$
N(s_t\mid\mathcal K_t)
$$

並觸發重新展開。

---

# 30. 對抗性狀態

自適應系統特別容易受：

$$
\text{adversarial state}
$$

影響。

例如某個狀態故意長得像：

$$
s_{\mathrm{known}}
$$

但真正語義不同。

所以不能只有：

$$
\text{similarity}.
$$

還需要：

$$
\text{guard}
+
\text{invariant}
+
\text{validator}.
$$

因此：

$$
\boxed{
\text{Similarity-based routing alone is insufficient}.
}
$$

---

# 31. Fail-Closed

若：

$$
G(\Phi,s_t)
$$

無法判定，

則不應默認：

$$
\text{allow}.
$$

而應：

$$
\boxed{
\text{unknown}
\rightarrow
\text{reveal / verify}.
}
$$

這是第一版安全模型最重要的簡化之一。

---

# 32. AI 不應自動取得更高權限

即使：

$$
\mathcal M
$$

學到：

> 某條高權限路徑比較快。

也不能推出：

$$
\text{permission expansion}.
$$

所以：

$$
\boxed{
\text{Learning}
\not\Rightarrow
\text{Self-Authorization}.
}
$$

Adaptive Corridor Generator 可以學：

$$
\text{which path is useful},
$$

不能自行決定：

$$
\text{which forbidden capability becomes allowed}.
$$

---

# 33. 內部實驗域

第一代應限制：

$$
\mathcal W_{\mathrm{experiment}}
\subset
\mathcal W_{\mathrm{safe}}.
$$

可以包括：

- synthetic world；
- local game state；
- local database；
- read-only corpus；
- sandbox execution；
- mock services。

避免：

- real payment；
- production mutation；
- external irreversible action；
- privileged account management。

---

# 34. Adaptive Generator 與 Omphalos

Omphalos / AUSI 的方法思想可以被一般化。

原本：

$$
\text{Task}
\rightarrow
\text{Search Method}
\rightarrow
\text{Provider}.
$$

UNPNP 中：

$$
\text{State}
\rightarrow
\text{Corridor Method}
\rightarrow
\text{Transition}.
$$

因此 Search Method Runtime 可以成為：

$$
\mathcal M
$$

的一個子系統，而不是整台 UNPNP Computer。

---

# 35. Adaptive Generator 與 DRC

DRC：

$$
D
\rightarrow
R
\rightarrow
C.
$$

可以映射為：

$$
\text{candidate expansion}
\rightarrow
\text{corridor resonance}
\rightarrow
\text{route compression}.
$$

所以：

$$
\boxed{
\text{DRC}
\subset
\text{possible corridor-generation operator family}.
}
$$

它不必是唯一方法。

---

# 36. Adaptive Generator 與語義顯影

語義顯影：

$$
\Pi_{\xi_t}
$$

負責把巨大：

$$
\mathcal L
$$

壓成：

$$
F_t.
$$

Adaptive Generator 則在：

$$
F_t
$$

上生成：

$$
\Phi_t.
$$

因此：

$$
\boxed{
\text{Revealing}
\neq
\text{Routing}.
}
$$

顯影回答：

> 現在哪些路值得看？

Generator 回答：

> 現在實際走哪一條？

---

# 37. Adaptive Generator 與路徑編譯

第一次：

$$
\mathcal M
\rightarrow
\Gamma_t.
$$

若：

$$
\Gamma_t
$$

反覆成功，

則後續：

$$
\Gamma_t
\xrightarrow{K}
\widehat{\ell}.
$$

因此：

$$
\boxed{
\mathcal M
\text{ discovers paths;}
\quad
K
\text{ creates new primitives.}
}
$$

兩者不同。

---

# 38. Generator 本身也可以學習

令：

$$
\theta_t
$$

是 generator policy。

可以有：

$$
\theta_{t+1}
=
U(
\theta_t,
\text{receipts},
\text{success},
\text{cost},
\text{failure}
).
$$

但第一代不一定需要更新 neural weights。

也可以只更新：

$$
\mathcal K_t,
\mathcal S_t,
\mathcal R_t.
$$

即：

- corridor library；
- statistics；
- routing preferences。

所以：

$$
\boxed{
\text{Adaptive learning}
\neq
\text{weight training}.
}
$$

---

# 39. Model-Frozen Experiment

為了驗證架構本身，可以故意：

$$
\theta_{\mathrm{model}}(t+1)
=
\theta_{\mathrm{model}}(t).
$$

而只允許：

$$
\mathcal K_{t+1}
\supseteq
\mathcal K_t.
$$

如果性能仍提升：

$$
P(t+1)>P(t),
$$

則證明改善主要來自：

$$
\text{computational architecture learning},
$$

而非模型重新訓練。

這會是重要實驗。

---

# 40. Uniformity Warning

即使：

$$
\forall x
\exists\Phi_x
$$

都存在好 corridor，

也不能推出：

$$
\exists\mathcal M
\forall x:
\mathcal M(x)=\Phi_x.
$$

因此：

$$
\boxed{
\forall x\exists\Phi_x
\centernot\Rightarrow
\exists\mathcal M\forall x.
}
$$

這是本文最重要的理論限制之一。

---

# 41. Discoverability Warning

甚至：

$$
\exists\Phi_x
$$

也不意味：

$$
C_{\mathcal M}(x)
$$

低。

可能存在一條極好路，

但找到它本身：

$$
\text{exponential}.
$$

所以：

$$
\boxed{
\text{Corridor existence}
\neq
\text{efficient corridor discovery}.
}
$$

---

# 42. Verification Bottleneck

若：

$$
C_V(\Phi)
\gg
C_{\mathrm{traverse}}(\Phi),
$$

則 corridor 雖快，

整體仍可能不快。

因此：

$$
C_{\mathrm{effective}}
=
C_G
+
C_T
+
C_V.
$$

三者必須一起看。

---

# 43. Corridor Generator 的完整成本

第一版：

$$
\boxed{
C_{\mathcal M}
=
C_{\mathrm{reveal}}
+
C_{\mathrm{search}}
+
C_{\mathrm{reason}}
+
C_{\mathrm{rank}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{route}}.
}
$$

因此：

> 「AI 選到好路」不能只看最後 traversal。

必須把選路成本一起算。

---

# 44. Adaptive Corridor Regret

可以定義：

$$
\operatorname{Regret}(T)
=
\sum_{t=1}^{T}
\left[
C(\Phi_t)
-
C(\Phi_t^\*)
\right].
$$

其中：

$$
\Phi_t^\*
$$

是事後知道的最佳 corridor。

如果：

$$
\frac{\operatorname{Regret}(T)}{T}
\rightarrow
0,
$$

表示 adaptive routing 長期逼近最佳已知策略。

這可以成為未來 benchmark。

---

# 45. 不追求「永遠最佳」

在動態世界中要求：

$$
\Phi_t=\Phi_t^\*
$$

每次都成立，

通常不現實。

更實用的是：

$$
\boxed{
\text{bounded regret}
+
\text{bounded risk}
+
\text{improving reuse}.
}
$$

這比宣稱全域最優更可實驗。

---

# 46. Corridor Generator 的最小架構

第一版可以是：

```text
State Observer
    ↓
Novelty Detector
    ↓
Known-Route Matcher
    ↓
Semantic Revealing
    ↓
Candidate Corridor Generator
    ↓
Utility / Risk Ranker
    ↓
Verifier
    ↓
Router
    ↓
Execution
    ↓
Receipt
```

其中只有：

$$
\text{Candidate Corridor Generator}
$$

在高 novelty 時才必須使用大型模型。

---

# 47. Minimal Adaptive Loop

形式：

$$
s_t
\rightarrow
N_t
\rightarrow
F_t
\rightarrow
\Phi_t
\rightarrow
V_t
\rightarrow
s_{t+1}.
$$

再記錄：

$$
r_t
=
\operatorname{Receipt}
(s_t,\Phi_t,s_{t+1}).
$$

並更新：

$$
\mathcal K_{t+1}
=
U(\mathcal K_t,r_t).
$$

---

# 48. 從固定程式到動態通道世界

固定程式：

$$
P
=
(V,E).
$$

其中：

$$
E
$$

大致固定。

自適應 UNPNP：

$$
P_t
=
(V_t,E_t),
$$

且：

$$
E_{t+1}
=
E_t
+
\Delta E_t^+
-
\Delta E_t^-.
$$

其中：

- $\Delta E_t^+$：新增通道；
- $\Delta E_t^-$：淘汰通道。

這就是：

$$
\boxed{
\text{program as evolving transition topology}.
}
$$

---

# 49. 核心命題一

$$
\boxed{
\textbf{
真正可行的通用性更可能存在於「生成、辨識、驗證與淘汰快速通道的能力」，
而不是存在於一條固定且永久有效的捷徑。
}
}
$$

---

# 50. 核心命題二

$$
\boxed{
\textbf{
AI 原生計算不應預設每一步都需要 AI 深度推理；
穩定已知路徑應直接執行，只有新穎性與不確定性超過門檻時才提升 reasoning。
}
}
$$

---

# 51. 核心命題三

$$
\boxed{
\textbf{
Adaptive Corridor Generator 的價值不只在「找出目前最便宜的路」，
還在於建立能被未來重用、編譯與結晶的新路。
}
}
$$

---

# 52. 結論

UNPNP Computer 若只有超連結，仍然只是一張可導航的計算圖。

真正讓它成為動態計算系統的，是：

$$
\boxed{
\text{Adaptive Corridor Generator}.
}
$$

它負責在：

$$
\mathcal L_t
$$

之中持續判斷：

- 哪些 route 已知；
- 哪些 route 可直接重用；
- 哪些狀態已超出既有 guard；
- 哪些問題需要重新顯影；
- 哪些候選值得探索；
- 哪些 corridor 值得結晶；
- 哪些 corridor 已經失效。

因此：

$$
\boxed{
\text{UNPNP Runtime}
=
\text{Hyperlink World}
+
\text{Adaptive Corridor Generator}.
}
$$

但這還不是完整系統。

因為 generator 選出 corridor 之後，仍然需要一個更底層的動態循環：

$$
\boxed{
\text{展開}
\rightarrow
\text{連結}
\rightarrow
\text{收斂}.
}
$$

這個循環將解釋：

> 新路徑究竟如何從未知空間中被展開、連接並重新壓縮為下一個狀態？

這正是下一篇的主題。

---

## 後續篇章

**Series 04｜展開—連結—收斂：UNPNP 計算的三元循環**

下一篇將正式處理：

$$
E
\rightarrow
L
\rightarrow
C
\rightarrow
E',
$$

並建立：

- Expansion；
- Linking；
- Convergence；
- DRC 與 frontier；
- 語義顯影；
- local working set；
- 收斂後 seed；
- 呼吸式計算；
- 為何收斂不是終點；
- 為何每次呼吸都可能留下可結晶結構。
