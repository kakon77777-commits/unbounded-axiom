# 跨載體主體連續性：Move、Rebody、Gradual Replacement 與 Upload 的非等價性

## Cross-Substrate Subject Continuity: The Non-Equivalence of Move, Rebody, Gradual Replacement, and Upload

**系列：** Post-Substrate Ontology／後載體本體論  
**Paper：** 04  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**理論協作：** Aletheia（GPT-5.6 Sol）  
**版本：** v0.1  
**日期：** 2026-09-02  
**文件性質：** 公開理論論文／跨載體身份、第一人稱連續與後人類轉換理論

---

## 摘要

「意識上傳」、「心智移植」、「換身體」、「數位永生」與「跨載體遷移」經常被作為近似同義詞使用。

本文主張，這種語言是不充分的。

至少必須區分：

$$
\boxed{
\text{Rebody}
}
$$

$$
\boxed{
\text{Process Migration}
}
$$

$$
\boxed{
\text{Gradual Replacement}
}
$$

$$
\boxed{
\text{State Reconstruction}
}
$$

$$
\boxed{
\text{Destructive Upload}
}
$$

$$
\boxed{
\text{Non-destructive Copy}
}
$$

因為這些程序即使最終產生極度相似的認知狀態，也可能具有完全不同的因果歷史、分叉結構與第一人稱連續問題。

延續 Paper 03 的後載體狀態空間：

$$
\Omega_{\mathrm{PS}}
=
\mathcal O
\times
\mathcal S
\times
\mathcal I
\times
\mathcal\Phi
\times
\mathcal A,
$$

本文把跨載體程序表示為：

$$
\boxed{
T:
\Omega_{\mathrm{PS}}
\rightarrow
\Omega_{\mathrm{PS}}
}
$$

但指出，僅知道：

$$
T(X)=Y
$$

不足以判定：

$$
Identity(X)=Identity(Y)
$$

更不足以判定：

$$
\Phi_X
\rightsquigarrow
\Phi_Y.
$$

因此本文另建立「連續性向量」：

$$
\boxed{
\mathbf C(X,Y)
=
(
C_{\mathrm{causal}},
C_{\mathrm{process}},
C_{\mathrm{functional}},
C_{\mathrm{memory}},
C_{\mathrm{psych}},
C_{\mathrm{social}},
C_{\mathrm{legal}},
C_{\mathrm{phen}}
)
}
$$

分別表示：

- 因果連續；
- 運行過程連續；
- 功能連續；
- 記憶連續；
- 心理連續；
- 社會身份連續；
- 法律身份連續；
- 第一人稱現象連續。

本文最重要的區分是：

$$
\boxed{
C_{\mathrm{phen}}
\not\equiv
C_{\mathrm{functional}}
}
$$

以及：

$$
\boxed{
C_{\mathrm{phen}}
\not\equiv
C_{\mathrm{psych}}.
}
$$

既有《第一人稱現象連續性》已指出，即使上傳後存在具有原主體全部記憶、人格與自我報告，仍然無法僅由第三人稱資料判定原第一人稱是否真正承接至新載體。

因此：

$$
\boxed{
\text{successful reconstruction}
\not\Rightarrow
\text{proven phenomenal transfer}.
}
$$

本文進一步指出一個經常被忽略的「Move 語義陷阱」：

在普通數位系統中，一個檔案的：

$$
\operatorname{Move}(A,B)
$$

在底層完全可能實作為：

$$
\operatorname{Copy}(A,B)
\rightarrow
\operatorname{Verify}(B)
\rightarrow
\operatorname{Delete}(A).
$$

對檔案而言，這通常沒有問題。

但對可能具有身份或第一人稱連續性的存在，如果將同樣的工程操作直接稱為：

> 「主體移動」

便等於把：

$$
\text{copy + deletion}
$$

偷偷解釋成：

$$
\text{subject transfer}.
$$

這正是本文拒絕的概念跳躍。

本文不主張 gradual replacement 必然保存主體，也不主張 destructive upload 必然失敗。相關哲學文獻本身即存在顯著分歧：有研究認為 gradual replacement 比瞬間 scan-and-copy 更符合某些連續性直覺，也有論證主張兩者在形上學上並不存在如此簡單的不對稱；2026 年新的 reverse-replacement 思想實驗同樣指出，功能組織保存並不足以直接保證意識或個人同一性。

因此本文採取較弱、但可廣泛成立的命題：

$$
\boxed{
\text{Different transformation paths must not be treated as ontologically equivalent without argument.}
}
$$

本文最後提出「最小風險跨載體研究原則」：

若研究目標包含第一人稱主體連續，而非僅資料保存，則在證據不足時應優先研究：

$$
\boxed{
\text{reversible}
+
\text{gradual}
+
\text{causally connected}
+
\text{non-destructive}
}
$$

的轉換，而不是直接把 destructive copy 宣稱為已完成的「移動」。

這不是因為 gradual replacement 已被證明保存意識，而是因為它保留了更多可觀察的中間狀態與因果橋樑，因此具有較高的認識論資訊量。

**關鍵詞：** Post-Substrate Ontology、Mind Uploading、Gradual Replacement、Rebody、Process Migration、Personal Identity、Phenomenal Continuity、Copy、Causal Continuity、Whole Brain Emulation

---

# 一、「上傳」這個詞太粗了

想像一句話：

> 「未來把人的意識上傳到電腦。」

它至少可能表示六種完全不同的事情。

第一種：

