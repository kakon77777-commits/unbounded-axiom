# UNPNP Series 08  
## 有效度超連結路徑編碼：不是所有程式都值得被改寫  
### Effective Hyperlink Path Encoding: Not Every Program Path Should Be Rewritten

**系列名稱：** UNPNP Hyperlink & Crystallized Computation Series  
**系列篇次：** 08  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** AI 原生計算／選擇性再編譯／UNPNP 理論論文  
**狀態：** Canonical Draft  

---

## 摘要

UNPNP Series 06 提出 Path Compilation，使多階 traversal 可以被重新編譯為新的直接超連結；Series 07 進一步提出 Computational Crystallization，使已驗證且具有生命週期價值的新路徑被提升為可重用計算原語。然而，這兩個能力若被無限制套用，會導致另一種極端：系統為了「超連結化」而將所有程式、所有路徑、所有狀態轉移都重新分析、重新編譯、重新驗證並持久化，最終讓 optimizer 自身變成新的複雜度來源。

本文提出 **Effective Hyperlink Path Encoding，EHPE**，中文稱為**有效度超連結路徑編碼**。其核心命題是：

$$
\boxed{
\text{能被編譯成超連結}
\neq
\text{值得被編譯成超連結}.
}
$$

一條路徑是否值得被重新編譯與結晶，不應由「能不能做」決定，而應由完整生命週期效用決定。本文提出：

$$
\boxed{
U_H(\Gamma)
=
B_{\mathrm{runtime}}
+
B_{\mathrm{future}}
-
C_{\mathrm{compile}}
-
C_{\mathrm{verify}}
-
C_{\mathrm{maintain}}
-
C_{\mathrm{select}}
-
C_{\mathrm{risk}}.
}
$$

其中：

- $B_{\mathrm{runtime}}$：目前執行節省；
- $B_{\mathrm{future}}$：未來可重用與高階結晶價值；
- $C_{\mathrm{compile}}$：編譯成本；
- $C_{\mathrm{verify}}$：等價與安全驗證成本；
- $C_{\mathrm{maintain}}$：版本與依賴維護成本；
- $C_{\mathrm{select}}$：未來尋找與選擇該 crystal 的成本；
- $C_{\mathrm{risk}}$：錯誤、失效與安全風險成本。

只有當：

$$
U_H(\Gamma)>0
$$

且達到最低信任、穩定與可回退門檻時，該路徑才值得進入 path compilation 或 crystallization。

本文進一步提出 frequency、cost saving、stability、verification burden、maintenance burden、domain width、volatility、risk、selection overhead 與 future composability 九類核心因素，並建立 break-even：

$$
N^\*
=
\left\lceil
\frac{
C_{\mathrm{fixed}}
}{
\Delta C_{\mathrm{run}}
-
C_{\mathrm{variable}}
}
\right\rceil.
$$

如果預期重用次數：

$$
N_{\mathrm{expected}}
<
N^\*,
$$

即使單次 fast path 很快，也不應持久化成正式 crystal。

本文亦提出 **Selective Recompilation Principle**：

$$
\boxed{
\text{Legacy Program}
=
\text{Canonical Program}
+
\text{Selective Crystal Overlay}.
}
$$

第一代 AI 再編譯系統不需要把整個傳統程式轉換成「全超連結程式碼」，而只需要對高頻、高成本、高穩定、可驗證且正向收益明確的區域建立有效 fast path。其餘一次性、低頻、高變動、難驗證、低收益或高風險路徑應保留原始形式。

本文進一步提出 Effective Hyperlink Density：

$$
\rho_H
=
\frac{
|\mathcal K_{\mathrm{useful}}|
}{
|\mathcal P_{\mathrm{candidate}}|
},
$$

並指出合理系統不應追求：

$$
\rho_H\rightarrow1,
$$

而應追求：

$$
\boxed{
\max
\sum_{\kappa\in\mathcal K}
U_L(\kappa)
}
$$

亦即最大化整體有價值結晶，而不是最大化超連結數量。

最後，本文建立 Negative Optimization、Crystal Debt、Maintenance Explosion、Selection Congestion、Over-Specialization、Under-Generalization 與 Hyperlink Saturation 等失敗模式，並為 Series 09 的安全可達世界提供接口：即使某條路在純性能上極具價值，只要它穿越過高風險、權限不穩定或不可逆作用域，就可能被判定為不值得進入 fast path。

因此，本文的核心可以壓縮成：

$$
\boxed{
\textbf{
UNPNP 的目標不是把世界全部變成超連結，
而是只把真正值得的計算路徑結晶成新的超連結。
}
}
$$

**關鍵詞：** UNPNP、Effective Hyperlink Path Encoding、EHPE、Selective Recompilation、Utility、Break-Even、Crystallization、Negative Optimization、Crystal Debt、AI Compiler

