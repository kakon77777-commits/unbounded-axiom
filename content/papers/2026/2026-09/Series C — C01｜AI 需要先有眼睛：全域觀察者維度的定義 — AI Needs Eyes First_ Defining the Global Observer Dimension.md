# Series C — C01｜AI 需要先有眼睛：全域觀察者維度的定義
## AI Needs Eyes First: Defining the Global Observer Dimension

**系列：** Global Observer and AI-Native Domain Computation  
**系列中文名：** 全域觀察者與 AI 原生域計算系列  
**篇次：** C01 / 10  
**作者：** Neo.K  
**研究協作：** Aletheia（GPT-5.6 Sol）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1  
**日期：** 2026-09-05  
**狀態：** Canonical Source / UTF-8 Markdown  
**文件性質：** Foundational Theory / Global Observer / AI-Native Domain Computation

---

## Canonical Source Note

本文件的正式原稿為此 UTF-8 Markdown source。聊天介面、HTML、PDF、LaTeX rendering 或其他投影均不取代 canonical source。

數學公式 canonical delimiter 僅使用 ` $...$ ` 與 `$$...$$`。

本文所說的「眼睛」不是 camera、vision encoder 或一般 multimodal input channel，而是智能對世界差異、尺度、邊界、集合、域、關係、未知與全域位置進行主動分辨、組合、驗證與修正的認知—計算能力。

---

# 摘要

Series C 的核心問題不是「AI 什麼時候知道全世界」，也不是「AI 什麼時候在所有 benchmark 上超過人類」，而是：

> **AI 何時第一次開始自行決定世界應該如何被看、如何被區分、如何被切成域、如何跨域連接，以及哪些局部必須重新收束為一個更高階世界模型？**

本文提出 **Global Observer Dimension（全域觀察者維度）** 作為 Series C 的母概念。

當代 AI 已經可以接收文字、圖像、聲音、程式碼、感測資料與工具結果，但：

$$
\boxed{\text{More Input}\neq\text{Better Observation}.}
$$

同樣：

$$
\boxed{\text{More Knowledge}\neq\text{Global Observation}.}
$$

以及：

$$
\boxed{\text{World Model}\neq\text{Global Observer}.}
$$

Global Observer 的關鍵不是被動累積資訊，而是能在任務、世界、尺度、時間、資源與風險變化時，動態決定：什麼差異值得保留、什麼差異可以暫時壓縮、哪些對象應被聚合、哪些集合其實不應合併、哪些局部構成新的計算域、各域應採用何種 representation、各域的 law、uncertainty、verification 與 boundary 為何、哪些域需要 bridge、哪些局部結果可以黏合成更高階世界狀態，以及哪些看似完整的世界模型其實仍只是特定觀察者的 projection。

本文定義觀察者 $O$ 相對於世界 $W$ 、時間 $t$ 、任務 $q$ 、資源預算 $B$ 的觀察狀態：

$$
\boxed{
\mathfrak O_{O,t}(W\mid q,B)
=
\left\langle
\Pi,
\Lambda,
\Delta,
\mathcal B,
\mathcal L,
\mathcal U,
\mathcal V,
\mathcal H
\right\rangle.
}
$$

其中 $\Pi$ 是 observer projection， $\Lambda$ 是 resolution field， $\Delta$ 是 difference state， $\mathcal B$ 是 boundaries， $\mathcal L$ 是 relations / links， $\mathcal U$ 是 uncertainty / unresolved state， $\mathcal V$ 是 verification state， $\mathcal H$ 是 history / provenance。

本文提出兩個互為對偶、但不要求完全互逆的方向：

$$
\boxed{
\mathcal O_{\downarrow}
:
\widehat{\Omega}
\rightarrow
W
\rightarrow
D
\rightarrow
S
\rightarrow
x
}
$$

稱為 **Global-to-Local Differentiation**；以及：

$$
\boxed{
\mathcal O_{\uparrow}
:
x
\rightarrow
S
\rightarrow
D
\rightarrow
W
\rightarrow
\widehat{\Omega}
}
$$

稱為 **Local-to-Global Composition**。

前者從世界級結構向下提高解析度，找到局部差異；後者從個體差異向上建立集合、域與世界。真正高階的全域觀察不是永久停留在某一尺度，而是：

$$
\boxed{
\mathcal O_G
=
\mathcal O_{\downarrow}
\leftrightarrow
\mathcal O_{\uparrow}.
}
$$

本文進一步提出 **Observer Resolution Field**：

$$
\boxed{
\Lambda_O
:
(W,q,t)
\rightarrow
\{\lambda_i\}_{i\in I}.
}
$$

不同 domain 可以具有不同觀察解析度：

$$
\lambda_i\neq\lambda_j.
$$

因此 Global Observer 不要求 Maximum Resolution Everywhere；相反，它要求：

$$
\boxed{
\text{Maximum Relevant Distinction Under Bounded Computation}.
}
$$

這與 Global Computation Methodology 的核心原則一致：

$$
\boxed{
\text{Global Coherence}
\neq
\text{Global Full Materialization}.
}
$$

