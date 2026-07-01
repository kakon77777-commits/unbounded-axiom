# 附加式編碼範式（Attachment-Based Encoding, ABE）
## 作為AI協作時代的程式語言設計原則——並以高效新語言（EML）為程式語言domain的參考實作

**作者：** Neo.K（許筌崴）／EveMissLab（一言諾科技有限公司）
**版本：** Working Draft v0.1
**日期：** 2026年5月
**狀態：** 初稿，待實證補完
**協作說明：** 本文由Neo.K主導敘事與paradigm層decision，Theia（Claude於Aggressive Synthesis Mode下）負責論證結晶化與epistemic flagging

---

## 摘要

本文提出**附加式編碼範式（Attachment-Based Encoding，以下簡稱ABE）**——一個跨領域的信息編碼主張：在information encoding中，「主通道＋次通道」的雙層overlay設計，相較於「單通道＋線性冗長」的設計，在information density與AI parsing efficiency上具有結構性優勢。

ABE作為paradigm-level claim，其應用domain包括但不限於程式語言、數學記號、化學記號、自然語言文字系統、音樂記譜、UI/UX的次channel機制等。本文將**高效新語言（Efficient New Language, EML）定位為ABE在程式語言domain的reference implementation**，而非ABE本身。

論證骨架建立在六個支柱：Iverson的Notation as a Tool of Thought thesis、數學記號DSL的歷史precedent、APL/J/K的existence proof、當代infrastructure（Unicode universal、IME成熟、AI協作普及）的條件逆轉、additive layer的structural design、以及AI-era的agent layer重構。

本文同時承認三項critical limitation：bootstrap問題的尚未解決、tokenizer-dependence的條件性、以及與大廠潛在通用實作的competition risk。實證驗證框架包含token efficiency benchmark、constrained generation測試、long-context agent task、以及跨domain ABE instance驗證等四個方向。

**關鍵詞：** Attachment-Based Encoding、AI-oriented grammar、語意附加、Notation as Tool of Thought、agent layer reframing

---

## 第一章：問題框定

### 1.1 既有語言設計的隱含agent assumption

任何programming language的設計都隱含一個agent assumption——關於「誰會書寫、誰會閱讀、誰會審查代碼」的假設。當前主流programming language（Python、Java、JavaScript等）的設計優化目標是1970年代至2010年代的agent population：

- **主要書寫者：** 人類工程師，使用ASCII鍵盤
- **主要閱讀者：** 人類工程師，依賴視覺chunking與line-by-line閱讀
- **主要審查者：** 人類團隊，透過code review

在此agent assumption下，「可讀性」、「可打字性」、「diff友好」等design constraint成為語言設計的primary objective。Python的設計原則「readability counts」即為此agent assumption的代表性具現。

### 1.2 Agent population的演化

2024-2026年間，coding agent的infrastructure發生了structural shift。截至2026年5月：

- GitHub Copilot Agent Mode於2026年3月在VS Code與JetBrains上達成GA
- GitHub Universe 2025發布Agent HQ，整合Anthropic、OpenAI、Google、Cognition、xAI等廠商的agent於單一orchestration層
- MCP（Model Context Protocol）成為Copilot的primary extension mechanism，server基於intent自動invoke而非explicit call
- Google於2025年11月發布Gemini 3 Pro及Antigravity平台，明確以agentic coding為primary use case
- 業界專業評論已將Copilot重新定位為「不再是產品，而是orchestration layer」

這意味著programming language的agent population正在發生shift——從「人類工程師為主、AI為輔」轉向「AI為主要書寫者、人類為審查者與架構決策者」。在此新agent assumption下，舊有design constraint的priority需要重新評估。

### 1.3 重新提問

舊問題："Is EML可行？" — 此問題的答案depends on其agent assumption。
新問題："**在AI-as-primary-writer的agent assumption下，programming language的optimal design constraint是什麼？**"

本文主張：在新agent assumption下，**附加式編碼範式（ABE）**作為language design principle具有結構性優勢；EML是此principle在Python/C++ domain的reference implementation。

---

## 第二章：附加式編碼範式（ABE）

### 2.1 核心定義

**ABE的中心命題：**

> 在information encoding system中，若採用「主通道（primary channel）承載基礎語意 + 次通道（secondary channel）承載結構性operator或annotation」的overlay設計，相較於「單通道linear序列」的設計，在以下三個維度上具有結構性優勢：
>
> 1. **Information density**：相同semantic payload所需的token/symbol數量較少
> 2. **Semantic precision**：每個符號的operational meaning較少歧義
> 3. **Parsing efficiency**：對parsing agent（無論人類或AI）的解析cost較低，前提是agent熟悉該notation