---

# 1. 從「能不能」到「值不值得」

Series 06 問：

> 能不能把多階 path 編譯成一條新 link？

Series 07 問：

> 哪些 compiled path 可以成熟成 crystal？

本文進一步問：

> 即使能，而且能驗證，真的值得做嗎？

因此：

$$
\boxed{
\text{Feasibility}
\neq
\text{Utility}.
}
$$

---

# 2. 最危險的錯誤：全程式 Hyperlink 化

假設一個程式有：

$$
M
$$

條候選路徑。

如果對每一條都：

$$
\text{observe}
\rightarrow
\text{compile}
\rightarrow
\text{verify}
\rightarrow
\text{store}
\rightarrow
\text{maintain},
$$

則 optimizer 成本：

$$
C_{\mathrm{opt}}
$$

可能迅速膨脹。

甚至：

$$
C_{\mathrm{opt}}
>
C_{\mathrm{saved}}.
$$

這就是：

$$
\boxed{
\text{optimization-induced complexity}.
}
$$

---

# 3. Effective Hyperlink Path Encoding

本文將一條 path：

$$
\Gamma
$$

是否值得超連結化的判定稱為：

$$
\boxed{
\operatorname{EHPE}(\Gamma).
}
$$

其結果可以是：

$$
\operatorname{EHPE}(\Gamma)
\in
\{
\text{retain},
\text{observe},
\text{compile},
\text{crystallize},
\text{retire}
\}.
$$

---

# 4. Utility First

核心不是：

$$
\operatorname{CanCompile}(\Gamma).
$$

而是：

$$
\boxed{
U_H(\Gamma).
}
$$

如果：

$$
U_H(\Gamma)\le0,
$$

即使技術上可以編譯，

也不應 promotion。

---

# 5. 第一版 Utility

本文提出：

$$
\boxed{
U_H(\Gamma)
=
B_R
+
B_F
-
C_C
-
C_V
-
C_M
-
C_S
-
C_R.
}
$$

其中：

- $B_R$：runtime benefit；
- $B_F$：future benefit；
- $C_C$：compile cost；
- $C_V$：verification cost；
- $C_M$：maintenance cost；
- $C_S$：selection / storage cost；
- $C_R$：risk cost。

---

# 6. Runtime Benefit

令原始成本：

$$
C_0(\Gamma).
$$

compiled path：

$$
C_1(\Gamma).
$$

單次節省：

$$
\Delta C_{\mathrm{run}}
=
C_0-C_1.
$$

若：

$$
\Delta C_{\mathrm{run}}\le0,
$$

立即沒有 runtime 理由。

---

# 7. Future Benefit

某條 path 目前使用頻率不高，

但可能是：

- 上層 crystal 的 constituent；
- 多個任務共享 primitive；
- future family-generalization seed；
- expensive reasoning replacement。

因此加入：

$$
B_F.
$$

---

# 8. Future Benefit 不能亂估

如果把所有未來可能性都算成巨大收益，

則所有 path 都會看起來值得結晶。

因此：

$$
B_F
$$

應被 discount：

$$
B_F^{\mathrm{disc}}
=
p_{\mathrm{reuse}}
\gamma
B_F.
$$

其中：

$$
0\le p_{\mathrm{reuse}}\le1.
$$

---

# 9. Frequency

令：

$$
f(\Gamma)
$$

為觀察窗口內頻率。

高頻：

$$
f\uparrow
$$

通常增加：

$$
U_H.
$$

因為固定成本更容易攤銷。

---

# 10. Frequency 不是唯一條件

一條 path 即使高頻，

若：

$$
C_0
$$

本來極低，

則：

$$
f
\Delta C
$$

仍可能很小。

因此：

$$
\boxed{
\text{high frequency}
\neq
\text{high optimization value}.
}
$$

---

# 11. Cost Intensity

定義：

$$
I_C(\Gamma)
=
f(\Gamma)
C_0(\Gamma).
$$

這比只看：

$$
f
$$

更合理。

高：

$$
I_C
$$

表示該 path 消耗大量總資源。

---

# 12. Stability

令：

$$
S(\Gamma)
$$

表示 path 結構穩定度。

高：

$$
S
$$

表示：

- branch pattern 穩定；
- contract 穩定；
- dependency 穩定；
- domain 穩定；
- failure rate 低。

---

# 13. Volatility

與 stability 對偶：

$$
V_o(\Gamma)
$$

表示 volatility。

若：

$$
V_o\uparrow,
$$

則：

$$
C_M\uparrow.
$$

---

# 14. Stable but Rare

一條非常穩定但幾乎不執行的 path，

也不一定值得結晶。

所以：

$$
S\uparrow
$$

只是必要加分，

不是充分條件。

---

# 15. High-Cost but Unstable

