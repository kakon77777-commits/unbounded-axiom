# 從 MOD 到世界線：AI 共生成時代的遊戲原生性分化命題

## From Mods to Worldlines: A Conjecture on the Stratification of Game Nativeness in the Age of AI Co-Generation

**作者：Neo.K**  
**機構：EveMissLab／一言諾科技有限公司**  
**版本：v1.0-public**  
**日期：2026 年 8 月 12 日**  
**文件性質：公開命題猜想論文／技術與產業預測**

---

## 摘要

本文提出「**遊戲世界線常規化猜想**」（Game Worldline Normalization Conjecture, GWNC）：當人工智慧逐步取得對遊戲內容、角色、事件、資產與部分規則的理解能力，並能在權限、驗證與回滾機制下於遊戲運行期間生成或修改內容時，今日被視為附加物的 MOD，將不再只是少數玩家在遊戲外部安裝的修改包，而會逐步成為遊戲的常規互動形式。

在此條件下，遊戲市場不會簡單地從「原生」轉向「全部生成」，而會形成多層次的原生性分化：歷史原生、原生增強、官方生成、驗證分支、社群分支、個人 AI 世界線與完全轉換世界將長期並存。玩家不再只回答「我有沒有玩過這款遊戲」，而會回答「我玩的是哪一個基底版本、哪一條世界線、使用哪些生成權限，以及該世界是否仍屬可驗證的原作譜系」。

本文以形式化方式區分遊戲本體、修改序列、世界線與原生性向量，提出十項可檢驗的次級猜想，並建立弱版本與強版本兩種預測。弱版本預測 AI 將大幅降低 MOD 與使用者生成內容的製作門檻；強版本則預測，部分遊戲類型將出現玩家在遊玩過程中與 AI 持續共同修改世界、事件乃至局部規則的商業化產品。本文同時提出 2030、2032 與 2035 年的觀察指標，以及可使強版本猜想被否證的條件。

本文不主張所有遊戲都會成為生成式世界，也不主張傳統作者制、固定劇情或原生版本會消失。相反地，本文預測：當分支世界大量增加時，可驗證的原生版本將因其歷史性、可比較性、競技公平與共同記憶而獲得更高的基準價值。

**關鍵詞：** 人工智慧、遊戲 MOD、使用者生成內容、即時生成、遊戲世界線、原生性、世界分支、動態遊戲、生成式遊戲、數位文化保存

---

## Abstract

This paper proposes the **Game Worldline Normalization Conjecture (GWNC)**. The conjecture states that, once artificial intelligence can understand and modify game content, characters, events, assets, and selected rules during play under explicit authorization, validation, and rollback constraints, modifications will cease to be merely external add-ons produced by a technical minority. Instead, they will become a normal mode of interacting with games.

The resulting market will not simply replace “native games” with fully generated games. It will stratify into historically canonical editions, enhanced canonical editions, officially generated content, verified branches, community branches, personal AI worldlines, and total conversions. Players will increasingly identify not only the title they played, but also its base version, branch lineage, generation permissions, and verification status.

The paper formalizes the distinction between a base game, a sequence of modifications, a persistent worldline, and a multidimensional nativeness vector. It advances ten subordinate conjectures, separates a weak prediction from a strong prediction, and proposes observable milestones for 2030, 2032, and 2035. The weak prediction concerns the normalization of AI-assisted mod creation. The strong prediction concerns persistent, in-play, player–AI co-generated game branches that may alter content and selected rules.

The paper does not predict the disappearance of static games, authored narratives, or canonical editions. On the contrary, it argues that increasing branch diversity may raise the cultural and commercial value of verified canonical play.

**Keywords:** artificial intelligence, game mods, user-generated content, live generation, game worldlines, nativeness, branching worlds, generative games

---

# 一、公開範圍與命題聲明

本文是一篇公開的預測性命題論文，而不是特定產品的技術規格、公司路線圖或開發承諾。

本文刻意不涉及：

- 特定企業、團隊或商業收購計畫；
- 特定經典遊戲的改造目標；
- 私有 Runtime、資料格式或中間表示；
- 可直接實作的核心程式架構；
- 尚未公開的研究樣本與測試資料；
- 特定模型供應商或內部權限設計。

本文只處理一個公共命題：

> **當 AI 能在遊戲運行期間，以足夠低的成本理解並受控地修改遊戲時，MOD 是否會從遊戲之外的附加行為，轉變為遊戲之內的常規行為？**

本文的答案是：**在部分遊戲類型中，高機率會；但它不會消滅原生遊戲，而會迫使「原生」被重新定義。**

---

# 二、問題的提出：MOD 為何仍被視為例外？

傳統遊戲產品大多遵循以下結構：

```text
開發者建立遊戲
→ 測試與封裝
→ 發行固定版本
→ 玩家消費完成品
→ 少數玩家在遊戲之外製作 MOD
```

在這個結構中，MOD 之所以是例外，不只是因為遊戲公司不允許修改，也因為修改本身具有很高的摩擦成本：

1. 玩家需要理解檔案、腳本、引擎或逆向工具；
2. 修改內容需要離開主要遊戲流程；
3. 不同 MOD 可能彼此衝突；
4. 更新可能破壞相容性；
5. 多人遊戲需要版本一致；
6. 玩家往往無法判斷修改的來源、品質與安全性；
7. 大型規則變更需要接近專業開發者的能力。

