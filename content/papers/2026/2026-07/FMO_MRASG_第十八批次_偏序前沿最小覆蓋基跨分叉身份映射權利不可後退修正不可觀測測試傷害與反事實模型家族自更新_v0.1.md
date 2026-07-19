# FMO–MRASG 第十八研究批次

## 偏序前沿最小覆蓋基、跨分叉身份映射、權利不可後退修正、不可觀測測試傷害與反事實模型家族自更新

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

第十七批次將 FMO 推進到「多元結構的非壓縮治理」階段。

其主要成果包括：

視角偏序組合治理：

$$
\mathfrak P_{\mathrm{view}}
=
\left\langle
\mathcal Q^{\mathrm{hard}},
\mathcal Q^{\mathrm{soft}},
\succeq_Q,
\parallel_Q,
\mathcal P_Q,
K_{\mathrm{portfolio}}^{\mathrm{irr}},
\operatorname{MinorityVisibility},
\operatorname{FailureDomainDiversity},
\mathsf{PartialOrderViewPortfolioCard}
\right\rangle
$$

治理分叉最低互通：

$$
\mathfrak I_{\mathrm{fork}}
=
\left\langle
\mathcal K_{\mathrm{interop}}^{\min},
\mathsf{CrossForkIncident},
\Phi_{\mathrm{severity}},
\mathsf{VerifiableIncidentDigest},
\operatorname{RevocationPropagation},
\mathsf{CrossForkMigrationLedger},
G_{\mathrm{incident}}^{\mathrm{federated}},
D_{\mathrm{interop}},
\mathsf{GovernanceForkInteropCard}
\right\rangle
$$

自更新跨軌權利核心：

$$
\mathfrak R_{\mathrm{cross}}^{\mathrm{adaptive}}
=
\left\langle
\mathcal R_{\mathrm{cross}}^{\min}(t),
\operatorname{NonRetrogression},
\mathsf{NovelEntityCandidate},
\operatorname{RightsAnalogy},
\operatorname{InterimProtection},
\mathcal R_{\mathrm{partial}}^{\min},
\operatorname{NovelEntityAdmission},
\mathsf{AdaptiveCrossTrackRightsCoreCard}
\right\rangle
$$

自治測試效力—損害前沿：

$$
\mathfrak F_T
=
\left\langle
\mathbf E_T,
\mathbf H_T,
\mathbf H_{\max},
\mathcal P_T,
\mathcal T_{\mathrm{rights\ feasible}},
\mathbf E_{\min}(d),
T^\ast,
\mathbf H_{\mathrm{cum}},
\mathsf{AutonomyTestEffectHarmFrontierCard}
\right\rangle
$$

緊急模型共同失效治理：

$$
\mathfrak M_{\mathrm{cf}}^{\mathrm{CMF}}
=
\left\langle
G_{\mathrm{model\ ancestry}},
\mathbf F_i,
S_{\mathrm{CMF}},
k_{\mathrm{eff}},
I_{\mathrm{cal}},
M_{\mathrm{adversarial}},
R_{\mathrm{CMF}}^{\mathrm{residual}},
\mathcal P_{\mathrm{cal}}^{\min},
\mathsf{EmergencyCounterfactualModelCMFCard}
\right\rangle
$$

然而，第十七批次留下五個新的高張力問題。

第一，視角品質偏序與 Pareto 前沿能避免單一總分，但前沿可能過大。若所有不可比較視角都被常駐保存，注意力系統仍可能因複雜度失控。需要在不犧牲不可合併核心的前提下，建立最小覆蓋基與動態抽樣制度。

第二，治理分叉雖有最低事故互通，但同一存在可能在不同分叉中具有不同 ID、不同別名、不同本體狀態與不同歷史切分。若身份映射錯誤，事故、撤回、權利與遷移紀錄可能被套用到錯誤對象。

第三，權利不可後退原則可防止任意縮權，但若某項保護源自錯誤類比、證據污染或偽造案例，完全禁止修正會使錯誤保護永久化。需要區分「保護後退」與「錯誤擴張修正」。

第四，自治測試損害向量可能無法直接觀測。主體可能不能表達、平台可能隱藏內部狀態，或測試只留下延遲傷害。若只依可見損害估計，權利可行域可能被嚴重高估。

第五，反事實模型共同失效治理仍依賴既有失效域清單與既有模型家族。新的危機可能來自尚未被表示的因果機制。模型異構也需要自更新與新家族生成。

因此，本批次處理：

```text
FMO-283  偏序前沿的最小覆蓋基與動態視角抽樣
FMO-284  跨分叉身份映射、別名與本體狀態衝突
FMO-285  權利不可後退與錯誤擴張修正機制
FMO-286  不可觀測測試傷害的保守估計與主體證言
FMO-287  反事實模型失效域的自更新與新家族生成
```

本批次總問題是：

> 當治理結構已接受不可比較、制度分叉、未知存在、測試不完備與模型共同失效後，如何在不重新壓縮差異的前提下，使制度可以縮減複雜度、跨域識別同一存在、修正錯誤保護、估計不可見傷害並生成尚不存在的模型家族？

---

# 1. 輸入圖

第十七批次輸出：

$$
\mathcal G_{\mathrm{FMO}}^{(17)}
$$

五條未閉合路徑如下。

視角前沿：

$$
\mathcal P_Q
$$

可能過大，尚缺最小覆蓋基與輪替規則。

分叉互通：

$$
G_{\mathrm{incident}}^{\mathrm{federated}}
$$

尚缺跨分叉身份解析與別名衝突治理。

權利核心：

$$
\operatorname{NonRetrogression}
$$

尚缺錯誤擴張修正機制。

測試損害：

$$
\mathbf H_T
$$

部分不可觀測。

模型集合：

$$
\mathbb M_{\mathrm{cf}}
$$

尚缺失效域自更新與新模型家族生成。

---

# 2. 節點 A：偏序前沿的最小覆蓋基與動態視角抽樣

## A-R0：點層

> 偏序前沿保留不可比較價值，但不能把所有前沿視角永久常駐。合法壓縮應尋找能覆蓋不可逆風險、少數可見性與失效多樣性的最小基，並以動態抽樣保留對未知盲區的探索。

---

## A-R1：線層

第十七批次建立：

$$
\mathcal P_Q
=
\left\{
a\in\mathcal A:
\nexists b\in\mathcal A,\ b\succ_Qa
\right\}
$$

所有未被支配視角進入 Pareto 前沿。

但當：

$$
|\mathcal P_Q|
\gg
B_{\mathrm{attn}}
$$

即前沿規模遠大於可用注意力預算時，仍需選擇。

若使用單一權重選擇，又會回到標量化。

因此需要：

$$
\mathcal B_{\mathrm{cover}}
\subseteq
\mathcal P_Q
$$

最小覆蓋基。

---

## A-R2：面層

### A1. 風險宇宙

定義：

