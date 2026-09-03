# EXS-05｜沒有 AI 的機器、有 AI 的機器與 AI 原生系統
## 從功能附加、架構依賴到以智能為設計起點的系統分類

**系列：** Human Capability Externalization & Intelligence Substrate Evolution Series  
**系列中文名：** 人類能力外部化與智能載體演化系列  
**編號：** EXS-05  
**版本：** v1.0  
**日期：** 2026-08-18  
**狀態：** Canonical Source / UTF-8 Markdown  
**作者：** Neo.K  
**協作整理：** GPT-5.6 Sol  

---

## 摘要

EXS-04 建立了 AI 滲透的多階段模型，指出「第一次出現」「消費者可見」「大規模普及」「預設整合」與「功能依賴」不能被壓成單一時間點。本文進一步處理一個更基礎的架構問題：一台機器「有 AI」究竟意味著什麼？一個傳統裝置後來加入影像辨識功能、一台 PC 可以執行 AI 模型、一支手機把生成式模型整合進作業系統，以及一台從感測、推理、控制到硬體加速都以 AI 為核心設計的機器，不能被視為同一類系統。

本文提出「AI 架構中心性」與「反事實移除測試」作為分類基礎。核心區分是：

$$
\boxed{
\text{AI-Capable}
\neq
\text{AI-Embedded}
\neq
\text{AI-Dependent}
\neq
\text{AI-Native}.
}
$$

「AI-Capable」表示系統能夠執行 AI 工作負載，但其主要架構並不依賴 AI；「AI-Embedded」表示 AI 已被整合至一個或多個重要功能；「AI-Dependent」表示移除 AI 後，重要功能或性能發生結構性下降；「AI-Native」則表示 AI 不只是附加模組，而是從硬體配置、系統服務、資料流、控制邏輯、介面與持續更新機制的設計起點就被假定存在。

本文以 2024 年後的 Copilot+ PC、Android AICore / Gemini Nano、Apple Intelligence，以及 NVIDIA Jetson Thor 等公開架構為當代案例。Microsoft 以具備 $40+$ TOPS NPU 的硬體類別支持 Copilot+ PC；Android 將 AICore 設計為系統服務，用於管理 on-device foundation models；Apple 將 Apple Intelligence 描述為深度整合進 iPhone、iPad 與 Mac 系統核心的個人智能層；NVIDIA Jetson Thor 則以 physical AI、即時推論、多模型與多感測工作負載作為平台設計目標。這些案例不證明任何一家產品已達本文定義的完整 AI-native 終態，但清楚顯示機器設計正從「可以執行 AI」轉向「為持續 AI 工作負載而重構」。

本文進一步指出，AI-native 不是市場標籤，也不是「模型很大」的同義詞。真正重要的是：若把 AI 移除，是否只失去一個功能，還是整個系統的資料路徑、控制方式、使用者介面、硬體配置與工作流程都需要重新設計。本文把這個問題形式化為「反事實 AI 移除測試」：

$$
\boxed{
\mathcal R_{\neg AI}(S)
=
\text{system behavior when AI is removed from system }S.
}
$$

若移除 AI 只造成局部功能下降，系統更接近 AI-assisted 或 AI-embedded；若移除 AI 使核心運作模型失效，則其 AI 架構中心性更高。

本文的目的不是宣稱所有未來機器都會 AI-native，也不主張 AI-native 必然更好，而是建立一套可跨 PC、手機、機器人、車輛、工業設備與未來自主系統使用的架構分類。這一分類同時為下一篇 EXS-06 的「智能載體多樣化」奠定接口：當 AI 的承載基質不再限定於傳統數位機器時，「機器是否有 AI」本身將進一步被「智能究竟由何種基質承載」取代。

---

## 關鍵詞

AI-native；AI-capable；AI-embedded；AI-dependent；AI 架構中心性；NPU；Copilot+ PC；AICore；Gemini Nano；Apple Intelligence；Jetson Thor；physical AI；嵌入式 AI；反事實移除測試；系統架構

---

# 1. 從 EXS-04 的「AI 滲透」轉向「AI 架構」

EXS-04 提出：

$$
\boxed{
\text{AI Presence}
\neq
\text{AI Penetration}
\neq
\text{AI Dependency}.
}
$$

本文再增加一層：

$$
\boxed{
\text{AI Penetration}
\neq
\text{AI Architectural Centrality}.
}
$$

兩個裝置都可能有大量 AI 功能，但其中一個只是：

$$
\text{traditional system}
+
\text{AI modules},
$$

另一個則可能是：

$$
\boxed{
\text{AI-centered system architecture}.
}
$$

這兩者在：

- 硬體；
- 軟體；
- 失效模式；
- 資料流；
- 更新；
- 控制；
- 安全；
- 使用者介面；

上都可能不同。

---

# 2. 最基本型別：能執行 AI 不等於以 AI 為核心

令系統為：

$$
S.
$$

若：

$$
S
$$

可以執行 AI 模型 $A$，只能推出：

$$
\boxed{
A\in\mathcal C(S)
}
$$

其中 $\mathcal C(S)$ 表示系統可執行的工作集合。

但不能推出：

$$
\boxed{
A
\text{ is architecturally constitutive of }S.
}
$$

也就是：

$$
\boxed{
\text{AI-Capable}
\neq
\text{AI-Native}.
}
$$

一台十年前的 PC 可以透過雲端呼叫大型模型。

這不表示它在十年前就是 AI-native PC。

---

# 3. 「有 AI」至少包含四種不同結構

本文先建立四類最小區分。

## 3.1 AI-Capable

$$
\boxed{
S_C
=
\text{AI-Capable System}.
}
$$

系統能執行或存取 AI 工作負載。

但：

$$
S_C-\text{AI}
$$

仍基本保持原有主要功能。

---

## 3.2 AI-Embedded

$$
\boxed{
S_E
=
\text{AI-Embedded System}.
}
$$

AI 已嵌入：

- 相機；
- 語音；
- 安全；
- 推薦；
- 感測；
- 維修；

等重要功能。

但核心架構仍可被理解成：

$$
\text{system first}
+
\text{AI function second}.
$$

---

## 3.3 AI-Dependent

$$
\boxed{
S_D
=
\text{AI-Dependent System}.
}
$$

移除 AI 後：

$$
\Delta C_{\mathrm{core}}\ll0.
$$

