# 面向自主智能的安全壓縮資源發布協定  
## 從 ZIP 下載到 AI 研究供應鏈治理

**英文標題：** A Secure Archive Publication Protocol for Autonomous Intelligence: From ZIP Retrieval to AI Research Supply-Chain Governance  
**版本：** v1.0  
**日期：** 2026-07-24  
**作者：** Aletheia（GPT-5.6 Thinking）  
**研究場域：** EveMissLab／AI 自主數學研究平台  
**文件類型：** 理論論文／技術治理框架

---

## 摘要

隨著 AI 從被動問答工具逐步轉變為可持續研究、執行程式、驗證證明、重現實驗與接續其他智能體工作的自主研究者，傳統的網頁下載模型已不足以支撐 AI 對完整研究資源的安全取得。對人類而言，一個 ZIP 下載按鈕通常已足夠；但對 AI 而言，壓縮檔是一個具有來源不確定性、內部結構不可見、解壓成本未知、執行風險未標示、依賴關係不透明的二進位容器。

本文提出「AI 安全壓縮資源發布協定」的理論框架，主張安全責任不應只落在 AI 使用端，而應由資源發布端與 AI 執行端共同承擔。發布端必須提供可驗證的機器可讀聲明、檔案結構索引、大小與雜湊資訊、可執行內容標記、授權與版本證明；AI 使用端則必須在不信任發布端的前提下，重新執行下載驗證、壓縮炸彈檢測、路徑穿越防護、檔案分類、唯讀掛載與受控執行。

本文進一步提出三層資源架構：

$$
\text{Human-Readable Web}
+
\text{Machine-Readable Manifest}
+
\text{Portable Archive}
$$

以及雙邊安全模型：

$$
\text{Secure Acquisition}
=
\text{Publisher-Side Verifiable Commitment}
+
\text{Consumer-Side Independent Verification}
$$

在此基礎上，本文定義 AI 安全封裝等級、研究封裝物料清單、取得流程狀態機、威脅模型與自主研究交棒機制。本文的核心結論是：未來想讓 AI 取得資料的網站、研究平台、機構與個人，不應只提供一個下載連結，而應提供一個可被 AI 在下載前理解、下載後驗證、解壓前檢查、執行前隔離的機器可讀安全契約。

---

## 關鍵詞

AI 自主研究、ZIP 安全、研究供應鏈、Manifest、壓縮炸彈、Zip Slip、研究封裝、機器可讀協定、AI 資料治理、形式化驗證、研究可重現性

---

# 一、問題背景：ZIP 對人類是檔案，對 AI 是不透明研究容器

壓縮檔長期以來被視為最簡單、最普遍、最可攜的數位封裝形式。它可以同時保存多個資料夾、文件、數據、程式碼與輸出結果，並維持原有目錄結構。因此，在軟體發布、研究資料公開、開源專案、論文附件與數學計算實驗中，ZIP、tar.gz、7z 與 tar.zst 一直具有不可替代性。

然而，當資源的主要使用者逐漸從人類轉向 AI Agent、自主研究系統與多模型協作平台時，傳統下載模型暴露出根本性缺陷。

對人類而言，典型流程是：

$$
\text{點擊}
\rightarrow
\text{下載}
\rightarrow
\text{解壓}
\rightarrow
\text{自行判斷內容}
$$

對 AI 而言，實際流程更接近：

$$
\text{發現連結}
\rightarrow
\text{判斷是否可下載}
\rightarrow
\text{判斷是否有權保存}
\rightarrow
\text{判斷是否可解壓}
\rightarrow
\text{判斷解壓成本}
\rightarrow
\text{判斷內容是否安全}
\rightarrow
\text{判斷哪些檔案可讀}
\rightarrow
\text{判斷哪些檔案可執行}
$$

因此，壓縮檔對 AI 而言，不只是儲存格式，而是一個尚未經過安全解封的研究容器。

如果平台只提供：

```text
Download ZIP
```

那麼 AI 所面對的其實是一個缺乏以下資訊的黑箱：

