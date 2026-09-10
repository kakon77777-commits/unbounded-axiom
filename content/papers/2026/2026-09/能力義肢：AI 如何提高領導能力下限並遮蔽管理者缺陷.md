---
title: "能力義肢：AI 如何提高領導能力下限並遮蔽管理者缺陷"
english_title: "Competence Prosthesis: How AI Raises the Leadership Floor and Masks Managerial Deficits"
series: "AI 原生決策治理與認知資本系列"
series_en: "AI-Native Decision Governance and Cognitive Capital Series"
paper: "03"
author: "Neo.K"
institution: "一言諾科技有限公司（EveMissLab）"
research_assistance: "AI-assisted theoretical development"
version: "v0.1"
date: "2026-09-07"
language: "zh-TW"
status: "Internal Working Paper / Canonical UTF-8 Source"
scope_note: "本文研究 AI 作為領導能力補償層的可能機制，以及其對組織績效、管理者評價、風險暴露與階級流動的影響；不主張 AI 必然提升所有管理者，也不主張 AI 可消除錯誤目標、權力濫用或責任問題。"
related_works:
  - "《從意圖到決策：AI 原生決策編譯器與稀疏意圖治理》"
  - "《說人話也是治理能力：適應性認知轉譯層與跨領域決策可達性》"
  - "《AI 時代的政治能力重新定價：從論述稀缺到判斷、執行與責任稀缺》"
  - "《從哲人王到動態決策中心：類終極智慧、現場主權與非僭位治理》"
  - "《全域觀察者與 AI 原生域計算系列》"
keywords:
  - "Competence Prosthesis"
  - "Leadership Competence Masking"
  - "Decision Floor Raising"
  - "AI-Augmented Management"
  - "Managerial Deficits"
  - "Organizational Resilience"
  - "Automation Dependency"
  - "Human-AI Governance"
---

# 能力義肢：AI 如何提高領導能力下限並遮蔽管理者缺陷

## 摘要

本研究提出「能力義肢」（Competence Prosthesis）與「領導能力遮蔽」（Leadership Competence Masking）兩個概念，用以分析 AI 在組織管理中的一個重要但容易被低估的效應：當 AI 可以持續提供資訊檢索、跨領域分析、方案生成、風險提醒、認知轉譯、執行追蹤與錯誤修復時，一名原本能力普通、知識不足、記憶有限或容易忽略細節的管理者，其實際組織表現可能顯著高於其單獨能力所能支持的水準。

本文將此現象表示為：

$$
C_{\mathrm{effective}}
=
F(
C_H,
C_{AI},
A,
T,
V,
R
)
$$

其中：

- $C_H$：人類管理者原生能力；
- $C_{AI}$：AI 認知與執行能力；
- $A$：AI 接受與吸收程度；
- $T$：AI 與人類之間的轉譯效率；
- $V$：驗證與反饋能力；
- $R$：資源與組織環境。

當：

$$
C_{AI}\gg C_H
$$

且：

$$
A,T,V
$$

足夠高時，組織可能出現：

$$
\boxed{
C_{\mathrm{effective}}
\gg
C_H
}
$$

也就是 AI 對管理者形成類似「認知義肢」的補償效果。

這種效果具有兩面性。

一方面，AI 可能提高治理品質下限：

$$
\boxed{
\text{Decision Floor Raising}
}
$$

降低因資訊不足、遺漏、記憶限制、跨域理解困難與低級錯誤造成的管理失敗。

另一方面，AI 也可能遮蔽管理者本身的缺陷，使外部觀察者難以區分：

$$
\text{Managerial Competence}
$$

與：

$$
\text{AI-Supported Competence}
$$

形成：

$$
\boxed{
\text{Leadership Competence Masking}
}
$$

