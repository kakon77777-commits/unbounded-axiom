# 演化積木：AEREC 驅動的版本族、證書、回滾與停止

## Evolutionary Blocks: AEREC-Driven Version Families, Certificates, Rollback, and Stopping

**系列名稱：** 遞歸自適應積木組合語言（Recursive Adaptive Block Composition Language, RABCL）  
**系列編號：** EML-RABCL-2026-06  
**作者：** Neo.K（許筌崴）with Aletheia（GPT）  
**機構：** EveMissLab／一言諾科技有限公司  
**版本：** v0.1 基礎演化稿  
**日期：** 2026 年 7 月 30 日  
**文件定位：** AEREC 接合、積木版本族、候選生成、證書鏈、漸進提升、回滾拓撲、負知識與演化停止  

---

## 摘要

RABCL 前五篇已建立工作流封裝、封裝靜止屏障、函數化契約、遞歸閉包積木語言，以及格子語言、CAIR、MSSP 與 RDR 的權威—索引—執行分層。然而，一個已經被封裝、註冊並可呼叫的積木仍然只是某一時點的實現。模型、硬體、資料分布、使用情境、依賴版本、成本限制與安全要求會持續變動；若積木只能以人工方式重寫，它仍然沒有成為真正的自適應計算單元。

本文將 AEREC（AI 自適應封裝與遞歸演化系統）接入 RABCL，提出「演化積木」模型。其核心不是允許 AI 直接改寫正在使用的穩定積木，而是把一個積木的定義、契約與實現分離，形成具有共同功能身分、不同實現版本、不同適用環境與不同證據強度的版本族：

$$
\mathcal F_B
=
\left(
B^{(0)},B^{(1)},\ldots,B^{(n)}
\right).
$$

更精確地說，版本族不是單一線性序列，而是有向無環演化圖：

$$
\mathcal G_B^{\mathrm{evo}}
=
(V_B^{\mathrm{ver}},E_B^{\mathrm{der}}),
$$

其中每個版本節點都具有內容指紋、來源、父版本、轉換算子、契約相容性、驗證證據、部署狀態、適用環境及回滾路徑。AEREC 的工作是根據觀測、目標與限制生成候選版本；CAIR 保存候選與穩定版本的權威表示；MSSP 發布其能力身分與治理狀態；RDR 則在精確版本鎖定下完成沙盒、影子、金絲雀、正式提升與回滾。

本文主張，演化必須以「候選隔離」為前提：

$$
B_{\mathrm{stable}}
\not\leftarrow
\mathsf{MutateDirectly},
$$

而應採用：

$$
B_{\mathrm{stable}}
\xrightarrow{\mathsf{derive}}
B_{\mathrm{candidate}}
\xrightarrow{\mathsf{verify}}
B_{\mathrm{eligible}}
\xrightarrow{\mathsf{promote}}
B_{\mathrm{stable}}'.
$$

候選是否可提升，不只取決於輸出是否相同，也取決於狀態、效果、權限、安全、成本、延遲、可解釋性、重播性與特定環境下的統計品質。本文因此建立多層等價與證書模型：

$$
\operatorname{Cert}(B_i,B_j)
=
(
Z_{\mathrm{type}},
Z_{\mathrm{contract}},
Z_{\mathrm{behavior}},
Z_{\mathrm{effect}},
Z_{\mathrm{safety}},
Z_{\mathrm{performance}},
Z_{\mathrm{provenance}}
).
$$

回滾亦不能被簡化為指標退回上一版。對無狀態積木，版本指標回切可能足夠；對有狀態或具有不可逆副作用的積木，還必須處理狀態向後遷移、補償交易、雙寫、前向修復與不可回復標記。因此本文提出回滾拓撲：

$$
\mathcal R_B
=
(
R_{\mathrm{pointer}},
R_{\mathrm{state}},
R_{\mathrm{compensate}},
R_{\mathrm{forward}},
R_{\mathrm{contain}}
).
$$

最後，演化系統必須具有停止能力。若沒有淨收益、證據不足、風險超限、候選震盪、成本超預算、連續多代改善低於門檻，或外部契約已無法在現有邊界內保持，AEREC 必須停止、暫停或要求重新封裝，而不是把「持續演化」誤解為無止境改寫。

本文完成 RABCL 中從靜態積木到演化積木的基本生命週期，並為第七篇統合總論及後續 MVP 鎖定最低可實作範圍。

**關鍵詞：** AEREC、演化積木、版本族、候選版本、契約保持、證書鏈、漸進部署、回滾拓撲、停止條件、負知識、RABCL

---

# 0. 問題定位：封裝完成不等於演化完成

前五篇已使一張工作流可以經由：

$$
\text{連線}
\rightarrow
\text{靜止}
\rightarrow
\text{邊界推斷}
\rightarrow
\text{契約形成}
\rightarrow
\text{CAIR 提交}
\rightarrow
\text{MSSP 索引}
\rightarrow
\text{RDR 物化}
$$

成為可呼叫積木。

但這只回答了：

> 這個工作流如何在現在成為一個積木？

它尚未回答：

> 當環境、資料、模型、依賴或目標改變時，這個積木如何形成新的實現，而不破壞既有使用者與上層積木？

傳統軟體通常以人工發布新版本處理此問題。AEREC 則嘗試讓 AI 參與：

- 觀察瓶頸；
- 提出結構改寫；
- 生成替代實現；
- 組合既有元件；
- 替換模型與演算法；
- 改變快取、批次、並行與路由策略；
- 重新配置硬體與部署拓撲；
- 產生驗證；
- 選擇候選；
- 在治理條件下提升或回滾。

