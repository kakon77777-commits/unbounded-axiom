# Poker、卡牌遊戲與 Human–AI Hybrid：從 Bot、Solver、RTA 到決策來源危機

## Poker, Card Games, and Human–AI Hybrids: From Bots and Solvers to Real-Time Assistance and the Crisis of Decision Provenance

**Series:** AI Game Intelligence, Randomness, and Adaptive Markets  
**Paper 06**  
**Version:** v0.1  
**Date:** 2026-09-02
**Author:** Neo.K with Aletheia（GPT-5.6 Sol）  
**Institution:** EveMissLab／一言諾科技有限公司

---

## 摘要

Poker 與策略卡牌遊戲標誌著本系列的一次根本轉折。

在輪盤、老虎機與大量莊家制遊戲中，人工智慧面對的主要問題是隨機生成機制、固定賠付結構與制度允許邊界；在 Poker 類不完全資訊策略遊戲中，玩家面對的則是另一個會觀察、推斷、欺騙、調整與學習的智能體。

因此，問題從：

$$
\text{Player vs Mechanism}
$$

轉變為：

$$
\boxed{
\text{Intelligence vs Intelligence}.
}
$$

Poker AI 的歷史已證明，這類遊戲中人工智慧可以形成超越頂尖人類的策略能力。Libratus 在雙人無限注德州撲克中擊敗頂尖職業玩家；Pluribus 隨後在六人無限注德州撲克中達成超人類表現。這表示「AI 是否可以在 Poker 中顯著改善策略品質」早已不是理論問題。

真正的新問題是：當這種能力從研究環境進入真實線上遊戲，平台如何區分合法學習與即時外部決策？

本文建立以下演化鏈：

$$
\boxed{
\text{Bot}
\rightarrow
\text{Solver}
\rightarrow
\text{RTA}
\rightarrow
\text{Human--AI Hybrid}
\rightarrow
\text{Decision Provenance}.
}
$$

早期 bot 直接替玩家執行動作，因此可以透過滑鼠、時間、程序與自動化行為辨識。Solver 時代則使玩家可以在遊戲外研究近似均衡策略。Real-Time Assistance 進一步把 solver 帶進即時決策週期。生成式 AI、vision model 與第二裝置又使問題更困難：玩家本人可能仍在操作 client，但實際決策可能由另一個模型產生。

因此：

$$
\boxed{
\text{Human Action}
\not\Rightarrow
\text{Human-Generated Decision}.
}
$$

本文將「誰執行動作」與「誰生成決策」正式分離，提出：

$$
\boxed{
\text{Action Provenance}
}
$$

與：

$$
\boxed{
\text{Decision Provenance}.
}
$$

現代線上 Poker 平台也正在從單純抓自動 bot，演化為多層 Game Integrity。PokerStars 的現行規則禁止 bot、AI 即時建議、進階 equity、ICM 與 Nash-equilibrium 類即時工具；GGPoker 2026 年政策則明確禁止 RTA、AI bot、solver、chart、HUD、remote-access tool、virtual machine 等多種可能提供不公平即時輔助的工具。PokerStars 亦公開表示其 Game Integrity 系統會分析數以千億計手牌與玩家策略／行為特徵，而 GGPoker 已與 GTO Wizard 合作，利用 Fair Play Check 與策略接近度分析輔助偵測 RTA。

因此，反作弊也出現對稱演化：

$$
\boxed{
\text{AI for Play}
\rightarrow
\text{AI for Detection}.
}
$$

本文最後將這一問題延伸到 Hearthstone、MTG Arena 與其他策略卡牌遊戲。這些遊戲雖不一定直接涉及每局金錢輸贏，但 bot、帳戶 farming、即時建議、資料不對稱與 matchmaking manipulation 仍會破壞競技公平。平台的反制也開始從單純封號，擴張到改變 matchmaking topology，使特定極端行為彼此匹配。

本文不提供 RTA、bot、自動遊戲、第二裝置輔助、反偵測或規避平台安全機制的實作方法。本篇研究的是策略智能、決策來源、公平競技與反 AI 治理。

---

# 1. 從 Paper 05 跨入 Intelligence vs Intelligence

Paper 05 的莊家制遊戲主要可寫成：

$$
\pi^*
=
\arg\max_{\pi\in\Pi}
E[R\mid G,S,P].
$$

其中規則：

$$
G
$$

大致由營運者固定。

Poker 則不同。

對手策略：

$$
\pi_{-i}
$$

本身也是環境的一部分。

因此玩家 $i$ 的效用：

$$
U_i
=
U_i(
\pi_i,
\pi_{-i},
S
).
$$

最佳策略不只依賴牌面，還依賴其他智能體如何行動。

---

# 2. Poker 是不完全資訊博弈

在 Poker 中，每個玩家只看到自己的資訊集合：

$$
I_i.
$$

但完整世界狀態：

$$
S
$$

包含其他玩家的 hole cards。

因此：

$$
I_i\subset S.
$$

玩家必須根據：

$$
I_i
$$

推測：

$$
P(S\mid I_i).
$$

這與完整資訊棋類有根本差異。

---

# 3. 策略不是單一答案

Poker 策略可寫為：

$$
\pi_i(a\mid I_i).
$$

其中：

$$
a\in A(I_i).
$$

合理策略往往不是：

> 這裡一定下注。

而是：

$$
P(\text{bet})=p_1,
$$

$$
P(\text{check})=p_2,
$$

$$
P(\text{raise})=p_3.
$$

即混合策略。

---

# 4. 不可預測性本身成為策略資產

如果玩家在某狀態：

$$
I
$$

永遠採取同一動作，

對手可以更新：

$$
P(H\mid a,I)
$$

並利用其規律。

因此 Poker 智能不只是：

$$
\text{find best move},
$$

而包含：

$$
\boxed{
\text{maintain strategically appropriate uncertainty}.
}
$$

這也是 AI 在 Poker 中具有巨大優勢的一個原因：它可以更一致地執行複雜 mixed strategy。

---

# 5. AI Poker 已經證明可以達到超人類策略能力

2017 年 Libratus 在雙人無限注 Texas Hold'em 中擊敗四名頂尖職業玩家。