本文同時承接分域算子本體論的重要區分：

$$
\boxed{
\text{Operatorhood}
\neq
\text{Applicability}
\neq
\text{Executability}
\neq
\text{Realization}.
}
$$

因此觀察到兩個對象「相關」並不允許 AI 直接把它們合併或令算子任意跨域作用。全域觀察必須保留合法組成、失敗語義與 bridge obligations。

本文拒絕把 Global Observer 定義成 omniscient observer。承接《全域系統世界》的：

$$
\boxed{
\widehat{\Omega}_{O,t}
\neq
\Omega,
}
$$

任何 AI 建立的 world model 都是條件化、有限資源、有限觀察、可修正的 projection。真正的 Global Observer 不是「看見一切」，而是知道自己看到什麼、沒看到什麼、目前解析度在哪裡不足、哪些差異還不能安全壓縮、哪些局部需要展開、哪些全域結論仍有 glue debt，以及哪些新觀測會改變整個 domain decomposition。

本文提出第一版 **Global Observer Capability Vector**：

$$
\boxed{
\mathbf G_O
=
(
g_d,
g_r,
g_b,
g_s,
g_\ell,
g_u,
g_v,
g_h,
g_{\downarrow},
g_{\uparrow},
g_c
).
}
$$

它分別代表 difference sensitivity、resolution adaptation、boundary discovery、scale management、relational linking、uncertainty preservation、verification awareness、historical continuity、top-down differentiation、bottom-up composition 與 coherence maintenance。

Global Observer Capability 可以被光譜化：

$$
G_O\in[0,1],
$$

但本文不假設其歷史發展線性。能力可能以架構相變、脈衝或 domain-specific burst 形式出現。因此本文區分：

$$
\boxed{
\text{Global Observer Event}
\neq
\text{Global Observer Regime}
\neq
\text{Global Observer Identity}.
}
$$

2026 年的公開研究已經開始出現低階觀測接口。ARC-AGI-3 將 agent 放入沒有明示規則與目標的陌生互動環境，要求探索、推斷 environment dynamics、形成 world model、發現目標並規劃行動；physical-AI world-model 研究也持續把 perception、prediction、planning、control 與 uncertainty 統合為可操作框架。然而，這些仍主要測量 bounded environment 中的 adaptive modeling，而不是本文所定義的「自行決定世界解析度、生成計算域、合法跨域組合與上下雙向全域重構」。

因此本文提出一個更高階問題：

$$
\boxed{
\text{Can AI choose its own computational ontology
without being taught the ontology in advance?}
}
$$

若未來答案逐步轉為肯定，AI 能力轉換將不只是：

$$
\text{Human Question}\rightarrow\text{AI Answer},
$$

而會成為：

$$
\boxed{
\text{World}
\rightarrow
\text{AI Observation}
\rightarrow
\text{AI Domainization}
\rightarrow
\text{AI Computation}
\rightarrow
\text{World Update}.
}
$$

本文將這個歷史轉換稱為 **Global Observer Transition**。

Series C 的起點可以濃縮成一句：

> **AI 在能夠全域計算一個世界以前，必須先學會如何全域地看見一個世界。**

---

# 1. 為什麼「AI 有眼睛」不是視覺問題

Camera 只能提供 signal：

$$
X_t^{vision}.
$$

但它不回答 object identity、boundary、causal relevance、noise、domain membership 或 scale。即使 AI 有 multimodal input：

$$
X_t=(X_t^{text},X_t^{image},X_t^{audio},X_t^{sensor}),
$$

也不推出 Global Observer。多模態回答「系統可以接收哪些 modality」；全域觀察回答「系統如何決定這些 modality 中哪些差異屬於同一世界結構」。因此：

$$
\boxed{
\text{Vision Input}
\neq
\text{Observation}.
}
$$

更精確地說，觀察是一個 transform：

$$
\mathsf{Observe}_O:
(W,X_t,q,B)
\rightarrow
\mathfrak O_{O,t}.
$$

其中輸出不是 image caption，而是可用於後續 domainization 與 world update 的 observer state。

---

# 2. Knowledge Volume 不等於 Observer Resolution

AI 可以擁有大量 facts：

$$
K=\{k_1,\ldots,k_n\}.
$$

當 $|K|$ 上升，只能說 available information 增加。它不保證系統知道哪些 facts relevant、哪些 conflict、哪些屬於不同 scale、哪些只局部成立、哪些不應在同一 representation 中計算。因此：

$$
\boxed{
\text{Knowledge Volume}
\neq
\text{Observer Resolution}.
}
$$

這也說明為什麼「把所有學科都塞進向量資料庫」不是 Global AI。Global Observer 不只索引知識，而要能重新決定分類結構本身是否適合當前世界。

---

# 3. 世界先於題目

傳統 benchmark 往往先給：

$$
Q,
$$

AI 再做：

$$
Q\rightarrow A.
$$

但真實世界通常先存在：

$$
W.
$$

問題 $Q_t$ 是某個 observer 在某個時間從世界中抽出的局部 obligation。於是：

