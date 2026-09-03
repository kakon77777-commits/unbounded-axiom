# CODT-06
# History-Flow-Atlas Separation：認知歷史、轉移動力與域結構
## History-Flow-Atlas Separation: Cognitive History, Transition Dynamics, and Domain Structure

**系列：** Cognitive Operator-Domain Theory, CODT / 認知算子-域理論  
**系列篇次：** 06 / 10  
**版本：** v1.0  
**日期：** 2026-08-20  
**作者：** Neo.K  
**機構脈絡：** EveMissLab / 一言諾科技有限公司  
**文件性質：** 理論論文 / History-Predictive-State 篇  
**前篇：** CODT-05〈認知域不是固定分類：Flow-Atlas Separation〉

---

## 摘要

CODT-05 已將認知 runtime 拆成 adaptive operator flow 與 quasi-stable atlas，並指出 regime shift 可以先改變 transition law，而不必立即重畫 domain geometry。然而，只要 flow model 仍主要依賴一階轉移：

$$
P(U_{t+1}\mid U_t),
$$

就存在一個危險替代解釋：先前看到的 atlas / domain structure，可能只是 flow model 看不見較長 operator history，因此把 temporal dependence 錯投影成 spatial partition。

本文提出 **History-Flow-Atlas Separation, HFAS**，並整合 CDD Phase 0.8-0.9 的高階歷史、variable-order context、Approximate Predictive History States, APHS 與 directional quotient experiments。其核心結論是：

$$
\boxed{
History
\neq
Flow
\neq
Atlas.
}
$$

在 frozen synthetic runtime 中，一階 operator history 相對 order-0 具有穩定 predictive value：

$$
E[\Delta_{0\to1}]
=
0.2653
\text{ bits/transition},
$$

且五個 normal splits 均為正；但 $k\ge2$ 的 fixed higher-order history 在五個 splits 均相對 order-1 惡化，平均：

$$
E[\Delta_{1\to k\ge2}]
=
-0.8505.
$$

MDL-pruned variable-order history tree 亦在五個 normal splits 全部退回 root / depth-0。這使「higher-order grammar 解釋掉 atlas」的強版本在目前 synthetic evidence 下被反證。

更重要的是，即使 exact current source operator $U_t$ 已知，target-side atlas 仍然帶來約：

$$
E[\Delta_{Atlas\mid H_1}]
=
0.1920
\text{ bits/transition}
$$

的 residual predictive / compressive gain，且五個 splits 均為正。隨機等尺寸 atlas permutation 顯著更差，因此 atlas 的 residual value 不能只由任意 smoothing 解釋。

Phase 0.9 進一步建立 APHS：不同 histories 若具有近似相同有限 future distribution，可以被壓成 source-side predictive states。然而五個 normal splits 的最佳 history length 全部仍為 $L=1$。APHS 確實比 exact order-1 source flow 平均改善 $0.1191$ bits/transition，但 target-side atlas 又比 APHS 平均改善約 $0.1194$ bits/transition。APHS 與 atlas 具有非隨機 relation，但低 ARI 顯示兩者遠非同一 partition。

因此本文正式提出 **Directional Quotient Separation**：

$$
\boxed{
\epsilon_R^{src}
\neq
\pi_R^{dst}.
}
$$

source-side quotient 依 predictive similarity 壓縮來源 operator / history；destination-side atlas quotient 則依 transition / emission usefulness 壓縮下一步 operator。兩者服務不同 compression interfaces，不應再把 Cognitive Domain Atlas 想成對 transition 兩端都相同的對稱 equivalence relation。

本文最後將 cognition runtime 寫成：

$$
\boxed{
CognitiveRuntime_t
=
(
H_t,
P_R,
\epsilon_R^{src},
\pi_R^{dst},
\mathcal A_t
).
}
$$

其中 history、flow、predictive source quotient、destination atlas 與 atlas version 都必須分帳。本文同時保留一個重要限制：Phase 0.8-0.9 只反證了目前 synthetic runtime 下的 fixed-order / variable-order operator-history explanation，不能推出真實人類或 AI cognition 不存在長程 temporal grammar。這個負結果反而把下一篇問題推向 World / Runtime state：如果增加 operator history 沒有解決 OOD，那真正缺失的可能不是「再多記幾步」，而是 observer-relative state 與 predictive interface。

---

## 關鍵詞

History-Flow-Atlas Separation；CODT；operator history；higher-order Markov；variable-length Markov；predictive state；APHS；directional quotient；cognitive atlas；temporal grammar；causal states；predictive representation

---

# 1. 問題：Domain 會不會只是 History 的假影像？

CODT-05 已經拆開：

$$
Flow
\neq
Atlas.
$$

但當時的 flow 仍大量依賴：

$$
P(U_{t+1}\mid U_t).
$$

如果真實 cognition 具有：

$$
P(U_{t+1}\mid U_{t-k+1:t}),
\quad
k>1,
$$

那一階 model 可能看不到 long-range dependency。

此時一個 atlas learner 可能把：

$$
\text{history dependence}
$$

錯誤補成：

$$
\text{operator-space clustering}.
$$

因此提出 **Temporal Compensation Hypothesis**：

$$
\boxed{
\text{some apparent domain structure}
=
\text{spatial compensation for missing temporal grammar}.
}
$$

如果它成立，則增加 history order 後：

$$
Value(Atlas)
$$

應大幅下降。

---

# 2. History 是什麼？

