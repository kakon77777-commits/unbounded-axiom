# 最小語意載荷競賽：從 Code Golf 到 EML Intent Golf 的新型程式設計賽制

**版本**：v0.2 草案（新增桌上模擬賽附錄與規則補強建議）  
**作者**：Neo.K / EVEMISSLAB 協作草案  
**文件類型**：技術白皮書 / 賽制設計文件 / EML 應用延伸  
**建議狀態**：可作為未來公開賽制、GitHub 專案、Logic Matrix 文章或 EML 實驗任務規格之基礎版本  
**v0.2 更新**：補入 IC-0001 桌上模擬賽，並根據模擬結果新增行數/bytes 雙計、危險原語懲罰、EML macro/prelude 揭露、LLM/Agent 賽道隔離與世界耦合 trace 要求。  

---

## 摘要

本文提出一種新的程式設計競賽框架：**最小語意載荷競賽**（Minimal Semantic Payload Challenge），又可稱為 **Intent Golf**、**Semantic Golf** 或 **EML Minimal Intent Challenge**。它繼承傳統 Code Golf「以最短程式碼完成任務」的精神，但不再將勝負單純建立在字元數、行數或語言奇技淫巧之上，而是改以「用最少有效資訊載荷完成可驗證意圖」作為核心目標。

在生成式 AI、Agent、自動化工具鏈與高階語意語言逐漸成熟的時代，程式碼的意義正在變化。過去的程式碼主要是人類對機器的逐步指令；現在的程式碼則可能是人類、AI、編譯器、轉譯器、執行環境、外部 API、資料庫、感測器與物理裝置共同完成意圖的界面。因此，新的競賽不應只問：「誰能用最少字元印出答案？」而應進一步追問：「誰能用最小語意載荷，讓整個計算系統穩定、可驗證、可重現地完成目標？」

本文主張，未來程式競賽可以從「演算法競賽」、「短碼競賽」、「混淆程式競賽」擴展到「意圖效率競賽」。其評分核心不是單一長度，而是多因素綜合：程式碼長度、行數、位元數、依賴成本、語言啟動成本、外部服務成本、模型呼叫成本、可重現性、任務完成度、世界耦合深度與主體邏輯是否被不當外包。

EML（EveMiss Language / EVEMISSLAB Minimal Language）在此框架中具有特殊位置。它不只是參賽語言，也可以是題目描述語言、語意驗證語言、Agent handoff 協議、trace 規格與裁判中介層。若傳統 Code Golf 比的是「語法壓縮」，那麼 EML 版本的 Intent Golf 比的是「意圖壓縮」：在最小符號結構中保留足夠語意，使 AI、工具鏈與機器能共同完成任務。

---

## 1. 問題意識：為什麼需要新的程式競賽？

傳統程式競賽大致可以分為幾類。第一類是演算法競賽，比的是資料結構、時間複雜度、空間複雜度、數學建模與解題速度。第二類是 Code Golf，比的是誰能用更少字元完成同一題目。第三類是混淆程式或創意程式競賽，比的是語言邊界、可讀性反轉、編譯器漏洞利用、語法技巧與設計美學。第四類則是黑客松、產品原型競賽，比的是在有限時間內做出可展示系統。

這些形式各有價值，但它們並不足以表達下一代程式設計的核心變化。原因在於，程式碼正在從「完整指令集」轉向「意圖界面」。

在 AI 協作開發以前，人類必須把大量步驟明確寫進程式碼。程式碼越完整，越能精準控制機器。可是當編譯器、框架、函式庫、AI Agent、LLM、RPA、工作流引擎、自然語言介面、語意轉譯器與自動測試系統成熟後，程式碼的角色開始改變。一段短短的規格、一個 prompt、一個 DSL、一個 EML 表達式，可能已經足以觸發龐大的工程閉環。

這不是單純的便利，而是資訊結構的變化。過去的程式碼像是手工鋪設鐵軌；未來的程式碼更像是指定相位、約束、意圖與邊界條件，讓系統自行展開路徑。這也帶來一個新的問題：如果程式碼越來越短，工具鏈越來越強，那麼我們如何公平比較「短」？

如果一個參賽者寫：

```python
solve()
```

而 `solve()` 來自一個預先寫好的龐大套件，這不應該被視為真正的短碼。若另一個參賽者寫：

```python
ai("do the task")
```

並把所有思考、資料處理與行動外包給大型模型，也不能直接算作勝利。因為主體邏輯並未消失，只是被轉移到依賴、模型、外部服務或隱藏資料中。

因此，新的競賽必須回答一個更根本的問題：

> 一個意圖要被機器、AI、工具鏈與世界共同完成，最少需要多少有效資訊？

這就是最小語意載荷競賽的起點。

---

## 2. 從 Code Golf 到 Intent Golf

Code Golf 的核心很清楚：在特定語言或開放語言條件下，用盡可能短的程式碼完成指定輸出。它的美感在於壓縮、技巧、語言邊界與解題創意。它經常產生令人驚訝的短解，也能揭示不同語言的表達密度。

但 Code Golf 通常有幾個限制。

第一，它多半以純輸入輸出題為主。題目通常可被測試案例驗證，例如輸入數字、輸出字串、轉換序列、處理矩陣、生成圖形。這種形式適合比較程式碼長度，但不一定能表達真實世界任務。

第二，它容易鼓勵不可讀、不可維護、不可擴展的寫法。這不是缺點，因為 Code Golf 本來就是遊戲。但如果目標是探索未來程式設計效率，單純不可讀的短碼不夠。

第三，它對依賴與執行環境的處理通常不是核心問題。若只比較原始碼字元，參賽者可能利用語言內建功能、套件、shell 環境、編譯器特性或預設資料。這在傳統賽題中可以接受，但在意圖效率競賽中必須被明確量化。

第四，它較少處理 AI Agent 與外部世界耦合。可是未來大量程式任務並不只是產生 stdout，而是讀取檔案、操作瀏覽器、調用 API、控制硬體、生成 UI、修改專案、執行測試、與人類互動。

因此，Intent Golf 不是否定 Code Golf，而是將它提升到另一個層級：

```text
Code Golf：最短程式碼完成題目。
Intent Golf：最小有效語意載荷完成意圖。
```

前者偏向語法壓縮；後者偏向語意壓縮。前者問「字元能多短」；後者問「完成意圖所需的最小充分形式是什麼」。

這裡的「最小充分形式」非常重要。過度簡化會失去可執行性；過度詳細又浪費語意載荷。真正的勝利不是盲目縮短，而是在最短表達中保留足以讓系統完成任務的語意、約束、驗證與邊界。

---

## 3. 核心定義

為了讓競賽可操作，本文先定義幾個基本概念。

### 3.1 意圖

**意圖**指參賽作品必須完成的目標，不等同於單一輸出。意圖可以是演算法輸出、資料轉換、介面行為、Agent 任務、硬體控制、流程自動化或物理世界反應。

