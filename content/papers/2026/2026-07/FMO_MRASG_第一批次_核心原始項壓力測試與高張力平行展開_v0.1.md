# FMO–MRASG 第一研究批次

## 核心原始項壓力測試與高張力節點平行展開

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

本批次不沿用「一輪只處理一個問題」的線性方式，而將事實模態本體論的核心結構轉換為多解析度論證語義圖，先計算高張力節點，再對多個節點進行平行展開。

本批次的目標不是封閉整套理論，而是完成以下工作：

1. 建立事實模態本體論的第一版核心圖；
2. 區分核心節點、派生節點與模型節點；
3. 計算第一輪研究優先度；
4. 平行展開五個最高張力節點；
5. 保存未消解差異，不強制過早收斂；
6. 產生新版局部核心；
7. 形成下一批次的搜尋佇列。

本批次的方法循環為：

$$
\text{建圖}
\rightarrow
\text{張力評分}
\rightarrow
\text{平行展開}
\rightarrow
\text{跨節點對齊}
\rightarrow
\text{局部收斂}
\rightarrow
\text{更新研究佇列}
$$

---

# 1. 初始理論圖

## 1.1 圖定義

令目前事實模態本體論的研究圖為：

$$
\mathcal G_{\mathrm{FMO}}^{(0)}
=
\left(
V^{(0)},
E^{(0)},
S^{(0)},
R^{(0)},
M^{(0)}
\right)
$$

其中：

- $V^{(0)}$ ：理論節點；
- $E^{(0)}$ ：節點之間的依賴、支持、衝突與派生關係；
- $S^{(0)}$ ：既有正事實、反事實與六輪推論材料；
- $R^{(0)}$ ：點、線、面、體四級解析度；
- $M^{(0)}$ ：版本與生成紀錄。

---

## 1.2 初始核心節點

| 節點 ID | 名稱 | 類型 | 初始地位 |
|---|---|---|---|
| FMO-000 | 事實模態本體論 | root | 理論根節點 |
| FMO-101 | 結構載域 $\mathcal S_W$ | primitive-candidate | 候選原始項 |
| FMO-102 | 約束系統 $\Gamma_W$ | primitive-candidate | 候選原始項 |
| FMO-103 | 世界實際性 $\mathsf A_W$ | primitive-candidate | 候選原始項 |
| FMO-104 | 實際性制度 $\Theta_A$ | primitive-candidate | 候選原始項 |
| FMO-201 | 合法歷史空間 $\Pi$ | derived | 由 $\mathcal S_W,\Gamma_W$ 派生 |
| FMO-202 | 存在者與同一性 | derived-candidate | 由連續性規則派生 |
| FMO-203 | 正事實圖 $\mathbb F^+$ | derived | 由世界實現與索引派生 |
| FMO-204 | 可能本體空間 $\Omega$ | derived-candidate | 尚未完成生成規則 |
| FMO-205 | 反事實干預 $\Delta$ | operator | 待建立型別系統 |
| FMO-206 | 耦合 $\mathcal C$ | derived | 由約束依賴派生 |
| FMO-207 | 張力 $\mathcal T$ | derived-candidate | 暫定為最小重寫成本 |
| FMO-208 | 本體邊界 $\mathcal B$ | derived-candidate | 暫定由不變量派生 |
| FMO-209 | 可達性 $\mathcal R$ | derived | 由合法重寫路徑派生 |
| FMO-301 | 模型實際性 $\mathsf A^M$ | epistemic | 模型層 |
| FMO-302 | 認識實際性 $\mathsf A^K$ | epistemic | 主體判定層 |
| FMO-303 | 衝突分類 $\Xi$ | diagnostic | 模型診斷層 |
| FMO-304 | 多層一致性 $\mathbf{Con}$ | diagnostic | 向量化一致性 |
| FMO-305 | 模型更新 $\mathcal U_M$ | epistemic | 與世界更新分離 |
| FMO-306 | 世界更新 $\mathcal U_W$ | ontic | 世界歷史變化 |

---

## 1.3 初始主要依賴邊

```text
FMO-101 結構載域
    ├─ enables → FMO-201 合法歷史
    ├─ participates_in → FMO-202 同一性
    └─ grounds → FMO-203 正事實圖

FMO-102 約束系統
    ├─ generates → FMO-201 合法歷史
    ├─ induces → FMO-206 耦合
    ├─ constrains → FMO-205 反事實干預
    └─ participates_in → FMO-202 同一性

FMO-103 世界實際性
    ├─ selects_or_realizes → FMO-203 正事實圖
    └─ contrasts_with → FMO-301 模型實際性

FMO-104 實際性制度
    ├─ constrains → FMO-103 世界實際性
    └─ determines → 單一路徑／分支／多層實際性

FMO-205 反事實干預
    ├─ propagates_through → FMO-206 耦合
    ├─ incurs → FMO-207 張力
    ├─ may_cross → FMO-208 本體邊界
    └─ determines → FMO-209 可達性

FMO-303 衝突分類
    ├─ evaluates → FMO-203 正事實圖
    └─ contributes_to → FMO-304 多層一致性
```