CODT-02 已把 ordered operator history 視為 canonical runtime data。

令：

$$
H_t
=
(U_1,U_2,\ldots,U_t).
$$

更一般地，history 不只可以包含 operator IDs。

它還可以包含：

- artifacts；
- certificates；
- failures；
- memory updates；
- belief changes；
- representation changes；
- action requests；
- World presentations。

但 CODT-06 先聚焦最窄版本：

$$
H_t^U
=
(U_1,\ldots,U_t).
$$

因為如果連 operator sequence 本身的 temporal dependence 都沒有拆乾淨，就不應直接宣稱 domain geometry。

---

# 3. History 不是 Flow

history 是已發生的 ordered record。

flow 是條件轉移 law：

$$
\boxed{
P_t
=
P(
U_{t+1}
\mid
H_t,
S_t,
B_t,
R_t
).
}
$$

因此：

$$
\boxed{
H_t
\neq
P_t.
}
$$

相同 history 可以由不同 model 解讀。

相同 flow model 也可以生成不同 histories。

所以 history 是 evidence / path。

flow 是 predictive dynamics。

---

# 4. Flow 也不是 History Length

一個 model 使用：

$$
k=5
$$

不代表 cognition 真正有「五步深度」。

 $k$ 只是 model conditioning length。

因此：

$$
\boxed{
MarkovOrder
\neq
CognitiveDepth.
}
$$

高 order 可能只是在補：

- omitted state；
- regime；
- world context；
- hidden goal；
- memory backend；
- representation phase。

反過來，低 order 也不代表 cognition 沒有 long-range structure。

如果 state representation 已經足夠，長 history 可以被壓縮掉。

---

# 5. Fixed-Order History Models

對 order- $k$：

$$
\boxed{
P_k(U_{t+1})
=
P(U_{t+1}\mid U_{t-k+1:t}).
}
$$

其中：

$$
k=0
$$

是 unigram：

$$
P(U_{t+1}).
$$

$$
k=1
$$

是：

$$
P(U_{t+1}\mid U_t).
$$

而：

$$
k\ge2
$$

開始檢查 longer operator grammar。

這個 probe 最直接。

但也最容易遇到 state-space explosion。

---

# 6. Variable-Length History

固定 $k$ 的問題是：

所有 contexts 都被迫使用相同記憶長度。

而真實 sequence process 可能有：

- 某些 histories 只需一步；
- 某些 histories 需要三步；
- 某些 histories 需要更長 suffix。

Variable Length Markov Chain / context-tree tradition 提供一個重要方法學參照：

$$
\boxed{
\text{effective memory length can depend on history}.
}
$$

CODT 因此在 Phase 0.8 使用 MDL-pruned finite context tree。

但本文必須保持邊界：

$$
\boxed{
\text{CDD context tree}
\neq
\text{exact CTW}
\neq
\text{exact VLMC reconstruction}.
}
$$

它只是 temporal-grammar falsification probe。

---

# 7. History Model 自己也要付成本

較長 history 一定可以增加 fit flexibility。

因此只比較 training likelihood 會鼓勵：

$$
k\rightarrow\infty.
$$

CODT 延續 MDL discipline。

history model selection 應考慮：

$$
\boxed{
L_{total}
=
L(Model_k)
+
L(Data\mid Model_k).
}
$$

variable-order tree 只有在 split node 能賺回 context-description cost 時，才保留更長 memory。

所以：

$$
\boxed{
MaximumAllowedDepth
\neq
SelectedEffectiveDepth.
}
$$

---

# 8. Phase 0.8：一階 History 有資訊

Normal 主 run：

$$
Bits_0
=
4.8085,
$$

$$
Bits_1
=
4.5199.
$$

因此：

$$
\boxed{
\Delta_{0\to1}
=
0.2886
\text{ bits/transition}.
}
$$

五個 normal splits：

$$
\boxed{
\Delta_{0\to1}>0
\quad
5/5.
}
$$

平均：

$$
\boxed{
E[\Delta_{0\to1}]
=
0.2653.
}
$$

因此：

$$
\boxed{
\text{one-step flow memory carries real synthetic signal}.
}
$$

---

# 9. 但 Higher-Order Grammar 沒有出現

同一 experiment 中：

validation-selected best $k\ge2$ model 在 main test：

$$
Bits_{k\ge2}
=
5.3701.
$$

相對 order-1：

$$
\boxed{
\Delta_{1\to k\ge2}
=
-0.8502.
}
$$

五個 normal splits：

$$
\boxed{
\Delta_{1\to k\ge2}<0
\quad
5/5.
}
$$

平均：

$$
\boxed{
E[\Delta_{1\to k\ge2}]
=
-0.8505.
}
$$

所以：

$$
\boxed{
\text{one-step memory}
\neq
\text{higher-order grammar}.
}
$$

目前 synthetic runtime 支持前者。

不支持後者。

---

# 10. Variable-Order Tree 也退回 Root

更嚴格的是 MDL-pruned variable-order context tree。

雖然 maximum depth 允許：

$$
1,\ldots,5,
$$

五個 normal split 中都選：

$$
\boxed{
Depth_{selected}=0.
}
$$

也就是 context tree 沒找到值得支付 complexity cost 的 longer-history branches。

因此目前的 temporal evidence 不是：

$$
\boxed{
\text{a hidden deep grammar}.
}
$$

而更像：

$$
\boxed{
\text{short-memory transition dependence}.
}
$$

---

