# 從 EXE 與 DLL 到演化膠囊：自適應封裝的新本體

## From EXE and DLL to Evolutionary Capsules: A New Ontology of Adaptive Software Packaging

**系列名稱**：AI 自適應封裝與遞歸演化計算論（AI-Adaptive Encapsulation and Recursive Evolutionary Computation, AEREC）  
**系列編號**：EML-AEREC-2026-03  
**作者**：Neo.K（許筌崴）with Aletheia（GPT）  
**機構**：EveMissLab／一言諾科技有限公司  
**版本**：v0.1 演化封裝本體初稿  
**日期**：2026 年 7 月 29 日  
**文件定位**：演化膠囊、軟體封裝本體、執行投影、變體族、證書鏈、部署與回滾

---

## 摘要

EXE、DLL、共享函式庫、套件、容器映像與 WebAssembly 模組，皆是不同時代為了散布、載入、連結與執行而形成的軟體封裝技術。它們有效地把複雜的來源程式、依賴、資源、入口與平台假設壓縮為可執行或可重用的形式。然而，這些封裝大多仍以「某一版本的固定實現」為中心：當原始碼、編譯器、硬體、依賴、工作負載或最佳化策略改變時，系統通常重新產生另一份封裝物，而舊封裝則被替換、保留或淘汰。

AI 自適應封裝需要不同的本體。若同一應用可以在功能契約保持不變的前提下，持續生成低延遲版、低能耗版、低記憶版、離線版、安全強化版、GPU 版、邊緣版與不同硬體特化版，那麼 EXE、DLL、容器或 WASM 就不應再被視為應用本身，而應被視為權威程式本體在特定環境與目標函數下的執行投影。

本文提出「演化膠囊」本體：

$$
\mathbb E_n
=
\left(
\mathcal I_{\mathrm{app}},
P^\ast,
\mathcal C,
\mathcal V_n,
\Pi_n,
\mathcal Z_n,
\mathcal B_n,
\mathcal H_n,
\mathcal D_n,
\mathcal G,
\mathcal R_n
\right).
$$

其中 $\mathcal I_{\mathrm{app}}$ 是應用身分， $P^\ast$ 是權威程式本體， $\mathcal C$ 是功能契約， $\mathcal V_n$ 是第 $n$ 代合法執行變體族， $\Pi_n$ 是投影與編譯集合， $\mathcal Z_n$ 是驗證與等價證書鏈， $\mathcal B_n$ 是環境與成本剖面， $\mathcal H_n$ 是演化歷史， $\mathcal D_n$ 是部署拓撲， $\mathcal G$ 是治理規則， $\mathcal R_n$ 是回滾與恢復結構。

本文進一步區分五個封裝層次：身分封裝、語義封裝、實現封裝、部署封裝與演化封裝。傳統 EXE 與 DLL 主要位於實現封裝層；容器與套件主要位於部署封裝層；演化膠囊則將身分、語義、變體、證書、歷史與治理共同封裝，使應用能跨越多代重寫而保持連續身分。

本文也提出「變體不是分叉」原則。同一膠囊可以同時維護多個合法變體，只要每個變體都攜帶適用域、環境條件、契約差異、成本向量與驗證證據。變體選擇器根據當前硬體、期限、能源、記憶、風險與依賴條件，選擇或生成最適實現：

$$
P^\star
=
\arg\min_{P\in\mathcal V_n(E_t)}
J_{\mathbf w_t}(P).
$$

本文最後處理演化膠囊的部署、更新與恢復。正式版本不應被 AI 直接覆寫，而應經候選分支、沙盒驗證、證書簽署、金絲雀部署、分階段擴張與自動回滾。膠囊本身也不應是一個不可分割的大檔案，而應是一個內容定址、可部分載入、可差分更新、可驗證重建的封裝圖。

本文的核心命題是：未來軟體封裝的目的，不只是把程式變成方便執行的檔案，而是把應用的身分、功能承諾、合法執行形態、驗證證據、部署歷史與演化能力共同保存為一個可持續生長的計算實體。

**關鍵詞**：演化膠囊、EXE、DLL、容器、WebAssembly、軟體封裝、執行投影、變體族、證書鏈、自適應部署

