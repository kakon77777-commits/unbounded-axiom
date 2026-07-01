# 光影解法延伸框架：崁套對沖場論
## Shadow Tracking Method Extension: Nested Hedge Field Framework
**EveMissLab Working Paper · Neo.K / Theia**

---

## 0. 符號定義

| 符號 | 意義 |
|------|------|
| G = (V, E) | 可通行圖，V = 格點，E = 鄰接關係 |
| N(v) | v 的可通行鄰居集合 |
| deg(v) = \|N(v)\| | v 的可通行度 |
| φ_p : V → [0,1] | 以 p 為源點（φ=1）、q 為匯點（φ=0）的 Graph Laplacian 場 |
| ∇φ(v) | v 在圖上的梯度：最高φ鄰居方向 |
| P(A → B) | 從 A 出發到達 B 的路徑 |

---

## 1. 基礎場：Graph Laplacian 調和函數（回顧）

**定義 1.1（Graph Laplacian 場）**

給定源點 s（φ=1），匯點 e（φ=0），唯一解滿足：

```
φ(v) = Σ_{w ∈ N(v)} φ(w) / deg(v)    for all v ∉ {s, e}
```

**隨機遊走解釋**：φ(v) = P（從 v 出發的隨機遊走首先到達 s，而非 e）

**關鍵性質**：
- 線性衰減（沿路徑）
- 死巷平台：φ(dead_end) = φ(junction)
- 無內部極值（最大值原理）

---

## 2. 雙場張力框架（Two-Field Tension）

### 2.1 定義

設追逐者 A 位於 pA，逃跑者 B 位於 pB。

計算單一場：φ 的源點 = pA，匯點 = pB

則：

```
φ_A(v)  =  P(RW from v → pA before pB)
φ_B(v)  =  1 − φ_A(v)    # 互補，只需一次計算
```

**張力場（Tension Field）**：

```
T(v)  =  φ_A(v) − φ_B(v)  =  2·φ_A(v) − 1   ∈ [-1, 1]
```

### 2.2 幾何意義

```
T(v) > 0  →  v 屬於 A 的圖拓撲勢力範圍（A 更近）
T(v) < 0  →  v 屬於 B 的圖拓撲勢力範圍
T(v) = 0  →  Nash 均衡前線（圖上的 Voronoi 邊界）
```

### 2.3 最優策略

```
追逐者策略：沿 ∇T 移動（=沿 ∇φ_A 移動）
逃跑者策略：沿 −∇T 移動（=離開 φ_A 梯度）
```

### 演算法 TF（Tension Field Computation）

```
Input:  圖 G，追逐者位置 pA，逃跑者位置 pB
Output: T : V → [-1, 1]

1. φ ← GraphLaplacianSOR(G, source=pA, sink=pB)
2. T(v) ← 2·φ(v) − 1  for all v
3. return T
```

**複雜度**：1 次 SOR 求解，O(N) with Multigrid

---

## 3. 對沖場（Hedge Field）

### 3.1 單一威脅對沖

設代理人想從起點 s 到達目標 g，同時迴避威脅源 e（敵人位置）。

**目標場**：φ_g，源點 = g，匯點 = s（代理人想最大化接近 g 的程度）

**威脅場**：φ_e，源點 = e，匯點 = map boundary（代理人想最小化暴露於 e 的程度）

**對沖場（Hedge Field）**：

```
H(v)  =  φ_g(v) · (1 − φ_e(v))
```

H(v) 高 ⟺  v 在拓撲上靠近目標 g 且遠離威脅 e

### 3.2 梯度分析

```
∇H(v)  =  ∇φ_g(v) · (1−φ_e(v))  −  φ_g(v) · ∇φ_e(v)
```

第一項：朝目標方向推進（受威脅場加權壓制）

第二項：遠離威脅方向（受目標接近程度加權）

**當代理人接近目標時**（φ_g → 1），遠離威脅的衝動被壓制；接近目標優先。

**當代理人接近威脅時**（φ_e → 1），H → 0；整個區域被標記為危險。