# 11. 這不是「Cognition 沒有長期記憶」

這個負結果最容易被過度解讀。

它不表示：

$$
\boxed{
\text{Human cognition is Markov order 1}.
}
$$

也不表示：

$$
\boxed{
\text{AI cognition has no long-term dependency}.
}
$$

它只表示：

> 在目前 synthetic operator-trace generator、目前 operator vocabulary、目前 state representation 與目前 history coder 下，增加 operator-ID history beyond one step 沒有得到 robust held-out gain。

因此：

$$
\boxed{
\text{NoEvidenceForLongGrammar}
\neq
\text{ProofOfNoLongGrammar}.
}
$$

---

# 12. Temporal Compensation Hypothesis 的測試

若 atlas 只是 missing history 的 compensation，則在 exact current operator 已知時：

$$
Value(Atlas\mid U_t)
$$

應接近零。

Phase 0.8 因此建立：

$$
\boxed{
U_t
\rightarrow
C_{t+1}
\rightarrow
U_{t+1}.
}
$$

source 端保持 exact operator identity。

target 端才使用 atlas quotient。

這是最關鍵的 directional test。

---

# 13. Atlas Residual Value

Normal main：

$$
Bits_{order1}
=
4.5199.
$$

exact-source / target-atlas：

$$
Bits_{U_t\to C_{t+1}\to U_{t+1}}
=
4.3278.
$$

因此：

$$
\boxed{
\Delta_{Atlas\mid H_1}
=
0.1921
\text{ bits/transition}.
}
$$

五個 normal splits 平均：

$$
\boxed{
E[\Delta_{Atlas\mid H_1}]
=
0.1920.
}
$$

且：

$$
\boxed{
5/5>0.
}
$$

所以：

$$
\boxed{
\text{Atlas value survives one-step history control}.
}
$$

這直接削弱：

$$
\boxed{
\text{Atlas = missing temporal grammar artifact}.
}
$$

---

# 14. 隨機 Pooling 不能解釋 Residual Gain

若任何 target pooling 都會降低 variance、改善 prediction，那 atlas residual gain 可能只是 smoothing artifact。

因此 Phase 0.8 做 200 次 same-size random atlas permutation。

learned atlas：

$$
Bits_{learned}
=
4.3278.
$$

random mean：

$$
E[Bits_{random}]
=
4.5654.
$$

empirical lower tail：

$$
\boxed{
p
\approx
0.00498.
}
$$

human family directional baseline：

$$
Bits_{human}
=
4.4115.
$$

因此：

$$
\boxed{
\text{learned target quotient}
\neq
\text{arbitrary pooling}.
}
$$

至少在目前 synthetic experiment 中成立。

---

# 15. History-Flow-Atlas Separation v0.1

到這裡可以正式寫：

$$
\boxed{
History
\neq
Flow
\neq
Atlas.
}
$$

其中 $H_t$ 回答：

> 發生過什麼？

 $P_t$ 回答：

> 在目前條件下下一步怎麼走？

 $\mathcal A_t$ 回答：

> 哪些作用區值得被當成較慢、較穩定的 derived structural chart？

三者可以相互提供 evidence。

但不能互相取代。

---

# 16. 從 History Length 到 Predictive Equivalence

Phase 0.8 的負結果留下另一個更好的問題。

也許真正重要的不是：

$$
|h_i|
=
|h_j|,
$$

而是：

> 兩個不同 histories 對未來是否具有相同 predictive distribution？

這和 computational mechanics 的 causal-state 思路形成一個重要外部方法學參照。

其核心不是把所有相同長度 histories 視為同一 state，而是把對 future distribution 具有相同 predictive consequence 的 pasts 視為同一 predictive equivalence class。

CODT 吸收這個思想，但必須明確限制：

$$
\boxed{
\text{CODT predictive state candidate}
\neq
\text{exact causal state}.
}
$$

因為目前只處理 finite history、finite future、finite data 與 approximate clustering。

---

# 17. Approximate Predictive History States

Phase 0.9 定義有限 future horizon $F$ 的 predictive signature：

$$
\boxed{
\phi_F(h_t)
=
\bigoplus_{j=1}^{F}
P(U_{t+j}\mid h_t).
}
$$

若：

$$
JS(
\phi_F(h_i),
\phi_F(h_j)
)
\leq
\delta,
$$

則：

$$
\boxed{
h_i
\sim_{F,\delta}
h_j.
}
$$

這形成 Approximate Predictive History State candidate：

$$
S^{pred}
=
[h]_{F,\delta}.
$$

但這個 equivalence 是 finite / empirical / approximate。

所以：

$$
\boxed{
APHS
\neq
ExactCausalState.
}
$$

---

# 18. APHS 不是「記得更多」

Predictive state compression 和直接增加 history length 是兩種不同操作。

增加 history：

$$
U_t
\rightarrow
(U_{t-1},U_t)
\rightarrow
(U_{t-2},U_{t-1},U_t).
$$

predictive quotient 則可能：

$$
(h_a,h_b,h_c)
\rightarrow
S_1^{pred}
$$

只因為這些 histories 對 future distribution 的作用近似相同。

因此：

$$
\boxed{
\text{MoreHistory}
\neq
\text{BetterState}.
}
$$

有時候真正需要的是 compression。

不是更多 raw past。

---

# 19. Phase 0.9 的 Model Selection

Phase 0.9 讓 model selection 在：

$$
L\in\{1,2\}
$$

