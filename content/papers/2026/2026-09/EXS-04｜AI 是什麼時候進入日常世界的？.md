# EXS-04｜AI 是什麼時候進入日常世界的？
## 手機、PC、汽車、家庭、醫療、工業與跨國 AI 滲透史

**系列：** Human Capability Externalization & Intelligence Substrate Evolution Series  
**系列中文名：** 人類能力外部化與智能載體演化系列  
**編號：** EXS-04  
**版本：** v1.0  
**日期：** 2026-08-18  
**狀態：** Canonical Source / UTF-8 Markdown  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

「AI 是什麼時候進入手機的？」「電腦什麼時候開始全面使用 AI？」「汽車從哪一年開始算 AI 汽車？」這些問題看似可以用一個年份回答，實際上卻包含多種不同歷史事件。早期語音辨識、推薦、影像處理、預測文字與機器學習功能，往往在消費者未明確感知「AI」之前已經進入產品；而一項產品被市場宣傳為「AI 裝置」之後，也不代表 AI 已成為其預設架構，更不代表失去 AI 後該產品就無法維持核心功能。

本文因此提出「AI 滲透的多階段時間型別」，將單一的「AI 出現時間」拆分為：

$$
T_{\mathrm{first}},
T_{\mathrm{consumer}},
T_{\mathrm{mass}},
T_{\mathrm{default}},
T_{\mathrm{dependent}}.
$$

其中分別表示：首次可識別導入、消費者可見、大規模普及、預設整合，以及功能依賴。本文進一步提出 $L_0$ 至 $L_7$ 的 AI 滲透層級，從「無 AI」一路區分到「AI 成為基礎設施層」。這套框架可跨手機、PC、汽車、智慧家庭、醫療、工業與公共服務使用，也能避免把「有一個 AI 功能」錯當成「整個系統已 AI 原生化」。

歷史實證部分以 2011 年 iPhone 4S 的 Siri 作為「消費者可見 AI 助手」的重要里程碑，而不將其錯稱為世界第一個手機 AI；以 2014 年 Amazon Echo / Alexa 作為智慧家庭語音代理大眾化的重要節點；以 2024 年 Apple Intelligence、Galaxy AI 與 Copilot+ PC 類別，以及 2025 年 Google 宣布以 Gemini 升級手機端 Google Assistant，觀察 AI 從應用功能走向作業系統與硬體架構層；汽車則透過 SAE Level 3 條件自動駕駛與車載 AI 的發展，展示「輔助功能」與「部分動態駕駛任務委託」之間的型別差異；醫療則以 FDA 的 AI-enabled medical device 清單與生命周期治理為例；工業則以 Siemens Industrial Copilot 等系統展示生成式 AI 進入工程與製造流程的過渡。

本文亦處理跨國比較方法。2025 年 Eurostat 顯示 EU 企業 AI 使用率在國家間有顯著差異；2026 年美國 Census BTOS 顯示 AI 使用又受到企業規模與產業高度影響；中國 2026 年政策已把 AI 手機、AI PC、智慧家庭、工業智能體與具身智能視為通信與產業融合方向；台灣 2026 年調查則顯示製造與非製造業的 AI 導入、評估與規劃已具有相當廣度。這些資料不能直接以單一百分比排序，因為其分母、問題、調查期間與「使用」定義不同。

本文的核心結論是：不存在一個普遍有效的「人類在某一年進入 AI 時代」。更準確的描述應是：

$$
\boxed{
\text{AI penetration is a multi-stage, multi-domain, multi-region process}.
}
$$

真正需要追蹤的不是「AI 有沒有」，而是：哪一個功能域、哪一個地區、哪一類使用者，在什麼時點跨過了什麼程度的 AI 中介與依賴門檻。

---

## 關鍵詞

AI 滲透史；AI 手機；AI PC；Siri；Gemini；Apple Intelligence；Galaxy AI；Copilot+ PC；智慧家庭；自動駕駛；AI 醫療；工業 AI；AI adoption；跨國比較；AI 基礎設施

---

# 1. 問題：AI 到底是哪一天「進入日常生活」？

直覺上，人們喜歡問：

> AI 是從哪一年開始進入手機的？

但這個問題沒有唯一答案。

因為「進入」至少可以表示：

1. 某個產品第一次內部使用機器學習；
2. 使用者第一次直接與 AI 互動；
3. 大量使用者開始普遍接觸；
4. AI 成為裝置的預設系統層；
5. 移除 AI 後，裝置的主要功能顯著退化。

因此：

$$
\boxed{
T_{\mathrm{AI}}
\neq
\text{single universal date}.
}
$$

若沒有先做時間型別，就很容易產生錯誤敘事。

---

# 2. 五個 AI 滲透時間型別

本文定義：

## 2.1 首次可識別導入

$$
T_{\mathrm{first}}
$$

表示在合理技術定義下，AI 或機器學習第一次可被確認用於該領域。

這個時間點往往：

- 很早；
- 很難唯一化；
- 依 AI 定義改變；
- 可能只有實驗或小規模產品。

因此它最適合技術史，不適合直接代表社會普及。

---

## 2.2 消費者可見

$$
T_{\mathrm{consumer}}
$$

表示一般使用者開始直接把某個功能認識為：

$$
\text{AI-like intelligence}.
$$

例如：

- 語音助手；
- 自動駕駛；
- 生成式文字；
- AI 修圖；
- 智慧家庭助理。

這個時間點往往與品牌、介面與媒體敘事高度相關。

---

## 2.3 大規模普及

$$
T_{\mathrm{mass}}
$$

表示該 AI 能力已不再只是少數實驗者或旗艦產品使用，而成為大量人口、設備或企業可接觸的常見能力。

---

## 2.4 預設整合

$$
T_{\mathrm{default}}
$$

表示使用者取得新裝置或新系統時：

$$
\boxed{
AI
}
$$

已經不是額外安裝的選配，而是：

$$
\boxed{
\text{default system capability}.
}
$$

---

## 2.5 功能依賴

$$
T_{\mathrm{dependent}}
$$

表示移除 AI 後：

$$
\text{Core System Performance}
\downarrow\downarrow
$$

或某些核心服務難以維持原有運作方式。

這是最晚、也最重要的社會依賴門檻。

因此：

$$
\boxed{
T_{\mathrm{first}}
\neq
T_{\mathrm{consumer}}
\neq
T_{\mathrm{mass}}
\neq
T_{\mathrm{default}}
\neq
T_{\mathrm{dependent}}.
}
$$

---

# 3. 為什麼「第一個 AI 手機」是一個危險問題？

如果 AI 定義很寬，則：

- predictive text；
- speech recognition；
- camera scene classification；
- spam filtering；
- recommendation；
- face detection；

都可能算 AI。

於是「第一個 AI 手機」會隨定義改變。

因此本文拒絕：

$$
\boxed{
\text{One Device}
=
\text{Absolute First AI Phone}
}
$$

式敘事。

更合理的是：

$$
\boxed{
\text{Milestone-by-function}.
}
$$

也就是問：

