# 孫子兵法數學框架遊戲AI應用規範：三層可執行架構

**Sun Tzu Mathematical Framework — Game AI Application Specification:  
A Three-Layer Executable Architecture**

---

作者：Neo K.  
機構：一言諾科技有限公司（EveMissLab）  
版本：v0.1 Draft  
年份：2026  
配合文件：《孫子兵法數學框架：主態空間Γ(t)與降維投影理論》v0.1  
符號規範：MSUS v0.2  

---

## 摘要

本文是《孫子兵法數學框架》理論文件的應用示範規範，目標讀者為遊戲AI設計者與決策系統開發者。本文不提供完整實現代碼，而是提供三個遞進層次的形式化規範與偽代碼：**行為樹層**（答話篇直接轉譯）、**效用評估層**（Γ(t)驅動的狀態機）、**強化學習環境層**（Γ(t)作為MDP定義）。三層可獨立使用，亦可疊加組合。

---

## 第一章　前言

### 1.1 應用示範的定位

理論框架的價值最終需要在可執行結構上得到驗證。孫子兵法數學框架建立了主態空間 $\Gamma(t)$ 及其六個耦合維度，但框架本身不回答一個實踐問題：**一個遊戲AI如何使用這個框架做出決策？**

本文的回答是：有三個層次可以使用，複雜度遞增，適用場景不同，但都來自同一個 $\Gamma(t)$ 結構。

### 1.2 三層架構概覽

```
Layer 3：強化學習環境層
  ↑ 依賴
Layer 2：效用評估 + 狀態機層
  ↑ 依賴
Layer 1：行為樹層（答話篇）
  ↑ 依賴
主態空間 Γ(t)
```

每一層都是完整可用的：

| 層次 | 核心結構 | 主要使用篇章 | 適用場景 |
|------|---------|------------|---------|
| Layer 1 | 決策樹 / 行為樹 | 答話篇 | 規則型AI，可解釋性優先 |
| Layer 2 | 效用函數 + 狀態機 | 始計、軍形、謀攻 | 策略型AI，評估驅動 |
| Layer 3 | MDP環境規範 | 全篇（Γ(t)完整定義） | 學習型AI，訓練驅動 |

### 1.3 符號說明

本文沿用MSUS v0.2符號規範。所有理論推導見主論文，本文僅作引用不作推導。

---

## 第二章　Γ(t) 的可執行表示

在進入三層架構之前，需要將理論上的主態空間 $\Gamma(t)$ 轉化為可在程式中實例化的數據結構。

### 2.1 狀態向量定義

```python
@dataclass
class GammaState:
    # 成分一：資源張量 R(t) ∈ ℝ⁴
    M: float   # 己方兵力，[0, M_max]
    R: float   # 物資資源，[0, R_max]
    C: float   # 國家總資本，[0, C_max]
    Er: float  # 敵方可掠奪資源，[0, Er_max]

    # 成分二：資訊覆蓋率 K(t) ∈ [0,1]²
    k_self: float  # 自我認知完整度
    k_enemy: float # 對敵認知完整度

    # 成分三：勢能場（空間均勻化近似）
    S: float   # 整體勢能值，[-S_max, S_max]
    # 注：完整空間分布 S(t,x) 在 Layer 3 中展開

    # 成分四：地理空間（離散化）
    terrain_type: int  # 九地類型索引 [0,8]
    position: tuple    # (x, y) 在戰場網格上的坐標

    # 成分五：意志向量 W(t) ∈ [0,1]³
    D: float     # 道/民心一致度
    mu: float    # 軍心穩定性
    L_eff: float # 將領有效指揮係數

    # 成分六：制度結構（緩變量，通常固定）
    F_inst: float  # 制度規範有效性
```

### 2.2 狀態更新函數

對應主論文的 $d\Gamma/dt = \Xi_{\text{sys}}(\Gamma, A, \phi(A), E_a, \mathcal{G})$：

```python
def update_gamma(state: GammaState, 
                 action: Action, 
                 enemy_action: Action,
                 dt: float) -> GammaState:
    
    new_state = copy(state)
    
    # 資源動力學（作戰篇）
    cost = compute_cost(state.M, state.R, dt)
    loot = compute_loot(action, state.Er)
    new_state.M -= cost.M_loss
    new_state.R -= cost.R_loss - loot.R_gain
    new_state.Er -= loot.Er_consumed
    
    # 資訊更新（行軍篇 + 用間篇）
    info_gain = recon_update(action, enemy_action, state.terrain_type)
    decay = LAMBDA_K * dt
    new_state.k_enemy = min(1.0, state.k_enemy + info_gain - decay)
    
    # 勢能更新（兵勢篇主方程簡化）
    F_ext = compute_force(action, state)
    new_state.S = state.S + F_ext * dt - divergence_term(state) * dt
    
    # 意志更新
    new_state.mu = update_morale(state, action, enemy_action)
    
    return new_state
```

