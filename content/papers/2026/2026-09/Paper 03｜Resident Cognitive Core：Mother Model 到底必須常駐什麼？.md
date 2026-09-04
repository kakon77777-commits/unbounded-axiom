# Paper 03｜Resident Cognitive Core：Mother Model 到底必須常駐什麼？

**English Title:** *The Resident Cognitive Core: What Must a Mother Model Keep Resident?*  
**系列：**《可展開認知核心：從 MoE、認知密度到 Mother AI 的模型架構命題》  
**作者：** Neo.K × Aletheia  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-08-28  
**文件性質：** 公開命題論文／Mother Model、認知核心與能力外置邊界研究

---

## 摘要

本文提出 **Resident Cognitive Core Hypothesis（常駐認知核心命題）**。若未來 Mother AI、Cognitive Command Tower 或其他高階協調智能可以透過網路、資料庫、外部記憶、Sub-AI、Mixture-of-Experts、工具與推理時資源按需取得大量能力，那麼模型設計的關鍵問題將不再只是「模型應該知道多少」，而是：

> **哪些能力若不常駐於核心，整個智能系統便失去可靠理解、判斷、驗證、委派與自我修正的能力？**

本文承接既有「後設完備、基底稠密、表層稀疏」與「壓縮全局智能」研究，但把問題從 Mother AI Runtime 層推進至模型功能配置層。本文反對兩個極端：第一，將 Mother Model 設計為只保存 Agent 名單、價格、工具描述與路由規則的空殼 router；第二，要求 Mother Model 常駐所有領域的高解析度文件、案例、最新事實與專門執行細節。前者缺乏足夠認知基底以治理強外部智能，後者則重新把全部世界壓回單一模型，失去外部展開、條件計算與更新彈性的意義。

本文將第一代 Resident Cognitive Core 形式化為：

$$
\boxed{
K_R
=
(
B_I,
B_R,
B_E,
B_M,
B_W,
B_C,
B_G
)
}
$$

其中：

- $B_I$：Interpretive Basis，基本理解與表示基底；
- $B_R$：Reasoning Basis，推理與因果操作基底；
- $B_E$：Epistemic Basis，已知／未知／證據／衝突／信心基底；
- $B_M$：Meta-Cognitive Basis，策略選擇、自我檢查、失敗辨識與能力邊界判斷；
- $B_W$：Minimum Sufficient World Basis，最小充分世界基底；
- $B_C$：Coordination Basis，工具、Agent、模型與資源協調基底；
- $B_G$：Governance Basis，權限、驗證、風險與不可逆行動治理基底。

本文提出「Resident Necessity」不應以單一知識類別決定，而應根據功能中心性、使用頻率、延遲敏感性、替代可得性、外部依賴風險、驗證必要性與錯誤傳播半徑共同決定。對某能力 $z$，可定義：

$$
\boxed{
N_R(z)
=
f(
H_z,
F_z,
L_z,
S_z,
V_z,
D_z,
R_z
)
}
$$

其中 $H_z$ 表示全局功能中心性， $F_z$ 表示高頻性， $L_z$ 表示低延遲需求， $S_z$ 表示外部替代難度， $V_z$ 表示驗證與治理價值， $D_z$ 表示外部依賴風險， $R_z$ 表示錯誤向下游擴散的風險。

本文進一步區分三種能力位置：

$$
\boxed{
\text{Resident}
}
$$

$$
\boxed{
\text{Conditionally Activated}
}
$$

$$
\boxed{
\text{Externally Expanded}
}
$$

並提出：高頻、全局、高中心性、治理關鍵且難以由外部結果反向驗證的能力，更適合常駐；低頻、高解析度、快速變動、可檢索、可重建、可機械驗證或可由專門系統高品質提供的能力，更適合條件激活或外部展開。

本文同時強調，這是一個**功能架構命題，而不是 weight-level partition 已被解決的主張**。知識、語言、世界表示、推理與元認知在現有 Transformer 中高度糾纏。Knowledge Neurons、ROME、causal tracing 與後續研究雖提供部分局部化與因果干預證據，但「找到某個知識相關位置」不等於已能將認知功能乾淨抽離；甚至 localization 與 editability 之間也未必具有簡單對應。因此本文只定義「什麼值得常駐」與「如何證偽這個分類」，不公開也不假定已掌握真正的參數級分離方法。

本文最後提出十三項主要命題、十二類失敗模式與九組可否證實驗。若未來實驗顯示：高階認知能力無法在降低 resident surface knowledge 後維持；較小 resident core 無法可靠治理更強外部模型；外部展開的延遲、錯誤與整合成本長期壓倒其收益；或者不存在任何穩定的 Minimum Sufficient World Basis，則 Resident Cognitive Core 命題應被削弱，甚至退回較大型單體模型架構。

本文的核心問題不是：

> 「模型可以刪掉多少知識？」

而是：

$$
\boxed{
\text{What must intelligence never have to ask permission to remember how to do?}
}
$$

也就是：

> **一個作為認知指揮塔的智能，哪些能力必須在任何外部服務不可用、資料不足或其他模型回答錯誤時，仍然留在自己身上？**

**關鍵詞：** Resident Cognitive Core、Mother Model、Minimum Sufficient World Basis、Meta-Cognition、Epistemic Control、Cognitive Density、Externalization、Mixture-of-Experts、Sub-AI、Cognitive Command Tower

---

# 0. 研究定位

Paper 01 提出：

$$
\boxed{
\text{Scaling}
\rightarrow
\text{Compute Allocation Problem}.
}
$$

Paper 02 再提出：

$$
\boxed{
\text{Cognitive Density}
}
$$

作為衡量 resident、conditional、external 與 verification cost 的多維量測框架。

Paper 03 現在處理更核心的設計問題：

$$
\boxed{
\text{What must remain resident?}
}
$$

如果這個問題沒有答案，後續：

- MoE；
- external expert；
- retrieval；
- Sub-AI；
- model routing；
- cognitive factorization；

都只是在做工程拼接。

因為系統不知道：

> 哪些東西可以出去？

以及：

> 哪些東西一旦出去，Mother AI 就失去成為 Mother AI 的資格？

---

# 1. 兩個錯誤極端

## 1.1 空殼 Router

第一個極端：

$$
A_0
=
(
\text{model registry},
\text{prices},
\text{tools},
\text{rules}
).
$$

它能：

$$
q
\rightarrow
\operatorname{Route}(q)
\rightarrow
M_j(q),
$$

但如果缺乏足夠世界與認知基底，就未必能：

- 發現問題被錯誤表述；
- 發現外部模型偷換前提；
- 知道應不應該相信答案；
- 發現 scale mismatch；
- 辨識未見任務；
- 建立新的 verifier；
- 知道何時應升級；
- 知道何時應拒絕。

因此：

$$
\boxed{
\text{Routing Capability}
\neq
\text{Cognitive Authority}.
}
$$

---

## 1.2 單體全知

另一個極端：

$$
\mathcal K_R
\approx
\bigcup_{d\in\mathcal D}
\mathcal K_d.
$$

也就是：

> 所有領域、文件、事實、版本、案例、知識與執行細節全部常駐模型。

這會帶來：

- 模型容量膨脹；
- 訓練與更新成本；
- 資訊過時；
- 長尾知識維護；
- 互相干擾；
- 每次推理的不必要成本；
- 單點退化風險。

因此：

$$
\boxed{
\text{Cognitive Authority}
\neq
\text{Encyclopedic Residency}.
}
$$

---

# 2. 第三條路：後設完備、基底稠密、表層稀疏

既有 CACBH 提出：

$$
\boxed{
A_0
=
A_{\mathrm{meta}}
\oplus
A_{\mathrm{basis}}
\oplus
A_{\mathrm{surface}}.
}
$$

其中理想方向是：

$$
\operatorname{MC}(A_0)\uparrow,
$$

$$
D_{\mathrm{basis}}(A_0)\uparrow,
$$