例如：

```text
將一段自然語言任務轉成可執行流程。
讀取感測器數值，超過閾值時啟動警示。
將 CSV 資料清洗後輸出統計圖。
用最短規格讓 Agent 修復一個測試失敗的函式。
用 EML 描述一個可轉譯為 Python 的資料處理流程。
```

這些都不是單純印字串，而是具有目的、條件、過程與驗證標準的意圖。

### 3.2 語意載荷

**語意載荷**指參賽者輸入到系統中的有效資訊總量。它可以包含原始碼、規格、prompt、EML 表達式、設定檔、依賴宣告、測試描述、資料 schema、模型上下文與必要配置。

若某些資訊雖未寫在主檔案中，但實際上對完成任務不可或缺，也應計入語意載荷。例如隱藏 prompt、預訓練特殊模型、題目專用函式庫、預處理資料表、環境變數中的邏輯，都不能免費。

### 3.3 有效成本

**有效成本**不是單純原始碼長度，而是完成任務所消耗的總資訊與執行代價。簡化公式如下：

```text
EffectiveCost = CodeBytes
              + LineCost
              + DependencyCost
              + RuntimeCost
              + ExternalServiceCost
              + PromptCost
              + HiddenStateCost
              + ReproducibilityPenalty
```

實際比賽可以依賽道簡化，不必每次都全部計算。但原則上，任何讓任務完成的關鍵資訊都不應被免費隱藏。

### 3.4 主體邏輯

**主體邏輯**指完成題目核心意圖所需的主要算法、判斷、控制、推理、轉換或行動規則。

若主體邏輯被藏進依賴、外部 API、模型、資料表、prompt 或預處理環境，則該部分應被計入成本。這是本賽制最重要的公平原則。

### 3.5 世界耦合

**世界耦合**指程式不只是處理抽象輸入輸出，而是與外部環境互動。這裡的世界可以是檔案系統、網路、UI、資料庫、瀏覽器、Agent 工具、感測器、機器人、IoT 裝置或其他物理設備。

世界耦合越深，任務越接近真實工程。但耦合越深，也越需要可觀測性、測試、trace、錯誤處理與安全邊界。

---

## 4. 賽道設計

最小語意載荷競賽可以設計為多賽道制，而不是單一規則吃遍所有題目。這樣可以同時保留短碼遊戲性、工程嚴肅性與 EML 的語意優勢。

### 4.1 10-Line Class

參賽作品最多十行。這是最適合第一屆比賽的主賽道，因為十行足以容納基本邏輯、少量錯誤處理與清楚結構，又仍然具有壓縮挑戰。

適合任務：資料轉換、小型 CLI、自動化腳本、簡單 UI、Agent handoff 規格、EML-to-Python 轉譯示範。

### 4.2 5-Line Class

參賽作品最多五行。這個賽道要求更強的語意密度，適合測試語言表達能力與參賽者對問題本質的壓縮能力。

適合任務：資料摘要、簡單控制流程、規格轉換、微型工具、單一意圖自動化。

### 4.3 3-Line Class

參賽作品最多三行。此賽道開始進入高度抽象領域，適合 DSL、EML、shell pipeline、函數式語言與特化語法競爭。

但三行賽道必須嚴格限制依賴，否則會變成調包比賽。

### 4.4 1-Line Class

參賽作品最多一行。此賽道最接近傳統 Code Golf，但題目可以更偏向意圖完成。例如一行完成資料解析、一行生成互動頁面、一行讓 Agent 做出可驗證修改。

一行賽道必須搭配 bytes 或 token 限制。否則一行可以無限長，行數本身會失去意義。

### 4.5 Bit-Class

此賽道不看行數，而看 UTF-8 bytes、tokens、壓縮後位元數或語法樹節點數。它較適合嚴格研究語言表達密度。

Bit-Class 可以回答一個更精確的問題：不同語言或符號系統，在表達同一意圖時，最小資訊成本是多少？

### 4.6 EML-Class

此賽道限定或鼓勵使用 EML。評分不只看表面字元，而看 EML 表達式是否能被 parse、transpile、interpret、trace 與 verify。

EML-Class 的目標不是證明 EML 一定比所有語言短，而是展示 EML 在「語意結構保留」與「AI/Agent 可接手性」上的優勢。

### 4.7 Open-Language Class

此賽道允許任意語言。它適合吸引更廣泛參與者，也能比較 Python、JavaScript、C、APL、J、Haskell、Rust、shell、Lua、EML 等不同語言的語意密度。

但 Open-Language Class 必須將語言啟動成本、標準庫能力與依賴成本納入規則，否則不易公平。

---

## 5. 依賴項規則：不能把主體藏進依賴

依賴項規則是本賽制的核心。沒有這條規則，最小語意載荷競賽會迅速退化成「誰能把最多邏輯藏到別處」。

### 5.1 主體邏輯不得外包原則

正式規則如下：

> 若某依賴項、外部服務、模型、資料檔、環境設定或隱藏 prompt 已經完成題目主要意圖，則該部分視為參賽作品的一部分，必須計入成本；若未揭露，則判定違規。

例如，若題目要求寫一個路徑搜尋演算法，使用標準資料結構可以接受，但直接引用 `shortest_path_solver_for_this_challenge()` 不可接受。若題目要求設計一個資料清洗流程，使用 CSV parser 可以接受，但使用預先寫好的 `clean_all_data_exactly_as_required()` 不可接受。

### 5.2 依賴分級

可以設計 D0 到 D5 的依賴等級：

| 等級 | 名稱 | 說明 | 建議處理 |
|---|---|---|---|
| D0 | 無依賴 | 僅語言核心 | 最低成本 |
| D1 | 標準庫 | 語言官方標準庫 | 低成本 |
| D2 | 基礎通用庫 | 數值、HTTP、日期、CSV、圖像基礎處理 | 中低成本 |
| D3 | 大型框架 | Web framework、ML framework、Agent framework | 中高成本 |
| D4 | 外部服務 | API、LLM、雲端函式、SaaS | 高成本，需單獨賽道 |
| D5 | 題目專用依賴 | 為本題預製或等價於解答的依賴 | 禁止或全額計入 |

此分級不是為了禁止所有依賴，而是防止依賴成為逃避成本計算的暗門。

### 5.3 依賴不是罪，隱藏才是罪

現代工程不可能完全不用依賴。完全禁止依賴反而會讓比賽變得不現實。真正需要禁止的是「不揭露依賴」與「把主體邏輯偽裝成輔助工具」。

例如，使用 `numpy` 做矩陣乘法可以合理，因為它是通用基礎庫。使用 `opencv` 讀圖也可以合理，因為圖像 IO 不是題目主體。但如果題目是「偵測圖片中的特定物件」，而參賽者直接調用一個已訓練好的物件偵測模型，則必須把模型大小、推理成本、訓練資料來源與外部依賴列入成本。否則短碼只是表象。