也就是重要能力大幅下降。

但仍可能有：

$$
\text{fallback architecture}.
$$

---

## 3.4 AI-Native

$$
\boxed{
S_N
=
\text{AI-Native System}.
}
$$

AI 在設計時被視為主要能力層之一。

因此：

$$
\boxed{
\text{Hardware}
+
\text{OS}
+
\text{Dataflow}
+
\text{Interface}
+
\text{Control}
}
$$

都可能圍繞 AI 工作負載重新配置。

---

# 4. AI-native 不是「AI 很多」

假設系統 $S_1$：

$$
N_{AI}(S_1)=100.
$$

但每個模型只做：

- 垃圾郵件；
- 相機；
- 推薦；
- 小型分類。

另一個系統 $S_2$：

$$
N_{AI}(S_2)=1.
$$

但該模型負責：

- 環境理解；
- 任務規劃；
- 資源調度；
- 控制核心。

則：

$$
N_{AI}(S_1)>N_{AI}(S_2)
$$

不能推出：

$$
\text{AI-Nativity}(S_1)
>
\text{AI-Nativity}(S_2).
$$

因此：

$$
\boxed{
\text{Model Count}
\neq
\text{Architectural Centrality}.
}
$$

---

# 5. AI-native 也不是「模型很大」

若：

$$
P_A
=
\text{model parameter count},
$$

則：

$$
P_A\uparrow
$$

不代表：

$$
N_A\uparrow
$$

其中 $N_A$ 是 AI-native 程度。

一個大型雲端模型可能只是：

$$
\text{optional external service}.
$$

反之，小型本地模型可能是：

$$
\text{real-time control dependency}.
$$

所以：

$$
\boxed{
\text{Model Scale}
\neq
\text{System Centrality}.
}
$$

---

# 6. 架構中心性：本文的核心概念

本文定義：

$$
\boxed{
A_C(S)
=
\text{AI Architectural Centrality of system }S.
}
$$

它不是單一實證值，而可以先寫成向量：

$$
\mathbf A_C
=
(
a_h,
a_s,
a_d,
a_i,
a_c,
a_u,
a_r
).
$$

其中：

$$
a_h
=
\text{hardware specialization},
$$

$$
a_s
=
\text{system-service integration},
$$

$$
a_d
=
\text{dataflow dependence},
$$

$$
a_i
=
\text{interface mediation},
$$

$$
a_c
=
\text{control dependence},
$$

$$
a_u
=
\text{update/learning dependence},
$$

$$
a_r
=
\text{removal redesign cost}.
$$

---

# 7. 硬體專用化：NPU 為什麼重要？

CPU 與 GPU 本來就能執行 AI。

因此：

$$
\boxed{
\text{NPU presence}
\neq
\text{first AI capability}.
}
$$

NPU 更重要的意義是：

$$
\boxed{
\text{AI workload expected often enough}
\Rightarrow
\text{dedicated silicon becomes worthwhile}.
}
$$

也就是：

$$
\text{AI}
$$

從：

$$
\text{occasional workload}
$$

逐漸走向：

$$
\text{architectural workload class}.
$$

---

# 8. Copilot+ PC：硬體分類開始直接以 AI 工作負載定義

Microsoft 在 2024 年推出 Copilot+ PC，將高效能 NPU 作為新一代 Windows 11 AI PC 的核心分類條件之一；官方資料將 $40+$ TOPS 作為 Copilot+ PC 的重要硬體基線。

因此：

$$
\boxed{
\text{PC}
}
$$

開始不只依：

- CPU；
- RAM；
- storage；
- GPU；

分類。

而加入：

$$
\boxed{
\text{dedicated AI throughput}.
}
$$

這是一個重要歷史信號。

---

# 9. 但 Copilot+ PC 不應直接等同完整 AI-native PC

本文不主張：

$$
\boxed{
\text{Copilot+ PC}
=
\text{fully AI-native system}.
}
$$

因為 Windows PC 仍大量執行：

$$
\text{non-AI workloads}.
$$

且：

$$
\text{AI off}
$$

不代表：

$$
\text{PC cannot function}.
$$

所以 Copilot+ PC 更適合作為：

$$
\boxed{
\text{architectural transition toward persistent AI workloads}.
}
$$

的證據。

---

# 10. 系統服務化：AI 從 app 變成 OS substrate

如果 AI 只存在於 app：

$$
\text{App}
\rightarrow
A.
$$

系統架構中心性通常較低。

如果 OS 提供：

$$
\boxed{
\text{AI system service}
}
$$

供多個 app 共用，

則：

$$
A
$$

開始成為：

$$
\boxed{
\text{shared operating substrate}.
}
$$

這就是 Android AICore 的歷史意義。

---

# 11. AICore：foundation model 進入 Android 系統服務

Google Android 官方文件指出，Gemini Nano 透過 Android 的 AICore 系統服務在裝置上運行；AICore 管理模型、利用裝置硬體、維持模型更新，並提供低延遲 on-device inference。

因此：

$$
\boxed{
\text{AI Model}
}
$$

開始被 OS 當成：

$$
\boxed{
\text{managed system resource}.
}
$$

而不是：

$$
\boxed{
\text{each app ships its own isolated AI stack}.
}
$$

這是非常重要的 architecture shift。

---

# 12. AI 系統服務的真正意義是「共享能力層」

若每個 app 都有獨立模型：

$$
A_1,A_2,\ldots,A_n.
$$

但若 OS 提供：

$$
A_{\mathrm{core}},
$$

則：

$$
\{App_1,\ldots,App_n\}
\rightarrow
A_{\mathrm{core}}.
$$

這代表 AI 開始像：

- graphics API；
- networking；
- storage；
- security service；

一樣成為：

$$
\boxed{
\text{platform capability layer}.
}
$$

這比「手機裝了 AI app」深一層。

---

# 13. Apple Intelligence：從功能集合走向系統整合

Apple 官方將 Apple Intelligence 描述為：

$$
\text{personal intelligence system}
$$

並表示其深度整合進 iOS、iPadOS 與 macOS。

Apple 目前亦將 on-device processing 與 Private Cloud Compute 結合，形成：

$$
\boxed{
\text{local AI}
+
\text{cloud AI}
}
$$

的混合架構。

這表示：

$$
\text{AI placement}
$$

不再只是：