因此，過去的 MOD 生態系雖然能延長遊戲壽命，卻通常建立在「遊戲已完成、修改者在外部追加內容」的前提上。

AI 改變的並不只是內容生成速度。它可能同時降低四種成本：

$$
C_{\mathrm{mod}}
=
C_{\mathrm{expression}}
+
C_{\mathrm{creation}}
+
C_{\mathrm{integration}}
+
C_{\mathrm{maintenance}}.
$$

其中：

- $C_{\mathrm{expression}}$：玩家把想法轉換成可執行規格的成本；
- $C_{\mathrm{creation}}$：製作文字、圖片、聲音、程式與資料的成本；
- $C_{\mathrm{integration}}$：把新內容接回遊戲的成本；
- $C_{\mathrm{maintenance}}$：版本更新、相容性、測試與修復的成本。

當玩家只需要用自然語言或簡單操作表達意圖，而 AI 可以協助完成後續轉換時，MOD 的社會位置就可能發生根本改變。

---

# 三、現有前兆：零件已出現，但尚未完成合流

本文並不主張通用的即時遊戲共生成已經實現。更準確的說法是：構成它的若干零件已分別出現在不同技術路線中。

## 3.1 平台已承認「運行中生成」是一種正式產品型態

Steamworks 的內容調查已明確區分「開發期間預先生成」與「遊戲運行期間生成」的 AI 內容。後者需要開發者說明防護措施，平台文件甚至直接討論持續推理成本可能如何透過本體價格、微交易、訂閱或 DLC 處理。[1]

這不代表即時共生成已成熟，但它表示大型發行平台已經把「遊戲運行中持續生成內容」視為需要正式治理與商業處理的產品類型，而不是純粹的研究展示。

## 3.2 MOD 與 UGC 已具有成熟的分發、更新與商業機制

Steam Workshop 長期支援玩家上傳、下載、更新與販售 MOD 或使用者生成內容。其官方文件特別指出，大規模 MOD 需要遊戲事先提供建立、編輯、驗證與載入內容的工具，並區分可直接使用與需要策展審核的兩種模式。[2]

這表示「玩家內容成為遊戲長期組成」早已存在。AI 帶來的主要變化不是發明 UGC，而是降低其製作門檻、提高生成速度，並把部分創作行為移入遊玩過程。

## 3.3 遊戲引擎中的 AI 已開始取得專案語境與編輯權限

Unity 的官方 AI 工具已強調專案內的語境理解，可以檢查場景、GameObject 與元件，協助執行編輯器操作，並檢查變更是否符合預期。[3] Roblox Studio 的 Assistant 則能直接建立與修改物件及腳本、插入資產、生成材質與模型，並透過命令系統操作專案資料模型。[4]

這些工具目前主要服務開發階段，但它們顯示 AI 已從「回答遊戲開發問題」進入「理解並修改遊戲工程」的階段。

## 3.4 玩家創作平台正在把規則建立與經濟回報制度化

UEFN 與 Verse 讓創作者建立自己的遊戲規則與行為，而 Fortnite 的創作者生態也已有依玩家參與度分配收益的機制。[5][6] 這說明大型遊戲平台正在從單一作品轉向「穩定基底＋大量創作者世界」的結構。

## 3.5 即時生成世界已具有初步技術證據

GameNGen 展示了以神經模型即時模擬《DOOM》互動軌跡的可能性，論文報告其可在單一 TPU 上超過每秒 20 幀。[7] Google DeepMind 的 Genie 3 則展示了由文字描述生成可即時探索環境的能力，並支援可提示的世界事件；但其持續時間、動作空間、多智能體互動與精確一致性仍有限。[8]

這些研究證明「生成式模型直接產生可互動畫面」正在進步，但它們尚不能替代具有長期狀態、可驗證規則、完整存檔與數十小時因果一致性的傳統遊戲引擎。

## 3.6 角色記憶與社會模擬已有可行原型

Generative Agents 研究展示了帶有記憶、反思與規劃機制的角色如何在互動環境中形成日常行為與社會事件。[9] 這支持 AI NPC 從單次對話介面轉向持續角色狀態的可能性。

綜合而言，現有技術呈現的是：

```text
AI 專案編輯
＋
即時生成世界
＋
持續角色代理
＋
成熟 UGC 分發
＋
平台治理與商業化
```

但上述零件尚未普遍合流成：

```text
玩家遊玩
→ 與 AI 協商修改
→ 世界產生持久分支
→ 修改經過驗證
→ 可分享、回滾與治理
```

本文的預測正是關於這一合流是否會發生，以及發生後遊戲概念將如何改變。

---

# 四、核心定義

## 4.1 基底遊戲

令一款已發行或被指定為基準的遊戲為：

$$
\mathcal G_0
=
\left(
S_0,
R_0,
A_0,
E_0,
U_0
\right),
$$

其中：

- $S_0$：初始與可持續的遊戲狀態；
- $R_0$：規則與判定；
- $A_0$：資產；
- $E_0$：事件、文本與敘事；
- $U_0$：介面與操作方式。

 $\mathcal G_0$ 不必是最早歷史版本，也可以是某個官方指定的重製版、賽季版或競技版。

## 4.2 修改操作

一次修改記作：

$$
\pi_i:
\mathcal G_{i-1}
\longrightarrow
\mathcal G_i.
$$

 $\pi_i$ 可以是：