一條非常昂貴但高度不穩定的 path，

可能：

$$
C_M
+
C_V
$$

太高。

因此也可能不值得。

---

# 16. Verification Burden

定義：

$$
B_V(\Gamma)
=
C_{\mathrm{verify}}(\Gamma).
$$

若 equivalence 很難驗，

則即使：

$$
\Delta C_{\mathrm{run}}
$$

高，

也可能無法 promotion。

---

# 17. Verification Amortization

若 verifier 可以重用：

$$
V_{\mathrm{fast}},
$$

則後續：

$$
C_V^{\mathrm{run}}
$$

下降。

所以要區分：

$$
C_V^{\mathrm{build}}
$$

與：

$$
C_V^{\mathrm{runtime}}.
$$

---

# 18. Maintenance Burden

定義：

$$
B_M(\Gamma)
=
C_{\mathrm{maintain}}
(
\Gamma,
\Delta\mathcal W
).
$$

包含：

- version updates；
- schema drift；
- dependency change；
- hardware change；
- rule change；
- revalidation。

---

# 19. Domain Width

令：

$$
D_\Gamma
$$

為 compiled path 有效域。

其寬度可以抽象表示：

$$
W_D(\Gamma).
$$

通常較寬的有效域：

$$
W_D\uparrow
$$

增加 reuse value。

---

# 20. 但太寬可能降低安全性

如果為追求 generalization，

把 guard 放太寬，

則：

$$
\operatorname{FalsePositiveGuard}
\uparrow.
$$

所以：

$$
\boxed{
\text{wide domain}
\neq
\text{good domain}.
}
$$

---

# 21. Guard Precision

定義：

$$
P_G
=
\frac{
TP
}{
TP+FP
}.
$$

若：

$$
P_G
$$

低，

fast path 可能被錯用。

---

# 22. Guard Recall

同時：

$$
R_G
=
\frac{
TP
}{
TP+FN
}.
$$

若太低，

大量本來可走 fast path 的狀態仍走 slow path。

---

# 23. Guard Utility

因此可定義：

$$
U_G
=
\alpha P_G
+
\beta R_G
-
\gamma C_G.
$$

不只是：

> guard 越嚴越好。

---

# 24. Risk

令：

$$
R(\Gamma)
$$

表示：

- side effect；
- irreversibility；
- privilege；
- data sensitivity；
- attack surface；
- failure impact。

即使性能收益巨大：

$$
\Delta C\gg0,
$$

高：

$$
R
$$

仍可能讓：

$$
U_H<0.
$$

---

# 25. Risk-Adjusted Utility

正式：

$$
\boxed{
U_H^R
=
U_H
-
\lambda_R R.
}
$$

高風險 domain：

$$
\lambda_R
$$

應更大。

---

# 26. Selection Cost

若 crystal library：

$$
|\mathcal K|
$$

很大，

每次找：

$$
\kappa^\*
$$

也有成本。

令：

$$
C_{\mathrm{select}}.
$$

因此：

$$
\boxed{
\text{more shortcuts}
\neq
\text{faster routing}.
}
$$

---

# 27. Storage Cost

每個 crystal 可能保存：

- executable；
- guard；
- validator；
- provenance；
- benchmark；
- dependency fingerprint；
- receipts。

所以：

$$
C_{\mathrm{store}}>0.
$$

---

# 28. Memory Is Not Free

即使外部 storage 很便宜，

索引、載入、驗證、版本同步仍然有成本。

因此：

$$
\boxed{
\text{cheap storage}
\neq
\text{zero memory complexity}.
}
$$

---

# 29. Break-Even

固定成本：

$$
C_F
=
C_{\mathrm{compile}}
+
C_{\mathrm{verify-build}}
+
C_{\mathrm{deploy}}.
$$

每次節省：

$$
\Delta C_{\mathrm{net}}
=
\Delta C_{\mathrm{run}}
-
C_{\mathrm{guard}}
-
C_{\mathrm{verify-run}}
-
C_{\mathrm{select}}.
$$

則：

$$
\boxed{
N^\*
=
\left\lceil
\frac{
C_F
}{
\Delta C_{\mathrm{net}}
}
\right\rceil.
}
$$

---

# 30. 無法 Break-Even

若：

$$
\Delta C_{\mathrm{net}}\le0,
$$

則：

$$
N^\*=\infty.
$$

這類 path 不應結晶。

---

# 31. Expected Reuse

令：

$$
N_E
=
\mathbb E[N_{\mathrm{future}}].
$$

若：

$$
N_E<N^\*,
$$

則不持久化。

---

# 32. Confidence-Aware Reuse

預期 reuse 不是確定值。

可以有：

$$
N_E
\pm
\sigma_N.
$$

保守判定：

$$
N_E-k\sigma_N>N^\*.
$$

才 promotion。

---