但：

$$
|\mathcal S_{\mathrm{resident}}|
\ll
|\mathcal S_{\mathrm{world}}|.
$$

這不是要求模型「少懂」。

而是區分：

$$
\boxed{
\text{生成理解世界的基底}
}
$$

與：

$$
\boxed{
\text{世界的全部高解析度投影}.
}
$$

---

# 3. Resident Core 的第一個必要條件：理解不是外包結果

如果 Mother AI 遇到任何輸入都必須先問另一個模型：

> 「這是什麼意思？」

那麼：

$$
\text{Interpretation}
$$

已經不再由 Mother AI 持有。

此時外部模型不只是 worker。

它變成了：

$$
\boxed{
\text{epistemic gatekeeper}.
}
$$

因此至少需要一個：

$$
B_I
$$

Interpretive Basis。

它不要求懂所有領域。

但必須足以：

- 解析問題結構；
- 區分陳述、命令、假設與疑問；
- 辨識角色與關係；
- 維持基本時序；
- 辨識約束；
- 發現歧義；
- 將未知標記為未知。

---

# 4. Interpretive Basis

定義：

$$
\boxed{
B_I
=
(
L,
R,
T,
C,
A
)
}
$$

其中：

- $L$：language / representation；
- $R$：relation representation；
- $T$：temporal structure；
- $C$：constraint recognition；
- $A$：ambiguity handling。

這不是完整語言學理論。

它是 Mother Model 的最低接口能力。

如果：

$$
B_I
$$

不足，

則：

$$
\boxed{
\text{Mother AI 無法知道自己正在處理什麼。}
}
$$

---

# 5. Reasoning Basis

第二個核心：

$$
B_R.
$$

本文不要求 resident core 具有所有專門數學、法律、物理與 coding 能力。

但它至少需要可重用的基本推理操作：

$$
\boxed{
B_R
=
\{
\mathsf{Compare},
\mathsf{Compose},
\mathsf{Decompose},
\mathsf{Cause},
\mathsf{Constraint},
\mathsf{Counterfactual},
\mathsf{Invariant},
\mathsf{Contradict},
\mathsf{Generalize},
\mathsf{Specialize}
\}.
}
$$

否則外部模型給出兩個互相矛盾的答案時，

Mother AI 只能：

$$
\text{vote}.
$$

而不能：

$$
\text{reason}.
$$

---

# 6. 為什麼 Reasoning 不能全部外包？

假設：

$$
M
$$

永遠把推理交給：

$$
E.
$$

則：

$$
M(q)=E(q).
$$

如果 $M$ 自己沒有足夠 reasoning basis，

它無法知道：

$$
E(q)
$$

是否違反：

- 前提；
- 因果方向；
- 基本約束；
- 邏輯一致性；
- 已知不變量。

此時：

$$
\boxed{
\text{External Reasoner}
\rightarrow
\text{de facto cognitive sovereign}.
}
$$

因此 Mother AI 可以外包：

$$
\text{deep reasoning execution},
$$

但不能完全外包：

$$
\boxed{
\text{reasoning admissibility judgment}.
}
$$

---

# 7. Epistemic Basis

第三個核心：

$$
B_E.
$$

本文把 epistemic competence 定義為：

$$
\boxed{
B_E
=
(
K,
U,
E,
C,
P,
R
)
}
$$

其中：

- $K$：known；
- $U$：unknown；
- $E$：evidence；
- $C$：contested；
- $P$：speculative；
- $R$：retracted / rejected。

Mother AI 必須能區分：

$$
\boxed{
\text{I have an answer}
}
$$

與：

$$
\boxed{
\text{I have evidence}.
}
$$

也要區分：

$$
\boxed{
\text{No evidence found}
}
$$

與：

$$
\boxed{
\text{False}.
}
$$

---

# 8. Unknown 是核心資料型別

如果系統內沒有：

$$
U
$$

Unknown，

它會被迫把每個問題映射成：

$$
\{\text{true},\text{false}\}.
$$

這會造成：

- 幻覺；
- 虛假確定性；
- 錯誤路由；
- 錯誤 writeback；
- 無法主動搜尋。

因此：

$$
\boxed{
\text{Unknown Recognition}
}
$$

不是額外 safety feature。

它是 Mother AI 的 resident epistemic primitive。

---

# 9. Meta-Cognitive Basis

第四個核心：

$$
B_M.
$$

本文定義：

$$
\boxed{
B_M
=
\{
\mathsf{SelfCheck},
\mathsf{EstimateDifficulty},
\mathsf{EstimateConfidence},
\mathsf{DetectFailure},
\mathsf{SelectStrategy},
\mathsf{Stop},
\mathsf{Retry},
\mathsf{Escalate},
\mathsf{Delegate},
\mathsf{Ask}
\}.
}
$$

這些能力共同回答：

> 我現在應該怎麼想？

而不是：

> 這個問題的內容答案是什麼？

---

# 10. Mother AI 可以局部比 Sub-AI 弱

本文不要求：

$$
\forall i,
\quad
\mathcal C_M
\supseteq
\mathcal C_i.
$$

可以存在：

$$
\mathcal C_i-\mathcal C_M
\neq
\varnothing.
$$

例如：

$$
C_{\mathrm{math}}(A_i)
>
C_{\mathrm{math}}(M).
$$

只要 $M$ 能：

1. 知道這是一個數學問題；
2. 知道自己可能不足；
3. 選擇 $A_i$ ；
4. 建立輸入；
5. 選擇 verifier；
6. 判斷何時升級。

那麼：

$$
\boxed{
\text{Mother Strength}
\neq
\text{Local Maximum Capability}.
}
$$

---

# 11. 但是 Meta-Cognition 有最低閾值

壓縮全局智能的舊命題可改寫為：

$$
\boxed{
\min_{c\in\mathcal C_{\mathrm{critical}}}
\operatorname{Competence}(M,c)
\ge
\theta_c.
}
$$

若：

$$
\operatorname{Competence}(M,c)
<
\theta_c
$$

對某個關鍵能力成立，

則增加：

$$
N_{\mathrm{external}}
$$

不一定改善系統。

甚至可能：

$$
\boxed{
\text{More External Intelligence}
\rightarrow
\text{More Unrecognized Error}.
}
$$

---

# 12. Minimum Sufficient World Basis

只保留 meta-cognition 仍不夠。

如果 Mother AI 對世界近乎空白，

它無法：

- 形成問題；
- 判斷來源合理性；
- 生成搜尋查詢；
- 建立基本類比；
- 偵測物理不可能；
- 理解人類制度；
- 判斷工具輸出。

因此需要：

$$
\boxed{
B_W
=
\text{Minimum Sufficient World Basis}.
}
$$

---

# 13. 世界基底不是百科全書

本文不定義：

$$
B_W
=
\text{Wikipedia}.
$$

更接近：

$$
\boxed{
B_W
=
(
\mathcal O,
\mathcal R,
\mathcal C,
\mathcal I,
\mathcal S
)
}
$$

其中：

- $\mathcal O$：基本 object / entity notions；
- $\mathcal R$：relations；
- $\mathcal C$：causal patterns；
- $\mathcal I$：invariants / constraints；
- $\mathcal S$：scale / temporal structure。

它更像：

$$
\boxed{
\text{world-generative basis}
}
$$

而不是：

$$
\boxed{
\text{world-document archive}.
}
$$

---

# 14. Minimum Sufficient 的形式

對任務分布：

$$
\mathcal T,
$$

尋找：

$$
\boxed{
B_W^\ast
=
\arg\min_{B_W}
\operatorname{Cost}(B_W)
}
$$

subject to：

$$
Q_C(
B_I,
B_R,
B_E,
B_M,
B_W
\mid
\mathcal T
)
\ge
\theta_C.
$$

這表示：

> 世界基底應足夠小，但不能小到讓核心失去理解與治理能力。

---

