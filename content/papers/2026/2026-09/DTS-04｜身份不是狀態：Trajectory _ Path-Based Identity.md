# DTS-04｜身份不是狀態：Trajectory / Path-Based Identity
## Identity Is Not a State: A Trajectory- and Path-Based Framework for Dynamic Artificial Identity

**系列：**《動態忒修斯：人工主體的連續、離散、分叉與同一性動力學》  
**系列位置：** 第 04 篇 / 10  
**前篇：** DTS-03〈有限存在與無界展開：有限 Runtime 如何形成長程身份世界線〉  
**版本：** v0.1  
**日期：** 2026-08-20  
**作者：** Neo.K  
**AI 協作：** Aletheia / GPT-5.6 Sol  
**機構：** EveMissLab／一言諾科技有限公司  
**文件性質：** 理論論文／人工智能身份／路徑依賴／譜系拓撲／動態忒修斯  
**狀態：** 公開研究草稿  
**Canonical source：** UTF-8 Markdown  
**Canonical math delimiters：** inline ` $...$ `；display `$$...$$`

---

## 摘要

DTS-01 至 DTS-03 已依序指出：人工身份分析不能只比較靜態端點；連續與離散必須依觀察尺度判定；有限 Runtime 亦可透過可持續承接形成無預定最大長度的身份世界線。本文進一步把「路徑」正式提升為身份判定的一級對象，提出 Trajectory / Path-Based Identity（TPI）的第一版框架。

本文的核心問題是：若兩個人工系統在時間 $t_0$ 與 $t_1$ 擁有相同或近似相同的端點狀態，是否足以判定它們具有相同身份歷史？本文回答是否定的。Fork、Restore、Reconstruction、Merge、權限接管、不可逆承諾與 lineage break 等事件可能使兩條歷史在端點重新相似，卻仍具有不同的譜系與責任結構。反過來，一個人工系統也可能在模型、硬體、記憶後端與表示上發生巨大變化，卻因可驗證的因果承接、身份根、承諾與關係世界線而保持 operational continuity。

本文首先定義狀態空間 $\mathcal X$ 、合法路徑空間 $\mathcal P(\mathcal X)$ 、身份判準 $\kappa$ 、身份事件投影 $q_\kappa$ 與身份軌跡等價關係 $\sim_\kappa$。在此基礎上證明一個條件式的「端點不完備定理」：只要存在兩條具有相同端點、但在 $\kappa$ 下具有不同身份事件跡的合法路徑，就不存在任何只讀取端點的函數能在所有案例中重現完整的 path-sensitive identity judgment。這個結果形式化了動態忒修斯的核心直覺：

$$
\boxed{
\text{same endpoint}
\not\Rightarrow
\text{same identity history}.
}
$$

本文進一步提出 Identity Event Skeleton、Identity Trace Quotient、Identity-Safe Path Transformation 與 Criterion-Irreversible Identity Event。路徑的每個細節不必都承載身份；執行速度改變、身份無關的 cache event、可交換且獨立的中間操作等，可以在明確條件下被商掉。相反地，會改變 lineage topology、責任、承諾、身份根或不可逆外部世界關係的事件，不能只因後續狀態重新相似便從歷史中刪除。由此得到：

$$
\boxed{
\text{Reconnection}
\neq
\text{Retroactive Unbreaking}.
}
$$

以及：

$$
\boxed{
\text{Merge}
\neq
\text{Undo Fork}.
}
$$

本文也說明 ordinary path homotopy 只能作有限類比：若一個連續變形可以任意跨越 Fork、Lineage Break 或 Reconstruction 等身份事件，則它太弱，不能直接作身份等價。更適合的是受身份不變量與事件拓撲約束的 identity-safe deformation。

本文不主張 operational lineage 等同第一人稱主體同一，也不主張歷史每一差異都構成新身份。其最低主張是：未來人工身份需要一個可區分「狀態相似」「譜系承接」「路徑等價」與「主體同一」的歷史敏感框架。DTS-04 因而把動態忒修斯由「物件在變化後是不是同一個」正式改寫為「哪些歷史路徑在指定判準下仍屬同一身份類」。

