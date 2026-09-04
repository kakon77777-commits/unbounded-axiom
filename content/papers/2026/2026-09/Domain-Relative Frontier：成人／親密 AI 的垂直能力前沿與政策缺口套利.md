# Domain-Relative Frontier：成人／親密 AI 的垂直能力前沿與政策缺口套利

**系列：** Intimacy-Native AI / Relationship Intelligence  
**篇次：** 03 / 09  
**版本：** v0.1  
**研究性質：** 理論／模型策略／產業結構論文  
**語言：** 繁體中文  
**作者：** Neo.K  
**機構：** EveMissLab／一言諾科技有限公司  
**日期：** 2026-08-30

## 摘要

大型前沿模型通常以通用推理、程式設計、知識、工具使用、多模態與長上下文等綜合能力衡量，但產品市場並不存在唯一的「全域排行榜」。對特定使用者族群而言，真正重要的是模型在指定任務、政策條件、部署成本、隱私需求與持續互動條件下所提供的有效效用。

本文提出 **Domain-Relative Frontier（領域相對前沿）**：一個模型即使在通用能力上顯著落後於前沿模型，仍可能在某個狹窄領域的有效使用者效用上形成局部前沿。本文以成人／親密 AI 作為高對比案例，分析四種可形成相對前沿的來源：Domain Specialization、Policy Gap、Local/Privacy Advantage 與 System-Level Augmentation。

本文特別區分「解除拒答」與「增加領域智能」。降低拒答只會擴大模型既有能力的可達域，無法自動創造原模型未具備的關係建模、敘事控制、長期狀態追蹤與上下文判斷能力。真正的垂直前沿需要使：

$$
U_D(M_s)>U_D(M_f)
$$

在指定領域 $D$ 成立，即便全域能力仍滿足：

$$
G(M_s)<G(M_f).
$$

本文進一步提出 Effective Domain Capability、Policy Shadow、Specialization Gain 與 Domain Arbitrage Potential 等概念。本文亦強調：政策缺口不是免費套利。支付處理、法律差異、年齡治理、非自願內容風險、分發平台限制與品牌風險會同步提高合規成本。可持續策略不是「無底線模型」，而是在合法域內建立高能力、高情境敏感度與可配置治理架構。

**關鍵詞：** Domain-Relative Frontier、Vertical AI、Small Language Model、Domain Specialization、Policy Gap、Local AI、Adult AI、Intimacy-Native AI、Relationship Intelligence

---

## 1. AI 前沿並不只有一條

常見模型比較可寫成：

$$
M_1>M_2>M_3.
$$

但這通常是把多維能力壓縮成單一綜合分數。令：

$$
\mathbf{c}(M)=
(
c_{\text{reason}},
c_{\text{code}},
c_{\text{knowledge}},
c_{\text{tool}},
c_{\text{multimodal}},
c_{\text{memory}},
\dots
)
$$

表示模型能力向量，再令：

$$
G(M)=g(\mathbf{c}(M))
$$

代表全域能力分數。

對特定領域 $D$，使用者真正最大化的卻是：

$$
U_D(M).
$$

一般而言：

$$
U_D(M)\neq G(M).
$$

因此完全可能存在：

$$
G(M_s)<G(M_f)
$$

但：

$$
U_D(M_s)>U_D(M_f).
$$

本文稱 $M_s$ 在領域 $D$ 中形成 **Domain-Relative Frontier**。

---

## 2. Domain-Relative Frontier 的基本定義

令候選模型集合為：

$$
\mathcal{M}.
$$

令部署約束為：

$$
\mathcal{K}
=
\{
\text{VRAM},
\text{latency},
\text{cost},
\text{privacy},
\text{license},
\text{policy}
\}.
$$

可行模型集合為：

$$
\mathcal{M}_{\mathcal{K}}
=
\{
M\in\mathcal{M}:M\text{ satisfies }\mathcal{K}
\}.
$$

則：

$$
F_D(\mathcal{K})
=
\arg\max_{M\in\mathcal{M}_{\mathcal{K}}}
U_D(M).
$$

所以：

$$
\boxed{
\text{Global Frontier}
\neq
\text{Domain Frontier}.
}
$$

只要領域、使用者效用或部署約束改變，前沿排序就可能改變。

---

## 3. 小模型專門化：可行，但不是魔法

2026 年已有研究直接測試 135M 至 3B 的開放權重模型在本地硬體與參數高效微調條件下的專門化。部分模型在受控狹窄 benchmark 上得到明顯提升，說明「可用的本地專家」並不要求複製 frontier model 的全部通用能力。

可以定義：

$$
\Delta_{\text{spec}}(M,D)
=
U_D(M^{\text{specialized}})
-
U_D(M^{\text{base}}).
$$

某些領域存在：

$$
\Delta_{\text{spec}}(M,D)>0.
$$

