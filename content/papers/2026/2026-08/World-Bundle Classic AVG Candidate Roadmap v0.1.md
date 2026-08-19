# World-Bundle Classic AVG Candidate Roadmap v0.1
## 經典 AVG／分支敘事遊戲的世界束改造候選清單、實驗目的與優先順序

**版本：** v0.1  
**定位：** 研究規劃／MVP 選型／經典遊戲改造路線圖  
**核心框架：** World-Bundle Narrative Game、Heterogeneous-Observer Asynchronous Semantic-Causal Computation、T Query Runtime

---

## 0. 研究目標

本文件不是單純列出「哪些 AVG 很經典」。

真正要找的是：

> **哪些既有作品最適合拿來驗證 World-Bundle Narrative Game 的不同核心命題？**

世界束敘事遊戲與一般 branching narrative 的主要差異，不是分支數量更多，而是：

\[
\boxed{
\text{玩家每一次語義選擇，都會改變下一階可達未來空間本身。}
}
\]

傳統 branching narrative：

\[
S_t \rightarrow \{S_{t+1}^{(1)},S_{t+1}^{(2)},\dots\}.
\]

World-Bundle：

\[
\boxed{
S_t
\xrightarrow{PlayerIntent}
I_t
\xrightarrow{AI}
\mathcal B_t
\xrightarrow{WorldRules}
\mathcal B_t^{valid}
\xrightarrow{Commit}
S_{t+1}.
}
\]

因此：

\[
\boxed{Flowchart \neq WorldBundle.}
\]

---

## 1. 候選作品評估標準

### 1.1 分支／狀態密度
是否已有多路線、多結局、角色狀態、旗標與跨章節因果。

### 1.2 Hard World Rule 清晰度
是否容易抽象成：

\[
WorldState + EventRules + CausalConstraints.
\]

世界束最重要的原則仍然是：

\[
\boxed{AI \neq WorldAuthority.}
\]

### 1.3 異質觀察者程度
是否存在多個：

\[
O_1,O_2,\dots,O_n
\]

且各自具有不同資訊、目標、時間軸與世界投影：

\[
\boxed{\Pi_i(W)\neq\Pi_j(W).}
\]

### 1.4 AI 語義輸入的價值
原本固定選項是否明顯壓縮了玩家真正想做的事？如果自由輸入能把：

\[
ChoiceID \rightarrow SemanticAction
\]

做出真正差異，改造價值就高。

### 1.5 可改造性
研究原型要考慮腳本格式、mod 生態、引擎、資料可抽取性，以及能不能只切一個區段做 patch。

### 1.6 語音連續性
全語音作品若新增 branch 沒有一致語音，玩家會立刻知道哪段是動態內容。正式產品必須採授權角色聲音／聲優／合法 digital voice 或商業可用合成聲音。

---

## 2. 第一梯隊候選

目前核心候選：

\[
\boxed{
\text{寒蟬}
+
428
+
CLANNAD/Little\ Busters!
+
STEINS;GATE
+
Zero\ Escape
+
Detroit:Become\ Human
}
\]

它們不是互相替代，而是分別驗證不同問題。

---

## 3. 寒蟬鳴泣之時
### 定位：工程接入／第一個真正改造原型

核心問題：

\[
\boxed{
\text{傳統 VN 到底能不能實際掛上 World-Bundle Runtime？}
}
\]

優勢：
- 適合局部切片；
- 既有 mod／腳本研究生態；
- 語音與圖像 patch 經驗成熟；
- 世界本身具有多版本歷史／碎片式語義親和性。

**建議實驗：** 只取一個 20–30 分鐘片段，加入：

```text
自由語義輸入
→ AI Intent Parse
→ Candidate Bundle
→ Rule Validation
→ NPC Response
→ State Transition
```

這一款最適合回答「能不能真的改」。

---

## 4. 428 ～被封鎖的澀谷～
### 定位：異質觀察者／多時間軸因果束

核心問題：

\[
\boxed{
\text{多角色、不同時間軸的世界束是否能真正非同步運作？}
}
\]

作品天然接近：

\[
\boxed{
O_1\parallel O_2\parallel O_3\parallel O_4\parallel O_5.
}
\]

不同角色知道不同資訊，而且：

\[
a_i \rightarrow S_j
\]

會跨 observer 產生因果影響。

**建議實驗：** 取同一 30–60 分鐘區間、3 個角色、1–2 個跨角色重大事件。讓 AI 分別預展：

\[
SpecExpand(\mathcal B_i)
\]

再由同一 world simulator 驗證。

這是 HOASC 最直接的遊戲 benchmark。

---

## 5. CLANNAD / Little Busters!
### 定位：Relationship-State World Bundle

