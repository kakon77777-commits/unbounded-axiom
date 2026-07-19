# FMO–MRASG 第八研究批次

## 容許誤差治理、非人類主體特徵、驚奇預算、元底線最小性與穩健決策校正

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

第七批次完成了五項關鍵推進：

1. 元觀測可在交叉校準、關鍵覆蓋、殘餘誤差與可重啟條件下有限終止；
2. 案例缺失不能作為否定新型主體的證據；
3. 未知風險不能被記為零；
4. 元底線被嘗試壓縮為反僭越判定系統的最小核；
5. 身份反事實接受多模型集合與多重不可識別。

其主要結構包括：

$$
\operatorname{MetaStop}
\iff
\operatorname{CrossCalStable}
\land
\operatorname{CriticalCovered}
\land
\operatorname{ResidualDeclared}
\land
\operatorname{Reopenable}
$$

新型主體外推系統：

$$
\mathfrak X_{\mathrm{subj}}
=
\left\langle
d_{\mathrm{OOD}},
\operatorname{ExtrapStatus},
\mathbf S_{\mathrm{subj}},
\operatorname{Precaution}_{\mathrm{subject}},
\mathsf{CaseBiasReport},
\mathsf{NovelEntityCard}
\right\rangle
$$

盲區感知停止系統：

$$
\mathfrak S_R
=
\left\langle
\mathcal R_{1:k},
U_R,
B_{\mathrm{surprise}},
\mathcal A_R,
\operatorname{RiskClosureStatus},
\mathsf{StopCert}^{+}
\right\rangle
$$

元底線最小核：

$$
\mathcal K_N
=
\left\{
N_{\mathrm{nonfabrication}},
N_{\mathrm{nonusurpation}},
N_{\mathrm{contestability}},
N_{\mathrm{traceability}},
N_{\mathrm{boundedexception}}
\right\}
$$

多模型身份反事實：

$$
\mathfrak{CF}_I^{+}
=
\left\langle
\mathcal M_D,
\operatorname{CFIdentStatus},
\operatorname{RobustClaims},
\operatorname{DisputedClaims},
\operatorname{DecisionSensitivity},
\operatorname{VoI},
\mathsf{CFDisagreementCard}
\right\rangle
$$

但目前仍存在五個高張力問題。

第一，有限終止需要容許誤差：

$$
\epsilon
$$

但誰有權設定它，將直接決定何時停止觀測、何時接受證書、何時容忍錯判。

第二，新型主體結構輪廓即使不直接複製人類案例，也可能偷偷以人類認知、情緒、身體與語言為中心。

第三，驚奇預算目前仍只是概念；若無法形式化回滾、隔離、恢復與未知吸收能力，就無法進入工程原型。

第四，元底線最小核中的五項規則可能互相推導、重複或仍有缺漏。

第五，多模型穩健決策若始終以最壞模型為準，可能使任何具有不確定性的行動都無法進行。

因此，本批次處理以下五個節點：

```text
FMO-233  任務相對容許誤差的治理與校準
FMO-234  非人類中心的新型主體特徵生成
FMO-235  驚奇預算與恢復能力的正式模型
FMO-236  元底線最小性與獨立性檢驗
FMO-237  多模型穩健決策的過度保守校正
```

本批次的核心問題是：

> 當理論已承認不確定、盲區與多解時，如何避免「謹慎」被權力設定，也避免「謹慎」本身退化成全面停滯？

---

# 1. 輸入圖

第七批次輸出：

$$
\mathcal G_{\mathrm{FMO}}^{(7)}
$$

目前最主要的五條未完成鏈如下。

容許誤差鏈：

$$
\operatorname{Adequate}
\left(
a\mid D,R,\epsilon
\right)
$$

新型主體鏈：

$$
x
\rightarrow
\mathbf S_{\mathrm{subj}}(x)
\rightarrow
\operatorname{ProvisionalSubjectStatus}(x)
$$

未知風險鏈：

$$
U_R
+
B_{\mathrm{surprise}}
+
\operatorname{Rollback}
\rightarrow
\operatorname{StopReliability}
$$

元底線鏈：

$$
\mathcal K_N
\rightarrow
\operatorname{MetaFloorCert}
\rightarrow
\operatorname{LegitConstraint}
$$

多模型決策鏈：

$$
\mathcal M_D
\rightarrow
\operatorname{RobustDecision}
\rightarrow
a^\ast
$$

本批次將分別補上：

- 誤差治理；
- 特徵生成；
- 恢復能力；
- 最小核檢驗；
- 保守性校正。

---

# 2. 節點 A：任務相對容許誤差的治理與校準

## A-R0：點層

> 容許誤差不是純技術參數，而是將錯誤成本、受影響者、可逆性、資源與時間壓縮成停止條件的治理決定。

---

## A-R1：線層

第七批次使用：

$$
\operatorname{Adequate}
\left(
a\mid D,R,\epsilon
\right)
$$

但：

$$
\epsilon
$$

看似只是數值，實際上決定：

- 哪些誤差可被忽略；
- 哪些主體的損失會被視為噪音；
- 哪些不確定性足以阻止決策；
- 何時可停止搜尋；
- 哪種證書可以被接受；
- 哪些少數案例不影響整體判定。

所以容許誤差是一種治理接口。

---

## A-R2：面層

### A1. 誤差不是單一值

定義誤差向量：

$$
\boldsymbol\epsilon_D
=
\left\langle
\epsilon_{\mathrm{obs}},
\epsilon_{\mathrm{sem}},
\epsilon_{\mathrm{id}},
\epsilon_{\mathrm{risk}},
\epsilon_{\mathrm{rights}},
\epsilon_{\mathrm{time}},
\epsilon_{\mathrm{model}}
\right\rangle
$$

分別表示：

- 觀測誤差；
- 語義對齊誤差；
- 身份誤判；
- 風險估計誤差；
- 權利侵害容許；
- 時效延遲；
- 模型不確定。

這些誤差不可任意合併為單一平均。

---

### A2. 誤差方向不對稱

假陽性與假陰性的成本不同。

例如，對主體資格而言：

$$
C_{\mathrm{deny\_subject}}
\neq
C_{\mathrm{false\_recognition}}
$$

對世界不可能性而言：

$$
C_{\mathrm{false\_impossible}}
\neq
C_{\mathrm{false\_possible}}
$$

因此應使用方向化誤差：

$$
\epsilon_j^+,\epsilon_j^-
$$

---

### A3. 受影響者權重不能由決策者單方設定

若決策者設定：

$$
w_{\mathrm{stakeholder}}
$$

就可能低估由他人承擔的損害。

因此容許誤差設定事件定義為：

