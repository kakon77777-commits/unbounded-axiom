# 從畫布到自編譯工作台：RABCL 統合總論與 MVP 前置邊界

## From Canvas to a Self-Compiling Workbench: RABCL Synthesis and Pre-MVP Boundaries

**系列名稱：** 遞歸自適應積木組合語言（Recursive Adaptive Block Composition Language, RABCL）  
**系列編號：** EML-RABCL-2026-07  
**作者：** Neo.K（許筌崴）with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1 系列統合稿  
**日期：** 2026 年 7 月 30 日  
**文件定位：** RABCL 系列封頂、統一架構、可編譯工作台、最小工程邊界、MVP 驗收基準  

---

## 摘要

RABCL 系列的起點是一個簡單但具有結構性後果的觀察：節點式工作流不必是最終形式。一組經由人類或 AI 連接、形成相對完整功能的節點，可以先進入局部靜止狀態，再由系統推斷其邊界、端口、契約、狀態、副作用、權限與來源，經過驗證後封裝成新的高階積木。該積木可以被命名、保存、引用、執行、展開、版本化、再次組合，並透過 AEREC 生成具有證據的候選實現。

前六篇分別建立：連線即封裝總命題、封裝靜止屏障、工作流函數化、遞歸閉包積木語言、格子語言—CAIR—MSSP—RDR 接合，以及 AEREC 驅動的演化積木。本文作為系列第七篇，不再新增平行理論，而是將上述概念收斂成一條完整生命週期：

$$
\boxed{
\text{Edit}
\rightarrow
\text{Quiesce}
\rightarrow
\text{Infer}
\rightarrow
\text{Validate}
\rightarrow
\text{Commit}
\rightarrow
\text{Index}
\rightarrow
\text{Materialize}
\rightarrow
\text{Execute}
\rightarrow
\text{Observe}
\rightarrow
\text{Evolve}
}
$$

本文將「自編譯工作台」嚴格定義為：一個能把使用者在多種操作表面上形成的工作流，轉換為具有權威結構、可檢查契約、穩定身分、精確版本、可執行 Runtime 與可回復演化歷史的系統。它不是指畫布在沒有權限、驗證與治理的情況下自行重寫正式軟體，也不是宣稱 AI 已能可靠理解任意工作流的全部隱藏語義。

RABCL 的統一架構由五層構成：

$$
\mathcal R
=
(
\mathcal U,
\mathcal A,
\mathcal I,
\mathcal X,
\mathcal E
),
$$

其中：

- $\mathcal U$ ：格子語言與畫布操作層；
- $\mathcal A$ ：CAIR 權威中介表示；
- $\mathcal I$ ：MSSP 能力索引與治理層；
- $\mathcal X$ ：RDR 執行與派發層；
- $\mathcal E$ ：AEREC 候選演化層。

五層不是五份平行真相。格子語言只提出操作；CAIR 是提交後的語義權威；MSSP 發布可發現的能力描述；RDR 只物化已核准精確版本；AEREC 的觀測與改寫只形成候選，不直接覆寫穩定權威。

本文進一步鎖定 MVP 的最小目標。第一版不實作完整 Agent OS、雲端多人協作、任意程式語言編譯、正式服務自主重寫或無人監督部署。MVP 只需證明：

$$
\boxed{
\text{一張有限工作流}
\rightleftarrows
\text{一個可版本化積木}
}
$$

且該往返具有：

1. 邊界與端口保存；
2. JSON Schema 或同等結構驗證；
3. CAIR 單一權威；
4. 原子提交；
5. 精確版本引用；
6. 本地可重播執行；
7. Trace 與效果帳本；
8. 候選分叉；
9. 人工核准提升；
10. 一鍵回切穩定版本。

本文最後建立 MVP 的物件模型、編譯階段、Runtime 模組、最小 UI、驗收測試、風險邊界與停止條件。系列至此完成基本概念封頂；下一階段不再增加同層理論，而應進入 RABCL MVP 的工程實作與實驗驗證。

**關鍵詞：** RABCL、自編譯工作台、工作流編譯、積木語言、格子語言、CAIR、MSSP、RDR、AEREC、版本化工作流、MVP

---

# 0. 系列封頂聲明

RABCL 系列共七篇：

1. 連線即封裝；
2. 封裝靜止屏障；
3. 工作流如何成為函數；
4. 遞歸閉包積木組合語言；
5. 權威結構與執行派發；
6. 演化積木；
7. 統合總論與 MVP 前置邊界。

前六篇分別解決不同缺口。第七篇的任務不是繼續橫向添加概念，而是回答三個收斂問題：

1. 七篇共同描述的系統究竟是什麼？
2. 哪些主張已經完成概念定義，哪些仍需工程證明？
3. 第一個 MVP 最少必須做什麼，最多只能做到哪裡？

本系列在本文後停止同層展開。後續若出現新問題，應被歸入：

- MVP 工程規格；
- 實驗報告；
- Runtime 白皮書；
- 安全與治理規格；
- 新的獨立理論系列。

不應再以「補概念」為名無限增加 RABCL 基礎篇章。

---

# 1. 統一問題：為何工作流需要升格

## 1.1 節點式工具的典型結構

一般工作流工具具有：

$$
\mathcal W
=
(V,E,L),
$$

其中：

- $V$ ：節點；
- $E$ ：連線；
- $L$ ：畫布布局。

使用者完成工作流後，系統通常保存節點、連線與座標。若支援群組或子流程，則再加入父子關係與折疊狀態。

這已足以實現：

- 可視化流程；
- 節點拖曳；
- 流程執行；
- 工作流模板；
- 群組與子流程。

但它沒有自然回答：

