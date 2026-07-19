# FMO–MRASG 第六研究批次

## 外部錨點、邊界校準、搜尋停止、底線衝突與身份反事實估計

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

第五批次建立了反身封閉風險的初步治理架構。

主要成果包括：

$$
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
$$

長期邊界狀態：

$$
\operatorname{BStatus}
=
\left\langle
\mathbf B,
\mathbf D_B,
\mathcal K_B,
\operatorname{Hyst}_B,
\mathcal S_\eta
\right\rangle
$$

偏誤感知語義近似：

$$
\mathbf E_{\mathcal O_E}(P_1,P_2)
$$

不可補償合法性：

$$
\forall j\in\mathcal N_L,
\quad
L_j\geq\theta_j
$$

以及身份去僭越審計：

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

但第五批次也暴露出五個更深問題。

第一，證書網路需要外部錨點，但外部錨點本身也可能受到觀測誤差、制度選擇與資料偏誤影響。

第二，本體邊界的自適應門檻仍缺乏可測試的校準方法。

第三，對抗性維度搜尋若沒有停止規則，可能使比較永遠無法收斂。

第四，不可補償底線彼此之間也可能直接衝突。

第五，身份去僭越需要反事實基線，但「沒有制度干預時會怎樣」通常不可直接觀測。

因此，本批次處理以下五個節點：

```text
FMO-223  外部錨點的可信度與觀測者依賴
FMO-224  邊界案例庫與門檻校準
FMO-225  對抗性維度搜尋的停止條件
FMO-226  不可補償底線之間的衝突
FMO-227  身份反事實基線的估計與不確定性
```

本批次的核心問題是：

> 當理論必須與世界、案例與反事實估計接軌時，如何避免把觀測、校準與停止規則本身當成無條件真理？

---

# 1. 輸入圖

第五批次輸出：

$$
\mathcal G_{\mathrm{FMO}}^{(5)}
$$

其主要結構包括：

證書錨點：

$$
a\in\mathcal A_C
$$

多尺度邊界漂移：

$$
\mathbf D_B(\eta)
=
\left[
D_B^{\sigma,\ell}
\right]
$$

語義觀測架構：

$$
\mathcal O_E
=
\{q_1,\ldots,q_n\}
$$

不可補償底線集合：

$$
\mathcal N_L
$$

身份反事實差異：

$$
\Delta_{\mathrm{inst}}
=
\mathbf c_I^{\mathrm{obs}}
-
\mathbf c_I^{\mathrm{cf}}
$$

---

# 2. 節點 A：外部錨點的可信度與觀測者依賴

## A-R0：點層

> 外部錨點不是無條件真理入口，而是受觀測條件、測量工具、選樣制度、翻譯鏈與觀測者位置限制的世界接口。

## A-R1：線層

第五批次要求證書網路必須具有外部錨點：

$$
a\in\mathcal A_C
$$

錨點可能是世界觀測、實驗、原始資料、直接構造、可重複測量、機器驗證或獨立實作。

然而，外部錨點仍可能測量錯誤、受到取樣偏差、被制度性過濾、被錯誤翻譯、只在特定尺度成立、被觀測行為改變，或因資料權力而被選擇性保存。

所以「外部」不等於「無偏」。

## A-R2：面層

### A1. 錨點描述子

$$
a
=
\left\langle
target,
observer,
instrument,
protocol,
context,
sampling,
translation,
disturbance,
provenance,
version
\right\rangle
$$

### A2. 錨點是接口鏈

$$
W
\xrightarrow{\mathcal O}
D_{\mathrm{raw}}
\xrightarrow{\mathcal T_1}
D_{\mathrm{clean}}
\xrightarrow{\mathcal T_2}
F_M
\xrightarrow{\mathcal I}
C
$$

其中每一段都可能引入誤差。

### A3. 觀測者位置

$$
\mathsf{Pos}(o)
=
\left\langle
access,
scale,
interest,
power,
risk,
embodiment,
history
\right\rangle
$$