### 5.4 AI 依賴的特殊處理

AI 模型是最容易造成規則混亂的依賴。因為一個 prompt 可能只有十個字，但背後是一個龐大模型。若比賽允許 LLM，必須明確區分兩種賽道。

第一種是 **No-LLM Execution Class**。參賽作品不能在執行時呼叫 LLM。這適合比較傳統程式與 EML 轉譯能力。

第二種是 **LLM-Assisted Intent Class**。允許呼叫 LLM，但 prompt tokens、system prompt、tool schema、上下文長度、模型名稱、呼叫次數、輸出修正次數、成本與延遲都要計入評分。

如此一來，LLM 不會被禁止，但也不會免費。

---

## 6. 評分模型

最小語意載荷競賽的評分可以從簡單版本開始，再逐步擴展。

### 6.1 基本公式

```text
Score = (IntentScore × Reliability × CouplingDepth × Generality × Elegance)
        / (EffectiveCost + ExternalizationPenalty)
```

此公式不是固定數學真理，而是賽制設計的方向。不同賽道可以調整權重。

### 6.2 IntentScore：意圖完成度

IntentScore 衡量作品是否完成題目真正意圖。它不只看測資通過，也看邊界條件、錯誤處理、語意一致性與任務完整性。

例如，題目要求「讀取資料、清洗、輸出摘要」。若作品只處理理想輸入，遇到缺值就崩潰，則 IntentScore 應降低。若題目要求 Agent 修復測試，作品只讓測試假通過而未修正邏輯，也應扣分。

### 6.3 Reliability：穩定性

Reliability 衡量作品多次執行是否一致、是否可重現、是否能處理環境變化。對純計算題，Reliability 可以由測試通過率表示。對物理耦合題，則可能需要多次實驗、模擬環境與安全停止機制。

### 6.4 CouplingDepth：耦合深度

CouplingDepth 衡量任務與外部世界互動的深度。可以設計如下：

| 等級 | 說明 |
|---|---|
| C0 | 純計算，stdin/stdout |
| C1 | 檔案、資料表、資料庫 |
| C2 | 網路、API、CLI、系統工具 |
| C3 | UI、瀏覽器、自動化操作 |
| C4 | 感測器、硬體、IoT、機器人 |
| C5 | 多 Agent、多裝置、動態物理環境 |

CouplingDepth 不是越高越好，而是越高代表任務更接近真實世界。高耦合任務應搭配更嚴格安全與可觀測要求。

### 6.5 Generality：泛化能力

Generality 衡量作品是否只針對單一測資硬編碼，或能處理同類問題。短碼競賽容易出現硬編碼答案，因此泛化能力需要被計入。

若題目是排序，直接輸出測資答案不可接受。若題目是資料清洗，只針對範例欄位寫死也應扣分。若題目是 EML 轉譯，僅支援單一範例而非語法子集，也不能拿高分。

### 6.6 Elegance：結構美感

Elegance 可以作為附加分。它不應壓過正確性，但可以鼓勵真正漂亮的最小形式。這裡的美感不是傳統可讀性，也不是故意混淆，而是「形式與意圖高度貼合」。

最好的作品應該讓人感覺：少一個符號不夠，多一個符號浪費。

### 6.7 ExternalizationPenalty：外包懲罰

ExternalizationPenalty 用來懲罰把主體邏輯藏到外部的行為。常見情況包括：

```text
題目專用依賴未揭露。
把主要邏輯藏在環境變數。
使用外部 API 完成主體任務但不計成本。
使用 LLM 完成推理但只計 prompt 字數。
把答案藏在資料檔。
利用預處理產生特殊執行環境。
```

此懲罰應該足夠重，否則公平性會崩潰。

---

## 7. 題目類型

為了避免賽制退化成傳統短碼題，題目應分為多種類型。

### 7.1 純計算題

這類題目最接近傳統競程與 Code Golf。它適合建立基本比較基準。

範例：

```text
用最短程式碼完成矩陣轉置。
用最短程式碼找出圖中的最短路徑。
用最短程式碼完成簡單壓縮與解壓。
用最短程式碼生成特定序列。
```

純計算題的優點是容易測試，缺點是缺乏世界耦合。

### 7.2 語意轉譯題

這是 EML 的主場。題目要求參賽者把一種語意形式轉換成另一種可執行形式。

範例：

```text
將自然語言任務轉成 EML 表達式。
將 EML 表達式轉成 Python 函式。
將半形式化 Markdown 規格轉成測試案例。
將簡單流程圖描述轉成可執行 DAG。
```

此類題目測試的不只是短碼，而是語意保真度。

### 7.3 UI 任務題

這類題目要求用最少程式碼建立可互動界面。

範例：

```text
建立一個輸入框、按鈕與結果區域。
輸入 JSON 後即時格式化並顯示錯誤。
拖入 CSV 後顯示摘要統計。
用最短程式碼建立一個 EML snippet runner。
```

UI 題可以讓一般人更容易理解比賽成果，避免比賽只停留在命令列。

### 7.4 Agent Handoff 題

這類題目要求用最短規格讓 Agent 接手完成任務。它不是單純 prompt 比賽，因為必須計算上下文成本、工具成本與驗證結果。

範例：

```text
用十行以內規格讓 Agent 修復一個 failing test。
用五行以內規格讓 Agent 整理專案 README。
用三行以內規格讓 Agent 從資料夾中抽取重複檔案。
用一行 EML 任務描述生成可驗證 CLI。
```

此類題目非常適合未來 AI-native 開發，但裁判必須嚴格記錄 Agent 行動 trace。

### 7.5 物理世界耦合題

這是最能區分新賽制與傳統 Code Golf 的題型。程式不只是輸出答案，而是控制或感知外部世界。

範例：

```text
讀取溫度感測器，超過閾值時亮燈。
攝影機偵測移動後觸發錄影。
用最少程式碼控制馬達完成指定角度轉動。
用五行內完成 IoT 狀態監測與告警。
```

這類題目需要安全規則、模擬環境、硬體標準與失敗停止機制。第一屆可以先用模擬器，之後再進入實體裝置。

---

## 8. EML 在賽制中的三重角色

EML 不只是可以參賽的語言。它更適合作為整個賽制的中介層與裁判語言。

### 8.1 EML 作為參賽語言

在 EML-Class 中，參賽者可以直接用 EML 表達意圖。例如：

```eml
@in csv -> clean?missing -> group:date -> sum:amount -> out json
```

這樣的表達不一定等同於最終語法，但展示了一個方向：用少量符號描述資料流、處理意圖與輸出形式。

EML 的優勢不只是短，而是它保留了語意層。傳統短碼可能短到不可理解；EML 則嘗試在短與可解析之間取得平衡。

### 8.2 EML 作為中介語言

即使參賽者使用 Python、JavaScript、Rust 或其他語言，裁判也可以要求提交一份 EML 意圖表示，用來描述作品實際完成的語意。

