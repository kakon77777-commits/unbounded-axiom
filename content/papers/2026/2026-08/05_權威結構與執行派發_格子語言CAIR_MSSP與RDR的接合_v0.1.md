# 權威結構與執行派發：格子語言、CAIR、MSSP × RDR 的接合

## Authoritative Structure and Execution Dispatch: Integrating Grid Language, CAIR, MSSP, and RDR

**系列名稱：** 遞歸自適應積木組合語言（Recursive Adaptive Block Composition Language, RABCL）  
**系列編號：** EML-RABCL-2026-05  
**作者：** Neo.K（許筌崴）with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1 基礎接合稿  
**日期：** 2026 年 7 月 30 日  
**文件定位：** 權威中介表示、格子操作表面、能力索引、執行派發、版本物化、投影一致性與跨層接合  

---

## 摘要

RABCL 前四篇已建立工作流封裝、靜止屏障、函數化契約及遞歸閉包積木語言。然而，一個可折疊、可展開、可引用並可再次組合的積木，仍面臨一個決定系統能否長期維持一致性的核心問題：**畫布上的格子、權威結構、能力索引與 Runtime 執行物件，究竟哪一個才是真正的系統狀態？**

若格子畫布、CAIR、MSSP 與 RDR 各自保存一份完整且可修改的結構，系統將形成多重真相。畫布可能已刪除一條連線，但執行圖仍保留舊依賴；MSSP 索引可能宣告某積木可用，但 Runtime 尚未物化其版本；RDR 可能正在執行舊程式，而 AI 已把新候選結構寫入可視畫布。此時，畫面看似一致，實際語義、治理與執行卻已分裂。

本文提出 RABCL 的四層接合模型：

$$
\boxed{
\text{Grid Language}
\xrightarrow{\text{proposal}}
\text{CAIR}
\xrightarrow{\text{index}}
\text{MSSP}
\xrightarrow{\text{materialize/dispatch}}
\text{RDR}
}
$$

其中：

- **格子語言**是人類與 AI 的操作表面，負責選取、連接、折疊、展開、命名與提出修改；
- **CAIR** 是提交後的權威中介表示，保存節點、邊、端口、契約、狀態、效果、來源、版本與驗證結果；
- **MSSP** 是描述與能力索引平面，回答積木是什麼、屬於何處、提供什麼能力、依賴什麼以及由誰治理；
- **RDR** 是執行與物化平面，負責版本解析、能力綁定、依賴載入、權限閘門、派發、追蹤、回收與回滾。

本文主張：**CAIR 是唯一可提交的語義權威；其他三層均為受約束的投影、索引或物化結果。** 格子語言不得直接改寫執行物件；MSSP 不得把描述索引冒充運行狀態；RDR 不得把 Runtime 快取反向提升為定義真相。所有修改必須先形成候選差異，經驗證後原子提交為新的 CAIR 版本，再由 MSSP 更新能力索引，最後由 RDR 解析並物化指定版本。

在此架構下，畫布可以重新排版而不改變語義，MSSP 可以重建而不改變積木定義，RDR 可以針對不同裝置生成不同實現而不改變外部契約。其一致性條件可表示為：

$$
\operatorname{Sem}
\bigl(
\Pi_{\mathrm{grid}}(P^\ast)
\bigr)
\equiv_C
\operatorname{Sem}(P^\ast),
$$

以及：

$$
\operatorname{Obs}
\bigl(
\mathsf{Run}_{\mathrm{RDR}}(
\mathsf{Materialize}(P^\ast,v,e)
)
\bigr)
\models C(P^\ast).
$$

本文進一步建立定義身分、版本身分、索引身分與 Runtime 實例身分的分離；定義提案、權威提交、索引發布、執行物化及追蹤回寫五條資料路徑；以及權威唯一、投影可重建、索引可重建、物化可替換、執行可追溯與反向寫入受限等核心不變量。由此，RABCL 從單純的視覺積木工具，進一步成為具有明確控制平面與資料平面的 AI 原生可編譯工作台架構。

**關鍵詞：** CAIR、格子語言、MSSP、RDR、權威表示、單一真相、執行派發、物化、能力索引、投影、工作流、RABCL

---

# 0. 問題定位：四份結構如何避免變成四份真相

一個完整的 RABCL 工作台至少會同時存在下列對象：

1. 使用者眼前的畫布；
2. 可保存與驗證的結構表示；
3. 可供人類與 AI 搜尋的能力目錄；
4. Runtime 中真正被載入與呼叫的實現。

它們看起來都像「工作流」，但實際上回答不同問題：