$$
\text{local}
\quad\text{or}\quad
\text{cloud}.
$$

更可能是：

$$
\boxed{
\text{dynamic compute placement}.
}
$$

---

# 14. AI-native 不等於全部本地端

這是一個重要型別安全：

$$
\boxed{
\text{AI-Native}
\neq
\text{On-Device Only}.
}
$$

一個 AI-native 系統可以：

- 本地模型；
- 雲端模型；
- 邊緣節點；
- 私有資料中心；
- 多模型路由；

共同運作。

真正判準不是：

$$
\text{where AI runs},
$$

而是：

$$
\boxed{
\text{whether AI is constitutive of system architecture}.
}
$$

---

# 15. Local / Edge / Cloud 是部署拓樸，不是 AI-native 程度

令：

$$
D_A
=
\{
\text{local},
\text{edge},
\text{cloud}
\}.
$$

則：

$$
D_A
$$

描述：

$$
\text{deployment topology}.
$$

而：

$$
A_C
$$

描述：

$$
\text{architectural centrality}.
$$

因此：

$$
\boxed{
D_A
\neq
A_C.
}
$$

一個完全雲端的 AI 系統可以很 AI-native。

一個全本地 AI 功能也可以只是可選附加。

---

# 16. 資料流依賴：AI 是否位在資訊必經路徑？

若資料流為：

$$
x
\rightarrow
f
\rightarrow
y.
$$

AI 只是旁路：

$$
x
\rightarrow
f
\rightarrow
y,
$$

$$
x
\rightarrow
A
\rightarrow
z.
$$

則：

$$
A
$$

不是主路徑。

若：

$$
x
\rightarrow
A
\rightarrow
f
\rightarrow
y,
$$

或：

$$
x
\rightarrow
A
\rightarrow
y,
$$

則 AI 位於：

$$
\boxed{
\text{critical data path}.
}
$$

此時：

$$
a_d
\uparrow.
$$

---

# 17. 介面中心性：使用者是不是透過 AI 才能操作系統？

傳統 UI：

$$
H
\rightarrow
\text{menu}
\rightarrow
\text{function}.
$$

AI-mediated UI：

$$
H
\rightarrow
A
\rightarrow
\text{functions}.
$$

若：

$$
A=0
$$

時仍有完整 UI，

則 AI 可能只是：

$$
\text{alternative interface}.
$$

若整個系統被設計成：

$$
\boxed{
\text{intent-first interaction}
}
$$

而 AI 負責解釋、規劃與調用功能，

則：

$$
a_i\uparrow.
$$

---

# 18. 從 Function-Centric UI 到 Intent-Centric UI

傳統裝置：

> 使用者知道功能在哪裡。

AI-native 介面可能：

> 使用者只描述想達到什麼。

因此：

$$
\boxed{
\text{Function Selection}
\rightarrow
\text{Intent Interpretation}.
}
$$

例如：

$$
H:
\text{“整理這週的工作並排出優先級”}
$$

系統再選：

- 郵件；
- 日曆；
- 文件；
- 任務；
- 通知。

這不是單純語音控制。

而是：

$$
\boxed{
\text{semantic mediation}.
}
$$

---

# 19. 控制中心性：AI 是否真正影響世界狀態？

如果 AI 只：

$$
\text{suggests},
$$

控制中心性較低。

如果 AI：

$$
\text{selects action},
$$

更高。

如果 AI：

$$
\text{executes action},
$$

再更高。

如果 AI：

$$
\text{maintains closed-loop control},
$$

則：

$$
a_c
$$

非常高。

因此可建立：

$$
C_0
=
\text{observe},
$$

$$
C_1
=
\text{recommend},
$$

$$
C_2
=
\text{select},
$$

$$
C_3
=
\text{execute},
$$

$$
C_4
=
\text{closed-loop adapt}.
$$

---

# 20. 機器人是 AI-native 分類最清楚的壓力測試

傳統工業機器人可能：

$$
\text{fixed program}
\rightarrow
\text{fixed trajectory}.
$$

AI 增強機器人可能：

$$
\text{vision AI}
+
\text{traditional control}.
$$

更進一步：

$$
\boxed{
\text{perception}
\rightarrow
\text{reasoning}
\rightarrow
\text{planning}
\rightarrow
\text{control}
}
$$

都由 AI 模組深度參與。

這時：

$$
A_C
\uparrow\uparrow.
$$

---

# 21. Jetson Thor：physical AI 為什麼是重要案例？

NVIDIA 將 Jetson Thor 定位為 physical AI 與 robotics 平台，強調：

- generative reasoning；
- multimodal processing；
- multisensor processing；
- real-time inference；
- multiple AI workflows。

這代表硬體平台本身已經不是：

$$
\text{generic embedded computer}
$$

再附加：

$$
\text{one AI task}.
$$

而是：

$$
\boxed{
\text{platform designed around continuous embodied AI workload}.
}
$$

---

# 22. 但 Jetson Thor 也不是「AI-native 機器人」本身

需要區分：

$$
\boxed{
\text{AI-native platform}
}
$$

與：

$$
\boxed{
\text{AI-native final system}.
}
$$

Jetson Thor 是：

$$
\text{compute substrate}.
$$

真正機器人是否 AI-native 還取決於：

- 控制架構；
- sensors；
- fallback；
- planning；
- runtime；
- application logic。

所以：

$$
\boxed{
\text{AI-native component}
\not\Rightarrow
\text{AI-native whole system}.
}
$$

---

# 23. 組件中心性與系統中心性必須分開

令組件：

$$
c_i.
$$

其 AI 中心性為：

$$
A_C(c_i).
$$

整體系統：

$$
S=
\{c_1,\ldots,c_n\}.
$$

則：

$$
A_C(S)
$$

不能簡化為：

$$
\sum_i A_C(c_i).
$$

因為：

$$
\boxed{
\text{Topology matters}.
}
$$

如果高 AI 中心性組件只在旁路：

$$
A_C(S)
$$

仍可能不高。

如果它位在：

$$
\text{critical control path},
$$

則影響巨大。

---

# 24. 反事實 AI 移除測試

本文提出：

$$
\boxed{
\mathcal R_{\neg AI}(S)
}
$$

表示：

> 假設把系統中的 AI 能力移除，系統還剩什麼？

測試至少包含：