---

## 1. 封裝技術的本來目的

封裝的核心目的從來不只是一個檔案副檔名。

它通常同時完成：

- 隱藏內部複雜度；
- 固定可調用界面；
- 保存依賴；
- 定義載入方式；
- 建立版本；
- 支援散布；
- 提供安全與權限邊界；
- 確定執行入口；
- 限定平台與環境。

可抽象表示為：

$$
\mathsf{Package}
=
\left(
\mathsf{Implementation},
\mathsf{Interface},
\mathsf{Dependencies},
\mathsf{Loader},
\mathsf{Metadata},
\mathsf{Policy}
\right).
$$

EXE 偏向完整入口與直接執行；DLL 偏向模組化重用與動態連結；容器映像偏向環境與依賴重現；WASM 偏向可攜式沙盒執行；套件管理器則偏向版本、依賴與散布。

這些封裝都很有效，但它們主要回答：

> 如何保存並部署一個已經決定好的實現？

AEREC 則要回答：

> 如何保存一個身分穩定、但實現會持續改變的應用？

---

## 2. 傳統封裝的固定實現假設

傳統封裝近似建立：

$$
\mathcal P_n
=
\operatorname{Pack}
\left(
P_n,
D_n,
R_n,
M_n
\right),
$$

其中：

- $P_n$ ：第 $n$ 版程式；
- $D_n$ ：依賴；
- $R_n$ ：資源；
- $M_n$ ：中繼資料。

當程式改變時：

$$
P_n\neq P_{n+1}
$$

通常就重新建立：

$$
\mathcal P_{n+1}.
$$

封裝物本身不包含一個主動的演化制度。它可能帶有更新器，但更新器只是取得下一個已經由外部產生的版本。

演化膠囊則把：

- 候選生成；
- 等價驗證；
- 多目標評估；
- 變體保留；
- 部署決策；
- 回滾；
- 失敗學習；

納入封裝本體。

---

## 3. 五層封裝本體

本文將封裝分成五層。

## 3.1 身分封裝

保存：

$$
\mathcal I_{\mathrm{app}}
=
\left(
r^\ast,
\mathcal C,
\Omega,
v_s,
\mathcal G,
H
\right).
$$

它回答：

> 這是哪一個應用？

## 3.2 語義封裝

保存：

- 權威程式本體；
- 功能契約；
- 型別；
- 效果；
- 狀態；
- 權限；
- 不變量。

它回答：

> 這個應用承諾做什麼？

## 3.3 實現封裝

保存：

- 原始碼投影；
- IR；
- EXE；
- DLL；
- WASM；
- GPU kernel；
- 專用資料布局；
- 編譯與連結資訊。

它回答：

> 在某個環境中如何執行？

## 3.4 部署封裝

保存：

- 容器；
- 套件；
- 依賴鎖定；
- 平台條件；
- 設定；
- 憑證；
- 資源限制；
- 滾動部署策略。

它回答：

> 如何安全地進入實際環境？

## 3.5 演化封裝

保存：

- 候選版本；
- 證書鏈；
- 成本模型；
- 失敗記錄；
- 變體選擇；
- 分支；
- 回滾；
- 演化權限。

它回答：

> 如何在不失去身分的情況下繼續改變？

因此：

$$
\boxed{
\mathsf{EvolutionaryPackage}
=
\mathsf{Identity}
+
\mathsf{Semantics}
+
\mathsf{Implementation}
+
\mathsf{Deployment}
+
\mathsf{Evolution}.
}
$$

---

## 4. 演化膠囊的完整形式

本文定義：

$$
\boxed{
\mathbb E_n
=
\left(
\mathcal I_{\mathrm{app}},
P^\ast,
\mathcal C,
\mathcal V_n,
\Pi_n,
\mathcal Z_n,
\mathcal B_n,
\mathcal H_n,
\mathcal D_n,
\mathcal G,
\mathcal R_n
\right).
}
$$

---

## 5. 應用身分 $\mathcal I_{\mathrm{app}}$

應用身分提供跨代連續根。

它與特定內容指紋分離：

$$
r^\ast
\neq
h(P_n).
$$