因此：

$$
\operatorname{Observe}_o(W)\neq W
$$

### A4. 觀測不完備

若：

$$
x\notin\operatorname{Range}(\mathcal O)
$$

只能說目前觀測架構無法取得 $x$ ，不能推出：

$$
\neg\operatorname{Exists}(x)
$$

### A5. 觀測干擾

$$
W
\xrightarrow{\mathcal O}
W'
$$

若 $W'\neq W$ ，資料描述的是受觀測影響後的狀態。

### A6. 多錨點三角校準

$$
\mathcal A^\ast=\{a_1,\ldots,a_n\}
$$

不同方法、觀測者與資料鏈若收斂，可信度提高，但必須扣除來源相關性：

$$
R_A(i,j)
$$

### A7. 錨點衝突

若：

$$
a_1\Rightarrow F
$$

而：

$$
a_2\Rightarrow\neg F
$$

需要對齊指涉、尺度、時間、制度、干擾與翻譯規則。

### A8. 錨點可信度輪廓

$$
\mathbf T_A(a)
=
\left\langle
T_{\mathrm{access}},
T_{\mathrm{instrument}},
T_{\mathrm{protocol}},
T_{\mathrm{sampling}},
T_{\mathrm{translation}},
T_{\mathrm{independence}},
T_{\mathrm{disturbance}},
T_{\mathrm{audit}}
\right\rangle
$$

### A9. 錨點狀態

$$
\operatorname{AnchorStatus}
\in
\{
\mathsf{Calibrated},
\mathsf{Qualified},
\mathsf{Contested},
\mathsf{Drifting},
\mathsf{Compromised},
\mathsf{Superseded},
\mathsf{Unknown}
\}
$$

### A10. 世界接口謙抑原則

模型不得由單一錨點推出：

$$
F_M=F_W
$$

只能宣稱 $F_M$ 是透過特定接口鏈形成的有條件表徵。

## A-局部決定

$$
\boxed{
\mathfrak A_W
=
\left\langle
a,
\mathcal O,
\mathcal T,
\mathsf{Pos},
R_A,
\mathbf T_A,
\operatorname{AnchorStatus}
\right\rangle
}
$$

外部錨點可提高證書可信度，但不能被視為無條件、無觀測者的世界真理。

---

# 3. 節點 B：邊界案例庫與門檻校準

## B-R0：點層

> 本體邊界門檻不能只由抽象直覺決定，必須透過正例、反例、近邊界例、對抗例與跨領域案例進行校準。

## B-R1：線層

第五批次建立：

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

但若沒有案例庫，門檻仍只是形式符號。

因此建立：

$$
\mathcal D_B
$$

即本體邊界案例資料庫。

## B-R2：面層

### B1. 案例結構

$$
b
=
\left\langle
O_0,
\eta,
O_n,
layers,
evidence,
judgments,
outcomes,
disputes,
version
\right\rangle
$$

### B2. 六類案例

1. 明確延續正例；
2. 明確斷裂反例；
3. 近邊界案例；
4. 欺騙性相似案例；
5. 欺騙性差異案例；
6. 對抗案例。

### B3. 跨領域案例

涵蓋生物個體、人格與記憶、法人、軟體、AI 模型、組織、國家制度、語言、生態系統、科學理論與數位身份。

### B4. 爭議分布標註

$$
\mathcal J_B(b)=\{J_1,\ldots,J_m\}
$$

並保存每位判定者的觀測位置：

$$
\mathsf{Pos}(J_i)
$$

### B5. 風險敏感門檻

$$
\mathcal L_B(\theta)
=
\alpha FP
+
\beta FN
+
\gamma C_{\mathrm{irrev}}
+
\delta C_{\mathrm{rights}}
+
\epsilon C_{\mathrm{uncert}}
$$

### B6. 關鍵斷裂優先

判定流程為：