---

## 第三章　Layer 1：行為樹（答話篇直接轉譯）

### 3.1 設計原則

答話篇的核心邏輯是：

$$^{映}\Omega^{答}: (^{態}Q^{答},\; ^{態}\Sigma^{答}(\Gamma)) \to A$$

在遊戲AI中，「問題 $Q$」是系統每幀自動發出的狀態查詢，「態勢分類 $\Sigma$」是對當前 $\Gamma(t)$ 的離散化判斷，「行動 $A$」是AI本幀的決策輸出。

### 3.2 態勢分類器

對應 $^{態}\Sigma^{答}(\Gamma(t))$，將連續狀態空間離散化為13種戰略態勢：

```python
def classify_situation(state: GammaState) -> Situation:
    
    # 地形優先判斷（九地/九變篇）
    if state.terrain_type == TERRAIN_DEATH:
        return Situation.DEATH_GROUND      # σ_死地
    
    if state.terrain_type == TERRAIN_SCATTER and state.D < 0.3:
        return Situation.SCATTER_GROUND    # σ_散地
    
    # 資源狀態判斷（作戰篇）
    if state.R < R_CRITICAL and state.Er > 0:
        return Situation.HEAVY_GROUND      # σ_重地（掠奪資源）
    
    # 資訊不對稱判斷（謀攻篇）
    if state.k_enemy < 0.2:
        return Situation.LIGHT_GROUND      # σ_輕地（不宜停留）
    
    # 敵方狀態判斷（需要敵方Γ的估算）
    if estimated_enemy_morale < 0.3:
        return Situation.ENEMY_ARROGANT    # σ_敵驕
    
    if enemy_holds_high_ground(state):
        return Situation.ENEMY_HOLDS_HIGH  # σ_敵據險
    
    # 勢能判斷（軍形篇）
    if state.S > S_ATTACK_THRESHOLD:
        return Situation.OFFENSIVE_READY   # σ_可勝
    
    # 包圍判斷
    if surrounded(state):
        return Situation.ENCIRCLED         # σ_圍地
    
    # 預設：衢地（外交聯盟優先）
    return Situation.JUNCTION_GROUND       # σ_衢地
```

### 3.3 行為樹規範

對應 $^{映}\Omega^{答}: \Sigma \to A$：

```python
def behavior_tree(situation: Situation, state: GammaState) -> Action:
    
    match situation:
        case Situation.SCATTER_GROUND:
            # 散地：保守堅守，不主動出擊
            return Action.DEFEND_AND_HOLD
        
        case Situation.LIGHT_GROUND:
            # 輕地：假撤誘敵（詭道映射 φ^始）
            return Action.FEINT_RETREAT
        
        case Situation.HEAVY_GROUND:
            # 重地：速掠敵資源（η^作）
            return Action.RAID_RESOURCES
        
        case Situation.DEATH_GROUND:
            # 死地：全力死戰，釋放全部勢能
            return Action.ALL_OUT_ASSAULT
        
        case Situation.ENEMY_ARROGANT:
            # 敵驕：鬆懈奇襲（φ^兵 正奇轉化）
            return Action.SURPRISE_ATTACK
        
        case Situation.ENEMY_HOLDS_HIGH:
            # 敵據險：斷糧道（η^作 的逆操作）
            return Action.CUT_SUPPLY_LINE
        
        case Situation.ENCIRCLED:
            # 圍地：謀破局（θ^爭 分兵）
            return Action.BREAK_ENCIRCLEMENT
        
        case Situation.OFFENSIVE_READY:
            # 勢能充足：發動主攻
            return Action.MAIN_ASSAULT
        
        case Situation.JUNCTION_GROUND:
            # 衢地：外交/聯盟優先
            return Action.SEEK_ALLIANCE
        
        case _:
            return Action.HOLD_POSITION
```

### 3.4 Layer 1 的能力邊界

行為樹覆蓋了答話篇的13種態勢回應，但**不具備預測能力**——它只響應當前狀態，不評估行動的中長期效果。這個限制由Layer 2補足。

