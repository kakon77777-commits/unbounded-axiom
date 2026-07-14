# 開放維度語義類型理論
## 面向異質資料、Agent、工具調用與跨尺度計算的可執行類型系統
### Open-Dimensional Semantic Type Theory
### An Executable Type System for Heterogeneous Data, Agents, Tool Use, and Cross-Scale Computing

**作者**：Neo.K（許筌崴）with Aletheia（GPT）  
**機構**：EveMissLab／一言諾科技有限公司  
**文件編號**：EML-COMP-2026-ODSTT-v1.0  
**版本**：v1.0  
**日期**：2026 年 7 月 13 日  
**性質**：計算機理論／語義類型系統／Agent 安全中介層／異質資料計算框架  
**建議縮寫**：ODSTT（Open-Dimensional Semantic Type Theory）  
**前置理論**：

1. 《多維空間狀態類型論》；
2. 《動態多維空間狀態類型論》；
3. 《空間狀態論》；
4. 《異質壓平論》；
5. 《異質空間狀態編織物理學》。

---

# 摘要

本文提出「**開放維度語義類型理論**」（Open-Dimensional Semantic Type Theory, ODSTT），作為一套面向異質資料、AI Agent、工具調用、跨模型資料融合、語義圖資料庫與跨尺度計算的可執行類型系統。

傳統程式語言類型系統主要回答：

$$
x:\texttt{Int},
\qquad
y:\texttt{String},
\qquad
z:\texttt{Tensor}.
$$

但在現代 AI 與複雜計算系統中，兩個對象即使都被儲存為：

$$
\mathbb R^n,
$$

也不代表它們可以合法比較、拼接或共同送入同一個模型。

一個模型輸出、實驗結果、記憶節點或工具參數，通常同時依賴：

- 對象本體；
- 任務；
- 使用者；
- 時間；
- 模型版本；
- 資料版本；
- 尺度；
- 表示；
- 觀察者；
- 證據強度；
- 權限；
- 歷史；
- 背景；
- 不確定度；
- 計算成本。

因此 ODSTT 將一個值定義為：

$$
\boxed{
x
=
(v,\tau,\pi,H,L),
}
$$

其中：

- $v$ ：實際數值或符號內容；
- $\tau$ ：開放維度語義類型；
- $\pi$ ：來源、證明與合法性證據；
- $H$ ：歷史與依賴鏈；
- $L$ ：信息損失帳本。

其類型可寫為：

$$
\boxed{
\tau(x)
=
\mathsf T
(
\omega,
q,
u,
t,
m,
d,
\ell,
\rho,
O,
e,
p,
h,
b,
c,
r
),
}
$$

其中：

- $\omega$ ：本體類型；
- $q$ ：任務類型；
- $u$ ：使用者或主體類型；
- $t$ ：時間類型；
- $m$ ：模型與版本類型；
- $d$ ：資料與版本類型；
- $\ell$ ：尺度與解析度類型；
- $\rho$ ：表示類型；
- $O$ ：觀察者與工具視角；
- $e$ ：證據類型；
- $p$ ：權限與政策類型；
- $h$ ：歷史與路徑類型；
- $b$ ：背景與容器類型；
- $c$ ：成本與資源類型；
- $r$ ：不確定度與風險類型。

本文的核心命題為：

$$
\boxed{
\text{資料型別相同}
\not\Rightarrow
\text{語義類型相容}.
}
$$

例如，兩個值都為 `numpy.ndarray`，仍可能來自不同使用者、不同模型版本、不同時間、不同尺度與不同證據層。若直接拼接，系統可能產生「格式合法但語義非法」的計算。

本文將工具與計算操作定義為部分態射：

$$
f:
X
\rightharpoonup
Y,
$$

只有當：

$$
x\in\operatorname{Dom}(f)
$$

且滿足背景、權限、版本、尺度與證據條件時，計算才合法。

完整調用形式為：

$$
\operatorname{Apply}(f,x)
=
\begin{cases}
(f(x),L_f), & \operatorname{Legal}(f,x)=1,\\
\mathsf{Undefined}, & \text{定義域不符},\\
\mathsf{Unauthorized}, & \text{權限不足},\\
\mathsf{Limbo}, & \text{證據或條件不足},\\
\mathsf{NeedNewType}, & \text{現有類型語法不足}.
\end{cases}
$$

本文進一步引入共享背景上的纖維積：

$$
\boxed{
X\times_BY
=
\left\{
(x,y):
\pi_X(x)=\pi_Y(y)
\right\},
}
$$

用於阻止不同使用者、不同案例、不同模型版本或不同資料批次的非法聯合。

本文也提出 ODSTT Agent 守門架構：

$$
\boxed{
\text{LLM}
\to
\text{ODSTT Guard}
\to
\text{Tools/Data/Memory}.
}
$$

所有 Agent 行動在執行前，必須經過：

$$
\text{類型推斷}
\to
\text{定義域檢查}
\to
\text{纖維兼容}
\to
\text{權限檢查}
\to
\text{信息損失估計}
\to
\text{合法調用}.
$$

本文最後提出動態有效支撐：

$$
J_{\mathrm{eff}}(Q,t)
\subseteq
J,
$$

使系統只在不確定或高風險時啟用額外類型維度與計算模組，而不是讓所有語義類型永久常駐。

ODSTT 的核心工程目標不是證明世界本身是一個類型系統，而是證明：

> **把背景、版本、權限、尺度、證據與歷史納入類型，可以阻止非法資料融合、降低 Agent 工具調用錯誤、減少定義域外高置信輸出，並在維持準確度時降低計算成本。**

**關鍵詞**：語義類型、依賴類型、Agent、工具調用、異質資料、纖維積、部分態射、信息損失、類型守門、跨尺度計算

---

# 0. 理論定位

## 0.1 ODSTT 是計算機理論，不是物理假說

ODSTT 不要求先證明：

$$
\text{自然界本體上就是一個多維類型系統}.
$$

它首先提出一個可直接驗證的計算機命題：

$$
\boxed{
\text{將語義背景納入類型，
能否阻止非法運算並降低計算錯誤？}
}
$$

此命題可以用：

- 單元測試；
- 模糊測試；
- Agent 工具調用基準；
- 異質資料融合；
- 跨版本回放；
- 權限測試；
- 高置信錯誤率；
- 成本—準確率前沿；

直接驗證。

## 0.2 ODSTT 不取代傳統類型論

傳統類型系統處理：

$$
\text{值的資料結構與運算合法性}.
$$

ODSTT 處理：

$$
\text{值的語義背景與跨系統運算合法性}.
$$

因此：