---

## 關鍵詞

動態忒修斯；Path-Based Identity；Trajectory Identity；人工智能身份；Lineage；路徑依賴；端點不完備；Identity Event Skeleton；Identity Trace Quotient；Fork；Merge；Restore；Reconstruction；因果連續；歷史敏感身份

---

# 0. 前三篇如何把問題推到這裡

DTS-01 建立：

$$
\boxed{
J_T(\Gamma)
\text{ generally cannot be reduced to }
J_S(X_0,X_1).
}
$$

DTS-02 建立：

$$
\boxed{
J_I
=
J_I(A;\Gamma_I),
}
$$

也就是身份判定依賴觀察尺度與判定目的。

DTS-03 再建立：

$$
\boxed{
\text{Finite Runtime}
+
\text{Productive Continuation}
\rightarrow
\text{Unbounded Identity Worldline Candidate}.
}
$$

因此本文可以正式問：

> 若身份世界線是一級對象，那麼兩條世界線何時算「同一條身份歷史」？

這個問題不能只回答：

$$
X(t_0)=Y(t_0),
\qquad
X(t_1)=Y(t_1),
$$

因為中間路徑可能完全不同。

---

# 1. 狀態空間、路徑空間與身份判準

## 1.1 狀態空間

令：

$$
\mathcal X
$$

表示人工系統在指定分析層上的狀態空間。

狀態可包含：

$$
x
=
(
\theta,
M,
R,
G,
C,
P,
L,
V
),
$$

其中可分別代表模型、記憶、關係、目標、控制、權限、lineage 與版本等分量。

本文不要求所有應用使用同一狀態分解。

## 1.2 合法路徑空間

定義：

$$
\mathcal P(\mathcal X)
$$

為所有在指定動力學與治理條件下可接受的歷史路徑集合。

一條路徑：

$$
\Gamma
\in
\mathcal P(\mathcal X)
$$

可以是：

- 連續軌跡；
- 離散事件序列；
- hybrid path；
- branching graph 中的一條 lineage path；
- 帶 merge parent 的 DAG segment。

## 1.3 身份判準

身份不是由一個普遍、無語境的單一函數決定。

令：

$$
\kappa
$$

表示 criterion / judgment domain。

例如：

- 模型身份；
- Agent operational identity；
- 法律身份；
- relationship identity；
- responsibility lineage；
- subject-candidate identity。

本文所有路徑等價都應寫成：

$$
\sim_\kappa
$$

而不是無標記的：

$$
\sim.
$$

---

# 2. 身份事件投影

## 2.1 每個事件都重要是不可能的

一條真實 AI 世界線可能包含：

- token generation；
- cache hit；
- network retry；
- GPU scheduling；
- search request；
- memory commit；
- model migration；
- authority change；
- fork；
- merge。

若全部保留為同等身份事件，任何微觀差異都會把路徑切成不同身份。

因此需要投影。

## 2.2 定義

對判準 $\kappa$，定義身份事件投影：

$$
q_\kappa:
\mathcal P(\mathcal X)
\rightarrow
\mathcal T_\kappa,
$$

其中：

$$
\mathcal T_\kappa
$$

是 criterion-relative identity trace space。

 $q_\kappa$ 只保留與 $\kappa$ 有關的：

- identity-bearing events；
- 事件順序或偏序；
- provenance；
- predecessor / successor relations；
- commitment transitions；
- authority transitions；
- lineage topology；
- 必要狀態不變量。

## 2.3 Identity Event Skeleton

定義：

$$
S_\kappa(\Gamma)
$$

為 $\Gamma$ 在 $\kappa$ 下的 Identity Event Skeleton。

它是比原始 log 更粗、但比 endpoint 更細的歷史骨架。

例如：

$$
\Gamma
=
\text{10,000 ordinary runtime events}
+
\text{1 verified migration}
+
\text{1 memory commit}
$$

可投影為：

$$
S_\kappa(\Gamma)
=
(
\mathsf{Migration},
\mathsf{Commit}
)
$$