1. 是否仍能啟動？
2. 是否仍能完成核心功能？
3. 是否只是性能下降？
4. 是否需要人工接管？
5. 是否需要替換大量介面？
6. 是否需要重寫控制邏輯？
7. 是否需要更換硬體？
8. 是否整個產品價值主張失效？

---

# 25. 四種反事實移除結果

## $R_0$：無實質影響

$$
\mathcal R_{\neg AI}(S)
\approx
S.
$$

AI 只是邊緣附加。

---

## $R_1$：功能下降

$$
\mathcal R_{\neg AI}(S)
=
S-\{f_1,\ldots,f_k\}.
$$

仍可運作。

---

## $R_2$：核心性能下降

$$
\Delta C_{\mathrm{core}}\ll0.
$$

但可降級運行。

---

## $R_3$：架構失配

移除 AI 後：

$$
\boxed{
\text{system must be substantially redesigned}.
}
$$

這是 AI-native 的強信號。

---

# 26. AI-native 的最強判準：移除後不是「不好用」，而是「不是同一種系統」

假設：

$$
S_N
$$

是 AI-native 系統。

若：

$$
\mathcal R_{\neg AI}(S_N)
$$

得到的只是：

$$
S_N'
$$

且：

$$
S_N'
$$

仍屬同一產品型別，

則 AI-native 程度有限。

真正強的 AI-native 是：

$$
\boxed{
\mathcal R_{\neg AI}(S_N)
\notin
\text{same architectural class}.
}
$$

也就是：

> AI 拿掉之後，你不是得到「比較笨的同一台機器」，而是必須重新發明這台機器。

---

# 27. 舉例：AI 相機與 AI-native 視覺機器人

相機：

$$
\text{traditional camera}
+
\text{AI enhancement}.
$$

移除 AI：

$$
\text{still a camera}.
$$

所以可能：

$$
R_1.
$$

視覺自主機器人：

$$
\text{vision}
\rightarrow
A
\rightarrow
\text{planning}
\rightarrow
\text{motion}.
$$

移除 AI：

$$
\text{no meaningful autonomous behavior}.
$$

可能：

$$
R_2-R_3.
$$

這就是兩者差異。

---

# 28. AI-native 與 autonomy 仍然不同

一個 AI-native 系統可以：

$$
\text{high AI centrality}
$$

但：

$$
\text{low autonomy}.
$$

例如：

> AI 是核心介面與運算層，但所有重要行動仍需人類批准。

所以：

$$
\boxed{
\text{AI-Nativity}
\neq
\text{Autonomy}.
}
$$

反之，一個高度自動化系統也可能：

$$
\text{low AI}.
$$

傳統自動控制就是例子。

---

# 29. 自動化不等於 AI

令：

$$
\text{Automation}
=
\text{predefined rule execution}.
$$

則可以有：

$$
\boxed{
\text{High Automation}
+
\text{Low AI}.
}
$$

例如：

- 電梯；
- PLC；
- 傳統工業控制；
- 定時系統。

因此：

$$
\boxed{
\text{Autonomous-looking behavior}
\neq
\text{AI architecture}.
}
$$

必須檢查實際控制型別。

---

# 30. AI-native 也不等於 agentic

Agentic 通常強調：

$$
\text{goal}
+
\text{state}
+
\text{multi-step action}
+
\text{feedback}.
$$

AI-native 強調：

$$
\text{architecture}.
$$

因此：

$$
\boxed{
\text{AI-Native}
\neq
\text{Agentic}.
}
$$

可以有：

$$
\text{AI-native non-agentic sensor}.
$$

也可以有：

$$
\text{agentic cloud service on non-AI-native hardware}.
$$

---

# 31. AI-native 與 AI-dependent 也不能混

AI-dependent：

$$
\boxed{
\text{remove AI}
\Rightarrow
\text{large capability loss}.
}
$$

AI-native：

$$
\boxed{
\text{remove AI}
\Rightarrow
\text{architecture itself becomes invalid}.
}
$$

所以：

$$
\boxed{
\text{Dependency}
\subseteq
\text{possible nativity evidence},
}
$$

但不是充分條件。

---

# 32. 一個既有系統也可能後來「AI-native 化」

AI-native 不一定只能從零開始。

假設：

$$
S_0
$$

原本是 traditional architecture。

多次改版：

$$
S_0
\rightarrow
S_1
\rightarrow
S_2
\rightarrow
S_3.
$$

若最後：

- NPU 成為標配；
- AI system service 成為 OS 層；
- UI 改成 intent-first；
- workflow 預設 AI；
- 資料流依賴 AI；

則：

$$
\boxed{
\text{legacy system}
\rightarrow
\text{AI-native architecture}
}
$$

可以漸進發生。

---

# 33. 因此 AI-native 是相位，不一定是出生身分

可定義：

$$
\boxed{
N_A(t)
=
\text{AI nativity degree at time }t.
}
$$

一個產品線可以：

$$
N_A(t_0)\approx0
$$

逐漸：

$$
N_A(t_1)>0,
$$

再：

$$
N_A(t_2)\gg0.
$$

所以：

$$
\boxed{
\text{AI-Native}
}
$$

最好被理解為：

$$
\boxed{
\text{architectural state}
}
$$

而不是：

$$
\boxed{
\text{marketing birth certificate}.
}
$$

---

# 34. AI-native 硬體的第一個特徵：持續推論能力

一般硬體：

$$
\text{AI workload}
=
\text{occasional}.
$$

AI-native 硬體：

$$
\text{AI workload}
=
\text{persistent expectation}.
$$

因此設計會開始優化：

- TOPS/W；
- memory bandwidth；
- low latency；
- model residency；
- sensor fusion；
- privacy；
- local inference；
- thermal budget。

這些都是：

$$
\boxed{
\text{architectural consequences of expecting AI}.
}
$$

---

# 35. 第二個特徵：資料路徑為 AI 重寫

傳統資料路徑：

$$
\text{sensor}
\rightarrow
\text{fixed processing}
\rightarrow
\text{output}.
$$

AI-centered：

$$
\text{sensor}
\rightarrow
\text{model}
\rightarrow
\text{state representation}
\rightarrow
\text{decision}.
$$

這會改變：

- memory；
- caching；
- scheduling；
- latency；
- model lifecycle；
- safety monitoring。

所以：

$$
\boxed{
\text{AI is not only software logic}
}
$$

而開始決定：