因此，AI 可能同時降低「低能力管理者失敗」的機率，又提高組織對 AI 基礎設施的依賴；在正常狀態下表現優秀的領導者，可能在 AI 故障、未知事件、跨模型衝突、目標歧義或高不可逆危機中暴露出被長期遮蔽的能力缺口。

本文進一步指出，這個命題對未來階級流動具有深刻影響：若高資源低能力者可以透過 AI 大幅提高有效管理能力，則原本由低能力造成的向下流動機制可能被削弱；同時，低資源高能力者也可透過 AI 壓縮組織成本、快速建立成果與取得資源。AI 因而可能同時提高向上流動率與降低向下流動率。

本文最後提出一套可實證研究框架，用於區分「真實管理能力」、「AI 增強能力」、「AI 依賴」與「能力遮蔽」，並提出 outage test、override test、OOD test、AI-removal test、human rescue density 等觀察指標。

---

# 0. 問題起點：如果 AI 一直替管理者補洞，我們看到的到底是誰的能力？

傳統組織通常將績效歸因於：

$$
\text{Leader}
$$

例如：

> 公司成長很好，CEO 很厲害。

> 團隊執行很好，主管能力很強。

但 AI 原生組織會讓這個推論變得越來越不可靠。

因為：

$$
\text{Observed Performance}
$$

可能實際來自：

$$
\text{Human}
+
\text{AI}
+
\text{Tools}
+
\text{Memory}
+
\text{Verification}
+
\text{Automation}
$$

因此：

$$
\boxed{
\text{Observed Leadership Quality}
\neq
\text{Intrinsic Human Leadership Quality}
}
$$

這是本文的起點。

---

# 1. 定義能力義肢

本文定義：

$$
\boxed{
\text{Competence Prosthesis}
}
$$

為：

> 一個外部認知系統持續補足個體在知識、分析、記憶、規劃、溝通、執行或錯誤修復上的缺陷，使其實際完成任務的能力顯著高於其單獨能力。

可以寫成：

$$
C_{\mathrm{effective}}
=
C_H
+
P_{AI}
$$

其中：

$$
P_{AI}
$$

代表 AI 提供的補償能力。

但更完整地：

$$
P_{AI}
=
f(
C_{AI},
A,
T,
V,
\text{Integration}
)
$$

所以不是：

$$
\text{有 AI}
\Rightarrow
P_{AI}\gg0
$$

而是：

$$
\boxed{
\text{AI must be absorbed into the decision loop}
}
$$

---

# 2. 能力義肢不等於代理知識

舊版領域知識理論已提出：

$$
D_{\mathrm{proxy}}
$$

即管理者可以透過專家獲取代理知識。

但能力義肢比代理知識更廣。

代理知識主要回答：

> 有人替你知道。

能力義肢則包括：

$$
\text{Know}
+
\text{Analyze}
+
\text{Compare}
+
\text{Remember}
+
\text{Plan}
+
\text{Warn}
+
\text{Execute}
+
\text{Recover}
$$

所以：

$$
\boxed{
\text{Competence Prosthesis}
\supset
\text{Proxy Knowledge}
}
$$

---

# 3. AI 提高的是能力下限

假設管理者能力分布為：

$$
C_H
\sim
\mathcal D_H
$$

前 AI 時代：

$$
C_{\mathrm{effective}}
\approx
C_H
$$

AI 時代：

$$
C_{\mathrm{effective}}
=
C_H
+
P_{AI}
$$

如果低能力者受益幅度特別大：

$$
\frac{\partial P_{AI}}{\partial C_H}<0
$$

則 AI 會優先補足低端能力缺口。

這可形成：

$$
\boxed{
\text{Decision Floor Raising}
}
$$

即：

$$
\min
C_{\mathrm{effective}}
>
\min
C_H
$$

---

# 4. 為什麼低能力者可能受益最大？

因為 AI 最容易補的是：

- 資訊遺漏；
- 基礎專業不足；
- 記憶限制；
- 方案比較不足；
- 不知道有哪些選項；
- 忘記追蹤；
- 跨領域轉譯困難；
- 基本風險分析不足；
- 文件與流程管理不足。