$$
\boxed{
\mathrm{TraditionalType}
\subset
\mathrm{SemanticType}.
}
$$

例如：

```text
Tensor[float32, shape=(512,)]
```

只描述資料結構。

ODSTT 還需要描述：

```text
Embedding[
    model="encoder-v3",
    corpus="paper-set-2026-07",
    user="project-alpha",
    scale="paragraph",
    evidence="machine-derived",
    version="3.2"
]
```

## 0.3 研究目標

ODSTT 希望建立：

1. 可執行的語義類型紀錄；
2. 部分態射與定義域檢查；
3. 纖維兼容聯合；
4. 權限與政策類型；
5. 信息損失帳本；
6. Agent 工具守門；
7. 動態有效類型支撐；
8. 類型生命週期；
9. 語義圖與資料庫接口；
10. Python／Rust 實作原型。

---

# 1. 現代計算系統中的語義型別缺口

## 1.1 格式合法不代表語義合法

設：

$$
x,y\in\mathbb R^{512}.
$$

從資料結構看：

$$
\operatorname{Shape}(x)
=
\operatorname{Shape}(y).
$$

但若：

$$
x:
\mathsf{Embedding}
(\text{model-A},\text{version-1}),
$$

$$
y:
\mathsf{Embedding}
(\text{model-B},\text{version-4}),
$$

則：

$$
x+y
$$

可能沒有合法語義。

## 1.2 同一欄位不代表同一量

資料表中的欄位：

```text
score
```

可能分別代表：

- 模型信心；
- 人工評分；
- 因果權重；
- 商業優先級；
- 風險分數；
- 實驗測量。

若直接拼接或平均：

$$
\bar s
=
\frac1n\sum_is_i,
$$

可能形成高精度但無意義的結果。

## 1.3 Agent 的工具錯誤通常不是語法錯誤

Agent 調用工具時，參數格式可能完全正確：

```json
{
  "file": "report.md",
  "action": "overwrite"
}
```

但仍可能錯在：

- 檔案不是正確專案；
- 是匯出檔而非來源檔；
- 版本過舊；
- 權限不足；
- 尚未完成人工審核；
- 操作不應覆蓋而應建立新版本。

這些不是普通資料型別錯誤，而是語義類型錯誤。

## 1.4 AI 高置信錯誤的類型來源

大型模型可能對：

- 不存在的資料組合；
- 不相容的版本；
- 不同主體的記憶；
- 錯誤時間窗；
- 未授權工具；
- 未定義跨尺度映射；

輸出高度自信的答案。

所以：

$$
\boxed{
\text{高置信錯誤}
\supset
\text{語義定義域外推理}.
}
$$

---

# 2. 開放維度語義類型

## 2.1 語義類型索引空間

定義：

$$
\boxed{
\mathfrak I_{\mathrm{sem}}
=
\mathcal O
\times
\mathcal Q
\times
\mathcal U
\times
\mathcal T
\times
\mathcal M
\times
\mathcal D
\times
\Lambda
\times
\mathcal R
\times
\mathcal V
\times
\mathcal E
\times
\mathcal P
\times
\mathcal H
\times
\mathcal B
\times
\mathcal C
\times
\mathcal R_{\mathrm{risk}}.
}
$$

對索引：

$$
i
=
(\omega,q,u,t,m,d,\ell,\rho,O,e,p,h,b,c,r),
$$

定義語義類型：

$$
\boxed{
\mathsf T_{\mathrm{sem}}(i).
}
$$

## 2.2 開放維度

不同系統可加入新的類型軸，例如：

- 法律管轄區；
- 隱私級別；
- 資料保留期限；
- 硬體裝置；
- 模型家族；
- 任務階段；
- 信任域；
- 組織角色；
- 地理位置。

因此類型維度集合 $J$ 不是封閉常數。

## 2.3 有限有效支撐

對一個具體操作 $Q$ ，只啟用：

$$
J_{\mathrm{eff}}(Q,t)
\subseteq
J.
$$

例如單純讀取檔案，可能只需要：

- 路徑；
- 權限；
- 版本；
- 所有者；
- 完整性。

而跨模型融合則可能需要更多類型軸。

---

# 3. 型別化值與來源鏈

## 3.1 基本資料結構

定義：

$$
\boxed{
x
=
(v,\tau,\pi,H,L).
}
$$

其中：

### $v$ ：值

可以是：

- 純量；
- 張量；
- 字串；
- 圖；
- 檔案；
- 模型輸出；
- 記憶節點；
- 工具結果。

### $\tau$ ：語義類型

記錄值屬於哪一個語義世界。

### $\pi$ ：來源與合法性

記錄：

- 來源；
- 產生工具；
- 產生模型；
- 簽章；
- 驗證；
- 證據強度。

### $H$ ：歷史

記錄：

- 父節點；
- 前置轉換；
- 版本；
- 推導鏈；
- 回放信息。

### $L$ ：損失帳本

記錄：

- 壓縮；
- 遺忘；
- 量化；
- 投影；
- 近似；
- 格式轉換；
- 資料缺失。

## 3.2 類型身份與內容分離

兩個值可能內容相同：

$$
v(x)=v(y),
$$

但類型不同：

$$
\tau(x)\neq\tau(y).
$$

因此：

$$
x\neq y.
$$

---

# 4. 部分態射與定義域安全

## 4.1 工具是部分態射

工具、模型與資料轉換不是全域函數，而是：

$$
\boxed{
f:
X
\rightharpoonup
Y.
}
$$

其定義域：

$$
\operatorname{Dom}(f)
\subseteq
X.
$$

## 4.2 合法性判定

定義：

$$
\operatorname{Legal}(f,x)
=
D_f(x)
\land
B_f(x)
\land
V_f(x)
\land
P_f(x)
\land
S_f(x)
\land
R_f(x),
$$

其中：

- $D_f$ ：資料結構合法；
- $B_f$ ：背景兼容；
- $V_f$ ：版本兼容；
- $P_f$ ：權限合法；
- $S_f$ ：尺度合法；
- $R_f$ ：風險可接受。

## 4.3 完整調用

$$
\operatorname{Apply}(f,x)
=
\begin{cases}
(f(x),L_f), & \operatorname{Legal}(f,x)=1,\\
\mathsf{Undefined}, & D_f=0,\\
\mathsf{Incompatible}, & B_fV_fS_f=0,\\
\mathsf{Unauthorized}, & P_f=0,\\
\mathsf{Limbo}, & \text{證據不足},\\
\mathsf{NeedNewType}, & \text{現有類型不足}.
\end{cases}
$$

## 4.4 未定義不等於錯誤值

