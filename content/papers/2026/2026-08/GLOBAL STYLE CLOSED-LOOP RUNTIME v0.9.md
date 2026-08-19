# GLOBAL STYLE CLOSED-LOOP RUNTIME v0.9

## 1. 本版完成什麼

v0.9 首次把前面的資料與控制邏輯串成一個真正可跑的 Python 原型：

```text
Natural-language Query
        ↓
Style Kernel Searcher (v0.3 logic)
        ↓
Prompt Compiler / GAR Binding (v0.4 logic)
        ↓
Unified Runtime Packet (v0.5 / v0.6 logic)
        ↓
Mock Generation Backend
        ↓
Metric Vector / Gates (v0.7 logic)
        ↓
Adaptive Controller (v0.8 logic)
        ↓
RESAMPLE / RECOMPILE / REBIND / REPAIR / ACCEPT
        ↓
下一輪
```

公式上：

$$
q \rightarrow s \rightarrow c \rightarrow p \rightarrow a \rightarrow m \rightarrow d \rightarrow p'
$$

這已經是第一個真正的 **closed-loop runtime prototype**。

---

## 2. 為什麼先用 Mock Backend

v0.9 的目的不是假裝已接好任意影像引擎，而是先驗證：

- 搜尋
- 編譯
- 封包
- 評分
- 診斷
- 自動修正

這條控制鏈本身可以工作。

因此 `MockBackend` 不生成圖片，只生成 deterministic mock artifact 與 synthetic metric vector。

真正接 ComfyUI / Diffusers 時，只需要替換 backend 與 verifier provider，不必重寫整個控制器。

---

## 3. 目前的 Runtime Actions

```text
ACCEPT
RESAMPLE
RECOMPILE
REBIND
REPAIR
SWITCH_BACKEND
STOP
```

### RESAMPLE
增加 diversity、降低 named-style weight。

### RECOMPILE
增加明確語意／構圖約束。

### REBIND
切換 model profile / adapter strategy。

### REPAIR
增加 quality pass。

---

## 4. ComfyUI 邊界

v0.9 輸出的是：

```text
ComfyUI API Workflow Patch Plan
```

而不是自稱完整工作流。

原因是實際 `/prompt` 所需 workflow 必須是使用者環境裡真實存在、可驗證的 API-format node graph。

因此 v0.9 的 exporter 輸出：

- `template_id`
- model patch
- positive prompt patch
- negative prompt patch
- style weight patch
- diversity patch

下一步只要把 `workflow://user/replace-me` 綁到真實 API-format template 即可。

---

## 5. Diffusers 邊界

Diffusers exporter 目前輸出：

```text
model profile
prompt
negative prompt
steps
guidance scale
adapter policy
named-style weight
```

它是 pipeline config，不在 v0.9 中直接載入大型模型。

---

## 6. 目錄

```text
style-closed-loop-runtime-v0.9/
├── style_runtime/
│   ├── searcher.py
│   ├── compiler.py
│   ├── packet.py
│   ├── backends.py
│   ├── verifier.py
│   ├── controller.py
│   ├── runtime.py
│   └── cli.py
├── data/
├── tests/
├── examples/
├── run_demo.py
└── GLOBAL_STYLE_CLOSED_LOOP_RUNTIME_v0.9.md
```

---

## 7. 執行方式

在解壓縮目錄內：

```bash
python -m style_runtime "低飽和、空氣感、偏日式、不要太網紅臉" --output result.json
```

或者：

```bash
python run_demo.py
```

測試：

```bash
python -m unittest discover -s tests -v
```

這一版只使用 Python 標準庫。

---

## 8. 成功條件

v0.9 的成功不是「畫出最漂亮的一張圖」，而是：

1. Query 可被搜尋器解析。
2. 可選出 Style Kernel。
3. 可編譯 Prompt / GAR model profile。
4. 可生成統一 Runtime Packet。
5. Verifier 可回傳 `P/Q/A/S/D/H/C/R`。
6. Controller 可以選擇修正 Action。
7. 修正能改變下一輪狀態。
8. 最終可收斂到 `ACCEPT` 或有界停止。
9. 可輸出 ComfyUI patch plan 與 Diffusers config。

---

## 9. v1.0 前最後幾步

v0.9 後面不需要再無限拆規格。

最自然的是：

### v0.10
接一個真正 ComfyUI API-format workflow template。

### v0.11
接一個真 verifier provider 或人工評分輸入。

### v1.0
形成第一個真正：

```text
Query
→ Search
→ Compile
→ Generate
→ Verify
→ Refine
→ Final Image
```

的 AI Art Direction Runtime。