然而，只要 AI 可以提出修改，就會立刻出現三個風險：

1. **穩定版本被原地改寫**；
2. **輸出相似被誤認為語義等價**；
3. **局部 benchmark 改善被誤認為整體淨收益**。

因此，本篇的核心不是證明 AI 可以不斷生成新程式，而是建立：

$$
\boxed{
\text{如何讓演化發生，卻不讓穩定性消失。}
}
$$

---

# 1. AEREC 與 RABCL 的職責分離

## 1.1 RABCL 回答積木如何存在

RABCL 前五篇主要處理：

- 積木如何從工作流形成；
- 積木的外部邊界；
- 積木的契約與狀態；
- 積木如何被折疊、展開與再次組合；
- 積木的權威版本如何被索引與執行。

其核心對象是：

$$
B
=
(
I,C,P^\ast,S,E,Z,H,R
),
$$

其中：

- $I$ ：身分；
- $C$ ：契約；
- $P^\ast$ ：CAIR 權威結構；
- $S$ ：狀態模型；
- $E$ ：效果模型；
- $Z$ ：證據；
- $H$ ：歷史；
- $R$ ：恢復與回滾資料。

## 1.2 AEREC 回答積木如何產生後代

AEREC 處理的是：

$$
B^{(t)}
\xrightarrow{
\mathsf{Observe}
}
O_t
\xrightarrow{
\mathsf{Generate}
}
\{B_{t+1}^{c_1},\ldots,B_{t+1}^{c_m}\}
\xrightarrow{
\mathsf{VerifySelect}
}
B^{(t+1)}.
$$

其中：

- $O_t$ ：對目前版本的觀測；
- $B_{t+1}^{c_i}$ ：候選版本；
- $B^{(t+1)}$ ：被核准的新版本。

因此：

$$
\boxed{
\text{RABCL 定義可演化的積木容器，AEREC 定義候選生成與演化選擇。}
}
$$

兩者不能互相吞併。若 AEREC 自行定義積木身分、契約與 Runtime，它會形成第二套真相；若 RABCL 直接把任何觀測改寫成新版本，又會失去候選隔離與證據治理。

## 1.3 演化不得直接覆寫穩定版本

基本不變量為：

$$
\forall B_s\in\mathcal S_{\mathrm{stable}},
\quad
\mathsf{AEREC}(B_s)
\neq
\mathsf{MutateInPlace}(B_s).
$$

正確路徑是：

$$
B_s
\xrightarrow{\mathsf{fork}}
B_c
\xrightarrow{\mathsf{transform}}
B_c'
\xrightarrow{\mathsf{validate}}
B_e
\xrightarrow{\mathsf{promote}}
B_s'.
$$

其中穩定版本 $B_s$ 在新版本正式提升前保持不可變。

---

# 2. 演化積木的形式定義

## 2.1 從單一積木到版本族

演化積木不是某一個版本，而是版本族與治理資料的組合：

$$
\mathbb B
=
(
I_{\mathrm{def}},
C_{\mathrm{family}},
\mathcal G_{\mathrm{evo}},
\mathcal Z,
\mathcal D,
\mathcal R,
\mathcal N,
\Sigma
).
$$

其中：

- $I_{\mathrm{def}}$ ：共同定義身分；
- $C_{\mathrm{family}}$ ：版本族共同契約邊界；
- $\mathcal G_{\mathrm{evo}}$ ：版本演化圖；
- $\mathcal Z$ ：證書與證據集合；
- $\mathcal D$ ：部署與適用環境集合；
- $\mathcal R$ ：回滾拓撲；
- $\mathcal N$ ：負知識；
- $\Sigma$ ：演化政策與停止條件。

版本族中的每個版本為：

$$
B_v
=
(
I_v,
h_v,
P_v^\ast,
C_v,
S_v,
E_v,
A_v,
Z_v,
D_v,
L_v
).
$$

其中：

- $I_v$ ：版本身分；
- $h_v$ ：內容指紋；
- $P_v^\ast$ ：CAIR 權威結構；
- $C_v$ ：該版本契約；
- $S_v$ ：狀態 Schema 與遷移規則；
- $E_v$ ：效果與權限集合；
- $A_v$ ：適用環境；
- $Z_v$ ：證據包；
- $D_v$ ：部署狀態；
- $L_v$ ：生命週期狀態。

## 2.2 版本族不是線性編號

若版本只能是：

$$
v_0\rightarrow v_1\rightarrow v_2\rightarrow v_3,
$$

則系統無法表達：

- 同一穩定版針對不同硬體生成兩個候選；
- 某候選通過速度測試但未通過安全測試；
- 某分支適合離線批次，另一分支適合低延遲；
- 某個候選被拒絕但其部分改寫可被另一候選繼承；
- 某次回滾後從舊穩定版重新分叉。

因此版本族應表示為有向圖：

$$
\mathcal G_{\mathrm{evo}}
=
(V,E),
$$

其中邊：

$$
e_{ij}
=
(
v_i,
v_j,
T_{ij},
O_{ij},
Z_{ij}
)
$$

記錄：

- 父版本；
- 子版本；
- 轉換算子；
- 生成原因與觀測；
- 轉換證據。

一般情況下，已提交版本的演化來源圖應保持無環：

$$
\mathcal G_{\mathrm{evo}}\ \text{is a DAG}.
$$

執行時可能存在循環，演化歷史本身則不應因回滾而抹除或形成邏輯時間環。回滾是部署指標重新指向舊節點，不是刪除後代歷史。