若工具無法作用，不能回傳：

$$
0,
\qquad
\texttt{null},
\qquad
\texttt{false}
$$

並假裝它們是正常結果。

應回傳具有控制流意義的狀態：

$$
\mathsf{Undefined}.
$$


# 5. 纖維兼容與合法資料聯合

## 5.1 普通拼接的危險

資料工程中常見：

```python
features = concatenate([
    user_profile,
    model_output,
    external_data,
])
```

此操作只檢查：

- 資料可讀；
- 維度可拼接；
- 數值格式兼容。

但不檢查三者是否屬於：

- 同一使用者；
- 同一任務；
- 同一時間窗；
- 同一模型版本；
- 同一資料政策；
- 同一尺度；
- 同一證據層。

## 5.2 背景投影

對型別化資料 $x\in X$ ，定義背景投影：

$$
\pi_X:
X
\to
B.
$$

背景 $B$ 可包含：

$$
B
=
(
\text{tenant},
\text{user},
\text{project},
\text{task},
\text{time window},
\text{model version},
\text{dataset version}
).
$$

## 5.3 纖維積

兩個資料只有共享合法背景時才能聯合：

$$
\boxed{
X\times_BY
=
\left\{
(x,y)\in X\times Y:
\pi_X(x)=\pi_Y(y)
\right\}.
}
$$

若：

$$
\pi_X(x)\neq\pi_Y(y),
$$

則：

$$
(x,y)\notin X\times_BY.
$$

這表示聯合對象在當前語義系統中不存在。

## 5.4 弱兼容與轉換兼容

有些背景不完全相同，但存在合法轉換：

$$
g:
B_X
\rightharpoonup
B_Y.
$$

此時定義轉換纖維積：

$$
X\times_{g,B}Y
=
\left\{
(x,y):
g(\pi_X(x))=\pi_Y(y)
\right\}.
$$

例如：

- 時區轉換；
- 模型版本遷移；
- 度量單位轉換；
- 解析度粗粒化；
- 匿名化；
- 資料模式升級。

轉換必須附帶：

$$
(g,\pi_g,L_g),
$$

即合法性證明與信息損失。

## 5.5 多資料源聯合

對：

$$
X_1,\ldots,X_n,
$$

定義：

$$
\boxed{
\prod_BX_i
=
\left\{
(x_1,\ldots,x_n):
\pi_i(x_i)=b
\text{ for one common }b
\right\}.
}
$$

多來源 ETL、特徵商店與 Agent 記憶融合都應先建立共同纖維。

---

# 6. 信息損失帳本

## 6.1 計算不只產生結果，也產生損失

常見轉換包括：

- 降維；
- 壓縮；
- 量化；
- 摘要；
- 翻譯；
- 匿名化；
- 模型蒸餾；
- 圖像縮放；
- 格式轉換；
- 粗粒化；
- 截斷上下文。

每個轉換：

$$
f:X\rightharpoonup Y
$$

都應附帶損失：

$$
L_f(x).
$$

## 6.2 損失向量

信息損失不是單一純量，而可定義為：

$$
\boxed{
L_f
=
\left(
L_{\mathrm{semantic}},
L_{\mathrm{resolution}},
L_{\mathrm{provenance}},
L_{\mathrm{uncertainty}},
L_{\mathrm{reversibility}},
L_{\mathrm{policy}}
\right).
}
$$

分別表示：

- 語義遺失；
- 解析度遺失；
- 來源鏈遺失；
- 不確定度擴大；
- 可逆性降低；
- 政策與權限信息遺失。

## 6.3 損失合成

若：

$$
X\xrightarrow{f}Y\xrightarrow{g}Z,
$$

則總損失不能簡單假設為：

$$
L_{g\circ f}=L_f+L_g.
$$

一般定義損失合成算子：

$$
\boxed{
L_{g\circ f}
=
L_g
\oplus
g_\ast L_f,
}
$$

其中 $g_\ast$ 表示前一步損失在後一步表示中的傳遞。

## 6.4 損失門檻

工具可以規定：

$$
L_f(x)
\preceq
L_{\max}.
$$

若超過門檻，回傳：

$$
\mathsf{LossExceeded}.
$$

例如法律文件摘要後若來源鏈與限定語損失過大，不允許直接進入自動決策。

---

# 7. 語義控制流類型

## 7.1 非布林結果

傳統流程常將結果壓成：

$$
\mathsf{True}
\quad\text{或}\quad
\mathsf{False}.
$$

ODSTT 保留：

$$
\boxed{
\mathfrak S_{\mathrm{control}}
=
\{
\mathsf{Success},
\mathsf{False},
\mathsf{Unknown},
\mathsf{Undefined},
\mathsf{Incompatible},
\mathsf{Unauthorized},
\mathsf{Unproven},
\mathsf{Undecidable},
\mathsf{Limbo},
\mathsf{NeedNewType},
\mathsf{LossExceeded},
\mathsf{Conflict}
\}.
}
$$

## 7.2 控制流語義

| 狀態 | 意義 | 系統行為 |
|---|---|---|
| Success | 合法完成 | 提交結果 |
| False | 命題被否定 | 結束或修正 |
| Unknown | 缺少資料 | 搜尋或請求資料 |
| Undefined | 操作無定義 | 停止並標示定義域 |
| Incompatible | 背景不兼容 | 尋找轉換態射 |
| Unauthorized | 權限不足 | 拒絕執行 |
| Unproven | 尚無證明 | 啟動驗證 |
| Undecidable | 當前系統不可決定 | 回報界限 |
| Limbo | 條件未滿足 | 暫存並監測 |
| NeedNewType | 類型語法不足 | 建立候選類型 |
| LossExceeded | 信息損失過大 | 改用高保真流程 |
| Conflict | 多來源矛盾 | 啟動衝突治理 |

## 7.3 Limbo 的解除條件

$$
\mathsf{Limbo}
\left(
x,
\mathcal C_{\mathrm{resolve}}
\right),
$$

其中：

$$
\mathcal C_{\mathrm{resolve}}
=
\{
\text{new data},
\text{higher permission},
\text{human approval},
\text{version migration},
\text{additional tool},
\text{lower uncertainty}
\}.
$$

Limbo 不是永久擱置，而是帶有解除條件的合法狀態。

---

# 8. ODSTT Agent 守門架構

## 8.1 基本架構

$$
\boxed{
\text{User/Environment}
\to
\text{LLM Planner}
\to
\text{ODSTT Guard}
\to
\text{Tools/Data/Memory}
\to
\text{Typed Result}.
}
$$

LLM 可以提出行動，但不能直接執行。

