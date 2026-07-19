# FMO–MRASG 第五研究批次

## 證書網路、長期漂移、近似偏誤、合法性衝突與身份去僭越

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

第四批次已將事實模態本體論推進到證書、邊界、語義近似、治理與身份回饋層。

目前已有：

$$
\mathfrak C
=
\left\langle
\mathsf{Cert},
G_{\mathrm{Cert}},
\operatorname{Defeat},
\operatorname{CertStatus},
\mathcal H_{\mathrm{Cert}}
\right\rangle
$$

強化本體邊界證書：

$$
\operatorname{BCert}^{+}
$$

語義等價三區判定：

$$
\mathsf{ProvedEq},
\mathsf{ProvedNeq},
\mathsf{Undetermined}
$$

元治理選擇事件：

$$
\mathsf{Sel}
=
\left\langle
A,C,P,S,E,R,T
\right\rangle
$$

以及身份治理回饋：

$$
\mathcal Q_I^\ell
:
\left(
J_I^\ell,\mathbf r_I^\ell
\right)
\rightarrow
\Delta\mathbf c_I^\ell
$$

但這些機制本身仍可能形成新的封閉問題。

例如：

1. 證書可以互相引用，最後形成循環自證；
2. 每一步都在邊界內，長期累積後卻可能完全越界；
3. 語義近似維度由誰選擇，可能直接決定誰被判定為相似；
4. 合法性向量之間可能互相衝突，且高分總和可能掩蓋底線破壞；
5. 制度先宣告身份，再用宣告造成的結果證明該身份，形成自我實現鎖定。

因此，本批次選取以下五個節點：

```text
FMO-218  證書依賴循環與證書網路可信度
FMO-219  邊界漂移門檻與非傳遞性
FMO-220  語義近似維度的完備性與偏誤
FMO-221  合法性衝突與不可補償門檻
FMO-222  身份回饋鎖定與去僭越機制
```

本批次的核心任務是：

> 防止理論中的驗證機制、近似機制與治理機制，反過來形成不可質疑的自我強化結構。

---

# 1. 輸入圖

第四批次輸出：

$$
\mathcal G_{\mathrm{FMO}}^{(4)}
$$

其主要結構包括：

證書系統：

$$
\mathsf{Cert}
=
\left\langle
claim,
base,
method,
scope,
assumptions,
provenance,
confidence,
falsifier,
version
\right\rangle
$$

邊界狀態向量：