---

# 3. 四種身分與三種穩定性

## 3.1 定義、契約、實現與部署身分

演化積木至少需要分離：

$$
I(\mathbb B)
=
(
I_{\mathrm{def}},
I_{\mathrm{contract}},
I_{\mathrm{impl}},
I_{\mathrm{deploy}}
).
$$

- $I_{\mathrm{def}}$ ：它在語言中是哪一種能力；
- $I_{\mathrm{contract}}$ ：它遵守哪個外部契約版本；
- $I_{\mathrm{impl}}$ ：它是哪個具體 CAIR 實現；
- $I_{\mathrm{deploy}}$ ：哪個環境目前使用哪個實現。

因此可以有：

$$
I_{\mathrm{def}}^{(1)}
=
I_{\mathrm{def}}^{(2)},
$$

但：

$$
I_{\mathrm{impl}}^{(1)}
\neq
I_{\mathrm{impl}}^{(2)}.
$$

同一積木能力可以擁有多個不同實現。

## 3.2 三種穩定性

「穩定」不能只用一個布林值。至少應區分：

### 語義穩定

$$
\operatorname{Stable}_{\mathrm{sem}}(B)
$$

表示外部契約已核准，不應在修補實現時無聲漂移。

### 執行穩定

$$
\operatorname{Stable}_{\mathrm{run}}(B,e)
$$

表示版本在環境 $e$ 中達到指定可靠性與效能要求。

### 部署穩定

$$
\operatorname{Stable}_{\mathrm{deploy}}(B,e,t)
$$

表示它在特定時間窗內已被正式流量驗證並成為回滾錨點。

某候選可能語義相容，但尚未證明執行穩定；也可能在 GPU 環境穩定，但在 CPU 環境不穩定。

---

# 4. AEREC 的候選生成空間

## 4.1 候選生成不是任意重寫

令目前版本為 $B_t$ ，候選生成器為：

$$
\mathsf{Gen}
(
B_t,
O_t,
G_t,
K_t,
\Pi_t
)
=
\{B_{t+1}^{c_i}\}_{i=1}^{m},
$$

其中：

- $O_t$ ：觀測；
- $G_t$ ：改善目標；
- $K_t$ ：硬限制；
- $\Pi_t$ ：治理政策。

候選必須附帶生成理由，而不是只有修改結果：

$$
J_i
=
(
\text{problem},
\text{hypothesis},
\text{transformation},
\text{expected gain},
\text{known risk}
).
$$

## 4.2 主要改寫算子

AEREC 可對積木內部施加：

$$
\mathcal T_{\mathrm{AEREC}}
=
\{
\mathsf{Fuse},
\mathsf{Split},
\mathsf{Inline},
\mathsf{Extract},
\mathsf{Eliminate},
\mathsf{Share},
\mathsf{Reorder},
\mathsf{Parallelize},
\mathsf{Batch},
\mathsf{Cache},
\mathsf{Specialize},
\mathsf{Route},
\mathsf{ReplaceModel},
\mathsf{ChangeRuntime},
\mathsf{Isolate},
\mathsf{Repackage}
\}.
$$

這些算子作用於內部實現，不自動獲得修改外部契約的權力。

## 4.3 封裝邊界也可以演化

某些瓶頸不是節點本身，而是封裝邊界錯誤。例如：

- 兩個積木之間傳遞大量中間資料；
- 一個應該共享的快取被封裝在單一實例內；
- 一個具有獨立風險的步驟被錯誤包入高權限積木；
- 一個可並行區域被封裝成單一序列呼叫。

AEREC 可以提出：

$$
\partial B_t
\rightarrow
\partial B_{t+1}.
$$

但邊界變更可能改變：

- 端口；
- 狀態所有權；
- 權限；
- 副作用；
- 故障域；
- 上層組合方式。

因此，邊界演化必須重新進入封裝靜止屏障與契約推斷流程，而不能被當成普通內部最佳化。

---

# 5. 契約保持不是單一等價

## 5.1 七層相容性

候選 $B_c$ 與基準 $B_b$ 的相容性可拆為：

$$
\mathcal E(B_b,B_c)
=
(
E_{\mathrm{type}},
E_{\mathrm{interface}},
E_{\mathrm{behavior}},
E_{\mathrm{state}},
E_{\mathrm{effect}},
E_{\mathrm{safety}},
E_{\mathrm{stat}}
).
$$

### 型別相容

輸入輸出型別、端口方向與必要欄位相容。

### 介面相容

必需端口、錯誤通道、能力導入與版本約束相容。

### 行為相容

對契約要求的輸入集合，後置條件與不變量成立。

### 狀態相容

舊狀態可讀取、遷移或明確失效；更新規則不破壞狀態所有權。

### 效果相容

檔案、網路、資料庫、付款、通知或外部控制等效果不被隱藏增加。

### 安全相容

候選沒有擴張未核准的權限、資料外洩面或危險行為。

### 統計相容

對非確定性模型，候選在指定資料分布與信賴區間內符合品質要求。

## 5.2 確定性等價與統計等價

對確定性積木，可要求：

$$
\forall x\in X_{\mathrm{valid}},
\quad
F_c(x)=F_b(x)
$$

或更一般地：

$$
F_c(x)\equiv_C F_b(x).
$$

但對生成模型、檢索、分類或規劃型 Agent，不可能要求逐字輸出相同。此時應比較：

$$
Q(F_c,\mathcal D)
\ge
Q_{\min},
$$

