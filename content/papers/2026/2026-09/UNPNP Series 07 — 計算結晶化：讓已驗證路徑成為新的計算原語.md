# UNPNP Series 07  
## 計算結晶化：讓已驗證路徑成為新的計算原語  
### Computational Crystallization: Turning Verified Paths into New Computational Primitives

**系列名稱：** UNPNP Hyperlink & Crystallized Computation Series  
**系列篇次：** 07  
**作者：** Neo.K with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-07  
**文件性質：** AI 原生計算／計算結晶化／UNPNP 理論論文  
**狀態：** Canonical Draft  

---

## 摘要

UNPNP Series 06 已提出 Path Compilation：當一段多階 traversal 在某個有效域內具有穩定語義、可驗證終態與可界定副作用時，系統可以將：

$$
B_1
\rightarrow
B_2
\rightarrow
\cdots
\rightarrow
B_n
$$

重新編譯成：

$$
B_1
\xrightarrow{\widehat{\ell}_{1,n}}
B_n.
$$

然而，一個被編譯出的 fast path 並不必然立刻成為系統長期使用的基本計算單位。它可能只是暫時 optimization、局部 session artifact、特定版本捷徑，甚至是只在一次測試中成立的候選。

本文提出 **Computational Crystallization**，用以描述一條已編譯路徑經過反覆成功、驗證、穩定化、成本評估、有效域界定與 provenance 固定之後，被提升為新的可重用計算原語的過程。

令：

$$
\Gamma
$$

為原始路徑，

$$
\operatorname{PC}(\Gamma)
=
\widehat{\ell}
$$

為 path compilation 結果。

若：

$$
\widehat{\ell}
$$

進一步滿足穩定性、可驗證性、可回退性、有效度與生命週期收益等條件，則結晶算子：

$$
\boxed{
K(
\widehat{\ell},
\mathcal E,
\mathcal H,
\mathcal C
)
=
\kappa
}
$$

生成一個計算結晶：

$$
\kappa.
$$

本文將計算結晶定義為：

$$
\boxed{
\kappa
=
\langle
D,
G,
F,
I,
O,
V,
P,
R,
X,
U,
L
\rangle,
}
$$

其中包含有效域、guard、快速執行形式、輸入與輸出契約、validator、provenance、rollback / fallback、invalidation condition、utility 與 lifecycle state。

因此：

$$
\boxed{
\text{Crystallization}
\neq
\text{Caching}
\neq
\text{Macro Packaging}
\neq
\text{Path Compilation}.
}
$$

Path Compilation 產生候選新路；Crystallization 則把其中足夠成熟的路提升為上一層可直接使用的新 primitive。

本文進一步提出高階結晶：

$$
K^{(2)}
(
\kappa_1,
\kappa_2,
\ldots,
\kappa_m
)
=
\kappa^{(2)},
$$

使一次結晶的結果可以再成為下一次結晶的材料。由此形成：

$$
\text{primitive}
\rightarrow
\text{compiled path}
\rightarrow
\text{crystal}
\rightarrow
\text{higher-order crystal}
\rightarrow
\cdots
$$

的多尺度計算階層。

本文同時提出正向結晶、負向結晶、暫時結晶、局部結晶、跨問題族結晶、解晶、失效、降級、合併與去重等機制。尤其重要的是，失敗路徑也可以結晶成「不要再走」的負向結構，使學習不只累積成功捷徑，也能累積已驗證的禁止、無效與高成本區域。

最後，本文將 Series 04 的「呼吸」與本文的「結晶」正式結合：

$$
\boxed{
ELC_t
\rightarrow
K_t
\rightarrow
ELC_{t+1}.
}
$$

其中：

$$
E
\rightarrow
L
\rightarrow
C
$$

產生可結晶結構，而：

$$
K_t
$$

反過來改寫下一輪可用 link set：

$$
\mathcal L_{t+1}
=
\mathcal L_t
\cup
\mathcal K_t^+
-
\mathcal K_t^-.
$$

因此：

$$
\boxed{
\textbf{
呼吸產生結晶，結晶改變下一次呼吸。
}
}
$$

在 UNPNP 中不再只是描述性比喻，而可以成為一個正式的自我優化計算模型。

**關鍵詞：** UNPNP、Computational Crystallization、Path Compilation、計算原語、Higher-Order Crystal、Cold Warm Hot、Decrystallization、Negative Crystal、Adaptive Runtime、AI Recompilation

---

# 1. 為什麼 Path Compilation 還不夠？

Series 06 已經建立：

$$
\Gamma
\xrightarrow{\operatorname{PC}}
\widehat{\ell}.
$$

但：

$$
\widehat{\ell}
$$

可能只是：

- 一次 session 的暫時捷徑；
- 某個版本專用優化；
- 尚未累積足夠驗證證據的 candidate；
- 高成本編譯後只值得執行一次的 path；
- 過度特化於單一 input 的 procedure。

因此：

$$
\boxed{
\text{Compiled}
\neq
\text{Crystallized}.
}
$$

---

# 2. 結晶化的基本直覺

結晶不是：

> 把一段程式碼壓成比較短。

而是：