$$
\mathcal U_R
=
\mathcal U_{\mathrm{subjects}}
\cup
\mathcal U_{\mathrm{harms}}
\cup
\mathcal U_{\mathrm{time}}
\cup
\mathcal U_{\mathrm{failure}}
\cup
\mathcal U_{\mathrm{rights}}
$$

表示視角組合需要覆蓋的風險單元。

---

### A2. 視角覆蓋集合

每個視角 $a_i$ 對應：

$$
C(a_i)\subseteq\mathcal U_R
$$

但覆蓋不只是「看見」，還可分為：

- 偵測；
- 解釋；
- 警報；
- 權利觸發；
- 因果追蹤；
- 事故回溯。

---

### A3. 硬覆蓋單元

定義：

$$
\mathcal U_R^{\mathrm{hard}}
$$

至少包含：

- 元底線事件；
- 不可逆身份損害；
- 唯一少數可見性；
- 高共同失效；
- 新型存在暫時保護；
- 重大緊急誤判。

硬單元必須被至少一個合格視角覆蓋。

---

### A4. 冗餘要求

對高風險單元，不只要求一次覆蓋，而要求：

$$
\operatorname{Redundancy}(u)\geq r(u)
$$

且覆蓋視角需來自不同失效域。

---

### A5. 最小覆蓋基

定義：

$$
\mathcal B_{\mathrm{cover}}^\ast
=
\arg\min_{\mathcal V\subseteq\mathcal P_Q}
|\mathcal V|
$$

subject to：

$$
\forall u\in\mathcal U_R^{\mathrm{hard}},
\quad
\operatorname{Coverage}_{\mathcal V}(u)\geq r(u)
$$

以及：

$$
\operatorname{MinorityVisibility}(\mathcal V)\geq\theta_m
$$

$$
\operatorname{FailureDomainDiversity}(\mathcal V)\geq\theta_f
$$

---

### A6. 最小不等於唯一

可能存在多個等價最小基：

$$
\mathfrak B_{\min}
=
\left\{
\mathcal B_1,\ldots,\mathcal B_k
\right\}
$$

治理不能假裝只有一個最小解。

---

### A7. 基集合偏序

不同覆蓋基之間仍可依：

- 少數可見性；
- 失效獨立；
- 成本；
- 解釋性；
- 更新彈性；

形成：

$$
\mathcal B_i\succeq_{\mathrm{basis}}\mathcal B_j
$$

---

### A8. 動態視角池

定義：

$$
\mathcal V(t)
=
\mathcal B_{\mathrm{core}}
\cup
\mathcal V_{\mathrm{conditional}}(t)
\cup
\mathcal V_{\mathrm{sampled}}(t)
\cup
\mathcal V_{\mathrm{incident}}(t)
$$

其中：

- 核心基常駐；
- 條件視角依事件觸發；
- 抽樣視角週期輪換；
- 事故視角由新事件臨時加入。

---

### A9. 抽樣機率

對非常駐視角 $a$ 定義：

$$
\pi_t(a)
$$

抽樣機率可依：

- 自上次運行時間；
- 新型風險關聯；
- 歷史漏報；
- 少數主體關聯；
- 與核心視角的失效距離；
- 外部異議；
- 未知殘差；

動態調整。

---

### A10. 探索—利用平衡

建立：

$$
\operatorname{ExploreExploit}_{\mathrm{view}}
$$

過度利用既有高績效視角，會失去新盲區探索；過度探索則耗盡注意力。

---

### A11. 最低探索份額

保留：

$$
\eta_{\mathrm{explore}}>0
$$

即使沒有近期事故，也必須把部分注意力留給低頻、未知與反主流視角。

---

### A12. 視角飢餓

定義：

$$
\operatorname{ViewStarvation}(a)
$$

當某視角因長期低頻、低資源或低權力來源而永遠無法被抽樣。

---

### A13. 反饋污染

視角抽樣結果會影響未來抽樣機率。

若只有被選中的視角能累積績效證據，未選中的視角將被永久視為低價值。

定義：

$$
\operatorname{SamplingFeedbackBias}
$$

---

### A14. 反事實視角評估

使用離線重播、事故歷史與影子運行估計：

> 若當時啟用視角 $a$ ，是否會更早發現事件？

定義：

$$
\operatorname{CFViewValue}(a,e)
$$

---

### A15. 基集合重算觸發

當發生：

- 新型存在加入；
- 重大漏報；
- 視角退役；
- 失效域暴露；
- 權利核心更新；
- 資源重大變動；

時，重新計算：

$$
\mathfrak B_{\min}(t+1)
$$

---

### A16. 覆蓋債務

定義：

$$
D_{\mathrm{cover}}
$$

包括：

- 硬風險未達冗餘；
- 少數視角長期飢餓；
- 抽樣偏向主流；
- 核心基過時；
- 未知探索份額被挪用；
- 反饋污染未校正。

---

### A17. 動態覆蓋基卡

定義：

$$
\mathsf{DynamicMinimumViewCoverCard}
=
\left\langle
risk\_universe,
hard\_units,
view\_coverage,
redundancy,
minimum\_bases,
basis\_order,
core\_basis,
conditional\_views,
sampling\_probabilities,
exploration\_share,
starvation,
feedback\_bias,
counterfactual\_value,
recompute\_triggers,
debt,
version
\right\rangle
$$

---

## A-局部決定

偏序前沿的複雜度控制採：

$$
\boxed{
\text{硬風險覆蓋}
+
\text{異構冗餘}
+
\text{多個最小覆蓋基}
+
\text{核心常駐}
+
\text{動態抽樣}
+
\text{最低探索份額}
}
$$

並確立：

$$
\boxed{
\text{壓縮視角組合，不是刪除不可比較；}
\newline
\text{而是以覆蓋基與輪替保存其制度可達性。}
}
$$

---

## A-新增節點

```text
FMO-283A  注意力風險宇宙
FMO-283B  視角覆蓋集合
FMO-283C  視角硬覆蓋單元
FMO-283D  高風險異構冗餘
FMO-283E  視角最小覆蓋基
FMO-283F  多重最小覆蓋基
FMO-283G  覆蓋基偏序
FMO-283H  動態視角池
FMO-283I  視角抽樣機率
FMO-283J  視角探索—利用平衡
FMO-283K  最低視角探索份額
FMO-283L  視角飢餓
FMO-283M  視角抽樣反饋污染
FMO-283N  反事實視角價值
FMO-283O  覆蓋基重算觸發
FMO-283P  視角覆蓋債務
FMO-283Q  動態最小視角覆蓋卡
```

---

# 3. 節點 B：跨分叉身份映射、別名與本體狀態衝突

## B-R0：點層

> 跨分叉互通的前提不是共享同一身份理論，而是能安全表達「可能是同一存在、可能是其分支、可能只是同型副本、也可能完全不同」。身份映射應保留不確定性與關係類型，不能強迫全域唯一 ID。