- 修正錯誤；
- 替換資產；
- 新增角色；
- 生成支線；
- 修改數值；
- 改變規則；
- 加入新的互動方式；
- 由玩家與 AI 在運行期間共同提出的變更。

## 4.3 遊戲世界線

由基底遊戲與一連串持久修改形成的世界，定義為：

$$
\mathcal W_t
=
\pi_t
\circ
\pi_{t-1}
\circ
\cdots
\circ
\pi_1
\left(
\mathcal G_0
\right).
$$

本文將 $\mathcal W_t$ 稱為「**遊戲世界線**」。

世界線與傳統 MOD 組合的差別，不一定在技術格式，而在其社會與產品位置：世界線被視為玩家實際遊玩的持續版本，具備來源、歷史、權限與可分享身分，而不是臨時覆寫的一組散落檔案。

## 4.4 常規化

本文所稱「常規化」，不是指所有玩家都必須使用，而是某種功能同時滿足：

1. 能從遊戲或平台的標準介面進入；
2. 不要求專業程式或逆向技能；
3. 平台承認並治理其存在；
4. 玩家把它視為正常玩法，而不是例外操作；
5. 內容可持久保存、更新與分享。

令上述條件分別為 $u,e,p,s,h$，則可簡化表示為：

$$
\operatorname{Norm}(x)
=
u
\land
e
\land
p
\land
s
\land
h.
$$

當 $\operatorname{Norm}(\text{AI-assisted modification})=1$ 時，AI 修改才真正從開發工具轉為常規遊戲功能。

## 4.5 原生性向量

「原生／非原生」不應只是二元標籤。本文定義：

$$
\mathbf N(\mathcal W)
=
\left(
n_{\mathrm{source}},
n_{\mathrm{rule}},
n_{\mathrm{history}},
n_{\mathrm{license}},
n_{\mathrm{verification}}
\right)
\in [0,1]^5.
$$

其中：

- $n_{\mathrm{source}}$：是否由原權利方、官方團隊或其授權系統產生；
- $n_{\mathrm{rule}}$：是否遵守原生規則與世界約束；
- $n_{\mathrm{history}}$：內容是否存在於初始或歷史版本；
- $n_{\mathrm{license}}$：內容是否具備清楚合法的使用與改作權；
- $n_{\mathrm{verification}}$：世界線是否可驗證、重現並通過相容性檢查。

一個官方 AI 在遊戲中生成的新任務，可能具有：

```text
來源原生：高
規則原生：高
歷史原生：低
授權原生：高
驗證原生：中至高
```

玩家自行製作但嚴格遵守世界設定的支線，則可能具有：

```text
來源原生：低
規則原生：高
歷史原生：低
授權原生：視授權而定
驗證原生：視平台而定
```

因此，未來爭論的重點不再只是「這是不是 MOD」，而是「它在哪些維度上仍屬原作譜系」。

---

# 五、遊戲世界線常規化猜想

## 5.1 主猜想

> **遊戲世界線常規化猜想：**  
> 當 AI 的意圖理解、內容生成、專案理解、規則修改、測試與驗證能力，配合遊戲引擎提供的合法修改權限，將玩家個人化世界的總成本降至其主觀與社群價值以下時，至少在角色扮演、模擬、沙盒、經營與創作平台等類型中，持久的玩家—AI 世界分支將由少數 MOD 行為轉變為常規玩法。

可表示為：

$$
C_{\mathrm{creation}}
+
C_{\mathrm{integration}}
+
C_{\mathrm{validation}}
+
C_{\mathrm{governance}}
\le
V_{\mathrm{personalization}}
+
V_{\mathrm{community}}
+
V_{\mathrm{retention}}.
$$

若上述不等式長期成立，則在適合的遊戲類型集合 $\mathfrak G$ 中：

$$
\Pr
\left(
\text{玩家使用至少一條持久個人分支}
\mid
\mathcal G \in \mathfrak G
\right)
$$

將顯著提高。

主猜想並不要求「超過所有玩家的一半」才成立。只要世界分支成為平台、媒體、商店與遊戲介面必須正式支援的主流產品類別，即可視為常規化。

---

# 六、弱版本與強版本

## 6.1 弱版本猜想

弱版本主張：

> AI 將使製作、移植、除錯、翻譯、整合與維護 MOD 的門檻大幅下降；大量原本不會寫程式的玩家，將能透過自然語言與可視化介面建立個人內容。

弱版本不要求 AI 在遊戲運行期間改寫規則，也不要求永久世界分支。它可以發生在遊戲之外：

```text
玩家描述需求
→ AI 修改專案或 MOD
→ 測試
→ 玩家重新載入遊戲
```

依照目前引擎與創作平台的發展，弱版本具有較高可信度。

## 6.2 強版本猜想

強版本主張：

> 部分遊戲將允許玩家在遊玩期間，直接與 AI 協商新增角色、事件、地區、系統或局部規則；變更會成為該玩家世界的持久歷史，並可被驗證、回滾、分享或策展。

其流程可抽象為：

```text
玩家意圖
→ AI 提出變更
→ 權限與一致性檢查
→ 建立持久分支
→ 遊戲繼續運行
```

強版本要求的不只是生成能力，而是：

