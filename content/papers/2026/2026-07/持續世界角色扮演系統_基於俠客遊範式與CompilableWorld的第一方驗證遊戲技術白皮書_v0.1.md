---
title: "持續世界角色扮演系統：基於《俠客遊》範式與 CompilableWorld 的第一方驗證遊戲技術白皮書"
subtitle: "Persistent-World Role-Playing System on CompilableWorld"
version: "v0.1"
date: "2026-07-13"
author: "許筌崴（Neo.K）"
organization: "EVEMISSLAB／一言諾科技有限公司"
status: "內部技術白皮書／概念與工程規格草案"
---

# 持續世界角色扮演系統  
## 基於《俠客遊》範式與 CompilableWorld 的第一方驗證遊戲技術白皮書

> 世界不因玩家登入而誕生，也不因玩家角色死亡而終止。  
> 玩家只是世界在某一段時間內所採用的一個可更換觀測點。

---

## 摘要

本文提出一套建立於 **CompilableWorld** 之上的持續世界角色扮演系統，暫稱為 **Persistent-World Role-Playing System，PWRPS**。其設計靈感來自《俠客遊／Lunatic Dawn》系列所展現的開放式人生、角色替換、世界延續、多層級空間與非固定主線思想，但並不以重製既有作品為目標。

本系統的定位不是新的通用世界引擎，也不是將所有遊戲機制重新塞入 CompilableWorld Core。其正確分層為：

$$
\text{CompilableWorld Core}
\rightarrow
\text{Living World Runtime}
\rightarrow
\text{Reference Game}
\rightarrow
\text{World Packages / Mods}
$$

其中：

- **CompilableWorld Core** 負責世界中間表示、規則、狀態、事件、驗證、編譯、版本與執行追蹤；
- **Living World Runtime** 負責持續世界 RPG 所需的時間、NPC 行動、家庭、組織、委託、經濟、旅行、死亡與繼承；
- **Reference Game** 是一款真正可遊玩的第一方驗證遊戲；
- **World Packages** 則承載不同題材與世界觀。

本文明確排除以《命運之欲》作為第一個驗證遊戲。《命運之欲》具有龐大的既有歷史、城市、種族、神學、魔法與力量體系，若過早投入，將使世界內容需求反向綁定引擎結構。第一個驗證世界應採用規模小、規則清楚、低設定負擔且容易長期模擬的中性世界包，用來驗證世界是否能在沒有固定主線、沒有天命主角、沒有即時大型語言模型介入的情況下持續運作。

本文的核心命題為：

$$
\boxed{
\text{World Lifetime}
>
\text{Character Lifetime}
>
\text{Quest Lifetime}
}
$$

任務不是世界存在的理由，玩家角色也不是世界運作的中心。世界先存在，角色只是暫時進入其中。

---

# 一、問題背景

## 1.1 傳統角色扮演遊戲的中心化問題

大多數角色扮演遊戲都隱含一個相同的本體假設：

$$
\text{World}
\approx
\text{Content Prepared for the Player}
$$

城市等待玩家抵達，NPC 等待玩家交談，任務等待玩家觸發，戰爭等待玩家參與。即使畫面上存在龐大的地圖，世界真正運作的部分仍然只圍繞玩家附近的腳本。

此類結構帶來三個限制：

1. **世界缺乏自主時間**：玩家不行動，世界便停滯。
2. **NPC 缺乏自身目的**：NPC 主要是任務、交易或敘事接口。
3. **選擇缺乏持久後果**：事件多半只改變局部旗標，不形成跨層級傳播。

開放世界因此常被誤解為「玩家可以前往很多地方」，而不是：

> 玩家可以在一個自行運轉的世界中造成不可忽略的持久改變。

## 1.2 《俠客遊》範式的歷史價值

《俠客遊》系列的重要性不只在自由度，而在於它曾經接近一個不同的遊戲本體論：

- 世界具有自己的時間；
- 玩家不是唯一行動者；
- 人物可以生活、旅行、結盟、死亡與繁衍；
- 玩家角色生命週期可以短於世界生命週期；
- 任務只是暫時出現的世界結構；
- 宏觀地圖、城市、地點、人物與戰鬥是不同精度的世界投影。

早期作品受限於硬體、資料量與硬編碼，無法充分展開此範式。今日的狀態機、事件溯源、圖資料、可編譯世界表示、Agent 政策與受治理的生成式 AI，使這條路有機會被重新推進。

## 1.3 三個月前構想與當前 CompilableWorld 的關係

早期的「通用世界模擬器」構想已經提出：

- 宏觀、中觀、微觀多層級空間；
- 規則—敘事雙向耦合；
- AI 內容生成受規則約束；
- 因果鏈持久化與跨層級傳播；
- NPC 目標與記憶；
- 世界觀一致性層；
- 世界編輯器與 MOD 生態；
- 低延遲、多視窗、零層級資訊界面。

但當時的世界仍主要存在於遊戲引擎內：

$$
\text{World}
\subset
\text{Game Engine}
$$

當前 CompilableWorld 將關係反轉：

$$
\text{World Definition}
\rightarrow
\text{Validated World IR}
\rightarrow
\text{Runtime Targets}
$$

世界首先以可驗證、可版本化、可編譯的結構存在，遊戲 Runtime 只是其中一種執行形式。

因此，本文不再將現代《俠客遊》式遊戲描述為「通用世界引擎本身」，而將其定位為：

> CompilableWorld 上的第一個持續世界 Runtime 類型與第一方旗艦應用。