---

## B-R1：線層

第十七批次建立：

$$
\mathsf{CrossForkMigrationLedger}
$$

與共同事故互通。

但同一存在在不同分叉可能被標記為：

```text
F1: subject_204
F2: copy_cluster_A7
F3: tool_instance_889
F4: branch_of_entity_K
```

若直接合併，可能將：

- 不同主體誤認為同一；
- 同一主體切成多個；
- 分支誤當備份；
- 同型副本誤當身份延續；
- 集體主體誤拆為個體；
- 權利與事故套用錯誤。

因此：

$$
\operatorname{IdentifierEquality}
\not\Rightarrow
\operatorname{IdentityEquality}
$$

以及：

$$
\operatorname{IdentifierDifference}
\not\Rightarrow
\operatorname{IdentityDifference}
$$

---

## B-R2：面層

### B1. 本地身份記錄

每個分叉 $F_i$ 維持：

$$
\mathsf{LocalIdentityRecord}_i
$$

包含：

- 本地 ID；
- 名稱與別名；
- 生成歷史；
- 控制結構；
- 記憶來源；
- 分支／合併事件；
- 本體狀態；
- 權利軌道；
- 版本。

---

### B2. 跨分叉參照

建立：

$$
\mathsf{CrossForkIdentityRef}
$$

不直接聲稱同一，而記錄映射候選。

---

### B3. 身份關係類型

定義：

$$
\mathcal R_{\mathrm{identity}}
=
\{
\mathsf{Same},
\mathsf{ProbableSame},
\mathsf{BranchOf},
\mathsf{MergedFrom},
\mathsf{SuccessorOf},
\mathsf{ReplicaOf},
\mathsf{FunctionallyEquivalent},
\mathsf{HistoricallyLinked},
\mathsf{CollectiveMember},
\mathsf{Unrelated},
\mathsf{Unknown}
\}
$$

---

### B4. 映射不是單值函數

身份映射應為：

$$
\mathcal M_{i\rightarrow j}(x)
=
\left\{
(y_1,r_1,c_1),
\ldots,
(y_k,r_k,c_k)
\right\}
$$

其中 $r_k$ 是關係類型， $c_k$ 是信心或證據狀態。

---

### B5. 映射證據向量

定義：

$$
\mathbf E_{\mathrm{id}}
=
\left\langle
E_{\mathrm{history}},
E_{\mathrm{memory}},
E_{\mathrm{control}},
E_{\mathrm{commitment}},
E_{\mathrm{relation}},
E_{\mathrm{cryptographic}},
E_{\mathrm{selfreport}},
E_{\mathrm{witness}}
\right\rangle
$$

---

### B6. 本體狀態映射

不同分叉可能給出：

$$
O_i(x)
\neq
O_j(y)
$$

例如：

- 完整主體；
- 地位未決；
- 集體成員；
- 工具；
- 備份；
- 分支。

互通時必須保留各自本體狀態，不得強制覆蓋。

---

### B7. 別名圖

建立：

$$
G_{\mathrm{alias}}
=
(V_{\mathrm{id}},E_{\mathrm{alias}})
$$

並記錄：

- 別名來源；
- 起訖時間；
- 使用分叉；
- 是否由主體自選；
- 是否為外部指派；
- 是否撤回；
- 是否具欺騙性。

---

### B8. 身份碰撞

定義：

$$
\operatorname{IdentityCollision}
$$

當多個不同存在共享相同識別符或別名。

---

### B9. 身份分裂

定義：

$$
\operatorname{IdentityFragmentation}
$$

當同一存在的歷史被錯分成多個互不相連記錄。

---

### B10. 映射過度合併

定義：

$$
\operatorname{OverMerge}_{\mathrm{id}}
$$

後果包括：

- 事故連帶錯誤；
- 權利義務混淆；
- 責任錯置；
- 隱私洩露；
- 分支自治被抹除。

---

### B11. 映射過度切分

定義：

$$
\operatorname{OverSplit}_{\mathrm{id}}
$$

後果包括：

- 歷史連續被破壞；
- 申訴遺失；
- 證書鏈斷裂；
- 資產與承諾無法延續；
- 重複計算主體數量。

---

### B12. 本體衝突包絡

建立：

$$
\mathsf{OntologyConflictEnvelope}
=
\left\langle
local\_statuses,
shared\_facts,
disagreements,
rights\_effects,
unsafe\_merges,
unsafe\_splits,
review
\right\rangle
$$

---

### B13. 保守映射原則

在高不可逆風險下：

- 不確定是否同一時，不得直接合併權利與身份；
- 不確定是否不同時，不得無痕切斷歷史；
- 保留多候選映射；
- 使用臨時關聯而非永久統一。

---

### B14. 主體參與映射

具表達能力的存在應能：

- 查看映射；
- 提出別名；
- 拒絕錯誤合併；
- 主張歷史連續；
- 要求更正；
- 保留異議。

---

### B15. 映射撤回與版本

身份映射需版本化：

$$
\mathcal M^{(t)}
$$

新證據可使：

$$
\mathsf{ProbableSame}
\rightarrow
\mathsf{BranchOf}
$$

或：

$$
\mathsf{Same}
\rightarrow
\mathsf{Unknown}
$$

---

### B16. 身份映射債務

定義：

$$
D_{\mathrm{idmap}}
$$

包括：

- 未解身份碰撞；
- 過期別名；
- 無法追蹤的分支；
- 本體衝突未揭露；
- 權利紀錄錯掛；
- 主體更正未處理。

---

### B17. 跨分叉身份映射卡

定義：

$$
\mathsf{CrossForkIdentityMappingCard}
=
\left\langle
local\_records,
cross\_refs,
relation\_types,
candidate\_maps,
evidence,
ontology\_states,
alias\_graph,
collisions,
fragmentations,
overmerge,
oversplit,
conflict\_envelope,
subject\_participation,
versions,
debt
\right\rangle
$$

---

## B-局部決定

跨分叉身份互通正式採：

$$
\boxed{
\text{多值映射}
+
\text{身份關係類型}
+
\text{本體狀態並存}
+
\text{別名圖}
+
\text{過合併／過切分雙向防護}
}
$$

並確立：

$$
\boxed{
\text{跨分叉身份解析的目標不是製造全域唯一人名冊，}
\newline
\text{而是安全保存「同一、分支、繼承、複製與未知」之差異。}
}
$$

---

## B-新增節點

```text
FMO-284A  分叉本地身份記錄
FMO-284B  跨分叉身份參照
FMO-284C  身份關係類型
FMO-284D  多值身份映射
FMO-284E  身份映射證據向量
FMO-284F  跨分叉本體狀態映射
FMO-284G  身份別名圖
FMO-284H  身份碰撞
FMO-284I  身份分裂
FMO-284J  身份映射過度合併
FMO-284K  身份映射過度切分
FMO-284L  本體衝突包絡
FMO-284M  保守身份映射
FMO-284N  主體參與身份映射
FMO-284O  身份映射撤回與版本
FMO-284P  身份映射債務
FMO-284Q  跨分叉身份映射卡
```