1. 檢查關鍵斷裂；
2. 檢查祖源；
3. 檢查歷史滯後；
4. 再使用校準門檻。

### B7. 校準與測試分離

$$
\mathcal D_B^{\mathrm{train}},
\quad
\mathcal D_B^{\mathrm{cal}},
\quad
\mathcal D_B^{\mathrm{test}}
$$

### B8. 對抗案例生成

$$
b^\ast
=
\arg\max_b
\operatorname{Instability}
\left(
\operatorname{BStatus}(b)
\right)
$$

### B9. 校準漂移

$$
\theta_{B,t}\neq\theta_{B,t+1}
$$

需要監測：

$$
\operatorname{CalibrationDrift}
$$

### B10. 邊界判定卡

$$
\mathsf{BoundaryCard}
=
\left\langle
\text{case\_family},
threshold,
\text{critical\_breaks},
uncertainty,
analogues,
dissent,
version
\right\rangle
$$

## B-局部決定

$$
\boxed{
\mathcal D_B
=
\mathcal D_B^{\mathrm{train}}
\cup
\mathcal D_B^{\mathrm{cal}}
\cup
\mathcal D_B^{\mathrm{test}}
}
$$

門檻由關鍵斷裂規則、案例校準、任務風險、權利成本、對抗測試與校準漂移共同決定。

---

# 4. 節點 C：對抗性維度搜尋的停止條件

## C-R0：點層

> 對抗性維度搜尋不追求「再也找不到任何差異」，而是在任務風險、搜尋收益、證據穩定與資源限制下達到可辯護停止。

## C-R1：線層

第五批次建立：

$$
q^\ast
=
\arg\max_q
\operatorname{Disc}_q(P_1,P_2)
$$

但任何兩個不同本體幾乎都能找到更多差異，因此需要停止規則。

## C-R2：面層

### C1. 邊際區分收益

$$
\Delta_t
=
\operatorname{DiscGain}(q_t)
$$

### C2. 風險加權收益

$$
\Delta_t^{R}
=
\operatorname{DiscGain}(q_t)
\times
\operatorname{RiskImpact}(q_t)
$$

### C3. 停止條件族

- 收益飽和；
- 判定穩定；
- 關鍵風險覆蓋；
- 對抗測試通過；
- 資源上限。

### C4. 停止狀態

$$
\operatorname{StopStatus}
\in
\{
\mathsf{Sufficient},
\mathsf{RiskBounded},
\mathsf{Provisional},
\mathsf{ResourceLimited},
\mathsf{Forced},
\mathsf{Unresolved}
\}
$$

### C5. 可重啟條件

若出現新反例、新利益相關者、新技術、新高風險領域、新資料或觀測架構漂移，則：

$$
\operatorname{Reopen}(\mathcal O_E)
$$

### C6. 搜尋債務

因資源或時程提前停止時，記錄：

$$
D_E
$$

其中包括尚未測試的維度族、已知盲區、可能受影響者與重啟條件。

### C7. 維度冗餘

若：

$$
q_{\mathrm{new}}
\in
\operatorname{Span}_\epsilon(\mathcal O_E)
$$

需區分語義冗餘、測量冗餘與治理冗餘。

### C8. 反例覆蓋率

$$
\operatorname{Cov}(\mathcal O_E,\mathcal R_E)
$$

覆蓋不足不得宣稱任務充分。

### C9. 多代理停止

保留不同代理的停止分歧：

$$
\operatorname{StopDissent}
$$

### C10. 停止證書

$$
\mathsf{StopCert}
=
\left\langle
task,
risk,
coverage,
\text{marginal\_gain},
\text{critical\_flags},
budget,
dissent,
debt,
reopen
\right\rangle
$$

## C-局部決定

$$
\boxed{
\operatorname{Stop}
\iff
\operatorname{Saturation}
\land
\operatorname{DecisionStable}
\land
\operatorname{CriticalCovered}
\land
\operatorname{RiskAcceptable}
}
$$