---

# 二、產品與技術定位

## 2.1 四層產品結構

### 第一層：CompilableWorld Core

負責與題材無關的世界工程能力：

- World IR；
- Entity Registry；
- State Store；
- Action IR；
- Event IR；
- Transition Rules；
- Function Registry；
- Scheduler；
- Event Bus；
- Snapshot；
- Event Log；
- Schema Validation；
- Semantic Validation；
- Scenario Tests；
- Runtime Trace；
- Version、Migration 與 Diff；
- Agent Patch Governance。

### 第二層：Living World Runtime

負責持續世界角色扮演遊戲的共通機制：

- 世界時間與時鐘；
- NPC 日程與行為政策；
- 人際、家庭、血緣與繼承；
- 勢力、職位與組織；
- 城市、聚落與交通；
- 經濟、生產、消費與物流；
- 委託、契約、傳聞與情報；
- 犯罪、法律、聲望與追捕；
- 戰鬥、傷勢、死亡與替換角色；
- 世界精度分層與懶展開；
- 玩家角色生命週期與世界生命週期分離。

### 第三層：Reference Game

一款內容規模刻意受限、但世界閉環完整的遊戲，用來證明：

$$
\text{Persistent World}
+
\text{Autonomous Agents}
+
\text{Replaceable Player Character}
+
\text{Causal Continuity}
$$

能否形成真正有趣的遊戲體驗。

### 第四層：World Packages

題材、設定與內容透過世界包掛載，例如：

- 低奇幻邊境；
- 武俠江湖；
- 商業都市；
- 王朝末世；
- 太空殖民地；
- 修仙宗門；
- 《命運之欲》。

《命運之欲》屬於未來的大型旗艦世界包，而非第一驗證包。

---

## 2.2 系統不是什麼

本計畫第一階段**不做**：

- 無縫大型 3D 開放世界；
- 依賴大型語言模型才能運作的 NPC；
- 每個居民逐秒全精度模擬；
- 固定救世主主線；
- MMORPG；
- 全題材一次完成；
- 完整自然語言任意行動；
- 《命運之欲》全世界觀實裝；
- 先做數百種技能與複雜戰鬥公式；
- 讓 AI 直接改寫核心狀態；
- 將世界規則藏在不可檢查的模型黑箱中。

第一階段追求的是小世界的完整生命，而不是大世界的表面規模。

---

# 三、核心設計公理

## 公理一：世界不依附玩家

令世界狀態為 $W_t$ ，所有世界 Agent 的行動集合為 $A_t$ ，外部事件為 $E_t$ ，則：

$$
W_{t+1}
=
F(W_t,A_t,E_t)
$$

即使玩家沒有輸入， $A_t$ 仍包含 NPC、家庭、商隊、組織與自然事件的行動，因此：

$$
A_t \neq \varnothing
$$

世界必須能在玩家離線、休息、監禁、死亡或切換角色時繼續推進。

## 公理二：玩家控制的是觀測點，不是世界中心

玩家在時間 $t$ 控制角色 $C_i$ ：

$$
P_t=(W_t,C_i)
$$

當角色死亡、退休、失去自由或玩家主動切換時：

$$
(W_t,C_i)
\rightarrow
(W_{t+\Delta},C_j)
$$

其中 $C_j$ 可以是：

- 子女；
- 弟子；
- 隊友；
- 家族成員；
- 僱員；
- 盟友；
- 仇敵；
- 世界中符合接管條件的其他人物。

## 公理三：任務是世界中的暫時契約

傳統任務常是預先寫好的線性內容。本系統將任務重構為：

$$
Q=
(\text{Issuer},\text{Goal},\text{Constraints},
\text{Deadline},\text{Reward},\text{Consequences})
$$

任務由世界需求產生，例如：

- 商隊需要護衛；
- 家族需要尋人；
- 城市需要糧食；
- 組織需要情報；
- 法院需要逮捕嫌犯；
- 個人需要復仇。

任務即使無人承接，也可能：

- 由 NPC 接取；
- 自然失敗；
- 被其他事件取代；
- 惡化為更大的危機；
- 失去原本的委託人。

## 公理四：規則決定事實，AI 只生成提案與表達

任何世界事實都必須經過：

$$
\text{Proposal}
\rightarrow
\text{Validation}
\rightarrow
\text{Transition}
\rightarrow
\text{Commit}
$$

AI 可以提出：

- 對話措辭；
- 人物外貌；
- 地方傳聞；
- 任務描述；
- 記憶摘要；
- 行動候選；
- 小型背景故事。

AI 不得直接決定：

- 某人已死亡；
- 某物已轉移；
- 某組織已滅亡；
- 某場戰爭已勝利；
- 某角色已擁有能力；
- 某人已知曉秘密。

世界真值只能由規則與狀態轉移提交。

## 公理五：有限規則優先於無限生成

$$
\text{有限規則}
\times
\text{有限範本}
\times
\text{狀態組合}
\times
\text{AI 細節投影}
\Rightarrow
\text{高多樣性體驗}
$$

AI 生成不是自由度的來源，只是表達層的增幅器。真正的自由度來自規則能否處理玩家與 NPC 的合理行為。

## 公理六：所有重要後果必須可追蹤

若玩家行為 $a$ 導致世界狀態 $s_n$ ，系統必須保留因果路徑：

$$
a
\rightarrow
s_1
\rightarrow
s_2
\rightarrow
\cdots
\rightarrow
s_n
$$

例如：