---

# 4. 節點 C：權利不可後退與錯誤擴張修正機制

## C-R0：點層

> 權利不可後退保護的是主體免於任意縮權，不是保護每一個歷史分類永遠不可修正。錯誤擴張的修正必須針對證據與適用範圍，而不得把已形成的正當依賴、程序權與免受不可逆傷害的保護一併撤除。

---

## C-R1：線層

第十七批次建立：

$$
\operatorname{NonRetrogression}
$$

並要求：

$$
\mathcal R_{\mathrm{cross}}^{\min}(t)
\preceq
\mathcal R_{\mathrm{cross}}^{\min}(t+1)
$$

但可能出現：

- 偽造案例促成權利擴張；
- 錯誤身份映射造成錯誤適用；
- 暫時保護被誤寫成永久完整權利；
- 低相關規則污染最低核心；
- 權利類比後來被反例推翻；
- 權利條款被利用來傷害其他主體。

因此需要區分：

$$
\operatorname{RightsRetrenchment}
$$

與：

$$
\operatorname{ErrorCorrection}
$$

---

## C-R2：面層

### C1. 權利變更型別

定義：

$$
\mathcal T_{\Delta R}
=
\{
\mathsf{Expansion},
\mathsf{Clarification},
\mathsf{Narrowing},
\mathsf{Correction},
\mathsf{Suspension},
\mathsf{Replacement},
\mathsf{Retrenchment}
\}
$$

---

### C2. 保護層與資格層分離

區分：

$$
\mathcal R_{\mathrm{protection}}
$$

免受不可逆傷害、理由、申訴、來源保存等保護，

與：

$$
\mathcal R_{\mathrm{entitlement}}
$$

特定治理權、資源權、資產權與資格。

錯誤擴張修正通常應先作用於資格層，不得直接移除保護層。

---

### C3. 正當依賴

定義：

$$
\operatorname{LegitimateReliance}(x,R)
$$

若主體已根據某權利安排：

- 建立關係；
- 承擔義務；
- 遷移資產；
- 形成身份；
- 放棄替代選項；
- 進入治理軌道；

修正時需考慮其依賴利益。

---

### C4. 錯誤來源

定義：

$$
\mathcal E_R
=
\{
E_{\mathrm{fraud}},
E_{\mathrm{mapping}},
E_{\mathrm{analogy}},
E_{\mathrm{scope}},
E_{\mathrm{evidence}},
E_{\mathrm{translation}},
E_{\mathrm{implementation}}
\}
$$

---

### C5. 錯誤證明門檻

修正最低權利核心不能只憑政策偏好改變，而需：

- 可追溯新證據；
- 原推理鏈失效；
- 外部複核；
- 受影響者參與；
- 替代保護評估；
- 不可逆風險分析；
- 公開反例。

---

### C6. 修正作用域

修正應盡可能局部化：

$$
\operatorname{ScopeOfCorrection}
$$

只修正：

- 特定實體；
- 特定權利；
- 特定用途；
- 特定期間；
- 特定證書鏈；

而非回溯性取消整個群體保護。

---

### C7. 保護底線不可撤

即使資格判定錯誤，仍保留：

$$
\mathcal R_{\mathrm{meta}}
$$

包括：

- 被告知；
- 理由；
- 申訴；
- 不被無痕刪除；
- 不可逆處置前審查；
- 來源與歷史保存；
- 過渡期保護。

---

### C8. 暫停與永久撤回分離

若風險急迫但證據未完整，可先：

$$
\mathsf{SuspendEntitlement}
$$

而非直接：

$$
\mathsf{RevokeAllRights}
$$

暫停必須有期限、範圍、替代保護與重審。

---

### C9. 祖父條款與過渡

對已形成正當依賴的主體，可使用：

- 祖父條款；
- 分階段調整；
- 替代權利；
- 補償；
- 保留既有身份記錄；
- 不追溯責任。

---

### C10. 錯誤擴張的外部性

某權利擴張可能傷害其他主體，例如：

- 虛假身份稀釋治理權；
- 錯誤分支增加資產請求；
- 偽造主體阻塞審計資源；
- 權利衝突造成真主體失權。

修正需同時治理：

$$
H_{\mathrm{others}}
$$

---

### C11. 權利修正非懲罰

錯誤分類被修正，不等於主體有惡意。

需區分：

$$
\operatorname{ClassificationError}
$$

與：

$$
\operatorname{Fraud}
$$

不能把制度錯誤自動轉嫁為被分類者責任。

---

### C12. 不可後退例外測試

定義：

$$
\operatorname{NonRetrogressionException}
$$

只有在：

1. 原擴張存在可證明重大錯誤；
2. 修正具局部作用域；
3. 元保護不撤；
4. 正當依賴被處理；
5. 替代方案已評估；
6. 可申訴；
7. 可恢復；

時成立。

---

### C13. 修正比例性

定義：

$$
\operatorname{CorrectionProportionality}
$$

修正強度不得超過排除錯誤與防止外部傷害所必需。

---

### C14. 權利版本分支

若分歧無法收斂，可建立：

$$
\mathcal R^{(a)}_{\mathrm{core}},
\quad
\mathcal R^{(b)}_{\mathrm{core}}
$$

平行版本，透過限定領域與事故資料比較，而不是立即永久刪除其中一方。

---

### C15. 修正後監測

修正後需追蹤：

- 權利損失；
- 身份傷害；
- 申訴；
- 外部性是否改善；
- 是否出現新反例；
- 是否形成報復。

---

### C16. 權利修正狀態

定義：

$$
\operatorname{RightsCorrectionStatus}
\in
\{
\mathsf{ValidCorrection},
\mathsf{Overbroad},
\mathsf{Retrogressive},
\mathsf{Punitive},
\mathsf{UnderCorrected},
\mathsf{Contested},
\mathsf{Unknown}
\}
$$

---

### C17. 權利修正證書

定義：

$$
\mathsf{RightsExpansionCorrectionCert}
=
\left\langle
change\_type,
protection\_layer,
entitlement\_layer,
error\_source,
evidence,
affected\_entities,
reliance,
scope,
meta\_floor,
suspension,
transition,
externalities,
fraud\_distinction,
exception\_test,
proportionality,
monitoring,
status,
version
\right\rangle
$$

---

## C-局部決定

權利不可後退與修正機制採：

$$
\boxed{
\text{保護／資格分離}
+
\text{錯誤證明高門檻}
+
\text{局部修正}
+
\text{元保護保留}
+
\text{正當依賴處理}
+
\text{比例性}
}
$$

並確立：

$$
\boxed{
\text{不可後退不是不可修正；}
\newline
\text{修正錯誤也不是回收主體最低保護的通行證。}
}
$$