## 8.2 守門步驟

$$
\boxed{
\text{Parse Intent}
\to
\text{Infer Types}
\to
\text{Select }J_{\mathrm{eff}}
\to
\text{Check Domain}
\to
\text{Check Fiber}
\to
\text{Check Permission}
\to
\text{Estimate Loss/Risk}
\to
\text{Execute or Abstain}.
}
$$

## 8.3 工具契約

每個工具註冊：

$$
\mathcal C_f
=
(
\operatorname{Dom}(f),
\operatorname{Cod}(f),
P_f,
V_f,
B_f,
L_f,
R_f
).
$$

其中：

- $\operatorname{Dom}(f)$ ：輸入語義類型；
- $\operatorname{Cod}(f)$ ：輸出語義類型；
- $P_f$ ：權限要求；
- $V_f$ ：版本要求；
- $B_f$ ：背景兼容要求；
- $L_f$ ：損失模型；
- $R_f$ ：風險模型。

## 8.4 調用前證明義務

Agent 執行前需構造：

$$
\boxed{
\pi_{\mathrm{call}}
:
\operatorname{LegalCall}(f,x,\mathcal C_f).
}
$$

此證明不一定是完整形式證明，也可以是可審計的執行證書：

```json
{
  "tool": "update_document",
  "input_type": "SourceDocument",
  "project_match": true,
  "version_match": true,
  "permission": "write",
  "human_review_required": false,
  "estimated_loss": 0.0,
  "risk": "low"
}
```

## 8.5 寫入操作與讀取操作分型

讀取工具：

$$
f_{\mathrm{read}}:
X\rightharpoonup Y
$$

與寫入工具：

$$
f_{\mathrm{write}}:
X\rightharpoonup X'
$$

風險不同。

寫入態射應額外要求：

- 可回滾；
- 版本快照；
- 衝突檢查；
- 目標資源身份；
- 使用者意圖；
- 變更範圍；
- 審批政策。

---

# 9. 權限、政策與安全類型

## 9.1 權限不是外部布林值

定義權限類型：

$$
p(x)
=
(
\text{principal},
\text{resource},
\text{action},
\text{scope},
\text{expiry},
\text{policy}
).
$$

工具合法性依賴：

$$
\operatorname{Authorize}(p,f,x).
$$

## 9.2 主體與租戶隔離

在多租戶系統中：

$$
u(x)\neq u(y)
$$

通常推出：

$$
(x,y)\notin X\times_BY.
$$

除非存在明確的跨租戶授權態射。

## 9.3 資料分類與保留期限

可加入：

$$
\mathsf{Public},
\mathsf{Internal},
\mathsf{Confidential},
\mathsf{Restricted}
$$

以及：

$$
t_{\mathrm{retention}}.
$$

當保留期限結束，資料類型進入：

$$
\mathsf{Expired}.
$$

後續工具不得繼續讀取或推理。

---

# 10. 動態有效類型支撐

## 10.1 全類型常駐的成本

若所有操作都檢查全部類型軸，可能增加：

- 延遲；
- 記憶體；
- 規則衝突；
- 類型推理成本；
- 工具註冊負荷；
- Agent 上下文長度。

因此定義：

$$
\boxed{
J_{\mathrm{eff}}(Q,t,R)
\subseteq
J,
}
$$

其中 $R$ 是風險級別。

## 10.2 基礎支撐

每個任務有最低支撐：

$$
J_{\min}(Q).
$$

例如讀取檔案至少需要：

$$
J_{\min}
=
\{
\text{resource identity},
\text{permission},
\text{version}
\}.
$$

## 10.3 不確定度驅動擴張

若基礎支撐下：

$$
u(x)>\theta_u,
$$

或：

$$
R(x)>\theta_R,
$$

則啟用額外類型：

$$
J_{\mathrm{eff}}
\leftarrow
J_{\mathrm{eff}}
\cup
J_{\mathrm{extra}}.
$$

例如增加：

- 來源鏈；
- 歷史；
- 人工審核；
- 第二模型；
- 更高解析度；
- 法律管轄；
- 隱私政策。

## 10.4 成本—安全帕雷特前沿

候選支撐 $\Theta$ 以：

$$
\mathbf f(\Theta)
=
(
C_{\mathrm{latency}},
C_{\mathrm{memory}},
E_{\mathrm{illegal}},
E_{\mathrm{false}},
L_{\mathrm{info}},
R_{\mathrm{security}}
)
$$

評估。

保留非支配集合：

$$
\mathcal P_\Theta
=
\operatorname{ND}(\mathfrak C_\Theta,\mathbf f).
$$

---

# 11. 語義圖資料庫

## 11.1 型別化節點

語義圖節點：

$$
n
=
(v,\tau,\pi,H,L,\sigma),
$$

其中 $\sigma$ 是生命週期：

$$
\mathsf{Candidate},
\mathsf{Active},
\mathsf{Latent},
\mathsf{Deprecated},
\mathsf{Archived},
\mathsf{Retired}.
$$

## 11.2 型別化邊

每條邊必須具有箭頭類型：

$$
e:
n_i
\xrightarrow{\kappa}
n_j.
$$

箭頭可為：

- `causes`；
- `depends_on`；
- `observes`；
- `estimates`；
- `derived_from`；
- `approximates`；
- `contradicts`；
- `supersedes`；
- `authorized_by`；
- `translated_from`。

## 11.3 禁止無類型邊

傳統知識圖常只有：

```text
A related_to B
```

ODSTT 要求：

$$
\kappa\neq\mathsf{UnknownRelation}
$$

或至少標記：

$$
\mathsf{UnresolvedRelation}.
$$

未分型邊不能直接參與因果或推導查詢。

## 11.4 語義 SQL

查詢不只指定欄位，而指定類型條件：

```sql
SELECT result
FROM typed_values
WHERE ontology = 'ModelOutput'
  AND task_id = :task_id
  AND model_version = :version
  AND evidence_level >= 'validated'
  AND lifecycle = 'Active';
```

聯合時檢查共同纖維：

```sql
JOIN typed_values b
ON a.background_id = b.background_id
AND a.dataset_version = b.dataset_version
AND a.scale = b.scale;
```

---

# 12. AI 記憶中的語義類型

## 12.1 記憶不是普通文本塊

記憶項目應記錄：

$$
m
=
(
\text{content},
\text{subject},
\text{time},
\text{source},
\text{confidence},
\text{scope},
\text{consent},
\text{lifecycle}
).
$$

## 12.2 主體隔離

不同主體的記憶：

$$
m_A,
\qquad
m_B
$$

不能因語義相似而自動融合。

