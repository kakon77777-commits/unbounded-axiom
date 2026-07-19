# FMO–MRASG 第三研究批次

## 真可能、本體邊界、表示不變性、元穩定與身份強度

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

第二批次建立了：

$$
\Omega_{\leq k}
\left(
O^+;
\mathcal D,
\mathcal E_{\mathrm{edit}},
\Gamma^\tau
\right)
$$

即由實際根、編輯語言、干預型別與約束系統共同生成的有根可能空間。

同時建立：

$$
\Delta^\tau
=
\left\langle
\tau,
target,
op,
scope,
guard,
closure,
reversibility
\right\rangle
$$

與：

$$
\mathcal E_{\mathrm{edit}}
$$

以及三層元約束：

$$
\Gamma^{(0)},
\Gamma^{(1)},
\Gamma^{(2)}
$$

和身份延續圖：

$$
G_I
=
\left(
V_I,
E_I,
\Lambda_I
\right)
$$

然而，第二批次也暴露五個更深的問題。

第一，模型能夠生成某個候選本體，不表示該本體在世界層真正可能。

第二，核心不變量相同，不必然表示兩個本體仍屬於同一本體區域。

第三，同一本體可以有多種表示方式，若成本依賴表示，張力便不具有穩定意義。

第四，元約束算子可能有多個固定點、沒有固定點，甚至形成循環。

第五，身份延續邊上的強度 $\lambda$ 容易被誤解為「部分是同一個人」。

本批次將平行處理以上五個高張力節點。

---

# 1. 輸入圖

第二批次輸出：

$$
\mathcal G_{\mathrm{FMO}}^{(2)}
$$

目前主要結構為：

$$
\mathfrak W_2^+
=
\left\langle
\mathcal S_W,
\Gamma_W^{(0:2)},
\mathsf{Real}_W,
\Theta_A
\right\rangle
$$

可能生成系統：

$$
\mathfrak P_O
=
\left\langle
O^+,
\mathcal E_{\mathrm{edit}},
\mathcal D,
\operatorname{Adm},
\operatorname{Cl}_{\mathcal C}
\right\rangle
$$

身份系統：

$$
\mathfrak I_O
=
\left\langle
G_I,
\Gamma_I,
\mathcal A_R
\right\rangle
$$

本批次選取節點：

```text
FMO-211  可達可能與世界真可能
FMO-208  本體邊界與不變量充分性
FMO-212  編輯表示不變性
FMO-102K 多固定點／無固定點元約束
FMO-202L 身份延續強度語義
```

---

# 2. 節點 A：可達可能與世界真可能

## A-R0：點層

> 可由模型編輯語言生成，只能證明「模型可構造」；它既不是世界真可能的充分條件，也未必是必要條件。

---

## A-R1：線層

第二批次定義：

$$
O'
\in
\Omega_{\mathrm{reach}}(O^+)
$$

當且僅當存在一條合法編輯路徑：

$$
O^+
\xrightarrow{\eta}
O'
$$

但這只表示：

> 在目前模型、語言與約束下，系統能構造 $O'$ 。

它不直接證明：

$$
\Diamond_W O'
$$

即 $O'$ 在世界層真正可能。

因此需要分離：

$$
\Diamond_M O'
$$

模型可達可能；

與：

$$
\Diamond_W O'
$$

世界真可能。

---

## A-R2：面層

### A1. 模型可達不蘊含世界可能

存在三種典型錯誤。

#### 規則不足

模型的約束系統：

$$
\widehat{\Gamma}
$$

可能漏掉世界中的真實限制：

$$
\Gamma_W
$$

因此：

$$
O'
\in
\Omega_{\mathrm{adm}}(\widehat{\Gamma})
$$

但：

$$
O'
\notin
\Omega_{\mathrm{adm}}(\Gamma_W)
$$

#### 表示虛構

語言能組合出形式正確的候選結構，但該結構並無世界實現條件。

#### 閉包不完整

系統只計算了局部耦合閉包，忽略遠端或跨尺度影響。

因此：

$$
\Diamond_M O'
\not\Rightarrow
\Diamond_W O'
$$

---

### A2. 世界可能也不必然模型可達

反方向也可能失敗。

模型的編輯語言可能過弱：

$$
\mathcal E_{\mathrm{edit}}^M
$$

無法表達世界中真正可能的轉換。

因此：

$$
\Diamond_W O'
$$

可能成立，但：

$$
O'
\notin
\Omega_{\mathrm{reach}}^M(O^+)
$$

所以：

$$
\Diamond_W O'
\not\Rightarrow
\Diamond_M O'
$$