```text
玩家殺死商人
→ 商隊失去負責人
→ 城市補給量下降
→ 糧價上升
→ 底層居民不滿
→ 犯罪率上升
→ 城主增加巡邏
→ 鄰近勢力判斷城市衰弱
```

每一步都應能在 Runtime Trace 或 Studio 因果圖中查看。

---

# 四、世界模型

## 4.1 持續世界狀態

Living World Runtime 的世界狀態定義為：

$$
W_t=
(
\mathcal{E},
\mathcal{S},
\mathcal{R},
\mathcal{A},
\mathcal{O},
\mathcal{H},
\mathcal{L},
\mathcal{C},
\mathcal{K},
\mathcal{M},
\mathcal{V},
\mathcal{T}
)_t
$$

其中：

- $\mathcal{E}$ ：實體集合；
- $\mathcal{S}$ ：實體狀態；
- $\mathcal{R}$ ：關係圖；
- $\mathcal{A}$ ：Agent 政策與目標；
- $\mathcal{O}$ ：組織與職位；
- $\mathcal{H}$ ：家庭、血緣與繼承；
- $\mathcal{L}$ ：地點、聚落與交通網；
- $\mathcal{C}$ ：契約、任務與承諾；
- $\mathcal{K}$ ：知識、情報與傳聞；
- $\mathcal{M}$ ：記憶；
- $\mathcal{V}$ ：事件佇列；
- $\mathcal{T}$ ：世界時間與歷史。

## 4.2 核心實體類型

第一版至少支援：

| 類型 | 說明 |
|---|---|
| Person | 可行動、可記憶、可死亡與被接管的人物 |
| Household | 家庭、共同財產、撫養與繼承單位 |
| Organization | 幫派、商會、軍隊、政府、宗派 |
| Role | 組織內的職位、權限與責任 |
| Settlement | 村莊、城鎮、城市 |
| Location | 建築、道路、房間、野外節點 |
| Route | 地點間旅行、成本、風險與物流 |
| Item | 可擁有、交易、消耗或損壞的物件 |
| Resource | 糧食、貨幣、材料、勞動力等可聚合資源 |
| Contract | 委託、雇傭、債務、婚約、通緝或交易約定 |
| Event | 已發生或排程中的世界事件 |
| Rumor | 可傳播、失真、被相信或被否定的資訊 |
| Memory | 特定 Agent 對事件與人物的記錄 |
| Law | 某管轄區中的禁止、允許與懲罰規則 |
| Lineage | 血緣、師承、繼承與身份延續 |

## 4.3 穩定 ID 與身份連續性

所有持續實體使用穩定 ID：

```yaml
person_id: person_000184
household_id: household_000031
organization_id: org_merchant_guild
settlement_id: settlement_rivergate
```

名稱可以改變，身份 ID 不變。這是處理：

- 改名；
- 婚姻；
- 身份偽裝；
- 組織改制；
- 城市易主；
- 後代繼承；
- 跨 Runtime 編譯；
- 存檔 Migration

的必要條件。

---

# 五、時間、精度與世界調度

## 5.1 多時間尺度

不同機制不應使用同一更新頻率。

| 尺度 | 典型更新 |
|---|---|
| 即時／戰術 | 移動、攻擊、對話選擇 |
| 分鐘／小時 | 日程、旅行、店鋪、巡邏 |
| 日 | 消費、生產、委託、疾病、關係變化 |
| 週 | 商隊、組織決策、人口遷移 |
| 月 | 經濟趨勢、政治變化、懷孕與訓練 |
| 年 | 年齡、繼承、世代、長期戰爭與制度變化 |

世界調度器不逐秒模擬所有人，而是以事件與下一次行動時間驅動：

$$
t_{\text{next}}
=
\min_i
\left(
t_i^{\text{scheduled}}
\right)
$$

系統跳轉到下一個有意義事件，而不是浪費計算於空白時間。

## 5.2 四級模擬精度

### L0：統計態

適用於遠距離、非重要地區與大量人口：

- 人口總量；
- 經濟指數；
- 治安；
- 物資庫存；
- 組織力量。

### L1：群體態

以家庭、商隊、部隊、工坊等群體為單位：

- 群體位置；
- 群體資源；
- 群體目的；
- 群體風險。

### L2：人物簡化態

有穩定身份，但只維持：

- 年齡；
- 職業；
- 所屬；
- 關係摘要；
- 當前目標；
- 健康；
- 重要記憶索引。

### L3：人物完整態

只有核心人物、玩家附近人物與重要事件參與者使用：

- 完整記憶；
- 多目標權重；
- 情緒；
- 對話風格；
- 詳細裝備；
- 行為候選；
- 個人歷史。

精度轉換為：

$$
L_k
\xrightarrow{\text{focus / importance}}
L_{k+1}
$$

以及：

$$
L_{k+1}
\xrightarrow{\text{summarize / unload}}
L_k
$$

當人物離開玩家關注範圍時，完整歷史會摘要後降階，而不是刪除身份。

---

# 六、NPC Agent 系統

## 6.1 Agent 決策函數

NPC $i$ 在時間 $t$ 的行動選擇為：

$$
a_i^*(t)
=
\arg\max_{a\in\mathcal{A}_i}
U_i
\left(
a\mid
s_i(t),
g_i(t),
m_i(t),
r_i(t),
k_i(t),
W_t
\right)
$$

其中：

- $s_i$ ：個人狀態；
- $g_i$ ：目標；
- $m_i$ ：記憶；
- $r_i$ ：人際與組織關係；
- $k_i$ ：已知資訊；
- $W_t$ ：可觀察世界狀態。