| 層級 | 回答的問題 |
|---|---|
| 格子語言 | 使用者與 AI 現在如何觀察、選取與操作？ |
| CAIR | 系統經核准後究竟是什麼？ |
| MSSP | 這個能力位於何處、如何被認識與治理？ |
| RDR | 指定版本此刻如何被物化、綁定與執行？ |

若四者都能獨立修改，將產生：

$$
T_{\mathrm{grid}}
\neq
T_{\mathrm{CAIR}}
\neq
T_{\mathrm{MSSP}}
\neq
T_{\mathrm{RDR}},
$$

其中 $T$ 表示各層自認為的真相。

這種分裂並不一定立即報錯。更危險的情況是：畫布、索引與執行結果在多數時候看似一致，只在重播、回滾、多人協作、權限變更或 AEREC 演化時才暴露差異。

因此，本篇的根本問題是：

> 如何讓四層各有自由度，卻只保留一個可提交的語義權威？

---

# 1. 四層接合模型

## 1.1 格子語言：操作表面

格子語言負責把複雜結構投影成人類與 AI 可操作的格子、端口、連線、區域與層級。其主要操作包括：

$$
\mathcal O_{\mathrm{grid}}
=
\{
\mathsf{select},
\mathsf{connect},
\mathsf{disconnect},
\mathsf{collapse},
\mathsf{expand},
\mathsf{name},
\mathsf{annotate},
\mathsf{propose}
\}.
$$

格子語言可以保存視覺資料，例如：

- 座標；
- 尺寸；
- 顏色；
- 縮放；
- 展開狀態；
- 使用者自訂排列；
- 暫時選取與對焦。

但這些不應自動成為積木語義。

令畫布投影為：

$$
G
=
\Pi_{\mathrm{grid}}
(P^\ast,U,D),
$$

其中：

- $P^\ast$ ：CAIR 權威版本；
- $U$ ：使用者偏好與局部視圖；
- $D$ ：裝置與顯示條件。

因此，同一份 $P^\ast$ 可以有多個合法畫布投影：

$$
G_1\neq G_2,
$$

但：

$$
\operatorname{Sem}(G_1)
\equiv_C
\operatorname{Sem}(G_2)
\equiv_C
\operatorname{Sem}(P^\ast).
$$

## 1.2 CAIR：權威結構平面

CAIR 在本文中指一種**規範化、可驗證、可版本化的權威中介表示**。它不是特定序列化格式，也不要求第一版使用某種編譯器框架；它是一組系統職責。

其最低結構可表示為：

$$
P^\ast
=
(
N,E,R,T,C,S,X,P,H,Z,V
),
$$

其中：

- $N$ ：節點與積木定義；
- $E$ ：資料、控制、事件與能力邊；
- $R$ ：區域、封裝與層級；
- $T$ ：型別與 Schema；
- $C$ ：功能、效果、安全與資源契約；
- $S$ ：狀態模型；
- $X$ ：副作用與外部能力；
- $P$ ：權限與治理政策；
- $H$ ：來源、歷史與變更紀錄；
- $Z$ ：驗證證據與證書；
- $V$ ：版本、內容指紋與相容性資訊。

CAIR 的核心不是「資料很多」，而是：

$$
\boxed{
\text{所有會改變積木語義的事實，必須在 CAIR 中有規範位置。}
}
$$

若某個執行依賴只存在於畫布隱藏欄位、提示詞、Runtime 快取或開發者記憶中，則該積木不能被視為完整封裝。

## 1.3 MSSP：描述與能力索引平面

MSSP 不重新保存完整 CAIR，而是建立一個可認識、可導航、可治理的索引：

$$
M
=
\Pi_{\mathrm{MSSP}}
(P^\ast).
$$

MSSP 應回答：

- 積木名稱與穩定身分；
- 所屬母集與子集；
- 核心能力與可選能力；
- 外部契約摘要；
- 依賴能力；
- 支援環境；
- 所需權限；
- 目前核准版本；
- 維護者與治理者；
- 驗證狀態；
- 棄用與替代關係。

MSSP 可以被全文檢索、向量檢索、圖遍歷或 Agent 規劃器使用，但它不應被當作完整的執行圖。

因此：

$$
\operatorname{Rebuild}
\bigl(
\Pi_{\mathrm{MSSP}}(P^\ast)
\bigr)
\not\equiv
P^\ast
$$

通常成立，因為索引有意省略了內部實現細節。

但：

$$
\operatorname{ResolveDefinition}(M,I_{\mathrm{def}},I_{\mathrm{ver}})
=
P^\ast_{I_{\mathrm{def}},I_{\mathrm{ver}}}
$$

必須成立。

## 1.4 RDR：物化與執行平面

RDR 負責將已核准的積木版本轉為特定執行環境中的可呼叫實現。