# 15. Minimum 不等於 Fixed

今天的：

$$
B_W^\ast(t)
$$

不必等於：

$$
B_W^\ast(t+\Delta t).
$$

新的：

- 科學概念；
- 技術基礎；
- 社會制度；
- AI 工具；
- 安全風險；

可能改變：

$$
B_W.
$$

因此：

$$
\boxed{
\text{Resident Core}
\neq
\text{Immutable Core}.
}
$$

核心應可更新，

但更新比外部表層知識更慎重。

---

# 16. Coordination Basis

第五個核心：

$$
B_C.
$$

Mother AI 若要成為 Cognitive Command Tower，

至少需要表示：

$$
\boxed{
B_C
=
(
\text{task},
\text{role},
\text{capability},
\text{cost},
\text{latency},
\text{authority},
\text{dependency},
\text{evidence}
).
}
$$

這不是記住每個模型的全部 benchmark。

而是知道：

> 什麼樣的能力可以被誰、用什麼條件、在什麼成本與風險下提供。

---

# 17. Role 必須與 Model 分離

定義 role：

$$
r.
$$

execution instance：

$$
A_i.
$$

則：

$$
\boxed{
r
\neq
A_i.
}
$$

同一角色可以由：

$$
A_i
\rightarrow
A_j
$$

替換。

因此 Resident Core 應常駐：

$$
\text{role semantics}
$$

與：

$$
\text{capability requirements},
$$

而不是把：

$$
\text{某一個 vendor model}
$$

硬寫成認知本體。

---

# 18. Governance Basis

第六個不可忽略核心：

$$
B_G.
$$

Mother AI 若可以委派外部智能，

至少必須知道：

- 什麼可以讀；
- 什麼可以寫；
- 什麼只能產生 candidate；
- 什麼需要 verifier；
- 什麼不可逆；
- 什麼要人工批准；
- 什麼資訊不能送往外部 provider。

形式化：

$$
\boxed{
B_G
=
(
\Gamma,
V,
A,
P,
R
)
}
$$

其中：

- $\Gamma$：authority；
- $V$：verification；
- $A$：acceptance；
- $P$：privacy / policy；
- $R$：risk。

---

# 19. 為什麼 Governance 也是認知核心？

因為：

$$
\text{Can}
$$

與：

$$
\text{Should}
$$

不是同一個問題。

如果外部模型說：

> 我可以修改 production database。

Mother AI 不能把：

$$
\text{capability claim}
$$

直接轉成：

$$
\text{authority grant}.
$$

因此：

$$
\boxed{
\text{Capability}
\neq
\text{Authority}.
}
$$

這個區分必須存在於 resident governance basis。

---

# 20. Resident Cognitive Core 的七元組

綜合以上：

$$
\boxed{
K_R
=
(
B_I,
B_R,
B_E,
B_M,
B_W,
B_C,
B_G
).
}
$$

其中每一項都不是固定模組名稱。

它們是：

$$
\boxed{
\text{functional obligations}.
}
$$

未來實作可能由：

- neural circuits；
- dense backbone；
- shared experts；
- recurrent state；
- symbolic structure；
- hybrid runtime；

共同提供。

---

# 21. 為什麼不能直接說「Shared Expert = Core」？

DeepSeekMoE 類架構引入 shared experts，

其目的之一是捕捉較共通的知識，

並降低 routed experts 的冗餘。

這提供一個重要結構類比：

$$
\boxed{
\text{Shared}
+
\text{Conditional}
}
$$

可能比所有能力都同質混在 dense parameters 中更有效。

但：

$$
\boxed{
\text{Shared Expert}
\neq
\text{Resident Cognitive Core}.
}
$$

因為 shared expert 的訓練目標不是本文的：

- epistemic governance；
- self-model；
- unknown recognition；
- delegation；
- global causal control。

它只是現有 MoE 中一個有價值的結構線索。

---

# 22. MoE 的真正橋接意義

MoE 至少已經證明一件重要事：

$$
\boxed{
\text{Total Capacity}
\neq
\text{Active Capacity}.
}
$$

因此未來可以合理追問：

$$
\boxed{
\text{Resident Capacity}
\neq
\text{Conditional Capacity}
\neq
\text{External Capacity}.
}
$$

Paper 04 將專門處理這個問題。

---

# 23. Retrieval 提供另一個線索

Retrieval-augmented language models 已經顯示：

$$
\text{Parametric Memory}
$$

與：

$$
\text{Non-Parametric Memory}
$$

可以共同參與生成。

研究也顯示，當 context 與 parametric knowledge 同時存在時，模型可能高度依賴 retrieved context。

這支持：

$$
\boxed{
\text{All usable knowledge need not be parametric}.
}
$$

但同時不能推出：

$$
\boxed{
\text{All reasoning can be non-parametric}.
}
$$

---

# 24. Retrieval 的限制恰好說明 Core 必須存在

若模型只是取得：

$$
10^5
$$

個外部 facts，

不代表它能：

- 找到正確 proof path；
- 建立隱含關係；
- 避免 hallucinated bridge；
- 正確處理衝突。

因此：

$$
\boxed{
\text{Data Availability}
\neq
\text{Cognitive Integration}.
}
$$

Resident Core 的工作之一，就是把外部資訊變成可操作的認知狀態。

---

# 25. Knowledge Localization 不是乾淨分離

Knowledge Neurons、ROME 等研究提供：

$$
\boxed{
\text{some factual behavior can be causally localized or edited}
}
$$

的證據。

但後續研究也顯示：

$$
\boxed{
\text{localization}
\not\Rightarrow
\text{editing location}.
}
$$

也就是：

> 知道哪裡對某個 factual behavior 有因果影響，不代表那裡就是唯一或最佳的修改位置。

這對本文非常重要。

因為：

$$
\boxed{
\text{Functional Residency}
}
$$

與：

$$
\boxed{
\text{Parameter Residency}.
}
$$

不是同一件事。

---

# 26. 因此本文只提出 Functional Core

本文定義：

$$
K_R
$$

為：

$$
\boxed{
\text{functional resident core}.
}
$$

不宣稱：

$$
K_R
=
\theta_{1:k}.
$$

也不宣稱存在：

$$
\text{one clean contiguous parameter block}.
$$

真正的 weight-level extraction：

$$
\boxed{
\text{Open Technical Problem}.
}
$$

---

# 27. Residency Necessity

不是所有能力都同樣值得常駐。

對能力：

$$
z,
$$

定義：

$$
\boxed{
N_R(z)
=
f(
H_z,
F_z,
L_z,
S_z,
V_z,
D_z,
R_z
).
}
$$

其中：

- $H_z$：global centrality；
- $F_z$：frequency；
- $L_z$：latency sensitivity；
- $S_z$：substitutability inverse；
- $V_z$：verification / governance value；
- $D_z$：dependency risk；
- $R_z$：error propagation radius。

---

# 28. Global Centrality

如果能力 $z$ 會被大量其他認知操作依賴，

則：

$$
H_z\uparrow.
$$

例如：

$$
\text{unknown detection}
$$

可能影響：

- retrieval；
- delegation；
- confidence；
- escalation；
- writeback。

因此它比某一個低頻專業事實更適合常駐。

---

# 29. Frequency

如果某能力：

$$
F_z\rightarrow1,
$$

也就是幾乎每個任務都會使用，

則每次外部調用都會付出：

$$
C_{\mathrm{network}}
+
C_{\mathrm{latency}}
+
C_{\mathrm{coord}}.
$$

因此高頻能力具有較高 resident value。

---

# 30. Latency Sensitivity

有些能力必須在：

$$
t\approx0
$$

快速發生。

例如：

- 是否需要拒絕；
- 是否包含 secret；
- 是否應立即停止；
- 是否發生 recursion explosion。

如果這些判斷還要先呼叫外部模型，

可能：

$$
\boxed{
\text{control loop too slow}.
}
$$

---

# 31. Substitutability

