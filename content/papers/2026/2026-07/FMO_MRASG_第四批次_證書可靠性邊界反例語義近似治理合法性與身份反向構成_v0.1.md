# FMO–MRASG 第四研究批次

## 證書可靠性、邊界反例、語義近似、治理合法性與身份反向構成

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

第三批次完成了五項核心分離：

$$
\Diamond_M
\neq
\Diamond_W
$$

$$
\operatorname{SameInvariant}
\not\Rightarrow
\operatorname{SameOntology}
$$

$$
\vec{\mathcal T}_{\mathrm{sem}}
\neq
\vec{\mathcal T}_{\mathrm{rep}}
$$

$$
\operatorname{MetaStable}
\neq
\operatorname{UniqueFixedPoint}
$$

以及：

$$
\mathbf c_I
\neq
q_I
\neq
J_I
\neq
\mathbf r_I
$$

然而，這些分離仍依賴若干尚未驗證的「證書」與「判定機制」。

例如：

- 可能性見證本身可能是假的；
- 不可能性證書可能依賴錯誤核心公理；
- 邊界證書可能遺漏不可見斷裂；
- 語義等價可能不可判定；
- 多固定點的選擇可能被權力劫持；
- 制度身份可能反向塑造人們對存在者本身的理解。

因此，本批次選取以下五個節點：

```text
FMO-213  可能性見證與不可能性證書的可靠性
FMO-214  本體邊界證書的反例壓力測試
FMO-215  語義等價不可判定時的近似策略
FMO-216  多固定點治理與選擇合法性
FMO-217  制度對身份分類的反向構成
```

本批次的核心問題是：

> 當理論開始依賴證書、近似與治理程序時，如何防止模型把自己的判定機制偽裝成世界真理？

---

# 1. 輸入圖

第三批次輸出：

$$
\mathcal G_{\mathrm{FMO}}^{(3)}
$$

目前主要結構包括：

世界可能性包絡：

$$
\Omega_M^-
\subseteq
\Omega_W
\subseteq
\Omega_M^+
$$

路徑化本體邊界：