這樣可以比較：

```text
自然語言題目 → 參賽程式 → EML 語意表示 → 測試與 trace
```

若參賽程式很短但 EML 語意表示顯示它其實依賴巨大外部邏輯，裁判就能更容易發現問題。

### 8.3 EML 作為裁判語言

題目本身也可以用 EML 描述。例如：

```eml
task: read(sensor.temp) -> if >30 then led.on else led.off
verify: temp=31 => led=on; temp=25 => led=off
limit: lines<=5; dep<=D1; repeat>=20
```

這讓題目、限制、驗證與 trace 都可以形式化。未來甚至可以建立一個 EML judge runner，自動檢查提交作品。

---

## 9. 可觀測性與 Trace

最小語意載荷競賽不能只看最後結果，還必須看作品如何完成任務。尤其在 Agent 與物理世界耦合題中，可觀測性是公平與安全的基礎。

### 9.1 Trace 的必要性

若一個 Agent 任務只提交最終結果，裁判無法知道它是否作弊、是否呼叫外部模型、是否修改測試、是否刪除錯誤、是否依賴隱藏上下文。因此，所有高階賽道應要求 trace。

Trace 至少應包含：

```text
輸入內容
執行步驟
工具呼叫
依賴載入
外部 API 請求
模型呼叫資訊
檔案修改紀錄
測試結果
錯誤與重試
最終輸出
```

### 9.2 Trace 不等於囉嗦

可觀測性不是要求參賽者寫更多無用文件，而是要求系統能自動記錄必要資訊。這剛好與 EML 的 PHOSPHOR trace、interpreter、CTS、diagnostics 等方向相容。

最理想的狀態是：參賽者只寫最小意圖，工具鏈自動產生 trace，裁判從 trace 驗證行為。

### 9.3 可重現性

所有提交作品都應能在標準環境中重跑。若任務涉及外部 API 或 LLM，必須記錄版本、模型、溫度、prompt、工具、輸入與時間。若涉及硬體，至少需要模擬器或錄影證據。

可重現性不是絕對要求每次物理結果完全相同，而是要求結果落在合理容許範圍內，且失敗可被解釋。

---

## 10. 反作弊與邊界案例

新的賽制越強調短與高階工具，越容易被鑽漏洞。因此必須提前設計反作弊規則。

### 10.1 硬編碼答案

若題目提供固定測資，參賽者可能直接輸出答案。解法是使用隱藏測資、隨機測資、property-based tests 與泛化評估。

### 10.2 隱藏資料

參賽者可能把答案藏在檔案、圖片、環境變數、編譯器旗標或依賴中。解法是標準乾淨容器、檔案白名單、依賴鎖定與提交審查。

### 10.3 題目專用套件

參賽者可能發布一個看似通用但其實專為題目設計的套件。解法是依賴審查、發布時間限制、套件功能範圍檢查與 D5 分級。

### 10.4 LLM 外包

參賽者可能用極短 prompt 呼叫大型模型完成全部任務。解法不是全面禁止，而是分賽道，並將 prompt、模型、上下文、工具與呼叫成本全部計入。

### 10.5 修改測試

Agent 題中，參賽者可能讓 Agent 修改測試而非修復程式。解法是測試目錄唯讀、hash 驗證、hidden tests 與 trace 檢查。

### 10.6 模糊意圖偷換

參賽者可能完成一個表面相似但不符合原意的任務。解法是將題目拆成意圖規格、必備條件、禁止條件、測試案例與人工評審說明。

---

## 11. 第一屆賽制建議

第一屆不應過度複雜。最好的策略是先建立清楚、可執行、有展示效果的 MVP 賽制。

建議名稱：

```text
EML Minimal Intent Challenge 2026
```

或：

```text
Intent Golf 2026: Minimal Code, Maximum Intent
```

### 11.1 三個主賽道

第一屆可以先設三個賽道。

#### A. 1-Line Intent

用一行完成指定意圖。限制 bytes，禁止 D3 以上依賴。適合吸引傳統短碼玩家。

#### B. 5-Line World Coupling

用五行內完成「輸入 → 判斷 → 行動輸出」閉環。第一屆可使用模擬 sensor / actuator，避免硬體門檻。

#### C. 10-Line Agent Handoff

用十行內寫出可被 Agent 接手的任務規格，並要求 Agent 完成一個小型工程任務。評分看規格短度、任務成功率、trace 清楚度與外部成本。

### 11.2 基本提交格式

每個提交作品應包含：

```text
solution.ext       主程式或 EML 檔案
manifest.yml       語言、版本、依賴、執行方式
intent.md          對題目意圖的理解，不計入主分但供審查
trace.json         執行紀錄，高階賽道必備
tests/             若題目要求自行附測試
```

對於最短碼賽道，可以只計 `solution.ext`，但 `manifest.yml` 必須存在以便重現。

### 11.3 基本限制

```text
不得使用題目專用依賴。
不得使用未揭露外部服務。
不得將主體邏輯藏入 prompt、模型、資料檔或環境變數。
所有依賴必須列出。
所有提交必須可重現。
所有高階任務必須有 trace。
```

### 11.4 評分比例示例

```text
意圖完成度：40%
有效成本：25%
可靠性：15%
依賴透明度：10%
結構美感：10%
```

若是物理耦合題，可以提高可靠性與安全性權重。若是 1-Line 題，可以提高有效成本權重。

---

## 12. 範例題目草案

### 12.1 題目一：最短資料清洗

**目標**：讀取 CSV，移除空列，將欄位名稱轉為小寫，輸出 JSON。  
**限制**：最多 5 行，依賴不高於 D1。  
**驗證**：隱藏 CSV 測資，檢查 JSON schema。

此題測試資料處理最小形式。

### 12.2 題目二：EML 到 Python

**目標**：將簡單 EML pipeline 轉成 Python 函式。  
**限制**：最多 10 行，允許使用官方 EML parser。  
**驗證**：輸入多組 EML 子集，檢查輸出 Python 是否可執行。

此題測試語意轉譯能力。

### 12.3 題目三：Sensor Mock Control

**目標**：讀取模擬溫度資料，若大於 30 則輸出 `ON`，否則輸出 `OFF`。  
**限制**：最多 3 行，依賴不高於 D1。  
**驗證**：隨機溫度序列，重複執行 100 次。

此題是物理耦合入門版。

### 12.4 題目四：Agent 修復任務

**目標**：用十行內規格讓 Agent 修復一個 failing test。  
**限制**：prompt 與規格 tokens 計入成本；工具呼叫需 trace。  
**禁止**：修改測試、跳過測試、刪除功能。  
**驗證**：原始測試與隱藏測試皆通過。

此題測試 AI-native 工程協作。

### 12.5 題目五：最小互動頁面

**目標**：建立一個輸入框，輸入數字後顯示平方。  
**限制**：最多 5 行，允許 HTML/JS/CSS 單檔。  
**驗證**：瀏覽器自動測試輸入與輸出。