令執行環境描述為 $e$ ，目標版本為 $v$ ，則：

$$
Q_{v,e}
=
\mathsf{Materialize}_{\mathrm{RDR}}
(P^\ast_v,e).
$$

$Q_{v,e}$ 可以是：

- 直譯圖；
- Python／JavaScript 函數；
- WebAssembly Component；
- 容器任務；
- 遠端 API 綁定；
- GPU／NPU 執行圖；
- Agent 任務圖；
- 耐久工作流實例；
- 多種後端的混合派發計畫。

RDR 的責任包括：

$$
\mathcal O_{\mathrm{RDR}}
=
\{
\mathsf{resolve},
\mathsf{bind},
\mathsf{load},
\mathsf{gate},
\mathsf{schedule},
\mathsf{dispatch},
\mathsf{trace},
\mathsf{reclaim},
\mathsf{rollback}
\}.
$$

RDR 可以因裝置、資源、成本或策略而產生不同物化結果：

$$
Q_{v,e_1}
\neq
Q_{v,e_2},
$$

但兩者均必須滿足同一契約：

$$
\operatorname{Obs}(Q_{v,e_1})
\models
C_v,
$$

$$
\operatorname{Obs}(Q_{v,e_2})
\models
C_v.
$$

---

# 2. 單一權威原則

## 2.1 權威不等於唯一副本

系統可以有快取、索引、投影、執行映像與日誌副本，但只有 CAIR 的已提交版本能改變定義語義。

令所有派生表示集合為：

$$
\mathcal D(P^\ast)
=
\{
G,M,Q,L,K
\},
$$

其中：

- $G$ ：格子投影；
- $M$ ：MSSP 索引；
- $Q$ ：RDR 物化結果；
- $L$ ：追蹤與日誌；
- $K$ ：快取。

單一權威原則不是要求：

$$
|\mathcal D(P^\ast)|=1,
$$

而是要求：

$$
\forall d\in\mathcal D(P^\ast),
\quad
\operatorname{Authority}(d)=P^\ast.
$$

## 2.2 哪些資料可以由各層自行持有

### 格子語言可自行持有

- 視覺位置；
- 展開偏好；
- 使用者私人註記；
- 暫時選取；
- 未提交候選操作。

### MSSP 可自行持有

- 搜尋索引；
- 排名；
- 使用頻率；
- 推薦關係；
- 可重建的摘要與嵌入。

### RDR 可自行持有

- 編譯快取；
- 連線池；
- 裝置配置；
- 執行中狀態；
- Trace；
- 暫時資源句柄；
- Runtime 健康度。

### 必須回到 CAIR 的資料

- 節點與連線語義；
- 外部端口；
- 契約；
- 權限要求；
- 持續狀態 Schema；
- 副作用宣告；
- 依賴版本；
- 正式來源；
- 驗證結果；
- 已核准演化變體；
- 相容性與棄用關係。

---

# 3. 身分分離與映射

前一篇已區分積木定義、版本、實例與引用。本篇再增加索引與 Runtime 身分：

$$
I(B)
=
(
I_{\mathrm{def}},
I_{\mathrm{ver}},
I_{\mathrm{content}},
I_{\mathrm{index}},
I_{\mathrm{runtime}},
I_{\mathrm{run}}
).
$$

其中：

- $I_{\mathrm{def}}$ ：長期穩定的積木定義身分；
- $I_{\mathrm{ver}}$ ：不可變的語義版本身分；
- $I_{\mathrm{content}}$ ：CAIR 內容指紋；
- $I_{\mathrm{index}}$ ：MSSP 索引項身分；
- $I_{\mathrm{runtime}}$ ：特定物化實現身分；
- $I_{\mathrm{run}}$ ：單次或持續執行實例身分。

映射關係為：

$$
I_{\mathrm{def}}
\xrightarrow{\mathrm{version}}
I_{\mathrm{ver}}
\xrightarrow{\mathrm{content}}
I_{\mathrm{content}},
$$

$$
I_{\mathrm{ver}}
\xrightarrow{\mathrm{publish}}
I_{\mathrm{index}},
$$

$$
(I_{\mathrm{ver}},e)
\xrightarrow{\mathrm{materialize}}
I_{\mathrm{runtime}},
$$

$$
(I_{\mathrm{runtime}},x,s)
\xrightarrow{\mathrm{invoke}}
I_{\mathrm{run}}.
$$

這種分離避免下列錯誤：

- 把重新索引誤判為新版本；
- 把重新編譯誤判為新定義；
- 把一次執行狀態寫回積木定義；
- 把同一版本在不同裝置的實現誤判為不同語義；
- 把可移動的 `stable` 標籤當成不可變版本。

