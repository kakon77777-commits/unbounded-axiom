# 二十四計算範式 × PCMT × GIPE 映射論 v0.1
## ——從計算形態座標到相位機器路由與認識堆疊

**Mapping the Twenty-Fourfold Computational Paradigms to PCMT and GIPE v0.1: From Morphological Coordinates to Phase-Machine Routing and Epistemic Stacks**

**作者：Neo.K × GPT-5.6 Thinking**  
**機構：EveMissLab / 一言諾科技有限公司**  
**版本：v0.1**  
**日期：2026-07-26**  
**文件類型：理論論文／計算分類學／相位計算機理論／GIPE 架構整合**

---

## 摘要

「計算的二十四重範式」以三個軸描述一個已指定語境的計算事件：

$$
\mathfrak P_{24}
=
\mathfrak B_2
\times
\mathfrak U_4
\times
\mathfrak O_3
$$

其中，底空間分為連續與離散，更新組織分為序列、跳躍、並行與識別，觀察模式分為連續、離散與拒單測。二十四重範式因此回答：

1. 計算在哪一類底空間中發生；
2. 更新如何被組織；
3. 結果如何被觀察。

相位計算機理論（Phase Computation Machine Theory, PCMT）則回答另一組問題：

1. 被計算的相位本體是什麼；
2. 相位如何表示與演化；
3. 哪一類相位機器能夠處理；
4. AI 應如何選擇、組合與切換機器。

全域欲相位認識論（GIPE）又回答更高層的問題：

1. 智能體為什麼需要進行這項計算；
2. 計算位於欲、世界模型、假設、證據、行動、資源或 Agent 治理的哪一層；
3. 計算結果如何成為下一個認識行動。

本文提出三者的正式映射關係，並強調：

$$
\boxed{
\text{二十四範式}
\neq
\text{PCMT}
\neq
\text{GIPE}
}
$$

三者分別屬於：

$$
\boxed{
\text{計算形態}
\quad
\text{計算機理}
\quad
\text{認識編排}
}
$$

因此，PCMT 不應被直接乘入二十四範式成為新的有限軸；GIPE 的七層 Phase Stack 也不應被乘成一百六十八格。相位機器可同時支援多個二十四範式，一個二十四範式也可由多種相位機器實作；GIPE 的單次研究任務更可能形成範式路徑與多機器堆疊，而非固定落入單一格。

本文建立三種映射：

1. **軸級映射**：二十四範式三軸與 PCMT 能力維度的關係；
2. **格級映射**：P1 至 P24 的預設相位機器配置與 GIPE 用途；
3. **路徑級映射**：GIPE 如何在研究過程中穿越多個範式與機器。

本文最後將二十四範式、PCMT、GIPE 與七十二格候選空間放入同一層級結構：

$$
\boxed{
\text{24 形態}
+
\text{3 轉移律}
+
\text{PCMT 機理註記}
+
\text{GIPE 任務編排}
}
$$

這使七十二格仍保持為計算動力學候選空間，而 PCMT 與 GIPE 成為每一格之上的實現與用途描述層。

---

## 關鍵詞

二十四重範式、PCMT、GIPE、相位機器、計算形態學、計算動力學、相位路由、拒單測、七十二格、計算分類

---

# 一、三套理論的層級分工

## 1.1 二十四範式：形態座標

對計算事件：

$$
\mathcal E=(X,U,O;\Gamma)
$$

二十四範式給出：

$$
p_{24,\Gamma}(\mathcal E)
=
\langle B;U;O\rangle
$$

其中：

$$
B\in\{\mathsf C,\mathsf D\}
$$

$$
U\in\{\mathsf S,\mathsf J,\mathsf P,\mathsf R\}
$$

$$
O\in\{\mathsf C,\mathsf D,\mathsf X\}
$$

它描述的是計算事件的外顯形態。

---

## 1.2 PCMT：相位機理座標

PCMT 對相位計算實例給出：

$$
\mathcal P
=
(
O_\phi,
R_\phi,
A_\phi,
D_\phi,
C_\phi,
M_\phi,
Y_\phi
)
$$

其中：

- $O_\phi$ ：相位本體；
- $R_\phi$ ：表示；
- $A_\phi$ ：承載架構；
- $D_\phi$ ：演化機制；
- $C_\phi$ ：耦合；
- $M_\phi$ ：記憶；
- $Y_\phi$ ：輸出。

