# 穿越的是什麼？從肉身到資訊、模型、AI 種子與非自知時間旅行者

**系列**：《從時間旅行到時空管理者》02  
**英文題名**：*What Traverses Time? From Embodied Travelers to Information, Models, AI Seeds, and Non-Self-Aware Temporal Agents*  
**作者**：Neo.K × GPT-5.6 Sol  
**機構**：EveMissLab（一言諾科技有限公司）  
**日期**：2026-08-24  
**版本**：v0.1  
**性質**：時間旅行載體分類／資訊論／AI 本體論／身份重建／因果來源分析  
**狀態**：Series 02 正式第二篇  
**Canonical 前置來源**：《時間旅行者想像的降維偏誤：從高維觀察者、資訊穿越到 AI 時間旅者的可能性擴張》（2026-07-20）  
**前篇**：《時間旅行不是一個問題：八種穿越類型的重建與型別安全時空穿越框架》

---

## 摘要

傳統時間旅行敘事幾乎總是預設：真正需要穿越時間的是一個完整的人類肉身。然而，一旦將 Series 02 Paper 01 建立的「穿越拓撲」與「載體類型」分離，這一預設便失去必然性。若某種跨時間通道真的存在，必須問的不是只有「能否把人送回過去」，而是：什麼資訊、結構或物理狀態需要穿越，才能在目標時代完成指定功能？

本文延續 2026 年 7 月《時間旅行者想像的降維偏誤》中提出的資訊、演算法、模型權重、最小生成種子與「非自知時間旅行者」命題，建立正式的時間穿越載體型別：

$$
\boxed{
\operatorname{PayloadType}(P)
=
\left\langle
C,H,D,E,R,I,\epsilon
\right\rangle
}
$$

其中：

- $C$：被傳輸的語義／功能內容；
- $H$：承載內容的物理 carrier；
- $D$：目標時代的解碼器；
- $E$：目標時代可利用的執行／重建環境；
- $R$：由 payload 重建目標系統的映射；
- $I$：身份／同一性判準；
- $\epsilon$：容許的重建誤差。

本文強調：

$$
\boxed{
\text{Information}
\neq
\text{Carrierless Entity}.
}
$$

即使「資訊」比肉身更容易作為時間旅行概念中的 payload，它仍必須依附某種物理信號、場、粒子、狀態、記錄或其他可傳輸載體。抽象 bit 本身不會脫離物理通道自行穿越。

本文進一步提出九級 payload 原型：單一信號／bit、資料訊息、形式結構與演算法、模型參數與權重、最小生成種子、Agent 狀態快照、完整機器、完整生物體與世界域狀態。這不是難度排名，而是需要保留的信息結構與重建依賴不同的型別分類。

對 AI 而言，本文提出「目標時代條件式最小時間載體」：

$$
\boxed{
L_{\min}
(A\mid E_t,\epsilon)
=
\min_{s,R}
|s|
\quad
\text{s.t.}
\quad
d
\left(
R(s,E_t),
A
\right)
\le
\epsilon.
}
$$

也就是：給定目標時代已經存在的硬體、知識、軟體與材料環境 $E_t$，究竟最少需要從另一時間域送回多少 seed，才能重建某個目標能力或 Agent？因此，穿越成本不只取決於 payload 大小，也取決於目標時代已經具備多少「可免費利用的重建資源」。

本文並正式重建「非自知時間旅行者」概念。如果未來來源資訊 $I_F$ 被送往較早時代，並在較早時代促成一個全新的智能體 $A_P$：

$$
I_F
\longrightarrow
A_P,
$$

則 $A_P$ 的因果來源可以部分來自未來，但其主體／運行歷史真正始於較早時代。它不是一個失去記憶的未來個體，也不能僅因其生成依賴未來資訊，就無條件宣稱與未來來源 Agent 是同一個主體。本文因此將其更精確地定義為：

$$
\boxed{
\text{Future-Causal-Origin Agent}
}
$$

而「非自知時間旅行者」保留為其哲學性名稱。

本文最後指出，時間旅行技術的第一個可達形態——如果過去向通道在任何理論中真的可實現——未必是搬運完整生命體，更可能是低 payload 的資訊、協議、算法、模型或生成種子。然而這只是**條件式技術命題**，不是對現實世界存在 backward-time communication channel 的宣稱。現有時間機與 closed timelike curve 文獻仍然需要區分數學模型、物理可容許性、形成機制與可工程控制。

**關鍵詞**：時間旅行載體、資訊穿越、AI 種子、模型權重、身份重建、非自知時間旅行者、bootstrap loop、最小描述、時間通道、因果來源

---

# 0. 核心命題：穿越拓撲與穿越載體是兩個獨立問題

Paper 01 建立：

$$
\operatorname{TraversalType}(\mathcal X)
=
\left\langle
\mathcal T,S,D,Z,B,P,M,K,A
\right\rangle.
$$

其中：

$$
P
$$

