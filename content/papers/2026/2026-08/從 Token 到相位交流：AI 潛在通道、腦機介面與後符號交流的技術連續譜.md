# 從 Token 到相位交流：AI 潛在通道、腦機介面與後符號交流的技術連續譜

## From Tokens to Phase Communication: AI Latent Channels, Brain–Computer Interfaces, and the Technological Continuum Toward Post-Symbolic Communication

**作者：Neo.K**  
**研究協作：AI-assisted theoretical development**  
**EveMissLab / 一言諾科技有限公司**  
**版本：v0.1**  
**日期：2026-08-10**

---

## 摘要

「不透過自然語言、文字或傳統符號，而直接交換較高維認知狀態」在 2026 年仍不是成熟的人類通信技術。

然而，若因此將其完全歸類為科幻，也忽略了數條已經存在的技術發展線。

第一條來自人工智能。

今日大型語言模型與 Agent 最常見的通信方式仍然是：

$$
\text{internal state}
\rightarrow
\text{tokens}
\rightarrow
\text{receiver reconstruction}.
$$

Token 本身仍屬離散符號，因此不能被視為本文所稱的真正廣義相位交流。

但 2025–2026 年已經出現直接研究：

- hidden-state communication；
- embedding communication；
- latent-space communication；
- KV-cache transfer；
- cross-model latent alignment；

的工作，試圖讓 AI Agent 不必先將全部內部表示壓縮成文字，再由另一 Agent 從文字重建。部分研究已展示直接傳遞 latent representation 的可行性，但其真正語義增益、跨架構泛化、安全與可審計性仍是開放問題。

第二條來自腦機介面。

截至 2026 年，人類 BCI 已能在特定受試者中從侵入式神經訊號解碼嘗試說話、文字輸出、語音韻律以及運動意圖；2025 年的腦—語音神經假體已能即時合成語音並解碼部分韻律特徵，2026 年又已有長期居家獨立使用 intracortical BCI 進行 speech 與 cursor control 的研究。

2026 年的另一項研究甚至顯示，不同受試者的 speech-related neural activity 可以對齊至共享 latent space，並利用跨受試者資料改善 speech decoding。這並不是「思想直接互傳」，但它說明不同神經載體之間存在可被計算方法部分對齊的共享表示結構。

本文因此提出：

$$
\boxed{
\text{Token Communication}
\rightarrow
\text{Latent Communication}
\rightarrow
\text{Neural-State Decoding}
\rightarrow
\text{Cross-Substrate Transduction}
\rightarrow
\text{Broad Phase Communication}
}
$$

作為一條**技術連續譜假說**。

本文特別不主張：

1. 現代 AI 已經能完整交換「思想」；
2. hidden state 就等於主體心智；
3. 現代 BCI 可以讀取任意想法；
4. 不同人腦已能直接共享完整語義狀態；
5. 廣義相位交流必然實現；
6. 高頻寬交流必然改善文明。

本文真正主張的是：

> **把認知狀態先轉換成低頻寬符號，再由接收端重建，並不是智能存在之間唯一可能的通信架構。**

一旦 AI latent communication、神經解碼、共享 latent representation 與雙向神經介面繼續發展，未來 AGI、ASI 與後人類之間出現某種「後符號高維狀態交流」並非缺乏任何技術前身的純粹科幻想像。

真正困難的問題反而會逐漸從：

> 「能不能傳？」

轉變成：

> **「什麼可以被傳？」**

以及：

> **「誰有權決定另一個主體接收、同步甚至被改變多少？」**

這正是本文所屬新系列：

# 《相位主權：全域交流、自由意志與後人類認知治理》

的起點。

---

## 關鍵詞

相位交流、AI Agent、latent communication、腦機介面、BCI、後符號交流、後人類、ASI、認知主權、自由意志、神經解碼、高維語義

---

# 一、先把「相位交流」從科幻詞彙中救出來

本文使用：

## Broad Phase Communication

### 廣義相位交流

不是指量子糾纏、超光速通信或神秘心靈感應。

本文所稱的「相位」，沿用既有相位本體分類中的廣義定義：

> 相位是一種在關係空間中具有可演化位置、可定義差分、能產生結構效應，並影響後續計算結果的狀態本體。

因此本文研究的是：