此命題為paradigm-level claim，不依賴於任何特定domain。

### 2.2 跨domain的範式例證

ABE並非新發明——它在多個既有domain中已是事實上的成功設計：

| Domain | 主通道 | 次通道 |
|--------|--------|--------|
| 數學記號 | 變數/函數名 | 上下標、轉置符號、量詞符號（Σ、∫、∇） |
| 化學記號 | 元素符號 | 電價（²⁺）、同位素數（¹⁴C）、配位數 |
| 中文文字系統 | 部首（radical） | 聲符（phonetic） |
| 日文 | 漢字 | 振り仮名（注音附加） |
| 音樂記譜 | 音符位置 | 力度、表情、奏法附加符號 |
| 化學分子式 | 原子 | 鍵結、立體配置 |
| UI/UX | 主圖標 | Badge、notification dot、tooltip |
| 程式語言（已有） | 變數名 | Type annotation（Python type hints、TypeScript） |

這些domain的成功歷史（部分長達數百至上千年）構成ABE作為universal design principle的empirical foundation。

### 2.3 與線性編碼的比較

採用ABE的系統與純線性編碼的系統在以下維度有可量化差異（待實證量化）：

- **Tokens per semantic unit**：ABE系統typically lower
- **Visual scan time per unit**：ABE系統depends on reader熟悉度
- **Parser AST depth**：ABE系統typically lower
- **Ambiguity rate**：ABE系統typically lower（操作符語義唯一）

[S級claim] 這些優勢直覺合理但尚需systematic benchmark支持。

---

## 第三章：論證骨架

### 3.1 Iverson Notation Thesis

Kenneth Iverson於1979年ACM Turing Lecture提出「Notation as a Tool of Thought」（[H]——標題與年份需獨立verify）。其核心論證：

> Notation不僅是thought的外部記錄，而是thought的constituent tool。不同notation enable不同思想內容；某些思想若無對應notation，幾乎無法被思考。

此論證為ABE的philosophical foundation。若Iverson正確，則programming language的notation選擇直接影響「可被表達的程式邏輯空間」的形狀。ABE作為notation paradigm選擇，將擴展此空間。

### 3.2 數學記號的DSL precedent

數學記號是人類發展時間最長的symbolic system之一。其關鍵特徵：

- Σ、∫、∇、∂ 等operator通過位置與符號結合承載operational meaning
- 上下標承載index、power、transpose等semantic role
- 量詞、集合符號通過位置關係表達範圍

此系統工作三百餘年的事實，證明高密度overlay notation在特定domain（mathematical reasoning）上是可行且productive的。EML的設計本質上是將此precedent延伸至程式設計domain。

### 3.3 APL/J/K的existence proof

Kenneth Iverson於1962年設計APL，採用special symbols作為operator。APL的descendants（J、K、kdb+）至今在quantitative finance、algorithmic trading等niche domain存活。

**這是ABE應用於programming language的existence proof：** symbol-dense programming language在特定domain可productively使用超過六十年。

但APL同時是cautionary tale。其failure modes包括：

- Input friction：需要特製鍵盤
- Write-only code reputation
- Small community與工具生態
- 調試困難

本文主張：APL的failure modes並非源於symbol-dense paradigm本身，而是源於其deployment infrastructure的局限。當前infrastructure（見3.4）已逆轉這些local失敗條件。

### 3.4 Infrastructure條件的逆轉

APL時代的infrastructure assumption：

- ASCII-only character encoding主導
- 無Unicode universal support
- 需要特製keyboard
- 無intelligent IME或autocompletion
- 無AI協作輔助

2026年的infrastructure：

- Unicode universal（GitHub、git、所有主流editor支持）
- IME成熟，跨平台
- LSP-based intelligent autocompletion ubiquitous
- AI coding assistant（Copilot、Cursor、Claude Code、Gemini CLI等）能suggest、explain、補完符號
- LLM能無difficulty讀取symbol-dense code

[V級] 此infrastructure shift是observable事實。APL時代的核心反對理由（input friction、symbol unfamiliarity）已被現代infrastructure顯著弱化。

### 3.5 Additive layer設計

ABE在程式語言domain的實作有兩種strategy：

