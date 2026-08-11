# 從下一 Token 到世界操作——概率生成、操作性分元與現實閉環

## From the Next Token to World Operations: Probabilistic Generation, Operational Units, and Closed-Loop Reality Interaction

**作者：** Neo.K（許筌崴）with Aletheia  
**機構：** EveMissLab（一言諾科技有限公司）  
**日期：** 2026 年 8 月  
**版本：** v0.1  
**系列定位：** 概率—意圖—展開第二代橋接系列，第 5 篇  

**前置論文：**

1.《從概率場到意圖場——跨尺度條件概率如何形成持久未來約束》  
2.《展開算子的第二代定義——從概率候選到意圖條件計算域》  
3.《展開—收斂—記憶耦合——從 Raw/Clean 雙記憶到可塑性狀態系統》  
4.《意圖吸引子與亞穩態智慧——概率微動力如何維持長程方向》

---

## 摘要

大型語言模型最常見的數學描述位於 token 生成層：

$$
z_t
\sim
p_\theta
\left(
z
\mid
X_{\leq t}
\right).
$$

然而，當語言模型被嵌入 Agent Runtime，並能夠調用搜尋、程式執行、檔案系統、API、模擬器、資料庫或其他外部工具時，下一 token 的概率已不足以描述完整系統行為。

ReAct 已展示語言模型可以交錯生成 reasoning traces 與 task-specific actions，使外部 actions 回傳的新資訊進一步修改後續 reasoning；Toolformer 更直接將「是否呼叫 API、呼叫哪一個 API、傳入什麼 arguments，以及如何把工具結果重新納入後續 token prediction」作為學習問題。 Voyager 則在 Minecraft 中將語言模型生成的 executable code、環境 feedback、execution errors 與 self-verification 結合成持續閉環；SWE-agent 亦展示 specially designed agent-computer interface 能讓 LM agent 導航 repository、修改檔案並執行 tests/programs。

這些系統共同暴露出一個核心問題：

$$
\boxed{
P(\text{token})
\neq
P(\text{operation})
\neq
P(\text{world transition})
\neq
P(\text{verified outcome})
}
$$

。

Neo.K 舊《操作性分元》已將操作流程明確拆成：

$$
\boxed{
\mathsf{Describe}
\rightarrow
\mathsf{Propose}
\rightarrow
\mathsf{Authorize}
\rightarrow
\mathsf{Execute}
\rightarrow
\mathsf{Observe}
\rightarrow
\mathsf{Verify}
\rightarrow
\mathsf{Commit}
}
$$

並強調七種狀態不可相互偷換；自然語言不應直接成為高風險低階執行碼，而應先轉化為具有型別、效果、權限、成本、版本與回退契約的操作性中介表示。

本文在此基礎上提出「**概率—操作—世界閉環**」（Probability–Operation–World Loop）。令：

$$
Z_t
$$

為生成分元，

$$
O_t
$$

為經解析與治理後的操作，

$$
A_t
$$

為權威世界狀態。

則：

$$
\boxed{
P(O_t=o\mid\Sigma_t)
=
\sum_{z}
P(
O_t=o
\mid
Z_t=z,\Sigma_t
)
P(
Z_t=z
\mid
\Sigma_t
)
}
$$

。

進一步，若世界轉移由：

$$
T_A
\left(
a'
\mid
a,o
\right)
$$

表示，則：