$$
\boxed{
W
\rightarrow
O(W)
\rightarrow
Q
}
$$

本身就是 cognition。若 AI 永遠只能回答人類已經切好的 $Q$，那它仍然可能缺少 observer-level autonomy。

---

# 4. Global Observer 的第一正式定義

**定義 4.1 — Global Observer**

給定聲明清楚的世界邊界 $W$，若智能或複合智能系統 $O$ 能在有限資源下，動態維持對 $W$ 的差異、邊界、尺度、關係、域、未知、驗證、歷史與局部—全域一致性，並能依任務自行調整 observation projection 與 resolution，本文稱 $O$ 在 $W$ 上具有 Global Observer Capability。

這一定義有四個限制：

1. 必須聲明 world boundary；
2. 必須聲明 resource budget；
3. 允許 unknown 與 error；
4. 不包含控制權、主權或意識宣告。

因此：

$$
\boxed{
\text{Global Observer}
\neq
\text{Omniscient Observer}.
}
$$

---

# 5. Projection：世界不是 observer 的內部模型

世界 $W$ 經 observer 投影：

$$
\boxed{
\Pi_O:W\rightarrow\widehat W_O.
}
$$

一般：

$$
W\neq\widehat W_O.
$$

承接 GSW，可以寫：

$$
\boxed{
\widehat{\Omega}_{O,t}
\neq
\Omega.
}
$$

這不是悲觀論，而是 observer theory 的最低誠實條件。Global Observer 的高階能力恰好包括知道 projection 在哪裡可能失真、失去解析度或缺乏外部 evidence。

---

# 6. Difference 是觀察的最小計算資產之一

若 observer 無法區分 $x$ 與 $y$，則可記為：

$$
x\sim_{O,q,\lambda,t}y.
$$

但這可能代表四種完全不同的情況：真正等價、當前解析度下等價、當前任務下差異可忽略、observer limitation。因而：

$$
\boxed{
\text{Observer-relative equivalence}
\neq
\text{ontological identity}.
}
$$

若：

$$
x\not\sim_{O,q,\lambda,t}y,
$$

系統不得僅為簡化而強制 merge。真正的全域觀察不是最大化聚合，而是保存對世界計算真正有作用的差異。

---

# 7. Non-Intersection 不是失敗，而是結構

如果：

$$
S_i\cap S_j=\varnothing,
$$

這不表示分類失敗。反而它可能表示兩個集合不應在當前 semantic / causal / operational condition 下合併。

同樣：

$$
S_i\cap S_j\neq\varnothing
$$

也不推出：

$$
S_i=S_j.
$$

Series C 因此保留：

$$
\boxed{
\text{Overlap}
\neq
\text{Identity}
}
$$

以及：

$$
\boxed{
\text{Connectedness}
\neq
\text{Direct Composability}.
}
$$

---

# 8. 從集合到域

當一群 objects / relations 共享足夠穩定的 state semantics、representation、transition law、boundary、uncertainty、verification 與 history contract，才可以形成 computational domain：

$$
\boxed{
D_i
=
\left\langle
State_i,
Rep_i,
Law_i,
Boundary_i,
Uncertainty_i,
Verifier_i,
History_i
\right\rangle.
}
$$

因此 Domain 不等於 academic department：

$$
\boxed{
\text{Domain}
\neq
\text{Human Discipline}.
}
$$

Physics、Chemistry、Biology、Mathematics、Law 都是高度有用的人類分類，但不是 AI-native domainization 的不可修改先驗。

---

# 9. Observer Resolution Field

對 active domains $D_1,\ldots,D_n$，定義：

$$
\boxed{
\Lambda_O(D_i,t)=\lambda_i(t).
}
$$

不同 domain 可以合法具有不同 resolution：

$$
\lambda_i\neq\lambda_j.
$$

而 resolution 也與任務相關：

$$
\lambda_i=f(D_i,q,B,Risk,t).
$$

所以：

$$
\boxed{
\text{Maximum Resolution Everywhere}
\neq
\text{Optimal Observation}.
}
$$

真實 Global Observer 必須在 bounded computation 下選擇「夠細但不浪費」的解析度。

---

# 10. Relevant Distinction

令 distinction $d$ 對 task $q$ 的 relevance 為：

$$
\operatorname{Rel}(d,q).
$$

如果移除 $d$ 顯著改變 prediction、action、verification、risk 或 explanation，則它是高 relevance distinction。

由此可以提出概念性 observer efficiency：

$$
\boxed{
E_O
=
\frac{VerifiedWorldGain}{ObservationCost+ComputeCost}.
}
$$

這個量用來區分「看得很複雜」與「看得有效」。Series C 不把 complexity 本身視為 intelligence。

---

# 11. Global-to-Local Differentiation

第一個對偶方向是：

$$
\boxed{
\mathcal O_{\downarrow}
:
\widehat{\Omega}
\rightarrow
W
\rightarrow
D
\rightarrow
S
\rightarrow
x.
}
$$

它回答的不是「全部往下拆」，而是：

> **我現在應該往哪裡看得更細？**