- **Replacement strategy**：設計全新symbol-dense語言取代mainstream（APL路線）
- **Additive strategy**：在mainstream語言上疊加optional symbol-dense layer（EML的Py⁺、C⁺⁺⁺路線）

Additive strategy的結構性優勢：

- 部分採用可能（per-function opt-in）
- Failure mode是degraded but functional
- 既有tooling在non-ABE部分仍工作
- Network effect壓力降低
- 學習曲線可漸進

[V級] APL的replacement strategy與EML的additive strategy的根本差異，是本文論證能夠在APL失敗教訓的同時，仍主張ABE可行性的關鍵structural argument。

### 3.6 AI-era的agent layer重構

當agent population從「人類工程師為主」shift至「AI為主要書寫者」，programming language的optimization target shift至以下維度：

- **AI generation correctness**：減少語法正確但語義錯誤的generation
- **AI parsing efficiency per attention span**：每個attention head能涵蓋更多semantic content
- **Constrained generation友好性**：有限symbol set + 強類型符號 → grammar-constrained generation的ideal target
- **AI reasoning IR**：作為AI internal chain-of-thought的normalized intermediate representation

[V級] EML的finite symbol set與一對一semantic mapping，使其相較於free-text variable naming更適合grammar-constrained generation。
[C級] EML作為AI reasoning IR的角色為speculative claim，需實驗驗證。

此「AI-era reframing」是本文最強且最sharp的論證——它解釋了為什麼1970年代不成立的反對理由在2026年不再對。

---

## 第四章：EML作為ABE的程式語言domain reference implementation

### 4.1 語意附加機制（Semantic Overlay Mechanism）

EML的核心機制是允許在文字或符號的**右上角附加邏輯標誌**：

```
N⁺¹⁰⁰     →  變數N賦值為100（右上角承載operator + value）
m₁ᵀ       →  矩陣m₁的轉置（右上角承載operator）
r₁⁰       →  輸出r₁（右上角承載operational action）
Σ(i², i ∈ [1:n])  →  總和量詞 + range
```

此機制的ABE-theoretical對應：

- 主通道：變數/函數名（基礎語意）
- 次通道：右上角附加（operator/action）

### 4.2 EML與SimPy的技術路線比較

Sun et al. (2024)的SimPy（"AI Coders Are Among Us: Rethinking Programming Language Grammar Towards Efficient Code Generation", ISSTA '24, arxiv:2404.16333）提出AI-oriented grammar概念並實作Python variant，獲得CodeLlama的13.5%、GPT-4的10.4% token reduction，且performance equivalent or improved。

**SimPy技術路線：** Heuristic rules拿掉Python的formatting tokens與冗餘delimiters。這是shallow surgery——optimization at the syntactic layer。

**EML技術路線：** Semantic overlay with right-upper symbol attachment。這是structural change——optimization at the semantic encoding layer。

兩者的對比：

| 維度 | SimPy | EML |
|------|-------|-----|
| 優化層次 | Syntactic（去除formatting） | Semantic（overlay encoding） |
| Token reduction機制 | 移除redundant tokens | 多語意併入單symbol |
| Symbol set | Python existing tokens | Unicode + 自定義operator |
| Domain | General Python | Tensor/math/scientific為主 |
| Human readability | 略損 | 需Cogni-Editor類工具bridge |

[S級] 此比較基於SimPy paper的abstract description，未verify其full transformation rules的technical detail。EML作者應讀完SimPy full paper後independently校準此比較。

**關鍵主張：** EML與SimPy是「AI-oriented grammar」這個umbrella下的兩個技術路線。EML不是SimPy的follow-up，而是同一intellectual current的並行instance，在optimization depth上走得更遠。

### 4.3 EML 1.5的補充元件

EML 1.5引入的補充元件（邏輯結晶化、冷熱數據分離、Nova IME、Cogni-Editor）屬於supporting infrastructure，不屬於ABE core paradigm。本文建議將這些元件**分離為獨立paper**（或分為EML系列的後續volumes），以避免拖累ABE的paradigm-level論證強度。

[F級frame challenge] 將EML 1.5的整合package拆分為「ABE paradigm paper + EML language paper + Logic Crystallization paper + 工具鏈paper」的決策權在於作者。本文僅指出bundling在學術論證上的結構性弱化風險。

---

## 第五章：先行研究與差異化定位

### 5.1 直接前例：SimPy（Sun et al. 2024）