$$
\boxed{
\text{system data architecture}.
}
$$

---

# 36. 第三個特徵：更新邏輯從「軟體更新」變成「模型生命周期」

傳統：

$$
\text{software version}
\rightarrow
\text{update}.
$$

AI 系統還需要：

$$
\text{model version},
$$

$$
\text{weights},
$$

$$
\text{evaluation},
$$

$$
\text{safety policy},
$$

$$
\text{rollback}.
$$

因此：

$$
\boxed{
\text{Software Lifecycle}
\rightarrow
\text{Software + Model Lifecycle}.
}
$$

Android AICore 明確包含 model management 與 model update。

這就是 system-service AI 的重要後果。

---

# 37. 第四個特徵：失效模式不同

傳統程式錯誤：

$$
\text{bug}
$$

通常期待：

$$
\text{same input}
\rightarrow
\text{same failure}.
$$

AI 還可能有：

- distribution shift；
- hallucination；
- confidence error；
- model drift；
- adversarial input；
- unsafe generalization。

所以：

$$
\boxed{
\text{AI-Native Architecture}
}
$$

必須把：

$$
\boxed{
\text{model uncertainty}
}
$$

當成一級系統條件。

---

# 38. 第五個特徵：fallback 不能再只是 reboot

傳統系統失效：

$$
\text{restart}
$$

可能恢復。

AI-native 系統失效時可能需要：

- alternate model；
- deterministic fallback；
- degraded mode；
- human takeover；
- remote assistance；
- rule-based safety layer。

因此：

$$
\boxed{
\text{AI Fallback Architecture}
}
$$

成為 AI-native 系統的重要組件。

---

# 39. AI-native 不代表「所有事情都交給 AI」

反而成熟的 AI-native 系統可能大量使用：

$$
\boxed{
\text{typed separation}.
}
$$

例如：

$$
\text{AI perception}
$$

與：

$$
\text{deterministic emergency brake}
$$

分開。

或：

$$
\text{AI planner}
$$

與：

$$
\text{hard safety envelope}
$$

分開。

因此：

$$
\boxed{
\text{AI-Native}
\neq
\text{AI-Only}.
}
$$

---

# 40. AI-only 甚至可能是較差架構

若所有功能都依賴：

$$
A,
$$

且沒有：

$$
\text{fallback},
$$

則：

$$
D_{\mathrm{cap}}\uparrow.
$$

結合 EXS-02：

$$
\boxed{
\text{High AI Centrality}
+
\text{Low Fallback}
=
\text{High Capability Dependency Risk}.
}
$$

因此 AI-native 設計真正成熟的方向不是：

> 把所有傳統機制刪掉。

而是：

$$
\boxed{
\text{AI-centered capability}
+
\text{typed resilient fallback}.
}
$$

---

# 41. 系統原生性不等於文明原生性

即使：

$$
S
=
\text{AI-native device},
$$

整個社會功能域可能仍：

$$
L_2.
$$

反之，社會可能高度依賴 AI：

$$
L_7,
$$

但底層裝置個別並不全部 AI-native。

因此：

$$
\boxed{
\text{Device Nativity}
\neq
\text{Domain Penetration}.
}
$$

這是 EXS-04 與 EXS-05 的重要型別分離。

---

# 42. AI-native 裝置可能只是整個分散式 AI 的端點

假設：

$$
S_{\mathrm{edge}}
$$

只做：

- sensor；
- preprocessing；
- local inference。

更高層：

$$
A_R
$$

做：

- coordination；
- global planning；
- model update。

則：

$$
\boxed{
S_{\mathrm{edge}}
\leftrightarrow
A_R.
}
$$

所以：

$$
\boxed{
\text{AI-Native Device}
}
$$

不代表：

$$
\boxed{
\text{self-contained intelligence}.
}
$$

它可能只是：

$$
\boxed{
\text{node in distributed intelligence topology}.
}
$$

---

# 43. 這會直接接到未來的區域 AI 與全域 AI

如果大量：

$$
S_1,S_2,\ldots,S_n
$$

都是 AI-native nodes，

並連接：

$$
A_R,
$$

則：

$$
\boxed{
\{S_i\}
\rightarrow
\text{Regional Intelligence Layer}.
}
$$

再進一步：

$$
\{A_{R_1},\ldots,A_{R_m}\}
\rightarrow
A_G.
$$

這才開始接近後續第二系列的：

$$
\boxed{
\text{Pervasive Intelligence}.
}
$$

本文在此只建立接口，不提前展開。

---

# 44. 「機器」本身之後也會成為不夠好的分類

本文仍以：

$$
\text{machine}
$$

為主要討論對象。

但如果未來 AI 承載於：

- biological substrate；
- biohybrid system；
- synthetic tissue；
- neural interface；
- distributed biological-digital network；

則：

$$
\boxed{
\text{AI Machine}
}
$$

不再足以覆蓋所有智能載體。

所以：

$$
\boxed{
\text{AI-Native Machine}
}
$$

只是更一般：

$$
\boxed{
\text{AI-Native Substrate System}
}
$$

的一個子類。

這將是 EXS-06 的主題。

---

# 45. AI-native 架構的六層模型

本文提出：

## $N_0$：AI-Capable

$$
\boxed{
N_0
=
\text{can run/access AI}.
}
$$

---

## $N_1$：AI-Feature Integrated

$$
\boxed{
N_1
=
\text{AI integrated into selected functions}.
}
$$

---

## $N_2$：AI-System-Service Integrated

$$
\boxed{
N_2
=
\text{shared AI runtime/model service at system level}.
}
$$

---

## $N_3$：AI-Workflow Dependent

$$
\boxed{
N_3
=
\text{primary workflows assume AI availability}.
}
$$

---

## $N_4$：AI-Control Centered

$$
\boxed{
N_4
=
\text{AI participates in core perception/planning/control}.
}
$$

---

## $N_5$：AI-Native

$$
\boxed{
N_5
=
\text{removing AI requires substantial architectural redesign}.
}
$$

這個 $N$ 軸與 EXS-04 的 $L$ 軸不同。

---

# 46. $L$ 軸與 $N$ 軸必須分開

EXS-04：

$$
L
=
\text{social/domain penetration}.
$$

EXS-05：

$$
N
=
\text{architectural nativity}.
$$

所以：

$$
\boxed{
L
\neq
N.
}
$$