---

# 4. 五條核心資料路徑

## 4.1 提案路徑：格子語言到 CAIR 候選分支

畫布操作首先生成差異：

$$
\Delta_G
=
\operatorname{Diff}
(G_t,G_{t+1}).
$$

系統再將其轉換為 CAIR 提案：

$$
\Delta_P
=
\mathsf{Lower}_{\mathrm{grid}\rightarrow\mathrm{CAIR}}
(\Delta_G,P^\ast_t).
$$

這一步不直接改寫權威版本，而是形成：

$$
\widetilde P_{t+1}
=
\mathsf{Apply}
(P^\ast_t,\Delta_P).
$$

其中 $\widetilde P_{t+1}$ 是候選，不是已提交真相。

## 4.2 提交路徑：候選到新權威版本

候選必須經過：

$$
\operatorname{Validate}
(\widetilde P_{t+1})
=
Z_{t+1}.
$$

若：

$$
Z_{t+1}
\models
C_{t+1}
\land
\operatorname{GovernanceOK}
\land
\operatorname{NoCriticalAmbiguity},
$$

才可原子提交：

$$
P^\ast_{t+1}
=
\mathsf{Commit}
(\widetilde P_{t+1},Z_{t+1}).
$$

## 4.3 發布路徑：CAIR 到 MSSP

索引發布為：

$$
M_{t+1}
=
\mathsf{Index}
(P^\ast_{t+1}).
$$

若索引失敗，不應回滾已成功提交的 CAIR；系統應將 MSSP 標記為落後並重建：

$$
\operatorname{Lag}(M,P^\ast)>0.
$$

因此，MSSP 是可重建派生層，而不是提交事務中的唯一權威。

## 4.4 物化路徑：CAIR／MSSP 到 RDR

RDR 首先透過 MSSP 或直接版本引用解析定義：

$$
(I_{\mathrm{def}},r,e)
\xrightarrow{\mathrm{resolve}}
I_{\mathrm{ver}},
$$

再取得對應 CAIR：

$$
I_{\mathrm{ver}}
\xrightarrow{\mathrm{fetch}}
P^\ast_v.
$$

最後物化：

$$
(P^\ast_v,e)
\xrightarrow{\mathrm{materialize}}
Q_{v,e}.
$$

MSSP 只協助找到版本，真正的執行物化必須以精確版本及內容指紋為依據。

## 4.5 回寫路徑：執行觀測到證據庫

RDR 產生：

$$
T_{\mathrm{run}}
=
(
I_{\mathrm{run}},
I_{\mathrm{ver}},
I_{\mathrm{runtime}},
X,Y,E,C_{\mathrm{obs}},R
).
$$

其中包括輸入摘要、輸出摘要、效果、成本、錯誤、環境與契約觀測。

這些資料可以進入 Trace／證據庫，但不得直接修改 $P^\ast_v$ ：

$$
T_{\mathrm{run}}
\not\rightarrow
P^\ast_v.
$$

若觀測結果引發最佳化或修正，應建立新提案：

$$
T_{\mathrm{run}}
\xrightarrow{\mathrm{analyze}}
\Delta_P^{\mathrm{proposal}}.
$$

這是 RDR 與 AEREC 接合的重要治理邊界。

---

# 5. 投影、索引與物化的守恆關係

## 5.1 畫布投影守恆

對不涉及視覺資訊的語義查詢 $q$ ：

$$
q
\bigl(
\Pi_{\mathrm{grid}}(P^\ast)
\bigr)
=
q(P^\ast).
$$

例如：

- 端口型別；
- 必要權限；
- 邊方向；
- 封裝成員；
- 依賴版本。

畫布可改變位置，但不能默默改變這些事實。

## 5.2 MSSP 可解析守恆

$$
\operatorname{Resolve}
\bigl(
\Pi_{\mathrm{MSSP}}(P^\ast),
I_{\mathrm{def}},I_{\mathrm{ver}}
\bigr)
=
I_{\mathrm{content}}.
$$

若索引無法解析到精確內容指紋，則不得用於可重現部署。

## 5.3 RDR 契約守恆

對所有核准環境 $e\in\mathcal E_{\mathrm{approved}}$ ：

$$
\operatorname{Obs}
\bigl(
\mathsf{Run}(Q_{v,e})
\bigr)
\models
C_v.
$$

不同後端不需要逐指令相同，但其可觀測行為必須落在契約允許的等價類內。

## 5.4 來源守恆

所有派生物件必須能回指：

$$
I_{\mathrm{run}}
\rightarrow
I_{\mathrm{runtime}}
\rightarrow
I_{\mathrm{ver}}
\rightarrow
I_{\mathrm{content}}
\rightarrow
I_{\mathrm{def}}.
$$

