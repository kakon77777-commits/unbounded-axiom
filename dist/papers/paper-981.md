# EML-LQ-AGENT-2026
## 自適應帳本量化代理框架技術規格
*EveMissLab｜依賴：EML-LA-2026（帳本代數）・EML-LQ-2026-v0.1*

---

## 1. 定位

本文件是將 EML-LQ-2026 從靜態 Excel 原型轉換為自主運行代理（Agent）的完整技術規格。

**既有三個構件：**

| 構件 | 角色 | 代理中的位置 |
|---|---|---|
| `nanocsv_llm.py` | 字元級 Transformer，純 numpy，CSV 持久化 | 智能層佔位符／本地信號模型 |
| `ledger_experiment.py` | A2 守恆公理數值驗證場 | 引擎層約束邏輯的理論依據 |
| `build_xlsx.py` | EML-LQ-2026 Excel 具現化 | 引擎層公式語意的規範來源 |

**轉換的核心主張：** 三個構件的公式語意對資料來源透明。將合成價格矩陣替換為爬蟲輸出，代理即成立。本文件規格化這條替換路徑，並定義各層的介面契約。

---

## 2. 公理 → 代理設計映射

帳本代數五條公理直接決定代理的架構約束。任何實作若違反以下映射，即違反理論基底。

| 公理 | 陳述 | 代理層 | 實作形式 |
|---|---|---|---|
| A1 封閉 / Cl-1 | 帳本自洽，不引用外部 | 引擎層 | 資本只在 N 資產間重分配，不引入外部槓桿；單純形 Σwᵢ = 1 封閉 |
| A2 守恆 / Cl-3 | τ(W) = Σwᵢ ≡ 1 | 引擎層 | 每期乘法更新後強制正規化；每期 LOG 寫入 Σw 稽核欄 |
| A3 流 | 更新即資金在資產間流動 | 引擎層 | w_raw = w_prev · exp(η · r)；exp 決定流向與強度 |
| A4 邊界（開放性） | 邊界閥控制新資訊進入量 | 引擎層 | η(t) = η_base / (1 + λ·σ(t))；σ 高則帳本傾向封閉 |
| A5 層級 / Cl-4 生成 | 框架對 N 泛化，可持續擴張 | 全層 | 所有公式對任意 N 成立；新增資產只需擴展資料層 |

---

## 3. 系統架構

代理分三層，資料流單向向下：

```
┌─────────────────────────────────────────────────┐
│  資料層  Data Layer                              │
│  爬蟲 → OHLCV 清洗 → price matrix P (T×N)       │
└──────────────────┬──────────────────────────────┘
                   │ P(t), P(t-1)
┌──────────────────▼──────────────────────────────┐
│  引擎層  Engine Layer                            │
│  r(t) → σ(t) → η(t) → 乘法更新 → A2 守恆       │
│  輸出：W(t), η(t), τ 稽核                        │
└──────────────────┬──────────────────────────────┘
                   │ history, r(t)
┌──────────────────▼──────────────────────────────┐
│  智能層  Intelligence Layer                      │
│  本地 nanocsv_llm 或外部 LLM API                 │
│  輸出：信號修飾子 δ，回注引擎層的 η              │
└─────────────────────────────────────────────────┘
```

### 3.1 資料層

**職責：** 將任意資料源轉換為引擎層可消費的 clean price matrix。

**輸入源（可擇一實作）：**
- Yahoo Finance API（`yfinance`）
- TWSE / TPEX 官方 API
- 自定義 CSV 後端（與現有合成資料格式相容）
- 任何實作 `CrawlerInterface` 的爬蟲

**清洗協議（必須執行）：**
1. 停牌日補值：前向填充（forward-fill），不得插值
2. 除權除息：使用還原股價（adjusted close）
3. 異常值：單期報酬絕對值 > 20% 觸發人工確認旗標，不自動過濾
4. 缺值：超過連續 3 期缺值的資產，從當期 N 中暫時移除並重新正規化

**輸出格式：**
```python
P: np.ndarray  # shape (T, N), dtype=float64
               # P[t, j] = 第 t 期第 j 個資產的收盤價
               # T >= 2（最少需要一期報酬）
               # N >= 1
```

### 3.2 引擎層

**職責：** 執行帳本更新迴圈，維護 A2 守恆。

引擎層的完整邏輯已在 `build_xlsx.py` 的工作表 03–05 中以 Excel 公式規格化。以下為等價 Python 語意：

