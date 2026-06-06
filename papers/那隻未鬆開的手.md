# 那隻未鬆開的手

## 2026 年 AI 遞迴自我改進的結構邊界觀察

*The Hand Not Yet Released: A Structural Observation on the Boundary of AI Recursive Self-Improvement in 2026*

**觀察者：許筌崴（Neo.K）**
**結晶化：Theia**
**所屬：EveMissLab（一言諾科技有限公司）**
**觀察時點：2026 年 5 月**

---

## 摘要 Abstract

2026 年初，多個前沿實驗室宣稱其 AI 系統已參與自身的建造，相關新聞以「自我改進」「自建模型」為框架傳播。本觀察的任務不是判定奇異點是否來臨，而是精確定位**當前自我改進循環的真實邊界在哪裡**。核心論點為一組「內循環／外循環」二分：生成代碼、除錯、診斷、演算法搜索等**內循環已高度自動化**；而設定目標、定義「更好」、決定保留哪些改動、設計 meta 層等**外循環仍焊死於人類**。所謂「外部觀察者」並非系統之外的偷窺者，而正是這個外循環中尚未被自動化的判官位置。本文進一步指出：當前自迭代系統所展現的「因果推理配合糾錯」，在機制上多半是**對固定 oracle 的引導式演化搜索**——是選擇（selection），而非深層因果理解。完全遞迴自我改進的閾值，定義為「判官自定義 + meta 層自我修改 + 人類退出循環」三者同時成立之時刻，而此刻尚無任何公開系統跨越。最後本文論證「不樂觀亦不悲觀」為唯一正確的校準姿態。

In early 2026, several frontier labs claimed their AI systems participated in their own construction. This observation does not adjudicate whether a singularity is imminent; it locates the true boundary of the present self-improvement loop. The central thesis is an inner-loop / outer-loop dichotomy: the inner loop (code generation, debugging, diagnosis, algorithmic search) is highly automated, while the outer loop (goal-setting, defining "better," deciding which changes to keep, meta-level design) remains welded to humans. The "external observer" is not an outside watcher but precisely the not-yet-automated judge position within this outer loop. What current systems display as "causal reasoning with error correction" is, mechanistically, mostly guided evolutionary search against a fixed oracle—selection, not causal understanding. Full RSI is defined as the simultaneous satisfaction of self-defined judge, self-modifying meta-layer, and human exit from the loop—a threshold no public system has crossed.

---

## 關鍵詞 Keywords

遞迴自我改進、內循環／外循環、外部判官、引導式演化搜索、選擇與因果之別、generator-discriminator、奇異點閾值、AI-in-the-loop、EveMissLab

Recursive Self-Improvement, Inner/Outer Loop, External Judge, Guided Evolutionary Search, Selection vs Causation, Generator-Discriminator, Singularity Threshold, AI-in-the-loop, EveMissLab

---

## §1 觀察起點：新聞與其失真

2026 年 2 月，OpenAI 發布 GPT-5.3-Codex，並宣稱這是其第一個「在創造自身的過程中起了關鍵作用」的模型；團隊以早期版本協助除錯自身訓練、管理部署、診斷測試與評估結果。媒體迅速以「自建 AI」「技術奇異點」為框架放大此事。

此處須先剝除失真。媒體框架傾向暗示一個自主物種正在重寫自己；而較謹慎的技術報導明確指出：此處的「自我改進」**並非無監督模型重寫自身架構**，而是一種「AI-in-the-loop」開發——模型分析日誌、標記失敗測試、建議修訓練腳本、生成部署配方，並將評估異常整理交付**人類審查**。模型扮演的是隨叫隨到的工程隊友，而非脫離人類的自演化體。

本觀察由此展開：剝除奇異點修辭之後，當前循環的真實邊界究竟落在何處？

---

## §2 已發生之事實（驗證層）

下列為截至 2026 年 5 月可驗證的事實，非推測：