並要求：

$$
\Pr
\left[
\Delta Q
\ge
-\epsilon
\right]
\ge
1-\alpha.
$$

其中：

- $\mathcal D$ ：評估分布；
- $\epsilon$ ：允許退化；
- $\alpha$ ：可接受錯判風險。

## 5.3 輸出等價不足以證明積木等價

若兩版本輸出相同，但候選額外：

- 把資料傳給第三方；
- 寫入未宣告檔案；
- 使用更高權限；
- 消耗十倍成本；
- 無法重播；
- 破壞狀態 Schema；

則它們不應被視為可替換。

因此：

$$
E_{\mathrm{output}}
\not\Rightarrow
E_{\mathrm{block}}.
$$

完整替換關係至少要求：

$$
E_{\mathrm{block}}
=
E_{\mathrm{contract}}
\land
E_{\mathrm{state}}
\land
E_{\mathrm{effect}}
\land
E_{\mathrm{safety}}.
$$

---

# 6. 證書不是一個分數

## 6.1 演化證書包

每個候選版本應附帶：

$$
Z_v
=
(
Z_{\mathrm{identity}},
Z_{\mathrm{provenance}},
Z_{\mathrm{schema}},
Z_{\mathrm{contract}},
Z_{\mathrm{tests}},
Z_{\mathrm{effects}},
Z_{\mathrm{safety}},
Z_{\mathrm{benchmark}},
Z_{\mathrm{deployment}}
).
$$

其中：

- $Z_{\mathrm{identity}}$ ：版本身分與內容指紋；
- $Z_{\mathrm{provenance}}$ ：父版本、生成者、工具、模型與轉換歷史；
- $Z_{\mathrm{schema}}$ ：結構與型別驗證；
- $Z_{\mathrm{contract}}$ ：契約保持證據；
- $Z_{\mathrm{tests}}$ ：測試與重播結果；
- $Z_{\mathrm{effects}}$ ：副作用與權限差異；
- $Z_{\mathrm{safety}}$ ：安全檢查；
- $Z_{\mathrm{benchmark}}$ ：品質、成本、延遲與資源結果；
- $Z_{\mathrm{deployment}}$ ：影子、金絲雀與正式流量觀測。

## 6.2 證書的強度分級

可定義：

| 級別 | 最低含義 |
|---|---|
| $Z_0$ | 僅有候選與來源，未驗證 |
| $Z_1$ | 結構、Schema、型別通過 |
| $Z_2$ | 單元測試與契約測試通過 |
| $Z_3$ | 差分、效果、安全與重播驗證通過 |
| $Z_4$ | 沙盒或離線 benchmark 通過 |
| $Z_5$ | 影子或金絲雀觀測通過 |
| $Z_6$ | 正式部署時間窗通過並成為穩定錨點 |

不同風險積木可要求不同最低等級：

$$
Z_{\min}
=
f(
\text{risk},
\text{effect},
\text{permission},
\text{blast radius}
).
$$

## 6.3 簽章與證明材料

內容指紋只能證明內容對應某個雜湊，不能單獨證明：

- 是誰產生；
- 由哪個流程產生；
- 是否通過指定測試；
- 是否在指定時間由可信執行器驗證。

因此，證書包應允許簽章、身份、時間戳與證明材料綁定：

$$
\operatorname{Attest}
(
h_v,
\text{subject},
\text{predicate},
\text{issuer},
t
).
$$

Sigstore 與 in-toto 的工程實踐顯示，簽章與 attestation 可以把工件身分、產生者及驗證述詞放入可驗證材料；但證書的存在不保證所有必要證書都被提供，因此 RABCL 還需要「必要證據集合」政策，防止只提交有利證據。

## 6.4 證據缺失也是狀態

候選評估不應只輸出成功或失敗，還需保留：

$$
\{
\text{PASS},
\text{FAIL},
\text{INCONCLUSIVE},
\text{MISSING},
\text{EXPIRED}
\}.
$$

當證據不完整時，正確結果是暫停或拒絕提升，而不是由 AI 自動補寫「推測通過」。

---

# 7. 候選選擇與多目標淨收益

## 7.1 不存在單一最佳版本

版本品質通常是向量：

$$
\mathbf q(B,e)
=
(
q_{\mathrm{correct}},
q_{\mathrm{quality}},
q_{\mathrm{latency}},
q_{\mathrm{cost}},
q_{\mathrm{memory}},
q_{\mathrm{energy}},
q_{\mathrm{safety}},
q_{\mathrm{maintain}},
q_{\mathrm{replay}}
).
$$

一個候選可能更快但更貴；更便宜但品質略降；品質更高但需要外部 API；可在 GPU 上運行但無法在本地 CPU 上使用。

因此，不應假設存在全域唯一：

$$
B^\ast
=
\arg\max_B q(B).
$$

更合理的是環境條件下的偏序或 Pareto 集：

$$
\mathcal P_e
=
\operatorname{Pareto}
\left(
\{B_i\},
\mathbf q,
e
\right).
$$

## 7.2 提升函數

令基準穩定版為 $B_s$ ，候選為 $B_c$ 。提升條件可寫為：

$$
\operatorname{Promote}(B_c)
\iff
\operatorname{HardConstraints}(B_c)
\land
\operatorname{EvidenceSufficient}(B_c)
\land
\Delta U(B_c,B_s;e)
>
\theta_e.
$$

其中：

$$
\Delta U
=
\sum_i w_i(e)\Delta q_i
-
\lambda_r R
-
\lambda_m M
-
\lambda_d D,
$$