---

# 2. 第一輪張力評分

## 2.1 評分函數

對任一研究節點 $v$ ，定義研究優先度：

$$
P(v)
=
0.30T(v)
+
0.25I(v)
+
0.20U(v)
+
0.10B(v)
+
0.10N(v)
-
0.05C(v)
$$

其中各項以 $0$ 至 $5$ 評分：

- $T(v)$ ：理論張力；
- $I(v)$ ：對整體理論的影響度；
- $U(v)$ ：未解程度；
- $B(v)$ ：跨分支橋接價值；
- $N(v)$ ：新推論潛力；
- $C(v)$ ：展開成本。

此分數不是客觀真理值，而是研究導航值。

---

## 2.2 初始評分表

| 排名 | 節點 | $T$ | $I$ | $U$ | $B$ | $N$ | $C$ | $P(v)$ |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 世界實際性是否可約化 | 5 | 5 | 5 | 5 | 4 | 4 | 4.45 |
| 2 | 約束系統是否成為萬用黑箱 | 5 | 5 | 4 | 4 | 4 | 3 | 4.20 |
| 3 | 本體張力成本是否任意 | 4 | 4 | 5 | 5 | 5 | 4 | 4.05 |
| 4 | 同一性是否真的可由約束派生 | 4 | 5 | 4 | 4 | 4 | 3 | 3.90 |
| 5 | 局部矛盾應採何種推理語義 | 4 | 4 | 4 | 4 | 4 | 3 | 3.75 |
| 6 | 可能空間是否能由實際根完整生成 | 4 | 4 | 5 | 4 | 4 | 4 | 3.80 |
| 7 | 本體邊界是否能由不變量充分定義 | 4 | 4 | 4 | 4 | 4 | 4 | 3.70 |
| 8 | 反事實干預的合法型別 | 3 | 5 | 4 | 4 | 4 | 4 | 3.65 |

本批次選擇前五個節點平行展開。第六節點「可能空間生成」雖分數略高於第五節點，但局部矛盾語義會直接影響整個圖的資料保存方式，因此被人工提升進入本批次。

此處保留一項方法論紀錄：

> 張力函數提供導航，但研究者仍可基於結構依賴調整批次順序。調整必須被記錄，而不能偽裝成純粹由公式自動產生。

---

# 3. 高張力節點 A：世界實際性是否可約化

## A-R0：點層

> 若兩條合法歷史在結構上完全不可區分，單靠結構與約束無法指出哪一條真正實現；因此世界實際性不能被普通結構性質完全約化。

---

## A-R1：線層

目前世界核心包含：

$$
\mathfrak W^+
=
\left\langle
\mathcal S_W,
\Gamma_W,
\mathsf A_W,
\Theta_A
\right\rangle
$$

問題在於：

$$
\mathsf A_W
$$

究竟是必要原始項，還是可以從：

$$
\mathcal S_W,\Gamma_W
$$

導出。

若存在兩條歷史：

$$
\pi_1,\pi_2\in\Pi_{\mathcal S,\Gamma}
$$

且它們對所有結構述詞都不可區分：

$$
\pi_1
\equiv_{\mathcal S,\Gamma}
\pi_2
$$

那麼任何只使用 $\mathcal S,\Gamma$ 的定義，都不能選出其中一條為實際。

因此至少需要：

1. 世界實現關係；
2. 實際根索引；
3. 或把實際世界當成理論起點，而不是從可能集合中被選出的元素。

---

## A-R2：面層

### A1. 結構可定義論

主張：

$$
\mathsf A_W(\pi)
\iff
P_{\mathcal S,\Gamma}(\pi)
$$

即實際性可以由某個結構性質 $P$ 定義。

問題是，如果存在保持全部結構的自同構：

$$
g:
\Pi\rightarrow\Pi
$$

使得：

$$
g(\pi_1)=\pi_2
$$

且：

$$
g
$$

保持所有 $\mathcal S,\Gamma$ 可表示關係，則任何結構性述詞都無法區分 $\pi_1$ 與 $\pi_2$ 。

所以：

$$
P_{\mathcal S,\Gamma}(\pi_1)
=
P_{\mathcal S,\Gamma}(\pi_2)
$$