# 33. Lifecycle Utility

完整：

$$
\boxed{
U_L(\kappa,N)
=
N\Delta C_{\mathrm{net}}
-
C_F
-
C_M(N)
-
C_R(N).
}
$$

---

# 34. Lifecycle 不應只看一次 benchmark

一次：

$$
C_{\mathrm{new}}<C_{\mathrm{old}}
$$

不足。

真正：

$$
\boxed{
\sum_{t=1}^{T}
C_{\mathrm{new}}(t)
<
\sum_{t=1}^{T}
C_{\mathrm{old}}(t).
}
$$

才有生命週期價值。

---

# 35. Negative Optimization

如果：

$$
U_L<0,
$$

則：

$$
\boxed{
\text{Negative Optimization}.
}
$$

也就是：

> 優化後整體更貴。

---

# 36. Negative Optimization 的來源

包括：

- compilation too expensive；
- verification too expensive；
- guard too expensive；
- low reuse；
- frequent invalidation；
- high maintenance；
- slow selection；
- memory overhead。

---

# 37. Crystal Debt

結晶建立後，

可能前期：

$$
U_L>0,
$$

後期因環境改變：

$$
C_M\uparrow.
$$

定義：

$$
\boxed{
D_K
=
C_M
+
C_{\mathrm{repair}}
-
B_{\mathrm{remaining}}.
}
$$

若：

$$
D_K>0,
$$

形成 crystal debt。

---

# 38. Debt Trigger

如果：

$$
D_K>\theta_D,
$$

則：

$$
\kappa
\rightarrow
\text{retire / rebuild}.
$$

---

# 39. Maintenance Explosion

若：

$$
|\mathcal K|
$$

大量增加，

可能：

$$
C_M(\mathcal K)
$$

超線性增長。

例如 dependency 交叉。

所以需要：

$$
\boxed{
\text{crystal governance}.
}
$$

---

# 40. Selection Congestion

如果很多 crystal guard：

$$
G_1,\ldots,G_m
$$

高度重疊，

routing 可能必須評估大量候選。

這就是：

$$
\boxed{
\text{selection congestion}.
}
$$

---

# 41. Effective Hyperlink Density

令候選 path 數：

$$
|\mathcal P_C|.
$$

真正保留 crystal：

$$
|\mathcal K_U|.
$$

定義：

$$
\boxed{
\rho_H
=
\frac{
|\mathcal K_U|
}{
|\mathcal P_C|
}.
}
$$

---

# 42. 不追求 $\rho_H=1$

如果：

$$
\rho_H\rightarrow1,
$$

表示幾乎所有 path 都被 crystallize。

這通常不是成熟，

而可能是：

$$
\boxed{
\text{over-crystallization}.
}
$$

---

# 43. 最佳密度不是固定常數

理想：

$$
\rho_H^\*
$$

依：

- workload；
- hardware；
- domain；
- volatility；
- memory；
- risk；

改變。

---

# 44. Crystal Saturation

當新增 crystal 的 marginal benefit：

$$
\Delta U_K
$$

趨近：

$$
0
$$

甚至負數，

就出現：

$$
\boxed{
\text{crystal saturation}.
}
$$

---

# 45. Marginal Utility

第：

$$
m
$$

個 crystal 的邊際價值：

$$
MU_m
=
U(\mathcal K_m)
-
U(\mathcal K_{m-1}).
$$

當：

$$
MU_m\le0,
$$

應停止擴張。

---

# 46. Selective Recompilation Principle

本文正式提出：

$$
\boxed{
\textbf{
Only paths with positive risk-adjusted lifecycle utility should be promoted into persistent compiled hyperlinks.
}
}
$$

中文：

$$
\boxed{
\textbf{
只有具有正向風險調整後生命週期效用的路徑，
才應被提升為持久化超連結。
}
}
$$

---

# 47. Legacy Program 不需要被整體替換

第一代：

$$
P_{\mathrm{legacy}}
$$

可以保持 canonical。

只疊加：

$$
\mathcal K_t.
$$

所以：

$$
\boxed{
P_t
=
P_{\mathrm{legacy}}
\oplus
\mathcal K_t.
}
$$

---

# 48. Crystal Overlay

Overlay 只處理：

$$
\Gamma_i
$$

使：

$$
U_H(\Gamma_i)>0.
$$

其餘：

$$
\Gamma_j
$$

仍走 legacy path。

---

# 49. 為什麼這更適合傳統程式？

因為 legacy program 可能有：

- 複雜 side effect；
- 不完整 tests；
- undocumented behavior；
- plugin；
- mod；
- external dependency。

整體翻譯風險太高。

---

# 50. Shadow Recompilation

候選：

$$
\widehat{\Gamma}
$$

先不 active。

而是：

$$
\Gamma
\parallel
\widehat{\Gamma}_{\mathrm{shadow}}.
$$