- 足夠的遊戲語義理解；
- 對內容或規則的受控寫入權；
- 狀態與存檔遷移；
- 衝突檢查；
- 版本身分；
- 回滾；
- 內容治理；
- 長期成本模型。

因此，強版本發生得更慢，也更可能先出現在時間離散、狀態明確、規則可模組化的類型中，而不是高競技性或高物理複雜度的作品。

---

# 七、十項次級猜想

## 命題一：MOD 常規化猜想

當 AI 使「想法到可玩內容」的轉換不再需要專業工具鏈時，MOD 將由名詞轉為動詞。

玩家不再說：

> 我去找一個符合需求的 MOD。

而可能說：

> 我讓遊戲替這一局生成一個新的職業系統。

這不是 MOD 消失，而是 MOD 的行為被吸收進遊玩介面。

---

## 命題二：原生性分層猜想

未來遊戲將不再只分成：

```text
未修改
／
已修改
```

而會形成至少六個常見層級：

| 層級 | 名稱 | 說明 |
|---|---|---|
| L0 | 歷史原生 | 原始版本或經嚴格模擬的歷史版本 |
| L1 | 原生增強 | 不改核心規則，只改善相容性、介面與品質 |
| L2 | 官方生成 | 由官方授權 AI 在規則邊界內生成 |
| L3 | 驗證分支 | 非歷史內容，但通過官方或社群驗證 |
| L4 | 個人世界線 | 玩家與 AI 共同形成的持久個人版本 |
| L5 | 完全轉換 | 大幅改變世界、玩法或身分的衍生作品 |

其中任何一層都不必被視為低於另一層；它們滿足的是不同的遊玩目的。

---

## 命題三：世界線將成為新的消費單位

傳統商品單位是：

$$
\text{Game Product}
=
\text{Versioned Build}.
$$

未來部分產品將轉為：

$$
\text{Game Product}
=
\left(
\text{Canonical Core},
\text{Permissions},
\text{Generation Capacity},
\text{Branch History},
\text{Governance}
\right).
$$

玩家購買的不再只是固定內容量，而是：

- 進入哪個世界的權利；
- 能修改哪些層級；
- 可以生成多少內容；
- 是否能保存與分享分支；
- 是否能使用官方驗證與託管；
- 是否能將個人世界轉為公開作品。

---

## 命題四：原生版本溢價猜想

直覺上，分支越多，原生版本的重要性似乎越低。本文預測相反效果也會同時發生。

令分支多樣性為 $B$，原生基準價值為 $V_{\mathrm{canonical}}$。在一定區間內：

$$
\frac{\partial V_{\mathrm{canonical}}}{\partial B}
>
0.
$$

原因是分支越多，玩家越需要：

- 共同基準；
- 歷史保存；
- 競速與競技比較；
- 原作者設計研究；
- 社群共同記憶；
- 判斷改造效果的對照組。

因此，「原汁原味」不會消失，而可能從預設選項轉為被主動選擇的高可信模式。

---

## 命題五：開發者角色將由內容作者擴張為世界憲法設計者

在固定遊戲中，開發者主要決定玩家能看到什麼內容。

在可持續生成的遊戲中，開發者還必須決定：

- 什麼可以被生成；
- 什麼可以被修改；
- 哪些角色與規則不可變；
- 哪些修改需要玩家確認；
- 哪些內容只能存在於私人分支；
- 哪些分支能進入多人或排行榜；
- 什麼條件下仍算同一款遊戲。

因此，原作者不會因 AI 而消失，而會部分轉為設計世界的「憲法、權限與身分邊界」。

---

## 命題六：作者性將由單點轉為分層結構

一條 AI 世界線可能同時包含：

- 原始世界與角色作者；
- 原權利方；
- 引擎與工具提供者；
- 模型與資料提供者；
- 玩家提出的意圖；
- AI 生成的候選內容；
- 策展者的取捨；
- 社群的修正與驗證。

因此：

$$
\text{Authorship}
\neq
\text{Single Author}.
$$

更接近：

$$
\text{Authorship}
=
\text{Origin}
+
\text{Constraint}
+
\text{Generation}
+
\text{Selection}
+
\text{Curation}.
$$

未來爭論不只是「AI 算不算作者」，而是每一層對作品負責到什麼程度，以及收益與署名如何分配。

---

## 命題七：驗證遊玩將成為獨立模式

多人遊戲、排行榜、速通與成就需要可比較的規則。

因此未來遊戲可能提供：

```text
Verified Canonical
Verified Extended
Open Generated
Private Experimental
```

不同模式具有不同權限：

| 功能 | 驗證原生 | 驗證擴展 | 開放生成 |
|---|---:|---:|---:|
| 官方成就 | 是 | 部分 | 否或另立 |
| 全球排行榜 | 是 | 視規則 | 否 |
| AI 對話 | 可選 | 是 | 是 |
| 規則修改 | 否 | 有限 | 是 |
| 世界分支 | 僅存檔 | 經驗證 | 自由 |
| 多人相容 | 完整 | 同分支 | 私人或自訂 |

「你用了 MOD，所以不能進排行榜」將被更細緻的版本與能力聲明取代。

---

## 命題八：世界分支經濟將形成

當世界線可以保存、策展與分享後，可能出現新的商品與勞動：

- 高品質世界分支；
- 事件包與規則包；
- AI 角色人格包；
- 驗證與相容性服務；
- 世界託管；
- 私人生成額度；
- 策展與編輯；
- 版權方授權的 IP 世界模板；
- 社群分支收益分配。