若只因資源限制停止，必須標記 $\mathsf{ResourceLimited}$ ，並保存搜尋債務。

---

# 5. 節點 D：不可補償底線之間的衝突

## D-R0：點層

> 不可補償底線也可能彼此衝突；此時不能用普通加權求和，而應建立底線優先圖、最小侵害原則、臨時例外證書與殘餘損害記錄。

## D-R1：線層

第五批次要求：

$$
\forall j\in\mathcal N_L,\quad L_j\geq\theta_j
$$

但隱私與透明、安全與程序、自主與公共保護可能直接衝突。

## D-R2：面層

### D1. 底線衝突

$$
\operatorname{FloorConflict}(N_i,N_j\mid c)
$$

### D2. 底線優先圖

$$
G_N=(V_N,E_N)
$$

邊表示條件優先、絕對禁止、暫時讓位、需要補償、互相支持或不可共同滿足。

### D3. 情境化優先

$$
\operatorname{Priority}
=
\operatorname{Priority}(N_i,N_j\mid c)
$$

不預設全域固定排序。

### D4. 最小侵害原則

$$
a^\ast
=
\arg\min_a
\operatorname{Harm}_{\mathcal N_L}(a)
$$

### D5. 底線侵害報告

$$
\mathsf{FloorBreach}
=
\left\langle
floor,
reason,
scope,
duration,
affected,
alternatives,
mitigation,
review
\right\rangle
$$

### D6. 例外證書

$$
\mathsf{ExceptionCert}
=
\left\langle
conflict,
necessity,
proportionality,
duration,
reversibility,
compensation,
oversight,
expiry
\right\rangle
$$

### D7. 候選絕對元底線

$$
\mathcal N_L^{\mathrm{abs}}
$$

候選包括：

- 禁止偽造證據；
- 禁止把制度決定偽裝成世界真理；
- 禁止隱藏已知重大受害；
- 禁止取消所有申訴與審查路徑；
- 禁止無限期擴張緊急例外。

### D8. 多方審查

納入受影響者、反對者、專業判定、獨立審查、少數者與後續承擔者。

### D9. 殘餘損害

$$
H_{\mathrm{res}}
$$

需要記錄、補償、追蹤與後續修復。

### D10. 衝突狀態

$$
\operatorname{FloorConflictStatus}
\in
\{
\mathsf{Resolved},
\mathsf{Minimized},
\mathsf{Provisional},
\mathsf{Deadlocked},
\mathsf{IllegitimateOverride},
\mathsf{Undetermined}
\}
$$

## D-局部決定

$$
\boxed{
\mathcal N_L
=
\mathcal N_L^{\mathrm{abs}}
\cup
\mathcal N_L^{\mathrm{context}}
}
$$

情境底線衝突時採最小侵害、例外證書、時限、可逆性、殘餘損害記錄與多方審查。

---

# 6. 節點 E：身份反事實基線的估計與不確定性

## E-R0：點層

> 身份反事實基線通常不可直接觀測，只能透過多模型、近鄰案例、結構因果與敏感度分析形成區間估計，不能假裝得到唯一無制度世界。

## E-R1：線層

第五批次使用：

$$
\Delta_{\mathrm{inst}}
=
\mathbf c_I^{\mathrm{obs}}
-
\mathbf c_I^{\mathrm{cf}}
$$

但 $\mathbf c_I^{\mathrm{cf}}$ 通常不可直接觀測。

## E-R2：面層

### E1. 反事實基線描述子

$$
\mathsf{CFBase}_I
=
\left\langle
target,
intervention,
time,
model,
comparators,
assumptions,
range,
uncertainty,
version
\right\rangle
$$

### E2. 結構因果估計

$$
\mathbf c_I^{\mathrm{cf}}
=
\mathbf c_I
\left(
do(\mathsf{Institution}=0)
\right)
$$