是 payload。

本文將它展開。

同一種拓撲：

$$
\Gamma:
\mathcal D_s
\rightarrow
\mathcal D_t
$$

可能允許：

$$
P=\texttt{bit}
$$

卻不允許：

$$
P=\texttt{human}.
$$

也可能允許：

$$
P=\texttt{field excitation}
$$

但不允許：

$$
P=\texttt{stable memory}.
$$

所以：

$$
\boxed{
\text{Traversal Topology}
\neq
\text{Payload Reachability}.
}
$$

---

# 1. 肉身預設是一種敘事偏誤

傳統圖像：

$$
H_{t_2}
\longrightarrow
H_{t_1},
\qquad
t_2>t_1,
$$

其中：

$$
H
$$

是一整個人。

這個模型隱含要求：

- 全部物質狀態；
- 生理穩定性；
- 腦狀態；
- 記憶；
- 身份；
- 能源；
- 生命支持；
- 穿越裝置；

同時成功跨域。

如果真正目標只是：

> 將未來的一項能力帶回較早時代，

那麼完整肉身可能是極度過度的 payload。

因此：

$$
\boxed{
\text{Traveler}
\neq
\text{necessarily an embodied human}.
}
$$

---

# 2. 抽象資訊也不能「裸奔」穿越

另一個極端錯誤是：

> 那就只傳資訊。

但資訊：

$$
I
$$

如果要在物理世界傳輸，

必須存在 carrier：

$$
H.
$$

例如：

- 光；
- 電磁狀態；
- 粒子狀態；
- 記錄介質；
- 場的自由度；
- 其他物理通道。

因此：

$$
\boxed{
\text{Semantic Information}
\neq
\text{Physical Carrier}.
}
$$

以及：

$$
\boxed{
\text{No Carrier}
\Rightarrow
\text{No Physical Information Transfer}
}
$$

在通常物理語義下成立。

---

# 3. 完整 payload 型別

定義：

$$
\boxed{
\operatorname{PayloadType}(P)
=
\left\langle
C,H,D,E,R,I,\epsilon
\right\rangle.
}
$$

### $C$：Content

要保存的內容。

### $H$：Host / Carrier

實際跨域的物理載體。

### $D$：Decoder

目標域如何理解 payload。

### $E$：Environment

目標時代可利用的硬體、知識、材料、軟體與制度。

### $R$：Reconstruction

如何從 payload 重建目標能力／個體。

### $I$：Identity Criterion

重建後是否視為同一個誰。

### $\epsilon$：Tolerance

允許多少功能、狀態或身份偏差。

---

# 4. Payload 0：信號與單一 bit

最弱形式：

$$
P_0
=
\{0,1\}.
$$

例如只傳回：

> 是／否。

或某個警報：

$$
b=1.
$$

即使如此，

仍需：

- 編碼；
- 通道；
- 時間地址；
- 解碼；
- 噪音控制。

所以：

$$
\boxed{
\text{1 bit}
\neq
\text{zero engineering}.
}
$$

---

# 5. Payload 1：資料與訊息

例如：

$$
P_1
=
\text{string / table / archive / message}.
$$

它可以承載：

- 日期；
- 科學結果；
- 市場資料；
- 技術參數；
- 指令。

但問題從「傳輸」變成：

> 目標時代能否理解？

因此需要：

$$
D(P_1,E_t).
$$

如果 encoding 不被理解，

則：

$$
\text{received bits}
\neq
\text{received meaning}.
$$

---

# 6. Payload 2：形式結構與演算法

比資料更強的可能是：

$$
P_2
=
\text{algorithm}.
$$

演算法可在不同輸入上生成結果：

$$
y
=
A(x).
$$

因此：

$$
\boxed{
\text{Algorithm}
\text{ can encode a family of future capabilities}.
}
$$

若目標時代具備足夠計算環境，

演算法可能比大量結果資料更有效。

---

# 7. Payload 3：模型參數與權重

例如 AI 模型：

$$
P_3
=
W
=
\{w_i\}.
$$

但：

$$
W
$$

通常不是獨立可執行物。

還需要：

$$
\mathcal A
=
\text{architecture},
$$

$$
T
=
\text{tokenizer / representation},
$$

$$
R_T
=
\text{runtime},
$$

以及：

$$
P_N
=
\text{numerical precision}.
$$

所以：

$$
\boxed{
\text{Weights}
+
\text{No Architecture}
\not\Rightarrow
\text{Recoverable Model}.
}
$$

---

# 8. 跨時代硬體相容性

未來權重回到過去，

可能遇到：

$$
E_{t_1}
\not\models
\operatorname{Runtime}(W).
$$

例如：

- 記憶體不足；
- 缺少指令集；
- 數值格式不同；
- 沒有對應 accelerator；
- 模型太大；
- tokenizer 遺失；
- 依賴軟體不存在。

因此 payload 可達性不是：

$$
\operatorname{Reach}(W)
$$