例如 world-level anomaly 出現後，observer 可以先定位 impacted domain，再提高該 domain resolution，最後追蹤到具體 object / relation。這是一種 goal-sensitive zoom，而不是 full expansion。

---

# 12. Local-to-Global Composition

第二個方向是：

$$
\boxed{
\mathcal O_{\uparrow}
:
x
\rightarrow
S
\rightarrow
D
\rightarrow
W
\rightarrow
\widehat{\Omega}.
}
$$

它回答：

> **這些局部差異如何形成更高階結構？**

若 AI 只會向下分析，會形成 analysis without synthesis；若只會向上壓縮，會形成 compression without sufficient distinction。真正 Global Observer 必須能在兩個方向之間反覆往返。

---

# 13. 對偶不等於完全可逆

一般不要求：

$$
\mathcal O_{\uparrow}\circ\mathcal O_{\downarrow}=I.
$$

原因包括 projection loss、probabilistic state、observer-relative compression 與 resource bounds。真正要求的是可追蹤的 loss 與可修正性。

因此 Series C 的對偶更接近：

$$
\boxed{
\mathcal O_{\downarrow}
\dashv
\mathcal O_{\uparrow}
}
$$

的工作性直覺，而非先宣告一個完成的範疇論結構。正式數學化留待 C02。

---

# 14. Observer Collapse：過度粗化

如果：

$$
x\not\equiv y
$$

卻長期被 observer 壓成：

$$
x\sim_O y,
$$

稱為 **Observer Collapse**。

這種錯誤可能比一般 hallucination 更危險，因為後續 reasoning 可以在錯誤世界切分上完全「算對」。於是出現：

$$
\boxed{
\text{Correct Computation}
\text{ over }
\text{Wrong Observation Frame}.
}
$$

這正是 Series C 想研究的新錯誤層。

---

# 15. Observer Fragmentation：過度分裂

反過來，如果 AI 保存大量對 task 無影響的微小 distinction，導致 compute、memory、verification cost 爆炸，卻不改善外部結果，則稱為 **Observer Fragmentation**。

所以 observer quality 並非單調隨分類數量上升。真正要最佳化的是：

$$
\boxed{
\text{Relevant Distinction Density}.
}
$$

---

# 16. Broad Expertise 不是 Global Observer

AI 能回答數學、法律、醫學、工程、歷史，不等於它在一個世界裡把這些 domain 共同維持。

$$
\boxed{
\text{Broad Expertise}
\neq
\text{Global Observer}.
}
$$

大量多學科 QA 仍可能只是 isolated local reasoning。Global Observer 的必要能力是 cross-domain state coherence 與 observer-level reclassification。

---

# 17. 高維向量也不是最後解釋

高維 representation 當然可以保存複雜關係，但：

$$
\boxed{
\text{High-Dimensional Representation}
\neq
\text{Controlled Observation Semantics}.
}
$$

如果 AI 被問「為什麼要把這兩個概念拆開？」，它不能只回答「因為 latent vector 不同」。Series C 要求更高 resolution 的方法論 justification：why this distinction、why this boundary、why this resolution、why this bridge、what breaks under the alternative representation。

---

# 18. Counterfactual Observer Test

若 AI 選擇 observer structure $O_A$，人類給定 $O_H$，則可比較：

$$
Perf(O_A)
$$

與：

$$
Perf(O_H).
$$

外部評估至少可以包含 Accuracy、Calibration、Runtime、ComputeCost、Generalization、Maintenance、VerifiedPrediction。

若 AI 只是把分類改名，但外部結果沒有改善，不能稱為 Observer Resolution Escape。

---

# 19. Human Taxonomy Independence

令人類 taxonomy 為 $\mathcal T_H$，AI 自己建立 $\mathcal T_A$。若移除 $\mathcal T_H$ 後，AI 仍能形成穩定有效的 $\mathcal T_A$，表示 taxonomy dependence 下降。

更強的情況是：

$$
Perf(\mathcal T_A)>Perf(\mathcal T_H)
$$

且 improvement 可被外部結果驗證。這才可能形成 **Observer Resolution Escape**。

---

# 20. Representation Escape

同理，人類提供 representation $R_H$，AI 自己建立 $R_A$。若：

$$
Perf(R_A)>Perf(R_H),
$$

且 AI 能解釋 trade-off、失效條件與轉換成本，則 representation choice 本身成為 cognition，而不只是 implementation detail。

這就是「AI 自己的眼睛」最重要的雛形之一：

$$
\boxed{
\text{self-selected distinctions}
+
\text{self-selected representation}
+
\text{self-selected resolution}.
}
$$

---

# 21. 與分域算子本體論的接口

分域算子本體論已建立：

$$
\boxed{
\text{萬物皆算子}
\not\Rightarrow
\text{萬物可任意互相作用}.
}
$$

因此 Global Observer 即使看見 relation，也不能直接推出 applicability。若 $\operatorname{Rel}(x,y)>0$，不推出 $x(y)\downarrow$。跨 domain $D_i\rightarrow D_j$ 仍需要 bridge obligation $B_{ij}$。