- 這張子圖的外部契約是什麼？
- 哪些資料是輸入，哪些是環境能力？
- 哪些狀態屬於積木，哪些狀態屬於外部系統？
- 它會產生哪些副作用？
- 它需要哪些權限？
- 它的語義版本與畫布布局版本是否相同？
- 展開後修改，何時形成新版本？
- 哪個版本正在被 Runtime 使用？
- 執行結果如何回到候選演化？

因此，單純把子圖放入父節點，只完成了視覺嵌套，沒有完成語義升格。

## 1.2 RABCL 的核心反轉

傳統模型是：

$$
\text{Primitive Nodes}
+
\text{Connections}
=
\text{Workflow}.
$$

RABCL 增加第二次轉換：

$$
\text{Workflow}
\xrightarrow{\text{compile}}
\text{New Primitive}.
$$

於是形成循環：

$$
\text{Primitive}
\rightarrow
\text{Workflow}
\rightarrow
\text{Higher-Order Primitive}
\rightarrow
\text{Higher-Order Workflow}
\rightarrow
\cdots
$$

這不是表示任意連線都自動生成新語言，而是表示：

> 經過受約束的封裝、驗證與提交後，組合結果可以重新進入合法積木集合。

令合法積木集合為 $\mathfrak B$ ，則：

$$
B_1,\ldots,B_n\in\mathfrak B
\land
\operatorname{ComposeOK}(B_1,\ldots,B_n)
\Rightarrow
\operatorname{Pack}(B_1,\ldots,B_n)\in\mathfrak B.
$$

這是受約束的相對閉包，不是無條件代數閉包。

---

# 2. 自編譯工作台的嚴格定義

## 2.1 「自編譯」不等於自行部署

本文將自編譯工作台定義為：

$$
\mathsf{SCW}
:
\mathcal P_{\mathrm{surface}}
\rightarrow
\mathcal P_{\mathrm{authority}}
\rightarrow
\mathcal P_{\mathrm{executable}}.
$$

其中：

- $\mathcal P_{\mathrm{surface}}$ ：畫布、表單、文字或 AI 操作形成的提案；
- $\mathcal P_{\mathrm{authority}}$ ：經驗證並提交的 CAIR；
- $\mathcal P_{\mathrm{executable}}$ ：由 RDR 物化的執行版本。

「自編譯」表示系統能協助或自動完成：

- 子圖辨識；
- 邊界推斷；
- 端口生成；
- Schema 生成；
- 契約草擬；
- 效果與權限列舉；
- CAIR 正規化；
- 驗證器執行；
- 版本與內容指紋建立；
- Runtime 註冊；
- 執行計畫生成。

它不表示系統可以自動：

- 核准高風險權限；
- 忽略不確定契約；
- 修改穩定版本；
- 將候選直接部署到正式環境；
- 把不可逆副作用當成測試；
- 宣稱任何 AI 推斷都正確。

因此：

$$
\boxed{
\text{Self-compiling}
\neq
\text{Self-authorizing}
\neq
\text{Self-deploying}
}
$$

## 2.2 工作台而非單一編譯器

RABCL 不是只把一種文字語言轉成機器碼。它需要同時處理：

- 視覺圖；
- 結構化表單；
- 契約；
- 狀態；
- 權限；
- Runtime 能力；
- Trace；
- 版本族；
- 演化證據。

因此它更接近多投影工作台：

$$
P^\ast
\xrightarrow{
\pi_{\mathrm{canvas}},
\pi_{\mathrm{text}},
\pi_{\mathrm{form}},
\pi_{\mathrm{runtime}},
\pi_{\mathrm{trace}}
}
\{
V_{\mathrm{canvas}},
V_{\mathrm{text}},
V_{\mathrm{form}},
V_{\mathrm{runtime}},
V_{\mathrm{trace}}
\}.
$$

所有投影都應來自同一 CAIR 權威，不能各自保存一份可漂移的核心語義。

---

# 3. 五層統一架構

## 3.1 格子語言／操作層

記為：

$$
\mathcal U.
$$

它負責：

- 畫布中的節點與連線；
- 任意區域選取；
- 群組與解組；
- 折疊與展開；
- 顯示端口；
- 編輯積木配置；
- 提交修改提案；
- 顯示驗證結果；
- 顯示版本與 Trace。

格子語言是操作表面，不是權威儲存。

其輸出應是操作：

$$
\delta_u
=
\operatorname{OperationProposal}.
$$

而不是直接改寫：

$$
P^\ast.
$$

## 3.2 CAIR／權威層

記為：

$$
\mathcal A.
$$

CAIR 至少包含：

$$
P^\ast
=
(
N,E,R,T,C,S,F,P,V,H
),
$$

其中：

- $N$ ：節點；
- $E$ ：邊；
- $R$ ：區域與封裝層級；
- $T$ ：型別與 Schema；
- $C$ ：契約；
- $S$ ：狀態模型；
- $F$ ：效果模型；
- $P$ ：權限與能力；
- $V$ ：驗證與證據；
- $H$ ：來源、版本與歷史。

CAIR 是提交後唯一語義權威。畫布位置可以是附屬表示，但不可用畫布座標決定核心語義。

## 3.3 MSSP／索引與治理層

記為：

$$
\mathcal I.
$$

MSSP 負責發布：

- 積木定義身分；
- 版本；
- 能力名稱；
- 類別；
- 摘要；
- 契約摘要；
- 輸入輸出；
- 依賴；
- 權限；
- 風險級別；
- 穩定狀態；
- 已核准環境；
- 內容指紋；
- 文件與測試入口。

MSSP 回答：

> 有哪些能力？它們是什麼？哪個版本可被誰使用？

它不保存每次執行中的動態狀態，也不自行執行積木。

## 3.4 RDR／執行派發層

