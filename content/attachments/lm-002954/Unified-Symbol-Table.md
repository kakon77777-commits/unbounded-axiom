# GPC-CS 統一符號表

**Series:** Generalized Phase Communication and Carrier Safety  
**Scope:** Papers 00–10  
**Version:** v1.0  
**Date:** 2026-08-14  
**Canonical source encoding:** UTF-8  
**Canonical mathematics delimiters:** `$...$` and `$$...$$` only

## 1. 使用原則

1. 本表以 **系列統一** 為目的，優先保留已在各篇論文中反覆出現且具有結構意義的符號。
2. 若同一字母在不同篇章中有不同用途，於「符號重載與建議修正」中明示。
3. 此表分為：狀態／安全、轉導、容量、算子、雙向耦合、恢復、連續性、共模與異質、網路與級聯、可觀測性與驗證。

## 2. 統一符號總表

| ID | 符號 | 名稱 | 類型 | 首次核心出現 | 說明 |
|---|---|---|---|---|---|
| S001 | $\mathcal X$ | 狀態空間 | Set | P00/P01 | 單載體可能狀態全集。 |
| S002 | $x$ | 單載體狀態 | Element | P00/P01 | 通常 $x\in\mathcal X$。 |
| S003 | $\mathcal X_i$ | 第 $i$ 個載體的狀態空間 | Set | P01 | 多載體時的局部狀態空間。 |
| S004 | $x_i$ | 第 $i$ 個載體狀態 | Element | P01 | 局部狀態。 |
| S005 | $\mathcal X_G$ | 全域聯合狀態空間 | Set | P01/P09 | $\prod_i \mathcal X_i$。 |
| S006 | $\mathbf X$ | 全域聯合狀態 | Vector | P01/P09 | $(x_1,\ldots,x_N)$。 |
| S007 | $\mathbf X_t$ | 時刻 $t$ 的全域聯合狀態 | Vector | P09 | 網路動力學主變數。 |
| S008 | $\mathcal S$ | 安全域 | Set | P00/P01 | 單載體安全狀態集合。 |
| S009 | $\mathcal S_i$ | 第 $i$ 個載體安全域 | Set | P01 | 局部安全集合。 |
| S010 | $\mathcal C_G$ | 全域關係約束集合 | Set | P01 | 相位、同步、延遲等關係安全約束。 |
| S011 | $\mathcal S_G^\star$ | 全域安全域 | Set | P01 | $(\prod_i\mathcal S_i)\cap\mathcal C_G$。 |
| S012 | $\mathcal Q_k$ | 至少 $k$ 個節點存活之 quorum 集 | Set | P08 | 群體韌性中的基礎集合。 |
| S013 | $\mathcal S_{G,k}^{\star}$ | relation-safe quorum 全域安全集 | Set | P08/P09 | 同時要求 quorum 與關係安全。 |
| S014 | $\mathcal K_O(\mathcal S)$ | 算子下最大前向不變安全核 | Set | P04 | 在 $O$ 下留在安全域中的最大子集。 |
| S015 | $\mathcal K_{G,k}$ | 全域網路安全核 | Set | P09 | 在全域更新下持續落在 $\mathcal S_{G,k}^{\star}$ 的核心。 |
| S016 | $E$ | 編碼映射 | Map | P02 | 將狀態或內容映為可傳輸表示。 |
| S017 | $T$ | 轉導映射 | Map | P02 | 跨載體轉導。 |
| S018 | $D$ | 解碼／重建映射 | Map | P02 | 接收端重建器。 |
| S019 | $z$ | 編碼結果 | Variable | P02 | 中介表示。 |
| S020 | $u$ | 轉導後中介量 | Variable | P02 | 傳輸後表示。 |
| S021 | $r$ | 重建結果 | Variable | P02 | 接收端重建輸出。 |
| S022 | $\Delta_{ij}$ | 跨載體錯配向量 | Vector | P02 | 幾何、解碼、功能、資訊、安全等錯配。 |
| S023 | $\delta_{\mathrm{geom}}$ | 幾何錯配 | Scalar | P02 | 表示空間幾何不一致。 |
| S024 | $\delta_{\mathrm{dec}}$ | 解碼錯配 | Scalar | P02 | 解碼過程不一致。 |
| S025 | $\delta_{\mathrm{func}}$ | 功能錯配 | Scalar | P02 | 功能表現不一致。 |
| S026 | $\delta_{\mathrm{info}}$ | 資訊錯配 | Scalar | P02 | 資訊損失或歧義。 |
| S027 | $\delta_{\mathrm{safe}}$ | 安全錯配 | Scalar | P02 | 安全性相關偏差。 |
| S028 | $\mathfrak C(x)$ | 容量可行域 | Set-valued map | P03 | 狀態 $x$ 下可承受資源／負載集合。 |
| S029 | $\mathfrak C_i(x_i)$ | 第 $i$ 節點容量可行域 | Set-valued map | P03/P08 | 局部容量。 |
| S030 | $q$ | 需求／負載向量 | Vector | P03 | 與容量域比對的工作需求。 |
| S031 | $M$ | 記憶長度／上下文長度 | Scalar | P03 | 有限記憶分析的核心變數。 |
| S032 | $R_{\mathrm{upd}}$ | 更新速率 | Scalar | P03 | Paper 03 的核心速率量。 |
| S033 | $O$ | 狀態更新算子 | Map | P04 | 單一更新步驟。 |
| S034 | $O_\alpha$ | 參數化狀態更新算子 | Map | P04 | 由模式／參數索引。 |
| S035 | $\mathfrak O$ | 算子族 | Family | P04 | 所有可用更新算子。 |
| S036 | $\sigma_t$ | 切換序列／模式索引 | Index | P04/P09 | 決定當前使用哪個算子。 |
| S037 | $\Phi_w$ | 歷史／字串 $w$ 作用後的合成更新 | Map | P06 | 對應路徑依賴。 |
| S038 | $\Gamma_{AB}$ | 雙載體耦合更新 | Map | P05 | 兩載體的聯合更新。 |
| S039 | $a_A,a_B$ | 自增益參數 | Scalars | P05 | 局部收縮或自影響。 |
| S040 | $\gamma_{AB},\gamma_{BA}$ | 交叉增益 | Scalars | P05 | 雙向影響強度。 |
| S041 | $\mathcal M_h$ | 廣義同步流形 | Set | P05 | $x_B=h(x_A)$ 型關係集合。 |
| S042 | $\mathcal L_R$ | 恢復／回復算子 | Map/Family | P06 | 恢復機制的抽象表示。 |
| S043 | $I(X;Y)$ | 互資訊 | Information quantity | P06 | 恢復與可識別性分析中使用。 |
| S044 | $R_{\mathrm{rec}}$ | 恢復異質成本 | Scalar | P08 | 不同恢復算子之分散度。 |
| S045 | $\Psi$ | 外部可觀測輪廓映射 | Map | P07 | 由內部狀態到可觀測 profile。 |
| S046 | $\mathbf C$ | 連續性向量 | Vector | P07 | $(C_{\mathrm{obs}},C_{\mathrm{info}},C_{\mathrm{func}},C_{\mathrm{lin}},C_{\mathrm{sub}})$。 |
| S047 | $C_{\mathrm{obs}}$ | 觀測連續性 | Scalar | P07 | 輸出輪廓是否維持。 |
| S048 | $C_{\mathrm{info}}$ | 資訊連續性 | Scalar | P07 | 資訊可恢復程度。 |
| S049 | $C_{\mathrm{func}}$ | 功能連續性 | Scalar | P07 | 功能是否維持。 |
| S050 | $C_{\mathrm{lin}}$ | 譜系／分支連續性 | Scalar | P07 | 是否可追溯到同一 lineage。 |
| S051 | $C_{\mathrm{sub}}$ | 主體相關連續性 | Scalar | P07 | 身份問題中的主體性維度。 |
| S052 | $B_\tau$ | 分支算子 | Operator | P07 | 產生支線連續體。 |
| S053 | $F_i$ | 第 $i$ 節點失效指示變數 | Bernoulli variable | P08 | 群體失效分析基本量。 |
| S054 | $K$ | 總失效數 | Random variable | P08 | $K=\sum_i F_i$。 |
| S055 | $\Sigma_F$ | 失效共變異矩陣 | Matrix | P08 | 二階失效依賴描述。 |
| S056 | $\rho$ | 等相關參數 | Scalar | P08 | 簡化模型中的 pairwise correlation。 |
| S057 | $\Omega_{ij}$ | 共享依賴重疊 | Scalar | P08 | dependency overlap 指標。 |
| S058 | $D_i$ | 第 $i$ 節點依賴集合 | Set | P08 | shared dependency 分析。 |
| S059 | $\mathcal H_D$ | 依賴超圖 | Hypergraph | P08 | 共享依賴結構。 |
| S060 | $\mathcal R_{\mathrm{het}}$ | 異質韌性向量 | Vector | P08 | 以多目標方式評估 heterogeneity。 |
| S061 | $H_{ij}$ | 結構異質度 | Scalar | P08 | 節點對之間的結構差異。 |
| S062 | $\bar H_t$ | 平均異質度 | Scalar | P08 | 時間 $t$ 的平均 pairwise heterogeneity。 |
| S063 | $\Gamma_G$ | 全域網路更新算子 | Map | P09 | 聯合網路狀態更新。 |
| S064 | $\mathbf d_t$ | 狀態差異向量 | Vector | P09 | 比較系統中的偏差向量。 |
| S065 | $d_i(\cdot,\cdot)$ | 局部距離 | Metric-like quantity | P09 | 定義第 $i$ 節點偏差。 |
| S066 | $G_t=[g_{ij,t}]$ | 增益矩陣 | Matrix | P09 | 局部差異如何一步傳播。 |
| S067 | $g_{ij}$ | 從 $j$ 到 $i$ 的一步增益 | Scalar | P09 | 有向靈敏度。 |
| S068 | $\mathcal T_G$ | 總網路敏感度矩陣 | Matrix | P09 | $(I-G)^{-1}$ 或 $\\sum_k G^k$。 |
| S069 | $A_H$ | 有限時域放大量 | Scalar | P09 | $\max_{0\le k\le H}\|G^k\|$。 |
| S070 | $S_t$ | 失效節點集合 | Set | P09 | 級聯動力學中的失效集合。 |
| S071 | $\mathcal C(S)$ | 級聯閉包映射 | Set map | P09 | 給定失效集合後的下一輪失效集合。 |
| S072 | $\Phi_G(t,s)$ | 時變增益轉移乘積 | Matrix | P09 | $G_{t-1}\cdots G_s$。 |
| S073 | $G(S_t)$ | 依賴失效集合的增益矩陣 | Matrix-valued map | P09 | 狀態—算子共演化。 |
| S074 | $G_{\mathrm{multi}}$ | 多層網路 block 增益矩陣 | Block matrix | P09 | interdependent network 抽象。 |
| S075 | $\mathcal B_\mu$ | 加權安全盒 | Set | P09 | $\{ \mathbf d: 0\preceq \mathbf d \preceq \mu \}$。 |
| S076 | $\mu$ | 安全裕度向量 | Vector | P09 | 建立全域安全管的 margin。 |
| S077 | $H$ | 觀測映射 | Map | P10 | $H:\mathcal X\to\mathcal Y$。 |
| S078 | $\mathcal F_H(y)$ | 觀測 fiber | Set | P10 | $H^{-1}(y)$。 |
| S079 | $\mathcal A_H^{\mathcal S}$ | 安全歧義輸出集 | Set | P10 | 同一觀測可對應安全與不安全內部狀態。 |
| S080 | $\mathcal O_T(x_0)$ | 長度 $T$ 的觀測窗 | Tuple/Map | P10 | 時間窗可觀測性。 |
| S081 | $\mathscr O_n$ | Kalman 觀測矩陣 | Matrix | P10 | 線性可觀測性判準。 |
| S082 | $V(M,\varphi)$ | 三值驗證器 | Map | P10 | $\{\mathrm{PROVED},\mathrm{REFUTED},\mathrm{UNKNOWN}\}$。 |
| S083 | $\widehat M$ | 被驗證模型 | Model | P10 | 形式驗證作用對象。 |
| S084 | $M^\star$ | 真實部署系統 | Model/System | P10 | runtime system。 |
| S085 | $\varepsilon_t$ | 模型—部署誤差上界 | Scalar | P10 | $d(x_t^\star,\hat x_t)$ 的上界。 |
| S086 | $h(x)$ | 安全 margin 函數 | Function | P10 | $\mathcal S=\{x:h(x)\ge 0\}$。 |
| S087 | $L_h$ | 安全 margin 函數的 Lipschitz 常數 | Scalar | P10 | 用於 robust transfer。 |
| S088 | $p_U$ | 零失敗測試的上置信界 | Scalar | P10 | $1-\delta^{1/n}$。 |
| S089 | $\mathfrak V$ | 驗證對象五元組 | Tuple | P10 | $(M,\varphi,K,H,A)$。 |
| S090 | $\mathfrak R_{\mathrm{claim}}$ | claim provenance 記錄 | Tuple | P10 | $(C,K,A,H,M,E,R)$。 |

