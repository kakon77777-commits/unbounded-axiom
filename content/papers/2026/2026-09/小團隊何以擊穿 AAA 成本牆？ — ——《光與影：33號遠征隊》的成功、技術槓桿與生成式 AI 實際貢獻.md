# 小團隊何以擊穿 AAA 成本牆？
## ——《光與影：33號遠征隊》的成功、技術槓桿與生成式 AI 實際貢獻

**系列：** AI 時代的創作、選擇與人類復古系列  
**篇次：** 第 12 篇  
**版本：** v0.1  
**性質：** 實證案例研究／公開資料因果分析／公開版  
**資料截點：** 2026-09-08

---

## 摘要

《光與影：33號遠征隊》（Clair Obscur: Expedition 33）是 2025–2026 年最具代表性的「小核心團隊、高製作品質、全球商業成功」案例之一。官方於 2025 年 10 月宣布全球銷量達 500 萬套，同時原聲帶累積超過 3.33 億次串流；2026 年一周年時，官方再宣布銷量達 800 萬套。[S01][S02] Xbox 則表示，本作是 2025 年 Game Pass 最大的新第三方遊戲首發，以前 30 日 unique users 計算。[S09]

然而，市場與媒體對本作成功原因的敘述經常混合三種不同概念：

$$
\boxed{
\text{Small-Team Leverage}
}
$$

$$
\boxed{
\text{Modern Technology Leverage}
}
$$

以及：

$$
\boxed{
\text{Generative AI Leverage}
}
$$

本篇透過 Sandfall Interactive、Expedition 33 官方、Epic / Unreal Engine、Xbox、開發者專訪、GDC 技術報導、完整 credits、藝術家作品說明與 GenAI 爭議資料進行交叉驗證。研究結果顯示：

$$
\boxed{
\text{Technology Leverage}
\neq
\text{Generative AI Leverage}
}
$$

公開證據強烈支持 Unreal Engine 5、Blueprint、Sequencer、MetaHuman、Lumen、Nanite、World Partition、MetaSounds、Marketplace / Fab 生態、外包專業網路、Kepler Interactive 與 Xbox / Game Pass 對本作具有顯著槓桿作用。[S03][S04][S05][S06][S08][S09]

相反地，Sandfall 對 El País 的後續澄清表示：團隊於 2022 年短暫實驗生成式 AI，用於 temporary placeholder textures；少量 placeholder 在發售時誤留於遊戲中，約五日後被替換，而目前遊戲中沒有生成式 AI 製作的最終資產。[S10] 官方 Patch 1.3.0 亦明確記載移除特定 placeholder textures。[S11]

因此，基於目前可公開驗證的資料，本篇對「生成式 AI 直接造成《33號遠征隊》成功」的命題給予低支持度；對「現代工具鏈大幅提高小團隊生產槓桿」則給予極高支持度。

更重要的是，本案真正支持的並不是：

$$
\boxed{
\text{Use AI}
\Rightarrow
\text{Success}
}
$$

而是：

$$
\boxed{
\text{Success}
\approx
\text{Vision}
\times
\text{Selection}
\times
\text{Scope Discipline}
\times
\text{Tool Leverage}
\times
\text{Integration}
\times
\text{Network}
\times
\text{Distribution}
}
$$

換言之，《33號遠征隊》最值得研究的可能不是「AI 幫了多少忙」，而是 Sandfall 如何從當代已存在的巨大選擇底空間中，**選對了哪些東西、拒絕了哪些東西，又讓哪些外部工具與人替自己承擔原本昂貴的工作。**

---

## 關鍵詞

Clair Obscur: Expedition 33、Sandfall Interactive、生成式 AI、Unreal Engine 5、Blueprint、MetaHuman、Scope Control、Technology Leverage、Selection Capital、Small Team、Game Pass、Process Capital

---

# 1. 研究問題

本篇不把《33號遠征隊》當成「AI 遊戲案例」。

真正的研究問題共有五個：

### RQ1
《33號遠征隊》的成功可以由哪些因素公開驗證？

### RQ2
它的「小團隊神話」應如何重新定義？

### RQ3
現代技術工具如何改變人力與成本結構？

### RQ4
生成式 AI 的直接、間接與不可知貢獻各是什麼？

### RQ5
這個案例究竟支持「AI 生產論」，還是更廣義的「選擇與技術槓桿論」？

---

# 2. 方法：公開資料下的因果貢獻分析

本研究不是 Sandfall 內部成本審計，因此不能得到真正精確的：

$$
\boxed{
\text{Causal Percentage}
}
$$

例如不能嚴肅聲稱：

> UE5 貢獻 23.4%。

或：

> AI 貢獻 4.7%。

因此本篇採：

$$
\boxed{
\text{Evidence-Weighted Contribution Assessment}
}
$$

將每個成功因素分成：

- **Very High**
- **High**
- **Medium**
- **Low**
- **Unknown**

同時標記證據強度。

---

# 3. 證據分級

本篇使用以下證據層級：

### A — 第一方／直接開發資料
例如：

- Sandfall 官方；
- Expedition 33 官方；
- 開發者本人技術訪談；
- Xbox 官方合作資料；
- 官方 patch notes。

### B — 高品質第二方／直接採訪
例如：

- GameMakers；
- Game Developer；
- New York Times syndication；
- Game Informer；
- 巴哈姆特 GNN；
- MobyGames credits。

### C — 輔助脈絡
例如：

- 新聞評論；
- 頒獎爭議；
- 第三方產業討論。

### U — Unknown
公開資料不足，不能可靠判斷。

---

# 4. 先確認：它確實是極端成功案例

官方數據顯示：

$$
Sales_{2025-10}
=
5,000,000
$$

並且：

$$
OSTStreams_{2025-10}
>
333,000,000
$$

[S01]

到了 2026 年 4 月一周年：

$$
Sales_{2026-04}
=
8,000,000
$$

[S02]

這已經不是「小團隊做出一款評價不錯的遊戲」。

而是：

$$
\boxed{
\text{Global Breakout Success}
}
$$

---

# 5. Game Pass 使「玩家數」大於「銷量」

本作首日加入 Game Pass。

Xbox 在 2025 年底表示，以首 30 日 unique users 計算，《33號遠征隊》是該年最大的全新第三方 Game Pass 首發。[S09]