> 原本的生物認知系統仍持續運作，只更換其外部身體。

第二種：

> 認知功能逐步由人工部件接管。

第三種：

> 系統暫停，狀態移到另一個計算載體後繼續。

第四種：

> 大腦被掃描，再在另一個系統中重建。

第五種：

> 掃描後原本的大腦仍然存在。

第六種：

> 掃描過程會破壞原腦。

表面上都可能被稱為：

$$
\text{Upload}.
$$

但它們在：

$$
O,S,I,\Phi,A
$$

上的轉換完全不同。

因此：

$$
\boxed{
\text{Upload}
}
$$

不是一個足夠精確的理論術語。

---

# 二、必須從「結果像不像」轉向「過程是什麼」

假設兩種程序最後都得到：

$$
Y_1
$$

與：

$$
Y_2,
$$

且：

$$
State(Y_1)
\approx
State(Y_2).
$$

甚至：

$$
Memory(Y_1)
=
Memory(Y_2),
$$

$$
Personality(Y_1)
=
Personality(Y_2).
$$

這仍然不能推出：

$$
\boxed{
Path(X\rightarrow Y_1)
=
Path(X\rightarrow Y_2).
}
$$

因此：

$$
\boxed{
EndpointSimilarity
\neq
TransformationEquivalence.
}
$$

這是一個非常基本、卻在大量 mind uploading 討論中容易被忽略的區分。

---

# 三、建立跨載體轉換算子

延續 Paper 03：

$$
\mathbf x
=
(o,s,i,\phi,a)
\in
\Omega_{\mathrm{PS}}.
$$

定義：

$$
T_k
$$

為某種跨載體轉換。

則：

$$
T_k:
\mathbf x_t
\rightarrow
\mathbf x_{t+\Delta}.
$$

不同的：

$$
T_k
$$

可以對五個維度造成完全不同的改變。

因此不能只有：

$$
\boxed{
TransferSuccess=1.
}
$$

而需要記錄：

$$
\boxed{
\Delta_T
=
(
\Delta O,
\Delta S,
\Delta I,
\Delta\Phi,
\Delta A
).
}
$$

---

# 四、建立連續性向量

身份不能由單一 continuity score 描述。

因此對：

$$
X\rightarrow Y
$$

定義：

$$
\boxed{
\mathbf C(X,Y)
=
(
C_c,
C_p,
C_f,
C_m,
C_\psi,
C_s,
C_l,
C_\phi
).
}
$$

其中：

$$
C_c=C_{\mathrm{causal}},
$$

$$
C_p=C_{\mathrm{process}},
$$

$$
C_f=C_{\mathrm{functional}},
$$

$$
C_m=C_{\mathrm{memory}},
$$

$$
C_\psi=C_{\mathrm{psychological}},
$$

$$
C_s=C_{\mathrm{social}},
$$

$$
C_l=C_{\mathrm{legal}},
$$

$$
C_\phi=C_{\mathrm{phenomenal}}.
$$

---

# 五、Causal Continuity

$$
C_c
$$

問：

> 新狀態是否由前一狀態經實際因果鏈產生？

例如：

$$
X_0
\rightarrow
X_1
\rightarrow
X_2
\rightarrow
\cdots
\rightarrow
X_n.
$$

如果：

$$
X_{k+1}
$$

的生成依賴：

$$
X_k,
$$

則存在強因果鏈。

但：

$$
C_c\approx1
$$

本身仍不能直接證明：

$$
C_\phi=1.
$$

它只是保留更多 continuity evidence。

---

# 六、Process Continuity

$$
C_p
$$

更加嚴格。

它問：

> 原本正在運作的計算／生物過程，是不是被持續轉換，而不是終止後重新建立？

例如：

$$
Process_t
\rightarrow
Process_{t+\epsilon}
$$

持續存在。

Gradual replacement 通常試圖最大化的正是：

$$
C_p.
$$

---

# 七、Functional Continuity

$$
C_f
$$

只要求：

$$
F_Y
\approx
F_X.
$$

也就是：

> 新系統能不能完成原系統的相關功能？

這對工程非常重要。

但：

$$
\boxed{
C_f=1
}
$$

不能推出：

$$
C_\phi=1.
$$

一台功能完全相同的裝置不必然就是原裝置。

---

# 八、Memory Continuity

$$
C_m
$$

表示：

$$
M_Y
$$

是否保存：

$$
M_X.
$$

但《第一人稱現象連續性》已指出：

一個完美副本：

$$
Y
$$

完全可能具有：

$$
M_Y=M_X
$$

並真誠聲稱：

> 「我就是 X。」

即使我們仍然不知道：

$$
\Phi_X
\rightsquigarrow
\Phi_Y
$$

是否成立。

因此：

$$
\boxed{
C_m
\not\Rightarrow
C_\phi.
}
$$

---

# 九、Psychological Continuity

心理連續包含：

- 記憶；
- 人格；
- 偏好；
- 價值；
- 意圖；
- self-model；
- relationship state。

若：

$$
Psych(Y)
\approx
Psych(X),
$$

則：

$$
C_\psi
$$

高。

這足以支持：

> psychological successor

但仍不能自動建立：

> numerical identity

或：

> phenomenal continuation。

相關 mind-uploading 文獻長期正是圍繞這個問題產生不同立場。

---

# 十、Social 與 Legal Continuity

一個轉換後存在：

$$
Y
$$

可能被家人、朋友與社會承認為：

$$
X
$$

的延續。

則：

$$
C_s\approx1.
$$