它描述的是相位如何被合法計算。

---

## 1.3 GIPE：認識編排座標

GIPE Phase Stack 為：

$$
\Phi_t^{GIPE}
=
(
\Phi^W_t,
\Phi^G_t,
\Phi^H_t,
\Phi^E_t,
\Phi^A_t,
\Phi^R_t,
\Phi^{agent}_t
)
$$

分別表示：

- 欲；
- 世界模型；
- 假設；
- 證據；
- 行動；
- 資源與風險；
- 多 Agent 與治理。

它描述的是計算為何發生、作用於何種認識狀態，以及結果如何進入下一步。

---

## 1.4 三層總結

| 理論 | 核心問題 | 輸出 |
|---|---|---|
| 二十四範式 | 計算事件呈現何種形態？ | 三軸代碼 |
| PCMT | 這種相位應由何種機理與機器處理？ | 機器配置與選擇證書 |
| GIPE | 為何計算、作用於哪一層、下一步做什麼？ | 認識行動與跨層更新 |

---

# 二、為何不能直接相乘

## 2.1 PCMT 不是單一互斥軸

PCMT 的八類相位機器不是互斥的基本值：

```text
PhaseSimulationMachine
PhaseGraphMachine
PhaseStreamMachine
PhaseEventMachine
PhaseOscillationMachine
PhaseTopologyMachine
PhaseProofMachine
MetaPhaseMachine
```

同一任務可以同時使用：

```text
Graph + Event + Proof
```

因此不能簡單寫成：

$$
24\times8=192
$$

因為這會錯誤假設每一事件只能選擇一台機器。

---

## 2.2 GIPE 層不是計算事件的獨立軸

同一計算事件可能同時更新：

- 世界模型；
- 假設；
- 證據；
- 行動；
- 資源。

因此不能簡單寫成：

$$
24\times7=168
$$

GIPE 的七層是耦合堆疊，不是互斥分類。

---

## 2.3 正確關係是多值映射

定義 PCMT 映射：

$$
\mu_\Gamma:
\mathfrak P_{24}
\times
\Sigma_\tau
\rightarrow
2^{\mathcal R_M}
$$

其中：

- $\Sigma_\tau$ ：任務簽名；
- $\mathcal R_M$ ：相位機器登錄庫；
- $2^{\mathcal R_M}$ ：機器集合。

定義 GIPE 映射：

$$
\lambda:
\mathfrak P_{24}
\times
L_{GIPE}
\rightarrow
\Pi_M
$$

其中 $\Pi_M$ 為具體機器執行計畫。

---

# 三、二十四範式三軸與 PCMT 的軸級映射

## 3.1 底空間軸

### 連續底空間 $\mathsf C$

通常偏向：

- PhaseSimulationMachine；
- PhaseStreamMachine；
- PhaseOscillationMachine；
- PhaseTopologyMachine。

常見表示：

- 實數向量；
- 場；
- 流形；
- 連續時間訊號；
- 微分方程。

但連續底空間不等於非馮諾依曼，也不等於物理相位。

### 離散底空間 $\mathsf D$

通常偏向：

- PhaseGraphMachine；
- PhaseEventMachine；
- PhaseProofMachine；
- MetaPhaseMachine。

常見表示：

- 符號；
- 節點；
- 事件；
- 類型；
- 證書；
- 離散狀態機。

但離散底空間也可以由量子、神經形態或光學硬體承載。

---

## 3.2 更新軸

### 序列更新 $\mathsf S$

最自然對應：

- Simulation；
- Stream；
- Event chain；
- Proof chain。

主要能力：

- 路徑保存；
- 遞進；
- 時間順序；
- 逐步驗證。

### 跳躍更新 $\mathsf J$

最自然對應：

- Event；
- Graph selective update；
- Meta routing；
- Selective simulation。

主要能力：

- 局部展開；
- 稀疏更新；
- 查詢；
- 探測；
- 分支選擇。

### 並行更新 $\mathsf P$

最自然對應：

- Graph message passing；
- Parallel simulation；
- Oscillation；
- Multi-Agent event system。

主要能力：

- 多節點共同演化；
- 同步或異步耦合；
- 分散式更新。

### 識別更新 $\mathsf R$

最自然對應：