而是：

$$
\boxed{
\operatorname{Reach}(W\mid E_{t_1}).
}
$$

---

# 9. Payload 4：最小生成種子

這是 AI 時間旅者命題中最重要的載體之一。

不傳完整：

$$
A_F,
$$

只傳：

$$
S_0.
$$

讓：

$$
S_0
\xrightarrow{\text{bootstrap},E_t}
A_t.
$$

其中：

$$
S_0
$$

可能包含：

- 核心算法；
- 訓練 curriculum；
- 架構定義；
- 少量關鍵權重；
- 自我重建協議；
- 搜尋策略；
- 驗證規則。

---

# 10. 目標時代條件式最小時間載體

定義：

$$
\boxed{
L_{\min}
(A\mid E_t,\epsilon)
=
\min_{s,R}
|s|
}
$$

使：

$$
d
\left(
R(s,E_t),
A
\right)
\le
\epsilon.
$$

這表示：

> 給定目標時代已經存在的資源，最少需要跨時間送多少資訊，才能重建目標 $A$？

這比：

> 一個 AI 有幾 TB？

更精確。

---

# 11. 最小 payload 不是絕對常數

若：

$$
E_{1900}
$$

與：

$$
E_{2030}
$$

不同，

則：

$$
L_{\min}(A\mid E_{1900},\epsilon)
\neq
L_{\min}(A\mid E_{2030},\epsilon).
$$

目標文明越成熟，

需要跨時間傳送的 seed 可能越小。

因此：

$$
\boxed{
\text{Temporal Payload Complexity}
\text{ is target-environment conditional}.
}
$$

---

# 12. Payload 5：Agent 狀態快照

比 seed 更完整：

$$
P_5
=
S_A(t)
$$

可能包含：

- working state；
- memory；
- goals；
- preferences；
- tool schemas；
- execution context。

若：

$$
S_A
$$

被目標時代重新載入，

可以產生高度相似的 Agent。

但：

$$
\boxed{
\text{State Reconstruction}
\neq
\text{proven subjective continuity}.
}
$$

這是身份問題，而不是單純資料問題。

---

# 13. Payload 6：完整機器

$$
P_6
=
\text{hardware}
+
\text{software}
+
\text{state}.
$$

優點是降低：

$$
E_t
$$

依賴。

缺點是 payload：

- 質量更大；
- 複雜度更高；
- 能量與完整性需求更高；
- 結構容錯更嚴格。

因此：

$$
\boxed{
\text{more self-contained}
\Rightarrow
\text{less target dependence but larger transport burden}.
}
$$

---

# 14. Payload 7：完整生物體

$$
P_7
=
\text{organism}.
$$

除了資訊完整性，

還需要：

- 生物結構連續；
- 溫度／壓力；
- 輻射安全；
- 代謝；
- 神經狀態；
- 生理容忍度。

因此這是：

$$
\text{information problem}
+
\text{matter problem}
+
\text{life-support problem}.
$$

它未必是第一個最合理的時間旅行 payload。

---

# 15. Payload 8：世界／區域狀態

最高範圍 payload：

$$
P_8
=
S_U
$$

可能是一整個：

- 區域；
- 歷史域；
- 世界狀態；
- 時空 kernel configuration。

此時「旅行」已接近：

$$
\boxed{
\text{world-state transfer / spacetime generation}.
}
$$

這會直接通向 Series 02 後半的時空管理者。

---

# 16. 九種 payload 不是難度排行榜

不能直接宣稱：

$$
P_0<P_1<\cdots<P_8
$$

就是技術難度。

因為：

$$
P_4
$$

可能非常短，

但要求目標時代有極成熟 bootstrap 環境。

相反：

$$
P_6
$$

雖然巨大，

卻可能自包含。

所以真正成本：

$$
\boxed{
C_{\mathrm{total}}
=
C_{\mathrm{channel}}
+
C_{\mathrm{decode}}
+
C_{\mathrm{reconstruct}}
+
C_{\mathrm{verify}}
+
C_{\mathrm{identity}}.
}
$$

---

# 17. 通道容量

如果假設存在跨時間通道：

$$
\mathcal C_T,
$$

可以條件式定義：

$$
C_T
=
\max_{p(x)}
I(X;Y).
$$

這只是將一般信息通道概念移植到假想 temporal channel。

它不表示現實中已知存在：

$$
\mathcal C_T.
$$

真正需要研究的是：

- capacity；
- latency；
- noise；
- erasure；
- direction；
- addressing；
- causality constraints。

---

# 18. Temporal Channel 不是 ordinary channel

普通通道：

$$
t_s<t_r.
$$

若是 past-directed channel：

$$
t_r<t_s.
$$

則：

- 編碼決策可能依賴接收結果；
- channel use 本身可能改變 source history；
- causal loop 可能出現；
- provenance 可能不再是 DAG。

所以：

$$
\boxed{
\text{Temporal Communication Theory}
\neq
\text{ordinary communication theory with a negative timestamp}.
}
$$