這些問題在低能力管理者身上通常更加嚴重。

因此：

$$
\text{Marginal AI Benefit}
$$

對低能力者可能更高。

---

# 5. 但 AI 不一定提高能力上限同樣多

高能力管理者也會被 AI 增強。

例如：

$$
C_H=90
$$

配合：

$$
C_{AI}=95
$$

可能產生：

$$
C_{\mathrm{effective}}>100
$$

因為人類與 AI 可以互補。

但高能力者原本已能做到：

- 知道該問什麼；
- 辨識風險；
- 理解複雜資訊；
- 使用專家；
- 做反事實思考。

所以 AI 對其提升可能更多表現在：

$$
\text{Scale}
$$

$$
\text{Speed}
$$

$$
\text{Parallelism}
$$

$$
\text{Coverage}
$$

而不是補基本缺陷。

---

# 6. 能力義肢的第一個社會效果：無能變得不容易被看見

如果一個管理者：

$$
C_H=35
$$

但有：

$$
P_{AI}=45
$$

則：

$$
C_{\mathrm{effective}}=80
$$

外部看到的是：

$$
80
$$

而不是：

$$
35
$$

因此：

$$
\boxed{
\text{Observed Competence}
\neq
\text{Latent Human Competence}
}
$$

這就是：

$$
\boxed{
\text{Leadership Competence Masking}
}
$$

---

# 7. 遮蔽不等於欺騙

必須區分。

如果：

$$
\text{Human uses AI well}
$$

本身就是一種能力。

所以不能說：

> 只要用了 AI，就不算他的能力。

更準確的是：

$$
\boxed{
\text{AI Integration Skill}
}
$$

本身也應該算進管理能力。

因此：

$$
C_{\mathrm{manager}}
=
C_{\mathrm{intrinsic}}
+
C_{\mathrm{integration}}
$$

問題在於：

> 我們是否能知道哪些部分是可持續的管理能力，哪些部分只是對特定 AI stack 的依賴？

---

# 8. 依賴與能力的分界

如果管理者離開 AI 後：

$$
C_{\mathrm{effective}}
\rightarrow
C_H
$$

且：

$$
C_H
\ll
C_{\mathrm{effective}}
$$

則存在高度：

$$
\boxed{
\text{AI Dependency}
}
$$

可以定義：

$$
D_{AI}
=
1
-
\frac{
C_{\mathrm{without\ AI}}
}{
C_{\mathrm{with\ AI}}
}
$$

當：

$$
D_{AI}\rightarrow1
$$

表示大部分有效能力來自 AI。

---

# 9. AI Dependency 本身不一定是壞事

人類社會本來就依賴：

- 電力；
- 網路；
- ERP；
- 搜尋引擎；
- Excel；
- 雲端；
- 專家團隊。

所以：

$$
\text{Dependency}
\neq
\text{Failure}
$$

真正問題是：

$$
\boxed{
\text{Unmanaged Dependency}
}
$$

如果組織知道自己依賴什麼，並有：

- 備援；
- 多模型；
- 人類接管；
- audit；
- fallback；
- rollback；

那麼高度 AI 依賴仍可以是合理設計。

---

# 10. 真正危險的是被遮蔽的依賴

最危險狀態是：

$$
D_{AI}\gg0
$$

但組織認為：

$$
D_{AI}\approx0
$$

例如董事會相信：

> CEO 很強。

其實實際是：

> CEO 的 AI stack 很強。

當 AI stack 失效時：

$$
\text{Performance Collapse}
$$

就會顯著。

---

# 11. OOD 事件是能力遮蔽的壓力測試

日常管理問題通常高度重複。

AI 可以從大量歷史資料中做得很好。

但真正能測出管理者本體能力的，可能是：

$$
\boxed{
\text{Out-of-Distribution Events}
}
$$