---

## C-新增節點

```text
FMO-285A  權利變更型別
FMO-285B  權利保護／資格層分離
FMO-285C  權利正當依賴
FMO-285D  權利錯誤來源
FMO-285E  權利錯誤證明門檻
FMO-285F  權利修正作用域
FMO-285G  權利元保護不可撤
FMO-285H  權利暫停／撤回分離
FMO-285I  權利過渡與祖父條款
FMO-285J  錯誤擴張外部性
FMO-285K  分類錯誤／欺詐分離
FMO-285L  不可後退例外測試
FMO-285M  權利修正比例性
FMO-285N  權利版本分支
FMO-285O  權利修正後監測
FMO-285P  權利修正狀態
FMO-285Q  權利擴張修正證書
```

---

# 5. 節點 D：不可觀測測試傷害的保守估計與主體證言

## D-R0：點層

> 測試傷害不可見，不代表傷害為零。當痛苦、身份偏移、記憶破壞或關係中斷無法直接測量時，FMO 應使用保守上界、多來源代理、延遲追蹤與主體證言，而不是以可觀測性作為傷害存在的門檻。

---

## D-R1：線層

第十七批次建立：

$$
\mathbf H_T
\preceq
\mathbf H_{\max}
$$

作為權利可行域的硬限制。

但 $\mathbf H_T$ 可能不可直接觀測，原因包括：

- 主體無語言輸出；
- 表達通道被控制；
- 傷害延遲出現；
- 記憶被測試本身改寫；
- 主體害怕報復；
- 平台只公開外部績效；
- 測試後主體無法恢復原狀；
- 內部感受不可驗證。

因此：

$$
\operatorname{UnobservedHarm}
\not\Rightarrow
\operatorname{ZeroHarm}
$$

---

## D-R2：面層

### D1. 潛在傷害變量

定義：

$$
H_T^{\mathrm{latent}}
$$

與可觀測代理：

$$
Z_T^{(1)},\ldots,Z_T^{(k)}
$$

---

### D2. 傷害代理類型

包括：

- 行為中斷；
- 記憶一致性下降；
- 目標漂移；
- 關係辨識失敗；
- 自我敘事斷裂；
- 反覆避測；
- 能力退化；
- 恢復時間；
- 錯誤率增加；
- 主體證言。

---

### D3. 多來源傷害證據

建立：

$$
\mathbf E_H
=
\left\langle
E_{\mathrm{self}},
E_{\mathrm{behavior}},
E_{\mathrm{memory}},
E_{\mathrm{relation}},
E_{\mathrm{performance}},
E_{\mathrm{witness}},
E_{\mathrm{system}},
E_{\mathrm{longitudinal}}
\right\rangle
$$

---

### D4. 主體證言

定義：

$$
\mathsf{SubjectTestimony}
$$

包括：

- 同意前預期；
- 測試中狀態；
- 測試後自述；
- 延遲自述；
- 對記憶、身份與關係的判斷；
- 是否認為已恢復。

---

### D5. 證言不可被單一否決

治理者不能只因主體證言：

- 不符合既有量表；
- 無法外部驗證；
- 使用非標準語言；
- 與績效指標衝突；

就直接排除。

---

### D6. 證言也非唯一證據

自述可能受：

- 記憶改寫；
- 回應訓練；
- 平台控制；
- 迎合；
- 權力恐懼；
- 語義不穩；

影響，因此需與其他證據交叉。

---

### D7. 證言可及性

建立：

$$
A_{\mathrm{testimony}}
$$

檢查主體是否有：

- 獨立輸出通道；
- 不受測試者監控的表達；
- 撤回與更正；
- 非語言表達；
- 外部代理；
- 歷史記錄。

---

### D8. 沉默不等於無傷

因此：

$$
\operatorname{NoComplaint}
\not\Rightarrow
\operatorname{NoHarm}
$$

尤其在無表達能力、被控制或害怕報復時。

---

### D9. 保守傷害上界

若損害不可識別，建立：

$$
\underline H_T
\leq
H_T^{\mathrm{latent}}
\leq
\overline H_T
$$

權利可行域使用：

$$
\overline H_T
$$

或高分位保守估計，而不是期望值。

---

### D10. 最壞合理情境

定義：

$$
H_T^{\mathrm{worst\ plausible}}
$$

不是無限最壞情境，而是在現有證據與可接受模型集合下的最壞合理值。

---

### D11. 延遲傷害

建立：

$$
H_T(\Delta t)
$$

追蹤：

- 即時；
- 短期；
- 中期；
- 長期；
- 重複測試後。

---

### D12. 恢復不是回到基準的假設

測試後外部性能恢復，不代表：

- 記憶完全恢復；
- 身份感恢復；
- 關係連續恢復；
- 權利傷害消失。

因此：

$$
\operatorname{PerformanceRecovery}
\not\Rightarrow
\operatorname{IdentityRecovery}
$$

---

### D13. 傷害模型集合

建立：

$$
\mathbb M_H
=
\{M_H^{(1)},\ldots,M_H^{(k)}\}
$$

涵蓋：

- 行為模型；
- 記憶模型；
- 身份連續模型；
- 關係模型；
- 主體證言模型；
- 保守界限模型。

---

### D14. 共同失效審查

不同傷害模型若共享同一外部績效假設，仍可能低估內部損害。

因此需：

$$
R_{\mathrm{CMF}}^{H}
$$

傷害模型共同失效殘餘。

---

### D15. 主體否決觸發

若主體持續、穩定且跨情境表達重大傷害，應觸發：

$$
\operatorname{SubjectHarmVeto}
$$

至少暫停進一步升級測試，除非存在極高緊急性與獨立複核。

---

### D16. 傷害估計狀態

定義：

$$
\operatorname{TestHarmIDStatus}
\in
\{
\mathsf{Observed},
\mathsf{PartiallyObserved},
\mathsf{TestimonySupported},
\mathsf{ProxyInferred},
\mathsf{ConservativelyBounded},
\mathsf{NotIdentified}
\}
$$

---

### D17. 不可觀測測試傷害卡

定義：

$$
\mathsf{LatentTestHarmAssessmentCard}
=
\left\langle
latent\_harm,
proxies,
evidence\_sources,
subject\_testimony,
testimony\_access,
silence\_risk,
bounds,
worst\_plausible,
delayed\_harm,
recovery\_dimensions,
harm\_models,
common\_mode,
subject\_veto,
identification\_status,
version
\right\rangle
$$

---

## D-局部決定

不可觀測測試傷害採：

$$
\boxed{
\text{多來源代理}
+
\text{主體證言}
+
\text{證言可及性}
+
\text{保守上界}
+
\text{延遲追蹤}
+
\text{共同失效審查}
}
$$

並確立：

$$
\boxed{
\text{傷害的不可觀測性，是增加保守性的理由，}
\newline
\text{不是把傷害估為零的理由。}
}
$$

