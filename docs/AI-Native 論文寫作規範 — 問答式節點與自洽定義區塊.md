# AI-Native 論文寫作規範 — 問答式節點與自洽定義區塊

給 Neo 寫論文時對照用的規範文件。兩個慣例都是「內容形狀觸發」（opt-in by
content shape）：照格式寫，ingest pipeline 會自動偵測並產生對應的 schema.org
結構化資料；不照格式寫，就只是普通段落，不會出任何錯誤或警告，但也拿不到
額外的 AI/答案引擎信號。

跟 `/llms.txt`（見 `scripts/ai_layer.py` 的 `_llms_txt()`）是同一個目標的兩個
層次：llms.txt 解決「AI 怎麼找到這個網站的拓樸」，這份文件解決「AI 怎麼在單篇
論文內部，精準命中一個子問題或一個術語」。

## 慣例一・問答式 H2 節點（Answer-first Sub-query）

規則：`## ` 標題本身就是一個完整問句（以 `?` 或 `？` 結尾），緊接著的**第一段**
就是這個問題的直接答案（自洽、可獨立引用，不要用「如上所述」「見下文」這種
依賴上下文的寫法）。

```markdown
## Cl-3 守恆性如何判斷一個結構是否完成閉合？

Cl-3 守恆性透過檢查系統在拓撲轉換前後，特定不變量（如資訊熵、因果序）是否
維持恆定來判斷；與 Cl-4 生成性的雙重閉合，是 DCO 5.0 框架判定「一個結構已經
完成閉合」的核心判準。

（這裡開始可以接更長的推導、範例、延伸討論——這些不會被當成答案本體。）
```

抽取規則（見下方「自動化」）：答案 = 標題後第一個非空行到下一個空行/標題之間
的內容。太短會被 lint 標記為 `qa_answer_too_thin`（目前門檻：估算 < 8 tokens）
——代表那其實是一個開放式研究問題的小節標題，不是真的問答節點，兩者都可以
存在，只是後者不會被當成 FAQ 收錄。

## 慣例二・自洽定義區塊（Self-contained Definition Block）

規則：**單行**的 blockquote，格式固定為：

```markdown
> **定義｜{術語}**：{說明，自洽、獨立成段，控制在 ~200 token 以內}
```

英文版用 `**Definition｜{term}**:`。範例：

```markdown
> **定義｜Cl-3 守恆性**：Cl-3 守恆性是指系統在拓撲轉換過程中，特定不變量
> （如資訊熵、因果序）維持恆定的性質；與 Cl-4 生成性共同構成 DCO 5.0 框架
> 判斷一個結構是否完成閉合的雙重判準。
```

⚠️ 上面故意用兩行示範"看起來像"換行，但實際寫的時候必須是 markdown 原始碼裡
**不手動斷行的一整行**（`>` 開頭那一行一路寫到底，讓編輯器自動換行顯示即可）。
原因：目前的 renderer（Python `markdown` 套件 / 內建 fallback / Astro 端的
`marked`）對「連續多行 `>` 是否合併成同一個 blockquote」的行為不完全一致；
寫成單行可以在三種 renderer 下都保證被解析成同一個區塊，不會被切散。

自洽性的兩個機器可檢查條件：
1. **長度預算**：body 估算 token 數（CJK 字元算 1 token、其餘字元約 4 字算
   1 token）超過 220 會被 lint 標記 `definition_too_long`——這是「切成 200
   token 區塊還要完整」這個要求的量化版本。
2. **自我指涉**：body 裡必須重新出現一次 `{術語}` 本身（不能只用「這個概念」
   「此性質」這種代詞開頭），否則標記 `definition_not_self_restating`——
   否則區塊被單獨切出去餵給 AI 時，讀者不知道在講什麼。

## 自動化：ingest 時發生什麼事

兩邊 pipeline 各自獨立偵測（規則完全一致，避免其中一邊漏掉）：

- **Python 引擎**（`scripts/geo_layer.py`，由 `scripts/build.py` 呼叫）：
  - 對每篇 `.md` 來源論文的**原始 markdown 原文**（不是渲染後的 HTML）跑
    偵測，寫入 `registry/generated/geo-lint.json`（warn-only，不會擋 build，
    跟 `broken-links.json` 同一套模式)。
  - 同時把偵測到的訊號轉成 `FAQPage` / `DefinedTermSet` JSON-LD，注入純
    Python 引擎自己產生的 `/p/{id}/index.html`（`scripts/idroutes.py`）——
    這條路徑只在單獨跑 `python build.py`（不套 Astro）時看得到效果。
  - build 完會印一行 `[diag] geo: N md papers scanned | M with signals |
    K lint findings`。
- **Astro 殼層**（`shell/src/lib/geo.ts`，`shell/src/pages/p/[id].astro`
  呼叫）：**這才是正式站上線上看到的版本**——`build-site.sh` 第 2/3 步會用
  Astro 重新產生 `/p/{id}/`，蓋掉 Python 引擎產生的版本（機器 metadata 有
  保留，但 HTML/JSON-LD 是 Astro 那份說了算）。邏輯是同一套規則的 TypeScript
  版本，操作對象一樣是原始 markdown 原文。

換句話說：論文用 `.md` 格式、照上面兩個慣例寫，**存進 `content/papers/` 跑一次
`bash build-site.sh` 就會自動生效**，不需要額外手動步驟。跑完之後可以看
`registry/generated/geo-lint.json` 自我檢查有沒有寫得不夠自洽的區塊。

## 限制

- 只對 `.md` 來源的論文有效。`.docx`／`.ipynb`／`.pdf` 等格式在抽取原始文字
  時會失去 markdown 的標題/blockquote 語法（`scripts/render.py` 的
  `extract_raw_text()`），兩個慣例都偵測不到——如果要用這套自動化，新論文
  請直接寫成 `.md`。
- 這是「多寫一點結構」換「多一點機器信號」的自願慣例，不是強制規則；沒有
  問答式標題或定義區塊的論文完全不受影響，也不會出現在 lint 報告裡（因為
  根本沒有東西可以違規）。