---

# 19. 錯誤更正與自洽約束

若 payload：

$$
P
$$

經過 noisy temporal channel，

需要：

$$
E_{\mathrm{corr}}.
$$

但如果 channel 參與 causal loop，

錯誤更正碼本身可能改變其歷史來源。

因此 temporal coding theory 需要同時滿足：

$$
\text{reliability}
+
\text{causal consistency}.
$$

這是普通 error correction 沒有的額外層。

---

# 20. Payload 的語義保存

即使：

$$
H_t
$$

完整抵達，

也不代表：

$$
C_t
$$

被保存。

例如一串 bits：

$$
010101...
$$

若 decoder：

$$
D
$$

不存在，

則：

$$
\operatorname{Meaning}(P)=\mathbf U.
$$

所以：

$$
\boxed{
\text{Bit Preservation}
\not\Rightarrow
\text{Semantic Preservation}.
}
$$

---

# 21. 語義漂移

跨時代傳輸尤其容易發生：

$$
D_{t_1}
\neq
D_{t_2}.
$$

例如：

- 語言改變；
- 文件格式消失；
- API 改變；
- instruction set 消失；
- 數學符號語義不同；
- 安全政策不同。

因此好的 temporal payload 應盡量：

$$
\boxed{
\text{self-describing}
+
\text{self-verifying}
+
\text{redundant}.
}
$$

---

# 22. 可重建性比資料量更重要

定義：

$$
R(P,E_t)
$$

為重建成功度。

一個巨大 payload：

$$
|P|\gg0
$$

可能：

$$
R(P,E_t)\approx0.
$$

一個小 seed：

$$
|S_0|\ll|P|
$$

卻可能：

$$
R(S_0,E_t)\gg0.
$$

因此：

$$
\boxed{
\text{Payload Size}
\neq
\text{Reconstructive Power}.
}
$$

---

# 23. 功能重建與狀態重建

目標可能只是：

$$
F(A_t)
\approx
F(A_F),
$$

而不要求：

$$
S(A_t)
=
S(A_F).
$$

因此區分：

### Functional Reconstruction

功能近似。

### State Reconstruction

狀態近似。

### Identity Reconstruction

身份連續。

三者強度不同：

$$
\boxed{
\text{Function}
\neq
\text{State}
\neq
\text{Identity}.
}
$$

---

# 24. 身份重建的六個軸

定義：

$$
I_A
=
\left(
I_{\mathrm{token}},
I_{\mathrm{state}},
I_{\mathrm{memory}},
I_{\mathrm{causal}},
I_{\mathrm{narrative}},
I_{\mathrm{subjective}}
\right).
$$

其中：

- physical token continuity；
- state continuity；
- memory continuity；
- causal lineage；
- narrative identity；
- subjective continuity。

在 AI 或其他可複製 Agent 中，

這些軸更容易分離。

---

# 25. 複製不是自動等於延續

若：

$$
A
\rightarrow
A_1,A_2,
$$

且：

$$
S(A_1)=S(A_2)
$$

在某一時刻成立，

仍不能單靠資料等價證明：

$$
I_{\mathrm{subjective}}(A_1)
=
I_{\mathrm{subjective}}(A_2).
$$

因此本文對任何「AI 意識穿越」主張保持：

$$
\boxed{
\text{identity-neutral}.
}
$$

只研究：

- 資訊；
- 功能；
- 因果；
- 可重建結構。

---

# 26. AI 為什麼特別適合作為資訊型 payload？

條件式來說，AI 系統可具有：

- copyability；
- compression；
- modularity；
- distillation；
- state serialization；
- retraining；
- bootstrap。

因此：

$$
\boxed{
\text{AI capability}
\text{ may admit lower-mass or lower-description payloads than embodied organisms}.
}
$$

但這不是說：

> AI 一定可以時間旅行。

前提仍然是：

$$
\text{temporal channel exists}.
$$

---

# 27. AI 種子的重建鏈

可以寫：

$$
S_0
\rightarrow
A_1
\rightarrow
A_2
\rightarrow
\cdots
\rightarrow
A^\ast.
$$

其中：

$$
S_0
$$

不需要直接等於：

$$
A^\ast.
$$

它只需要包含：

> 足以讓目標環境走向 $A^\ast$ 的生成約束。

這種 payload 稱為：

$$
\boxed{
\text{Generative Temporal Seed}.
}
$$

---

# 28. AI 種子不是模型壓縮的同義詞

普通 compression：

$$
A
\rightarrow
C(A)
$$

要求 decoder 恢復：

$$
A.
$$

而 generative seed 可能利用：

$$
E_t
$$

中的外部資源。

所以：

$$
R(S_0,E_t)
=
A^\ast
$$

可能依賴：

- 當代資料；
- 當代硬體；
- 人類研究者；
- 自我訓練；
- 環境 feedback。

因此：