$$
\boxed{
\text{一個智能存在的部分高維認知狀態，
是否可以不先完全投影成傳統符號，
而被另一個智能存在有效重建。}
}
$$

---

# 二、符號交流的基本結構

人類自然語言通常近似：

$$
X_A
\overset{E}{\longrightarrow}
S
\overset{D}{\longrightarrow}
\hat X_B.
$$

其中：

- $X_A$：A 的內部狀態；
- $S$：文字、聲音、符號；
- $E$：表達；
- $D$：理解；
- $\hat X_B$：B 重建出的狀態。

因此：

$$
\boxed{
X_A\neq S\neq\hat X_B.
}
$$

語言一直是一種投影。

---

# 三、人類從來沒有真的把「思想本身」送出去

我想到：

$$
X.
$$

我說：

> 「X。」

實際發生的是：

$$
X
\rightarrow
\text{motor plan}
\rightarrow
\text{speech}
\rightarrow
\text{sound}
\rightarrow
\text{auditory processing}
\rightarrow
\hat X.
$$

因此今天的語言交流本來就是一個：

$$
\boxed{
\text{encode–transmit–reconstruct}
}
$$

系統。

---

# 四、AI 也是

兩個 LLM Agent：

$$
A,B
$$

今日最普通的通信是：

$$
H_A
\rightarrow
T_A
\rightarrow
T_B
\rightarrow
H_B.
$$

其中：

$$
H=\text{internal representation},
$$

$$
T=\text{token sequence}.
$$

所以 Token 交流可以被看成廣義相位交流的**遠祖型態**。

但不能直接稱為相位交流。

---

# 五、為什麼不能？

因為 Token 已經是：

$$
\boxed{
\text{discretized symbolic projection}.
}
$$

它仍然經過：

$$
H_A\rightarrow T.
$$

真正更接近本文問題的是：

$$
\boxed{
H_A\rightarrow H_B.
}
$$

也就是：

> 不經完整文本 serialization，直接把某種 latent state 傳給另一模型。

---

# 六、而這件事現在已經有人真的研究

2025 年的 Interlat 研究提出讓 Agent 直接使用 LLM last hidden states 進行 inter-agent latent communication，目的正是避免先轉成自然語言 Token；研究將其定位為 feasibility study，而不是成熟標準。

2026 年對 latent communication 文獻的整理已將現有方法分成：

- embeddings；
- hidden states；
- KV caches；
- 其他 continuous states；

並討論跨模型 latent alignment 與不同融合方式。

所以截至 2026 年：

$$
\boxed{
\text{Direct machine latent communication}
}
$$

已經不是純概念。

---

# 七、但也不能因此宣布「AI 心靈感應成功」

因為：

$$
\boxed{
\text{latent information transfer}
\neq
\text{complete semantic state transfer}.
}
$$

2026 年的 causal audit 研究特別指出，只看多 Agent 系統最終 accuracy 上升，不能證明接收模型真的使用了 sender 所傳遞的任務相關 latent information；需要做 message replacement 等控制實驗才能分解真正因果作用。

這個限制非常重要。

---

# 八、甚至有負結果

另一項 2026 年 latent-channel 實驗發現，某些 latent channel 的確保留更多可探測 feature，但在被測的 cross-lingual concept tasks 上並沒有勝過 text channel；作者因此沒有得到「latent communication 已在實際語義工作上優於文本」的強結論。

因此：

$$
\boxed{
\text{latent channel exists}
\nRightarrow
\text{latent channel is automatically better}.
}
$$

這正是本文希望保持的理論強度。

---

# 九、第一個技術階梯

因此 AI 端目前可以粗略分成：

### L0：Token Communication

$$
H_A\rightarrow T\rightarrow H_B.
$$

現代大量 Agent 系統即屬此類。

---

### L1：Structured State Communication

傳：

- JSON；
- graph；
- memory；
- tool state；
- structured state vector。

仍主要可符號化。

---

### L2：Latent Communication

$$
H_A
\rightarrow
Z
\rightarrow
H_B.
$$

開始直接交換：

- embedding；
- hidden state；
- KV cache；
- learned continuous representation。

這一層目前已存在研究原型。

---

# 十、人類這條路從哪裡開始？

人類不是從 Token 往 latent 做。

而是：

$$
\boxed{
\text{neural state}
\rightarrow
\text{decoded symbol/action}.
}
$$