因此：

$$
\boxed{
\text{Copies Sold}
\neq
\text{Total Players Reached}
}
$$

800 萬套銷售之外，另有 Game Pass 使用者。

這意味著本作的文化擴散面比單純銷量更大。

---

# 6. 成功不能只用「便宜 AAA」解釋

如果唯一原因是：

> 看起來像 AAA，但成本低。

那麼大量 UE5 中小型專案理論上都應該成功。

顯然不是。

因此：

$$
\boxed{
\text{Low Cost}
}
$$

只能解釋：

> 為什麼它有較好的投入產出比。

不能單獨解釋：

> 為什麼幾百萬人真的想買。

---

# 7. 第一個核心：產品本身有高度可辨識的差異

Epic 的開發者訪談把本作定位為：

$$
\boxed{
\text{Reactive Turn-Based RPG}
}
$$

即傳統回合制搭配：

- 即時閃避；
- 格擋；
- counter；
- QTE；
- free aim。

[S03]

這個核心並不是發售前才補上。

早期 prototype 階段，Guillaume Broche 與 Tom Guillermin 已經在測這套 reactive battle system，團隊在一個 boss demo 中輪流挑戰時，認為玩法開始真正「click」。[S03]

因此：

$$
\boxed{
\text{Core Loop Differentiation}
}
$$

出現在非常早期。

---

# 8. 這一點很重要：他們不是先做很多，再找核心

公開開發歷史顯示，早期 prototype 曾探索：

- double jump；
- open world；
- Marketplace assets；
- 與早期資產綁定的故事。

但正式進入 production 時，Sandfall 幾乎全部丟掉，只留下：

$$
\boxed{
\text{Battle System}
}
$$

[S05]

也就是：

$$
\boxed{
\text{Prototype}
\rightarrow
\text{Selection}
\rightarrow
\text{Core Retention}
}
$$

而不是：

$$
\text{Prototype}
\rightarrow
\text{Keep Everything}
$$

---

# 9. 這是一個非常典型的 Selection Capital 案例

他們不是沒有做過錯誤方向。

恰恰相反。

他們做過：

$$
\mathfrak B_{prototype}
=
\{
OpenWorld,
DoubleJump,
OldStory,
MarketplaceAssets,
BattleSystem,\dots
\}
$$

最後只留下：

$$
\boxed{
BattleSystem
}
$$

因此：

$$
\boxed{
\text{Value of Prototype}
}
$$

不只是：

> 做出了多少。

而是：

$$
\boxed{
\text{知道什麼值得丟掉。}
}
$$

---

# 10. 第二個核心：Scope Discipline

New York Times 的後續報導（由 The Star 刊載）指出，Sandfall 刻意避開昂貴 open-world 結構，採用：

- 高度精製但較線性的關卡；
- 遭遇敵人後進入控制良好的戰鬥空間；
- 縮小比例的 overworld map。

[S07]

因此它給玩家：

$$
\boxed{
\text{World Scale Perception}
}
$$

但避免支付：

$$
\boxed{
\text{Full Open-World Detail Cost}
}
$$

---

# 11. 不是「30 人硬做 300 人工作」

更準確的說法是：

$$
\boxed{
\text{他們重新設計了哪些工作根本不需要做。}
}
$$

例如真正完整 open world 會增加：

- asset density；
- navigation；
- streaming；
- encounter design；
- traversal；
- QA surface；
- world interaction；
- content fill。

Sandfall 不是暴力吸收全部成本，而是：

$$
\boxed{
\text{Scope Selection}
\rightarrow
\text{Cost Avoidance}
}
$$

---

# 12. 高品質小團隊的核心不是「做更多」

這個案例反而非常支持本系列前面的命題：

$$
\boxed{
\text{Feature Count}
\neq
\text{Experience Value}
}
$$

當大型產品很容易走向：

$$
\text{More World}
+
\text{More Systems}
+
\text{More Content}
$$

Sandfall 的成功部分來自：

$$
\boxed{
\text{Selective Density}
}
$$

---

# 13. 第三個核心：Unreal Engine 是極大的技術槓桿

Epic 訪談中，Tom Guillermin 明確指出：

> 以這種團隊規模，在幾年前不可能完成同樣 vision。

[S03]

其中被反覆點名的工具包括：

$$
\boxed{
Blueprint
}
$$

$$
\boxed{
Sequencer
}
$$

$$
\boxed{
MetaHuman
}
$$

$$
\boxed{
Lumen
}
$$

$$
\boxed{
Nanite
}
$$

$$
\boxed{
WorldPartition
}
$$

$$
\boxed{
MetaSounds
}
$$

以及 Unreal 生態中的 plugins、assets 與 template projects。[S03]

---

# 14. 但這些不是「生成式 AI」

這是本案最重要的概念清理之一。

$$
\boxed{
\text{MetaHuman}
\neq
\text{GenAI}
}
$$

$$
\boxed{
\text{Blueprint}
\neq
\text{GenAI}
}
$$

$$
\boxed{
\text{Nanite}
\neq
\text{GenAI}
}
$$

$$
\boxed{
\text{Lumen}
\neq
\text{GenAI}
}
$$

它們可以是：

$$
\boxed{
\text{Advanced Production Technology}
}
$$

但不應全部塞入：

$$
\boxed{
\text{Generative AI Contribution}
}
$$

---

# 15. Blueprint 的價值甚至不是「少寫程式」而已

Epic 資料指出，早期 Tom 一度是唯一 programmer；後來整個 programming team 也只有四人。[S03]

Blueprint 讓非程式成員可以：

- 理解 logic；
- 修改 gameplay；
- 添加 polish；
- 不必等 programmer。

因此：

$$
\boxed{
\text{Blueprint Leverage}
}
$$

真正改變的是：

$$
\boxed{
\text{Organizational Bottleneck}
}
$$

---

# 16. 2026 GDC 的資料更極端

Game Developer 報導 Sandfall 在 GDC 2026 的分享：

$$
\boxed{
95\%
}
$$

左右的遊戲由 Unreal Blueprints 構成。[S04]

其核心意義不是：

> 視覺 scripting 比 C++ 神奇。

而是：

$$
\boxed{
\text{更多職能可以直接改變產品。}
}
$$

這提高：

$$
\boxed{
\text{Cross-Role Production Bandwidth}
}
$$