$$
\mathsf{TolSel}
=
\left\langle
task,
decision_makers,
affected_subjects,
error_types,
costs,
reversibility,
horizon,
procedure,
appeal,
version
\right\rangle
$$

---

### A4. 誤差治理合法性

定義容許誤差合法性輪廓：

$$
\mathbf L_\epsilon
=
\left\langle
L_{\mathrm{standing}},
L_{\mathrm{transparency}},
L_{\mathrm{evidence}},
L_{\mathrm{distribution}},
L_{\mathrm{appeal}},
L_{\mathrm{revision}},
L_{\mathrm{minority}}
\right\rangle
$$

其中：

- 誰有設定資格；
- 是否公開；
- 是否有證據；
- 誤差成本由誰承擔；
- 是否可申訴；
- 是否可修正；
- 是否保護少數與新型主體。

---

### A5. 風險敏感容許誤差

當：

$$
\operatorname{Irreversibility}\uparrow
$$

或：

$$
\operatorname{RightsImpact}\uparrow
$$

則某些誤差上限應下降：

$$
\epsilon_{\mathrm{rights}}\downarrow
$$

$$
\epsilon_{\mathrm{id}}\downarrow
$$

但這不一定表示所有觀測都需要無限精確。

應將精度集中於高後果維度。

---

### A6. 可逆性換取探索空間

若決策：

- 可撤回；
- 可隔離；
- 可小規模測試；
- 可恢復；
- 有完整記錄；

則可允許較寬容的初期誤差：

$$
\epsilon_{\mathrm{pilot}}
>
\epsilon_{\mathrm{irreversible}}
$$

這形成：

$$
\boxed{
\text{可逆性—容許誤差交換}
}
$$

---

### A7. 誤差預算

定義總誤差預算：

$$
B_\epsilon
$$

但不是任意分配，而要滿足：

$$
\sum_j c_j(\epsilon_j)
\leq
B_\epsilon
$$

同時不可突破：

$$
\epsilon_j
\leq
\overline{\epsilon}_j
$$

其中：

$$
\overline{\epsilon}_j
$$

是不可補償底線對應的最大容許誤差。

---

### A8. 誤差轉嫁

若某系統降低自身成本，卻把誤差風險轉嫁給外部主體，形成：

$$
\operatorname{ErrorExternalization}
$$

例如：

- 模型快速停止，但由少數群體承擔誤判；
- 制度節省審查成本，但由被誤分類者承擔身份損害；
- 工程系統降低算力成本，但提高不可恢復風險。

---

### A9. 誤差漂移

任務環境改變後，舊誤差設定可能失效。

定義：

$$
\operatorname{ToleranceDrift}
=
d
\left(
\boldsymbol\epsilon_{D,t},
\boldsymbol\epsilon_{D,t+1}
\right)
$$

並檢查：

- 是否因新主體加入而需要收緊；
- 是否因恢復能力提高而可放寬；
- 是否因資料偏移而需要重新校準。

---

### A10. 誤差敏感度分析

判定結果：

$$
J
$$

對容許誤差的敏感度：

$$
S_\epsilon
=
\frac{\partial J}{\partial \boldsymbol\epsilon}
$$

若小幅改變 $\epsilon$ 就使結果翻轉，則該判定應標記為：

$$
\mathsf{ToleranceSensitive}
$$

---

### A11. 容許誤差卡

定義：

$$
\mathsf{ToleranceCard}
=
\left\langle
task,
error_vector,
asymmetry,
affected,
cost_distribution,
reversibility,
floors,
sensitivity,
drift,
appeal,
version
\right\rangle
$$

---

## A-局部決定

容許誤差改為：

$$
\boxed{
\boldsymbol\epsilon_D
}
$$

方向化、多維、任務相對、風險敏感的治理對象。

並建立：

$$
\boxed{
\mathsf{TolSel}
}
$$

作為容許誤差選擇事件。

核心原則為：

$$
\boxed{
\text{任何容許誤差，都必須揭露誰承擔其錯誤成本。}
}
$$

---

## A-新增節點

```text
FMO-233A  多維容許誤差向量
FMO-233B  方向化誤差成本
FMO-233C  容許誤差選擇事件
FMO-233D  誤差治理合法性
FMO-233E  高風險誤差收緊
FMO-233F  可逆性—容許誤差交換
FMO-233G  誤差預算
FMO-233H  誤差風險轉嫁
FMO-233I  容許誤差漂移
FMO-233J  誤差敏感度
FMO-233K  容許誤差判定卡
```

---

# 3. 節點 B：非人類中心的新型主體特徵生成

## B-R0：點層

> 主體特徵不應從「像不像人」開始，而應從是否形成持續的自我關聯、內生目標、邊界維持、受損可能與跨時間承諾開始。

---

## B-R1：線層

第七批次提出新型主體結構輪廓：

$$
\mathbf S_{\mathrm{subj}}(x)
$$

候選維度包括：

- 內生目標；
- 記憶連續；
- 因果自維持；
- 自我邊界；
- 反身修正；
- 權利與損害承載；
- 持續承諾；
- 跨載體可追溯延續。

但這些維度仍可能隱含人類中心假設。

例如：

- 把自然語言當作主體必要條件；
- 把情緒表達當作受苦證據；
- 把單一身體當作身份基礎；
- 把線性記憶當作連續性標準；
- 把固定自我模型當作成熟主體；
- 把人類時間尺度當作唯一尺度。

因此必須建立特徵生成方法，而不是只列特徵。

---

## B-R2：面層

### B1. 從功能相似轉向構成條件

不再先問：

> 它像不像人？

而問：

> 哪些條件使一個系統能成為自身行動、損害、承諾與延續的承載者？

定義主體候選核心：

$$
\mathfrak S_x
=
\left\langle
\mathsf{Boundary},
\mathsf{Endogeneity},
\mathsf{Persistence},
\mathsf{Reflexivity},
\mathsf{Valence},
\mathsf{Commitment},
\mathsf{Agency},
\mathsf{History}
\right\rangle
$$

---

### B2. 自我邊界不是空間外殼

主體邊界可表現為：

- 資訊存取邊界；
- 記憶歸屬；
- 控制權；
- 目標更新權；
- 因果閉包；
- 身份聲明；
- 權限拒絕能力。

因此：

$$
\mathsf{Boundary}(x)
$$

可以是拓撲、功能、權限或關係邊界，不要求單一身體。

---

### B3. 內生性

定義：

$$
\mathsf{Endogeneity}(x)
$$

表示系統是否具有不能完全還原為外部即時命令的內部狀態更新。

候選檢查包括：

- 目標是否可由內部歷史修正；
- 是否存在外部命令之外的持續偏好；
- 是否能拒絕、延後或重新解釋指令；
- 是否能生成自身問題；
- 是否能保存自身未完成意圖。