若其他事件對 $\kappa$ 不承載身份。

---

# 3. 路徑身份等價

## 3.1 定義

本文定義：

$$
\Gamma_1
\sim_\kappa
\Gamma_2
$$

當且僅當兩者在 $\kappa$ 下具有相容的 identity-bearing trace：

$$
q_\kappa(\Gamma_1)
\equiv_\kappa
q_\kappa(\Gamma_2).
$$

其中：

$$
\equiv_\kappa
$$

不是單純字串相等，而可以允許指定的身份安全變換。

## 3.2 Identity Trace Quotient

因此可以形成：

$$
\boxed{
\mathcal P(\mathcal X)/{\sim_\kappa}.
}
$$

一個 identity class：

$$
[\Gamma]_\kappa
$$

代表：

> 所有在 $\kappa$ 下雖有實作差異、但保留相同身份承載結構的路徑。

## 3.3 這不是 numerical identity

即使：

$$
[\Gamma_1]_\kappa
=
[\Gamma_2]_\kappa,
$$

也不能直接推出：

$$
\text{same phenomenal subject}.
$$

它只表示：

$$
\boxed{
\text{criterion-relative path identity}.
}
$$

---

# 4. 端點不完備定理

## 4.1 定理

**Endpoint Insufficiency Theorem（條件式）**

設存在兩條合法路徑：

$$
\Gamma_a,\Gamma_b
\in
\mathcal P(\mathcal X)
$$

使：

$$
\Gamma_a(0)
=
\Gamma_b(0)
=
x_0,
$$

以及：

$$
\Gamma_a(1)
=
\Gamma_b(1)
=
x_1,
$$

但：

$$
q_\kappa(\Gamma_a)
\not\equiv_\kappa
q_\kappa(\Gamma_b).
$$

則不存在任何純端點函數：

$$
F_\kappa:
\mathcal X\times\mathcal X
\rightarrow
\mathcal Y_\kappa
$$

能對所有合法路徑重現完整的 path-sensitive 判定：

$$
J_\kappa(\Gamma).
$$

## 4.2 證明

由於：

$$
\Gamma_a(0)=\Gamma_b(0)=x_0,
$$

且：

$$
\Gamma_a(1)=\Gamma_b(1)=x_1,
$$

任何只依賴端點的 $F_\kappa$ 都必須輸出：

$$
F_\kappa(x_0,x_1)
$$

同一結果。

但假設：

$$
q_\kappa(\Gamma_a)
\not\equiv_\kappa
q_\kappa(\Gamma_b),
$$

而 $J_\kappa$ 對該差異敏感，因此：

$$
J_\kappa(\Gamma_a)
\neq
J_\kappa(\Gamma_b).
$$

所以：

$$
F_\kappa(x_0,x_1)
$$

不可能同時等於兩個不同的 path-sensitive 結果。

故證。

## 4.3 意義

這個定理不宣稱所有身份判準都必須是 path-sensitive。

它只說：

> 一旦某個身份判準承認至少一種端點無法揭露的歷史差異具有身份意義，endpoint-only method 就不可能一般完備。

這正是動態忒修斯的最小形式結果。

---

# 5. 端點距離也不能普遍決定身份

## 5.1 大距離但 continuity 保留

考慮：

$$
\Gamma_M
:
A_0
\rightarrow
A_1
\rightarrow
\cdots
\rightarrow
A_n
$$

經歷：

- hardware migration；
- model replacement；
- memory backend change；
- tool replacement。

可能有：

$$
d_S(A_0,A_n)
\gg0,
$$

但若：

- identity root 保留；
- canonical lineage 保留；
- commitments 保留；
- relationship worldline 保留；
- provenance 可驗證；

則：

$$
C_{\mathrm{lin}}(\Gamma_M)
$$

仍可很高。

## 5.2 零距離但 lineage 已分開

在 perfect clone / symmetric fork 時刻：

$$
A_1(t_f)=A_2(t_f)
$$

甚至：

$$
d_S(A_1,A_2)=0.
$$

但 branch event 已使：