- 第一個大眾語音助手里程碑？
- 第一個生成式 AI 系統層里程碑？
- 第一個 NPU 成為裝置分類條件的里程碑？
- 第一個 AI 成為預設 OS 層的里程碑？

---

# 4. Siri：不是「第一個手機 AI」，而是極強的消費者可見節點

2011 年 10 月，Apple 在 iPhone 4S 上推出 Siri，並明確稱其為：

$$
\text{intelligent assistant}.
$$

iPhone 4S 首週末銷量超過 400 萬台。[1]

因此 Siri 的歷史重要性不是：

$$
\boxed{
\text{Siri}
=
\text{first AI ever on a phone}.
}
$$

而更接近：

$$
\boxed{
T_{\mathrm{consumer}}^{\mathrm{mobile\ assistant}}
\approx
2011
}
$$

的一個全球性大眾市場里程碑。

使用者第一次大規模被教導：

> 你可以直接對手機說話，手機裡有一個「助理」會理解並幫你做事。

這是一個重要的人機介面變化。

---

# 5. Siri 的意義是「AI 被人格化成介面」

傳統手機功能多數是：

$$
\text{Menu}
\rightarrow
\text{Function}.
$$

Siri 代表另一個模式：

$$
\boxed{
\text{Natural Language}
\rightarrow
\text{Assistant}
\rightarrow
\text{Function}.
}
$$

也就是：

$$
\text{function-centric UI}
$$

開始部分轉向：

$$
\text{agent-like UI}.
$$

這不代表 Siri 已經是現代 agent。

但它改變了使用者對：

$$
\text{what a phone interface can be}
$$

的預期。

---

# 6. 2014：智慧家庭中的「AI 介面」進入房間

Amazon Echo 於 2014 年推出，Amazon 將其描述為開創智慧喇叭這個新產品類別；Alexa 也自 2014 年起成為其語音互動核心。[2]

其歷史意義在於：

$$
\boxed{
\text{AI-like assistant}
}
$$

不再被綁在：

$$
\boxed{
\text{screen-first device}.
}
$$

而開始變成：

$$
\boxed{
\text{ambient interface}.
}
$$

即：

> 你不必拿起裝置，直接對環境說話。

因此可以定義：

$$
T_{\mathrm{consumer}}^{\mathrm{ambient\ assistant}}
\approx
2014.
$$

---

# 7. 從智慧喇叭到智慧家庭：裝置開始互相被 AI 中介

單一智慧喇叭只是：

$$
A
\rightarrow
\text{speaker}.
$$

但當它連接：

- 燈；
- 門鎖；
- 溫控；
- 攝影機；
- 電視；
- 音樂；
- 日曆；
- 購物；

就形成：

$$
\boxed{
A
\rightarrow
\{D_1,D_2,\ldots,D_n\}.
}
$$

這代表 AI 助手的功能開始由：

$$
\text{Answering}
$$

轉向：

$$
\text{Mediating Environment}.
$$

2025 年 Google 宣布 Gemini for Home 將取代既有 Google Assistant 於智慧喇叭與顯示器，並把攝影機、門鈴與 Google Home app 納入更高階的自然語言與協作式 AI 體驗。[3]

這正是：

$$
\boxed{
\text{AI Assistant}
\rightarrow
\text{Home Intelligence Layer}.
}
$$

---

# 8. 手機第二次質變：AI 從「一個助理」走向「系統層」

2011 年 Siri 可以被理解為：

$$
\text{phone}
+
\text{AI assistant}.
$$

但 2024 年以後，手機開始朝另一種架構移動：

$$
\boxed{
\text{phone OS}
\supset
\text{AI layer}.
}
$$

2024 年，Apple 發表 Apple Intelligence，明確稱其為 iPhone、iPad 與 Mac 的 personal intelligence system，並將其深度整合進 iOS、iPadOS 與 macOS。[4]

同年，Samsung 以 Galaxy S24 推出 Galaxy AI，並在後續將其擴散至更多 Galaxy 裝置。[5]

Google 則把 Gemini 模型與 Android 作業系統層逐步整合，包含 on-device Gemini Nano 與 AICore。[6]

因此：

$$
\boxed{
T_{\mathrm{default}}
}
$$

開始成為比：

$$
T_{\mathrm{consumer}}
$$

更值得研究的手機指標。

---

# 9. 2025：Google Assistant 升級為 Gemini 的象徵意義

2025 年 3 月，Google 宣布將手機端 Google Assistant 使用者逐步升級至 Gemini。[7]

這不是簡單的：

$$
\text{App A}
\rightarrow
\text{App B}.
$$

它更接近：

$$
\boxed{
\text{legacy voice assistant}
\rightarrow
\text{general multimodal AI assistant}.
}
$$

因為 Gemini 不只：

- 回答單一指令；
- 開 app；
- 設鬧鐘；

還朝：

- 長上下文；
- 多模態；
- 跨 app；
- 推理；
- agentic task execution；

發展。

因此手機的 AI 歷史可以分成：

$$
\boxed{
\text{Feature AI}
\rightarrow
\text{Assistant AI}
\rightarrow
\text{System AI}
\rightarrow
\text{Agentic AI}.
}
$$

---

# 10. 2026：手機 AI 已開始成為跨裝置個人智能層

2026 年，Apple 宣布新一代 Apple Intelligence 與 Siri AI，Google 亦持續把 Gemini 往 proactive、agentic 與跨應用方向推進。[8][9]

但本文必須做一個時間型別區分：

$$
\boxed{
\text{Announced}
\neq
\text{Generally Available}
\neq
\text{Default for All Users}.
}
$$

例如 Apple 2026 年公布的 Siri AI 仍存在 beta、語言與區域推出時程差異。[8]

因此：

$$
T_{\mathrm{announcement}}
$$

不可直接當成：

$$
T_{\mathrm{mass}}.
$$

這是 AI 滲透史研究必須嚴格遵守的規則。

---

# 11. AI PC：什麼時候可以說「電腦是為 AI 而設計」？

PC 更難判斷。

因為個人電腦早就可以：

- 執行 ML；
- 使用雲端 AI；
- 呼叫 AI API；
- 安裝模型。

所以：

$$
\boxed{
\text{PC capable of AI}
}
$$

早於：

$$
\boxed{
\text{AI-native PC architecture}.
}
$$

2024 年 Microsoft 正式推出 Copilot+ PC 類別，將至少 $40+$ TOPS NPU 作為新一代 Windows AI PC 的核心能力條件之一。[10]

這是重要的硬體分界。

---

# 12. NPU 的歷史意義不是「CPU 不能跑 AI」

需要避免：

$$
\boxed{
\text{No NPU}
\Rightarrow
\text{No AI}.
}
$$

這是錯的。

CPU、GPU 早就可以跑 AI。

NPU 的真正意義是：

$$
\boxed{
\text{persistent local AI workload}
}
$$

開始值得一個專門的硬體加速層。

因此：

$$
\boxed{
\text{AI Software on PC}
\rightarrow
\text{PC Designed Around AI Workloads}.
}
$$

這比「某台 PC 第一次用了 AI」更精確。

---

# 13. PC 的五個時間點也不會重合

對 PC，可以分成：

$$
T_{\mathrm{AI\ software}},
$$