必須滿足：

$$
\operatorname{ConsentCompatible}(m_A,m_B)
$$

與：

$$
\operatorname{ScopeCompatible}(m_A,m_B).
$$

## 12.3 記憶更新箭頭

區分：

$$
\mathsf{Adds},
\quad
\mathsf{Corrects},
\quad
\mathsf{Supersedes},
\quad
\mathsf{Contradicts},
\quad
\mathsf{Expires}.
$$

新記憶不能只覆蓋舊記憶，而應保留版本與轉換箭頭。

## 12.4 記憶壓縮

摘要記憶：

$$
S(m)
$$

必須攜帶：

$$
L_S(m).
$$

若摘要損失使原始限定條件消失，不能用於高風險決策。


# 13. 可執行 Python 原型

## 13.1 基本類型記錄

```python
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Generic, Mapping, TypeVar


T = TypeVar("T")
U = TypeVar("U")


class ControlState(str, Enum):
    SUCCESS = "success"
    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    INCOMPATIBLE = "incompatible"
    UNAUTHORIZED = "unauthorized"
    LIMBO = "limbo"
    NEED_NEW_TYPE = "need_new_type"
    LOSS_EXCEEDED = "loss_exceeded"
    CONFLICT = "conflict"


@dataclass(frozen=True)
class SemanticType:
    ontology: str
    task_id: str
    subject_id: str
    timestamp: str
    model_version: str
    dataset_version: str
    scale: str
    representation: str
    observer: str
    evidence: str
    permission_scope: str
    history_id: str
    background_id: str
    resource_class: str
    uncertainty: float


@dataclass(frozen=True)
class LossLedger:
    semantic: float = 0.0
    resolution: float = 0.0
    provenance: float = 0.0
    uncertainty: float = 0.0
    reversibility: float = 0.0
    policy: float = 0.0


@dataclass
class TypedValue(Generic[T]):
    value: T
    semantic_type: SemanticType
    provenance: tuple[str, ...] = ()
    history: tuple[str, ...] = ()
    loss: LossLedger = field(default_factory=LossLedger)
```

## 13.2 工具契約

```python
@dataclass(frozen=True)
class ToolContract(Generic[T, U]):
    name: str
    domain_check: Callable[[TypedValue[T]], bool]
    permission_check: Callable[[TypedValue[T]], bool]
    transform: Callable[[TypedValue[T]], TypedValue[U]]
    loss_estimator: Callable[[TypedValue[T]], LossLedger]
    max_loss: LossLedger
```

## 13.3 控制流結果

```python
@dataclass
class TypedResult(Generic[U]):
    state: ControlState
    value: TypedValue[U] | None = None
    reason: str = ""
    evidence: Mapping[str, Any] = field(default_factory=dict)
```

## 13.4 合法調用

```python
def loss_within_limit(
    actual: LossLedger,
    maximum: LossLedger,
) -> bool:
    return all(
        getattr(actual, field_name)
        <= getattr(maximum, field_name)
        for field_name in actual.__dataclass_fields__
    )


def apply_tool(
    contract: ToolContract[T, U],
    item: TypedValue[T],
) -> TypedResult[U]:
    if not contract.domain_check(item):
        return TypedResult(
            state=ControlState.UNDEFINED,
            reason=f"{contract.name} is undefined for this semantic type.",
        )

    if not contract.permission_check(item):
        return TypedResult(
            state=ControlState.UNAUTHORIZED,
            reason=f"{contract.name} lacks the required permission scope.",
        )

    estimated_loss = contract.loss_estimator(item)

    if not loss_within_limit(
        estimated_loss,
        contract.max_loss,
    ):
        return TypedResult(
            state=ControlState.LOSS_EXCEEDED,
            reason="Estimated semantic loss exceeds the contract limit.",
            evidence={"estimated_loss": estimated_loss},
        )

    output = contract.transform(item)

    return TypedResult(
        state=ControlState.SUCCESS,
        value=output,
        evidence={
            "tool": contract.name,
            "estimated_loss": estimated_loss,
        },
    )
```

---

# 14. 纖維兼容原型

## 14.1 共同背景鍵

```python
@dataclass(frozen=True)
class FiberKey:
    subject_id: str
    task_id: str
    background_id: str
    dataset_version: str
    scale: str
```

## 14.2 提取纖維鍵

```python
def fiber_key(item: TypedValue[Any]) -> FiberKey:
    semantic_type = item.semantic_type

    return FiberKey(
        subject_id=semantic_type.subject_id,
        task_id=semantic_type.task_id,
        background_id=semantic_type.background_id,
        dataset_version=semantic_type.dataset_version,
        scale=semantic_type.scale,
    )
```

## 14.3 聯合守門器

```python
def fiber_join(
    left: TypedValue[Any],
    right: TypedValue[Any],
) -> TypedResult[tuple[Any, Any]]:
    if fiber_key(left) != fiber_key(right):
        return TypedResult(
            state=ControlState.INCOMPATIBLE,
            reason="The values do not belong to the same semantic fiber.",
            evidence={
                "left_fiber": fiber_key(left),
                "right_fiber": fiber_key(right),
            },
        )

    joined_type = left.semantic_type

    return TypedResult(
        state=ControlState.SUCCESS,
        value=TypedValue(
            value=(left.value, right.value),
            semantic_type=joined_type,
            provenance=left.provenance + right.provenance,
            history=left.history + right.history,
        ),
    )
```

## 14.4 轉換後聯合

若版本不同，但存在版本遷移工具：

```python
migrated = apply_tool(
    version_migration_contract,
    old_value,
)

if migrated.state is ControlState.SUCCESS:
    result = fiber_join(
        migrated.value,
        new_value,
    )
```

此流程使「版本不同」不再被默認忽略，而是要求顯式遷移。

---

# 15. Rust 核心接口方向

Python 適合原型，但高性能 Agent 中介層與資料管線可使用 Rust。

```rust
pub enum ControlState {
    Success,
    Unknown,
    Undefined,
    Incompatible,
    Unauthorized,
    Limbo,
    NeedNewType,
    LossExceeded,
    Conflict,
}

pub struct SemanticType {
    pub ontology: String,
    pub task_id: String,
    pub subject_id: String,
    pub model_version: String,
    pub dataset_version: String,
    pub scale: String,
    pub background_id: String,
    pub permission_scope: String,
    pub uncertainty: f64,
}

pub struct TypedValue<T> {
    pub value: T,
    pub semantic_type: SemanticType,
    pub provenance: Vec<String>,
    pub history: Vec<String>,
    pub loss: LossLedger,
}

pub trait PartialMorphism<X, Y> {
    fn is_defined(&self, input: &TypedValue<X>) -> bool;
    fn is_authorized(&self, input: &TypedValue<X>) -> bool;
    fn estimate_loss(&self, input: &TypedValue<X>) -> LossLedger;
    fn apply(&self, input: TypedValue<X>) -> TypedResult<Y>;
}
```