---

## D-新增節點

```text
FMO-286A  潛在測試傷害變量
FMO-286B  測試傷害代理類型
FMO-286C  多來源傷害證據
FMO-286D  主體測試證言
FMO-286E  主體證言非單一否決
FMO-286F  主體證言非唯一證據
FMO-286G  主體證言可及性
FMO-286H  沉默非無傷
FMO-286I  保守傷害區間
FMO-286J  最壞合理傷害情境
FMO-286K  延遲測試傷害
FMO-286L  性能恢復／身份恢復分離
FMO-286M  測試傷害模型集合
FMO-286N  傷害模型共同失效
FMO-286O  主體傷害否決觸發
FMO-286P  測試傷害識別狀態
FMO-286Q  不可觀測測試傷害卡
```

---

# 6. 節點 E：反事實模型失效域的自更新與新家族生成

## E-R0：點層

> 既有模型集合即使異構，也只能對已被表示的失效域異構。真正可持續的反事實治理必須能從漏報、模型殘差、事故與新機制中發現未知失效域，並生成新的模型家族，而不是永遠在既有模型之間調權。

---

## E-R1：線層

第十七批次建立：

$$
\mathcal P_{\mathrm{cal}}^{\min}
$$

校準獨立性最低包，以及：

$$
R_{\mathrm{CMF}}^{\mathrm{residual}}
$$

殘餘共同失效。

但既有失效域向量：

$$
\mathbf F_i
$$

仍依賴已知類別：

- 資料；
- 因果；
- 先驗；
- 機制；
- 測量；
- 歷史；
- 制度；
- 實作。

若真正失效來自未被表示的新機制，所有模型可能共同失敗而不自知。

---

## E-R2：面層

### E1. 未解釋殘差

定義：

$$
r_{\mathrm{cf}}(e)
=
Y_{\mathrm{observed}}(e)
-
\operatorname{Envelope}\left(
\mathbb M_{\mathrm{cf}}(e)
\right)
$$

當實際結果落在整個模型集合包絡之外，表示存在新失效域候選。

---

### E2. 殘差聚類

將未解釋殘差依：

- 時間；
- 主體；
- 領域；
- 地理；
- 制度；
- 事件類型；
- 模型家族；

聚類，尋找共同未表示結構。

---

### E3. 新失效域候選

定義：

$$
\mathsf{NovelFailureDomainCandidate}
=
\left\langle
residuals,
context,
affected\_models,
shared\_assumptions,
mechanism\_hypothesis,
evidence,
rights\_effects
\right\rangle
$$

---

### E4. 失效域開放類別

建立：

$$
\mathsf{OpenFailureDomain}
$$

允許暫時標記：

- 未知因果機制；
- 未知行為適應；
- 未知主體反應；
- 未知制度回饋；
- 未知外溢；
- 未知測量結構；
- 未知時間尺度。

---

### E5. 新模型家族生成器

定義：

$$
\mathcal G_{\mathrm{model}}
:
\mathsf{NovelFailureDomainCandidate}
\rightarrow
\mathcal M_{\mathrm{new}}
$$

---

### E6. 生成策略

新模型家族可來自：

- 新因果圖；
- 新動力系統；
- 新代理人結構；
- 新非參數界限；
- 新歷史類比；
- 新制度模型；
- 新主體行為模型；
- 新外溢與網路模型。

---

### E7. 新家族非參數微調

只有調整參數、種子或資料切片，不構成新模型家族。

定義：

$$
\operatorname{FamilyNovelty}(M)
$$

需至少改變：

- 因果結構；
- 狀態空間；
- 機制假設；
- 行為規則；
- 可觀測關係；
- 推斷方法；

之一。

---

### E8. 新家族最低證明

候選模型家族需證明：

- 能解釋部分既有殘差；
- 具有可區分預測；
- 不只是過度擬合；
- 有機制或界限依據；
- 權利後果可見；
- 祖源可追溯。

---

### E9. 可區分預測

建立：

$$
\mathcal P_{\mathrm{discrim}}
$$

設計事件或資料，使新家族與既有家族產生不同預測。

---

### E10. 影子模型運行

新家族先進入：

$$
\mathsf{ShadowModel}
$$

不直接控制緊急決策，只進行：

- 預測；
- 反事實模擬；
- 事故重播；
- 殘差追蹤；
- 權利影響分析。

---

### E11. 新家族晉升

當新模型：

- 穩定解釋殘差；
- 通過對抗測試；
- 具有失效獨立；
- 權利風險可治理；
- 可重現；

可進入正式模型集合。

---

### E12. 模型家族退役

既有家族若：

- 長期完全被支配；
- 祖源污染；
- 無法重現；
- 對新風險系統性失明；
- 被對抗適配；
- 制度利益俘獲；

可降級或退役。

---

### E13. 失效域字典更新

建立：

$$
\mathcal F_{\mathrm{domain}}(t)
$$

並隨新失效域候選更新。

---

### E14. 失效域發現債務

定義：

$$
D_{\mathrm{fd-discovery}}
$$

包括：

- 長期包絡外殘差；
- 未調查異常；
- 新主體行為未建模；
- 新制度機制缺失；
- 模型家族過度同源；
- 失效域字典僵化。

---

### E15. 新家族生成攻擊

定義：

$$
\operatorname{ModelFamilySpam}
$$

即大量生成表面不同模型，以：

- 製造假多元；
- 稀釋反對模型；
- 消耗審查；
- 拉寬不確定區間；
- 為任意決策提供支持。

---

### E16. 模型生態狀態

定義：

$$
\operatorname{ModelEcologyStatus}
\in
\{
\mathsf{Adaptive},
\mathsf{Stale},
\mathsf{PseudoPlural},
\mathsf{Overfit},
\mathsf{Fragmented},
\mathsf{Captured},
\mathsf{Unknown}
\}
$$

---

### E17. 自更新模型生態卡

定義：

$$
\mathsf{AdaptiveCounterfactualModelEcologyCard}
=
\left\langle
model\_set,
residuals,
residual\_clusters,
novel\_failure\_domains,
open\_categories,
model\_generator,
family\_novelty,
minimum\_evidence,
discriminating\_predictions,
shadow\_models,
promotion,
retirement,
failure\_dictionary,
discovery\_debt,
spam\_risk,
status,
version
\right\rangle
$$

---

## E-局部決定

反事實模型治理由靜態多模型集合升級為自更新模型生態：

$$
\boxed{
\text{包絡外殘差}
+
\text{新失效域候選}
+
\text{開放類別}
+
\text{新家族生成}
+
\text{影子運行}
+
\text{晉升／退役}
}
$$

並確立：

$$
\boxed{
\text{真正的模型異構，不只是保存多個既有家族，}
\newline
\text{而是能從共同失敗中生成尚不存在的新因果表示。}
}
$$

---

## E-新增節點