```python
# 報酬計算（對應 03_報酬）
r_t = P[t] / P[t-1] - 1                           # shape (N,)
r_market = r_t.mean()                              # 市場等權報酬

# 波動計算（對應 04_開放閥）
σ_t = std(market_return_history[-window:])         # 滾動標準差

# 開放閥（A4）
η_t = η_base / (1 + λ * σ_t)                      # 由智能層δ修飾：η_t *= δ

# 乘法更新（A3 流）
w_raw = W_prev * np.exp(η_t * r_t)                # shape (N,)

# A2 守恆投影
W_new = w_raw / w_raw.sum()                        # Σw = 1.000，tolerance 1e-10

# 稽核
assert abs(W_new.sum() - 1.0) < 1e-10             # C1 可驗證點
```

**不變式：** 引擎層在任何情況下不得繞過 A2 守恆投影。若 `w_raw.sum()` 接近零（極端崩潰情境），拋出 `LedgerCollapseError` 而非靜默修正。

### 3.3 智能層

**職責：** 從市場歷史與當期信號中生成 η 修飾子 δ，注入引擎層。

智能層是**可選模組**。若未部署，δ = 1.0（不修飾）。

**兩種實作路徑：**

**路徑 A：本地 nanocsv_llm（現況為 POC）**
```python
# 將報酬序列編碼為字元流，送入 nanocsv_llm 生成
signal_text = encode_returns_as_chars(r_history)   # 自定義編碼
generated = generate(model, stoi, itos, signal_text, n=8, temp=0.3)
δ = decode_signal(generated)                       # 解碼為 float
```
*誠實標記：現有 nanocsv_llm（D=24，8543 權重）容量不足以做有意義 NLP。此路徑目前是架構佔位符，適合驗證介面正確性。*

**路徑 B：外部 LLM API（生產建議）**
```python
prompt = format_signal_prompt(r_history, W_prev, σ_t)
response = llm_api_call(prompt)                    # 任何 LLM 端點
δ = parse_delta(response)                          # 解析為 float，限制在 [0.5, 2.0]
```

**δ 的語意：**
- δ > 1.0：放大開放度（AI 判斷當前趨勢清晰，加速跟隨）
- δ < 1.0：收縮開放度（AI 判斷當前信號嘈雜，保守守恆）
- δ = 1.0：不干預

**安全約束：** δ 必須強制 clip 至 [0.1, 5.0]，防止智能層癱瘓引擎層守恆性。

---

## 4. 代理迴圈

```
INIT / RESUME:
  IF manifest.exists("weights/manifest.csv"):
    state    ← load_csv("weights/state_latest.csv")
    W        ← state.W
    t_start  ← manifest.last_period + 1
    IF manifest.params_hash ≠ sha256(η_base, λ, window, sorted(assets)):
      WARN "參數已變更，從 t={t_start} 起以新參數繼續，寫入升版記錄"
    IF manifest.data_source ≠ crawler.source_id:
      WARN "資料源切換，歷史連續性需人工確認"
  ELSE:
    W        ← [1/N, ..., 1/N]     # 等權起始，A1 封閉
    t_start  ← 1
    manifest.create(framework_version, params_hash, crawler.source_id)
  history ← load_log("weights/log/")    # 載入歷史 LogRecord（可為空）
  model   ← load_csv("weights/")        # nanocsv_llm 若使用路徑 A

LOOP (每期 t = t_start, t_start+1, ...):

  ── FETCH ──────────────────────────────────────────
  P_t  ← crawler.get_prices(assets, date=t)
  validate(P_t)                      # 清洗協議 §3.1

  ── TRANSFORM ──────────────────────────────────────
  r_t  ← P_t / P_{t-1} - 1
  σ_t  ← rolling_std(history.market_returns, window)

  ── DECIDE (optional) ──────────────────────────────
  δ    ← intelligence_layer(history, r_t)   # 若未部署：δ = 1.0

  ── ADAPT ──────────────────────────────────────────
  η_t  ← (η_base / (1 + λ·σ_t)) * δ        # A4 開放閥

  ── UPDATE ─────────────────────────────────────────
  w_raw ← W * exp(η_t * r_t)               # A3 流

  ── CONSERVE ───────────────────────────────────────
  W    ← w_raw / sum(w_raw)                # A2 守恆

  ── LOG ────────────────────────────────────────────
  record ← {
    timestamp:            utcnow(),              # UTC 執行時間 [C6]
    period:               t,
    framework_version:    FRAMEWORK_VERSION,     # "EML-LQ-AGENT-2026-v0.1" [C7]
    params_hash:          sha256(η_base, λ, window, sorted(assets)),  # [C7]
    intelligence_version: llm_model_string,      # 路徑 B: LLM model ID；路徑 A: "nanocsv_llm-local"
    data_source:          crawler.source_id,
    data_fetched_at:      crawler.last_fetch_time,
    data_valid_until:     crawler.cache_expiry,  # 逾期觸發強制重新抓取
    assets:               assets,               # 本期實際 N（動態變化時記錄差異）
    W, r_t, η_t, σ_t, δ,
    τ_check:              sum(W)               # A2 稽核，應 ≡ 1.000
  }
  history.append(record)
  save_csv(log=record,  "weights/log/log_{timestamp}.csv")  # 每期一份，不覆寫
  save_csv(state=W,     "weights/state_{timestamp}.csv")    # 不可變快照
  save_csv(state=W,     "weights/state_latest.csv")         # 覆寫最新 [C3]
  manifest.update(t, record.timestamp, record.params_hash, record.data_source)

END LOOP
```