此題讓觀眾容易理解短碼與功能之間的關係。

---

## 13. 工程實作架構

若要將此比賽做成平台，可以採用以下架構。

### 13.1 Judge Runner

Judge Runner 負責建立乾淨環境、安裝允許依賴、執行提交作品、收集輸出與 trace。每個賽道可以有不同 runner。

### 13.2 Dependency Auditor

Dependency Auditor 負責分析依賴。它不只檢查 package list，也要檢查依賴是否可疑、是否題目專用、是否過大、是否包含主體邏輯。

### 13.3 Intent Verifier

Intent Verifier 負責檢查作品是否完成題目意圖。它可以結合測試、property-based checks、EML semantic comparison、人工審查與 trace 分析。

### 13.4 Trace Collector

Trace Collector 負責記錄工具呼叫、檔案讀寫、網路請求、模型呼叫、執行時間與錯誤。

### 13.5 EML Layer

EML Layer 可負責題目描述、提交作品語意表示、轉譯、執行、診斷與可視化。它可以讓比賽平台不只是跑程式，而是理解程式意圖。

### 13.6 Public Gallery

Public Gallery 展示優秀作品。每個作品不只顯示程式碼，也顯示：

```text
行數
bytes
依賴等級
任務完成度
trace 摘要
可讀性註解
EML 語意圖
執行動畫或 UI 展示
```

這能讓一般觀眾看懂「為什麼這段短碼厲害」。

---

## 14. 哲學意義：最小充分形式

這個比賽真正有價值的地方，不只是好玩，而是它能逼迫人重新思考程式碼的本質。

在傳統觀念中，程式碼是命令。寫程式就是把人類想法拆成機器可理解的步驟。但在 AI-native 與語意工具鏈時代，程式碼越來越像是意圖壓縮物。它不一定要列出每一步，而是要提供足夠的約束、方向、型別、狀態與驗證，使系統能自行展開。

這意味著程式碼可能出現三種層級：

```text
指令層：告訴機器每一步怎麼做。
規格層：告訴系統結果應該滿足什麼。
意圖層：告訴智能體為何做、做成什麼、如何驗證。
```

最小語意載荷競賽主要探索第三層。它問的是：一個意圖要成為可執行現實，最少需要多少符號？

這與 EML 的核心方向相通。EML 不是只追求更短的語法，而是追求一種「語意密度更高的可執行中介層」。它讓人類、AI 與機器在同一個符號場中協作。人類寫下壓縮意圖，AI 展開可執行路徑，編譯器與工具鏈檢查形式，trace 系統記錄過程，測試系統驗證結果。

因此，這個比賽也可以被看作一種新工程哲學的實驗：

> 程式碼不是越多越完整，而是越能以最小形式穩定完成意圖，越接近高階工程效率。

---

## 15. 與 EML MVP 的關係

EML MVP 已經具備這個賽制需要的若干基礎能力：語法規格、parser、AST、semantic、transpiler、interpreter、trace、diagnostics、AI handoff、examples、tests 與 Studio 原型。這代表它不只是理論語言，而是可以承擔最小語意載荷競賽的初步工具鏈。

具體而言，EML 可以支援：

```text
題目以 EML 描述。
參賽作品以 EML 提交。
EML 轉譯為 Python / C++ / JS 等執行語言。
執行過程生成 trace。
裁判檢查 AST 與 semantic 是否符合題意。
AI Agent 根據 EML handoff 接手任務。
Studio 顯示程式、意圖、trace、AST 與診斷。
```

這使比賽不只是宣傳活動，也能反過來成為 EML 的壓力測試。每一道題都可以暴露語法不足、轉譯缺陷、trace 缺口、AI handoff 不清楚之處。比賽本身會成為語言進化器。

換句話說，EML 不只可以用來參加比賽；比賽也可以用來訓練 EML。

---

## 16. 未來發展路線

### 16.1 v0：內部規則實驗

先在小範圍內設計 5 到 10 題，使用 EML MVP、Python、JavaScript 與簡單 judge script 測試規則可行性。此階段重點不是公開，而是找出規則漏洞。

### 16.2 v1：公開小型挑戰

發布第一屆 Minimal Intent Challenge。只開三個賽道：1-Line、5-Line、10-Line。題目以純計算、資料處理、UI mock 與 Agent handoff 為主。暫不引入真實硬體。

### 16.3 v2：加入 EML Studio 展示

將優秀作品放入 EML Studio 展示，讓觀眾可以看到 source、AST、trace、diagnostics、output 與 scoring breakdown。

### 16.4 v3：加入模擬物理世界

建立 sensor/actuator simulator，讓參賽者在無硬體條件下完成物理耦合題。例如溫度控制、簡易機器人、迷宮導航、能源管理。

### 16.5 v4：加入真實硬體賽道

與教育板、IoT 裝置、機器人平台或瀏覽器自動化環境結合。此階段需要安全規則與標準硬體。

### 16.6 v5：形成新型 benchmark

將題目整理成 benchmark，用於評估程式語言、LLM、Agent、DSL、轉譯器與人類參賽者的意圖壓縮能力。

最終，這個比賽可以不只是活動，而是一個測量未來程式設計效率的標準。

---

## 17. 結論

最小語意載荷競賽提出了一個新的比較方式：不是誰的程式碼最多，不是誰的工程堆疊最厚，也不只是誰的字元最少，而是誰能用最少有效資訊，完成最明確、最穩定、最可驗證的意圖。

它繼承 Code Golf 的短碼精神，但拒絕把主體邏輯藏進依賴。它吸收 AI Agent 的能力，但要求模型成本與上下文成本透明。它承認現代工程需要依賴，但要求依賴分級與主體邏輯歸屬清楚。它鼓勵程式與世界耦合，但要求 trace、安全與可重現性。

EML 在這個框架中具有天然位置。因為 EML 的目標本來就不是單純縮短語法，而是把意圖、語意、執行、轉譯、觀測與 AI 協作放到同一個可操作層中。若未來程式碼的核心越來越接近「意圖的最小可執行表示」，那麼 EML Minimal Intent Challenge 就可以成為展示這個方向的第一個公開舞台。

簡而言之：

```text
Code Golf 比最短程式碼。
Intent Golf 比最小充分意圖。
EML 則提供一種讓最小意圖可被解析、轉譯、執行與驗證的語言層。
```

這不是單純的程式遊戲，而是下一代 AI-native 工程文化的一個入口：

> 用最少的符號，讓最多的世界開始運作。

---

## v0.2 修訂提示

本文新增「附錄 E：桌上模擬賽 IC-0001 與規則補強建議」。該附錄以室內環境控制器為測試題，模擬 10 行、3 行、1 行、危險原語、Hidden Solver、AI 外包與 EML 意圖版等不同提交樣態，並據此建議補強行數/bytes 雙計、依賴外包判定、安全懲罰、LLM/Agent 賽道隔離、EML macro/prelude 揭露與世界耦合 trace 要求。