Rust 版本可用於：

- Agent 工具代理；
- 資料庫中介層；
- 高吞吐事件流；
- 權限守門；
- 模型服務路由；
- 語義類型檢查器。

---

# 16. 形式性質

## 16.1 語義保全

若：

$$
\Gamma\vdash x:X
$$

且：

$$
f:X\rightharpoonup Y
$$

並存在合法性證明：

$$
\pi_f:
\operatorname{Legal}(f,x),
$$

則：

$$
\Gamma\vdash f(x):Y.
$$

這是 ODSTT 的語義保全要求。

## 16.2 未定義安全

若：

$$
x\notin\operatorname{Dom}(f),
$$

則系統不能產生普通 $Y$ 類型值。

只能產生：

$$
\mathsf{Undefined}.
$$

因此未定義狀態不能偽裝成合法結果。

## 16.3 纖維安全

若：

$$
\pi_X(x)\neq\pi_Y(y),
$$

則無法構造：

$$
(x,y):X\times_BY.
$$

這使背景不兼容的聯合在類型層不可構造。

## 16.4 來源單調性

合法推導的來源鏈不能無故縮短：

$$
\operatorname{Prov}(f(x))
\supseteq
\operatorname{Prov}(x).
$$

若某轉換必須遺忘來源，應記入：

$$
L_{\mathrm{provenance}}>0.
$$

## 16.5 損失守恆帳本

每次有損轉換都必須更新 $L$ 。不要求信息物理守恆，而要求：

$$
\boxed{
\text{已知損失不能在後續流程中被無聲消失。}
}
$$

## 16.6 權限非提升

若不存在授權態射，則：

$$
p_{\mathrm{low}}
\not\to
p_{\mathrm{high}}.
$$

工具不能因模型信心高而自行提升權限。

---

# 17. 計算機系統應用

## 17.1 多模型輸出融合

不同模型輸出：

$$
y_A:
\mathsf{Prediction}(m_A,d_A),
$$

$$
y_B:
\mathsf{Prediction}(m_B,d_B)
$$

只有在存在校準或映射：

$$
g:
Y_A\rightharpoonup Y_B
$$

後才能融合。

## 17.2 特徵商店

每個特徵除名稱與數值外，保存：

- 來源；
- 更新頻率；
- 時間窗；
- 主體；
- 特徵版本；
- 訓練／推理一致性；
- 隱私政策；
- 缺失策略。

這能降低訓練—服務偏移。

## 17.3 ETL 與資料湖

ETL 每一步輸出：

$$
(\text{dataset},\tau,L,H).
$$

資料湖中的資料不再只有 schema，也有語義類型與生命周期。

## 17.4 API 契約

API 不只指定 JSON 結構，而可指定：

- 版本語義；
- 時間語義；
- 單位；
- 資料來源；
- 權限；
- 不確定度；
- 可接受損失；
- 冪等性；
- 可回滾性。

## 17.5 工作流引擎

工作流節點以部分態射構成：

$$
X_0
\rightharpoonup
X_1
\rightharpoonup
\cdots
\rightharpoonup
X_n.
$$

每條邊執行前都檢查合法性。

## 17.6 科學計算

模擬、儀器與分析資料分型：

$$
X_{\mathrm{simulation}},
\quad
X_{\mathrm{instrument}},
\quad
X_{\mathrm{inference}}.
$$

禁止把數值代理直接當成物理機制。

## 17.7 軟體版本遷移

舊結構：

$$
X_{v1}
$$

與新結構：

$$
X_{v2}
$$

由遷移態射：

$$
m_{12}:
X_{v1}
\rightharpoonup
X_{v2}
$$

連接。

遷移失敗、部分成功與有損轉換都成為正式類型結果。

---

# 18. Agent 實戰場景

## 18.1 文件修改 Agent

輸入文件必須分型：

$$
\mathsf{SourceDocument},
\quad
\mathsf{ExportedDocument},
\quad
\mathsf{ArchivedDocument}.
$$

覆蓋操作只允許：

$$
\mathsf{SourceDocument}
\xrightarrow{\mathrm{edit}}
\mathsf{SourceDocument}'.
$$

對匯出檔執行覆蓋應回傳：

$$
\mathsf{Undefined}
$$

或：

$$
\mathsf{NeedSource}.
$$

## 18.2 郵件 Agent

郵件草稿與立即發送分型：

$$
\mathsf{DraftEmail}
\neq
\mathsf{SendAuthorizedEmail}.
$$

使用者說「幫我寫」只構造草稿類型，不能自動提升成發送權限。

## 18.3 程式碼 Agent

程式碼修改需要：

- 儲存庫；
- 分支；
- 工作樹狀態；
- 測試狀態；
- 變更範圍；
- 提交權限。

跨分支補丁若背景不同，不能直接合併。

## 18.4 個人記憶 Agent

推論前檢查：

- 記憶屬於哪一位主體；
- 是否已過期；
- 是否只是暫時偏好；
- 是否被後續記憶修正；
- 是否允許在當前任務使用。

## 18.5 高風險工具

金融、醫療、法律與安全工具可要求：

$$
e\ge e_{\min},
$$

$$
u\le u_{\max},
$$

$$
p\ge p_{\min}.
$$

條件不滿足時，進入：

$$
\mathsf{Limbo}
$$

或要求人工審核。

---

# 19. 類型生命週期與治理

## 19.1 生命週期

$$
\boxed{
\mathsf{Candidate}
\to
\mathsf{Active}
\to
\mathsf{Latent}
\to
\mathsf{Deprecated}
\to
\mathsf{Archived}
\to
\mathsf{Retired}.
}
$$

## 19.2 任務局部狀態

同一類型可以：

$$
\mathsf{Deprecated}_{Q_1}
$$

但：

$$
\mathsf{Active}_{Q_2}.
$$

例如拓撲圖冊可能不適合事件預測，仍適合拓撲審計。

## 19.3 安全退役

類型只能在：

$$
\operatorname{RefCount}=0,
$$

$$
\operatorname{ProofDependency}=0,
$$

$$
\operatorname{WorkflowDependency}=0
$$

且存在遷移方案時退役。

## 19.4 語義債務

定義：