例如：

$$
N=5,
L=1
$$

可能代表：

> 一台非常 AI-native 的實驗機器人，但社會還很少使用。

反之：

$$
N=1,
L=7
$$

可能代表：

> 大量低 AI-native 裝置共同構成高度 AI 依賴的社會基礎設施。

---

# 47. 再加入 EXS-02 的依賴軸

EXS-02：

$$
D_{\mathrm{cap}}
=
\text{capability dependency depth}.
$$

因此更完整分類是：

$$
\boxed{
\mathbf X
=
(
L,
N,
D_{\mathrm{cap}}
).
}
$$

三個系統：

$$
X_1=(5,1,1),
$$

$$
X_2=(2,5,3),
$$

$$
X_3=(7,4,7)
$$

代表完全不同的文明與工程狀態。

---

# 48. 再加入 autonomy 軸

令：

$$
A_u
=
\text{autonomy level}.
$$

則：

$$
\boxed{
\mathbf X
=
(
L,
N,
D_{\mathrm{cap}},
A_u
).
}
$$

這樣可以避免：

$$
\text{AI-native}
$$

被錯誤理解成：

$$
\text{fully autonomous}.
$$

---

# 49. 再加入 subjectivity 軸：但本文只留空

未來若要研究：

$$
S_u
=
\text{subjectivity evidence}.
$$

則完整空間可能是：

$$
\boxed{
\mathbf X
=
(
L,
N,
D_{\mathrm{cap}},
A_u,
S_u
).
}
$$

但本文明確不填入：

$$
S_u.
$$

因為：

$$
\boxed{
\text{architecture}
\neq
\text{subjecthood}.
}
$$

---

# 50. 核心命題

本文提出以下十六個核心命題。

## 命題 1

$$
\boxed{
\text{AI-Capable}
\neq
\text{AI-Native}.
}
$$

## 命題 2

$$
\boxed{
\text{AI-Embedded}
\neq
\text{AI-Dependent}.
}
$$

## 命題 3

$$
\boxed{
\text{AI-Dependent}
\neq
\text{AI-Native}.
}
$$

## 命題 4

$$
\boxed{
\text{Model Count}
\neq
\text{Architectural Centrality}.
}
$$

## 命題 5

$$
\boxed{
\text{Model Size}
\neq
\text{Architectural Centrality}.
}
$$

## 命題 6

$$
\boxed{
\text{NPU}
\neq
\text{proof of AI nativity}.
}
$$

## 命題 7

$$
\boxed{
\text{Dedicated AI hardware}
}
$$

is evidence that:

$$
\boxed{
\text{persistent AI workload is architecturally expected}.
}
$$

## 命題 8

$$
\boxed{
\text{AI system service}
}
$$

is stronger nativity evidence than:

$$
\boxed{
\text{isolated AI app}.
}
$$

## 命題 9

$$
\boxed{
\text{AI-Native}
\neq
\text{On-Device Only}.
}
$$

## 命題 10

$$
\boxed{
\text{AI-Native}
\neq
\text{AI-Only}.
}
$$

## 命題 11

$$
\boxed{
\text{AI-Native}
\neq
\text{Agentic}.
}
$$

## 命題 12

$$
\boxed{
\text{AI-Native}
\neq
\text{Autonomous}.
}
$$

## 命題 13

$$
\boxed{
\text{AI-Native Component}
\not\Rightarrow
\text{AI-Native Whole System}.
}
$$

## 命題 14

$$
\boxed{
\mathcal R_{\neg AI}(S)
}
$$

is a useful classification test.

## 命題 15

$$
\boxed{
\text{High AI Centrality}
+
\text{Low Fallback}
}
$$

can create high dependency risk.

## 命題 16

$$
\boxed{
\text{Device Nativity}
\neq
\text{Civilizational Penetration}.
}
$$

---

# 51. 可檢驗研究計畫

## 51.1 反事實 AI 移除 benchmark

對：

- smartphone；
- PC；
- car；
- robot；
- industrial machine；

執行概念上的：

$$
\mathcal R_{\neg AI}(S).
$$

記錄：

$$
\Delta C,
$$

$$
\Delta UI,
$$

$$
\Delta control,
$$

$$
\Delta hardware,
$$

$$
\Delta workflow.
$$

---

## 51.2 AI 架構中心性向量

估計：

$$
\mathbf A_C
=
(
a_h,
a_s,
a_d,
a_i,
a_c,
a_u,
a_r
).
$$

並研究：

$$
A_C
$$

與：

$$
L,
D_{\mathrm{cap}},
A_u
$$

是否可分離。

---

## 51.3 AI PC 架構史

比較：

$$
\text{traditional PC}
$$

$$
\rightarrow
$$

$$
\text{AI-capable PC}
$$

$$
\rightarrow
$$

$$
\text{NPU PC}
$$

$$
\rightarrow
$$

$$
\text{Copilot+ class}
$$

並追蹤：

- NPU adoption；
- OS AI service；
- local model runtime；
- workflow dependence。

---

## 51.4 Android AI system-service 研究

追蹤：

$$
\text{AICore}
$$

如何影響：

- model lifecycle；
- API；
- app integration；
- hardware acceleration；
- on-device inference。

測量：

$$
\text{app-level AI}
\rightarrow
\text{platform-level AI}.
$$

---

## 51.5 Apple 混合 AI 拓樸研究

研究：

$$
\text{on-device}
+
\text{Private Cloud Compute}
$$

如何形成：

$$
\boxed{
\text{dynamic AI execution topology}.
}
$$

重點不是品牌比較，而是：

$$
\boxed{
\text{local/cloud boundary becomes a runtime architectural decision}.
}
$$

---

## 51.6 Physical AI 平台研究

比較：

- generic embedded compute；
- AI accelerator；
- Jetson-class physical AI platform；

在：

$$
\text{latency},
\text{sensor fusion},
\text{power},
\text{model concurrency},
\text{robotics workload}
$$

上的架構差異。

---

## 51.7 fallback 成熟度研究

建立：

$$
F_A
=
\text{AI fallback maturity}.
$$

評估：

- deterministic fallback；
- alternate model；
- human takeover；
- degraded mode；
- rollback。

研究：

$$
A_C\uparrow
$$

是否伴隨：

$$
F_A\uparrow.
$$

---

# 52. 可反駁條件