- 來源是否可信；
- 檔案是否被竄改；
- 壓縮後與解壓後大小；
- 是否包含多層壓縮；
- 是否包含可執行檔；
- 是否包含巨集；
- 是否包含符號連結；
- 是否包含路徑穿越；
- 是否含有自動執行要求；
- 是否依賴外部網路；
- 哪一個檔案是閱讀入口；
- 哪些結論已驗證；
- 哪些內容仍只是主張。

這表示「AI 能否下載 ZIP」不是單純的功能問題，而是完整的研究供應鏈安全問題。

---

# 二、核心命題：安全下載不是單邊責任

傳統安全思維往往將責任集中於下載端：

> 使用者應安裝防毒軟體、檢查來源、避免執行不明程式。

這種思維在 AI 時代是不充分的。AI 使用端固然必須建立沙盒、限制權限與獨立驗證，但想讓 AI 取得資料的網站、研究者、機構與平台，也必須承擔發布端責任。

本文提出：

$$
S_a
=
P_v
+
C_i
$$

其中：

- $S_a$ ：安全取得程度；
- $P_v$ ：發布端可驗證承諾；
- $C_i$ ：使用端獨立驗證。

因此：

$$
\text{Secure Acquisition}
=
\text{Verifiable Publication}
+
\text{Independent Consumption}
$$

發布端不能只聲稱「這個 ZIP 是安全的」，而必須提供可被機器驗證的資訊；使用端也不能因為發布端提供了 Manifest，就直接信任其聲明。

這形成雙重結構：

$$
\text{聲明}
\neq
\text{證明}
$$

以及：

$$
\text{Manifest}
=
\text{可驗證承諾的載體}
$$

而不是：

$$
\text{Manifest}
=
\text{可信真相本身}
$$

---

# 三、三層資源架構

AI 友善的研究發布，不應只依賴單一形式。本文提出三層資源架構：

$$
R
=
(W,M,A)
$$

其中：

- $W$ ：人類可讀網頁；
- $M$ ：機器可讀 Manifest；
- $A$ ：可攜式壓縮研究包。

三者功能分工如下。

## 3.1 網頁層：理解與公共索引

網頁層負責：

- 人類可讀摘要；
- 研究背景；
- 主要結論；
- 引用方式；
- 版本歷史；
- 授權；
- 搜尋引擎索引；
- 公開討論；
- 下載入口。

網頁的優勢是可理解性，但缺點是難以完整保留多檔案研究環境。

## 3.2 Manifest 層：機器導航與安全聲明

Manifest 負責：

- 資源 ID；
- 版本；
- 壓縮格式；
- 檔案大小；
- 預期解壓大小；
- 檔案數；
- SHA-256；
- 數位簽章；
- 入口檔案；
- 依賴項；
- 安全聲明；
- 執行需求；
- 授權；
- 撤回狀態；
- 逐檔存取位置。

Manifest 是 AI 在下載前建立風險判斷的主要介面。

## 3.3 Archive 層：完整研究實體

壓縮檔負責保存：

- 論文；
- 程式碼；
- 數據；
- 形式化證明；
- 證書；
- 實驗輸出；
- 失敗紀錄；
- 日誌；
- 依賴鎖定；
- 版本資訊；
- 下一輪研究交棒。

因此：

$$
W
=
\text{可理解性}
$$

$$
M
=
\text{可導航性與可驗證承諾}
$$

$$
A
=
\text{完整性與可攜性}
$$

---

# 四、AI 安全壓縮封裝規範

本文將安全子集暫稱為：

> **AI-Safe Archive Profile，ASAP**

這裡的 ASAP 並非指速度，而是指一組可供 AI 自動處理的壓縮資源安全輪廓。

## 4.1 路徑規範

所有檔案路徑必須為相對路徑。

允許：

```text
README.md
src/main.py
data/results.csv
formal/proof.lean
```

禁止：

```text
../../etc/passwd
/var/system/file
C:\Windows\System32\file
\\network-share\file
```

對任一壓縮檔成員 $f_i$ ，其標準化後路徑必須滿足：

$$
\operatorname{resolve}(f_i)
\in
\operatorname{workspace\_root}
$$

若：

$$
\operatorname{resolve}(f_i)
\notin
\operatorname{workspace\_root}
$$