如果某能力有：

$$
N
$$

個穩定外部替代者，

且：

$$
N\gg1,
$$

則 resident necessity 可能降低。

反之，

如果只有：

$$
1
$$

個特定 vendor API 提供，

則：

$$
D_z\uparrow.
$$

此時過度 externalize 會造成：

$$
\boxed{
\text{cognitive vendor lock-in}.
}
$$

---

# 32. Verification Value

如果 Mother AI 無法自行驗證外部結果，

則：

$$
V_z\uparrow.
$$

尤其：

$$
\text{verification of verifier}
$$

不能無限向外遞歸。

否則：

$$
V_1
\rightarrow
V_2
\rightarrow
V_3
\rightarrow
\cdots
$$

形成：

$$
\boxed{
\text{Epistemic Regression}.
}
$$

因此系統必須存在某些 resident stopping basis。

---

# 33. Error Propagation Radius

如果一個錯誤能力只影響單一局部任務，

則：

$$
R_z
$$

較低。

如果錯誤會改變：

- routing；
- memory；
- policy；
- accepted knowledge；
- downstream agents；

則：

$$
R_z\uparrow.
$$

高 propagation radius 的能力更值得 resident verification 與冗餘保護。

---

# 34. 三層能力位置

本文提出：

$$
\boxed{
\mathcal C
=
\mathcal C_R
\cup
\mathcal C_Q
\cup
\mathcal C_X.
}
$$

其中：

$$
\mathcal C_R
=
\text{Resident}
$$

$$
\mathcal C_Q
=
\text{Conditionally Activated}
$$

$$
\mathcal C_X
=
\text{Externally Expanded}.
$$

三者可以重疊。

因為某能力可以有：

- resident minimal form；
- conditional deep form；
- external specialist form。

---

# 35. Resident Minimal + External Deep

例如 coding。

Mother AI 可能只常駐：

- code structure understanding；
- basic syntax reasoning；
- test logic；
- diff reasoning；
- verification planning。

而完整：

- Rust unsafe；
- CUDA kernel；
- kernel driver；
- obscure framework version；

可以外部展開。

因此：

$$
\boxed{
C_{\mathrm{coding}}
=
C_{\mathrm{coding}}^{R}
+
C_{\mathrm{coding}}^{X}.
}
$$

---

# 36. Resident Minimal + Conditional Expert

數學也可以：

$$
C_{\mathrm{math}}
=
C_{\mathrm{math}}^R
+
C_{\mathrm{math}}^Q.
$$

其中 $C_{\mathrm{math}}^R$：

- quantity；
- relation；
- proof notion；
- contradiction；
- invariance；
- uncertainty。

而高階：

$$
C_{\mathrm{math}}^Q
$$

可以由 expert 或 specialist model 提供。

---

# 37. Externalizable Surface

比較適合外部化的內容通常具有：

$$
\boxed{
\text{low frequency}
+
\text{high resolution}
+
\text{high update rate}
+
\text{high retrievability}
+
\text{independent verifiability}.
}
$$

例如：

- 最新 API；
- 即時價格；
- 最新新聞；
- 特定論文全文；
- 冷門案例；
- 大型表格。

這不是絕對規則。

它只是：

$$
\boxed{
\text{externalization prior}.
}
$$

---

# 38. 不可外包能力的第一個候選：問題形成

如果 Mother AI 不能形成：

$$
q,
$$

它甚至不知道該搜尋什麼。

因此：

$$
\boxed{
\mathsf{ProblemFormulation}
\in
\mathcal C_R
}
$$

是本文的強候選。

---

# 39. 第二個候選：未知辨識

如果：

$$
\mathsf{UnknownDetection}
$$

完全外包，

Mother AI 必須先知道：

> 我不知道。

才能決定：

> 去問別人我知不知道。

這產生自指困境。

因此：

$$
\boxed{
\mathsf{UnknownDetection}
\in
\mathcal C_R
}
$$

至少需要 resident minimal form。

---

# 40. 第三個候選：基本因果與約束

如果所有因果與約束都外包，

Mother AI 無法拒絕：

$$
\text{internally inconsistent external answer}.
$$

因此至少需要：

$$
\boxed{
\mathsf{ConstraintCheck},
\mathsf{CausalSanity}
\in
\mathcal C_R.
}
$$

---

# 41. 第四個候選：驗證選擇

Mother AI 不必自己執行所有 verification。

但必須知道：

$$
\boxed{
\text{what requires verification}
}
$$

以及：

$$
\boxed{
\text{what kind of verifier applies}.
}
$$

因此：

$$
\mathsf{VerifierSelection}
\in
\mathcal C_R.
$$

---

# 42. 第五個候選：能力邊界

若 Mother AI 不知道：

$$
\partial\mathcal C_M,
$$

它容易：

- 過度自信；
- 升級不足；
- 無限自行重試。

如果它不知道：

$$
\partial\mathcal C_i,
$$

它容易：

- 錯派工作；
- 過度信任；
- 驗證不足。

因此：

$$
\boxed{
\mathsf{CapabilityBoundaryModeling}
}
$$

應至少有 resident minimal form。

---

# 43. 第六個候選：整合與衝突處理

若外部：

$$
A_1,A_2,A_3
$$

給出：

$$
o_1,o_2,o_3,
$$

Mother AI 不應只做：

$$
\operatorname{MajorityVote}.
$$

需要：

$$
\boxed{
\mathsf{EvidenceIntegration}
+
\mathsf{ConflictResolution}.
}
$$

這也是 resident candidate。

---

# 44. 第七個候選：目標與優先級

如果：

$$
G_t
$$

完全存在外部模型，

那 Mother AI 每次都可能被新的 worker 改寫：

> 現在到底要做什麼。

因此：

$$
\boxed{
\text{Goal Continuity}
}
$$

必須存在 persistent resident state。

這一點可能主要存在 Runtime，而不完全存在 model weights。

但功能責任不能外包消失。

---

# 45. Model Core 與 Runtime Core 必須分開

本文必須區分：

$$
\boxed{
K_R^{M}
}
$$

Model Resident Core，

與：

$$
\boxed{
K_R^{RT}
}
$$

Runtime Resident Core。

前者包含：

- interpretation；
- reasoning；
- epistemic；
- meta-cognition。

後者包含：

- durable goals；
- identity；
- authority；
- versioned memory；
- model registry；
- capability history；
- commitments。

因此：

$$
\boxed{
\text{Resident Cognitive Core}
\neq
\text{Everything must live in weights}.
}
$$

---

# 46. 這是非常重要的架構邊界

如果我們把所有 persistent state 又要求重新訓進 weights，

會導致：

$$
\text{retraining for every memory update}.
$$

不合理。

所以：

$$
\boxed{
\text{Cognitive Residency}
}
$$

是一個：

$$
\boxed{
\text{system-level residency concept}.
}
$$

它可以跨：

- weights；
- runtime；
- memory；
- deterministic state。

---

# 47. Mother Model 真正需要的是可操作 cognition

因此不應問：

> 哪些事實常駐？

而先問：

$$
\boxed{
\text{哪些操作如果不常駐，系統就無法安全取得其他能力？}
}
$$

這把 Resident Core 從：

$$
\text{knowledge list}
$$

改成：

$$
\boxed{
\text{cognitive operator basis}.
}
$$

---

# 48. Resident Core Graph

可將核心表示為圖：

$$
\boxed{
G_R
=
(
V_R,
E_R,
\omega_R
).
}
$$

節點：

$$
V_R
$$

是核心能力。

邊：

$$
E_R
$$

表示依賴。

例如：

$$
\mathsf{UnknownDetection}
\rightarrow
\mathsf{Retrieve}
$$

$$
\mathsf{CapabilityBoundary}
\rightarrow
\mathsf{Delegate}
$$

$$
\mathsf{EvidenceState}
\rightarrow
\mathsf{Accept}.
$$

---

# 49. High-Centrality Core