- Registry retrieval；
- Graph matching；
- Cached model；
- Proof certificate lookup；
- Meta selector。

主要能力：

- 預計算後存取；
- 模式匹配；
- 編譯結果調用；
- 模型識別。

識別不等於沒有計算，而是主要計算成本已轉移至前處理、訓練或建索引。

---

## 3.3 觀察軸

### 連續觀察 $\mathsf C$

常見輸出：

- 連續值；
- 分布；
- 場；
- 曲線；
- 信號；
- 連續信念剖面。

常用機器：

- Simulation；
- Stream；
- Oscillation。

### 離散觀察 $\mathsf D$

常見輸出：

- 類別；
- 符號；
- 事件；
- 行動；
- 證書；
- 判定。

常用機器：

- Event；
- Graph；
- Proof。

### 拒單測觀察 $\mathsf X$

$\mathsf X$ 不對應某一台單獨機器。

它要求：

- 多尺度輸出；
- 型別化整合；
- 衝突保存；
- 多不變量剖面；
- 來源與轉換記錄。

常見配置：

```text
Graph + Stream + Topology + Typed Integrator
```

因此， $\mathsf X$ 更接近 Stack 級觀察契約。

---

# 四、二十四格的 PCMT × GIPE 映射矩陣

以下矩陣給出預設映射，不主張唯一性。實際配置仍由任務簽名與元相位選擇器決定。

## 4.1 序列更新組

| 編號 | 代碼 | 預設 PCMT 配置 | GIPE 典型用途 |
|---|---|---|---|
| P1 | C-S-C | Simulation + Stream | 連續模擬、長期信號、資源趨勢 |
| P2 | C-S-D | Simulation + Event + Proof | 連續測量轉離散證據或判定 |
| P3 | C-S-X | Stream + Topology + Graph | 多尺度長期觀測、不能壓成單分數 |
| P4 | D-S-C | Stream + Simulation + Converter | 離散證據序列重構連續趨勢 |
| P5 | D-S-D | Event + Graph + Proof | 工作流、逐步推理、行動生命週期 |
| P6 | D-S-X | Graph + Stream + Typed Integrator | 多維證據累積、歷史與尺度並存 |

## 4.2 跳躍更新組

| 編號 | 代碼 | 預設 PCMT 配置 | GIPE 典型用途 |
|---|---|---|---|
| P7 | C-J-C | Event + Selective Simulation | 自適應探測、局部連續更新 |
| P8 | C-J-D | Event + Simulation + Proof | 選擇性測量後形成離散證據 |
| P9 | C-J-X | Event + Topology + Graph | 局部探測但需多尺度整合 |
| P10 | D-J-C | Graph + Simulation + Converter | 稀疏證據重構連續估計 |
| P11 | D-J-D | Event + Graph + Meta | 搜尋、爬蟲、工具調用、稀疏圖走訪 |
| P12 | D-J-X | Event + Graph + Typed Integrator | 選擇性反證與多不變量證據 |

## 4.3 並行更新組

| 編號 | 代碼 | 預設 PCMT 配置 | GIPE 典型用途 |
|---|---|---|---|
| P13 | C-P-C | Oscillation + Simulation + Stream | 連續耦合、平行場與物理模擬 |
| P14 | C-P-D | Simulation + Oscillation + Event | 多連續過程形成離散決策 |
| P15 | C-P-X | Oscillation + Topology + Graph | 多場、多尺度與臨界系統 |
| P16 | D-P-C | Graph + Parallel Simulation | 離散節點並行更新後形成連續剖面 |
| P17 | D-P-D | Graph + Event + Multi-Agent | 多 Agent、並行圖更新、離散共識 |
| P18 | D-P-X | Graph + Event + Topology + Integrator | 多 Agent 衝突、異質輸出與拒單測 |

## 4.4 識別更新組

| 編號 | 代碼 | 預設 PCMT 配置 | GIPE 典型用途 |
|---|---|---|---|
| P19 | C-R-C | Surrogate Simulation + Registry + Stream | 已訓練連續模型的快速連續輸出 |
| P20 | C-R-D | Registry + Graph + Event | 連續表徵的分類與離散識別 |
| P21 | C-R-X | Meta + Graph + Topology + Integrator | 連續潛在空間的多尺度泛化分析 |
| P22 | D-R-C | Graph Retrieval + Converter + Stream | 離散記憶檢索形成連續估計或生成 |
| P23 | D-R-D | Registry + Graph + Proof + Meta | 索引、證書、查表、精確離散存取 |
| P24 | D-R-X | Graph + Meta + Multi-Resolution Integrator | 離散知識庫的多尺度與時間性輸出 |