若其中只有一條實際，結構性定義便失敗。

---

### A2. 外部選擇算子論

可以保留：

$$
\mathsf A:
\Pi\rightarrow\pi^+
$$

但「選擇」容易使實際性看起來像模型或研究者的操作。

這會混淆：

$$
\mathsf A_W
$$

與：

$$
\mathsf A^M
$$

世界不是等待模型從可能集合中挑選一條路徑。

---

### A3. 實際根論

另一種處理方式是：

> 實際世界不是可能世界集合中的普通成員，而是模態建構的根。

先給定：

$$
\mathfrak W^+
$$

再由它生成可能空間：

$$
\Omega(\mathfrak W^+)
=
\left\{
O_\Delta
\mid
\Delta\in\mathcal D
\right\}
$$

此時，實際性不是「從對稱集合中選出一條」，而是所有反事實生成的基準。

在模型語義中，可以使用有根模型：

$$
\mathfrak M
=
\left\langle
\mathbf O,
\mathcal R,
@
\right\rangle
$$

其中 $@$ 是模型中的實際根標記。

但仍要區分：

$$
@_M
$$

與世界真正的實現關係。

---

## A-張力分類

| 分支 | 優點 | 問題 |
|---|---|---|
| 結構可定義論 | 核心最小化 | 無法打破結構對稱 |
| 外部選擇算子論 | 形式簡單 | 容易把世界實際性模型化 |
| 實際根論 | 符合正事實作為反事實基準 | 仍保留不可約的根指示 |

---

## A-局部決定

本批次暫時採用：

$$
\boxed{
\text{世界實際性不是普通性質，而是不可約的實現錨定關係}
}
$$

並將符號從容易引起「選擇」聯想的：

$$
\mathsf A_W
$$

改寫為：

$$
\mathsf{Real}_W
$$

世界核心暫改為：

$$
\boxed{
\mathfrak W^+
=
\left\langle
\mathcal S_W,
\Gamma_W,
\mathsf{Real}_W,
\Theta_A
\right\rangle
}
$$

模型層則使用：

$$
@_M
$$

作為模型中的實際根。

二者的對應條件為：

$$
\operatorname{Adeq}(M,W)
\Rightarrow
@_M
\simeq
\mathsf{Real}_W
$$

但任何模型都不能僅由自身保證其充分對應世界。

---

## A-新增節點

```text
FMO-103A  世界實現錨定關係 Real_W
FMO-103B  模型實際根 @M
FMO-103C  結構對稱不可區分命題
FMO-103D  實際根生成可能空間命題
```

---

# 4. 高張力節點 B：約束系統是否成為萬用黑箱

## B-R0：點層

> 若所有未解問題都被塞進 $\Gamma$ ，約束系統會變成無法分析的萬用容器；因此 $\Gamma$ 必須是具型別、作用域、優先序與可追溯來源的約束代數。

---

## B-R1：線層

目前：

$$
\Gamma_W
$$

承擔：

- 邏輯合法性；
- 結構構成；
- 動態轉換；
- 歷史限制；
- 同一性；
- 制度規範。

這使它極其強大，但也可能導致：

> 任何理論困難都被回答成「因為約束如此」。

如果 $\Gamma$ 沒有內部結構，理論將失去解釋力與可計算性。

---

## B-R2：面層

### B1. 約束的型別

單一約束記為：

$$
\gamma
=
\left\langle
\tau,
\operatorname{scope},
\operatorname{trigger},
\operatorname{condition},
\operatorname{effect},
\operatorname{priority},
\operatorname{source}
\right\rangle
$$

其中：

- $\tau$ ：約束型別；
- $\operatorname{scope}$ ：作用域；
- $\operatorname{trigger}$ ：啟動條件；
- $\operatorname{condition}$ ：需要滿足的條件；
- $\operatorname{effect}$ ：允許、禁止、要求或轉換；
- $\operatorname{priority}$ ：衝突時優先序；
- $\operatorname{source}$ ：來源與構成依據。

---

### B2. 約束家族

將 $\Gamma$ 改寫為型別化家族：

$$
\Gamma^\tau
=
\left\{
\Gamma_L,
\Gamma_C,
\Gamma_D,
\Gamma_H,
\Gamma_I,
\Gamma_N,
\Gamma_M
\right\}
$$

其中新增：

- $\Gamma_H$ ：跨時間歷史約束；
- $\Gamma_M$ ：約束自身的元約束。

$\Gamma_M$ 規定：

- 約束如何生效；
- 約束何時衝突；
- 優先序如何比較；
- 約束是否可局部修復；
- 哪些約束屬於核心；
- 哪些約束可以被反事實干預。

---

### B3. 防止黑箱化的四項要求