---

# 17. Blueprint 是「組織技術」

因此 Blueprint 在本案中應被理解為：

$$
\boxed{
\text{Technical Tool}
+
\text{Organizational Technology}
}
$$

它降低：

$$
\text{Designer}
\rightarrow
\text{Programmer}
\rightarrow
\text{Implementation}
$$

這條鏈的等待成本。

這和本系列第七篇 Agentic Development 的問題結構高度相似：

> 真正的槓桿不只是能力增加，而是角色邊界重新設計。

---

# 18. Sequencer 讓戰鬥技能本身成為小型 cinematic

Sandfall 將技能當成「mini-cinematic」來 author，透過 Sequencer 動態綁定 battle actors。[S03]

這讓：

- animation；
- camera；
- VFX；
- gameplay；

共享同一個 authoring surface。

因此：

$$
\boxed{
\text{Tool Integration}
\rightarrow
\text{Art / Gameplay Integration}
}
$$

---

# 19. MetaHuman 降低高品質角色表演成本

Sandfall 在 UE5 後將整個角色創作 pipeline 轉向 MetaHuman，並搭配：

- body mocap；
- facial mocap；
- MetaHuman Animator；
- Animation Blueprint；
- 自訂 dirt / blood / sweat / tear material system。

[S03]

所以角色品質不是：

$$
\boxed{
\text{One AI Button}
}
$$

而是：

$$
\boxed{
\text{Human Performance}
+
\text{Capture}
+
\text{Character Art}
+
\text{Engine Toolchain}
}
$$

---

# 20. Lumen / Nanite 降低環境反覆迭代成本

Sandfall 特別指出：

- Lumen 讓 lighting ideas 更快 iteration；
- Nanite 改變 level / asset production；
- World Partition 支撐 world map；
- HLOD 與 navigation 仍需要技術設計。

[S03]

這顯示：

$$
\boxed{
\text{Automation}
}
$$

沒有消滅專業工作。

它改變的是：

$$
\boxed{
\text{Which Work Needs Manual Attention}
}
$$

---

# 21. 第四個核心：強 Art Direction，而不是「工具自己變漂亮」

Epic 訪談指出，Art Director Nicholas Maxson-Francombe 長期與 Guillaume 對齊 art style，讓 French fantasy identity 持續演化。[S03]

Nicholas 自己在 ArtStation 表示，他為本作做了約四年半 art direction，作品標記 `#NoAI`。[S15]

Lead Character Artist Alan Reynaud 則表示，他在四年間負責幾乎所有角色的 modelling、low poly、texturing，並與 Nicholas 一起處理角色 design / final look。[S16]

---

# 22. 這是非常重要的「負面證據」

它不能證明：

$$
AIUsage=0
$$

但至少強烈反對一個常見想像：

> 這款遊戲的人物主要靠 GenAI 批量生成。

公開的人員工作說明顯示，大量角色製作存在長期、具名、可追蹤的人類美術工作。[S15][S16]

所以：

$$
\boxed{
\text{Human Art Direction Contribution}
}
$$

證據非常強。

---

# 23. 第五個核心：人才選擇非常不傳統

作曲家 Lorien Testard 在加入前沒有大型遊戲配樂履歷。

Sandfall 從 SoundCloud 找到他。[S13]

他最終為遊戲創作：

$$
154
$$

首曲目。[S13]

而官方五百萬銷量公告又顯示：

$$
OSTStreams>333,000,000
$$

[S01]

因此音樂不只是：

> 生產中的一個項目。

而成為：

$$
\boxed{
\text{Product Identity Amplifier}
}
$$

---

# 24. Lead Writer 的招募也不是傳統 AAA 路徑

NYT syndication 報導指出，Jennifer Svedberg-Yen 最初是回應 Reddit 上的 voice-acting 招募而接觸團隊；composer 則來自 SoundCloud。[S07]

GNN 訪談中，Jennifer 表示她在 2020 年加入，是早期第四位成員。[S14]

這形成一個非常有意思的模式：

$$
\boxed{
\text{Selection Quality}
>
\text{Conventional Prestige Filter}
}
$$

至少在本案中是如此。

---

# 25. 但不能把「新人」浪漫化

本案不是：

> 沒經驗的人比較厲害。

核心團隊同時也有：

- Ubisoft 經驗；
- engine / programming 經驗；
- 外部專業人士；
- 發行商經驗；
- outsourced specialists。

所以更準確是：

$$
\boxed{
\text{New Talent}
+
\text{Experienced Anchors}
+
\text{External Expertise}
}
$$

---

# 26. 「30 人做完全部」是一個錯誤神話

Epic 在發售前稱核心團隊不到 30 人。[S03]

GameMakers 則記錄 production peak 約：

$$
35
$$

人，並列出：

- programmer 4；
- environment 5；
- character 3；
- game design 3；
- cinematics 6；
- battle animation 8（韓國 freelancers）；
- audio 4。

[S05]

同時 QA、localization、porting 亦有外部合作。[S05]

---

# 27. 完整 credits 更能拆掉神話

MobyGames 的 Windows credits 頁面列出：

$$
438
$$

人，

其中：

$$
429
$$

個 professional roles，

另有：

$$
9
$$

個 thanks。[S12]

因此：

$$
\boxed{
\text{Core Team}\approx30\text{–}35
}
$$

不等於：

$$
\boxed{
\text{Total Human Contributors}\approx30
}
$$

---

# 28. 更好的組織模型

本案比較像：

$$
\boxed{
\text{Small Core}
+
\text{External Specialist Network}
+
\text{Publisher}
+
\text{Platform Partners}
}
$$

這就是：

$$
\boxed{
\text{Networked Small-Team Production}
}
$$

而不是孤立的一人／三十人奇蹟。

---

# 29. 第六個核心：Kepler Interactive 是槓桿，不只是出錢

Sandfall 2023 官方更新顯示，在與 Kepler 建立合作後：

$$
Team:
12
\rightarrow
22
$$

並增加與 animation / lighting freelancers 及 experts 的合作。[S06]

GNN 訪談中，Jennifer 也明確提到 Kepler 提供：

- resources；
- guidance；
- advice；
- release experience；
- platform coordination。

[S14]

因此：

$$
\boxed{
PublisherContribution
>
FundingOnly
}
$$