- $R$ ：部署與安全風險；
- $M$ ：遷移成本；
- $D$ ：不可逆性與回滾困難；
- $\theta_e$ ：環境相關最低淨收益。

## 7.3 硬限制不能被加權抵消

某些條件不是分數，而是閘門：

$$
\operatorname{ContractOK}=1,
$$

$$
\operatorname{PermissionOK}=1,
$$

$$
\operatorname{RollbackReady}=1.
$$

不能用「速度提高很多」抵消「新增未授權資料外傳」。因此提升函數必須先通過硬限制，再比較軟目標。

---

# 8. 演化生命週期

## 8.1 候選狀態機

候選版本的最低狀態機為：

```text
OBSERVED
   │
   ▼
PROPOSED
   │
   ▼
GENERATED
   │
   ▼
STATIC_VALIDATED
   │
   ▼
SANDBOXED
   │
   ▼
SHADOWED
   │
   ▼
CANARY
   │
   ▼
PROMOTED
   │
   ▼
STABLE
```

任何階段都可以進入：

```text
REJECTED
QUARANTINED
INCONCLUSIVE
ROLLED_BACK
RETIRED
```

## 8.2 靜態驗證

在執行前完成：

- Schema；
- 型別；
- 依賴；
- 權限差異；
- 端口差異；
- 契約差異；
- 危險效果；
- 來源與內容指紋。

## 8.3 沙盒

沙盒階段使用隔離輸入、模擬能力與有限資源，避免候選接觸正式權限。

## 8.4 影子執行

影子執行可以接收正式輸入的複本，但不讓結果影響外部世界：

$$
x_{\mathrm{prod}}
\rightarrow
\begin{cases}
B_s(x) & \text{authoritative}\\
B_c(x) & \text{shadow}
\end{cases}
$$

影子版本的副作用必須被攔截、模擬或送入隔離命名空間。

## 8.5 金絲雀與漸進提升

若候選需要正式效果驗證，可逐步配置小比例流量：

$$
\rho_0
<
\rho_1
<
\cdots
<
\rho_k
=
1.
$$

每一階段都根據證據決定：

$$
\mathsf{continue},
\quad
\mathsf{pause},
\quad
\mathsf{abort},
\quad
\mathsf{rollback}.
$$

Kubernetes Deployment 的版本歷史、暫停、恢復、進度期限與回滾，以及 Argo Rollouts 的分析驅動金絲雀、藍綠部署與自動回退，提供了成熟的工程參照。RABCL 的差異在於：被部署的不只是容器映像，而是具有契約、狀態、效果與 CAIR 來源的積木版本。

---

# 9. 回滾不是「上一版」按鈕

## 9.1 五類回滾

定義：

$$
\mathcal R_B
=
\{
R_{\mathrm{pointer}},
R_{\mathrm{state}},
R_{\mathrm{compensate}},
R_{\mathrm{forward}},
R_{\mathrm{contain}}
\}.
$$

### 指標回切

把 RDR 的穩定引用重新指向舊版本：

$$
\operatorname{stable}
:
v_{n+1}
\rightarrow
v_n.
$$

適合無狀態或狀態完全外部化且相容的積木。

### 狀態回遷

把新狀態 Schema 遷回舊格式：

$$
M_{n+1\rightarrow n}
:
S_{n+1}
\rightarrow
S_n.
$$

只有存在可靠逆遷移時才可使用。

### 補償回滾

對已發生副作用執行補償：

$$
a
\xrightarrow{\text{compensate}}
\bar a.
$$

例如取消預約、發送更正、撤銷尚未結算交易。補償不保證世界回到完全相同狀態，只建立業務可接受的修復。

### 前向修復

當狀態或外部效果不可逆時，不能回到舊版本，只能發布修復版：

$$
v_{n+1}
\rightarrow
v_{n+2}^{\mathrm{fix}}.
$$

### 圍堵

若既不能立即回滾，也不能立刻修復，先限制流量、關閉危險能力或切換到降級模式。

## 9.2 回滾圖

每個可提升候選在部署前應存在：

$$
R_v
=
(
v_{\mathrm{fallback}},
M_{\mathrm{state}},
C_{\mathrm{effects}},
T_{\max},
L_{\mathrm{loss}}
).
$$

其中：

- $v_{\mathrm{fallback}}$ ：回退目標；
- $M_{\mathrm{state}}$ ：狀態處理；
- $C_{\mathrm{effects}}$ ：效果補償；
- $T_{\max}$ ：最大可接受回復時間；
- $L_{\mathrm{loss}}$ ：允許資料或功能損失。

若無法回答，則：

$$
\operatorname{RollbackReady}(v)=0.
$$

## 9.3 回滾窗口

舊版本若仍保留相容 Runtime、資料 Schema 與已熱啟動資源，可以快速回切。超過窗口後，依賴、資料與基礎設施可能已變化，回滾成本上升。

定義：

$$
W_r(v)
=
[t_{\mathrm{promote}},t_{\mathrm{expire}}].
$$

在窗口內可進行快速回切；窗口外必須重新驗證。Argo Rollouts 的 rollback window 顯示，保留有限數量舊修訂可以快速返回近期穩定版本。RABCL 應進一步把狀態 Schema 與能力依賴納入窗口判定。

---

# 10. 有狀態積木的演化

## 10.1 狀態 Schema 是契約的一部分

若積木具有：

$$
S_t
=
\operatorname{StateSchema}(B_t),
$$

則新版本必須聲明：