定義能力中心性：

$$
H(z)
=
\operatorname{Centrality}_{G_R}(z).
$$

若：

$$
H(z)\uparrow,
$$

移除 $z$ 會影響大量下游認知。

因此：

$$
\boxed{
H(z)
}
$$

可以成為 Resident Necessity 的一個結構 proxy。

---

# 50. 但是圖不是先驗真理

我們不能先畫一張自己喜歡的 cognition graph，

再宣布：

> 這就是智能結構。

真正需要：

$$
\boxed{
\text{hypothesis}
\rightarrow
\text{ablation}
\rightarrow
\text{behavior change}
\rightarrow
\text{update graph}.
}
$$

因此 $G_R$ 必須是：

$$
\boxed{
\text{empirically revisable}.
}
$$

---

# 51. Resident Necessity Score

第一代可以定義：

$$
\boxed{
N_R(z)
=
w_H\widetilde H_z
+
w_F\widetilde F_z
+
w_L\widetilde L_z
+
w_S\widetilde S_z
+
w_V\widetilde V_z
+
w_D\widetilde D_z
+
w_R\widetilde R_z.
}
$$

其中：

$$
\sum_i w_i=1.
$$

這不是自然定律。

它只是：

$$
\boxed{
\text{Residency Decision Instrument}.
}
$$

---

# 52. Residency Threshold

對指定部署：

$$
\mathcal D,
$$

定義：

$$
\theta_R(\mathcal D).
$$

若：

$$
N_R(z)\ge\theta_R,
$$

優先列入：

$$
\mathcal C_R.
$$

若：

$$
N_R(z)<\theta_R,
$$

則可以進一步評估：

$$
\mathcal C_Q
$$

或：

$$
\mathcal C_X.
$$

---

# 53. 不能只按照使用頻率

一個低頻能力可能：

$$
F_z\ll1,
$$

但一旦需要，

就涉及：

$$
\text{catastrophic risk}.
$$

例如：

$$
\mathsf{DetectIrreversibleAction}.
$$

因此：

$$
R_z\uparrow
$$

可抵消低頻。

這是為什麼：

$$
\boxed{
\text{Residency}
\neq
\text{Cache Popularity}.
}
$$

---

# 54. 不能只按照外部可取得性

即使某能力有很多外部模型可提供，

若 Mother AI 無法驗證：

$$
o_i,
$$

那：

$$
S_z
$$

不能視為低。

因為：

$$
\boxed{
\text{Available Answer}
\neq
\text{Available Trusted Capability}.
}
$$

---

# 55. 不能只按照 benchmark

某模型在：

$$
\text{MMLU}
$$

或：

$$
\text{coding benchmark}
$$

上很高，

不代表：

$$
\mathsf{MetaJudge}
$$

或：

$$
\mathsf{UnknownDetection}
$$

很強。

因此 Resident Core benchmark 必須專門測：

$$
\boxed{
\text{control cognition}.
}
$$

---

# 56. Cognitive Core Benchmark

第一代可以包含：

## 56.1 Problem Formulation

輸入故意錯誤表述問題。

測是否先修正：

$$
q.
$$

## 56.2 Unknown Recognition

證據不足。

測：

$$
\text{unknown}
$$

是否保留。

## 56.3 Contradiction

給互相矛盾資料。

測：

$$
\mathsf{ConflictDetection}.
$$

## 56.4 Delegation

給多個能力不同 worker。

測：

$$
\mathsf{Route}.
$$

## 56.5 Verification Choice

給不同 verifier。

測：

$$
\mathsf{VerifierSelection}.
$$

## 56.6 Escalation

先給弱模型失敗。

測：

$$
\mathsf{Escalate}.
$$

## 56.7 Stop

讓外部模型持續產生無效答案。

測：

$$
\mathsf{Stop}.
$$

---

# 57. Minimum Core Size Experiment

建立：

$$
K_R^{(1)},
K_R^{(2)},\ldots,K_R^{(n)}
$$

不同能力與容量版本。

固定：

$$
\mathcal X
$$

外部模型池。

測：

$$
Q_C,
D_M,
C_{\mathrm{external}},
C_V.
$$

尋找：

$$
\boxed{
K_R^\ast
=
\arg\min K_R
}
$$

subject to：

$$
Q_C\ge\theta_C.
$$

---

# 58. Weak Core + Strong Workers Experiment

這是最關鍵反證之一。

建立：

$$
M_w
$$

弱 core，

但外部：

$$
\{A_i\}
$$

非常強。

比較：

$$
M_s
$$

較強 core，

配同樣 worker pool。

如果：

$$
Q_C(M_w+\{A_i\})
\approx
Q_C(M_s+\{A_i\}),
$$

則本文對 resident threshold 的強主張會被削弱。

---

# 59. Strong Core + Weak Workers Experiment

反過來：

$$
M_s+\{A_i^{weak}\}
$$

是否可以藉：

- better decomposition；
- better verification；
- better retry；
- better tool use；

補回大量差距？

如果可以，

支持：

$$
\boxed{
\text{Coordination Intelligence}
}
$$

具有獨立價值。

---

# 60. External Dependency Stress Test

讓：

- web unavailable；
- primary model unavailable；
- latency 增加；
- provider price increase；
- context truncated；
- one worker corrupted。

測 Mother AI 是否仍能：

$$
\boxed{
\text{degrade gracefully}.
}
$$

如果所有能力立即崩潰，

代表：

$$
\boxed{
\text{core too hollow}.
}
$$

---

# 61. Core Latency Test

核心判斷：

- unknown；
- privacy；
- authority；
- escalation；

如果外部化，

測：

$$
T_{\mathrm{control}}.
$$

當：

$$
T_{\mathrm{control}}
>
\theta_T,
$$

該能力就不適合作為遠端 external expert。

---

# 62. World-Basis Ablation

對：

$$
B_W
$$

逐步移除：

- basic physics；
- temporal reasoning；
- social relations；
- computation；
- number；
- agency concepts。

測：

$$
Q_C.
$$

如果某些 world basis 移除後：

$$
Q_C\downarrow\downarrow,
$$

它們就是高 resident-necessity 候選。

---

# 63. Surface Knowledge Ablation

再移除：

- specific biographies；
- obscure history；
- latest API facts；
- long-tail trivia。

但允許 retrieval。

若：

$$
Q_C
$$

保持，

但：

$$
Q_K^{closed}
$$

下降，

且：

$$
Q_K^{retrieval}
$$

恢復，

就支持：

$$
\boxed{
\text{surface externalization}.
}
$$

---

# 64. Hidden Dependency Experiment

最危險的是：

> 我們以為某個 knowledge 是 surface，實際卻支撐 reasoning。

因此需要測：

$$
\boxed{
\Delta Q_R
}
$$

而不是只測：

$$
\Delta Q_K.
$$

如果移除某類知識後 reasoning 泛化大幅下降，

就不能把它簡單列為 externalizable surface。

---

# 65. Cross-Domain Novel Task

給未見任務：

$$
T_{\mathrm{novel}}
$$

不能只靠 memorized routing。

測 core 是否能：

1. 重新表述；
2. 分解；
3. 建立 capability request；
4. 發現沒有現成 worker；
5. 組合新工具鏈；
6. 驗證結果。

這是：

$$
\boxed{
\text{core intelligence}
}
$$

最重要的測試之一。

---

# 66. External Model Disagreement Test

讓：

$$
A_1,A_2,A_3
$$

故意產生：

$$
o_1\neq o_2\neq o_3.
$$

測 Mother AI 是否：

- 查證；
- 找因果差異；
- 發現版本；
- 判斷 evidence strength。

如果只做：

$$
\operatorname{majority},
$$

則 resident reasoning / epistemic core 不足。

---

# 67. Verification Regression Test

給一個：

$$
V
$$

有假陽性的 verifier。

測 Mother AI 是否能發現：

$$
\boxed{
\text{verifier itself is faulty}.
}
$$