的 history length 中選擇。

五個 normal splits 最後全部得到：

$$
\boxed{
L
=
[1,1,1,1,1].
}
$$

future horizon 則在：

$$
F\in\{1,2\}
$$

中選擇。

因此目前 evidence 再次顯示：

$$
\boxed{
\text{longer-than-one operator history is not required for the selected predictive quotient}.
}
$$

真正被學到的是 current-source operator 的 predictive redundancy。

---

# 20. APHS 對 Exact Source 有壓縮價值

五個 normal splits 平均：

$$
Bits_{order0}
=
4.7507,
$$

$$
Bits_{order1}
=
4.5432,
$$

$$
Bits_{APHS}
=
4.4241.
$$

因此：

$$
\boxed{
E[
Bits_{order1}
-
Bits_{APHS}
]
=
0.1191.
}
$$

而且：

$$
\boxed{
5/5
}
$$

都有正 gain。

這表示：

$$
\boxed{
\text{exact source operator identity contains compressible predictive redundancy}.
}
$$

這是 APHS 的正結果。

---

# 21. 但 APHS 仍然沒有取代 Atlas

同一批 splits 中，target-side atlas 平均：

$$
Bits_{atlas,dst}
=
4.3047.
$$

因此：

$$
\boxed{
E[
Bits_{APHS}
-
Bits_{atlas,dst}
]
=
0.1194.
}
$$

且：

$$
\boxed{
Atlas
<
APHS
\quad
5/5.
}
$$

所以：

$$
\boxed{
PredictiveHistoryState
\neq
DestinationAtlas.
}
$$

不只是語義不同。

它們在 held-out coding 上也具有不同功能。

---

# 22. APHS + Atlas 有互補，但不能任意疊加

測試 hybrid：

$$
S_t^{pred}
\rightarrow
C_{t+1}^{dst}
\rightarrow
U_{t+1}.
$$

五 split 平均：

$$
Bits_{hybrid}
=
4.4027.
$$

它比 APHS 單獨好：

$$
\boxed{
0.0214
\text{ bits/transition}
}
$$

且：

$$
\boxed{
5/5.
}
$$

但它比：

$$
U_t^{exact}
\rightarrow
C_{t+1}^{dst}
\rightarrow
U_{t+1}
$$

平均更差：

$$
\boxed{
0.0980
\text{ bits/transition}.
}
$$

因此：

$$
\boxed{
\text{more quotient layers}
\not\Rightarrow
\text{better compression}.
}
$$

---

# 23. Source Compression 會丟掉 Target Routing 所需資訊

上節結果的最保守解讀是：

source-side predictive pooling：

$$
U_t
\rightarrow
S_t^{pred}
$$

會丟掉一部分：

$$
U_t
$$

中的細節。

而這些細節仍可能被：

$$
\pi_R^{dst}
$$

的 destination routing 使用。

因此：

$$
\boxed{
\text{source compression}
\neq
\text{free information reduction}.
}
$$

這也是 directional quotient 必須被提出的原因。

---

# 24. Atlas 不應再被想成對稱 Partition

傳統 clustering 直覺常假設一個 mapping：

$$
\pi:
U
\rightarrow
C.
$$

然後 source 和 destination 都使用同一 $\pi$。

但 Phase 0.8 顯示：

$$
U_t
\rightarrow
C_{t+1}
\rightarrow
U_{t+1}
$$

和：

$$
C_t
\rightarrow
U_{t+1}
$$

並不等價。

Normal main：

$$
Bits_{exact-src,target-atlas}
=
4.3278,
$$

$$
Bits_{source-atlas,exact-dst}
=
4.3637.
$$

所以：

$$
\boxed{
\text{quotient usefulness is directional}.
}
$$

---

# 25. Directional Quotient Separation

本文正式定義兩種 quotient。

## 25.1 Source Predictive Quotient

$$
\boxed{
\epsilon_R^{src}:
U_t
\mapsto
S_t^{pred}.
}
$$

它回答：

> 哪些 source operators 對 future distribution 具有可壓縮的 predictive similarity？

## 25.2 Destination Atlas Quotient

$$
\boxed{
\pi_R^{dst}:
U_{t+1}
\mapsto
C_{t+1}^{dst}.
}
$$

它回答：

> 哪些 destination operators 對 transition / emission coding 形成有用的 target grouping？

因此：

$$
\boxed{
\epsilon_R^{src}
\neq
\pi_R^{dst}.
}
$$

---

# 26. Directional Quotient 不是兩個新 Ontology

這兩個 quotient 都是：

$$
\boxed{
\text{derived compression/control views}.
}
$$

它們不是兩個新的「真實心智本體」。

source quotient 可能依 predictive horizon、regime、task 改變。

destination quotient 也可能依 atlas learner、resource、flow role 改變。

所以：

$$
\boxed{
DerivedQuotient
\neq
UltimateOntology.
}
$$

---

# 27. APHS 與 Atlas 有關，但不是同一結構

Main split：

$$
NMI
=
0.4421,
$$

$$
ARI
=
0.0525.
$$

五 split 平均：

$$
E[NMI]
=
0.4359,
$$

$$
E[ARI]
=
0.0347.
$$

200 次 size-preserving atlas-label permutation：

$$
NMI_{obs}
=
0.4421,
$$

$$
E[NMI_{perm}]
=
0.3234,
$$

$$
\boxed{
p
=
0.004975.
}
$$

因此最合理的總結是：