但市場的核心稀缺資源未必是「生成量」，而更可能是：

- 品質；
- 一致性；
- 可玩性；
- 原作理解；
- 合法性；
- 長期維護；
- 社群信任。

因此，AI 可能使低品質內容爆量，也同時提高優秀策展者與系統設計者的價值。

---

## 命題九：經典遊戲重製將更常見，但瓶頸會轉移

AI 能協助：

- 素材分類與修復；
- 程式轉譯；
- 規則整理；
- 測試生成；
- 介面重建；
- 翻譯；
- 角色與事件擴充。

因此，經典遊戲重製與再發行的技術成本可能下降。

然而瓶頸將轉移到：

- 權利鏈是否清楚；
- 原始資料是否保存；
- 修改是否尊重原作；
- 新內容是否形成一致風格；
- 是否能證明新版本沒有破壞核心規則；
- AI 生成內容的授權與責任。

經典遊戲不會因 AI 自動全部復活，但「原本不值得投入重製成本的作品」可能重新進入商業可行區間。

---

## 命題十：固定遊戲不會消失

本文拒絕「所有遊戲都將生成化」的強決定論。

以下作品仍可能偏好固定內容：

- 精密設計的線性敘事；
- 作者風格高度集中的藝術遊戲；
- 電競與嚴格平衡作品；
- 需要共同解謎答案的遊戲；
- 以關卡手工節奏為核心的作品；
- 玩家希望獲得有限、完整與可結束體驗的作品。

生成式世界與固定作品的關係，更可能類似：

```text
電影
與
互動式媒體

桌遊固定規則
與
角色扮演自由敘事

原生遊戲
與
個人世界線
```

兩者並存，而不是單向淘汰。

---

# 八、為什麼這不只是「程序生成 2.0」？

傳統程序生成通常由開發者事先定義生成器：

$$
x
\sim
P_\theta
\left(
x
\mid
R_{\mathrm{fixed}}
\right),
$$

其中 $R_{\mathrm{fixed}}$ 是固定規則。玩家得到不同地圖或事件，但無法自然語言協商生成器本身。

AI 共生成的強版本則可能允許：

$$
R_t
\longrightarrow
R_{t+1},
$$

也就是玩家不只要求「生成另一張地圖」，還可能要求：

- 改變地圖如何生成；
- 新增一種社會制度；
- 讓某個 NPC 形成長期記憶；
- 新增職業或交易規則；
- 改變一條任務的因果結構；
- 建立只存在於本次世界線的玩法。

差異不在於 AI 比亂數更「有創意」，而在於生成對象可能從內容擴張到部分規則與世界結構。

---

# 九、為什麼這不只是「更方便的 MOD 工具」？

從技術譜系看，它確實是 MOD 的延伸。

但當以下四個條件同時發生時，量變會造成產品類型的質變：

1. **時間位置改變**：修改從遊戲外部進入遊玩期間；
2. **參與人口改變**：從技術少數擴張到普通玩家；
3. **持久性改變**：修改成為世界歷史，而非一次性覆寫；
4. **治理位置改變**：平台正式辨識、驗證、分發與收費。

傳統 MOD 的核心語法是：

```text
我修改了一個完成品。
```

世界線遊戲的核心語法則是：

```text
我正在遊玩一個會因我與 AI 的共同決定而持續形成的版本。
```

兩者有連續性，但玩家主觀經驗與產業結構不同。

---

# 十、遊戲身分與動態不動點

當一款遊戲被持續修改，終究會遇到忒修斯式問題：

> 修改到什麼程度，它仍然是原來那款遊戲？

令世界線與基底遊戲的加權差異為：

$$
D_\omega
\left(
\mathcal W,
\mathcal G_0
\right)
=
\sum_{k=1}^{m}
\omega_k d_k,
$$

其中 $d_k$ 可以分別表示：

- 規則差異；
- 角色差異；
- 敘事差異；
- 美術差異；
- 操作差異；
- 世界觀差異；
- 勝負與結局結構差異。

定義身分連續性：

$$
I
\left(
\mathcal W,
\mathcal G_0
\right)
=
1
-
D_\omega
\left(
\mathcal W,
\mathcal G_0
\right).
$$

若某個模式要求：

$$
I
\left(
\mathcal W,
\mathcal G_0
\right)
\ge
\tau,
$$

則 $\tau$ 就是該模式的最低身分門檻。

不同模式可以有不同門檻：

$$
\tau_{\mathrm{archive}}
>
\tau_{\mathrm{enhanced}}
>
\tau_{\mathrm{rebirth}}
>
\tau_{\mathrm{total\ conversion}}.
$$

未來遊戲不必為「它到底還是不是原作」尋找唯一答案，而可以公開聲明其身分政策。

---

# 十一、玩家語言將如何改變？

當世界線成為常規，玩家對遊戲的描述會逐漸改變。

今天常見的是：

> 我玩過某款遊戲。

> 我裝了哪些 MOD。

未來可能變成：

> 我玩的是原生世界線。

> 我用官方規則，但開啟了 AI 角色模式。

> 我的世界基於第二季，之後分支了三年。

> 我只接受驗證過的社群事件。

> 這個存檔已經偏離原作主線，但仍保留原生經濟與戰鬥規則。