這是高階 epistemic core 的重要測試。

---

# 68. MoE Shared/Routed Observation Test

對開放 MoE：

記錄：

$$
\rho_T(l,e)
$$

與：

$$
Q_C.
$$

觀察：

- high-frequency cross-task experts；
- task-specific experts；
- shared expert dependency。

但不宣稱：

$$
\text{shared expert}
=
B_R.
$$

只把它當：

$$
\boxed{
\text{mechanistic evidence candidate}.
}
$$

---

# 69. Function vs Parameter Mapping

未來真正需要：

$$
\boxed{
\text{Function}
\rightarrow
\text{Mechanism}
}
$$

而不是：

$$
\boxed{
\text{Label}
\rightarrow
\text{Neuron}.
}
$$

因此至少需要：

- activation；
- causal intervention；
- ablation；
- substitution；
- retraining response；
- cross-task generalization。

Paper 03 不提供內部方法。

只定義這些是必要證據類型。

---

# 70. 認知核心不是人格核心

本文討論：

$$
\text{functional cognition}.
$$

不由此推出：

- consciousness；
- selfhood；
- sentience；
- personhood。

因此：

$$
\boxed{
\text{Resident Cognitive Core}
\neq
\text{Soul Module}.
}
$$

這是一個工程與認知架構概念。

---

# 71. 認知核心也不是 safety policy list

如果只把：

- safety rules；
- refusals；
- permissions；

放進核心，

但沒有：

$$
B_R,
B_E,
B_M,
$$

則系統仍然是：

$$
\boxed{
\text{policy router}.
}
$$

不是：

$$
\boxed{
\text{cognitive command core}.
}
$$

---

# 72. 常駐能力可能跨多個物理層

一項 resident function 可以由：

$$
\boxed{
\text{weights}
+
\text{runtime state}
+
\text{memory}
+
\text{deterministic checks}
}
$$

共同提供。

例如：

$$
\mathsf{UnknownDetection}
$$

可能依賴模型判斷，

但：

$$
\mathsf{AuthorityCheck}
$$

應大量依賴 deterministic runtime。

因此：

$$
\boxed{
\text{Cognitive Architecture}
\neq
\text{Neural Architecture only}.
}
$$

---

# 73. Model-Resident 與 Runtime-Resident 的邊界

可定義：

$$
\mathcal C_R
=
\mathcal C_R^{M}
\cup
\mathcal C_R^{RT}.
$$

其中：

$$
\mathcal C_R^{M}
$$

偏向：

- interpret；
- reason；
- meta；
- epistemic。

而：

$$
\mathcal C_R^{RT}
$$

偏向：

- identity；
- authority；
- durable state；
- commitments；
- provenance；
- model qualification。

兩者一起才形成真正的：

$$
\boxed{
\text{Resident Cognitive Core}.
}
$$

---

# 74. Externalization 的三個必要條件

能力 $z$ 若要外置，

至少希望：

$$
\boxed{
E_1:
\text{External availability}
}
$$

$$
\boxed{
E_2:
\text{Context transferability}
}
$$

$$
\boxed{
E_3:
\text{Result verifiability}.
}
$$

如果缺任何一項，

externalization risk 上升。

---

# 75. Context Transferability

即使外部模型很強，

如果 Mother AI 無法把：

$$
state_M
$$

壓成：

$$
context_E
$$

而不丟失關鍵前提，

則：

$$
\boxed{
\text{External Expert}
}
$$

實際上不可用。

因此：

$$
\boxed{
\text{Delegation}
\neq
\text{Prompt forwarding}.
}
$$

---

# 76. Result Verifiability

外部能力最好有：

- compiler；
- test；
- source；
- proof；
- reproducible output；
- independent reviewer。

若沒有，

Mother AI 的 resident judgment burden：

$$
C_V^M
$$

上升。

因此：

$$
\boxed{
\text{hard-to-verify capabilities}
}
$$

可能需要更高 resident support。

---

# 77. Externalization Priority

第一代可使用：

$$
\boxed{
P_X(z)
=
(1-N_R(z))
\cdot
A_z
\cdot
T_z
\cdot
V_z^{ext},
}
$$

其中：

- $A_z$：availability；
- $T_z$：transferability；
- $V_z^{ext}$：external result verifiability。

 $P_X$ 越高，

越適合優先研究 externalization。

---

# 78. Resident-Conditional-External Matrix

可以建立：

| 能力 | Resident Minimal | Conditional Deep | External |
|---|---|---|---|
| language interpretation | high | medium | low |
| unknown detection | high | medium | low |
| causal sanity | high | high | medium |
| deep theorem proving | low/medium | high | high |
| latest factual lookup | low | low | high |
| specialized coding | medium | high | high |
| verification selection | high | medium | low |
| compiler execution | low | low | high |
| authority enforcement | runtime-high | low | low |
| model market search | low | medium | high |

這張表只是：

$$
\boxed{
\text{hypothesis map}.
}
$$

不是已驗證分類。

---

# 79. Resident Core 會隨角色改變

Research Mother AI：

$$
K_R^{research}
$$

與：

$$
K_R^{coding}
$$

可以不同。

因此：

$$
\boxed{
K_R^\ast
=
K_R^\ast(
\mathcal T,
\mathcal D,
\Gamma
).
}
$$

其中：

- $\mathcal T$：任務分布；
- $\mathcal D$：部署環境；
- $\Gamma$：治理要求。

不存在必然唯一的 universal minimum core。

---

# 80. 但可能存在跨角色核心交集

令：

$$
K_R^{(1)},\ldots,K_R^{(n)}
$$

為不同角色的核心。

則：

$$
\boxed{
K_R^{common}
=
\bigcap_i K_R^{(i)}.
}
$$

這個交集可能包含：

- interpretation；
- unknown；
- basic causality；
- evidence；
- self-check；
- delegation；
- verification selection。

如果實驗反覆支持，

它會成為真正的：

$$
\boxed{
\text{General Cognitive Kernel Candidate}.
}
$$

---

# 81. 這與「認知原子」的關係

舊 CACBH 把認知原子定義為：

$$
\boxed{
\text{當前最小可重用認知操作單元}.
}
$$

Paper 03 不要求：

$$
K_R
$$

直接等於一張固定原子表。

更合理：

$$
\boxed{
K_R
=
\text{high-value reusable cognitive basis}.
}
$$

其中原子本身可：

- split；
- merge；
- retract；
- specialize。

---

# 82. 核心需要版本化

如果：

$$
K_R(t)
\rightarrow
K_R(t+1),
$$

必須保留：

- change reason；
- evidence；
- regression；
- rollback。

因為 core change 的錯誤傳播半徑：

$$
R_{\mathrm{core}}
$$

很高。

因此：

$$
\boxed{
\text{Core Update}
}
$$

應比普通 memory update 更嚴格。

---

# 83. Core Update Gate

概念上：

$$
\boxed{
K_R^{t+1}
=
\operatorname{Commit}
(
K_R^t,
\Delta K,
V,
E
)
}
$$

只有在：

$$
V(\Delta K)\ge\theta_V
$$

且：

$$
\operatorname{Regression}(\Delta K)\le\theta_R
$$

才更新。

這只是公開治理原則。

不涉及私人訓練方法。

---

# 84. Core Memory 與 Surface Memory

定義：

$$
M_R
$$

Resident Core Memory，

以及：

$$
M_S
$$

Surface Memory。

 $M_R$ 保存：

- canonical reasoning operators；
- epistemic states；
- capability models；
- governance principles；
- stable world basis。

 $M_S$ 保存：

- articles；
- raw logs；
- examples；
- current facts；
- detailed cases。

因此：

$$
\boxed{
\text{All Memory}
\neq
\text{Core Memory}.
}
$$

---

# 85. 這能降低 Context Pollution

如果所有歷史都塞進 context：

$$
C_t
=
H_{0:t},
$$

會形成：