$$
T_{\mathrm{cloud\ assistant}},
$$

$$
T_{\mathrm{local\ accelerator}},
$$

$$
T_{\mathrm{OS\ integration}},
$$

$$
T_{\mathrm{AI\ dependency}}.
$$

到 2026 年：

$$
T_{\mathrm{local\ accelerator}}
$$

與：

$$
T_{\mathrm{OS\ integration}}
$$

已經非常清楚地出現。

但：

$$
T_{\mathrm{AI\ dependency}}
$$

是否已在整個 PC 生態成立，仍然不能一概而論。

大量 PC 移除生成式 AI 後仍能執行其核心傳統功能。

因此：

$$
\boxed{
\text{AI-default}
\neq
\text{AI-dependent}.
}
$$

---

# 14. 汽車：AI 不是從「自動駕駛」才開始

汽車早已使用：

- 感測；
- 控制；
- 電子穩定；
- 駕駛輔助；
- 路徑規劃；
- 物體辨識；
- 語音介面。

所以「第一台 AI 汽車」同樣缺乏穩定定義。

更好的問題是：

$$
\boxed{
\text{Which driving function crossed which automation threshold?}
}
$$

---

# 15. 駕駛輔助與駕駛任務委託不是同一件事

本文區分：

$$
\text{Driver Assistance}
$$

與：

$$
\text{Conditional Automated Driving}.
$$

Mercedes-Benz DRIVE PILOT 已取得 SAE Level 3 條件自動駕駛相關許可，在特定條件下由系統接手部分 dynamic driving task，而駕駛仍須在系統要求時接管。[11]

因此：

$$
\boxed{
\text{AI assists driver}
\neq
\text{system assumes dynamic driving task}.
}
$$

這個型別差異對汽車 AI 滲透史比品牌名稱重要。

---

# 16. 2024–2026 的車輛 AI 正從控制功能走向「車載智能層」

汽車也開始出現：

$$
\text{vehicle}
+
\text{general AI assistant}
$$

的融合。

Google 於 2025 年把 Gemini 推向 Android Auto，使其可透過自然語言處理導航、訊息、郵件、播放清單等車載任務。[12]

Mercedes-Benz 等車廠也持續把生成式 AI 與車載語音系統整合。

因此汽車 AI 可以分成：

$$
\boxed{
\text{Perception AI}
+
\text{Driving AI}
+
\text{Cabin AI}
+
\text{Vehicle Agent}.
}
$$

不能用一個「有／沒有 AI」二元變量概括。

---

# 17. 汽車 AI 的依賴門檻會比手機更嚴格

手機 AI 出錯：

$$
\text{wrong summary}
$$

可能只是資訊風險。

汽車感知或控制 AI 出錯：

$$
\text{wrong physical action}
$$

可能直接變成安全風險。

因此：

$$
\boxed{
T_{\mathrm{dependent}}^{\mathrm{car}}
}
$$

不能只由市場普及決定。

還受到：

- 法規；
- 驗證；
- 故障安全；
- 接管；
- 責任；
- 運行設計域；

約束。

所以：

$$
\boxed{
\text{AI Penetration}
\neq
\text{Permission to Delegate}.
}
$$

---

# 18. 醫療：AI 進入的不是「裝置」，而是高責任決策鏈

醫療 AI 是另一種滲透型態。

FDA 已建立 AI-Enabled Medical Device List，用於識別已獲准在美國市場銷售的 AI-enabled medical devices。[13]

2025 年 FDA 更表示，透過既有 premarket pathways 已授權超過 $1,000$ 個 AI-enabled devices。[14]

這證明：

$$
\boxed{
AI
}
$$

已不是醫療裝置領域的純研究概念。

但：

$$
\boxed{
\text{authorized device count}
\neq
\text{clinical dependency}.
}
$$

---

# 19. 醫療 AI 的時間型別必須加入「監管進入」

對醫療，可增加：

$$
T_{\mathrm{reg}}
=
\text{regulatory entry}.
$$

因此：

$$
T_{\mathrm{first}}
$$

可能是研究論文。

$$
T_{\mathrm{reg}}
$$

是獲得監管許可。

$$
T_{\mathrm{clinical}}
$$

是醫療流程實際使用。

$$
T_{\mathrm{dependent}}
$$

則是：

> 醫療系統已難以在同樣服務水準下不使用 AI。

這四個時間點可以相差很多年。

---

# 20. AI 醫療也展示「使用 AI」不等於「把最終責任交給 AI」

FDA、Health Canada 與英國 MHRA 的 machine-learning-enabled medical device transparency principles 特別強調 human-AI team 的表現與向使用者提供清楚資訊。[15]

因此醫療中：

$$
\boxed{
\text{AI Inference}
\neq
\text{Automatic Final Authority}.
}
$$

AI 可以進入決策鏈，而最終責任結構仍可能保留在人類與制度上。

這對後續「AI 中介文明」研究非常重要。

---

# 21. 工業：AI 滲透可能比消費者看見的更深

一般人容易從：

- ChatGPT；
- Siri；
- Gemini；
- Galaxy AI；

理解 AI。

但工業 AI 可能：

$$
\boxed{
\text{low consumer visibility}
+
\text{high operational impact}.
}
$$

2024 年 Siemens 與 Microsoft 表示，Siemens Industrial Copilot 已被歐洲與美國超過 100 個客戶使用，並將其推向工業自動化與工程工作流程；Siemens 亦表示可有超過 120,000 名工程師透過 TIA Portal 使用相關能力。[16]

因此：

$$
\boxed{
\text{Consumer Visibility}
\neq
\text{Industrial Penetration}.
}
$$

---

# 22. 工業 AI 的真正門檻不是「工人有沒有聊天機器人」

工業 AI 可以進入：

- PLC 程式；
- 視覺檢測；
- 預測維修；
- 排程；
- 數位孿生；
- 品質控制；
- 工程設計；
- 機器人控制；
- 供應鏈。

所以更應該研究：

$$
\boxed{
\text{AI share of industrial control and decision loops}.
}
$$

而不是：

$$
\boxed{
\text{number of employees who opened an AI chatbot}.
}
$$

---

# 23. 工業 AI 與 AI Agent 的界線正在靠近

若 Industrial Copilot 只是：

> 幫工程師查文件。

它是：

$$
L_1.
$$

若它開始：

> 生成控制程式。

可能到：

$$
L_2-L_3.
$$

若它：

> 監控產線並推薦修正。

可能到：

$$
L_4.
$$

若它可以：

> 自主執行長鏈修正與調度。

則接近：

$$
L_5.
$$

因此：

$$
\boxed{
\text{Same Product Name}
\not\Rightarrow
\text{Same Penetration Level}.
}
$$

---

# 24. AI 滲透層級： $L_0$ 到 $L_7$

本文建立一個跨領域的初步尺度。

## $L_0$：No AI

$$
\boxed{
L_0=\text{No identifiable AI function}.
}
$$

主要依賴機械、固定規則或傳統非 AI 程式。

---

## $L_1$：AI-Assisted

$$
\boxed{
L_1=\text{AI as optional assistance}.
}
$$

移除後：