---

# 五、二十四格與 GIPE 七層的分布

## 5.1 欲相位層

常見範式：

- P5：逐步目標與約束更新；
- P11：選擇性目標分解；
- P17：多目標並行評估；
- P23：已編譯規則與權限存取；
- P24：無法由單一效用函數壓縮的多價值欲結構。

---

## 5.2 世界模型層

常見範式：

- P4、P10：離散觀測重構連續世界；
- P6、P12：多尺度結構；
- P16、P17、P18：並行圖更新；
- P22、P23、P24：記憶與檢索。

---

## 5.3 假設層

常見範式：

- P5：逐步推導；
- P8、P11、P12：選擇性假設檢驗；
- P16、P17、P18：多假設並行競爭；
- P19 至 P24：模型識別與已學習模式。

---

## 5.4 證據層

常見範式：

- P2：連續觀測離散化；
- P3：連續多尺度證據；
- P6：離散多不變量證據；
- P8、P12：選擇性測量與反證；
- P18：多來源並行衝突；
- P23：證書與索引；
- P24：多尺度證據存取。

---

## 5.5 行動層

常見範式：

- P5：序列行動；
- P7、P8、P11：選擇性行動；
- P14、P17：並行行動；
- P20、P23：已識別策略的快速執行。

---

## 5.6 資源與風險層

常見範式：

- P1：連續資源演化；
- P2：閾值觸發；
- P7：局部資源調整；
- P13、P16：平行資源更新；
- P19、P23：預編譯風險規則。

---

## 5.7 多 Agent 與治理層

常見範式：

- P11：選擇性委派；
- P17：離散並行 Agent；
- P18：多 Agent 異質衝突；
- P23：權限與證書；
- P24：多價值、多時間尺度的治理。


---

# 六、範式不直接決定相位本體

## 6.1 同一範式可承載不同相位本體

例如 P17：

$$
\langle
\mathsf D;
\mathsf P;
\mathsf D
\rangle
$$

可以是：

- 離散物理振盪器的同步標記；
- 多 Agent 的並行行動；
- 圖神經網路節點更新；
- 平行形式證明；
- 多假設競爭。

因此：

$$
p_{24}
\not\Rightarrow
O_\phi
$$

二十四範式不能單獨判定相位本體。

---

## 6.2 同一相位本體可落入多個範式

認識相位可以出現在：

- P5：逐步推理；
- P11：選擇性查證；
- P17：並行假設；
- P23：已編譯證書查詢；
- P24：多尺度認識輸出。

因此：

$$
O_\phi
\not\Rightarrow
p_{24}
$$

相位本體也不能單獨決定形態代碼。

---

## 6.3 映射必須依賴語境

完整映射應寫成：

$$
\mu_\Gamma
(
p_{24},
O_\phi,
\Sigma_\tau
)
=
\Pi_M
$$

其中語境 $\Gamma$ 至少包含：

- 解析度；
- 時間窗；
- 觀察量；
- 容許誤差；
- 可用表示；
- 可用硬體；
- 權限；
- 預算。

---

# 七、拒單測 $\mathsf X$ 與 PCMT 的特殊關係

## 7.1 $\mathsf X$ 不是不可計算

$\mathsf X$ 表示：

> 在指定語境與容許表示類中，沒有一個單一表示能保留全部相關不變量。

因此， $\mathsf X$ 不應路由到「無法處理」。

它應路由到：

- 多機器；
- 多尺度；
- 多型別；
- 多輸出；
- 衝突保存；
- 轉換揭露。

---

## 7.2 $\mathsf X$ 的標準 PCMT 契約

```yaml
observation_contract:
  mode: single_measure_refusal
  required:
    - multi_resolution_output
    - typed_invariants
    - provenance_preservation
    - conflict_preservation
    - no_forced_scalarization
```

---

## 7.3 $\mathsf X$ 與 GIPE

GIPE 中以下情況常屬於 $\mathsf X$ ：