## 3. 符號重載與建議修正

| 符號 | 重載情況 | 建議統一寫法 |
|---|---|---|
| $H$ | P08 的 $H_{ij}$ 為 heterogeneity；P10 的 $H$ 為 observation map。 | 保留 $H_{ij}$ 作 heterogeneity，將觀測映射統一寫成 $H_{\mathrm{obs}}$ 亦可。 |
| $h$ | P05 的同步流形寫成 $x_B=h(x_A)$；P10 的 $h$ 是 safety margin function。 | 建議同步映射寫成 $\eta$ 或 $h_{\mathrm{sync}}$，安全 margin 寫成 $h_{\mathrm{safe}}$。 |
| $G$ | P09 中同時有 topology graph 與 gain matrix 的語意風險。 | 建議 topology graph 固定寫成 $\mathcal G_t$，增益矩陣保留 $G_t$。 |
| $D$ | P02 的 $D$ 為解碼／重建器；P08 的 $D_i$ 為 dependency set。 | 保留 $D$ 作 decoder，依賴集合可記為 $\mathcal D_i$ 以避免混淆。 |

## 4. 建議的 canonical naming 規則

- 拓撲 graph 建議固定寫成 $\mathcal G_t$。
- 增益矩陣固定寫成 $G_t=[g_{ij,t}]$。
- 觀測映射可在需要時寫成 $H_{\mathrm{obs}}$，避免與 heterogeneity 字母衝突。
- 安全 margin 函數建議寫成 $h_{\mathrm{safe}}$，同步對應映射可寫成 $h_{\mathrm{sync}}$ 或 $\eta$。
- dependency sets 建議寫成 $\mathcal D_i$，而 decoder 保留 $D$。

## 5. 備註

本表不是最終不可變字典，而是 **Papers 00–10 第一輪核心系列的 canonical working glossary**。