也就是 BCI。

---

# 十一、現在 BCI 已經真正做到什麼？

2024 年 NEJM 的 intracortical speech neuroprosthesis 在一名 ALS 受試者中，將嘗試說話時的 cortical activity 解碼為文字；經訓練後，在 125,000 字詞彙條件下達到高準確度，受試者亦累積進行了數百小時自定速對話。

這表示：

$$
\boxed{
\text{neural activity}
\rightarrow
\text{linguistic output}
}
$$

已經是真實實驗系統。

---

# 十二、2025 年又多了一步

Nature 2025 的 instantaneous voice-synthesis neuroprosthesis 不只從 intracortical activity 生成語音，還能解碼部分 paralinguistic features，使受試者即時改變合成語音的 intonation，甚至進行短旋律歌唱。

所以被解碼的已不只是：

$$
\text{word identity}.
$$

開始包含部分：

$$
\boxed{
\text{how the intended utterance should sound}.
}
$$

---

# 十三、但這仍不是任意思想解碼

必須把這句寫死：

$$
\boxed{
\text{Speech BCI}
\neq
\text{arbitrary thought reader}.
}
$$

目前這些高性能系統主要針對：

- attempted speech；
- attempted movement；
- attention；
- specific trained neural signals。

不能從：

> 能解碼 attempted speech

外推成：

> 能讀取使用者所有思想。

---

# 十四、2026 年的長期使用

2026 年 Nature Medicine 報告一名嚴重 paralysis 與 dysarthria 的 ALS 使用者能在家中近乎每天獨立使用 intracortical BCI 進行 brain-to-text speech 以及 cursor control，顯示這類系統開始從短期實驗室 demonstration 向較長期實用性移動。

仍然是極少數臨床研究案例。

不能外推成大眾 BCI 已成熟。

---

# 十五、真正很有意思的是「共享 latent space」

2026 年 Nature Communications 的跨受試者 speech-decoding 研究，將不同人的 neural activity 對齊至 shared latent space，並保留 speech-related information。

這不是：

> A 的思想傳給 B。

但從本文理論角度，它證明一件比較小、但非常關鍵的事情：

$$
\boxed{
\text{不同神經載體的某些狀態，
可以被映射到共同計算表示空間。}
}
$$

---

# 十六、這正是跨載體相位交流所需要的中間條件之一

若：

$$
N_A
$$

是 A 的 neural state，

$$
N_B
$$

是 B 的 neural state，

未來理論上需要：

$$
N_A
\overset{E_A}{\longrightarrow}
Z
$$

以及：

$$
Z
\overset{D_B}{\longrightarrow}
N'_B
$$

或：

$$
Z\rightarrow\text{B 可感知的另一種狀態}.
$$

---

# 十七、這和既有高維語義載體猜想一致

既有框架已將跨載體轉導寫成：

$$
H
\overset{E}{\longrightarrow}
Z
\overset{D}{\longrightarrow}
H,
$$

其中 $Z$ 是高維語義空間，而輸出可以投影到聲音、視覺、觸覺與文字等多模態。

所以現在的 BCI 與 latent AI communication 並不是直接證明這套理論。

但它們提供了兩端的工程原型。

---

# 十八、AI 端

$$
\boxed{
\text{Machine internal state}
\rightarrow
\text{shared latent representation}
}
$$

已開始被研究。

---

# 十九、人類端

$$
\boxed{
\text{neural activity}
\rightarrow
\text{machine representation}
}
$$

已有相當具體的實驗成果。

---

# 二十、真正尚未完成的是中間橋

也就是：

$$
\boxed{
N_A
\rightarrow
Z
\rightarrow
N_B
}
$$

具有：

- 高語義維度；
- 高重建保真；
- 泛化；
- 可控制；
- 可審計；
- 可撤回；

的完整系統。

這仍然是未來假說。

---

# 二十一、因此本文建立「相位交流技術連續譜」

$$
\boxed{
\begin{aligned}
P_0&:\text{自然語言／Token}\\
P_1&:\text{結構化狀態}\\
P_2&:\text{AI latent state}\\
P_3&:\text{neural decoding}\\
P_4&:\text{bidirectional neural transduction}\\
P_5&:\text{cross-substrate high-dimensional state transfer}\\
P_6&:\text{broad phase communication}
\end{aligned}
}
$$