記為：

$$
\mathcal X.
$$

RDR 接收：

$$
(
I_{\mathrm{def}},
I_{\mathrm{ver}},
h_{\mathrm{content}},
e_{\mathrm{runtime}}
)
$$

並完成：

- 精確版本解析；
- 能力與依賴綁定；
- 權限閘門；
- 執行計畫；
- 節點調度；
- 狀態載入；
- 效果攔截；
- Trace；
- 結果與錯誤回傳；
- 候選隔離；
- 版本入口切換。

RDR 不能在執行中無聲修改 CAIR。其觀測只能回寫成 Trace、指標或新提案。

## 3.5 AEREC／候選演化層

記為：

$$
\mathcal E.
$$

AEREC 接收：

$$
(
B_{\mathrm{stable}},
O,
G,
K,
\Pi
),
$$

其中：

- $O$ ：觀測；
- $G$ ：改善目標；
- $K$ ：硬限制；
- $\Pi$ ：政策。

輸出候選版本族：

$$
\{B_{c_1},\ldots,B_{c_m}\}.
$$

候選必須經過 CAIR 提交、證據生成、RDR 沙盒或影子執行，再由人工或政策批准提升。

因此統一架構為：

$$
\boxed{
\mathcal U
\xrightarrow{\text{proposal}}
\mathcal A
\xrightarrow{\text{publish}}
\mathcal I
\xrightarrow{\text{resolve/materialize}}
\mathcal X
\xrightarrow{\text{observe}}
\mathcal E
\xrightarrow{\text{candidate}}
\mathcal A
}
$$

---

# 4. 統一積木物件

## 4.1 積木定義

積木定義表示一種穩定能力：

$$
B_{\mathrm{def}}
=
(
I_{\mathrm{def}},
N,
D,
C_{\mathrm{family}},
G
),
$$

其中：

- $I_{\mathrm{def}}$ ：定義身分；
- $N$ ：名稱；
- $D$ ：描述；
- $C_{\mathrm{family}}$ ：契約族；
- $G$ ：治理政策。

## 4.2 積木版本

積木版本表示不可變實現：

$$
B_{\mathrm{ver}}
=
(
I_{\mathrm{ver}},
I_{\mathrm{def}},
h,
P^\ast,
C,
Z,
A
).
$$

其中：

- $h$ ：內容指紋；
- $P^\ast$ ：CAIR；
- $C$ ：契約版本；
- $Z$ ：證據包；
- $A$ ：適用環境。

## 4.3 積木實例

實例表示在某工作流中的使用：

$$
B_{\mathrm{inst}}
=
(
I_{\mathrm{inst}},
I_{\mathrm{ver}},
\theta,
S,
R_{\mathrm{bind}}
).
$$

其中：

- $\theta$ ：配置；
- $S$ ：實例狀態；
- $R_{\mathrm{bind}}$ ：外部端口與能力綁定。

## 4.4 積木執行

單次執行為：

$$
B_{\mathrm{run}}
=
(
I_{\mathrm{run}},
I_{\mathrm{inst}},
X,
\Gamma,
P,
Y,
S',
E,
T
).
$$

其中：

- $X$ ：輸入；
- $\Gamma$ ：環境能力；
- $P$ ：已授權權限；
- $Y$ ：輸出；
- $S'$ ：更新狀態；
- $E$ ：效果；
- $T$ ：Trace 與證據。

四層身分不能混用：

$$
I_{\mathrm{def}}
\neq
I_{\mathrm{ver}}
\neq
I_{\mathrm{inst}}
\neq
I_{\mathrm{run}}.
$$

---

# 5. 端到端生命週期

## 5.1 編輯態

使用者或 AI 在畫布建立：

$$
\mathcal W=(V,E).
$$

此時所有修改都屬於草稿，不具有正式執行權威。

## 5.2 候選封裝

封裝候選可以由：

- 使用者框選；
- 明確「封裝」指令；
- AI 建議；
- 重用頻率；
- 拓撲完整性；
- 任務完成標記；

觸發。

但：

$$
\mathsf{Connect}
\rightarrow
\mathsf{Candidate},
$$

不是：

$$
\mathsf{Connect}
\rightarrow
\mathsf{AuthorityCommit}.
$$

## 5.3 封裝靜止

系統為候選區域建立局部屏障：

$$
\mathsf{EQB}
=
(
B_{\mathrm{scope}},
e_{\mathrm{epoch}},
Q_{\mathrm{inflight}},
S_{\mathrm{snapshot}},
L_{\mathrm{effect}}
).
$$

它必須：

- 固定候選邊界；
- 阻止新的衝突修改；
- 排空、取消或記錄在途操作；
- 形成因果一致快照；
- 建立效果帳本；
- 具有逾時與退出機制。

## 5.4 推斷

推斷器輸出：

$$
A
=
(
\partial B,
I,
O,
S,
\Gamma,
P,
E,
C,
U
),
$$

其中 $U$ 是不確定性與歧義。

AI 可以提出推斷，但不得隱藏不確定性：

$$
U_i
=
(
\text{field},
\text{candidates},
\text{confidence},
\text{reason}
).
$$

## 5.5 正規化

工作流被轉為 CAIR：

$$
\mathsf{Lower}_{\mathrm{CAIR}}
:
\mathcal W
\rightarrow
P^\ast.
$$

正規化包括：

- 穩定節點 ID；
- 邊排序；
- 型別展開；
- 顯式能力導入；
- 顯式效果；
- 顯式狀態；
- 循環標記；
- 來源；
- 移除純布局差異。

## 5.6 驗證

最低驗證為：