遊玩身分可抽象為：

$$
\operatorname{Played}
\left(
\mathcal G
\right)
\longrightarrow
\operatorname{Played}
\left(
\mathcal G_0,
\mathcal W,
\Pi,
\Gamma
\right),
$$

其中：

- $\mathcal G_0$：基底版本；
- $\mathcal W$：實際世界線；
- $\Pi$：修改歷史；
- $\Gamma$：權限與治理設定。

未來「同一款遊戲」可能只是不同玩家世界線的共同祖先。

---

# 十二、不同遊戲類型的採用速度

## 12.1 較早採用

較可能優先採用的類型包括：

- 角色扮演；
- 人生與養成模擬；
- 沙盒；
- 經營；
- 城市建設；
- 生存；
- 策略；
- 文字冒險；
- 創作平台；
- 單人開放世界。

這些類型通常具有：

- 大量可替換內容；
- 長期存檔；
- 玩家個人敘事；
- NPC、事件與物品系統；
- 對重玩性與個人化的高需求。

## 12.2 中度採用

可能採取有限生成的類型包括：

- 動作角色扮演；
- 合作遊戲；
- 卡牌與桌遊；
- 關卡制動作遊戲；
- 模擬競速；
- 大型線上世界。

它們可能先開放外觀、任務、角色對話與私人伺服器規則，但保留核心戰鬥與公平性。

## 12.3 較慢採用

較慢採用的類型包括：

- 電競；
- 格鬥；
- 高精度節奏遊戲；
- 固定解答的益智遊戲；
- 嚴格作者式敘事；
- 高度依賴手工關卡節奏的作品。

這些類型仍可能使用 AI 輔助開發，但不一定把生成權交給玩家。

因此，本文的預測是**類型分化**，不是全產業同速轉換。

---

# 十三、商業模式的變化

當遊戲可以持續生成，發行後成本不再只是伺服器與客服，還可能包含：

- 模型推理；
- 資產生成；
- 世界儲存；
- 版本驗證；
- 內容審核；
- 分支託管；
- 存檔遷移；
- 作者與權利方分潤。

Steamworks 已把運行期 AI 服務的持續成本視為可由定價、微交易、訂閱或 DLC 處理的問題。[1] 這暗示未來遊戲可能販售不同層次的生成權限。

可能的產品結構包括：

| 商品 | 內容 |
|---|---|
| 原生買斷版 | 固定遊戲與基本更新 |
| 個人化權限 | 對話、外觀與局部事件生成 |
| 世界創作者權限 | 新角色、任務、規則包與分享 |
| 本地生成版 | 使用玩家本地模型與運算 |
| 託管世界 | 雲端保存、同步與多人分支 |
| 驗證服務 | 相容性、安全、競技與來源驗證 |
| 官方世界包 | 權利方策展的生成式擴展 |

然而，若每次遊玩都按 Token 收費，玩家可能產生強烈反感。因此真正可持續的產品，可能更偏向：

- 本地小模型處理高頻互動；
- 雲端高階模型處理低頻重大生成；
- 固定額度或包含式價格；
- 經過整理的世界包；
- 生成結果長期重用，而不是每次重新付費。

---

# 十四、治理將成為遊戲設計的一部分

當玩家與 AI 能修改世界，遊戲必須回答：

- 誰能改什麼？
- 誰批准修改？
- 哪些修改可以分享？
- 哪些內容只能私人使用？
- 哪些分支能進排行榜？
- 哪些模型可以存取玩家資料？
- 生成內容的權利屬於誰？
- 如何處理不合法或侵權生成？
- 如何回復被破壞的世界？
- 多人世界發生衝突時由誰治理？

因此，未來遊戲設計將包含一個新的核心層：

$$
\text{Game Design}
=
\text{Rules}
+
\text{Content}
+
\text{Permissions}
+
\text{Governance}.
$$

平台對運行期生成內容要求防護說明，[1] 以及 Workshop 對內容驗證、可覆寫範圍與策展模式的要求，[2] 都可視為此趨勢的早期形式。

---

# 十五、版權與合法性：技術常規化不等於權利自動化

AI 可以降低重建與修改成本，但不能自動創造法律權利。

世界線可能涉及：

- 基底遊戲著作權；
- 美術與音樂；
- 配音與表演；
- 商標；
- 翻譯；
- 模型訓練資料；
- 角色衍生內容；
- 玩家生成內容；
- 不同地區的發行權；
- 平台條款。

因此，未來「原生性向量」中的授權維度不可被省略。

技術上能生成，不代表可以公開發布；玩家私人分支、社群分享、商業販售與官方收錄，也可能需要不同權利。

本文預測，成熟平台將逐步要求世界線附帶機器可讀的來源與權限聲明，例如：

```yaml
base_title: "Example Game"
base_version: "2.1"
branch_type: "personal-ai"
official_assets: true
generated_assets: true
rule_changes: limited
public_distribution: allowed
commercial_use: prohibited
competitive_verification: false
```

這類聲明不會消滅法律爭議，但能使平台治理不再完全依賴人工猜測。

---

# 十六、情境時間表

以下時間不是精確發布預言，而是依現有技術與平台前兆提出的情境窗口。

## 16.1 第一階段：AI 成為常規開發與 MOD 助手（2026–2029）

特徵：