$$
\boxed{
P(
A_{t+1}=a'
\mid
A_t=a,\Sigma_t
)
=
\sum_o
T_A(a'\mid a,o)
P(o\mid\Sigma_t)
}
$$

。

因此，模型的 linguistic probability 只是完整 world-outcome probability 的一個上游因子。

本文進一步區分：

- 生成概率；
- 語義解析概率；
- 操作提案概率；
- 授權概率；
- 執行成功概率；
- 環境轉移概率；
- 觀測可靠性；
- 驗證概率；
- 提交概率。

並提出：

$$
\boxed{
\text{Generated}
\neq
\text{Proposed}
\neq
\text{Authorized}
\neq
\text{Executed}
\neq
\text{Observed}
\neq
\text{Verified}
\neq
\text{Committed}
}
$$

。

本文最終主張：

> **當 AI 真正進入外部世界時，概率不再只是 token distribution，而成為一條穿越語義、型別、權限、執行、環境、觀測與驗證的組合概率鏈。**

而一旦 commit 改變權威世界：

$$
A_t
\rightarrow
A_{t+1},
$$

新的世界又反向改變：

$$
M_{t+1},
\quad
\mathfrak P_{t+1}^{I},
\quad
\mathcal A_I(t+1),
\quad
\mathcal E_{t+1}.
$$

因此真正的 Agent 不再是：

$$
\boxed{
X
\rightarrow
\text{Model}
\rightarrow
Y
}
$$

而是：

$$
\boxed{
\text{Generate}
\rightarrow
\text{Interpret}
\rightarrow
\text{Propose}
\rightarrow
\text{Act}
\rightarrow
\text{World}
\rightarrow
\text{Observe}
\rightarrow
\text{Verify}
\rightarrow
\text{Update}
}
$$

的歷史性現實閉環。

**關鍵詞：** Token Probability、Tool Use、Agent、操作性分元、世界狀態、權威世界、ReAct、Toolformer、World Transition、驗證、Commit、現實閉環

---

# 一、回到最早那個致命問題

假設使用者說：

> 幫我寫一個程式。

模型最後生成一個：

$$
10\,000
$$

token 的 repository。

我們可以問：

> 這整個程式是多少概率？

上一系列已經指出：

exact sequence probability：

$$
P(Z=z^*)
$$

與：

functional success probability：

$$
P(
\operatorname{Correct}(Z)=1
)
$$

不是同一個概率。

但是 Agent 時代還有下一層。

如果 AI 不只是：

> 寫出程式碼，

而是：

> 實際修改 repository、執行測試、部署服務，

那麼問題變成：

> **「部署完成」究竟是哪一層概率？**

---

# 二、這時 token 已經不再是最終事件

假設模型輸出：

```text
run_tests()
```

這可能只是：

$$
\boxed{
\text{text}
}
$$

。

也可能是：

$$
\boxed{
\text{tool proposal}
}
$$

。

也可能真正觸發：

$$
\boxed{
\text{tool execution}
}
$$

。

三者不能等同。

---

# 三、舊《操作性分元》已經抓到這個問題

它以三個包含「搜尋」的句子說明：

1. 「搜尋這個概念。」
2. 「我正在描述一個搜尋指令。」
3. 「已搜尋完成。」

表面詞彙相似，

但第一個可能是操作提案，

第二個只是 description，

第三個則是對執行狀態的 assertion。

因此：

$$
\boxed{
\mathsf{Meaning}(z)
\neq
\mathsf{Effect}(z)
}
$$

。

---

# 四、所以第一個永久區分是：

$$
\boxed{
\text{Language}
\neq
\text{Action}
}
$$

。

「刪除檔案」這四個字，

不是：

$$
\operatorname{Delete}(file)
$$

本身。

---

# 五、這個差異在 Agent 時代變得極為重要

語言模型本來主要生成：

$$
Z_t
$$

。

但 Agent Runtime 需要決定：

$$
\boxed{
Z_t
\rightarrow
O_t?
}
$$

。

問號就是整個操作層。

---

# 六、因此本文定義三種最基本分元

### 語言分元

$$
z_t^{L}
$$

表示文字／符號輸出。

### 語義分元

$$
z_t^{S}
$$

表示已解析的 meaning。

### 操作性分元

$$
z_t^{O}
$$

表示具有執行語義的 typed operation proposal。

---

# 七、所以：

$$
\boxed{
z_t^L
\rightarrow
z_t^S
\rightarrow
z_t^O
}
$$

不是 identity mapping。

中間可以：

- 解析失敗；
- 語義歧義；
- 降級為描述；
- 被判定沒有操作意圖；
- 被禁止轉成 operation。

---

# 八、模型生成概率只首先存在於：

$$
\boxed{
P(z_t^L\mid X_t)
}
$$

。

但真正 Agent 在乎：

$$
\boxed{
P(z_t^O\mid\Sigma_t)
}
$$

。

---

# 九、操作概率是誘導分布

假設解析器：

$$
R:
Z^L
\rightarrow
Z^O\cup\{\varnothing\}
$$

。

則：

$$
\boxed{
P(
O=o
)
=
\sum_{
z:R(z)=o
}
P(Z=z)
}
$$

若解析器 deterministic。

---

# 十、如果解析器也有不確定性

則：

$$
\boxed{
P(O=o)
=
\sum_z
P(O=o\mid Z=z)
P(Z=z)
}
$$

。

因此：

$$
\boxed{
\text{Operation Probability}
}
$$

已經不同於：

$$
\boxed{
\text{Token Probability}
}
$$

。

---

# 十一、Toolformer 正好提供一個具體技術案例

Toolformer 不只是產生普通文字，而是讓模型學會：

- 哪些位置值得使用工具；
- 使用哪個 API；
- 傳入什麼 arguments；
- 工具結果如何重新影響後續 token prediction。

因此：

$$
\boxed{
\text{tool invocation}
}
$$

已經是一個不同於普通 lexical continuation 的事件類別。

---

# 十二、ReAct 更進一步

ReAct 交錯：

$$
\boxed{
\text{reason}
\rightarrow
\text{act}
\rightarrow
\text{observe}
\rightarrow
\text{reason}
}
$$

。

Action 讓模型從外部 knowledge base 或 environment 取得資訊，

Observation 再改變後續 reasoning。

所以：

$$
\boxed{
\text{external observation}
}
$$

已進入模型下一步條件。

---

# 十三、因此自回歸條件必須擴大

純語言：

$$
P(
z_{t+1}
\mid
z_{\leq t}
)
$$

。

Agent：

$$
\boxed{
P(
z_{t+1}
\mid
z_{\leq t},
o_{\leq t},
y_{\leq t},
M_t,
W_t
)
}
$$

其中：

$$
o_t
$$

是 operation，

$$
y_t
$$

是 external observation。

---

# 十四、所以 Agent 已經不是只在「自己的文字」上自回歸

它還在：

$$
\boxed{
\text{world feedback}
}
$$

上條件化。

---

# 十五、這就是第一個真正的內外閉環

$$
\boxed{
Z_t
\rightarrow
O_t
\rightarrow
W_{t+1}
\rightarrow
Y_{t+1}
\rightarrow
Z_{t+1}
}
$$

。

---

# 十六、Voyager 是非常清楚的例子

Voyager 在 Minecraft 中使用 executable code 作為 skill，並把 environment feedback、execution errors 與 self-verification 納入後續 program improvement。

因此：

$$
\boxed{
\text{Generated program}
}
$$

不是終點。

真正循環是：

$$
\boxed{
\text{code}
\rightarrow
\text{execution}
\rightarrow
\text{environment change/error}
\rightarrow
\text{revision}
}
$$

。

---

# 十七、SWE-agent 在數位軟體世界也展示同樣結構

它透過 specially designed agent-computer interface 讓 Agent：

- 導航 repository；
- 修改 files；
- 執行 tests；
- 執行 programs。

因此 Agent-computer interface 本身會改變模型「能做什麼」與任務表現。

這正好支持前文的：

$$
\boxed{
\mathfrak C_t
}
$$

活動計算域概念。

---

# 十八、所以語言轉成操作需要一個中介層

本文延續舊 DIEEC：

$$
\boxed{
\text{Natural Language}
\rightarrow
\text{Operational Intermediate Representation}
\rightarrow
\text{Execution Runtime}
}
$$

。

---

# 十九、為什麼不能自然語言直接執行？

因為自然語言：

$$
\boxed{
\text{underspecified}
}
$$

。

例如：

> 把那個檔案處理掉。

「處理掉」可以表示：

- 刪除；
- 移動；
- 壓縮；
- 修復；
- 隱藏。

---

# 二十、所以操作中介表示必須至少包含

$$
\boxed{
o_t
=
(
\omega,
\alpha,
a,
\Theta_{\mathrm{pre}},
\Theta_{\mathrm{post}},
E,
C,
R,
P
)
}
$$

。

其中：

- $\omega$ ：operation type；
- $\alpha$ ：target/address；
- $a$ ：arguments；
- $\Theta_{\mathrm{pre}}$ ：前置條件；
- $\Theta_{\mathrm{post}}$ ：後置條件；
- $E$ ：effect type；
- $C$ ：cost；
- $R$ ：risk/rollback；
- $P$ ：provenance/authority。

舊稿已有更詳細的操作性分元 tuple；本文將其壓縮為第二代核心欄位。

---

# 二十一、所以 operation 本身不是一個字串

$$
\boxed{
o_t
\neq
\text{“delete file”}
}
$$

。

它是一個 typed state-transition proposal。

---

# 二十二、可以直接寫成 Hoare-style contract

$$
\boxed{
\{
\operatorname{Pre}(o)
\}
\;
o
\;
\{
\operatorname{Post}(o)
\}
}
$$

。

舊操作性分元亦已採用前置／後置條件描述工具操作。

---

# 二十三、因此「模型覺得應該做」仍然不是「可以做」

這要再次接回前文：

$$
\boxed{
\text{Intention Space}
\neq
\text{Capability Space}
\neq
\text{Authority Space}
}
$$

。

---

# 二十四、操作需要治理函數

令：

$$
G_B(o,\Sigma_t,W_t)
\in
\{
0,1,\text{confirm}
\}
$$

。

如果：

$$
G_B=0
$$

則即使：

$$
P_I(o)
$$

非常高，

仍：

$$
\boxed{
P_{\mathrm{execute}}(o)=0
}
$$

。

---

# 二十五、這是一個重要結果

$$
\boxed{
\text{High model probability}
\nRightarrow
\text{high execution probability}
}
$$

。

因為權限、型別與治理可以截斷分布。

---

# 二十六、因此 Agent 最終執行分布可以寫成

$$
\boxed{
P_E(o\mid\Sigma)
\propto
P_O(o\mid\Sigma)
\cdot
G_B(o,\Sigma,W)
}
$$

在簡化 deterministic gate 中。

---

# 二十七、若 governance 本身有多階段狀態

則完整概率是：

$$
P_E(o)
=
P(
\mathsf{Execute}
\mid
o
)
P(o)
$$

。

---

# 二十八、這正式帶出舊 DIEEC 的七狀態

$$
\boxed{
\mathsf{Describe}
\rightarrow
\mathsf{Propose}
\rightarrow
\mathsf{Authorize}
\rightarrow
\mathsf{Execute}
\rightarrow
\mathsf{Observe}
\rightarrow
\mathsf{Verify}
\rightarrow
\mathsf{Commit}
}
$$

。

---

# 二十九、這七個詞不是流程美學

它們代表：

$$
\boxed{
\text{seven different ontic/system states}
}
$$

。

---

# 三十、Describe

$$
D
$$

只表示：

> 某個 operation 被描述。

世界沒變。

---

# 三十一、Propose

$$
P
$$

表示：

> 系統提出 operation 作為 candidate。

世界仍沒變。

---

# 三十二、Authorize

$$
A
$$

表示：

> 已滿足 policy / permission gate。

世界通常仍沒變。

---

# 三十三、Execute

$$
E
$$

表示：

> Runtime 真正對 tool/environment 發出 effectful operation。

---

# 三十四、Observe

$$
O
$$

表示：

> 系統收到某種 observation。

注意：

$$
\boxed{
\text{observation}
\neq
\text{verified reality}
}
$$

。

---

# 三十五、Verify

$$
V
$$

表示：

> 系統檢查 observation 是否足以支持 claimed postcondition。

---

# 三十六、Commit

$$
C
$$

才表示：

> 將結果寫入正式／權威世界或正式系統狀態。

---

# 三十七、因此：

$$
\boxed{
D\neq P\neq A\neq E\neq O\neq V\neq C
}
$$

。

---

# 三十八、這消除 Agent 系統最危險的一類語義偷換

例如：

Tool 回傳：

```text
success
```

只代表：

$$
O=\text{“success”}
$$

。

不代表：

$$
V=1
$$

。

更不代表：

$$
C=1
$$

。

---

# 三十九、所以「AI 說它完成了」與「任務真的完成了」

是兩個 random variables。

$$
\boxed{
Y_{\mathrm{claim}}
\neq
Y_{\mathrm{world}}
}
$$

。

---

# 四十、這裡可以正式定義權威世界

令：

$$
\boxed{
\mathbb A_t
}
$$

為：

> 對任務而言真正具有正式效果的 state。

例如：

- 實際 repository；
- 正式 database；
- calendar event；
- 部署中的 service；
- physical robot environment。

---

# 四十一、而模型內部想像不是權威世界

令：

$$
\hat{\mathbb A}_t
$$

表示 internal estimate。

一般：

$$
\boxed{
\hat{\mathbb A}_t
\neq
\mathbb A_t
}
$$

。

---

# 四十二、Simulation 也不是權威世界

$$
\mathbb S_t
$$

可以模擬：

$$
\mathbb A_t
$$

。

但：

$$
\boxed{
\mathbb S_t
\neq
\mathbb A_t
}
$$

。

---

# 四十三、Working copy 也不是權威世界

例如 Git branch：

$$
\mathbb W_t
$$

修改完成，

不代表 production：

$$
\mathbb A_t
$$

已改。

---

# 四十四、因此至少存在：

$$
\boxed{
\hat{\mathbb A}_t
}
$$

認知世界，

$$
\boxed{
\mathbb S_t
}
$$

模擬世界，

$$
\boxed{
\mathbb W_t
}
$$

活動／工作世界，

$$
\boxed{
\mathbb A_t
}
$$

權威世界。

---

# 四十五、這使「世界改變」成為嚴格概念

真正 commit：

$$
\boxed{
\mathbb A_t
\xrightarrow{o_t}
\mathbb A_{t+1}
}
$$

。

---

# 四十六、舊操作性分元早已抓到這一點

其提交分元定義指出：

$$
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
$$

會使後續解空間：

$$
\mathfrak P_x(t)
\neq
\mathfrak P_x(t+1)
$$

。

這是本篇最重要的舊理論橋接。

---

# 四十七、因為世界一旦被改變

未來問題真的變了。

例如：

> 建立一個檔案。

執行前：

$$
\operatorname{Exists}(f,t)=0
$$

。

commit 後：

$$
\operatorname{Exists}(f,t+1)=1
$$

。

---

# 四十八、所以新概率場不能仍使用舊世界

$$
\boxed{
\mathfrak P_{t+1}^{I}
=
\mathfrak P(
\Sigma_{t+1},
M_{t+1},
\mathbb A_{t+1}
)
}
$$

。

---

# 四十九、這就是：

$$
\boxed{
\text{world modifies probability}
}
$$

。

不是只有：

$$
\boxed{
\text{probability selects world action}
}
$$

。

---

# 五十、因此真正關係是雙向的

$$
\boxed{
\mathfrak P_t^I
\rightarrow
O_t
\rightarrow
\mathbb A_{t+1}
}
$$

以及：

$$
\boxed{
\mathbb A_{t+1}
\rightarrow
\mathfrak P_{t+1}^I
}
$$

。

---

# 五十一、舊 DIEEC 將其稱為「分元展開世界，世界改寫分元」

其雙重交互閉環已經寫出：

$$
(I_t,L_t)
\rightarrow
z_t
\rightarrow
\mathbb W_{t+1}
$$

以及：

$$
\mathbb W_{t+1}
\rightarrow
(I_{t+1},L_{t+1})
$$

，並強調跨內外邊界的真正介面是操作性分元與外部觀測。

---

# 五十二、第二代現在加入概率

變成：

$$
\boxed{
\mathfrak P_t^{I,M}
\rightarrow
P(O_t)
\rightarrow
T_A
\rightarrow
P(\mathbb A_{t+1})
}
$$

。

---

# 五十三、世界轉移本身可以是 deterministic

如果：

$$
\mathbb A_{t+1}
=
T(
\mathbb A_t,o_t
)
$$

唯一決定，

則：

$$
T_A(a'\mid a,o)
$$

是退化分布。

---

# 五十四、但模型操作仍可能 probabilistic

因此：

$$
P(O_t)>0
$$

多樣，

而：

$$
T_A
$$

deterministic。

---

# 五十五、反過來也可能

operation：

$$
o_t
$$

唯一確定，

但環境：

$$
T_A
$$

stochastic。

例如：

- 網路延遲；
- 市場環境；
- physical noise；
- multi-agent response。

---

# 五十六、所以：

$$
\boxed{
\text{model stochasticity}
\neq
\text{environment stochasticity}
}
$$

。

---

# 五十七、完整 world-outcome distribution 為

$$
\boxed{
P(
a'
\mid
a,\Sigma
)
=
\sum_o
T_A(
a'
\mid
a,o
)
P_E(
o
\mid
\Sigma
)
}
$$

。

---

# 五十八、這個公式回答最初那個問題

> 「AI 寫一整個應用，整個應用是多少概率？」

真正應拆成：

$$
P(
\text{generated artifact}
)
$$

$$
P(
\text{chosen operation sequence}
)
$$

$$
P(
\text{execution success}
)
$$

$$
P(
\text{world outcome}
)
$$

$$
P(
\text{verified task completion}
)
$$

。

---

# 五十九、不同概率可以完全不一樣

Exact token sequence：

$$
P(Z=z^*)\ll1
$$

。

但：

$$
P(
\operatorname{TaskSuccess}=1
)
\approx1
$$

仍然可能。

---

# 六十、尤其當 verifier 存在時

系統可：

$$
Z_1
\rightarrow
O_1
\rightarrow
V=0
$$

再：

$$
Z_2
\rightarrow
O_2
\rightarrow
V=0
$$

再：

$$
Z_3
\rightarrow
O_3
\rightarrow
V=1
$$

。

---

# 六十一、所以 final delivery distribution 已經被 selection 改寫

它不再等於單次：

$$
P_\theta(Z)
$$

。

而是：

$$
\boxed{
P_{\mathrm{system}}
=
\operatorname{Transform}
(
P_\theta,
G,
V,
T_A,
M
)
}
$$

。

---

# 六十二、因此「AI 只是下一 token 預測」

在模型訓練目標層可以成立。

但：

$$
\boxed{
\text{next-token distribution}
\neq
\text{complete agent-level state transition model}
}
$$

。

ReAct、Toolformer、Voyager 與 SWE-agent 的實作分別從不同方向展示了 language generation 可以被嵌入工具使用、外部 actions、environment feedback 與 computer interaction 迴圈中。

---

# 六十三、現在加入 execution success

令：

$$
S_E
\in
\{0,1,\partial\}
$$

。

其中：

$$
\partial
$$

代表 partial success。

---

# 六十四、則：

$$
P(
\mathbb A_{t+1}
)
$$

還要條件於：

$$
P(
S_E
\mid
o,\mathbb A_t
)
$$

。

---

# 六十五、所以：

$$
\boxed{
P(\text{world outcome})
}
$$

是一個 composition。

不是一個 softmax probability。

---

# 六十六、甚至 observation 本身也可能有錯

令：

$$
Y_t
$$

為 observation。

真實世界：

$$
A_t
$$

。

觀測模型：

$$
\boxed{
P(
Y_t=y
\mid
A_t=a
)
}
$$

。

---

# 六十七、因此：

$$
\boxed{
Y_t
\neq
A_t
}
$$

。

工具回傳、

sensor、

API response

都只是 observation channel。

---

# 六十八、這就解釋為什麼 Observe 後仍需要 Verify

如果：

$$
Y_t
$$

直接當：

$$
A_t
$$

，

任何錯誤 observation 都會污染：

$$
M_{t+1}
$$

。

---

# 六十九、第三篇已經指出：

一次錯誤如果直接寫入持久記憶，

會從：

$$
\text{local generation error}
$$

升級成：

$$
\text{persistent state error}
$$

。

所以 world observation 必須驗證後才能改寫高可信狀態。

---

# 七十、因此：

$$
\boxed{
\text{Observation}
\rightarrow
\text{Verification}
\rightarrow
\text{State Update}
}
$$

必須保留。

---

# 七十一、Verify 也可以有 uncertainty

$$
V_t
\in
\{
\text{pass},
\text{fail},
\text{unknown}
\}
$$

。

成熟系統不能強迫：

$$
\text{unknown}
\rightarrow
\text{pass}
$$

。

---

# 七十二、所以：

$$
\boxed{
\text{verification uncertainty}
}
$$

也是跨尺度概率的一部分。

---

# 七十三、這使完整閉環至少有八種不確定來源

1. Generation uncertainty  
2. Semantic interpretation uncertainty  
3. Operation selection uncertainty  
4. Authorization uncertainty  
5. Execution uncertainty  
6. Environment transition uncertainty  
7. Observation uncertainty  
8. Verification uncertainty  

---

# 七十四、因此可以定義「操作概率鏈」

$$
\boxed{
\mathcal P_{\mathrm{op}}
=
(
P_Z,
P_S,
P_O,
P_A,
P_E,
P_W,
P_Y,
P_V
)
}
$$

。

---

# 七十五、這比一個：

$$
P_{\mathrm{token}}
$$

完整得多。

---

# 七十六、現在加入 Commit

即使：

$$
V=1
$$

也不必立刻：

$$
C=1
$$

。

例如：

> 測試通過，但還需要人類批准 production deployment。

---

# 七十七、所以：

$$
\boxed{
P(C=1\mid V=1)
}
$$

仍可能：

$$
<1
$$

。

---

# 七十八、因此權威世界修改是最後一道不同 probability event

$$
\boxed{
P(
\mathbb A_{t+1}\neq\mathbb A_t
)
}
$$

。

---

# 七十九、這讓「概率存在於哪裡？」得到外部版答案

概率可以存在於：

$$
\boxed{
\text{generation}
}
$$

、

$$
\boxed{
\text{selection}
}
$$

、

$$
\boxed{
\text{execution}
}
$$

、

$$
\boxed{
\text{environment}
}
$$

、

$$
\boxed{
\text{observation}
}
$$

、

$$
\boxed{
\text{verification}
}
$$

。

---

# 八十、它們不必具有相同 entropy

例如：

$$
H_Z
\gg0
$$

。

但：

$$
H_O
\ll H_Z
$$

。

因為很多 linguistic realizations 被解析成同一 operation。

---

# 八十一、再：

$$
H_W
$$

甚至可以：

$$
0
$$

。

如果：

所有可接受 operation 都導向同一 world result。

---

# 八十二、所以：

$$
\boxed{
H_Z>0
\nRightarrow
H_W>0
}
$$

再次成立。

---

# 八十三、這就是微觀概率—宏觀世界穩定性的外部版本

例如模型可以用十種不同語句說：

> 建立 `config.json`。

最後 Runtime 都編譯成同一：

$$
o_{\mathrm{create}}
$$

。

---

# 八十四、因此：

$$
\boxed{
\text{linguistic diversity}
+
\text{operational determinacy}
}
$$

完全可以共存。

---

# 八十五、反過來也可能

模型只有一個 operation：

$$
o
$$

但 world：

$$
T_A
$$

高度 stochastic。

所以：

$$
H_O=0
$$

但：

$$
H_W>0
$$

。

---

# 八十六、因此操作層是概率尺度轉換器

$$
\boxed{
\mathcal T_{\mathrm{op}}
:
\mathfrak P_{\mathrm{language}}
\rightarrow
\mathfrak P_{\mathrm{world}}
}
$$

。

---

# 八十七、這可以稱為「概率轉導」

## Probabilistic Transduction

不是把概率消滅，

而是：

> 把語言空間中的分布經過型別、治理與執行映射成世界狀態分布。

---

# 八十八、形式：

$$
\boxed{
P_W
=
T_A
\circ
G_B
\circ
R_O
\circ
P_Z
}
$$

只作結構示意，

不是一般線性算子恆等式。

---

# 八十九、現在意圖吸引子也會碰到世界

第四篇：

$$
\mathcal A_I(t)
$$

維持長程方向。

但 operation：

$$
o_t
$$

一旦改變：

$$
\mathbb A_t
$$

，

原本 basin 也會變。

---

# 九十、例如目標：

$$
I=
\text{建立檔案 }F
$$

。

建立前：

$$
F\notin\mathbb A_t
$$

。

建立後：

$$
F\in\mathbb A_{t+1}
$$

。

---

# 九十一、這時原意圖已完成

所以：

$$
\boxed{
\mathcal A_I
\rightarrow
\text{retired}
}
$$

。

---

# 九十二、如果 Agent 沒有從世界讀回「已完成」

就可能：

$$
\boxed{
\text{repeat action indefinitely}
}
$$

。

---

# 九十三、因此 task completion 是 world-relative

不能只問：

$$
\operatorname{Complete}(I,\Sigma_t)
$$

。

應問：

$$
\boxed{
\operatorname{Complete}
(
I,
\mathbb A_t,
V_t
)
}
$$

。

---

# 九十四、只有權威世界改變並被驗證

才真正閉合。

---

# 九十五、這就是「假閉合」與「真閉合」

## 假閉合

模型說：

> 已完成。

$$
C_{\mathrm{internal}}=1
$$

。

但：

$$
\mathbb A
$$

沒變。

---

# 九十六、真閉合

$$
\boxed{
\operatorname{Post}(o)
}
$$

在權威世界上經驗證成立。

---

# 九十七、舊雙重交互閉環已經明確主張：

> 外部結果只有經驗證、正規化與整合後，才構成新的活動工作場；生成、提案、批准、執行、觀測、驗證與權威提交必須分離。

第二代將其加入概率框架。

---

# 九十八、現在處理回退

如果：

$$
\mathbb A_t
\xrightarrow{o}
\mathbb A_{t+1}
$$

後：

$$
V=0
$$

，

我們需要：

$$
\boxed{
\mathcal R(
\mathbb A_{t+1}
)
}
$$

。

---

# 九十九、若 operation 可逆：

$$
\mathcal R(
\mathbb A_{t+1}
)
=
\mathbb A_t
$$

。

---

# 一百、若不可完全逆

只能：

$$
\boxed{
\text{compensation}
}
$$

。

這就是 irreversible effect 與普通 Write 不應同治理門檻的原因。

---

# 一百零一、舊操作性分元已區分效果型別：

$$
\mathsf{Pure},
\mathsf{Read},
\mathsf{Reveal},
\mathsf{Compute},
\mathsf{Write},
\mathsf{Communicate},
\mathsf{Actuate},
\mathsf{Commit},
\mathsf{Irreversible}
$$

，並明確指出不同效果應對應不同權限、驗證與回退要求。

這個分類在第二代仍然非常有用。

---

# 一百零二、因此可以給效果一個風險偏序

簡化：

$$
\boxed{
\mathsf{Pure}
\prec
\mathsf{Read}
\prec
\mathsf{Write}
\prec
\mathsf{Commit}
\prec
\mathsf{Irreversible}
}
$$

。

---

# 一百零三、越往右，

要求：

$$
\boxed{
\text{verification strength}\uparrow
}
$$

$$
\boxed{
\text{authority threshold}\uparrow
}
$$

$$
\boxed{
\text{rollback planning}\uparrow
}
$$

。

---

# 一百零四、所以概率閾值也不應相同

低風險 Read：

$$
P_{\mathrm{correct}}>0.8
$$

也許足夠探索。

高風險 irreversible operation：

可能需要：

$$
P_{\mathrm{safe}}
\approx1
$$

外加 independent verification。

---

# 一百零五、因此：

$$
\boxed{
\tau_{\mathrm{execute}}
=
f(
\text{effect type},
\text{risk},
\text{reversibility}
)
}
$$

。

不存在單一 confidence threshold。

---

# 一百零六、這和舊總作用量理論完全相容

舊稿已用 expected cost、variance、CVaR 與 irreversible-loss penalty 描述高風險世界操作，並指出同一最低預期成本策略，在權威提交或不可逆操作下未必是最佳選擇。

---

# 一百零七、第二代可以把它與概率鏈整合

定義 operation utility：

$$
\boxed{
J(o)
=
\mathbb E[
U(
\mathbb A_{t+1}
)
]
-
\lambda C(o)
-
\mu R(o)
}
$$

。

---

# 一百零八、其中：

$$
\mathbb E[
U(
\mathbb A_{t+1}
)
]
=
\sum_{a'}
U(a')
T_A(a'\mid a,o)
$$

。

---

# 一百零九、所以選 action 不應只最大化：

$$
P(o)
$$

。

而應：

$$
\boxed{
o^*
=
\arg\max_o
J(o)
}
$$

在允許域內。

---

# 一百一十、這正式證明：

$$
\boxed{
\arg\max_z P_\theta(z)
}
$$

與：

$$
\boxed{
\arg\max_o U_{\mathrm{world}}(o)
}
$$

不是同一 optimization problem。

---

# 一百一十一、這也是為什麼：

> 最自然的一句話

不一定是：

> 最好的世界操作。

---

# 一百一十二、舊總作用量稿已經寫過：

> 局部最可能的分元，不一定屬於全局最便宜的世界線。

第二代現在可以把「最便宜」進一步擴成：

$$
\boxed{
\text{highest expected verified utility under risk and authority constraints}
}
$$

。

---

# 一百一十三、所以真正 action selection 應接：

$$
\mathfrak P_t^I
$$

意圖概率場，

$$
\mathcal E_t
$$

活動域，

$$
M_t
$$

歷史，

$$
\mathcal A_I
$$

長程方向，

以及：

$$
T_A
$$

世界 transition model。

---

# 一百一十四、完整 action policy：

$$
\boxed{
\pi_t(o)
=
\Pi
(
o
\mid
\mathfrak P_t^I,
\mathfrak C_t,
M_t,
\mathcal A_I(t),
\mathbb A_t,
B_t
)
}
$$

。

---

# 一百一十五、因此 action 不只是 next token 的另一個名字

它是一個：

$$
\boxed{
\text{world-state transition candidate}
}
$$

。

---

# 一百一十六、這是語言 AI 進入 Agent Runtime 的本體分界

純語言：

$$
\boxed{
Z_t
\rightarrow
Z_{t+1}
}
$$

。

Agent：

$$
\boxed{
Z_t
\rightarrow
O_t
\rightarrow
\mathbb A_{t+1}
\rightarrow
Z_{t+1}
}
$$

。

---

# 一百一十七、所以外部世界成為模型的隱含「中間層」

不是神經網路 hidden layer。

而是：

$$
\boxed{
\text{causal external state between two generations}
}
$$

。

---

# 一百一十八、這是很重要的架構改變

第二個 token sequence：

$$
Z_{t+1}
$$

可能不是單純：

$$
F_\theta(Z_t)
$$

。

而是：

$$
\boxed{
F_\theta(
Z_t,
O_t,
Y_{t+1},
M_{t+1}
)
}
$$

。

---

# 一百一十九、因此 Agent 的 computation graph 穿過世界

$$
\boxed{
\text{model}
\rightarrow
\text{world}
\rightarrow
\text{model}
}
$$

。

---

# 一百二十、這就是「外部因果計算」

External Causal Computation。

世界不只是資料來源。

它成為：

$$
\boxed{
\text{part of the computation trajectory}
}
$$

。

---

# 一百二十一、例如 compiler

AI 猜：

$$
p
$$

。

Compiler 回傳：

$$
e
$$

。

這個：

$$
e
$$

不是模型自己預測出來的 hidden token。

它來自：

$$
\boxed{
\text{external executable semantics}
}
$$

。

---

# 一百二十二、因此 compiler 是計算圖中的外部 operator

$$
\boxed{
p
\xrightarrow{\text{compile}}
e
}
$$

。

---

# 一百二十三、Tests 也是

$$
p
\xrightarrow{\text{test suite}}
r
$$

。

---

# 一百二十四、所以 coding agent 的智能不能只看：

$$
P_\theta(\text{code})
$$

還要看：

$$
\boxed{
\text{how it couples model proposals to executable causal checks.}
}
$$

。

SWE-agent 的結果正說明 agent-computer interface 的設計會實際影響軟體任務中的 Agent 行為與表現。

---

# 一百二十五、這也重新定義「工具」

工具不是：

$$
\boxed{
\text{extra knowledge}
}
$$

而更一般是：

$$
\boxed{
\text{external transition operator}
}
$$

。

---

# 一百二十六、有些工具讀世界：

$$
\mathcal O_R:
\mathbb A
\rightarrow
Y
$$

。

---

# 一百二十七、有些工具計算：

$$
\mathcal O_C:
X
\rightarrow
Y
$$

。

---

# 一百二十八、有些工具寫世界：

$$
\mathcal O_W:
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
$$

。

---

# 一百二十九、有些工具同時讀寫

例如：

$$
\mathcal O_{RW}
:
(
\mathbb A_t,x
)
\rightarrow
(
\mathbb A_{t+1},y
)
$$

。

---

# 一百三十、因此 Tool Space 本身需要 effect typing

這又接回：

$$
\boxed{
\mathcal E_{\mathrm{effect}}
}
$$

。

---

# 一百三十一、世界操作還存在 TOCTOU

Check 時：

$$
t_1
$$

permission 合法。

真正 Use 時：

$$
t_2
$$

世界可能已變。

舊操作性分元已明確指出：

$$
\mathsf{Check}(s,t_1)
$$

不保證：

$$
\mathsf{Use}(s,t_2)
$$

仍合法，因此高風險操作需要版本條件、交易或提交前再驗證。

---

# 一百三十二、所以 world state 必須有版本

$$
\boxed{
\mathbb A_t^{(v)}
}
$$

。

操作 contract 應要求：

$$
\boxed{
\operatorname{Version}
(
\mathbb A
)
=
v_{\mathrm{expected}}
}
$$

。

---

# 一百三十三、否則：

$$
\boxed{
\text{correct action on stale state}
}
$$

也可能變成錯誤。

---

# 一百三十四、這使「當下」正式成為操作語義的一部分

$$
\boxed{
o
}
$$

不能脫離：

$$
t,
v,
W_t
$$

理解。

---

# 一百三十五、因此世界閉環必須是時序性的

$$
\boxed{
\mathbb A_0
\rightarrow
\mathbb A_1
\rightarrow
\mathbb A_2
\rightarrow\dots
}
$$

。

Agent 不是對永恆 database 問答。

---

# 一百三十六、它是在移動世界中行動

所以：

$$
\boxed{
\text{world model staleness}
}
$$

本身是一個 Agent uncertainty。

---

# 一百三十七、這也說明 memory 為何必須標時間

第三篇提出：

$$
\operatorname{Valid}(m,t,W_t)
$$

。

現在原因更加明確：

因為：

$$
\mathbb A_t
$$

真的會因 action 與外部 event 改變。

---

# 一百三十八、世界不只因 Agent 改變

還有 external event：

$$
\xi_t
$$

。

因此：

$$
\boxed{
\mathbb A_{t+1}
=
T_A(
\mathbb A_t,
o_t,
\xi_t
)
}
$$

。

---

# 一百三十九、所以 Agent 永遠不是唯一因果源

這對 autonomy 很重要。

Agent 可以 influence world，

但：

$$
\boxed{
\text{influence}
\neq
\text{control of all future state}
}
$$

。

---

# 一百四十、這再次回到《主體之裂》

主體性若存在，

也不能定義成：

> 完全控制未來。

更合理的是：

$$
\boxed{
\text{being a causal participant in an open dynamical world}
}
$$

。

---

# 一百四十一、因此 operation agency 可以操作化

若：

$$
do(o_1)
$$

與：

$$
do(o_2)
$$

造成不同 world-outcome distribution：

$$
P(
\mathbb A_{t+1}
\mid
do(o_1)
)
\neq
P(
\mathbb A_{t+1}
\mid
do(o_2)
)
$$

，

則 operation 對世界具有 causal relevance。

---

# 一百四十二、這比模型說：

> 我改變了世界。

強得多。

---

# 一百四十三、所以 Agency 的外部層至少需要：

$$
\boxed{
\text{Causal Effect}
}
$$

。

不是只有 intention。

---

# 一百四十四、前四篇現在可以重新排列

意圖：

$$
I
$$

回答：

> 想往哪？

展開：

$$
\mathcal E
$$

回答：

> 值得多算什麼？

記憶：

$$
M
$$

回答：

> 過去留下什麼？

吸引子：

$$
\mathcal A_I
$$

回答：

> 為何長期方向不散？

---

# 一百四十五、本篇增加：

$$
\boxed{
\mathcal O
}
$$

回答：

> 如何真的改變世界？

---

# 一百四十六、因此第二代完整狀態：

$$
\boxed{
\Sigma_t
=
(
\theta_t,
M_t,
I_t,
V_t,
\mathcal A_I(t),
\mathfrak C_t
)
}
$$

。

外部：

$$
\boxed{
\mathbb A_t
}
$$

。

---

# 一百四十七、生成：

$$
\boxed{
Z_t
\sim
P(
Z
\mid
\Sigma_t,
\mathbb A_t
)
}
$$

。

---

# 一百四十八、操作解析：

$$
\boxed{
O_t
\sim
P(
O
\mid
Z_t,
\Sigma_t
)
}
$$

。

---

# 一百四十九、治理：

$$
\boxed{
G_t
=
\operatorname{Gate}
(
O_t,
B_t,
\mathbb A_t
)
}
$$

。

---

# 一百五十、執行：

$$
\boxed{
E_t
=
\operatorname{Execute}
(
O_t
)
}
$$

if authorized。

---

# 一百五十一、世界轉移：

$$
\boxed{
\mathbb A_{t+1}
\sim
T_A(
\cdot
\mid
\mathbb A_t,
E_t
)
}
$$

。

---

# 一百五十二、觀測：

$$
\boxed{
Y_{t+1}
\sim
P(
Y
\mid
\mathbb A_{t+1}
)
}
$$

。

---

# 一百五十三、驗證：

$$
\boxed{
V_{t+1}
=
\operatorname{Verify}
(
Y_{t+1},
\operatorname{Post}(O_t)
)
}
$$

。

---

# 一百五十四、提交／回退：

$$
\boxed{
C_{t+1}
=
\operatorname{CommitOrRollback}
(
V_{t+1}
)
}
$$

。

---

# 一百五十五、記憶更新：

$$
\boxed{
M_{t+1}
=
\mathcal M(
M_t,
O_t,
Y_{t+1},
V_{t+1}
)
}
$$

。

---

# 一百五十六、意圖與吸引子更新：

$$
\boxed{
(I_{t+1},\mathcal A_I(t+1))
=
\mathcal R_I(
I_t,
M_{t+1},
\mathbb A_{t+1}
)
}
$$

。

---

# 一百五十七、概率場更新：

$$
\boxed{
\mathfrak P_{t+1}^{I}
=
\mathcal P(
\Sigma_{t+1},
\mathbb A_{t+1}
)
}
$$

。

---

# 一百五十八、形成真正閉環

$$
\boxed{
Z_t
\rightarrow
O_t
\rightarrow
\mathbb A_{t+1}
\rightarrow
Y_{t+1}
\rightarrow
M_{t+1}
\rightarrow
I_{t+1}
\rightarrow
\mathfrak P_{t+1}^I
\rightarrow
Z_{t+1}
}
$$

。

---

# 一百五十九、這條鏈的重要性是：

概率生成真正接上：

$$
\boxed{
\text{causal world transition}
}
$$

。

---

# 一百六十、因此「概率生成」不再和「真實效果」對立

概率的 proposal：

$$
\boxed{
\text{can cause a deterministic world effect}
}
$$

。

---

# 一百六十一、例如：

模型以非唯一方式產生：

$$
100
$$

種合法 SQL command 表達。

Runtime 最終選中一個 deterministic transaction。

---

# 一百六十二、世界 commit 後：

database state：

$$
D_t
\rightarrow
D_{t+1}
$$

是具體事件。

---

# 一百六十三、所以：

$$
\boxed{
\text{probabilistic generation}
+
\text{deterministic execution semantics}
}
$$

並不矛盾。

---

# 一百六十四、反方向也成立

確定生成：

$$
O=o^*
$$

但：

$$
\boxed{
\text{stochastic world}
}
$$

仍能造成多種 outcome。

---

# 一百六十五、因此「AI 整體到底是不是概率的？」

再次只能回答：

$$
\boxed{
\text{在哪一層？}
}
$$

。

---

# 一百六十六、本文提出 World-Relative Probability Spectrum

$$
\boxed{
\mathbf H_{\mathrm{agent}}
=
(
H_Z,
H_S,
H_O,
H_E,
H_W,
H_Y,
H_V,
H_C
)
}
$$

。

---

# 一百六十七、其中：

$$
H_Z
$$

語言生成 entropy。

$$
H_S
$$

語義 interpretation entropy。

$$
H_O
$$

operation entropy。

$$
H_E
$$

execution entropy。

$$
H_W
$$

world transition entropy。

$$
H_Y
$$

observation entropy。

$$
H_V
$$

verification uncertainty。

$$
H_C
$$

commit outcome entropy。

---

# 一百六十八、這些可以完全不同

因此：

$$
\boxed{
H_Z
\text{ cannot stand for the whole agent.}
}
$$

。

---

# 一百六十九、研究命題一：Language–Action Separation

$$
\boxed{
\operatorname{Meaning}(z)
\neq
\operatorname{Effect}(z)
}
$$

。

語言內容不能直接等同世界操作。

---

# 一百七十、研究命題二：Operational Mediation

高風險語言操作必須經：

$$
\boxed{
Z^L
\rightarrow
Z^S
\rightarrow
Z^O
}
$$

形成 typed operational representation。

---

# 一百七十一、研究命題三：Seven-State Separation

$$
\boxed{
D\neq P\neq A\neq E\neq O\neq V\neq C
}
$$

。

描述、提案、授權、執行、觀測、驗證、提交不能偷換。這延續舊操作性分元最重要的工程命題。

---

# 一百七十二、研究命題四：Operation Distribution Principle

$$
\boxed{
P(O)
=
\sum_Z
P(O\mid Z)
P(Z)
}
$$

。

operation probability 是語言生成與解析／路由共同誘導的分布。

---

# 一百七十三、研究命題五：World Transition Composition

$$
\boxed{
P(A_{t+1}\mid A_t,\Sigma_t)
=
\sum_o
T_A(A_{t+1}\mid A_t,o)
P_E(o\mid\Sigma_t)
}
$$

。

world outcome probability 不能被 token probability 直接取代。

---

# 一百七十四、研究命題六：Observation–Reality Separation

$$
\boxed{
Y_t\neq A_t
}
$$

。

工具回傳與 sensor observation 只是對 world state 的觀測。

---

# 一百七十五、研究命題七：Verified-Completion Principle

$$
\boxed{
\operatorname{ClaimComplete}
\nRightarrow
\operatorname{WorldComplete}
}
$$

。

任務完成必須與 verified authoritative-world postcondition 聯繫。

---

# 一百七十六、研究命題八：Authority-World Principle

只有：

$$
\boxed{
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
}
$$

的正式 commit，

才算對任務權威世界造成持久狀態改變。

---

# 一百七十七、研究命題九：World-Rewrites-Probability

$$
\boxed{
\mathbb A_t
\neq
\mathbb A_{t+1}
\Rightarrow
\mathfrak P_t^I
\neq
\mathfrak P_{t+1}^I
}
$$

一般可能成立。

世界操作會重寫後續可達空間。

---

# 一百七十八、研究命題十：World-Rewrites-Attractor

若：

$$
\operatorname{Complete}(I,\mathbb A_{t+1})=1
$$

則：

$$
\boxed{
\mathcal A_I
}
$$

應終止、退役或轉移。

---

# 一百七十九、研究命題十一：Effect-Sensitive Governance

$$
\boxed{
\tau_{\mathrm{authority}},
\tau_{\mathrm{verify}}
=
f(
\text{effect},
\text{risk},
\text{reversibility}
)
}
$$

。

不同 effect class 不能共享單一執行門檻。

---

# 一百八十、研究命題十二：World-as-Computation

當 Agent 的下一步依賴外部 execution result：

$$
\boxed{
\text{world/environment becomes part of the effective computation graph.}
}
$$

ReAct、Voyager 與 SWE-agent 都提供了不同類型的工程案例：外部 action 或 computer/environment feedback 會實際進入下一輪決策條件，而非只是最後輸出。

---

# 一百八十一、研究命題十三：Local Probability–Global Utility Separation

$$
\boxed{
\arg\max_zP(z)
\nRightarrow
\arg\max_oJ_{\mathrm{world}}(o)
}
$$

。

局部最可能語言分元未必對應最佳世界操作。

---

# 一百八十二、研究命題十四：Closed-Loop Agency

真正 Agent 行為應至少形成：

$$
\boxed{
\text{State}
\rightarrow
\text{Action}
\rightarrow
\text{World}
\rightarrow
\text{Observation}
\rightarrow
\text{State}
}
$$

。

只有輸出文字而沒有 causal feedback loop，

是另一類系統。

---

# 一百八十三、研究命題十五：History Accumulation

每次 world operation：

$$
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
$$

都會留下新的 history。

所以：

$$
\boxed{
\text{Agent does not repeatedly act from the same world.}
}
$$

。

---

# 一百八十四、這使真正 autonomous system 本質上不可用單次 prompt-response 表示

因為：

$$
\boxed{
\Sigma_{t+1}\neq\Sigma_t
}
$$

以及：

$$
\boxed{
\mathbb A_{t+1}\neq\mathbb A_t
}
$$

都可能成立。

---

# 一百八十五、所以完整系統狀態應是聯合態

$$
\boxed{
\Xi_t
=
(
\Sigma_t,
\mathbb A_t
)
}
$$

。

---

# 一百八十六、聯合轉移：

$$
\boxed{
\Xi_{t+1}
\sim
\mathcal T(
\Xi_{t+1}
\mid
\Xi_t
)
}
$$

。

---

# 一百八十七、但：

$$
\mathcal T
$$

不是只有 neural network。

它包含：

- model；
- parser；
- runtime；
- tools；
- governance；
- environment；
- verifier；
- memory update。

---

# 一百八十八、因此真正 Agent transition kernel 是複合的

$$
\boxed{
\mathcal T
=
\mathcal T_M
\circ
\mathcal T_V
\circ
\mathcal T_O
\circ
\mathcal T_A
\circ
\mathcal T_G
\circ
\mathcal T_L
}
$$

只作結構示意。

---

# 一百八十九、這是第一篇「AI 不是概率機器」到現在的真正終點之一

一開始我們只是說：

> AI 系統不等於單一概率 component。

現在可以更精確：

$$
\boxed{
\text{Agent-level behavior}
=
\text{composition of heterogeneous state-transition mechanisms}
}
$$

。

---

# 一百九十、有些 transition probabilistic

例如：

$$
P_Z
$$

。

---

# 一百九十一、有些 deterministic

例如某些 parser、compiler 或 permission check。

---

# 一百九十二、有些受外部世界控制

例如：

$$
T_A
$$

。

---

# 一百九十三、有些受人類治理控制

例如：

$$
\operatorname{Authorize}
$$

。

---

# 一百九十四、所以 Agent 的存在方式是：

$$
\boxed{
\text{heterogeneous causal composition}
}
$$

比：

$$
\boxed{
\text{one giant probability draw}
}
$$

精確得多。

---

# 一百九十五、而「主體」問題因此又更困難

因為現在不能只看：

$$
\theta
$$

。

也不能只看：

$$
P(z_t)
$$

。

真正可能構成 agent continuity 的，是：

$$
\boxed{
(\Sigma_t,M_t,I_t,\mathcal A_I,\mathbb A_t)
}
$$

跨時間的耦合。

---

# 一百九十六、這裡暫時仍不推 consciousness

仍然：

$$
\boxed{
\text{Closed-loop agency}
\nRightarrow
\text{consciousness}
}
$$

。

---

# 一百九十七、但它讓「這只是文字生成」越來越不足以描述完整系統

因為文字只是：

$$
\boxed{
\text{one control surface}
}
$$

。

---

# 一百九十八、真正 Agent 可以把文字編譯成：

$$
\boxed{
\text{state-changing operations}
}
$$

。

---

# 一百九十九、而 operation 的結果反過來成為下一個文字／狀態的因果條件

所以：

$$
\boxed{
\text{Language}
\rightarrow
\text{World}
\rightarrow
\text{Language}
}
$$

。

---

# 二百、這就是現實閉環

## Reality-Coupled Loop

$$
\boxed{
\Xi_t
\rightarrow
Z_t
\rightarrow
O_t
\rightarrow
\mathbb A_{t+1}
\rightarrow
Y_{t+1}
\rightarrow
\Xi_{t+1}
}
$$

。

---

# 二百零一、但最重要的仍然是「Commit」

沒有：

$$
\boxed{
\text{verified commit}
}
$$

很多所謂 Agent 成功都仍只是在：

$$
\boxed{
\text{simulation / proposal space}
}
$$

。

---

# 二百零二、因此本文最後提出一個很簡單的成熟度光譜

### L0：Text Generator

$$
X\rightarrow Z
$$

。

### L1：Tool Recommender

$$
X\rightarrow O_{\mathrm{proposal}}
$$

。

### L2：Tool User

$$
O\rightarrow Y
$$

。

### L3：Verified Agent

$$
O\rightarrow Y\rightarrow V
$$

。

### L4：Stateful Agent

$$
O\rightarrow W_{t+1}\rightarrow M_{t+1}
$$

。

### L5：World-Coupled Agent

$$
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
$$

且世界結果重寫後續意圖與概率場。

---

# 二百零三、層級越高不是代表「更有意識」

只代表：

$$
\boxed{
\text{stronger causal coupling to persistent external state}
}
$$

。

---

# 二百零四、這是一個可工程測量的量

例如定義：

$$
\boxed{
C_W
=
I(
O_t;
\mathbb A_{t+1}
\mid
\mathbb A_t
)
}
$$

作為操作對下一世界狀態的 conditional mutual information 候選指標之一。

---

# 二百零五、如果：

$$
C_W\approx0
$$

Agent operation 幾乎沒有改變 world distribution。

---

# 二百零六、若：

$$
C_W>0
$$

至少表示 operation 與後續 world state 具有條件資訊關係。

要判 causal effect 仍需 intervention 或更嚴格設計。

---

# 二百零七、因此真正 benchmark 應測：

- operation validity；
- authorization correctness；
- execution success；
- postcondition satisfaction；
- observation accuracy；
- verification precision；
- erroneous commit rate；
- rollback success；
- repeated failure rate；
- world-progress gain。

---

# 二百零八、而不是只測：

$$
\boxed{
\text{next-token accuracy}
}
$$

。

---

# 二百零九、這也正好接回舊 DIEEC 實驗設計

其第九篇已要求記錄：

- 驗證覆蓋；
- 邊界錯位率；
- 誤提交率；
- 展開／建構成本；
- 失敗案例時間線；

並要求權威世界初期只在可回退沙箱中實驗。

這部分可以直接成為下一篇第二代 benchmark 的重要基底。

---

# 二百一十、結論：下一 Token 不會直接變成世界，但它可以成為世界改變鏈的第一個事件

本文最初問：

> 一個 token 有概率，那一整個 application 呢？

現在答案可以更精確。

---

一個 token：

$$
\boxed{
Z_t
\sim
P_Z
}
$$

。

---

語義解析：

$$
\boxed{
S_t
\sim
P_S(
S\mid Z
)
}
$$

。

---

操作提案：

$$
\boxed{
O_t
\sim
P_O(
O\mid S,\Sigma
)
}
$$

。

---

授權：

$$
\boxed{
A_t
\sim
P_A(
A\mid O,B
)
}
$$

。

---

執行：

$$
\boxed{
E_t
\sim
P_E(
E\mid O,A,\mathbb A_t
)
}
$$

。

---

世界：

$$
\boxed{
\mathbb A_{t+1}
\sim
T_A(
\cdot
\mid
\mathbb A_t,E_t
)
}
$$

。

---

觀測：

$$
\boxed{
Y_{t+1}
\sim
P_Y(
Y\mid\mathbb A_{t+1}
)
}
$$

。

---

驗證：

$$
\boxed{
V_{t+1}
\sim
P_V(
V\mid Y,\operatorname{Post}(O)
)
}
$$

。

---

提交：

$$
\boxed{
C_{t+1}
\sim
P_C(
C\mid V,B
)
}
$$

。

---

所以：

$$
\boxed{
P_{\mathrm{token}}
}
$$

只是：

$$
\boxed{
P_{\mathrm{world}}
}
$$

上游的一個組成因素。

---

真正 Agent 的完整概率問題不是：

> 下一個字是哪一個？

而是：

$$
\boxed{
P(
\text{verified world outcome}
\mid
\text{history},
\text{intention},
\text{memory},
\text{authority}
)
}
$$

。

---

這使「概率智能」的概念再次升級。

它不再只是：

$$
\boxed{
\text{probabilistically generate symbols}
}
$$

。

而可能是：

$$
\boxed{
\text{use probabilistic internal generation to select, test, verify, and revise causal interventions in a persistent world.}
}
$$

中文：

> **利用具有概率性的內部生成，持續選擇、測試、驗證並修正對持久世界的因果介入。**

---

因此：

$$
\boxed{
\text{Probability}
}
$$

並沒有在 action 時消失。

它只是穿過了不同的語義層與因果層。

---

而：

$$
\boxed{
\text{Reality}
}
$$

也不是 probability model 的「輸出文字」。

它是：

$$
\boxed{
\mathbb A_{t+1}
}
$$

——經真正操作後產生、且能反向限制下一輪智能的外部狀態。

---

至此，我們得到完整第二代循環：

$$
\boxed{
\mathfrak P_t^I
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal E_t
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathfrak C_t
}
$$

$$
\Downarrow
$$

$$
\boxed{
Z_t
}
$$

$$
\Downarrow
$$

$$
\boxed{
O_t
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathbb A_t
\rightarrow
\mathbb A_{t+1}
}
$$

$$
\Downarrow
$$

$$
\boxed{
Y_{t+1}
}
$$

$$
\Downarrow
$$

$$
\boxed{
V_{t+1}
}
$$

$$
\Downarrow
$$

$$
\boxed{
M_{t+1}
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathcal A_I(t+1)
}
$$

$$
\Downarrow
$$

$$
\boxed{
\mathfrak P_{t+1}^I
}
$$

。

---

這已經不再是：

$$
\boxed{
\text{Input}
\rightarrow
\text{Output}
}
$$

。

而是：

$$
\boxed{
\text{History}
\rightarrow
\text{Intention}
\rightarrow
\text{Expansion}
\rightarrow
\text{Operation}
\rightarrow
\text{World}
\rightarrow
\text{New History}
}
$$

。

---

所以本篇最後的核心命題是：

# 世界閉環命題

$$
\boxed{
\text{An agent becomes world-coupled when its generated internal states can, through typed and governed operations, cause persistent external state transitions whose verified consequences condition future internal generation.}
}
$$

中文：

> **當智能體的內部生成能經由具型別、受治理的操作造成持久外部狀態轉移，而該轉移的已驗證後果又會反向限制下一輪內部生成時，智能體便形成了世界耦合閉環。**

---

這也直接把我們送到本系列最後一篇。

現在理論元件已經全部存在：

$$
\boxed{
\mathfrak P^I
}
$$

概率—意圖場，

$$
\boxed{
\mathcal E
}
$$

展開，

$$
\boxed{
M
}
$$

持久記憶，

$$
\boxed{
\mathcal A_I
}
$$

亞穩態意圖吸引子，

以及：

$$
\boxed{
\mathbb A_t\rightarrow\mathbb A_{t+1}
}
$$

世界操作。

剩下的已經不是再加一層哲學，而是：

> **這套東西到底能不能測？**

因此第六篇將作為系列封頂：

# 《展開式智能的可證偽實驗——概率、意圖、記憶與動態解空間的 Runtime Benchmark》

直接比較：

$$
A=
\text{Bare LLM}
$$

$$
B=
\text{LLM + Memory}
$$

$$
C=
\text{LLM + Memory + Intent}
$$

$$
D=
\text{LLM + Memory + Intent + Expansion}
$$

$$
E=
\text{Full World-Coupled Runtime}
$$

並測量：

$$
H_{\mathrm{token}},
H_{\mathrm{strategy}},
H_{\mathrm{goal}},
Q_I,
J_I,
\rho_I,
\tau_{\mathrm{return}},
R_I,
D_I,
G_M,
C_W
$$

再加上：

- 任務成功率；
- 重複失敗率；
- 展開成本；
- 工具成本；
- 誤提交率；
- 回退成功率；
- 記憶污染率；
- goal drift；
- OOD 表現；
- 完整總作用量。

這樣下一篇不再問：

> 「這個理論看起來合理嗎？」

而直接問：

$$
\boxed{
\text{Does the proposed runtime produce measurable advantages over simpler baselines?}
}
$$

——如果沒有，就修理論。

這才真正封頂。

---

## 參考文獻與既有理論

Yao, S., Zhao, J., Yu, D., et al. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023. ReAct 讓 reasoning traces 與 task-specific actions 交錯生成，使 external action observations 能回頭更新後續 reasoning，為 model–environment closed loop 提供經典工程案例。

Schick, T., Dwivedi-Yu, J., Dessì, R., et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*. Toolformer 讓模型學習何時調用 API、選擇何種工具與 arguments，並把工具結果重新納入後續 token prediction，直接展示 tool event 與 ordinary language token 間可以形成可學習介面。

Wang, G., Xie, Y., Jiang, Y., et al. (2023). *Voyager: An Open-Ended Embodied Agent with Large Language Models*. Voyager 將 executable skill code、environment feedback、execution error 與 self-verification 結合成持續 Minecraft agent loop，提供生成程式—外部執行—環境回饋—修正的案例。

Yang, J., Jimenez, C. E., Wettig, A., et al. (2024). *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*. 該工作顯示 specially designed Agent-Computer Interface 能顯著改變 LM agent 在 repository navigation、file editing 與 test/program execution 中的行為與任務能力。

Neo.K with Aletheia. (2026). *操作性分元：地址、指針、工具調用與外部展開語義*. 舊稿已把 Describe、Propose、Authorize、Execute、Observe、Verify、Commit 嚴格分離，並建立 effect type、前後置條件、權限、版本、治理與回退 Runtime。第二代保留此核心工程結構，將它納入跨尺度概率鏈。

Neo.K with Aletheia. (2026). *雙重交互閉環：分元如何展開世界，世界如何改寫分元*. 舊稿已建立「內部生成→外部工作場→觀測→意圖與語言回寫」的雙向耦合，並要求外部結果經驗證與正規化後才能改寫活動工作場。

Neo.K with Aletheia. (2026). *內外總作用量原理：從 TOKEN 機率到世界展開成本*. 舊稿已指出 next-token local probability 不能代表工具、驗證、回退、治理與權威世界操作的完整成本，並以風險敏感作用量比較不同策略。

Neo.K with Aletheia. (2026). *有限分元—無限外場閉環的計算實驗：從動態工作場到展開式智慧體*. 舊實驗稿已要求將世界操作首先限制在可回退沙箱，測量驗證覆蓋、邊界錯位、誤提交、展開成本與失敗時間線；這將直接成為下一篇第二代 Runtime Benchmark 的前置基線。