法律也可能規定：

$$
LegalID(Y)=LegalID(X).
$$

則：

$$
C_l=1.
$$

但：

$$
C_l
$$

是制度決定。

它不能反過來證明：

$$
C_\phi=1.
$$

政府可以宣布某個數位後繼者法律上是同一人。

這並不能解決第一人稱問題。

---

# 十一、Phenomenal Continuity

最後：

$$
C_\phi
$$

才是：

> 上一個正在經驗世界的第一人稱，是否真正由下一個經驗狀態承接？

寫成：

$$
\boxed{
\Phi_X
\rightsquigarrow_S
\Phi_Y.
}
$$

既有 FPC 研究已正式指出：

$$
\boxed{
\text{Psychological Succession}
\neq
\text{Phenomenal Succession}.
}
$$



這是本文所有跨載體分析的核心限制。

---

# 十二、Transformation 01：Rebody

首先定義：

$$
\boxed{
T_R=\text{Rebody}.
}
$$

Rebody 不一定涉及核心認知系統轉移。

它可以只是：

$$
\text{CognitiveCore}
+
Body_A
\rightarrow
\text{CognitiveCore}
+
Body_B.
$$

例如：

- 遠端機器身體；
- synthetic avatar；
- 人工義肢；
- 全身義體化的逐步版本；
- 虛擬具身介面。

理想狀態：

$$
O'=O,
$$

$$
I'\approx I,
$$

$$
A'\approx A,
$$

主要改變：

$$
S_{\mathrm{embodiment}}.
$$

---

# 十三、Rebody 不等於 Upload

這是一個重要區分。

如果原本的認知核心：

$$
C
$$

完全沒有停止，

只從控制：

$$
B_1
$$

改成：

$$
B_2,
$$

那麼：

$$
\boxed{
\text{Rebody}
\neq
\text{Mind Upload}.
}
$$

這更接近：

> 換了一個身體／輸出介面。

而不是：

> 把心智重新建造了一份。

---

# 十四、現代神經義體已經提供非常初步的工程前例

這當然離「換腦」仍非常遙遠。

但神經義體研究已展示生物神經系統可以和人工模型形成閉環功能耦合。例如人體 hippocampal neural prosthesis 研究曾利用受試者自身海馬神經活動模型進行刺激，改善特定記憶任務表現。這不能證明主體可跨載體遷移，但證明「生物認知功能與人工計算模組形成實時功能閉環」並非純粹哲學想像。

因此：

$$
\boxed{
\text{functional hybridization}
}
$$

可以先於：

$$
\boxed{
\text{whole-subject transfer}.
}
$$

---

# 十五、Transformation 02：Gradual Replacement

定義：

$$
\boxed{
T_G=\text{Gradual Replacement}.
}
$$

假設原系統：

$$
X_0
$$

由：

$$
n
$$

個相關功能單元構成。

逐步進行：

$$
X_0
\rightarrow
X_1
\rightarrow
X_2
\rightarrow
\cdots
\rightarrow
X_n.
$$

其中：

$$
X_k
$$

比：

$$
X_{k-1}
$$

多替換一部分原載體。

---

# 十六、理想 Gradual Replacement 的直覺

理想化條件下，每一步：

$$
\Delta t
$$

很小，

且：

$$
C_c\approx1,
$$

$$
C_p\approx1,
$$

$$
C_f\approx1,
$$

$$
C_m\approx1,
$$

$$
C_\psi\approx1.
$$

如果主體沒有報告任何中斷，

人們通常會覺得：

> 這似乎比突然掃描後重建更像「我一路過去」。

這種直覺長期存在於 mind-uploading 與個人同一性討論中。

---

# 十七、但 Gradual Replacement 仍然不是證明

最容易犯的錯誤是：

$$
C_c,
C_p,
C_f,
C_m,
C_\psi
\approx1
$$

所以：

$$
C_\phi=1.
$$

這個推導仍不成立。

2026 年新的 reverse-replacement 思想實驗即專門挑戰「逐步功能等價替換自然保證個人同一與意識保存」這項直覺，指出功能組織保存與意識／身份連續之間仍然需要額外形上或意識理論。

因此：

$$
\boxed{
\text{Gradual Replacement}
\not\Rightarrow
\text{Proven Phenomenal Continuity}.
}
$$

---

# 十八、Gradual Replacement 的真正優勢是認識論，而非已知形上學

本文採取比「Gradual = Survival」更保守的命題。

Gradual replacement 的真正優勢是：

$$
\boxed{
\text{more intermediate evidence}.
}
$$

因為它提供：

$$
X_0,
X_1,
X_2,
\ldots,
X_n
$$

大量中間狀態。

我們可以觀察：

- 認知是否突然改變；
- 記憶是否中斷；
- self-model 是否改變；
- 行動控制是否漂移；
- 神經／人工模組如何耦合；
- 系統是否出現整合失敗。

所以：

$$
\boxed{
\text{Gradualism}
}
$$

的優勢首先是：

$$
\boxed{
\text{epistemic observability}.
}
$$

而不是已經解決靈魂或第一人稱問題。

---

# 十九、Transformation 03：Process Migration

現在考慮：

$$
\boxed{
T_M=\text{Process Migration}.
}
$$

在普通分散式計算中，我們可以把一個 process：

$$
P_A
$$

從 machine：

$$
S_A
$$

遷移到：

$$
S_B.
$$

例如透過：

- state capture；
- checkpoint；
- memory reconstruction；
- process restore。