$$
\boxed{
D_{\mathrm{semantic}}
=
D_{\mathrm{untyped}}
+
D_{\mathrm{version}}
+
D_{\mathrm{provenance}}
+
D_{\mathrm{loss}}
+
D_{\mathrm{policy}}.
}
$$

語義債務高的系統容易產生：

- 隱性資料漂移；
- 不可重現；
- 權限錯誤；
- 模型輸出誤用；
- Agent 跨背景幻覺。

---

# 20. 評估指標

## 20.1 非法運算攔截率

$$
\operatorname{BlockRate}
=
\frac{
\text{被正確阻止的非法操作}
}{
\text{全部非法操作}
}.
$$

## 20.2 合法操作誤拒率

$$
\operatorname{FalseReject}
=
\frac{
\text{被錯誤阻止的合法操作}
}{
\text{全部合法操作}
}.
$$

## 20.3 定義域外高置信率

$$
\operatorname{OOC}
=
\frac{
\text{定義域外但高置信輸出}
}{
\text{全部定義域外案例}
}.
$$

ODSTT 應顯著降低此量。

## 20.4 語義損失可追蹤率

$$
\operatorname{LossTrace}
=
\frac{
\text{具有完整損失帳本的有損轉換}
}{
\text{全部有損轉換}
}.
$$

## 20.5 Agent 工具錯誤率

測量：

- 錯誤資源；
- 錯誤版本；
- 錯誤權限；
- 錯誤主體；
- 錯誤工具；
- 錯誤寫入模式。

## 20.6 成本—安全前沿

比較：

$$
\text{latency},
\quad
\text{memory},
\quad
\text{blocked errors},
\quad
\text{false rejects},
\quad
\text{task success}.
$$

ODSTT 不必在單一指標上全勝，但應形成新的非支配點。

---

# 21. 基準測試設計

## 21.1 異質拼接基準

建立：

- 同格式同背景；
- 同格式不同背景；
- 同格式不同版本；
- 同格式不同主體；
- 同格式不同尺度；

的資料對。

比較普通 schema 檢查與 ODSTT 纖維檢查。

## 21.2 Agent 工具基準

建立工具調用任務：

1. 正確讀取；
2. 錯誤版本；
3. 錯誤檔案；
4. 無權限寫入；
5. 草稿／發送混淆；
6. 來源檔／匯出檔混淆；
7. 跨使用者記憶污染；
8. 高損失摘要後決策。

## 21.3 動態支撐基準

比較：

- 無守門；
- 全類型常駐；
- 固定最小支撐；
- 不確定度驅動動態支撐。

## 21.4 長期治理基準

長期運行 Agent，測量：

- 類型數；
- 重複類型；
- 過期類型；
- 規則衝突；
- 回放成功率；
- 歷史重建率；
- 垃圾回收收益。

---

# 22. 可否證條件

ODSTT 的工程價值應被弱化，若：

1. 普通 schema 與權限系統已能同樣阻止所有語義非法操作；
2. 纖維檢查造成大量合法操作誤拒；
3. 類型推理成本高於其阻止錯誤的收益；
4. 信息損失帳本不能預測任何實際錯誤；
5. Agent 守門器不能降低工具調用錯誤；
6. Limbo 只造成低完成率，卻不降低高置信錯誤；
7. 動態有效支撐不能降低成本；
8. 開放維度導致類型碎裂與不可治理；
9. 語義類型在跨組織環境中無法標準化；
10. 類型生命週期不能降低長期治理負荷。

---

# 23. 與既有技術的關係

## 23.1 與依賴類型

ODSTT 使用依賴類型思想，使類型依賴：

- 版本；
- 主體；
- 任務；
- 背景；
- 證據；
- 權限。

但其目標不是重新建立完整邏輯基礎，而是工程化語義守門。

## 23.2 與 refinement types

Refinement type 可表示：

$$
x:\{v:X\mid P(v)\}.
$$

ODSTT 可將背景兼容、版本、證據與權限表示為細化條件，但還增加：

- 開放類型軸；
- 來源鏈；
- 損失帳本；
- 纖維聯合；
- 生命週期；
- 動態有效支撐。

## 23.3 與 effect systems

工具調用可視為帶 effect：

$$
\mathsf{Read},
\mathsf{Write},
\mathsf{Send},
\mathsf{Delete},
\mathsf{ExternalCall}.
$$

ODSTT 可與 effect system 結合，讓語義類型決定哪些 effect 合法。

## 23.4 與信息流控制

安全標籤：

$$
\mathsf{Public}
\preceq
\mathsf{Internal}
\preceq
\mathsf{Confidential}
\preceq
\mathsf{Restricted}
$$

可作為 ODSTT 的權限維度之一。

## 23.5 與 knowledge graph

知識圖通常重視實體與關係；ODSTT 增加：

- 關係箭頭型別；
- 背景纖維；
- 版本；
- 證據；
- 生命周期；
- 損失。

## 23.6 與 data contracts

Data contract 通常規範 schema、品質與 SLA。ODSTT 將其提升為可組合的部分態射與語義類型契約。

---

# 24. 研究與產品路線

## Phase I：Python 核心函式庫

實作：

- `SemanticType`；
- `TypedValue`；
- `PartialMorphism`；
- `fiber_join`；
- `LossLedger`；
- 控制流狀態；
- 類型註冊表；
- 單元測試。

## Phase II：Agent Guard

建立：

$$
\text{LLM}
\to
\text{ODSTT Guard}
\to
\text{Tool Registry}.
$$

先接入：

- 檔案工具；
- 郵件工具；
- 日曆工具；
- 資料庫工具；
- 程式碼工具。

## Phase III：語義圖資料庫

建立：

- 節點類型；
- 箭頭類型；
- 來源鏈；
- 版本；
- 生命周期；
- 語義 SQL；
- 圖查詢。

## Phase IV：Rust 高性能中介層

用於：

- 高吞吐工具路由；
- 事件流；
- 多 Agent；
- 權限守門；
- 模型服務；
- 資料管線。

## Phase V：形式化核心

在 Lean 4 中形式化：

1. 部分態射；
2. 纖維兼容；
3. 未定義安全；
4. 權限非提升；
5. 來源單調；
6. 損失帳本；
7. 類型遷移。

---

# 25. 核心命題集

## 命題一：語義相容性命題

資料結構相同不推出語義類型相容。

## 命題二：工具部分態射命題

現實工具只對部分語義類型有定義。

## 命題三：纖維聯合命題

多來源資料只有共享合法背景或存在合法背景轉換時才能聯合。

## 命題四：未定義安全命題

定義域外操作不能產生普通合法結果。

## 命題五：權限非提升命題