然而 KOCO-BENCH 同時顯示：當任務要求真正取得並使用新的領域知識時，即使採用 SFT、RAG 等方法，最強系統仍可能遭遇顯著困難。

所以不應寫成：

$$
\text{Fine-tuning}
\Rightarrow
\text{Domain Expert}.
$$

更合理的是：

$$
\boxed{
\text{Specialization Potential}
\neq
\text{Guaranteed Specialization}.
}
$$

---

## 4. 成人／親密 AI 的特殊性：能力之外還有政策可達域

令模型原始領域能力為：

$$
C_D(M).
$$

令平台政策下可實際使用的比例為：

$$
\rho_D(M)\in[0,1].
$$

可定義：

$$
E_D(M)
=
C_D(M)\rho_D(M),
$$

其中 $E_D(M)$ 為 **Effective Domain Capability**。

如果：

$$
C_D(M_f)\gg C_D(M_s)
$$

但：

$$
\rho_D(M_f)\ll\rho_D(M_s),
$$

則仍可能出現：

$$
E_D(M_s)>E_D(M_f).
$$

這不是小模型突然比前沿模型更聰明，而是前沿模型的一部分能力在指定產品條件下不可達。

本文把：

$$
1-\rho_D(M)
$$

造成的效用損失稱為 **Policy Shadow**。

---

## 5. Policy Gap 不是「審查／無審查」二元

現行主流服務本身就顯示政策空間不是 Boolean。

Gemini API 將 sexually explicit content 作為獨立安全類別，可在一定範圍內調整過濾設定，但仍存在平台政策與濫用監測。

Grok 在 2026 年消費端明確存在 NSFW 設定，但官方 FAQ 同時說明，啟用 NSFW 並不關閉 moderation；涉及未成年人及非自願私密影像等類別仍不可解除。

因此：

$$
\text{Policy Space}
\neq
\{
\text{Censored},
\text{Uncensored}
\}.
$$

而應視為：

$$
\mathcal{P}
=
\{
p_1,p_2,\dots,p_n
\}.
$$

本文將市場需要效用與主流服務可達效用的差定義為：

$$
\Delta_P(D)
=
U_D^{\text{demand}}
-
U_D^{\text{mainstream-accessible}}.
$$

若：

$$
\Delta_P(D)>0,
$$

便存在 Policy Gap。

---

## 6. De-restriction 不等於 Domain Intelligence

令：

$$
M_b
$$

為基礎模型，降低拒答後得到：

$$
M_u.
$$

若原模型已知道相關內容，只是因 alignment 或 policy layer 拒絕，則可能有：

$$
\rho_D(M_u)>\rho_D(M_b).
$$

但：

$$
C_D(M_u)\approx C_D(M_b)
$$

仍可能成立。

因此：

$$
\boxed{
\text{De-restriction}
\neq
\text{New Intelligence}.
}
$$

降低拒答不會自動增加：

- 關係狀態追蹤；
- 長程角色一致性；
- 情境尺度控制；
- 親密與日常之間的自然切換；
- 世界模型；
- 具身行動判斷。

真正的垂直專門化必須提高：

$$
C_D(M),
$$

而不只是：

$$
\rho_D(M).
$$

---

## 7. 成人內容效用不是單一 explicitness 分數

若產品只最大化：

$$
U_D
=
Q_{\text{explicit-content}},
$$

便容易把「成人內容品質」誤認為整個親密 AI 的產品價值。

依本系列前兩篇，更合理的效用向量為：

$$
\mathbf{u}_D
=
(
Q_{\text{character}},
Q_{\text{continuity}},
Q_{\text{world}},
Q_{\text{memory}},
Q_{\text{style}},
Q_{\text{intimacy}},
Q_{\text{activation}},
Q_{\text{boundary}}
).
$$

因此：

$$
U_D=w^\top\mathbf{u}_D.
$$

一個中小型模型即使在數學、科學與程式設計上遠低於通用前沿，只要它在角色一致性、長期記憶、情境啟動、關係狀態與隱私上更符合需求，就可能滿足：

$$
U_D(M_s)>U_D(M_f).
$$

這才是成人／親密 AI 的 **Domain-Relative Frontier**。

---

## 8. 前沿可能存在於系統，而不是模型權重

真正產品應寫成：

$$
S_D
=
(
M,
R,
W,
H,
P,
N,
G
),
$$

其中：

- $M$：基礎模型；
- $R$：Relationship State；
- $W$：World State；
- $H$：Long-Term History；
- $P$：Preference Model；
- $N$：Narrative Controller；
- $G$：Governance Kernel。

所以：

$$
\text{Product Intelligence}
\neq
\text{Model Intelligence}.
$$

產品效用更準確地是：

$$
U_D(S_D)
$$

而不是單純：