> 一段原本需要多個步驟才能完成的計算，在反覆驗證後，被上一層系統視為一個穩定、可直接使用的新基本單位。

所以：

$$
\boxed{
\text{many operations}
\rightarrow
\text{one higher-level primitive}.
}
$$

---

# 3. 結晶算子

令：

$$
\widehat{\ell}
$$

為 compiled path。

令：

$$
\mathcal E
$$

為 verification evidence，

$$
\mathcal H
$$

為 execution history，

$$
\mathcal C
$$

為 cost / lifecycle information。

定義：

$$
\boxed{
K(
\widehat{\ell},
\mathcal E,
\mathcal H,
\mathcal C
)
=
\kappa.
}
$$

其中：

$$
\kappa
$$

為 computational crystal。

---

# 4. 計算結晶的第一版結構

本文定義：

$$
\boxed{
\kappa
=
\langle
D,
G,
F,
I,
O,
V,
P,
R,
X,
U,
L
\rangle.
}
$$

其中：

- $D$：valid domain；
- $G$：guard；
- $F$：fast executable form；
- $I$：input contract；
- $O$：output / postcondition；
- $V$：validator；
- $P$：provenance；
- $R$：rollback / fallback；
- $X$：invalidation conditions；
- $U$：utility statistics；
- $L$：lifecycle state。

---

# 5. 結晶與 Cache 的差別

Cache 通常保存：

$$
x\mapsto y.
$$

結晶保存的可以是：

$$
\boxed{
D
\mapsto
F_D.
}
$$

也就是：

> 對一個有效輸入域 $D$，存在一個成熟、可執行、可驗證的快速 procedure。

因此：

$$
\boxed{
\text{Cache stores results;}
}
$$

而：

$$
\boxed{
\text{Crystal stores validated reusable computation}.
}
$$

---

# 6. 結晶與 Macro 的差別

Macro：

$$
M
=
(\Theta_1,\ldots,\Theta_n)
$$

可能只是包裝。

結晶：

$$
\kappa
$$

要求：

$$
C(\kappa)
<
C(\Gamma)
$$

在有效域內真實成立。

所以：

$$
\boxed{
\text{Crystallization requires actual computational value}.
}
$$

---

# 7. 結晶與 Path Compilation 的差別

Path Compilation：

$$
\Gamma
\rightarrow
\widehat{\ell}.
$$

Crystallization：

$$
\widehat{\ell}
\rightarrow
\kappa.
$$

前者回答：

> 能否做出新路？

後者回答：

> 這條新路是否成熟到值得成為系統的新 primitive？

---

# 8. 結晶的 Promotion 條件

第一版可以要求：

$$
\operatorname{Promote}(\widehat{\ell})=1
$$

當：

$$
S(\widehat{\ell})\ge\theta_S,
$$

$$
V(\widehat{\ell})\ge\theta_V,
$$

$$
U(\widehat{\ell})>0,
$$

$$
R(\widehat{\ell})\le\theta_R.
$$

---

# 9. Stability

定義：

$$
S(\widehat{\ell})
=
f(
\text{success},
\text{repeatability},
\text{domain stability},
\text{dependency stability}
).
$$

高成功率但環境高度漂移，

仍不代表高穩定。

---

# 10. Verification Maturity

定義：

$$
M_V
$$

表示驗證成熟度。

它可以依：

- differential tests；
- property tests；
- replay；
- deterministic digest；
- shadow run；
- formal proof；
- statistical test；

累積。

---

# 11. Utility

結晶的有效度：

$$
U(\widehat{\ell})
$$

至少考慮：

$$
\Delta C,
$$

$$
f,
$$

$$
C_M,
$$

$$
R,
$$

$$
C_V.
$$

即節省多少、使用多頻繁、維護多昂貴、風險多高、驗證多困難。

---

# 12. Lifecycle State

一個結晶不是永久固定。

令：

$$
L(\kappa)
\in
\{
\text{candidate},
\text{cold},
\text{warm},
\text{hot},
\text{stale},
\text{retired}
\}.
$$

---

# 13. Candidate Crystal

剛完成 path compilation：

$$
\widehat{\ell}
$$

先進：

$$
\text{candidate}.
$$

它還不是 runtime primitive。

---

# 14. Cold Crystal

經初步驗證後：

$$
\text{candidate}
\rightarrow
\text{cold}.
$$

Cold 表示：

- 已有價值；
- 使用歷史少；
- 驗證仍較深；
- 不宜 aggressive reuse。

---

# 15. Warm Crystal

當：

$$
n_{\mathrm{success}}
\ge
\theta_W
$$

且：

$$
S(\kappa)
\ge
\theta_W^S,
$$

可：

$$
\text{cold}
\rightarrow
\text{warm}.
$$

Warm 可以被較積極調用。

---

# 16. Hot Crystal

若：

$$
f(\kappa)
$$

高，

且：

$$
V(\kappa)
$$

成熟，

以及：

$$
G(\kappa)
$$

便宜，

則：

$$
\text{warm}
\rightarrow
\text{hot}.
$$

Hot crystal 是真正的 fast primitive。

---

# 17. Stale Crystal

如果：