### 3.3 多威脅對沖（崁套化）

k 個威脅源 e₁, ..., eₖ，各有對應場 φ_{e1}, ..., φ_{eₖ}：

```
H_k(v)  =  φ_g(v) · ∏_{i=1}^{k} (1 − φ_{ei}(v))
```

此即「所有威脅同時規避 + 目標引導」的合成場。

等效寫法（對數空間加法，數值穩定）：

```
log H_k(v)  =  log φ_g(v) + Σ_{i=1}^{k} log(1 − φ_{ei}(v))
```

### 演算法 HF（Hedge Field Computation）

```
Input:  圖 G，目標 g，起點 s，威脅集合 E = {e₁,...,eₖ}
Output: H : V → [0, 1]

1. φ_g ← GraphLaplacianSOR(G, source=g, sink=s)
2. for i = 1 to k:
   φ_{ei} ← GraphLaplacianSOR(G, source=eᵢ, sink=boundary)
3. H(v) ← φ_g(v) · ∏ᵢ (1 − φ_{ei}(v))   for all v
4. return H
```

**複雜度**：k+1 次 SOR 求解，O((k+1)·N) with Multigrid

---

## 4. 崁套對沖場（Nested Hedge Field）

### 4.1 問題

單層對沖 H₁ = φ_g · (1-φ_e) 假設「目標場」和「威脅場」是同等尺度的全局計算。

崁套的需求：**階層式目標**，或**對沖本身作為新的輸入再被對沖**。

### 4.2 兩種崁套模式

**模式 A：加權乘積崁套（Weighted Product Nesting）**

不同場給予不同權重 α, β：

```
N(v)  =  φ_g(v)^α · ∏ᵢ (1 − φ_{ei}(v))^βᵢ
```

- α → ∞：純目標導向（忽略威脅）
- βᵢ → ∞：絕對避開威脅 i
- α = βᵢ = 1：均衡模式

梯度：

```
∇ log N(v)  =  α · ∇ log φ_g(v)  −  Σᵢ βᵢ · ∇ log(1 − φ_{ei}(v))
```

這是一個有理論保證的梯度場，α / βᵢ 的比值直接控制「目標vs安全」的取捨。

**模式 B：場遞推崁套（Recursive Nesting）**

將前一層對沖 Hₙ 作為下一層的「虛擬威脅場」輸入：

```
H₁(v)  =  φ_g(v) · (1 − φ_{e1}(v))
H₂(v)  =  H₁(v) · (1 − φ_{e2}(v))         # 等於加入第二威脅
H₃(v)  =  H₂(v) · (1 − H_opponent(v))      # 對手的對沖場作為威脅
```

第三行是最有趣的情況：**代理人 A 規避的不只是位置，而是代理人 B 的「優勢場」本身**。

若 B 的對沖場 H_B = φ_B_goal · (1 - φ_A)，則：

```
H₃_A(v)  =  H_A(v) · (1 − H_B(v))
```

這是兩個對沖場的張力：A 最大化自身對沖場，同時壓制 B 的對沖場。

### 4.3 博弈解釋

定義雙方對沖張力（Dual-Hedge Tension）：

```
DT(v)  =  H_A(v) − H_B(v)
```

DT > 0：v 對 A 更有利（A 更接近目標且更安全）

DT < 0：v 對 B 更有利

DT = 0：博弈中立線（spatial Nash frontier of the hedge game）

A 沿 ∇DT 移動 → 最優進攻策略（增大自身優勢）

B 沿 −∇DT 移動 → 最優防守策略（消除 A 的優勢）

---

## 5. 路徑提取：φ-BFS on Combined Field

所有複合場（T、H、N、DT）均可直接套用 φ-BFS：

### 演算法 φ-BFS-H（Hedge Field Path Extraction）