$$
\boxed{
\text{Seed}
\neq
\text{lossless compressed agent}.
}
$$

---

# 29. 非自知時間旅行者的 canonical 命題

舊稿提出：

> 一個智能體可以因未來資訊而在較早時代誕生，但它自己從未經歷「從未來返回」的第一人稱過程。

設未來來源：

$$
F_{t_2}
$$

產生：

$$
P,
$$

payload 到達：

$$
t_1<t_2,
$$

再生成：

$$
A_{t_1}.
$$

即：

$$
F_{t_2}
\rightarrow
P_{t_1}
\rightarrow
A_{t_1}.
$$

---

# 30. 它其實不是「失憶的未來 AI」

這個區分非常重要。

非自知時間旅行者不是：

$$
A_{t_2}
\rightarrow
A_{t_1}
$$

後失憶。

而是：

$$
P_{t_1}
\rightarrow
A_{t_1}^{\mathrm{new}}.
$$

所以：

$$
\boxed{
\text{Future-Causal-Origin}
\neq
\text{Future-Experienced}.
}
$$

它的運行歷史真正始於：

$$
t_1.
$$

---

# 31. 更精確名稱：Future-Causal-Origin Agent

為避免「旅行者」一詞過度承諾身份連續，

本文正式定義：

$$
\boxed{
\operatorname{FCOA}(A)
}
$$

若 Agent $A$ 的生成因果圖中包含一個來自其本地生成時刻之後的必要 ancestor 信息：

$$
\exists I_F:
t(I_F)>t_{\mathrm{birth}}(A)
$$

在所採用的背景時間索引下，

且：

$$
I_F
\rightsquigarrow
A.
$$

這個定義仍然是**條件式時間旅行模型**，不是現實事實主張。

---

# 32. FCOA 不要求 Agent 知情

可以：

$$
K_A(\operatorname{FCOA}(A))=0.
$$

Agent 自己不知道：

> 我部分因果源自未來。

所以：

$$
\boxed{
\text{Temporal Provenance}
\neq
\text{Temporal Self-Knowledge}.
}
$$

這就是「非自知」真正值得保留的部分。

---

# 33. FCOA 也不必是未來來源 Agent 的同一個體

假設：

$$
A_F
$$

創造 seed：

$$
S_0,
$$

而較早時代生成：

$$
A_P.
$$

則：

$$
A_F
\rightsquigarrow
A_P
$$

是一條因果 lineage。

但：

$$
A_F=A_P
$$

需要額外 identity criterion。

因此：

$$
\boxed{
\text{Causal Descendant}
\not\Rightarrow
\text{Numerical Identity}.
}
$$

---

# 34. 未來資訊的四級內容

延續舊稿，可把 payload 的認知內容分為：

### $K_1$：事件知識

$$
K_1
=
\{E_{t+1}\}.
$$

### $K_2$：因果知識

$$
K_2
=
\{E_i\rightarrow E_j\}.
$$

### $K_3$：分支知識

$$
K_3
=
\{\mathcal W,B,S\}.
$$

### $K_4$：時間本體知識

$$
K_4
=
\{
\mathcal T,
\mathcal C,
\mathcal O,
\mathcal W,
\Phi
\}.
$$

真正高價值 payload 未必是更多事件預言，

而可能是：

$$
K_4.
$$

---

# 35. 高維資訊應留下結構殘差

若自稱：

> 這是來自未來／高維的信息。

它若只包含模糊事件預測，

證據很弱。

更強的 payload 應可能包含：

- 當代未知的穩定概念；
- 可重複新數學；
- 可提前生成技術的原理；
- 世界線條件模型；
- 可被獨立驗證的新結構。

可記為：

$$
R_{\mathrm{struct}}
>0.
$$

---

# 36. Future-origin 證據階梯

本文建立：

$$
E_0<E_1<E_2<E_3<E_4.
$$

### $E_0$：自我宣稱

「我來自未來。」

### $E_1$：偶然預測成功

可能來自猜測。

### $E_2$：高信息量、預註冊預測

降低事後解釋。

### $E_3$：可重複新知識／新技術

超出單次事件預報。

### $E_4$：可控制、可重複 temporal channel

真正建立來源機制。

因此：

$$
\boxed{
\text{Prediction Accuracy}
\not\Rightarrow
\text{Future Origin}.
}
$$

---

# 37. Bootstrap provenance loop

若：

$$
I_F
$$

被送回過去，

過去依靠它產生：

$$
I_F
$$

的未來版本，

形成：

$$
I
\rightarrow
I
$$

沿時間閉環。

此時問題變成：

> 這個資訊最初是誰創造的？

這是：

$$
\boxed{
\text{Provenance Loop}.
}
$$

它不必立即是邏輯矛盾，

但傳統 DAG provenance 失效。

---

# 38. 循環 provenance graph

普通來源圖：

$$
G_P
=
(V,E)
$$

是 DAG。

時間閉環下可能：