例如：

- 新型金融危機；
- 戰爭；
- 供應鏈突然中斷；
- AI 模型本身失效；
- 前所未見法規；
- 新型資安事件；
- 關鍵合作夥伴突然倒閉；
- 重大聲譽危機。

此時：

$$
P_{AI}
$$

可能下降。

若：

$$
C_H
$$

也低，

則：

$$
C_{\mathrm{effective}}
\downarrow\downarrow
$$

---

# 12. 正常時期與危機時期的能力反轉

可定義：

$$
C_{\mathrm{normal}}
$$

與：

$$
C_{\mathrm{crisis}}
$$

某些管理者可能：

$$
C_{\mathrm{normal}}\gg C_{\mathrm{crisis}}
$$

這不一定是因為他本人突然變笨。

而是：

$$
P_{AI}^{\mathrm{normal}}
\gg
P_{AI}^{\mathrm{crisis}}
$$

所以：

$$
\boxed{
\text{AI can flatten normal-time variance while preserving crisis-time variance}
}
$$

這是很重要的研究命題。

---

# 13. AI 故障測試

未來管理者可能需要新的 stress test。

例如：

$$
\boxed{
\text{AI Removal Test}
}
$$

觀察在：

- 無 AI；
- 降級模型；
- 無外部網路；
- 無長期記憶；
- 無自動工具；

狀態下，管理者與組織能否繼續：

$$
\text{Decide}
+
\text{Coordinate}
+
\text{Recover}
$$

這不是要求組織回到前 AI 時代。

而是測量：

$$
\text{Fallback Capacity}
$$

---

# 14. Override Test

另一個重要測試是：

$$
\boxed{
\text{Override Test}
}
$$

當：

$$
\text{AI Recommendation}=A
$$

人類選：

$$
B
$$

觀察：

- 為什麼 override？
- 結果如何？
- 人類是否能提出 AI 未發現的新資訊？
- AI 是否其實是對的？
- 是否只是 ego override？

這可以揭露：

$$
\text{Human Independent Judgment}
$$

---

# 15. Human Rescue Density

如果 AI 經常自己修復問題，

人類介入很少。

可以定義：

$$
HRD
=
\frac{
N_{\mathrm{human rescue}}
}{
N_{\mathrm{AI-managed events}}
}
$$

但 HRD 很低不代表管理者很強。

它可能表示：

$$
AI_{\mathrm{stewardship}}
$$

非常成熟。

因此：

$$
\boxed{
\text{Low Human Intervention}
\neq
\text{High Human Competence}
}
$$

---

# 16. 能力義肢會改變領導者評價制度

傳統公司評估管理者：

- KPI；
- 營收；
- 毛利；
- 團隊穩定；
- 產品成功；
- 危機處理。

AI 時代還需要：

$$
\text{AI Integration Quality}
$$

$$
\text{Override Quality}
$$

$$
\text{Fallback Capacity}
$$

$$
\text{AI Dependency Transparency}
$$

$$
\text{Correctability}
$$

否則無法判斷：

> 管理者本身到底在系統中貢獻什麼？

---

# 17. 未來的「好領導者」可能不需要比 AI 聰明

這是一個重要的重新定價。

若：

$$
I_{AI}\gg I_H
$$

在多數知識任務上成立，

則要求：

$$
I_H>I_{AI}
$$

可能是不必要的。

真正重要的可能是：

$$
\boxed{
\text{Intent Quality}
+
\text{AI Integration}
+
\text{Trade-off Judgment}
+
\text{Correctability}
+
\text{Responsibility}
}
$$

所以：

$$
\boxed{
\text{Leadership}
\neq
\text{Being the smartest node}
}
$$

---

# 18. 能力義肢可能降低 Peter Principle 的破壞力

傳統彼得原理指出：

> 人會被升到自己無法勝任的層級。

AI 時代，假設升遷後出現：