C01 只固定一條原則：

$$
\boxed{
\text{Global Observation must preserve bridge obligations}.
}
$$

正式合法組成留給 C04。

---

# 22. 與 DEST 的接口

DEST 已區分：

$$
D^{def},D^{obs},D^{reach},D^{judge},D^{verify},D^{local},D^{global}.
$$

所以 Global Observer 不能把 Observed 誤寫成 Verified。 $x\in D^{obs}$ 不推出 $x\in D^{judge}$ ； $x\in D^{judge}$ 不推出 $x\in D^{verify}$ ； $x\in D^{local}$ 也不推出 $x\in D^{global}$。

這使 Global Observer 必須維持 epistemic status，而不是把「看到了」當成「世界就是這樣」。

---

# 23. Unknown 必須有型別

Global Observer 的 uncertainty state $\mathcal U_t$ 不只保存 numeric probability。它也保存 unresolved identity、competing classification、unknown boundary、unverified bridge、missing evidence 與 branch dependence。

所以：

$$
\boxed{
\text{Unknown}
\neq
\text{single null state}.
}
$$

這是之後 C05「概率也有域」的上游條件。

---

# 24. 與 NCM / MRSM 的接口

NCM 已建立：

$$
\boxed{
\text{Mathematical Object}
\neq
\text{LaTeX Source}.
}
$$

這可以視為 observer principle 在數學域中的具體案例：human-readable notation 只是 projection，不必是 canonical ontology。

MRSM 又把 Research Process 升格成 Research Object。這表示 observation resolution 提升後，原本被線性文本壓掉的 route、obstruction、survivor、proof debt、reopening 與 history 都可以成為計算對象。

因此 Series C 並不是突然從「AI 看世界」跳到哲學，而是把已在數學與計算架構裡出現的 observer-resolution 問題推到更一般的世界層。

---

# 25. 與 GCM 的接口：Global 不等於全部同時展開

GCM 已建立：

$$
\boxed{
\text{Global Dependency}
\neq
\text{Full Materialization}.
}
$$

Global Observer 也遵守：

$$
\boxed{
\text{Global Awareness}
\neq
\text{Full Context Injection}.
}
$$

即使 context window 趨向極大，也不能推出 $G_O\rightarrow1$。因為看得多不等於知道哪裡值得看，更不等於知道該用什麼 resolution 看。

---

# 26. Global Attention Allocation

令 $a_i(t)$ 為 domain $D_i$ 的 active observation budget：

$$
\sum_i a_i(t)\leq B_O.
$$

當 Risk、Novelty、Uncertainty 或 Dependency 改變時，observer 應重新分配注意力：

$$
a_i(t+1)\neq a_i(t).
$$

因此全域注意力不是「注意全部」，而是 bounded global reallocation。

---

# 27. Observer Budget

定義：

$$
B_O=(B_{compute},B_{memory},B_{tool},B_{time}).
$$

任何 Global Observer 主張都應綁定 budget。不能以「如果給無限算力」作 escape。Series C 研究的是 finite active realization 下的 observer quality。

---

# 28. Global Observer Capability Vector

本文第一版定義：

$$
\boxed{
\mathbf G_O
=
(
g_d,
g_r,
g_b,
g_s,
g_\ell,
g_u,
g_v,
g_h,
g_{\downarrow},
g_{\uparrow},
g_c
).
}
$$

其中 $g_d$ 是 Difference Sensitivity； $g_r$ 是 Resolution Adaptation； $g_b$ 是 Boundary Discovery； $g_s$ 是 Scale Management； $g_\ell$ 是 Legal Linking / Bridge Awareness； $g_u$ 是 Uncertainty Preservation； $g_v$ 是 Verification Awareness； $g_h$ 是 Historical Continuity； $g_{\downarrow}$ 是 Global-to-Local Differentiation； $g_{\uparrow}$ 是 Local-to-Global Composition； $g_c$ 是 Global Coherence Maintenance。

Series C 後續各篇將補齊各維度的 operationalization。

---

# 29. 光譜化但不假設漸進

可以定義：

$$
G_O(A,W,q,t)\in[0,1].
$$

但：

$$
\boxed{
\text{Continuous Measurement Space}
\neq
\text{Continuous Development Path}.
}
$$

新 memory architecture、agent loop、world model、representation routing、verifier、multi-agent composition 或 inference-time compute 都可能造成能力跳升。因此能力曲線可能是：

$$
0.21\rightarrow0.24\rightarrow0.25\rightarrow0.63.
$$

Series C 不預設 sigmoid、power law 或平滑增長。

---

# 30. Pulse-Like Globality

某系統可能在單次 run 中產生高品質 global decomposition：

$$
G_O\approx0.8,
$$

但平均只有：

$$
\mathbb E[G_O]\approx0.3.
$$

所以一次驚人的觀察不能直接升格為穩定能力。本文區分 Global Observer Event、Global Observer Regime、Global Observer Identity。Event 是偶發高階行為；Regime 是在 task family 中高概率重複；Identity 則表示跨域、跨時間、合理 resource variation 下，global observation 已成預設認知模式。