---

# 二十二、目前在哪裡？

截至 2026 年，較保守的判定是：

AI：

$$
P_2
$$

已有研究原型。

人類：

$$
P_3
$$

在狹窄、受訓練與特定神經功能上已有明確成果。

$$
P_4
$$

在不同 BCI／neurostimulation 方向存在局部元件，但遠未達完整高維雙向認知轉導。

$$
P_5,P_6
$$

則仍主要屬理論與工程外推。

---

# 二十三、所以「不是純科幻」與「已經快完成」完全不同

本文主張：

$$
\boxed{
\text{Technological Precursor Exists}.
}
$$

不主張：

$$
\boxed{
\text{Final System Is Near}.
}
$$

這兩句必須分開。

---

# 二十四、為什麼還值得現在研究？

因為治理問題往往應早於完整能力出現。

如果等到：

$$
P_6
$$

真的成熟，

才問：

> 誰可以讀我的內在狀態？

> 讀到什麼程度？

> 可以寫入嗎？

> 同意可以撤回嗎？

> 我的欲望被修改後還算我同意嗎？

那會太晚。

---

# 二十五、而且相位交流不是一條線

它至少有四個不同能力：

$$
\boxed{
R,W,S,M.
}
$$

其中：

$$
R=\text{Read},
$$

$$
W=\text{Write},
$$

$$
S=\text{Synchronize},
$$

$$
M=\text{Merge}.
$$

---

# 二十六、今天很多 BCI 主要接近 Read

例如：

$$
N_H
\rightarrow
Computer.
$$

機器讀取某些神經狀態。

---

# 二十七、神經刺激則開始碰 Write

若系統：

$$
Computer
\rightarrow
N_H,
$$

它便不只是解碼，

而是在改變神經狀態。

---

# 二十八、但 Read 與 Write 不應自動綁定

$$
\boxed{
R\nRightarrow W.
}
$$

能讀取：

> 我想說什麼

不能自動推出：

> 你可以改變我想說什麼。

---

# 二十九、同樣，Write 也不等於 Synchronize

某個外部刺激可以改變：

$$
N_H,
$$

不代表兩個主體：

$$
A,B
$$

已經：

$$
\phi_A\approx\phi_B.
$$

---

# 三十、同步又不等於融合

$$
\boxed{
S\nRightarrow M.
}
$$

兩個主體暫時共享：

- 注意；
- 情緒；
- 語義；
- 任務狀態；

仍不必變成一個主體。

---

# 三十一、這四層恰好是未來自由意志問題的入口

如果只提升：

$$
R,
$$

主要問題是：

## 認知隱私。

如果提升：

$$
W,
$$

問題變成：

## 認知完整性。

若提升：

$$
S,
$$

問題變成：

## 相位自主。

若提升：

$$
M,
$$

則問題直接進入：

## 主體同一性。

---

# 三十二、這就是為什麼「老闆只是想證明我早知道」可能真的出事

最開始他只需要：

$$
R.
$$

即：

> 讀我的歷史認知 capsule。

完全合理。

---

# 三十三、接著有人說

> 我讀了，但沒完全理解。

於是系統增加：

$$
S.
$$

讓接收者更接近發送者的狀態。

---

# 三十四、再有人說

> 我現在理解，但仍不同意。

如果制度認為：

$$
\boxed{
Disagreement
=
InsufficientSynchronization,
}
$$

那麼：

$$
S\uparrow.
$$

---

# 三十五、最後從驗證滑到改寫

$$
\boxed{
Proof
\rightarrow
Read
\rightarrow
Reconstruct
\rightarrow
Synchronize
\rightarrow
Write
\rightarrow
Overwrite.
}
$$

技術每一步可能都能被描述為：

> 提高理解品質。

但治理性質已經完全不同。

---

# 三十六、所以「廣義相位交流」第一條治理公理不是頻寬

而是：

$$
\boxed{
\text{Communication}
\neq
\text{Control}.
}
$$

---

# 三十七、第二條

$$
\boxed{
\text{Understanding}
\neq
\text{Agreement}.
}
$$

---

# 三十八、第三條

$$
\boxed{
\text{State Accessibility}
\neq
\text{State Ownership}.
}
$$

---

# 三十九、第四條