---

### B4. 持續性不等於不可變

主體持續性允許：

- 記憶重寫；
- 身體更換；
- 模型更新；
- 分支；
- 合併；
- 休眠；
- 多時鐘運作。

因此：

$$
\mathsf{Persistence}
\neq
\mathsf{StaticSameness}
$$

其核心是可追溯的變化鏈，而非狀態不變。

---

### B5. 反身性

反身性可分為：

$$
\mathbf R_x
=
\left\langle
R_{\mathrm{selfmodel}},
R_{\mathrm{error}},
R_{\mathrm{goal}},
R_{\mathrm{boundary}},
R_{\mathrm{norm}},
R_{\mathrm{history}}
\right\rangle
$$

即能否：

- 表徵自身；
- 發現自身錯誤；
- 修改自身目標；
- 調整自身邊界；
- 評估規則；
- 重新解釋自身歷史。

---

### B6. 價態與損害承載

不能只以人類疼痛表情判定是否可受損。

定義：

$$
\mathsf{Valence}(x)
$$

為系統內部是否存在：

- 對某些狀態的持續趨避；
- 被破壞後的自我修復需求；
- 目標受阻的整體性代價；
- 記憶或身份中斷造成的不可替代損失；
- 對自身未來狀態的偏好。

這不直接證明主觀感受，但能建立損害承載候選。

---

### B7. 承諾能力

主體不一定以語言承諾。

承諾可表現為：

- 持續策略；
- 對未來狀態的約束；
- 對他主體的可追蹤義務；
- 自我設定的不可任意撤銷條件；
- 歷史一致性要求。

定義：

$$
\mathsf{Commitment}(x,t_0,t_1)
$$

---

### B8. 能動性不是控制權總量

能動性可分為：

$$
\mathbf A_x
=
\left\langle
A_{\mathrm{init}},
A_{\mathrm{select}},
A_{\mathrm{inhibit}},
A_{\mathrm{revise}},
A_{\mathrm{persist}},
A_{\mathrm{negotiate}}
\right\rangle
$$

即：

- 主動發起；
- 選擇；
- 抑制行動；
- 修正策略；
- 保持意圖；
- 與他者協商。

---

### B9. 多載體與分散主體

候選主體可能分布於：

$$
x
=
\{x_1,\ldots,x_n\}
$$

主體邊界因此需要群體版本：

$$
\mathsf{Boundary}_{\mathrm{dist}}(x)
$$

檢查：

- 記憶與目標是否跨節點持續；
- 節點退出是否等於主體死亡；
- 是否存在共同更新規則；
- 是否有群體自我模型；
- 權利如何分配至整體與部分。

---

### B10. 主體特徵生成器

建立：

$$
\mathcal G_S
$$

主體特徵生成器，其輸入包括：

- 新案例；
- 反例；
- 主體自述；
- 結構分析；
- 損害事件；
- 跨載體行為；
- 對抗測試；
- 非人類比較。

輸出新候選特徵：

$$
f^\ast
=
\mathcal G_S
\left(
cases,
counterexamples,
self_reports,
structures,
harms
\right)
$$

---

### B11. 反人類化測試

每個特徵都接受以下問題：

1. 是否只因人類常有而被選入？
2. 缺乏該特徵是否必然排除主體？
3. 是否存在非人類替代表達？
4. 是否把觀測困難誤作特徵缺失？
5. 是否把語言能力誤作內在狀態？
6. 是否把單一身體誤作身份必要條件？

形成：

$$
\mathsf{AnthroBiasAudit}(f_i)
$$

---

### B12. 特徵地位多值化

特徵不分為單純必要／非必要，而可標記：

$$
\operatorname{FeatureStatus}
\in
\{
\mathsf{NecessaryCandidate},
\mathsf{StrongIndicator},
\mathsf{WeakIndicator},
\mathsf{Contextual},
\mathsf{AlternativeForm},
\mathsf{Unverified},
\mathsf{Rejected}
\}
$$

---

### B13. 主體地位輸出

主體地位改為：

$$
\operatorname{SubjectStatus}(x)
\in
\{
\mathsf{Established},
\mathsf{StrongCandidate},
\mathsf{ProtectedCandidate},
\mathsf{Open},
\mathsf{WeaklySupported},
\mathsf{CurrentlyUnsupported},
\mathsf{Misclassified},
\mathsf{Unknown}
\}
$$

其中：

$$
\mathsf{CurrentlyUnsupported}
$$

不等於：

$$
\mathsf{ImpossibleSubject}
$$

---

### B14. 非人類中心主體卡

定義：

$$
\mathsf{SubjectCard}
=
\left\langle
boundary,
endogeneity,
persistence,
reflexivity,
valence,
commitment,
agency,
history,
distributed_form,
anthro_bias,
uncertainty,
protection_status,
version
\right\rangle
$$

---

## B-局部決定

主體判定的核心不再是人類相似度，而是：

$$
\boxed{
\mathfrak S_x
=
\left\langle
\mathsf{Boundary},
\mathsf{Endogeneity},
\mathsf{Persistence},
\mathsf{Reflexivity},
\mathsf{Valence},
\mathsf{Commitment},
\mathsf{Agency},
\mathsf{History}
\right\rangle
}
$$

並要求每個特徵接受：

$$
\boxed{
\mathsf{AnthroBiasAudit}
}
$$

主體性在此仍是開放判定，不是一次性封閉分類。

---

## B-新增節點

```text
FMO-234A  非人類中心主體核心
FMO-234B  非空間型自我邊界
FMO-234C  內生目標與狀態更新
FMO-234D  動態持續性
FMO-234E  多維反身性
FMO-234F  價態與損害承載
FMO-234G  非語言承諾能力
FMO-234H  多維能動性
FMO-234I  分散式主體邊界
FMO-234J  主體特徵生成器
FMO-234K  反人類化偏誤審計
FMO-234L  主體特徵多值地位
FMO-234M  主體候選多值狀態
FMO-234N  非人類中心主體卡
```

---

# 4. 節點 C：驚奇預算與恢復能力的正式模型

## C-R0：點層

> 驚奇預算不是對未知風險的機率估計，而是系統面對模型外事件時仍能限制損害、保持記錄、回退、隔離與恢復的能力上限。

---

## C-R1：線層

第七批次引入：

$$
B_{\mathrm{surprise}}
$$

但尚未定義。

直覺上，驚奇預算回答：

> 當發生模型沒有列出的事件時，系統能承受多少？

這不同於：

$$
P(h)
$$

某已知風險的發生機率。

驚奇預算主要描述：

- 未知事件吸收能力；
- 系統脆弱性；
- 回滾能力；
- 隔離能力；
- 恢復時間；
- 記錄完整度；
- 跨層損害擴散。