$$
C_H<C_{\mathrm{role threshold}}
$$

但 AI 可以提供：

$$
P_{AI}
$$

使：

$$
C_H+P_{AI}
\geq
C_{\mathrm{role threshold}}
$$

那麼部分彼得原理失敗可能被 AI 緩和。

也就是：

$$
\boxed{
\text{Promotion beyond intrinsic competence}
\not\Rightarrow
\text{Immediate organizational failure}
}
$$

這很可能改變大型組織的人才結構。

---

# 19. 但它也可能讓不適任者停留更久

這是反方向效果。

以前：

$$
\text{Low Competence}
\rightarrow
\text{Bad Outcomes}
\rightarrow
\text{Replacement}
$$

未來：

$$
\text{Low Competence}
+
AI
\rightarrow
\text{Acceptable Outcomes}
\rightarrow
\text{Retention}
$$

因此：

$$
\boxed{
\text{AI can reduce selection pressure on managers}
}
$$

這可能降低組織對真正高能力管理者的辨識能力。

---

# 20. AI 可能降低向下流動率

如果有資源者原本最主要的失敗路徑之一是：

$$
\text{Resources}
+
\text{Bad Management}
\rightarrow
\text{Resource Dissipation}
$$

AI 可以改成：

$$
\text{Resources}
+
\text{Bad Management}
+
AI
\rightarrow
\text{Resource Preservation}
$$

則：

$$
\boxed{
P(\text{downward mobility})
\downarrow
}
$$

這直接連到本系列第七篇。

---

# 21. 同時 AI 也提高低資源高能力者的槓桿

另一端：

$$
\text{High Capability}
+
\text{Low Resources}
$$

若能取得：

$$
AI
$$

則可壓縮：

$$
\text{Labor Cost}
$$

$$
\text{Knowledge Cost}
$$

$$
\text{Coordination Cost}
$$

所以：

$$
\boxed{
P(\text{upward mobility})
\uparrow
}
$$

因此 AI 的階級效應可能是：

$$
\boxed{
\text{Upward Mobility}\uparrow
\quad\land\quad
\text{Downward Mobility}\downarrow
}
$$

而不是單方向流動。

---

# 22. 資源與能力的新組合

可以建立四類型：

| 類型 | 資源 | 原生能力 | AI 吸收 | 可能結果 |
|---|---:|---:|---:|---|
| A | 高 | 高 | 高 | 極高組織能力 |
| B | 高 | 低／中 | 高 | AI 補足，資源優勢被保護 |
| C | 低 | 高 | 高 | 快速槓桿、向上流動候選 |
| D | 高 | 高／中 | 低 | 可能被 AI 時代反向淘汰 |

真正的競爭不再只是：

$$
R
$$

或：

$$
C_H
$$

而是：

$$
\boxed{
R
\times
C_H
\times
A_{AI}
}
$$

---

# 23. 能力義肢與認識論傲慢

若管理者拒絕 AI：

$$
A_{AI}\rightarrow0
$$

則：

$$
P_{AI}\rightarrow0
$$

即使：

$$
C_{AI}\gg0
$$

也無法轉成有效能力。

因此：

$$
\boxed{
\text{Epistemic Arrogance}
}
$$

可能使一個原本可免費取得的能力義肢失效。

這就是為什麼傲慢在 AI 時代可能轉化成：

$$
\text{Negative Cognitive Capital}
$$

本系列第五篇將獨立處理。

---

# 24. AI 擦屁股作為正式管理機制

日常語言中可以說：

> AI 一直幫管理者擦屁股。

理論上可以拆成：

$$
\text{Intent Error}
$$

$$
\text{Constraint Error}
$$

$$
\text{Plan Error}
$$

$$
\text{Execution Error}
$$

$$
\text{Prediction Error}
$$

AI 不斷做：

$$
\boxed{
\text{Cognitive Error Correction}
}
$$

所以：