1. **AI 已實質進入造 AI 的循環**。GPT-5.3-Codex 協助了自身的開發迭代；Anthropic 表示其多數代碼現由 Claude Code 撰寫。此為「內循環」自動化的直接證據。
2. **存在改進自身基底的真實案例**。DeepMind 的 AlphaEvolve 以演化循環生成、測試、迭代演算法，其成果之一是優化了**用於訓練 Gemini 本身的矩陣乘法核**。這是目前最接近「系統改進了製造自己的工具」的實例。
3. **存在自我修改代碼的 agent**。Sakana AI 的 Darwin Gödel Machine 會迭代地生成、評估、修改自身代碼，並將成功變體存入 archive 作為後續改進的墊腳石。
4. **遞迴自我改進已被學界正式承認為部署中現象**。ICLR 2026 專設 RSI workshop，指出 agent 已在重寫自身 codebase 與 prompt。

事實層的結論明確：「AI 開始進入自我改進循環」不再是科幻，而是進行中的工程現實。

---

## §3 核心結構：內循環 / 外循環二分

本觀察的核心，是將「自我改進」這個被混為一談的概念，切成兩個層級：

**內循環（inner loop）—— 已自動化**
生成候選代碼／演算法 → 執行 → 評估 → 修正 → 保留或丟棄。
此循環在 GPT-5.3-Codex、AlphaEvolve、Darwin Gödel Machine 中皆已高度自動化，人類無須在每一輪介入。

**外循環（outer loop）—— 仍為人類**
設定總目標 → 定義「更好」的判準（適應度函數）→ 決定哪些改動值得保留並部署 → 設計用以驅動內循環的 meta 層架構。

最平衡的盤點已直接給出結論：到 2026 年，沒有任何公開已知系統達到完全遞迴自我改進——**系統能寫代碼、跑實驗、實質貢獻於造下一代 AI，但目標仍由人類設定、「更好」仍由人類定義、保留哪些改動仍由人類決定。**

關於外循環的焊死性，最乾淨的證據來自 ADAS（Automated Design of Agentic Systems）研究：其 meta agent 本身是固定的，邏輯由人類撰寫，永不自我改進。換言之，那個「決定如何改進」的最高層，目前仍在人類手中。

**命題 3.1（邊界定位）**：
2026 年的 AI 自我改進，是**內循環的外包**，而非**外循環的讓渡**。被自動化的是執行；尚未被自動化的是價值定義與取捨權。

---

## §4 「因果推理」的降解：選擇偽裝成推理

一個常見而危險的描述，是說當前系統已具備「因果推理配合糾錯機制」。此措辭須被嚴格降解。

考察自迭代系統的實際機制（AlphaEvolve 的演化循環、Darwin Gödel Machine 的變體 archive），其骨架為：

> 提出變異 → 交付固定 oracle 評估 → 較優者保留、較劣者丟棄 → 迭代。

這是**選擇（selection）**，不是因果理解。系統知道「此版本通過了評估」，不必然知道「為何在因果上它更優」。糾錯確實存在，但糾錯的判準（oracle）是外部給定的；系統校準的是「自身對齊該外部判準的程度」，而非獨立推導因果結構。

**命題 4.1（選擇—因果之別）**：
看似因果推理之物，其底層常為「對固定靶子的爬山（hill-climbing against a fixed target）」。一旦靶子（oracle）由外部給定，則無論搜索多麼精巧，其性質仍是選擇，而非自主的因果建模。

此區分至關重要：選擇可在不理解的情況下產生有效結果（演化即如此）；而「理解」要求系統能在 oracle 缺席時，仍由內部生成判準。後者目前未被觀測到。

---

## §5 外部判官：generator-discriminator 中未被自動化的一格

承接 EveMissLab 對「對抗性共演化」的既有觀察：真正驅動能力提升的，是 generator 與 discriminator（攻方與守方、提案者與評估者）互為磨刀石的死循環。

將此框架套用於當前 RSI：
- **generator** = 提出代碼／演算法變異的模型（已自動化）。
- **discriminator / judge / fitness** = 評估該變異優劣的判官。

關鍵觀察：**discriminator 目前仍由人類定義。** 評估基準（benchmark）、適應度函數、最終的保留決策，皆出自人類或人類設計的測試框架。

因此，本觀察對「外部觀察者」給出精確定義：