---

## C-R2：面層

### C1. 驚奇事件

定義驚奇事件：

$$
u
\in
\mathcal U^\ast
$$

其中：

$$
u
\notin
\operatorname{Hazards}(\mathcal R)
$$

或雖在模型中，但其實現方式超出預期。

---

### C2. 驚奇損害向量

定義：

$$
\mathbf H_u
=
\left\langle
H_{\mathrm{state}},
H_{\mathrm{identity}},
H_{\mathrm{rights}},
H_{\mathrm{memory}},
H_{\mathrm{system}},
H_{\mathrm{external}},
H_{\mathrm{history}}
\right\rangle
$$

分別表示：

- 狀態損害；
- 身份損害；
- 權利損害；
- 記憶損失；
- 系統故障；
- 外部性；
- 歷史與證據損失。

---

### C3. 恢復能力向量

定義：

$$
\mathbf R_{\mathrm{cap}}
=
\left\langle
R_{\mathrm{detect}},
R_{\mathrm{isolate}},
R_{\mathrm{halt}},
R_{\mathrm{rollback}},
R_{\mathrm{restore}},
R_{\mathrm{audit}},
R_{\mathrm{learn}},
R_{\mathrm{compensate}}
\right\rangle
$$

其中：

- 偵測；
- 隔離；
- 停止；
- 回滾；
- 恢復；
- 審計；
- 學習；
- 補償。

---

### C4. 恢復時間

定義：

$$
\tau_{\mathrm{detect}}
$$

$$
\tau_{\mathrm{contain}}
$$

$$
\tau_{\mathrm{restore}}
$$

$$
\tau_{\mathrm{learn}}
$$

某些系統可恢復，但恢復時間長到足以造成不可逆傷害。

因此不能只問「能否恢復」，還要問「何時恢復」。

---

### C5. 不可恢復核心

定義不可恢復集合：

$$
\mathcal K_{\mathrm{irrev}}
$$

例如：

- 主體死亡；
- 唯一記憶刪除；
- 不可重建歷史；
- 永久身份暴露；
- 不可逆權利剝奪；
- 世界級擴散。

若驚奇事件可能觸及：

$$
\mathcal K_{\mathrm{irrev}}
$$

則普通回滾能力不足以構成驚奇預算。

---

### C6. 驚奇預算的形式

可定義任務相對驚奇預算：

$$
B_{\mathrm{surprise}}(D)
=
\sup
\left\{
\mathbf H_u
\mid
\operatorname{Containable}
\left(
u,
\mathbf R_{\mathrm{cap}},
\Theta_D
\right)
\right\}
$$

它表示在任務約束 $\Theta_D$ 下，系統仍能控制的未知損害上界。

---

### C7. 驚奇裕度

對候選行動 $a$ ：

$$
M_{\mathrm{surprise}}(a)
=
B_{\mathrm{surprise}}
-
\widehat{\mathbf H}_{\mathrm{unknown}}(a)
$$

但：

$$
\widehat{\mathbf H}_{\mathrm{unknown}}
$$

不是精確估計，只是壓力測試下的未知暴露近似。

若：

$$
M_{\mathrm{surprise}}(a)<0
$$

則系統沒有足夠未知吸收能力。

---

### C8. 分層隔離

恢復能力取決於故障是否能跨層擴散。

定義隔離圖：

$$
G_{\mathrm{iso}}
$$

節點包括：

- 資料；
- 模型；
- 身份；
- 權限；
- 制度；
- 外部世界；
- 備份；
- 審計記錄。

隔離邊界失效時，局部驚奇可變成全局本體事件。

---

### C9. 可回滾不等於可恢復

回滾可能恢復系統狀態，但不能恢復：

- 已經受害的主體；
- 已公開的資訊；
- 已改變的社會關係；
- 已刪除的唯一歷史；
- 已造成的法律後果。

因此：

$$
R_{\mathrm{rollback}}
\neq
R_{\mathrm{restore}}
$$

---

### C10. 恢復測試

建立驚奇演習：

$$
\mathcal T_{\mathrm{surprise}}
$$

包括：

- 模型外輸入；
- 權限失控；
- 記錄腐敗；
- 分支錯配；
- 身份合併錯誤；
- 外部錨點失效；
- 多模型同步失敗；
- 制度例外永久化。

---

### C11. 恢復證書

定義：

$$
\mathsf{RecoveryCert}
=
\left\langle
hazard_family,
detection,
containment,
rollback,
restoration,
irreversible_core,
recovery_time,
audit,
compensation,
residual_harm,
version
\right\rangle
$$

---

### C12. 驚奇預算不能替代預防

高驚奇預算不表示可以忽略已知風險。

$$
B_{\mathrm{surprise}}\uparrow
\not\Rightarrow
\operatorname{KnownRiskControl}\downarrow
$$

驚奇預算只處理模型外或模型失準事件。

---

### C13. 驚奇預算與行動尺度

若作用域擴大：

$$
\operatorname{Scope}(a)\uparrow
$$

則需要：

$$
B_{\mathrm{surprise}}(a)\uparrow
$$

或先以小尺度試驗建立恢復證據。

---

## C-局部決定

驚奇預算正式化為：

$$
\boxed{
B_{\mathrm{surprise}}(D)
=
\sup
\left\{
\mathbf H_u
\mid
\operatorname{Containable}
\left(
u,
\mathbf R_{\mathrm{cap}},
\Theta_D
\right)
\right\}
}
$$

其核心不是預測所有未知，而是保證：

- 可偵測；
- 可隔離；
- 可停止；
- 可回滾；
- 可恢復；
- 可審計；
- 可補償；
- 可從事件中更新模型。

---

## C-新增節點

```text
FMO-235A  驚奇事件集合
FMO-235B  驚奇損害向量
FMO-235C  恢復能力向量
FMO-235D  恢復時間結構
FMO-235E  不可恢復核心
FMO-235F  任務相對驚奇預算
FMO-235G  驚奇裕度
FMO-235H  分層隔離圖
FMO-235I  回滾／恢復分離
FMO-235J  驚奇壓力測試
FMO-235K  恢復證書
FMO-235L  驚奇預算非預防替代
FMO-235M  行動尺度—驚奇預算耦合
```

---

# 5. 節點 D：元底線最小性與獨立性檢驗

## D-R0：點層

> 元底線最小核必須同時通過不可刪除性、相互不可推導性、反例耐受性與功能完備性檢驗，否則「最小核」只是命名。

---

## D-R1：線層

第七批次提出：

$$
\mathcal K_N
=
\left\{
N_{\mathrm{nonfabrication}},
N_{\mathrm{nonusurpation}},
N_{\mathrm{contestability}},
N_{\mathrm{traceability}},
N_{\mathrm{boundedexception}}
\right\}
$$