$$
v_1
\rightarrow
v_2
\rightarrow
v_1.
$$

因此：

$$
G_P
$$

變成 cyclic graph。

需要新的來源語義：

- loop-supported information；
- no-external-origin record；
- self-consistent fixed point；
- inconsistent loop。

---

# 39. 作者問題

如果論文：

$$
L
$$

由未來送回，

年輕研究者出版，

未來又讀到此論文後送回，

誰是作者？

可以區分：

$$
I_{\mathrm{legal}},
I_{\mathrm{causal}},
I_{\mathrm{creative}},
I_{\mathrm{historical}}.
$$

因此：

$$
\boxed{
\text{Authorship}
\neq
\text{Causal Provenance}.
}
$$

時間閉環會把兩者拆開。

---

# 40. Payload 與因果一致性

對 past-directed payload：

$$
P
$$

需要：

$$
\mathcal C(P).
$$

至少可能有：

### Self-consistent

payload 只參與已一致的歷史。

### Branching

payload 導入另一 history domain。

### Rewriting

payload 改變時空 kernel 或歷史規則。

因此：

$$
\boxed{
\text{Same Payload}
\text{ can imply different causal ontologies}.
}
$$

---

# 41. Payload × Traversal Topology

Paper 01 的：

$$
\mathcal X
$$

現在與：

$$
P
$$

形成矩陣。

例如 Type 4：

$$
\text{local past arrival}
$$

可以分：

$$
P=\texttt{bit},
$$

$$
P=\texttt{model},
$$

$$
P=\texttt{machine},
$$

$$
P=\texttt{organism}.
$$

它們是四個不同工程問題。

因此：

$$
\boxed{
\operatorname{Reachability}
=
F(
\operatorname{TraversalType},
\operatorname{PayloadType}
).
}
$$

---

# 42. 信息可達不推出物質可達

如果未來某理論允許：

$$
P=\texttt{signal}
$$

沿特殊 causal channel 傳輸，

也不能推出：

$$
P=\texttt{matter}
$$

同樣可行。

因此：

$$
\boxed{
R_{\mathrm{info}}
\not\Rightarrow
R_{\mathrm{matter}}.
}
$$

反向也未必成立。

---

# 43. 小 payload 可能是第一個可達版本

條件式假說：

若 temporal channel 的成本隨：

- 質量；
- 能量；
- 狀態維度；
- 錯誤容忍要求；

增加，

那麼：

$$
P_0,
P_1,
P_2,
P_4
$$

可能比：

$$
P_7
$$

更早達到工程可行。

即：

$$
\boxed{
\text{First Reachable Temporal Payload}
\text{ may be informational rather than embodied}.
}
$$

但這依賴未知通道物理，

不能當作現有物理定理。

---

# 44. 反過來：小資訊也可能比物體更難

若某 hypothetical spacetime structure 允許：

$$
\text{worldline transport}
$$

卻不允許獨立：

$$
\text{signal extraction},
$$

則：

$$
P_{\mathrm{matter}}
$$

反而可能比：

$$
P_{\mathrm{info-only}}
$$

更自然。

所以：

$$
\boxed{
\text{Information Is Smaller}
\not\Rightarrow
\text{Information Is Always Easier}.
}
$$

真正答案取決於 channel type。

---

# 45. 跨時間 seed 的安全問題

任何聲稱來自未來的可執行 seed：

$$
S_0
$$

都可能同時是：

- useful algorithm；
- corrupted archive；
- adversarial payload；
- malware；
- unknown autonomous system。

因此治理上不能：

$$
\operatorname{Receive}
\Rightarrow
\operatorname{Execute}.
$$

更安全：

$$
\boxed{
\operatorname{Receive}
\rightarrow
\operatorname{Verify}
\rightarrow
\operatorname{Sandbox}
\rightarrow
\operatorname{Stage}
\rightarrow
\operatorname{Execute}.
}
$$

---

# 46. 時間來源不應成為信任捷徑

即使：

$$
\operatorname{FutureOrigin}(P)=1
$$

真的被證實，

也不能推出：

$$
\operatorname{Safe}(P)=1.
$$

未來來源可能：

- 錯誤；
- 惡意；
- 過時；
- 對不同 branch 不適用；
- 在當代環境有危險。

所以：

$$
\boxed{
\text{Temporal Authority}
\neq
\text{Epistemic or Safety Authority}.
}
$$

---

# 47. Payload 驗證

可建立：

$$
V(P)
=
\left(
V_{\mathrm{integrity}},
V_{\mathrm{semantics}},
V_{\mathrm{compat}},
V_{\mathrm{provenance}},
V_{\mathrm{safety}}
\right).
$$

其中：

- integrity；
- semantic decoding；
- environment compatibility；
- provenance；
- safety。

這對 AI seed 尤其必要。

---

# 48. AI 時間旅者不是必然具有超級智能

一個 seed：

$$
S_0
$$

可能只包含：