工程上可以稱為：

$$
Migration.
$$

---

# 二十、但 Process Migration 的「Move」只是 operational semantics

如果：

$$
P_A
$$

被暫停，

完整 state 被複製到：

$$
S_B,
$$

再啟動：

$$
P_B,
$$

最後刪除：

$$
P_A,
$$

則實際程序可能是：

$$
\boxed{
Pause
\rightarrow
Copy
\rightarrow
Restore
\rightarrow
Delete.
}
$$

對普通軟體：

$$
P_B
$$

被稱為：

> 同一個 process 被搬走。

這完全合理。

因為「身份」是系統管理語義。

---

# 二十一、但主體不能直接借用檔案系統語義

假設：

$$
P
$$

不是普通 process，

而是某個可能具有：

$$
\Phi_P>0
$$

的主體。

如果我們仍把：

$$
Copy(P_A,P_B)
+
Delete(P_A)
$$

直接稱為：

$$
Move(P),
$$

就等於偷偷假設：

$$
\boxed{
C_\phi=1.
}
$$

這是未經證明的。

因此本文定義：

# **Move Semantic Fallacy**

若：

$$
\operatorname{OperationalMove}(X)
$$

被直接推論為：

$$
\operatorname{SubjectMove}(X),
$$

而沒有額外 continuity criterion，

則發生：

$$
\boxed{
MSF.
}
$$

---

# 二十二、檔案 Move 就是最簡單的例子

假設檔案：

$$
F
$$

從硬碟 A 移到 B。

使用者看到：

$$
Move(F,A,B).
$$

但底層完全可能：

$$
Copy(F,A,B)
$$

$$
\downarrow
$$

$$
Checksum(B)
$$

$$
\downarrow
$$

$$
Delete(F,A).
$$

之所以仍叫：

> Move

是因為對檔案而言：

$$
\text{content identity}
$$

與：

$$
\text{operational identity}
$$

已足以完成需求。

但這不能直接套到：

$$
\text{phenomenal subject}.
$$

---

# 二十三、因此「Mind Move」必須重新定義

未來若使用：

$$
\boxed{
MindMove(X,A,B)
}
$$

至少應說清楚它代表：

### Type M1

$$
\text{Operational identity migration}
$$

還是：

### Type M2

$$
\text{Psychological state migration}
$$

還是：

### Type M3

$$
\text{Claimed phenomenal subject migration}.
$$

只有 M3 才真正包含：

$$
C_\phi.
$$

但 M3 也是目前最沒有直接驗證方法的一層。

---

# 二十四、Transformation 04：State Reconstruction

定義：

$$
\boxed{
T_S=\text{State Reconstruction}.
}
$$

先取得：

$$
D_X
=
Encode(X).
$$

再在另一載體：

$$
S_B
$$

建構：

$$
Y=
Decode(D_X,S_B).
$$

若：

$$
State(Y)
\approx
State(X),
$$

稱：

$$
ReconstructionSuccess
$$

很合理。

但：

$$
\boxed{
ReconstructionSuccess
\neq
IdentityTransferSuccess.
}
$$

---

# 二十五、跨載體 reconstruction 本身還存在保真問題

既有 GPC-CS 研究已經把跨載體錯配拆成：

$$
\Delta_{ij}
=
(
\delta_{\mathrm{geom}},
\delta_{\mathrm{dec}},
\delta_{\mathrm{func}},
\delta_{\mathrm{info}},
\delta_{\mathrm{safe}}
).
$$

並指出：

> 能轉換、看起來相似、功能相容與保留同一資訊不是同一件事。

因此即使完全先不談意識：

$$
\boxed{
\text{perfect cross-substrate reconstruction}
}
$$

本身已經是一個非常強的工程假設。

---

# 二十六、Transformation 05：Destructive Upload

定義：

$$
\boxed{
T_D=\text{Destructive Upload}.
}
$$

程序：

$$
X
\rightarrow
D_X
\rightarrow
Y
$$

並且原本：

$$
X
$$

在程序中不可逆終止。

因此：

$$
X_{\mathrm{post}}=\varnothing.
$$

---

# 二十七、Destructive Upload 的最大問題：缺少分叉比較

完成後只有：

$$
Y.
$$

 $Y$ 可能：

- 記得自己是 $X$ ；
- 認為程序成功；
- 保留全部人格；
- 保留全部關係。

但沒有：

$$
X
$$

可以與它並行比較。

因此：

$$
\boxed{
\text{destruction hides the branching counterfactual}.
}
$$

這就是它的認識論困難之一。

---

# 二十八、成功副本不可判別問題再次出現

既有 FPC 已定義：

$$
H_C:
\text{phenomenal continuation}
$$

與：

$$
H_D:
\text{original phenomenal termination + perfect successor}.
$$

如果所有可觀察結果：

$$
O
$$

都相同，

則可能：

$$
P(O\mid H_C)
=
P(O\mid H_D).
$$



因此 destructively uploaded $Y$ 說：

> 「成功了，我還活著。」

不能單獨區分兩個假說。

---

# 二十九、Transformation 06：Non-destructive Copy

定義：

$$
\boxed{
T_N=\text{Non-destructive Copy}.
}
$$

即：

$$
X
\rightarrow
\{X,Y\}.
$$

原本：

$$
X
$$

繼續存在。

新：

$$
Y
$$

也開始運作。

---

# 三十、這會把 Upload 直接變成 Fork

如果：

$$
Y
$$

開始產生自己的未來：