- dependency changed；
- version changed；
- schema changed；
- distribution shifted；
- permission changed；

則：

$$
\kappa
\rightarrow
\text{stale}.
$$

Stale 不應繼續走 fast path。

---

# 18. Retired Crystal

如果：

$$
U(\kappa)\le0
$$

或：

$$
\operatorname{FailureRate}>\theta_F,
$$

則：

$$
\kappa
\rightarrow
\text{retired}.
$$

---

# 19. 結晶不是永久真理

即：

$$
\boxed{
\text{Verified before}
\neq
\text{valid forever}.
}
$$

所以每個結晶都必須有：

$$
X
=
\text{invalidation conditions}.
$$

---

# 20. 依賴指紋

可建立：

$$
d_{\mathrm{dep}}
=
H(
v_1,\ldots,v_m
).
$$

若：

$$
d_{\mathrm{dep}}'
\neq
d_{\mathrm{dep}},
$$

則：

$$
\kappa
\rightarrow
\text{revalidation}.
$$

---

# 21. 解晶

本文將：

$$
\boxed{
\text{Decrystallization}
}
$$

定義為：

$$
D_K(\kappa)
\rightarrow
\Gamma.
$$

即：

> 將一個高階 primitive 重新展開回較低階 path。

---

# 22. 為什麼一定要能解晶？

因為：

- debugging；
- audit；
- version migration；
- failure analysis；
- verification；
- explanation；

都可能要求重新查看原始結構。

所以：

$$
\boxed{
\text{Crystallization}
\neq
\text{irreversible forgetting}.
}
$$

---

# 23. Provenance Chain

一個結晶：

$$
\kappa^{(2)}
$$

可能來自：

$$
\kappa_1,
\kappa_2.
$$

而：

$$
\kappa_1
$$

又來自：

$$
\Gamma_1.
$$

因此 provenance：

$$
\kappa^{(2)}
\rightarrow
\{
\kappa_1,\kappa_2
\}
\rightarrow
\{
\Gamma_1,\Gamma_2
\}.
$$

必須可追。

---

# 24. 結晶層級

定義：

$$
K^{(0)}
$$

為原始 primitive。

一次：

$$
K^{(1)}
$$

形成一階 crystal。

再一次：

$$
K^{(2)}
$$

形成二階 crystal。

一般：

$$
K^{(n)}.
$$

---

# 25. Higher-Order Crystallization

若：

$$
\kappa_1,
\kappa_2,
\ldots,
\kappa_m
$$

經常形成穩定 sequence：

$$
\kappa_1
\rightarrow
\kappa_2
\rightarrow
\cdots
\rightarrow
\kappa_m,
$$

則：

$$
\boxed{
K^{(2)}
(
\kappa_1,\ldots,\kappa_m
)
=
\kappa^{(2)}.
}
$$

---

# 26. $1\rightarrow100\rightarrow10000$

第一次：

$$
1
\rightarrow
2
\rightarrow
\cdots
\rightarrow
100.
$$

結晶：

$$
1
\rightarrow
100.
$$

再有：

$$
100
\rightarrow
101
\rightarrow
\cdots
\rightarrow
10000.
$$

結晶：

$$
100
\rightarrow
10000.
$$

最後高階：

$$
1
\rightarrow
10000.
$$

---

# 27. 結晶的遞歸性

因此：

$$
\boxed{
\text{crystals can be constituents of new crystals}.
}
$$

這使：

$$
\mathcal K
$$

不只是 flat cache。

而可以形成階層式計算世界。

---

# 28. Crystal Graph

令：

$$
\mathcal G_K
=
(V_K,E_K).
$$

其中：

$$
V_K
=
\{\kappa_1,\ldots,\kappa_n\}.
$$

邊表示：

- composition；
- dependency；
- alternative；
- specialization；
- generalization；
- conflict；
- invalidation。

---

# 29. Crystal Hypergraph

多個 crystal 共同形成一個新 primitive 時，

更自然是：

$$
e:
\{
\kappa_1,\kappa_2,\ldots,\kappa_m
\}
\rightarrow
\kappa'.
$$

因此計算結晶更一般可形成：

$$
\boxed{
\text{Crystallized Computational Hypergraph}.
}
$$

---

# 30. Crystal 不一定是線性 path

一個結晶可以代表：

- DAG；
- parallel execution；
- conditional branch；
- solver call；
- generated function；
- query plan；
- state machine；

只要上一層可把它當成一個 stable primitive。

---

# 31. Positive Crystal

最常見：

$$
\kappa^+.
$$

表示：

> 在條件 $G$ 下，走這條路是已驗證的有效 fast path。

---

# 32. Negative Crystal

若某條 route：

$$
\Gamma^{-}
$$

反覆證明：

- 無效；
- 太慢；
- 危險；
- 不可達；
- 會造成錯誤；

可以形成：

$$
\boxed{
\kappa^-.
}
$$

---

# 33. Negative Crystal 的語義

例如：

$$
\kappa^-
=
\langle
D,
G,
\text{avoid},
P,
V
\rangle.
$$

它不是 executable shortcut。

而是：

$$
\boxed{
\text{verified route suppression primitive}.
}
$$

---

# 34. 為什麼負向結晶重要？