## 6.2 目標不是單一行為樹

每個 NPC 至少具有：

- 生存；
- 安全；
- 財富；
- 社會地位；
- 家庭；
- 忠誠；
- 信念；
- 復仇；
- 探索；
- 享樂；
- 長期計畫。

目標權重會隨事件改變：

$$
w_{i,g}(t+1)
=
w_{i,g}(t)
+
\Delta w_{i,g}(e_t)
$$

一名原本重視財富的商人，在子女遭綁架後，家庭目標權重可暫時高於財富。

## 6.3 行動候選由規則生成

系統不要求 AI 自由想像每個行動。候選行動由模組提供：

```text
travel
work
rest
buy
sell
eat
train
socialize
investigate
accept_contract
refuse_contract
attack
flee
report
marry
separate
recruit
resign
inherit
```

AI 最多負責：

- 對候選行動進行語義補充；
- 生成自然語言理由；
- 在多個規則允許的候選間提出排序建議。

最終動作仍必須通過 Action IR 驗證。

---

# 七、家庭、世代與角色替換

## 7.1 家庭是持續世界的核心單位

單一人物死亡後，世界連續性常由家庭與組織保存。家庭系統負責：

- 共同居所；
- 共同財產；
- 親屬義務；
- 撫養；
- 婚姻；
- 收養；
- 血緣；
- 姓名與身份；
- 繼承；
- 家族聲望；
- 債務。

## 7.2 繼承函數

人物 $C_i$ 死亡後，財產與權利分配為：

$$
I(C_i)
=
f(
\text{law},
\text{will},
\text{kinship},
\text{organization},
\text{debt},
\text{possession}
)
$$

繼承不只包含物品，也可包含：

- 商號；
- 土地；
- 職位；
- 仇恨；
- 債務；
- 秘密；
- 盟約；
- 通緝；
- 名聲。

## 7.3 玩家角色接管規則

玩家角色死亡後，不應只顯示「讀取存檔」。系統提供世界內接管：

```text
角色死亡
→ 執行遺產與事件結算
→ 推進必要時間
→ 產生可接管人物清單
→ 顯示人物與死者的關係
→ 玩家選擇新觀測點
→ 世界繼續
```

接管資格由世界規則定義，例如：

$$
\text{eligible}(C_j)
=
\text{alive}
\land
\text{reachable}
\land
\text{player\_policy\_allows}
$$

第一版可限制為：

- 子女；
- 配偶；
- 弟子；
- 隊友；
- 同家庭成員。

後續才開放任意 NPC 接管。

---

# 八、組織、城市與權力

## 8.1 組織不是固定陣營標籤

組織由以下元素構成：

$$
O=
(
\text{members},
\text{roles},
\text{resources},
\text{rules},
\text{goals},
\text{territory},
\text{relations}
)
$$

組織可以：

- 招募與驅逐；
- 任命與罷免；
- 分裂與合併；
- 宣戰與議和；
- 破產；
- 改名；
- 改變制度；
- 被玩家或 NPC 掌控。

## 8.2 權力來自可執行能力

角色的權力不是抽象數值，而是：

$$
\text{Power}
=
f(
\text{authority},
\text{resources},
\text{followers},
\text{information},
\text{coercion},
\text{legitimacy}
)
$$

一名城市官員可能具有法律權威但缺乏武力；一名幫派首領可能缺乏合法性但控制街道；一名商人可能沒有職位卻能控制糧食。

## 8.3 城市是多系統耦合節點

每個聚落至少維持：

- 人口；
- 糧食；
- 財富；
- 生產；
- 庫存；
- 治安；
- 稅收；
- 法律；
- 組織控制；
- 道路連接；
- 事件壓力。

城市狀態不是裝飾資料，而會影響：

- 價格；
- 犯罪；
- 移民；
- 任務；
- NPC 情緒；
- 組織策略；
- 戰爭結果。

---

# 九、委託、事件與非主線敘事

## 9.1 事件先於任務

世界先產生問題：

```text
商隊失蹤
城市糧食不足
某人失蹤
組織需要情報
道路出現盜匪
繼承權發生爭議
```

然後不同角色對問題形成需求，需求才可能轉化為委託。

$$
\text{World Pressure}
\rightarrow
\text{Agent Need}
\rightarrow
\text{Contract Proposal}
$$

## 9.2 NPC 也能接取委託

任務不為玩家保留。若玩家拒絕：

- NPC 冒險者可能承接；
- 委託人可能提高報酬；
- 問題可能惡化；
- 委託人可能死亡；
- 組織可能改用暴力；
- 任務可能永久消失。

## 9.3 沒有唯一主線，但有世界主題

「沒有固定主線」不等於沒有敘事方向。世界可以存在：

- 長期政治危機；
- 經濟衰退；
- 王位繼承；
- 疫病；
- 邊境衝突；
- 宗教改革；
- 技術擴散。

這些是世界進程，不是要求玩家參與的主線。

玩家可能：

- 改變事件；
- 利用事件；
- 逃離事件；
- 完全忽略事件；
- 成為事件的受害者；
- 由後代面對事件結果。

---

# 十、情報、記憶與傳聞

## 10.1 世界真值與角色知識分離

世界中真實發生的事件集合為 $\mathcal{F}$ ，角色 $i$ 所知為 $\mathcal{K}_i$ ：

$$
\mathcal{K}_i
\subseteq
\mathcal{F}
\cup
\mathcal{R}
$$