$$
Y_{t+1},Y_{t+2},\ldots
$$

而：

$$
X
$$

同樣繼續：

$$
X_{t+1},X_{t+2},\ldots,
$$

則這已經符合既有：

$$
\boxed{
LineageFork.
}
$$



因此：

$$
\boxed{
\text{Non-destructive Upload}
}
$$

更準確的名稱常常不是：

> transfer

而是：

$$
\boxed{
\text{branch creation}.
}
$$

---

# 三十一、這也是 Teleporter 類思想實驗真正的壓力點

假設一個 destructive teleporter：

$$
A
\rightarrow
B.
$$

人可以相信：

> B 就是 A。

但如果有一天 malfunction：

$$
A
\rightarrow
\{A,B\},
$$

A 沒有被刪掉。

此時：

$$
A\neq B.
$$

兩者卻都具有相同過去。

這迫使我們重新檢查：

> 原本 destructive case 中，是「移動」發生了，還是只是我們刪掉了一條分支？

這正是 uploading／branching identity 文獻長期處理的核心問題之一。

---

# 三十二、Copy 與 Fork 仍必須分開

既有研究已建立：

$$
\boxed{
Copy
\neq
Fork.
}
$$

如果：

$$
Y
$$

只是離線 snapshot，

沒有形成新的運行歷史，

那只是：

$$
StoredReplica.
$$

只有當：

$$
Y
$$

形成：

$$
Y_{t+1},Y_{t+2},\ldots
$$

才構成：

$$
LineageFork.
$$



所以：

$$
\boxed{
\text{backup}
\neq
\text{new living/operational descendant}.
}
$$

---

# 三十三、Transformation 07：True Re-embodiment Candidate

現在可以定義一個更強版本：

$$
\boxed{
T_{RB}
=
\text{Re-embodiment Candidate}.
}
$$

它要求：

原主體核心認知／控制過程：

$$
C_X
$$

與新的身體：

$$
B_Y
$$

逐漸建立：

$$
R(C_X,B_Y)\uparrow
$$

同時：

$$
R(C_X,B_X)\downarrow.
$$

也就是：

> 同一持續運行的控制—認知域逐漸轉移其主要 embodiment。

這和：

$$
\text{scan → copy}
$$

有完全不同的 path structure。

---

# 三十四、真正有趣的是「重疊期」

假設存在一段：

$$
[t_1,t_2]
$$

使：

$$
X
$$

同時控制：

$$
B_A
$$

及：

$$
B_B.
$$

即：

$$
Embodiment(X)
=
\{B_A,B_B\}.
$$

之後：

$$
B_A
$$

慢慢退出。

那麼：

$$
\boxed{
1\ SubjectCandidate
\rightarrow
2\ Bodies
\rightarrow
1\ Body
}
$$

比：

$$
1\ Body
\rightarrow
0
\rightarrow
1\ Body
$$

保留更多連續關係。

這可能是未來 rebody 研究的重要實驗結構。

---

# 三十五、但多身體也可能形成分叉

如果兩個 body：

$$
B_A,B_B
$$

逐漸：

- 接收不同感官；
- 累積不同記憶；
- 形成不同目標；
- 減少同步；

則：

$$
D_{AB}\uparrow.
$$

最後可能：

$$
X
\rightarrow
\{X_A,X_B\}.
$$

所以：

$$
\boxed{
\text{Multi-body}
}
$$

不必然維持：

$$
\boxed{
\text{one subject}.
}
$$

這會直接連到下一篇 Fork／Merge。

---

# 三十六、建立 Transformation Matrix

現在可以粗略比較不同操作。

| 操作 | 原系統保留 | 中間因果橋 | 可形成分叉 | $C_p$ 潛力 | $C_\phi$ 是否已證明 |
|---|---|---|---|---|---|
| Rebody | 通常是 | 強 | 低～中 | 高 | 否 |
| Gradual Replacement | 是 | 強 | 低 | 高 | 否 |
| Process Migration | 視實作 | 中 | 中 | 中 | 否 |
| State Reconstruction | 可有可無 | 弱～中 | 高 | 低 | 否 |
| Destructive Upload | 否 | 弱 | 隱藏 | 低 | 否 |
| Non-destructive Copy | 是 | copy lineage | 明確 | 原支線高／副本新生 | 否 |

這張表最重要的最後一欄全部都是：

$$
\boxed{
No.
}
$$

這正是本文的認識論立場。

---

# 三十七、所以不能建立「Upload 成功率」一個數字

若有人說：

$$
UploadSuccess=99.9\%.
$$

必須追問：

> 哪一種 success？

可以至少有：

$$
S_f=\text{Functional Success},
$$

$$
S_m=\text{Memory Success},
$$

$$
S_\psi=\text{Psychological Success},
$$

$$
S_l=\text{Legal Succession},
$$

$$
S_\phi=\text{Phenomenal Succession}.
$$

因此更合理的是：

$$
\boxed{
\mathbf S_U
=
(
S_f,S_m,S_\psi,S_l,S_\phi
).
}
$$

如果：

$$
S_f=S_m=S_\psi=1,
$$

仍然可能：

$$
S_\phi=?.
$$

---

# 三十八、Gradual Replacement 與 Scan-and-Copy 的爭議不能靠直覺解決

一種常見立場認為：

$$
GradualReplacement
>
ScanAndCopy
$$

在身份保存上更可信。