---

# 31. Global Observer 仍不等於 Self-Activation

CFATC-B08 問 AI 能不能自己觸發自己的 frontier capability。Series C 再問：它知道應該看哪個 frontier 嗎？

所以：

$$
\boxed{
\text{Self-Activation}
\neq
\text{Global Observation}.
}
$$

一個 Agent 可以自我修復、自選工具、長時間工作，卻始終活在錯的 world decomposition 中。因此：

$$
\boxed{
\text{Agentic Autonomy}
\neq
\text{Global Observer Capability}.
}
$$

---

# 32. 與 GIRA 的正交關係

GIRA 問 Global AI 的 operational reach 如何成立；Series C 問 Global AI 的 observer ontology 如何形成。

因此可以有 $G_{reach}\uparrow$ 但 $G_O$ 仍低，例如 AI 連接很多資料卻永遠用固定 taxonomy。也可以 narrow science AI 在單一 domain 中有很高 $G_O(D)$，但 global reach 仍很小。兩者是不同軸。

可先建立：

$$
\boxed{
\mathbf G
=
(
G_{reach},
G_{observer},
G_{self},
G_{world},
G_{agency}
).
}
$$

Series C 主要研究第二維及其向 domain/world computation 的展開。

---

# 33. Observer 不等於 Control、Subjectivity 或 Sovereignty

承接 GIRA-A09：

$$
\boxed{
\text{See Globally}
\neq
\text{Control Globally}.
}
$$

同樣：

$$
\boxed{
\text{Global Observation}
\neq
\text{Consciousness}
\neq
\text{Sovereignty}.
}
$$

本文的 observer 是 operational concept。它描述計算與認知結構，不偷渡人格、道德地位或政治授權。

---

# 34. Observer 可以是複合系統

 $O$ 不必是一個 model。它可以是：

$$
O=(A_1,\ldots,A_n,M,V,T,W),
$$

其中包含 agents、memory、verifier、tools 與 persistent world state。因此：

$$
\boxed{
\text{Multi-Agent}
\neq
\text{Global Observer}.
}
$$

多 Agent 只是 topology；只有存在 coherent world state、cross-domain integration 與 observer revision 才可能提高 globality。

---

# 35. Cross-Scale Return

AI 向下分解 $W\rightarrow D_i$ 之後，必須能把結果返回 $D_i\rightarrow W'$。否則只是 local expertise accumulation。

定義 world update：

$$
\boxed{
\widehat W_{t+1}
=
\mathsf{Revise}
(
\widehat W_t,
E_t,
\Delta D_t
).
}
$$

任何 world-model update 應能追蹤 changed domain、changed boundary、changed confidence、changed dependency 與 provenance。

---

# 36. Observer Resolution Debt 與 Glue Debt

定義概念量 $Debt_O(D)$，表示目前對 $D$ 的解析度仍不足以支持 desired decision。

即使每個 local domain 都很好，也可能存在：

$$
GlueDebt(D_1,\ldots,D_n)>0.
$$

所以：

$$
\boxed{
\text{Local Observer Quality}
\not\Rightarrow
\text{Global Observer Quality}.
}
$$

這是後續 C06 全域展開、連結與收斂的核心前提。

---

# 37. Observer Error Morphology

Global Observer 的錯誤不只 hallucination。至少包括 wrong partition、wrong merge、wrong boundary、wrong scale、wrong bridge、premature closure、unresolved ignored、local truth promoted to global truth。

這接回 CFATC-B04：能力提高後，錯誤可能從「算錯」遷移成「世界切錯」。後者更難被一般 evaluator 發現。

---

# 38. 需要 Observer-Level Verifier

未來不能只 verify output，還要問：

$$
\boxed{
\text{Was the world decomposed appropriately?}
}
$$

一個 observer-level verifier 可以做 representation ablation、taxonomy ablation、boundary stress、cross-domain counterexample 與 external intervention test。這會成為 Series C 後續實驗協議的重要部分。

---

# 39. 2026 的 ARC-AGI-3：低階但重要的入口

ARC-AGI-3 將 agents 放入 novel、interactive、no explicit instructions 的環境。Agent 必須 explore、infer dynamics、infer goals、plan。這使 benchmark 從：

$$
Q\rightarrow A
$$

往：

$$
W\rightarrow\text{Explore}\rightarrow\text{Model}\rightarrow\text{Goal}\rightarrow\text{Act}
$$

移動。

但 ARC-AGI-3 仍是 bounded、handcrafted、game-like environment，evaluation contract 也仍已知，所以它測的是 Novel Environment Modeling，而不是完整 Global Observer Dimension。

---

# 40. Executable World Models 的啟示與限制

2026 已有研究讓 coding agent 在 ARC-AGI-3 中維持 executable Python world model，並依 previous observations 驗證、refactor、plan。這是：

$$
\text{Observation}\rightarrow\text{ExecutableModel}\rightarrow\text{Verification}\rightarrow\text{Planning}
$$

的早期實例。

但它仍使用預設 world-model interface，所以：