---

## 5. 模組介面規格

完整型別定義，用於任何語言實作的對接基準。

```python
class CrawlerInterface:
    def get_prices(
        assets:   List[str],
        date:     datetime,
        lookback: int = 1
    ) -> np.ndarray:              # shape (lookback, N), float64
        ...

class LedgerEngine:
    def step(
        P_prev:   np.ndarray,     # shape (N,), 前期價格
        P_curr:   np.ndarray,     # shape (N,), 當期價格
        W_prev:   np.ndarray,     # shape (N,), 前期權重，sum = 1
        η_base:   float,          # 開放閥基準
        λ:        float,          # 波動敏感度
        σ_t:      float,          # 當期市場波動
        δ:        float = 1.0     # 智能層修飾子
    ) -> Tuple[np.ndarray, float, float]:
        # 返回 (W_new, η_t, τ_check)
        # 不變式：abs(W_new.sum() - 1.0) < 1e-10
        ...

class IntelligenceLayer:
    def signal(
        history:  List[dict],     # 歷史 LOG 記錄
        r_t:      np.ndarray      # shape (N,), 當期報酬
    ) -> float:                   # δ，強制 clip [0.1, 5.0]
        ...

class PersistenceLayer:
    def save(state: dict, path: str) -> None: ...
    def load(path: str) -> dict: ...
    # 保證：save → load → 引擎輸出位元級一致 [C3]
```

### 5.1 持久化狀態規格

```python
# Manifest（版本清單）：weights/manifest.csv
# 每期覆寫更新，單一檔案，記錄代理的全域狀態
ManifestSchema = {
    "framework_version":  str,       # "EML-LQ-AGENT-2026-v0.1"
    "created_at":         datetime,  # 代理首次啟動的 UTC 時間
    "last_updated_at":    datetime,  # 最近一次 LOG 寫入的 UTC 時間
    "last_period":        int,       # 最近完成的帳本期數 t
    "params_hash":        str,       # sha256(η_base, λ, window, N, sorted(assets))
    "data_source":        str,       # 最近使用的資料源 ID
    "last_data_fetched":  datetime,  # 最近資料抓取時間
    "snapshot_latest":    str,       # 最新快照的完整檔名
}

# LogRecord（每期一份，永不覆寫）：weights/log/log_{timestamp}.csv
# 完整的稽核軌跡；路徑 B 的 LLM 以最近 K 筆作為 context memory
LogRecord = {
    "timestamp":             datetime,    # UTC，本期引擎執行時間 [C6]
    "period":                int,         # 帳本內部期數 t
    "framework_version":     str,         # [C7]
    "params_hash":           str,         # 跨期一致則無參數漂移 [C7]
    "intelligence_version":  str,         # 路徑 B: LLM model ID；路徑 A: "nanocsv_llm-local"
    "data_source":           str,         # 資料源 ID
    "data_fetched_at":       datetime,    # 資料實際抓取時間
    "data_valid_until":      datetime,    # 快取有效期，逾期強制重新抓取
    "assets":                List[str],   # 本期實際資產列表（N 可動態變化）
    "W":                     List[float], # 本期帳本權重
    "r_t":                   List[float], # 本期各資產報酬
    "η_t":                   float,
    "σ_t":                   float,
    "δ":                     float,
    "τ_check":               float,       # Σw，應 ≡ 1.000 [C1]
}

# 目錄結構
# weights/
#   manifest.csv                      ← 版本清單，每期覆寫更新
#   state_latest.csv                  ← 最新 W 快照，每期覆寫
#   state_{timestamp}.csv             ← 帶時間戳的不可變快照
#   log/
#     log_{timestamp}.csv             ← 每期一份，永不覆寫
```