$$
\mathcal B_\eta(O)
=
\left\{
O'
\mid
\operatorname{BCert}(O,O';\eta)
\right\}
$$

表示商上的語義張力：

$$
\widetilde{\mathcal T}
:
[P_1]\times[P_2]
\rightarrow
\mathbb R_{\geq 0}^{n}
$$

元穩定分類：

$$
\operatorname{MetaStatus}
\in
\{
\mathsf{UniqueStable},
\mathsf{MultiStable},
\mathsf{Periodic},
\mathsf{BoundedDynamic},
\mathsf{Divergent},
\mathsf{Undetermined}
\}
$$

身份延續標籤：

$$
\Lambda_I(e)
=
\left\langle
\mathbf c_I,
q_I,
J_I,
\mathbf r_I,
t,
source
\right\rangle
$$

---

# 2. 節點 A：可能性見證與不可能性證書的可靠性

## A-R0：點層

> 證書只能相對於其公理、測量與翻譯條件成立；任何可能性或不可能性證書都必須附帶依賴、適用域、反駁條件與校準紀錄。

---

## A-R1：線層

第三批次使用：

$$
w_P(O')
$$

表示可能性見證；

以及：

$$
c_\bot(O')
$$

表示不可能性證書。

但證書的存在不等於證書可靠。

例如：

- 實驗可能測量錯誤；
- 構造可能只在模型內成立；
- 形式證明可能依賴錯誤公理；
- 跨模型收斂可能只是共同偏誤；
- 不可能性證明可能只證明「在目前語言內不可表達」。

因此需要將證書本身變成可被審查的結構。

---

## A-R2：面層

### A1. 證書描述子

定義一般證書：

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

其中：

- $claim$ ：證書要支持的命題；
- $base$ ：使用的公理、資料或世界實例；
- $method$ ：證明、實驗、模擬或構造方式；
- $scope$ ：適用範圍；
- $assumptions$ ：未被證書內部證明的假設；
- $provenance$ ：來源與生成歷史；
- $confidence$ ：認識層信心；
- $falsifier$ ：可使證書失效的條件；
- $version$ ：證書版本。

---

### A2. 可能性見證的類型

可能性見證至少分為：

#### 實現見證

世界中已有實例：

$$
w_{\mathrm{real}}
$$

這是最強見證之一，但仍需確認案例與候選本體是否真正同型。

#### 構造見證

存在明確構造：

$$
w_{\mathrm{construct}}
$$

可從已知結構生成候選。

#### 動力見證

存在合法演化路徑：

$$
w_{\mathrm{dyn}}
:
O^+
\leadsto
O'
$$

#### 模型見證

在形式模型中可滿足：

$$
w_{\mathrm{model}}
:
M\models O'
$$

但它只直接支持：

$$
\Diamond_M O'
$$

#### 跨模型收斂見證

多個獨立模型得到相同結果：

$$
w_{\mathrm{cross}}
$$

其可靠性取決於模型是否真正獨立。

---

### A3. 見證強度偏序

不能用單一分數將所有見證排序。

定義見證輪廓：

$$
\mathbf w(O')
=
\left\langle
w_R,
w_C,
w_D,
w_F,
w_X,
w_I
\right\rangle
$$

其中：

- $w_R$ ：實現程度；
- $w_C$ ：構造完整度；
- $w_D$ ：動力合法性；
- $w_F$ ：形式嚴格度；
- $w_X$ ：跨模型獨立性；
- $w_I$ ：適用域完整度。

見證之間採偏序比較，而非預設總排序。

---

### A4. 不可能性證書的類型

#### 型別不可能

$$
c_{\mathrm{type}}
$$

候選結構不符合語言或類型規則。

#### 約束不可滿足

$$
c_{\mathrm{unsat}}
$$

核心約束與候選結構無共同模型。

#### 動力不可達

$$
c_{\mathrm{dyn}}
$$

不存在合法轉換路徑。

#### 構成缺失

$$
c_{\mathrm{const}}
$$

候選本體缺少必要構成條件。

#### 語言內不可表達

$$
c_{\mathrm{lang}}
$$

目前表示語言無法形成候選。

其中只有部分證書真正支持世界不可能。

尤其：

$$
c_{\mathrm{lang}}
\not\Rightarrow
\neg\Diamond_W O'
$$

---

### A5. 證書依賴圖

任何證書都應展開成依賴圖：

$$
G_{\mathrm{Cert}}
=
(V_C,E_C)
$$

其中節點包括：

- 公理；
- 測量；
- 資料；
- 翻譯；
- 推理步驟；
- 軟體版本；
- 模型版本；
- 人工判定。

若某依賴失效，證書不應被永久保留為有效。

---

### A6. 證書反駁

定義：

$$
\operatorname{Defeat}(C,D)
$$

表示證書 $D$ 成功擊敗證書 $C$ 。

擊敗方式包括：

- 找到反例；
- 暴露錯誤假設；
- 發現來源不可靠；
- 顯示適用域錯置；
- 證明翻譯不保真；
- 發現循環依賴；
- 找到更強不相容證書。

---

### A7. 證書狀態

證書狀態不應只有有效／無效。

定義：

$$
\operatorname{CertStatus}
\in
\{
\mathsf{Valid},
\mathsf{Qualified},
\mathsf{Contested},
\mathsf{Defeated},
\mathsf{Expired},
\mathsf{Superseded},
\mathsf{Undetermined}
\}
$$

---

### A8. 可能包絡的更新

模型可能空間上下界應隨證書狀態更新。

若可能性見證被擊敗：

$$
O'
:
\Omega_M^-
\rightarrow
\Omega_M^{?}
$$

若取得可靠不可能性證書：

$$
O'
:
\Omega_M^{?}
\rightarrow
\Omega_M^\bot
$$

若不可能性證書被擊敗：

$$
O'
:
\Omega_M^\bot
\rightarrow
\Omega_M^{?}
$$

因此可能空間不是靜態集合，而是證書驅動的版本化結構。

---

## A-局部決定

可能性與不可能性證書改為：

$$
\boxed{
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
}
$$

任何證書都必須：

1. 顯示依賴；
2. 顯示適用域；
3. 顯示反駁條件；
4. 可被降級、撤銷或取代；
5. 不得把語言限制誤作世界不可能。

---

## A-新增節點

```text
FMO-213A  一般證書描述子
FMO-213B  可能性見證類型
FMO-213C  見證輪廓與偏序
FMO-213D  不可能性證書類型
FMO-213E  證書依賴圖
FMO-213F  證書擊敗關係
FMO-213G  證書多值狀態
FMO-213H  證書驅動可能包絡更新
```

---

# 3. 節點 B：本體邊界證書的反例壓力測試

## B-R0：點層

> 邊界證書仍可能被複製、重建、遺忘、緩慢漂移與不可逆中斷擊穿；因此證書必須加入斷裂測試、祖源測試與反事實回復測試。

---

## B-R1：線層

第三批次定義：

$$
\operatorname{BCert}
=
\operatorname{InvPres}
\land
\operatorname{GenCont}
\land
\operatorname{Recover}
\land
\operatorname{Trace}
$$

這比單純不變量更強，但仍可能產生假陽性。

本批次以極限反例測試：

- 完美複製；
- 中斷後重建；
- 忒修斯式漸進替換；
- 記憶消失；
- 分支再合併；
- 制度宣告同一；
- 功能等價但因果歷史不同。

---

## B-R2：面層

### B1. 完美複製反例

令：

$$
O
\rightarrow
O_1,O_2
$$

其中：

$$
O_1\simeq O_2
$$

且兩者保留同樣不變量與生成結構。

若只看端點，兩者都可能得到邊界證書。

但不能因此推出：

$$
O_1=O_2
$$

所以邊界證書需要區分：

- 類型連續；
- 個體祖源連續。

新增祖源條件：

$$
\operatorname{AncestryCont}(O,O';\eta)
$$

---

### B2. 中斷後完美重建

假設原本本體被完全刪除，後來根據備份重建：

$$
O
\rightarrow
\varnothing
\rightarrow
O'
$$

且：

$$
O'\simeq O
$$

不變量與可恢復映射都可能成立，但歷史中存在完全斷裂。

因此需要斷裂檢查：

$$
\operatorname{NoTerminalBreak}(\eta)
$$

若存在：

$$
t^\ast
$$

使核心生成與身份關係全部歸零，則不能僅靠重建後相似性宣告連續。

---

### B3. 漸進替換反例

若系統逐步替換全部部件：

$$
O_0
\rightarrow
O_1
\rightarrow
\cdots
\rightarrow
O_n
$$

每一步都很小，局部邊界證書可能成立。

但累積結果：

$$
O_n
$$

可能與：

$$
O_0
$$

在生成規則、功能或身份上完全不同。

因此局部邊界關係未必具有全域傳遞性：

$$
O_0\sim_B O_1
\land
O_1\sim_B O_2
\not\Rightarrow
O_0\sim_B O_2
$$

需要累積漂移量：

$$
D_B(\eta)
=
\sum_i
d_B(O_i,O_{i+1})
$$

---

### B4. 記憶消失反例

對主體本體而言，物理與功能結構可能連續，但全部記憶被消除。

此時：

- 生物同一可能保留；
- 人格同一可能破裂；
- 法律同一可能保留；
- 敘事同一可能消失。

所以本體邊界是層級化的：

$$
\mathcal B^\ell_\eta(O)
$$

不同本體層可能給出不同結果。

---

### B5. 分支再合併反例

若：

$$
O
\rightarrow
O_1,O_2
\rightarrow
O'
$$

合併後 $O'$ 可能恢復多數核心結構。

但其歷史包含兩條互不相容分支。

因此需要多祖源證書：

$$
\operatorname{MultiAncestry}(O';O_1,O_2)
$$

而不是強迫回復單一路徑身份。

---

### B6. 制度宣告反例

制度可能宣告：

$$
\operatorname{SameLegalEntity}(O,O')
$$

即使物理或組織構成發生巨大變化。

這只能支持：

$$
\mathcal B^{\mathrm{legal}}
$$

不能直接支持：

$$
\mathcal B^{\mathrm{all}}
$$

---

### B7. 功能等價反例

兩個系統可能輸入輸出完全相同：

$$
O_1
\simeq_{\mathrm{func}}
O_2
$$

但其內部因果結構不同。

因此：

$$
\operatorname{FuncEq}
\not\Rightarrow
\operatorname{GenCont}
$$

---

### B8. 強化邊界證書

將證書改寫為：

$$
\operatorname{BCert}^{+}(O,O';\eta,\ell)
$$

其條件包括：

$$
\operatorname{InvPres}^{\ell}
$$

$$
\operatorname{GenCont}^{\ell}
$$

$$
\operatorname{Recover}^{\ell}
$$

$$
\operatorname{Trace}^{\ell}
$$

$$
\operatorname{AncestryCont}^{\ell}
$$

$$
\operatorname{NoTerminalBreak}^{\ell}
$$

$$
D_B^\ell(\eta)<\theta_B^\ell
$$

---

### B9. 邊界狀態向量

單一本體可能在不同層得到不同邊界結果。

定義：

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

分別表示：

- 物理；
- 因果；
- 記憶；
- 法律；
- 社會；
- 數位；
- 規範層。

---

## B-局部決定

第三批次的邊界證書升級為：

$$
\boxed{
\operatorname{BCert}^{+}
=
\operatorname{InvPres}
\land
\operatorname{GenCont}
\land
\operatorname{Recover}
\land
\operatorname{Trace}
\land
\operatorname{AncestryCont}
\land
\operatorname{NoTerminalBreak}
\land
\operatorname{BoundedDrift}
}
$$

並以：

$$
\boxed{
\mathbf B_\eta(O,O')
}
$$

取代單一邊界判定。

---

## B-新增節點

```text
FMO-214A  完美複製反例
FMO-214B  中斷重建反例
FMO-214C  累積漂移
FMO-214D  邊界非傳遞性
FMO-214E  層級化邊界
FMO-214F  多祖源邊界
FMO-214G  功能等價非生成連續
FMO-214H  強化邊界證書 BCert+
FMO-214I  邊界狀態向量
```

---

# 4. 節點 C：語義等價不可判定時的近似策略

## C-R0：點層

> 當語義等價不可判定時，系統應輸出可證明等價、可證明不等價與未決三區，而不是強迫產生單一相似度分數。

---

## C-R1：線層

第三批次要求張力定義在：

$$
[P_1],[P_2]
$$

即語義等價類上。

但：

$$
P_1\simeq_{\mathrm{sem}}P_2
$$

在一般情況下可能不可判定。

若沒有近似策略，語義張力難以實作。

但若只使用向量相似度，又可能把表面相似誤認為語義等價。

---

## C-R2：面層

### C1. 三區判定

定義：

$$
\operatorname{SemEqStatus}(P_1,P_2)
\in
\{
\mathsf{ProvedEq},
\mathsf{ProvedNeq},
\mathsf{Undetermined}
\}
$$

只有在：

$$
\mathsf{ProvedEq}
$$

時，才將兩者完全商為同一等價類。

---

### C2. 等價證書

語義等價證書可以來自：

#### 同構

$$
P_1\cong P_2
$$

#### 雙模擬

$$
P_1\sim_{\mathrm{bis}}P_2
$$

#### 雙向編譯

存在：

$$
C_{12},C_{21}
$$

且核心行為往返保持。

#### 共同規範形式

兩者可化為同一規範核心：

$$
N(P_1)=N(P_2)
$$

#### 測試完備域內等價

對指定輸入域：

$$
\forall x\in X_{\mathrm{test}},
\quad
P_1(x)=P_2(x)
$$

但最後一種只支持域內行為等價，不支持完整本體等價。

---

### C3. 不等價證書

只需找到一個保真觀測差異：

$$
\exists q
\quad
q(P_1)\neq q(P_2)
$$

即可證明在觀測族 $Q$ 下不等價。

或找到：

- 不同可達狀態；
- 不同身份結果；
- 不同因果干預反應；
- 不同核心約束；
- 不同歷史依賴。

---

### C4. 多層近似輪廓

若無法證明完整等價，建立近似輪廓：

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

分別表示：

- 結構近似；
- 行為近似；
- 因果近似；
- 歷史近似；
- 身份近似；
- 規範近似；
- 模態近似。

---

### C5. 近似不是等價

即使：

$$
E_{\mathrm{beh}}\approx1
$$

也不能推出：

$$
P_1\simeq_{\mathrm{sem}}P_2
$$

因為兩者可能只是行為上相似。

因此近似輪廓必須保留維度名稱，不能壓成單一模糊相似度。

---

### C6. 反例導向細化

若目前兩個表示尚未被區分，可以主動搜尋反例：

$$
q^\ast
=
\arg\max_q
\left|
q(P_1)-q(P_2)
\right|
$$

這相當於尋找最具區分力的觀測或干預。

---

### C7. 語義張力區間

對未決對象，張力輸出：

$$
\underline{\vec{\mathcal T}}_{\mathrm{sem}}
\preceq
\vec{\mathcal T}_{\mathrm{sem}}
\preceq
\overline{\vec{\mathcal T}}_{\mathrm{sem}}
$$

其中：

- 下界：已證明不可消除的語義差異；
- 上界：目前找到的最小具體重寫成本。

---

### C8. 近似狀態版本化

新的反例、測試或證書可能改變判定。

因此：

$$
\operatorname{SemEqStatus}_{t}
\rightarrow
\operatorname{SemEqStatus}_{t+1}
$$

必須保留歷史。

---

## C-局部決定

語義等價計算改為三區證書系統：

$$
\boxed{
\mathsf{ProvedEq},
\mathsf{ProvedNeq},
\mathsf{Undetermined}
}
$$

未決時使用：

$$
\boxed{
\mathbf E(P_1,P_2)
}
$$

多層近似輪廓，以及：

$$
\boxed{
\underline{\vec{\mathcal T}}_{\mathrm{sem}}
\preceq
\vec{\mathcal T}_{\mathrm{sem}}
\preceq
\overline{\vec{\mathcal T}}_{\mathrm{sem}}
}
$$

張力區間。

---

## C-新增節點

```text
FMO-215A  語義等價三區判定
FMO-215B  等價證書
FMO-215C  不等價證書
FMO-215D  多層近似輪廓
FMO-215E  反例導向細化
FMO-215F  語義張力區間
FMO-215G  語義等價版本歷史
```

---

# 5. 節點 D：多固定點治理與選擇合法性

## D-R0：點層

> 多固定點之間沒有純形式上的唯一正解；任何選擇都必須揭露選擇主體、程序、受影響者、可逆性與申訴機制。

---

## D-R1：線層

若元約束算子具有多個固定點：

$$
\Gamma_1^\ast,
\Gamma_2^\ast,
\ldots,
\Gamma_k^\ast
$$

則不同制度都可能內部穩定。

形式穩定不能回答：

> 應選哪一個？

若直接由權力選擇，穩定性可能成為支配的技術包裝。

因此需要治理合法性層。

---

## D-R2：面層

### D1. 形式可行不等於合法

$$
\operatorname{Stable}(\Gamma_i^\ast)
\not\Rightarrow
\operatorname{Legit}(\Gamma_i^\ast)
$$

某制度可以非常穩定，但建立在：

- 排除；
- 強制；
- 資訊不對稱；
- 不可申訴；
- 永久鎖定；
- 對弱勢者高成本。

---

### D2. 選擇事件

定義固定點選擇事件：

$$
\mathsf{Sel}
=
\left\langle
A,
C,
P,
S,
E,
R,
T
\right\rangle
$$

其中：

- $A$ ：選擇主體；
- $C$ ：候選固定點集合；
- $P$ ：選擇程序；
- $S$ ：受影響主體；
- $E$ ：證據與預測；
- $R$ ：可逆與申訴機制；
- $T$ ：時間與版本。

---

### D3. 合法性向量

定義：

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

其中：

- $L_A$ ：權限正當性；
- $L_P$ ：程序公平；
- $L_I$ ：資訊透明；
- $L_T$ ：可追溯性；
- $L_R$ ：可逆與救濟；
- $L_M$ ：少數保護；
- $L_U$ ：受影響者參與。

---

### D4. 治理選擇不能直接變成世界真理

制度選擇：

$$
\operatorname{Select}(\Gamma_i^\ast)
$$

可以使某固定點成為：

$$
\Gamma_{\mathrm{effective}}
$$

即有效制度。

但不能推出：

$$
\Gamma_i^\ast
=
\Gamma_W
$$

也就是：

> 被制度採用，不代表它是世界唯一正確本體。

---

### D5. 多固定點保留

若多個固定點各有合理支持，系統應允許：

$$
\mathcal F^\ast
=
\{
\Gamma_1^\ast,
\ldots,
\Gamma_m^\ast
\}
$$

並保留分支模型，而不是過早消滅差異。

---

### D6. 臨時固定點

治理可選擇具有期限的制度：

$$
\Gamma^\ast_{[t_0,t_1]}
$$

到期後重新評估。

這避免把當前選擇永久本體化。

---

### D7. 退出與分叉權

若不同群體無法共享同一固定點，可允許：

$$
\Gamma_A^\ast
\oplus
\Gamma_B^\ast
$$

形成制度分叉，只要跨制度互動規則仍可運作。

---

### D8. 權力捕獲檢測

若選擇結果主要由少數主體控制，且成本由其他主體承擔，可定義：

$$
\operatorname{CaptureRisk}
=
f
\left(
\operatorname{ControlConcentration},
\operatorname{CostExternalization},
\operatorname{ExitBarrier},
\operatorname{Opacity}
\right)
$$

---

### D9. 合法性不是單一加權分數

合法性向量不應輕易被壓成單一數值。

例如，高效率不能自動補償完全沒有申訴機制。

因此某些維度應採最低門檻：

$$
L_j
\geq
\theta_j
$$

而不是只看加權總和。

---

## D-局部決定

多固定點的選擇改為治理事件：

$$
\boxed{
\mathsf{Sel}
=
\left\langle
A,
C,
P,
S,
E,
R,
T
\right\rangle
}
$$

合法性以：

$$
\boxed{
\mathbf L(\mathsf{Sel})
}
$$

表示，並要求若干不可被其他優點抵銷的最低門檻。

制度選擇只產生：

$$
\Gamma_{\mathrm{effective}}
$$

而不是直接宣告：

$$
\Gamma_W
$$

---

## D-新增節點

```text
FMO-216A  固定點選擇事件
FMO-216B  合法性向量
FMO-216C  有效制度／世界規則分離
FMO-216D  多固定點保留
FMO-216E  臨時固定點
FMO-216F  制度分叉與退出
FMO-216G  權力捕獲風險
FMO-216H  合法性最低門檻
```

---

# 6. 節點 E：制度對身份分類的反向構成

## E-R0：點層

> 制度不只判定既有身份，也會透過權利、責任、承認與記錄反向塑造身份的持續條件；但這種構成只在制度層有效，不能抹除其他本體層。

---

## E-R1：線層

第三批次將身份分成：

$$
\mathbf c_I
$$

結構延續；

$$
q_I
$$

證據信心；

$$
J_I
$$

身份分類；

$$
\mathbf r_I
$$

權利責任配置。

但制度效果：

$$
\mathbf r_I
$$

可能反過來改變：

$$
\mathbf c_I
$$

與：

$$
J_I
$$

例如：

- 法律承認使組織持續存在；
- 身份文件影響社會承認；
- 權利配置影響資源與記憶保存；
- 制度記錄使某主體具有歷史連續性；
- 排除制度使某身份逐漸消失。

因此身份不是純粹先存在，再被制度標記。

---

## E-R2：面層

### E1. 描述性判定與構成性判定

制度判定可分為：

#### 描述性判定

制度嘗試描述已存在身份：

$$
J_I^{\mathrm{desc}}
$$

#### 構成性判定

制度行為本身使某身份成立：

$$
J_I^{\mathrm{const}}
$$

例如公司法人成立、婚姻身份、國籍、職位、授權代理。

---

### E2. 反向構成迴路

身份與制度可能形成：

$$
\mathbf c_I
\rightarrow
J_I
\rightarrow
\mathbf r_I
\rightarrow
\mathbf c_I'
$$

例如制度賦予資源與記錄權，使身份在下一時段更容易延續。

因此：

$$
\mathcal Q_I
:
\left(
J_I,\mathbf r_I
\right)
\rightarrow
\Delta \mathbf c_I
$$

可稱為身份治理回饋算子。

---

### E3. 正向構成

制度可能增強：

- 法律連續；
- 社會承認；
- 記錄保存；
- 資源控制；
- 代理能力；
- 歷史可追溯。

因此：

$$
\Delta \mathbf c_I^{+}
$$

---

### E4. 負向構成

制度也可能削弱或抹除：

- 名稱；
- 記錄；
- 財產；
- 行動資格；
- 社會承認；
- 法律主體地位。

因此：

$$
\Delta \mathbf c_I^{-}
$$

---

### E5. 制度不能全層決定身份

即使法律宣告某主體不存在，也不必推出：

$$
\neg\operatorname{Exists}^{\mathrm{physical}}(x)
$$

因此需要層級限制：

$$
\mathcal Q_I^\ell
$$

制度只直接構成其有權作用的本體層。

---

### E6. 身份僭越

若制度將自己的判定擴張為所有層的真理：

$$
J_I^{\mathrm{legal}}(x)
\Rightarrow
J_I^{\mathrm{all}}(x)
$$

則形成：

$$
\mathsf{IdentityUsurpation}
$$

即身份判定僭越。

---

### E7. 記錄與身份

長期身份常依賴記錄：

$$
\operatorname{Record}(x,t)
$$

若制度控制全部記錄，便可能控制：

- 誰被視為存在過；
- 誰具有祖源；
- 誰擁有權利；
- 誰承擔責任；
- 誰可被未來模型辨識。

因此記錄系統本身是身份構成基礎設施。

---

### E8. 對抗性身份

主體可能拒絕制度分類：

$$
J_I^{\mathrm{self}}
\neq
J_I^{\mathrm{institution}}
$$

此時形成身份衝突圖，而不是簡單選一方為真。

---

### E9. 多層身份向量

定義：

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

分別表示：

- 物理；
- 因果；
- 記憶；
- 法律；
- 社會；
- 數位；
- 自我認同。

制度只能直接決定部分分量。

---

### E10. 制度構成的合法性

制度若要構成身份，至少需要：

- 有效權限；
- 公開規則；
- 適用範圍；
- 可申訴；
- 不追溯抹除；
- 記錄可稽核；
- 與其他本體層不混淆。

---

## E-局部決定

身份系統加入治理回饋：

$$
\boxed{
\mathcal Q_I^\ell
:
\left(
J_I^\ell,
\mathbf r_I^\ell
\right)
\rightarrow
\Delta\mathbf c_I^\ell
}
$$

並將身份分類改為多層向量：

$$
\boxed{
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
}
$$

制度可以構成法律、社會與部分數位身份，但不能自動覆蓋物理、因果、記憶與自我層。

---

## E-新增節點

```text
FMO-217A  描述性／構成性身份判定
FMO-217B  身份治理回饋算子
FMO-217C  正向身份構成
FMO-217D  負向身份構成
FMO-217E  層級化制度作用域
FMO-217F  身份判定僭越
FMO-217G  記錄作為身份基礎設施
FMO-217H  對抗性身份
FMO-217I  多層身份向量
FMO-217J  制度身份構成合法性
```

---

# 7. 跨節點對齊

本批次五個節點共同揭示：

> 一旦理論進入證書、近似與治理階段，任何判定都必須附帶其生成程序。

---

## 7.1 證書與語義近似

語義等價證書本身也是：

$$
\mathsf{Cert}
$$

因此它也具有：

- 依賴；
- 適用域；
- 反駁條件；
- 版本。

---

## 7.2 邊界證書與身份

邊界判定不能忽略身份祖源。

若：

$$
\operatorname{AncestryCont}=0
$$

即使端點結構近似，也可能只是重建，而非延續。

---

## 7.3 治理與固定點

多固定點選擇會改變：

$$
\Gamma_{\mathrm{effective}}
$$

並進一步改變：

- 可能空間；
- 身份規則；
- 邊界判定；
- 證書有效性；
- 權利責任。

因此治理不是理論外部附加，而是模型與制度本體的內部操作。

---

## 7.4 制度與證書

制度可以指定哪些證書被承認。

但：

$$
\operatorname{InstitutionAccepts}(C)
\not\Rightarrow
\operatorname{WorldValid}(C)
$$

---

## 7.5 身份與記錄

證書、邊界與身份都依賴歷史記錄。

因此：

$$
\mathcal H_{\mathrm{prov}}
$$

即來源與版本歷史，開始成為整套理論的共同基礎層。

---

# 8. 第四批次後的更新核心

## 8.1 證書系統

$$
\boxed{
\mathfrak C
=
\left\langle
\mathsf{Cert},
G_{\mathrm{Cert}},
\operatorname{Defeat},
\operatorname{CertStatus},
\mathcal H_{\mathrm{Cert}}
\right\rangle
}
$$

---

## 8.2 強化本體邊界

$$
\boxed{
\operatorname{BCert}^{+}
}
$$

與：

$$
\boxed{
\mathbf B_\eta(O,O')
}
$$

---

## 8.3 近似語義系統

$$
\boxed{
\mathfrak E_{\mathrm{sem}}
=
\left\langle
\operatorname{SemEqStatus},
\mathbf E,
\underline{\vec{\mathcal T}},
\overline{\vec{\mathcal T}},
\mathcal H_E
\right\rangle
}
$$

---

## 8.4 元治理系統

$$
\boxed{
\mathfrak G_{\mathrm{meta}}
=
\left\langle
\operatorname{Fix}(\mathcal F_M),
\mathsf{Sel},
\mathbf L,
\operatorname{CaptureRisk},
\Gamma_{\mathrm{effective}}
\right\rangle
}
$$

---

## 8.5 身份治理系統

$$
\boxed{
\mathfrak I_{\mathrm{gov}}
=
\left\langle
\mathbf c_I,
q_I,
\mathbf J_I,
\mathbf r_I,
\mathcal Q_I^\ell,
\mathcal H_I
\right\rangle
}
$$

---

# 9. 本批次新形成的穩定區

## 9.1 證書不是絕對真理

任何證書都相對於：

$$
base,
scope,
assumptions,
method
$$

成立。

---

## 9.2 邊界具有祖源與斷裂條件

端點相似不能取代：

$$
\operatorname{AncestryCont}
$$

與：

$$
\operatorname{NoTerminalBreak}
$$

---

## 9.3 語義等價採三區判定

$$
\mathsf{ProvedEq},
\mathsf{ProvedNeq},
\mathsf{Undetermined}
$$

---

## 9.4 穩定制度不等於合法制度

$$
\operatorname{Stable}
\not\Rightarrow
\operatorname{Legit}
$$

---

## 9.5 制度身份是構成性的，但有作用域

制度可構成部分身份層，但不能自動宣告全層本體真理。

---

# 10. 仍未解決的高張力問題

## 10.1 證書依賴可能循環

兩個證書可能互相支持：

$$
C_1\rightarrow C_2\rightarrow C_1
$$

需要建立非循環或有界循環規則。

---

## 10.2 邊界漂移門檻仍需校準

$$
D_B^\ell(\eta)<\theta_B^\ell
$$

中的：

$$
\theta_B^\ell
$$

尚未有客觀來源。

---

## 10.3 語義近似輪廓仍可能被權重操控

即使不壓成單一分數，維度選擇本身仍可能帶有偏見。

---

## 10.4 合法性向量可能存在衝突

程序公平、效率、少數保護與可逆性可能互相張力。

---

## 10.5 制度反向構成可能變成自我實現

制度先宣告身份，再利用宣告產生的結果證明原判定正確。

這可能形成：

$$
\mathsf{IdentityFeedbackLock}
$$

身份回饋鎖定。

---

# 11. 更新後的研究佇列

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 證書依賴循環與證書網路可信度 | 影響所有證書型判定 |
| 2 | 邊界漂移門檻與非傳遞性 | 決定長期本體延續 |
| 3 | 語義近似維度的完備性與偏誤 | 決定近似張力品質 |
| 4 | 合法性衝突與不可補償門檻 | 決定治理選擇 |
| 5 | 身份回饋鎖定與去僭越機制 | 防止制度自證 |
| 6 | 四值、機率、模糊與證書狀態統合 | 模型判定層仍分散 |
| 7 | 可能空間、證書與邊界的計算複雜度 | 準備演算法化 |
| 8 | 來源歷史作為共同基礎層 | 可能升格為新核心結構 |

---

# 12. 圖更新摘要

## 12.1 新增節點

本批次新增：

$$
8+9+7+8+10=42
$$

個子節點。

---

## 12.2 新增主要關係

```text
certifies
depends_on_certificate
defeats_certificate
qualifies_certificate
expires_certificate
preserves_ancestry
contains_terminal_break
accumulates_boundary_drift
proves_semantic_equivalence
proves_semantic_difference
approximates_semantics
selects_fixed_point
has_governance_legitimacy
risks_power_capture
constitutes_identity
feeds_back_into_identity
usurps_identity_layer
records_identity_history
```

---

## 12.3 圖版本更新

輸入：

$$
\mathcal G_{\mathrm{FMO}}^{(3)}
$$

輸出：

$$
\boxed{
\mathcal G_{\mathrm{FMO}}^{(4)}
}
$$

---

# 13. 本批次結論

第四批次將事實模態本體論從「具有操作與證書」推進到「能審查操作與證書」。

第一，可能性見證與不可能性證書不再被視為終局判定，而被轉換成可追溯、可反駁、可版本化的證書結構：

$$
\boxed{
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
}
$$

第二，本體邊界證書經過複製、重建、漸進漂移、分支合併與制度宣告等反例後，被強化為：

$$
\boxed{
\operatorname{BCert}^{+}
}
$$

並加入祖源連續、終止斷裂與累積漂移檢查。

第三，語義等價不可判定時，不再使用單一相似度代替，而採用：

$$
\boxed{
\mathsf{ProvedEq},
\mathsf{ProvedNeq},
\mathsf{Undetermined}
}
$$

三區判定、多層近似輪廓與張力上下界。

第四，多固定點的選擇被正式視為治理事件。形式穩定不等於合法：

$$
\boxed{
\operatorname{Stable}
\not\Rightarrow
\operatorname{Legit}
}
$$

第五，制度不只是被動標記身份，也會透過權利、記錄、資源與承認反向塑造身份延續：

$$
\boxed{
\mathcal Q_I^\ell
:
\left(
J_I^\ell,
\mathbf r_I^\ell
\right)
\rightarrow
\Delta\mathbf c_I^\ell
}
$$

但制度的構成能力必須受到本體層級與治理合法性限制。

因此，本批次形成了一項新的總原則：

$$
\boxed{
\text{任何本體判定}
=
\text{內容}
+
\text{生成程序}
+
\text{依賴證書}
+
\text{適用域}
+
\text{版本歷史}
}
$$

理論不能只保存「判定是什麼」，還必須保存：

- 為何得到；
- 依賴什麼；
- 誰作出；
- 在哪一層有效；
- 何時可能失效；
- 如何被反駁；
- 是否受到權力與制度塑造。

這使事實模態本體論進一步從靜態本體描述，轉向一套具有自我審查能力的本體治理與證書系統。

---

## 附錄 A：第四批次最小 JSON

```json
{
  "batch": "FMO-MRASG-004",
  "input_graph": "G_FMO_3",
  "output_graph": "G_FMO_4",
  "selected_nodes": [
    "FMO-213",
    "FMO-214",
    "FMO-215",
    "FMO-216",
    "FMO-217"
  ],
  "decisions": [
    {
      "node": "FMO-213",
      "result": "versioned_defeasible_certificate_system"
    },
    {
      "node": "FMO-214",
      "result": "ancestry_break_and_drift_aware_boundary_certificate"
    },
    {
      "node": "FMO-215",
      "result": "three_zone_semantic_equivalence_with_interval_tension"
    },
    {
      "node": "FMO-216",
      "result": "legitimacy_constrained_multistable_governance"
    },
    {
      "node": "FMO-217",
      "result": "layered_institutional_feedback_on_identity"
    }
  ],
  "next_queue": [
    "certificate_dependency_cycles",
    "boundary_drift_thresholds",
    "semantic_approximation_bias",
    "legitimacy_conflict",
    "identity_feedback_lock"
  ]
}
```

---

## 附錄 B：版本狀態

**批次狀態：** 已完成  
**理論狀態：** 證書、邊界、近似、治理與身份回饋已形成初步閉環  
**圖版本：** $\mathcal G_{\mathrm{FMO}}^{(4)}$  
**下一階段：** 證書網路、長期漂移、偏誤、合法性衝突與身份去僭越  