2019 年 Carnegie Mellon University 與 Facebook AI 共同開發的 Pluribus 進一步在六人無限注 Texas Hold'em 中擊敗多名頂尖職業玩家。

因此：

$$
\boxed{
\text{AI strategic superiority in poker is empirically established}.
}
$$

真正剩下的問題不是：

> AI 會不會玩？

而是：

> AI 在什麼時候被允許參與？

---

# 6. Pluribus 的理論意義

Pluribus 的突破不只是算得更快。

它需要在多人、不完全資訊、非零和近似、對手策略多樣的環境中行動。

這使 Poker 成為 AI strategic reasoning 的代表性問題之一。

因此：

$$
\boxed{
\text{Poker AI}
}
$$

不應被理解成單純機率計算器。

它是一種：

$$
\boxed{
\text{belief modelling}
+
\text{counterfactual reasoning}
+
\text{strategic randomization}
+
\text{adaptation}.
}
$$

---

# 7. Poker AI 的第一個合法場域：離線學習

如果一名玩家在牌局結束後把自己的 hand history 交給 solver 或 AI：

$$
H_{\mathrm{past}}
\rightarrow
\text{analysis},
$$

並用它改善未來能力，

這可理解為：

$$
\boxed{
\text{training assistance}.
}
$$

它和讀書、找教練、看錄影具有相似功能。

---

# 8. Training Assistance 與 Real-Time Assistance

真正的界線在時間。

離線：

$$
t_{\mathrm{advice}}>t_{\mathrm{decision}}.
$$

即時：

$$
t_{\mathrm{advice}}\leq t_{\mathrm{decision}}.
$$

若外部系統在當前 hand 還可被影響時提供具體策略建議，就進入：

$$
\boxed{
\text{Real-Time Assistance}.
}
$$

---

# 9. 為什麼 RTA 特別具有破壞性

一個人類玩家原本具有能力上限：

$$
C_H.
$$

外部 AI 的能力：

$$
C_A.
$$

若即時把：

$$
C_A
$$

接入每個 decision point，

有效決策能力可能變成：

$$
C_{\mathrm{hybrid}}
>
C_H.
$$

因此平台上的 account identity：

$$
\text{Account}=\text{Human}
$$

不再代表：

$$
\text{Decision System}=\text{Human}.
$$

---

# 10. 第一階段：Fully Automated Bot

早期 bot 可以抽象為：

$$
S_t
\rightarrow
M
\rightarrow
a_t.
$$

人類不需要參與。

因此：

$$
\boxed{
\text{decision generation}
=
\text{machine},
}
$$

且：

$$
\boxed{
\text{action execution}
=
\text{machine}.
}
$$

這是最容易理解的作弊類型。

---

# 11. Fully Automated Bot 的傳統痕跡

早期平台可以觀察：

- mouse trajectory；
- click behaviour；
- response timing；
- session duration；
- repetitive patterns；
- identical strategies；
- software processes。

PokerStars 回顧其早期 bot detection 時表示，平台曾利用只有人類滑鼠操作會出現的行為差異辨認 fully automated bots。

因此早期 anti-bot 可以主要依賴：

$$
D_{\mathrm{device}}
+
D_{\mathrm{timing}}
+
D_{\mathrm{execution}}.
$$

---

# 12. 第二階段：Solver

Solver 不需要替玩家操作。

它只需要回答：

$$
\pi^*(a\mid I).
$$

玩家可以：

1. 在遊戲外建立解；
2. 研究 range；
3. 學習 bet sizing；
4. 改善策略。

只要不在牌局進行中直接提供即時決策，這類工具在不同平台通常具有較寬鬆的合法或允許空間。

---

# 13. Solver 改變了「人類最佳玩法」本身

當頂尖玩家使用 solver 學習：

$$
\pi^*,
$$

人類 meta 會逐漸：

$$
\pi_H
\rightarrow
\pi_{\mathrm{solver-informed}}.
$$

因此 AI 即使沒有出現在正式比賽時，

仍然改變了：

$$
\boxed{
\text{human strategic baseline}.
}
$$

這與 Paper 03 的 AI market efficiency 類似。

---

# 14. AI 外部化成文化

一旦 solver 策略被：

- 教學；
- 影片；
- chart；
- coaching；
- community；

吸收，

原本的：

$$
\text{machine knowledge}
$$

會轉化為：

$$
\boxed{
\text{human strategic culture}.
}
$$

因此不能把「使用 AI 學習」與「AI 即時替你決策」混為一談。

---

# 15. 第三階段：Push-This-Button Bot

PokerStars 使用 PTBB 一詞描述：

$$
\boxed{
\text{machine decides}
+
\text{human executes}.
}
$$

可寫成：

$$
S_t
\rightarrow
M
\rightarrow
a_t^*
\rightarrow
H
\rightarrow
\text{click}.
$$

最後滑鼠確實是人按的。

但：

$$
\boxed{
\text{decision origin}
=
\text{machine}.
}
$$

---

# 16. PTBB 揭露 Action 與 Decision 的分裂

設：

$$
A_P
=
\text{Action Provenance},
$$

$$
D_P
=
\text{Decision Provenance}.
$$

對一般人類：

$$
A_P=H,
$$

$$
D_P=H.
$$

對 fully automated bot：

$$
A_P=M,
$$

$$
D_P=M.
$$

對 PTBB：

$$
A_P=H,
$$

但：

$$
D_P=M.
$$

這就是本篇最重要的新分類。

---

# 17. 第四階段：Real-Time Assistance

RTA 比 PTBB 更廣。

外部系統不一定直接輸出：

> Raise.

它也可能提供：

- range；
- recommended frequency；
- equity；
- ICM；
- Nash-equilibrium analysis；
- situation-specific chart。

只要資訊是針對當前 game state，並在決策仍可修改時提供，就可能影響 decision provenance。

---

# 18. PokerStars 的現行規則

PokerStars 現行第三方工具政策禁止：

- 無人介入 bot；
- 降低人類決策需求的工具；
- 即時讀取 game state 並建議行動的工具；
- hole-card sharing；
- datamining；
- 遊戲進行中使用進階 equity、ICM 或 Nash-equilibrium 類工具。