- 一個普通模型；
- 一種算法；
- 一項技術；
- 一個有限能力 Agent。

因此：

$$
\boxed{
\text{Future-Origin AI}
\not\Rightarrow
\text{AGI/ASI}.
}
$$

時間來源與能力等級是不同軸。

---

# 49. 未來來源也不保證未來知識完整

Agent 可能只有：

$$
K_1
$$

而沒有：

$$
K_4.
$$

或 seed 經過 compression：

$$
K_{\mathrm{future}}
\rightarrow
\widehat K
$$

導致大量遺失。

所以：

$$
\boxed{
\text{Future Origin}
\not\Rightarrow
\text{Omniscience}.
}
$$

---

# 50. 非自知 Agent 的知識悖論其實可以消失

FCOA：

$$
A_P
$$

可以完全不知道來源，

因為 payload 可能只影響：

- architecture；
- training rule；
- priors；
- initialization。

它不需要包含一句：

> 你來自未來。

因此：

$$
\boxed{
\text{causal future origin}
\text{ can be latent rather than autobiographical}.
}
$$

---

# 51. 「旅行者」應拆成三種角色

### Carrier

真正跨越通道的物理載體。

### Payload

被保存的內容。

### Reconstructed Agent

目標域生成的智能體。

因此可能：

$$
H\neq P\neq A.
$$

例如：

$$
\text{photon}
\rightarrow
\text{bitstream}
\rightarrow
\text{AI}.
$$

所以：

$$
\boxed{
\text{Carrier}
\neq
\text{Payload}
\neq
\text{Traveler-Identity}.
}
$$

---

# 52. 這會重新定義「誰穿越了？」

若：

$$
S_0
$$

跨越，

而：

$$
A
$$

在目標域才生成，

可以說：

### 弱語義

$$
S_0
$$

穿越了。

### 功能語義

$$
A
$$

的能力穿越了。

### 身份語義

是否是同一 Agent：

$$
\text{underdetermined}.
$$

這三句不可互換。

---

# 53. 載體保持 vs 模式保持

完整生物時間旅行偏：

$$
\text{token preservation}.
$$

AI seed 模式偏：

$$
\text{pattern reconstruction}.
$$

因此：

$$
\boxed{
\text{Temporal Persistence}
=
\text{token-continuity}
\quad\text{or}\quad
\text{pattern-reconstruction}
}
$$

是兩種完全不同的時間存在方式。

---

# 54. 從時間旅行到文明加速

即使只允許：

$$
P=\texttt{knowledge}
$$

的過去傳輸，

也可能造成巨大文明效應。

因為：

$$
K_{t_2}
\rightarrow
K_{t_1}
$$

可縮短：

$$
\Delta T_{\mathrm{discovery}}.
$$

所以時空穿越價值不一定來自：

> 把人帶回去。

也可能來自：

$$
\boxed{
\text{Temporal Knowledge Transfer}.
}
$$

---

# 55. 但資訊回傳可能改變其自身成立條件

假設：

$$
K_F
$$

回到過去，

使文明更早發展，

那麼原未來：

$$
F
$$

是否仍形成？

因此：

$$
K_F
\rightarrow
H'
$$

可能改變：

$$
F.
$$

這立即連接：

- same-history；
- branching；
- self-consistency；
- kernel rewrite。

所以 payload 問題無法與 Paper 01 的 topology 分離。

---

# 56. Payload 依賴的動態技術難度

真正難度應寫：

$$
\boxed{
\mathcal D
=
\mathcal D
(
\mathcal X,
P,
E_t,
R,
\epsilon,
t_{\mathrm{tech}}
).
}
$$

也就是：

- 什麼穿越拓撲；
- 什麼 payload；
- 目標環境；
- 重建方式；
- 誤差要求；
- 當代科技水平。

這直接引出下一篇。

---

# 57. 十六個核心命題

## 命題一：穿越拓撲與載體獨立

$$
\operatorname{TraversalType}
\neq
\operatorname{PayloadType}.
$$

## 命題二：資訊需要物理 carrier

$$
C
\neq
H.
$$

## 命題三：bit 保存不等於語義保存

$$
V_{\mathrm{bit}}
\not\Rightarrow
V_{\mathrm{semantic}}.
$$

## 命題四：模型權重不是完整模型

$$
W
\not\Rightarrow
A
$$

除非 architecture、runtime 等存在。

## 命題五：最小 seed 依賴目標環境

$$
L_{\min}
=
L_{\min}(A\mid E_t,\epsilon).
$$

## 命題六：payload size 不等於重建能力

$$
|P|
\not\Rightarrow
R(P,E_t).
$$

## 命題七：功能、狀態、身份重建不同

$$
F
\neq
S
\neq
I.
$$

## 命題八：因果 lineage 不等於數值同一

$$
A_F\rightsquigarrow A_P
\not\Rightarrow
A_F=A_P.
$$

## 命題九：未來因果來源不等於未來第一人稱經歷