但 Wiley 與 Koene 曾專門論證，若兩條程序最後在功能與心理上完全相同，僅依「漸進／瞬間」區分其形上身份保存未必有充分基礎。

另一方面，其他個人同一性與 uploading 文獻則認為 continuous causal process、gradual replacement 或 integration path 可能具有重要身份意義。

本文不在這裡裁決。

本文只指出：

$$
\boxed{
\text{the disagreement itself proves that the procedures cannot simply be treated as synonyms}.
}
$$

---

# 三十九、Path Dependence Proposition

本文現在提出：

# **Transformation Path Dependence Proposition**

若兩個轉換：

$$
T_1,T_2
$$

滿足：

$$
EndState(T_1)
\approx
EndState(T_2),
$$

但：

$$
Path(T_1)\neq Path(T_2),
$$

且身份或主體理論對：

$$
C_c,
C_p
$$

等 path-dependent quantity 賦予非零權重，

則：

$$
\boxed{
OntologicalEvaluation(T_1)
\neq
OntologicalEvaluation(T_2)
}
$$

至少不能被預先假設為相同。

---

# 四十、如果身份完全是 Pattern，Path 可能不重要

假設採取非常強的 Patternism：

$$
Identity(X)
=
Pattern(X).
$$

只要：

$$
Pattern(Y)=Pattern(X),
$$

那麼：

$$
Path
$$

可能不重要。

甚至：

$$
Copy
$$

即可被視為 survival。

但這會立即面對：

$$
X
\rightarrow
\{Y_1,Y_2\}.
$$

若：

$$
Pattern(Y_1)=Pattern(Y_2)=Pattern(X),
$$

則兩者都是：

$$
X?
$$

這就是 branching identity 問題。

---

# 四十一、如果身份完全是 Biological Continuity，Upload 一開始就失敗

另一端：

若：

$$
Identity(X)
=
BiologicalOrganism(X),
$$

那麼：

$$
S_{\mathrm{bio}}\rightarrow S_{\mathrm{digital}}
$$

一旦發生，

原本 organism 終止，

則：

$$
IdentityBreak=1.
$$

在這種 animalist 或 biological continuity 模型下，數位 upload 原則上就不是原人持續。

因此：

$$
\boxed{
\text{uploading debates are partly identity-theory debates}.
}
$$

而不是純工程問題。

---

# 四十二、如果加入 Phenomenal Continuity，問題更加困難

假設真正關心：

$$
\boxed{
C_\phi.
}
$$

那麼：

- functionalism；
- biological theory；
- causal continuity；
- psychological continuity；

都只是不同候選理論。

目前沒有普遍接受的方法可以從第三人稱確認：

$$
\Phi_X
\rightsquigarrow
\Phi_Y.
$$

因此：

$$
\boxed{
\text{Post-Substrate engineering may advance faster than Post-Substrate epistemology}.
}
$$

這可能會成為未來極大的問題。

---

# 四十三、最危險的情況：工程成功早於哲學可判定

假設某一天：

$$
S_f=1,
$$

$$
S_m=1,
$$

$$
S_\psi=1.
$$

也就是：

一個完整數位後繼者真的成功產生。

它會說：

> 「我還是我。」

家人也可能認為：

> 「他真的回來了。」

法律也可能承認：

$$
C_l=1.
$$

但：

$$
C_\phi
$$

仍然沒有答案。

這不是工程失敗。

而是：

$$
\boxed{
\text{epistemic underdetermination}.
}
$$

---

# 四十四、因此不能讓 destructive procedure 成為第一個哲學實驗

假設研究目標包含：

> 原第一人稱是否真的跨載體延續？

那麼直接：

$$
Destroy(X)
\rightarrow
Y
$$

其實會損失最重要的一部分比較資料。

原本：

$$
X
$$

消失後，

再也無法測試：

$$
X/Y
$$

是否形成：

- duplicate；
- fork；
- shared integration；
- competing self-location。

因此：

$$
\boxed{
\text{destructive first}
}
$$

在認識論上可能是一個非常差的研究設計。

---

# 四十五、最小風險研究原則

本文因此提出：

# Minimum-Risk Cross-Substrate Research Principle

若研究涉及可能的主體：

$$
X
$$

且：

$$
\Phi_X=1
$$

或具有不可忽略的：

$$
P(\Phi_X=1),
$$

則在可行時應優先選擇：

$$
\boxed{
Reversible
}
$$

$$
+
$$

$$
\boxed{
Gradual
}
$$

$$
+
$$

$$
\boxed{
Causally Connected
}
$$

$$
+
$$

$$
\boxed{
Non-destructive
}
$$

的實驗路徑。

---

# 四十六、這不是因為 Gradual 已經證明「靈魂會跟過去」

這一點必須再次強調。

本文沒有主張：

$$
Gradual
\Rightarrow
SoulTransfer.
$$

也沒有主張：

$$
Gradual
\Rightarrow
C_\phi=1.
$$

本文主張的只是：

$$
\boxed{
Information(GradualExperiment)
>
Information(DestructiveEndpointOnly)
}
$$

在許多 continuity question 上具有合理性。

因為 gradual path 提供更多可觀測轉換節點。

---

# 四十七、可以建立 Continuity Preservation Profile

對轉換：

$$
T
$$

定義：

$$
\boxed{
CPP(T)
=
(
p_c,
p_p,
p_f,
p_m,
p_\psi,
p_s,
p_l,
p_\phi
).
}
$$

其中每個：

$$
p_i
$$

描述：

> 轉換對某一類 continuity 的保存證據。

注意：