---

### A3. 三層可能性

需要至少區分：

#### 語法可能

$$
\Diamond_{\mathrm{syn}} O'
$$

可由語言合法生成。

#### 模型可能

$$
\Diamond_M O'
$$

符合模型的型別、約束與可達規則。

#### 世界可能

$$
\Diamond_W O'
$$

世界的真實構成條件容許其實現。

三者的關係通常不是等價：

$$
\Diamond_{\mathrm{syn}} O'
\not\Leftrightarrow
\Diamond_M O'
\not\Leftrightarrow
\Diamond_W O'
$$

---

### A4. 無法直接計算世界真可能

由於：

$$
\Gamma_W
$$

不能被模型完全掌握，系統通常無法直接決定：

$$
\Diamond_W O'
$$

因此，模型應輸出可能性邊界，而不是假裝給出世界真可能的完整判定。

定義：

$$
\Omega_M^-
$$

為有強實現見證支持的可能下界；

$$
\Omega_M^+
$$

為尚未被模型排除的可能上界。

理想關係為：

$$
\boxed{
\Omega_M^-
\subseteq
\Omega_W
\subseteq
\Omega_M^+
}
$$

其中：

$$
\Omega_W
$$

表示世界真可能空間。

---

### A5. 可能性見證

某候選本體 $O'$ 進入下界，需要至少一種可能性見證：