其中 $\mathcal{R}$ 為傳聞、誤解與謊言。

NPC 不應自動知道全世界事件。知識來源包括：

- 親眼觀察；
- 對話；
- 公告；
- 組織情報；
- 信件；
- 商旅傳播；
- 謠言；
- 推理。

## 10.2 傳聞是一等實體

每條傳聞至少具有：

```yaml
rumor_id: rumor_00042
claim: "北方道路已被盜匪封鎖"
source: person_000184
origin_event: event_001921
confidence: 0.62
distortion: 0.18
known_by:
  - person_000184
  - person_000201
```

傳播後可發生：

$$
r_{n+1}
=
\text{transform}(r_n,\text{speaker},\text{listener},\text{bias})
$$

因此，玩家的名聲不是全域數字瞬間更新，而是透過證人、組織、公告與傳聞逐漸傳播。

## 10.3 記憶分層

記憶分為：

- 事件記憶；
- 關係記憶；
- 承諾記憶；
- 創傷記憶；
- 技能記憶；
- 摘要記憶。

重要性函數可寫為：

$$
\operatorname{importance}(m)
=
\alpha I_{\text{emotion}}
+
\beta I_{\text{goal}}
+
\gamma I_{\text{relationship}}
+
\delta I_{\text{recency}}
$$

低重要性記憶可被壓縮成摘要，但影響不能任意消失。

---

# 十一、戰鬥與傷勢的最小設計

## 11.1 戰鬥不是第一核心

第一個驗證遊戲不應以大量技能和平衡為中心。戰鬥只需驗證：

- 行動；
- 距離；
- 命中；
- 傷害；
- 傷勢；
- 逃跑；
- 俘虜；
- 死亡；
- 目擊與法律後果。

## 11.2 最小判定

第一版可使用：

$$
P(\text{hit})
=
\sigma
\left(
A_{\text{skill}}
-
D_{\text{skill}}
+
T_{\text{position}}
+
R
\right)
$$

傷害為：

$$
D
=
\max
\left(
0,
W_{\text{power}}
+
A_{\text{strength}}
-
D_{\text{armor}}
+
\varepsilon
\right)
$$

其中 $\sigma$ 為壓縮至 $[0,1]$ 的函數， $R$ 與 $\varepsilon$ 為受控隨機量。

## 11.3 傷勢優先於血條歸零

人物狀態包括：

- 疲勞；
- 出血；
- 骨折；
- 疼痛；
- 感染；
- 昏迷；
- 永久傷殘。

戰鬥後果可以是：

- 投降；
- 被捕；
- 失去裝備；
- 欠下贖金；
- 形成仇恨；
- 失去工作能力；
- 最終死亡。

這比「每次戰鬥不是勝利就是讀檔」更符合持續世界。

---

# 十二、AI 整合邊界

## 12.1 AI 的四個位置

### A. 離線世界改編 Agent

將自然語言設定整理為：

- World Seed；
- Entity Templates；
- Rule Modules；
- Scenario Tests；
- 知識與文化約束。

### B. Studio 工程 Agent

產生 World IR Patch，必須經過：

```text
Patch
→ Schema Validation
→ Semantic Validation
→ Scenario Tests
→ Visual Diff
→ Human Review
→ Commit
```

### C. Runtime 表達 Agent

生成：

- 對話；
- 描述；
- 傳聞措辭；
- 信件；
- 日誌；
- 記憶摘要。

### D. Runtime 行動建議 Agent

在規則產生的候選行動中協助排序，但不能建立規則之外的狀態變化。

## 12.2 不允許 AI 在主迴圈阻塞

玩家互動延遲預算：

| 時間 | 必須出現的回饋 |
|---|---|
| $0$ – $100\text{ms}$ | 點擊、選取、動畫或介面外殼 |
| $100$ – $300\text{ms}$ | 規則結果與基礎對話 |
| $300$ – $1000\text{ms}$ | 個性化表達增強 |
| $>1000\text{ms}$ | 僅允許非阻塞背景內容 |

因此：

$$
\text{Game Loop}
\not\rightarrow
\text{Blocking LLM Call}
$$

AI 超時時，系統必須可降級到：

1. 已快取內容；
2. 範本內容；
3. 純規則描述。

## 12.3 AI 輸出必須結構化

```json
{
  "proposal_type": "dialogue",
  "speaker_id": "person_000184",
  "intent": "refuse_contract",
  "emotion": "cautious",
  "text": "這條路最近不太平。這點錢，不值得我拿命去換。",
  "world_mutations": []
}
```

若 AI 提出世界修改：

```json
{
  "proposal_type": "action",
  "actor_id": "person_000184",
  "action_id": "report_suspicious_player",
  "parameters": {
    "target_id": "player_000001",
    "organization_id": "org_city_watch"
  }
}
```

則必須由 Action IR 驗證後才可執行。

---

# 十三、玩家介面與認知流

## 13.1 多層級世界投影

遊戲介面保留《俠客遊》式快速切換：

$$
\text{Macro}
\leftrightarrow
\text{Meso}
\leftrightarrow
\text{Micro}
\leftrightarrow
\text{Tactical}
$$

- **宏觀層**：區域、道路、勢力、旅行；
- **中觀層**：城市、建築、組織與功能；
- **微觀層**：人物、對話、交易與局部行動；
- **戰術層**：戰鬥、追逐、潛入與危機。

這些不是四個不同世界，而是同一 World IR 的不同投影。