$$
V_{\min}
=
V_{\mathrm{schema}}
\land
V_{\mathrm{graph}}
\land
V_{\mathrm{contract}}
\land
V_{\mathrm{permission}}
\land
V_{\mathrm{replay}}.
$$

高風險積木還需：

- 效果沙盒；
- 狀態遷移；
- 安全政策；
- 統計品質；
- 人工審查。

## 5.7 原子提交

只有全部必要驗證完成，才進行：

$$
\operatorname{Commit}
(
P_{\mathrm{draft}},
P^\ast_{\mathrm{new}}
).
$$

提交必須全部成功或全部失敗：

$$
\operatorname{Commit}
\in
\{
\text{ALL},
\text{NONE}
\}.
$$

MVP 可利用本地交易資料庫實現此性質。SQLite 官方文件將原子提交描述為單一交易中的變更全部發生或全部不發生，即使程序、作業系統或電源中斷亦維持交易語義。這類機制適合用於 CAIR 版本、索引指標與提交紀錄的本地原子更新。

## 5.8 索引發布

MSSP 從已提交 CAIR 產生索引：

$$
\mathsf{PublishIndex}
:
P^\ast
\rightarrow
M_B.
$$

索引是衍生物，可以重建。若索引損壞，不得反向覆寫 CAIR。

## 5.9 執行物化

RDR 解析精確版本：

$$
\mathsf{Resolve}
(
I_{\mathrm{def}},
I_{\mathrm{ver}},
h
)
=
P^\ast_v.
$$

再建立執行計畫：

$$
X_v
=
\mathsf{Materialize}
(
P^\ast_v,
e,
\Gamma,
P
).
$$

## 5.10 觀測與演化

執行產生：

$$
T_{\mathrm{run}}
=
(
\text{trace},
\text{metrics},
\text{logs},
\text{effects},
\text{errors}
).
$$

OpenTelemetry 將 traces、metrics 與 logs 視為可被產生、收集與匯出的遙測訊號，並以 Context／Span 等結構追蹤分散式請求路徑。RABCL MVP 不必實作完整 OpenTelemetry 生態，但應採用相容的 Trace ID、Span、事件及狀態觀念，避免自創無法擴展的執行紀錄格式。

觀測只能形成：

$$
T_{\mathrm{run}}
\rightarrow
O
\rightarrow
B_{\mathrm{candidate}},
$$

不能直接形成：

$$
T_{\mathrm{run}}
\rightarrow
\operatorname{Mutate}(B_{\mathrm{stable}}).
$$

---

# 6. 編譯管線

RABCL 編譯器可以被拆為九階段：

$$
\mathcal C_{\mathrm{RABCL}}
=
C_0\circ C_1\circ\cdots\circ C_8.
$$

## $C_0$ ：捕捉

將畫布操作轉為草稿圖與操作日誌。

## $C_1$ ：劃界

識別封裝區域與跨界邊。

## $C_2$ ：靜止

建立局部一致快照與 epoch。

## $C_3$ ：介面推斷

推斷端口、型別、能力、狀態與效果。

## $C_4$ ：契約合成

生成前置條件、後置條件、不變量、錯誤與政策要求。

## $C_5$ ：CAIR 正規化

把異質節點轉為統一 IR。

## $C_6$ ：驗證

執行 Schema、圖、契約、權限與重播測試。

## $C_7$ ：提交與索引

建立不可變版本、指紋及 MSSP 索引。

## $C_8$ ：物化

生成 RDR 執行計畫與可呼叫入口。

整體可表示為：

$$
\mathsf{Compile}
(
\mathcal W,
\Pi
)
=
\begin{cases}
B_v, & V_{\min}=1,\\
\operatorname{NeedsReview}(U), & U>\tau,\\
\operatorname{Rejected}(R), & \text{unsafe or invalid}.
\end{cases}
$$

---

# 7. RABCL 與既有工程模型的關係

## 7.1 WebAssembly Component Model

WebAssembly Component Model 以機器可讀介面描述 imports 與 exports，允許元件包含子元件，並把相容元件組合成新的同類元件。其官方文件明確指出：若一個元件的 import 可由另一元件的 export 滿足，便能形成新的組合元件；組合可重複進行。

這為 RABCL 的兩個主張提供工程對照：

1. 介面相容是組合成立的前提；
2. 組合結果可以再次成為同類可組合單元。

但 RABCL 另處理：

- AI 推斷接口；
- 畫布折疊與展開；
- 狀態與效果契約；
- 權威版本與索引；
- AEREC 演化候選；
- 人工治理與回滾。

因此 RABCL 不等同 WebAssembly Component Model，也不應在 MVP 中試圖重建其 ABI。第一版只需借鑑其介面與組合原則。

## 7.2 MLIR

MLIR 的 Operation Definition Specification 將 operation 的 operands、results、attributes、traits、constraints 與文件集中於結構化規範，並讓工具生成部分實現與驗證邏輯。MLIR 也以 operation 作為轉換與抽象的重要單位。

RABCL 可借鑑：

- operation／積木的單一結構描述；
- traits 與效果屬性；
- 驗證器；
- rewrite pass；
- dialect／節點類型擴展。

但 MVP 不需要直接依賴 MLIR。CAIR 可先採用 JSON/YAML 序列化的圖 IR，以便快速驗證概念。

## 7.3 JSON Schema

JSON Schema 是描述並驗證 JSON 結構、限制與資料類型的宣告式語言，其規格分為 Core 與 Validation。RABCL MVP 可用它驗證：

- 積木清單；
- 節點配置；
- 端口；
- 契約；
- 狀態；
- Trace；
- 版本中介資料。

JSON Schema 只能驗證結構與部分條件，不能取代行為、權限與效果驗證。

## 7.4 React Flow／XYFlow

