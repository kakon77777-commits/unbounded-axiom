# GLOBAL STYLE PROMPT COMPILER + GAR BINDING v0.4

## 1. 這一版在做什麼

如果說：

- v0.1 是 **畫風地圖**
- v0.2 是 **風格組合器**
- v0.3 是 **Style Kernel Searcher**

那麼 v0.4 就是：

> **把查詢結果編譯成真正可執行的 prompt recipe 與 GAR binding。**

也就是把流程推到：

$$
\text{Intent} \to \text{Search} \to \text{Compile} \to \text{Bind} \to \text{Generate}
$$

---

## 2. 核心輸出

本版產出：

1. `prompt_compiler_schema.json`
2. `gar_binding_schema.json`
3. `compiled_prompt_examples.json`
4. `compiled_prompt_index.csv`
5. `model_profile_matrix.csv`
6. `ANTI_HOMOGENIZATION_RULES_v0.4.md`
7. 本說明文件

---

## 3. Prompt Compiler 的角色

Prompt Compiler 不再只把查詢翻成一句 prompt，而是產生四層：

### Layer A：Neutral Feature Recipe
以中性特徵語言表示風格核心，而非直接鎖定作者名。

### Layer B：Positive Prompt
輸出可直接餵給模型的正向 prompt（中英文）。

### Layer C：Negative Prompt / Anti-Homogenization
避免 generic AI 臉、構圖模板化、材質邏輯錯亂與過度商業化同質感。

### Layer D：GAR Binding
綁定：
- model profile
- adapter strategy
- reference policy
- control profile
- negative profile

---

## 4. GAR Binding 的角色

GAR 在這裡不只是 registry，而是 style runtime binding layer：

$$
B = (M, A, R, C, N)
$$

其中：
- $M$：Model profile
- $A$：Adapter strategy
- $R$：Reference policy
- $C$：Control profile
- $N$：Negative / anti-homogenization profile

---

## 5. Model Profile Matrix

本版建立 6 個初始模型配置：

- `mdl://anime-sdxl-stylized`
- `mdl://illustration-graphic-sdxl`
- `mdl://flux-painterly-fantasy`
- `mdl://flux-industrial-concept`
- `mdl://flux-semi-real-character`
- `mdl://general-sdxl-hybrid`

用途不是鎖死模型，而是提供：

```text
style kernel -> model family suggestion
```

---

## 6. 編譯原則

### 6.1 作者名退居索引層
作者名只作為導航索引，不作為最終唯一風格指令。

### 6.2 先特徵，後 adapter
先確定：
- 線條
- 色彩
- 密度
- 體積感
- 工業度
- 明暗
- 寫實度
- 動態性

再決定 LoRA / adapter。

### 6.3 限制命名風格綁定權重
建議：

$$
0 \leq w_{named\_style} \leq 0.35
$$

避免直接把整個輸出壓扁成某個單一作者模板。

---

## 7. 這版的實際內容

本版已根據 v0.3 的 10 個示範查詢，輸出對應的：

- compiled prompt
- neutral feature recipe
- GAR binding
- model suggestion
- negative profile

也就是說，這版已經從「查詢結果」走到「可執行規格」。

---

## 8. 下一步建議 v0.5

最自然的下一步是：

> **v0.5 Prompt Compiler Runtime MVP**

也就是真的做一個最小執行原型：

1. 接收 query
2. 呼叫 v0.3 searcher
3. 呼叫 v0.4 compiler
4. 輸出：
   - final prompt package
   - gar binding package
   - model selection package
   - adapter recommendation package

甚至可以直接輸出成：
- ComfyUI workflow seed
- Diffusers config
- internal AADS task packet

---

## 9. 總結

v0.4 的關鍵，不是又多寫了一層文件，而是把整體推到這裡：

```text
使用者意圖
→ 風格搜尋
→ 風格編譯
→ 資產綁定
→ 可執行生成
```

這已經非常接近你真正要的那種：

> **AI 自己理解意圖，自己找風格域，自己約束生成，自己組出可執行方案。**