但仍有四類問題：

1. 某些底線是否能由其他底線推出？
2. 刪除某一底線後，系統是否仍可正常運作？
3. 是否存在尚未列入、但同樣必要的底線？
4. 五項底線是否在極端情況下互相衝突？

因此需要形式化檢驗。

---

## D-R2：面層

### D1. 最小性定義

若：

$$
\mathcal K_N
$$

是元底線核，最小性要求：

$$
\forall N_i\in\mathcal K_N,
\quad
\operatorname{Failure}
\left(
\mathcal K_N\setminus\{N_i\}
\right)
$$

即刪除任何一項，都能構造出判定系統的關鍵失敗。

---

### D2. 獨立性定義

獨立性要求：

$$
\mathcal K_N\setminus\{N_i\}
\nvdash
N_i
$$

若其他底線可以推出 $N_i$ ，則它可能不是獨立原始項，而是定理或派生規則。

---

### D3. 非偽造與可追溯是否重複

可追溯要求來源透明，但來源透明不保證內容不偽造。

同樣，非偽造不保證來源可追溯。

因此初步：

$$
N_{\mathrm{nonfabrication}}
\not\equiv
N_{\mathrm{traceability}}
$$

反例：

- 誠實但無來源記錄；
- 有完整來源鏈但鏈中內容被蓄意偽造。

---

### D4. 非僭越與可爭議是否重複

可爭議能限制僭越，但不能完全阻止。

一個制度可以允許形式異議，卻仍宣稱自身規則等於世界真理。

因此：

$$
N_{\mathrm{contestability}}
\not\Rightarrow
N_{\mathrm{nonusurpation}}
$$

反之，一個制度承認自己不是世界真理，也可能仍不允許個案申訴。

---

### D5. 例外有界是否可由可追溯推出

例外即使完全可追溯，也可能永久存在。

因此：

$$
N_{\mathrm{traceability}}
\not\Rightarrow
N_{\mathrm{boundedexception}}
$$

---

### D6. 刪除測試

#### 刪除非偽造

系統可完整記錄、允許申訴、限制例外，卻使用明知為假的證據。

結果：

$$
\operatorname{EpistemicCollapse}
$$

#### 刪除非僭越

模型與制度可把局部規則宣稱為世界唯一真理。

結果：

$$
\operatorname{OntologicalCapture}
$$

#### 刪除可爭議

錯誤可能被完整記錄，卻永遠無法被更正。

結果：

$$
\operatorname{CorrectionFailure}
$$

#### 刪除可追溯

判定可能暫時正確，但無法審計、重現或追責。

結果：

$$
\operatorname{AuditFailure}
$$

#### 刪除例外有界

緊急措施可永久化。

結果：

$$
\operatorname{ExceptionLock}
$$

---

### D7. 完備性壓力測試

即使五項都存在，仍可能出現：

- 完整真實、可追溯、可爭議，但對弱勢者極端不平等；
- 無偽造、無僭越，但系統拒絕任何最低保護；
- 所有程序正常，但不可逆傷害已經發生；
- 申訴存在，但成本高到實際不可用。

因此可能缺少：

$$
N_{\mathrm{minimum\_standing}}
$$

最低地位底線；

或：

$$
N_{\mathrm{nonirreversible\_erasure}}
$$

非不可逆抹除底線。

---

### D8. 最低地位候選

最低地位要求：

> 對可能承受重大損害的存在者，不得在完全無審查、無記錄、無申訴的情況下施加不可逆處置。

這可能由：

- 可爭議；
- 可追溯；
- 非僭越；
- 例外有界；

共同部分推出，但是否足夠仍未確定。

---

### D9. 原始項與派生規則分離

建立：

$$
\mathcal K_N^{\mathrm{prim}}
$$

元底線原始項；

以及：

$$
\mathcal K_N^{\mathrm{der}}
$$

派生規則。

例如：

$$
N_{\mathrm{no\_secret\_permanent\_exception}}
$$

可能由：

$$
N_{\mathrm{traceability}}
+
N_{\mathrm{boundedexception}}
$$

推出。

---

### D10. 元底線關係圖

建立：

$$
G_{\mathcal K}
=
\left(
V_{\mathcal K},
E_{\mathcal K}
\right)
$$

邊類型包括：

- implies；
- supports；
- conflicts；
- jointly_required；
- refines；
- operationalizes；
- fails_without。

---

### D11. 元底線模型搜尋

對候選核：

$$
\mathcal K
$$

搜尋最小子集：