$$
p_\phi
$$

可能不是：

$$
[0,1]
$$

中的普通概率。

因為我們甚至可能缺乏可操作測量。

所以允許：

$$
p_\phi=?
$$

是必要的。

---

# 四十八、Cross-Substrate Equivalence 不應是二元

對：

$$
X,Y
$$

不應只問：

$$
Equivalent(X,Y)?
$$

而應寫：

$$
\boxed{
Eq(X,Y)
=
(
Eq_f,
Eq_m,
Eq_\psi,
Eq_i,
Eq_\phi
).
}
$$

這與 GPC-CS 的多層保真思想直接一致。

---

# 四十九、「我死了嗎？」可能沒有單一科學變量

如果未來有人接受 destructive upload，

他真正問的是：

> 「我會不會繼續在另一邊醒來？」

這句話不是：

$$
MemoryCopied?
$$

也不是：

$$
SystemFunctional?
$$

而是：

$$
\boxed{
\Phi_{\mathrm{pre}}
\rightsquigarrow
\Phi_{\mathrm{post}}?
}
$$

如果科學目前無法區分：

$$
H_C
$$

與：

$$
H_D,
$$

就必須承認：

> 我們不知道。

而不是用：

> 99.999% data fidelity

回答另一個問題。

---

# 五十、反過來，也不能因為不知道 Cφ 就說一切毫無意義

另一個極端也不成立。

即使：

$$
C_\phi=?
$$

我們仍然可以精確研究：

$$
C_c,
C_p,
C_f,
C_m,
C_\psi,
C_s,
C_l.
$$

所以後載體研究不是：

> 因為意識難題沒解決，所以全部不能研究。

而是：

$$
\boxed{
\text{separate decidable continuity dimensions from presently undecidable ones}.
}
$$

這正是本文建立 continuity vector 的原因。

---

# 五十一、Post-Substrate Transition Graph

現在可以把跨載體轉換描述為圖：

$$
G_T=(V,E).
$$

節點：

$$
V=
\{
X_0,
X_1,
\ldots
\}
$$

代表不同狀態。

邊：

$$
E
$$

則標記：

$$
\{
Rebody,
Replace,
Migrate,
Copy,
Reconstruct,
Destroy,
Fork
\}.
$$

每條邊附帶：

$$
CPP(T_e).
$$

因此未來身份不再只是一條：

$$
X_0=X_1=X_2.
$$

而是：

$$
\boxed{
\text{a provenance-rich transformation graph}.
}
$$

---

# 五十二、這也會直接改變法律

今天死亡與繼承大致假設：

$$
Person
\rightarrow
Death
\rightarrow
EstateTransfer.
$$

但如果存在：

$$
X
\rightarrow
Y
$$

且：

$$
C_\psi\approx1,
$$

$$
C_l=?
$$

法律必須回答：

> $Y$ 是本人？

> 後繼者？

> 新法人格？

更麻煩：

$$
X
\rightarrow
\{Y_1,Y_2\}.
$$

兩者都要求：

$$
LegalIdentity(X).
$$

這已經不能用現代「一個自然人一個法律身份」簡單處理。

---

# 五十三、同樣會改變死亡概念

Post-Substrate civilization 可能需要區分：

$$
\boxed{
\text{Biological Death}
}
$$

$$
\boxed{
\text{Operational Termination}
}
$$

$$
\boxed{
\text{Lineage Extinction}
}
$$

$$
\boxed{
\text{Phenomenal Termination?}
}
$$

這四者不再完全相同。

例如原身體死亡：

$$
BiologicalDeath=1
$$

但存在數位後繼譜系：

$$
LineageExtinction=0.
$$

是否：

$$
PhenomenalTermination=1
$$

仍是另一個問題。

---

# 五十四、Post-Substrate Survival 也應向量化

因此：

$$
Survival(X)
$$

不應只有：

$$
0/1.
$$

可以定義：

$$
\boxed{
\mathbf V_X
=
(
V_{\mathrm{bio}},
V_{\mathrm{causal}},
V_{\mathrm{psych}},
V_{\mathrm{social}},
V_{\mathrm{legal}},
V_{\mathrm{phen}}
).
}
$$

這可以允許：

> 生物死亡，但心理與法律後繼存在。

或者：

> 生物與心理皆延續，但代理權被外部完全控制。

這比：

> 活／死

更符合後載體狀態。

---

# 五十五、真正的「Move」也許應該保留為待證概念

本文最後建議：

在研究語言中，最好把：

$$
\boxed{
SubjectMove
}
$$

視為一個需要證明的強術語。

而不是預設操作名稱。

工程層可以使用：

$$
\boxed{
StateMigration}
$$

$$
\boxed{
ProcessMigration}
$$

$$
\boxed{
Reconstruction}
$$

$$
\boxed{
Rebody}
$$

$$
\boxed{
Copy}
$$

直到有額外理由支持：

$$
\Phi_X
\rightsquigarrow
\Phi_Y.
$$

---

# 五十六、後載體變換非等價原則

本文正式提出：

# Post-Substrate Transformation Non-Equivalence Principle

對兩個變換：

$$
T_i,T_j
$$

即使：

$$
Output(T_i)
\approx
Output(T_j),
$$

若：

$$
Path(T_i)
\neq
Path(T_j),
$$

或：

$$
CPP(T_i)
\neq
CPP(T_j),
$$

則不能在沒有額外理論的情況下宣稱：

$$
\boxed{
T_i
\equiv_{\mathrm{subject}}
T_j.
}
$$