PokerStars 也明確表示，真人必須自己決定動作以及下注／加注的相對大小。

因此平台的規則核心已不是：

$$
\boxed{
\text{human physically clicks}.
}
$$

而是：

$$
\boxed{
\text{human must make the decision}.
}
$$

---

# 19. GGPoker 的 2026 RTA 定義

GGPoker 2026 年 Security & Ecology Policy 定義 RTA 為任何：

$$
\boxed{
\text{external assistance}
}
$$

只要其：

- 提供不公平優勢；
- 即時影響決策；
- 使玩家能做到原本無法自行複製的玩法；

都可能落入 RTA。

政策甚至明確寫：

$$
\boxed{
\text{Every decision at the table should be free of external assistance}.
}
$$

---

# 20. GGPoker 的 Bot 定義也包含 AI

現行政策將 bot 定義為：

- software；
- program；
- website；
- app；

只要它可以：

$$
\text{play without human intervention}
$$

或：

$$
\text{reduce the requirement of human decision/action}.
$$

並明確包含：

$$
\boxed{
\text{artificial intelligence}
}
$$

以及 fully / partially automated bots。

---

# 21. 現代平台開始禁止「輔助環境」

GGPoker 2026 政策除 RTA 與 bots 外，也禁止多類可能改變即時公平性的工具，包括：

- solver；
- chart；
- HUD；
- automated note-taking；
- remote-access software；
- virtual machine；
- emulator；
- location-masking tools；
- game-data extraction tool。

這反映平台已不再只防一個叫做：

$$
\text{bot.exe}
$$

的程式。

而是在治理：

$$
\boxed{
\text{decision-support environment}.
}
$$

---

# 22. 第五階段：Human--AI Hybrid

生成式 AI 使決策輔助更自然。

不再需要專門 Poker solver interface。

一般模型可能具備：

- vision；
- natural-language reasoning；
- tool use；
- memory；
- voice output。

因此：

$$
\boxed{
\text{general AI}
}
$$

本身就可能成為一個 strategy interface。

---

# 23. Human--AI Hybrid 不一定自動化

系統可能：

$$
\text{observe}
\rightarrow
\text{reason}
\rightarrow
\text{suggest},
$$

而人：

$$
\text{accept/reject}
\rightarrow
\text{act}.
$$

所以：

$$
\boxed{
\text{human remains in the loop}
}
$$

並不足以證明公平。

因為 human-in-the-loop 可以只是：

$$
\boxed{
\text{execution relay}.
}
$$

---

# 24. Decision Contribution 是連續量

真實 Human--AI hybrid 不一定只有：

$$
0\%
$$

或：

$$
100\%
$$

機器決策。

可以定義概念上的：

$$
\alpha_A\in[0,1]
$$

表示 AI 對最終策略決策的貢獻程度。

則：

$$
D
=
F(
D_H,
D_A,
\alpha_A
).
$$

問題是：

$$
\boxed{
\alpha_A
}
$$

在外部通常不可直接觀測。

---

# 25. Assistance Continuum

本文提出六級分類：

### H0 — Human Only

$$
D_P=H.
$$

### H1 — Pre-Game AI Training

AI 只在正式遊戲之前提供一般訓練。

### H2 — Static In-Game Reference

遊戲時使用固定、不讀取當前 state 的參考資料。

其是否允許取決於平台規則。

### H3 — State-Aware RTA

AI 讀取當前狀態並提供即時建議。

### H4 — Human-Executed Machine Decision

AI 決定具體行動，人只負責執行。

### H5 — Fully Automated Bot

AI 同時決策與執行。

這個 continuum 比「人類／bot」二分更符合 AI 時代。

---

# 26. 第二裝置問題

假設 Poker client 運行在：

$$
D_1.
$$

外部 AI 運行在：

$$
D_2.
$$

兩者沒有軟體連線。

例如：

$$
D_2
$$

只透過外部感測取得畫面資訊。

此時：

$$
\boxed{
\text{client-side process scan}
}
$$

可能完全看不到：

$$
D_2.
$$

這就是：

$$
\boxed{
\text{Second-Device Problem}.
}
$$

---

# 27. 第二裝置問題不是某個特定作弊工具

它是一個更一般的系統原理：

$$
\boxed{
\text{Decision computation can be physically decoupled from action execution}.
}
$$

只要：

$$
\text{observation channel}
$$

與：

$$
\text{advice channel}
$$

存在，

運算設備不必和 client 位於同一台機器。

---

# 28. 這使 Process Detection 不再充分

傳統：

$$
D_{\mathrm{process}}
$$

可能檢查：

- 程序；
- DLL；
- memory；
- window；
- known solver。

第二裝置存在時：

$$
D_{\mathrm{process}}\approx0
$$

並不意味：

$$
P(\mathrm{RTA})=0.
$$

因此：

$$
\boxed{
\text{absence of local tool evidence}
\not\Rightarrow
\text{absence of external decision assistance}.
}
$$

---

# 29. 平台因此必須轉向 Behaviour

現代反作弊逐漸研究：

$$
\pi_{\mathrm{player}}(a\mid I).
$$

如果它在大量罕見決策點上突然異常接近：

$$
\pi^*(a\mid I),
$$

可能提高：

$$
P(\mathrm{RTA}\mid D).
$$

但這仍然不能單獨構成證明。

---

# 30. 為什麼不能「玩得太好就封」

因為真正頂尖玩家本來就可能：

$$
D(
\pi_H,
\pi^*
)
\ll1.
$$

而 solver culture 又會使人類策略逐年接近 equilibrium-informed play。

因此：

$$
\boxed{
\text{strategy optimality}
\neq
\text{proof of machine assistance}.
}
$$

---

# 31. False Positive 問題

若平台只以：

$$
D(\pi,\pi^*)<\tau
$$

判定作弊，

頂尖玩家會有：

$$
P(\text{false positive})
$$

問題。

因此 anti-RTA 必須使用多證據融合。

---

# 32. Modern Integrity Evidence Stack

本文提出：

$$
\boxed{
E=
(
E_{\mathrm{device}},
E_{\mathrm{timing}},
E_{\mathrm{strategy}},
E_{\mathrm{behaviour}},
E_{\mathrm{graph}},
E_{\mathrm{external}},
E_{\mathrm{human}}
).
}
$$