## 13.2 關鍵資訊零層級可達

永久顯示或一鍵可見：

- 時間；
- 地點；
- 健康；
- 疲勞；
- 金錢；
- 當前身份；
- 重要關係；
- 近期事件；
- 可立即執行的行動。

玩家不應為查看一個關鍵數字進入多層選單。

## 13.3 介面不展示全部模擬

世界可以複雜，但玩家介面應只呈現：

- 當前可感知；
- 當前可行動；
- 當前重要；
- 可追溯的原因。

複雜性應存在於世界，而不是全部堆在玩家螢幕上。

---

# 十四、第一個驗證遊戲

## 14.1 明確排除《命運之欲》

《命運之欲》不作為第一驗證遊戲，原因如下：

1. 已有大量世界史與勢力設定；
2. 城市制度具有強烈個性；
3. 存在多套力量與神學系統；
4. 內容規模會使工程驗證與世界創作混在一起；
5. 引擎容易被三十八符號魔法、結界城市與高階力量反向特化；
6. 任何失敗都難以判斷是 Runtime 問題、內容問題或設定整合問題。

《命運之欲》應在 Living World Runtime 穩定後，作為大型旗艦世界包進行適配。

## 14.2 中性參考世界包

第一個世界包暫稱：

> **Reference World Alpha／參考世界 Alpha**

它不是正式商業名稱，只是工程測試代號。

建議題材：

- 低奇幻或無魔法；
- 王國邊境的一個小區域；
- 三座聚落；
- 四個組織；
- 有道路、商業、治安與局部政治；
- 沒有救世預言；
- 沒有世界毀滅倒數；
- 沒有複雜職業樹；
- 沒有必須完成的主線。

## 14.3 初始規模

| 元素 | MVP 數量 |
|---|---:|
| 區域 | 1 |
| 聚落 | 3 |
| 野外地點 | 8–12 |
| 道路 | 6–10 |
| 組織 | 4 |
| 核心持續 NPC | 30–40 |
| 簡化持續 NPC | 100–150 |
| 家庭 | 20–30 |
| 商隊／工作群體 | 8–12 |
| 商品類型 | 15–20 |
| 基礎行動 | 20–30 |
| 契約類型 | 8–12 |
| 法律規則 | 10–15 |
| 戰鬥技能 | 4–6 |
| 世界模擬期限 | 至少 20 遊戲年 |

## 14.4 三個主要組織範例

可使用低設定負擔結構：

1. **地方行政機構**：負責稅收、法律與巡邏；
2. **商旅聯盟**：負責物流、價格與護衛；
3. **地方家族聯盟**：掌握土地、婚姻與地方權力；
4. **非正式邊境團體**：獵人、傭兵、走私者或盜匪。

重點不是設定新奇，而是它們能形成可觀察的權力、經濟與資訊流。

## 14.5 初始玩家身份

玩家不應以英雄開始，可選：

- 商隊學徒；
- 城鎮守衛；
- 小農家庭成員；
- 流浪傭兵；
- 工坊學徒；
- 無業旅人。

每個身份提供不同：

- 社會關係；
- 起始財產；
- 法律地位；
- 可見資訊；
- 可接觸組織；
- 生存壓力。

---

# 十五、MVP 驗收標準

## 15.1 世界連續性

- 玩家不操作時，世界能自行運作至少十個遊戲年；
- NPC 會出生、成長、工作、移動、結盟、衝突與死亡；
- 組織職位會因死亡或罷免而補位；
- 商隊與商品供應會影響價格；
- 任務不由玩家承接時仍有結果。

## 15.2 角色可替換性

- 玩家角色可以死亡；
- 死亡不要求讀取舊存檔；
- 系統能結算遺產、關係與事件；
- 玩家能接管至少三類關聯角色；
- 新角色繼續生活於同一世界歷史。

## 15.3 因果可追蹤性

- 任一重大事件可產生完整 Event Trace；
- Trace 能指出觸發條件、狀態修改與後續排程；
- Studio 可顯示跨人物、家庭、城市與組織的因果鏈。

## 15.4 AI 非必要性

- 關閉所有雲端 AI 後，遊戲仍能完整運作；
- 至少 $80\%$ 的 NPC 日常決策不依賴 LLM；
- AI 超時不阻塞玩家操作；
- 所有 AI 提議均可被記錄、拒絕與重播。

## 15.5 Runtime 一致性

- 相同 World IR 與隨機種子能重播相同結果；
- Snapshot 可恢復；
- Event Log 可驗證；
- ScenarioIR 在參考 Runtime 中通過；
- 世界包能被重新編譯而不破壞穩定 ID。

## 15.6 遊戲性

- 玩家能在沒有主線指示的情況下找到至少三類可持續活動；
- 玩家行為能在一小時內形成可見的中期後果；
- 玩家角色死亡後，仍願意繼續接管新角色；
- 世界事件不只出現在文字紀錄，而會改變價格、人物、地點或權力關係。

---

# 十六、工程架構

## 16.1 編譯流程

```text
World Seed
→ JSON / CSV / EML Authoring
→ Normalize
→ Schema Validation
→ Semantic Validation
→ Living World IR
→ Scenario Tests
→ Compile
→ Living World Runtime
→ Event Log / Trace / Snapshot
→ Studio Observatory
```

## 16.2 Living World IR 模組

建議拆分：

```text
core.identity
core.time
core.location
core.state
core.event
living.person
living.household
living.lineage
living.organization
living.contract
living.economy
living.knowledge
living.memory
living.law
living.travel
living.combat
living.player_control
presentation.dialogue
presentation.ui
```