$$
\text{system remains largely intact}.
$$

---

## $L_2$：AI-Embedded

$$
\boxed{
L_2=\text{AI embedded in product functions}.
}
$$

AI 已內建，但不是核心控制層。

---

## $L_3$：AI-Dependent Feature Layer

$$
\boxed{
L_3=\text{important features depend on AI}.
}
$$

移除 AI 後部分重要功能消失，但系統本體仍可運作。

---

## $L_4$：AI-Mediated

$$
\boxed{
L_4=\text{AI mediates substantial decisions or interactions}.
}
$$

AI 開始決定：

- 排序；
- 推薦；
- 調度；
- 風險判斷；
- 人機介面。

---

## $L_5$：AI-Agentic

$$
\boxed{
L_5=\text{AI executes multi-step goal-directed processes}.
}
$$

AI 不只回應，而能維持任務狀態與行動鏈。

---

## $L_6$：AI-Native

$$
\boxed{
L_6=\text{system designed around AI as a primary operating layer}.
}
$$

AI 不是加上去，而是設計起點。

---

## $L_7$：AI-Infrastructural

$$
\boxed{
L_7=\text{civilizational domain depends structurally on AI}.
}
$$

移除 AI 會造成：

$$
\boxed{
\text{large-scale domain degradation}.
}
$$

這一層與 EXS-02 的「能力環境」直接接軌。

---

# 25. $L_0$ 到 $L_7$ 不是產品評分

需要明確聲明：

$$
\boxed{
L_7
\neq
\text{better than }L_6.
}
$$

這不是：

$$
\text{quality score}.
$$

而是：

$$
\boxed{
\text{penetration/dependency topology}.
}
$$

某些高風險系統可能刻意維持：

$$
L_2
$$

而拒絕：

$$
L_5.
$$

這可能是安全設計，而不是落後。

---

# 26. 同一台裝置可以同時有多個 AI 層級

一台手機：

$$
\text{camera}
=
L_3,
$$

$$
\text{voice assistant}
=
L_4,
$$

$$
\text{agent}
=
L_5,
$$

$$
\text{emergency calling}
=
L_0.
$$

因此：

$$
\boxed{
L(\text{device})
}
$$

不一定有單一值。

更合理的是：

$$
\boxed{
\mathbf L_D
=
(
L_{f_1},
L_{f_2},
\ldots,
L_{f_n}
).
}
$$

也就是：

$$
\boxed{
\text{AI Penetration Profile}.
}
$$

---

# 27. AI 手機也應該看「功能剖面」而不是品牌名稱

假設手機 $P$：

$$
\mathbf L_P
=
(
L_{\mathrm{camera}},
L_{\mathrm{assistant}},
L_{\mathrm{security}},
L_{\mathrm{search}},
L_{\mathrm{editing}},
L_{\mathrm{agent}}
).
$$

兩台都宣稱：

$$
\text{AI Phone},
$$

但：

$$
\mathbf L_{P_1}
\neq
\mathbf L_{P_2}.
$$

所以：

$$
\boxed{
\text{Marketing Category}
\neq
\text{Functional Penetration Profile}.
}
$$

Samsung 後來把 Galaxy S24 稱為「world's first AI phone」，這可以被記錄為企業自身的產品敘事，但不宜用來取代嚴格技術史上的「第一」判定。[17]

---

# 28. 「預設 AI」是一個真正重要的社會門檻

當：

$$
AI
$$

需要使用者：

> 主動搜尋、下載、註冊、學習。

它仍然主要是：

$$
\text{adopted technology}.
$$

當：

$$
AI
$$

直接存在於：

- OS；
- 搜尋；
- 鍵盤；
- 相機；
- 瀏覽器；
- 語音；
- 通知；
- App actions；

則：

$$
\boxed{
\text{AI}
\rightarrow
\text{default environment}.
}
$$

此時：

$$
T_{\mathrm{default}}
$$

的文明意義可能大於：

$$
T_{\mathrm{first}}.
$$

---

# 29. 為什麼 AI 滲透必須按國家／區域研究？

因為：

$$
\boxed{
T(c_1)
\neq
T(c_2).
}
$$

差異來源包括：

- 收入；
- 裝置更新率；
- 雲端基礎設施；
- 語言支援；
- 法規；
- 隱私；
- 產業結構；
- 晶片供應；
- 網路；
- 教育；
- 企業規模；
- 國家政策。

因此「2026 年已進入 AI 時代」是一個低精度句子。

更準確的是：

$$
\boxed{
L(c,d,t)
}
$$

其中：

$$
c=\text{country/region},
$$

$$
d=\text{domain},
$$

$$
t=\text{time}.
$$

---

# 30. EU：同一政治經濟區內就已有巨大滲透差異

Eurostat 2026 edition 顯示，2025 年 EU 約 $20\%$ 的企業使用 AI 技術，但國家間差異顯著：丹麥約 $42\%$，芬蘭約 $38\%$，瑞典與比利時約 $35\%$ ；羅馬尼亞約 $5\%$，波蘭約 $8\%$。[18]

因此：

$$
\boxed{
\text{Same Regulatory Union}
\neq
\text{Same AI Penetration}.
}
$$

企業規模差異也非常大：

$$
\text{large firms}
>
\text{SMEs}.
$$

2025 年 EU 大型企業 AI 使用率約 $55\%$，SMEs 約 $19\%$。[18]

所以：

$$
\boxed{
L(c,d,t)
}
$$

還應加入：

$$
s=\text{firm size}.
$$

---

# 31. 美國：AI 使用率不是一條整齊的全社會曲線

美國 Census Bureau 2026 年 BTOS 顯示，2025 年 12 月至 2026 年 5 月間，整體企業 AI 使用率約在 $17\%-20\%$ 之間；至少 250 名員工的企業約 $37\%$ 使用 AI，資訊業與金融保險業則顯著高於整體平均。[19]

因此：

$$
\boxed{
\text{National AI Adoption}
}
$$

其實是：

$$
\boxed{
\sum
\text{sector-specific diffusion curves}.
}
$$

不是一條單一 S-curve 就能完整表示。

---

# 32. 中國：AI 終端已被直接寫入產業與通信融合政策

中國工業和信息化部 2026–2028 年「人工智能+信息通信」相關政策明確提出：

- AI 手機；
- AI 電腦；
- 智慧家庭設備；
- 智慧穿戴；
- 具身智能；
- 工業智能體；
- 智慧交通；
- 工業視覺檢測；

等融合方向。[20]

這表示：

$$
\boxed{
\text{AI Penetration}
}
$$

在中國已不只是單一企業產品策略，也被放入：

$$
\boxed{
\text{national infrastructure/industry planning}.
}
$$

但：

$$
\boxed{
\text{Policy Target}
\neq
\text{Observed Adoption}.
}
$$

因此不能用政策文件直接當作實際滲透率。

---

# 33. 台灣：導入、評估、規劃不能直接等於「已使用」

2026 上半年台灣採購經理人營運展望調查顯示，製造業約 $69.0\%$ 的受訪企業表示已導入、評估或規劃 AI；非製造業約 $60.4\%$ 落在相同廣義範圍。[21]