- 引擎內 AI 助手普及；
- 普通玩家可用自然語言生成腳本與資產；
- AI 協助修復 MOD 相容性；
- NPC 對話與局部任務生成增加；
- 平台的 AI 內容揭露與防護規則更完整；
- MOD 編輯器開始提供 AI 模式。

這一階段主要對應弱版本猜想。

## 16.2 第二階段：持久的個人生成分支（2028–2032）

特徵：

- 部分單人 RPG、模擬與沙盒遊戲允許遊玩中新增事件、角色與區域；
- AI 生成結果進入存檔，而不是一次性對話；
- 玩家可以保存、複製與分享分支；
- 官方開始區分原生、官方生成與私人生成模式；
- 個人世界具有可讀的修改摘要。

## 16.3 第三階段：規則級共生成與驗證世界線（2031–2036）

特徵：

- 部分遊戲允許受控修改職業、經濟、任務邏輯或局部戰鬥規則；
- 世界線具有版本身分、相容性檢查與回滾；
- 多人房間依世界線與規則相容性配對；
- 平台提供驗證原生與開放生成標章；
- 高品質社群世界形成正式經濟。

## 16.4 第四階段：跨作品的世界線平台（2035 年後，低信心）

特徵：

- 多種遊戲能共享部分角色、規則、資產或世界描述；
- 玩家擁有持續跨作品的創作者身分與世界庫；
- 經典遊戲可被授權接入新的世界線平台；
- 「遊戲引擎」與「遊戲產品」的界線進一步模糊。

這是本文信心最低的部分。它需要標準化、版權協議、長期狀態與安全治理同時成熟。

---

# 十七、可觀察指標與否證條件

一篇預測若永遠不可能被判錯，只是敘事，不是命題。

## 17.1 2030 指標：弱版本

截至 2030 年底，若至少同時出現以下三項，則弱版本獲得支持：

1. 主要商業引擎普遍提供能理解專案並修改物件或腳本的第一方 AI 工具；
2. 多個大型遊戲或創作平台允許非專業玩家以自然語言建立可玩的內容；
3. MOD 生態廣泛使用 AI 進行移植、修復、整合與測試。

若 AI 到 2030 年仍主要停留在概念美術、文案與獨立程式片段，無法可靠操作遊戲工程，弱版本需下調。

## 17.2 2032 指標：持久世界分支

截至 2032 年底，若至少三款具大型商業規模的作品，允許玩家在遊玩期間建立超越單次對話或純外觀的持久 AI 分支，則中等版本獲得支持。

「大型商業規模」可操作性定義為至少符合其中一項：

- 一百萬套以上公開銷售；
- 一百萬以上月活躍玩家；
- 大型訂閱或平台服務中的主力作品；
- 具全球發行與長期營運的主要 IP。

## 17.3 2035 指標：強版本

截至 2035 年底，若至少一個主要遊戲平台或大型作品生態同時具備：

- 世界分支身分；
- 機器可讀修改歷史；
- 原生／生成／驗證模式區分；
- 持久規則級修改；
- 回滾或存檔遷移；
- 社群分支分發或商業化；

則強版本猜想獲得實質支持。

## 17.4 強版本否證條件

若到 2035 年仍出現以下狀態，強版本應被視為未成立或至少延後：

- 運行期 AI 主要只生成台詞與外觀；
- 規則修改仍必須由專業開發者離線完成；
- 玩家普遍拒絕生成內容；
- 生成成本與延遲無法商業承受；
- 長期一致性與存檔遷移無法可靠處理；
- 平台因版權、安全或審核風險禁止持久生成分支；
- 沒有大型作品建立可分享的個人世界線。

---

# 十八、主要反對意見

## 18.1 「AI 內容品質太差，只會產生垃圾」

這是最有力的反對意見之一。

生成成本下降通常會先帶來內容爆量，而不是平均品質上升。低品質任務、角色失憶、風格破碎與規則衝突，可能使玩家重新偏好固定內容。

本文的回應是：世界線常規化不依賴所有生成內容都優秀，而依賴系統能否提供：

- 約束；
- 驗證；
- 策展；
- 版本；
- 回滾；
- 評價；
- 可信作者與社群。

若沒有這些機制，強版本確實可能失敗。

## 18.2 「玩家其實不想當設計師」

多數玩家不想操作複雜編輯器，這是正確的。

但本文預測的不是所有玩家都會建立整套遊戲，而是修改行為可能被包裝成普通選擇：

> 我希望這個 NPC 不要離開。

> 下一年加入一場旱災，但不要破壞主線。

> 我想讓這個職業可以轉為商人。

這更像向世界提出要求，而不是使用專業編輯器。

## 18.3 「這仍然只是開發者預先允許的選項」

任何安全系統都需要邊界。若遊戲只允許玩家從有限模板挑選，確實只是更靈活的內容系統。

強版本與普通選項的分界在於：玩家是否能提出原本沒有被逐項列出的意圖，而系統能否建立新的、持久且可驗證的結構。

## 18.4 「版權會阻止一切」

版權會阻止許多未經授權的公開商業化，但不一定阻止：

- 權利方自己的生成式產品；
- 有授權的經典遊戲重製；
- 私人本地修改；
- 原創世界；
- 公開提供 MOD 權限的作品；
- 以創作者平台條款治理的內容。

版權更可能決定哪些作品先進入此模式，而不是使整個模式不存在。

## 18.5 「玩家會失去共同文化」