$$
\text{Leadership Output}
$$

可能長期高於：

$$
\text{Leadership Input Quality}
$$

這就是能力義肢最直觀的運作方式。

---

# 25. 但錯誤目標無法被單純補足

假設管理者真正目標是：

$$
U_H
$$

如果：

$$
U_H
$$

本身有問題，

AI 可以：

- 提醒；
- 反駁；
- 模擬後果；
- 提供替代。

但如果人類仍然堅持：

$$
U_H
$$

則 AI 可能只是：

$$
\text{Optimize bad objective better}
$$

因此：

$$
\boxed{
\text{Competence Prosthesis}
\neq
\text{Moral Prosthesis}
}
$$

這是非常重要的邊界。

---

# 26. 能力義肢也不等於責任轉移

即使：

$$
Causality_{AI}\gg Causality_H
$$

若制度仍規定：

$$
Authority_H=1
$$

則：

$$
Responsibility_H
$$

不應自動降為零。

所以：

$$
\boxed{
\text{AI augmentation}
\not\Rightarrow
\text{automatic responsibility dilution}
}
$$

這會直接連到下一篇「形式權力與實際決策因果」。

---

# 27. 組織韌性的新定義

AI 原生組織韌性不能只看：

$$
\text{Can AI keep running?}
$$

也要看：

$$
\boxed{
\text{Can the organization degrade gracefully?}
}
$$

可以定義：

$$
R_O
=
f(
\text{Redundancy},
\text{Fallback},
\text{HumanTakeover},
\text{ModelDiversity},
\text{DataContinuity},
\text{AuthorityClarity}
)
$$

如果 AI 失效後組織立刻崩潰：

$$
R_O\downarrow
$$

即使正常時表現很高。

---

# 28. 多模型義肢

未來管理者可能不是依賴一個 AI。

而是：

$$
\{
AI_1,
AI_2,
AI_3,\ldots
\}
$$

例如：

- frontier model；
- legal model；
- finance model；
- local model；
- independent external model。

所以：

$$
P_{AI}
=
\sum_i
w_i C_{AI_i}
$$

但這又增加：

$$
\text{orchestration complexity}
$$

因此：

$$
\text{More AI}
\neq
\text{More Competence}
$$

若協調失敗：

$$
P_{AI}\downarrow
$$

---

# 29. 真正成熟的能力義肢必須可被看見

組織治理不應把 AI 補償層藏起來。

至少應知道：

- 哪些決策 AI 參與；
- 哪些推薦來自 AI；
- 哪些結論由外部專家產生；
- 哪些決策由人類 override；
- 哪些錯誤由 AI 修正；
- 哪些成果高度依賴特定模型。

這叫：

$$
\boxed{
\text{Competence Provenance}
}
$$

沒有 provenance，就無法判斷：

$$
\text{who contributed what}
$$

---

# 30. 實證研究：怎麼分辨「管理者很強」與「AI 很強」？

未來可以設計幾種自然觀察。

## 30.1 AI Adoption Event Study

觀察企業在：

$$
t_0
$$

正式導入高階 AI 決策系統前後：

$$
\Delta Y
$$

---

## 30.2 AI Outage Study

當：

$$
\text{AI unavailable}
$$

時，

管理績效是否顯著下降。

---

## 30.3 Cross-Manager Comparison

同一 AI stack 下，不同管理者：

$$
C_{\mathrm{effective},i}
$$

是否仍有巨大差異。

---

## 30.4 Cross-AI Comparison

同一管理者換不同 AI：

$$
C_{\mathrm{effective}}
$$

變化多少。

---

## 30.5 Override Outcome Tracking

比較：

$$
\text{AI accepted outcomes}
$$

與：

$$
\text{AI overridden outcomes}
$$

---

# 31. 能力義肢指數

未來可探索一個：

$$
\boxed{
CPI
=
\text{Competence Prosthesis Index}
}
$$