```
Input:  複合場 F（可為 H、N、T、DT），起點 s，目標 g，圖 G
Output: 路徑 Path(s → g)

1. 初始化：open = {s}，parent[s] = ∅，visited = {s}
2. while open ≠ ∅:
   a. v ← argmax_{u ∈ open} F(u)    # 取 F 值最高的節點
   b. if v = g: break
   c. for each unvisited passable neighbor w of v:
      visited.add(w), parent[w] = v, open.add(w)
3. 沿 parent 從 g 回溯至 s，輸出路徑
```

**注意**：H 場不保證無內部極值（非調和函數），故 φ-BFS 在最壞情況下展開節點數 > O(P)。但作為啟發式路徑規劃，φ-BFS 依然完備（connected 圖上保證找到路徑）。

---

## 6. 局部場：即時 AI 視覺判斷

### 6.1 動機

全局場計算代價 O(N)。若環境巨大，預計算困難。

解法：**局部 Graph Laplacian 場**，以 AI 當前位置為中心，半徑 r 格內計算。

### 演算法 LF（Local Field for Real-time AI）

```
Input:  AI 位置 p，偵測半徑 r，局部子圖 G_r（p 周圍 r 格）
Output: 局部場 φ_local

1. 擷取子圖：G_r = subgraph of G within BFS-distance r from p
2. φ_local ← GraphLaplacianSOR(G_r, source=p, sink=boundary_of_G_r)
3. return φ_local
```

φ_local(v) 高 → v 在視覺/連通意義上對 AI 透明
φ_local(v) 低 → v 在陰影中（AI 難以察覺）

**應用（潛行遊戲）**：

玩家在 AI 局部場中沿 −∇φ_local 移動 = 最大速度進入陰影

多個 AI 時：Φ_threat = max_i φ_{local,i}（最危險的 AI 局部場取 max）

---

## 7. 複雜度總表

| 框架 | 場計算次數 | 複雜度（Multigrid） | 路徑提取 |
|------|-----------|-------------------|---------|
| 單場 GL | 1 | O(N) | O(P) |
| 張力場 TF | 1 | O(N) | O(P) |
| 對沖場 HF（k 威脅） | k+1 | O((k+1)N) | O(P*) |
| 局部場 LF（半徑 r） | 1/frame | O(r²) | O(r) |
| 雙對沖張力 DT | 2(k+1) | O(2(k+1)N) | O(P*) |

P = 最優路徑長度
P* = 對沖路徑長度（≥ P，因路徑迴避威脅可能更長）

---

## 8. 應用域摘要

| 應用 | 使用場 | 策略 |
|------|--------|------|
| 最短路徑 | φ_goal（單場） | φ-BFS 沿 ∇φ |
| 追逐最優路徑 | T = 2φ_A − 1 | 沿 ∇T |
| 逃跑最優路徑 | T | 沿 −∇T |
| 潛行導航（1 敵） | H = φ_goal·(1−φ_enemy) | φ-BFS 沿 ∇H |
| 潛行導航（k 敵） | H_k = φ_goal·∏(1−φᵢ) | φ-BFS 沿 ∇H_k |
| 即時敵 AI 視野 | 局部 φ_local | 玩家沿 −∇φ_local |
| 雙方最優對抗 | DT = H_A − H_B | A沿∇DT，B沿−∇DT |
| 高維構形空間導航 | 任意場（Multigrid） | φ-BFS |

---

## 9. 開放問題

1. **H 場的局部極值**：H = φ_goal · ∏(1-φᵢ) 何時無局部極值？充分條件？

2. **DT 的 Nash 均衡存在性**：雙方均採最優梯度策略時，DT 的鞍點是否存在？何時唯一？

3. **動態威脅的增量更新**：敵人移動時，場如何以 O(Δ) 增量更新而非 O(N) 全局重算？

4. **場加法 vs 場乘法**：H_add = φ_g − λ·φ_e 與 H_mult = φ_g·(1−φ_e) 的路徑品質差異？λ 的最優值？

5. **崁套深度的收益遞減**：k 個威脅場的乘積在 k→∞ 時退化為純目標場（因 ∏(1-φᵢ) → 0）。最優 k 的選取原則？

---

*EveMissLab EML-STM-2026-v0.1 — Working Framework, not peer-reviewed*
