# T5：Bayesian Logic Judge
## 「貝葉斯邏輯判斷器」科普投影與產品介面

**版本：** v0.1  
**日期：** 2026-08-16  
**定位：** 對外別稱／科普介面  
**底層：** Dynamic Logic Runtime + AIMD-C + Evidence/History Layer

---

# 1. 為什麼叫「貝葉斯邏輯判斷器」

一般使用者容易理解：

> 新證據進來，支持度會改變。

這與：

$$
P(H)
\rightarrow
P(H\mid E)
$$

的 Bayesian 直覺相容。

因此產品對外可以叫：

$$
\boxed{
\text{Bayesian Logic Judge}.
}
$$

但文件必須明示：

$$
\boxed{
\text{這是低維投影名，
不是底層理論的完整定義。}
}
$$

---

# 2. 不等於普通 Bayesian Calculator

普通 calculator 可能只有：

```text
Prior
Likelihood
Posterior
```

本系統還有：

```text
evidence provenance
counterevidence
source independence
judgment state
closure policy
reopen
history
hypothesis split
model version
responsibility
```

所以：

$$
\boxed{
\text{Bayesian Updating}
\subset
\text{Dynamic Judgment}.
}
$$

---

# 3. 首頁最小介面

```text
┌────────────────────────────────────┐
│ 你想判斷什麼？                     │
│ [______________________________]   │
│                                    │
│ 目前狀態：Ω 仍在生成               │
│ 支持度：68%                         │
│ 反證壓力：31%                       │
│ 證據完整度：52%                     │
│                                    │
│ [加入證據] [查看理由] [回放歷史]   │
└────────────────────────────────────┘
```

---

# 4. 使用者不用先懂 $\Omega$

預設文案：

```text
仍在生成
```

tooltip：

```text
目前資料還不足以穩定閉合為支持或反對。
```

Advanced 才顯示：

$$
\Omega.
$$

---

# 5. 三種主要結果

對外：

```text
目前支持
目前反對
仍在生成
```

底層：

$$
\top_p,\bot_p,\Omega.
$$

一定要保留「目前」。

---

# 6. Support Score

可視化：

$$
S_t\in[0,1].
$$

但 UI 應標記：

```text
支持度
```

而非：

```text
真實機率
```

除非統計模型真的能支持 probability interpretation。

---

# 7. Counterpressure

另外顯示：

$$
C_t.
$$

避免：

$$
1-S_t
$$

被自動當作全部反證。

因為：

> 沒有支持

與：

> 有強反證

不同。

---

# 8. Completeness

$$
K_t
$$

表示 evidence coverage。

例如：

```text
支持度高
證據完整度低
```

使用者就不容易誤會：

> 90% = 幾乎證明。

---

# 9. Independence

顯示：

```text
12 reports
3 independent source clusters
```

這對新聞、超自然、政治、科學都重要。

---

# 10. 添加證據

使用者可：

```text
URL
Text
File
Manual observation
```

系統標記：

```text
verified
unverified
inference
```

---

# 11. AI 產生的東西

若 AI 說：

> 一個可能解釋是 X。

必須顯示：

```text
AI hypothesis
not evidence
```

核心：

$$
\boxed{
\text{推論不能偽裝成證據。}
}
$$

---

# 12. Why Changed?

任何狀態變化提供：

```text
Why changed?
```

例如：

```text
支持度 68% → 42%

原因：
- 原始來源被證實為後續修改
- 3 個轉載被合併為同一來源
- 新增 1 個高品質反證
```

---

# 13. History

```text
Aug 16 18:00  Still generating
Aug 16 18:20  Provisional support
Aug 16 19:10  Reopened
Aug 16 20:00  Provisional oppose
```

---

# 14. Replay

拖時間軸重新顯示當時：

- 數值；
- 證據；
- 公式；
- 理由。

這是產品最有辨識度的功能之一。

---

# 15. Advanced Mode

顯示：

$$
J(P,t)
$$

$$
P_t(H)
$$

$$
\Gamma_t
$$