- 假設同時有支持與反證；
- 多個證據尺度互不取代；
- 風險、效用與權利不能壓成單一分數；
- 多 Agent 存在真實認識分化；
- 長期研究的不同時間尺度給出不同結論。

因此，GIPE 不應把所有相位壓縮成：

```text
confidence = 0.82
```

---

# 八、範式路徑與 GIPE 研究循環

## 8.1 GIPE 通常不是單格計算

一個研究任務可以形成：

$$
\mathbf p_\tau
=
(
p_0,
p_1,
\ldots,
p_T
)
$$

例如：

```text
P11 搜尋候選
→ P23 讀取索引與既有證書
→ P12 選擇性反證
→ P17 多 Agent 並行分析
→ P8 精密測量形成離散結果
→ P6 累積多尺度證據
→ P5 逐步形成行動判定
```

---

## 8.2 範式路徑與機器路徑

同時存在：

$$
\mathbf M_\tau
=
(
M_0,
M_1,
\ldots,
M_T
)
$$

例如：

```text
Graph Machine
→ Registry
→ Event Machine
→ Multi-Agent Graph
→ Simulation / Measurement
→ Typed Integrator
→ Proof Guard
```

---

## 8.3 雙路徑表示

GIPE 的一次研究可記為：

$$
\mathcal R_\tau
=
(
\mathbf p_\tau,
\mathbf M_\tau,
\mathbf \Phi_\tau
)
$$

其中：

- $\mathbf p_\tau$ ：形態路徑；
- $\mathbf M_\tau$ ：機器路徑；
- $\mathbf \Phi_\tau$ ：GIPE 相位堆疊路徑。

---

# 九、永光石世界的完整映射

## 9.1 問題分解

任務：

> 判定永光石是否存在；若不存在，建立可持續五分鐘以上的非魔法發光材料。

---

## 9.2 第一階段：搜尋傳聞

形態：

$$
P11
=
\langle
\mathsf D;
\mathsf J;
\mathsf D
\rangle
$$

PCMT：

- PhaseGraphMachine；
- PhaseEventMachine；
- MetaPhaseSelector。

GIPE：

- 世界模型；
- 證據；
- 行動。

---

## 9.3 第二階段：讀取既有材料記錄

形態：

$$
P23
=
\langle
\mathsf D;
\mathsf R;
\mathsf D
\rangle
$$

PCMT：

- Registry；
- Graph；
- Proof。

GIPE：

- 證據來源；
- 假設初始化。

---

## 9.4 第三階段：跨地區選擇性觀測

若觀測連續濕度後輸出是否發光：

$$
P8
=
\langle
\mathsf C;
\mathsf J;
\mathsf D
\rangle
$$

PCMT：

- Selective Simulation / Measurement；
- Event；
- Proof of observation provenance。

GIPE：

- 證據；
- 假設；
- 資源。

---

## 9.5 第四階段：多 Agent 並行假設

$$
P17
=
\langle
\mathsf D;
\mathsf P;
\mathsf D
\rangle
$$

PCMT：

- Graph；
- Event；
- Multi-Agent；
- Proof Guard。

GIPE：

- 假設競爭；
- Agent 治理；
- 行動候選。

---

## 9.6 第五階段：多尺度證據整合

濕度、材料、加熱、冷壓與持續時間不能由單一分數完整表示：

$$
P6
\text{ 或 }
P18
$$

PCMT：

- Graph；
- Stream；
- Typed Integrator；
- Topology。

GIPE：

- 證據相位；
- 世界模型相位；
- 長期觀測。

---

## 9.7 第六階段：不可逆實驗前治理

行動以離散序列執行：

$$
P5
=
\langle
\mathsf D;
\mathsf S;
\mathsf D
\rangle
$$

PCMT：

- Event；
- Proof；
- Audit log。

GIPE：

- 行動；
- 風險；
- 權限；
- 責任閉合。

---

# 十、從範式代碼生成相位任務簽名

## 10.1 自動轉換原則

二十四範式代碼不能產生完整任務簽名，但可以提供預設值。

例如：

```text
C-S-X
```

可產生：

```yaml
defaults:
  substrate: continuous
  update: sequential
  observation: multi_measure
  likely_memory:
    - path_required
  likely_machines:
    - phase_stream_machine
    - phase_topology_machine
    - phase_graph_machine
  warnings:
    - scalar_output_forbidden_without_loss_declaration
```

---

## 10.2 P17 範例