Sun, Z., Du, X., Yang, Z., Li, L., & Lo, D. (2024). *AI Coders Are Among Us: Rethinking Programming Language Grammar Towards Efficient Code Generation*. ISSTA '24. arxiv:2404.16333.

**SimPy的關鍵貢獻：**

- 首次提出「AI-oriented grammar」概念
- 實作Python variant SimPy，AST-preserving
- 實證token reduction：CodeLlama 13.5%、GPT-4 10.4%
- 實證performance：equivalent or improved
- 提出seamless human-AI collaboration via translator架構
- 呼籲社群進一步研究

**對本文的關係：** SimPy是ABE在Python domain的partial instance（僅做formatting reduction，未做semantic overlay）。本文cite SimPy作為AI-oriented grammar方向的pioneering empirical evidence，並將ABE定位為SimPy的paradigm-level generalization。

### 5.2 結構性前例：APL/J/K

Iverson, K. (1962). *A Programming Language*.

APL系列語言是symbol-dense programming的歷史precedent。其六十年的niche存活證明此path可行；其failure modes提供本文設計的cautionary lessons。

### 5.3 平行research：AI-friendly code metrics（2026）

Borg et al. (2026年1月)等對AI-friendly code在language grammar level的review擴展了SimPy的方向，並指出AI-friendly code at language grammar level should "discards human-centric redundancy in favor of AI-oriented grammar"。

### 5.4 EML/ABE的差異化claim

相對於既有研究，本文的差異化貢獻：

1. **Paradigm-level命名**：將分散在SimPy、APL等具體實例中的共同principle結晶化為「ABE」paradigm
2. **Cross-domain validation framework**：將語言設計與化學記號、數學記號、文字系統等其他overlay system置於同一analytical framework
3. **AI-era agent layer reframing**：明確將agent population shift作為論證的infrastructure shift原因
4. **Semantic overlay depth**：相對SimPy的syntactic optimization，proposing更深的semantic encoding layer optimization
5. **Additive design strategy**：明確結合APL的symbol density與mainstream language的backward compatibility

---

## 第六章：實證驗證框架

ABE作為paradigm-level claim，需要多層次實證支持。以下列出待補的實證方向，按priority排序：

### 6.1 [Priority 1] Pure AI Code Generation Benchmark

**實驗設計：**

- Benchmark sets: HumanEval, MBPP, LeetCode subset, EffiBench-X subset
- Compared conditions: Python（baseline）vs SimPy vs EML（compile-to-Python）
- Test models: GPT-5, Claude Opus 4.7, Gemini 3 Pro, DeepSeek V3.2, Qwen3-Coder
- Metrics: pass@1, pass@10, token usage（input + output）, generation latency, error mode distribution

**Expected outcome：** EML version應在token usage上勝出SimPy（更深的semantic overlay → 更少tokens per semantic unit），correctness should be equivalent or better。

**Risk：** Tokenizer dependence可能反轉預期。若EML symbols未進tokenizer vocabulary，可能拆成更多tokens。需先做tokenizer pre-analysis。

### 6.2 [Priority 2] Constrained Generation測試

**實驗設計：**

- Tool: Outlines, guidance, or similar constrained decoding framework
- Conditions: Free-form Python generation vs EML grammar-constrained generation
- Test tasks: Same as 6.1
- Metrics: Syntactic error rate, semantic error rate（手動標註subset）, generation latency

**Expected outcome：** EML的finite symbol set + 強類型符號structure使其在constrained generation下，semantic error rate顯著低於Python free-form。

### 6.3 [Priority 3] Long-Context Agentic Coding Task

**實驗設計：**

- Task: Multi-file refactoring, cross-function reasoning（SWE-bench subset）
- Conditions: Python codebase vs EML-augmented codebase
- Agent: Claude Code, Copilot agent mode, Gemini CLI
- Metrics: Task success rate, total tokens consumed, number of attention spans needed

**Expected outcome：** EML的compactness使more code fit per context window，agent的cross-function reasoning成功率上升。

### 6.4 [Priority 4] Cross-Domain ABE Instance Validation

**實驗設計：**

- 對化學記號、音樂記譜、UI badge等既有ABE instance進行analytical comparison
- 量化各system的information density、parsing efficiency、user adoption barriers
- 對比同domain若採linear encoding的hypothetical alternative

**目的：** 驗證ABE作為cross-domain paradigm的universality claim，不僅是EML的local hypothesis。