若任一執行結果無法回溯到精確定義版本，則不可作為正式證據或 AEREC 演化基線。

---

# 6. 格子語言到 CAIR 的操作語義

## 6.1 操作不能只保存最終畫面

若使用者將節點 $a$ 與 $b$ 連接，不能只記錄一條視覺線。系統應生成具語義的操作：

$$
\mathsf{Connect}
(
I_a.p_o,
I_b.p_i,
\tau,
\kappa
),
$$

其中：

- $I_a.p_o$ ：來源輸出端口；
- $I_b.p_i$ ：目標輸入端口；
- $\tau$ ：邊型別；
- $\kappa$ ：契約與轉換條件。

斷線也不是刪除像素，而是：

$$
\mathsf{Disconnect}(I_e).
$$

折疊則是：

$$
\mathsf{Collapse}(R,\partial_R,C_R),
$$

而不是把多個方塊設為隱藏。

## 6.2 可逆操作與不可逆操作

格子操作可分為：

$$
\mathcal O
=
\mathcal O_{\mathrm{view}}
\cup
\mathcal O_{\mathrm{semantic}}
\cup
\mathcal O_{\mathrm{governance}}.
$$

### 視圖操作

通常不需新 CAIR 語義版本：

- 平移；
- 縮放；
- 改變顯示排列；
- 局部展開偏好。

### 語義操作

必須形成 CAIR 提案：

- 改變連線；
- 改變端口；
- 改變契約；
- 加入依賴；
- 改變持續狀態；
- 修改副作用；
- 再封裝。

### 治理操作

需要額外批准：

- 擴大權限；
- 移除驗證閘門；
- 將不可逆效果設為自動執行；
- 更換信任來源；
- 發布為全域 stable；
- 取代既有正式版本。

---

# 7. MSSP 索引模型

## 7.1 MSSP 不等於檔案清單

MSSP 應提供能力層次，而不只是列出檔案名稱。最低索引項可表示為：

$$
M_B
=
(
I_{\mathrm{def}},
I_{\mathrm{ver}},
N,
K,
C_{\mathrm{summary}},
D,
E,
P,
G,
Z,
A
),
$$

其中：

- $N$ ：名稱與別名；
- $K$ ：能力分類與關鍵詞；
- $C_{\mathrm{summary}}$ ：契約摘要；
- $D$ ：依賴摘要；
- $E$ ：支援環境；
- $P$ ：權限摘要；
- $G$ ：治理資訊；
- $Z$ ：驗證狀態；
- $A$ ：可用性、棄用與替代資訊。

## 7.2 能力查詢

Agent 不應只問「檔名包含什麼」，而應提出能力約束：

$$
q
=
(
\text{input type},
\text{output type},
\text{effects},
\text{permissions},
\text{cost},
\text{environment},
\text{trust}
).
$$

MSSP 回傳候選集合：

$$
\mathcal B_q
=
\operatorname{Search}_{\mathrm{MSSP}}(q).
$$

但最終相容性仍需由 CAIR 契約與 RDR 環境檢查確認。

## 7.3 索引不是批准

$$
\operatorname{Indexed}(B)
\not\Rightarrow
\operatorname{Executable}(B).
$$

積木可能：

- 可被搜尋但未部署；
- 已棄用但保留歷史；
- 只允許測試環境；
- 缺少本機所需能力；
- 等待人工批准；
- 驗證證書已過期。

因此，MSSP 必須保留狀態欄位，而不能把「搜尋得到」等同「可以立即執行」。

---

# 8. RDR 物化與派發模型

## 8.1 從定義到可呼叫實現

RDR 的物化可分為：

$$
\mathsf{Materialize}
=
\mathsf{Resolve}
\circ
\mathsf{Verify}
\circ
\mathsf{Lower}
\circ
\mathsf{Bind}
\circ
\mathsf{Load}.
$$

依序為：

1. 解析精確版本；
2. 驗證內容、契約與證書；
3. 將 CAIR 降低至目標後端；
4. 綁定外部能力與權限；
5. 載入可執行環境。

## 8.2 具現化派發

積木不必在註冊時全部編譯與載入。RDR 可以保存一個**可物化定義**，在首次查找或呼叫時才生成可執行實現：

$$
\operatorname{Lookup}(I_{\mathrm{def}},r,e)
\rightarrow
\begin{cases}
Q_{v,e}, & \text{若已存在有效物化};\\
\mathsf{Materialize}(P^\ast_v,e), & \text{否則}.
\end{cases}
$$

這允許：

- 延遲載入；
- 按需編譯；
- 遠端物化；
- 不同裝置後端；
- 失敗隔離；
- 可移除資源追蹤。