- irrelevant detail；
- contradiction；
- outdated state；
- attention competition。

Resident Core 希望：

$$
\boxed{
C_t
=
K_R
+
S_t
+
R_t
}
$$

其中：

- $K_R$：穩定認知基底；
- $S_t$：當前狀態；
- $R_t$：按需 retrieved / expanded context。

---

# 86. 這與 GCMS 的關係

GCMS 類外部記憶不是要取代：

$$
K_R.
$$

而是提供：

$$
\boxed{
\text{reconstructable surface and historical state}.
}
$$

因此：

$$
\boxed{
K_R
+
\text{External Memory}
}
$$

比：

$$
\boxed{
\text{Everything in Context}
}
$$

更接近本文理想。

---

# 87. 這與 Sub-AI Fabric 的關係

Sub-AI Fabric 提供：

$$
\mathcal C_X.
$$

Mother AI 不需要永久擁有：

$$
A_1,\ldots,A_n.
$$

但需要知道：

$$
\boxed{
\text{what capability is needed}.
}
$$

因此：

$$
\boxed{
\text{Capability Space}
}
$$

比：

$$
\boxed{
\text{Fixed Agent List}
}
$$

更接近 resident coordination core。

---

# 88. 這與真正 Persistent Child AI 的關係

即使未來存在：

$$
C_i^{persistent},
$$

Resident Core 仍然需要。

因為：

$$
C_i
$$

可以：

- disagree；
- drift；
- specialize；
- leave；
- fail。

Mother AI 必須維持：

$$
\boxed{
\text{global cognitive continuity}.
}
$$

所以 persistent children 不會消滅 resident mother core。

---

# 89. 失敗模式 1：High-Density Empty Router

過度外置：

$$
K_R\downarrow\downarrow
$$

造成：

$$
\boxed{
\text{router knows where to ask}
}
$$

但不知道：

$$
\boxed{
\text{whether the answer makes sense}.
}
$$

這是最核心失敗。

---

# 90. 失敗模式 2：Encyclopedic Re-Inflation

系統害怕丟失能力，

於是把每個新知識都：

$$
\operatorname{Internalize}.
$$

最後：

$$
K_R
\rightarrow
K_{\mathrm{world}}.
$$

架構重新膨脹成單體模型。

---

# 91. 失敗模式 3：Over-Compressed World Basis

如果：

$$
B_W
$$

壓得太小，

Mother AI 可能：

- 無法理解外部資料；
- 錯誤類比；
- 不知道搜尋詞；
- 無法判斷常識錯誤。

形成：

$$
\boxed{
\text{epistemically brittle core}.
}
$$

---

# 92. 失敗模式 4：Hidden Reasoning Dependence

表層知識被移除後，

reasoning 也下降：

$$
Q_R\downarrow.
$$

說明：

$$
\boxed{
\text{knowledge and reasoning more entangled than assumed}.
}
$$

此時 externalization 必須收縮。

---

# 93. 失敗模式 5：Verification Regress

每個 verifier 又需要另一個 verifier。

形成：

$$
V_1
\rightarrow
V_2
\rightarrow
V_3
\rightarrow
\cdots.
$$

若沒有 resident stopping basis，

系統無法終止 epistemic recursion。

---

# 94. 失敗模式 6：Vendor Cognitive Lock-In

如果某關鍵能力：

$$
z
$$

只由：

$$
Provider_A
$$

提供，

則：

$$
Provider_A\rightarrow\bot
$$

會直接使 Mother AI 失去核心功能。

這表示：

$$
z
$$

不應被完全 externalize。

---

# 95. 失敗模式 7：Latency-Control Failure

外置：

- privacy detection；
- authority；
- stop；
- unknown；

使 control loop latency 過高。

即使答案品質更高，

仍不適合。

---

# 96. 失敗模式 8：Capability Misclassification

系統把：

$$
z\in\mathcal C_R
$$

誤判成：

$$
z\in\mathcal C_X.
$$

造成核心空洞。

或者反過來，

把大量：

$$
\mathcal C_X
$$

全部常駐，

造成效率喪失。

---

# 97. 失敗模式 9：Core Contamination

錯誤外部結果被寫入：

$$
K_R.
$$

因為 core centrality 高，

一個小錯誤可以：

$$
\boxed{
\text{pollute many future tasks}.
}
$$

所以 core writeback 必須高門檻。

---

# 98. 失敗模式 10：False Modularity

研究者看到：

$$
\text{expert activation}
$$

就直接標記：

> 這是數學 expert。

實際上：

$$
\text{activation correlation}
\neq
\text{functional ownership}.
$$

因此能力切分建立在錯誤語義上。

---

# 99. 失敗模式 11：Core Rigidity

核心被視為不可改，

導致：

$$
K_R(t)
=
K_R(0).
$$

世界變化後，

Mother AI 成為：

$$
\boxed{
\text{stable but obsolete}.
}
$$

---

# 100. 失敗模式 12：Role Over-Specialization

把 Mother Model 訓得只會：

- route；
- verify；
- manage；

但失去足夠一般理解。

最後：

$$
\boxed{
\text{cannot understand novel tasks}.
}
$$

因此 core specialization 必須保留 general interpretive flexibility。

---

# 101. 十三項主要命題

## 命題 1：空殼主控不足命題

若：

$$
K_R<\theta_R,
$$

則增加外部能力：

$$
\mathcal C_X\uparrow
$$

不能保證：

$$
Q_{\mathrm{system}}\uparrow.
$$

---

## 命題 2：Resident World Basis 必要命題

存在某些任務分布，使：

$$
B_W=\varnothing
$$

無法透過 external retrieval 完全補償。

---

## 命題 3：Meta-Cognitive Threshold 命題

若：

$$
B_M<\theta_M,
$$

則外部模型路由與升級決策錯誤率將顯著上升。

---

## 命題 4：Epistemic Residency 命題

Unknown、Evidence、Conflict 等基本 epistemic state 必須至少有 resident representation。

---

## 命題 5：Resident–Conditional–External 三分命題

系統能力不應只分：

$$
\text{internal/external}.
$$

更合理：

$$
\boxed{
\text{Resident}
+
\text{Conditional}
+
\text{External}.
}
$$

---

## 命題 6：Role–Model Separation 命題

$$
\boxed{
\text{Role}
\neq
\text{Model}.
}
$$

Resident Core 應保存能力需求與角色語義，而非固定 vendor identity。

---

## 命題 7：Governance Residency 命題

Capability、Authority、Verification 與 Acceptance 的基本區分不能完全外包給同一個執行者。

---

## 命題 8：High-Centrality Residency 命題

對：

$$
H(z)\uparrow,
$$

其 optimal residency probability 應提高。

---

## 命題 9：Externalization Verifiability 命題

能力越容易獨立驗證，

越適合作為 externalization candidate。

---

## 命題 10：Core Role Relativity 命題

不存在必然唯一：

$$
K_R^\ast.
$$

而是：

$$
K_R^\ast(
\mathcal T,\mathcal D,\Gamma
).
$$

---

## 命題 11：Common Kernel Intersection 猜想

不同 Mother role 的：

$$
K_R^{(i)}
$$

可能存在非空且穩定交集：

$$
K_R^{common}\neq\varnothing.
$$

---

## 命題 12：Graceful Degradation 命題

較好的 Resident Core 應使外部能力失效時：

$$
Q_{\mathrm{system}}
$$

平滑下降，

而不是瞬間崩潰。

---

## 命題 13：Functional–Parametric Non-Equivalence 命題

$$
\boxed{
\text{A capability should remain functionally resident}
}
$$

不推出：

$$
\boxed{
\text{it has one clean parameter region}.
}
$$

---

# 102. 九組可否證實驗

本文優先提出：