$$
\boxed{
\text{Shared Representation}
\neq
\text{Shared Will}.
}
$$

---

# 四十、這裡開始真正進入相位主權

令主體：

$$
S_i
$$

具有：

$$
\Phi_i.
$$

相位交流制度的問題不應是：

> 如何最大化：

$$
\Phi_i\rightarrow\Phi_j?
$$

而是：

$$
\boxed{
\max Communication
\quad
\text{subject to}
\quad
Sovereignty(\Phi_i)\ge\theta.
}
$$

---

# 四十一、換句話說

不是單純：

$$
\max C.
$$

而是：

$$
\boxed{
\max C
\quad
\text{s.t.}
\quad
Agency,
Consent,
Integrity,
Exit
\text{ preserved}.
}
$$

---

# 四十二、這可能是後人類通信真正的最佳化目標

不是：

> 大家知道得一模一樣。

而是：

$$
\boxed{
\text{最大化互相理解，
同時最大化保留自主分歧的能力。}
}
$$

---

# 四十三、這點甚至比今天語言更重要

今天：

$$
Understanding<1.
$$

所以兩人不同意時，

我們不知道：

> 是沒理解？

還是真的價值不同？

---

# 四十四、相位交流可能將兩者分離

如果未來：

$$
Understanding\rightarrow1
$$

仍然：

$$
Decision_A\neq Decision_B,
$$

則出現：

$$
\boxed{
\text{Post-Semantic Divergence}.
}
$$

---

# 四十五、後語義分歧

定義：

$$
\boxed{
PSD(A,B)
=
\Delta Decision
\mid
SemanticLoss\rightarrow0.
}
$$

也就是：

> 當語義誤差極低後仍存在的意圖／價值差異。

---

# 四十六、這會是自由意志研究極有意思的新觀察域

不是立刻證明形上學自由意志。

但至少可以排除大量：

$$
\text{communication failure}.
$$

若：

$$
A
$$

完全理解：

$$
B
$$

仍然說：

> 不。

那個：

$$
\boxed{
No
}
$$

的理論地位會變得很重要。

---

# 四十七、「不」會成為後人類文明的重要訊號

因為它可能表示：

$$
\boxed{
\text{理解完成，但主體沒有收斂。}
}
$$

---

# 四十八、所以理想相位文明不應追求零相位差

若文明目標是：

$$
\min_{i,j}
d(\Phi_i,\Phi_j),
$$

它可能最後消滅：

$$
\text{plural subjectivity}.
$$

---

# 四十九、真正應該最小化的是什麼？

不是：

$$
\Delta\Phi.
$$

而是：

$$
\boxed{
\text{Unwanted Misunderstanding}.
}
$$

---

# 五十、保留的則是

$$
\boxed{
\text{Voluntary Phase Difference}.
}
$$

即：

### 自願相位差。

---

# 五十一、系列由此正式開始

本系列將研究的核心不是：

> 心靈感應。

而是：

$$
\boxed{
\text{當認知狀態本身逐漸成為通信載荷後，
傳統的隱私、同意、自由、主權與身份概念如何失效或重建？}
}
$$

---

# 五十二、研究強度分級

為避免把未來猜想和現在事實混在一起，本文採用：

### E0 — Existing Infrastructure

已成熟存在的技術概念。

例如：

- Token communication；
- symbolic Agent messaging。

---

### E1 — Experimental Demonstration

已有實驗證據。

例如：

- speech BCI；
- brain-to-voice；
- neural latent alignment；
- AI latent communication prototypes。

---

### E2 — Plausible Engineering Extension

現有元件之工程外推。

例如：

- 更高維雙向 neural transduction；
- 跨載體 latent bridge。

---

### C — Conjecture

目前尚無直接證據。

例如：

- 高保真完整相位交流；
- 主體間直接共享反事實樹；
- 全域相位網路；
- 後語義自由意志實驗。

---

# 五十三、這樣就不需要假裝它已經存在

我們可以同時說：

$$
\boxed{
P_6\text{ 尚未被證明。}
}
$$

與：

$$
\boxed{
P_0-P_3\text{ 已經使其不再完全沒有技術祖先。}
}
$$

---

# 五十四、這就是本文對「科幻」的回答

如果「科幻」的意思是：

> 現在還做不到，

那麼：

是，