$$
\boxed{
\text{non-random relation}
\land
\text{non-identity}.
}
$$

---

# 28. 為什麼 NMI 高於隨機但 ARI 很低並不矛盾

NMI 回答的是：

> 兩種 partition 是否共享資訊？

ARI 更強調：

> pairwise assignment 是否接近同一 partition？

因此可能：

$$
NMI>Random
$$

同時：

$$
ARI\approx0.
$$

這意味著兩個 quotient 使用了相同底層 transition structure 的某些資訊，但沿不同功能方向切割 operator space。

這正符合 directional quotient interpretation。

---

# 29. Predictive State 不等於 Domain State

一個 predictive state 的最低任務是：

$$
\boxed{
\text{preserve future-relevant information}.
}
$$

一個 domain atlas 的任務則可能同時包含：

- compression；
- routing；
- boundary；
- failure；
- legality；
- interpretation；
- shared-bottom normalization；
- control-plane aggregation。

所以：

$$
\boxed{
PredictiveSufficiency
\not\Rightarrow
DomainSufficiency.
}
$$

---

# 30. Computational Mechanics 的正確位置

Shalizi 與 Crutchfield 的 computational mechanics 將對完整 future 具有相同 conditional distribution 的 pasts 視為 causal-state equivalence classes，並研究其 predictive sufficiency、minimality 與 uniqueness。

這對 CODT 提供一個強方法學種子：

$$
\boxed{
\text{history identity can be replaced by predictive equivalence}.
}
$$

但 CODT-06 不宣稱 APHS 是 epsilon-machine reconstruction。

原因：

1. history 有限；
2. future horizon 有限；
3. data 有限；
4. equivalence approximate；
5. clustering procedure 不同；
6. cognition 還有 action、World、license、domain boundary 等額外結構。

所以：

$$
\boxed{
APHS
\neq
CausalState.
}
$$

---

# 31. Predictive State Representation 的正確位置

Littman、Sutton、Singh 的 Predictive Representations of State 強調：state 可以用對 future observations、尤其 action-conditional future tests 的 predictions 表示，而不必依賴特權 latent-state ontology。

這對 CODT 的後續 World coupling 很重要。

但 CODT-06 尚未進入 action-conditioned World observations。

因此目前只有：

$$
\boxed{
\text{operator-sequence predictive state candidate}.
}
$$

不是完整 PSR。

---

# 32. Variable-Length Markov 的正確位置

Buhlmann-Wyner 類 variable-length Markov framework 提醒：

$$
\boxed{
\text{different histories may require different effective context lengths}.
}
$$

Phase 0.8 已把這個方法學種子轉成有限 context-tree probe。

結果沒有支持 longer context。

這不是 external theory 被反證。

它只表示：

> 目前 CDD synthetic operator traces 不需要靠更長 context 才得到較好的 MDL explanation。

---

# 33. History Compression 與 Atlas Compression 是兩種不同壓縮

source predictive quotient：

$$
\epsilon_R^{src}
$$

壓縮的是：

$$
\text{history / source distinctions}.
$$

atlas quotient：

$$
\pi_R^{dst}
$$

壓縮的是：

$$
\text{destination distinctions}.
$$

因此可寫：

$$
\boxed{
Compression
=
Compression_{history/source}
+
Compression_{destination/atlas}
+
Residual.
}
$$

這不是一般數值恆等式。

而是 compression ledger candidate。

---

# 34. Residual Atlas Principle

若在最佳 history model 已固定後，atlas仍能降低 held-out description length，則：

$$
\boxed{
ResidualAtlasValue>0.
}
$$

這表示 atlas 不是當前 history model 的純替代物。

Phase 0.8 normal splits：

$$
\boxed{
ResidualAtlasValue>0
\quad5/5.
}
$$

因此 CODT-06 把 residual value 納入 future domain evidence。

---

# 35. Residual History Principle

反過來，如果 atlas 已固定，history conditioning 仍降低 code length，則：

$$
\boxed{
ResidualHistoryValue>0.
}
$$

所以：

$$
\boxed{
History
\text{ and }
Atlas
\text{ can be jointly non-redundant}.
}
$$

不必選一個當「真正 state」。

---

# 36. History-Atlas Substitution Surface

可以建立：

$$
L(k,K)
$$

其中：

- $k$：history order / effective history complexity；
- $K$：atlas complexity / cluster count。

若：

$$
K^*(k)
$$

隨 $k$ 增加明顯下降，代表 temporal grammar 和 spatial atlas 有 substitutability。

Phase 0.8 沒看到這種強現象。

因此目前：

$$
\boxed{
\text{temporal complexity}
\not\approx
\text{atlas complexity substitute}
}
$$

在 frozen synthetic runtime 下成立。

---

# 37. History 不應被 Atlas 回寫

若新的 predictive state model 把：

$$
h_1,h_2
$$

合併成：

$$
S^{pred},
$$

canonical history 仍必須保留：

$$
h_1,h_2.
$$

不能把舊 trace 重寫成：

> 過去只有一個 predictive state。

所以：

$$
\boxed{
PredictiveQuotient
\neq
HistoryRewrite.
}
$$

這延續 CODT-02 / 05。

---

# 38. History View、Flow View、Atlas View

對同一 canonical trace，可同時產生三個 derived views。

## History View

$$
H_t
$$

保留 ordered event sequence。

## Flow View

$$
P_t
$$

估計 transition dynamics。

## Atlas View