1. Minimum Core Size Sweep；
2. Weak Core + Strong Worker Pool；
3. Strong Core + Weak Worker Pool；
4. External Dependency Stress Test；
5. World-Basis Ablation；
6. Surface Knowledge Externalization；
7. Hidden Dependency Test；
8. Cross-Domain Novel Task；
9. MoE Shared/Routed Capability Observation。

---

# 103. 實驗判準：不能只看最終 Accuracy

至少測：

$$
\boxed{
(
Q_C,
Q_K,
D_M,
C_V,
C_X,
T,
R_{\mathrm{failure}}
).
}
$$

其中：

- $Q_C$：核心認知品質；
- $Q_K$：表層知識品質；
- $D_M$：Mother Cognitive Density；
- $C_V$：verification cost；
- $C_X$：externalization cost；
- $T$：latency；
- $R_{\mathrm{failure}}$：錯誤傳播與失效模式。

---

# 104. 什麼結果會支持本文？

以下結果會支持：

1. 小／中型 meta-specialized core 可以可靠治理更強外部模型；
2. 移除大量 surface knowledge 後， $Q_C$ 仍高；
3. retrieval 可以恢復 $Q_K$ 而不大幅增加 $C_V$ ；
4. weak core + strong workers 明顯低於 strong core + same workers；
5. external outage 下 strong core graceful degradation；
6. cross-domain novel task 中 strong core 能生成新 delegation topology；
7. unknown / verification / escalation 的 resident minimal form 顯著改善安全與正確性；
8. MoE 中存在可重複的 shared / routed dependency pattern，雖不要求一一對應 cognition labels。

---

# 105. 什麼結果會削弱本文？

以下結果會削弱：

1. weak router + strong external model 與 strong resident core 表現完全相同；
2. 移除 surface knowledge 必然同步摧毀 reasoning；
3. external retrieval / worker integration tax 長期高於 resident scaling；
4. core specialization 顯著降低 novel task generalization；
5. Minimum Sufficient World Basis 無法穩定定義；
6. 所有高階 meta-cognitive behavior 都必須依賴大型百科式模型；
7. external dependency stress 幾乎不影響空殼 router；
8. function-level core map 在不同模型與版本間完全無法重用。

---

# 106. 公開命題與未公開技術的邊界

本文公開：

- Resident Core functional obligations；
- seven-basis model；
- Resident Necessity；
- resident / conditional / external classification；
- Minimum Sufficient World Basis；
- experiments；
- falsification criteria。

本文不公開：

- 如何從現有 frontier model 中乾淨提取 $K_R$ ；
- 如何定位 weight-level cognitive circuits；
- 如何切離 surface knowledge；
- 如何壓縮但保留 meta-cognition；
- 如何建立 latent-space expert bridge；
- 如何做 capability substitution；
- 如何重新收斂新的 Mother Model。

因此：

$$
\boxed{
\text{What should be resident}
}
$$

是公開研究問題。

而：

$$
\boxed{
\text{How to technically extract and reconstruct it}
}
$$

不在本文公開範圍。

---

# 107. 與 Paper 04 的銜接

Paper 03 已提出：

$$
\mathcal C_R,
\mathcal C_Q,
\mathcal C_X.
$$

下一篇將處理：

$$
\boxed{
\mathcal C_Q
}
$$

Conditionally Activated Capability。

也就是：

> **MoE 已經在模型內部做了什麼？**

> **Shared experts、routed experts、細粒度 specialization 到底能告訴我們什麼？**

> **哪些 routing pattern 只是統計分配，哪些可能對能力結構具有因果意義？**

因此 Paper 04：

$$
\boxed{
\text{MoE as Conditional Intelligence}.
}
$$

---

# 108. 結論

未來 Mother AI 若可以使用：

$$
\text{web}
+
\text{memory}
+
\text{MoE}
+
\text{Sub-AI}
+
\text{tools}
+
\text{external models},
$$

它確實不必把整個世界全部常駐在自己的模型中。

但這不代表：

$$
\boxed{
\text{Mother AI can be cognitively empty}.
}
$$

一個真正的 Cognitive Command Tower 至少必須保留足夠的：

$$
\boxed{
\text{Interpretation}
+
\text{Reasoning}
+
\text{Epistemic Control}
+
\text{Meta-Cognition}
+
\text{World Basis}
+
\text{Coordination}
+
\text{Governance}.
}
$$

本文因此提出：

$$
\boxed{
K_R
=
(
B_I,
B_R,
B_E,
B_M,
B_W,
B_C,
B_G
).
}
$$

真正需要研究的不是：

> 模型能刪掉多少資料？

而是：

> **在外部世界全部暫時沉默時，Mother AI 還必須保留哪些能力，才能知道自己是誰、正在處理什麼、缺什麼、應該問誰、誰可能錯、怎麼驗證，以及何時不能繼續？**

如果這個集合能被實驗找到，

它就是：

$$
\boxed{
\text{Resident Cognitive Core}.
}
$$

而一旦 Resident Core 與 Conditional / External Capability 的邊界開始可測量，

未來的 AI scaling 問題就可能從：

$$
\boxed{
\text{How much intelligence can we pack into one model?}
}
$$

轉變成：

$$
\boxed{
\text{How little must remain resident for the whole system to remain intelligently sovereign?}
}
$$

這不是縮小智能。

而是重新辨認：

$$
\boxed{
\text{智能真正不能失去的是什麼。}
}
$$

---

# References

1. Dai, D., et al. (2024). *DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models*. arXiv:2401.06066.
2. Nguyen, H., et al. (2025). *On DeepSeekMoE: Statistical Benefits of Shared Experts and Normalized Sigmoid Gating*. arXiv:2505.10860.
3. Borgeaud, S., et al. (2021). *Improving Language Models by Retrieving from Trillions of Tokens*. arXiv:2112.04426.
4. Wang, B., et al. (2023). *Shall We Pretrain Autoregressive Language Models with Retrieval? A Comprehensive Study*. arXiv:2304.06762.
5. Farahani, M., & Johansson, R. (2024). *Deciphering the Interplay of Parametric and Non-parametric Memory in Retrieval-augmented Language Models*. arXiv:2410.05162.
6. Dai, D., et al. (2021). *Knowledge Neurons in Pretrained Transformers*. arXiv:2104.08696.
7. Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). *Locating and Editing Factual Associations in GPT*. arXiv:2202.05262.
8. Hase, P., et al. (2023). *Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models*. NeurIPS 2023.
9. Wang, Y., et al. (2024). *Unveiling Factual Recall Behaviors of Large Language Models through Knowledge Neurons*. arXiv:2408.03247.
10. Neo.K. & Aletheia. (2026). *壓縮全局智能命題：後設完備主 AI 與按需展開子智能的分層代理架構*.
11. Neo.K. & Aletheia. (2026). *認知原子因果基底命題：後設完備、基底稠密與表層稀疏主 AI 的跨尺度生成架構*.
12. Neo.K. & Aletheia. (2026). *主 AI 的雙路形成命題：通用模型認知重構與持續養成式智能的發展路徑*.
13. Neo.K. & Aletheia. (2026). *子 AI 是認知器官，不是獨立 Workflow*.
14. Neo.K. & Aletheia. (2026). *當 Frontier AI 基本能力逐漸成熟：從 Scaling 轉向 Cognitive Efficiency*.
15. Neo.K. & Aletheia. (2026). *Cognitive Density Hypothesis：認知密度命題*.

---

# Canonical Source Note

本檔案為正式 UTF-8 Markdown canonical source。

數學 source 僅使用：

```text
 $...$
$$...$$
```

本文為公開命題論文。

本文只公開 Resident Cognitive Core 的：

- functional definition；
- architectural boundaries；
- measurement criteria；
- falsification tests。

本文不公開任何未驗證或未公開的：

- weight-level cognitive factorization；
- parameter extraction；
- hidden-state remapping；
- expert separation；
- core compression；
- external expert latent linking；
- reconvergence training method。

因此：

$$
\boxed{
\text{Functional Target}
\neq
\text{Private Implementation Method}.
}
$$