React Flow 支援節點、邊、父子節點與 sub-flow／grouping。官方文件把 sub flow 描述為節點內部的 flow，並允許子圖連接外部節點。

它適合 MVP 的視覺操作層，因為不必從零實作畫布互動。但 React Flow 中的父節點與群組仍只是 UI／圖結構能力。RABCL 必須在其上增加：

- 語義封裝；
- CAIR；
- 契約；
- 版本；
- Runtime；
- 驗證；
- 回滾。

因此選用畫布函式庫不等於已實現 RABCL。

## 7.5 Temporal 與耐久執行

Temporal 的官方文件強調工作流可在程序崩潰、網路故障或基礎設施中斷後從原位置恢復。這對未來長時間積木具有價值。

但第一版 MVP 不需要引入完整耐久工作流平台。可先使用本地事件日誌與可重播步驟，證明：

- 執行歷史可保存；
- 失敗可定位；
- 無副作用節點可重播；
- 有副作用節點需要冪等鍵或效果帳本。

---

# 8. 最小可行產品的核心命題

MVP 不是要證明「AI 可以自動開發所有軟體」。它只需證明：

> 一張有限、可觀測、低風險工作流，可以經過封裝編譯，成為一個具有穩定身分、契約、權威版本、執行入口與往返展開能力的新積木。

形式化驗收為：

$$
\exists \mathcal W,B_v:
\quad
\mathsf{Compile}(\mathcal W)=B_v,
$$

$$
\mathsf{Execute}(B_v,x)=r,
$$

$$
\mathsf{Expand}(B_v)=\mathcal W',
$$

且：

$$
\mathcal W'\equiv_C\mathcal W.
$$

再加上候選版本：

$$
B_v
\xrightarrow{\mathsf{fork}}
B_c
\xrightarrow{\mathsf{approve}}
B_{v+1},
$$

以及：

$$
\mathsf{rollback}(B_{v+1})=B_v.
$$

若以上成立，RABCL 的基本工程命題即獲得初步支持。

---

# 9. MVP 的唯一示範案例

第一版應只選一個低風險、容易觀察、具有明確輸入輸出的案例。建議使用：

> **文字處理與檔案輸出工作流**

例如：

```text
讀取 Markdown
→ 擷取標題與段落
→ 套用轉換規則
→ 產生摘要
→ 驗證輸出 Schema
→ 儲存結果
```

其優點：

- 不必依賴高成本模型；
- 可提供純規則與 AI 節點；
- 輸入輸出容易比較；
- 檔案效果可放入沙盒；
- 可演示權限；
- 可演示冪等鍵；
- 可演示失敗；
- 可演示重新執行；
- 可演示封裝與再使用。

第一版不應同時做圖片、影片、聲音、網頁發布、郵件與資料庫寫入。多模態可在基礎閉環穩定後加入。

---

# 10. MVP 最小物件模型

## 10.1 NodeSpec

```yaml
node:
  id: node.normalize_text
  kind: transform
  version: 0.1.0
  inputs:
    - name: source
      schema: text
  outputs:
    - name: normalized
      schema: text
  capabilities: []
  effects: []
  executor:
    type: python
    entry: rabcl_nodes.text.normalize
```

## 10.2 EdgeSpec

```yaml
edge:
  id: edge.001
  source:
    node: node.read_file
    port: content
  target:
    node: node.normalize_text
    port: source
  mode: data
```

## 10.3 BlockContract

```yaml
contract:
  id: contract.markdown_summary
  version: 0.1.0
  inputs:
    source_file:
      schema_ref: schema.file_ref
  outputs:
    summary_file:
      schema_ref: schema.file_ref
  capabilities:
    - fs.read:sandbox
    - fs.write:sandbox
  effects:
    - kind: file.write
      reversible: true
      scope: sandbox
  errors:
    - invalid_input
    - permission_denied
    - node_failed
  invariants:
    - output_must_exist
    - output_must_validate
```

## 10.4 BlockVersion

```yaml
block_version:
  definition_id: block.markdown_summary
  version_id: 0.1.0
  content_hash: sha256:...
  cair_uri: local://objects/sha256/...
  contract_ref: contract.markdown_summary@0.1.0
  status: stable
  parent_versions: []
  evidence:
    schema: passed
    graph: passed
    replay: passed
```

## 10.5 RunRecord

```yaml
run:
  run_id: run_...
  block_version: block.markdown_summary@0.1.0
  input_hash: sha256:...
  status: succeeded
  started_at: ...
  completed_at: ...
  trace_id: ...
  effects:
    - kind: file.write
      target: sandbox/output/summary.md
      result: committed
```

上述格式只是 MVP 建議，不是最終標準。

---

# 11. MVP 最小模組

## 11.1 Canvas

功能：

- 新增節點；
- 連接端口；
- 刪除與移動；
- 框選；
- 建立群組；
- 封裝；
- 展開；
- 顯示驗證錯誤；
- 顯示版本與執行狀態。

可使用 React Flow／XYFlow 或同類函式庫實作。

## 11.2 Draft Store

保存：

- 草稿圖；
- UI 布局；
- 未提交操作；
- 選取區域；
- AI 建議；
- 驗證錯誤。

草稿不能被 Runtime 直接當成穩定版本。

## 11.3 EQB Manager

實作：

- 候選區域鎖；
- epoch；
- 在途執行檢查；
- 快照；
- 逾時；
- 取消；
- 解除屏障。

MVP 只需支援局部邏輯靜止，不需分散式全域快照。

## 11.4 Inference Engine

第一版只需半自動：

- 根據跨界邊推斷資料端口；
- 根據節點宣告聚合能力；
- 根據節點效果聚合副作用；
- 根據內部狀態宣告生成狀態摘要；
- AI 草擬名稱與描述；
- 歧義要求人工確認。