---

# 30. 發行商其實是一種「外接組織記憶」

Sandfall 是首次發行大型跨平台作品。

Kepler 已經處理過其他作品的：

- platform；
- release；
- localization；
- marketing；
- coordination。

因此它提供的其實不只是資金：

$$
\boxed{
\text{External Process Capital}
}
$$

這正好對應本系列第九篇。

---

# 31. 第七個核心：Xbox / Game Pass 放大了成功

Xbox 官方表示：

- Summer 2024 announcement；
- 2025 Developer_Direct；
- Game Pass day one；

都幫助作品擴大 reach。[S09]

Broche 特別指出，Game Pass 降低了不熟悉 turn-based RPG 玩家嘗試本作的門檻。[S09]

因此：

$$
\boxed{
\text{Product Quality}
}
$$

與：

$$
\boxed{
\text{Distribution Reach}
}
$$

必須分開。

---

# 32. 好產品如果沒被看見，仍可能失敗

可以粗略寫：

$$
\boxed{
CommercialSuccess
=
Desirability
\times
Reach
\times
Conversion
}
$$

如果：

$$
Reach\rightarrow0
$$

即使：

$$
Desirability
$$

很高，

成功仍然可能受限。

Game Pass / Xbox 在本案中很明顯提高了：

$$
\boxed{
Reach}
$$

---

# 33. 第八個核心：音樂形成獨立口碑引擎

154 首曲目與 3.33 億以上串流，不只是：

> OST 很成功。

它意味著音樂本身已經進入：

$$
\boxed{
\text{Discovery Loop}
}
$$

玩家可能：

$$
Game
\rightarrow
Music
$$

也可能：

$$
Music
\rightarrow
Game
$$

---

# 34. 產品成功是多個 subsystem 互相放大

因此本案不像：

$$
\text{One Killer Feature}
$$

而更接近：

$$
\boxed{
\text{Combat}
\times
\text{Story}
\times
\text{Art}
\times
\text{Music}
\times
\text{Performance}
\times
\text{Distribution}
}
$$

這正是：

$$
\boxed{
\text{Integration}
}
$$

比單一 asset 更重要的案例。

---

# 35. 預算：不能把「約 1000 萬美元」當成精確 all-in 數字

公開資料存在衝突。

El País 在 2025 年報導：

> just over USD 10 million。[S10]

NYT 後續 syndication 則寫：

> Sandfall said the budget was less than USD 10 million。[S07]

因此最嚴謹寫法是：

$$
\boxed{
\text{Public Budget Reporting}
\approx
USD 10M
}
$$

但：

$$
\boxed{
\text{Exact Accounting Scope}
=
Unknown
}
$$

---

# 36. Core Development Budget 不等於 Total Ecosystem Input

因為本作還有：

- external QA；
- localization；
- porting；
- battle animation；
- marketing；
- publisher resources；
- platform promotion；
- Game Pass economics。

所以不能直接：

$$
8,000,000
\times
USD 49.99
-
USD 10M
$$

來計算真實利潤。

這會忽略：

- regional pricing；
- discounts；
- platform cut；
- publisher split；
- tax；
- Game Pass deal；
- marketing；
- external services。

---

# 37. 但「成本效率很高」的方向仍高度可信

即使不接受精確：

$$
USD 10M
$$

all-in，

相對傳統大型 AAA：

$$
\boxed{
\text{Core Cost Structure}
}
$$

顯然小很多。

這和：

- 小核心團隊；
- scope control；
- Unreal tooling；
- 外部專家；
- publisher network；

完全一致。

---

# 38. 現在進入最關鍵的問題：生成式 AI 到底做了什麼？

El País 原始訪談中，producer François Meurisse 曾說：

> 團隊有使用一些 AI，但不多。[S10]

如果只看這一句，很容易產生：

$$
\boxed{
\text{AI materially helped build the game}
}
$$

的推論。

但文章後來加入 Sandfall 的正式澄清。

---

# 39. Sandfall 後續澄清

Sandfall 表示：

1. Unreal Marketplace 的 pre-existing assets 不是 AI 生成；
2. 目前遊戲中沒有 generative-AI-created assets；
3. 2022 年早期 AI 工具出現時，部分成員短暫實驗；
4. 用途是生成 temporary placeholder textures；
5. 發售時有 placeholder 誤留；
6. 約五日內被替換成原本預定的正式 textures；
7. 漏出原因被描述為 QA 遺漏。

[S10]

---

# 40. 官方 Patch 也提供獨立佐證

Patch 1.3.0 的官方 patch notes 明確寫有：

$$
\boxed{
\text{Placeholder textures removed}
}
$$

並指向 Chromatic Boucheclier 附近與 battle arena。[S11]

因此：

$$
\boxed{
\text{Some GenAI Placeholder Use}
}
$$

是已確認事實。

---

# 41. 但「使用過 GenAI」與「GenAI 是成功主因」相距非常遠

目前公開證據支持：

$$
\boxed{
GenAI_{placeholder}>0
}
$$

但沒有可靠公開證據支持：

$$
\boxed{
GenAI_{core\ story}
}
$$

$$
\boxed{
GenAI_{music}
}
$$

$$
\boxed{
GenAI_{core\ code}
}
$$

$$
\boxed{
GenAI_{final\ character\ art}
}
$$

對成功具有可證明的重大貢獻。

---

# 42. 因此必須分成三種 AI Contribution

### A. Confirmed Direct GenAI

$$
\boxed{
\text{Temporary Placeholder Textures}
}
$$

證實。

### B. Claimed Current Final Assets

Sandfall 表示：

$$
\boxed{
\text{No current final GenAI-created assets}
}
$$

[S10]

### C. Undisclosed / Private Workflow

$$
\boxed{
Unknown
}
$$

公開資料不能證明完全不存在。

---

# 43. 「沒有公開證據」不能被寫成「絕對沒有」

本篇不能宣稱：

$$
\boxed{
GenAIUsage=0
}
$$

因為我們沒有：

- private logs；
- internal chat；
- source provenance；
- model usage records。

因此更嚴謹是：

$$
\boxed{
\text{No reliable public evidence found}
}
$$

---

# 44. 但同樣不能因「曾用過 AI」就把所有技術槓桿歸給 AI

如果把：