$$
\mathcal I
$$

以及：

```text
model
policy
threshold
source graph
```

---

# 16. 可不可模式

產品可以增加：

```text
Can / Cannot
```

一個問題：

> 「AI 現在可以替病人直接下醫療決策嗎？」

顯示：

```text
技術上：可
資料上：部分可
權限上：不可
倫理上：需人類審核
```

這直接把可不可論科普化。

---

# 17. God / Paranormal 使用情境

若使用者問：

> 這是不是神蹟？

系統不應直接吐：

```text
God probability: 67%
```

而應拆：

```text
事件真實性
普通因果解釋度
未知殘差
意向來源證據
宗教歸因證據
```

避免把不相同命題壓成單一數字。

---

# 18. 科學使用情境

例如：

> 藥物 X 是否有效？

可顯示：

- meta-analysis；
- study quality；
- conflict；
- current closure；
- update history。

---

# 19. 新聞使用情境

例如：

> 某事件是否真的發生？

Evidence Cluster：

```text
primary source
independent confirmation
derivative reports
contradictions
```

---

# 20. 個人決策使用情境

例如：

> 我應不應該現在買這台機器？

這不是純 truth claim。

系統要把：

$$
\text{fact judgment}
$$

與：

$$
\text{decision utility}
$$

分開。

---

# 21. 不要製造假精確

如果資料不足：

```text
支持度：未知
```

可能比：

```text
53.72%
```

更誠實。

因此允許：

$$
S_t=\mathrm{NA}.
$$

---

# 22. 中立不是 50/50

若證據：

$$
99:1
$$

中立不能顯示：

```text
兩邊都有道理。
```

中立是：

$$
\boxed{
\text{同樣要求證據，
不是同樣分配概率。}
}
$$

---

# 23. 產品警告

介面應避免：

```text
AI has decided the truth.
```

推薦：

```text
Current evidence-based assessment
```

---

# 24. 分享卡片

對外分享：

```text
Claim
Current state
Snapshot time
Evidence count
Independent sources
```

並標：

```text
Live judgment — may update.
```

---

# 25. 靜態截圖風險

Screenshot 很容易在判斷更新後仍流傳。

因此 share image 可嵌：

```text
snapshot timestamp
short state id
```

---

# 26. API

```text
GET /judge/{id}/summary
GET /judge/{id}/evidence
GET /judge/{id}/history
GET /judge/{id}/advanced
```

---

# 27. Privacy Mode

個人案例：

```text
local only
no cloud
no public share
```

需要與公開研究模式分離。

---

# 28. Product Modes

```text
Simple
Research
Developer
```

### Simple

科普判斷器。

### Research

證據圖、來源、歷史。

### Developer

Runtime state、schema、event ledger。

---

# 29. 與 EveGlyph

最自然的產品形態不是另造一個巨大產品。

可以先成為 EveGlyph 的：

```text
Dynamic Judge panel
```

並允許任一 Live Paper 將 claim 投影進來。

---

# 30. 最小 Demo 文案

```text
命題：明天會下雨。

目前狀態：仍在生成
支持度：72%
證據完整度：80%

新增：
氣象模式更新

狀態：
仍在生成 → 目前支持

後來：
鋒面偏移

目前支持 → 重新開啟
```

普通人看到這一段就能理解動態判斷。

---

# 31. 名稱分層

$$
\boxed{
\begin{aligned}
\text{外部俗名}
&:\ \text{Bayesian Logic Judge}\\
\text{產品能力}
&:\ \text{Dynamic Judge}\\
\text{技術層}
&:\ \text{Executable Dynamic Logic Runtime}\\
\text{理論層}
&:\ \text{Generative Judgment Theory}
\end{aligned}
}
$$

---

# 32. 最終產品命題

$$
\boxed{
\text{不要只告訴使用者答案；
讓使用者看到答案如何形成、為何改變、何時可以重新打開。}
}
$$

這就是「貝葉斯邏輯判斷器」真正與普通 AI 問答介面不同的地方。