其中：

- $r^\ast$ ：長期身分；
- $h(P_n)$ ：某一代內容指紋。

同一身分根可擁有多個版本與投影：

$$
r^\ast
\mapsto
\left\{
P_{n,i}
\right\}_{n,i}.
$$

---

## 6. 權威程式本體 $P^\ast$

權威本體不是單一來源文字，而是一個具有語義、型別、效果、狀態、權限與來源的計算結構：

$$
P^\ast
=
\left(
V,E,\Lambda,\Theta,\Sigma,H,G
\right).
$$

它是所有合法投影的共同錨點。

### 6.1 權威性原則

若兩個投影衝突：

$$
\pi_i(P^\ast)
\neq
\pi_j(P^\ast),
$$

系統不能依介面偏好任意決定，而必須回到權威本體、語義差異與驗證規則。

### 6.2 不可變快照

每次正式提交產生權威快照：

$$
P_n^\ast.
$$

舊快照不可被覆寫，只能新增後繼：

$$
P_n^\ast
\rightarrow
P_{n+1}^\ast.
$$

---

## 7. 功能契約 $\mathcal C$

契約定義哪些實現改寫仍屬於同一應用。

所有合法變體必須滿足：

$$
P_{n,i}
\equiv_{\mathcal C_i}
P_n^\ast.
$$

若變體具有額外限制，例如只適用離線模式，則其契約為：

$$
\mathcal C_i
=
\mathcal C_{\mathrm{base}}
+
\Delta\mathcal C_i.
$$

任何差異必須顯式標記。

---

## 8. 執行變體族 $\mathcal V_n$

第 $n$ 代可以同時包含：

$$
\mathcal V_n
=
\left\{
P_n^{\mathrm{general}},
P_n^{\mathrm{latency}},
P_n^{\mathrm{energy}},
P_n^{\mathrm{memory}},
P_n^{\mathrm{offline}},
P_n^{\mathrm{secure}},
P_n^{\mathrm{gpu}},
P_n^{\mathrm{edge}}
\right\}.
$$

### 8.1 變體不是分叉

變體共享：

- 同一身分根；
- 同一基礎契約；
- 同一權威本體；
- 同一證書鏈；
- 同一演化歷史。

產品分叉則會建立新的身分根。

### 8.2 變體適用域

每個變體具有環境述詞：

$$
\chi_i(E)=
\begin{cases}
1,& \text{變體適用}\\
0,& \text{變體不適用}
\end{cases}
$$

### 8.3 變體成本向量

$$
\mathbf J(P_{n,i}\mid E)
=
\left(
T,M,E_c,L,S,X,R,V,G
\right).
$$

其中 $E_c$ 表示能源成本，以免與環境符號混淆。

---

## 9. 投影與編譯集合 $\Pi_n$

演化膠囊包含：

$$
\Pi_n
=
\left\{
\pi_{\mathrm{text}},
\pi_{\mathrm{exe}},
\pi_{\mathrm{dll}},
\pi_{\mathrm{wasm}},
\pi_{\mathrm{container}},
\pi_{\mathrm{gpu}},
\pi_{\mathrm{edge}},
\pi_{\mathrm{debug}}
\right\}.
$$

### 9.1 投影不必全部預先存在

某些投影可按需生成：

$$
P_{e,c}
=
\pi_{e,c}
\left(
P^\ast,
\mathcal B_n
\right).
$$

### 9.2 可重建性

任何正式投影應能由：

- 權威快照；
- 投影器版本；
- 環境剖面；
- 編譯參數；
- 依賴指紋；

重建。

若不能重建，該投影不可被視為可信正式產物。

### 9.3 雙向回寫限制

執行投影中的修改不能直接成為權威改寫。

必須先產生候選差異：

$$
\Delta_i
=
\operatorname{Diff}
\left(
P^\ast,
P_i'
\right),
$$

再經驗證與提交。

---

## 10. 證書鏈 $\mathcal Z_n$

證書不是單一「通過」標記，而是一組具有適用域的證據圖：