- Unreal；
- MetaHuman；
- Blueprint；
- motion capture；
- Marketplace；
- Nanite；
- Lumen；

全部稱為：

$$
\boxed{\text{AI Contribution}}
$$

那會產生嚴重分類錯誤。

因此：

$$
\boxed{
\text{Modern Toolchain Leverage}
\gg
\text{Disclosed Direct GenAI Leverage}
}
$$

是目前證據最支持的結論。

---

# 45. AI 爭議真正重要的是 governance，不是成功因果

2025 年底，Indie Game Awards 因其嚴格的 no-GenAI eligibility rule，撤回《33號遠征隊》的兩項獎項；爭議核心包括團隊先前 submission 中的 AI 使用聲明與後來確認的 placeholder 使用。[S17]

這件事證明：

$$
\boxed{
\text{Even Minor GenAI Use}
}
$$

也可能造成：

$$
\boxed{
\text{Disclosure / Eligibility Risk}
}
$$

但它不能證明：

$$
\boxed{
\text{GenAI caused the game's commercial success}
}
$$

---

# 46. 這是第 4 篇「製程價值」的現實例子

即使：

$$
V_{experience}
$$

完全沒有因 placeholder 爭議改變，

$$
V_{provenance}
$$

與：

$$
Trust
$$

仍可能改變。

所以：

$$
\boxed{
\text{Experience Value}
\neq
\text{Provenance Value}
}
$$

在本案中得到很好的實例。

---

# 47. Success Contribution Matrix

基於目前公開證據，本篇做如下**非百分比**評估：

| 因素 | 推定影響 | 證據強度 | 理由 |
|---|---|---:|---|
| 核心玩法／產品 vision | Very High | A | reactive turn-based 很早就確立並通過 prototype 驗證 |
| Scope Discipline | Very High | A/B | 大量 prototype 被丟棄；避開 full open world |
| UE5 / Blueprint / 技術工具鏈 | Very High | A | 開發者直接稱其為小團隊完成 vision 的關鍵槓桿 |
| Art Direction / 人類美術 | Very High | A/B | 長期具名 art direction、角色建模、mocap pipeline |
| 故事／角色／音樂人才 | Very High | A/B | 核心品牌辨識與 OST 獨立爆發 |
| 外部專業網路 | High | A/B | battle animation、QA、localization、porting 等 |
| Kepler 發行／流程資本 | High | A/B | 提供資源、建議、平台 release 經驗 |
| Xbox / Game Pass / 曝光 | High | A | 最大新第三方 Game Pass 首發；降低進入門檻 |
| Word-of-mouth / 社群擴散 | High but hard to isolate | B | 銷售曲線、社群與官方描述一致 |
| 生成式 AI：temporary placeholders | Low | A/B | 已確認，但對 current final product 的直接貢獻極小 |
| 生成式 AI：最終核心資產 | Not established | A/U | 官方稱 current game 無此類資產，無公開反證證明大量使用 |
| 運氣／時機 | Unknown but non-zero | A/B | 開發者自己亦承認與 UE5 時機相遇有幸運成分 |

---

# 48. 為什麼不能用百分比

因為這些因素不是相加：

$$
S
=
a_1+a_2+\dots+a_n
$$

而更像互相乘：

$$
\boxed{
S
\approx
V
\times
Q
\times
T
\times
I
\times
D
}
$$

例如：

> 沒有 Game Pass 是否還會成功？

可能仍會。

但：

> 沒有好產品，只剩 Game Pass？

很可能不會。

所以：

$$
\boxed{
\text{Causal Factors Are Interdependent}
}
$$

---

# 49. 本案最重要的不是「小團隊」

如果只看：

$$
N_{core}\approx30
$$

會錯過：

$$
\boxed{
\text{Effective Capability Network}
}
$$

真正投入能力包括：

- core；
- freelancers；
- external studios；
- publisher；
- engine ecosystem；
- platform partner。

所以：

$$
\boxed{
\text{Small Core}
\neq
\text{Small Capability Surface}
}
$$

---

# 50. 「小」的是管理核心，不是整個世界

這或許才是 Sandfall 模型真正值得學的地方：

$$
\boxed{
\text{Keep Intent Core Small}
}
$$

但：

$$
\boxed{
\text{Expand Capability Through Networks}
}
$$

於是：

$$
\boxed{
\text{Small Decision Core}
+
\text{Large External Capability Surface}
}
$$

---

# 51. 這和 Agentic Development 完全同構

第七篇提出：

$$
1\text{ Human}
+
N\text{ Specialized Agents}
$$

本案在人類組織上其實是：

$$
\boxed{
\text{Small Core Team}
+
N\text{ Specialized External Capabilities}
}
$$

共同核心都是：

$$
\boxed{
\text{Do Not Internalize Every Capability}
}
$$

---

# 52. 真正的能力是「選擇外接什麼」

Sandfall 沒有自己做：

- 全部 battle animation；
- 全部 QA；
- 全部 localization；
- 全部 porting；
- 自建 engine；
- 自建 rendering stack。

這些選擇可以理解成：

$$
\boxed{
\text{Selective Non-Ownership}
}
$$

這不是弱點。

而是：

$$
\boxed{
\text{Resource Allocation}
}
$$

---

# 53. 他們把內部資源留在哪裡？

公開資料顯示內部特別集中於：

- core gameplay；
- creative direction；
- art direction；
- narrative；
- characters；
- cinematics；
- technical integration。

這些更接近：

$$
\boxed{
\text{Identity-Critical Work}
}
$$

---

# 54. 這正是 Human-Retro 系列的核心

不是：

> 所有東西都人類自己做。

而是：

$$
\boxed{
\text{Human Attention}
\rightarrow
\text{Highest Identity Value Regions}
}
$$

其餘則可以：

- engine；
- middleware；
- external specialists；
- marketplace；
- automation；

共同承擔。

---

# 55. Value Transfer Efficiency

第四篇定義：

$$
\eta
=
\frac{
V_T
}{
E_{producer}
}
$$

《33號遠征隊》就是高：

$$
\boxed{
\text{Value Transfer Efficiency}
}
$$

案例。

不是因為：

> 團隊沒有投入努力。

而是因為：

$$
\boxed{
\text{大量投入集中在玩家真正能感受到的地方。}
}
$$

---

# 56. Scope Discipline 是最大的「負生產力」

一般人會把 productivity 理解成：

$$
\boxed{
\text{More Output}
}
$$

但 Sandfall 的案例顯示：

$$
\boxed{
\text{Not Building Expensive Low-Value Things}
}
$$

本身也是生產力。

可以稱：

$$
\boxed{
\text{Negative Production Efficiency}
}
$$

即：

> 因為沒有做錯東西，所以省下巨大成本。

---

# 57. Blueprint 是 Process Capital

第九篇定義 Process Capital。

在本案中 Blueprint 不只是 tool。

它形成：

$$
\boxed{
\text{Reusable Internal Production Logic}
}
$$

讓 non-programmers 能直接參與 implementation。

所以它提高：

$$
\boxed{
C_P
}
$$

而不只是：

$$
C_A
$$

---

# 58. Kepler 是外部 Process Capital

對第一次大型發行的 Sandfall：

$$
\boxed{
Kepler
}
$$

提供已經存在的：

- release knowledge；
- platform coordination；
- publishing experience。

這其實是：

$$
\boxed{
\text{Borrowed Process Capital}
}
$$

---

# 59. Unreal Marketplace / Fab 是外部 Artifact Capital

不需要自己：

> 每棵樹、每塊石頭、每個 generic prop 都從零做。

因此：

$$
\boxed{
\text{External Artifact Capital}
}
$$

讓內部 team 把時間集中到：

$$
\boxed{
\text{Hero Assets}
}
$$

與：

$$
\boxed{
\text{Identity-Critical Assets}
}
$$

---

# 60. 本案真正否定的是「全手工才有作者性」

如果一個作品大量使用：

- engine；
- MetaHuman；
- Marketplace；
- mocap；
- external studios；
- publisher；
- platform；

卻仍然呈現極強：

$$
\boxed{
\text{Authorial Identity}
}
$$

那就證明：

$$
\boxed{
\text{Authorial Identity}
\neq
\text{Manual Self-Production Ratio}
}
$$

---

# 61. 作者性更像選擇密度

第三篇定義：

$$
\boxed{
\text{Selection Density}
}
$$

本案真正讓人記住的：

- Belle Époque French fantasy；
- reactive turn-based；
- 特殊音樂；
- 角色；
- 情緒；
- scope。

都是：

$$
\boxed{
\text{High-Impact Selections}
}
$$

---

# 62. 這就是為什麼 GenAI 貢獻小，反而更有研究價值

如果最後研究結果是：

$$
\boxed{
\text{Direct GenAI Contribution}
\approx
\text{Minor}
}
$$

卻仍然：

$$
Success\gg
$$

那麼它直接否定：

> AI 是所有效率革命的中心。

真正更好的命題是：

$$
\boxed{
\text{Technology Choice}
+
\text{Scope Choice}
+
\text{Talent Choice}
+
\text{Partner Choice}
}
$$

---

# 63. 現代技術革命比生成式 AI 更大

Sandfall 真正使用的技術槓桿：

$$
\boxed{
\text{Engine}
+
\text{Visual Scripting}
+
\text{Realtime Rendering}
+
\text{Character Pipeline}
+
\text{Asset Ecosystem}
+
\text{Digital Distribution}
}
$$

很多根本不屬於 GenAI。

因此：

$$
\boxed{
\text{AI Era}
}
$$

不能被狹義理解成：

$$
\boxed{
\text{GenAI Era Only}
}
$$

---

# 64. 更精確的成功模型

本篇最終提出：

$$
\boxed{
S_{E33}
\approx
H_V
\times
S_Q
\times
S_D
\times
T_L
\times
I_Q
\times
N_E
\times
D_L
}
$$

其中：

- $H_V$：Human Vision；
- $S_Q$：Selection Quality；
- $S_D$：Scope Discipline；
- $T_L$：Technology Leverage；
- $I_Q$：Integration Quality；
- $N_E$：Network Externalization；
- $D_L$：Distribution Leverage。

---

# 65. GenAI 在這個公式裡放哪裡？

目前公開證據下：

$$
\boxed{
GenAI
\subset
T_L
}
$$

但只是：

$$
\boxed{
\text{small confirmed subcomponent}
}
$$

不能把：

$$
T_L
$$

全部等同：

$$
GenAI
$$

---

# 66. Counterfactual 1：沒有 GenAI placeholder，會不會失去成功？

依公開資料：

$$
\boxed{
\text{Probably Not}
}
$$

因為它們本來就是 temporary placeholders，且最終被替換。

因此：

$$
\boxed{
\Delta Success(GenAI_{placeholder})
\approx
0
}
$$

是合理的定性推論。

但這仍不是可精確測量的因果百分比。

---

# 67. Counterfactual 2：沒有 Unreal / UE5 呢？

這個反事實顯著不同。

開發者自己直接表示 Unreal 與 UE5 的能力，讓小團隊能完成幾年前不可能完成的 vision。[S03]

所以：

$$
\boxed{
\Delta Feasibility(Unreal)
}
$$

很可能非常大。

---

# 68. Counterfactual 3：沒有 scope discipline 呢？

如果改成：

$$
\boxed{
\text{Full Open World}
}
$$

在相同預算與團隊下：

$$
\boxed{
\text{Production Risk}\uparrow\uparrow
}
$$

而核心品質很可能被稀釋。

因此 scope control 很可能是：

$$
\boxed{
\text{Necessary Efficiency Condition}
}
$$

之一。

---

# 69. Counterfactual 4：沒有 Kepler / Xbox 呢？

作品仍然可能：

> 很好。

但：

$$
\boxed{
Reach
}
$$

與：

$$
\boxed{
\text{Release Capability}}
$$

很可能下降。

所以它們更像：

$$
\boxed{
\text{Success Amplifiers}
}
$$

而非：

$$
\text{Core Product Generators}
$$

---

# 70. Counterfactual 5：沒有 Lorien Testard 呢？

無法直接觀察。

但 154 首曲目與 3.33 億串流表示：

$$
\boxed{
\text{Music}
}
$$

已經成為品牌重要部分。

所以：

$$
\boxed{
\text{Talent Selection}
}
$$

很難被視為次要因素。

---

# 71. 這個案例對 AI 開發真正的啟示

最淺層：

> 用更好的工具。

更深層：

$$
\boxed{
\text{Use Tools to Change the Cost Structure}
}
$$

更深：

$$
\boxed{
\text{Use Cost Changes to Reallocate Human Attention}
}
$$

最深：

$$
\boxed{
\text{Use Human Attention on High-Identity Decisions}
}
$$

---

# 72. 所以真正問題不是「要不要 AI」

成熟問題是：

$$
\boxed{
\text{Which capability should be human?}
}
$$

$$
\boxed{
\text{Which capability should be tool-assisted?}
}
$$

$$
\boxed{
\text{Which capability should be externalized?}
}
$$

$$
\boxed{
\text{Which capability should not exist at all?}
}
$$

---

# 73. 這其實就是選擇底空間

設：

$$
\mathfrak B
$$

為開發者可用選擇底空間。

Sandfall 面對：

- engine；
- scope；
- team；
- freelancers；
- publisher；
- Game Pass；
- Marketplace；
- MetaHuman；
- art direction；
- combat design。

真正成功的不是：

$$
\boxed{
\text{選了一個 AI 工具。}
}
$$

而是：

$$
\boxed{
\text{在整個 }\mathfrak B\text{ 中形成了一組高品質選擇。}
}
$$

---

# 74. 「選擇」甚至發生在不選什麼

例如：

$$
\boxed{
\neg OpenWorld
}
$$

$$
\boxed{
\neg CustomEngine
}
$$

$$
\boxed{
\neg InternalizeAllSpecialists
}
$$

這些：

$$
\boxed{
\text{Negative Choices}
}
$$

同樣是成功因果的一部分。

---

# 75. 被選擇也同樣重要

Sandfall 選 Kepler。

但 Kepler 也選 Sandfall。

Sandfall 選 Xbox 合作。

Xbox 也因早期 build、視覺與玩法認為它值得投入曝光。[S09]

因此：

$$
\boxed{
\text{Selection}
}
$$

是雙向的：

$$
\boxed{
\text{A chooses B}
\land
\text{B chooses A}
}
$$

---

# 76. 人才也是互選

Guillaume 找到 Lorien。

Lorien 也選擇加入。

團隊找到 Jennifer。

Jennifer 也選擇留下並成為 lead writer。

所以：

$$
\boxed{
\text{Successful Team Formation}
}
$$

本身就是：

$$
\boxed{
\text{Mutual Selection Network}
}
$$

---

# 77. 本案例真正支持第 14 篇，而不是「AI 勝利論」

如果 GenAI 直接貢獻其實很小，

但成功仍巨大，

那整個系列的最終命題反而更清楚：

$$
\boxed{
\text{真正重要的不是 AI 本身。}
}
$$

而是：

$$
\boxed{
\text{如何選擇，以及如何讓自己進入會被正確人、工具與平台選擇的位置。}
}
$$

---

# 78. 研究限制

本篇仍有以下限制。

第一：

$$
\boxed{
\text{No Internal Cost Ledger}
}
$$

所以無法精確分配成本。

第二：

$$
\boxed{
\text{No Private AI Logs}
}
$$

所以不能證明所有未公開 AI 用途為零。

第三：

$$
\boxed{
\text{Public Interviews Have Narrative Bias}
}
$$

成功後訪談會自然重新敘述成功。

第四：

$$
\boxed{
\text{Contribution Factors Interact}
}
$$

所以不能把每項拆成真正百分比。

---

# 79. 未來如果有更完整資料，可以怎麼驗證

如果未來取得：

- production logs；
- source history；
- outsourcing contracts；
- publisher budget；
- model usage logs；
- Steam / platform telemetry；
- marketing spend；

就可以建立：

$$
\boxed{
\text{Counterfactual Production Model}
}
$$

更精確估計：

$$
\Delta Cost
$$

$$
\Delta Time
$$

$$
\Delta Reach
$$

與：

$$
\Delta Quality
$$

---

# 80. 本篇的最終判斷

基於截至 2026-09-08 的公開證據：

### 判斷一

$$
\boxed{
\text{Direct Disclosed GenAI Contribution}
=
\text{Low}
}
$$

### 判斷二

$$
\boxed{
\text{Modern Technology Leverage}
=
\text{Very High}
}
$$

### 判斷三

$$
\boxed{
\text{Human Creative / Selection Contribution}
=
\text{Very High}
}
$$

### 判斷四

$$
\boxed{
\text{External Network / Publisher / Platform Leverage}
=
\text{High}
}
$$

---

# 81. 這不是「人類打敗 AI」

因為 Unreal、MetaHuman、Blueprint、自動化工具本身就是現代技術槓桿。

所以不能寫：

$$
\boxed{
\text{Human}
>
\text{Technology}
}
$$

更合理是：

$$
\boxed{
\text{Human Vision}
\times
\text{Technology Leverage}
}
$$

---

# 82. 也不是「AI 打敗 AAA」

因為目前證據完全不足以支持：

$$
\boxed{
GenAI
\rightarrow
\text{AAA-cost collapse}
}
$$

真正可以支持的是：

$$
\boxed{
\text{Mature Engines}
+
\text{Accessible Tools}
+
\text{Digital Ecosystems}
+
\text{External Networks}
}
$$

共同降低成本牆。

---

# 83. 最終結論：真正稀缺的是選擇品質

《光與影：33號遠征隊》的成功故事，如果只被壓縮成：

> 三十個人做出 AAA。

太淺。

如果壓縮成：

> AI 讓小團隊成功。

更不符合現有證據。

更精確的描述是：

$$
\boxed{
\text{一個小型決策核心，使用現代工具與外部能力網路，將有限資源集中在高身份、高體驗價值的選擇上。}
}
$$

因此本篇最重要的公式不是：

$$
\boxed{
AI
\rightarrow
Success
}
$$

而是：

$$
\boxed{
\text{Selection Quality}
\times
\text{Technology Leverage}
\times
\text{Human Vision}
\rightarrow
\text{Disproportionate Output}
}
$$

本案最值得學習的地方，不是：

> 他們用了哪一個神奇工具？

而是：

$$
\boxed{
\text{他們知道哪些東西值得自己做，哪些東西值得交給工具，哪些值得交給外部專家，哪些根本不值得做。}
}
$$

這也把整個系列的問題從：

$$
\boxed{
\text{AI vs Human}
}
$$

徹底推進到：

$$
\boxed{
\text{Selection vs Unexamined Production}
}
$$

而這正是第 13 篇「人類復古創作者」與第 14 篇「選擇的選擇與被選擇的選擇」真正需要的實證支點。

---

# 附錄 A：核心證據矩陣

| Evidence ID | 主題 | 證據層級 | 可支持的核心命題 |
|---|---|---:|---|
| S01 | 500 萬銷量、3.33 億 OST streams | A | 商業與文化擴散成功 |
| S02 | 一周年 800 萬銷量 | A | 長尾商業成功 |
| S03 | Unreal 開發者訪談 | A | Blueprint / MetaHuman / Lumen / Nanite / 小團隊槓桿 |
| S04 | GDC 2026 / 95% Blueprint | B | Blueprint 作為組織與生產 force multiplier |
| S05 | GameMakers 開發史 | B | prototype 篩選、peak 35、外包、QA/localization/porting |
| S06 | Sandfall 2023 update | A | 12→22、Kepler、freelancer / UE5 |
| S07 | NYT syndication / The Star | B | 約 USD 10M、scope control、外部支援、人才招募 |
| S08 | MobyGames credits | B | 438 credits，拆解「30 人完成全部」神話 |
| S09 | Xbox Wire | A | Game Pass、Xbox 曝光與降低進入門檻 |
| S10 | El País + Sandfall clarification | A/B | GenAI placeholder 實際用途與 current assets 澄清 |
| S11 | 官方 Patch 1.3.0 | A | placeholder textures 被移除 |
| S12 | MobyGames detailed credits | B | 多種外部 production roles |
| S13 | Game Informer 作曲家訪談 | B | SoundCloud 招募、154 首曲目 |
| S14 | GNN Jennifer 訪談 | B | Kepler 流程槓桿、團隊持續調整流程 |
| S15 | Nicholas ArtStation | B | 4.5 年 art direction、#NoAI |
| S16 | Alan Reynaud ArtStation | B | 長期角色 modeling / texturing / final look |
| S17 | Indie Game Awards 爭議報導 | C | GenAI 微量使用仍可能造成 disclosure / eligibility risk |

---

# 附錄 B：來源

**[S01]** Sandfall Interactive / Expedition 33. “Thank you from Sandfall Interactive!” 2025-10-08.  
https://www.expedition33.com/post/thank-you-from-sandfall-interactive

**[S02]** Sandfall Interactive / Expedition 33. “1st Anniversary of Clair Obscur: Expedition 33.” 2026-04-24.  
https://www.expedition33.com/post/1st-anniversary-of-clair-obscur-expedition-33

**[S03]** Epic Games / Unreal Engine. “Inside the development journey of Clair Obscur: Expedition 33.” 2025-03-27.  
https://www.unrealengine.com/developer-interviews/inside-the-development-journey-of-clair-obscur-expedition-33

**[S04]** Game Developer. “Clair Obscur: Expedition 33 was built ‘95 percent’ with Unreal Engine Blueprints.” 2026-03-11.  
https://www.gamedeveloper.com/programming/clair-obscur-expedition-33-was-built-95-percent-with-unreal-blueprints

**[S05]** GameMakers Japan. Guillaume Broche / Tom Guillermin interview. 2025-08-05.  
https://gamemakers.jp/article/2025_08_05_112871/?PageSpeed=noscript

**[S06]** Sandfall Interactive. “March 2023 update: Project W to be published by Kepler Interactive.” 2023-03-21.  
https://www.sandfall.co/post/march-2023-update-project-w-to-be-published-by-kepler-interactive

**[S07]** The New York Times report syndicated by The Star. “A gaming tour de force that is very, very French.” 2025-12-29.  
https://www.thestar.com.my/tech/tech-news/2025/12/29/a-gaming-tour-de-force-that-is-very-very-french

**[S08]** MobyGames. “Clair Obscur: Expedition 33 credits (Windows, 2025).”  
https://www.mobygames.com/game/241065/clair-obscur-expedition-33/credits/windows/

**[S09]** Xbox Wire. “Clair Obscur: Expedition 33 Is the Biggest New Third-Party Game Launch on Xbox Game Pass of 2025.” 2025-12-03.  
https://news.xbox.com/en-us/2025/12/03/clair-obscur-expedition-33-game-pass-biggest-launch/

**[S10]** El País. “The low-cost creative revolution: How technology is making art accessible to everyone.” 2025-07-19, including Sandfall clarification.  
https://english.elpais.com/culture/2025-07-19/the-low-cost-creative-revolution-how-technology-is-making-art-accessible-to-everyone.html

**[S11]** Expedition 33. “Patch 1.3.0 Is Now Live.”  
https://www.expedition33.com/post/patch-1-3-0-is-now-live

**[S12]** MobyGames. Full Windows credits, 438 people / 530 credits at retrieval.  
https://www.mobygames.com/game/241065/clair-obscur-expedition-33/credits/windows/

**[S13]** Game Informer. “Clair Obscur’s Composer Talks Going From Unknown To Scoring 2025’s Most Celebrated RPG.” 2025-05-16.  
https://www.gameinformer.com/interview/2025/05/15/clair-obscurs-composer-talks-going-from-unknown-to-scoring-2025s-most

**[S14]** 巴哈姆特 GNN. “《光與影：33 號遠征隊》首席編劇獨家專訪…” 2025-03-17.  
https://gnn.gamer.com.tw/detail.php?sn=282338

**[S15]** Nicholas Maxson-Francombe. ArtStation, “Clair Obscur: Expedition 33.”  
https://nicholas-maxson-francombe.artstation.com/projects/1xmQXK

**[S16]** Alan Reynaud. ArtStation, Clair Obscur character work (e.g. Verso / Gustave).  
https://www.artstation.com/artwork/x3rx3X

**[S17]** PC Gamer. Indie Game Awards GenAI eligibility dispute. 2025-12-21.  
https://www.pcgamer.com/games/rpg/indie-game-awards-pulls-two-awards-from-clair-obscur-over-generative-ai-use-we-have-a-hard-stance-against-gen-ai-in-videogames/

---

## 附錄 C：一句話結論

$$
\boxed{
\text{《33號遠征隊》不是「AI 取代人類」的成功案例，而是「人類用選擇把現代技術變成槓桿」的成功案例。}
}
$$