$$
M_{t\rightarrow t+1}
:
S_t
\rightarrow
S_{t+1}.
$$

可能策略包括：

- 向後相容讀取；
- 啟動時遷移；
- 背景遷移；
- 雙讀；
- 雙寫；
- 影子狀態；
- 狀態重建；
- 明確不相容。

## 10.2 雙版本並存

在漸進提升期間可能同時存在：

$$
B_t
\quad\text{與}\quad
B_{t+1}.
$$

若二者共享狀態，必須確保：

$$
\operatorname{ReadCompat}
\land
\operatorname{WriteCompat}.
$$

否則新版本寫出的資料可能使舊版本無法回切。

## 10.3 不可逆狀態變更

若：

$$
\nexists
M_{t+1\rightarrow t},
$$

則不能宣稱普通回滾可用。系統必須選擇：

- 保留舊狀態複本；
- 延遲不可逆遷移；
- 建立新命名空間；
- 使用事件重播重建；
- 標示只能前向修復；
- 禁止自動提升。

## 10.4 長時間工作流

對持續數小時、數天或更久的積木，版本提升時可能仍有舊執行在途。必須明確選擇：

- 舊執行繼續由舊版本完成；
- 在安全點遷移；
- 重新開始；
- 使用版本化步驟；
- 由新版本只接收新工作。

Temporal 的耐久執行模型提供一個重要參照：工作流歷史可讓執行在故障後恢復。然而，RABCL 還需額外處理積木版本族、契約證書及 AEREC 生成的候選實現。

---

# 11. 負知識：被拒絕版本也有價值

## 11.1 不能只保存成功版本

若 AEREC 每次都忘記失敗候選，會反覆生成同樣錯誤：

$$
B_c^{(1)}
\approx
B_c^{(2)}
\approx
\cdots
$$

因此需保存負知識：

$$
\mathcal N
=
\{
N_1,\ldots,N_k
\}.
$$

每項負知識至少包含：

$$
N_i
=
(
\text{pattern},
\text{context},
\text{failure},
\text{evidence},
\text{avoidance},
\text{expiry}
).
$$

## 11.2 負知識不是永久禁令

某候選在環境 $e_1$ 失敗，不代表在 $e_2$ 永遠失敗。因此失敗記錄必須帶有：

- 硬體；
- 模型；
- 資料分布；
- 依賴；
- 契約；
- 時間；
- 測試版本。

負知識可作為生成懲罰：

$$
\operatorname{ScoreCandidate}(B_c)
-
\lambda_N
\operatorname{Similarity}(B_c,\mathcal N).
$$

但當環境或前提改變時，可以重新評估，而非永久封死搜索空間。

---

# 12. 遞歸演化與版本族治理

## 12.1 演化遞歸

AEREC 的遞歸表示：

$$
B^{(t+1)}
=
\mathsf{Select}
\left(
\mathsf{Generate}
(
B^{(t)},
O_t
)
\right).
$$

新穩定版本成為下一輪觀測與生成的基準。

## 12.2 不等於執行遞歸

演化遞歸發生在版本生命週期：

$$
t\rightarrow t+1\rightarrow t+2.
$$

執行遞歸發生在單次運行中的呼叫堆疊或循環。兩者必須有不同限制與監控。

## 12.3 多分支版本族

不同環境可以同時維持：

$$
B_{\mathrm{cpu}},
\quad
B_{\mathrm{gpu}},
\quad
B_{\mathrm{edge}},
\quad
B_{\mathrm{cloud}}.
$$

它們共享定義身分與契約族，但具有不同實現與適用環境。AEREC 的目標不必把所有分支收斂成單一版本，而可以維持條件式路由：

$$
\mathsf{Resolve}(I_{\mathrm{def}},e)
=
B_e^\ast.
$$

## 12.4 分支合併

若候選 $B_a$ 改善效能， $B_b$ 改善安全，可以生成合併候選：

$$
B_m
=
\mathsf{Merge}(B_a,B_b).
$$

合併不是文字 diff 合併，而是 CAIR 結構、契約、狀態與效果的重新驗證。若兩個改寫互相衝突，必須建立新候選，不能把兩份證書直接相加。

---

# 13. 演化停止條件

## 13.1 沒有停止的演化不是成熟系統

若系統把「能生成更多候選」視為持續演化的理由，將造成：

- 算力浪費；
- benchmark 過擬合；
- 版本爆炸；
- 反覆部署；
- 使用者語義漂移；
- 安全審查疲勞；
- 回滾拓撲失控。

因此，停止是 AEREC 的一級能力。

## 13.2 七類停止條件

### 淨收益不足

若連續 $k$ 代：

$$
\Delta U_t
<
\epsilon,
$$

則停止或延長觀測窗口。

### 預算耗盡

$$
C_{\mathrm{compute}}
+
C_{\mathrm{validation}}
+
C_{\mathrm{deployment}}
>
B_{\max}.
$$

### 風險超限

$$
R(B_c)
>
R_{\max}.
$$

### 證據不足

候選反覆處於：

$$
\text{INCONCLUSIVE}
\quad\text{或}\quad
\text{MISSING}.
$$

### 震盪

若版本在策略 $A$ 與 $B$ 間反覆切換：

$$
A\rightarrow B\rightarrow A\rightarrow B,
$$

且沒有穩定淨收益，應停止並重新檢查目標函數。

### 契約邊界失效

若改善需要持續突破現有契約：

$$
\neg
\operatorname{Preserve}(C_{\mathrm{family}}),
$$

則停止「同一版本族」演化，轉為新定義或重大契約版本。