不要讓 AI 憑自然語言猜測未宣告效果。

## 11.5 CAIR Store

最低需求：

- 內容定址物件；
- 不可變版本；
- 父版本；
- 交易提交；
- 內容指紋；
- 讀取與展開；
- 差異；
- 回切指標。

本地 SQLite 加檔案內容儲存即可。

## 11.6 Validator

最低驗證器：

- JSON Schema；
- 節點 ID 唯一；
- 邊端口存在；
- 端口型別相容；
- 必要輸入已連接；
- 禁止未標記循環；
- 能力與效果已宣告；
- 沙盒路徑；
- 重播測試。

## 11.7 MSSP Index

提供：

- 積木清單；
- 搜尋；
- 定義與版本；
- 狀態；
- 契約摘要；
- 證據摘要；
- 精確內容指紋。

## 11.8 RDR Local Runtime

第一版只需：

- DAG 拓撲排序；
- 節點執行；
- 輸入輸出傳遞；
- 錯誤中止；
- Trace；
- 效果攔截；
- 精確版本載入；
- 低風險檔案沙盒。

不需要分散式排程、容器編排或多租戶。

## 11.9 Evolution Lab

最低功能：

- 從穩定版分叉；
- 手工或 AI 改寫候選；
- 比較 CAIR diff；
- 執行同一測試集；
- 顯示 benchmark；
- 人工提升；
- 一鍵回切；
- 保存拒絕原因。

第一版 AEREC 不需自主多代循環。

---

# 12. MVP 最小 UI

整個 MVP 可以只有五個主要畫面。

## 12.1 畫布

建立、連接、框選、封裝與展開。

## 12.2 積木檢查器

顯示：

- 名稱；
- 輸入輸出；
- 契約；
- 能力；
- 效果；
- 狀態；
- 歧義；
- 驗證錯誤。

## 12.3 版本頁

顯示：

- 穩定版本；
- 候選版本；
- 父子關係；
- 內容指紋；
- 差異；
- 證據；
- 提升與回切。

## 12.4 執行頁

顯示：

- 輸入；
- 節點進度；
- Trace；
- 輸出；
- 錯誤；
- 效果帳本。

## 12.5 積木庫

搜尋已提交積木並拖回畫布。

不需要一開始實作社群市集、模板商店或雲端註冊中心。

---

# 13. 驗收測試

## 13.1 封裝往返

建立三節點工作流，封裝為積木，展開後：

$$
\operatorname{HashSemantic}
(
\mathsf{Expand}(B)
)
=
\operatorname{HashSemantic}(\mathcal W).
$$

布局可以不同，語義必須一致。

## 13.2 邊界推斷

跨界輸入與輸出應被正確生成為積木端口。

## 13.3 隱藏能力拒絕

若節點需要檔案寫入但未宣告：

$$
\operatorname{Compile}(\mathcal W)
=
\operatorname{Rejected}.
$$

## 13.4 原子提交

模擬提交中斷後，系統只能看到舊穩定版或完整新版本，不得看到半提交版本。

## 13.5 精確重播

同一穩定版本、同一確定性輸入及同一環境，應產生同一結果或同一契約等價結果。

## 13.6 積木再組合

已封裝積木應能像原子節點一樣與其他節點連接，再次封裝成更高階積木。

## 13.7 候選隔離

候選執行不得改變穩定版本入口或正式沙盒輸出。

## 13.8 版本提升

候選通過測試並經人工核准後，穩定指標切換到新版本。

## 13.9 一鍵回切

回切後新執行使用舊版本，既有版本歷史與失敗證據仍保留。

## 13.10 停止條件

連續多次候選沒有超過改善門檻時，Evolution Lab 應停止建議繼續演化。

MVP 完成條件可寫成：

$$
A_{\mathrm{MVP}}
=
\bigwedge_{i=1}^{10}T_i.
$$

---

# 14. 安全與治理最低線

## 14.1 預設拒絕能力

所有外部能力必須顯式導入：

$$
\Gamma_{\mathrm{allowed}}
\subseteq
\Gamma_{\mathrm{declared}}.
$$

未宣告能力一律拒絕。

## 14.2 效果隔離

MVP 只允許：

- 沙盒檔案讀取；
- 沙盒檔案寫入；
- 無副作用純計算；
- 可攔截的模型呼叫模擬。

不允許：

- 寄送真實郵件；
- 公開發布；
- 付款；
- 系統管理；
- 任意命令列；
- 任意網路存取；
- 修改使用者正式檔案。

## 14.3 AI 權限

AI 可以：

- 建議封裝；
- 草擬契約；
- 產生描述；
- 提出候選；
- 解釋錯誤。

AI 不可以：

- 自行核准權限；
- 隱藏歧義；
- 直接提升候選；
- 刪除失敗證據；
- 修改已提交版本；
- 關閉安全驗證器。

## 14.4 敏感資料

CAIR 與 Trace 不應保存：

- API Key；
- Token；
- 密碼；
- 私密檔案原文；
- 未遮蔽個人資料。

只保存秘密引用：

$$
\text{secret\_ref}
\neq
\text{secret\_value}.
$$

## 14.5 不完整推斷

若 AI 無法確認：

- 狀態所有權；
- 副作用；
- 權限；
- 錯誤語義；

則封裝狀態應是：

$$
\texttt{NEEDS\_REVIEW},
$$

而不是自動填補。

---

# 15. MVP 明確不做什麼

第一版不做：