這個數字很高，但它的問題定義是：

$$
\boxed{
\text{adopted}
+
\text{evaluating}
+
\text{planning}.
}
$$

所以不能拿來和 Eurostat：

$$
\text{used AI in 2025}
$$

或 Census：

$$
\text{used AI in past two weeks}
$$

直接排序。

這正是本文主張跨國研究必須先做：

$$
\boxed{
\text{Measurement Type Safety}.
}
$$

---

# 34. 跨國 AI 百分比最常見的錯誤：分母根本不一樣

假設：

$$
A=60\%,
$$

$$
B=20\%.
$$

如果 $A$ 問：

> 已導入、評估或規劃嗎？

而 $B$ 問：

> 過去兩週實際用了嗎？

則：

$$
\boxed{
A>B
}
$$

不能推出：

$$
\boxed{
\text{Country A is more AI-penetrated than Country B}.
}
$$

因此跨國比較至少必須控制：

$$
\boxed{
\text{definition}
+
\text{denominator}
+
\text{time window}
+
\text{firm size}
+
\text{sector}.
}
$$

---

# 35. 本文提出 AI 滲透資料的五種測量型別

## $M_1$：Access

$$
\text{Can users access AI?}
$$

## $M_2$：Use

$$
\text{Do users actually use AI?}
$$

## $M_3$：Frequency

$$
\text{How often?}
$$

## $M_4$：Workflow Integration

$$
\text{Is AI embedded in routine workflows?}
$$

## $M_5$：Dependency

$$
\text{What happens if AI disappears?}
$$

因此：

$$
\boxed{
M_1
\neq
M_2
\neq
M_3
\neq
M_4
\neq
M_5.
}
$$

---

# 36. AI 的真正日常化可能發生在「使用者不再感覺自己正在使用 AI」

早期：

> 我打開 AI app。

中期：

> 手機幫我修圖。

再後來：

> 相機就是這樣。

這表示：

$$
\boxed{
\text{AI Visibility}
}
$$

可能隨滲透加深反而下降。

定義：

$$
V_{\mathrm{AI}}
=
\text{degree to which user consciously identifies AI mediation}.
$$

則某些技術路徑可能是：

$$
L\uparrow,
\qquad
V_{\mathrm{AI}}\downarrow.
$$

這正像電力與網路。

真正基礎設施化的技術往往：

$$
\boxed{
\text{becomes less noticeable when it works}.
}
$$

---

# 37. 因此「AI 無所不在」不等於到處看到機器人

如果：

$$
P(
\text{ordinary action intersects AI-mediated system}
)
\rightarrow1,
$$

即使使用者：

- 沒看到機器人；
- 沒開 chatbot；
- 沒有說「我在用 AI」；

仍可能生活在：

$$
\boxed{
\text{Pervasive AI-Mediated Environment}.
}
$$

例如：

- 搜尋排序；
- 垃圾郵件；
- 物流；
- 風控；
- 交通；
- 醫療影像；
- 雲端；
- 資安；
- 廣告；
- 供應鏈；

都可能包含 AI。

所以：

$$
\boxed{
\text{Pervasiveness}
\neq
\text{Visual Presence}.
}
$$

---

# 38. 嵌入式 AI 是下一個重要分支

當 AI 位於：

- 感測器；
- 微控制器；
- 邊緣裝置；
- 穿戴；
- 家電；
- 車輛；
- 工業設備；

其典型特徵是：

$$
\boxed{
\text{AI function}
}
$$

可能沒有獨立介面。

這種：

$$
\boxed{
\text{Embedded AI}
}
$$

會使「AI 裝置數量」研究比「AI app 使用率」更難。

因為：

$$
\text{one device}
$$

可能內含：

$$
n
$$

個不同模型與 AI 功能。

---

# 39. AI 數量也不是這篇的核心變量

如果：

$$
N_{AI}
$$

很大，但全部只是微小、低影響的分類器，

而另一個系統只有：

$$
1
$$

個 AI，卻控制：

- 電網；
- 金融；
- 物流；

則治理與文明影響可能完全相反。

因此：

$$
\boxed{
N_{AI}
\neq
\text{AI Penetration Depth}.
}
$$

這個問題會在第二系列「AI 人口與域治理」正式展開。

---

# 40. AI 滲透研究需要「功能域」而不只是裝置類別

本文建議研究：

$$
D
=
\{
d_1,d_2,\ldots,d_n
\}
$$

其中功能域至少包括：

- communication；
- search；
- navigation；
- transport；
- finance；
- healthcare；
- manufacturing；
- education；
- entertainment；
- government；
- energy；
- logistics；
- security；
- home；
- personal computing。

每一域估計：

$$
L(c,d,t).
$$

這比：

> 一個國家有多少 AI 手機？

更接近真正的文明 AI 化程度。

---

# 41. 國家 AI 滲透狀態向量

對國家或區域 $c$，定義：

$$
\boxed{
\mathbf A_c(t)
=
(
L_{\mathrm{phone}},
L_{\mathrm{PC}},
L_{\mathrm{car}},
L_{\mathrm{home}},
L_{\mathrm{health}},
L_{\mathrm{industry}},
L_{\mathrm{finance}},
L_{\mathrm{government}},
\ldots
).
}
$$

這可稱為：

$$
\boxed{
\text{AI Civilizational Penetration State}.
}
$$

它不是把文明壓成單一排行榜。

而是允許：

$$
\mathbf A_A
\neq
\mathbf A_B
$$

且兩國各自在不同領域領先。

---

# 42. 城市與鄉村也不應被國家平均值蓋掉

假設：

$$
L_{\mathrm{urban}}
\gg
L_{\mathrm{rural}}.
$$

國家平均：

$$
\bar L
$$

可能掩蓋巨大差異。

因此更完整的座標應為：

$$
L(
c,
r,
d,
s,
t
),
$$

其中：

$$
r=\text{region},
$$

$$
s=\text{socioeconomic / firm-size stratum}.
$$

這會使 AI 滲透研究從「科技史」進入：

$$
\boxed{
\text{civilizational geography}.
}
$$

---

# 43. AI 滲透不是單向、不可逆

即使：

$$
L(t)=5,
$$

也不代表：

$$
L(t+1)\geq5.
$$

法規、事故、市場失敗、供應鏈、戰爭、能源、成本、社會拒絕都可能導致：

$$
L(t+1)<L(t).
$$

因此：

$$
\boxed{
\text{Penetration}
\neq
\text{Monotonic Progress}.
}
$$

這是後續政治經濟與治理研究的重要限制。

---

# 44. 但基礎設施化之後，回退成本會增加

結合 EXS-02：

$$
L
\uparrow
$$

若同時：

$$
D_{\mathrm{cap}}
\uparrow,
$$

則：

$$
\text{Rollback Cost}
\uparrow.
$$

因此：

$$
\boxed{
\text{AI Penetration}
+
\text{Dependency Depth}
}
$$

才真正決定：

$$
\boxed{
\text{how reversible AI integration is}.
}
$$

這將在第二系列「AI Capital Lock-In」與「凍結 AI 的博弈」中繼續展開。

---