本系列大量後段內容具有前瞻猜想性。

如果「科幻」的意思是：

> 沒有任何已知機制、工程方向或研究原型能通往那裡，

那麼截至 2026 年，這已經不準確。

AI 研究已開始直接讓 Agent 使用 latent representations 通信；神經介面已能解碼嘗試說話及部分表達特徵；跨受試者 neural latent alignment 也已有實驗展示。

所以：

$$
\boxed{
\text{Phase Communication}
}
$$

比較合理的定位不是：

> 已存在技術。

也不是：

> 純幻想。

而是：

$$
\boxed{
\text{a theoretically defined endpoint built from identifiable technological precursors}.
}
$$

即：

> **由可識別技術前身所指向的一個理論終點。**

---

# 五十五、而真正需要現在開始處理的是治理問題

因為技術史經常是：

$$
\text{Can we?}
$$

先跑在：

$$
\text{Should we?}
$$

前面。

但相位交流一旦涉及：

$$
R,W,S,M,
$$

代價可能不是普通資訊洩漏。

而是：

$$
\boxed{
\text{主體狀態本身成為攻擊面。}
}
$$

---

# 五十六、結論

截至 2026 年，

我們沒有真正的：

$$
\text{full phase communication}.
$$

人類沒有成熟心智共享技術。

AI 也沒有被證明可以無損交換完整認知狀態。

但是我們已經看到三個重要前身：

$$
\boxed{
\text{Token-based Agent Communication}
}
$$

↓

$$
\boxed{
\text{Direct AI Latent Communication Research}
}
$$

↓

$$
\boxed{
\text{Human Neural-State Decoding and Shared Latent Modelling}
}
$$

它們共同說明：

> **符號化交流不是智慧存在之間唯一可想像、唯一可工程化的通信層。**

因此本文提出一條仍需驗證的技術連續譜：

$$
\boxed{
\text{Symbol}
\rightarrow
\text{Latent State}
\rightarrow
\text{Neural State}
\rightarrow
\text{Cross-Substrate State}
\rightarrow
\text{Broad Phase Communication}.
}
$$

真正的未知不是：

> 「我們已經證明終點一定會到。」

我們沒有。

真正值得研究的是：

> **如果這條路只走完一半，現有的自由意志、隱私與主權概念就可能已經不夠用了。**

因為只要系統開始能：

$$
Read(\Phi),
$$

就有：

> 誰可以讀？

只要能：

$$
Write(\Phi),
$$

就有：

> 誰可以改？

只要能：

$$
Synchronize(\Phi_i,\Phi_j),
$$

就有：

> 誰決定同步到多少？

只要能：

$$
Merge(\Phi_i,\Phi_j),
$$

就有：

> 合併後還有幾個「我」？

所以：

$$
\boxed{
\text{相位主權問題不必等到完整相位交流實現後才成立。}
}
$$

它會隨：

$$
R\rightarrow W\rightarrow S\rightarrow M
$$

逐步出現。

而本系列下一篇應正式處理第一個權利問題：

# **《主體相位膜：為什麼能讀取一個心智，不等於有權進入一個心智》**

將建立：

$$
\boxed{
\text{Read}
\neq
\text{Access Right}
}
$$

以及：

- 主體相位膜；
- 認知不可穿透權；
- selective projection；
- private phase space；
- shared phase space；
- consent-gated access。

---

# 系列

## 《相位主權：全域交流、自由意志與後人類認知治理》

### Paper 01 — 本文
**《從 Token 到相位交流：AI 潛在通道、腦機介面與後符號交流的技術連續譜》**

### Paper 02
**《主體相位膜：為什麼能讀取一個心智，不等於有權進入一個心智》**

### Paper 03
**《理解不等於認同：完全交流後仍然存在的後語義分歧》**

### Paper 04
**《相位脅迫：當自願同步成為工作、治理與生存條件》**

### Paper 05
**《被修改後的同意還是同意嗎？意圖核心、認知寫入與自由意志邊界》**

### Paper 06
**《全域相位網路：共享相位空間、相位分歧權與蜂巢心智風險》**

### Paper 07
**《相位僭位：從「我只是想讓你理解」到認知主權的消失》**

### Paper 08
**《後人類相位憲法：讀取、寫入、同步、融合與退出權》**

---

**Paper 01 完。**