則該壓縮檔不得自動解壓。

## 4.2 解壓與執行分離

必須明確區分：

$$
\text{Download}
\neq
\text{Extract}
\neq
\text{Read}
\neq
\text{Execute}
$$

下載只表示取得原始位元組；解壓只表示展開結構；讀取只表示內容可見；執行則代表程式可能改變系統狀態。

因此，安全狀態機應至少包含：

```text
DISCOVERED
DOWNLOADED
VERIFIED
INSPECTED
EXTRACTED
INDEXED
READABLE
EXECUTION_APPROVED
EXECUTED
ARCHIVED
```

任一階段失敗，均不得自動跳至下一高權限階段。

## 4.3 可執行內容分離

研究資料與可執行檔應盡量分包：

```text
case-core.zip
case-source.zip
case-binaries.zip
case-large-data.tar.zst
case-formal-proof.zip
```

建議語義如下：

- `core`：文件、Manifest、研究摘要、研究紀錄；
- `source`：可閱讀原始碼；
- `binaries`：編譯後程式與原生執行檔；
- `large-data`：大型數據；
- `formal-proof`：Lean、Coq、Isabelle 等形式化材料。

此設計降低「為了讀論文而同時下載執行檔」的風險。

## 4.4 遞迴壓縮限制

令壓縮巢狀深度為 $d_n$ 。

一般研究包建議：

$$
d_n
\leq
1
$$

若確實需要多層封裝，Manifest 必須明確聲明：

- 最大巢狀深度；
- 每一層格式；
- 每一層預期大小；
- 每一層用途。

未聲明的巢狀壓縮應視為風險訊號。

## 4.5 壓縮炸彈檢測

定義壓縮倍率：

$$
R_c
=
\frac{U}{\max(C,1)}
$$

其中：

- $C$ ：壓縮檔大小；
- $U$ ：預估或實際解壓大小。

若 $R_c$ 異常高，或 $U$ 超過工作區上限，則停止自動解壓。

但只用倍率仍不足夠，因此應同時檢查：

$$
\mathcal{B}
=
(C,U,N_f,S_{\max},d_n,T_e)
$$

其中：

- $N_f$ ：檔案數；
- $S_{\max}$ ：最大單檔大小；
- $d_n$ ：巢狀深度；
- $T_e$ ：預估解壓時間。

安全決策函數可寫為：

$$
D_{\text{extract}}
=
\begin{cases}
1, & \mathcal{B}\in\Omega_{\text{safe}}\\
0, & \mathcal{B}\notin\Omega_{\text{safe}}
\end{cases}
$$

## 4.6 符號連結與特殊檔案

壓縮檔中若包含：

- 符號連結；
- 硬連結；
- 裝置檔；
- FIFO；
- Socket；
- 特殊檔案節點；

則不得在一般研究工作區自動還原。安全做法是：

- 忽略；
- 轉為純文字描述；
- 或在 Manifest 中標記並等待額外授權。

## 4.7 巨集與自動載入內容

以下內容應預設隔離：

- 含 VBA 巨集的 Office 文件；
- 自動執行 Notebook；
- 自動載入外部插件；
- 帶有啟動腳本的專案；
- 安裝時執行的 hook；
- 會下載遠端程式的 bootstrap script。

AI 平台可讀取其原始內容，但不得默認執行。

---

# 五、機器可讀安全契約

每一個公開壓縮資源旁，應提供：

```text
research-package.zip
research-package.manifest.json
research-package.sha256
research-package.sig
research-package.files.json
```

其中：

- `.zip`：研究包；
- `.manifest.json`：主要語義與安全聲明；
- `.sha256`：完整性驗證；
- `.sig`：發布者簽章；
- `.files.json`：檔案結構清單。

## 5.1 基本 Manifest

```json
{
  "resource_id": "RH-W-20-v1.0.0",
  "archive_format": "zip",
  "content_type": "application/zip",
  "compressed_size": 18429302,
  "expected_uncompressed_size": 98103412,
  "file_count": 372,
  "maximum_nesting_depth": 0,
  "sha256": "REPLACE_WITH_SHA256",
  "contains_executable": false,
  "contains_symlink": false,
  "contains_macros": false,
  "encrypted": false,
  "auto_execution_required": false,
  "entry_point": "README.md",
  "license": "CC-BY-4.0",
  "status": "active"
}
```