$$
\mathcal Z_n
=
\left(
Z_{\mathrm{type}},
Z_{\mathrm{equiv}},
Z_{\mathrm{property}},
Z_{\mathrm{security}},
Z_{\mathrm{benchmark}},
Z_{\mathrm{dependency}},
Z_{\mathrm{deployment}},
Z_{\mathrm{runtime}}
\right).
$$

### 10.1 證書鏈

每個版本轉換具有：

$$
Z_{n\rightarrow n+1}.
$$

完整歷史形成：

$$
Z_{0\rightarrow1}
\rightarrow
Z_{1\rightarrow2}
\rightarrow
\cdots
\rightarrow
Z_{n-1\rightarrow n}.
$$

### 10.2 錨點證書

為防止漂移，還需保留：

$$
Z_{0\rightarrow n}.
$$

### 10.3 證書失效

若環境、依賴或契約改變，部分證書可能失效：

$$
\operatorname{Valid}
\left(
Z,E_t
\right)=0.
$$

膠囊必須知道哪些變體需要重新驗證。

---

## 11. 環境與成本剖面 $\mathcal B_n$

環境剖面為：

$$
B
=
\left(
H,O,D,W,N,R,C,T
\right),
$$

其中：

- $H$ ：硬體；
- $O$ ：作業系統與執行環境；
- $D$ ：資料分布；
- $W$ ：工作負載；
- $N$ ：網路與外部服務；
- $R$ ：風險與權限；
- $C$ ：成本權重；
- $T$ ：期限與時間條件。

### 11.1 剖面不是永久固定

實際環境會變化：

$$
B_{t+1}\neq B_t.
$$

所以變體選擇必須是動態的。

### 11.2 剖面簽名

相似環境可歸為剖面類：

$$
[B]
=
\left\{
B'\mid d(B,B')\leq\epsilon
\right\}.
$$

避免為每一台裝置產生完全獨立版本。

---

## 12. 演化歷史 $\mathcal H_n$

演化歷史保存：

- 正式提交；
- 候選；
- 拒絕；
- 分支；
- 回滾；
- 漂移；
- 性能；
- 適用域；
- 失敗原因；
- 人工決策。

可表示為有向無環歷史圖：

$$
\mathcal H_n
=
\left(
V_H,E_H
\right).
$$

### 12.1 非線性歷史

版本不必只有單一主線。

可能存在：

- 平台分支；
- 安全分支；
- 實驗分支；
- 長期支援分支；
- 硬體特化分支。

### 12.2 合併條件

兩個演化分支要合併，必須重新驗證契約、依賴與證書，不可只做文字合併。

---

## 13. 部署拓撲 $\mathcal D_n$

部署不是「把新檔案複製過去」，而是受控狀態轉換：

$$
\mathcal D_n
\rightarrow
\mathcal D_{n+1}.
$$

部署拓撲可包含：

- 正式穩定區；
- 候選區；
- 沙盒；
- 金絲雀區；
- 灰度區；
- 備援區；
- 回滾映像；
- 離線驗證區。

### 13.1 部署狀態

每個變體具有：

$$
s_i
\in
\left\{
\mathsf{candidate},
\mathsf{verified},
\mathsf{canary},
\mathsf{active},
\mathsf{deprecated},
\mathsf{quarantined},
\mathsf{rollback}
\right\}.
$$

### 13.2 漸進部署

$$
0\%
\rightarrow
1\%
\rightarrow
5\%
\rightarrow
25\%
\rightarrow
100\%.
$$

每一階段都可以中止或回滾。

---

## 14. 治理規則 $\mathcal G$

治理定義：

$$
\mathcal G
=
\left(
A,R,P,Q,S,L
\right),
$$

其中：

- $A$ ：主體；
- $R$ ：角色；
- $P$ ：權限；
- $Q$ ：法定人數或批准門檻；
- $S$ ：簽署規則；
- $L$ ：責任與日誌。

### 14.1 權力分離

應分開：

- 候選生成權；
- 驗證執行權；
- 證書簽署權；
- 部署權；
- 回滾權；
- 契約修改權。

### 14.2 風險分級

低風險純函數可高度自動化；高風險世界狀態操作則可能需要形式證明與人工批准。

---

## 15. 回滾與恢復結構 $\mathcal R_n$