## 8.3 派發不是只有函數表

RDR 的 Registry 至少應保存：

$$
R_B
=
(
I_{\mathrm{def}},
I_{\mathrm{ver}},
I_{\mathrm{content}},
\mathcal E,
\mathcal Q,
\mathcal G,
\mathcal H
),
$$

其中：

- $\mathcal E$ ：支援環境與後端；
- $\mathcal Q$ ：物化器與可呼叫入口；
- $\mathcal G$ ：權限、資源與安全閘門；
- $\mathcal H$ ：健康度、生命週期與回收策略。

## 8.4 呼叫流程

一次正式呼叫為：

$$
\mathsf{Invoke}
(B,x,s,p,e)
=
\mathsf{Trace}
\circ
\mathsf{Dispatch}
\circ
\mathsf{Gate}
\circ
\mathsf{Resolve}
(B,x,s,p,e).
$$

其結果不是只有 $y$ ：

$$
\mathcal R
=
(Y,S',\mathcal E,\mathcal T,\mathcal C_{\mathrm{obs}}).
$$

RDR 必須讓執行證據可回溯到版本、環境與物化器。

---

# 9. 控制平面與資料平面

可將四層重新分為兩類：

## 9.1 控制平面

$$
\mathcal C_{\mathrm{plane}}
=
\{
\text{Grid proposal},
\text{CAIR authority},
\text{MSSP index},
\text{RDR registry}
\}.
$$

控制平面負責：

- 定義；
- 版本；
- 契約；
- 能力發現；
- 權限；
- 部署與派發政策。

## 9.2 資料平面

$$
\mathcal D_{\mathrm{plane}}
=
\{
\text{runtime inputs},
\text{states},
\text{effects},
\text{outputs},
\text{traces}
\}.
$$

資料平面負責實際執行。

執行資料不應默默改寫控制平面：

$$
\mathcal D_{\mathrm{plane}}
\not\rightarrow
P^\ast
$$

除非經由明確的提案與提交程序。

---

# 10. 接合狀態機

一個新積木從畫布到正式執行，可表示為：

```text
DRAFT_GRID
    │ semantic edit
    ▼
CAIR_PROPOSAL
    │ validate / review
    ▼
CAIR_COMMITTED
    │ publish index
    ▼
MSSP_INDEXED
    │ deploy / resolve target
    ▼
RDR_REGISTERED
    │ lookup / materialize
    ▼
RUNTIME_READY
    │ invoke
    ▼
RUNNING
    │ trace / evidence
    ▼
OBSERVED
```

失敗支線包括：

```text
CAIR_PROPOSAL ── invalid ──► REJECTED
CAIR_COMMITTED ── index fail ──► INDEX_LAGGING
RDR_REGISTERED ── backend unavailable ──► UNMATERIALIZABLE
RUNTIME_READY ── gate denied ──► EXECUTION_DENIED
RUNNING ── contract violation ──► QUARANTINED
```

重要的是：某個後續層失敗，不一定推翻前一層真相。例如索引失敗不代表 CAIR 版本不存在；特定裝置無法物化也不代表積木契約無效。

---

# 11. 核心不變量

## 不變量一：權威唯一

$$
\operatorname{SemanticAuthority}(B)
=P^\ast_v.
$$

任何語義修改都必須產生新 CAIR 版本。

## 不變量二：投影可重建

$$
G
\approx
\Pi_{\mathrm{grid}}(P^\ast,U,D).
$$

遺失畫布快取後，系統仍能從 CAIR 重建可操作視圖。

## 不變量三：索引可重建

$$
M
=
\Pi_{\mathrm{MSSP}}(P^\ast).
$$

MSSP 資料損壞不應摧毀積木定義。

## 不變量四：物化可替換

$$
Q_{v,e_1}
\sim_{C_v}
Q_{v,e_2}.
$$

更換 Runtime、編譯器或硬體不得在未升版時改變外部契約。

## 不變量五：執行可追溯

$$
I_{\mathrm{run}}
\rightarrow
I_{\mathrm{ver}}
\rightarrow
I_{\mathrm{content}}.
$$

所有正式結果均可定位到精確權威版本。

## 不變量六：反向寫入受限

$$
\operatorname{RuntimeObservation}
\rightarrow
\operatorname{Proposal},
$$

而非：

$$
\operatorname{RuntimeObservation}
\rightarrow
\operatorname{AuthorityMutation}.
$$

## 不變量七：顯示非語義

$$
\Delta_{\mathrm{layout}}
\not\Rightarrow
\Delta_{\mathrm{semantic}}.
$$

純排版修改不應產生語義版本漂移。

## 不變量八：索引非執行

$$
\operatorname{Discoverable}
\not\Rightarrow
\operatorname{Authorized}
\land
\operatorname{Materializable}.
$$

---

# 12. 常見失敗模式

## 12.1 畫布即資料庫

若畫布 JSON 是唯一資料，視圖欄位、語義欄位與 Runtime 欄位會混在一起。任何 UI 升級都可能破壞執行重現性。

## 12.2 MSSP 成為第二權威

若 Agent 直接修改能力索引並讓 RDR 據此執行，索引摘要將逐漸與 CAIR 定義分離。

## 12.3 RDR 反向污染定義

Runtime 可能因自動調優產生新快取、融合圖或裝置配置。若直接寫回原定義，將無法區分語義升版與後端最佳化。

## 12.4 候選與正式版本共用 ID

若 AI 候選結構與正式版本使用相同身分，執行者可能在驗證完成前取得半成品。

## 12.5 可移動標籤未解析

若部署只保存 `stable` 或 `latest-tested`，日後該標籤移動後便無法重播。提交時必須記錄精確版本與內容指紋。

## 12.6 索引成功被誤認為部署成功

MSSP 可找到積木，不代表目標 Runtime 已具備模型、金鑰、裝置、網路或權限。

## 12.7 多層同步事務過大

若要求 CAIR、MSSP、所有 Runtime 與畫布必須在單一全域事務中同時更新，系統將變得脆弱。較合理的是：CAIR 原子提交，其他層以版本化事件與可重建機制最終一致。

---

# 13. 最小資料格式提案

以下不是最終標準，只用於鎖定 MVP 的分層。

## 13.1 CAIR 定義摘要

```yaml
cair:
  definition_id: evemiss.block.asset-generator
  version: 0.1.0
  content_hash: sha256:...
  contract:
    inputs:
      - name: source
        type: media/source
    outputs:
      - name: asset
        type: media/validated-asset
    effects:
      - model.invoke
      - storage.write
    permissions:
      - model.use:image
      - storage.write:workspace
  graph:
    nodes: [...]
    edges: [...]
    regions: [...]
  state_schema: {...}
  provenance: {...}
  validation:
    status: passed
    certificate_ids: [...]
```

## 13.2 MSSP 索引摘要

```yaml
mssp:
  definition_id: evemiss.block.asset-generator
  approved_version: 0.1.0
  content_hash: sha256:...
  mother_set: creative-tools
  subsets:
    - image-generation
    - validated-assets
  capabilities:
    - generate-asset
    - validate-output
  required_permissions:
    - model.use:image
    - storage.write:workspace
  status: approved
```

## 13.3 RDR Registry 摘要

```yaml
rdr:
  definition_id: evemiss.block.asset-generator
  version: 0.1.0
  content_hash: sha256:...
  materializers:
    - target: python-local
      handler: cair_python_lowerer
    - target: wasm-component
      handler: cair_wasm_lowerer
  gates:
    - permission-check
    - certificate-check
    - resource-budget-check
  lifecycle:
    cache: lazy
    removable: true
    rollback_to: 0.0.9
```

## 13.4 格子投影摘要

```yaml
grid_view:
  authority:
    definition_id: evemiss.block.asset-generator
    version: 0.1.0
    content_hash: sha256:...
  layout:
    x: 420
    y: 180
    width: 280
    height: 160
    collapsed: true
  local_annotations:
    note: "品牌素材生成"
```

視圖資料可改變，但 `authority` 指標必須保持明確。

---

# 14. 主要命題

## 命題一：權威分離命題

操作表面、描述索引與執行物化均不應取代 CAIR 的已提交權威版本。

## 命題二：投影多樣命題

同一 CAIR 版本可以有多個視覺投影，只要其非視覺語義保持契約等價。

## 命題三：索引可重建命題

MSSP 應能由 CAIR 重新產生；索引遺失不應導致定義遺失。

## 命題四：物化相對多形命題

同一積木版本可依環境物化為不同 Runtime 實現，但必須滿足同一外部契約。

## 命題五：精確版本派發命題

正式執行必須解析至不可變版本與內容指紋，不能只依賴可移動標籤。

## 命題六：執行觀測非權威命題

RDR 的執行結果、快取與調優資料只能形成新提案或證據，不能直接改寫既有積木定義。

## 命題七：局部原子、跨層可重建命題

CAIR 提交必須原子；MSSP 與 RDR 可透過版本事件最終一致並可由權威結構重建，不宜強迫所有層進入單一全域鎖。

## 命題八：描述與執行正交命題

MSSP 管理「它是什麼、如何被發現與治理」，RDR 管理「指定版本如何在指定環境中運行」。兩者透過精確版本與內容指紋接合，而非互相吞併。

---

# 15. 與既有工程架構的對照

本文並非聲稱所有概念均沒有工程前例，而是把若干已知原則重新組合到 AI 原生遞歸封裝工作台中。

MLIR 的 Operation Definition Specification 強調，關於一個操作的約束、格式與驗證資訊應集中於單一規範位置，避免事實散落於多段程式碼。這與 CAIR 的單一語義權威原則相近，但 RABCL 還需額外保存積木契約、來源、權限、封裝區域與演化證據。

WebAssembly Component Model 以 WIT `world` 描述元件的 imports 與 exports，顯示介面世界與內部實現可以分離。RABCL 可借用這種自描述邊界觀念，但其積木還包含可展開工作流、狀態、副作用與 AI 推斷契約。

LLVM ORCv2 將符號查找、物化、執行工作階段、派發與資源追蹤分開，並允許按需編譯或載入。這為 RDR 的具現化派發提供工程參照，但 RDR 的輸入不是限定於 LLVM IR，也不只處理程式符號，而是處理經 CAIR 與契約治理的多後端積木。

因此，RABCL 的新意不應表述為「第一次存在 IR、元件介面或延遲派發」，而在於：

$$
\boxed{
\text{將 AI 視覺工作流的形成、權威封裝、能力索引、跨後端物化與遞歸再組合統一為一條可驗證生命週期。}
}
$$

---

# 16. MVP 前的最低接合要求

後續 MVP 不需要立即完成完整編譯器，但至少應實現：

1. 一份規範化 CAIR JSON／YAML；
2. 畫布只透過差異提案修改 CAIR；
3. 視圖布局與語義欄位分離；
4. CAIR 每次提交產生不可變版本及內容指紋；
5. MSSP 索引可由 CAIR 重建；
6. RDR Registry 鎖定精確版本；
7. 至少一種本地物化器；
8. 每次呼叫產生可回溯 Trace；
9. Runtime 觀測只能建立提案，不直接改權威；
10. 可刪除 MSSP 索引與 Runtime 快取後重新建立。

最低驗收式為：

$$
\operatorname{RebuildGrid}(P^\ast)
\land
\operatorname{RebuildIndex}(P^\ast)
\land
\operatorname{Rematerialize}(P^\ast,e)
\land
\operatorname{TraceableRun}(P^\ast,e).
$$

若四者皆成立，才可初步證明分層不是文件上的命名，而是實際可重建架構。

---

# 結論

RABCL 的積木若只存在於畫布，就仍然只是 UI 物件；若只存在於索引，就只是可搜尋描述；若只存在於 Runtime，就只是暫時實現。要讓積木成為可長期演化的語言基元，必須建立清楚的權威與派生關係：

$$
\boxed{
\text{格子語言提出操作}
\rightarrow
\text{CAIR 保存權威}
\rightarrow
\text{MSSP 發布能力索引}
\rightarrow
\text{RDR 物化並派發執行}
}
$$

其反向路徑則只能是：

$$
\boxed{
\text{RDR 產生觀測}
\rightarrow
\text{形成證據或修改提案}
\rightarrow
\text{重新驗證}
\rightarrow
\text{提交新的 CAIR 版本}
}
$$

而不能是 Runtime 自動把暫時狀態寫成新的永久定義。

最終，四層的關係不是四套彼此競爭的系統，而是：

$$
\boxed{
\text{操作表面}
+
\text{語義權威}
+
\text{認知索引}
+
\text{執行物化}
}
$$

格子語言讓人類與 AI 能夠理解和操作；CAIR 讓系統知道自己究竟是什麼；MSSP 讓能力可以被發現、分類與治理；RDR 讓指定版本在特定環境中真正運行。只有完成這個接合，工作流封裝出的「大方塊」才不只是視覺捷徑，而能成為可重播、可移植、可追溯、可替換後端並可進一步交給 AEREC 演化的正式計算單元。

---

# 參考資料

1. MLIR, *Operation Definition Specification (ODS)*，關於操作定義、約束、格式與驗證資訊的集中式規範。
2. MLIR, *Language Reference*，關於 operations、regions、blocks、types 與多種圖結構的中介表示。
3. Bytecode Alliance, *WebAssembly Component Model — Worlds and WIT Reference*，關於元件 imports、exports 與自描述介面世界。
4. LLVM, *ORC Design and Implementation*，關於 ExecutionSession、symbol lookup、materialization、dispatch 與 resource tracking。
5. Neo.K／EveMissLab，*MSSP × RDR 整合規格書 v1.0*。
6. Neo.K／Aletheia，RABCL 系列第 01–04 篇。