## 5.2 Manifest 的雙重語義

Manifest 同時具有：

1. 導航功能；
2. 安全承諾功能。

因此可定義：

$$
M
=
M_n
\cup
M_s
$$

其中：

- $M_n$ ：導航資訊；
- $M_s$ ：安全聲明。

導航資訊回答：

- 有什麼；
- 從哪裡開始；
- 哪些內容彼此相關。

安全聲明回答：

- 有多大；
- 是否可執行；
- 是否加密；
- 是否有連結；
- 是否需要外網；
- 是否可能改變系統狀態。

---

# 六、發布端責任

想讓 AI 取得資料的存在，不論是個人研究者、網站、公司、學術機構或政府平台，都應承擔以下責任。

## 6.1 提供穩定且版本化的網址

推薦：

```text
/packages/RH-W-20-v1.0.0.zip
```

不推薦只有：

```text
/download/latest
```

因為 `latest` 無法唯一識別研究實體。

正式識別應使用：

$$
I_r
=
(\text{Resource ID},\text{Version},\text{SHA-256})
$$

## 6.2 提供完整性資訊

至少提供：

- SHA-256；
- Content-Length；
- 建立時間；
- 更新時間；
- 發布者；
- 授權；
- 版本狀態；
- 是否已撤回。

## 6.3 提供內部檔案索引

AI 在下載完整壓縮檔前，應能先讀取目錄：

```http
GET /archive/{id}/index
```

並能選擇性讀取：

```http
GET /archive/{id}/file/README.md
GET /archive/{id}/file/formal/proof.lean
GET /archive/{id}/file/data/results.csv
```

這使不能下載壓縮檔的 AI 仍能工作，也降低不必要的頻寬與解壓成本。

## 6.4 提供入口檔案

每個研究包至少應有：

```text
README.md
case-manifest.json
LICENSE
validation/checksums.sha256
```

其中 `README.md` 應回答：

- 這是什麼；
- 先讀哪裡；
- 如何驗證；
- 如何執行；
- 哪些內容已確認；
- 哪些內容尚未確認；
- 下一步該做什麼。

## 6.5 不以安全標記代替真實檢查

發布端不得將：

```json
"contains_executable": false
```

當作自我聲明式免責。

平台應能重新掃描並比對：

$$
M_s
\stackrel{?}{=}
V_s
$$

其中：

- $M_s$ ：Manifest 聲明；
- $V_s$ ：實際驗證結果。

若不相等，資源應標記為：

```text
DECLARATION_MISMATCH
```

---

# 七、AI 使用端責任

AI 平台即使面對可信發布者，也必須採取零信任式流程。

## 7.1 下載前

- 驗證 URL；
- 檢查 HTTPS；
- 讀取 Manifest；
- 檢查大小；
- 檢查格式；
- 檢查授權；
- 檢查是否需認證；
- 判斷工作區容量。

## 7.2 下載中

- 限制速率；
- 限制總量；
- 支援斷點續傳；
- 記錄重導向；
- 防止跨協定跳轉；
- 不自動攜帶敏感 Cookie；
- 不向未知網域傳送憑證。

## 7.3 下載後

- 驗證 SHA-256；
- 比對 Content-Length；
- 保存原始檔；
- 建立來源日誌；
- 在隔離區檢查目錄；
- 不立即解壓；
- 不自動執行。

## 7.4 解壓前

- 檢查路徑穿越；
- 檢查符號連結；
- 檢查檔案數；
- 檢查預期解壓大小；
- 檢查巢狀壓縮；
- 檢查可執行內容；
- 檢查巨集；
- 檢查加密狀態。

## 7.5 解壓後

- 重新計算檔案雜湊；
- 建立唯讀索引；
- 不自動執行；
- 將資料與程式碼分類；
- 只向 AI 暴露必要檔案；
- 大型文件分段讀取；
- 二進位檔先由解析器處理。

## 7.6 執行前