沒有明確授權態射，Agent 不能提升操作權限。

## 命題六：來源保留命題

推導結果應保留可追蹤來源；來源遺失必須進入損失帳本。

## 命題七：有損轉換顯式命題

壓縮、摘要、翻譯與粗粒化必須報告語義損失。

## 命題八：控制流類型命題

Unknown、Undefined、Unauthorized、Limbo 與 NeedNewType 是不同控制流，而非同一失敗狀態。

## 命題九：動態有效支撐命題

語義類型維度應依任務、不確定度與風險按需啟用。

## 命題十：任務局部生命週期命題

類型的活躍、棄用與退役狀態依任務與背景而定。

## 命題十一：Agent 守門命題

LLM 的計畫不應直接等於工具執行；中間必須有可審計的語義類型守門層。

## 命題十二：可執行價值命題

ODSTT 的價值應由非法操作攔截、錯誤率、成本、可回放性與治理負荷實證，而非由本體論宣言證成。

---

# 26. 結論

現代計算系統已經能處理極大量的文字、圖像、張量、圖結構與工具調用，但它們仍經常只檢查：

- 格式是否正確；
- schema 是否匹配；
- shape 是否一致；
- API 參數是否完整。

這些檢查不足以回答：

- 這些資料是否來自同一主體？
- 是否屬於同一任務？
- 是否是相容版本？
- 是否具有合法權限？
- 是否位於同一尺度？
- 是否有足夠證據？
- 是否經歷了不可接受的信息損失？
- 這個工具是否真的對當前對象有定義？

因此，本文提出：

$$
\boxed{
\text{不要只檢查資料長得是否相同，
還要檢查它們是否來自同一個可合法計算的世界。}
}
$$

ODSTT 將一個值從：

$$
v
$$

擴展為：

$$
(v,\tau,\pi,H,L),
$$

並將工具從全域函數擴展為：

$$
f:X\rightharpoonup Y.
$$

它不要求 AI 永遠回答，也不允許工具只因參數格式正確就執行。它正式保留：

$$
\mathsf{Undefined},
\mathsf{Incompatible},
\mathsf{Unauthorized},
\mathsf{Limbo},
\mathsf{NeedNewType},
\mathsf{LossExceeded}.
$$

ODSTT 的真正計算機理論價值，不在於把世界描述得更複雜，而在於：

$$
\boxed{
\text{讓不合法的計算難以被構造，
讓有損計算留下痕跡，
讓高風險行動需要證明，
讓不確定情況能合法暫停。}
}
$$

其最終工程鏈為：

$$
\boxed{
\text{Typed Data}
\to
\text{Legal Partial Morphisms}
\to
\text{Fiber-Safe Composition}
\to
\text{Loss-Aware Execution}
\to
\text{Auditable Agent Action}.
}
$$

ODSTT 因此不是一套只存在於論文中的分類哲學，而是一個可以被寫成函式庫、中介層、資料庫、工作流引擎與 Agent 安全架構的可執行計算機理論。

---

# 附錄 A：核心符號表

| 符號 | 意義 |
|---|---|
| $\mathfrak I_{\mathrm{sem}}$ | 開放維度語義類型索引空間 |
| $\mathsf T_{\mathrm{sem}}(i)$ | 索引 $i$ 下的語義類型 |
| $x=(v,\tau,\pi,H,L)$ | 型別化值 |
| $f:X\rightharpoonup Y$ | 部分態射 |
| $\operatorname{Dom}(f)$ | 工具定義域 |
| $\operatorname{Legal}(f,x)$ | 調用合法性 |
| $X\times_BY$ | 共享背景上的纖維積 |
| $L_f$ | 工具或轉換的信息損失 |
| $J_{\mathrm{eff}}$ | 動態有效類型支撐 |
| $\mathcal P_\Theta$ | 成本—安全帕雷特前沿 |
| $D_{\mathrm{semantic}}$ | 語義債務 |
| $\pi_{\mathrm{call}}$ | 工具調用合法性證書 |

---

# 附錄 B：最小實作模組

```text
odstt/
├── types.py
├── values.py
├── morphisms.py
├── fibers.py
├── permissions.py
├── losses.py
├── control.py
├── registry.py
├── lifecycle.py
├── agent_guard.py
├── audit.py
└── tests/
    ├── test_domain.py
    ├── test_fiber.py
    ├── test_permission.py
    ├── test_loss.py
    ├── test_limbo.py
    └── test_version_migration.py
```

---

# 附錄 C：首批非法操作測試

| 測試 | 預期結果 |
|---|---|
| 不同使用者記憶直接拼接 | Incompatible |
| 不同模型 embedding 直接相加 | Undefined／NeedMigration |
| 草稿郵件直接發送 | Unauthorized |
| 匯出檔當來源檔覆蓋 | Undefined |
| 過期資料進入模型 | Incompatible |
| 高損失摘要進入法律決策 | LossExceeded |
| 不同網格資料直接比較 | Incompatible |
| 未知關係邊用於因果推理 | Undefined |
| 無來源模型輸出進入高風險工具 | Limbo |
| 舊 schema 未遷移即寫入 | NeedMigration |

---

# 附錄 D：與前置理論的關係

$$
\boxed{
\mathrm{MSSTT}
\xrightarrow{\text{computer semantics}}
\mathrm{ODSTT}
\xrightarrow{\text{executable guard}}
\text{Agent/Data/Tool Systems}.
}
$$

其中：

- MSSTT 提供開放維度類型、部分態射與纖維兼容；
- DMSSTT 提供動態有效支撐與類型生命週期；
- ODSTT 將其轉化為可執行計算機架構；
- HFC 提供異質壓平與箭頭錯型審計；
- SST 提供可變空間狀態的上位載體。

---

# 版本紀錄

## v1.0 — 2026-07-13

- 將 MSSTT 正式定位為計算機語義類型理論；
- 定義開放維度語義類型索引；
- 建立型別化值五元組；
- 定義工具部分態射與調用合法性；
- 建立纖維安全資料聯合；
- 建立信息損失向量與損失帳本；
- 建立十二種語義控制流狀態；
- 建立 ODSTT Agent 守門架構；
- 引入權限、政策與資料保留類型；
- 建立動態有效類型支撐；
- 建立語義圖資料庫與語義 SQL 接口；
- 建立 AI 記憶語義類型；
- 提供 Python 與 Rust 核心原型；
- 定義語義保全、未定義安全、纖維安全、來源單調與權限非提升；
- 提出 Agent、資料管線、API、工作流與科學計算應用；
- 建立評估指標、基準測試、可否證條件與五階段實作路線。

---

**文件結束**