$$
w_P(O')
$$

可能見證類型包括：

- 已知世界實例；
- 可重複實驗；
- 已驗證構造；
- 從已實現結構的保真轉換；
- 具有完整約束閉包的形式證明；
- 跨模型獨立收斂的生成結果。

因此：

$$
O'\in\Omega_M^-
$$

當且僅當存在足夠強的見證：

$$
\exists w_P
\;
\operatorname{ValidWitness}(w_P,O')
$$

---

### A6. 不可能性證書

若能找到：

$$
c_\bot(O')
$$

使其證明候選本體違反不可放棄的核心條件，則：

$$
O'\notin\Omega_W
$$

至少在目前理論假設下成立。

可能的不可能性證書包括：

- 型別矛盾；
- 核心約束不可滿足；
- 動力閉包崩潰；
- 同一性條件自我否定；
- 必要構成條件缺失；
- 任何合法歷史都不存在。

形式上：

$$
c_\bot(O')
:
\operatorname{Unsat}
\left(
\Gamma_{\mathrm{core}}\cup O'
\right)
$$

---

### A7. 未決可能區

若既無正見證，也無不可能證書，則候選本體進入：

$$
\Omega_M^{?}
$$

因此模型可能空間應分為：

$$
\Omega_M
=
\Omega_M^-
\cup
\Omega_M^{?}
\cup
\Omega_M^\bot
$$

分別表示：

- 有見證支持；
- 未決；
- 已取得不可能性證書。

---

## A-局部決定

世界真可能保留為不可直接約化的世界層模態關係：

$$
\boxed{
\Diamond_W
}
$$

模型不宣稱完整計算 $\Omega_W$ ，而只維護：

$$
\boxed{
\Omega_M^-
\subseteq
\Omega_W
\subseteq
\Omega_M^+
}
$$

並以：

- 可能性見證；
- 不可能性證書；
- 未決區；

形成三分判定。

---

## A-新增節點

```text
FMO-211A  語法可能 ◇syn
FMO-211B  模型可能 ◇M
FMO-211C  世界真可能 ◇W
FMO-211D  可能空間下界 ΩM-
FMO-211E  可能空間上界 ΩM+
FMO-211F  可能性見證
FMO-211G  不可能性證書
FMO-211H  未決可能區 ΩM?
```

---

# 3. 節點 B：本體邊界與不變量充分性

## B-R0：點層

> 核心不變量相同只能提供邊界保留的必要線索，不能單獨證明兩個本體仍屬於同一本體；邊界還需要生成規則、翻譯可逆性與歷史路徑的共同見證。

---

## B-R1：線層

早期定義：

$$
\mathcal B(O)
=
\left\{
O'
\mid
\mathcal I_{\mathrm{core}}(O)
\simeq
\mathcal I_{\mathrm{core}}(O')
\right\}
$$

問題是，不同本體可能共享同一組不變量。

例如兩個系統可能都保持：

- 節點數；
- 對稱群；
- 某些守恆量；
- 外部行為；
- 觀測輸出。

但它們的構成規則、身份條件與歷史生成方式可能完全不同。

因此：

$$
\mathcal I_{\mathrm{core}}(O)
\simeq
\mathcal I_{\mathrm{core}}(O')
$$

不是充分條件。

---

## B-R2：面層

### B1. 不變量的必要性

若一項變化摧毀所有被本體視為核心的結構，通常代表已穿越邊界。

因此核心不變量仍有價值：

$$
\operatorname{PreserveInv}_{\mathcal K}(O,O')
$$

但只能作為第一層檢查。

---

### B2. 同不變量異本體

考慮：

$$
O_1
\neq
O_2
$$

但：

$$
\mathcal I_{\mathrm{core}}(O_1)
=
\mathcal I_{\mathrm{core}}(O_2)
$$

可能原因包括：

- 觀測等價；
- 粗粒化後等價；
- 統計量相同；
- 外部輸入輸出相同；
- 生成機制不同；
- 身份規則不同；
- 歷史來源不同。

所以：

$$
\operatorname{SameInvariant}
\not\Rightarrow
\operatorname{SameOntology}
$$

---

### B3. 邊界的四項見證

判定 $O'$ 是否仍在 $O$ 的本體邊界內，至少需要：

#### 核心不變量保留

$$
\operatorname{InvPres}(O,O')
$$

#### 生成規則連續

$$
\operatorname{GenCont}(O,O')
$$

即構成與生成方式沒有發生不可恢復斷裂。

#### 翻譯可逆或可恢復

存在：

$$
\Phi_{O\rightarrow O'}
$$

與：

$$
\Psi_{O'\rightarrow O}
$$

使：

$$
\Psi\circ\Phi
\simeq
\operatorname{id}_O
$$

至少對核心結構成立。

#### 歷史路徑可追溯

存在合法改寫路徑：

$$
\eta:
O\leadsto O'
$$

且所有中間狀態都可追蹤其邊界地位。

---

### B4. 邊界證書

定義本體邊界證書：

$$
\operatorname{BCert}(O,O')
=
\left\langle
\mathcal I_{\mathrm{core}},
\eta,
\Phi,
\Psi,
\Gamma_{\mathrm{core}}
\right\rangle
$$

若證書成立，則：

$$
O'
\in
\mathcal B_\eta(O)
$$

注意下標 $\eta$ ，表示邊界可能依賴路徑。

---

### B5. 路徑依賴

可能存在：

$$
\eta_1:
O\leadsto O'
$$

保留核心結構；

但另一條：

$$
\eta_2:
O\leadsto O'
$$

經過不可逆斷裂後重新構造相似結果。

最終狀態外觀相同，但歷史身份不同。

因此：

$$
\operatorname{BoundaryStatus}(O,O')
$$

不能完全由端點決定。

應改為：

$$
\operatorname{BoundaryStatus}(O,O';\eta)
$$

---

### B6. 四種邊界結果

可區分：

#### 彈性變形

$$
\mathsf{Elastic}
$$

核心生成規則與恢復映射皆保留。

#### 相變

$$
\mathsf{PhaseShift}
$$

宏觀結構改變，但仍存在共同底層構成框架。

#### 本體替換

$$
\mathsf{OntologyReplacement}
$$

核心生成與身份規則改變，不能由保真逆映射恢復。

#### 本體崩潰

$$
\mathsf{Collapse}
$$

候選結果不再構成可操作本體。

---

### B7. 邊界不是單一球面

同一本體在不同變化方向上可以有不同韌性。

例如：

- 對局部關係修改容忍高；
- 對身份規則修改容忍低；
- 對制度規則修改容忍中等；
- 對實際性制度修改幾乎零容忍。

因此：

$$
\mathcal B(O)
$$

更接近非均勻、方向相關的可變形區域，而不是固定半徑球體。

---

## B-局部決定

將本體邊界改為路徑索引的證書區域：

$$
\boxed{
\mathcal B_\eta(O)
=
\left\{
O'
\mid
\operatorname{BCert}(O,O';\eta)
\right\}
}
$$

其中：

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

核心不變量是必要線索，但不是單獨充分條件。

---

## B-新增節點

```text
FMO-208A  同不變量異本體反例
FMO-208B  生成規則連續性
FMO-208C  核心翻譯可恢復性
FMO-208D  路徑索引邊界
FMO-208E  本體邊界證書 BCert
FMO-208F  彈性／相變／替換／崩潰分類
FMO-208G  方向相關邊界
```

---

# 4. 節點 C：編輯語言的表示不變性

## C-R0：點層

> 本體張力必須定義在語義等價類上，而不是定義在某一種圖、程式或文本表示上；否則改寫成本只是編碼成本。

---

## C-R1：線層

同一本體可被表示為：

- 圖；
- 邏輯公式；
- 關聯資料庫；
- 程式；
- 狀態機；
- 超圖；
- 自然語言規則。

若本體張力直接計算編輯次數，則不同表示會產生不同結果。

因此需要區分：

$$
T_{\mathrm{syn}}
$$

語法編輯成本；

與：

$$
T_{\mathrm{sem}}
$$

語義本體改變成本。

---

## C-R2：面層

### C1. 表示與語義

令：

$$
P
$$

為本體的一個表示。

語義解釋函數為：

$$
\llbracket P\rrbracket
=
O
$$

兩個表示：

$$
P_1,P_2
$$

若：

$$
\llbracket P_1\rrbracket
\simeq
\llbracket P_2\rrbracket
$$

則它們屬於同一語義等價類：

$$
[P]_O
$$

---

### C2. 表示差異不應產生本體張力

若：

$$
P_1\simeq_{\mathrm{rep}}P_1'
$$

且：

$$
P_2\simeq_{\mathrm{rep}}P_2'
$$

則理想上：

$$
T_{\mathrm{sem}}(P_1,P_2)
=
T_{\mathrm{sem}}(P_1',P_2')
$$

這是表示不變性要求。

---

### C3. 商空間張力

定義表示商空間：

$$
\mathfrak P/{\simeq_{\mathrm{sem}}}
$$

本體張力應作用於等價類：

$$
\widetilde{\mathcal T}
:
[P_1]\times[P_2]
\rightarrow
\mathbb R_{\geq0}^n
$$

可寫成：

$$
\widetilde{\mathcal T}
([P_1],[P_2])
=
\inf_{
Q_1\in[P_1],
Q_2\in[P_2]
}
\operatorname{CostVec}(Q_1,Q_2)
$$

---

### C4. 正規形不一定存在

第二批次使用：

$$
\operatorname{NF}(\eta)
$$

但對複雜本體語言，可能：

- 不存在唯一正規形；
- 計算正規形代價過高；
- 不同正規形無法直接比較；
- 語義等價本身不可判定。

因此不能依賴唯一正規形作為唯一方案。

---

### C5. 三種替代機制

#### 雙模擬

若兩種表示可互相模擬且保持核心行為：

$$
P_1\sim_{\mathrm{bis}}P_2
$$

則視為語義等價候選。

#### 雙向編譯

存在：

$$
C_{1\rightarrow2}
$$

與：

$$
C_{2\rightarrow1}
$$

使往返後保留核心結構。

#### 最小描述正則化

對過度冗長表示加入表示成本懲罰：

$$
T_{\mathrm{adj}}
=
T_{\mathrm{edit}}
-
\lambda
\operatorname{Redundancy}
$$

避免把冗餘節點數量誤當成高本體張力。

---

### C6. 語法與語義雙層成本

完整成本應為：

$$
\vec{\mathcal T}_{\mathrm{full}}
=
\left\langle
\vec{\mathcal T}_{\mathrm{sem}},
\vec{\mathcal T}_{\mathrm{rep}}
\right\rangle
$$

其中：

- $\vec{\mathcal T}_{\mathrm{sem}}$ ：本體意義真正改變；
- $\vec{\mathcal T}_{\mathrm{rep}}$ ：轉換表示所需成本。

兩者都可能有工程價值，但不能混為一談。

---

### C7. 上下界計算

若語義等價不可判定，可以維護：

$$
\underline{\mathcal T}
\leq
\mathcal T_{\mathrm{sem}}
\leq
\overline{\mathcal T}
$$

其中：

- 下界來自不可避免的核心差異；
- 上界來自已找到的具體編輯路徑。

這使系統可以在無法精確計算時仍保持誠實。

---

## C-局部決定

本體張力正式分成：

$$
\boxed{
\vec{\mathcal T}_{\mathrm{sem}}
}
$$

與：

$$
\boxed{
\vec{\mathcal T}_{\mathrm{rep}}
}
$$

語義張力定義於表示等價類：

$$
\boxed{
\widetilde{\mathcal T}
([P_1],[P_2])
}
$$

當精確等價不可判定時，輸出張力上下界，而不是偽造單一精確值。

---

## C-新增節點

```text
FMO-212A  本體表示 P
FMO-212B  語義解釋函數 [[P]]
FMO-212C  表示等價類 [P]
FMO-212D  語義張力 Tsem
FMO-212E  表示張力 Trep
FMO-212F  雙模擬／雙向編譯
FMO-212G  張力上下界
FMO-212H  正規形不存在風險
```

---

# 5. 節點 D：多固定點與無固定點元約束

## D-R0：點層

> 元約束不必收斂到唯一固定點；理論應允許多穩定制度、週期性制度與無穩定解，並把它們視為不同元治理狀態。

---

## D-R1：線層

第二批次要求：

$$
\Gamma^\ast
=
\mathcal F_M(\Gamma^\ast)
$$

但實際上，算子：

$$
\mathcal F_M
$$

可能具有：

- 唯一固定點；
- 多個固定點；
- 沒有固定點；
- 週期軌道；
- 混沌或發散行為。

因此，固定點不能被當作必然存在且唯一。

---

## D-R2：面層

### D1. 唯一穩定固定點

若：

$$
\exists!\Gamma^\ast
$$

且對鄰近初始狀態：

$$
\mathcal F_M^n(\Gamma_0)
\rightarrow
\Gamma^\ast
$$

則系統具有單一元穩定制度。

---

### D2. 多固定點

若：

$$
\Gamma_1^\ast,
\Gamma_2^\ast,
\ldots,
\Gamma_k^\ast
$$

皆滿足：

$$
\mathcal F_M(\Gamma_i^\ast)
=
\Gamma_i^\ast
$$

則系統具有制度多穩態。

此時最終制度依賴：

- 初始條件；
- 歷史路徑；
- 權力分布；
- 更新順序；
- 外部干預。

因此：

$$
\Gamma^\ast
=
\Gamma^\ast(\Gamma_0,\pi,\mathcal Q)
$$

---

### D3. 無固定點但存在週期

可能有：

$$
\Gamma_1
\rightarrow
\Gamma_2
\rightarrow
\cdots
\rightarrow
\Gamma_m
\rightarrow
\Gamma_1
$$

此時系統沒有靜態固定點，但可能具有穩定週期：

$$
\mathcal C_m
$$

例如制度在兩套規則間反覆切換。

這不必然代表系統完全不可操作。

---

### D4. 有界吸引子

更一般地，可以定義吸引子集合：

$$
\operatorname{Attr}(\mathcal F_M)
$$

只要更新軌道保持在可操作區域：

$$
\Gamma_t
\in
\mathcal O_{\mathrm{operable}}
$$

系統就可能具有動態元穩定。

---

### D5. 發散與崩潰

若：

$$
d(\Gamma_t,\Gamma_{t+1})
\rightarrow
\infty
$$

或不斷產生新衝突而無法維持最低操作條件，則稱為：

$$
\mathsf{MetaCollapse}
$$

---

### D6. 元穩定分類

定義：

$$
\operatorname{MetaStatus}(\Gamma,\mathcal F_M)
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

---

### D7. 多固定點的選擇原則

若存在多個固定點，不能假定其中一個天然正確。

選擇可依賴：

- 最小修改；
- 歷史連續；
- 核心不變量保留；
- 可逆性；
- 規則透明度；
- 主體合法性；
- 世界證據；
- 治理程序。

定義任務相對選擇函數：

$$
\operatorname{Select}_{\rho}
\left(
\operatorname{Fix}(\mathcal F_M)
\right)
$$

其中 $\rho$ 是選擇準則。

---

### D8. 世界與模型固定點分離

模型元約束收斂：

$$
\widehat{\Gamma}^\ast
$$

不表示世界構成規則本身收斂。

因此：

$$
\operatorname{Fix}_M
\neq
\operatorname{Fix}_W
$$

模型中的固定點只是理論或制度的穩定狀態。

---

## D-局部決定

固定點要求改為更一般的元穩定判定：

$$
\boxed{
\operatorname{MetaStable}
\left(
\Gamma,\mathcal F_M
\right)
}
$$

其可接受形式包括：

- 唯一穩定固定點；
- 多穩定固定點；
- 可解釋週期；
- 有界動態吸引子。

只有發散與不可操作軌道才直接構成元約束失敗。

---

## D-新增節點

```text
FMO-102K  唯一固定點
FMO-102L  多固定點制度
FMO-102M  週期性元約束
FMO-102N  有界動態吸引子
FMO-102O  元約束發散
FMO-102P  元穩定分類
FMO-102Q  固定點選擇準則
FMO-102R  世界／模型固定點分離
```

---

# 6. 節點 E：身份延續強度的語義

## E-R0：點層

> 身份延續強度不是「同一性真值的百分比」，而是多種連續性見證、可信度與制度效果的結構化記錄。

---

## E-R1：線層

第二批次使用：

$$
x
\rightsquigarrow_{\tau,\lambda}
y
$$

其中 $\lambda$ 表示延續強度。

但若把：

$$
\lambda=0.7
$$

理解為：

> $y$ 有百分之七十是 $x$ 。

會產生嚴重混亂。

身份不是普通物理混合比例，也不必具有可加性。

---

## E-R2：面層

### E1. 強度可能混合了四種不同量

延續邊上的單一 $\lambda$ 可能同時混入：

1. 結構連續程度；
2. 證據可信度；
3. 身份判定信心；
4. 權利責任繼承比例。

這四者不能合併。

---

### E2. 延續輪廓

將延續強度改為向量：

$$
\mathbf c_I(x,y)
=
\left\langle
c_P,
c_C,
c_M,
c_G,
c_L,
c_S,
c_D,
c_B
\right\rangle
$$

分別表示：

- 物理連續；
- 因果連續；
- 記憶連續；
- 目標連續；
- 法律連續；
- 社會連續；
- 數位連續；
- 分支連續。

這些值描述結構程度，不是身份真值。

---

### E3. 證據信心

對延續輪廓的認識可信度另記為：

$$
q_I(x,y)
\in
[0,1]
$$

它表示：

> 模型對延續證據評估的信心。

因此：

$$
q_I
$$

屬於認識層，而不是身份本身。

---

### E4. 身份判定

身份判定由：

$$
\Gamma_I
$$

對延續輪廓進行分類：

$$
\operatorname{IdJudgment}_O(x,y)
=
J_{\Gamma_I}
\left(
\mathbf c_I(x,y)
\right)
$$

輸出可能為：

$$
\{
\mathsf{Same},
\mathsf{Continues},
\mathsf{Branches},
\mathsf{Inherits},
\mathsf{Copies},
\mathsf{Reconstructs},
\mathsf{Unrelated},
\mathsf{Indeterminate}
\}
$$

---

### E5. 權利責任配置另行表示

制度效果不放入身份強度，而由：

$$
\mathbf r_I(x,y)
$$

表示權利責任向量，例如：

- 財產權；
- 債務；
- 契約；
- 人格權；
- 記憶責任；
- 刑事責任；
- 資料控制權。

因此：

$$
\mathbf r_I
\neq
\mathbf c_I
$$

身份連續高，不必然全部權利責任完整轉移。

---

### E6. 分支不服從總量守恆

若：

$$
x\rightsquigarrow y_1
$$

與：

$$
x\rightsquigarrow y_2
$$

兩個分支都具有高度記憶與目標連續，則可能有：

$$
c_M(x,y_1)\approx1
$$

且：

$$
c_M(x,y_2)\approx1
$$

不需要滿足：

$$
c_M(x,y_1)+c_M(x,y_2)=1
$$

因此延續程度不是機率分配，也不是守恆資源。

---

### E7. 部分同一性只有在特定本體下成立

某些本體可能允許：

$$
\operatorname{PartlySame}(x,y)
$$

但這必須由本體明確定義，例如：

- 部分結構同一；
- 部分成員重疊；
- 部分法律人格延續；
- 部分歷史束共享。

不能由任意的 $0.7$ 自動推出。

---

### E8. 身份邊完整標籤

身份延續邊改為：

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

其中：

- $\mathbf c_I$ ：延續輪廓；
- $q_I$ ：證據信心；
- $J_I$ ：身份分類；
- $\mathbf r_I$ ：制度效果；
- $t$ ：時間；
- $source$ ：來源。

---

## E-局部決定

刪除單一身份強度 $\lambda$ 的核心地位。

改用：

$$
\boxed{
\mathbf c_I
+
q_I
+
J_I
+
\mathbf r_I
}
$$

四層分離：

1. 結構延續；
2. 認識信心；
3. 身份判定；
4. 權利責任配置。

---

## E-新增節點

```text
FMO-202L  多維延續輪廓 cI
FMO-202M  身份證據信心 qI
FMO-202N  身份分類 JI
FMO-202O  權利責任向量 rI
FMO-202P  分支非守恆延續
FMO-202Q  部分同一性的本體條件
FMO-202R  完整身份邊標籤 ΛI
```

---

# 7. 跨節點對齊

本批次五個節點形成一個更深的共同結構：

```text
模型表示
    ├─ 生成 → 模型可達可能
    ├─ 不等於 → 世界真可能
    └─ 需要 → 可能性上下界

本體端點
    ├─ 共享不變量
    ├─ 還需生成連續
    ├─ 還需可恢復翻譯
    └─ 還需歷史路徑

編輯表示
    ├─ 有語法成本
    ├─ 有語義成本
    └─ 必須商掉表示差異

元約束
    ├─ 可能唯一穩定
    ├─ 可能多穩定
    ├─ 可能週期
    └─ 可能發散

身份延續
    ├─ 有結構輪廓
    ├─ 有證據信心
    ├─ 有身份分類
    └─ 有制度效果
```

---

## 7.1 可能性與邊界

若：

$$
O'\in\Omega_{\mathrm{reach}}
$$

但沒有：

$$
\operatorname{BCert}(O,O')
$$

則 $O'$ 可能是跨本體候選，而非同一本體內變形。

但即使跨越邊界，也不表示世界真可能。

因此：

$$
\operatorname{BoundaryCross}
\neq
\operatorname{Impossible}
$$

---

## 7.2 表示不變性與邊界

如果兩個端點只是不同表示：

$$
[P_1]=[P_2]
$$

則不應被判定為本體邊界穿越。

因此邊界判定必須先商掉表示差異。

---

## 7.3 元穩定與可能空間

多固定點會使可能空間分支：

$$
\Gamma_1^\ast
\Rightarrow
\Omega_1
$$

$$
\Gamma_2^\ast
\Rightarrow
\Omega_2
$$

因此可能空間可能依賴元治理制度。

---

## 7.4 身份與本體邊界

若某干預保留物理結構，卻改寫：

$$
\Gamma_I
$$

則可能發生身份本體邊界穿越。

所以邊界不能只看物理或拓撲不變量。

---

# 8. 第三批次後的更新核心

## 8.1 世界與模型的可能性分離

世界層：

$$
\boxed{
\Omega_W
}
$$

模型層：

$$
\boxed{
\Omega_M^-
\subseteq
\Omega_W
\subseteq
\Omega_M^+
}
$$

---

## 8.2 路徑化本體邊界

$$
\boxed{
\mathcal B_\eta(O)
=
\left\{
O'
\mid
\operatorname{BCert}(O,O';\eta)
\right\}
}
$$

---

## 8.3 表示商上的語義張力

$$
\boxed{
\widetilde{\mathcal T}
:
[P_1]\times[P_2]
\rightarrow
\mathbb R_{\geq0}^n
}
$$

並分離：

$$
\vec{\mathcal T}_{\mathrm{sem}}
$$

與：

$$
\vec{\mathcal T}_{\mathrm{rep}}
$$

---

## 8.4 元穩定系統

$$
\boxed{
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
}
$$

---

## 8.5 身份延續完整標籤

$$
\boxed{
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
}
$$

---

# 9. 本批次新形成的穩定區

## 9.1 可達不等於真可能

$$
\Diamond_M O'
\not\Rightarrow
\Diamond_W O'
$$

且：

$$
\Diamond_W O'
\not\Rightarrow
\Diamond_M O'
$$

---

## 9.2 不變量不是邊界充分條件

$$
\operatorname{SameInvariant}
\not\Rightarrow
\operatorname{SameOntology}
$$

---

## 9.3 張力必須商掉表示差異

$$
T_{\mathrm{sem}}
\neq
T_{\mathrm{rep}}
$$

---

## 9.4 元約束不必有唯一固定點

多穩態與週期可能仍具操作性。

---

## 9.5 身份延續強度不是身份百分比

$$
\mathbf c_I
$$

描述連續結構，不是「多少比例為同一人」。

---

# 10. 仍未解決的高張力問題

## 10.1 可能性下界的見證是否真的可靠

模型可能錯誤地把某種構造見證當成世界可能見證。

---

## 10.2 邊界證書的充分性仍未證明

即使有不變量、生成連續、恢復映射與歷史路徑，也可能存在更深的本體差異。

---

## 10.3 語義等價可能不可判定

若：

$$
[P_1]=[P_2]
$$

本身不可判定，語義張力只能近似。

---

## 10.4 多固定點選擇可能被權力支配

制度可能以治理權力決定哪個固定點成為有效現實。

---

## 10.5 身份分類可能反向依賴制度

$$
J_I
$$

可能並非純粹描述，而會被法律與治理規則部分構成。

---

# 11. 更新後的研究佇列

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 可能性見證與不可能性證書的可靠性 | 決定可能上下界品質 |
| 2 | 邊界證書的反例壓力測試 | 決定 intra／trans 分類可靠性 |
| 3 | 語義等價不可判定時的近似策略 | 決定張力計算可實作性 |
| 4 | 多固定點的治理與選擇合法性 | 連接本體與權力 |
| 5 | 制度對身份分類的反向構成 | 連接身份與治理 |
| 6 | 四值、機率與模糊性的正式分離 | 模型判定仍不完整 |
| 7 | 可能空間與張力計算複雜度 | 進入演算法評估 |
| 8 | 世界真可能是否需要新的原始模態項 | 可能改寫核心本體 |

---

# 12. 圖更新摘要

## 12.1 新增節點

本批次新增：

$$
8+7+8+8+7=38
$$

個子節點。

---

## 12.2 新增主要關係

```text
is_syntactically_possible
is_model_possible
is_world_possible
lower_bounds
upper_bounds
witnesses_possibility
certifies_impossibility
preserves_invariant
preserves_generation
recovers_core
traces_boundary_path
is_representation_equivalent
has_semantic_cost
has_representation_cost
has_multiple_fixed_points
has_periodic_attractor
is_meta_stable
has_continuity_profile
has_identity_confidence
has_identity_classification
allocates_normative_effect
```

---

## 12.3 圖版本更新

輸入：

$$
\mathcal G_{\mathrm{FMO}}^{(2)}
$$

輸出：

$$
\boxed{
\mathcal G_{\mathrm{FMO}}^{(3)}
}
$$

---

# 13. 本批次結論

第三批次處理的不是新概念擴張，而是第二批操作架構中最容易被誤用的五個位置。

第一，可能空間被分成模型可達與世界真可能。模型不再宣稱可以完全列舉世界可能，而只維護：

$$
\boxed{
\Omega_M^-
\subseteq
\Omega_W
\subseteq
\Omega_M^+
}
$$

第二，本體邊界不再由核心不變量單獨決定，而改用路徑化邊界證書：

$$
\boxed{
\operatorname{BCert}
=
\operatorname{InvPres}
\land
\operatorname{GenCont}
\land
\operatorname{Recover}
\land
\operatorname{Trace}
}
$$

第三，本體張力不再直接依賴單一表示，而被分成語義張力與表示張力：

$$
\boxed{
\vec{\mathcal T}_{\mathrm{sem}}
\neq
\vec{\mathcal T}_{\mathrm{rep}}
}
$$

第四，元約束不再被限制為唯一固定點，而以更一般的元穩定分類處理：

$$
\boxed{
\mathsf{UniqueStable},
\mathsf{MultiStable},
\mathsf{Periodic},
\mathsf{BoundedDynamic},
\mathsf{Divergent}
}
$$

第五，身份延續強度不再被誤解為身份真值百分比，而被拆成：

$$
\boxed{
\mathbf c_I
+
q_I
+
J_I
+
\mathbf r_I
}
$$

分別表示結構連續、認識信心、身份分類與制度效果。

因此，本批次後的事實模態本體論開始具備一個更嚴格的分離原則：

$$
\boxed{
\text{世界}
\neq
\text{模型}
\neq
\text{表示}
\neq
\text{制度判定}
}
$$

世界真可能不能被模型可達取代。

本體同一不能被不變量相同取代。

語義張力不能被編輯次數取代。

元穩定不能被唯一固定點取代。

身份延續不能被單一百分比取代。

這五項分離，使理論避免在進入計算化之前，把模型方便性誤當成世界本體結構。

---

## 附錄 A：第三批次最小 JSON

```json
{
  "batch": "FMO-MRASG-003",
  "input_graph": "G_FMO_2",
  "output_graph": "G_FMO_3",
  "selected_nodes": [
    "FMO-211",
    "FMO-208",
    "FMO-212",
    "FMO-102K",
    "FMO-202L"
  ],
  "decisions": [
    {
      "node": "FMO-211",
      "result": "separate_model_reachability_from_world_possibility"
    },
    {
      "node": "FMO-208",
      "result": "path_indexed_boundary_certificate"
    },
    {
      "node": "FMO-212",
      "result": "semantic_tension_on_representation_quotient"
    },
    {
      "node": "FMO-102K",
      "result": "generalized_meta_stability"
    },
    {
      "node": "FMO-202L",
      "result": "separate_continuity_confidence_identity_and_normative_effect"
    }
  ],
  "next_queue": [
    "possibility_witness_reliability",
    "boundary_certificate_stress_test",
    "semantic_equivalence_approximation",
    "multistable_governance_legitimacy",
    "institutional_reverse_identity_constitution"
  ]
}
```

---

## 附錄 B：版本狀態

**批次狀態：** 已完成  
**理論狀態：** 世界／模型／表示／制度四層分離完成  
**圖版本：** $\mathcal G_{\mathrm{FMO}}^{(3)}$  
**下一階段：** 證書可靠性、反例壓力測試、近似計算與治理合法性  