觀察：

- equivalence；
- speed；
- resources；
- drift。

---

# 51. Promotion after Evidence

只有：

$$
V_{\mathrm{equiv}}\ge\theta_V,
$$

$$
U_H^R>0,
$$

才 promotion。

---

# 52. One-Shot Path

若：

$$
f\approx0
$$

且：

$$
N_E\approx1,
$$

則通常：

$$
U_H<0.
$$

不要結晶。

---

# 53. Expensive One-Shot Exception

但若單次原成本：

$$
C_0
$$

極大，

且 compile cost：

$$
C_F
$$

更低，

即使：

$$
N=1
$$

也可能值得。

所以 frequency 不是硬規則。

---

# 54. Low-Cost Repetitive Path

若 path 每秒執行很多次，

但單次只有：

$$
\epsilon
$$

成本，

總：

$$
f\epsilon
$$

仍可能值得或不值得，

需要實測。

---

# 55. Hot Loop

非常高頻 loop：

$$
f\gg1
$$

通常是 optimizer 重點。

這接近傳統 JIT / trace compiler。

---

# 56. Semantic Hot Path

UNPNP 更關心一種高階 hot path：

> 不一定是 CPU instruction 高頻，而是語義上反覆需要同一組跨底空間操作。

例如：

- NPC 決策；
- memory retrieval；
- repeated tool chain；
- game economy update；
- recurring query planning。

---

# 57. Semantic Frequency

令：

$$
f_S(\Gamma)
$$

表示語義等價 path 的頻率。

即使 byte trace 不同，

若：

$$
\Gamma_i
\simeq_{\mathcal T}
\Gamma_j,
$$

可被視為同一 path family。

---

# 58. Family-Level Compilation

若：

$$
\{\Gamma_1,\ldots,\Gamma_n\}
$$

共享 task contract，

可以編譯：

$$
\kappa_{\mathcal D}.
$$

這比 instance-level 更有價值。

---

# 59. Over-Specialization

如果每個 input 都產生：

$$
\kappa_x,
$$

則：

$$
|\mathcal K|
$$

可能接近：

$$
|\mathcal X|.
$$

這就是：

$$
\boxed{
\text{over-specialization}.
}
$$

---

# 60. Under-Generalization

若很多 crystal 可被 family abstraction 合併，

但系統沒有合併，

selection / maintenance cost 會上升。

---

# 61. Over-Generalization

反之，

把過多不同 path 合成同一 crystal，

guard domain 太寬，

會提高錯誤率。

---

# 62. Generalization Utility

可以定義：

$$
U_G
=
B_{\mathrm{merge}}
-
C_{\mathrm{guard-complexity}}
-
C_{\mathrm{error}}.
$$

只有：

$$
U_G>0
$$

才 generalize。

---

# 63. Path Portfolio

結晶庫應視為：

$$
\boxed{
\text{portfolio}
}
$$

而不是 artifact dump。

每個：

$$
\kappa
$$

有：

- 收益；
- 風險；
- 成本；
- 相關性；
- 重疊。

---

# 64. Portfolio Utility

$$
U(\mathcal K)
\neq
\sum U(\kappa_i)
$$

總是成立。

因為 crystal 可能：

- overlap；
- interfere；
- share verifier；
- share index；
- compete for selection。

---

# 65. Interaction Cost

加入：

$$
C_{\mathrm{interaction}}
(
\kappa_i,\kappa_j
).
$$

完整：

$$
U(\mathcal K)
=
\sum_i U(\kappa_i)
-
\sum_{i\neq j}
C_{\mathrm{interaction}}.
$$

---

# 66. Crystal Dependency Graph

結晶之間可有：

$$
G_K=(V,E).
$$

dependency graph 可以用於：

- invalidation；
- maintenance；
- merge；
- selection。

---

# 67. Dependency Centrality

某些 crystal：

$$
\kappa_c
$$

被很多 higher-order crystal 使用。

則其失效影響大。

需要更高驗證門檻。

---

# 68. Critical Crystal

定義：

$$
I_{\mathrm{impact}}(\kappa)
$$

若高，

則：

$$
\theta_V(\kappa)
$$

應提高。

---

# 69. Low-Impact Crystal

低 impact、可回滾 path：

$$
\theta_V
$$

可以低一些，

以加快實驗。

---

# 70. 風險與驗證應動態耦合

即：

$$
\boxed{
R\uparrow
\Rightarrow
V_{\mathrm{required}}\uparrow.
}
$$

---

# 71. Effective Hyperlink Score

第一版可定義：

$$
\boxed{
S_H(\Gamma)
=
w_fF
+
w_cC
+
w_sS
+
w_dD
+
w_pP
-
w_vV
-
w_mM
-
w_rR
-
w_qQ.
}
$$