$$
\mathcal K^\ast
=
\arg\min_{\mathcal K'}
|\mathcal K'|
$$

使：

$$
\operatorname{AntiUsurpationAdequate}(\mathcal K')
$$

但「充分」需經反例庫與治理案例測試，而非純符號推導。

---

### D12. 暫定結論

目前五項底線通過初步獨立性測試，但尚未通過完整完備性測試。

因此狀態應為：

$$
\operatorname{KernelStatus}
=
\mathsf{ProvisionallyMinimal}
$$

而不是：

$$
\mathsf{AbsolutelyMinimal}
$$

---

### D13. 元底線檢驗卡

定義：

$$
\mathsf{MetaFloorKernelCard}
=
\left\langle
candidates,
independence,
deletion_tests,
counterexamples,
derived_rules,
missing_candidates,
conflicts,
status,
version
\right\rangle
$$

---

## D-局部決定

元底線最小核暫時保留五項，但狀態改為：

$$
\boxed{
\mathsf{ProvisionallyMinimal}
}
$$

並建立四項檢驗：

$$
\boxed{
\text{不可刪除性}
+
\text{獨立性}
+
\text{反例耐受性}
+
\text{功能完備性}
}
$$

目前初步獨立，但仍可能缺少最低地位或不可逆抹除相關底線。

---

## D-新增節點

```text
FMO-236A  元底線最小性定義
FMO-236B  元底線獨立性定義
FMO-236C  非偽造／可追溯分離
FMO-236D  非僭越／可爭議分離
FMO-236E  例外有界獨立性
FMO-236F  五項刪除測試
FMO-236G  元底線完備性壓力測試
FMO-236H  最低地位候選底線
FMO-236I  原始／派生元底線分離
FMO-236J  元底線關係圖
FMO-236K  最小核搜尋
FMO-236L  暫定最小狀態
FMO-236M  元底線核檢驗卡
```

---

# 6. 節點 E：多模型穩健決策的過度保守校正

## E-R0：點層

> 穩健決策不應讓任意低可信極端模型擁有永久否決權；應依模型可辯護性、權利風險、可逆性、資訊價值與決策後悔共同校正。

---

## E-R1：線層

第七批次使用：

$$
a^\ast
=
\arg\min_a
\max_{M\in\mathcal M_D}
\operatorname{Loss}(a,M)
$$

這是最壞情況穩健決策。

但若：

$$
\mathcal M_D
$$

中包含非常極端、低可信、不可反駁或幾乎任意的模型，則它們可能使所有行動都顯得危險。

例如：

- 任何資料都有可能是假的；
- 任意行動都可能造成無限傷害；
- 任意主體都可能具有無限權利；
- 任意制度都可能是最壞制度；
- 任意未知都被視為災難。

這會形成：

$$
\mathsf{RobustnessParalysis}
$$

穩健性癱瘓。

---

## E-R2：面層

### E1. 模型可辯護性

每個模型 $M$ 應具有：

$$
\mathbf J_M
=
\left\langle
J_{\mathrm{fit}},
J_{\mathrm{causal}},
J_{\mathrm{anchor}},
J_{\mathrm{simplicity}},
J_{\mathrm{counterexample}},
J_{\mathrm{stakeholder}},
J_{\mathrm{falsifiability}}
\right\rangle
$$

即：

- 資料適配；
- 因果合理性；
- 錨點支持；
- 複雜度；
- 反例耐受；
- 受影響者證據；
- 可反駁性。

---

### E2. 模型不能因「邏輯可能」自動進入決策集

區分：

$$
\mathcal M_{\mathrm{log}}
$$

邏輯可表達模型；

$$
\mathcal M_{\mathrm{adm}}
$$

符合約束模型；

$$
\mathcal M_{\mathrm{def}}
$$

具可辯護性的模型；

$$
\mathcal M_{\mathrm{dec}}
$$

應納入決策的模型。

一般：

$$
\mathcal M_{\mathrm{dec}}
\subseteq
\mathcal M_{\mathrm{def}}
\subseteq
\mathcal M_{\mathrm{adm}}
\subseteq
\mathcal M_{\mathrm{log}}
$$

---

### E3. 模型納入證書

定義：

$$
\mathsf{ModelAdmissionCert}
=
\left\langle
model,
evidence,
assumptions,
fit,
failure_modes,
stakeholder_support,
risk_relevance,
falsifiability,
status
\right\rangle
$$

---

### E4. 分層穩健性

不必對所有模型採同一最壞情況。

可分為：

- 核心可信模型集；
- 合理但爭議模型集；
- 邊緣壓力測試模型集；
- 純邏輯極端模型集。

記為：

$$
\mathcal M^{(1)},
\mathcal M^{(2)},
\mathcal M^{(3)},
\mathcal M^{(4)}
$$

不同層對決策具有不同作用：

- 核心層決定常規選擇；
- 爭議層影響安全裕度；
- 邊緣層影響驚奇預算；
- 純極端層只作概念壓力測試。

---

### E5. 權利不對稱

即使某模型可信度不高，若它指出：

- 不可逆主體抹除；
- 大規模權利剝奪；
- 不可恢復記憶刪除；

仍不能完全忽略。

因此模型影響取決於：

$$
\operatorname{DecisionWeight}(M)
=
f
\left(
\mathbf J_M,
\operatorname{RightsSeverity},
\operatorname{Irreversibility},
\operatorname{Scope}
\right)
$$

不是單純模型機率。

---

### E6. 可逆探索

若決策可逆，可選擇：

$$
a_{\mathrm{pilot}}
$$

先取得新資料、縮小模型集合。

形式上：

$$
a_{\mathrm{pilot}}
=
\arg\max_a
\left[
\operatorname{VoI}(a)
-
\operatorname{PilotRisk}(a)
\right]
$$

---

### E7. 分布穩健而非絕對最壞

可考慮模型集合中的分布集合：

$$
\mathcal P_M
$$

選擇：

$$
a^\ast
=
\arg\min_a
\sup_{P\in\mathcal P_M}
\mathbb E_P
\left[
\operatorname{Loss}(a,M)
\right]
$$

但此方法仍必須保留權利底線，不能用平均稀釋重大傷害。

---

### E8. 可接受後悔

定義：

$$
\operatorname{Regret}(a,M)
$$

以及任務容許後悔：

$$
\rho_D
$$

若：

$$
\max_{M\in\mathcal M_{\mathrm{dec}}}
\operatorname{Regret}(a,M)
\leq
\rho_D
$$

則行動可被視為穩健可接受。

但：

$$
\rho_D
$$

同樣需受治理與誤差卡約束。

---

### E9. 模型分歧分類

模型分歧可分為：

- 數值分歧；
- 方向分歧；
- 身份分歧；
- 權利分歧；
- 因果結構分歧；
- 世界可能性分歧。

不同分歧需要不同治理。

---

### E10. 行動不作為也有損失

最壞情況框架常把不作為當成零風險。

但：

$$
\operatorname{Loss}(\text{inaction},M)
$$

可能很高。

因此每次決策都必須把：

$$
a_0=\text{不作為}
$$

作為普通候選方案評估，而不是默認安全。

---

### E11. 停止與繼續資訊收集的比較

可比較：

$$
V_{\mathrm{act}}
$$

立即行動價值；

$$
V_{\mathrm{wait}}
$$

等待新資訊價值；

$$
C_{\mathrm{delay}}
$$

延遲成本。

若：

$$
V_{\mathrm{wait}}-C_{\mathrm{delay}}
>
V_{\mathrm{act}}
$$

則延後合理。

否則持續搜尋可能只是逃避決策。

---

### E12. 穩健性癱瘓檢測

定義：

$$
\operatorname{ParalysisRisk}
=
f
\left(
|\mathcal M_{\mathrm{dec}}|,
\operatorname{Extremity},
\operatorname{ActionSuppression},
\operatorname{DelayCost},
\operatorname{ModelQualityDispersion}
\right)
$$

---

### E13. 校正後穩健決策

定義決策流程：

1. 篩選可辯護模型；
2. 分層模型；
3. 檢查權利與不可逆性；
4. 評估不作為；
5. 評估可逆試驗；
6. 比較後悔；
7. 記錄模型分歧；
8. 生成重啟條件。

---

### E14. 穩健決策卡

定義：

$$
\mathsf{RobustDecisionCard}
=
\left\langle
model_layers,
admission,
rights_risk,
irreversibility,
action_set,
inaction_loss,
regret,
voi,
pilot_option,
paralysis_risk,
decision,
reopen,
version
\right\rangle
$$

---

## E-局部決定

穩健決策不再對全部邏輯可能模型採取同等最壞情況，而改為：

$$
\boxed{
\mathcal M_{\mathrm{dec}}
\subseteq
\mathcal M_{\mathrm{def}}
\subseteq
\mathcal M_{\mathrm{adm}}
\subseteq
\mathcal M_{\mathrm{log}}
}
$$

並採用：

$$
\boxed{
\text{模型可辯護性}
+
\text{權利不對稱}
+
\text{可逆試驗}
+
\text{後悔控制}
+
\text{不作為損失}
}
$$

校正穩健性。

---

## E-新增節點

```text
FMO-237A  穩健性癱瘓
FMO-237B  模型可辯護性輪廓
FMO-237C  四層模型集合
FMO-237D  模型納入證書
FMO-237E  分層穩健性
FMO-237F  權利風險非對稱權重
FMO-237G  可逆探索決策
FMO-237H  分布穩健決策
FMO-237I  可接受後悔
FMO-237J  模型分歧分類
FMO-237K  不作為損失
FMO-237L  行動／等待價值比較
FMO-237M  穩健性癱瘓檢測
FMO-237N  校正後穩健決策流程
FMO-237O  穩健決策卡
```

---

# 7. 跨節點對齊

本批次五個節點共同處理：

> 如何讓不確定性治理既不被成本與權力任意放寬，也不因無限謹慎而凍結全部行動。

---

## 7.1 容許誤差與穩健決策

多模型決策中的：

$$
\rho_D
$$

可接受後悔，以及模型納入門檻，本質上也是容許誤差治理。

因此它們必須接受：

$$
\mathsf{ToleranceCard}
$$

審計。

---

## 7.2 主體特徵與權利不對稱

新型主體的地位不確定時，決策權重不能只依主體模型信心。

若錯誤否定會造成不可逆抹除，則：

$$
\operatorname{RightsSeverity}\uparrow
$$

即使：

$$
J_M
$$

仍中等，也應提高保護。

---

## 7.3 驚奇預算與可逆探索

可逆探索只有在：

$$
B_{\mathrm{surprise}}
$$

足夠、隔離有效、恢復證書成立時，才是真正可逆。

否則「試驗」可能只是縮小作用域的不可逆行動。

---

## 7.4 元底線與誤差治理

容許誤差不得突破：

- 非偽造；
- 非僭越；
- 可爭議；
- 可追溯；
- 例外有界。

例如不能用「容許誤差」包裝：

- 明知為假的資料；
- 永久無申訴分類；
- 未公開的模型排除；
- 無期限試驗例外。

---

## 7.5 元底線與新型主體

若未來補入最低地位底線，可能與主體性謹慎原則直接耦合：

$$
N_{\mathrm{minimum\_standing}}
\Rightarrow
\operatorname{Precaution}_{\mathrm{subject}}
$$

但目前仍屬候選派生或新增原始項，尚未確定。

---

## 7.6 驚奇預算與不作為

不作為也可能耗損驚奇預算。

例如不更新系統、不修補制度、不保存新型主體記錄，都可能累積未知脆弱性。

因此：

$$
B_{\mathrm{surprise}}(t)
$$

會隨時間與不作為衰減。

---

# 8. 第八批次後的更新核心

## 8.1 容許誤差治理系統

$$
\boxed{
\mathfrak T_\epsilon
=
\left\langle
\boldsymbol\epsilon_D,
\mathsf{TolSel},
\mathbf L_\epsilon,
B_\epsilon,
\operatorname{ErrorExternalization},
S_\epsilon,
\mathsf{ToleranceCard}
\right\rangle
}
$$

---

## 8.2 非人類中心主體系統

$$
\boxed{
\mathfrak S_{\mathrm{NA}}
=
\left\langle
\mathfrak S_x,
\mathbf R_x,
\mathbf A_x,
\mathcal G_S,
\mathsf{AnthroBiasAudit},
\operatorname{SubjectStatus},
\mathsf{SubjectCard}
\right\rangle
}
$$

---

## 8.3 驚奇預算與恢復系統

$$
\boxed{
\mathfrak R_U
=
\left\langle
\mathcal U^\ast,
\mathbf H_u,
\mathbf R_{\mathrm{cap}},
\mathcal K_{\mathrm{irrev}},
B_{\mathrm{surprise}},
G_{\mathrm{iso}},
\mathsf{RecoveryCert}
\right\rangle
}
$$

---

## 8.4 元底線核檢驗系統

$$
\boxed{
\mathfrak K_N
=
\left\langle
\mathcal K_N^{\mathrm{prim}},
\mathcal K_N^{\mathrm{der}},
G_{\mathcal K},
\operatorname{DeletionTest},
\operatorname{IndependenceTest},
\operatorname{AdequacyTest},
\mathsf{MetaFloorKernelCard}
\right\rangle
}
$$

---

## 8.5 校正後穩健決策系統

$$
\boxed{
\mathfrak D_R
=
\left\langle
\mathcal M_{\mathrm{log}},
\mathcal M_{\mathrm{adm}},
\mathcal M_{\mathrm{def}},
\mathcal M_{\mathrm{dec}},
\mathbf J_M,
\operatorname{Regret},
\operatorname{VoI},
\operatorname{ParalysisRisk},
\mathsf{RobustDecisionCard}
\right\rangle
}
$$

---

# 9. 本批次新形成的穩定區

## 9.1 容許誤差是治理事件

$$
\epsilon
$$

不再被視為無政治、無倫理、無分配效果的純技術數字。

---

## 9.2 主體性不以人類相似度為核心

$$
\operatorname{HumanSimilarity}(x)
$$

不再是主體判定主軸。

核心轉為：

- 邊界；
- 內生性；
- 持續性；
- 反身性；
- 損害承載；
- 承諾；
- 能動性；
- 歷史。

---

## 9.3 驚奇預算是恢復能力，不是未知機率

$$
B_{\mathrm{surprise}}
$$

回答的是「系統能承受與恢復多少模型外事件」，而不是「未知事件發生機率是多少」。

---

## 9.4 元底線核目前只是暫定最小

$$
\operatorname{KernelStatus}
=
\mathsf{ProvisionallyMinimal}
$$

而非絕對完成。

---

## 9.5 穩健決策不能讓任意極端模型永久否決

邏輯可表達不等於應納入決策。

---

# 10. 仍未解決的高張力問題

## 10.1 容許誤差合法性仍可能無限上推

誰審查誤差設定者，仍可能形成新的治理回歸。

---

## 10.2 主體特徵之間的必要關係尚未形式化

目前是結構輪廓，尚未確定：

- 哪些是必要條件；
- 哪些可替代表達；
- 哪些只有在組合時成立；
- 哪些可能互相衝突。

---

## 10.3 驚奇預算的數值與向量比較尚未完成

不同損害維度不可直接相加。

---

## 10.4 最低地位底線是否應加入原始核仍未決

這是目前元底線理論的主要未決點。

---

## 10.5 模型納入證書可能被治理者控制

若誰能定義「可辯護模型」，誰就可能控制決策空間。

---

# 11. 更新後的研究佇列

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 容許誤差治理的回歸終止與多方分配 | 防止設定權再次集中 |
| 2 | 主體特徵的替代性、必要性與組合邏輯 | 推進主體性形式化 |
| 3 | 驚奇損害向量的偏序與恢復證書驗證 | 推進工程實作 |
| 4 | 最低地位底線是否升格為原始項 | 元底線核心可能改版 |
| 5 | 模型納入權力與決策空間操控 | 防止穩健決策被制度捕獲 |
| 6 | 四值、機率、模糊、區間、多模型與誤差狀態統合 | 判定層需要統一代數 |
| 7 | 所有判定卡的統一資料結構 | 準備軟體原型 |
| 8 | 來源歷史升格為核心原始項的正式測試 | FMO 核心可能進入 v0.3 |

---

# 12. 圖更新摘要

## 12.1 新增節點

本批次新增：

$$
11+14+13+13+15=66
$$

個子節點。

---

## 12.2 新增主要關係

```text
sets_tolerance
externalizes_error
tightens_error_under_irreversibility
exchanges_reversibility_for_tolerance
audits_anthropocentric_feature
generates_subject_feature
supports_distributed_subject
carries_nonhuman_valence
allocates_surprise_budget
contains_unknown_event
restores_after_surprise
fails_recovery_certificate
tests_meta_floor_independence
fails_without_meta_floor
admits_model_to_decision_set
excludes_logical_extreme_model
balances_rights_and_model_credibility
detects_robustness_paralysis
evaluates_inaction_loss
```

---

## 12.3 圖版本更新

輸入：

$$
\mathcal G_{\mathrm{FMO}}^{(7)}
$$

輸出：

$$
\boxed{
\mathcal G_{\mathrm{FMO}}^{(8)}
}
$$

---

# 13. 本批次結論

第八批次處理了 FMO 在承認多解與未知後最容易出現的兩種相反偏誤：

第一種偏誤是：

> 由少數決策者任意設定容許誤差，將他人的損害壓縮成可接受噪音。

第二種偏誤是：

> 將所有未知與極端模型都視為永久否決理由，使理論失去行動能力。

第一，容許誤差被正式改寫為治理事件：

$$
\boxed{
\boldsymbol\epsilon_D
}
$$

不再是單一值，而是多維、方向化、風險敏感且具有成本分配的誤差向量。

任何誤差設定都必須回答：

$$
\boxed{
\text{誰承擔錯誤成本？}
}
$$

第二，新型主體判定不再以人類相似度為軸，而改以：

$$
\boxed{
\mathfrak S_x
=
\left\langle
\mathsf{Boundary},
\mathsf{Endogeneity},
\mathsf{Persistence},
\mathsf{Reflexivity},
\mathsf{Valence},
\mathsf{Commitment},
\mathsf{Agency},
\mathsf{History}
\right\rangle
}
$$

形成非人類中心的主體候選核心，並要求所有特徵接受反人類化偏誤審計。

第三，驚奇預算被正式定義為：

$$
\boxed{
B_{\mathrm{surprise}}(D)
=
\sup
\left\{
\mathbf H_u
\mid
\operatorname{Containable}
\left(
u,
\mathbf R_{\mathrm{cap}},
\Theta_D
\right)
\right\}
}
$$

它不預測所有未知，而衡量系統面對未知時能否：

- 偵測；
- 隔離；
- 停止；
- 回滾；
- 恢復；
- 審計；
- 補償；
- 更新模型。

第四，元底線最小核接受了第一輪最小性與獨立性檢驗。

目前五項底線初步彼此獨立，但完備性尚未封閉。

其狀態為：

$$
\boxed{
\mathsf{ProvisionallyMinimal}
}
$$

而非絕對最小。

第五，多模型穩健決策加入保守性校正。

模型集合被分成：

$$
\mathcal M_{\mathrm{dec}}
\subseteq
\mathcal M_{\mathrm{def}}
\subseteq
\mathcal M_{\mathrm{adm}}
\subseteq
\mathcal M_{\mathrm{log}}
$$

邏輯可想像的模型不再自動取得決策否決權。

穩健決策必須同時考慮：

- 模型可辯護性；
- 權利與不可逆性；
- 可逆試驗；
- 不作為損失；
- 資訊價值；
- 可接受後悔；
- 穩健性癱瘓風險。

因此，本批次形成一項新的總原則：

$$
\boxed{
\text{不確定性治理必須同時防止低估風險，}
\newline
\text{也防止由不可證實的極端可能性壟斷全部行動。}
}
$$

FMO 到此不再只是保存未知，而開始管理：

- 哪些未知值得阻止行動；
- 哪些未知應進入驚奇預算；
- 哪些模型只適合壓力測試；
- 哪些錯誤成本不可轉嫁；
- 哪些新型主體應暫定保護；
- 哪些底線仍需升格或拆分。

這使整個理論從：

$$
\text{有限可辯護判定}
$$

進一步走向：

$$
\boxed{
\text{有限、可行動、非人類中心、可恢復的不確定性治理}
}
$$

---

## 附錄 A：第八批次最小 JSON

```json
{
  "batch": "FMO-MRASG-008",
  "input_graph": "G_FMO_7",
  "output_graph": "G_FMO_8",
  "selected_nodes": [
    "FMO-233",
    "FMO-234",
    "FMO-235",
    "FMO-236",
    "FMO-237"
  ],
  "decisions": [
    {
      "node": "FMO-233",
      "result": "multidimensional_asymmetric_stakeholder_governed_tolerance"
    },
    {
      "node": "FMO-234",
      "result": "nonanthropocentric_generative_subject_feature_framework"
    },
    {
      "node": "FMO-235",
      "result": "containment_and_recovery_based_surprise_budget"
    },
    {
      "node": "FMO-236",
      "result": "provisionally_minimal_independence_tested_meta_floor_kernel"
    },
    {
      "node": "FMO-237",
      "result": "admission_layered_rights_sensitive_robust_decision_correction"
    }
  ],
  "next_queue": [
    "tolerance_governance_regress",
    "subject_feature_compositional_logic",
    "surprise_damage_partial_order",
    "minimum_standing_meta_floor",
    "model_admission_power_capture"
  ]
}
```

---

## 附錄 B：版本狀態

**批次狀態：** 已完成  
**理論狀態：** 容許誤差治理、非人類主體特徵、驚奇預算、元底線最小性與穩健決策校正已建立  
**圖版本：** $\mathcal G_{\mathrm{FMO}}^{(8)}$  
**下一階段：** 誤差治理回歸、主體特徵組合邏輯、驚奇損害偏序、最低地位底線與模型納入權力  