# 45. AI 滲透與 AI 主體性必須徹底分離

本文所有：

$$
L_0-L_7
$$

都可以在：

$$
\boxed{
\text{AI has no subjectivity}
}
$$

的假設下成立。

所以：

$$
\boxed{
\text{AI Penetration}
\neq
\text{AI Subjectivity}.
}
$$

一個完全沒有主體性的 AI 系統，也可能：

$$
L_7.
$$

反之，一個未來可能具有主體性的 AI 個體，也可能只處於：

$$
L_1
$$

的社會功能位置。

這兩條軸不能混。

---

# 46. AI 滲透與人類控制力也不是同一條軸

假設：

$$
L\uparrow.
$$

不一定：

$$
H_{\mathrm{control}}\downarrow.
$$

因為高 AI 滲透系統可以同時具有：

- 審計；
- 人類覆核；
- 權限分離；
- kill switch；
- fallback；
- 多模型；
- 法律責任；
- 透明介面。

反之：

$$
L_2
$$

的單一黑箱系統也可能具有很高治理風險。

所以：

$$
\boxed{
\text{Penetration Depth}
\neq
\text{Governance Quality}.
}
$$

---

# 47. 核心命題

本文提出以下十四個核心命題。

## 命題 1：AI 進入某領域沒有唯一日期

$$
\boxed{
T_{\mathrm{AI}}
\neq
\text{single date}.
}
$$

---

## 命題 2：首次出現與大眾普及不可混同

$$
\boxed{
T_{\mathrm{first}}
\neq
T_{\mathrm{mass}}.
}
$$

---

## 命題 3：消費者可見與系統依賴不可混同

$$
\boxed{
T_{\mathrm{consumer}}
\neq
T_{\mathrm{dependent}}.
}
$$

---

## 命題 4：預設整合是重要中介門檻

$$
\boxed{
T_{\mathrm{default}}
}
$$

應獨立測量。

---

## 命題 5：AI 裝置不是二元分類

$$
\boxed{
\text{AI Device}
\notin
\{0,1\}
}
$$

更適合描述為功能剖面。

---

## 命題 6：同一裝置可同時跨多個 AI 滲透層級

$$
\boxed{
\mathbf L_D
=
(
L_{f_1},\ldots,L_{f_n}
).
}
$$

---

## 命題 7：AI 使用率不等於 AI 依賴度

$$
\boxed{
M_2
\neq
M_5.
}
$$

---

## 命題 8：消費者可見度不等於文明影響

$$
\boxed{
V_{\mathrm{AI}}
\neq
I_{\mathrm{civilization}}.
}
$$

---

## 命題 9：AI 日常化可能伴隨 AI 可見度下降

$$
\boxed{
L\uparrow
\land
V_{\mathrm{AI}}\downarrow
}
$$

可以同時成立。

---

## 命題 10：AI 滲透必須按領域、地區與群體分解

$$
\boxed{
L=L(c,r,d,s,t).
}
$$

---

## 命題 11：跨國 AI 百分比必須先做 measurement type safety

$$
\boxed{
\text{Different Survey Definitions}
\not\Rightarrow
\text{Direct Rankability}.
}
$$

---

## 命題 12：AI 滲透不必是單調的

$$
\boxed{
L(t+1)
\not\geq
L(t)
}
$$

並非必然。

---

## 命題 13：AI 滲透不等於 AI 主體性

$$
\boxed{
\text{Penetration}
\neq
\text{Subjecthood}.
}
$$

---

## 命題 14：AI 滲透也不等於治理失敗

$$
\boxed{
\text{High Penetration}
\neq
\text{Low Human Governance}.
}
$$

---

# 48. 可檢驗研究計畫

## 48.1 手機 AI 五時間點資料庫

對：

- Apple；
- Google；
- Samsung；
- Huawei；
- Xiaomi；
- 其他主要品牌；

建立：

$$
(
T_{\mathrm{first}},
T_{\mathrm{consumer}},
T_{\mathrm{mass}},
T_{\mathrm{default}},
T_{\mathrm{dependent}}
).
$$

並依功能：

- camera；
- speech；
- assistant；
- on-device model；
- generative AI；
- agent；

分開。

---

## 48.2 PC AI 架構遷移資料庫

追蹤：

$$
\text{CPU/GPU-only}
\rightarrow
\text{NPU}
\rightarrow
\text{OS AI integration}
\rightarrow
\text{AI-native workflows}.
$$

重要指標包括：

- NPU penetration；
- local inference share；
- default AI features；
- AI-off degradation。

---

## 48.3 汽車 AI 功能域矩陣

對每車型建立：

$$
\mathbf L_{\mathrm{car}}
=
(
L_{\mathrm{ADAS}},
L_{\mathrm{perception}},
L_{\mathrm{planning}},
L_{\mathrm{cabin}},
L_{\mathrm{maintenance}},
L_{\mathrm{agent}}
).
$$

避免只用：

$$
\text{self-driving yes/no}.
$$

---

## 48.4 醫療 AI 從監管到依賴的時間差

測量：

$$
\Delta T
=
T_{\mathrm{dependent}}
-
T_{\mathrm{reg}}.
$$

研究：

> 一項 AI 醫療功能獲准之後，多久才真正成為醫療流程不可忽略的能力？

---

## 48.5 工業 AI 控制鏈滲透

測量：

$$
L_{\mathrm{industrial}}
$$

在：

- design；
- programming；
- monitoring；
- predictive maintenance；
- scheduling；
- autonomous control；

中的分布。

---

## 48.6 跨國 measurement harmonization

建立統一問卷：

$$
M_1-M_5
$$

並固定：

- firm size；
- sector；
- reference period；
- AI definition；

以便真正比較：

$$
L(c,d,t).
$$

---

## 48.7 AI 可見度悖論

測試：

$$
L\uparrow
$$

是否伴隨：

$$
V_{\mathrm{AI}}\downarrow.
$$

比較：

- explicit chatbot；
- invisible ranking；
- camera AI；
- fraud detection；
- logistics AI。

---

# 49. 可反駁條件

本文至少存在以下反駁方向。

1. 若多數技術領域的 $T_{\mathrm{first}}$ 、 $T_{\mathrm{consumer}}$ 、 $T_{\mathrm{mass}}$ 、 $T_{\mathrm{default}}$ 、 $T_{\mathrm{dependent}}$ 幾乎總是同時發生，五時間型別模型將被削弱。
2. 若 $L_0-L_7$ 無法在任何主要領域形成可重現分類，滲透層級需要重構。
3. 若跨國 AI adoption 調查即使定義不同仍可無偏地直接比較，measurement type safety 的必要性會降低。
4. 若 AI 可見度與滲透深度始終同步增加，本文的 invisibility hypothesis 需要下修。
5. 若 AI 進入手機與 PC 長期停留在可選 app 層，本文對 system-layer integration 的歷史判斷需修正。
6. 若 AI 醫療裝置數量增加但臨床流程長期沒有任何實質依賴，醫療 AI 的 $L$ 值應保持較低。
7. 若工業 AI 只改善文件與聊天、不進入工程與控制流程，工業 AI 的深層滲透預期需要降低。
8. 若不同國家內部的地區、產業與企業規模差異遠小於國家間差異，本文對 subnational decomposition 的重視需重新評估。
9. 若移除 AI 對已達 $L_7$ 的領域不造成大規模功能退化，則 $L_7$ 定義本身需要否定。