其中：

- $F$：frequency；
- $C$：cost-saving potential；
- $S$：stability；
- $D$：domain width；
- $P$：future composability；
- $V$：verification burden；
- $M$：maintenance；
- $R$：risk；
- $Q$：selection congestion contribution。

---

# 72. Score 不應取代成本帳本

$$
S_H
$$

適合 ranking。

真正 promotion 還是要求：

$$
U_L>0.
$$

---

# 73. Multi-Objective Decision

有些 path：

- latency 很好；
- energy 很差。

另一些反之。

因此：

$$
\mathbf U
=
(
U_{\mathrm{latency}},
U_{\mathrm{energy}},
U_{\mathrm{memory}},
U_{\mathrm{quality}},
U_{\mathrm{risk}}
).
$$

---

# 74. Pareto Frontier

不一定存在單一最佳 crystal。

可以保留：

$$
\boxed{
\text{Pareto-optimal crystal set}.
}
$$

Adaptive Corridor Generator 再依當時 budget 選。

---

# 75. Hardware Profile

同一路徑：

$$
\Gamma
$$

在 CPU：

$$
U_H^{CPU}
$$

與 GPU：

$$
U_H^{GPU}
$$

可能不同。

所以 EHPE 應 hardware-aware。

---

# 76. Energy Profile

未來若關心能耗：

$$
C_E
$$

也進 utility。

有些 path latency 下降，

但 energy 上升。

---

# 77. Memory Profile

某些 crystal 用更多 memory 換 compute。

則：

$$
C_{\mathrm{storage}}
\uparrow,
$$

$$
C_{\mathrm{compute}}
\downarrow.
$$

回到 Series 01 的 complexity redistribution。

---

# 78. Budget-Dependent Utility

$$
U_H(\Gamma\mid B_t)
$$

會依 budget 改變。

所以同一 crystal 不是永遠最好。

---

# 79. Cold / Warm / Hot 也應由有效度驅動

Hot 不只是：

> 用很多次。

而應：

$$
U_L(\kappa)\gg0
$$

且：

$$
T_K(\kappa)
$$

高。

---

# 80. Hot but Bad

若一個 path 高頻但：

$$
U_L<0,
$$

則「常用」本身不能救它。

應退回 legacy path。

---

# 81. Slow but Valuable

某些 crystal 沒有降低 latency，

但大幅降低：

- reasoning；
- failure；
- variance；
- verification。

仍可能：

$$
U_H>0.
$$

所以「快」不是唯一效益。

---

# 82. Reliability Benefit

可以加入：

$$
B_{\mathrm{reliability}}
=
C_{\mathrm{failure-old}}
-
C_{\mathrm{failure-new}}.
$$

---

# 83. Variance Reduction

即使平均成本相似，

若：

$$
\operatorname{Var}(C_{\mathrm{new}})
\ll
\operatorname{Var}(C_{\mathrm{old}}),
$$

也可能值得。

遊戲 real-time 尤其重要。

---

# 84. Tail Latency

可考慮：

$$
p95,
p99.
$$

不只：

$$
\mathbb E[C].
$$

---

# 85. 遊戲中的 EHPE

對單機遊戲，

候選：

- inventory query；
- pathfinding；
- NPC decision；
- quest lookup；
- combat micro-loop。

可以逐一計算：

$$
U_H.
$$

---

# 86. 第一階段不碰所有系統

只對：

$$
R_0,R_1,R_2
$$

低風險本地路徑做 EHPE：

- read；
- local reversible；
- sandbox。

---

# 87. 遊戲中的高價值候選

例如：

$$
\Gamma_{\mathrm{pathfinding}}
$$

高頻、高成本、穩定。

如果可建立：

$$
\kappa_{\mathrm{regional-route}}
$$

可能有大收益。

---

# 88. 遊戲中的低價值候選

例如：

> 只在一次劇情事件觸發的唯一動畫 transition。

即使可 compile，

也不一定值得。

---

# 89. Adaptive Threshold

$$
\theta_H
$$

不必固定。

系統可依：

- CPU load；
- memory；
- session duration；
- game phase；

調整。

---

# 90. Early Session

遊戲剛開始：

$$
N_E
$$

未知。

可以多 observe，

少 persistent crystallize。

---

# 91. Mature Session

重複模式穩定後：

$$
p_{\mathrm{reuse}}\uparrow.
$$

promotion threshold 可以更積極。

---

# 92. Late-Game Shift

遊戲進入後期，

distribution 改變。

早期 crystal：

$$
\kappa_{\mathrm{early}}
$$

可能 stale。

因此 EHPE 必須持續重算 utility。

---

# 93. Utility Drift

$$
U_H(\kappa,t+1)
\neq
U_H(\kappa,t).
$$

因此：

$$
\boxed{
\text{crystal value is time-dependent}.
}
$$