### 治理停止

人類、組織政策或上層 Agent 可以明確：

$$
\mathsf{pause},
\quad
\mathsf{freeze},
\quad
\mathsf{retire}.
$$

## 13.3 停止分數

可定義：

$$
\operatorname{StopScore}
=
w_1D_{\mathrm{diminish}}
+
w_2C_{\mathrm{budget}}
+
w_3R_{\mathrm{risk}}
+
w_4O_{\mathrm{oscillation}}
+
w_5E_{\mathrm{evidence}}
+
w_6G_{\mathrm{governance}}.
$$

當：

$$
\operatorname{StopScore}
\ge
\tau,
$$

系統進入停止或人工審查。

但此分數只用於決策輔助。硬風險、權限違規與契約破壞仍應直接觸發停止，不得被其他分數抵消。

---

# 14. 安全性與活性不變量

## 14.1 穩定版本不可原地變更

$$
\operatorname{Stable}(B_v)
\Rightarrow
\operatorname{Immutable}(P_v^\ast).
$$

## 14.2 每個提升都有證據

$$
\operatorname{Promoted}(B_v)
\Rightarrow
\exists Z_v.
$$

## 14.3 每個正式版本都有回復策略

$$
\operatorname{Production}(B_v)
\Rightarrow
\operatorname{RollbackPlan}(B_v)
\lor
\operatorname{ForwardOnlyDeclared}(B_v).
$$

## 14.4 Runtime 觀測不能直接改權威

$$
\operatorname{Observation}
\rightarrow
\operatorname{Proposal},
$$

而非：

$$
\operatorname{Observation}
\rightarrow
\operatorname{AuthorityMutation}.
$$

## 14.5 候選不接收未授權正式效果

$$
\operatorname{Candidate}(B_v)
\land
\neg\operatorname{EffectApproved}
\Rightarrow
\operatorname{EffectIsolated}.
$$

## 14.6 演化必須最終決定或停止

在有限政策窗口內，候選應進入：

$$
\{
\text{PROMOTED},
\text{REJECTED},
\text{PAUSED},
\text{EXPIRED}
\},
$$

避免永久停留在模糊候選狀態。

## 14.7 回滾不刪除歷史

$$
\operatorname{Rollback}(v_j\rightarrow v_i)
\not\Rightarrow
\operatorname{Delete}(v_j).
$$

失敗版本、證據與部署事件仍應被保留，以供審計與負知識使用。

---

# 15. 一個完整例子：圖片資產生成積木

假設積木：

$$
B_0
=
\texttt{GenerateValidatedAsset}
$$

內部包含：

1. 讀取素材；
2. 解析需求；
3. 產生提示；
4. 選擇圖片模型；
5. 生成候選圖；
6. 品質評分；
7. 不合格時重試；
8. 儲存資產；
9. 產生來源紀錄。

其外部契約要求：

- 輸入為素材與需求；
- 輸出為核准圖片與來源；
- 不得自動公開發布；
- 不得把私密素材送往未核准服務；
- 生成成本不得超過預算；
- 至少通過指定品質門檻。

## 15.1 觀測

RDR 觀測到：

- 重試率高；
- 某模型成本增加；
- 本地 GPU 閒置；
- 某類型圖片在模型 $M_2$ 品質更高。

## 15.2 候選

AEREC 生成：

$$
B_{1a}
=
\text{加入模型路由},
$$

$$
B_{1b}
=
\text{改用本地 GPU 批次},
$$

$$
B_{1c}
=
\text{將品質評分提前作為提示修正}.
$$

## 15.3 證書

三個候選分別產生：

- 契約測試；
- 私密資料路由檢查；
- 成本與品質 benchmark；
- 差分輸出評估；
- 影子執行；
- 效果攔截記錄。

## 15.4 選擇

若 $B_{1a}$ 品質提高但會將私密素材傳給未核准服務，硬限制失敗，直接拒絕。

若 $B_{1b}$ 成本降低但只適合具有指定 GPU 的環境，保留為環境分支：

$$
B_{\mathrm{gpu}}.
$$

若 $B_{1c}$ 在所有環境品質提升且契約保持，可成為通用穩定版。

## 15.5 回滾

若 $B_{1c}$ 上線後出現某類提示循環：

- 停止新流量；
- 指標回切 $B_0$ ；
- 保留新版本的失敗 Trace；
- 把問題加入負知識；
- 從 $B_0$ 或 $B_{1c}$ 分叉修復候選。

這個例子顯示，演化不是「AI 自動把工作流改好」，而是：

$$
\boxed{
\text{觀測}
\rightarrow
\text{候選族}
\rightarrow
\text{多層證據}
\rightarrow
\text{條件式選擇}
\rightarrow
\text{漸進提升}
\rightarrow
\text{可回復運行}
}
$$

---

# 16. 核心命題

## 命題一：候選隔離命題

AEREC 對穩定積木的任何改寫都必須形成新候選版本，不得原地修改既有權威版本。

## 命題二：版本族命題

演化積木的真實對象不是單一檔案，而是共享定義身分、契約族、演化圖、證書集合、部署狀態及回滾拓撲的版本族。

## 命題三：多層等價命題

候選可替換性不能只由輸出相似決定，還必須包含狀態、效果、安全、權限與統計品質。

## 命題四：證據先於提升命題

候選只有在必要證據集合達到該風險級別的最低門檻後，才能進入正式提升。

## 命題五：回滾拓撲命題

回滾不是單一版本指標，而是指標回切、狀態遷移、效果補償、前向修復與圍堵策略的組合。