$$
U_D(M).
$$

因此，小公司的護城河可能不是重新訓練 foundation model，而是：

$$
\boxed{
\text{Moderate Model}
+
\text{Excellent Domain Runtime}.
}
$$

對 Relationship Intelligence 而言，持久狀態與事件後果尤其重要。

---

## 9. Local AI 的另一條前沿：隱私與控制

親密互動資料具有高度私人性。

因此：

$$
U_D
$$

還可能包含：

$$
Q_{\text{privacy}},
Q_{\text{offline}},
Q_{\text{control}}.
$$

所以即使：

$$
G(M_{\text{local}})
<
G(M_{\text{cloud}}),
$$

仍可能因：

$$
Q_{\text{privacy}}(M_{\text{local}})
\gg
Q_{\text{privacy}}(M_{\text{cloud}})
$$

而得到更高總效用。

因此：

$$
\boxed{
\text{Local Advantage}
\neq
\text{Only Cost Advantage}.
}
$$

本地部署也可能代表更強的私人狀態保存、離線運作、政策可控性與資料最小外流。

---

## 10. 開源生態已形成，但模型數量不等於成熟智能

2026 年 Hugging Face 的 roleplay 標籤下已存在數千個模型條目，包含 creative writing、roleplay、uncensored 與 personality-oriented 微調。

這至少表示：

$$
D_{\text{roleplay}}
$$

已經形成明顯的開源專門化生態。

但：

$$
\text{Many Models}
\not\Rightarrow
\text{High Domain Intelligence}.
$$

大量模型仍可能主要改善風格、降低拒答、合併權重或強化角色語氣。

因此需要獨立 benchmark：

$$
B_D
=
(
B_{\text{continuity}},
B_{\text{state}},
B_{\text{activation}},
B_{\text{boundary}},
B_{\text{style}},
B_{\text{recovery}}
).
$$

沒有這些測試，很難區分：

$$
\text{More Permissive}
$$

與：

$$
\text{More Capable}.
$$

---

## 11. Domain Arbitrage Potential

本文提出概念性的 **Domain Arbitrage Potential**：

$$
A_D
=
\frac{
V_D
\cdot
\Delta_P(D)
\cdot
\Delta_{\text{spec}}(D)
\cdot
L_D
}{
C_{\text{train}}
+
C_{\text{infer}}
+
C_{\text{distribution}}
+
C_{\text{compliance}}
}.
$$

其中：

- $V_D$：領域需求與付費價值；
- $\Delta_P(D)$：政策缺口；
- $\Delta_{\text{spec}}(D)$：專門化增益；
- $L_D$：本地／隱私／控制價值；
- $C_{\text{train}}$：訓練成本；
- $C_{\text{infer}}$：推理成本；
- $C_{\text{distribution}}$：分發成本；
- $C_{\text{compliance}}$：法律、年齡治理、支付與安全成本。

這不是財務預測公式，而是比較領域機會的理論框架。

---

## 12. Policy Gap 同時也是摩擦來源

最危險的錯誤推論是：

$$
\text{Mainstream Refusal}
\Rightarrow
\text{Easy Money}.
$$

這不成立。

Stripe 目前的成人內容政策明確不支援色情與若干成人服務，也把符合相同條件的 AI-generated content 納入相關限制。

因此：

$$
\Delta_P(D)\uparrow
$$

可能同時伴隨：

$$
C_{\text{payment}}\uparrow.
$$

再加上不同司法轄區對年齡驗證、真人 likeness、deepfake、非自願私密影像與敏感資料處理具有不同要求，所以：

$$
\boxed{
\text{Opportunity}
=
\text{Gap}
-
\text{Friction}.
}
$$

Policy Gap 既是市場訊號，也是基礎設施退出的訊號。

---

## 13. Selective Domain Permissiveness

本文不把「無審查」視為理想技術終點。

更合理的是：

$$
\boxed{
\text{Domain-Bounded Freedom}.
}
$$

令合法成人親密域為 $D_L$，高傷害／不可接受域為 $D_H$。

則：

$$
P(a)=
\begin{cases}
1, & a\in D_L\text{ 且情境條件成立},\\
0, & a\in D_H.
\end{cases}
$$

真正的產品差異不是「什麼都做」，而是：

> 在合法垂直域中，比主流模型更懂、更穩、更持續、更私密，同時保留清楚硬邊界。

---

## 14. 從成人案例抽象到一般垂直 AI

成人／親密 AI 只是高對比案例。

相同結構也可以出現在：

$$
D_1=\text{Specialized Game Roleplay},
$$

$$
D_2=\text{Private Local Personal AI},
$$

$$
D_3=\text{Niche Professional Workflow},
$$

$$
D_4=\text{Historical Simulation},
$$

$$
D_5=\text{Creative Fiction Domain}.
$$