沒有負向結晶，

Adaptive Corridor Generator 可能反覆重新探索：

$$
\text{known bad path}.
$$

所以：

$$
\kappa^-
$$

直接降低未來 Expansion cost。

---

# 35. Positive / Negative Duality

因此：

$$
\mathcal K_t
=
\mathcal K_t^+
\cup
\mathcal K_t^-.
$$

正向：

$$
\text{go faster}.
$$

負向：

$$
\text{do not waste time here}.
$$

---

# 36. Conditional Crystal

有些結晶只在：

$$
G_1
$$

成立。

另一個：

$$
G_2
$$

可能使用不同 route。

所以：

$$
\kappa
=
\{
G_i
\mapsto
F_i
\}.
$$

---

# 37. Multi-Version Crystal

同一目標：

$$
T
$$

可能有：

$$
\kappa_{\mathrm{CPU}},
$$

$$
\kappa_{\mathrm{GPU}},
$$

$$
\kappa_{\mathrm{low-memory}},
$$

$$
\kappa_{\mathrm{high-accuracy}}.
$$

Adaptive Corridor Generator 動態選擇。

---

# 38. Hardware-Aware Crystal

因此：

$$
\kappa
=
K(
\Gamma,
H_t
),
$$

其中：

$$
H_t
$$

是 hardware state。

---

# 39. Resource-Aware Crystal

同樣：

$$
\kappa
=
K(
\Gamma,
B_t
),
$$

其中：

$$
B_t
$$

為 budget。

---

# 40. Crystal Specialization

一個 general crystal：

$$
\kappa_G
$$

可以針對 hot domain：

$$
D_h
$$

生成：

$$
\kappa_{D_h}.
$$

使：

$$
C(\kappa_{D_h})
<
C(\kappa_G)
$$

在：

$$
D_h
$$

上成立。

---

# 41. Crystal Generalization

多個：

$$
\kappa_{x_1},
\ldots,
\kappa_{x_n}
$$

若共享 structure，

可以抽象：

$$
\boxed{
K_G(
\kappa_{x_1},\ldots,\kappa_{x_n}
)
=
\kappa_{\mathcal D}.
}
$$

這是從 instance crystal 走向 family crystal。

---

# 42. Crystal Merge

若：

$$
D_a\cap D_b
$$

大，

且：

$$
F_a\simeq F_b,
$$

可嘗試：

$$
\operatorname{Merge}
(
\kappa_a,\kappa_b
)
=
\kappa_{ab}.
$$

---

# 43. Crystal Deduplication

若：

$$
\kappa_a
\simeq
\kappa_b
$$

且 lifecycle value 重複，

則應 deduplicate。

避免：

$$
|\mathcal K_t|
$$

無限制膨脹。

---

# 44. Crystal Pruning

定義：

$$
U_L(\kappa)
$$

為 lifecycle utility。

若：

$$
U_L(\kappa)<\theta_P,
$$

則：

$$
\kappa
\rightarrow
\text{retire}.
$$

---

# 45. 結晶庫不是越大越好

如果：

$$
|\mathcal K|
\rightarrow
\infty,
$$

則 routing、maintenance、verification 也會變貴。

所以：

$$
\boxed{
\text{memory of shortcuts has its own complexity}.
}
$$

---

# 46. Crystal Selection Cost

若找：

$$
\kappa^\*
$$

本身需要：

$$
C_{\mathrm{select}}
$$

很大，

則 fast path 優勢可能被抵銷。

因此：

$$
C_{\mathrm{select}}
$$

也進完整成本帳本。

---

# 47. Crystal Index

可建立：

$$
I_K:
(s,g,h)
\mapsto
\{\kappa_1,\ldots,\kappa_m\}.
$$

使 candidate crystal 顯影成本下降。

---

# 48. Semantic Revealing of Crystals

用：

$$
\Pi_{\xi_t}
(
\mathcal K
)
=
\mathcal K_t^{\mathrm{visible}}.
$$

只顯影目前相關 crystals。

所以結晶庫可以很大，

active crystal set 仍小。

---

# 49. 結晶與 Working Set

因此：

$$
|\mathcal K_t^{\mathrm{active}}|
\ll
|\mathcal K|.
$$

這避免：

> 因為學會很多捷徑，反而每次選捷徑更慢。

---

# 50. Crystal Formation Cost

結晶成本：

$$
C_K
=
C_{\mathrm{qualify}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{index}}
+
C_{\mathrm{persist}}
+
C_{\mathrm{monitor}}.
$$

---

# 51. 結晶不是免費

完整：

$$
C_{\mathrm{crystal}}
=
C_{\mathrm{compile}}
+
C_K.
$$

只有長期：

$$
N\Delta C
>
C_{\mathrm{crystal}}
$$

才值得持久化。

---

# 52. Ephemeral Crystal

若：

$$
N
$$

預期很小，

但 session 內仍有價值，

可使用：

$$
\kappa_{\mathrm{ephemeral}}.
$$

session 結束即丟棄。

---

# 53. Persistent Crystal

若：

$$
N_{\mathrm{future}}
$$

高，

且：

$$
S(\kappa)
$$

高，