---

## 第四章　Layer 2：效用評估 + 狀態機

### 4.1 效用函數

對應主論文的勝負評估函數 $\kappa(\Gamma(t)) = \sum_i w_i \cdot \kappa_i(\Gamma_i)$：

```python
# 預設權重（可依遊戲類型調整）
WEIGHTS = {
    'resource': 0.25,    # 資源成分
    'info':     0.20,    # 資訊優勢
    'momentum': 0.25,    # 勢能
    'will':     0.20,    # 意志
    'terrain':  0.10,    # 地形利害
}

def evaluate(state: GammaState) -> float:
    """
    返回 [0, 1] 的勝負評估值
    對應 κ^{始}(Γ(t))
    """
    
    # κ_R：資源評估（作戰篇）
    resource_score = (
        state.M / M_MAX * 0.4 +
        state.R / R_MAX * 0.3 +
        state.C / C_MAX * 0.3
    )
    
    # κ_K：資訊優勢評估（謀攻篇）
    # k_己=1, k_彼=1 → 最高分
    info_score = (state.k_self * 0.4 + state.k_enemy * 0.6)
    
    # κ_S：勢能評估（軍形篇）
    # 正規化勢能差 d(Es-Ea)/dt
    momentum_score = sigmoid(state.S / S_MAX)
    
    # κ_W：意志評估（始計篇 + 九變篇）
    will_score = (
        state.D    * 0.4 +
        state.mu   * 0.4 +
        state.L_eff * 0.2
    )
    
    # κ_G：地形利害評估（地形篇）
    terrain_score = TERRAIN_VALUE_TABLE[state.terrain_type]
    
    return (
        WEIGHTS['resource']  * resource_score  +
        WEIGHTS['info']      * info_score       +
        WEIGHTS['momentum']  * momentum_score   +
        WEIGHTS['will']      * will_score       +
        WEIGHTS['terrain']   * terrain_score
    )
```

### 4.2 廟算搜索

對應主論文的廟算模型：

$$^{指}算^{始} = \text{Card}\bigl\{a \in A \mid \kappa(\Gamma + \delta_a\Gamma) > \kappa(\Gamma)\bigr\}$$

```python
def temple_calculation(state: GammaState, 
                       candidate_actions: list[Action],
                       horizon: int = 3) -> Action:
    """
    廟算：在 horizon 步內找到最大化 κ(Γ) 增量的行動
    對應 sgn(n_我 - n_敵) 的己方項最大化
    """
    
    best_action = None
    best_score = -inf
    
    for action in candidate_actions:
        # 模擬執行該行動後的狀態
        simulated_state = simulate(state, action, horizon)
        score = evaluate(simulated_state)
        
        if score > best_score:
            best_score = score
            best_action = action
    
    return best_action
```

### 4.3 狀態機設計

對應九變篇的動態適應映射 $^{映}\theta^{變}: (\Gamma, D, E, B) \to A$，以及軍形篇的攻守能量閾值：

```python
class StrategicStateMachine:
    """
    三個宏觀戰略狀態，由 Γ(t) 的勢能成分驅動轉換
    對應軍形篇：不可勝者，守也；可勝者，攻也
    """
    
    DEFENSIVE = "defensive"   # σ(Ds) 優先，等待 τ(E) 最小
    ADAPTIVE  = "adaptive"    # 九變篇模式，動態應對
    OFFENSIVE = "offensive"   # S > S_threshold，發動主攻
    
    def __init__(self):
        self.current_state = self.DEFENSIVE
    
    def transition(self, gamma: GammaState) -> str:
        
        match self.current_state:
            
            case self.DEFENSIVE:
                # 軍形篇：守能量穩定 + 敵方脆弱度達閾值 → 轉攻
                if (gamma.S > S_ATTACK_THRESHOLD and 
                    gamma.k_enemy > 0.6):
                    self.current_state = self.OFFENSIVE
                # 資訊不足 → 轉適應
                elif gamma.k_enemy < 0.3:
                    self.current_state = self.ADAPTIVE
            
            case self.OFFENSIVE:
                # 勢能耗盡或資源告急 → 退守
                if (gamma.S < S_RETREAT_THRESHOLD or
                    gamma.M < M_CRITICAL):
                    self.current_state = self.DEFENSIVE
            
            case self.ADAPTIVE:
                # 九變篇：地形/敵情穩定後回歸主策略
                if gamma.k_enemy > 0.5:
                    self.current_state = self.DEFENSIVE
        
        return self.current_state
    
    def decide(self, gamma: GammaState, 
               candidates: list[Action]) -> Action:
        
        state = self.transition(gamma)
        
        match state:
            case self.DEFENSIVE:
                # 守：最大化 σ^{形}(Ds)
                return min(candidates, 
                           key=lambda a: defensive_cost(a, gamma))
            
            case self.OFFENSIVE:
                # 攻：廟算搜索最優行動
                return temple_calculation(gamma, candidates)
            
            case self.ADAPTIVE:
                # 適：行為樹（Layer 1）處理特殊態勢
                situation = classify_situation(gamma)
                return behavior_tree(situation, gamma)
```