#### 可定位性

任何非法狀態都應能返回違反的約束集合：

$$
\operatorname{Violation}(s,\Gamma)
=
\left\{
\gamma_i
\mid
s\not\models\gamma_i
\right\}
$$

#### 可追溯性

每項約束應保存其來源：

$$
\operatorname{Prov}(\gamma_i)
$$

#### 可分解性

約束衝突應能定位到局部子集合：

$$
\Gamma'
\subseteq\Gamma
$$

而不是把整個系統標為失敗。

#### 可干預性

應區分：

$$
\Delta_s
$$

狀態干預；

$$
\Delta_\gamma
$$

約束干預；

$$
\Delta_{\Gamma_M}
$$

元約束干預。

三者產生的本體後果不同。

---

## B-局部決定

約束系統仍保留在核心，但不再視為單一未分析原始物。

新版形式為：

$$
\boxed{
\Gamma_W^\tau
=
\left\langle
\Gamma_L,
\Gamma_C,
\Gamma_D,
\Gamma_H,
\Gamma_I,
\Gamma_N,
\Gamma_M
\right\rangle
}
$$

其中每項約束都必須具有：

$$
\operatorname{type},
\operatorname{scope},
\operatorname{priority},
\operatorname{provenance}
$$

因此，原始項不是「一個裝著所有規則的箱子」，而是：

> 一套具有內部型別與運算規則的約束代數。

---

## B-新增節點

```text
FMO-102A  型別化約束代數 Γτ
FMO-102B  元約束 ΓM
FMO-102C  約束違反定位
FMO-102D  約束來源追溯
FMO-102E  狀態干預／約束干預／元約束干預
```

---

# 5. 高張力節點 C：本體張力成本是否任意

## C-R0：點層

> 本體張力不應先被壓成單一數值；更穩健的形式是多維重寫成本向量，單一標量只是在特定任務下的投影。

---

## C-R1：線層

原先定義：

$$
\mathcal T(O_i,O_j)
=
\inf_{\eta:O_i\Rightarrow O_j}
\sum_{e\in\eta}c(e)
$$

問題在於：

$$
c(e)
$$

由誰決定？

若不同研究者可任意設定成本，則同一對本體之間的張力可以被任意調整。

---

## C-R2：面層

### C1. 單一標量的問題

從 $O_i$ 到 $O_j$ 的改寫可能同時涉及：

- 結構節點變化；
- 關係變化；
- 約束變化；
- 同一性規則變化；
- 制度規則變化；
- 歷史重寫；
- 證據與模型重建。

將所有變化立即壓成單一數字會遺失差異。

---

### C2. 張力向量

定義：

$$
\vec{\mathcal T}(O_i,O_j)
=
\left\langle
T_S,
T_R,
T_C,
T_D,
T_I,
T_N,
T_H,
T_E
\right\rangle
$$

其中：

- $T_S$ ：結構載域修改；
- $T_R$ ：關係修改；
- $T_C$ ：構成規則修改；
- $T_D$ ：動力規則修改；
- $T_I$ ：同一性規則修改；
- $T_N$ ：制度與規範修改；
- $T_H$ ：歷史重寫成本；
- $T_E$ ：認識與證據重建成本。

---

### C3. 偏序比較

兩個改寫方案 $\eta_1,\eta_2$ 不必總能被單一排序。

若：

$$
\vec{\mathcal T}(\eta_1)
\preceq
\vec{\mathcal T}(\eta_2)
$$

表示 $\eta_1$ 在所有維度不高於 $\eta_2$ ，且至少一維更低，則 $\eta_1$ 支配 $\eta_2$ 。

若兩者各有高低，則它們可能不可比較。

因此本體張力首先形成：

$$
\text{Pareto 前沿}
$$

而不是唯一最小值。

---

### C4. 任務投影

只有在特定研究任務中，才選擇權重：

$$
\omega
=
\left\langle
w_S,w_R,w_C,w_D,w_I,w_N,w_H,w_E
\right\rangle
$$

並定義：

$$
\mathcal T_\omega
=
\omega\cdot
\vec{\mathcal T}
$$

因此：

$$
\mathcal T_\omega
$$

是任務相對張力，不是宇宙唯一張力。

---

### C5. 成本函數最低要求

任何可接受成本系統至少應滿足：

#### 非負性

$$
c(e)\geq 0
$$

#### 同一性

$$
\mathcal T(O,O)=0
$$

#### 串接次可加性

$$
\mathcal T(O_1,O_3)
\leq
\mathcal T(O_1,O_2)
+
\mathcal T(O_2,O_3)
$$

#### 表示不變性

若兩個圖只是不同編碼，但本體結構等價：