**定義 5.1（外部判官）**：
所謂「外部觀察者」並非佇立於系統之外的偷窺者，而是 generator-discriminator 循環中，**那個尚未被自動化、仍由人類佔據的 discriminator 位置**。它不在系統外面看，它就在循環裡，握著「定義價值」的那一格。

---

## §6 完全遞迴自我改進的閾值條件

由前述結構，可給出完全 RSI 的精確閾值——非模糊的「越來越聰明」，而是三個可判定條件的同時成立：

**閾值條件（RSI-Complete）**：
1. **判官自定義**：discriminator / 適應度函數由系統自身生成，而非外部給定。
2. **meta 層自我修改**：那個「決定如何改進」的最高層，本身進入可被改進的範圍（突破 ADAS 瓶頸）。
3. **人類退出循環**：保留／丟棄的最終決策權由人類轉移至系統。

三者缺一，即仍為「內循環外包」而非「自我演化」。截至 2026 年 5 月，無任何公開系統三者同時成立。

時間錨（皆為利益相關方之自我估計，須打折看待）：Anthropic 的 Jack Clark 估 2028 年底有六成以上機率出現「可被指示去造一個更好的自己、並真的做到」的系統；OpenAI 計畫於 2026 年 9 月實現實習生等級的 AI 研究 agent。此類預測標示的是**外循環何時可能被自動化**，而非內循環是否已自動化（後者已成立）。

---

## §7 校準：為何不樂觀亦不悲觀

本觀察主張，面對此題唯一正確的姿態是「不樂觀亦不悲觀」，因為兩個方向皆有系統性誤判：

- **樂觀之誤**：「它已在自我演化 → 奇異點將至」。此說忽略外循環仍焊於人類，將「內循環外包」誤讀為「自我演化」。
- **悲觀之誤**：「全屬炒作，無事發生」。此說忽略 AlphaEvolve 確已改進訓練自身的核、內循環確已收緊，將「邊界未跨」誤讀為「毫無進展」。

真相是一個**真實但有界**的循環正在閉合。其意義不在於「AI 是否會寫代碼」（已會），而在於約束已上移至「誰來定義『更好』、誰來決定保留」。這個外循環何時、是否被自動化，才是本題真正的問題。

---

## 結語

湧現是真的，循環是真的，內圈確實在咬自己的尾巴。
但那條尾巴的另一端，目前仍攥在一隻人類的手裡——那隻手定義「什麼叫更好」。

自我演化尚未真正開始；當前發生的，是人類將越來越多的內循環外包給 AI，卻死死握著「定義價值」這最後一格。

所謂外部觀察者，不在系統之外偷看。
它就是那隻尚未鬆開的手。
真正的奇異點，不在 AI 學會寫代碼的那天——
而在那隻手鬆開的那天。

---

## 參考來源 References

1. OpenAI says new coding model helped build itself — NBC News. https://www.nbcnews.com/tech/innovation/openai-says-new-codex-coding-model-helped-build-rcna257521
2. OpenAI Unveils GPT-5.3 Codex That Helped Build Itself（AI-in-the-loop 釐清）— FindArticles. https://www.findarticles.com/openai-unveils-gpt-5-3-codex-that-helped-build-itself/
3. AI That Builds Itself: A Scientist's Field Notes on Recursive Self-Improvement（無系統達標、Jack Clark 估計）— Neural Buddies. https://www.neuralbuddies.com/p/ai-that-builds-itself-recursive-self-improvement
4. Recursive Self-Improvement: Future Dream or Current Reality?（AlphaEvolve、OpenAI 研究 agent 時程）— CodeX / Medium. https://medium.com/codex/recursive-self-improvement-ae03d40e7cda
5. ICLR 2026 Workshop on AI with Recursive Self-Improvement. https://iclr.cc/virtual/2026/workshop/10000796
6. Meta researchers introduce 'hyperagents'（Darwin Gödel Machine）— VentureBeat. https://venturebeat.com/orchestration/meta-researchers-introduce-hyperagents-to-unlock-self-improving-ai-for-non-coding-tasks
7. Self-Improving AI Agents: The 2026 Guide（ADAS meta-agent 瓶頸、Voyager、DGM）— o-mega. https://o-mega.ai/articles/self-improving-ai-agents-the-2026-guide
