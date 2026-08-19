# GLOBAL STYLE RUNTIME MVP v0.5

## 1. 目標

v0.5 的目的，是把前面幾版正式收束成一個**可執行的最小運行流程**：

$$
Intent \to Search \to Compile \to Bind \to Package \to Generate
$$

也就是把：

- v0.1 畫風地圖
- v0.2 Style Combiner
- v0.3 Style Kernel Searcher
- v0.4 Prompt Compiler + GAR Binding

整合成一個真正能跑的 **Runtime MVP**。

---

## 2. Runtime MVP 的最小輸入／輸出

### 2.1 輸入

使用者輸入可以最小化為：

```json
{
  "query_text": "低飽和、空氣感、偏日式、不要太網紅臉",
  "target_medium": "illustration",
  "aspect_ratio": "3:4",
  "quality_preset": "high",
  "anti_homogenization_level": "high"
}
```

### 2.2 輸出

Runtime MVP 應輸出四種核心包：

1. `search_result`
2. `compiled_prompt_package`
3. `gar_binding_package`
4. `execution_packet`

最後形成：

$$
R = (S, C, G, E)
$$

其中：

- $S$：Search result
- $C$：Compiled prompt package
- $G$：GAR binding package
- $E$：Execution packet

---

## 3. 系統模組

Runtime MVP 建議拆成六個模組：

### Module A — Query Intake
接收自然語言意圖與基本參數。

### Module B — Style Kernel Searcher
呼叫 v0.3 搜尋器，找出：
- 最近畫師節點
- 最近 hybrid recipe
- 最近 path recipe

### Module C — Prompt Compiler
呼叫 v0.4 編譯器，輸出：
- neutral feature recipe
- positive prompt
- negative prompt
- model profile suggestion

### Module D — GAR Binder
將 prompt 與風格特徵綁到：
- model profile
- adapter strategy
- control profile
- reference policy
- negative profile

### Module E — Task Packet Assembler
產出下游執行包，例如：
- AADS task packet
- ComfyUI workflow seed
- Diffusers config

### Module F — Runner / Dispatcher
把封裝好的 packet 發往：
- 本地 ComfyUI
- Diffusers pipeline
- 內部 agent
- 其他 rendering backend

---

## 4. 最小資料流

```text
User Query
  ↓
Query Intake
  ↓
Style Kernel Searcher
  ↓
Prompt Compiler
  ↓
GAR Binder
  ↓
Task Packet Assembler
  ↓
Runner / Dispatcher
  ↓
Generation Backend
```

可形式化為：

$$
q \to f_s(q)=s \to f_c(s)=c \to f_g(c)=g \to f_e(g)=e
$$

---

## 5. AADS Task Packet

建議 AADS task packet 的最小結構為：

```json
{
  "task_id": "aads://task/0001",
  "query_text": "低飽和、空氣感、偏日式、不要太網紅臉",
  "search_result_id": "query://style-kernel/001",
  "compiled_prompt_id": "compile://style-prompt/001",
  "gar_binding_id": "gar://binding/001",
  "target_medium": "illustration",
  "aspect_ratio": "3:4",
  "backend": "comfyui",
  "priority": "normal"
}
```

---

## 6. ComfyUI Workflow Seed

Runtime MVP 不直接綁死某一份工作流，而是先輸出「seed schema」。

它至少包含：

- base model
- positive prompt
- negative prompt
- image size
- sampler preset
- adapter slots
- control slots
- seed

如此可避免因不同環境的 ComfyUI 節點不一致而失效。

---

## 7. Diffusers Config Template

Diffusers 版可最小輸出：

- model identifier
- prompt
- negative prompt
- num inference steps
- guidance scale
- width / height
- seed
- optional adapters

---

## 8. Anti-Homogenization 在 Runtime 中的位置

反同質化不應只存在於 prompt 字串，而應存在於三層：

### 8.1 Search 層
避免總是選出相同熱門節點。

### 8.2 Compile 層
避免 prompt 被壓縮成單一審美模板。

### 8.3 Binding 層
限制直接作者名風格權重：

$$
0 \leq w_{named\_style} \leq 0.35
$$

並優先使用：
- 分解式 adapter
- 中性 reference board
- composition / palette / material control

---

## 9. MVP 的成功條件

v0.5 不追求一次到位，而追求可驗證的最小成功條件：

1. 能輸入自然語言 query。
2. 能返回 search result。
3. 能返回 compiled prompt。
4. 能返回 GAR binding。
5. 能輸出 task packet。
6. 能被 ComfyUI / Diffusers / AADS 下游讀取。

---

## 10. 建議實作順序

### Phase 1
先實作純資料流：
- intake
- searcher bridge
- compiler bridge
- binder bridge
- packet assembler

### Phase 2
再做輸出器：
- ComfyUI seed exporter
- Diffusers config exporter
- AADS packet exporter

### Phase 3
最後接真正的 runner：
- local queue
- retry
- result logging
- lineage tracking

---

## 11. 後續 v0.6 方向

當 v0.5 打通後，v0.6 最自然的是：

- runtime benchmark
- style divergence metrics
- anti-homogenization scoring
- asset lineage registry
- automatic feedback loop

也就是：

$$
Generate \to Evaluate \to Refine \to Rebind
$$

---

## 12. 總結

v0.5 的本質不是再多一篇白皮書，而是把整個系統從：

```text
理論與規格
```

推到：

```text
可執行的最小運作結構
```

也就是你真正要的：

> AI 自己接收意圖，自己找風格域，自己編譯，自己綁定，自己輸出執行包。