## 16.3 最小人物定義

```yaml
id: person_000184
type: person
identity:
  name: 林安
  age: 23
  household_id: household_000031
state:
  health: 0.88
  fatigue: 0.21
  wealth: 42
  location_id: location_rivergate_market
roles:
  - organization_id: org_merchant_guild
    role_id: apprentice
goals:
  survival: 0.8
  wealth: 0.7
  family: 0.6
  status: 0.3
knowledge:
  known_rumors:
    - rumor_00042
relationships:
  person_000201:
    trust: 0.55
    affection: 0.20
    fear: 0.00
policy_id: policy_merchant_apprentice
```

## 16.4 最小事件定義

```yaml
id: event_001921
type: caravan_delayed
time: "year_3.month_4.day_12.hour_16"
actor_ids:
  - caravan_00008
location_id: route_north_pass
preconditions:
  - route_north_pass.blocked == true
effects:
  - settlement_rivergate.food_stock -= 40
  - contract_food_delivery.status = delayed
  - schedule(event_price_recalculation, after=1_day)
emits:
  - rumor_caravan_missing
trace_tags:
  - economy
  - travel
  - settlement
```

## 16.5 行動驗證

```text
Action Proposal
→ Actor Exists?
→ Actor Alive?
→ Actor Has Capacity?
→ Target Exists?
→ Location Reachable?
→ Resources Sufficient?
→ Law and Permission Check
→ Conflict Resolution
→ State Transition
→ Event Emission
→ Log Commit
```

---

# 十七、開發階段

## Phase 0：規格凍結與 ScenarioIR

交付：

- Living World IR 最小 Schema；
- Person、Household、Organization、Settlement、Contract；
- 時間與 Scheduler；
- 五個標準 Scenario；
- 確定性重播規格；
- AI 權限邊界。

驗收：

- 純資料即可表示第一個小型世界；
- 不需要遊戲畫面即可在測試中推進三十天。

## Phase 1：無玩家世界模擬

交付：

- NPC 工作、休息、消費、旅行；
- 家庭財產；
- 組織職位；
- 商隊與基礎價格；
- 事件記錄與 Snapshot。

驗收：

- 世界可自行運行十年；
- 不出現大量無效狀態；
- 重要人口與資源指標可解釋。

## Phase 2：玩家觀測與行動

交付：

- 宏觀、中觀、微觀介面；
- 玩家控制人物；
- 對話、交易、工作、旅行；
- 基本犯罪與法律；
- Event Trace。

驗收：

- 玩家能在世界中生活，不依賴主線。

## Phase 3：傷勢、死亡與繼承

交付：

- 戰鬥；
- 傷勢；
- 俘虜；
- 死亡；
- 遺產；
- 角色接管；
- 世界時間延續。

驗收：

- 玩家死亡後可在同一世界繼續至少兩代。

## Phase 4：情報、傳聞與受控 AI

交付：

- 角色知識隔離；
- 傳聞傳播；
- 記憶摘要；
- AI 對話投影；
- 快取、降級與超時；
- Proposal Validation。

驗收：

- AI 關閉時仍可玩；
- AI 開啟時只提升表達，不改變規則正確性。

## Phase 5：Studio 視圖與世界包

交付：

- 人物表格；
- 家庭圖；
- 組織圖；
- 城市狀態；
- 事件時間線；
- 因果 Trace；
- World Package 匯入與匯出。

驗收：

- 非核心程式修改即可建立第二個小型世界包。

---

# 十八、主要技術風險

## 18.1 狀態空間爆炸

風險：

- 每個 NPC、家庭、物品與事件持續累積；
- 關係圖可能呈平方成長；
- 記憶無限增加。

策略：

- 多精度模擬；
- 稀疏關係；
- 事件摘要；
- 冷資料歸檔；
- 只保存有因果價值的狀態；
- 週期性 Snapshot；
- 可重建資料不重複保存。

## 18.2 世界雖能運作但不好玩

風險：

- 模擬正確不等於具有遊戲性；
- 玩家可能找不到目標；
- 事件後果過慢或不明顯。

策略：

- 提供「機會面板」而不是主線；
- 呈現附近需求、傳聞、風險與關係；
- 將中期後果投影為可見變化；
- 允許玩家自訂長期目標；
- 以世界回饋代替任務箭頭。

## 18.3 NPC 看似自主但行為單調

策略：

- 多目標權重；
- 角色身份與資源限制；
- 關係與記憶改變決策；
- 組織政策影響個人；
- 允許少量非最優行為；
- 對重要人物使用更高精度政策。

## 18.4 AI 表達破壞一致性

策略：

- AI 不直接寫狀態；
- 嚴格輸出 Schema；
- 提示詞只讀角色可知資訊；
- 生成後檢查禁洩漏資訊；
- 提供範本降級；
- 所有輸出保留來源與版本。

## 18.5 CompilableWorld 被單一遊戲特化

策略：

- Living World 功能全部以可選模組提供；
- RPG 名詞不進入 Core Schema；
- Core 只保留 Entity、State、Function、Event、Transition、Policy、Scenario；
- Reference Game 需求先映射至通用 IR，再進 Runtime；
- 《命運之欲》等大型世界只能透過世界包擴展，不可修改 Core 本體假設。

---

# 十九、研究命題

本系統同時可作為以下問題的實驗平台。

## 19.1 世界是否能在沒有主線時保持可玩性