核心問題：

\[
\boxed{
\text{玩家真正的語義，而非 Choice ID，能不能改變角色關係的可達未來？}
}
\]

例如同一句：

> 「今天我陪你回家。」

可能是：
- romantic interest；
- protective behavior；
- politeness；
- guilt；
- social obligation；
- avoid-other-event。

結合不同：

\[
History_t
\]

之後：

\[
\boxed{
SameSentence + DifferentRelationshipHistory
\rightarrow
DifferentFutureBundle.
}
\]

**CLANNAD** 適合個人 route／情感狀態。  
**Little Busters!** 更適合多人團體關係束。

若只選一個做關係實驗，略偏 Little Busters!。

---

## 6. STEINS;GATE
### 定位：World Line → World Bundle

核心問題：

\[
\boxed{
\text{傳統「世界線」能不能真正升級成「世界束」？}
}
\]

世界線可抽象成：

\[
WorldLine_i.
\]

世界束：

\[
\boxed{
\mathcal B_t
=
\{WorldLine_1,WorldLine_2,\ldots\}.
}
\]

AI 可以在玩家真正觸發 phone action 前：

\[
SpecExpand(\mathcal B_t).
\]

最適合驗證：

\[
\boxed{
\text{Causal Speculative Precomputation}.
}
\]

**不建議第一個做**，因為原始因果鏈太複雜，容易把研究變成理解原作規則。

---

## 7. Zero Escape
### 定位：Hard-State Validator

核心問題：

\[
\boxed{
\text{AI 的語義自由能不能和 deterministic hard-state rule engine 共存？}
}
\]

適合原因：
- room state；
- inventory；
- knowledge state；
- survival；
- puzzle constraints；
- branching；
- information asymmetry。

分工非常乾淨：

\[
\boxed{AI=SemanticInterpreter}
\]

\[
\boxed{Computer=StateValidator}
\]

適合驗證 AI 自由輸入是否能安全進入硬規則遊戲。

---

## 8. Detroit: Become Human
### 定位：大型成熟 Branching Narrative Benchmark

核心問題：

\[
\boxed{
\text{當傳統 branching narrative 已經非常複雜時，
World Bundle 是否仍然是另一種結構？}
}
\]

這是 Detroit 最重要的研究價值。

它本來已具有：
- 多角色；
- 大型 flowchart；
- 跨角色因果；
- 角色死亡後故事持續；
- 多狀態；
- 多結局；
- 大量 authored branches。

所以不是用它證明「AI 可以增加更多 branch」。

而是要比較：

\[
\boxed{
Many\ Preauthored\ Paths
}
\]

與：

\[
\boxed{
Dynamically\ Reconstructed\ Reachable\ Future\ Space.
}
\]

差異是生成結構，不是 branch count。

---

## 9. Detroit 的多觀察者世界束

可以抽象：

\[
O_K=Kara,\qquad
O_C=Connor,\qquad
O_M=Markus.
\]

三者共享世界：

\[
W,
\]

但：

\[
\boxed{
\Pi_K(W)
\neq
\Pi_C(W)
\neq
\Pi_M(W).
}
\]

因此各自有：

\[
\mathcal B_K,\quad
\mathcal B_C,\quad
\mathcal B_M.
\]

最後再收連到：

\[
\boxed{\mathcal B_W.}
\]

這是大型異質觀察者世界束最好的展示型 benchmark。

---

## 10. Detroit 的自由語義選擇

例如 Connor 審問 Android。

傳統選項：

```text
Threaten
Empathize
Pressure
Calm
```

World-Bundle 玩家可以輸入：

> 「不要直接威脅。我故意說錯一個證據細節，看他會不會主動糾正。」

AI 解析：

```text
non_threatening
evidence_signaling
deliberate_misstatement
reaction_probe
```

再展開：

\[
\mathcal B=
\{
F_{corrects},
F_{silent},
F_{stress},
F_{detects\ trap},
F_{trust},
F_{shutdown}
\}.
\]

傳統狀態機再依：

```text
Stress
Trust
EvidenceKnown
PriorDialogue
TimeRemaining
Deviancy
```

驗證。

這就是：

\[
\boxed{
ChoiceMenu\rightarrow SemanticActionSpace.
}
\]

---

## 11. Detroit Flowchart → World-Bundle UI

可將 flowchart 升級成：

```text
              Current State
                   ●
          ┌────────┼────────┐
          │        │        │
      Authored  Predicted  Latent
        ○         ◌◌◌       ?
                  │
               Validated
                  ●
```

建議：
- 實線：Canonical authored path；
- 虛線：AI speculative future；
- 亮線：Validated；
- 灰線：曾可達、現在失效；
- 鎖：Hard constraint；
- 收束符號：多 narrative paths 已 CRL 到同一 hard state。