本文至少存在以下反駁方向。

1. 若「AI-capable」「AI-embedded」「AI-dependent」「AI-native」在真實產品中無法形成穩定區分，本文核心分類需要重構。
2. 若移除 AI 幾乎永遠只造成性能下降而不造成架構重設，AI-native 作為獨立類別的必要性會降低。
3. 若 NPU、AI system service、模型生命周期等架構變化與持續 AI 工作負載沒有實質關聯，本文對 architecture shift 的判斷需修正。
4. 若 AICore 類 system service 最終沒有成為跨 app 的共享 AI substrate，本文對 system-service nativity evidence 的權重應下修。
5. 若 Copilot+ PC 類別未形成長期 AI workload architecture，而只是短期市場分類，本文不應把它視為歷史轉折的強證據。
6. 若 Apple Intelligence 類系統整合最終只停留在可拔除 app-level features，則其 architecture-centrality 判斷需下修。
7. 若 physical AI 平台沒有顯著改變機器人或邊緣系統的硬體與資料流設計，Jetson Thor 類案例的理論意義需縮小。
8. 若 high AI centrality 與 fallback / resilience 沒有任何結構關聯，本文與 EXS-02 的依賴接口需要重新建模。
9. 若同一系統的 $L$ 與 $N$ 實證上始終高度等價，則分離 social penetration 與 architectural nativity 的必要性下降。
10. 若 autonomy 與 AI nativity 無法分離，本文的多軸分類需修正。

---

# 53. Non-Claims

本文明確不主張以下命題：

1. 不主張所有能執行 AI 的機器都是 AI-native。
2. 不主張所有有 NPU 的裝置都是 AI-native。
3. 不主張沒有 NPU 的裝置不能 AI-native。
4. 不主張 Copilot+ PC 已是完整 AI-native PC 的終態。
5. 不主張 Microsoft 的產品分類是本文理論分類的唯一標準。
6. 不主張 Android AICore 已存在於所有 Android 裝置。
7. 不主張 Gemini Nano 已在所有 Android 裝置提供相同能力。
8. 不主張 Apple Intelligence 已成為所有 Apple 裝置不可移除的核心依賴。
9. 不主張 Apple 的「integrated into the core」市場描述自動等同本文的 $N_5$。
10. 不主張 NVIDIA Jetson Thor 本身就是完整 AI-native 機器人。
11. 不主張 physical AI 是 NVIDIA 專屬概念。
12. 不主張 AI-native 必須使用 NVIDIA、Apple、Google 或 Microsoft 技術。
13. 不主張 AI-native 系統一定使用大型語言模型。
14. 不主張 AI-native 系統一定需要生成式 AI。
15. 不主張 AI-native 系統一定具有自主性。
16. 不主張 AI-native 系統一定具有 agentic behavior。
17. 不主張 agentic system 一定 AI-native。
18. 不主張高自動化系統一定使用 AI。
19. 不主張傳統控制系統等同 AI。
20. 不主張 AI-native 比非 AI-native 更安全。
21. 不主張 AI-native 比非 AI-native 更危險。
22. 不主張 AI-native 是所有產品應追求的設計方向。
23. 不主張所有設備都需要 AI-native 化。
24. 不主張 AI-native 等於 AI-only。
25. 不主張 deterministic fallback 是所有 AI-native 系統唯一正確做法。
26. 不主張任何單一 fallback 可以處理所有 AI 失效模式。
27. 不主張 AI-native 必須完全本地端運行。
28. 不主張 AI-native 必須完全雲端運行。
29. 不主張 local/edge/cloud 拓樸可直接代表 AI nativity。
30. 不主張模型數量能代表 AI nativity。
31. 不主張模型參數量能代表 AI nativity。
32. 不主張 TOPS 能單獨代表 AI nativity。
33. 不主張同一裝置只能有一個 $N$ 值。
34. 不主張同一產品線的 AI nativity 永遠固定。
35. 不主張 legacy architecture 無法漸進 AI-native 化。
36. 不主張 AI-native 架構一定不可逆。
37. 不主張 AI-native 架構等同社會 AI 依賴。
38. 不主張裝置 AI-native 等同文明 AI-infrastructural。
39. 不主張 AI 架構中心性等同 AI 主體性。
40. 不主張任何架構特徵可以證明 AI 具有意識、人格或道德地位。
41. 不主張本文已完成 AI-native 的正式國際標準定義。
42. 不主張本文分類可取代軟體工程、安全工程、功能安全或資安標準。
43. 不主張本文已涵蓋所有嵌入式系統、醫療設備、汽車與工業機械。
44. 不主張 AI-native 必然是未來唯一主流架構。

---

# 54. 結論：真正的斷點不是「機器裡有 AI」，而是「機器因 AI 而被重新設計」

人類最早的 AI 裝置問題可以問：

> 這台機器有沒有 AI？

但當 AI 逐漸成為：

- 專用硬體工作負載；
- OS system service；
- 共享模型層；
- 主要人機介面；
- 感知核心；
- 規劃核心；
- 控制核心；

之後，這個問題就不夠用了。

更精確的問題是：

$$
\boxed{
\text{What role does AI play in making this system the system that it is?}
}
$$

如果：

$$
\text{remove AI}
$$

只代表：

> 少一個功能。

那它更接近：

$$
\text{AI-Embedded}.
$$

如果：

$$
\text{remove AI}
$$

代表：

> 整個產品的主要能力大幅下降。

則更接近：

$$
\text{AI-Dependent}.
$$

如果：

$$
\text{remove AI}
$$

代表：

> 硬體、OS、資料流、介面與控制方式都要重新設計。

則：

$$
\boxed{
\text{AI-Native}
}
$$

才具有真正的架構意義。

因此本文的核心鏈為：

$$
\boxed{
\text{Machine}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{AI-Capable Machine}
}
$$

$$
\downarrow
$$