共同形式是：

$$
\boxed{
\text{Domain Opportunity}
=
\text{Specialized Utility}
+
\text{Access Gap}
+
\text{Deployment Advantage}.
}
$$

因此真正問題不是：

> 小模型能不能打贏大模型？

而是：

> 在什麼效用函數、政策域、成本、隱私與部署條件下，哪個系統位於真正的使用者前沿？

---

## 15. 可檢驗研究命題

### P1：Domain Frontier 與 Global Frontier 可分離

存在 $D,M_s,M_f$ 使：

$$
G(M_s)<G(M_f)
$$

同時：

$$
U_D(M_s)>U_D(M_f).
$$

### P2：Policy Shadow 可使較弱模型形成有效前沿

若：

$$
C_D(M_s)<C_D(M_f)
$$

但：

$$
\rho_D(M_s)\gg\rho_D(M_f),
$$

則可能有：

$$
E_D(M_s)>E_D(M_f).
$$

### P3：De-restriction 與 Specialization Gain 可被區分

對同一基座模型，降低拒答與領域微調應在 continuity、state tracking、context sensitivity 等 benchmark 上呈現不同增益模式。

### P4：System Runtime 可補償部分模型規模差距

加入持久記憶、關係狀態與世界狀態的中型模型，在長程角色任務中可能超過缺乏持久 runtime 的更大通用模型。

### P5：Local Privacy Premium 可反轉排序

當私人資料效用權重提高時，原本：

$$
M_1>M_2
$$

可能反轉為：

$$
U_D(M_2)>U_D(M_1).
$$

### P6：政策缺口可能被合規摩擦抵消

若：

$$
C_{\text{compliance}}
+
C_{\text{distribution}}
$$

成長速度高於缺口價值，則：

$$
A_D
$$

仍可能下降。

---

## 16. 結論

本文提出 Domain-Relative Frontier，用以修正「只有通用前沿模型才具有競爭價值」的單一路徑想像。

核心命題是：

$$
\boxed{
\text{Global Intelligence Frontier}
\neq
\text{Domain Utility Frontier}.
}
$$

一個中小型模型可能滿足：

$$
G(M_s)<G(M_f),
$$

卻在特定領域滿足：

$$
U_D(M_s)>U_D(M_f).
$$

成人／親密 AI 特別容易出現這種現象，因為它同時存在：

$$
\text{Domain Specialization}
+
\text{Policy Gap}
+
\text{Privacy Advantage}
+
\text{System-Level Augmentation}.
$$

但真正可持續的策略不是把「無審查」當作能力本身。

最終可寫成：

$$
\boxed{
F_D
=
f(
\text{Capability},
\text{Accessibility},
\text{Specialization},
\text{System},
\text{Privacy},
\text{Cost},
\text{Compliance}
).
}
$$

小公司真正值得追求的不是用有限資源複製整個 frontier foundation model，而是在合法且可持續的條件下，把一個足夠重要的垂直領域推到有效效用前沿。

下一篇將處理：

**Observation Data ≠ Interaction Experience：為什麼「看過」與「做過」不是同一種模型資料，以及政策如何造成互動軌跡截斷。**

---

## 參考資料

1. Cersosimo, D. (2026). *Democratizing AI with Small Language Models: Structured Benchmarking and Parameter-Efficient Fine-Tuning for Local Deployment*. arXiv:2607.16202.
2. Jiang, X. et al. (2026). *KOCO-BENCH: Can Large Language Models Leverage Domain Knowledge in Software Development?* arXiv:2601.13240.
3. Sinha, S. et al. (2026). *AutoAdapt: An Automated Domain Adaptation Framework for LLMs*. Microsoft Research / arXiv.
4. Grangier, D., Katharopoulos, A., Ablin, P., & Hannun, A. (2024). *Need a Small Specialized Language Model? Plan Early!* arXiv:2402.01093.
5. Google AI for Developers. (2026). *Gemini API Safety Settings*.
6. Google AI for Developers. (2026). *Gemini API Abuse Monitoring / Usage Policies*.
7. SpaceXAI. (2026). *FAQ - Grok Website / Apps*. Updated July 6, 2026.
8. Hugging Face. (2026). *Models tagged roleplay*. Dynamic model index.
9. Stripe. (2026). *Prohibited and Restricted Businesses / Adult Content FAQ*.

---

## 研究聲明

本文提出的 Domain-Relative Frontier、Policy Shadow、Effective Domain Capability 與 Domain Arbitrage Potential 均為理論性分析框架，不構成投資、法律或商業保證。本文不主張成人／親密 AI 必然具有較高收益，也不主張透過解除模型安全措施進入違法或高傷害領域。實際市場可行性取決於司法轄區、支付與分發基礎設施、年齡治理、資料治理、模型品質、使用者需求與持續合規成本。