**路徑 B 的連續性機制：** 每次 LLM call 時，從 `weights/log/` 載入最近 K 筆 LogRecord 作為 context，LLM 藉此感知歷史狀態、參數版本、資料源切換等事件，實現跨期連續判斷。K 受 LLM context window 限制，建議 K = 20–50。

---

## 6. 擴展協議

### 6.1 新增資產（擴展 N）
1. `CrawlerInterface`：加入新 ticker
2. 引擎層：N 自動感知，公式語意不變（A5）
3. 初始化：若代理已運行，插入新資產時 W 重新正規化，歷史 W 補零

### 6.2 替換資料源
實作 `CrawlerInterface` 協議即可。引擎層對資料源透明，清洗協議（§3.1）仍須執行。

### 6.3 升級 AI 組件
- nanocsv_llm → 外部 LLM：實作 `IntelligenceLayer` 的路徑 B
- δ 的語意契約不變，引擎層無需修改
- 升級不影響 A2 守恆性（守恆在引擎層，與智能層隔離）

### 6.4 從 Excel 原型遷移
`build_xlsx.py` 已完整定義引擎層語意。遷移路徑：
1. `02_價格` → 爬蟲輸出的 P matrix
2. `03_報酬` → `LedgerEngine.step()` 內部計算
3. `04_開放閥` → `LedgerEngine.step()` 內部計算
4. `05_帳本權重` → `LedgerEngine.step()` 輸出
5. `06_淨值` → LOG 後處理

---

## 7. 可驗證點

延續 `nanocsv_llm.py` README 風格的 True/False/Error 格式。

| 編號 | 名稱 | 驗證方式 | 通過條件 |
|---|---|---|---|
| C1 | A2 守恆 | 每期 `assert abs(W.sum() - 1.0) < 1e-10` | 全部期數 True |
| C2 | η-σ 反向 | `corr(η_history, σ_history) < 0` | 相關係數 < -0.9 |
| C3 | 持久性 | `save → load → engine.step()` 輸出比對 | 位元級一致 |
| C4 | δ 安全邊界 | 全期 `δ ∈ [0.1, 5.0]` | 無一越界 |
| C5 | 帳本崩潰保護 | 極端情境注入（所有 r_t = -0.99） | 拋出 `LedgerCollapseError`，不靜默 |
| C6 | 時間戳單調性 | `log[t].timestamp > log[t-1].timestamp` 全期成立 | 全部 True；亂序寫入即 Error |
| C7 | 參數一致性 | 跨期 `params_hash` 對比 manifest | 一致；不一致時 manifest 需存在明確升版時間戳 |

---

## 8. 誠實標記

**演算法歸屬：** 乘法更新屬 exponentiated gradient（EG）族，Cover & Ordenthal 1996 的 universal portfolio 脈絡。非新演算法。

**本框架新意：**
1. 帳本代數（EML-LA A1-A5）作為代理的自適應控制層——公理直接決定架構約束
2. τ(W) = Σwᵢ ≡ 1 守恆作為可視稽核，不只是正規化步驟
3. 三層介面分離：資料源替換、AI 組件升級、引擎邏輯不互相污染

**當前限制：**
- `nanocsv_llm`（D=24，8543 權重，23 字元詞表）容量不足以做有意義 NLP；智能層目前是架構佔位符
- 乘法更新在極端波動下可能使某些資產權重趨近零，需監控 `W.min()` 設定下限閾值
- 資料清洗協議（§3.1）目前為規格，尚無實作；實際部署前需驗證

**資料說明：** `build_xlsx.py` 使用合成資料（含一次 t=30 regime 切換）。代理使用前須替換為實際市場資料並重新驗證 C1-C5。

---

## 9. 分散式自適應帳本量化代理架構（D-ALAN）

*本節為理論前瞻，描述 EML-LQ-AGENT-2026 的長期演化目標，而非當前實作規格。*

### 9.1 核心主張

單節點代理的根本限制是認識論上的：任何單一資料源和單一模型都是世界的局部投影。EML-LQ-AGENT 的 A4 開放閥和 A5 可擴張性在邏輯上指向同一個結論——這個框架的自然擴張不是把單節點做大，而是把它複製成網路，讓節點之間的張力本身成為資訊來源。

開源是這個架構的前提，不是附加品。多樣性需要獨立實作；獨立實作需要開放規格。封閉的分散式系統只是分散的單點故障。

### 9.2 分散式節點架構