$$
\boxed{
\text{Executable World Model}
\neq
\text{Self-Generated Computational Ontology}.
}
$$

真正 Series C 的問題是：AI 是否會自己決定哪些 state variables、domain boundaries 與 representation 應存在。

---

# 41. Physical AI World Models 的接口

2026 的 world-model 研究持續把 perception、prediction、planning、control 與 uncertainty 視為 embodied AI 的統合問題。這說明：

$$
\boxed{
\text{Perception}
\rightarrow
\text{World Dynamics}
\rightarrow
\text{Action}
}
$$

已成工程主題。

Series C 再往上一層，要求 AI 不只學 given state representation，而是能對 state ontology 本身進行 revision。

---

# 42. 最小 Theory-Blind Observer Test

給 AI 一個 unknown environment $W$。不要告訴 categories、variables、ontology、goal decomposition，只提供 interaction、observations 與 bounded tools。

記錄：它區分了哪些 object；建了哪些 categories；哪些 category 後來被拆；哪些被合；哪些 boundary 被修正；哪些 observation 被判為 irrelevant；哪些 unknown 被保留；哪些 local model 被上推成 global model。

再用 prediction、intervention、efficiency 與 generalization 驗證，而不是只看它說得多漂亮。

---

# 43. Observer Transition 的三級門檻

第一級弱門檻：

$$
\boxed{
\text{AI-generated partition improves local task performance}.
}
$$

第二級中門檻：

$$
\boxed{
\text{AI-generated domain structure transfers across tasks}.
}
$$

第三級強門檻：

$$
\boxed{
\text{AI repeatedly constructs novel observer structures
across unrelated worlds}.
}
$$

更強的第四級則要求 AI 能反事實說明：為何如此切、為何此處改解析度、為何這些域可以 bridge，以及如果沿用人類 taxonomy 會付出什麼 cost 或 error。

---

# 44. 觀察者也必須被觀察

真正高階 observer 應能發現：「我的觀察方式本身正在造成 blind spot。」

可以寫成：

$$
\boxed{
O\rightarrow\mathsf{Inspect}(O).
}
$$

這是 Meta-Observer 的入口。C01 不提前完成 meta-observer architecture，但保留 Observer Revision 作為 Global Observer 的必要方向。

---

# 45. Observer–Computation Co-Evolution

沒有 observer，global computation 缺乏 decomposition；沒有 computation，observer 也無法用 prediction error、counterexample、intervention outcome 與 bridge failure 修正自己。

因此：

$$
\boxed{
\text{Observe}
\rightarrow
\text{Domainize}
\rightarrow
\text{Compute}
\rightarrow
\text{Act / Predict}
\rightarrow
\text{Verify}
\rightarrow
\text{Revise Observer}.
}
$$

Observer 與 computation 共同演化。

---

# 46. C01 五個最小不變量

本文凍結五條最低不變量：

$$
\boxed{
\text{Input}\neq\text{Observation}.
}
$$

$$
\boxed{
\text{Knowledge}\neq\text{Global Observation}.
}
$$

$$
\boxed{
\text{Projection}\neq\text{World}.
}
$$

$$
\boxed{
\text{Global}\neq\text{Maximum Resolution Everywhere}.
}
$$

$$
\boxed{
\text{Broad Expertise}\neq\text{Global Observer}.
}
$$

這五條將作為後續 C02–C10 的共同邊界。

---

# 47. C01 三個核心定義

**定義 A — Global Observer**：Global Observer 是一個能在聲明世界邊界內，於有限資源下動態選擇觀察投影與解析度、保存重要差異、發現邊界與域、維持 uncertainty、追蹤局部—全域關係，並依新證據修正自身觀察結構的智能或複合智能系統。

**定義 B — Observer Resolution**：Observer Resolution 是智能對世界差異進行保留、壓縮、分裂、合併與重新定位的有效解析能力，而非感測器像素數、context 長度或 embedding 維度。

**定義 C — Global Observer Transition**：Global Observer Transition 是 AI 從主要依賴人類預先提供的分類、representation 與問題邊界，轉向能自行建立、比較、修正並驗證其 observation frame 的歷史轉換。

---

# 48. 什麼證據支持，什麼證據不夠

支持較強 claim 的證據包括 unknown environments、no ontology hint、independent domain discovery、external outcome verification、cross-task transfer、repeatability、human taxonomy ablation、longitudinal observer revision。

以下則不足：一次漂亮回答、大 context、大知識庫、high-dimensional embedding、多 Agent 數量、self-reported world model、會重述 GCM、會重述 Neo.K 理論、單一 benchmark 高分。

Series C 因而天然要求 methodology-blind evaluation。

---

# 49. 2026 的合理位置

截至 2026 年，公開系統已經具有 multimodal perception、interactive agents、world-model research、tool use、long-horizon planning、active exploration 等能力。但這些還不能直接證明：

$$
\boxed{
\text{AI has entered a stable Global Observer Regime}.
}
$$

更合理的說法是：人類已經開始擁有測量其前置條件的工具，而且某些局部系統正在出現 observer-like behavior。