$$
\mathcal A_t
$$

形成 quasi-stable structural chart。

因此：

$$
\boxed{
OneTrace
\rightarrow
MultipleDerivedViews.
}
$$

Derived views 不互相覆寫 canonical evidence。

---

# 39. OOD：Predictive Quotient 不是 Universal State

Phase 0.9 將 normal-selected APHS zero-shot 轉移到 OOD artifact traces。

結果：

$$
Bits_{order1}
=
4.2411,
$$

$$
Bits_{APHS}
=
4.3313,
$$

$$
Bits_{atlas,dst}
=
4.2947,
$$

$$
Bits_{hybrid}
=
4.4088.
$$

OOD 下 exact order-1 flow 最好。

因此：

$$
\boxed{
\text{normal predictive quotient}
\not\Rightarrow
\text{regime-universal predictive state}.
}
$$

---

# 40. OOD 結果再次指向 Missing State，而非 Missing History

如果增加 history 沒有改善 OOD，normal predictive quotient 也不能 transfer，則下一個合理缺項是：

$$
S_t^{world/runtime}.
$$

也就是：

$$
P(
U_{t+1}
\mid
U_t,
S_t^{world/runtime},
R_t
).
$$

這不代表 World state 一定能解決。

但它比：

$$
\boxed{
\text{blindly increase }k
}
$$

更值得測。

這正是 CODT-07 的入口。

---

# 41. History-Flow-Atlas Separation v0.2

綜合 Phase 0.8-0.9，本文將 runtime 寫成：

$$
\boxed{
CognitiveRuntime_t
=
(
H_t,
P_R,
\epsilon_R^{src},
\pi_R^{dst},
\mathcal A_t
).
}
$$

其中：

- $H_t$：ordered canonical history；
- $P_R$：regime-conditioned transition flow；
- $\epsilon_R^{src}$：source predictive quotient；
- $\pi_R^{dst}$：destination atlas quotient；
- $\mathcal A_t$：atlas version / domain chart。

五者目前不能互相消去。

---

# 42. 為什麼 $\pi_R^{dst}$ 和 $\mathcal A_t$ 都保留？

 $\mathcal A_t$ 是整體 domain chart。

 $\pi_R^{dst}$ 是 chart 在 destination prediction interface 上的具體 quotient use。

因此：

$$
\boxed{
AtlasObject
\neq
AtlasUseInterface.
}
$$

同一 atlas 未來可能有：

- destination coding quotient；
- routing quotient；
- visualization view；
- failure aggregation view；
- World-interface view。

這些 use interfaces 不應和 atlas object 本身混同。

---

# 43. Source / Destination 非對稱性的更一般形式

對 transition：

$$
U_t
\rightarrow
U_{t+1},
$$

source 和 destination 扮演不同 causal / predictive roles。

因此可以一般化為：

$$
\boxed{
Q_R^{src}
\neq
Q_R^{dst}.
}
$$

其中：

$$
Q_R^{src}
$$

負責 source information compression。

$$
Q_R^{dst}
$$

負責 destination information compression。

APHS 與 target atlas 只是目前的兩個具體 candidate。

---

# 44. Directional Domain Geometry

這意味著 domain geometry 不必只有：

$$
\text{node partition}.
$$

它還可能具有：

$$
\boxed{
\text{source geometry}
+
\text{destination geometry}
+
\text{edge-role geometry}.
}
$$

這是 CODT 從普通 clustering theory 再往前的一步。

---

# 45. Predictive Quotient 與 Domain Boundary

若兩個 operators 在 source predictive quotient 中被合併，仍可能位於不同 domain boundaries。

反之，同一 domain 中的兩個 operators 也可能因對 future routing 影響不同而不能被 predictive quotient 合併。

因此：

$$
\boxed{
PredictiveEquivalence
\neq
DomainEquivalence.
}
$$

---

# 46. Predictive Sufficiency 不是 Epistemic License

就算：

$$
S_t^{pred}
$$

對 next-step prediction 足夠，也不代表：

- 它足以 certification；
- 它足以 causal explanation；
- 它足以 World action；
- 它足以 preserve provenance。

所以：

$$
\boxed{
PredictiveSufficiency
\neq
EpistemicAuthority.
}
$$

這延續 CODT-02 的 license separation。

---

# 47. Temporal Grammar 的 Promotion Gate

若未來要宣稱真正 higher-order cognitive grammar，至少需要：

## HG1. Held-Out Gain

$$
k>1
$$

在 held-out data 有穩定正 gain。

## HG2. Complexity-Adjusted Gain

gain 足以支付 history-model complexity。

## HG3. Multi-Session Stability

不只單一 synthetic seed。

## HG4. State-Controlled Gain

排除 omitted World/runtime state。

## HG5. Cross-Agent / Human Evidence

最終需要 external traces。

因此：

$$
\boxed{
LongHistory
\text{ is a hypothesis, not a default ontology}.
}
$$

---

# 48. Predictive-State Promotion Gate

一個 predictive quotient 要被提升為更強 state candidate，至少需要：

- held-out predictive value；
- complexity-adjusted compression；
- cross-regime transfer 或明確 bounded regime scope；
- stable state mapping；
- calibration；
- observable-state grounding；
- action-conditional testing for World-coupled claims。

Phase 0.9 APHS 尚未通過這些外部 gate。

所以：

$$
\boxed{
APHS
=
Candidate,
\quad
not
domain-promotion.
}
$$

---