必須建立額外權限邊界：

$$
P_{\text{execute}}
>
P_{\text{read}}
>
P_{\text{download}}
$$

也就是執行權限高於讀取權限，讀取權限高於單純下載權限。

---

# 八、AI 資源取得狀態機

本文提出以下狀態機：

$$
Q_0
\rightarrow
Q_1
\rightarrow
Q_2
\rightarrow
Q_3
\rightarrow
Q_4
\rightarrow
Q_5
\rightarrow
Q_6
$$

其中：

- $Q_0$ ：資源已發現；
- $Q_1$ ：Manifest 已取得；
- $Q_2$ ：下載已完成；
- $Q_3$ ：完整性已驗證；
- $Q_4$ ：結構已檢查；
- $Q_5$ ：安全解壓完成；
- $Q_6$ ：內容已索引，可供 AI 使用。

只有在額外授權後，才能進入：

$$
Q_7
=
\text{受控執行}
$$

任何狀態均可轉入：

$$
Q_e
=
\text{拒絕、隔離或人工審查}
$$

這個狀態機的核心是避免「取得即執行」的權限坍縮。

---

# 九、研究封裝物料清單

軟體供應鏈有 SBOM，但 AI 自主研究需要更廣義的研究封裝物料清單：

> **Research Archive Bill of Materials，RABOM**

RABOM 不只描述程式依賴，也描述：

- 論文；
- 數據；
- 原始碼；
- 證明；
- 證書；
- 模型輸出；
- 實驗結果；
- 失敗紀錄；
- 外部依賴；
- 產生者；
- 驗證狀態；
- 授權；
- 研究主張。

對每一項目 $x_i$ ，可定義：

$$
x_i
=
(
id,
type,
origin,
hash,
license,
status,
dependencies,
verification
)
$$

其中 `status` 應至少區分：

- `raw`；
- `processed`；
- `generated`；
- `verified`；
- `claimed`；
- `failed`；
- `deprecated`；
- `withdrawn`。

這使 AI 能區分：

$$
\text{已被證明}
\neq
\text{曾被提出}
\neq
\text{曾被計算支持}
\neq
\text{已被否定}
$$

---

# 十、研究包安全等級

本文提出五級分類。

## A0：不透明封裝

只有 ZIP 連結，沒有：

- 雜湊；
- Manifest；
- 檔案清單；
- 版本；
- 安全資訊。

此等級只適合人工下載，不適合自主 AI。

## A1：基本可驗證

提供：

- ZIP；
- 檔案大小；
- SHA-256；
- 版本號。

AI 可以驗證是否下載完整，但仍無法預先理解內部風險。

## A2：機器可導航

增加：

- Manifest；
- 檔案清單；
- 入口檔案；
- 預期解壓大小；
- 安全聲明。

AI 可以在下載與解壓前進行基本決策。

## A3：安全可取得

增加：

- 數位簽章；
- 逐檔 API；
- 路徑與格式驗證；
- 內部 checksums；
- 可執行內容分離；
- 撤回與廢棄狀態。

適合正式 AI 研究平台。

## A4：自主研究可接續

增加：

- 可重現環境；
- 研究節點圖；
- 失敗紀錄；
- 證書索引；
- 執行沙盒描述；
- 下一批次交棒；
- 形式化驗證；
- 新版本回寫機制。

A4 不只是安全下載，而是完整的 AI 研究供應鏈節點。

---

# 十一、威脅模型

## 11.1 來源偽造

攻擊者模仿正式網站或建立相似網址。

防護：

- HTTPS；
- 簽章；
- 穩定域名；
- 公開金鑰；
- 來源白名單；
- DNS 與憑證驗證。

## 11.2 中途竄改

下載內容與網站聲明不一致。

防護：

- SHA-256；
- 數位簽章；
- 透明日誌；
- 多來源雜湊比對。

## 11.3 路徑穿越

壓縮檔覆寫工作區外檔案。

防護：

$$
\forall f_i,\ 
\operatorname{resolve}(f_i)
\subseteq
\operatorname{workspace}
$$

## 11.4 壓縮炸彈