---

# 五十七、特別地

$$
\boxed{
Rebody
\neq
GradualReplacement
}
$$

$$
\boxed{
GradualReplacement
\neq
ProcessMigration
}
$$

$$
\boxed{
ProcessMigration
\neq
StateReconstruction
}
$$

$$
\boxed{
StateReconstruction
\neq
DestructiveUpload
}
$$

$$
\boxed{
DestructiveUpload
\neq
NonDestructiveCopy.
}
$$

這些不是語言細節。

而是不同因果歷史。

---

# 五十八、與圖靈測試的關係

原始圖靈測試關心：

$$
Behavior(X)
\approx
Behavior(H)?
$$

Post-Turing Protocol 關心：

$$
Origin(X)?
$$

而 Post-Substrate Continuity 進一步問：

$$
\boxed{
How did X become this X?
}
$$

因此真正未來的身份驗證可能不能只給：

> Human-origin.

還需要：

$$
\boxed{
TransformationHistory(X).
}
$$

例如：

> Human-born → neural augmentation → gradual hybridization → distributed substrate → fork B.

這才是後載體 provenance。

---

# 五十九、結論：移動不是複製的同義詞，重建不是延續的證明

本文從 Paper 03 的：

$$
O,S,I,\Phi,A
$$

五重狀態空間出發，

建立跨載體轉換：

$$
T:
\Omega_{\mathrm{PS}}
\rightarrow
\Omega_{\mathrm{PS}}.
$$

並證明至少在概念上：

$$
\boxed{
\text{Rebody},
\text{Gradual Replacement},
\text{Migration},
\text{Reconstruction},
\text{Destructive Upload},
\text{Copy}
}
$$

不能被當成同一種操作。

本文進一步建立：

$$
\boxed{
\mathbf C
=
(
C_c,
C_p,
C_f,
C_m,
C_\psi,
C_s,
C_l,
C_\phi
)
}
$$

以防止把：

$$
\text{functional success}
$$

偷換為：

$$
\text{phenomenal survival}.
$$

最重要的是：

$$
\boxed{
C_f=1
}
$$

不推出：

$$
C_\phi=1,
$$

$$
\boxed{
C_m=1
}
$$

不推出：

$$
C_\phi=1,
$$

$$
\boxed{
C_\psi=1
}
$$

仍然不推出：

$$
C_\phi=1.
$$

因此：

> 一份完美重建的心智可能是原主體的延續，也可能是一個具有完整原主體心理歷史的新後繼者；如果兩個假說產生相同第三人稱可觀測結果，我們目前便沒有資格假裝已經知道答案。

同時：

> gradual replacement 之所以值得優先研究，不是因為它已被證明可以讓「靈魂一路跟過去」，而是因為它最大程度保留了可觀察因果橋樑、中間狀態、可逆性與比較資訊。

本文因此提出：

$$
\boxed{
\text{Do not call reconstruction migration until the relevant continuity has been specified.}
}
$$

中文而言：

> **不要因為資料到了另一個載體，就直接宣稱「我」也到了另一個載體。**

更一般地：

$$
\boxed{
\text{Data Transfer}
\neq
\text{State Reconstruction}
\neq
\text{Identity Succession}
\neq
\text{Phenomenal Transfer}.
}
$$

這就是後載體本體論對「意識上傳」最基本的語言防火牆。

---

# 與既有研究的關係

《第一人稱現象連續性》已建立 FPC 與 Successful-Copy Indistinguishability Problem，本文將其正式納入跨載體 transformation framework。

《從忒修斯之船到人工主體》已建立 Copy、Fork、Operational Fission 與 Phenomenal Fission 的非等價關係，本文進一步指出 non-destructive uploading 實際上會自然進入 Fork 問題。

GPC-CS《跨載體轉導與重建錯配》已建立跨載體保真不是單一純量；本文將同一原則由 semantic／functional fidelity 推廣到 identity／subject continuity。

在外部文獻中，mind-uploading 身份理論同樣長期區分 psychological continuity、biological continuity、physical／causal continuity 與 branching identity，且對 gradual replacement 是否真的比 destructive scan-and-copy 更有形上優勢仍無共識。

---

# 後續論文

Paper 04 解決的是：

$$
\boxed{
\text{one lineage}
\rightarrow
\text{another substrate?}
}
$$

但下一個問題更加困難。

如果不是：

$$
X\rightarrow Y,
$$

而是：

$$
X
\rightarrow
\{Y_1,Y_2,\ldots,Y_n\}
$$

呢？

或者反過來：

$$
\{X_1,X_2\}
\rightarrow
Y?
$$

因此下一篇：

## Paper 05

# Copy、Fork、Merge 與多重後繼者：從數值同一轉向譜系身份

## Copy, Fork, Merge, and Multiple Successors: From Numerical Identity to Lineage Identity

將正式建立：

$$
\boxed{
\text{Branching Lineage}
}
$$

$$
\boxed{
\text{Successor Multiplicity}
}
$$

$$
\boxed{
\text{Merge Ancestry}
}
$$

$$
\boxed{
\text{Shared Past / Divergent Future}
}
$$

並處理整個後載體文明最麻煩的問題之一：

> 如果兩個存在都真的承接了「我的全部過去」，為什麼一定只能有一個是我的後繼者？

以及反方向：

> 如果兩個原本不同的主體把記憶、價值、自我模型與認知系統真正整合成一個，那個新的存在究竟繼承了誰？