$$
O\simeq O'
$$

則不應因表示格式不同產生巨大張力：

$$
\vec{\mathcal T}(O_1,O_2)
\simeq
\vec{\mathcal T}(O_1',O_2')
$$

#### 局部可分解性

若兩項修改互不耦合，其成本可以局部組合。

---

## C-局部決定

將原先單一張力改為：

$$
\boxed{
\vec{\mathcal T}
:
O_i\times O_j
\rightarrow
\mathbb R_{\geq 0}^{\,8}
}
$$

單一數值只保留為任務投影：

$$
\boxed{
\mathcal T_\omega
=
\omega\cdot
\vec{\mathcal T}
}
$$

此決定不消除成本校準問題，但避免把任意權重偽裝成唯一客觀距離。

---

## C-新增節點

```text
FMO-207A  多維本體張力向量
FMO-207B  張力偏序與 Pareto 前沿
FMO-207C  任務相對投影 Tω
FMO-207D  表示不變性要求
FMO-207E  基本成本公理
```

---

# 6. 高張力節點 D：同一性是否真的可由約束派生

## D-R0：點層

> 同一性不能只靠性質相似或不變量相同建立；它需要跨歷史的連續性見證，而不同本體可以承認不同類型的連續性見證。

---

## D-R1：線層

原先存在者被表示為：

$$
e=[x]_{\sim_O}
$$

問題是：

$$
\sim_O
$$

從哪裡來？

若只用不變量判定同一性，會遇到：

- 完全相同的複製體；
- 狀態完全恢復但歷史中斷；
- 性質大幅改變但仍被視為同一人；
- 法律身份延續但物理載體替換。

所以同一性既不能等於性質相同，也不能等於單一物理連續。

---

## D-R2：面層

### D1. 相似性不等於同一性

即使：

$$
\forall p,\quad
p(x)=p(y)
$$

也不能推出：

$$
x=y
$$

完全相同的複製體可能仍是兩個存在者。

---

### D2. 狀態恢復不等於歷史同一

若：