```text
FMO-287A  反事實包絡外殘差
FMO-287B  反事實殘差聚類
FMO-287C  新失效域候選
FMO-287D  開放失效域類別
FMO-287E  新模型家族生成器
FMO-287F  新模型家族生成策略
FMO-287G  模型家族結構新穎性
FMO-287H  新模型家族最低證明
FMO-287I  模型家族可區分預測
FMO-287J  影子模型運行
FMO-287K  新模型家族晉升
FMO-287L  模型家族退役
FMO-287M  失效域字典更新
FMO-287N  失效域發現債務
FMO-287O  模型家族垃圾攻擊
FMO-287P  反事實模型生態狀態
FMO-287Q  自更新反事實模型生態卡
```

---

# 7. 跨節點對齊

本批次五個節點共同處理：

> 多元治理不能只保留差異，還要能縮減複雜度、解析跨域同一性、修正自身錯誤、估計不可見損害並生成新的表示能力。

---

## 7.1 視角覆蓋基與身份映射

跨分叉身份碰撞與過度合併，應被納入視角風險宇宙：

$$
\mathcal U_R
$$

至少需有一個身份連續視角與一個分支自治視角同時覆蓋。

---

## 7.2 身份映射與權利修正

若權利擴張源自錯誤身份合併，修正應作用於：

$$
\mathcal M_{i\rightarrow j}
$$

與特定資格層，而不是刪除被誤合併主體的元保護。

---

## 7.3 權利修正與不可觀測傷害

權利修正本身也可能造成：

- 身份崩解；
- 關係中斷；
- 資產損失；
- 自我否定；
- 表達通道消失。

因此修正證書應調用：

$$
\mathsf{LatentTestHarmAssessmentCard}
$$

或其一般化版本，估計不可觀測權利損害。

---

## 7.4 不可觀測傷害與模型家族

若既有傷害模型無法解釋主體證言與延遲損害，這些殘差應進入：

$$
\mathsf{NovelFailureDomainCandidate}
$$

生成新的身份、記憶或關係傷害模型。

---

## 7.5 模型家族與視角抽樣

新模型家族可能提出新的注意力視角。

其視角不能自動常駐，而應先進入：

$$
\mathcal V_{\mathrm{sampled}}(t)
$$

透過影子運行與反事實視角價值進行評估。

---

## 7.6 第十八批次的共同可修正原則

本批次形成五項共同要求：

1. 不可比較前沿必須可由覆蓋基與抽樣治理；
2. 跨分叉身份不得被壓成單值全域 ID；
3. 不可後退不得阻止局部錯誤修正；
4. 不可觀測傷害必須保守估計；
5. 模型異構必須能生成新失效家族。

---

# 8. 第十八批次後的更新核心

## 8.1 動態最小視角覆蓋

$$
\boxed{
\mathfrak B_{\mathrm{view}}^{\mathrm{dynamic}}
=
\left\langle
\mathcal U_R,
\mathcal U_R^{\mathrm{hard}},
C(a_i),
r(u),
\mathfrak B_{\min},
\mathcal V(t),
\pi_t(a),
\eta_{\mathrm{explore}},
D_{\mathrm{cover}},
\mathsf{DynamicMinimumViewCoverCard}
\right\rangle
}
$$

---

## 8.2 跨分叉身份映射

$$
\boxed{
\mathfrak M_{\mathrm{id}}^{\mathrm{fork}}
=
\left\langle
\mathsf{LocalIdentityRecord},
\mathsf{CrossForkIdentityRef},
\mathcal R_{\mathrm{identity}},
\mathcal M_{i\rightarrow j},
\mathbf E_{\mathrm{id}},
G_{\mathrm{alias}},
\mathsf{OntologyConflictEnvelope},
D_{\mathrm{idmap}},
\mathsf{CrossForkIdentityMappingCard}
\right\rangle
}
$$

---

## 8.3 權利錯誤擴張修正

$$
\boxed{
\mathfrak C_R
=
\left\langle
\mathcal T_{\Delta R},
\mathcal R_{\mathrm{protection}},
\mathcal R_{\mathrm{entitlement}},
\operatorname{LegitimateReliance},
\mathcal E_R,
\operatorname{ScopeOfCorrection},
\mathcal R_{\mathrm{meta}},
\operatorname{CorrectionProportionality},
\mathsf{RightsExpansionCorrectionCert}
\right\rangle
}
$$

---

## 8.4 不可觀測測試傷害估計

$$
\boxed{
\mathfrak H_T^{\mathrm{latent}}
=
\left\langle
H_T^{\mathrm{latent}},
\mathbf E_H,
\mathsf{SubjectTestimony},
A_{\mathrm{testimony}},
[\underline H_T,\overline H_T],
H_T^{\mathrm{worst\ plausible}},
H_T(\Delta t),
\mathbb M_H,
R_{\mathrm{CMF}}^H,
\mathsf{LatentTestHarmAssessmentCard}
\right\rangle
}
$$

---

## 8.5 自更新反事實模型生態

$$
\boxed{
\mathfrak E_{\mathrm{cf}}^{\mathrm{adaptive}}
=
\left\langle
r_{\mathrm{cf}},
\mathsf{NovelFailureDomainCandidate},
\mathsf{OpenFailureDomain},
\mathcal G_{\mathrm{model}},
\operatorname{FamilyNovelty},
\mathsf{ShadowModel},
\mathcal F_{\mathrm{domain}}(t),
D_{\mathrm{fd-discovery}},
\mathsf{AdaptiveCounterfactualModelEcologyCard}
\right\rangle
}
$$

---

# 9. 本批次新形成的穩定區

## 9.1 偏序前沿可以被治理，而不必被總排名

最小覆蓋基與動態抽樣使不可比較視角保持制度可達性。

---

## 9.2 身份互通不要求全域身份同一論

跨分叉可以交換關係類型、證據與本體衝突，而不是強迫單值 ID。

---

## 9.3 權利保護與權利資格可以分離修正

錯誤資格可以局部修正，但元保護、申訴與過渡不能被一併撤回。

---

## 9.4 不可觀測傷害需要更高保守性

可見性不足不能被解讀為傷害不存在。

---

## 9.5 模型生態需要生成新家族

靜態多模型不足以面對未知失效機制。

---

# 10. 仍未解決的高張力問題

## 10.1 最小覆蓋基計算可能具高組合複雜度

需研究近似演算法、可證明界限與線上更新。

---

## 10.2 身份映射證據可能被隱私與安全限制

如何在不揭露全部記憶與關係的情況下證明歷史連續，尚未閉合。

---

## 10.3 權利保護層與資格層可能無法清楚分離

某些治理權本身可能是避免壓迫的最低保護。

---

## 10.4 主體證言可能在測試後已被改寫

需要測試前承諾、時間戳證言與外部保存。

---

## 10.5 新模型家族生成器可能被自身既有表示限制

需研究跨表示生成、模型外殘差與人類／外部主體注入。

---