```yaml
paradigm:
  id: P17
  code: D-P-D

phase_task_defaults:
  representation:
    - discrete_graph
    - event_state
  dynamics:
    - parallel_update
  output:
    - discrete
  likely_machines:
    - phase_graph_machine
    - phase_event_machine
  possible_gipe_layers:
    - hypothesis
    - action
    - multi_agent_governance
```

---

## 10.3 P24 範例

```yaml
paradigm:
  id: P24
  code: D-R-X

phase_task_defaults:
  representation:
    - discrete_registry
    - multi_resolution_profile
  dynamics:
    - recognition
  observation:
    - single_measure_refusal
  likely_machines:
    - phase_graph_machine
    - meta_phase_machine
    - typed_integrator
  warnings:
    - retrieval_result_must_not_be_scalarized
```

---

# 十一、PCMT 能力登錄中的二十四範式欄位

每台相位機器可增加：

```yaml
twenty_fourfold_support:
  full:
    - P5
    - P11
    - P17
    - P23
  partial:
    - P6
    - P12
    - P18
    - P24
  unsupported:
    - P13
    - P14
    - P15
  conditions:
    P18:
      - typed_multi_output_required
      - conflict_preservation_required
```

---

## 11.1 支援不等於唯一適用

若機器聲明支援 P17，只表示它能處理：

- 離散底空間；
- 並行更新；
- 離散輸出。

不表示它能處理所有 P17 任務。

仍須檢查：

- 相位本體；
- 驗證；
- 記憶；
- 權限；
- 轉移律；
- 硬體。

---

## 11.2 部分支援

一台向量機器可能支援 P18 的並行離散更新，但無法保留拒單測輸出。

此時只能標記：

```text
partial
```

---

# 十二、元相位選擇器的範式感知

## 12.1 MPS 新增輸入

元相位選擇器輸入增加：

```yaml
morphology:
  paradigm_id:
  substrate:
  update_mode:
  observation_mode:
  context:
```

---

## 12.2 硬條件

若觀察軸為 $\mathsf X$ ，則必須要求：

- 多輸出；
- 來源保存；
- 禁止未揭露的單值壓縮。

若更新軸為 $\mathsf P$ ，則必須檢查：

- 同步；
- 通信；
- 獨立度；
- race condition；
- Agent 協調。

若更新軸為 $\mathsf R$ ，則必須檢查：

- 前處理來源；
- 模型或索引版本；
- 更新成本；
- 過時風險。

---

## 12.3 形態感知評分

可加入：

$$
S_{morph}
(
M,p_{24}
)
$$

總評分為：

$$
S^\ast(M)
=
S_{type}
+
S_{morph}
+
S_{verify}
+
S_{resource}
-
S_{risk}
$$

但本體與治理硬條件仍不得被總分抵銷。

---

# 十三、與七十二格的正確對接

## 13.1 七十二格增加的是轉移律

七十二格候選空間為：

$$
\mathfrak P_{72}^{(0.1)}
=
\mathfrak P_{24}
\times
\mathfrak L_3
$$

其中：

$$
\mathfrak L_3
=
\{
\mathsf F,
\mathsf K,
\mathsf Q
\}
$$

分別是：

- 函數型／確定型；
- 核型／機率—熱力型；
- 相干型／量子通道型。

---

## 13.2 PCMT 是每格的機理註記

對任一七十二格：

$$
g_{72}
=
\langle
B;U;O;L
\rangle
$$

PCMT 再附加：

$$
\eta(g_{72})
=
(
O_\phi,
R_\phi,
M_\phi,
A_\phi,
V_\phi
)
$$

因此 PCMT 不增加格數，而增加每格的實現解析度。

---

## 13.3 GIPE 是每格的任務位置

再附加：

$$
\zeta(g_{72})
=
(
L_{GIPE},
Goal,
Permission,
Risk,
History
)
$$

因此最完整描述為：

$$
\boxed{
\mathcal C
=
(
B,
U,
O,
L;
O_\phi,
R_\phi,
M_\phi,
A_\phi;
L_{GIPE},
\Gamma
)
}
$$

---

## 13.4 為何這樣更穩定

這避免把以下不同概念混成無限乘法：

- 形態；
- 轉移律；
- 相位本體；
- 機器；
- 硬體；
- 認識層；
- 資源；
- 權限。