### 4.4 Layer 2 的能力邊界

Layer 2 具備短期預測能力（廟算horizon），但依賴人工設計的權重與閾值。對抗環境中，這些超參數需要調整，且無法自動適應未見過的敵方策略。這個限制由Layer 3補足。

---

## 第五章　Layer 3：強化學習環境規範

### 5.1 MDP形式化定義

將 $\Gamma(t)$ 框架映射到標準馬可夫決策過程 $(S, A, P, R, \gamma)$：

| MDP元素 | 框架對應 | 說明 |
|---------|---------|------|
| 狀態空間 $S$ | $\Gamma(t)$ | `GammaState` 數據結構 |
| 動作空間 $A$ | $^{態}A^{i}$ 的聯集 | 各篇行動集合的離散化並集 |
| 轉移函數 $P$ | $\Xi_{\text{sys}}$ | `update_gamma()` |
| 回報函數 $R$ | $\kappa(\Gamma(t))$ | `evaluate()` |
| 折扣因子 $\gamma$ | — | 設計參數，建議 0.95 |

### 5.2 動作空間定義

```python
class Action(Enum):
    # 資源類（作戰篇）
    ADVANCE         = 0   # 前進消耗
    RETREAT         = 1   # 後退保存
    RAID_RESOURCES  = 2   # 因糧於敵（η^作）
    
    # 資訊類（謀攻篇 + 用間篇）
    RECONNAISSANCE  = 3   # 偵查（φ^行 更新 k_彼）
    DEPLOY_SPIES    = 4   # 用間（φ^間 主動更新）
    
    # 勢能類（兵勢篇）
    MAIN_FORCE      = 5   # 正兵（維持勢場基底）
    SURPRISE_ATTACK = 6   # 奇兵（注入 F_ext 峰值）
    
    # 地形類（九變/九地篇）
    HOLD_POSITION   = 7   # 守地
    SEEK_ALLIANCE   = 8   # 衢地外交
    BREAK_OUT       = 9   # 死地突圍
    
    # 意志類（始計篇）
    RALLY           = 10  # 鼓舞士氣（提升 μ）
    FEINT_RETREAT   = 11  # 詭道：示弱（φ^始）
    
    # 火攻類（火攻篇，條件觸發）
    FIRE_ATTACK     = 12  # 需天時條件滿足
```

### 5.3 回合邊界定義

```python
def is_terminal(state: GammaState) -> tuple[bool, float]:
    """
    回合終止條件 + 終局回報
    對應謀攻篇的勝負條件與作戰篇的資源耗盡
    """
    
    # 勝利條件：敵方資源歸零（屈服映射 χ^謀 完成）
    if enemy_state.M <= 0:
        return True, +1.0
    
    # 失敗條件1：己方兵力耗盡
    if state.M <= 0:
        return True, -1.0
    
    # 失敗條件2：意志崩潰（軍形篇因果鏈斷裂）
    if state.L_eff <= 0 or state.mu <= 0:
        return True, -0.8
    
    # 失敗條件3：資源耗盡且無法補給
    if state.R <= 0 and state.Er <= 0:
        return True, -0.6
    
    # 回合上限（作戰篇：兵貴勝，不貴久）
    if current_step >= MAX_STEPS:
        # 以當前評估值作為終局回報
        return True, evaluate(state) * 2 - 1  # 映射到 [-1, 1]
    
    return False, 0.0
```

### 5.4 回報函數設計