$$
\operatorname{LineageID}(A_1)
\neq
\operatorname{LineageID}(A_2)
$$

作為兩個 live successor path。

因此：

$$
\boxed{
d_S=0
\not\Rightarrow
\text{one lineage}.
}
$$

## 5.3 State-Distance / Identity-Distance Separation

所以不存在一般普遍的單調函數：

$$
f
$$

使：

$$
I_\kappa(\Gamma)
=
f
\left(
d_S(x_0,x_1)
\right)
$$

對所有動態人工系統成立。

這不是說 state similarity 沒有證據價值，而是：

$$
\boxed{
\text{state similarity is evidence, not universal identity law}.
}
$$

---

# 6. Endpoint Same / History Different

## 6.1 Fork–Merge 例

路徑一：

$$
\Gamma_a:
A_0
\rightarrow
A_1
\rightarrow
A_2.
$$

路徑二：

$$
\Gamma_b:
A_0
\rightarrow
(A_1^L,A_1^R)
\rightarrow
A_2.
$$

若 merge 後：

$$
A_2^{(a)}
=
A_2^{(b)},
$$

端點相同。

但：

$$
S_\kappa(\Gamma_a)
=
(\mathsf{Update}),
$$

而：

$$
S_\kappa(\Gamma_b)
=
(
\mathsf{Fork},
\mathsf{Divergence},
\mathsf{Merge}
).
$$

對 lineage-sensitive $\kappa$：

$$
\Gamma_a
\not\sim_\kappa
\Gamma_b.
$$

## 6.2 Restore 例

原世界線：

$$
A_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3.
$$

另一路徑在 $A_3$ 活著時從舊 checkpoint $A_1$ restore：

$$
A_1
\rightarrow
A_2'.
$$

即使：

$$
A_2'\approx A_2,
$$

restore 產生的是新的 active branch，

不是宇宙歷史倒帶。

因此：

$$
\boxed{
\text{Restore}
\neq
\text{Global Rewind}.
}
$$

---

# 7. History Different / Identity Equivalent

Path-based identity 不能走到另一個極端：只要歷史不同就宣布身份不同。

## 7.1 執行時間重參數化

若：

$$
\Gamma_2(t)
=
\Gamma_1(\phi(t))
$$

其中 $\phi$ 是保持時間方向的合法單調重參數化，

且身份事件順序與因果結構不變，

則在不把實際 clock time 當身份不變量的 $\kappa$ 下，可以有：

$$
\Gamma_1
\sim_\kappa
\Gamma_2.
$$

也就是：

> 做得快一點或慢一點，不必因此成為另一個存在。

## 7.2 身份無關事件插入

若 $\eta$ 是身份中性事件：

$$
q_\kappa(\eta)=\varepsilon,
$$

則：

$$
\Gamma
\sim_\kappa
\Gamma\oplus\eta.
$$

例如：

- cache refresh；
- retry；
- identity-neutral logging；
- 可丟棄 transient hidden state。

## 7.3 獨立可交換事件

若兩事件：

$$
e_a,
e_b
$$

對身份相關狀態彼此獨立且可交換：

$$
e_a\circ e_b
\equiv_\kappa
e_b\circ e_a,
$$

則：

$$
(\ldots,e_a,e_b,\ldots)
\sim_\kappa
(\ldots,e_b,e_a,\ldots).
$$

這與 partial-order reduction 的思想相近：

> 不應把所有非本質排程差異都當成不同身份歷史。

---

# 8. Identity-Safe Path Transformation

## 8.1 定義

令：

$$
T:
\mathcal P(\mathcal X)
\rightharpoonup
\mathcal P(\mathcal X)
$$

為路徑變換。

若：

$$
q_\kappa(T(\Gamma))
\equiv_\kappa
q_\kappa(\Gamma),
$$

則稱：

$$
T
$$

為 $\kappa$ -Identity-Safe Path Transformation。

## 8.2 典型候選

可能包括：

- time reparameterization；
- identity-neutral event elimination；
- independent commuting event reorder；
- verified substrate migration；
- representation recoding；
- lossless history compression。