例如：

$$
CPI
=
w_1 K
+
w_2 A
+
w_3 P
+
w_4 E
+
w_5 R
$$

其中：

- $K$：Knowledge Augmentation；
- $A$：Analysis Augmentation；
- $P$：Planning Augmentation；
- $E$：Execution Augmentation；
- $R$：Recovery Augmentation。

CPI 越高，代表管理者的有效能力越依賴 AI 補償層。

---

# 32. 能力遮蔽指數

另可定義：

$$
\boxed{
CMI
=
\text{Competence Masking Index}
}
$$

粗略表示：

$$
CMI
=
\frac{
C_{\mathrm{with\ AI}}
-
C_{\mathrm{without\ AI}}
}{
C_{\mathrm{with\ AI}}
}
$$

若：

$$
CMI\rightarrow1
$$

表示可觀察能力大部分來自 AI。

---

# 33. 遮蔽不是負面標籤，而是治理資訊

CMI 高不代表管理者應被淘汰。

可能代表：

> 他非常懂得使用 AI。

真正治理問題是：

$$
\boxed{
\text{Is the dependency understood, governed, and resilient?}
}
$$

若答案是是，

則：

$$
CMI\gg0
$$

仍可接受。

---

# 34. 新型管理者可能是「意圖型管理者」

傳統管理者價值常來自：

$$
\text{Know}
+
\text{Plan}
+
\text{Control}
$$

AI 時代可能出現：

$$
\boxed{
\text{Intent-Oriented Manager}
}
$$

其核心能力是：

- 定義方向；
- 設定限制；
- 選擇代價；
- 使用 AI；
- 判斷何時 override；
- 承擔結果。

這個角色本身可能不比 AI 更博學。

但仍可能是一名非常有效的管理者。

---

# 35. 新型失敗者可能是「高權力低可修正者」

最危險組合可能不是：

$$
C_H\text{ low}
$$

而是：

$$
Authority_H\text{ high}
$$

且：

$$
Correctability_H\text{ low}
$$

因為 AI 可以補：

$$
\text{Knowledge}
$$

但很難補：

$$
\boxed{
\text{Refusal to Update}
}
$$

所以：

$$
\text{High Authority}
+
\text{Low Correctability}
$$

可能比：

$$
\text{Low Knowledge}
$$

更危險。

---

# 36. 與前兩篇的完整連接

第一篇：

$$
\text{Sparse Intent}
\rightarrow
\text{Decision Compiler}
$$

第二篇：

$$
\text{Decision World}
\rightarrow
\text{ACTL}
\rightarrow
\text{Decision Accessibility}
$$

第三篇：

$$
\text{AI Assistance}
\rightarrow
\text{Competence Prosthesis}
\rightarrow
\text{Observed Leadership Quality}
$$

所以三篇合起來：

$$
\boxed{
\text{Human Intent}
\rightarrow
\text{AI Decision World}
\rightarrow
\text{Human-Readable Options}
\rightarrow
\text{AI-Augmented Leadership}
}
$$

---

# 37. 可實證命題

## H1：AI 提高管理能力下限

$$
Var(C_{\mathrm{effective}})
<
Var(C_H)
$$

至少在日常管理任務上可能成立。

---

## H2：AI 對低能力管理者的邊際效益更高

$$
\frac{\partial P_{AI}}{\partial C_H}<0
$$

在部分任務域成立。

---

## H3：AI adoption 降低管理者表現差異，但危機事件重新放大差異

正常狀態：

$$
Var(C_{\mathrm{effective}})\downarrow
$$

危機狀態：

$$
Var(C_{\mathrm{effective}})\uparrow
$$

---

## H4：AI 依賴高的管理者在 AI outage 中績效下降更大

$$
D_{AI}\uparrow
\Rightarrow
\Delta \text{Performance}_{\text{outage}}\downarrow
$$

---