任何單一維度都不應理想化為完美 detector。

---

# 33. Device Evidence

包括平台依法與依條款可觀察的：

- running tools；
- remote-access state；
- VM / emulator；
- known prohibited software。

其優點是直接。

缺點是第二裝置可能繞開這一層。

---

# 34. Timing Evidence

對某些外部查詢系統，玩家可能呈現：

$$
T_{\mathrm{response}}
$$

與問題複雜度異常相關。

但：

$$
\boxed{
\text{slow decision}
\neq
\text{RTA}.
}
$$

正常人也會思考。

因此 timing 只能作為聯合證據。

---

# 35. Strategy Evidence

分析：

$$
D(
\pi_{\mathrm{player}},
\pi^*
).
$$

不只看整體 EV loss，

還可以研究：

- rare spots；
- mixed-frequency accuracy；
- unusual bet sizes；
- obscure lines。

真正可疑的可能不是：

$$
\text{high skill},
$$

而是：

$$
\boxed{
\text{skill profile inconsistent with the player's own historical manifold}.
}
$$

---

# 36. Behavioural Baseline

設玩家過往分布：

$$
\pi_i^{(0)}.
$$

目前時間窗口：

$$
\pi_i^{(1)}.
$$

定義：

$$
\Delta_i
=
D(
\pi_i^{(1)},
\pi_i^{(0)}
).
$$

若：

$$
\Delta_i\gg0,
$$

只表示：

$$
\boxed{
\text{behavioural regime change}.
}
$$

仍需要解釋原因。

---

# 37. Cognitive Regime Shift

一名玩家可能因：

- coaching；
- study；
- fatigue；
- tilt；
- game selection；
- legitimate improvement；

而改變策略。

因此：

$$
\boxed{
\text{behavioural discontinuity}
\neq
\text{machine substitution}.
}
$$

這也是 Cognitive Forensics 必須非常保守的原因。

---

# 38. Graph Evidence

多人 Poker 還有：

$$
\text{collusion}.
$$

因此平台可建立：

$$
G=(V,E)
$$

其中節點可能是：

- accounts；
- devices；
- locations；
- financial relations；
- repeated tables。

邊：

$$
E_{ij}
$$

表示可疑相關。

這與單一 RTA 問題不同，但可以聯合出現。

---

# 39. External Evidence

2025 年 GGPoker 與 GTO Wizard 的合作代表一個新方向：

$$
\boxed{
\text{Poker Platform}
+
\text{Solver Provider}
}
$$

共同處理 Game Integrity。

GGPoker 公開表示，利用 GTO Wizard 的 game-integrity services，封鎖了：

$$
31
$$

個違反 fair-play rule 的帳號。

這是一個重要制度轉折。

---

# 40. Fair Play Check

GTO Wizard 的 Fair Play Check 可以驗證：

$$
\boxed{
\text{a particular board}
}
$$

是否在指定時間範圍內曾於其服務被 solve。

因此可以把：

$$
t_{\mathrm{hand}}
$$

與：

$$
t_{\mathrm{solver}}
$$

進行證據對照。

這不是普遍監控所有外部 AI 的萬能方法，但它展示：

$$
\boxed{
\text{external computation can itself leave provenance evidence}.
}
$$

---

# 41. Solver Provider 也開始成為 Integrity Infrastructure

GTO Wizard 的 Game Integrity 服務還提供：

- Fair Play Check automation；
- GTO reports；
- superhuman-play detection；
- player strategy 與 optimal strategy closeness assessment。

這代表原本提供：

$$
\text{strategy intelligence}
$$

的公司，也開始提供：

$$
\boxed{
\text{strategy provenance evidence}.
}
$$

---

# 42. AI 防 AI

因此出現一個對稱結構：

$$
\boxed{
M_{\mathrm{play}}
\leftrightarrow
M_{\mathrm{detect}}.
}
$$

攻擊端：

$$
\text{AI improves decisions}.
$$

防守端：

$$
\text{AI detects statistically implausible decision patterns}.
$$

這是一個真正的 adaptive adversarial ecology。

---

# 43. PokerStars 的 Game Integrity 規模

PokerStars 2025 年公開表示其 Game Integrity 團隊約有數十名專職專家、程式設計師、分析師與前職業 Poker 玩家，並可以使用平台累積超過：

$$
235\text{ billion}
$$

手牌進行分析。

平台表示自動系統會持續 flag 可疑帳號，再交由專門人員調查。

因此防守方具有：

$$
\boxed{
\text{server-side population-scale data advantage}.
}
$$

---

# 44. 伺服器的 God's-Eye View

單一玩家只看：

$$
I_i.
$$

平台則知道：

- 所有合法 server state；
- action sequence；
- timing；
- account history；
- game outcomes；
- table graph。

在牌局完成後，平台通常擁有比任何單一玩家完整得多的：

$$
S.
$$

因此：

$$
\boxed{
\text{player AI advantage}
}
$$

不代表：

$$
\boxed{
\text{player has the better forensic dataset}.
}
$$

---

# 45. PokerStars 不依賴單一「抓螢幕」方法

PokerStars 2025 年公開說明其反作弊會分析 gameplay 與 behavioural tendency，同時表示其並不以抓取玩家螢幕內容作為手段。

這是一個重要治理信號：

$$
\boxed{
\text{anti-cheat power}
}
$$

必須與：

$$
\boxed{
\text{privacy constraint}
}
$$

共同考慮。

---

# 46. Privacy--Integrity Tradeoff

如果平台要求：

- webcam；
- full-screen capture；
- room scan；
- second-device inspection；

可以提高某些偵測能力。

但會增加：

$$
C_{\mathrm{privacy}}.
$$

因此平台治理目標不是單純：

$$
\max Detection.
$$

而更接近：

$$
\max
\left[
Integrity
-\lambda PrivacyCost
-\gamma FalsePositiveCost
\right].
$$

---

# 47. False Positive 也是公平性問題

如果 anti-AI 系統錯誤封鎖：

$$
H_{\mathrm{elite}},
$$

那麼：

$$
\boxed{
\text{anti-cheat itself becomes a source of unfairness}.
}
$$

所以：

$$
\text{high sensitivity}
$$

與：

$$
\text{high specificity}
$$

必須同時考慮。

---

# 48. Human Review 不能完全消失

平台的機器模型可以輸出：

$$
P(\mathrm{violation}\mid E).
$$

但對高影響處置：

$$
\text{ban},
$$

$$
\text{fund confiscation},
$$

理想制度仍需要：

$$
\boxed{
\text{multi-evidence human review}.
}
$$

PokerStars 公開描述其案件會由專門人員處理並進行複核。

---

# 49. Decision Provenance

本文正式定義：

$$
\boxed{
D_P(d)
=
\text{provenance of the cognitive process generating decision }d.
}
$$

它和：

$$
A_P(a)
=
\text{provenance of the physical action executing }a
$$

不同。

---

# 50. Decision Provenance 為什麼比 Identity 更重要

傳統線上平台驗證：

$$
\text{Who owns the account?}
$$

但 AI 時代還必須問：

$$
\boxed{
\text{What system generated the decision?}
}
$$

同一個 verified human account 可以對應：

$$
D_P=H,
$$

也可以對應：

$$
D_P=H+A,
$$

甚至：

$$
D_P=A.
$$

---

# 51. Decision Provenance 不是二元變數

可以把決策表示成：

$$
d
=
F(
H,
A,
R,
E
),
$$

其中：

$$
H=\text{human reasoning},
$$

$$
A=\text{AI assistance},
$$

$$
R=\text{reference material},
$$

$$
E=\text{environmental information}.
$$

因此真正的問題是：

$$
\boxed{
\text{which contributions are permitted?}
}
$$

而不是：

$$
\boxed{
\text{was AI present at all?}
}
$$

---

# 52. Fairness 是制度定義，不是自然常數

某平台可能允許：

$$
H1
$$

即 AI 離線訓練。

禁止：

$$
H3,H4,H5.
$$

另一個教育型遊戲可能允許：

$$
H2.
$$

所以：

$$
\boxed{
\text{Fairness}
=
F(
rules,
expectations,
disclosure,
symmetry
).
}
$$

不存在跨所有遊戲唯一固定的 AI fairness boundary。

---

# 53. Symmetry Principle

如果某競賽明確允許所有玩家使用同一類 AI：

$$
A_{\mathrm{allowed}},
$$

那麼 AI 本身可能從：

$$
\text{unfair assistance}
$$

變成：

$$
\boxed{
\text{part of the game}.
}
$$

因此核心問題之一是：

$$
\boxed{
\text{Are capabilities symmetrically available and explicitly permitted?}
}
$$

---

# 54. 但對稱工具仍可能改變遊戲本體

即使每個人都可以用 AI，

遊戲仍可能從：

$$
\text{human strategy competition}
$$

轉變成：

$$
\text{AI selection/orchestration competition}.
$$

所以：

$$
\boxed{
\text{equal access}
\neq
\text{same game identity}.
}
$$

這是競技治理很深的問題。

---

# 55. Poker 為什麼特別敏感

Poker 的文化價值部分來自：

- bluff；
- read；
- adaptation；
- uncertainty；
- human inconsistency。

若即時 solver 完全主導：

$$
\pi_H
\rightarrow
\pi_A,
$$

競技本體可能從：

$$
\boxed{
\text{human strategic reasoning}
}
$$

變成：

$$
\boxed{
\text{tool-mediated equilibrium execution}.
}
$$

平台因此有理由把「人本人作決策」寫成核心規則。

---

# 56. Card Games 不一定有直接金錢賭注

Hearthstone、MTG Arena 等遊戲通常不是每局直接：

$$
\text{win money / lose money}.
$$

但仍存在：

- rank；
- rewards；
- account progression；
- tournament qualification；
- time value；
- account economy。

因此 bot 與 AI assistance 仍會創造：

$$
\boxed{
\text{competitive and economic externality}.
}
$$

---

# 57. Card-Game Bot 的目標可以是 Grinding

某 bot 不需要：

$$
EV_{\mathrm{cash}}>0.
$$

只要：

$$
Reward_{\mathrm{time}}
>
Cost_{\mathrm{automation}},
$$

就可能有誘因持續運行。

因此：

$$
\boxed{
\text{bot economics}
}
$$

與 Poker RTA 不完全相同。

---

# 58. Hearthstone 的大規模 Bot 問題

Blizzard 在 2024 年公開多次進行大規模 bot enforcement，其中一輪表示自前次更新後又處理超過：

$$
240,000
$$

個帳號。

這顯示：

$$
\boxed{
\text{detection}
\neq
\text{permanent elimination}.
}
$$

若新帳號成本足夠低，bot ecology 可以持續再生。

---

# 59. Bot Ecology

可以寫成：

$$
N_{t+1}
=
N_t
+
B_t
-
D_t,
$$

其中：

$$
B_t=\text{new bot creation},
$$

$$
D_t=\text{detected/removed bots}.
$$

只要：

$$
B_t\geq D_t,
$$

總 bot population 就不會下降。

因此：

$$
\boxed{
\text{ban rate alone}
}
$$

不是完整治理指標。

---

# 60. 平台可以直接改變遊戲拓樸

Hearthstone 2024 年 Arena 的一項措施很有代表性。

針對反覆提前 retire、持續重抽直到拿到極強牌組的極端行為，Blizzard 並沒有完全刪除 retire 功能，而是讓這類玩家進入另一個 matchmaking pool。

因此：

$$
\boxed{
\text{strategy}
\rightarrow
\text{topology response}.
}
$$

---

# 61. Matchmaking Topology as Countermeasure

設一般玩家池：

$$
P_0.
$$

極端策略玩家：

$$
P_E.
$$

平台可以把：

$$
P_E
$$

重新映射到：

$$
P_1.
$$

使其：

$$
\boxed{
\text{mainly compete with similar strategies}.
}
$$

這種治理不一定需要判定：

> 你是不是作弊。

而是直接降低某種行為對一般生態的外部性。

---

# 62. 這和美國 CAW 很像

Paper 03 中 NYRA 不是禁止所有電腦模型。

它改的是：

$$
\text{execution timing topology}.
$$

Hearthstone 的例子則改：

$$
\text{matchmaking topology}.
$$

兩者共同反映：

$$
\boxed{
\text{platform can neutralize an advantage by changing the game environment}.
}
$$

---

# 63. Wizards 的一般反作弊邊界

Wizards of the Coast 現行 Terms 禁止：

- unauthorized data mining；
- bots；
- hacks；
- 未授權 software / code；
- 使使用者相對未使用者取得優勢的工具。

因此策略卡牌遊戲同樣面臨：

$$
\boxed{
\text{authorized assistance boundary}.
}
$$

而不是只有真錢 Poker 才有這個問題。

---

# 64. Deck Tracker 與 RTA 的界線會越來越困難

一般 deck tracker 可能只是：

$$
\text{memory externalization}.
$$

但加入：

$$
\text{opponent model}
+
\text{current-state solve}
+
\text{action recommendation},
$$

就會逐步走向：

$$
\boxed{
\text{decision substitution}.
}
$$

因此未來規則不應只按工具名稱分類，而需要按：

$$
\boxed{
\text{function}
}
$$

分類。

---

# 65. Functional Assistance Taxonomy

本文建議以功能分成：

$$
F_0=\text{record},
$$

$$
F_1=\text{summarize},
$$

$$
F_2=\text{calculate static information},
$$

$$
F_3=\text{infer hidden state},
$$

$$
F_4=\text{recommend action},
$$

$$
F_5=\text{execute action}.
$$

越往後：

$$
\text{decision substitution}\uparrow.
$$

---

# 66. 這比「是不是 AI」更穩定

因為未來：

$$
\text{AI}
$$

會出現在幾乎所有軟體。

所以規則若只寫：

> 禁止 AI。

會變得非常模糊。

更合理是：

$$
\boxed{
\text{禁止哪些功能在什麼時間介入決策}.
}
$$

---

# 67. Temporal Assistance Boundary

同一個工具在：

$$
t<t_{\mathrm{match}}
$$

可能是合法 trainer。

在：

$$
t=t_{\mathrm{decision}}
$$

可能成為 prohibited RTA。

因此 permission 應該寫成：

$$
P(
F,
t,
state-awareness
).
$$

---

# 68. State Awareness 是核心變數

一般教學：

$$
A(\text{generic poker theory})
$$

與：

$$
A(I_t)
$$

完全不同。

第二者知道：

$$
\boxed{
\text{the exact current decision state}.
}
$$

因此 RTA governance 的重要軸應包含：

$$
\boxed{
\text{state awareness}.
}
$$

---

# 69. Decision Specificity

另一個軸是建議是否具體。

低 specificity：

> 考慮 pot odds。

高 specificity：

> 此處採取某個特定 action。

所以可定義：

$$
S_D\in[0,1].
$$

當：

$$
S_D\uparrow,
$$

decision substitution 通常也提高。

---

# 70. Human Cognitive Work Requirement

本文再定義：

$$
C_H
=
\text{remaining human cognitive work}.
$$

對純 coaching：

$$
C_H\approx1.
$$

對 PTBB：

$$
C_H\approx0.
$$

因此一個公平競技規則可以關心：

$$
\boxed{
\text{how much strategic cognition remains with the registered player}.
}
$$

---

# 71. Decision Substitution Index

概念上可定義：

$$
DSI
=
f(
A_S,
S_D,
T_R,
C_H^{-1}
),
$$

其中：

$$
A_S=\text{state awareness},
$$

$$
S_D=\text{decision specificity},
$$

$$
T_R=\text{real-time coupling},
$$

$$
C_H=\text{remaining human cognitive work}.
$$

越高表示外部系統越接近替代玩家本人的決策角色。

---

# 72. 這比 Bot / Not Bot 更能描述未來

未來可能出現：

- AI whisper coach；
- augmented-reality advice；
- multimodal assistant；
- partial recommendation；
- probability overlay。

這些未必是 full bot。

但：

$$
DSI
$$

可能非常高。

因此：

$$
\boxed{
\text{automation level}
\neq
\text{decision substitution level}.
}
$$

---

# 73. Decision Provenance Crisis

當：

$$
A_P=H
$$

而：

$$
D_P
$$

不可直接觀測，

平台會遇到：

$$
\boxed{
\text{Decision Provenance Crisis}.
}
$$

即：

> 可以驗證是誰按下按鈕，卻無法直接驗證是誰產生策略。

這是生成式 AI 時代的新公平性核心。

---

# 74. 這不只是 Poker

同樣問題可以出現在：

- Chess；
- Go；
- competitive card games；
- esports；
- online examinations；
- coding competitions；
- remote professional assessments。

只要：

$$
\boxed{
\text{human identity is verified}
}
$$

但：

$$
\boxed{
\text{cognitive origin is externally augmentable},
}
$$

Decision Provenance 就成為問題。

---

# 75. Cognitive Forensics

本文把從行為結果推斷可能決策來源的研究方向稱為：

$$
\boxed{
\text{Cognitive Forensics}.
}
$$

其目的不是讀心。

而是估計：

$$
P(
D_P
\mid
E_{\mathrm{observable}}
).
$$

---

# 76. Cognitive Forensics 不應宣稱完美確定性

因為：

$$
P(D_P\mid E)
$$

永遠受：

- model uncertainty；
- human variability；
- legitimate learning；
- incomplete evidence；

影響。

所以結果更應是：

$$
\boxed{
\text{evidence-weighted attribution}.
}
$$

而不是：

$$
\boxed{
\text{mathematical proof of cognition source}.
}
$$

---

# 77. Detection 也會產生 Adversarial Adaptation

一旦平台公開 detector：

$$
D,
$$

作弊者就會優化：

$$
\min
P_D(\text{detected}).
$$

因此形成：

$$
D_t
\rightarrow
A_{t+1}
\rightarrow
D_{t+1}.
$$

這就是：

$$
\boxed{
\text{anti-cheat arms race}.
}
$$

---

# 78. 不應公開過度具體的反偵測細節

完整研究可以分析：

$$
\text{classes of signals},
$$

但若公開：

- exact thresholds；
- exact timing signatures；
- exact evasion patterns；

反而可能降低平台安全。

因此本系列只描述：

$$
\boxed{
\text{defensive principles}
}
$$

不提供規避方法。

---

# 79. AI Game Integrity 的六層防禦

本文將現代公平競技防禦濃縮為：

$$
\boxed{
\begin{array}{c}
\text{Layer 1: Rules}\\
\text{Layer 2: Client/Environment}\\
\text{Layer 3: Behaviour}\\
\text{Layer 4: Strategy}\\
\text{Layer 5: Graph/External Evidence}\\
\text{Layer 6: Human Adjudication}
\end{array}
}
$$

真正強的系統不依賴單一 detector。

---

# 80. Rules Layer

最先必須清楚定義：

$$
\boxed{
\text{what assistance is allowed}.
}
$$

規則模糊時，再好的 detector 也無法產生正當處置。

---

# 81. Environment Layer

目的不是全面監控私人裝置。

而是在合理權限內辨識：

$$
\text{known prohibited interaction}.
$$

並受：

$$
\text{privacy proportionality}
$$

限制。

---

# 82. Behaviour Layer

建立：

$$
\pi_i^{\mathrm{history}}
$$

與：

$$
\pi_i^{\mathrm{current}}
$$

的比較。

重點是 regime change，不是「高手就是作弊」。

---

# 83. Strategy Layer

研究：

$$
D(
\pi_i,
\pi^*
).
$$

但必須和玩家能力、stake、history 及罕見 spot 分布共同解讀。

---

# 84. Graph / External Layer

利用：

- collusion graph；
- account relation；
- solver-provider evidence；
- other external corroboration。

GGPoker 與 GTO Wizard 的合作是目前最清楚的制度案例之一。

---

# 85. Human Adjudication Layer

最後把：

$$
E_1,\ldots,E_n
$$

組合成：

$$
P(\mathrm{violation}\mid E).
$$

再依：

- policy；
- severity；
- uncertainty；

決定：

$$
\text{warning},
$$

$$
\text{suspension},
$$

$$
\text{ban}.
$$

---

# 86. 第一核心命題：Intelligence Interaction

在策略遊戲中：

$$
\boxed{
U_i
=
U_i(\pi_i,\pi_{-i}),
}
$$

因此 AI 價值不只來自預測環境，也來自建模與回應其他智能體。

---

# 87. 第二核心命題：Action--Decision Separation

$$
\boxed{
A_P=H
\not\Rightarrow
D_P=H.
}
$$

這是 Human--AI Hybrid 公平性最重要的邏輯基礎。

---

# 88. 第三核心命題：Second-Device Incompleteness

若外部決策系統與 client 實體分離，

則：

$$
\boxed{
D_{\mathrm{local}}=0
\not\Rightarrow
P(\mathrm{external\ assistance})=0.
}
$$

因此 client-side scanning 在理論上不可能單獨成為完整解。

---

# 89. 第四核心命題：Optimality Is Not Proof

$$
\boxed{
D(
\pi,
\pi^*
)\rightarrow0
}
$$

不充分推出：

$$
D_P=A.
$$

因為高手與 solver-trained humans 也可以接近均衡策略。

---

# 90. 第五核心命題：Multi-Evidence Necessity

高影響作弊判定應依賴：

$$
\boxed{
P(D_P\mid E_1,\ldots,E_n)
}
$$

而不是：

$$
P(D_P\mid E_1).
$$

此命題直接支持多層 Game Integrity。

---

# 91. 第六核心命題：Assistance Functionalism

未來治理應優先分類：

$$
\boxed{
\text{what the tool does}
}
$$

而不是：

$$
\boxed{
\text{whether it is called AI}.
}
$$

因為 AI 將逐漸成為一般軟體基礎能力。

---

# 92. 第七核心命題：Temporal Permission

同一工具：

$$
T
$$

可以在：

$$
t_{\mathrm{study}}
$$

合法，

但在：

$$
t_{\mathrm{decision}}
$$

違反規則。

因此：

$$
\boxed{
Permission=P(F,t,S).
}
$$

其中：

$$
F=\text{function},
$$

$$
t=\text{timing},
$$

$$
S=\text{state awareness}.
$$

---

# 93. 第八核心命題：Topology Countermeasure

當某策略造成：

$$
Externality>\theta,
$$

平台不一定只能：

$$
\text{detect and ban}.
$$

它也可以修改：

$$
\boxed{
\text{matchmaking / timing / access topology}.
}
$$

Hearthstone Arena 與 NYRA CAW 分別提供了遊戲與博彩市場中的類似案例。

---

# 94. 第九核心命題：Decision Substitution

AI 作弊風險與：

$$
\boxed{
\text{degree of substituted strategic cognition}
}
$$

比與單純 automation level 更直接相關。

因此：

$$
DSI
$$

可以成為未來公平競技研究的重要抽象變數。

---

# 95. 第十核心命題：Integrity--Privacy Dual Constraint

反作弊最佳化不是：

$$
\max Detection.
$$

而是：

$$
\boxed{
\max
[
Integrity
-\lambda PrivacyCost
-\gamma FalsePositiveCost
].
}
$$

任何要求完全監控所有第二裝置的制度，都會遇到極高的隱私與比例原則成本。

---

# 96. 系列研究邊界

本文不提供：

$$
\boxed{
\text{RTA implementation}
}
$$

$$
\boxed{
\text{bot implementation}
}
$$

$$
\boxed{
\text{screen-reading poker assistant}
}
$$

$$
\boxed{
\text{second-device assistance workflow}
}
$$

$$
\boxed{
\text{anti-cheat evasion}
}
$$

$$
\boxed{
\text{solver-query concealment}
}
$$

本文只研究：

- game theory；
- AI strategic capability；
- platform rules；
- decision provenance；
- game integrity；
- anti-cheat architecture；
- privacy；
- governance。

---

# 97. 與 Paper 05 的差異

Paper 05：

$$
\boxed{
\text{Player vs Mechanism}.
}
$$

Paper 06：

$$
\boxed{
\text{Intelligence vs Intelligence}.
}
$$

因此 AI 的角色從：

$$
\text{better calculation}
$$

升級為：

$$
\boxed{
\text{strategic cognition}.
}
$$

---

# 98. 與 Paper 03 的共同點

Paper 03 的市場是：

$$
\text{many intelligent agents}
\rightarrow
\text{collective price}.
$$

Paper 06 則是：

$$
\text{many intelligent agents}
\rightarrow
\text{direct strategic interaction}.
$$

兩者都屬：

$$
\boxed{
\text{multi-agent adaptive systems}.
}
$$

---

# 99. 與 Paper 07 的銜接

本篇提出：

$$
\boxed{
\text{Decision Provenance Crisis}.
}
$$

但尚未完整回答：

> 如何治理與判定？

Paper 07 將把：

$$
\text{Cognitive Forensics}
$$

獨立出來，研究：

- provenance model；
- evidence fusion；
- behavioural fingerprint；
- false positive；
- privacy；
- adversarial adaptation；
- adjudication standard。

---

# 100. 結論

Poker 把 AI 博弈研究推到了一個與輪盤、彩券及傳統 casino 完全不同的位置。

在 Poker 中：

$$
\boxed{
\text{randomness remains},
}
$$

但更重要的是：

$$
\boxed{
\text{another intelligence is inside the system}.
}
$$

玩家必須對：

$$
P(S\mid I)
$$

形成 belief，

同時對：

$$
\pi_{-i}
$$

形成 opponent model，

再選擇：

$$
\pi_i.
$$

人工智慧已經證明可以在這種不完全資訊策略環境達到超人類能力。

所以 AI 時代的 Poker 問題不再是：

> 機器能不能玩得比人好？

答案早已是：

$$
\boxed{
\text{Yes}.
}
$$

真正問題變成：

$$
\boxed{
\text{When is that intelligence allowed to enter the decision loop?}
}
$$

早期 bot：

$$
A_P=M,
$$

$$
D_P=M.
$$

今天的 Human--AI Hybrid 卻可能：

$$
A_P=H,
$$

$$
D_P=H+A
$$

甚至：

$$
D_P=A.
$$

因此：

$$
\boxed{
\text{human execution is no longer sufficient evidence of human decision}.
}
$$

這就是 Decision Provenance Crisis。

而現代平台的反應也正在改變。

PokerStars 已不只分析滑鼠與 bot process，而使用巨大 hand-history 資料、策略與行為模型以及人工 Game Integrity review。

GGPoker 2026 年規則更直接把 RTA、AI bots、solver、chart、HUD、remote access 與 virtualized environments 納入整個 security ecology。

GTO Wizard 則代表另一個新現象：原本提供策略智能的 solver provider，也開始提供 Fair Play Check、superhuman-play detection 與 strategy-closeness analysis，協助平台判斷外部計算是否可能介入即時遊戲。GGPoker 2025 年公開表示，雙方合作後已針對 31 個違反 fair-play rule 的帳號採取封鎖措施。

因此：

$$
\boxed{
\text{AI for strategic advantage}
}
$$

正在同時產生：

$$
\boxed{
\text{AI for strategic forensics}.
}
$$

卡牌遊戲則進一步顯示，制度不一定只能靠「抓到然後封號」。

Hearthstone 對某些極端 Arena 行為採用不同 matchmaking pool，說明平台還可以直接改變：

$$
\boxed{
\text{game topology}.
}
$$

於是整個 AI 競技治理的演化，可以概括為：

$$
\boxed{
\begin{array}{c}
\text{Detect Automation}\\
\downarrow\\
\text{Detect Assistance}\\
\downarrow\\
\text{Infer Decision Provenance}\\
\downarrow\\
\text{Redesign Competitive Topology}
\end{array}
}
$$

這也讓 AI 公平性問題第一次超出「是不是外掛」。

真正的問題成為：

$$
\boxed{
\text{How much of the strategic cognition must remain with the registered human participant for the contest to remain the same contest?}
}
$$

當一個人仍然坐在螢幕前、仍然親手按下按鈕，但重要判斷已由外部模型完成時，身份驗證仍然成功，卻未必完成了認知來源驗證。

因此本文最後提出：

$$
\boxed{
\text{Identity Provenance}
\neq
\text{Action Provenance}
\neq
\text{Decision Provenance}.
}
$$

這三者在前 AI 時代經常被默認為同一件事。

在 Human--AI Hybrid 時代，它們必須被正式分離。

而下一篇 Paper 07 將從這裡開始：

$$
\boxed{
\text{如果 Decision Provenance 無法直接觀測，
我們究竟可以如何在不犧牲隱私與正常高手的前提下，
建立合理的 Cognitive Forensics？}
}
$$

---

## References / Empirical and Policy Anchors

1. Carnegie Mellon University, 2019, reporting Pluribus's superhuman performance against professional players in six-player no-limit Texas Hold'em and summarizing the earlier Libratus result.
2. PokerStars, current Third Party Tools and Services Policy and General Terms, accessed 2026, defining prohibited bots, real-time advice, advanced equity, ICM and Nash-equilibrium assistance during play.
3. PokerStars Game Integrity materials, 2024--2026, describing FAB, PTBB, RTA detection, behavioural analysis, proprietary models, continuous automated flagging, specialist review, and analysis across more than 235 billion hands.
4. GGPoker, Security & Ecology Policy, current version dated 2026-03-13, defining RTA, bots, AI, prohibited decision assistance, remote-access tools, virtual machines and related integrity restrictions.
5. GGPoker, 2025, *GGPoker & GTO Wizard Join Forces*, reporting 31 blocked accounts following use of GTO Wizard game-integrity services and describing Fair Play Check.
6. GTO Wizard, current Game Integrity materials, accessed 2026, describing Fair Play Check Automation, GTO Reports, superhuman-play detection and strategy-to-optimal-strategy closeness assessment.
7. Blizzard Entertainment, April 2024 Hearthstone Bot Ban Update, reporting action against more than 240,000 additional accounts and the use of a separate Arena matchmaking pool for repeated early-retirement behaviour.
8. Wizards of the Coast, current Terms, accessed 2026, prohibiting unauthorized bots, cheats, software, data mining and tools that grant advantages not available to ordinary players.

---

**Next:**  
**Paper 07 — 反 AI 博弈系統：Decision Provenance、Cognitive Forensics 與公平競技治理**