## 命題六：負知識保存命題

被拒絕、退化或回滾的候選必須保留其失敗條件與證據，以降低重複探索和相同錯誤。

## 命題七：條件式最佳命題

不同硬體、資料分布、成本與安全條件下可以存在不同最適實現；AEREC 不必將所有環境強制收斂為單一版本。

## 命題八：停止必要命題

當淨收益不足、風險超限、證據不足、版本震盪、預算耗盡或契約邊界失效時，演化必須停止、暫停或轉為新積木定義。

---

# 17. 與既有工程機制的對照

Kubernetes Deployment 的更新機制保存修訂歷史，支援暫停、恢復、觀察進度及回滾到先前修訂。這說明版本提升不應只有「替換完成」與「替換失敗」兩個瞬間狀態，而需要可監測的 rollout 生命週期。

Argo Rollouts 進一步提供金絲雀、藍綠、分析、人工暫停、自動中止及回滾窗口。其核心啟示是：候選不應一次接收全部正式流量，證據可以在不同提升階段累積，分析結果也可以是成功、失敗或不確定。

Sigstore 與 in-toto attestation 顯示，版本內容、產生者、簽章、時間及驗證述詞可以形成可攜式證明材料。但簽章只能證明某項材料被特定身份簽署，不能單獨證明必要證據沒有被隱藏。RABCL 因此必須同時保存「已提交證據」與「政策要求的證據集合」。

Temporal 的耐久執行觀念則提醒：長時間工作流的執行狀態不能因程式版本更新而被簡單丟棄。RABCL 需在此基礎上增加積木契約、版本族、狀態遷移與 AEREC 候選治理。

本文的主張不是上述部署、簽章或耐久執行機制第一次出現，而是：

$$
\boxed{
\text{將 AI 生成的工作流實現候選，納入積木定義、契約、證書、部署、回滾與停止的一體化演化生命週期。}
}
$$

---

# 18. MVP 前的最低演化要求

後續 RABCL MVP 不應立即允許 AI 自主修改正式服務。最低實作只需完成受控本地演化閉環：

1. 一個已提交的穩定積木版本；
2. 從穩定版分叉候選；
3. 至少三種內部改寫算子；
4. 候選與穩定版內容指紋；
5. 契約、Schema、測試與 benchmark 證據；
6. 候選狀態機；
7. 人工批准提升；
8. 精確版本指標切換；
9. 一鍵回切舊穩定版；
10. 失敗候選與負知識保存；
11. 簡單停止條件；
12. 不允許候選直接取得不可逆正式效果。

最低演化驗收式為：

$$
\operatorname{Forkable}
\land
\operatorname{Verifiable}
\land
\operatorname{Promotable}
\land
\operatorname{Rollbackable}
\land
\operatorname{Stoppable}.
$$

第一版不要求：

- 自動正式部署；
- 自動調整全部流量；
- 跨組織證書基礎設施；
- 任意狀態 Schema 的自動逆遷移；
- 高風險外部副作用；
- 無人監督的版本提升；
- 全域最優搜索；
- 無限制多代演化。

---

# 結論

靜態積木只回答「這個工作流現在是什麼」；演化積木還要回答：

- 它可以產生哪些後代？
- 哪些後代保持相同契約？
- 哪些只適合特定環境？
- 誰生成了它們？
- 它們通過了哪些證據？
- 哪一版正在被誰使用？
- 出錯時如何回復？
- 哪些路徑已經證明失敗？
- 何時應該停止演化？

因此，RABCL 中的演化不應表示為：

$$
B
\rightarrow
B'
\rightarrow
B''
\rightarrow
\cdots
$$

而應表示為：

$$
\boxed{
\text{Stable Block}
\xrightarrow{\text{observe}}
\text{Candidate Family}
\xrightarrow{\text{verify}}
\text{Eligible Versions}
\xrightarrow{\text{progressive promotion}}
\text{New Stable Block}
}
$$

同時保留：

$$
\boxed{
\text{Certificates}
+
\text{Provenance}
+
\text{Negative Knowledge}
+
\text{Rollback Topology}
+
\text{Stopping Policy}
}
$$

AEREC 的價值不在於讓 AI 永遠重寫，而在於讓系統能夠在明確邊界內產生變體、以證據選擇、在風險可控時提升、在失敗時回復，並在沒有足夠理由繼續時停止。

至此，RABCL 已完成從工作流形成、封裝靜止、函數化、遞歸組合、權威派發到版本演化的基本理論鏈。下一篇將統合全系列，並把後續 MVP 限定在真正可實作、可驗收且不誇張的工程範圍內。

---

# 參考資料

1. Kubernetes Documentation, *Performing a Rolling Update* 與 *Update a Deployment Without Downtime*，關於版本化更新、暫停、進度監測、修訂歷史與回滾。
2. Argo Rollouts Documentation, *Analysis and Progressive Delivery*、*Rollback Window* 與 *Architecture*，關於金絲雀、藍綠、分析結果、自動提升、暫停與回退。
3. Sigstore Documentation, *Verifying Signatures*、*In-Toto Attestations* 與 *Bundle Format*，關於工件簽章、身份、證明述詞及可攜式驗證材料。
4. Temporal Documentation, *Temporal Platform Documentation*，關於耐久執行、故障後恢復與長時間工作流。
5. Neo.K／EveMissLab，AEREC（AI 自適應封裝與遞歸演化系統）系列文件。
6. Neo.K／Aletheia，RABCL 系列第 01–05 篇。