若每個人的劇情都不同，社群確實可能失去共同討論基礎。

這正是本文預測原生模式與官方世界線不會消失的原因。未來社群可能同時具有：

- 共同原生主線；
- 官方季節世界；
- 策展分支；
- 個人世界。

共同文化會從「所有人看到完全相同內容」轉為「共享祖先版本與部分公共事件」。

---

# 十九、可進一步研究的問題

本文留下至少十二個公開研究問題：

1. 如何定量衡量世界線與原作的身分連續性？
2. 原生性向量的各維度應如何加權？
3. 玩家何時把 AI 生成內容視為自己的作品？
4. 生成分支如何維持長達數百小時的因果一致性？
5. 規則修改後，舊存檔如何遷移？
6. 多人世界由誰批准重大變更？
7. 如何區分世界內角色對話與世界外作者指令？
8. 如何驗證 AI 沒有偷偷改變競技數值？
9. 生成內容如何附帶來源、授權與模型資訊？
10. 原作者對世界變形保有何種控制？
11. 個人世界線是否可被繼承、轉讓或保存？
12. 當遊戲永遠能生成新內容時，玩家如何感受到完成與結束？

其中最後一題尤其重要。無限內容不等於無限價值；一款永不結束的遊戲，也可能因缺乏結構而失去意義。

---

# 二十、結論

本文提出的不是「AI 會讓所有人都能一鍵做遊戲」這種單純樂觀敘事，而是一個更具體、也更可被反駁的預測：

> **當 AI 取得受控的遊戲修改能力，MOD 將從發行後附加物，逐步成為遊戲內部的常規世界分支機制。**

此轉變將帶來三個同時發生的結果。

第一，玩家將獲得前所未有的個人化與共同創作能力。

第二，遊戲公司將從只提供完成內容，轉向同時提供穩定核心、修改權限、治理規則與世界託管。

第三，原生遊玩不會被淘汰，反而會因分支增多而成為更清楚、更珍貴的文化基準。

因此，未來「我玩過這款遊戲」可能不再是完整句子。

更完整的說法將是：

> **我玩的是哪一個原生基底，進入哪一條世界線，允許 AI 改變什麼，以及這個世界最後由誰共同完成。**

MOD 不會死亡。

它會失去作為例外的名字，然後成為遊戲的一種基本文法。

---

# 參考文獻

[1] Valve. **Steamworks Documentation: Content Survey**. Generative AI disclosure, including pre-generated and live-generated content, guardrails, and ongoing service-cost options. Accessed 2026-08-12.  
https://partner.steamgames.com/doc/gettingstarted/contentsurvey

[2] Valve. **Steamworks Documentation: Steam Workshop**. User-generated content integration, ready-to-use and curated workshops, validation, loading, updates, and monetization. Accessed 2026-08-12.  
https://partner.steamgames.com/doc/features/workshop

[3] Unity Technologies. **Unity’s AI Game Development Tools & RT3D Software**. In-project agentic assistance, scene and GameObject inspection, Editor actions, AI gateway, and MCP integration. Accessed 2026-08-12.  
https://unity.com/features/ai

[4] Roblox. **Assistant for Studio**. AI-assisted creation and modification of objects, scripts, assets, materials, meshes, and procedural models within Studio. Accessed 2026-08-12.  
https://create.roblox.com/docs/assistant/guide

[5] Epic Games. **Programming with Verse in Unreal Editor for Fortnite**. Creating custom game rules and behaviors with Verse. Accessed 2026-08-12.  
https://dev.epicgames.com/documentation/fortnite/learn-programming-with-verse-in-unreal-editor-for-fortnite

[6] Epic Games. **Engagement Payout in Fortnite Creative**. Creator participation and revenue allocation based on engagement. Accessed 2026-08-12.  
https://dev.epicgames.com/documentation/fortnite/engagement-payout-in-fortnite-creative

[7] Valevski, D., Leviathan, Y., Arar, M., & Fruchter, S. **Diffusion Models Are Real-Time Game Engines**. arXiv:2408.14837, 2024.  
https://arxiv.org/abs/2408.14837

[8] Google DeepMind. **Genie 3: A New Frontier for World Models**. Real-time navigable generated environments, promptable world events, capabilities, and limitations, 2025.  
https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/

[9] Park, J. S., O’Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. **Generative Agents: Interactive Simulacra of Human Behavior**. arXiv:2304.03442, 2023.  
https://arxiv.org/abs/2304.03442

---

## 建議引用格式

Neo.K.（2026）。〈從 MOD 到世界線：AI 共生成時代的遊戲原生性分化命題〉，v1.0-public。

```bibtex
@misc{neok2026mods_worldlines,
  author       = {Neo.K},
  title        = {從 MOD 到世界線：AI 共生成時代的遊戲原生性分化命題},
  year         = {2026},
  month        = {8},
  version      = {v1.0-public},
  note         = {公開命題猜想論文／技術與產業預測}
}
```

---

## 版本紀錄

### v1.0-public — 2026-08-12

- 首次公開版本；
- 提出遊戲世界線常規化猜想；
- 區分弱版本與強版本；
- 定義基底遊戲、修改操作、世界線與原生性向量；
- 提出十項次級猜想；
- 加入 2030、2032、2035 觀察指標與否證條件；
- 移除特定產品、企業、遊戲標的與實作架構。