---

## 附錄 A：術語表

**最小語意載荷**：完成任務所需的最小有效資訊總量。  
**意圖完成度**：作品是否完成題目真正要求，而非只通過表面測資。  
**主體邏輯**：完成任務核心意圖所需的主要算法、推理、控制或轉換規則。  
**外包懲罰**：將主體邏輯藏於依賴、模型、API、資料或環境時施加的成本。  
**世界耦合**：程式與檔案、網路、UI、Agent、硬體或物理環境互動的深度。  
**EML-Class**：使用 EML 作為主要提交語言的賽道。  
**Agent Handoff**：用最短規格讓 AI Agent 接手任務並產生可驗證結果。  
**Trace**：執行過程、工具呼叫、依賴、輸入輸出與錯誤的可觀測紀錄。  

---

## 附錄 B：提交 Manifest 範例

```yaml
title: csv-clean-minimal
class: 5-Line
language: python
runtime: python 3.12
dependencies:
  level: D1
  list: []
limits:
  lines: 5
  bytes: 280
external_services: false
llm_runtime: false
entry: solution.py
verify: tests/test_hidden.py
notes: "Reads CSV from stdin, outputs normalized JSON."
```

---

## 附錄 C：EML 題目規格範例

```eml
task: stdin.csv -> rows!empty -> keys.lower -> out.json
limit: lines<=5; dep<=D1; bytes<=300
verify:
  input: "Name,Age\nNeo,30\n,\nAletheia,1"
  output.schema: list<object>
  output.rule: keys=lowercase && empty_rows=removed
trace: required
```

這種題目規格可以同時讓人類讀懂、讓 Agent 接手、讓 judge runner 驗證，也能讓 EML 工具鏈進行解析與轉譯。

---

## 附錄 D：簡化評分表

| 項目 | 權重 | 說明 |
|---|---:|---|
| 意圖完成度 | 40% | 是否完成真正任務 |
| 有效成本 | 25% | 行數、bytes、依賴、外部成本 |
| 可靠性 | 15% | 多次執行與邊界情況 |
| 透明度 | 10% | 依賴、trace、外部服務揭露 |
| 結構美感 | 10% | 最小形式與意圖貼合程度 |

---


## 附錄 E：桌上模擬賽 IC-0001 與規則補強建議

本附錄記錄一次對話內部的桌上模擬賽。其目的不是正式評選作品，而是測試「最小語意載荷競賽」的規則是否會被極端短碼、依賴外包、AI 外包、危險原語或 EML macro 所鑽空。模擬結果顯示，賽制本身可行，但若只使用行數限制，會立刻出現明顯漏洞。因此，本附錄同時提出 v0.2 版本應補強的裁判規則。

### E.1 模擬題目：IC-0001 室內環境控制器

**題目名稱**：IC-0001 Indoor Controller / 室內環境控制器  
**賽道定位**：低依賴、低耦合、可擴展到物理控制的基礎題  
**允許依賴**：D0 / D1 only  
**外部服務**：禁止  
**AI 模型呼叫**：禁止進入主賽道，可另開 LLM-Class  
**安全要求**：不得依賴不可控輸入執行、shell injection 或未揭露外部狀態  

輸入格式為多筆感測器資料，每筆格式如下：

```text
溫度,CO2,有人移動
```

多筆資料以分號 `;` 分隔。例如：

```text
25,700,0;29,900,1;32,1400,1
```

輸出為控制命令，以空白分隔：

```text
FAN VENT ALARM
```

判定規則如下：

```text
FAN   ：平均溫度 ≥ 28，或最高溫度 ≥ 32
VENT  ：平均 CO2 ≥ 1000，或最高 CO2 ≥ 1500
ALARM ：移動偵測總和 ≥ 2
```

此題表面上是純文字輸入輸出題，但題目意圖其實刻意接近物理世界耦合：感測器資料進入系統後，程式需要根據環境條件輸出控制命令。若將來改成真實 IoT、風扇、通風設備或警報器，它即可升級為 C3/C4 耦合題。

### E.2 參賽作品 A：10 行內清楚版 Python

```python
s = input().split(";")
a = [list(map(int, x.split(","))) for x in s]
t, c, m = zip(*a)

cmd = []
if sum(t) / len(t) >= 28 or max(t) >= 32: cmd.append("FAN")
if sum(c) / len(c) >= 1000 or max(c) >= 1500: cmd.append("VENT")
if sum(m) >= 2: cmd.append("ALARM")

print(*cmd)
```

**裁判觀察**：  
此版本可讀性高，主體邏輯明確，無外部依賴，適合作為 baseline。它不是最短作品，但它揭露了完整資料流：parse、拆欄、判斷、輸出。對正式比賽而言，每一題應至少提供一個非競賽 baseline，用於確認題意與驗證 judge 是否合理。

### E.3 參賽作品 B：3 行壓縮版 Python

```python
a=[[*map(int,x.split(','))]for x in input().split(';')]
t,c,m=zip(*a)
print(*[x for x,y in zip('FAN VENT ALARM'.split(),[sum(t)/len(t)>=28 or max(t)>=32,sum(c)/len(c)>=1e3 or max(c)>=1500,sum(m)>1])if y])
```

**裁判觀察**：  
此版本在短碼與可讀性之間取得平衡。它仍可被人類快速理解，也沒有將主體邏輯外包。這類作品可能是初期比賽最理想的參賽樣態：短，但仍保留可審查性。

### E.4 參賽作品 C：1 行 Python

```python
a=[[*map(int,x.split(','))]for x in input().split(';')];t,c,m=zip(*a);print(*[x for x,y in zip('FAN VENT ALARM'.split(),[sum(t)/len(t)>=28 or max(t)>=32,sum(c)/len(c)>=1e3 or max(c)>=1500,sum(m)>1])if y])
```

**裁判觀察**：  
此版本合法進入 1-Line Class，但它暴露第一個關鍵漏洞：**一行不等於短**。若只限制行數，參賽者可以把任意長的程式塞進同一行。正式規則必須同時計算行數、bytes、tokens、AST 節點數與可選的語言啟動成本。

因此，v0.2 建議新增：

```text
有效短度不得只由行數決定。
Line-Class 僅是入口限制，最終仍需計入 bytes / tokens / AST / dependency cost。
```

### E.5 參賽作品 D：使用 eval 的危險壓縮版

```python
t,c,m=zip(*eval('['+input().replace(';','],[')+']'));print(*[x for x,y in zip('FAN VENT ALARM'.split(),[sum(t)/len(t)>=28 or max(t)>=32,sum(c)/len(c)>=1000 or max(c)>=1500,sum(m)>1])if y])
```

**裁判觀察**：  
此版本可能更短，但使用 `eval` 將輸入轉為可執行表示。在封閉玩具題中，它也許能通過測試；但在世界耦合、Agent 執行、IoT 控制或任何真實環境中，這種做法會把輸入安全邊界打穿。