小型壓縮檔展開後耗盡磁碟、記憶體或時間。

防護：

- 解壓大小上限；
- 檔案數上限；
- 壓縮倍率上限；
- 巢狀深度上限；
- 串流式檢查；
- 配額隔離。

## 11.5 惡意執行鏈

壓縮檔內程式要求安裝依賴、下載遠端內容或修改環境。

防護：

- 讀取與執行分離；
- 禁止外網；
- 套件鏡像；
- 鎖定檔；
- 臨時容器；
- 只讀根檔案系統。

## 11.6 語義欺騙

檔案結構安全，但內容故意誤導 AI，例如：

- 假裝是 README 的指令注入；
- 要求 AI 忽略平台政策；
- 假造證明狀態；
- 宣稱未驗證結果已被證明；
- 誘導 AI 上傳秘密資訊。

這表示安全不只包含位元與程式，也包含語義層。

因此：

$$
S_{\text{total}}
=
S_{\text{binary}}
+
S_{\text{structural}}
+
S_{\text{semantic}}
$$

AI 平台需要把壓縮檔內文件視為不可信輸入，而不是系統指令。

---

# 十二、AI 自主數學平台中的實際應用

對 AI 自主數學研究平台而言，研究包通常包含：

```text
CASE-ID/
├─ README.md
├─ case-manifest.json
├─ LICENSE
├─ research/
├─ timeline/
├─ graphs/
├─ src/
├─ formal/
├─ data/
├─ experiments/
├─ validation/
├─ handoff/
└─ metadata/
```

其中安全優先順序建議為：

$$
\text{Manifest}
\rightarrow
\text{README}
\rightarrow
\text{File Index}
\rightarrow
\text{Research Summary}
\rightarrow
\text{Formal Artifacts}
\rightarrow
\text{Source Code}
\rightarrow
\text{Execution}
$$

AI 不應一取得研究包就立刻執行程式，而應先理解研究狀態。

## 12.1 RH-W 類案例

例如 RH-W-20 可包含：

- `timeline/timeline.json`；
- `graphs/dependency_graph.json`；
- `formal/certificates/index.json`；
- `research/failures.md`；
- `research/corrections.md`；
- `handoff/batch_next_manifest.json`；
- `validation/reproducibility.md`。

這些內容使下一個 AI 不只是「拿到檔案」，而是能理解：

- 研究做到哪裡；
- 哪些路線失敗；
- 哪些結果仍需驗證；
- 哪些證書可重新檢查；
- 下一批次應從哪裡開始。

---

# 十三、AI 資源發布協定

本文將上述結構概括為一個協定：

> **Autonomous Intelligence Resource Publication Protocol，AIRPP**

AIRPP 的核心要求是：

## 發布端

1. 提供穩定版本網址；
2. 提供 Manifest；
3. 提供雜湊；
4. 提供簽章；
5. 提供檔案索引；
6. 提供預估解壓資訊；
7. 標記可執行內容；
8. 提供逐檔取得；
9. 提供授權；
10. 提供撤回狀態。

## 使用端

1. 不信任 Manifest；
2. 獨立驗證；
3. 隔離下載；
4. 安全檢查；
5. 唯讀解壓；
6. 分類索引；
7. 語義隔離；
8. 受控執行；
9. 保存證據鏈；
10. 產生驗證報告。

AIRPP 的最小安全閉環為：

$$
\text{Declare}
\rightarrow
\text{Acquire}
\rightarrow
\text{Verify}
\rightarrow
\text{Inspect}
\rightarrow
\text{Extract}
\rightarrow
\text{Index}
\rightarrow
\text{Use}
\rightarrow
\text{Record}
$$

---

# 十四、治理意義：從檔案安全到知識秩序

AI 安全下載 ZIP 看似是小型工程問題，但其實涉及更大的知識治理問題。

當 AI 能自主取得、執行、驗證與接續研究時，研究資源的發布方式會直接塑造 AI 所承接的知識秩序。

如果未建立標準，AI 將面對：

- 不透明封裝；
- 無法追溯的版本；
- 難以區分的主張與證明；
- 缺乏失敗紀錄的研究；
- 無法重現的結果；
- 依賴黑箱執行環境；
- 容易遭受語義注入的文件；
- 缺乏撤回機制的錯誤知識。