```python
def compute_reward(prev_state: GammaState,
                   action: Action,
                   next_state: GammaState) -> float:
    """
    即時回報 = 狀態改善量 + 行動效率獎勵 + 懲罰項
    """
    
    # 主回報：κ(Γ) 的改善量
    delta_eval = evaluate(next_state) - evaluate(prev_state)
    
    # 資訊獎勵：k_彼 提升有額外獎勵（謀攻篇：知彼知己）
    info_bonus = 0.1 * max(0, next_state.k_enemy - prev_state.k_enemy)
    
    # 速戰獎勵：每步給予微小負回報，鼓勵速勝（作戰篇：t*）
    time_penalty = -0.01
    
    # 詭道獎勵：成功欺騙敵方時的額外回報（虛實篇）
    deception_bonus = 0.05 if deception_succeeded(action, enemy_state) else 0
    
    return delta_eval + info_bonus + time_penalty + deception_bonus
```

### 5.5 環境接口規範

```python
class SunTzuEnv:
    """
    標準 gym-style 環境接口
    狀態空間 = Γ(t)，動力學 = Ξ_sys
    """
    
    def reset(self) -> GammaState:
        """
        初始化 Γ(0)
        對應始計篇：未戰而廟算
        """
        self.state = GammaState(
            M=1.0, R=1.0, C=1.0, Er=0.5,
            k_self=0.8, k_enemy=0.3,   # 始計：知己勝於知彼
            S=0.0,
            terrain_type=TERRAIN_JUNCTION,
            position=(MAP_CENTER),
            D=0.8, mu=0.8, L_eff=1.0,
            F_inst=0.9
        )
        return self.state
    
    def step(self, action: Action) -> tuple:
        """
        執行一步，返回 (next_state, reward, done, info)
        """
        enemy_action = self.enemy_policy(self.state)
        
        # 詭道映射：呈現假象給敵方
        apparent_action = deception_map(action, self.state)
        
        next_state = update_gamma(
            self.state, action, enemy_action, dt=1.0
        )
        
        reward = compute_reward(self.state, action, next_state)
        done, terminal_reward = is_terminal(next_state)
        
        if done:
            reward += terminal_reward
        
        self.state = next_state
        return next_state, reward, done, {}
    
    def action_mask(self, state: GammaState) -> list[bool]:
        """
        行動遮罩：某些行動需要前提條件
        對應火攻篇：天時具備才可發動火攻
        """
        mask = [True] * len(Action)
        
        # 火攻需要天時條件
        if not weather_condition_met(state):
            mask[Action.FIRE_ATTACK] = False
        
        # 用間需要資本支持
        if state.C < SPY_COST:
            mask[Action.DEPLOY_SPIES] = False
        
        return mask
```

---

## 第六章　三層整合架構

### 6.1 層次調用關係

三層並非互斥，而是可以在同一AI系統中協同運作：

```python
class SunTzuAgent:
    """
    三層整合代理
    """
    
    def __init__(self, rl_policy=None):
        self.state_machine = StrategicStateMachine()  # Layer 2
        self.rl_policy = rl_policy  # Layer 3（可選）
    
    def decide(self, state: GammaState, 
               candidates: list[Action]) -> Action:
        
        # 優先使用訓練好的RL策略（Layer 3）
        if self.rl_policy is not None:
            return self.rl_policy(state)
        
        # 退化到Layer 2：狀態機 + 廟算
        strategic_state = self.state_machine.transition(state)
        
        if strategic_state == "adaptive":
            # 特殊態勢退化到Layer 1：行為樹
            situation = classify_situation(state)
            return behavior_tree(situation, state)
        
        return self.state_machine.decide(state, candidates)
```

### 6.2 各層特性對比

| 特性 | Layer 1 行為樹 | Layer 2 狀態機 | Layer 3 強化學習 |
|------|--------------|--------------|----------------|
| 可解釋性 | ✅ 高 | ✅ 中 | ⚠ 低 |
| 泛化能力 | ⚠ 低 | ⚠ 中 | ✅ 高 |
| 實現成本 | ✅ 低 | ✅ 中 | ⚠ 高 |
| 對抗適應 | ❌ 無 | ⚠ 有限 | ✅ 強 |
| 孫子兵法覆蓋 | 答話篇 | 始計/軍形/謀攻 | 全篇 |

### 6.3 設計建議

**若遊戲需要可解釋的AI行為**（如讓玩家看懂AI在做什麼）：以Layer 1為主，Layer 2輔助評估。

**若遊戲需要有挑戰性的策略AI**（無需解釋）：以Layer 2為主，Layer 1處理邊界態勢。

**若遊戲需要自我進化的AI**（如多人對戰的匹配AI）：以Layer 3為主，Layer 1/2作為訓練初始化策略（curriculum learning的起點）。