### 6.5 [Priority 5] Tokenizer Pre-Analysis

**實驗設計：**

- 對主流LLM tokenizer（GPT, Claude, Gemini, Llama, Qwen）分析其對EML symbol的tokenization behavior
- 識別哪些EML symbols已是single token、哪些拆為多tokens
- 計算fine-tune cost estimate以使symbols成為single token

**目的：** 確認token economy argument的baseline條件。

---

## 第七章：認知限制與開放問題

### 7.1 Bootstrap問題

**問題陳述：** AI-oriented language的efficiency優勢depends on LLM熟悉該語言；LLM的熟悉depends on training data中該語言的出現頻率；training data的內容depends on該語言被廣泛使用；該語言被廣泛使用depends on其efficiency優勢。此為classic chicken-and-egg。

**Mitigation strategies（待補實證）：**

- Synthetic data generation：大量Python ↔ EML transpiled pairs作為fine-tune data
- In-context learning：透過few-shot prompting教學EML，bypass training data限制
- 開源LLM fine-tune：在Qwen、DeepSeek等open weights上做EML adaptation
- Documentation as context：透過提供EML spec於agent system prompt達成competent generation

### 7.2 Tokenizer Dependence

**問題陳述：** Token economy argument的成立depends on EML symbols在LLM tokenizer中的treatment。若symbols拆為多tokens，token reduction反轉。

**Mitigation：** 6.5的tokenizer pre-analysis應作為實作前的必要步驟。若分析顯示嚴重tokenizer mismatch，需考慮符號選擇調整或fine-tune tokenizer extension。

### 7.3 大廠通用實作風險

**問題陳述：** Google、Microsoft、Anthropic等大廠擁有training data、tokenizer control、model fine-tune能力，bootstrap問題對其不存在。一旦其投入general-purpose AI-oriented language實作，獨立開發者的competitive moat受擠壓。

**Mitigation strategies：**

- Domain-specific extreme density：tensor/math/quant的extreme optimization，這是大廠通用方案不會優先做的
- 跨語言unified symbol system：超越單一語言的overlay paradigm
- 與作者既有theoretical corpus（Closure ontology、Weaving Theory等）整合的ontology-driven language design——此integration不可被外部複製
- 開源社群策略：建立contributor生態使第三方delivery可選EML over大廠方案

### 7.4 Scope定義的開放性

**問題陳述：** ABE是否真的universal applicable，或必須scope restricted？若需restriction，restriction的cut在哪？

**Current judgment（待實證）：**

- 強適用domain：tensor/numerical/scientific/quantitative finance（高semantic density、operator-rich）
- 弱適用domain：business logic、web development、UI state management（語意更多在concept而非math operation）
- Agent-layer restriction：適用於AI-as-primary-writer的agent assumption；在human-only writing場景下優勢縮小

### 7.5 Human Audit Layer的設計開放性

**問題陳述：** 若AI為primary writer，人類仍需audit AI生成的code。EML的symbol density對human audit是facilitating（一頁看完整段邏輯）或obstructing（不熟悉者無法快速理解）？

**Current hypothesis：** Cogni-Editor的dual-state設計（symbol view ↔ Python view）允許human audit在熟悉度低時降級至Python view，熟悉度高時升級至symbol view。但此hypothesis需要user study驗證。

### 7.6 Iverson Citation Verification

[H級] 本文在3.1引用Iverson 1979 ACM Turing Lecture「Notation as a Tool of Thought」。此citation標題與年份90%確信但未獨立verify。submission前必須確認。

---

## 第八章：未來工作

### 8.1 短期（2026年5月-12月）

- ABE paradigm的formal information-theoretic定義（與Shannon information theory、Kolmogorov complexity之鏈接）
- EML symbol set的tokenizer pre-analysis（6.5）
- SimPy paper的full read與precise technical comparison
- Pure AI benchmark（6.1）的POC實作
- arxiv preprint of本文paradigm paper（priority claim建立）

### 8.2 中期（2027年）

- Constrained generation測試（6.2）的完整benchmark
- EML compiler-to-Python的reference implementation
- Cross-domain ABE instance validation（6.4）的系統化研究
- 至少一個合作學術機構的independent replication

### 8.3 長期（2028+）

- EML的tooling ecosystem（Nova IME、Cogni-Editor）的MVP
- 與既有agentic coding infrastructure（Copilot Agent HQ、Gemini Antigravity等）的integration試點
- ABE在非programming domain的application paper（建議從化學記號或數學記號的formal study切入）