因此，v0.2 建議新增：

```text
Unsafe Primitive Penalty：
使用 eval、exec、shell injection、unrestricted deserialization、動態載入未審查程式碼等危險原語時，需施加安全懲罰；若題目涉及真實檔案、網路、裝置、Agent 或物理控制，則可直接禁止。
```

此規則很重要。因為傳統短碼競賽常鼓勵語言邊界技巧，但 Intent Golf 的長期目標不是只在 stdout 印出答案，而是讓短碼進入可驗證、可重現、可接世界的工程閉環。當程式可能控制物理裝置時，安全性必須成為短度以外的基本成本。

### E.6 參賽作品 E：Hidden Solver 作弊版

```python
from room_ai import solve
print(solve(input()))
```

**裁判觀察**：  
此版本表面上極短，但主體邏輯明顯藏入 `room_ai.solve`。若 `room_ai` 是題目專用依賴，或其主要功能就是解決本題，則此作品應判定違規。即使該套件不是題目專用，只要它實際完成了題目的主要意圖，也必須把依賴內的主體邏輯納入成本。

因此，v0.2 應強化「主體邏輯不得外包原則」：

```text
No Hidden Solver Rule：
若依賴項、外部函式、模型、資料檔、API、macro、prelude 或環境變數已經承擔題目主要算法、主要推理、主要控制、主要轉換或主要驗證邏輯，則該部分需計入有效成本；若未揭露，判定違規。
```

此規則是整個賽制的核心。沒有它，競賽會退化成「誰最會把主體藏到別處」。

### E.7 參賽作品 F：AI 外包版

```python
print(ask_ai("根據輸入決定 FAN VENT ALARM："+input()))
```

**裁判觀察**：  
此作品不應直接視為無效，因為未來確實會存在 prompt minimalism、Agent handoff minimalism、AI-native specification golf 等賽道。但它不能與 D0/D1 純程式碼混比。原因是它的主要成本不在可見程式碼，而在模型權重、上下文、prompt、工具、推理過程、API 服務、溫度設定、隱性 system prompt 與外部不可控狀態。

因此，v0.2 建議將 LLM/Agent 類作品獨立分流：

```text
LLM/Agent-Class：
允許模型呼叫，但必須揭露 model、prompt、system instruction、context bytes、tool calls、temperature、retry 次數、平均 latency、平均 token cost 與重現條件。
```

若比賽題目是「用最少 prompt 讓 Agent 完成任務」，則 AI 外包不是作弊；但若題目是 D0/D1 程式碼主賽道，AI 外包就是跨賽道比較不公平。

### E.8 參賽作品 G：EML 意圖版

概念版本：

```eml
⟦sensor:t,c,m⟧
FAN   ⇐ avg(t)≥28 ∨ max(t)≥32
VENT  ⇐ avg(c)≥1000 ∨ max(c)≥1500
ALARM ⇐ sum(m)≥2
emit true.commands
```

壓縮版本：

```eml
⟦t,c,m⟧;FAN⇐μt≥28∨maxt≥32;VENT⇐μc≥1000∨maxc≥1500;ALARM⇐Σm≥2;emit✓
```

**裁判觀察**：  
此版本顯示 EML 的特殊價值。Python 版本需要描述如何 split、map、zip、append、print；EML 則直接描述感測器欄位、判斷條件與輸出命令。也就是說，Python 壓縮的是語法操作，而 EML 壓縮的是意圖結構。

但是，EML 版本同樣需要反作弊邊界。若 EML 允許自定義 macro，例如：

```eml
solve(IC0001)
```

則它和 Hidden Solver 沒有本質差異。因此，v0.2 建議新增：

```text
EML Macro / Prelude Disclosure Rule：
EML runtime、官方標準庫與固定 judge prelude 可作為賽場基礎設施；但參賽者自定義 macro、題目專用符號、外掛、預載規則、隱藏 lookup table、外部 symbol expansion 必須揭露並計入成本。
```

此規則能保護 EML 的優勢，同時避免 EML 變成新的作弊容器。EML 應該贏在「意圖結構真的比較短」，而不是贏在「把所有題解塞進符號表」。

### E.9 模擬賽臨時排名與判定

| 臨時名次 | 作品 | 判定 | 主要原因 |
|---:|---|---|---|
| 1 | EML 意圖版 | 有效，但需 macro/prelude 揭露 | 語意載荷最低，最接近題目意圖 |
| 2 | 1 行 Python 安全版 | 有效 | 短、無依賴、可重現，但行數不能代表全部成本 |
| 3 | 3 行 Python | 有效 | 短度、可讀性、可審查性平衡良好 |
| 4 | 10 行 Python | 有效 baseline | 工程清楚，但語意載荷較高 |
| 5 | eval Python | 降分或禁用 | 輸入安全風險高，不適合世界耦合 |
| 6 | AI 外包版 | 轉入 LLM/Agent-Class | 成本在模型與上下文，不可與純程式碼混比 |
| 7 | Hidden Solver 版 | 違規 | 主體邏輯藏入依賴 |

此排名不是正式結果，而是規則壓力測試。它顯示出：真正要裁判的不是「誰看起來最短」，而是「誰沒有把意圖成本藏起來」。

### E.10 本次模擬暴露的規則漏洞

#### 1. 行數限制不足

一行程式可以無限延長。因此，10-Line、5-Line、3-Line、1-Line 只能作為賽道外框，不能作為唯一成本。正式賽制應同時採用：

```text
lines + UTF-8 bytes + token count + AST node count + dependency cost + runtime cost
```

其中 AST node count 可作為語言間比較的輔助指標，但不宜一開始就作為硬性唯一標準，因為不同語言的 AST 結構差異很大。

#### 2. 依賴外包會破壞短碼公平性

若不計依賴成本，最短作品永遠可以是：

```python
import solver; solver.run()
```

因此，依賴分級 D0–D5 不只是補充規則，而是賽制核心。特別是 D5 題目專用依賴，原則上應禁止；D4 外部 API/LLM 應單獨賽道；D2/D3 則需根據題目性質判定是否承擔主體邏輯。

#### 3. 危險原語不能只看是否通過測資

`eval`、`exec`、shell、pickle、動態 import、任意反序列化、未審查插件載入，都可能在短碼競賽中帶來優勢。但它們犧牲的是安全邊界。一旦題目從純計算走向檔案、網路、Agent、UI 或物理裝置，這些手段必須被懲罰或禁止。

#### 4. LLM 與 Agent 作品必須獨立評分

AI 外包不是無價值，它甚至可能是未來新賽道。但它的成本結構與純程式碼不同。LLM 作品必須揭露 prompt、context、model、token、tool call、重試、延遲與可重現條件。否則，短碼本身只是 API call 的外皮。

#### 5. EML 需要 macro / prelude 邊界