其結果依賴因果圖、未觀測混淆、干預定義、時間與主體適應。

### E3. 近鄰比較

尋找：

$$
x'\approx x
$$

作為比較，但需保存可比性誤差。

### E4. 縱向比較

$$
\mathbf c_I(t_0)
$$

與：

$$
\mathbf c_I(t_1)
$$

之間必須分離時間變化與制度變化。

### E5. 多模型估計

$$
\mathcal C_I^{\mathrm{cf}}
=
\left\{
\mathbf c_{I,1}^{\mathrm{cf}},
\ldots,
\mathbf c_{I,k}^{\mathrm{cf}}
\right\}
$$

### E6. 反事實區間

$$
\underline{\mathbf c}_I^{\mathrm{cf}}
\preceq
\mathbf c_I^{\mathrm{cf}}
\preceq
\overline{\mathbf c}_I^{\mathrm{cf}}
$$

制度效應也形成區間。

### E7. 敏感度分析

$$
S_I
=
\frac{\partial \Delta_{\mathrm{inst}}}{\partial u}
$$

若對未觀測混淆高度敏感，不能使用強因果語氣。

### E8. 主體適應效應

$$
\operatorname{Adapt}(x\mid do(I=0))
$$

不能假定移除制度後其他條件不變。

### E9. 制度替代效應

真正反事實可能是：

$$
I\rightarrow I'
$$

而不是簡單 $I=0$ 。

### E10. 不可識別

若：

$$
\operatorname{Identifiable}
\left(
\mathbf c_I^{\mathrm{cf}}
\right)=0
$$

則輸出：

$$
\mathsf{NotIdentified}
$$

### E11. 主體反事實見證

$$
w_{\mathrm{self}}^{\mathrm{cf}}
$$

屬於重要但非唯一的證據。

### E12. 身份反事實估計卡

$$
\mathsf{CFIdentityCard}
=
\left\langle
models,
comparators,
assumptions,
interval,
sensitivity,
adaptation,
alternatives,
identifiability,
dissent
\right\rangle
$$

## E-局部決定

身份反事實基線改為多模型集合與區間：

$$
\boxed{
\mathcal C_I^{\mathrm{cf}}
}
$$

$$
\boxed{
\underline{\mathbf c}_I^{\mathrm{cf}}
\preceq
\mathbf c_I^{\mathrm{cf}}
\preceq
\overline{\mathbf c}_I^{\mathrm{cf}}
}
$$

並要求因果假設、敏感度、主體適應、制度替代、不可識別標記與主體自身敘述。

---

# 7. 跨節點對齊

五個節點共同建立：

> 理論與世界接軌時，不只需要資料，也需要描述資料如何產生、如何校準、何時停止，以及哪些結論仍不可識別。

## 7.1 外部錨點與身份反事實

$$
\operatorname{CFEstimateQuality}
\leq
\operatorname{AnchorQuality}
$$

若原始記錄被制度控制，反事實估計會繼承制度偏誤。

## 7.2 邊界案例與觀測位置

案例共識不等於無觀測者真理。案例庫必須保存判定者、受影響者、制度位置與時代背景。

## 7.3 搜尋停止與合法性

因資源停止搜尋會累積：

$$
D_E
$$

並降低治理選擇的資訊與透明度合法性。

## 7.4 底線衝突與反事實估計

判斷某項底線侵害是否必要，通常依賴反事實，因此例外證書也必須附帶反事實不確定性。

## 7.5 統一判定卡

五個節點都需要結構化輸出：

- Anchor Card；
- Boundary Card；
- Stop Certificate；
- Floor Breach Report；
- CF Identity Card。

這表示理論正形成統一的可審計輸出格式。

---

# 8. 第六批次後的更新核心

## 8.1 世界接口系統

$$
\boxed{
\mathfrak A_W
=
\left\langle
a,
\mathcal O,
\mathcal T,
\mathsf{Pos},
R_A,
\mathbf T_A,
\operatorname{AnchorStatus}
\right\rangle
}
$$