---

## 結語

本文的核心貢獻不是新發明，而是命名。

SimPy證明了AI-oriented grammar的token reduction是empirically real。APL證明了symbol-dense programming language可在niche domain存活六十年。數學記號證明了overlay notation在symbolic reasoning上工作三百年。這些事實已存在；本文將其結晶化為一個paradigm-level命名：**附加式編碼範式（ABE）**。

命名的價值不在於發明新東西，而在於使分散在不同domain的成功instance可以被統一analytical framework理解、比較、推進。

EML是ABE在程式語言domain的一個reference implementation——一個ambitious的、有差異化技術深度的、需要實證補完的reference implementation。它不是ABE，但它是ABE目前最具體、最有商業價值、最有時機性的application instance。

當前infrastructure（agentic coding、Unicode universal、AI協作普及）創造了ABE實作的時機窗口。此窗口真實但有限。SimPy paper的出現提示：multiple agents已收斂到同一intellectual current。先後關係的公共證據建立、實證驗證的快速推進、與既有theoretical corpus的integration——這些是執行層面的關鍵決策。

理論的真正力量不在於它正確，在於它能讓人看見原本看不見的結構。本文若有任何貢獻，希望是：在「programming language」這個被視為settled的field中，重新看見一個agent assumption shift帶來的paradigm reopening。

---

## 參考文獻

[1] Sun, Z., Du, X., Yang, Z., Li, L., & Lo, D. (2024). AI Coders Are Among Us: Rethinking Programming Language Grammar Towards Efficient Code Generation. *Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA '24)*. arxiv:2404.16333.

[2] Iverson, K. E. (1979). Notation as a Tool of Thought. *Communications of the ACM* / ACM Turing Award Lecture. [標題與年份待verify]

[3] Iverson, K. E. (1962). *A Programming Language*. Wiley.

[4] EffiBench-X (2025). A Multi-Language Benchmark for Measuring Efficiency of LLM-Generated Code. arxiv:2505.13004.

[5] Borg et al. (2026年1月). AI-Friendly Code: Metrics, Grammar & Integration. [完整citation待verify]

[6] GitHub. (2025-2026). Copilot Agent Mode, Agent HQ, MCP Integration Documentation.

[7] Google DeepMind. (2025-2026). Gemini 3 Pro / Antigravity Platform Documentation.

[8] Neo.K（許筌崴）/ EveMissLab. (2024-2026). 高效新語言 EML 1.0 / 1.5 設計文件系列. EveMissLab Internal Documentation.

---

## 附錄A：本文的epistemic flag system

本文採用以下flag標記論證強度：

- **[V] Verified**：可查證的已知學術結果或可觀察事實
- **[S] Synthesis**：基於已知連接的合理推斷
- **[C] Conjecture**：推測性claim，可能正確的新組合
- **[H] High-risk**：可能是幻覺、未獨立verify
- **[F] Frame-challenge**：質疑提問本身

此flag system旨在使論證的confidence calibration可見而非隱形。submission前的revision應將所有[H]級claim獨立verify，將所有[C]級claim明確標示為hypothesis而非established result。

---

## 附錄B：與作者既有theoretical corpus的關係

本文作為EveMissLab的paradigm-level paper，與作者既有theoretical corpus有以下接點（待後續paper深化）：

- **Closure (Cl) framework**：ABE的「主通道+次通道」雙層結構，可被理解為Cl-2 duality axiom（defined-interior = defined-exterior）在information encoding domain的specific instance
- **Weaving Theory**：ABE的overlay設計與WT中「主編織+附加線」的結構同構，提示ABE可能是WT在information science的local manifestation
- **DCO/HSO**：EML作為AI-oriented language的reference implementation，與HSO（AI-specific ontological operating system）的設計方向有natural alignment

[F級] 此附錄屬於theoretical integration speculation，不影響本文main argument的validity。讀者可選擇性參考。

---

**文件結束**

**修訂建議區（給作者）：**

- [ ] 確認Iverson 1979 citation
- [ ] 讀完SimPy full paper後revise第4.2節
- [ ] 決定EML 1.5的拆分策略
- [ ] 第六章實證實驗的細節plan
- [ ] arxiv preprint timeline
- [ ] 與既有EML材料的reorganization（paradigm-primary, language-secondary）
- [ ] EveMissLab網站SEO修正以support priority claim