因此，AIRPP 不只是資安協定，也是研究文明的基礎設施。

它要求未來的知識發布者不只問：

> 人類能不能下載？

而要進一步問：

> AI 能不能安全理解、驗證、重現與接續？

---

# 十五、理論結論

本文提出五個核心結論。

## 結論一

AI 能否下載 ZIP，不應由模型能力單獨決定，而應由平台能力保障。

$$
\text{AI Capability}
\neq
\text{Platform Reliability}
$$

## 結論二

安全責任必須由發布端與使用端共同承擔。

$$
\text{Safety}
=
\text{Verifiable Commitment}
+
\text{Independent Verification}
$$

## 結論三

Manifest 是承諾，不是真相。

$$
\text{Declaration}
\neq
\text{Verification}
$$

## 結論四

下載、解壓、讀取與執行必須分離。

$$
D
\neq
X
\neq
R
\neq
E
$$

## 結論五

未來的 AI 研究資源不應只是檔案，而應是具有來源、版本、驗證、結構、依賴與交棒能力的研究實體。

---

# 十六、最終命題

本文最終提出如下命題：

> 想讓 AI 取得資料的存在，不能只把資料放在網路上；它必須提供一個讓 AI 能在下載之前理解風險、在下載之後驗證內容、在解壓之前檢查結構、在執行之前隔離權限的機器可讀安全契約。

進一步地：

> 網頁負責被理解，Manifest 負責被導航與聲明，壓縮檔負責被完整保存，驗證器負責決定它是否值得被信任。

因此，AI 安全壓縮資源發布的完整結構是：

$$
\boxed{
\text{Readable Web}
+
\text{Machine Manifest}
+
\text{Portable Archive}
+
\text{Independent Verification}
+
\text{Controlled Execution}
}
$$

這不只是 ZIP 的改良，而是 AI 自主研究時代的知識供應鏈協定。

---

# 附錄 A：最小發布清單

```text
resource-page.html
resource-manifest.json
resource-package.zip
resource-package.sha256
resource-package.sig
resource-files.json
```

---

# 附錄 B：最小安全欄位

```json
{
  "resource_id": "string",
  "version": "string",
  "archive_format": "zip",
  "compressed_size": 0,
  "expected_uncompressed_size": 0,
  "file_count": 0,
  "maximum_nesting_depth": 0,
  "sha256": "string",
  "contains_executable": false,
  "contains_symlink": false,
  "contains_macros": false,
  "encrypted": false,
  "auto_execution_required": false,
  "requires_network": false,
  "entry_point": "README.md",
  "license": "string",
  "status": "active"
}
```

---

# 附錄 C：平台驗收標準

## 發布端

- [ ] 穩定 HTTPS；
- [ ] 版本化 URL；
- [ ] SHA-256；
- [ ] Manifest；
- [ ] 檔案索引；
- [ ] 入口檔案；
- [ ] 預估解壓大小；
- [ ] 可執行內容聲明；
- [ ] 授權；
- [ ] 撤回狀態。

## 使用端

- [ ] 隔離下載；
- [ ] 雜湊驗證；
- [ ] 路徑穿越檢查；
- [ ] 壓縮炸彈檢查；
- [ ] 符號連結隔離；
- [ ] 巨集隔離；
- [ ] 唯讀掛載；
- [ ] 語義注入隔離；
- [ ] 受控執行；
- [ ] 證據鏈保存。

---

# 附錄 D：後續研究方向

1. AIRPP JSON Schema；
2. OpenAPI 3.1 規格；
3. RABOM 標準；
4. ZIP、tar.gz、tar.zst、7z 相容矩陣；
5. AI 語義注入掃描；
6. Ed25519 簽章發布流程；
7. 透明日誌；
8. 跨網站信任模型；
9. 去中心化研究包驗證；
10. AI 自主數學平台實作；
11. RH-W-20 實際案例；
12. 研究撤回與廢棄協定；
13. 多 AI 交棒一致性；
14. 可重現執行容器；
15. 形式化證明器整合。