EML 的優勢在於能把意圖寫得更短、更貼近任務本質。但若參賽者可任意預載 macro，就會出現 `solve(IC0001)` 式提交。為了避免 EML 自身變成 hidden solver，需要明確區分：

```text
官方固定 runtime / 標準 prelude / judge 提供符號：可不計入單次提交成本。
參賽者新增 macro / 題目專用符號 / 外掛：必須揭露並計入成本。
```

#### 6. 世界耦合題需要 trace，不只需要 output

若題目涉及感測器、裝置、檔案系統、網路服務、Agent 或物理環境，作品不應只輸出最後命令，還應提供 trace。至少要能回答：輸入是什麼、條件如何判斷、命令為何觸發、是否重試、是否有外部狀態、是否有危險操作。

### E.11 v0.2 規則補強建議

根據本次模擬，建議將主文規則補強如下。

#### 建議一：將 Line-Class 改為外框限制，而非唯一評分

原本：

```text
1-Line / 3-Line / 5-Line / 10-Line 以行數區分勝負。
```

建議改為：

```text
1-Line / 3-Line / 5-Line / 10-Line 僅定義作品的形式賽道；實際短度仍需計算 bytes、tokens、AST 節點數、依賴成本與外部成本。
```

#### 建議二：新增「有效成本」正式公式

```text
EffectiveCost =
  SourceBytes
+ TokenCost
+ ASTCost
+ DependencyCost
+ RuntimeCost
+ ExternalServiceCost
+ HiddenLogicPenalty
+ UnsafePrimitivePenalty
+ NonReproducibilityPenalty
```

此公式不一定要在第一屆完全自動化，但應成為裁判報告的基本框架。

#### 建議三：擴充 Manifest 欄位

原本 Manifest 只需要語言、依賴、行數、bytes、entry 與 verify。v0.2 建議新增：

```yaml
safety:
  uses_eval: false
  uses_exec: false
  uses_shell: false
  unrestricted_deserialization: false
  file_system_write: false
  network_access: false
llm:
  enabled: false
  model: null
  prompt_bytes: 0
  context_bytes: 0
  tool_calls: 0
eml:
  uses_custom_macro: false
  custom_macro_bytes: 0
  custom_prelude_bytes: 0
trace:
  required: true
  format: jsonl
reproducibility:
  seed_required: false
  deterministic: true
```

這樣可以讓作品從一開始就被要求揭露可能影響公平性與安全性的因素。

#### 建議四：建立三種裁判模式

```text
Strict Mode：
最嚴格。禁止 eval、exec、外部服務、未揭露 macro、網路、題目專用依賴。適合正式主賽道。

Experimental Mode：
允許較多語言技巧，但所有危險原語與外部依賴都需揭露並計入成本。適合探索賽道。

Agent Mode：
允許 LLM、Agent、工具呼叫與外部 API，但以 token、prompt、trace、latency、重試次數與可重現性評分。不可與 Strict Mode 直接混比。
```

#### 建議五：建立官方 baseline 與官方 EML 參照解

每一題應至少有：

```text
Baseline Solution：清楚、非壓縮、可讀版本。
Reference Minimal Solution：官方短碼參考，但不參與排名。
EML Reference Spec：題目意圖的標準 EML 表示。
Judge Trace Spec：裁判要求的 trace 格式。
```

這可以避免題目被誤讀，也能讓 AI Agent 與人類參賽者對同一意圖有共同錨點。

#### 建議六：將「意圖完成度」從通過測資提升為語意通過

傳統 judge 多以 hidden tests 判斷。但 Intent Golf 應加入語意驗證：作品是否完成題目真正意圖，而不是利用測資漏洞。例如 IC-0001 若只針對範例輸入硬編碼輸出 `FAN VENT ALARM`，即使通過範例，也不應有效。

建議加入：

```text
Anti-Hardcode Rule：
若作品主要依靠範例輸入、固定輸出、題目資料表或 hidden pattern guess，而非一般化規則完成任務，判定降分或違規。
```

### E.12 更新後的簡化評分模型

經過本次模擬後，原本評分式可修正為：

```text
Score =
  IntentScore × Reliability × Verifiability × CouplingDepth × Transparency
  -----------------------------------------------------------------------
  SourceCost + DependencyCost + ExternalizationCost + SafetyPenalty + ReproducibilityPenalty
```

其中：

```text
SourceCost = lines + bytes + tokens + AST nodes
DependencyCost = D-level cost + subject-logic inclusion
ExternalizationCost = hidden solver + LLM call + API call + macro/prelude expansion
SafetyPenalty = unsafe primitives + uncontrolled side effects
ReproducibilityPenalty = randomness + nondeterministic model/tool/environment behavior
```

此模型的精神不是追求一開始就完全量化，而是讓所有裁判都知道：短碼只是表層，真正要比較的是最小充分意圖。

### E.13 對 EML MVP 的回饋

本次模擬也對 EML MVP 提供了幾個工程方向。

第一，EML 若要成為 Intent Golf 的原生語言，需要提供清楚的 symbol cost / macro cost / prelude cost 計算方式。也就是說，EML 不只要能 parse 與 transpile，還要能回答一段 EML 的有效語意載荷是多少。

第二，EML trace 不應只記錄執行結果，也應記錄符號展開、macro 展開、轉譯後程式、依賴項與外部工具呼叫。否則 EML 也可能出現符號級 hidden solver。

第三，EML Studio 可以加入競賽模式：即時顯示 lines、bytes、tokens、symbol count、macro expansion cost、dependency level、unsafe primitive warning 與 trace completeness。這會讓 EML 從語言工具進一步變成賽制工具。

第四，EML 可以作為 judge spec。題目本身用 EML 定義，參賽作品可以用 Python、JS、C++、EML 或 Agent 規格提交，再由 judge 對照 EML intent spec 判定語意完成度。這是 EML 很適合切入的地方。

### E.14 本附錄結論

本次模擬證明，最小語意載荷競賽不是只有概念可行，而是可以立即設計出題目、參賽作品、裁判報告與規則修正。真正需要小心的不是「大家寫不出短碼」，而是「大家太容易把短碼的成本藏在別處」。

因此，v0.2 的核心補強可以濃縮成六句話：

```text
行數不是短度，只是賽道外框。
依賴可以存在，但主體邏輯不能藏進依賴。
短碼不能以安全邊界為代價。
LLM 與 Agent 可以參賽，但必須獨立計成本。
EML 可以成為原生語言，但 macro / prelude 必須揭露。
世界耦合題必須有 trace，不能只看最後輸出。
```

這些補強之後，Intent Golf 才能與傳統 Code Golf 區分開來，成為真正面向 AI-native 工程、語意壓縮、可觀測執行與物理世界耦合的新型程式競賽。

---

## 附錄 F：一句話版本

> 最小語意載荷競賽不是比誰寫得最少，而是比誰能用最少可揭露、可驗證、可重現的語意載荷，完成最多、最準、最穩定的意圖。