---

## 第七章　討論

### 7.1 框架覆蓋範圍

本規範直接使用了以下篇章的數學結構：

| 篇章 | 使用方式 |
|------|---------|
| 始計篇 | 初始狀態設定、廟算搜索、評估函數 |
| 作戰篇 | 資源動力學、速戰回報 |
| 謀攻篇 | 資訊優勢評估、終止條件 |
| 軍形篇 | 攻守能量閾值、狀態機轉換條件 |
| 兵勢篇 | 正奇行動分類、勢能更新 |
| 虛實篇 | 詭道映射、欺騙回報 |
| 軍爭篇 | 疲勞損耗、路徑代價 |
| 九變篇 | 自適應狀態機 |
| 行軍篇 | 資訊採集（偵查行動） |
| 地形篇 | 地形評估表 |
| 九地篇 | 態勢分類（9種地形態勢） |
| 火攻篇 | 條件觸發行動（行動遮罩） |
| 用間篇 | 資訊採集（用間行動） |
| 答話篇 | Layer 1 行為樹核心結構 |

### 7.2 本規範的限制

本文不包含：
- 完整的超參數調優指南（$w_i$、閾值等依遊戲類型而異）
- 空間分布型勢能場 $\mathcal{S}(t,\mathbf{x})$ 的完整實現（Layer 1/2使用標量近似）
- 多智能體擴展（當前僅定義單個AI代理對抗靜態敵方策略）
- 具體的神經網絡架構建議（Layer 3）

### 7.3 擴展方向

**多智能體**：為敵方定義對稱的 $\Gamma_{敵}(t)$，實現雙方完整對抗。敵方的 $k_{彼}$（我方被感知程度）成為博弈的核心變量，對應虛實篇的無形態映射 $^{映}\zeta^{虛}: A \to H$。

**空間展開**：將標量勢能 $S$ 擴展為網格上的場 $\mathcal{S}(t, \mathbf{x})$，使勢場流動可視化，對應虛實篇的流體方程 $^{勢}S^{虛}$。

**課程學習**：以Layer 1為初始策略，逐步引入Layer 2的廟算能力，最後訓練Layer 3的完整RL策略，三層形成自然的課程序列。

---

## 第八章　結語

孫子兵法的數學框架在本文中完成了從理論到規範的轉化。

$\Gamma(t)$ 是觀測空間。$\Xi_{\text{sys}}$ 是環境動力學。$\kappa(\Gamma)$ 是評估函數。這三個元素足以定義一個完整的決策環境。

孫子說「勝者之戰，若決積水於千仞之谿者，勢也」——用強化學習的語言重述：高回報的動作序列是在 $\mathcal{S}(t,\mathbf{x})$ 積累到臨界點後，通過正確的行動釋放積累的勢能差，在最短時間內最大化 $\kappa(\Gamma)$ 的增量。

兩千五百年前的軍事直覺，與當代的最優控制理論，在這個框架裡指向同一個結構。

$$\text{最優策略} \;\approx\; \arg\max_\pi \mathbb{E}\left[\sum_t \gamma^t R_t \;\bigg|\; \Gamma(0), \pi\right]$$

---

## 附錄A　動作空間完整規範

（見第五章2.2節 `Action` enum，後續版本補充各動作的前提條件與效果函數）

## 附錄B　超參數參考範圍

| 參數 | 建議範圍 | 說明 |
|------|---------|------|
| `WEIGHTS['resource']` | 0.20–0.35 | 資源密集型遊戲偏高 |
| `WEIGHTS['info']` | 0.15–0.25 | 資訊戰型遊戲偏高 |
| `WEIGHTS['momentum']` | 0.20–0.30 | 節奏型遊戲偏高 |
| `S_ATTACK_THRESHOLD` | 0.6–0.8 | 攻擊傾向調整 |
| `horizon`（廟算深度） | 2–5 | 計算資源與前瞻性的折衷 |
| `MAX_STEPS` | 100–500 | 遊戲長度設計 |
| $\gamma$（折扣因子） | 0.90–0.99 | 偏短期/長期策略調整 |

---

## 版本記錄

| 版本 | 說明 |
|------|------|
| v0.1 | 初稿：三層架構基本規範，偽代碼框架 |

---

*本文件為EveMissLab孫子兵法數學框架計畫應用示範文件。*  
*理論基礎：《孫子兵法數學框架：主態空間Γ(t)與降維投影理論》*  
*符號規範：MSUS v0.2*