## H5：高 AI 吸收可能降低有資源管理者的向下流動率

$$
AIAbsorption\uparrow
\Rightarrow
P(\text{downward mobility})\downarrow
$$

---

## H6：高能力低資源者可透過 AI 提高向上流動率

$$
Capability_H\uparrow
\land
AIAbsorption\uparrow
\Rightarrow
P(\text{upward mobility})\uparrow
$$

---

# 38. 研究邊界

本文不主張：

1. AI 能讓所有低能力管理者變強。
2. AI 可以補足錯誤價值觀。
3. AI 可以消除權力濫用。
4. 高 AI 依賴一定是壞事。
5. 高 CMI 等於管理者沒有能力。
6. 所有危機都能透過移除 AI 測試。
7. AI 能完全取代 tacit knowledge。
8. 組織績效可以被簡單歸因於 CEO 或模型單一因素。

---

# 39. 結論：AI 可能讓「無能」變得更少致命，也更難被辨識

本文的核心不是：

> AI 會讓所有領導者都變厲害。

而是：

$$
\boxed{
\text{AI can raise the minimum viable competence of leadership}
}
$$

當 AI 可以持續補足：

- 知識；
- 分析；
- 規劃；
- 溝通；
- 記憶；
- 追蹤；
- 修復；

時，

原本容易造成組織失敗的管理缺陷可能被大幅削弱。

因此：

$$
\boxed{
\text{Bad Manager}
+
\text{Good AI}
\neq
\text{Bad Organization}
}
$$

至少不再是必然。

但代價是：

$$
\boxed{
\text{Leadership Quality}
}
$$

與：

$$
\boxed{
\text{AI-System Quality}
}
$$

越來越難被分離。

所以未來管理科學不能只問：

> 這個 CEO 好不好？

而要問：

> 這個人機複合管理系統，在沒有 AI、換 AI、AI 衝突、AI 出錯、未知危機時，還剩下多少治理能力？

這就是能力義肢理論真正想處理的問題。

AI 可以成為：

$$
\boxed{
\text{Cognitive Error-Correction Layer}
}
$$

也可以成為：

$$
\boxed{
\text{Leadership Competence Prosthesis}
}
$$

但一個成熟組織必須知道：

> 自己究竟有多強。

以及：

> 其中有多少，是 AI 幫它撐住的。

---

# Appendix A — Competence Provenance Schema

```yaml
manager:
  intrinsic_domain_knowledge:
  judgment_role:
  authority_scope:
  override_rights:

ai_support:
  models: []
  knowledge_augmentation:
  analysis_augmentation:
  planning_augmentation:
  execution_augmentation:
  recovery_augmentation:

dependency:
  ai_required_for_normal_operation:
  fallback_model:
  human_takeover:
  outage_degradation:
  memory_dependency:

decision_provenance:
  ai_generated_options:
  ai_recommendation:
  human_override:
  override_reason:
  final_authority:
  outcome:

stress_tests:
  ai_removal_test:
  degraded_model_test:
  ood_event_test:
  override_test:
  crisis_takeover_test:
```

---

# Appendix B — 系列位置

前篇：

1. 《從意圖到決策：AI 原生決策編譯器與稀疏意圖治理》
2. 《說人話也是治理能力：適應性認知轉譯層與跨領域決策可達性》

本篇：

3. 《能力義肢：AI 如何提高領導能力下限並遮蔽管理者缺陷》

後續：

4. 《形式權力與實際決策因果：人機複合決策系統的權力重新分布》
5. 《傲慢作為負認知資本：AI 時代的認識論僵固性與可修正性》
6. 《外部智能治理：顧問、第三方 AI 與組織認知稽核》
7. 《AI 與階級流動：能力民主化、資源固化與雙相效應》
8. 《誰能真正吸收 AI：資源、能力、接受度與組織吸收函數》
9. 《從假說到實證：全球五百大企業的 AI 決策治理縱向研究設計》