Detroit 甚至可以把 speculative future visualization 直接合理化為 Connor 的分析能力。

---

## 12. 後期候選

### Fate/stay night
高密度 route、lore、identity；非常適合，但 scope 太大。

### Rewrite
Hard-world rules 與 route 結構很適合，但同樣容易 scope explosion。

### Umineko
不一定最適合自由 action world bundle，但非常適合：

\[
\boxed{
X^QX^OT
}
\]

即 observer、truth model、meta-query、interpretation。

---

## 13. 建議實驗順序

### Phase 1 — 工程接入
**寒蟬**

\[
\boxed{
\text{能不能真的把傳統 VN 改成 World-Bundle Runtime？}
}
\]

### Phase 2 — 異質觀察者
**428**

\[
\boxed{
\text{多 observer / 多時間軸是否能形成非同步因果世界束？}
}
\]

### Phase 3 — 關係語義
**Little Busters! / CLANNAD**

\[
\boxed{
\text{自由語義選擇能不能改變 relationship-state bundle？}
}
\]

### Phase 4 — 因果預計算
**STEINS;GATE**

\[
\boxed{
\text{World Line 能不能升級成 World Bundle？}
}
\]

### Phase 5 — Hard-State Validation
**Zero Escape**

\[
\boxed{
\text{AI semantic freedom + deterministic hard constraints 是否能穩定共存？}
}
\]

### Phase 6 — 大型 Benchmark / Showcase
**Detroit: Become Human**

\[
\boxed{
\text{當傳統 branching 已高度成熟，
World Bundle 是否仍能顯示結構上的不同？}
}
\]

---

## 14. 如果只選三款

優先：

\[
\boxed{
\text{寒蟬}
+
428
+
Detroit
}
\]

分別回答：

- 寒蟬：能不能真的接進舊 AVG？
- 428：異質觀察者非同步世界束是否成立？
- Detroit：世界束是否真的不同於極大型 Flowchart？

---

## 15. 如果只選四款

再加入：

\[
\boxed{STEINS;GATE}
\]

作：

\[
WorldLine\rightarrow WorldBundle
\]

最漂亮的概念展示。

---

## 16. 研究版 vs 公開版

### 私人研究原型
適合研究 scene graph、save state、flags、script、state transition。

### Mod / Patch
最好只發布自己新增的 patch / runtime，不直接重發原作資產。

### 正式產品
最乾淨的是：
- 自己 IP；
- 正式授權；
- 合法聲優／voice model；
- 自己的 World-Bundle Runtime。

所以經典 AVG 最適合作：

\[
\boxed{
\text{Reverse-Engineering Benchmark}.
}
\]

原創 MVP 則作：

\[
\boxed{
\text{Publishable Benchmark}.
}
\]

---

## 17. 語音策略

Voice Layer 屬於：

\[
\boxed{
SoftNarrativeRealization.
}
\]

資料可包含：

```text
VoiceProfile
CharacterID
Emotion
Prosody
Intensity
SceneContext
License
```

產品層必須使用已授權聲優、合法 digital voice replica、商業可用合成 voice 或自有角色聲線。

---

## 18. 最終候選矩陣

| 遊戲 | 核心實驗 |
|---|---|
| 寒蟬 | 舊 VN 技術接入 |
| 428 | 異質觀察者／跨時間因果 |
| CLANNAD | 個人 relationship-state |
| Little Busters! | 群體 relationship-state |
| STEINS;GATE | World Line → World Bundle |
| Zero Escape | deterministic hard-state validation |
| Detroit: Become Human | 大型成熟 branching benchmark |
| Umineko | Meta-Query / observer / truth-model |
| Rewrite | 大型 hard-world rule system |
| Fate/stay night | 高密度 route / lore / identity |

---

## 19. 最終結論

這些作品剛好可以形成：

\[
\boxed{
\text{World-Bundle Benchmark Suite}.
}
\]

從傳統 VN 一路測：

\[
\text{技術接入}
\rightarrow
\text{多角色異步}
\rightarrow
\text{關係狀態}
\rightarrow
\text{世界線}
\rightarrow
\text{硬規則}
\rightarrow
\text{大型 authored branching}.
\]

如果最後連 Detroit 這種高度成熟的 branching narrative 都能清楚看出：

\[
\boxed{
Flowchart\neq WorldBundle,
}
\]

那麼「世界束」就不只是「AI 多生成一些支線」的另一種說法。

它真正代表：

\[
\boxed{
\text{同一套世界法則下，
依玩家歷史、語義意圖、異質觀察者與即時預展，
動態重建每個玩家可達的未來空間。}
}
\]