## 8.2 邊界校準系統

$$
\boxed{
\mathfrak B_C
=
\left\langle
\mathcal D_B,
\mathcal A_B,
\Theta_B,
\mathcal L_B,
\operatorname{CalibrationDrift},
\mathsf{BoundaryCard}
\right\rangle
}
$$

## 8.3 搜尋停止系統

$$
\boxed{
\mathfrak S_E
=
\left\langle
\Delta^R,
\operatorname{Cov},
\operatorname{StopStatus},
D_E,
\operatorname{Reopen},
\mathsf{StopCert}
\right\rangle
}
$$

## 8.4 底線衝突系統

$$
\boxed{
\mathfrak N_L
=
\left\langle
\mathcal N_L^{\mathrm{abs}},
\mathcal N_L^{\mathrm{context}},
G_N,
\mathsf{ExceptionCert},
H_{\mathrm{res}},
\operatorname{FloorConflictStatus}
\right\rangle
}
$$

## 8.5 身份反事實估計系統

$$
\boxed{
\mathfrak{CF}_I
=
\left\langle
\mathcal C_I^{\mathrm{cf}},
\underline{\mathbf c}_I^{\mathrm{cf}},
\overline{\mathbf c}_I^{\mathrm{cf}},
S_I,
\mathcal B_I^{\mathrm{cf}},
\mathsf{CFIdentityCard}
\right\rangle
}
$$

---

# 9. 本批次新形成的穩定區

1. 外部錨點是世界接口，不是世界本身；
2. 邊界門檻必須案例校準；
3. 對抗搜尋採任務充分停止；
4. 不可補償底線仍需衝突治理；
5. 身份反事實基線是區間與模型集合。

---

# 10. 仍未解決的高張力問題

## 10.1 世界接口可能無限回歸

若每個錨點都需要另一個錨點校準，可能形成元觀測回歸。

## 10.2 案例庫可能固化既有偏見

歷史案例的主流判定可能排除少數者與新型主體。

## 10.3 搜尋停止仍依賴風險模型

若風險模型漏掉某類傷害，停止證書仍可能過早收斂。

## 10.4 絕對元底線的來源尚未公理化

目前只是候選集合，尚未證明其普遍地位。

## 10.5 身份反事實可能多重不可識別

多個因果模型可能同樣符合觀測，卻給出不同制度效果。

---

# 11. 更新後的研究佇列

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 元觀測回歸與錨點終止條件 | 世界接口仍可能無限上推 |
| 2 | 案例庫偏見與新型主體外推 | 邊界校準可能固化舊世界 |
| 3 | 風險模型盲區與停止證書可靠性 | 搜尋停止仍可能過早 |
| 4 | 絕對元底線的來源與可辯護性 | 治理核心仍未封閉 |
| 5 | 多重不可識別的身份反事實 | 去僭越審計可能無唯一答案 |
| 6 | 四值、機率、模糊、證書與區間統合 | 判定層仍需總整理 |
| 7 | 判定卡統一資料格式 | 準備計算原型 |
| 8 | 來源歷史升格為核心維度的可行性 | 理論核心可能再次更新 |

---

# 12. 圖更新摘要

本批次新增：

$$
10+10+10+10+12=52
$$

個子節點。

主要新增關係包括：

```text
anchors_world_interface
is_observer_positioned
is_instrument_mediated
is_observation_incomplete
disturbs_observed_system
triangulates_anchor
calibrates_boundary_threshold
belongs_to_boundary_case_family
generates_adversarial_boundary_case
stops_dimension_search
reopens_dimension_search
creates_search_debt
conflicts_with_floor
temporarily_overrides_floor
leaves_residual_harm
estimates_identity_counterfactual
is_counterfactually_unidentified
depends_on_adaptation
depends_on_institutional_substitute
```

圖版本更新：