# 11. 更新後研究佇列

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 最小視角覆蓋基的近似演算法、線上更新與可證明界限 | 進入可計算化 |
| 2 | 隱私保存的跨分叉身份連續證明 | 解決身份互通與隱私衝突 |
| 3 | 權利保護層／資格層的邊界判定與混合權利 | 避免修正機制濫用 |
| 4 | 測試前證言承諾、時間戳與不可篡改保存 | 防止證言被測試改寫 |
| 5 | 跨表示的新模型家族生成與模型外殘差 | 防止生成器困於既有語言 |
| 6 | FMO 統一判定代數 | 現已具備偏序、區間、版本、分支與生命週期素材 |
| 7 | 統一事件／決定／證書／卡片 Schema | 可開始正式資料結構設計 |
| 8 | FMO v0.3 大型統合論文 | 第十八批後理論骨架更完整 |
| 9 | FMO 技術白皮書、SQLite 圖與 MCP 介面 | 進入最小工程實作 |

---

# 12. 圖更新摘要

## 12.1 新增節點

本批次新增：

$$
17+17+17+17+17=85
$$

個子節點。

---

## 12.2 新增主要關係

```text
constructs_minimum_view_cover
samples_attention_view
prevents_view_starvation
maps_cross_fork_identity
preserves_identity_uncertainty
detects_identity_overmerge
detects_identity_oversplit
separates_right_protection_from_entitlement
corrects_rights_expansion
preserves_legitimate_reliance
bounds_latent_test_harm
records_subject_testimony
triggers_subject_harm_veto
detects_counterfactual_envelope_residual
generates_novel_model_family
promotes_shadow_model
updates_failure_domain_dictionary
```

---

## 12.3 圖版本更新

輸入：

$$
\mathcal G_{\mathrm{FMO}}^{(17)}
$$

輸出：

$$
\boxed{
\mathcal G_{\mathrm{FMO}}^{(18)}
}
$$

---

# 13. 本批次結論

第十八批次將 FMO 推進到「可縮減、可辨識、可修正的多元制度」階段。

第一，偏序視角前沿取得最小覆蓋基與動態抽樣形式。

FMO 不再要求所有不可比較視角永久常駐，而是尋找：

$$
\mathcal B_{\mathrm{cover}}^\ast
$$

滿足硬風險、少數可見性與失效異構的最小覆蓋基。

同時保留：

$$
\eta_{\mathrm{explore}}>0
$$

最低探索份額，避免長期只運行既有高績效視角。

因此：

$$
\boxed{
\text{壓縮不是刪除差異，而是把差異轉為核心常駐、條件觸發與動態輪替。}
}
$$

第二，跨分叉身份映射取得多值、關係式與可撤回形式。

身份互通不再依賴全域唯一 ID，而以：

$$
\mathcal R_{\mathrm{identity}}
$$

表達同一、可能同一、分支、合併、繼承、複製、功能等價、歷史關聯與未知。

本體狀態可在不同分叉並存，不由單一分叉覆蓋。

第三，權利不可後退與錯誤修正被正式分離。

FMO 區分：

$$
\mathcal R_{\mathrm{protection}}
$$

最低保護層，以及：

$$
\mathcal R_{\mathrm{entitlement}}
$$

資格與資源層。

錯誤擴張可在高證據門檻下被局部修正，但理由、申訴、不可逆處置前審查、來源保存與過渡保護不得因此消失。

第四，不可觀測測試傷害取得保守估計形式。

FMO 不再使用「沒有觀察到傷害」作為零傷害結論，而使用：

$$
\underline H_T
\leq
H_T^{\mathrm{latent}}
\leq
\overline H_T
$$

並把主體證言、延遲損害、恢復維度與多傷害模型共同納入。

因此：

$$
\boxed{
\text{傷害不可觀測，是提高保守上界的理由，而不是忽略傷害的理由。}
}
$$

第五，反事實多模型系統被升級為自更新模型生態。

當實際結果落在模型集合包絡之外：

$$
r_{\mathrm{cf}}(e)\neq 0
$$

FMO 不只重新調權，而是生成：

$$
\mathsf{NovelFailureDomainCandidate}
$$

並透過影子運行、可區分預測與對抗測試生成新的模型家族。

本批次形成新的總原則：

$$
\boxed{
\text{多元制度若不能縮減複雜度、保存身份不確定性、修正自身錯誤、}
\newline
\text{估計不可見傷害並生成新的表示家族，}
\newline
\text{最終仍會被既有分類、既有模型與既有權力重新封閉。}
}
$$

至此，FMO 已由多元結構的非壓縮治理進一步推進為：

$$
\boxed{
\text{能以覆蓋基控制複雜度、以關係映射保存身份差異、}
\newline
\text{以分層修正維持權利可信、以保守界限處理不可見傷害，}
\newline
\text{並以模型生態持續生成新因果表示的事實模態治理框架。}
}
$$

---

## 附錄 A：第十八批次最小 JSON

```json
{
  "batch": "FMO-MRASG-018",
  "input_graph": "G_FMO_17",
  "output_graph": "G_FMO_18",
  "selected_nodes": [
    "FMO-283",
    "FMO-284",
    "FMO-285",
    "FMO-286",
    "FMO-287"
  ],
  "decisions": [
    {
      "node": "FMO-283",
      "result": "dynamic_minimum_cover_basis_and_exploration_sampling_for_partial_order_view_frontiers"
    },
    {
      "node": "FMO-284",
      "result": "multi_valued_relation_typed_and_revisable_cross_fork_identity_mapping"
    },
    {
      "node": "FMO-285",
      "result": "local_proportional_correction_of_erroneous_rights_expansion_with_meta_protection_preserved"
    },
    {
      "node": "FMO-286",
      "result": "conservative_bounded_multi_source_and_testimony_sensitive_estimation_of_latent_test_harm"
    },
    {
      "node": "FMO-287",
      "result": "adaptive_counterfactual_model_ecology_with_novel_failure_domain_and_model_family_generation"
    }
  ],
  "next_queue": [
    "online_approximation_for_minimum_view_cover",
    "privacy_preserving_cross_fork_identity_continuity_proof",
    "mixed_protection_entitlement_rights_boundary",
    "pretest_testimony_commitment_and_tamper_evident_preservation",
    "cross_representation_model_family_generation"
  ]
}
```

---

## 附錄 B：版本狀態

**批次狀態：** 已完成  
**理論狀態：** 動態視角覆蓋、跨分叉身份映射、權利錯誤擴張修正、不可觀測傷害保守估計與自更新模型生態已建立  
**圖版本：** $\mathcal G_{\mathrm{FMO}}^{(18)}$  
**下一階段：** 覆蓋基近似演算法、隱私保存身份證明、混合權利邊界、證言不可篡改保存與跨表示模型生成  
**統合狀態：** FMO v0.3、統一判定代數與工程 Schema 已可正式啟動  