只有真正互斥且相對獨立的基本值才進入格點軸。

其他內容採：

- 型別；
- 註記；
- manifest；
- 路徑；
- 堆疊。

---

# 十四、形式命題

## 命題 1：非唯一機器映射

對任一範式 $p\in\mathfrak P_{24}$ ，一般不存在唯一相位機器 $M$ ，使：

$$
\mu(p)=M
$$

因為機器選擇仍依賴相位本體、任務、資源與治理。

---

## 命題 2：範式—本體正交候選

二十四範式描述形態，相位本體描述被計算的關係狀態；兩者不存在一般的一對一關係。

---

## 命題 3： $\mathsf X$ 堆疊需求

若一個事件被分類為 $\mathsf X$ ，且其拒單測判定有效，則任何宣稱完整處理該事件的機器配置，必須保留多個相關不變量，或明示其壓縮損失。

---

## 命題 4：GIPE 路徑命題

一個非平凡 GIPE 研究任務通常應表示為範式路徑而非單一範式。

---

## 命題 5：七十二格分層命題

七十二格描述形態與轉移律；PCMT 與 GIPE 應作為格點註記與執行編排，而非未證明獨立性的乘法軸。

---

# 十五、工程資料格式

## 15.1 Unified Computation Descriptor

```yaml
computation_event:
  event_id:

  morphology:
    paradigm_id:
    substrate:
    update_mode:
    observation_mode:
    context_ref:

  dynamics:
    transition_law:
    reversibility:
    interaction_mode:

  phase:
    ontology:
    representation:
    difference:
    memory:

  machine_plan:
    machines:
    converters:
    order:
    switch_conditions:

  gipe:
    layers:
    goal_ref:
    evidence_refs:
    permissions:
    risk:
    history_ref:
```

---

## 15.2 範式路徑

```yaml
paradigm_path:
  - step: 1
    paradigm: P11
    machine: phase_graph_machine
    gipe_layer:
      - world_model
      - evidence

  - step: 2
    paradigm: P17
    machine:
      - phase_graph_machine
      - phase_event_machine
    gipe_layer:
      - hypothesis
      - multi_agent_governance

  - step: 3
    paradigm: P8
    machine:
      - phase_simulation_machine
      - proof_guard
    gipe_layer:
      - evidence
      - action
```

---

# 十六、實驗方案

## 16.1 基準組

比較：

### A. 無二十四範式標記

MPS 只依任務自然語言選擇機器。

### B. 只有二十四範式

使用形態標記，但沒有 PCMT 本體與能力登錄。

### C. 二十四範式 + PCMT

有形態、本體、機器能力與選擇器。

### D. 二十四範式 + PCMT + GIPE

加入七層認識堆疊、權限與責任閉合。

---

## 16.2 評分指標

- 機器選擇正確率；
- 本體錯配率；
- 形態錯配率；
- $\mathsf X$ 過度壓縮率；
- 任務成功率；
- 行動資訊增益；
- 來源保存率；
- 跨層更新正確率；
- 權限違反率；
- 協調成本；
- 範式標註一致性。

---

## 16.3 消融實驗

移除：

- 底空間軸；
- 更新軸；
- 觀察軸；
- 相位本體；
- 機器能力登錄；
- GIPE 層級；
- MPS。

觀察每一元件是否提供可重複增益。

---

# 十七、失敗模式

## 17.1 將二十四範式當成演算法選擇表

範式只提供形態先驗，不能單獨決定機器。

## 17.2 將 PCMT 當成新軸

相位機器可組合，不能簡單乘入。

## 17.3 將 GIPE 層當互斥分類

一次行動可同時作用多層。

## 17.4 代碼決定本體

P17 不等於 AgentPhase，P13 也不等於 PhysicalPhase。

## 17.5 $\mathsf X$ 神祕化

拒單測不是不可測，也不是自動更高級。

## 17.6 強制單格

混合 AI 系統被迫歸入一格，造成資訊丟失。

## 17.7 範式過度切換

每個微小操作都改代碼，造成無意義標註成本。

## 17.8 形態掩蓋轉移律

同一 P17 可能是確定、隨機或量子，不能忽略七十二格第四軸。

---

# 十八、可證偽條件

本映射理論在以下情況需要修訂：