$$
\boxed{
\mathcal G_{\mathrm{FMO}}^{(5)}
\rightarrow
\mathcal G_{\mathrm{FMO}}^{(6)}
}
$$

---

# 13. 本批次結論

第六批次將事實模態本體論從「能防止反身封閉」推進到「能處理世界接口與校準不確定性」。

第一，外部錨點不再被視為無條件真實來源，而被建模為：

$$
\boxed{
W
\xrightarrow{\mathcal O}
D_{\mathrm{raw}}
\xrightarrow{\mathcal T_1}
D_{\mathrm{clean}}
\xrightarrow{\mathcal T_2}
F_M
\xrightarrow{\mathcal I}
C
}
$$

即一條具有觀測者、工具、取樣、翻譯與干擾的世界接口鏈。

第二，本體邊界門檻需要透過正例、反例、近邊界案例、欺騙性案例與對抗案例建立校準資料庫。

第三，對抗性維度搜尋建立可辯護停止條件：

$$
\boxed{
\operatorname{Saturation}
\land
\operatorname{DecisionStable}
\land
\operatorname{CriticalCovered}
\land
\operatorname{RiskAcceptable}
}
$$

第四，不可補償底線被分成：

$$
\boxed{
\mathcal N_L^{\mathrm{abs}}
\cup
\mathcal N_L^{\mathrm{context}}
}
$$

情境底線衝突時採最小侵害、例外證書、時限、補償與殘餘損害記錄。

第五，身份反事實基線不再被表示成單一虛構值，而是多模型集合與區間估計。

因此，本批次形成新的總體原則：

$$
\boxed{
\text{世界接口、案例校準、搜尋停止與反事實估計，}
\newline
\text{都必須把不可見部分與不可識別部分一起輸出。}
}
$$

一套可信的本體系統不只要說它看見了什麼，也必須說：

- 透過什麼看見；
- 哪些部分看不見；
- 門檻如何校準；
- 搜尋為何停止；
- 哪些底線互相衝突；
- 哪些反事實無法唯一識別。

至此，事實模態本體論開始具有真正的「世界接口層」：

$$
\boxed{
\text{世界}
\rightarrow
\text{觀測}
\rightarrow
\text{資料}
\rightarrow
\text{模型}
\rightarrow
\text{證書}
}
$$

每一步都可能產生差異、偏誤與未決。

---

## 附錄 A：第六批次最小 JSON

```json
{
  "batch": "FMO-MRASG-006",
  "input_graph": "G_FMO_5",
  "output_graph": "G_FMO_6",
  "selected_nodes": [
    "FMO-223",
    "FMO-224",
    "FMO-225",
    "FMO-226",
    "FMO-227"
  ],
  "decisions": [
    {
      "node": "FMO-223",
      "result": "observer_positioned_world_interface_anchor"
    },
    {
      "node": "FMO-224",
      "result": "risk_sensitive_case_calibrated_boundary_thresholds"
    },
    {
      "node": "FMO-225",
      "result": "defensible_reopenable_adversarial_search_stopping"
    },
    {
      "node": "FMO-226",
      "result": "absolute_and_contextual_floor_conflict_governance"
    },
    {
      "node": "FMO-227",
      "result": "interval_and_multimodel_identity_counterfactual_estimation"
    }
  ],
  "next_queue": [
    "meta_observation_regress",
    "case_library_bias",
    "risk_model_blind_spots",
    "absolute_meta_floor_justification",
    "multiple_nonidentifiable_identity_counterfactuals"
  ]
}
```

---

## 附錄 B：版本狀態

**批次狀態：** 已完成  
**理論狀態：** 世界接口、案例校準、搜尋停止、底線衝突與反事實估計已形成  
**圖版本：** $\mathcal G_{\mathrm{FMO}}^{(6)}$  
**下一階段：** 元觀測終止、案例偏見、風險盲區、元底線來源與多重不可識別  