$$
\mathbf B_\eta(O,O')
=
\left\langle
B_P,
B_C,
B_M,
B_L,
B_S,
B_D,
B_N
\right\rangle
$$

語義近似輪廓：

$$
\mathbf E(P_1,P_2)
=
\left\langle
E_{\mathrm{struct}},
E_{\mathrm{beh}},
E_{\mathrm{causal}},
E_{\mathrm{hist}},
E_{\mathrm{id}},
E_{\mathrm{norm}},
E_{\mathrm{modal}}
\right\rangle
$$

合法性向量：

$$
\mathbf L(\mathsf{Sel})
=
\left\langle
L_A,
L_P,
L_I,
L_T,
L_R,
L_M,
L_U
\right\rangle
$$

多層身份向量：

$$
\mathbf J_I(x)
=
\left\langle
J_P,
J_C,
J_M,
J_L,
J_S,
J_D,
J_{\mathrm{self}}
\right\rangle
$$

---

# 2. 節點 A：證書依賴循環與證書網路可信度

## A-R0：點層

> 證書網路可以包含循環，但循環本身不能增加外部證據；可信度必須來自獨立錨點、非循環支持或被明確標記的互相依賴群。

---

## A-R1：線層

第四批次要求每項證書保存依賴：

$$
G_{\mathrm{Cert}}
=
(V_C,E_C)
$$

但若：

$$
C_1\rightarrow C_2
$$

且：

$$
C_2\rightarrow C_1
$$

兩項證書可能互相支持，看起來形成高度一致的網路。

然而，若兩者沒有外部資料、實驗、原始公理或獨立證明，這只是：

> 兩個主張互相引用。

因此證書網路必須區分：

- 支持關係；
- 派生關係；
- 來源共用；
- 相互依賴；
- 獨立錨定。

---

## A-R2：面層

### A1. 證書依賴圖的邊類型

將證書圖擴充為：

$$
G_{\mathrm{Cert}}
=
(V_C,E_C,\Lambda_C)
$$

其中邊標籤包括：

- `derives_from`；
- `uses_data_from`；
- `assumes`；
- `translates_from`；
- `corroborates`；
- `defeats`；
- `shares_source_with`；
- `audits`；
- `reproduces`。

不同邊不能被等同為「支持」。

---

### A2. 強連通證書群

若一組證書形成強連通分量：

$$
\mathsf{SCC}_C
=
\{C_1,\ldots,C_n\}
$$

則群內任一證書都可經依賴路徑返回自身。

這類結構不必然錯誤，但不能把群內引用次數當作新增證據。

定義外部入邊：

$$
\operatorname{InExt}(\mathsf{SCC}_C)
$$

若：

$$
\operatorname{InExt}(\mathsf{SCC}_C)=\varnothing
$$

則該群是封閉證書循環。

---

### A3. 循環不增益原則

對同一強連通群內的重複支持，可信度不得循環放大。

若：

$$
C_i,C_j\in\mathsf{SCC}_C
$$

則：

$$
\operatorname{Gain}(C_i\leftrightarrow C_j)=0
$$

除非新增：

- 外部資料；
- 獨立實驗；
- 新反例檢驗；
- 不同方法的獨立重建；
- 可驗證的新推論。

---

### A4. 獨立錨點

證書可信度需要至少一種錨點：

$$
a\in\mathcal A_C
$$

錨點類型包括：

- 原始觀測；
- 可重複實驗；
- 形式公理與機器驗證；
- 可直接檢查的構造；
- 外部資料；
- 獨立實作；
- 世界實例。

但形式公理錨定只證明：

$$
\text{相對於公理的有效性}
$$

不自動證明世界真實性。

---

### A5. 來源相關性

兩項證書即使由不同模型生成，也可能共享：

- 同一訓練資料；
- 同一論文；
- 同一提示；
- 同一程式庫；
- 同一錯誤假設。

定義來源相關矩陣：

$$
R_C(i,j)
\in
[0,1]
$$

若：

$$
R_C(i,j)\approx1
$$

則兩項證書不能被當作兩份獨立證據。

---

### A6. 證書網路可信度輪廓

對證書 $C$ 定義：

$$
\mathbf T_C(C)
=
\left\langle
T_A,
T_D,
T_R,
T_F,
T_X,
T_U
\right\rangle
$$

其中：

- $T_A$ ：錨點強度；
- $T_D$ ：依賴透明度；
- $T_R$ ：可重現性；
- $T_F$ ：可反駁性；
- $T_X$ ：來源獨立性；
- $T_U$ ：未解依賴比例。

---

### A7. 循環容許條件

某些循環是正當的，例如：

- 相互約束的方程組；
- 固定點證明；
- 語義與語法的互相定義；
- 多模組互相驗證。

但必須提供循環合法性證書：

$$
\mathsf{CycleCert}
=
\left\langle
SCC,
semantics,
fixedpoint,
\text{external\_anchor},
noninflation
\right\rangle
$$

其中：

- $semantics$ ：循環的解釋；
- $fixedpoint$ ：是否存在穩定解；
- $\text{external\_anchor}$ ：是否有外部錨定；
- $noninflation$ ：是否避免可信度自我膨脹。

---

### A8. 證書網路狀態

定義：

$$
\operatorname{CertNetStatus}
\in
\{
\mathsf{Anchored},
\mathsf{PartiallyAnchored},
\mathsf{CircularButStable},
\mathsf{SelfSupporting},
\mathsf{Fragmented},
\mathsf{Contested},
\mathsf{Unknown}
\}
$$

---

### A9. 擊敗關係的循環

可能出現：

$$
C_1\triangleright C_2
$$

且：

$$
C_2\triangleright C_1
$$

此時不能簡單宣布兩者都無效。

應分析：

- 擊敗作用域；
- 擊敗依賴；
- 是否針對同一主張；
- 是否只是不同假設下互相排斥。

可形成條件化狀態：

$$
C_1\mid A_1
$$

與：

$$
C_2\mid A_2
$$

---

## A-局部決定

證書系統升級為網路可信度架構：

$$
\boxed{
\mathfrak C_2
=
\left\langle
G_{\mathrm{Cert}},
\mathsf{SCC}_C,
\mathcal A_C,
R_C,
\mathbf T_C,
\mathsf{CycleCert}
\right\rangle
}
$$

並採用：

$$
\boxed{
\text{循環不增益原則}
}
$$

證書循環可以存在，但不能只靠互相引用增加可信度。

---

## A-新增節點

```text
FMO-218A  證書邊型別
FMO-218B  證書強連通分量
FMO-218C  封閉證書循環
FMO-218D  循環不增益原則
FMO-218E  證書獨立錨點
FMO-218F  來源相關矩陣
FMO-218G  證書網路可信度輪廓
FMO-218H  循環合法性證書
FMO-218I  證書網路狀態
FMO-218J  擊敗循環條件化
```

---

# 3. 節點 B：邊界漂移門檻與非傳遞性

## B-R0：點層

> 本體延續不是逐步延續的簡單傳遞閉包；長期判定必須同時追蹤局部合法性、累積漂移、關鍵斷點與路徑壓縮後的全局差異。

---

## B-R1：線層

第四批次指出：

$$
O_0\sim_B O_1
$$

且：

$$
O_1\sim_B O_2
$$

不必推出：

$$
O_0\sim_B O_2
$$

若每一步都只有極小改變，仍可能產生：

$$
O_0
\rightarrow
O_1
\rightarrow
\cdots
\rightarrow
O_n
$$

而：

$$
O_n
$$

與：

$$
O_0
$$

已屬不同本體。

問題是：

> 漂移到什麼程度才算越界？

單一固定門檻：

$$
\theta_B
$$

可能過於武斷。

---

## B-R2：面層

### B1. 局部漂移與全局漂移

定義局部漂移：

$$
\delta_i
=
d_B(O_i,O_{i+1})
$$

累積路徑長度：

$$
D_{\mathrm{path}}
=
\sum_{i=0}^{n-1}
\delta_i
$$

端點漂移：

$$
D_{\mathrm{end}}
=
d_B(O_0,O_n)
$$

兩者不必相等。

若路徑繞行後返回近似狀態，可能：

$$
D_{\mathrm{path}}\gg D_{\mathrm{end}}
$$

若每一步改變在粗粒度測量下被低估，可能：

$$
D_{\mathrm{path}}<D_{\mathrm{end}}
$$

---

### B2. 關鍵斷點

某些變化即使數量很小，也可能造成質變。

定義關鍵事件集合：

$$
\mathcal K_B
=
\{
k_1,\ldots,k_m
\}
$$

例如：

- 核心生成規則被替換；
- 祖源鏈被永久切斷；
- 身份規則由單一延續改為任意複製；
- 實際性制度被改寫；
- 所有歷史記錄被清除；
- 模態空間生成規則被更換。

若：

$$
k_j\in\eta
$$

可能直接造成局部維度越界，不必等待累積門檻。

---

### B3. 多尺度漂移

不同觀測尺度得到不同漂移。

定義：

$$
D_B^{\sigma,\ell}(\eta)
$$

其中：

- $\sigma$ ：觀測尺度；
- $\ell$ ：本體層。

例如微觀部件全部替換，但宏觀功能保持。

因此漂移判定應為張量：

$$
\mathbf D_B(\eta)
=
\left[
D_B^{\sigma,\ell}
\right]
$$

---

### B4. 自適應門檻

門檻不應是單一常數，而應依賴：

$$
\theta_B
=
\theta_B
\left(
\ell,
\sigma,
purpose,
risk,
reversibility,
evidence
\right)
$$

例如：

- 法律責任判定要求較嚴；
- 工程版本相容可容忍較大內部改變；
- 高風險人格遷移要求更強祖源證據；
- 可逆實驗可使用較寬鬆門檻。

---

### B5. 不可補償斷裂

某些維度不能由其他維度補償。

例如：

- 祖源完全中斷；
- 核心權利被不可逆刪除；
- 主體記憶被全部抹除；
- 生成規則被完全替換。

即使其他維度高度相似，仍可能越界。

定義不可補償條件：

$$
K_j(\eta)=0
\Rightarrow
B_j=\mathsf{Broken}
$$

---

### B6. 滯後與回復

本體可能越界後又恢復表面結構。

但：

$$
O_0
\rightarrow
O_{\mathrm{break}}
\rightarrow
O_n\simeq O_0
$$

不必表示原本體延續。

因此邊界具有滯後：

$$
\operatorname{Hyst}_B(\eta)
$$

過去斷裂會影響現在判定。

---

### B7. 路徑分段

長期路徑可分成：

$$
\eta
=
\eta_1\oplus\eta_2\oplus\cdots\oplus\eta_m
$$

每段具有：

- 穩定區；
- 漂移區；
- 相變點；
- 重建區。

因此邊界分析不應只輸出終值，而應輸出分段圖。

---

### B8. 邊界判定輸出

定義：

$$
\operatorname{BStatus}
\left(
O_0,O_n;\eta
\right)
=
\left\langle
\mathbf B,
\mathbf D_B,
\mathcal K_B,
\operatorname{Hyst}_B,
\mathcal S_\eta
\right\rangle
$$

其中：

- $\mathbf B$ ：各層邊界狀態；
- $\mathbf D_B$ ：多尺度漂移；
- $\mathcal K_B$ ：關鍵事件；
- $\operatorname{Hyst}_B$ ：歷史滯後；
- $\mathcal S_\eta$ ：路徑分段。

---

### B9. 非傳遞不等於無法推理

雖然：

$$
\sim_B
$$

不具全域傳遞性，但可建立有界傳遞：

若：

$$
D_B(\eta)<\theta_B
$$

且無關鍵斷裂，則某段內可允許：

$$
O_i\approx_B O_j
$$

這形成局部傳遞區，而不是完全放棄連續推理。

---

## B-局部決定

長期本體邊界不再以單一門檻判定，而改為：

$$
\boxed{
\operatorname{BStatus}
=
\left\langle
\mathbf B,
\mathbf D_B,
\mathcal K_B,
\operatorname{Hyst}_B,
\mathcal S_\eta
\right\rangle
}
$$

並採用：

1. 多尺度漂移；
2. 關鍵斷點；
3. 自適應門檻；
4. 不可補償條件；
5. 歷史滯後；
6. 路徑分段。

---

## B-新增節點

```text
FMO-219A  局部漂移／全局漂移
FMO-219B  關鍵斷點集合
FMO-219C  多尺度漂移張量
FMO-219D  自適應邊界門檻
FMO-219E  不可補償斷裂
FMO-219F  邊界滯後
FMO-219G  路徑分段
FMO-219H  長期邊界狀態
FMO-219I  局部有界傳遞
```

---

# 4. 節點 C：語義近似維度的完備性與偏誤

## C-R0：點層

> 近似維度不是中立觀測表；選擇哪些維度、忽略哪些維度，本身就是理論決策，必須接受缺漏搜尋、對抗測試與多觀測者審查。

---

## C-R1：線層

第四批次建立：

$$
\mathbf E(P_1,P_2)
=
\left\langle
E_{\mathrm{struct}},
E_{\mathrm{beh}},
E_{\mathrm{causal}},
E_{\mathrm{hist}},
E_{\mathrm{id}},
E_{\mathrm{norm}},
E_{\mathrm{modal}}
\right\rangle
$$

但這七個維度並不必然完備。

可能遺漏：

- 時序；
- 空間；
- 主體經驗；
- 權力；
- 資源；
- 風險；
- 可恢復性；
- 尺度依賴；
- 資訊與記錄；
- 環境耦合。

若維度被遺漏，兩個本體可能被錯判為相似。

---

## C-R2：面層

### C1. 觀測架構

將近似輪廓視為觀測架構：

$$
\mathcal O_E
=
\left\{
q_1,\ldots,q_n
\right\}
$$

每個：

$$
q_i
$$

是一個觀測、干預或比較算子。

因此：

$$
\mathbf E_{\mathcal O_E}(P_1,P_2)
$$

始終相對於觀測架構成立。

---

### C2. 維度盲區

若存在性質：

$$
p^\ast
$$

使：

$$
p^\ast
\notin
\operatorname{Span}(\mathcal O_E)
$$

則：

$$
p^\ast
$$

是目前近似架構的盲區。

兩個本體可能在所有已選維度近似：

$$
\mathbf E_{\mathcal O_E}(P_1,P_2)\approx\mathbf 1
$$

但在：

$$
p^\ast
$$

上根本不同。

---

### C3. 完備性不能被絕對證明

對一般本體而言，無法確保有限維度集合涵蓋所有重要差異。

因此不應聲稱：

$$
\mathcal O_E
$$

絕對完備。

只能定義任務相對完備：

$$
\operatorname{Complete}
\left(
\mathcal O_E
\mid
D,\mathcal Q,\epsilon
\right)
$$

其中：

- $D$ ：任務域；
- $\mathcal Q$ ：已知問題族；
- $\epsilon$ ：容許遺漏程度。

---

### C4. 對抗性維度搜尋

建立維度生成器：

$$
\mathcal A_E
$$

主動尋找能最大化兩者差異的新觀測：

$$
q^\ast
=
\arg\max_{q\in\mathcal Q_{\mathrm{cand}}}
\operatorname{Disc}_q(P_1,P_2)
$$

如果找到高區分力維度，就更新：

$$
\mathcal O_E
\leftarrow
\mathcal O_E\cup\{q^\ast\}
$$

---

### C5. 受影響者維度

純技術觀測者可能忽略：

- 疼痛；
- 排除；
- 失去權利；
- 不可申訴；
- 被迫遷移；
- 身份抹除。

因此近似維度來源應包括：

$$
\mathcal O_E^{\mathrm{stake}}
$$

即受影響者提出的比較維度。

---

### C6. 權力偏誤

若某主體控制：

- 維度定義；
- 數據取得；
- 權重配置；
- 顯示介面；
- 門檻設定；

則其可能使對自身有利的差異消失。

定義：

$$
\operatorname{ObsCaptureRisk}
=
f
\left(
\operatorname{DimensionControl},
\operatorname{DataControl},
\operatorname{WeightControl},
\operatorname{VisibilityControl}
\right)
$$

---

### C7. 維度來源標註

每一維度應保存：

$$
q_i
=
\left\langle
definition,
purpose,
author,
stakeholders,
scope,
\text{failure\_modes},
version
\right\rangle
$$

---

### C8. 不可壓縮差異

某些差異不適合壓縮成 $0$ 到 $1$ 的相似度。

例如：

- 是否存在不可逆權利剝奪；
- 是否發生祖源斷裂；
- 是否出現世界矛盾；
- 是否缺少必要主體同意。

這些應表示為離散警示：

$$
\mathcal F_{\mathrm{critical}}
$$

---

### C9. 多觀測架構並存

不同任務可以使用不同：

$$
\mathcal O_E^{(1)},
\mathcal O_E^{(2)},\ldots
$$

系統不應強迫所有領域共用一個近似輪廓。

但不同架構之間需要對照：

$$
\operatorname{Map}
\left(
\mathcal O_E^{(i)},
\mathcal O_E^{(j)}
\right)
$$

---

### C10. 近似偏誤報告

每次語義近似輸出應附帶：

$$
\mathsf{BiasReport}
=
\left\langle
covered,
omitted,
stakeholders,
\text{critical\_flags},
\text{capture\_risk},
uncertainty
\right\rangle
$$

---

## C-局部決定

語義近似改為觀測架構相對判定：

$$
\boxed{
\mathbf E_{\mathcal O_E}(P_1,P_2)
}
$$

並加入：

1. 任務相對完備；
2. 對抗性維度搜尋；
3. 受影響者維度；
4. 權力捕獲風險；
5. 不可壓縮關鍵差異；
6. 近似偏誤報告。

---

## C-新增節點

```text
FMO-220A  語義觀測架構
FMO-220B  維度盲區
FMO-220C  任務相對完備性
FMO-220D  對抗性維度搜尋
FMO-220E  受影響者維度
FMO-220F  觀測權力捕獲風險
FMO-220G  維度來源標註
FMO-220H  不可壓縮關鍵差異
FMO-220I  多觀測架構映射
FMO-220J  近似偏誤報告
```

---

# 5. 節點 D：合法性衝突與不可補償門檻

## D-R0：點層

> 合法性不是可任意加權的效用總分；某些底線一旦被破壞，其他維度的高分不能補償，衝突必須被顯式保存與治理。

---

## D-R1：線層

第四批次建立合法性向量：

$$
\mathbf L(\mathsf{Sel})
=
\left\langle
L_A,
L_P,
L_I,
L_T,
L_R,
L_M,
L_U
\right\rangle
$$

但合法性維度之間可能衝突：

- 高效率與充分參與衝突；
- 快速決策與程序完整衝突；
- 多數意志與少數保護衝突；
- 制度穩定與退出權衝突；
- 透明度與隱私衝突。

若直接加權：

$$
L_{\mathrm{sum}}
=
\sum_i w_iL_i
$$

可能出現：

> 完全沒有申訴機制，但因效率高而仍取得高總分。

---

## D-R2：面層

### D1. 不可補償維度

定義不可補償集合：

$$
\mathcal N_L
\subseteq
\{L_A,L_P,L_I,L_T,L_R,L_M,L_U\}
$$

若某項：

$$
L_j<\theta_j
$$

則選擇事件不能被判為完整合法，即使其他維度很高。

---

### D2. 絕對底線與情境底線

某些底線可能普遍適用，例如：

- 不得完全無來源；
- 不得隱藏受影響者；
- 不得取消所有申訴；
- 不得偽造證據；
- 不得將制度選擇偽裝成世界真理。

另一些門檻依情境變化，例如：

- 緊急狀態中的參與程度；
- 高風險技術的可逆性要求；
- 私人系統與公共制度的透明度差異。

因此：

$$
\theta_j
=
\theta_j(context,risk,scope,duration)
$$

---

### D3. 合法性衝突圖

建立：

$$
G_L
=
(V_L,E_L)
$$

其中節點是合法性要求，邊表示：

- 衝突；
- 支持；
- 依賴；
- 優先；
- 條件化例外。

例如：

$$
L_I
\xleftrightarrow{\mathrm{conflict}}
Privacy
$$

---

### D4. 衝突不能被隱藏

當合法性要求無法同時最大化時，系統應輸出：

$$
\operatorname{LegitConflict}
=
\left\langle
requirements,
stakeholders,
tradeoff,
losers,
mitigation,
review
\right\rangle
$$

而不是只輸出最佳方案。

---

### D5. 否決權與否決濫用

不可補償底線可能產生否決權。

但否決權也可能被濫用。

因此每個否決需要：

$$
\mathsf{VetoCert}
=
\left\langle
ground,
scope,
evidence,
affected,
duration,
appeal
\right\rangle
$$

---

### D6. 不可逆性提升門檻

若選擇不可逆：

$$
\operatorname{Irrev}(\mathsf{Sel})\uparrow
$$

則合法性門檻應提高：

$$
\theta_j
\uparrow
$$

同理，影響範圍與持續時間越大，要求越嚴格。

---

### D7. 合法性 Pareto 前沿

若多方案互有優劣，保留：

$$
\operatorname{Pareto}_L
$$

而不是立即壓成唯一排名。

但所有方案仍需先通過不可補償底線。

---

### D8. 臨時合法性

在緊急或資訊不足情況下，可授予：

$$
\mathsf{ProvisionalLegitimacy}
$$

條件包括：

- 有期限；
- 可撤銷；
- 有事後審查；
- 不得擴張適用域；
- 保存受損權益記錄。

---

### D9. 合法性債務

若緊急制度犧牲部分程序，會累積：

$$
D_L
$$

合法性債務。

未來必須以：

- 補償；
- 說明；
- 審查；
- 恢復權利；
- 重新授權；

進行償還。

---

### D10. 最終合法性狀態

定義：

$$
\operatorname{LegitStatus}
\in
\{
\mathsf{Full},
\mathsf{Qualified},
\mathsf{Provisional},
\mathsf{Contested},
\mathsf{Illegitimate},
\mathsf{Undetermined}
\}
$$

---

## D-局部決定

合法性判定改為兩階段：

第一階段，檢查不可補償底線：

$$
\forall j\in\mathcal N_L,
\quad
L_j\geq\theta_j
$$

第二階段，在通過底線的方案中比較：

$$
\operatorname{Pareto}_L
$$

若存在未解衝突，必須輸出合法性衝突報告，而不是隱藏於總分。

---

## D-新增節點

```text
FMO-221A  不可補償合法性維度
FMO-221B  情境化合法性門檻
FMO-221C  合法性衝突圖
FMO-221D  合法性衝突報告
FMO-221E  否決證書
FMO-221F  不可逆性門檻提升
FMO-221G  合法性 Pareto 前沿
FMO-221H  臨時合法性
FMO-221I  合法性債務
FMO-221J  多值合法性狀態
```

---

# 6. 節點 E：身份回饋鎖定與去僭越機制

## E-R0：點層

> 制度身份可能透過記錄、資源與承認形成自我實現鎖定；解除鎖定需要保留層級差異、反事實基線、申訴通道、記錄更正與身份多重見證。

---

## E-R1：線層

第四批次指出制度可形成：

$$
\mathbf c_I
\rightarrow
J_I
\rightarrow
\mathbf r_I
\rightarrow
\mathbf c_I'
$$

這個回饋可以是正向的，但也可能形成鎖定。

例如：

1. 制度判定某主體不具資格；
2. 因而取消資源與記錄；
3. 主體失去持續身份的條件；
4. 制度再以「缺乏持續性」證明原判定正確。

此結構可寫成：

$$
J_t^{-}
\rightarrow
\mathbf r_t^{-}
\rightarrow
\Delta\mathbf c_{t+1}^{-}
\rightarrow
J_{t+1}^{-}
$$

---

## E-R2：面層

### E1. 身份回饋鎖定

定義：

$$
\mathsf{IFL}
=
\operatorname{IdentityFeedbackLock}
$$

當以下條件成立：

1. 制度判定改變身份延續條件；
2. 新條件被用作原判定的證據；
3. 缺乏外部反證通道；
4. 記錄由同一制度控制；
5. 主體無法恢復被剝奪的見證。

---

### E2. 正回饋與負回饋

身份回饋可分為：

$$
\mathcal Q_I^{+}
$$

身份增強回饋；

以及：

$$
\mathcal Q_I^{-}
$$

身份削弱回饋。

兩者都可能造成鎖定。

例如過度增強也可能使某制度身份壟斷其他身份層。

---

### E3. 反事實基線

判斷制度是否自證，需要比較：

$$
\mathbf c_I^{\mathrm{obs}}
$$

觀測到的身份延續；

與：

$$
\mathbf c_I^{\mathrm{cf}}
$$

若沒有該制度干預時的反事實延續。

定義制度構成效應：

$$
\Delta_{\mathrm{inst}}
=
\mathbf c_I^{\mathrm{obs}}
-
\mathbf c_I^{\mathrm{cf}}
$$

若制度先削弱身份，再把削弱結果當作自然事實，就構成回饋偏差。

---

### E4. 外部身份見證

身份判定不能只依賴單一制度記錄。

需要多來源見證：

$$
\mathcal W_I
=
\{
w_{\mathrm{self}},
w_{\mathrm{social}},
w_{\mathrm{causal}},
w_{\mathrm{memory}},
w_{\mathrm{digital}},
w_{\mathrm{legal}},
w_{\mathrm{historical}}
\}
$$

---

### E5. 記錄可更正性

身份記錄必須支持：

- 更正；
- 附註異議；
- 版本歷史；
- 來源分離；
- 不刪除原始爭議；
- 恢復被錯誤合併或分裂的身份。

定義：

$$
\operatorname{Rectifiable}(R_I)
$$

---

### E6. 去僭越條件

若制度判定只在：

$$
\ell=\mathrm{legal}
$$

有效，不得自動擴張至：

$$
\ell\in
\{
physical,
causal,
memory,
self
\}
$$

建立作用域防火牆：

$$
\operatorname{ScopeFirewall}
\left(
J_I^\ell
\right)
$$

---

### E7. 申訴與獨立審查

身份判定需要：

$$
\mathcal A_I
$$

申訴機制；

以及：

$$
\mathcal R_I
$$

獨立審查機制。

審查者不得完全依賴原制度的同一資料與規則，否則只是形式上的第二次確認。

---

### E8. 身份恢復

若錯誤制度判定造成身份延續受損，需要：

$$
\operatorname{Restore}_I
$$

其可能包括：

- 恢復記錄；
- 恢復權利；
- 補充歷史；
- 保存斷裂原因；
- 重新建立社會承認；
- 補償因錯誤判定造成的延續損失。

---

### E9. 不可逆身份損失

某些損害不可完全恢復，例如：

- 記憶被刪除；
- 主體死亡；
- 原始資料永久遺失；
- 社會關係不可逆破裂。

因此恢復結果應標記：

$$
\operatorname{RestoreStatus}
\in
\{
\mathsf{Full},
\mathsf{Partial},
\mathsf{Symbolic},
\mathsf{Impossible},
\mathsf{Undetermined}
\}
$$

---

### E10. 身份治理審計

定義身份治理審計：

$$
\mathsf{IGA}
=
\left\langle
feedback,
counterfactual,
witnesses,
scope,
appeal,
rectification,
restoration
\right\rangle
$$

---

### E11. 去僭越不是否定制度身份

法律、社會與數位身份仍可能真實且重要。

去僭越的目標不是：

> 制度不能構成身份。

而是：

> 制度不得把局部構成權擴張成對全部存在層的絕對主權。

---

## E-局部決定

身份治理系統新增：

$$
\boxed{
\mathsf{IGA}
=
\left\langle
feedback,
counterfactual,
witnesses,
scope,
appeal,
rectification,
restoration
\right\rangle
}
$$

並要求：

1. 回饋鎖定檢測；
2. 反事實基線；
3. 多來源身份見證；
4. 作用域防火牆；
5. 可更正記錄；
6. 獨立申訴；
7. 身份恢復與不可逆損失標記。

---

## E-新增節點

```text
FMO-222A  身份回饋鎖定 IFL
FMO-222B  正向／負向身份回饋
FMO-222C  制度身份反事實基線
FMO-222D  多來源身份見證
FMO-222E  身份記錄可更正性
FMO-222F  身份作用域防火牆
FMO-222G  身份申訴與獨立審查
FMO-222H  身份恢復
FMO-222I  不可逆身份損失
FMO-222J  身份治理審計
```

---

# 7. 跨節點對齊

本批次五個節點共同處理同一類結構：

> 系統先產生判定，再由判定改造世界或模型，最後使用被改造後的結果證明原判定。

這可稱為：

$$
\mathsf{ReflexiveClosureRisk}
$$

即反身封閉風險。

---

## 7.1 證書循環與身份回饋

證書可能互相引用，身份制度也可能互相證明。

例如：

```text
法律記錄
→ 證明法律身份
→ 法律身份允許建立更多記錄
→ 新記錄再證明法律身份
```

若缺乏外部身份見證，就形成制度—證書聯合循環。

---

## 7.2 邊界漂移與制度鎖定

制度可能逐步修改身份規則，每次改動都很小。

但長期可能導致：

$$
\Gamma_I^{(0)}
\rightarrow
\Gamma_I^{(n)}
$$

完全改寫誰有資格被視為主體。

因此身份治理也需要長期邊界漂移審查。

---

## 7.3 近似維度與合法性

如果治理者控制近似維度，就能使某些合法性損害不可見。

例如不測量：

- 少數者損失；
- 不可逆性；
- 退出障礙；
- 身份抹除。

則方案可能在可見指標上表現優良。

---

## 7.4 合法性底線與證書可信度

任何治理選擇若依賴封閉證書循環，其資訊透明度與證據合法性維度應被降級。

---

## 7.5 共同反封閉機制

五個節點共同需要：

1. 外部錨點；
2. 多來源見證；
3. 作用域限制；
4. 反事實比較；
5. 版本歷史；
6. 可申訴性；
7. 不可補償底線；
8. 主動反例搜尋。

---

# 8. 第五批次後的更新核心

## 8.1 證書網路系統

$$
\boxed{
\mathfrak C_2
=
\left\langle
G_{\mathrm{Cert}},
\mathsf{SCC}_C,
\mathcal A_C,
R_C,
\mathbf T_C,
\mathsf{CycleCert}
\right\rangle
}
$$

---

## 8.2 長期本體邊界系統

$$
\boxed{
\mathfrak B_L
=
\left\langle
\mathbf B,
\mathbf D_B,
\mathcal K_B,
\operatorname{Hyst}_B,
\mathcal S_\eta,
\Theta_B
\right\rangle
}
$$

---

## 8.3 偏誤感知語義近似

$$
\boxed{
\mathfrak E_B
=
\left\langle
\mathcal O_E,
\mathbf E_{\mathcal O_E},
\mathcal A_E,
\mathcal F_{\mathrm{critical}},
\mathsf{BiasReport}
\right\rangle
}
$$

---

## 8.4 非補償合法性系統

$$
\boxed{
\mathfrak L
=
\left\langle
\mathbf L,
\mathcal N_L,
\Theta_L,
G_L,
\operatorname{Pareto}_L,
D_L
\right\rangle
}
$$

---

## 8.5 去僭越身份治理

$$
\boxed{
\mathfrak I_{\mathrm{deusurp}}
=
\left\langle
\mathsf{IFL},
\mathbf c_I^{\mathrm{cf}},
\mathcal W_I,
\operatorname{ScopeFirewall},
\mathcal A_I,
\operatorname{Rectifiable},
\operatorname{Restore}_I
\right\rangle
}
$$

---

# 9. 本批次新形成的穩定區

## 9.1 證書循環不自動增加可信度

$$
\operatorname{CitationLoop}
\not\Rightarrow
\operatorname{EvidenceGain}
$$

---

## 9.2 本體邊界不具全域傳遞性

$$
O_0\sim_B O_1
\land
O_1\sim_B O_2
\not\Rightarrow
O_0\sim_B O_2
$$

但可以建立局部有界傳遞區。

---

## 9.3 語義近似始終相對於觀測架構

$$
\mathbf E
\rightarrow
\mathbf E_{\mathcal O_E}
$$

---

## 9.4 合法性底線不可被總分洗掉

$$
L_j<\theta_j
$$

對不可補償維度而言，其他高分不能自動抵銷。

---

## 9.5 制度身份需要反回饋審計

制度構成身份是可能的，但自證循環必須可被識別、申訴與修正。

---

# 10. 仍未解決的高張力問題

## 10.1 外部錨點本身也可能有偏誤

世界觀測、實驗與原始記錄並不天然中立。

---

## 10.2 邊界門檻仍需案例校準

自適應門檻雖比固定值合理，但仍需要領域案例與反例庫。

---

## 10.3 對抗性維度搜尋可能無限擴張

不斷尋找新差異，可能使任何兩個本體都永遠無法被視為近似。

---

## 10.4 不可補償底線之間可能衝突

例如隱私底線與完全透明底線可能直接衝突。

---

## 10.5 反事實身份基線可能不可觀測

制度干預已經發生後，無制度世界通常只能模型估計。

---

# 11. 更新後的研究佇列

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 外部錨點的可信度與觀測者依賴 | 證書網路仍需世界接口 |
| 2 | 邊界案例庫與門檻校準方法 | 將邊界理論推向可測試 |
| 3 | 對抗性維度搜尋的停止條件 | 防止近似分析無限展開 |
| 4 | 不可補償底線之間的衝突解法 | 合法性層仍可能死鎖 |
| 5 | 身份反事實基線的估計與不確定性 | 去僭越審計的核心 |
| 6 | 四值、機率、模糊與證書狀態統合 | 模型判定層需要收斂 |
| 7 | 證書、邊界與治理的複雜度分析 | 準備演算法原型 |
| 8 | 來源歷史是否升格為第五核心原始項 | 理論核心可能再次改寫 |

---

# 12. 圖更新摘要

## 12.1 新增節點

本批次新增：

$$
10+9+10+10+10=49
$$

個子節點。

---

## 12.2 新增主要關係

```text
forms_certificate_cycle
belongs_to_certificate_scc
anchors_certificate
shares_source_with
does_not_increase_evidence
accumulates_boundary_drift
crosses_critical_break
has_boundary_hysteresis
is_observation_relative
reveals_dimension_blind_spot
captures_observation_framework
violates_noncompensable_threshold
creates_legitimacy_debt
locks_identity_feedback
requires_counterfactual_identity_baseline
supports_identity_rectification
restores_identity_record
```

---

## 12.3 圖版本更新

輸入：

$$
\mathcal G_{\mathrm{FMO}}^{(4)}
$$

輸出：

$$
\boxed{
\mathcal G_{\mathrm{FMO}}^{(5)}
}
$$

---

# 13. 本批次結論

第五批次處理了理論進入自我驗證與治理階段後最危險的問題：

> 驗證機制本身可能形成封閉結構，並開始替自己製造證據。

第一，證書依賴圖被升級為證書網路。理論正式引入：

$$
\boxed{
\text{循環不增益原則}
}
$$

互相引用不構成新增證據，除非有外部錨點、獨立方法或新反例檢驗。

第二，本體邊界不再以單一累積距離或固定門檻判定，而改為：

$$
\boxed{
\operatorname{BStatus}
=
\left\langle
\mathbf B,
\mathbf D_B,
\mathcal K_B,
\operatorname{Hyst}_B,
\mathcal S_\eta
\right\rangle
}
$$

同時處理多尺度漂移、關鍵斷點、歷史滯後與路徑分段。

第三，語義近似被明確改為觀測架構相對：

$$
\boxed{
\mathbf E_{\mathcal O_E}(P_1,P_2)
}
$$

並要求維度來源、盲區搜尋、受影響者維度、權力捕獲風險與偏誤報告。

第四，合法性不再容許以總分掩蓋底線破壞。判定改為：

$$
\forall j\in\mathcal N_L,
\quad
L_j\geq\theta_j
$$

通過不可補償底線後，才進入 Pareto 比較。

第五，制度身份回饋加入去僭越機制。身份治理必須提供：

- 反事實基線；
- 多來源見證；
- 作用域防火牆；
- 可更正記錄；
- 獨立申訴；
- 恢復機制；
- 不可逆損失標記。

因此，本批次形成新的總體警戒原則：

$$
\boxed{
\text{任何可修改其自身證據來源的判定系統，}
\newline
\text{都必須接受反身封閉審查。}
}
$$

可修改證據來源的制度、模型或證書網路，不能僅憑其內部一致性證明自身正確。

它必須持續保留：

- 外部錨點；
- 獨立反例；
- 觀測盲區；
- 歷史版本；
- 權力來源；
- 受影響者異議；
- 可撤銷與恢復路徑。

至此，事實模態本體論已不只描述：

- 什麼是事實；
- 什麼是反事實；
- 什麼是可能；
- 什麼是本體邊界；
- 什麼是身份延續。

它也開始處理：

> 一套事實與本體判定系統，如何避免透過證書、制度與記錄控制，將自身封閉成不可反駁的現實製造機器。

---

## 附錄 A：第五批次最小 JSON

```json
{
  "batch": "FMO-MRASG-005",
  "input_graph": "G_FMO_4",
  "output_graph": "G_FMO_5",
  "selected_nodes": [
    "FMO-218",
    "FMO-219",
    "FMO-220",
    "FMO-221",
    "FMO-222"
  ],
  "decisions": [
    {
      "node": "FMO-218",
      "result": "noninflationary_anchored_certificate_network"
    },
    {
      "node": "FMO-219",
      "result": "multiscale_path_sensitive_boundary_drift_model"
    },
    {
      "node": "FMO-220",
      "result": "observation_relative_bias_audited_semantic_approximation"
    },
    {
      "node": "FMO-221",
      "result": "noncompensatory_legitimacy_with_pareto_comparison"
    },
    {
      "node": "FMO-222",
      "result": "counterfactual_scope_limited_identity_deusurpation"
    }
  ],
  "next_queue": [
    "external_anchor_reliability",
    "boundary_case_calibration",
    "adversarial_dimension_stopping",
    "noncompensable_threshold_conflicts",
    "identity_counterfactual_estimation"
  ]
}
```

---

## 附錄 B：版本狀態

**批次狀態：** 已完成  
**理論狀態：** 反身封閉風險與去封閉機制已建立  
**圖版本：** $\mathcal G_{\mathrm{FMO}}^{(5)}$  
**下一階段：** 外部世界錨定、門檻校準、停止條件、底線衝突與反事實估計  