---

# 94. Continuous Re-Evaluation

不必每 tick 全算。

可以事件驅動：

- version change；
- frequency change；
- failure spike；
- memory pressure；
- distribution shift。

---

# 95. Crystal Pruning

若：

$$
U_H<\theta_R,
$$

則：

$$
\kappa
\rightarrow
\text{retire}.
$$

釋放：

- index；
- memory；
- maintenance burden。

---

# 96. Retire 不等於 Forget

provenance 可以保留低成本 record：

$$
\text{retired crystal receipt}.
$$

避免未來重做同一失敗 optimization。

---

# 97. Negative Optimization Crystal

如果某類 path 曾證明：

$$
U_H<0,
$$

可以形成：

$$
\kappa_{\mathrm{no-opt}}^-.
$$

表示：

> 在目前條件下，不值得再編譯。

---

# 98. Reopen Negative Crystal

但若：

- hardware changed；
- algorithm changed；
- frequency changed；

則可以 reopen。

---

# 99. Effective Hyperlink Path Encoding Pipeline

第一版：

```text
Observe Path
→ Estimate Frequency
→ Measure Cost
→ Estimate Stability
→ Estimate Verification Burden
→ Estimate Maintenance
→ Estimate Risk
→ Estimate Future Reuse
→ Compute Utility
→ Shadow Compile if Positive
→ Verify
→ Recompute Lifecycle Utility
→ Promote / Retain / Retire
```

---

# 100. EHPE 與 Adaptive Corridor Generator

Series 03 的：

$$
\mathcal M
$$

負責找 route。

EHPE 負責決定：

> 這條 route 是否值得成為持久化 fast path？

所以：

$$
\boxed{
\mathcal M
\neq
\operatorname{EHPE}.
}
$$

---

# 101. EHPE 與 Path Compiler

Path Compiler：

$$
\Gamma
\rightarrow
\widehat{\ell}.
$$

EHPE：

$$
\Gamma
\rightarrow
\text{compile?}
$$

所以 EHPE 可以在 PC 前做 prefilter。

---

# 102. EHPE 與 Crystallizer

Crystallizer：

$$
\widehat{\ell}
\rightarrow
\kappa.
$$

EHPE 可在結晶前再做：

$$
U_H(\widehat{\ell}).
$$

因此：

$$
\boxed{
\text{EHPE gates both compilation and crystallization}.
}
$$

---

# 103. EHPE 與 Semantic Revealing

若候選 path 太多，

可先：

$$
\Pi_{\xi}
(
\mathcal P
)
=
\mathcal P_{\mathrm{visible}}.
$$

只評估當前高價值候選。

---

# 104. EHPE 與 DRC

DRC 可以：

- 發散 candidate optimization；
- 共振 high-value region；
- 壓縮為 optimization shortlist。

---

# 105. EHPE 與 SEDB

SEDB 可以保存：

- path stats；
- lifecycle receipts；
- utility history；
- crystal identity；
- invalidation；
- provenance。

但 EHPE 不依賴特定資料庫。

---

# 106. EHPE 與記憶方法

後續 Crystallized Semantic Graph 也會遇到同一問題：

> 是否每段對話都要做所有壓縮版本、所有 link、所有高階 crystal？

答案也是：

$$
\boxed{
\text{selective crystallization}.
}
$$

---

# 107. Memory Crystal Utility

未來記憶可以有：

$$
U_M(c)
$$

依：

- recall frequency；
- importance；
- semantic density；
- retrieval benefit；
- update burden。

但這屬技術白皮書展開。

---

# 108. 不是所有可記憶內容都要高階結晶

同樣：

$$
\text{stored}
\neq
\text{high-order crystallized}.
$$

---

# 109. EHPE 的安全前置

即使：

$$
U_H^{\mathrm{performance}}>0,
$$

若：

$$
R>\theta_R,
$$

仍可直接：

$$
\operatorname{EHPE}=\text{retain slow path}.
$$

---

# 110. Safety Veto

因此：

$$
\boxed{
\operatorname{SafetyVeto}=1
\Rightarrow
\operatorname{Promote}=0.
}
$$

性能不能凌駕必要安全邊界。

---

# 111. 外部不可逆路徑

例如：

- payment；
- destructive write；
- account privilege；
- production mutation。

第一代預設不進 automated crystallized fast path。

---

# 112. 內部 reversible path

這也是為什麼遊戲適合作為第一個實驗域。

其：

$$
C_R
$$

可以低很多。

---

# 113. EHPE 與 UNPNP 完整成本

Series 01：

$$
\mathbf C.
$$

本文把 EHPE 寫成：

$$
\boxed{
\operatorname{EHPE}
:
(\Gamma,\mathbf C,\mathcal R,\mathcal H)
\rightarrow
d.
}
$$