1. 完整 Agent OS；
2. 多人即時協作；
3. 雲端市場；
4. 手機端；
5. 任意語言編譯；
6. 自動容器部署；
7. Kubernetes 整合；
8. 真實金融或商業副作用；
9. 任意網路爬取；
10. 多模態影音管線；
11. 無人監督候選提升；
12. 自主修改 Runtime；
13. 自主更新驗證器；
14. 任意狀態 Schema 逆遷移；
15. 形式證明所有工作流等價；
16. 大型分散式系統；
17. 高可用與災難復原；
18. 插件商店；
19. 自訂完整程式語言語法；
20. 宣稱通用人工智能或自我進化軟體已完成。

這些不是永遠排除，而是為了讓 MVP 的可證偽問題保持清楚。

---

# 16. 建議實作路線

## M0：資料模型

完成：

- NodeSpec；
- EdgeSpec；
- BlockContract；
- CAIR；
- BlockVersion；
- RunRecord；
- JSON Schema；
- SQLite 交易提交。

驗收：手工 JSON 工作流可被驗證、提交與讀回。

## M1：本地 Runtime

完成：

- 三至五種節點；
- DAG 執行；
- Trace；
- 錯誤；
- 沙盒檔案效果。

驗收：手工 CAIR 可重播執行。

## M2：畫布

完成：

- 節點；
- 邊；
- 端口；
- 框選；
- 群組；
- 匯入／匯出。

驗收：畫布可生成與載入同一 CAIR 草稿。

## M3：封裝編譯

完成：

- EQB；
- 跨界邊推斷；
- 積木端口；
- 契約草稿；
- 驗證；
- 原子提交；
- 折疊／展開。

驗收：三節點工作流可往返為一個積木。

## M4：積木庫與再組合

完成：

- MSSP 本地索引；
- 搜尋；
- 拖入；
- 實例化；
- 高階再封裝。

驗收：已封裝積木可被另一工作流使用。

## M5：受控演化

完成：

- 候選分叉；
- CAIR diff；
- 同測試集比較；
- 人工提升；
- 回切；
- 負知識。

驗收：候選失敗不影響穩定版；候選成功可提升並可回切。

只有 M0–M5 全部成立，才能說 RABCL MVP 完成。

---

# 17. 可證偽研究問題

RABCL 不應只以「介面看起來能用」作為成功。MVP 至少要回答：

## 問題一：封裝是否降低重用成本？

比較：

$$
C_{\mathrm{reuse}}(\text{expanded workflow})
$$

與：

$$
C_{\mathrm{reuse}}(\text{encapsulated block}).
$$

## 問題二：AI 端口推斷正確率如何？

建立人工標註工作流集合，測量：

- Precision；
- Recall；
- 歧義校準；
- 隱藏能力漏報率。

## 問題三：往返是否保持語義？

測量：

$$
\mathsf{Collapse}
(
\mathsf{Expand}(B)
)
\equiv_C B.
$$

## 問題四：權威分層是否減少漂移？

比較只有畫布 JSON 的系統與 CAIR 單一權威系統，在多次編輯後的：

- 索引漂移；
- Runtime 漂移；
- 版本不可重現率。

## 問題五：候選隔離是否降低正式風險？

測量失敗候選能否在不污染穩定版、正式輸出與版本入口的情況下完成測試。

## 問題六：停止政策是否避免版本爆炸？

比較有無停止條件時的：

- 候選數量；
- 驗證成本；
- 淨收益；
- 重複失敗比例。

若 MVP 無法在有限案例中證明上述關係，RABCL 需要修訂，而不是以更大的理論敘事掩蓋失敗。

---

# 18. 主要失敗模式

## 18.1 過度封裝

任何小子圖都被封裝，造成積木數量爆炸。

對策：

- 重用門檻；
- 最小功能完整性；
- 使用者核准；
- 去重與相似性提示。

## 18.2 黑盒化

折疊後使用者看不到內部風險。

對策：

- 能力與效果摘要；
- 一鍵展開；
- Trace；
- 契約差異；
- 版本來源。

## 18.3 AI 過度自信

AI 把不確定副作用推斷成無副作用。

對策：

- 宣告優先；
- 靜態掃描；
- Runtime 攔截；
- 不確定即審查；
- 未宣告即拒絕。

## 18.4 CAIR 過度複雜

試圖在第一版表示所有語言與所有 Runtime。

對策：

- 只支援有限節點；
- 小型型別系統；
- 明確版本；
- 可擴展欄位；
- 不追求通用編譯器。

## 18.5 畫布成為第二真相

UI 自行保存語義欄位，與 CAIR 不一致。

對策：

- 投影生成；
- 操作提案；
- 提交後重載；
- 語義欄位禁止直接存在 UI 私有狀態。

## 18.6 候選污染正式狀態

候選寫入相同檔案或共享狀態。

對策：

- 沙盒命名空間；
- 候選專用效果帳本；
- 只讀輸入；
- 明確提升前不切換指標。

## 18.7 版本號等同內容

版本標籤相同但內容不同。

對策：

$$
\text{version label}
+
\text{content hash}.
$$

## 18.8 無限演化

AEREC 不斷產生微小候選。

對策：

- 預算；
- 淨收益門檻；
- 連續退化停止；
- 震盪檢測；
- 人工凍結。

---

# 19. 系列統一命題

## 命題一：工作流展開態命題

工作流可以是高階積木形成前的展開表示，而非最終語言形式。

## 命題二：封裝事務命題

工作流升格必須經過局部靜止、一致快照、推斷、驗證及原子提交。

## 命題三：契約函數命題

RABCL 積木不是被偽裝成純函數的黑盒，而是具有顯式狀態、環境、權限、效果與證據的契約呼叫單元：