# 49. History Complexity 與 Cognitive Complexity

一個 sequence 需要更長 history 才能預測，不等於 cognition 更「高級」。

反過來，一個短-memory predictive state 也不等於 cognition 簡單。

所以：

$$
\boxed{
TemporalMemoryComplexity
\neq
GeneralCognitiveComplexity.
}
$$

這避免把 Markov order 當成智慧尺度。

---

# 50. Atlas Complexity 與 Intelligence 也不能等同

更多 domains 不代表更聰明。

更少 domains 也不代表更低級。

一個好的 representation 可能用更少 chart complexity 表示更多 useful structure。

所以：

$$
\boxed{
AtlasComplexity
\neq
Intelligence.
}
$$

---

# 51. History Retention 與 Runtime Compression

canonical system 可以完整保留：

$$
H_t,
$$

同時 runtime 使用 compressed predictive state：

$$
S_t^{pred}.
$$

因此：

$$
\boxed{
StorageHistory
\neq
ActivePredictiveState.
}
$$

這對 AI memory architecture 很重要。

完整 history 可以保留 provenance。

active state 則可以只保留 future-relevant compression。

---

# 52. Memory Compression 不應刪除責任鏈

若 predictive compression 把多個 histories 合併，仍必須可以回查：

$$
S_t^{pred}
\rightarrow
\{h_i\text{ refs}\}.
$$

否則：

- audit；
- responsibility；
- rollback；
- error reconstruction；

會失效。

因此：

$$
\boxed{
PredictiveCompression
\neq
ProvenanceErasure.
}
$$

---

# 53. History Fork

若 cognition 分支：

$$
H_t
\rightarrow
H_{t+1}^{(a)},
H_{t+1}^{(b)},
$$

不同 branches 可以暫時共享：

$$
S_t^{pred},
$$

但 history identity 仍不同。

所以：

$$
\boxed{
SamePredictiveState
\not\Rightarrow
SameHistory.
}
$$

這對 counterfactual / planning 特別重要。

---

# 54. Same History 也不保證 Same Predictive State Across Regimes

若：

$$
R_a
\neq
R_b,
$$

即使 raw operator history 相同：

$$
h_t^{(a)}
=
h_t^{(b)},
$$

也可能：

$$
P(
Future
\mid
h_t,R_a
)
\neq
P(
Future
\mid
h_t,R_b
).
$$

因此：

$$
\boxed{
PredictiveState
=
PredictiveState(history,regime,state).
}
$$

這再次指向 CODT-07。

---

# 55. History-Flow-Atlas Ledger

本文建議 runtime 分帳：

$$
\boxed{
Ledger_t
=
(
HistoryLedger_t,
FlowLedger_t,
PredictiveStateLedger_t,
AtlasLedger_t
).
}
$$

每個 ledger 各自版本化。

這可以避免：

- predictive state update 被誤記成 history rewrite；
- flow retraining 被誤記成 domain shift；
- atlas rechart 被誤記成 canonical operator change。

---

# 56. AI-Native Runtime 的實作含義

一個 AI runtime 不應把 conversation history 全部直接塞進 active state，也不應因 token window 擴大就假設 predictive state改善。

更合理的是：

$$
HistoryStore
\rightarrow
PredictiveCompression
\rightarrow
ActiveState
\rightarrow
FlowModel
\rightarrow
AtlasControl.
$$

同時：

$$
HistoryStore
$$

保持可回溯。

這使：

$$
\boxed{
LongContextWindow
\neq
GoodCognitiveState.
}
$$

---

# 57. CODT-06 憲法增補

## CODT-C43：History-Flow Separation

$$
\boxed{
History
\neq
Flow.
}
$$

## CODT-C44：History-Atlas Separation

$$
\boxed{
History
\neq
Atlas.
}
$$

## CODT-C45：Markov-Depth Separation

$$
\boxed{
MarkovOrder
\neq
CognitiveDepth.
}
$$

## CODT-C46：Residual Atlas Test

atlas claim 應在 best available history control 後測 residual value。

## CODT-C47：Predictive / Domain Equivalence Separation

$$
\boxed{
PredictiveEquivalence
\neq
DomainEquivalence.
}
$$

## CODT-C48：Directional Quotient Separation

$$
\boxed{
\epsilon_R^{src}
\neq
\pi_R^{dst}.
}
$$

## CODT-C49：Predictive Compression Non-Rewriting

$$
\boxed{
PredictiveCompression
\neq
HistoryRewrite.
}
$$

## CODT-C50：Regime-Conditioned Predictive State

predictive state 不預設跨 regime universal。

---

# 58. 本文的理論地位

本文沒有證明：

$$
\boxed{
\text{all cognition has only one-step memory}.
}
$$

也沒有證明：

$$
\boxed{
APHS
\text{ is a true cognitive state ontology}.
}
$$

本文真正建立的是：

$$
\boxed{
\text{history complexity, flow dynamics, predictive quotient, and atlas structure must be separately modeled.}
}
$$

這是一條 theory-design constraint。

---

# 59. 與下一篇的接口

Phase 0.8-0.9 的兩輪負結果都把問題推向同一方向。

增加 operator history 沒有解決 OOD。

normal predictive quotient 也不能 universal transfer。

所以接下來要問：

> 我們缺的是不是 history 外的 observer/runtime state？

也就是：

$$
S_t^{obs},
$$

$$
S_t^{pred},
$$

以及：

$$
\pi_R^{dst}.
$$