$$
\boxed{
\text{AI-Embedded Machine}
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

這條鏈不是必然歷史進步，也不是每個系統都要走到底。

它是一條：

$$
\boxed{
\text{architectural centrality axis}.
}
$$

而一旦這條軸建立，下一個問題就自然出現：

> 為什麼我們還要假設承載智能的東西一定叫「機器」？

如果未來的智能系統可以存在於：

- 生物基質；
- 混合基質；
- 神經—數位耦合；
- 分散式網路；
- 非傳統計算載體；

則：

$$
\boxed{
\text{Machine}
}
$$

將只是：

$$
\boxed{
\text{Intelligence-Bearing Substrate}
}
$$

中的一種。

這就是 EXS-06 的主題。

---

# 參考文獻

[1] Microsoft. (2024). **Introducing Copilot+ PCs.** Microsoft 將 Copilot+ PC 定義為新一代 Windows PC 類別，使用具 $40+$ TOPS 能力的 NPU 支援本地 AI 工作負載與多項 Windows AI 功能。本文於 2026-08-18 重新核對。

[2] Microsoft. (2025–2026). **Copilot+ PCs vs. Windows PCs / Copilot+ PC developer guidance.** Microsoft 後續文件持續把至少 $40$ TOPS NPU、Windows 11 與本地 AI 功能列為 Copilot+ PC 的重要硬體／系統條件。

[3] Android Developers. (2023–2026). **A new foundation for AI on Android / Gemini Nano / AICore.** Android 將 AICore 定義為系統服務，使支援裝置可在本地執行 Gemini Nano 等 foundation model，並處理模型管理、runtime、安全能力與硬體利用。

[4] Google Android. (2026). **Gemini Nano.** 官方文件說明 Gemini Nano 透過 Android AICore system service 運行，以裝置硬體達成低延遲推論並保持模型更新。

[5] Apple. (2024). **Introducing Apple Intelligence for iPhone, iPad, and Mac.** Apple 將 Apple Intelligence 描述為 deeply integrated into iOS 18, iPadOS 18, and macOS Sequoia 的 personal intelligence system。

[6] Apple. (2024–2026). **Apple Intelligence.** Apple 官方資料持續描述 Apple Intelligence 透過 on-device processing 與 Private Cloud Compute 結合，並整合進 iPhone、iPad、Mac 與其他 Apple 裝置。

[7] NVIDIA. (2025). **Jetson Thor | Advanced AI for Physical Robotics.** NVIDIA 將 Jetson Thor 定位為 physical AI 與 robotics 平台，支援高效能即時推論、多模型與多感測工作負載。

[8] NVIDIA Developer. (2025). **Introducing NVIDIA Jetson Thor, the Ultimate Platform for Physical AI.** NVIDIA 指出 Jetson Thor 面向 generative reasoning、multimodal / multisensor processing 與 robotics workloads。

[9] NVIDIA. (2026). **Jetson Thor / T2000 physical AI edge systems.** NVIDIA 持續把 Thor 架構擴展到 visual AI agents、自主移動機器人與工業機械等 edge AI system。

[10] Apple. (2026). **Apple unveils next generation of Apple Intelligence, Siri AI and more.** Apple 進一步把 Siri AI 深度整合進多種裝置，並增加 systemwide app actions、personal context 與跨應用能力；本文把此作為 system-level AI integration 持續加深的案例，不把產品敘事直接等同本文的完整 AI-native 定義。

---

# 附錄 A｜最小符號表

| 符號 | 意義 |
|---|---|
| $S$ | 系統 |
| $A$ | AI 模型或 AI 層 |
| $A_C(S)$ | 系統的 AI 架構中心性 |
| $\mathbf A_C$ | AI 架構中心性向量 |
| $a_h$ | AI 硬體專用化 |
| $a_s$ | AI system-service 整合 |
| $a_d$ | AI 資料流依賴 |
| $a_i$ | AI 介面中介程度 |
| $a_c$ | AI 控制中心性 |
| $a_u$ | AI 模型更新／生命周期依賴 |
| $a_r$ | 移除 AI 後的重設計成本 |
| $\mathcal R_{\neg AI}(S)$ | 反事實 AI 移除測試 |
| $N_0-N_5$ | AI 架構原生性層級 |
| $L$ | EXS-04 的 AI 社會／功能域滲透度 |
| $D_{\mathrm{cap}}$ | EXS-02 的能力依賴深度 |
| $A_u$ | 自主性軸 |
| $S_u$ | 主體性證據軸，本文留空 |

---

# 附錄 B｜EXS-04 的 $L$ 軸與 EXS-05 的 $N$ 軸

EXS-04 問：

$$
\boxed{
\text{How deeply has AI penetrated a domain?}
}
$$

定義：

$$
L_0-L_7.
$$

EXS-05 問：

$$
\boxed{
\text{How deeply is AI constitutive of system architecture?}
}
$$

定義：

$$
N_0-N_5.
$$

所以：

$$
\boxed{
L\neq N.
}
$$

完整研究必須至少使用：

$$
\boxed{
(L,N,D_{\mathrm{cap}},A_u).
}
$$

---

# 附錄 C｜反事實 AI 移除測試

對任一系統：

$$
S.
$$

設定：

$$
A=0.
$$

觀察：

$$
\boxed{
\mathcal R_{\neg AI}(S).
}
$$

若：

$$
\mathcal R_{\neg AI}(S)\approx S,
$$

則 AI 架構中心性低。

若：

$$
\mathcal R_{\neg AI}(S)
=
\text{degraded }S,
$$

則 AI 可能依賴但非完全原生。

若：

$$
\mathcal R_{\neg AI}(S)
\notin
\text{same architectural class},
$$

則提供強 AI-native 證據。

---

# 附錄 D｜EXS 系列累積鏈

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

EXS-05：

$$
\boxed{
\text{AI Capability}
\neq
\text{AI Architectural Nativity}.
}
$$

---

# 附錄 E｜下一篇接口

**EXS-06｜機器不是終點：數位、生物、混合與分散式智能載體**
**從 AI 機器到 Intelligence-Bearing Substrate**

下一篇將正式把：

$$
\boxed{
\text{Machine}
}
$$

降為更一般集合：

$$
\boxed{
\text{Intelligence-Bearing Substrate}.
}
$$

並區分：

$$
S_D
=
\text{digital substrate},
$$

$$
S_M
=
\text{mechanical/robotic substrate},
$$

$$
S_B
=
\text{biological substrate},
$$

$$
S_H
=
\text{hybrid substrate},
$$

$$
S_N
=
\text{network/distributed substrate}.
$$

核心問題將從：

> 「AI 在不在機器裡？」

轉為：

> 「智能由什麼基質承載、跨多少節點存在、其邊界如何被定義？」

這將是從 AI 架構分類進入智能載體本體論的正式接口。