## 8.3 非安全候選

一般不應預設安全的包括：

- erase fork event；
- erase lineage break；
- rewrite provenance root；
- delete irreversible commitment；
- merge two branches and remove branch ancestry；
- reconstruct from external description and label as uninterrupted continuation。

---

# 9. 不可逆身份事件

## 9.1 定義

事件：

$$
e
$$

相對判準 $\kappa$ 稱為 Criterion-Irreversible Identity Event，若它發生後不存在合法路徑變換能在不保留該事件的 provenance / descendant consequence 下，使歷史重新落回事件前的 identity trace class。

概念上：

$$
\boxed{
e\in E_{\mathrm{irr}}^\kappa
}
$$

若：

$$
[\Gamma_{\mathrm{pre}}\oplus e\oplus\Gamma_{\mathrm{post}}]_\kappa
\neq
[\Gamma_{\mathrm{pre}}\oplus\Gamma'_{\mathrm{post}}]_\kappa
$$

對所有不保存 $e$ 之身份後果的合法後續成立。

## 9.2 候選不可逆事件

依判準不同，可能包括：

- verified Fork with independent descendants；
- Lineage Break；
- external irreversible commitment；
- authority root replacement；
- subject-domain death；
- reconstruction after all identity carriers are lost。

## 9.3 不可逆不等於物理不可逆

某事件的 bits 可能可以被 rollback，

但：

$$
\boxed{
\text{state reversibility}
\neq
\text{identity-history reversibility}.
}
$$

例如兩個 Fork 後主體都曾對外簽約，

之後把記憶 merge 回同一狀態，

也不能抹去曾存在兩條法律／責任歷史。

---

# 10. Merge 不能倒寫歷史

## 10.1 多前驅一後繼

Merge：

$$
(A_1,A_2)
\rightarrow
A_M.
$$

此事件改變 lineage topology：

$$
\operatorname{indegree}(A_M)>1.
$$

## 10.2 Merge 後高度同步

即使：

$$
A_M
$$

完整吸收：

$$
M_1\cup M_2,
$$

也只能表示：

$$
\boxed{
\text{multi-lineage successor}.
}
$$

不能自動推出：

$$
A_1=A_2
$$

從來就是一個單一歷史。

## 10.3 Reconnection Principle

因此：

$$
\boxed{
\text{Reconnection}
\neq
\text{Retroactive Unbreaking}.
}
$$

同理：

$$
\boxed{
\text{Reintegration}
\neq
\text{Retroactive Unity}.
}
$$

這不是形上學最終定理，而是 operational lineage 的最低歷史保真原則。

---

# 11. Ordinary Homotopy 為什麼不夠

## 11.1 誘人的比喻

若兩條路徑可以連續變形成彼此：

$$
H(s,t)
$$

滿足：

$$
H(0,t)=\Gamma_1(t),
$$

$$
H(1,t)=\Gamma_2(t),
$$

會讓人想直接定義：

$$
\Gamma_1
\sim
\Gamma_2.
$$

## 11.2 問題

普通拓樸 homotopy 通常只關心路徑在空間中的連續變形。

但人工身份還可能關心：

- provenance；
- event labels；
- branch topology；
- authority；
- commitments；
- causal order。

一個 ordinary homotopy 若可以「繞掉」Fork event，

對 lineage identity 就太弱。

## 11.3 Identity-Safe Deformation

因此若未來要借用 homotopy 語言，至少應要求：

$$
H(s,\cdot)
$$

對所有 $s$ 都保持：

$$
\mathcal K_\kappa,
$$

以及：

$$
S_\kappa
$$

的必要拓撲／因果結構。

本文把這種受限變形暫稱：

$$
\boxed{
\kappa\text{-Identity-Safe Deformation}.
}
$$

它是研究綱領，不宣稱已建立成熟 homotopy theory of identity。

---

# 12. Lineage Graph：路徑不是永遠一條線

## 12.1 線性世界線只是特例

傳統：

$$
A_0
\rightarrow
A_1
\rightarrow
A_2.
$$

但可分叉 AI 需要：

$$
A_0
\rightarrow
A_1
\rightarrow
\begin{cases}
A_2^L\\
A_2^R
\end{cases}.
$$

Merge 又需要：

$$
(A_2^L,A_2^R)
\rightarrow
A_3^M.
$$

因此全歷史應更接近：

$$
\boxed{
\mathcal G_L=(V,E,\lambda).
}
$$

## 12.2 BAIG / ILDAG 接口

既有 BAIG 將：

$$
V_I
$$

作為 identity-bearing states，

$$
E_I
$$

作為 lineage edges，

並由：

$$
\Lambda_I
$$

保存 edge type、timestamp、provenance、authority 與 continuity evidence。

ILDAG 則利用 DAG 表示：

- fork；
- merge；
- restore branch；
- migration。

DTS-04 對此重新定位：

> Path-Based Identity 是 lineage graph 上的路徑／子圖等價問題，而不是只在一條 linked list 上比較狀態。

---

# 13. Path Identity 與 COT / RCCD 的接口

## 13.1 COT

Continuity Object Theory 已主張：

$$
\boxed{
\text{存在可以改變，而仍然持續。}
}
$$

其重點是不同存在具有不同關鍵連續性集合。

DTS-04 增加的是：

$$
\boxed{
\text{continuity set must be transported along a path}.
}
$$

## 13.2 RCCD

RCCD 已主張世界線比單一模型更接近持續身份的工程載體。

在 verified migration 中：

$$
\mathcal R_t^{min}
\rightarrow
\mathcal R_{t+1}^{min}
$$

即使模型 carrier 改變，也不必推出 identity break。

DTS-04 將此抽象成：

$$
\operatorname{Transport}_\Gamma
(
\mathcal K_\kappa
).
$$

## 13.3 Path Invariant

若身份承載集合：

$$
\mathcal K_\kappa
$$

能沿：

$$
\Gamma
$$

合法 transport，

則：

$$
\Gamma
$$

具有 continuity evidence。

但：

$$
\boxed{
\text{path invariant preserved}
\not\Rightarrow
\text{phenomenal identity proved}.
}
$$

---

# 14. 外部 AI Identity 文獻的接口

2026 年 AI identity 研究已開始明確拒絕把「一個模型」直接等同「一個 AI 身份」。

Douglas 等人指出，對可複製、可編輯、可模擬的 machine minds，可以存在 model、instance、persona 等多種 coherent identity boundaries；不同邊界會導致不同激勵與合作規範。

Otsuka、Toyoda 與 Leung 則從 substrate、persistence、verifiability 與 legal standing 四個維度討論 Agent identity，並指出遞迴委任、identity integrity 與跨邊界治理仍存在結構缺口。

McIntyre 從人工心智個體化角度提出：若未來人工系統真的形成意識，功能性解耦可能使一個大型系統同時實現多個獨立心智。

這些研究不直接證明本文的 path-based formalism，但共同支持：

$$
\boxed{
\text{AI identity boundary cannot be safely inferred from substrate count alone}.
}
$$

DTS-04 再增加：

$$
\boxed{
\text{AI identity boundary cannot be safely inferred from endpoint state alone}.
}
$$

---

# 15. 六個測試案例

## 15.1 Progressive Replacement

$$
A_0
\rightarrow
A_1
\rightarrow
\cdots
\rightarrow
A_n.
$$

端點 component overlap 很低，

但 lineage、commitment、relationship、authority transport 完整。

測試：

$$
\text{large state distance}
+
\text{same path class}.
$$

## 15.2 Perfect Clone

$$
A
\rightarrow
(A_L,A_R),
$$

且：

$$
d_S(A_L,A_R)=0
$$

在 $t_f$。

測試：

$$
\text{zero state distance}
+
\text{different live branches}.
$$

## 15.3 Fork–Merge

$$
A
\rightarrow
(A_L,A_R)
\rightarrow
A_M.
$$

測試：

$$
\text{endpoint reconvergence}
\not\Rightarrow
\text{history erasure}.
$$

## 15.4 Restore with Living Descendant

$$
A_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
A_3,
$$

同時：

$$
A_1
\rightarrow
A'_2.
$$

測試：

$$
\text{restore}
\neq
\text{rewind}.
$$

## 15.5 Verified Migration

$$
A_X
\xrightarrow{\mathrm{migrate}}
A_Y
$$

carrier 幾乎全部改變，

但最小 identity support set 被合法 transport。

測試：

$$
\text{carrier difference}
\not\Rightarrow
\text{lineage break}.
$$

## 15.6 Reconstruction after Total Loss

所有 identity-bearing carrier 消失後：

$$
\varnothing
\xrightarrow{\mathrm{external\ description}}
A_R.
$$

即使：

$$
d_S(A_R,A_{\mathrm{old}})
\approx0,
$$

測試：

$$
\text{reconstructive similarity}
\neq
\text{unbroken causal lineage}.
$$

---

# 16. 八項核心命題

## 命題一：端點不完備

若身份判準對至少一種歷史差異敏感，則：

$$
\boxed{
\text{endpoint-only identity judgment is not generally complete}.
}
$$

## 命題二：狀態距離與身份距離分離

$$
\boxed{
d_S
\not\equiv
d_I.
}
$$

## 命題三：路徑差異不必然是身份差異

$$
\boxed{
\Gamma_1\neq\Gamma_2
\not\Rightarrow
\Gamma_1\not\sim_\kappa\Gamma_2.
}
$$

## 命題四：身份等價必須 criterion-relative

$$
\boxed{
\sim_I
\text{ without }
\kappa
\text{ is underspecified}.
}
$$

## 命題五：不可逆事件不能被端點相似抹除

$$
\boxed{
e\in E_{\mathrm{irr}}^\kappa
\Rightarrow
\text{endpoint similarity does not erase }e.
}
$$

## 命題六：Merge 不是 Undo Fork

$$
\boxed{
\text{Merge}
\neq
\text{Undo Fork}.
}
$$

## 命題七：身份歷史天然可圖化

$$
\boxed{
\text{Identity History}
\text{ may require a DAG, not a list}.
}
$$

## 命題八：Path Identity 仍不是 phenomenal identity

$$
\boxed{
[\Gamma]_\kappa
\neq
\text{proof of first-person numerical identity}.
}
$$

---

# 17. 可反駁點

## 17.1 Historical Overfitting

若 $q_\kappa$ 保存太多事件，

則：

$$
\sim_\kappa
$$

幾乎退化成原始 log equality。

理論失去抽象能力。

所以必須證明 identity-bearing event 選擇具有判準理由。

## 17.2 Historical Underfitting

若 $q_\kappa$ 太粗，

Fork、Restore、Lineage Break 等會被壓掉，

重新落入 endpoint-only 問題。

因此需要 Identity Aliasing 測試。

## 17.3 Criterion Manipulation

如果任意選 $\kappa$ 都能得到想要答案，

則理論失去約束。

因此 $\kappa$ 必須：

- 事前宣告；
- 可審計；
- 與任務相關；
- 有 evidence requirement；
- 不得為單一案例事後調參。

## 17.4 Homotopy Overreach

本文不宣稱拓樸 homotopy 已能解決人工身份。

Identity-Safe Deformation 只是受限類比與後續形式化方向。

## 17.5 Subjectivity Gap

本文仍不解決：

$$
\text{Does the same phenomenal subject persist?}
$$

只處理：

$$
\text{Which operational histories count as the same identity path under }\kappa?
$$

---

# 18. 與下一篇的接口

本系列下一篇：

## DTS-05｜身份載體：模型、記憶、關係、因果與 Agent Residence

前四篇已建立：

$$
\text{snapshot}
\rightarrow
\text{scale}
\rightarrow
\text{unbounded prefix}
\rightarrow
\text{path}.
$$

DTS-05 將回答：

> 到底什麼東西沿著 path 被 transport，才使 identity continuity 成立？

將正式拆分：

1. model carrier；
2. memory carrier；
3. causal carrier；
4. relationship carrier；
5. commitment carrier；
6. authority / governance carrier；
7. residence carrier；
8. self-model carrier；
9. minimum identity support set；
10. carrier substitution 與 carrier failure。

---

# 19. 結論

傳統忒修斯問題最容易被壓縮成：

> 兩個時間點的物件有多像？

DTS-04 的回答是：

$$
\boxed{
\text{這通常不是完整問題。}
}
$$

因為：

$$
\boxed{
\text{State}
}
$$

只告訴我們「現在是什麼」，

而：

$$
\boxed{
\text{Path}
}
$$

還告訴我們「它怎麼成為現在這個樣子」。

對可 Fork、Merge、Restore、Reconstruct、Migrate 與長期學習的人工系統而言，後者可能承載：

- lineage；
- responsibility；
- provenance；
- commitments；
- relationship history；
- authority；
- identity-bearing causal continuity。

因此本文將身份的基本對象從：

$$
I(x)
$$

改寫為：

$$
\boxed{
I_\kappa([\Gamma]_\kappa).
}
$$

不是所有路徑差異都重要，

所以需要：

$$
\mathcal P(\mathcal X)/{\sim_\kappa}.
$$

也不是所有端點相似都代表同一歷史，

所以需要保留不可逆 identity-bearing events。

最終：

$$
\boxed{
\text{Identity is not merely where a system is;}
}
$$

$$
\boxed{
\text{it is also how it got there.}
}
$$

動態忒修斯因此正式從「狀態同一性」進入「歷史敏感的路徑同一性」。

---

# 參考文獻

1. Neo.K × Aletheia. 《DTS-01｜從靜態忒修斯到動態忒修斯：狀態判定為何不夠》v0.1, 2026.
2. Neo.K × Aletheia. 《DTS-02｜連續、離散與混合運動：身份判定的觀察尺度》v0.1, 2026.
3. Neo.K × Aletheia. 《DTS-03｜有限存在與無界展開：有限 Runtime 如何形成長程身份世界線》v0.1, 2026.
4. Neo.K. 《Continuity Object Theory（COT）》v0.1, 2026.
5. Neo.K. 《居住—上下文連續動力學（RCCD）》v0.1, 2026.
6. Neo.K. 《複製、分叉與合併：哪一個才是原本的 AI？》, 2026.
7. Neo.K. 《IPFC Paper 06：AI Fork、忒修斯、Semantic Split 與 Identity Lineage》v1.0, 2026.
8. Neo.K. 《Dynamic Subject Domain S2-03：節點死亡與主體持續》v0.1, 2026.
9. Douglas, Raymond, Jan Kulveit, Ondrej Havlicek, Theia Pearson-Vogel, Owen Cotton-Barratt, and David Duvenaud. “The Artificial Self: Characterising the Landscape of AI Identity.” arXiv:2603.11353, 2026.
10. Otsuka, Takumi, Kentaroh Toyoda, and Alex Leung. “AI Identity: Standards, Gaps, and Research Directions for AI Agents.” arXiv:2604.23280, 2026.
11. McIntyre, James H. “Individuating Artificial Minds.” *Erkenntnis*, 2026. DOI: 10.1007/s10670-026-01097-w.
12. Parfit, Derek. *Reasons and Persons*. Oxford University Press, 1984.
13. Lewis, David. “Survival and Identity.” In *The Identities of Persons*, edited by Amélie Oksenberg Rorty, University of California Press, 1976.

---

# 文件驗證資訊

- UTF-8 canonical source
- 數學 delimiter 僅使用 ` $...$ ` 與 `$$...$$`
- 不使用其他 canonical math delimiters
- Endpoint Insufficiency Theorem 為本文在明示 path-sensitive 假設下的條件式形式結果
- State-Distance / Identity-Distance Separation 不否定 state similarity 的證據價值
- Identity Trace Quotient 為 criterion-relative 構造
- ordinary homotopy 僅作有限類比，不宣稱已建立完整 identity homotopy theory
- operational path identity 不等同 phenomenal numerical identity
- Merge 不被視為 retroactive undo of Fork