$$
\text{Playability}
\stackrel{?}{=}
f(
\text{opportunities},
\text{feedback},
\text{stakes},
\text{identity},
\text{continuity}
)
$$

## 19.2 玩家是否會對世界而非單一角色產生投入

當角色可死亡與替換時，玩家的投入對象可能從：

$$
\text{Avatar Attachment}
$$

轉向：

$$
\text{World-History Attachment}
+
\text{Lineage Attachment}
+
\text{Organization Attachment}
$$

## 19.3 有限規則與生成式 AI 的最佳分界

需要實驗：

- 哪些內容必須確定性；
- 哪些內容適合生成；
- 哪些資訊可以摘要；
- 哪些延遲會破壞 flow；
- 哪些 NPC 值得高精度推理。

## 19.4 可編譯世界是否能跨 Runtime 保持同一性

同一 World IR 編譯到文字、2D 與未來 3D Runtime 時，如何判斷它們仍是同一世界：

$$
\operatorname{Identity}(W^{\text{text}},W^{\text{2D}},W^{\text{3D}})
$$

可由：

- 穩定 ID；
- 核心規則；
- 事件歷史；
- 狀態轉移；
- Scenario 結果

共同約束。

---

# 二十、長期路線

## 20.1 第一階段：參考遊戲

證明小型持續世界可玩，玩家可跨角色與世代繼續。

## 20.2 第二階段：創作者世界包

開放：

- 地圖；
- 人物範本；
- 組織；
- 法律；
- 經濟；
- 契約；
- 視覺資源；
- AI 表達策略。

## 20.3 第三階段：大型世界適配

開始處理：

- 大量城市；
- 多種族；
- 複雜力量體系；
- 神學；
- 大型戰爭；
- 跨區域政治；
- 《命運之欲》。

## 20.4 第四階段：多 Runtime

同一世界包可輸出：

- 終端文字版；
- 瀏覽器 2D；
- 桌面 2.5D；
- Agent-only 模擬；
- 教學與研究觀測版；
- 未來 3D 客戶端。

---

# 結論

三個月前的「通用世界模擬器」提出了現代《俠客遊》式遊戲的玩家體驗、AI 生成、因果與多層級空間構想。CompilableWorld 則補上了它當時缺少的世界中間表示、編譯、驗證、事件溯源、版本、Trace、Agent 治理與多 Runtime 邊界。

兩者不應合併成一個模糊產品，而應形成清楚的上下游：

$$
\boxed{
\text{CompilableWorld}
=
\text{可編譯世界基礎設施}
}
$$

$$
\boxed{
\text{Living World Runtime}
=
\text{持續世界 RPG 執行層}
}
$$

$$
\boxed{
\text{Reference Game}
=
\text{現代《俠客遊》精神續作的第一方驗證遊戲}
}
$$

第一個驗證遊戲不採用《命運之欲》。它應以最小世界、最少設定與完整生命週期證明三件事：

$$
\boxed{
\text{世界不依附玩家}
}
$$

$$
\boxed{
\text{NPC 能在規則內自行生活}
}
$$

$$
\boxed{
\text{角色死亡後，歷史仍值得繼續}
}
$$

當這三項成立後，《命運之欲》才不再只是被塞入某個遊戲引擎的設定集，而能成為一個真正可編譯、可運作、可演化並能跨載體存在的持續世界。

---

# 附錄 A：最小驗證情境

## Scenario 1：無玩家十年

```yaml
given:
  world: reference_world_alpha
  player_control: disabled
when:
  simulate: 10_years
then:
  - population > 0
  - all_required_roles_filled_or_explicitly_vacant
  - event_log_is_valid == true
  - no_negative_inventory == true
  - no_dead_person_actions == true
```

## Scenario 2：商人死亡

```yaml
given:
  merchant: person_000184
  merchant.controls_caravan: caravan_00008
when:
  action: kill(person_000184)
then:
  - person_000184.alive == false
  - caravan_00008.manager != person_000184
  - inheritance_event_exists == true
  - supply_effect_scheduled == true
  - witnesses_update_knowledge == true
```

## Scenario 3：玩家角色繼承

```yaml
given:
  player_character: person_000001
  eligible_successor: person_000017
when:
  person_000001.dies
then:
  - estate_settled == true
  - world_time_continues == true
  - person_000017.is_selectable == true
  - event_history_preserved == true
```

## Scenario 4：AI 超時

```yaml
given:
  dialogue_ai: timeout
when:
  player_talks_to: person_000184
then:
  - ui_feedback_under_100ms == true
  - template_dialogue_available == true
  - no_world_state_corruption == true
```

## Scenario 5：任務無人承接

```yaml
given:
  contract: protect_caravan
  player_refuses: true
when:
  advance_time: 5_days
then:
  - contract_status in [accepted_by_npc, expired, failed, withdrawn]
  - world_consequence_exists == true
```

---

# 附錄 B：文件沿革

本白皮書承接並重構以下早期設計方向：

1. 《通用世界模擬器：基於俠客遊範式的 AI 驅動遊戲引擎》
2. 《通用世界模擬器：俠客遊範式的現代重構》
3. CompilableWorld Studio、MSSP × RDR、World IR 與模組化 Runtime 的近期工程設計

早期文件主要處理遊戲體驗、AI 內容、因果反應與創作者工具；本文則將其重新放入 CompilableWorld 的分層架構中，使「現代俠客遊式遊戲」成為可被驗證與編譯的第一方 Runtime 應用，而不是再次與底層引擎混為一體。