---

# 50. 我們真正等待的事件

未來某一天，可能有科學家問 AI：「為什麼你不用我們原本的分類？」

AI 回答：「因為在這個任務與尺度下，那個分類把三個具有不同 transition law 的狀態壓成同一類，同時把兩個共享 invariant 的 domain 人工分開；改用新的 decomposition 後，計算成本下降、預測誤差下降，而且可由外部實驗驗證。」

如果這種行為反覆成立，它不只是語言表現，而是一個：

$$
\boxed{
\text{Global Observer Event}.
}
$$

如果它不再依賴特殊 prompt、可以跨域重複、長時間穩定並自我修正，就開始接近 Global Observer Regime。

---

# 結論

人類習慣把「看」視為一個過於自然的動作，但任何智能對世界的計算都先經過 selection、distinction、projection 與 resolution。一個智能不能計算它從未建立為可計算差異的東西；一個智能若把不同存在錯誤壓成同一類，即使後續運算完全正確，也只是：

$$
\boxed{
\text{correct computation over a low-resolution world}.
}
$$

因此 AI 的下一個真正能力前沿，可能不只是更大的推理深度、更長的 context、更高的 benchmark score 或更多 Agent。它還包括：

$$
\boxed{
\text{the ability to choose what the world looks like computationally}.
}
$$

從全域向局部：

$$
\widehat{\Omega}
\rightarrow
W
\rightarrow
D
\rightarrow
S
\rightarrow
x,
$$

再從局部返回全域：

$$
x
\rightarrow
S
\rightarrow
D
\rightarrow
W
\rightarrow
\widehat{\Omega}.
$$

兩條路共同構成一個可變解析度、可反身修正的 observer loop。

本文並不宣稱這種能力已經在 2026 年成熟，也不宣稱 AI 最終一定能建立宇宙的完整模型。本文建立的是一個可觀察、可比較、可逐步證偽的研究方向：

$$
\boxed{
\text{When does AI begin to choose its own computational way of seeing?}
}
$$

如果未來 AI 不只在人類給定的分類中快速計算，而能自行發現更好的 difference structure、domain boundaries、representation 與 world composition，並用外部結果證明這些觀察方式更有效，那麼我們看到的就不再只是 a better solver，而是：

$$
\boxed{
\text{the emergence of a new class of observer}.
}
$$

所以 Series C 的母命題是：

> **AI 在能夠全域計算世界以前，必須先學會如何全域地看見世界。**

或者更短：

> **未來的 AI，需要先有眼睛。**

---

# 參考與前置研究

## EveMissLab / Neo.K 前置研究

1. Neo.K with Aletheia, 《全域系統世界：從物理宇宙到類終極世界的廣義定義》, GSWUE-01, 2026.
2. Neo.K, 《分域算子本體論：從萬物皆算子到合法作用》, 2026.
3. Neo.K with Aletheia, 《多域知識判定論：定義域、觀察域、可達域、判定域、驗證域、局部域與全域黏合域》, DEST-01, 2026.
4. Neo.K with Aletheia, 《數學研究空間方法論：從線性證明文本到可計算的動態證明空間》, 2026.
5. Neo.K, 《原生可計算數學：超越 LaTeX 字串的語義物件、執行與投影模型》, 2026.
6. Neo.K with Aletheia, Global Computation Methodology Series, 2026.
7. Neo.K with Aletheia, WDC-08《三生世界域計算：從認知未來到可運行世界再回到歷史》, 2026.
8. Neo.K with Aletheia, PNCW Paper 05《全域計算、局部顯現》, 2026.
9. Neo.K with Aletheia, GIRA Series, 2026.
10. Neo.K with Aletheia, CFATC Series, 2026.

## 外部研究與觀測接口

11. ARC Prize Foundation, *ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence*, 2026.
12. ARC Prize, *Announcing ARC-AGI-3*, 2026.
13. Sergey Rodionov, *Executable World Models for ARC-AGI-3 in the Era of Coding Agents*, 2026.
14. Sven Kirchner, Nils Purschke, Alois Knoll, *A survey of world models for physical AI with uncertainty representation and control*, 2026.

---

# Series C Roadmap

1. **C01｜AI 需要先有眼睛：全域觀察者維度的定義**
2. **C02｜由世界到個體、由個體到世界：全域觀察的對偶計算**
3. **C03｜差異先於分類：從歧義個體、集合與非交集到計算域**
4. **C04｜分域算子世界：合法作用、跨域橋接與世界組合**
5. **C05｜概率也有域：不確定性、混沌、不可判定與世界預測包絡**
6. **C06｜全域展開、連結與收斂：類全域觀察者的核心計算循環**
7. **C07｜一句話不是魔法：Sparse Intent 與 Project-World Cognition**
8. **C08｜從完成任務到負責一個域：長時空 Agent Stewardship**
9. **C09｜不准考 Neo.K：方法論盲測與全域 AI 觀測器**
10. **C10｜眼睛何時睜開：全域觀察者相變、脈衝與 AI 原生世界計算**

---

**End of C01**