則持久化：

$$
\kappa_{\mathrm{persistent}}.
$$

---

# 54. Persistence 不等於永久 hot

Persistent 只表示：

> 值得保存。

不表示：

$$
L=\text{hot}
$$

永遠成立。

---

# 55. Crystal Replay

為驗證：

$$
\kappa
$$

可定期：

$$
\operatorname{Replay}(\kappa,D_{\mathrm{sample}}).
$$

若結果漂移：

$$
\kappa
\rightarrow
\text{stale}.
$$

---

# 56. Shadow Verification

新版本：

$$
\kappa'
$$

可以與原 path：

$$
\Gamma
$$

shadow run。

比較：

$$
\operatorname{Obs}(\kappa')
$$

與：

$$
\operatorname{Obs}(\Gamma).
$$

---

# 57. Fast Verification

Hot crystal 不一定每次 deep verification。

可用：

$$
V_{\mathrm{fast}}.
$$

例如：

- hash；
- state invariant；
- version token；
- range check；
- deterministic digest。

---

# 58. Deep Verification Trigger

若：

$$
U_t>\theta_U
$$

或：

$$
N_t>\theta_N,
$$

則：

$$
V_{\mathrm{fast}}
\rightarrow
V_{\mathrm{deep}}.
$$

---

# 59. 結晶的防錯機制

因此成熟 crystal 不是：

> 以後都相信它。

而是：

$$
\boxed{
\text{cheap continuous validation}
+
\text{conditional deep validation}.
}
$$

---

# 60. Crystal Failure

如果：

$$
V(\kappa)=0,
$$

則不能直接：

$$
\kappa\rightarrow\text{delete}.
$$

先判斷：

- transient failure；
- domain mismatch；
- version drift；
- implementation bug；
- corrupted dependency。

---

# 61. Repair

若：

$$
C_{\mathrm{repair}}
<
C_{\mathrm{recrystallize}},
$$

則：

$$
\kappa
\rightarrow
\kappa'.
$$

---

# 62. Recrystallization

如果 repair 不值得，

則：

$$
D_K(\kappa)
\rightarrow
\Gamma
\rightarrow
\operatorname{PC}
\rightarrow
\widehat{\ell}'
\rightarrow
K
\rightarrow
\kappa'.
$$

---

# 63. 解晶—再結晶循環

因此：

$$
\boxed{
\kappa
\rightarrow
\text{decrystallize}
\rightarrow
\text{recompile}
\rightarrow
\kappa'.
}
$$

這使結晶不是僵化結構。

---

# 64. 結晶與動態世界

如果：

$$
\mathcal W_t
$$

持續變動，

則：

$$
\mathcal K_t
$$

也必須動態變動：

$$
\mathcal K_{t+1}
\neq
\mathcal K_t.
$$

---

# 65. Crystal Evolution

可以寫：

$$
\mathcal K_{t+1}
=
U(
\mathcal K_t,
R_t,
\Delta\mathcal W_t
).
$$

其中：

$$
R_t
$$

為 execution receipts。

---

# 66. 晶格式計算世界

當 crystal 數量與層級增加，

整個世界可以想像成：

$$
\boxed{
\text{a lattice of reusable computational shortcuts}.
}
$$

但這裡的「晶格」是結構比喻與工程表示，不主張與數學 lattice theory 完全等同。

---

# 67. 原始程式與結晶層

Legacy program：

$$
P_0.
$$

觀察後形成：

$$
\mathcal K_1.
$$

之後 runtime 可以執行：

$$
P_0
+
\mathcal K_1.
$$

再形成：

$$
\mathcal K_2.
$$

---

# 68. 不需要一開始改寫全部程式

所以：

$$
\boxed{
\text{legacy source may remain canonical while crystals form as an optimization layer}.
}
$$

這對第一代實驗非常重要。

---

# 69. Crystal Overlay

可寫：

$$
P_t
=
P_{\mathrm{legacy}}
\oplus
\mathcal K_t.
$$

其中：

$$
\oplus
$$

表示：

> 在不抹掉原始程式的前提下疊加已驗證 fast paths。

---

# 70. 逐步替換

如果某些 crystal 長期成熟，

才可能：

$$
P_{\mathrm{legacy}}
\rightarrow
P_{\mathrm{recompiled}}.
$$

所以完全再編譯是後期結果，不是初始必要條件。

---

# 71. 遊戲中的結晶化

單機遊戲提供：

$$
S_t
$$

大量重複 transition。

例如：

- inventory query；
- pathfinding；
- combat routine；
- NPC behavior；
- resource lookup；
- quest update。

這些都是候選 crystal source。

---

# 72. 遊戲中的正向結晶

若：

$$
\Gamma_{\mathrm{heal}}
$$

反覆成立，

形成：

$$
\kappa_{\mathrm{heal}}^+.
$$

下一次：

$$
s_t
\xrightarrow{\kappa_{\mathrm{heal}}}
s_{t+1}.
$$

---

# 73. 遊戲中的負向結晶

如果某 route：

$$
\Gamma_{\mathrm{danger}}
$$

反覆造成：

$$
\text{death / failure},
$$

可形成：

$$
\kappa_{\mathrm{danger}}^-.
$$

直接在 Expansion 階段遮蔽。

---

# 74. 遊戲是結晶演化的風洞

因為：

- state 可保存；
- failure 可重播；
- performance 可量；
- world 複雜；
- side effect 可回滾。

所以非常適合觀察：

$$
\mathcal K_t
$$

是否真正逐步改善 runtime。

---

# 75. Crystallization Ratio

定義：

$$
R_K(t)
=
\frac{
N_{\mathrm{crystal\ transitions}}
}{
N_{\mathrm{all\ transitions}}
}.
$$

理想穩定 workload：

$$
R_K(t)\uparrow.
$$

---

# 76. Deep Reasoning Ratio

同時：

$$
R_D(t)
=
\frac{
N_{\mathrm{deep\ reasoning}}
}{
N_{\mathrm{all\ transitions}}
}.
$$

若結晶有效：

$$
R_D(t)\downarrow.
$$

---

# 77. Average Runtime Cost

$$
C_{\mathrm{avg}}(t)
=
\frac{
\sum C_t
}{
N_t
}.
$$

最重要的觀察之一：

$$
\boxed{
\frac{dC_{\mathrm{avg}}}{dt}<0
}
$$

在穩定 workload 中是否成立。

---

# 78. Crystal Utility Curve

一個 crystal 的累積價值：

$$
U_N(\kappa)
=
N
\Delta C
-
C_{\mathrm{crystal}}
-
C_{\mathrm{maintain}}(N).
$$

若：

$$
U_N>0,
$$

代表 lifecycle beneficial。

---

# 79. Crystal Debt

某些 crystal 前期有收益，

後期維護變貴。

可定義：

$$
D_K
=
C_{\mathrm{maintain}}
-
N\Delta C.
$$

若：

$$
D_K>0,
$$

應考慮退役。

---

# 80. 結晶與外部複雜度

結晶把：

$$
C_{\mathrm{runtime}}
$$

轉移為：

$$
C_{\mathrm{compile}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{store}}
+
C_{\mathrm{maintain}}.
$$

因此仍然符合 Series 01：

$$
\boxed{
\text{complexity moves}.
}
$$

---

# 81. 結晶不是免費超能力

一個世界如果變化太快，

可能：

$$
C_{\mathrm{maintain}}
\gg
\Delta C_{\mathrm{run}}.
$$

則結晶化不划算。

---

# 82. Crystallizability

可以定義某 path 的可結晶度：

$$
Q_K(\Gamma)
=
f(
\text{frequency},
\text{stability},
\text{cost},
\text{verifiability},
\text{domain width},
\text{maintenance burden}
).
$$

---

# 83. 高可結晶區域

通常：

$$
f\uparrow,
$$

$$
S\uparrow,
$$

$$
C_{\mathrm{old}}\uparrow,
$$

$$
C_V\downarrow
$$

會提高：

$$
Q_K.
$$

---

# 84. 低可結晶區域

例如：

- one-shot task；
- rapidly changing state；
- high uncertainty；
- irreversible external action；
- difficult equivalence；
- very low frequency。

不應強迫結晶。

---

# 85. 選擇性結晶

因此：

$$
\boxed{
\max
\text{crystal count}
}
$$

不是目標。

而是：

$$
\boxed{
\max
\sum_{\kappa\in\mathcal K}
U_L(\kappa).
}
$$

---

# 86. 結晶與有效度超連結

這直接通向 Series 08。

真正應決定是否結晶的是：

$$
\boxed{
\text{Effective Hyperlink Utility}.
}
$$

而不是：

> 能不能做成 hyperlink？

---

# 87. Crystal as Primitive

當：

$$
\kappa
$$

成為 hot，

上一層 runtime 可以把它視為：

$$
p_{\mathrm{new}}.
$$

所以：

$$
\boxed{
P_{t+1}
=
P_t
\cup
\{p_{\mathrm{new}}\}.
}
$$

---

# 88. 程式原語不是固定集合

傳統：

$$
\mathcal P_t
=
\mathcal P_0.
$$

UNPNP：

$$
\boxed{
\mathcal P_{t+1}
=
\mathcal P_t
\cup
K_t^+
-
K_t^-.
}
$$

這是非常重要的差異。

---

# 89. Computational Vocabulary Growth

可以把 primitive set 看成：

$$
\mathcal V_t.
$$

結晶化使：

$$
|\mathcal V_{t+1}|
>
|\mathcal V_t|
$$

在有價值的新 primitive 出現時成立。

也就是：

> 計算機會長出自己的新「動詞」。

---

# 90. 但 Vocabulary 也需要壓縮

如果：

$$
|\mathcal V|
$$

太大，

routing 成本升高。

所以需要：

- merge；
- abstraction；
- hierarchy；
- pruning。

---

# 91. Higher-Order Vocabulary

多個 primitive：

$$
p_1,\ldots,p_n
$$

可結晶成：

$$
P.
$$

於是：

$$
P
$$

對上一層是 primitive，

對下一層是 compound path。

---

# 92. 自指結構

因此：

$$
\boxed{
\text{primitive at level }k
=
\text{path at level }k-1.
}
$$

這與 Series 02 的自指底空間完全相容。

---

# 93. 呼吸與結晶的正式接口

Series 04：

$$
S_t
\xrightarrow{E_t}
F_t
\xrightarrow{L_t}
O_t
\xrightarrow{C_t}
S_{t+1}.
$$

本文加入：

$$
\boxed{
K_t
=
K(
E_t,
L_t,
C_t,
R_t
).
}
$$

---

# 94. 下一輪計算世界更新

若：

$$
K_t^+
$$

為新增正向結晶，

$$
K_t^-
$$

為淘汰或負向結晶，

則：

$$
\boxed{
\mathcal L_{t+1}
=
\mathcal L_t
\cup
K_t^+
-
K_t^-.
}
$$

---

# 95. 呼吸產生結晶

即：

$$
\boxed{
ELC_t
\rightarrow
K_t.
}
$$

每一次完整計算都可能留下：

- reusable path；
- negative path；
- better guard；
- compressed state；
- new primitive。

---

# 96. 結晶改變下一次呼吸

因為：

$$
\mathcal L_{t+1}
\neq
\mathcal L_t,
$$

所以下一次 Expansion：

$$
E_{t+1}
$$

面對的是不同計算圖。

因此：

$$
\boxed{
K_t
\rightarrow
ELC_{t+1}.
}
$$

---

# 97. Breathing–Crystallization Loop

完整：

$$
\boxed{
ELC_t
\rightarrow
K_t
\rightarrow
ELC_{t+1}
\rightarrow
K_{t+1}
\rightarrow
\cdots
}
$$

這是本篇最核心的動態式。

---

# 98. 自我優化的真正含義

self-optimizing 不表示：

> AI 每次都修改自己的模型權重。

也可以只是：

$$
\mathcal K_{t+1}
\neq
\mathcal K_t.
$$

即：

> 可用計算 primitive 集合正在改善。

---

# 99. Frozen-Model Crystallization Experiment

故意固定：

$$
\theta_{\mathrm{model}}.
$$

只允許：

$$
\mathcal K_t
$$

變化。

若：

$$
C_{\mathrm{avg}}(t)\downarrow,
$$

則可證明：

> 性能提升來自架構結晶，而不是模型更新。

---

# 100. 結晶與學習

因此本文提出：

$$
\boxed{
\text{Learning}
\supset
\text{Crystallized Computational Adaptation}.
}
$$

weight update 只是學習的一種形式。

---

# 101. Path Memory

每個：

$$
\kappa
$$

其實也是：

$$
\boxed{
\text{verified computational memory}.
}
$$

它記住的不是：

> 曾經發生什麼。

而是：

> 以後遇到這類狀態，可以怎麼更便宜地算。

---

# 102. 與記憶結晶化的區別

後續結晶化語義圖白皮書處理：

$$
\text{semantic memory crystal}.
$$

本篇處理：

$$
\text{computational path crystal}.
$$

兩者可以互相連接，

但不是同一資料結構。

---

# 103. Semantic Crystal 與 Computational Crystal

語義結晶回答：

> 我知道什麼？

計算結晶回答：

> 我知道怎麼做。

因此：

$$
\boxed{
\text{knowledge crystal}
\neq
\text{execution crystal}.
}
$$

但未來可以形成雙向 link。

---

# 104. Safety Crystal

安全領域甚至可以有：

$$
\kappa_{\mathrm{safe}}
$$

記錄：

- approved route；
- denied route；
- capability boundary；
- verified rollback。

但權限本身不應因結晶自動擴張。

---

# 105. Learning 不能變成 Self-Authorization

所以：

$$
\boxed{
K
\not\Rightarrow
\text{permission expansion}.
}
$$

結晶可以讓合法路徑更快，

不能讓原本禁止的路徑因「常用」就自動合法。

---

# 106. Crystal Security Boundary

一個 crystal：

$$
\kappa
$$

必須攜帶：

$$
C_{\mathrm{req}}(\kappa).
$$

runtime 要求：

$$
C_{\mathrm{req}}(\kappa)
\subseteq
C_t.
$$

---

# 107. 快速錯誤問題

結晶使正確路徑變快。

也可能使錯誤路徑變快。

因此：

$$
\boxed{
\text{fast path}
\Rightarrow
\text{need fast invalidation}.
}
$$

---

# 108. Poisoned Crystal

如果：

$$
P
$$

或：

$$
V
$$

被污染，

則：

$$
\kappa
$$

可能變成 poisoned fast path。

所以 provenance 與 validator 不可省略。

---

# 109. Crystal Trust

可定義：

$$
T_K(\kappa)
=
f(
V,
P,
S,
R,
\text{freshness}
).
$$

只有：

$$
T_K>\theta_T
$$

才進 hot。

---

# 110. Crystal Trust 不是永久常數

$$
T_K(t+1)
\neq
T_K(t)
$$

可以因：

- stale；
- dependency change；
- new failure；
- new evidence；

改變。

---

# 111. Crystallization 不等於 P=NP

即使某一問題族形成大量：

$$
\kappa,
$$

也不代表：

$$
P=NP.
$$

因為：

- 建晶成本可能高；
- 外部資源可能巨大；
- worst case 未改善；
- uniform generator 未證明。

---

# 112. Non-Uniform Crystal

若：

$$
\forall x
\exists\kappa_x,
$$

也不代表：

$$
\exists K
\forall x.
$$

所以：

$$
\boxed{
\text{crystal existence}
\neq
\text{uniform crystallizer}.
}
$$

---

# 113. Universal Crystallizer 是更強命題

真正強的是存在：

$$
K^\*
$$

可以對問題族：

$$
\mathcal D
$$

低成本形成有價值 crystals。

這與 Series 03 的：

$$
\mathsf{AGC}
$$

及：

$$
\mathsf{UGC}
$$

相接。

---

# 114. 不可結晶區域

有些計算可能：

- 不重複；
- 不穩定；
- 不可驗證；
- 過度 context-dependent；
- 高度 adversarial；
- 編譯成本過高。

因此：

$$
Q_K\approx0.
$$

UNPNP 必須承認這些區域存在。

---

# 115. 核心命題一

$$
\boxed{
\textbf{
計算結晶化不是壓縮輸出，而是把反覆驗證且具有生命週期收益的計算路徑提升為新的可重用原語。
}
}
$$

---

# 116. 核心命題二

$$
\boxed{
\textbf{
結晶必須可追溯、可失效、可降級、可解晶；否則它只是不可觀測的黑箱捷徑。
}
}
$$

---

# 117. 核心命題三

$$
\boxed{
\textbf{
結晶可以再次結晶，因此計算 primitive 的抽象層級可以隨執行歷史逐步升高。
}
}
$$

---

# 118. 核心命題四

$$
\boxed{
\textbf{
負向失敗經驗也可以結晶，從而讓系統不只記住哪些路值得走，也記住哪些路不值得再走。
}
}
$$

---

# 119. 核心命題五

$$
\boxed{
\textbf{
呼吸產生結晶，結晶改變下一次呼吸。
}
}
$$

---

# 120. 第一版總模型

完整 runtime：

$$
S_t
\xrightarrow{E_t}
F_t
\xrightarrow{L_t}
O_t
\xrightarrow{C_t}
S_{t+1}
\xrightarrow{K_t}
\mathcal K_{t+1}.
$$

其中：

$$
\boxed{
\mathcal K_{t+1}
=
U(
\mathcal K_t,
K_t,
R_t,
\Delta\mathcal W_t
).
}
$$

---

# 121. Primitive Set Evolution

定義：

$$
\mathcal P_t
$$

為 runtime primitive set。

則：

$$
\boxed{
\mathcal P_{t+1}
=
\mathcal P_t
\cup
\operatorname{Promote}(\mathcal K_t)
-
\operatorname{Retire}(\mathcal K_t).
}
$$

---

# 122. 結論

路徑編譯使：

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

但只有當這條新路經過：

- 有效域界定；
- 多次成功；
- equivalence verification；
- cost validation；
- dependency binding；
- provenance 固定；
- rollback / fallback；
- lifecycle evaluation；

它才應從：

$$
\text{compiled candidate}
$$

真正升級為：

$$
\boxed{
\text{computational crystal}.
}
$$

一旦成為 crystal，

上一層不再需要把它視為：

> 一段複雜歷史。

而可以把它視為：

$$
\boxed{
\text{一個新的計算動詞。}
}
$$

而當多個新動詞又形成穩定路徑：

$$
\kappa_1
\rightarrow
\kappa_2
\rightarrow
\cdots
\rightarrow
\kappa_n,
$$

系統還能再一次：

$$
K^{(2)}
\rightarrow
\kappa^{(2)}.
$$

因此 UNPNP Computer 的 primitive vocabulary 不是永遠由原始程式設計者固定。

它可以：

$$
\boxed{
\text{執行}
\rightarrow
\text{觀察}
\rightarrow
\text{重編譯}
\rightarrow
\text{驗證}
\rightarrow
\text{結晶}
\rightarrow
\text{生成新的原語}.
}
$$

這就是計算結晶化真正重要的地方。

最終：

$$
\boxed{
\textbf{
呼吸不是白呼吸。
每一次成功的展開—連結—收斂，都可能留下新的結晶；
而每一塊結晶，都可能讓下一次世界穿越變得更短。
}
}
$$

下一篇將回答一個更務實的問題：

> 既然可以結晶，是不是所有可以結晶的路徑都應該結晶？

答案顯然是否定的。

真正需要的是一套：

$$
\boxed{
\text{有效度超連結路徑編碼}
}
$$

來決定哪些路值得被編譯、保存與提升為 fast path。

---

## 後續篇章

**Series 08｜有效度超連結路徑編碼：不是所有程式都值得被改寫**

下一篇將正式處理：

$$
U_H(\Gamma)
$$

與：

$$
U_K(\kappa),
$$

並建立：

- frequency；
- cost saving；
- stability；
- verification burden；
- maintenance；
- risk；
- domain width；
- break-even；
- selective recompilation；
- negative optimization；
- crystal pruning；
- effective hyperlink density；
- 為什麼目標不是「全程式 hyperlink 化」，而是「只改真正值得改的路」。