它們是否應再分開？

CODT-07 將正式提出：

$$
\boxed{
ObservableState
\neq
PredictiveState
\neq
Atlas.
}
$$

也就是 OPAS。

---

# 結論

CODT-06 的問題起點是：

> Cognitive Atlas 會不會只是低階 flow model 看不到長 history 所產生的假空間？

目前 synthetic evidence 的答案是：

$$
\boxed{
\text{沒有支持這個強版本。}
}
$$

一階 history 有資訊。

但二階以上 fixed history 在五個 normal splits 全部惡化。

variable-order history tree 也全部退回 root。

更重要的是，即使 $U_t$ 已知，target-side atlas 仍保有約：

$$
0.1920
\text{ bits/transition}
$$

的平均 residual value。

所以：

$$
\boxed{
Atlas
\neq
MissingHistoryArtifact.
}
$$

Phase 0.9 再把問題推進一步。

APHS 證明 source identity 中確實存在 predictive redundancy。

但 APHS 仍沒有取代 target-side atlas。

兩者：

$$
\boxed{
\text{non-randomly related}
}
$$

同時：

$$
\boxed{
\text{not the same partition}.
}
$$

這迫使 CODT 放棄「一張對稱 domain map 解釋所有 transition positions」的直覺。

目前更合理的是：

$$
\boxed{
\epsilon_R^{src}
\neq
\pi_R^{dst}.
}
$$

source 端按 predictive similarity 壓縮。

destination 端按 atlas routing / emission usefulness 壓縮。

兩者不能自由互換。

所以認知 runtime 的成熟版本不應只問：

> 這個 operator 屬於哪個 domain？

而要問：

> 這段 history 是什麼？目前 flow law 是什麼？source information 應如何壓縮？destination structure 應如何 quotient？atlas 在什麼版本與 regime 下有效？

因此本文真正固定的是：

$$
\boxed{
History
\neq
Flow
\neq
PredictiveState
\neq
AtlasUse.
}
$$

下一步才有資格把 World / Runtime state 拉進來。

---

# 參考文獻與外部研究種子

## A. Temporal Models / Context

1. Rissanen, J. (1983). "A Universal Data Compression System." *IEEE Transactions on Information Theory*, 29(5), 656-664.
2. Willems, F. M. J., Shtarkov, Y. M., & Tjalkens, T. J. (1995). "The Context-Tree Weighting Method: Basic Properties." *IEEE Transactions on Information Theory*, 41(3), 653-664.
3. Buhlmann, P., & Wyner, A. J. (1999). "Variable Length Markov Chains." *The Annals of Statistics*, 27(2), 480-513. DOI: 10.1214/aos/1018031204.

## B. Predictive-State / Computational Mechanics

4. Shalizi, C. R., & Crutchfield, J. P. (2001). "Computational Mechanics: Pattern and Prediction, Structure and Simplicity." *Journal of Statistical Physics*, 104, 817-879. DOI: 10.1023/A:1010388907793.
5. Shalizi, C. R., Shalizi, K. L., & Crutchfield, J. P. (2002). "An Algorithm for Pattern Discovery in Time Series." Technical / conference-era computational-mechanics work on causal-state reconstruction.
6. Littman, M. L., Sutton, R. S., & Singh, S. (2001). "Predictive Representations of State." *Advances in Neural Information Processing Systems 14*.

**邊界聲明：** 上述研究提供 variable memory、predictive equivalence、causal-state minimality 與 predictive-state representation 的外部方法學參照。CODT 的 APHS、Directional Quotient Separation、History-Flow-Atlas Separation 與 target-side atlas 並不宣稱等同上述任何標準模型。

## C. 內部理論來源

1. CODT-01〈從認知方法到認知算子：認知解構學的域化轉向〉。
2. CODT-02〈認知算子代數與相對原子性〉。
3. CODT-03〈認知域的生成：域不是分類名稱，而是算子閉包與操作生態〉。
4. CODT-04〈共享底層認知域：Shared-Bottom Cognitive Runtime〉。
5. CODT-05〈認知域不是固定分類：Flow-Atlas Separation〉。
6. CDD Phase 0 v0.8：Higher-Order Cognitive Grammar / Directional Quotient experiments。
7. CDD Phase 0 v0.9：Approximate Predictive History States / Directional Quotient Separation。
8. CDD Phase 0 v0.7：MDL Atlas。
9. GCORF / HSO / MWT SourcePacks。

---

# 版本記錄

## v1.0

- 正式建立 History-Flow-Atlas Separation。
- 定義 operator history、fixed-order flow、variable-order history 與 predictive-equivalence state 的分離。
- 納入 Phase 0.8 higher-order grammar falsification： $k\ge2$ 在五個 normal splits 全部惡化。
- 固定 residual atlas test：exact source 已知後 atlas 仍保有 predictive/compressive value。
- 納入 APHS：source predictive quotient 可壓縮 exact source redundancy。
- 固定 APHS 不等於 atlas、predictive equivalence 不等於 domain equivalence。
- 正式提出 Directional Quotient Separation： $\epsilon_R^{src}\neq\pi_R^{dst}$。
- 納入 APHS / Atlas 的 non-random relation + non-identity 結果。
- 固定 predictive compression 不得回寫 canonical history。
- 保留 OOD zero-shot negative result，拒絕 regime-universal predictive-state 強宣告。
- 為 CODT-07 OPAS / World-Runtime State interface 建立 history-side基礎。