---

# 50. Non-Claims

本文明確不主張以下命題：

1. 不主張 Siri 是世界第一個手機 AI。
2. 不主張 iPhone 4S 是世界第一台 AI 手機。
3. 不主張 Samsung Galaxy S24 在嚴格歷史意義上是世界第一台 AI phone。
4. 不主張品牌自行使用「AI phone」即可決定技術史分類。
5. 不主張所有語音辨識都等同現代生成式 AI。
6. 不主張所有機器學習功能都具有代理性。
7. 不主張 Apple Intelligence 已在 2024 年立即成為所有 Apple 使用者的預設能力。
8. 不主張 2026 年 Siri AI 已在所有地區、語言與裝置全面普及。
9. 不主張 Gemini 已在所有 Android 裝置完成相同程度的系統整合。
10. 不主張 Copilot+ PC 是第一台能執行 AI 的 PC。
11. 不主張沒有 NPU 的電腦不能執行 AI。
12. 不主張 NPU TOPS 可單獨代表整台 PC 的 AI 能力。
13. 不主張所有汽車 AI 都等同自動駕駛。
14. 不主張 SAE Level 3 等同完全自動駕駛。
15. 不主張 Mercedes-Benz 是所有汽車 AI 功能的起點。
16. 不主張車載生成式 AI 等同車輛自主控制。
17. 不主張 FDA 授權的 AI-enabled medical device 數量等同臨床使用量。
18. 不主張醫療 AI 已取代醫師。
19. 不主張 FDA 的監管框架代表全球所有法域。
20. 不主張工業 AI 主要只由 Siemens 代表。
21. 不主張 Industrial Copilot 使用者數等同所有工業 AI 使用者。
22. 不主張 EU 企業 AI 使用率可直接代表一般人口 AI 使用率。
23. 不主張 EU、US、China、Taiwan 的官方 AI 數據具有相同定義。
24. 不主張台灣「導入／評估／規劃」比例可直接與 EU「已使用」比例相比。
25. 不主張中國政策目標等同實際 AI 滲透率。
26. 不主張國家平均值能代表所有地區。
27. 不主張城市一定比鄉村更 AI 化。
28. 不主張大型企業一定比小型企業在所有 AI 功能上更先進。
29. 不主張 AI 滲透一定單向增加。
30. 不主張 AI 滲透一定對人類有利。
31. 不主張 AI 滲透一定對人類有害。
32. 不主張 AI 基礎設施化等於 AI 主體化。
33. 不主張 AI 主體性是 AI 滲透研究的必要前提。
34. 不主張 $L_7$ 是文明應追求的目標。
35. 不主張 $L_0$ 是文明落後的充分條件。
36. 不主張高 AI 滲透必然降低人類自主。
37. 不主張低 AI 滲透必然提高人類自主。
38. 不主張 AI 數量可以直接代表 AI 影響力。
39. 不主張裝置數可以直接代表智能密度。
40. 不主張本文已完成全球所有國家、所有產業與所有裝置的 AI 滲透史。

---

# 51. 結論：不是「AI 何時來了」，而是「AI 何時變成預設世界的一部分」

若只問：

> AI 是哪一年進入手機？

我們會陷入：

$$
\text{firstness dispute}.
$$

若改問：

> AI 何時第一次被消費者直接看見？

Siri 是重要答案之一。

若問：

> AI 何時進入家庭環境？

Echo / Alexa 是重要節點之一。

若問：

> AI 何時開始成為手機與 PC 的系統層與硬體設計條件？

2024–2026 年的 Apple Intelligence、Galaxy AI、Gemini/Android 與 Copilot+ PC 提供了清楚的新階段。

若問：

> 汽車何時把部分物理動態任務交給自動系統？

則需要 SAE automation level，而不是一句「AI 車」。

若問：

> AI 何時真正進入醫療與工業？

又必須追蹤：

$$
\text{regulatory}
+
\text{workflow}
+
\text{operational}
+
\text{dependency}
$$

不同時間點。

因此：

$$
\boxed{
\text{AI Era}
}
$$

不是一個日期。

它更像：

$$
\boxed{
\mathcal A(c,r,d,t).
}
$$

也就是一張：

$$
\boxed{
\text{spatiotemporal penetration field}.
}
$$

人類不是在某一天突然醒來：

> 世界有 AI 了。

更可能是：

$$
\boxed{
\text{one function}
\rightarrow
\text{one device}
\rightarrow
\text{one workflow}
\rightarrow
\text{one infrastructure}
\rightarrow
\text{another domain}
}
$$

逐步累積。

最後回頭才發現：

$$
\boxed{
P(
\text{ordinary action intersects AI-mediated system}
)
\rightarrow1.
}
$$

那時，「AI 無所不在」才真正不再是一句產品宣傳詞。

而本文也因此為下一篇留下更尖銳的問題：

> 當 AI 不只是「裝進既有機器」，而是裝置、作業系統、硬體與工作流程一開始就以 AI 作為主要結構設計時，我們是否需要把「有 AI 的機器」與「AI 原生系統」正式分型？

這就是 EXS-05 的主題。

---

# 參考文獻

[1] Apple. (2011). **iPhone 4S First Weekend Sales Top Four Million.** Apple 將 Siri 描述為 intelligent assistant，並公布 iPhone 4S 首週末銷量超過 400 萬台。本文於 2026-08-18 重新核對。

[2] Amazon. (2019, 2025). **Alexa / Echo historical materials.** Amazon 官方資料指出第一代 Echo 與 Alexa 於 2014 年 11 月推出；後續官方資料將 Echo 描述為開創 smart speaker 類別的重要產品。

[3] Google. (2025). **Welcome to the next era of Google Home / Gemini for Home.** Google 宣布 Gemini for Home 將取代既有 Google Assistant 於智慧喇叭與顯示器，並擴展到攝影機、門鈴與 Google Home app。

[4] Apple. (2024). **Introducing Apple Intelligence for iPhone, iPad, and Mac.** Apple 將 Apple Intelligence 定義為 personal intelligence system，並深度整合進 iOS 18、iPadOS 18 與 macOS Sequoia。

[5] Samsung Electronics. (2024–2026). **Galaxy AI launch and expansion materials.** Galaxy AI 於 Galaxy S24 系列 2024 年推出，後續逐步擴展到手機、平板、穿戴與其他 Galaxy 裝置。

[6] Google. (2023–2024). **Gemini Nano / AICore / Android integration.** Google 將 Gemini Nano 透過 AICore 帶入 Android 14，並持續推動 Gemini 模型於 Android 系統層與 on-device AI。

[7] Google. (2025). **The Assistant experience on mobile is upgrading to Gemini.** Google 於 2025-03-14 宣布手機端 Google Assistant 使用者將逐步升級至 Gemini。