$$
\operatorname{State}(x_t)
=
\operatorname{State}(x_{t'})
$$

仍不能推出：

$$
\operatorname{Id}(x_t)
=
\operatorname{Id}(x_{t'})
$$

因為中間可能發生：

- 中斷；
- 複製；
- 分支；
- 刪除後重建；
- 權利轉移；
- 記憶拼接。

---

### D3. 連續性見證

定義連續性見證集合：

$$
\mathsf{CW}
\left(
x_t,
x_{t'},
\pi,
\Gamma_I
\right)
$$

其中的見證可包括：

- $\omega_P$ ：物理連續；
- $\omega_C$ ：因果連續；
- $\omega_M$ ：記憶連續；
- $\omega_G$ ：目標與意圖連續；
- $\omega_L$ ：法律繼承；
- $\omega_S$ ：社會承認；
- $\omega_D$ ：數位狀態連續；
- $\omega_B$ ：分支繼承。

因此：

$$
x_t
\sim_{O,\tau}
x_{t'}
$$

當且僅當存在符合本體 $O$ 的類型 $\tau$ 連續性見證。

---

### D4. 同一性輪廓

不同本體可能使用多個見證共同判定。

可定義同一性輪廓：

$$
\mathbf I_O(x_t,x_{t'})
=
\left\langle
I_P,
I_C,
I_M,
I_G,
I_L,
I_S,
I_D,
I_B
\right\rangle
$$

再由本體規則：

$$
\Gamma_I
$$

決定哪些輪廓足以構成同一性。

例如：

$$
\Gamma_I^{(1)}
:
I_P\land I_C
\Rightarrow
\operatorname{Same}
$$

另一個本體則可能使用：

$$
\Gamma_I^{(2)}
:
I_M\land I_G\land I_D
\Rightarrow
\operatorname{Same}
$$

---

### D5. 分支後同一性

若一個主體分裂為：

$$
x\rightarrow x_1,x_2
$$

可能出現：

1. 兩者都延續原主體；
2. 兩者都不是原主體；
3. 只有一者延續；
4. 原本的「單一同一性」概念在此失效。

因此同一性未必在所有本體中形成普通等價關係。

尤其傳遞性可能失敗：

$$
x_1\sim x
$$

且：

$$
x_2\sim x
$$

不必推出：

$$
x_1\sim x_2
$$

---

## D-局部決定

同一性仍視為由約束系統派生，但不是單一等價關係。

改用：

$$
\boxed{
\mathbf I_O
+
\Gamma_I
\Rightarrow
\operatorname{IdJudgment}_O
}
$$

也就是：

> 先取得多維連續性見證，再由本體中的身份規則形成同一性判定。

「存在者」因此可能是：

- 等價類；
- 分支類；
- 有向歷史束；
- 法律繼承鏈；
- 多載體連續體。

不再預設所有存在者都可用同一種數學結構表示。

---

## D-新增節點

```text
FMO-202A  連續性見證集合 CW
FMO-202B  同一性輪廓 I⃗
FMO-202C  分支後非傳遞同一性
FMO-202D  身份判定規則 ΓI
FMO-202E  存在者表示型態多元性
```

---

# 7. 高張力節點 E：局部矛盾應採何種推理語義

## E-R0：點層

> 模型可以同時保存 $F$ 與 $\neg F$ ，但衝突只能沿明確依賴邊傳播；世界矛盾不能由資料矛盾直接推出。

---

## E-R1：線層

事實模態模型需要保存：

- 互相衝突的來源；
- 未決事實；
- 過時紀錄；
- 不同制度判定；
- 不同尺度結果。

若採經典爆炸：

$$
F,\neg F\vdash G
$$

則局部資料衝突會使整個系統失效。

因此需要非爆炸推理。

---

## E-R2：面層

### E1. 四種模型狀態

對任一命題 $F$ ，模型狀態可表示為：

$$
\nu_M(F)
\in
\{
\mathbf T,
\mathbf F,
\mathbf B,
\mathbf N
\}
$$

其中：

- $\mathbf T$ ：只有支持 $F$ ；
- $\mathbf F$ ：只有支持 $\neg F$ ；
- $\mathbf B$ ：同時支持 $F$ 與 $\neg F$ ；
- $\mathbf N$ ：兩者皆無充分支持。

注意：

$$
\mathbf B
$$

表示模型或證據層衝突，不直接表示世界矛盾。

---

### E2. 來源標註

每項判定應附帶來源集合：

$$
\nu_M(F)
=
\left\langle
v,
D_F,
D_{\neg F}
\right\rangle
$$

其中：

- $D_F$ ：支持 $F$ 的來源；
- $D_{\neg F}$ ：支持 $\neg F$ 的來源。

這使衝突可追溯，而不只是儲存一個抽象的「both」。

---

### E3. 相關性限制

由 $F$ 與 $\neg F$ 不得推出任意 $G$ 。

只有當圖中存在相關依賴路徑：

$$
F
\xrightarrow{\operatorname{depends}}
G
$$

或：

$$
\neg F
\xrightarrow{\operatorname{depends}}
G
$$

衝突才可能影響 $G$ 。

可寫成：

$$
F,\neg F
\nvdash
G
$$

若：

$$
G
\notin
\operatorname{Cl}_{\mathcal C}
\left(
\{F,\neg F\}
\right)
$$

---

### E4. 衝突與世界矛盾分離

模型可能有：

$$
\nu_M(F)=\mathbf B
$$

但世界層仍可能只有：

$$
\mathsf{Real}_W(F)=1
$$

或：

$$
\mathsf{Real}_W(\neg F)=1
$$

只是模型尚無法判定。

因此：

$$
\operatorname{ModelContr}(F)
\not\Rightarrow
\operatorname{WorldContr}(F)
$$

---

### E5. 衝突保留與局部修復

系統可以保留：

```text
F
├─ supported_by → D1
├─ supported_by → D2
└─ conflicts_with
    ¬F
    ├─ supported_by → D3
    └─ supported_by → D4
```

而不是立即刪除一方。

只有在完成：

- 指涉對齊；
- 時間對齊；
- 尺度對齊；
- 制度對齊；
- 來源評估；

之後，才進入修復。

---

## E-局部決定

模型層暫採：

$$
\boxed{
\nu_4
:
F
\rightarrow
\{
\mathbf T,
\mathbf F,
\mathbf B,
\mathbf N
\}
}
$$

並加入：

$$
\boxed{
\text{來源標註}
+
\text{圖相關性限制}
+
\text{局部衝突閉包}
}
$$

此處只決定語義骨架，尚未決定完整證明系統。

---

## E-新增節點

```text
FMO-303A  四值模型狀態 ν4
FMO-303B  衝突來源標註
FMO-303C  圖相關性推理限制
FMO-303D  模型矛盾／世界矛盾分離
FMO-303E  局部衝突閉包
```

---

# 8. 跨節點對齊

本批次五個節點不是獨立問題。

它們形成以下依賴：

```text
Real_W 世界實現錨定
    └─ grounds → 正事實

Γτ 型別化約束代數
    ├─ generates → 合法歷史
    ├─ defines → 身份規則 ΓI
    ├─ induces → 耦合
    └─ constrains → 合法干預

身份輪廓 I⃗
    └─ combined_with ΓI → 同一性判定

張力向量 T⃗
    ├─ evaluates → 本體重寫
    └─ cannot replace → 合法性判定

四值模型語義 ν4
    ├─ stores → 證據衝突
    ├─ does_not_define → 世界實際性
    └─ guides → 模型修復
```

---

## 8.1 第一個重要分離

$$
\mathsf{Real}_W
\neq
\nu_4
$$

世界實現關係不等於模型對命題的四值判定。

---

## 8.2 第二個重要分離

$$
\Gamma^\tau
\neq
\vec{\mathcal T}
$$

約束決定什麼合法；張力描述合法重寫需要付出什麼代價。

高成本不表示不合法，低成本也不表示真實。

---

## 8.3 第三個重要分離

$$
\mathbf I_O
\neq
\operatorname{Same}_O
$$

同一性輪廓只是連續性證據，最終身份判定仍依賴：

$$
\Gamma_I
$$

---

## 8.4 第四個重要分離

$$
\operatorname{Conflict}
\neq
\operatorname{WorldContr}
$$

四值語義保存的是模型狀態，不是直接宣告世界包含矛盾。

---

# 9. 本批次後的局部核心

經過本批次，世界核心暫更新為：

$$
\boxed{
\mathfrak W_1^+
=
\left\langle
\mathcal S_W,
\Gamma_W^\tau,
\mathsf{Real}_W,
\Theta_A
\right\rangle
}
$$

其中：

$$
\Gamma_W^\tau
=
\left\langle
\Gamma_L,
\Gamma_C,
\Gamma_D,
\Gamma_H,
\Gamma_I,
\Gamma_N,
\Gamma_M
\right\rangle
$$

模型核心暫更新為：

$$
\boxed{
\mathfrak M_1
=
\left\langle
\widehat{\mathcal S},
\widehat{\Gamma}^{\tau},
@_M,
\nu_4,
\mathcal E,
\mathcal U_M
\right\rangle
}
$$

---

## 9.1 主要派生結構

合法歷史：

$$
\Pi
=
\left\{
\pi
\mid
\pi\models\Gamma^\tau
\right\}
$$

同一性：

$$
\mathbf I_O
+
\Gamma_I
\Rightarrow
\operatorname{IdJudgment}_O
$$

正事實：

$$
F^+
\iff
\mathsf{Real}_W
\left(
\langle\varphi,O,t,\sigma,\beta,\ell\rangle
\right)
$$

耦合：

$$
\mathcal C
=
\operatorname{Dep}
\left(
\Gamma^\tau
\right)
$$

張力：

$$
\vec{\mathcal T}
:
O_i\times O_j
\rightarrow
\mathbb R_{\geq0}^{\,8}
$$

任務投影：

$$
\mathcal T_\omega
=
\omega\cdot
\vec{\mathcal T}
$$

模型衝突狀態：

$$
\nu_4(F)
\in
\{
\mathbf T,
\mathbf F,
\mathbf B,
\mathbf N
\}
$$

---

# 10. 本批次沒有解決的問題

本批次刻意保留以下張力。

## 10.1 世界實現錨定仍是原始項

雖然已證明它難以由純結構定義，但尚未證明：

$$
\mathsf{Real}_W
$$

是唯一可接受處理。

---

## 10.2 型別化約束代數仍可能過強

即使 $\Gamma$ 已分解，仍需證明：

- 元約束不會無限回歸；
- 約束型別是否完備；
- 約束衝突如何正式處理。

---

## 10.3 張力向量仍需要基本編輯語言

若「一次修改」的粒度不同，成本仍可能失真。

因此需要建立：

$$
\mathcal E_{\mathrm{edit}}
$$

即本體重寫的原始編輯操作集合。

---

## 10.4 同一性判定可能不是二值

某些分支與複製案例可能需要：

- 部分延續；
- 多重延續；
- 不可比較；
- 身份概念失效。

---

## 10.5 四值語義尚未處理模糊性

$\mathbf T,\mathbf F,\mathbf B,\mathbf N$ 處理支持與反對狀態，但未直接處理：

- 連續真值；
- 邊界模糊；
- 機率；
- 可信度。

這些不應被草率混入同一維度。

---

# 11. 更新後的研究佇列

根據本批次的新張力，下一批候選節點為：

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 可能空間如何由實際根生成 | 決定反事實是否完整 |
| 2 | 反事實干預的正式型別系統 | 決定何種改寫合法 |
| 3 | 本體原始編輯語言 | 決定張力成本是否可比較 |
| 4 | 元約束是否導致無限回歸 | 威脅核心架構 |
| 5 | 分支同一性的非等價關係模型 | 影響主體、人格與責任 |
| 6 | 四值語義與模糊／機率的分離 | 影響模型判定 |
| 7 | 本體邊界的不變量充分性 | 仍未經壓力測試 |
| 8 | 世界矛盾是否具有可判定條件 | 高風險但較後置 |

---

# 12. 圖更新摘要

## 12.1 新增節點數

本批次新增：

$$
4+5+5+5+5=24
$$

個子節點。

---

## 12.2 新增主要關係

新增關係類型包括：

```text
grounds
anchors
structurally_indistinguishable
typed_constraint
meta_constrains
violates
has_provenance
projects_to
dominates
has_continuity_witness
identity_judged_by
annotated_true
annotated_false
locally_conflicts
propagates_if_relevant
```

---

## 12.3 已形成的穩定區

目前局部穩定的結論：

1. 世界實際性不能與模型標記混同；
2. 約束系統必須型別化；
3. 張力首先是向量，不是唯一標量；
4. 同一性需要歷史連續性見證；
5. 模型衝突不應導致全面爆炸；
6. 世界矛盾不能由資料衝突直接推出。

---

## 12.4 仍屬高張力區

1. 實際性是否真正不可約；
2. 元約束如何停止；
3. 本體編輯的最小原語；
4. 分支身份是否仍可稱為同一性；
5. 可能空間是否能從實際根完整生成。

---

# 13. 本批次結論

第一批 FMO–MRASG 研究沒有繼續寫第七篇線性推論，而是把既有理論轉換為可搜索的研究圖。

本批次取得五項實質修正。

第一，將世界實際性由「選擇算子」改為：

$$
\mathsf{Real}_W
$$

即世界實現錨定關係。

第二，將約束系統改為：

$$
\Gamma_W^\tau
$$

即具有型別、作用域、優先序、來源與元約束的約束代數。

第三，將本體張力改為：

$$
\vec{\mathcal T}
$$

即多維重寫成本向量；單一張力只是在任務權重下的投影。

第四，將同一性改為：

$$
\mathbf I_O+\Gamma_I
\Rightarrow
\operatorname{IdJudgment}_O
$$

即多維連續性見證與身份規則共同生成的判定。

第五，將模型衝突改為四值、可追溯、局部非爆炸的圖狀態：

$$
\nu_4(F)
\in
\{
\mathbf T,
\mathbf F,
\mathbf B,
\mathbf N
\}
$$

因此，本批次後的核心不再只是概念列表，而形成了更清楚的依賴方向：

$$
\boxed{
\mathcal S_W
+
\Gamma_W^\tau
+
\mathsf{Real}_W
+
\Theta_A
\rightarrow
\Pi
\rightarrow
\mathbb F^+
\rightarrow
\Delta
\rightarrow
\mathcal C
\rightarrow
\vec{\mathcal T}
\rightarrow
\mathcal B
}
$$

模型則透過：

$$
\boxed{
\widehat{\mathcal S}
+
\widehat{\Gamma}^{\tau}
+
@_M
+
\nu_4
+
\mathcal E
+
\mathcal U_M
}
$$

追蹤世界，但不等同於世界。

本批次已完成第一次真正的「圖更新」，而不是第七輪單線推論。

---

## 附錄 A：本批次最小 JSON 示意

```json
{
  "batch": "FMO-MRASG-001",
  "version": "0.1",
  "selected_nodes": [
    "FMO-103",
    "FMO-102",
    "FMO-207",
    "FMO-202",
    "FMO-303"
  ],
  "decisions": [
    {
      "node": "FMO-103",
      "result": "replace_selector_with_realization_anchor",
      "new_symbol": "Real_W"
    },
    {
      "node": "FMO-102",
      "result": "typed_constraint_algebra",
      "new_symbol": "Gamma_W_tau"
    },
    {
      "node": "FMO-207",
      "result": "vector_tension",
      "new_symbol": "T_vector"
    },
    {
      "node": "FMO-202",
      "result": "identity_profile_plus_rules"
    },
    {
      "node": "FMO-303",
      "result": "four_valued_local_non_explosive_model_semantics"
    }
  ],
  "next_queue": [
    "possibility_generation",
    "intervention_type_system",
    "primitive_edit_language",
    "meta_constraint_regress",
    "branch_identity"
  ]
}
```

---

## 附錄 B：版本狀態

**輸入圖：**

$$
\mathcal G_{\mathrm{FMO}}^{(0)}
$$

**輸出圖：**

$$
\mathcal G_{\mathrm{FMO}}^{(1)}
$$

**批次狀態：** 已完成  
**理論狀態：** 局部收斂／整體開放  
**下一步：** 第二批高張力搜尋與平行展開  