$$
F_B:
(X,S,\Gamma,P)
\rightarrow
(Y,S',E,T).
$$

## 命題四：受約束閉包命題

合法積木只有在型別、契約、效果、權限、版本與治理相容時，組合結果才仍屬合法積木集合。

## 命題五：單一權威命題

畫布、索引、Runtime 與演化觀測不得各自成為語義真相；CAIR 是已提交版本的唯一權威表示。

## 命題六：精確派發命題

RDR 必須根據定義、版本及內容指紋解析實現，不得以模糊 `latest` 直接保證可重現執行。

## 命題七：候選隔離命題

AEREC 的任何改寫都先形成候選版本，不能原地修改穩定積木。

## 命題八：證據提升命題

候選只有在必要證據集合、契約保持及部署風險條件成立時才能提升。

## 命題九：回滾拓撲命題

回滾包含版本指標、狀態、效果補償、前向修復與圍堵，而不是單一「上一版」。

## 命題十：停止必要命題

若沒有淨收益、證據不足、風險超限、契約漂移或版本震盪，演化必須停止。

## 命題十一：自編譯非自授權命題

系統可以自動生成與驗證候選結構，但高風險權限、正式提升與不可逆效果仍需獨立治理。

## 命題十二：MVP 可證偽命題

RABCL 的基本有效性應由有限工作流的封裝往返、可執行性、可重現性、候選隔離與回切能力驗證，而不是由概念規模或介面美觀判定。

---

# 20. RABCL 的最終統合公式

RABCL 的靜態結構可表示為：

$$
\boxed{
\mathcal R
=
\mathcal U
\oplus
\mathcal A
\oplus
\mathcal I
\oplus
\mathcal X
\oplus
\mathcal E
}
$$

其中 $\oplus$ 表示具有明確接口的分工組合，而不是本體同一。

其編譯生命週期為：

$$
\boxed{
\mathcal W
\xrightarrow{\mathsf{EQB}}
\mathcal W_q
\xrightarrow{\mathsf{Infer}}
C_B
\xrightarrow{\mathsf{Lower}}
P^\ast
\xrightarrow{\mathsf{Validate}}
Z
\xrightarrow{\mathsf{Commit}}
B_v
\xrightarrow{\mathsf{Index}}
M_B
\xrightarrow{\mathsf{Materialize}}
X_B
}
$$

其執行與演化循環為：

$$
\boxed{
X_B
\xrightarrow{\mathsf{Run}}
T
\xrightarrow{\mathsf{Observe}}
O
\xrightarrow{\mathsf{AEREC}}
\{B_c\}
\xrightarrow{\mathsf{Verify/Approve}}
B_{v+1}
}
$$

其核心往返為：

$$
\boxed{
\mathsf{Collapse}
(
\mathsf{Expand}(B_v)
)
\equiv_C
B_v
}
$$

其治理邊界為：

$$
\boxed{
\text{AI may propose and compile;}
\quad
\text{authority, permission, and promotion remain governed.}
}
$$

---

# 結論

RABCL 的基本想法可以用一句話收斂：

> 一組已形成穩定功能的節點與連線，不只可以被保存為工作流，也可以經過受約束編譯，升格為新的可組合語言單元。

這個升格需要的不只是畫布群組，而是完整生命週期：

$$
\boxed{
\text{連線}
\rightarrow
\text{局部靜止}
\rightarrow
\text{邊界與契約推斷}
\rightarrow
\text{CAIR 權威提交}
\rightarrow
\text{MSSP 發布}
\rightarrow
\text{RDR 執行}
\rightarrow
\text{AEREC 候選演化}
}
$$

至此，RABCL 已完成其基本概念：

- 工作流不是終局；
- 積木不是視覺群組；
- 函數不是隱藏副作用的黑盒；
- 遞歸不是單一概念；
- 畫布不是權威；
- Runtime 不是治理者；
- 演化不是原地改寫；
- 回滾不是單一版本按鈕；
- 自編譯不是自授權；
- 持續演化必須能停止。

下一階段應停止新增同層總論，直接進入 MVP。第一個 MVP 的目標不是打造完整 AI 原生軟體世界，而是完成一個可清楚驗收的有限閉環：

$$
\boxed{
\text{建立工作流}
\rightarrow
\text{封裝成積木}
\rightarrow
\text{拖回畫布再組合}
\rightarrow
\text{執行與追蹤}
\rightarrow
\text{產生候選}
\rightarrow
\text{人工提升或回切}
}
$$

只要這個閉環真正運作，RABCL 就不再只是對工作流未來形態的理論描述，而會成為一個可以被測試、被推翻、被修訂並持續工程化的系統原型。

---

# 參考資料

1. Bytecode Alliance, *The WebAssembly Component Model — Components, Interfaces, Worlds, and Composing Components*.  
   https://component-model.bytecodealliance.org/

2. LLVM Project, *MLIR Operation Definition Specification (ODS)* 與 *MLIR Language Reference*.  
   https://mlir.llvm.org/docs/DefiningDialects/Operations/  
   https://mlir.llvm.org/docs/LangRef/

3. OpenTelemetry Project, *Documentation, Signals, Traces, and Trace API*.  
   https://opentelemetry.io/docs/

4. JSON Schema, *Specification 2020-12: Core and Validation*.  
   https://json-schema.org/specification

5. SQLite, *Atomic Commit in SQLite* 與 *SQLite Is Transactional*.  
   https://www.sqlite.org/atomiccommit.html  
   https://www.sqlite.org/transactional.html

6. XYFlow, *React Flow Sub Flows, Nodes, Edges, and Building a Flow*.  
   https://reactflow.dev/

7. Temporal, *Temporal Platform Documentation*.  
   https://docs.temporal.io/

8. Neo.K／Aletheia，RABCL 系列第 01–06 篇。

9. Neo.K／EveMissLab，AEREC、格子語言、CAIR、MSSP × RDR 相關文件。