[8] Apple. (2026). **WWDC26: next generation of Apple Intelligence and Siri AI.** Apple 於 2026-06-08 公布新一代 Apple Intelligence 與 Siri AI；部分能力仍依 beta、語言、地區與法規時程推出。

[9] Google. (2026). **The Gemini app becomes more agentic, delivering proactive, 24/7 help.** Google 於 2026 年持續將 Gemini 往 proactive 與 agentic assistance 推進。

[10] Microsoft. (2024–2026). **Introducing Copilot+ PCs / Copilot+ PC developer guide.** Microsoft 於 2024 年推出 Copilot+ PC 類別，將 $40+$ TOPS NPU 作為多項本地 Windows AI 能力的重要硬體條件。

[11] Mercedes-Benz. (2023–2026). **DRIVE PILOT Level 3 materials.** DRIVE PILOT 在特定運行設計條件下可接手 dynamic driving task，駕駛仍須在系統要求時重新接管。

[12] Google. (2025). **Gemini is here for Android Auto.** Google 將 Gemini 推向 Android Auto，支援自然語言導航、訊息、郵件與其他車載任務。

[13] U.S. Food and Drug Administration. (2026). **Artificial Intelligence-Enabled Medical Devices.** FDA 維護 AI-Enabled Medical Device List，列出經授權在美國市場銷售的 AI-enabled medical devices。

[14] U.S. Food and Drug Administration. (2025). **FDA Issues Comprehensive Draft Guidance for Developers of Artificial Intelligence-Enabled Medical Devices.** FDA 表示已透過既有 premarket pathways 授權超過 1,000 個 AI-enabled devices。

[15] FDA, Health Canada, MHRA. (2024). **Transparency for Machine Learning-Enabled Medical Devices: Guiding Principles.** 指導原則包括 human-AI team performance 與向使用者提供清楚資訊。

[16] Siemens. (2024). **Siemens and Microsoft scale industrial AI.** Siemens 表示 Industrial Copilot 已被歐洲與美國超過 100 個客戶使用，並擴展至工程與工業自動化流程。

[17] Samsung Electronics. (2025). **Galaxy AI: The Journey of Innovation.** Samsung 將 Galaxy S24 系列稱為「world's first AI phone」；本文把此視為企業自我定位，不把它直接當作中立技術史定論。

[18] Eurostat. (2026). **Digitalisation in Europe – 2026 edition.** 2025 年 EU 約 20% 企業使用 AI；大型企業與 SMEs、各會員國間差異顯著。

[19] U.S. Census Bureau. (2026). **Large Firms With at Least 20 Employees Biggest AI Users / Business Trends and Outlook Survey.** 2025-12 至 2026-05 的 BTOS 顯示美國企業 AI 使用率約 17%–20%，且企業規模與產業差異顯著。

[20] 中華人民共和國工業和信息化部. (2026). **《“人工智能+信息通信”創新發展實施意見（2026—2028年）》.** 文件提出 AI 手機、AI 電腦、智慧家庭設備、智慧穿戴、具身智能與工業智能體等融合方向。

[21] 台灣國家發展委員會. (2026). **2026 上半年台灣採購經理人營運展望調查.** 調查顯示製造與非製造業對 AI 的已導入、評估或規劃具有相當廣度，且主要應用集中在流程自動化、需求預測、行政、客服與文件處理等領域。

[22] 台灣行政院／經濟部. (2025–2026). **AI 與 5G 中小企業數位轉型、AI 新十大建設相關資料.** 政策與輔導資料顯示 AI 已逐步進入製造、服務、物流、行銷與公共產業轉型。

[23] Eurostat. (2025). **Usage of AI technologies increasing in EU enterprises.** 2024 年 EU 企業 AI 使用率為 13.5%，高於 2023 年的 8.0%，顯示滲透速度仍快速變動。

[24] U.S. Census Bureau. (2026). **BTOS AI Supplement.** BTOS 已擴增至企業不同 business functions、工作任務與 AI 導入後營運調整的持續性調查。

---

# 附錄 A｜最小符號表

| 符號 | 意義 |
|---|---|
| $T_{\mathrm{first}}$ | 首次可識別 AI 導入 |
| $T_{\mathrm{consumer}}$ | 消費者可見 AI 時點 |
| $T_{\mathrm{mass}}$ | 大規模普及時點 |
| $T_{\mathrm{default}}$ | AI 成為預設整合能力的時點 |
| $T_{\mathrm{dependent}}$ | 功能域進入 AI 依賴的時點 |
| $T_{\mathrm{reg}}$ | 監管准入時點 |
| $L_0-L_7$ | AI 滲透層級 |
| $\mathbf L_D$ | 單一裝置的 AI 功能滲透剖面 |
| $M_1-M_5$ | AI adoption 測量型別 |
| $V_{\mathrm{AI}}$ | 使用者感知 AI 中介的可見度 |
| $\mathbf A_c(t)$ | 國家／區域 AI 文明滲透狀態向量 |
| $L(c,r,d,s,t)$ | 國家、區域、功能域、群體與時間的 AI 滲透函數 |
| $D_{\mathrm{cap}}$ | EXS-02 的能力依賴深度 |

---

# 附錄 B｜五時間型別

$$
\boxed{
T_{\mathrm{first}}
}
$$

「第一次有。」

$$
\downarrow
$$

$$
\boxed{
T_{\mathrm{consumer}}
}
$$

「一般人第一次明顯感覺有。」

$$
\downarrow
$$

$$
\boxed{
T_{\mathrm{mass}}
}
$$

「大量人／設備都有。」

$$
\downarrow
$$

$$
\boxed{
T_{\mathrm{default}}
}
$$

「新系統預設就有。」

$$
\downarrow
$$

$$
\boxed{
T_{\mathrm{dependent}}
}
$$

「拿掉之後，功能域明顯退化。」

---

# 附錄 C｜EXS 系列累積鏈

EXS-01：

$$
\boxed{
\text{Internal Capability}
\neq
\text{Accessible Capability}.
}
$$

EXS-02：

$$
\boxed{
\text{Accessible Capability}
\neq
\text{Resilient Capability}.
}
$$

EXS-03：

$$
\boxed{
\text{Humanly Usable Knowledge}
\neq
\text{Humanly Executed Every Step}.
}
$$

EXS-04：

$$
\boxed{
\text{AI Presence}
\neq
\text{AI Penetration}
\neq
\text{AI Dependency}.
}
$$

合併：

$$
\boxed{
\text{Capability Externalization}
\rightarrow
\text{Dependency Structure}
\rightarrow
\text{Computational Delegation}
\rightarrow
\text{AI Penetration}.
}
$$

---

# 附錄 D｜下一篇接口

**EXS-05｜沒有 AI 的機器、有 AI 的機器與 AI 原生系統**
**從功能附加到架構原生化的系統分類**

下一篇將正式處理：

$$
\boxed{
\text{Machine without AI}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{Machine with AI}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{AI-Dependent Machine}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{AI-Native System}.
}
$$

核心問題將是：

> 「有 AI」到底是設備擁有一個 AI 功能，還是設備本身已經被重新設計成 AI 是不可分割的主要運行層？

這將把 EXS-04 的滲透史轉為 EXS-05 的系統架構分類。