其中：

$$
d
$$

是 compile decision。

---

# 114. 不是單純 Performance Optimizer

因為：

$$
\mathbf C
$$

包含：

- time；
- memory；
- energy；
- verification；
- maintenance；
- risk；
- selection。

所以 EHPE 是：

$$
\boxed{
\text{systemic optimization gate}.
}
$$

---

# 115. Core Proposition I

$$
\boxed{
\textbf{
可編譯性不是結晶化的充分條件；正向生命週期效用才是。
}
}
$$

---

# 116. Core Proposition II

$$
\boxed{
\textbf{
UNPNP 不應追求最大超連結數量，而應追求最大有效超連結總效用。
}
}
$$

---

# 117. Core Proposition III

$$
\boxed{
\textbf{
傳統程式的合理 AI 再編譯路線不是一次性整體翻譯，而是以原程式為 canonical fallback，逐步疊加已驗證的高價值 crystal overlay。
}
}
$$

---

# 118. Core Proposition IV

$$
\boxed{
\textbf{
任何 fast path 的價值都會隨頻率、環境、硬體、風險與維護負擔改變，因此 crystal utility 必須被重新評估，而不是一次 promotion 後永久有效。
}
}
$$

---

# 119. Core Proposition V

$$
\boxed{
\textbf{
最好的超連結系統，不是超連結最多的系統，而是最少浪費不必要計算的系統。
}
}
$$

---

# 120. 第一版決策模型

令：

$$
\Gamma
$$

為候選 path。

先計：

$$
\Delta C_{\mathrm{net}}
=
C_0
-
C_1
-
C_G
-
C_{V,\mathrm{run}}
-
C_S.
$$

若：

$$
\Delta C_{\mathrm{net}}\le0,
$$

則：

$$
\operatorname{retain}.
$$

若：

$$
\Delta C_{\mathrm{net}}>0,
$$

再估：

$$
N^\*.
$$

若：

$$
N_E<N^\*,
$$

則：

$$
\operatorname{observe}.
$$

若：

$$
N_E\ge N^\*
$$

且：

$$
R\le\theta_R,
$$

則：

$$
\operatorname{shadow\ compile}.
$$

驗證通過且：

$$
U_L>0,
$$

才：

$$
\operatorname{crystallize}.
$$

---

# 121. 結論

UNPNP 從 Series 06 開始具備一個很容易讓人興奮的能力：

$$
1
\rightarrow
2
\rightarrow
\cdots
\rightarrow
100
$$

可以變成：

$$
1
\rightarrow
100.
$$

Series 07 更進一步指出：

> 這條新路還可以結晶，甚至再結晶。

但如果只停在這裡，就很容易產生新的錯誤：

> 既然可以，那就全部做。

本文給出的答案是：

$$
\boxed{
\text{No.}
}
$$

真正成熟的 UNPNP Computer 不應把每一條 path 都編譯。

它必須持續問：

$$
\boxed{
\text{這條路，值不值得？}
}
$$

一條真正值得被超連結化的路徑，至少應該在：

- 執行頻率；
- 單次成本；
- 穩定度；
- 可驗證性；
- 有效域；
- 維護負擔；
- 選擇成本；
- 未來組合價值；
- 風險；

之間取得正向生命週期效用。

因此未來一般程式的 AI 再編譯，不應是：

$$
\text{Legacy Program}
\rightarrow
\text{Everything becomes hyperlinks}.
$$

而應是：

$$
\boxed{
\text{Legacy Program}
+
\text{Selective High-Utility Crystallized Hyperlink Overlay}.
}
$$

原本慢的地方，

如果值得，

AI 才重組。

原本已經夠快、只跑一次、變動太大或太危險的地方，

就不要碰。

所以本篇可以用一句話收束：

$$
\boxed{
\textbf{
不是所有程式都值得被改寫；
只有真正能讓整個生命週期更便宜、更穩定或更可靠的路，
才值得成為新的超連結。
}
}
$$

下一篇將進入這個系列另一個必要邊界：

> 當 fast path 真的可以快速跨越底空間時，如何限制它只能在被授權的世界中運行？

這將引出：

$$
\boxed{
\text{安全可達世界}.
}
$$

---

## 後續篇章

**Series 09｜安全可達世界：UNPNP 計算中的權限、能力與快速通道**

下一篇將正式處理：

$$
\mathcal W_t^{\mathrm{accessible}}
=
\mathcal W
\cap
\mathcal R(C_t),
$$

並建立：

- Reachable $\neq$ Authorized；
- capability envelope；
- identity / actor；
- multi-gate permission；
- internal experiment domain；
- read-only external domain；
- irreversible external action；
- safe shortest path；
- permission attenuation；
- fail-closed；
- fast authorization；
- poisoned fast path；
- why security must be part of the transition contract。