回滾不是附加功能，而是演化膠囊的一級結構。

$$
\mathcal R_n
=
\left(
P_{\mathrm{last\ known\ good}},
S_{\mathrm{snapshot}},
M_{\mathrm{migration}},
Q_{\mathrm{queue}},
F_{\mathrm{fallback}}
\right).
$$

### 15.1 程式回滾

恢復上一個穩定實現。

### 15.2 狀態回滾

恢復資料與狀態快照。

### 15.3 依賴回滾

恢復外部服務、模型與套件版本。

### 15.4 語義回滾

若契約升級失敗，恢復舊語義版本與遷移狀態。

### 15.5 部分回滾

只撤回某個模組或投影，而不必回滾整個應用。

---

## 16. 演化膠囊不是單一大檔案

一個膠囊若被封成不可分割巨型檔案，會產生：

- 更新成本；
- 重複儲存；
- 驗證困難；
- 差分不透明；
- 局部載入困難；
- 供應鏈風險。

因此，更合理的形式是內容定址封裝圖：

$$
\mathbb E_n
=
G_{\mathrm{capsule}}
\left(
V_C,E_C
\right).
$$

節點可包括：

- 權威快照；
- 契約；
- 投影器；
- 二進位；
- 資源；
- 證書；
- 依賴；
- 環境剖面；
- 部署策略；
- 回滾資料。

### 16.1 內容定址

每個節點具有：

$$
h(v)
=
\operatorname{Hash}(v).
$$

### 16.2 差分更新

新版本只需增加或替換變動節點。

### 16.3 部分載入

執行裝置只載入需要的變體、依賴與證書。

### 16.4 可重建根

整個膠囊具有 Merkle 型根：

$$
h_{\mathbb E_n}.
$$

用以驗證完整性。

---

## 17. 變體選擇器

在環境 $B_t$ 下，合法變體集合為：

$$
\mathcal V_n(B_t)
=
\left\{
P_i\in\mathcal V_n
\mid
\chi_i(B_t)=1
\right\}.
$$

系統選擇：

$$
P^\star_t
=
\arg\min_{P\in\mathcal V_n(B_t)}
J_{\mathbf w_t}(P).
$$

但還需滿足：

$$
\operatorname{ValidCert}(P,B_t)=1,
$$

以及：

$$
\operatorname{Permit}_{\mathcal G}(P,B_t)=1.
$$

### 17.1 選擇成本

如果選擇器本身成本過高：

$$
C_{\mathrm{select}}
\geq
\Delta C_{\mathrm{variant}},
$$

則應採用快取、預選或固定策略。

### 17.2 錯誤選擇

若環境辨識錯誤，系統必須可快速切回通用穩定版。

---

## 18. 按需生成與預先生成

### 18.1 預先生成

提前建立常見環境變體。

優點：

- 可充分驗證；
- 啟動快；
- 可預測。

缺點：

- 儲存多；
- 可能過時；
- 變體爆炸。

### 18.2 按需生成

在部署或執行前生成特化版本。

優點：

- 更貼近環境；
- 減少無用變體。

缺點：

- 啟動成本；
- 驗證壓力；
- 即時風險。

### 18.3 混合策略

$$
\mathcal V_n
=
\mathcal V_n^{\mathrm{prebuilt}}
\cup
\mathcal V_n^{\mathrm{ondemand}}.
$$

高風險核心使用預建版本；低風險區域允許按需特化。

---

## 19. 封裝的遞歸性

演化膠囊本身也可被封裝為更高層膠囊。

例如：

- 函式膠囊；
- 模組膠囊；
- 應用膠囊；
- 服務膠囊；
- 多代理系統膠囊；
- 世界狀態膠囊。

可寫為：

$$
\mathbb E^{(k+1)}
=
\operatorname{Compose}
\left(
\mathbb E_1^{(k)},
\ldots,
\mathbb E_m^{(k)}
\right).
$$

### 19.1 層級契約

高層膠囊不必暴露所有低層細節，只需依賴低層契約與證書。

### 19.2 證書組合

若低層證書可以組合，則高層驗證成本可以下降。