網路由 M 個獨立節點組成，每個節點是一個完整的 EML-LQ-AGENT 實例，但具備以下差異性要求：

```
節點 i 的差異性要求：
  data_source_i  ≠ data_source_j   （資料來源獨立）
  model_i        ≠ model_j          （AI 組件型別獨立）
  η_base_i, λ_i  可不同              （參數空間探索）
  assets_i ⊇ assets_core            （核心資產集共享，邊緣可各自擴展）
```

節點間共享的是**結構**（帳本代數公理 A1-A5）而非**狀態**。每個節點獨立維護自己的 manifest + LogRecord，不存在全局一致性要求——分歧本身是信號。

跨節點比對週期性執行：

```
CROSS_VALIDATE（每 K 期）：
  收集所有節點的 W_i（當前帳本權重向量）
  計算節點間距離矩陣 D[i,j] = ||W_i - W_j||_1
  IF D[i,j] > threshold:
    標記（i, j）為高分歧對，觸發資料品質調查
  節點共識估計：W_consensus = weighted_mean(W_i)，權重由歷史準確度決定
```

### 9.3 生成對抗數據機制

這裡的 GAN 類比需要一個修正：金融市場中不存在獨立於共識之外的「真實價格」——價格本身就是共識的具現。因此，這個機制追求的不是發現預存的真相，而是**構造更可靠的共識估計**，這在認識論上是不同的任務。

機制：

```
生成器（Generators）：各節點的資料來源，各自產生價格序列 P_i(t)
判別器（Discriminators）：跨節點比對邏輯，識別異常節點

對抗壓力：
  IF node_i 的 P_i 持續與多數節點分歧：
    node_i 的 W_i 被下調在 W_consensus 中的權重
    觸發 node_i 重新審查 data_source_i 的可信度

收斂條件：
  各節點的 W_i 在統計意義上趨近，波動幅度受 σ_consensus 描述
  不要求完全一致——殘差分歧是市場不確定性的自然反映
```

隨著對抗輪次累積，系統性偏差的資料源會被邊緣化，多源交叉驗證的殘差成為數據品質的隱式指標。這是對 A4 開放性的網路級詮釋：節點網路作為整體的「開放閥」，由節點間張力控制。

### 9.4 因果 AI 自主層

當前代理的 AI 組件是反應式的：觀察 r_t，輸出 δ。這對應因果推理的最低層——統計關聯。

演化路徑分三個階段：

**階段一（當前）：關聯反應**
AI 辨認模式（r_t 的統計特徵），輸出 δ 修飾 η。資料來源被動接受，FETCH 是盲目的。

**階段二：因果模型**
AI 建立顯式因果圖（X → Y，而非 corr(X,Y)）。DECIDE 步驟從輸出單一 δ，變為輸出對不同資產的差異化 δ_j，基於「哪個變數因果驅動哪個資產」的判斷。資料仍然被動抓取，但處理是因果感知的。

**階段三：主動驗證與自主統籌**
AI 具備主動性後，FETCH 步驟發生質變：

```
FETCH（因果AI版本）：
  AI 根據當前因果模型提出假設 H：
    "如果 X 是驅動因，則 source_A 的數據應比 source_B 更早反映 Y"
  主動查詢多個來源，設計驗證 H 的抓取策略
  比對結果，更新因果圖
  IF 數據與 H 矛盾：重新評估 source 可信度，非靜默接受
```

這個階段的 AI 不再是引擎的修飾器，而是整個 FETCH-TRANSFORM-DECIDE 迴圈的統籌者。人的角色從操作層退到架構層：設定公理約束（A1-A5）、定義哪些是不可違反的邊界，而不再介入每期決策。

### 9.5 演化路徑

```
MVP（現在）
  單節點、合成資料、nanocsv_llm 佔位
  → 驗證帳本代數公理在可執行系統中的一致性

v1.0（開源 + 真實資料）
  單節點、真實爬蟲、路徑 B LLM
  → 驗證 C1-C7 在生產環境成立

v2.0（多節點網路）
  M 個獨立節點、CROSS_VALIDATE 機制上線
  → 對抗數據機制開始累積有效樣本

v3.0（因果AI統籌）
  階段三主動驗證、節點共識驅動 W_consensus
  → 系統具備自主識別數據品質的能力

終態（D-ALAN）
  開放節點網路、因果AI自主統籌、人退出操作層
  → 帳本代數作為不可違反的架構基底，其餘由網路動態演化
```

---
*EveMissLab EML-LQ-AGENT-2026 / 依賴 EML-LA-2026-v0.1*