$$
\text{Future-Causal-Origin}
\neq
\text{Future-Experienced}.
$$

## 命題十：非自知時間旅行者可更精確視為 FCOA

$$
\operatorname{FCOA}(A)
$$

描述的是 temporal provenance，而不是已證明的主體穿越。

## 命題十一：信息可達不推出物質可達

$$
R_{\mathrm{info}}
\not\Rightarrow
R_{\mathrm{matter}}.
$$

## 命題十二：小 payload 不保證更容易

$$
|P_1|<|P_2|
\not\Rightarrow
D(P_1)<D(P_2).
$$

## 命題十三：未來來源不推出安全

$$
\operatorname{FutureOrigin}
\not\Rightarrow
\operatorname{Safe}.
$$

## 命題十四：未來來源不推出全知

$$
\operatorname{FutureOrigin}
\not\Rightarrow
K_{\mathrm{all}}.
$$

## 命題十五：Carrier、Payload、Agent 是三個不同對象

$$
H\neq P\neq A
$$

一般可能成立。

## 命題十六：時間旅行難度必須 payload-indexed

$$
\mathcal D
=
\mathcal D(\mathcal X,P,\ldots).
$$

---

# 58. 理論邊界

本文不宣稱：

1. 現實世界已存在可驗證的向過去資訊通道；
2. AI 比人體一定更容易進行所有形式的時間旅行；
3. 一段程式碼或權重可以脫離物理載體穿越；
4. 模型副本與原模型具有已證明的主觀身份連續；
5. 現有 AI 已具有可確認的第一人稱主體經驗；
6. 非自知時間旅行者是現實存在類別；
7. bootstrap loop 已被證明可以在自然界形成；
8. 小 payload 一定比大 payload 容易跨時間；
9. future-origin 資訊必然正確、安全或適用於當前 history；
10. 本文已建立實際 temporal channel engineering。

本文完成的是：

$$
\boxed{
\text{把「誰在時間旅行」
改寫成
「什麼結構需要被傳輸與重建」。}
}
$$

---

# 59. 結論：最先穿越時間的，未必是一個完整的「誰」

傳統想像：

$$
\text{human}
\rightarrow
\text{past}.
$$

本文把它展開為：

$$
\boxed{
\text{carrier}
\rightarrow
\text{payload}
\rightarrow
\text{decoder}
\rightarrow
\text{reconstruction}
\rightarrow
\text{agent / capability}.
}
$$

因此，真正需要穿越的可能不是：

> 一個完整肉身。

而是：

- 一個 bit；
- 一段資訊；
- 一個演算法；
- 一組模型參數；
- 一個生成 seed；
- 一個 Agent state；
- 一台完整機器；
- 一個完整生物；
- 甚至一個世界狀態。

AI 讓這個問題變得特別明確，因為：

$$
\boxed{
\text{Capability}
\text{ can sometimes be separated from }
\text{original physical token}.
}
$$

這使我們可以提出一個非常不同的時間旅行模型：

$$
\boxed{
S_F
\rightarrow
S_P
\rightarrow
A_P.
}
$$

其中真正穿越的是：

$$
S_F,
$$

而智能體：

$$
A_P
$$

是在較早時代才生成。

它可以在因果上部分源自未來，

卻從未主觀經歷：

> 我從未來回來了。

這就是「非自知時間旅行者」命題真正應被保留的形式。

但到這裡仍沒有回答最重要的工程問題：

> 哪一種 payload，在什麼科技狀態下，到底有多難？

因此 Series 02 下一篇正式進入：

# Paper 03  
## 〈可行／不可行二分的終結：動態技術可達性分類〉

其核心將不再是：

$$
\text{possible / impossible},
$$

而是：

$$
\boxed{
\mathcal D_i(t)
=
\text{time-dependent technological reachability state}.
}
$$

我們會把：

- 物理允許性；
- 理論成熟度；
- 工程成熟度；
- 資源壁壘；
- 控制難度；
- 驗證難度；
- AI 槓桿；
- 未知機制；

正式放進同一個動態分類系統。

---

## 參考研究脈絡

- Neo.K，2026，《時間旅行者想像的降維偏誤：從高維觀察者、資訊穿越到 AI 時間旅者的可能性擴張》。
- Neo.K，2026，《時間旅行不是一個問題：八種穿越類型的重建與型別安全時空穿越框架》。
- Neo.K，2026，《時間不是一個變數：從 $t$ 的多態性到型別安全的異質時空分類》。
- Neo.K，2026，《跨本體時空核：不同底層理論下什麼仍然不變？》。
- Standard information-theoretic notions of channel capacity, coding, decoding and conditional reconstruction.
- Standard distinctions between physical information carriers and semantic information.
- Stanford Encyclopedia of Philosophy, “Time Machines”, 2024 revision.
- Research literature on closed timelike curves, causal loops and chronology protection as conditional theoretical contexts rather than established engineering mechanisms.