但若介面、時序或副作用耦合複雜，不能假設局部等價自動推出全域等價。

---

## 20. 封裝與解空間幾何

演化膠囊把每次解空間改寫固化為可部署實現。

若：

$$
\Phi_n:
\mathfrak P_n
\rightarrow
\widetilde{\mathfrak P}_n
$$

經驗證有效，則可被轉化為新投影：

$$
P_{n+1}
=
\operatorname{Materialize}
\left(
\Phi_n(P_n)
\right).
$$

因此，快速通道不只存在於一次運行時，而可能進入：

- IR；
- 索引；
- 快取；
- DLL 邊界；
- 特化核心；
- 部署配置；
- 硬體映射。

---

## 21. 封裝與內外雙生展開

演化膠囊不是封閉物件。

外部環境持續提供：

- 新硬體；
- 新模型；
- 新依賴；
- 新負載；
- 新風險；
- 新漏洞；
- 新驗證方法。

膠囊則向外輸出：

- 遙測；
- 候選請求；
- 環境需求；
- 證書；
- 部署狀態；
- 失敗記錄。

因此：

$$
\mathbb E_n
\leftrightarrow
\mathfrak E_{\mathrm{external}}.
$$

---

## 22. 供應鏈與可信執行

演化膠囊必須保存供應鏈證據：

- 來源；
- 建置器；
- 編譯器；
- 依賴；
- 模型；
- 資料；
- 簽章；
- 時間戳；
- 執行環境。

### 22.1 可追溯建置

$$
P_{n,i}
=
\operatorname{Build}
\left(
P_n^\ast,
\pi_i,
B_i,
D_i
\right).
$$

每一輸入都必須可追溯。

### 22.2 可重現與可驗證建置

即使位元級重現不總是可行，也至少要能驗證語義、來源與建置條件。

### 22.3 AI 生成來源

AI 所提出的改寫必須記錄：

- 模型版本；
- 提示與上下文摘要；
- 使用工具；
- 候選差異；
- 驗證證據；
- 人工批准。

---

## 23. 主要理論命題

### 命題一：封裝—身分分離命題

EXE、DLL、WASM 與容器是執行投影，不是應用身分本體。

### 命題二：五層封裝命題

完整自適應封裝必須同時處理身分、語義、實現、部署與演化。

### 命題三：演化膠囊命題

未來應用封裝應包含權威本體、契約、變體族、投影器、證書鏈、成本剖面、歷史、部署與回滾。

### 命題四：變體非分叉命題

多個平台與目標特化版本可以共享同一應用身分，只要契約差異與適用域被明確記錄。

### 命題五：證書一級化命題

證書不是外部報告，而是決定變體可否被選擇、部署與重用的一級封裝物件。

### 命題六：部署拓撲命題

正式、候選、金絲雀、隔離與回滾區應成為膠囊內建狀態，而不是臨時運維腳本。

### 命題七：內容定址命題

演化膠囊應以可差分、可部分載入、可重建的內容定址圖存在，而非不可分割大檔案。

### 命題八：遞歸組合命題

函式、模組、應用、服務與多代理系統都可以形成不同尺度的演化膠囊，但全域等價不能由局部等價無條件推出。

---

## 24. 可反駁條件

### 24.1 膠囊開銷過大

若保存變體、證書、歷史與回滾的成本長期高於演化收益，膠囊需要縮減或分層。

### 24.2 變體爆炸

若：

$$
|\mathcal V_n|
$$

隨環境維度組合爆炸，系統將無法維護。

### 24.3 證書不可組合

若每個變體都必須重新驗證全部系統，遞歸封裝的效益會大幅下降。

### 24.4 環境辨識不可靠

若選擇器無法判斷變體適用域，專用版本可能比通用版更危險。

### 24.5 回滾不完整

只回滾程式而不能回滾狀態、依賴與契約，可能無法恢復真正穩定狀態。

### 24.6 權威根失去唯一性

若不同系統持有互相衝突的權威本體，演化膠囊會退化為多份不同步封裝。

### 24.7 內容定址不足以保證語義

內容雜湊只能證明內容未變，不能證明內容正確或功能等價。

---

## 25. 理論邊界

本文不主張：