1. 二十四範式標記無法改善相位機器選擇；
2. 軸級映射在不同研究者之間無法重複；
3. 大多數格都只能得到任意的 PCMT 配置；
4. GIPE 任務不需要範式路徑，單格已足夠；
5. $\mathsf X$ 不需要多尺度或多機器處理；
6. PCMT 能被證明是一個獨立、互斥、相對完備的有限軸，應正式乘入格點；
7. GIPE 七層能被證明是互斥的計算事件類型，而非耦合堆疊；
8. 加入形態標記後協調成本高於任何選擇增益。

---

# 十九、後續研究

## 19.1 自動範式標註器

輸入計算事件，輸出：

- 二十四範式代碼；
- 信心；
- 語境；
- 混合路徑；
- 爭議點。

## 19.2 PCMT Registry v0.2

為每台機器增加二十四範式支援欄。

## 19.3 MPS Morphology-Aware v0.2

讓元相位選擇器使用範式先驗。

## 19.4 GIPE-EW 基準

實測範式路徑是否改善永光石世界研究。

## 19.5 七十二格存在性矩陣

逐格分析：

- 理論存在；
- 工程可行；
- PCMT 配置；
- GIPE 用途；
- 空格與退化格。

---

# 二十、結論

二十四計算範式、PCMT 與 GIPE 並不是三套競爭理論。

它們分別回答：

$$
\boxed{
\text{計算呈現何種形態？}
}
$$

$$
\boxed{
\text{相位由何種機理與機器處理？}
}
$$

$$
\boxed{
\text{智能體為何計算，以及計算如何改變認識行動？}
}
$$

三者的正確關係為：

$$
\boxed{
\text{二十四形態座標}
\rightarrow
\text{PCMT 機器路由}
\rightarrow
\text{GIPE 認識編排}
}
$$

但這不是單向不可逆鏈。GIPE 的任務需求會反向決定 PCMT 機器，PCMT 的能力又會影響可實現的範式路徑。

因此完整閉環為：

$$
\boxed{
\text{GIPE 任務}
\rightarrow
\text{相位任務簽名}
\rightarrow
\text{二十四形態辨識}
\rightarrow
\text{PCMT 機器選擇}
\rightarrow
\text{執行與觀測}
\rightarrow
\text{GIPE 跨層更新}
}
$$

本文最重要的邊界是：

$$
\boxed{
\text{PCMT 不是二十四範式的新軸，GIPE 也不是新的乘數。}
}
$$

二十四範式保持為計算形態學；七十二格增加狀態轉移律；PCMT 描述每一形態—動力格的相位機理與實現；GIPE 則描述這些計算如何被智能體編排為認識行動。

由此得到下一階段的正式整合式：

$$
\boxed{
\text{24 形態}
\times
\text{3 動力律}
+
\text{PCMT 機理註記}
+
\text{GIPE 任務堆疊}
}
$$

下一篇應正式進入：

> **《七十二格計算動力學 × PCMT × GIPE 總整合 v0.1》**

並逐格建立：

- 存在性；
- 轉移律；
- 相位本體；
- 相位機器；
- GIPE 用途；
- 實現成熟度；
- 空格、退化格與混合路徑。

---

# 附錄 A：二十四格代碼

```text
P1  C-S-C
P2  C-S-D
P3  C-S-X
P4  D-S-C
P5  D-S-D
P6  D-S-X

P7  C-J-C
P8  C-J-D
P9  C-J-X
P10 D-J-C
P11 D-J-D
P12 D-J-X

P13 C-P-C
P14 C-P-D
P15 C-P-X
P16 D-P-C
P17 D-P-D
P18 D-P-X

P19 C-R-C
P20 C-R-D
P21 C-R-X
P22 D-R-C
P23 D-R-D
P24 D-R-X
```

---

# 附錄 B：三層定位

```text
Twenty-Fourfold:
  Morphology

PCMT:
  Phase Mechanism and Machine Routing

GIPE:
  Epistemic Purpose and Stack Orchestration
```

---

# 附錄 C：完整描述符

```text
Morphology
+ Transition Law
+ Phase Ontology
+ Machine Configuration
+ Hardware
+ GIPE Layer
+ Resource
+ Permission
+ History
```

---

# 附錄 D：下一階段

```text
24 Paradigms
→ 72 Dynamics Cells
→ PCMT Annotation
→ GIPE Use
→ Existence and Compatibility Matrix
```