- 所有應用都必須同時保存大量變體；
- 演化膠囊應取代所有現有封裝格式；
- EXE 與 DLL 將失去價值；
- 內容雜湊等同功能證明；
- 局部模組證書必然可組合為全域證書；
- 按需生成永遠優於預建；
- AI 可以繞過平台簽署與發布制度；
- 封裝越大、資訊越多就越安全。

更準確的定位是：

$$
\boxed{
\text{EXE、DLL、WASM 與容器仍然存在，但它們被重新定位為演化膠囊的執行投影與部署材料。}
}
$$

---

## 26. 初步膠囊目錄結構

一個概念性封裝可以包含：

```text
capsule/
├── identity/
│   ├── root.json
│   ├── semantic-version.json
│   └── governance.json
├── authority/
│   ├── cair.json
│   ├── contracts/
│   └── invariants/
├── projections/
│   ├── source/
│   ├── exe/
│   ├── dll/
│   ├── wasm/
│   ├── gpu/
│   └── container/
├── variants/
│   ├── general/
│   ├── low-latency/
│   ├── low-energy/
│   └── offline/
├── certificates/
│   ├── equivalence/
│   ├── security/
│   ├── benchmark/
│   └── deployment/
├── profiles/
│   ├── hardware/
│   ├── workload/
│   └── risk/
├── history/
│   ├── accepted/
│   ├── rejected/
│   └── rollback/
└── deployment/
    ├── canary/
    ├── active/
    └── recovery/
```

這只是人類可讀投影；實際儲存可採內容定址圖與物件庫。

---

## 27. 結論

本文將傳統軟體封裝從「保存固定實現的檔案」提升為「保存跨代應用身分與演化能力的計算本體」。

EXE、DLL、WebAssembly、GPU kernel、容器映像與平台套件仍然重要，但它們不再是應用本身，而是：

$$
\pi_{e,c}
\left(
P^\ast
\right)
=
P_{e,c}.
$$

也就是權威程式本體在特定環境、硬體、成本與風險條件下的執行投影。

完整演化膠囊為：

$$
\boxed{
\mathbb E_n
=
\left(
\mathcal I_{\mathrm{app}},
P^\ast,
\mathcal C,
\mathcal V_n,
\Pi_n,
\mathcal Z_n,
\mathcal B_n,
\mathcal H_n,
\mathcal D_n,
\mathcal G,
\mathcal R_n
\right).
}
$$

它不只保存程式，也保存：

- 程式是誰；
- 程式承諾什麼；
- 有哪些合法實現；
- 在什麼環境適用；
- 有哪些證據；
- 如何部署；
- 如何回滾；
- 如何繼續演化。

因此，未來軟體封裝的核心不再只是：

$$
\text{把程式變成方便執行的檔案},
$$

而是：

$$
\boxed{
\text{把應用的身分、承諾、合法形態、證據、歷史與演化能力共同封裝。}
}
$$

本文的核心結論為：

$$
\boxed{
\text{EXE 與 DLL 是某一時刻的執行形態；演化膠囊才是跨越時間持續存在的應用本體。}
}
$$

---

## 系列內部定位

本文為《AI 自適應封裝與遞歸演化計算論》第三篇。

第一篇建立總命題；第二篇建立應用身分與觀測等價；本文建立演化膠囊的封裝本體、變體族、證書鏈、部署拓撲與回滾結構。

下一篇為：

**《全層最佳化空間：從演算法、資料結構到封裝與硬體》**。

---

## 前置文件

1. Neo.K with Aletheia，《程式完成之後：AI 自適應封裝與遞歸演化計算論的總命題》。  
2. Neo.K with Aletheia，《同一個應用是什麼：功能契約、觀測等價與程式身分》。  
3. Neo.K with Aletheia，《多重投影程式論：原始碼不再是程式本體》。  
4. Neo.K with Aletheia，《穩定核心與動態表面：自適應程式語言的分層設計》。  
5. Neo.K with Aletheia，《多重投影程式系統技術架構白皮書：權威 IR、可驗證回寫與 AI 原生治理》。  
6. Neo.K with Aletheia，《解空間幾何計算論》系列。
