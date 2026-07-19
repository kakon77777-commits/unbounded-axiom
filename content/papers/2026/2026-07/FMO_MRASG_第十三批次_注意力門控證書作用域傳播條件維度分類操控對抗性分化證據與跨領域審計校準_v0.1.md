# FMO–MRASG 第十三研究批次

## 注意力門控、證書作用域傳播、條件維度分類操控、對抗性分化證據與跨領域審計校準

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

第十二批次將 FMO 推進到有限認知、有限證明、有限維度、有限治理權與有限審計資源條件下的可行治理。

其主要成果包括：

注意力敏感治理：

$$
\mathfrak G_{\mathrm{attn}}
=
\left\langle
B_{\mathrm{attn}},
\mathbf C_{\mathrm{review}},
\mathcal A_{\mathrm{attn}},
P_{\mathrm{attn}},
\operatorname{ReviewTrigger},
\operatorname{SummaryFidelity},
D_{\mathrm{attn}},
\mathsf{AttentionGovernanceCard}
\right\rangle
$$

近似生成等價系統：

$$
\mathfrak E_S^{\approx}
=
\left\langle
\mathcal D_{\mathrm{eq}},
\operatorname{Inv}_S,
\mathbf\Delta_{\mathrm{gen}},
\mathcal N_\Delta,
\operatorname{GenCounterexample},
D_{\mathrm{eq}},
\mathsf{ApproxKernelEqCert}
\right\rangle
$$

強制維度核：

$$
\mathfrak K_D
=
\left\langle
\mathcal C_{\mathrm{always}},
\mathcal C_{\mathrm{triggered}},
\mathcal C_{\mathrm{task}},
\mathcal C_{\mathrm{exploratory}},
G_D^{\mathrm{conf}},
L_{\mathrm{dim\_compress}},
\mathsf{MandatoryDimensionKernelCard}
\right\rangle
$$

數位治理權解聚合：

$$
\mathfrak G_{\mathrm{DSU}}
=
\left\langle
\mathbf D_G,
\mathcal C_G,
W_G,
\mathcal L_G,
\operatorname{Deaggregate},
\operatorname{DeaggregationManipulation},
S_G,
\mathsf{GovernanceDeaggregationCert}
\right\rangle
$$

審計成本—可靠性前沿：

$$
\mathfrak F_A
=
\left\langle
\mathbf C_A,
\mathbf R_A,
R_{\mathrm{CMF}}^{\mathrm{res}},
\mathcal F_A,
\mathcal L_{\mathrm{risk}},
\mathcal P_A^{(L)},
\operatorname{AuditEscalationTrigger},
\mathsf{AuditFrontierCard}
\right\rangle
$$

然而，第十二批次仍留下五個高張力問題。

第一，注意力分配器：

$$
\mathcal A_{\mathrm{attn}}
$$

本身決定哪些事件值得被看見。它若被捕獲，治理系統可能在形式透明的情況下，仍然隱藏關鍵異常。

第二，近似等價證書只在特定測試域與門檻下成立，但證書在組織、模型、文件與實作之間傳播時，容易被省略作用域，最後被誤寫成普遍同一。

第三，條件啟動維度依賴任務分類與事件觸發。治理者若把「分支」標為「備份」、把「刪除」標為「清理」、把「身份重寫」標為「系統更新」，就可能逃避身份與權利維度。

第四，數位分化證據可能被偽造。系統可以人工製造偏好差異與記憶差異以取得獨立治理權，也可以壓制真實差異，使已分化分支無法取得地位。

第五，審計成本—可靠性前沿仍主要是單任務內部結構。醫療、金融、公共基礎設施、AI 主體地位與研究系統的風險尺度不同，不能直接共享同一預算與可靠性門檻。

因此，本批次處理：

```text
FMO-258  注意力分配器的門控權與異常放大失真
FMO-259  近似等價證書的作用域誤用與證書傳播
FMO-260  條件維度觸發器的分類操控
FMO-261  數位分化證據的真偽與對抗性分化
FMO-262  審計前沿的跨領域校準與預算分配
```

本批次總問題是：

> 當治理結論透過摘要、證書、分類、證據與預算傳播時，如何防止原本有界、可撤回的判定被重新包裝成普遍、確定與不可爭議的制度事實？

---

# 1. 輸入圖

第十二批次輸出：

$$
\mathcal G_{\mathrm{FMO}}^{(12)}
$$

目前五條未閉合路徑如下。

注意力治理：

$$
\mathcal E_{\mathrm{gov}}
\xrightarrow{\mathcal A_{\mathrm{attn}}}
\mathcal E_{\mathrm{review}}
$$

但 $\mathcal A_{\mathrm{attn}}$ 可被操控。

近似等價：

$$
\mathcal R_{S,1}
\approx_{\Theta,\mathcal D}
\mathcal R_{S,2}
$$

但傳播後可能變成：

$$
\mathcal R_{S,1}
=
\mathcal R_{S,2}
$$

條件維度：

$$
\operatorname{Classify}(e)
\rightarrow
\operatorname{Trigger}(q_i)
$$

但分類本身可能被操控。

數位治理：

$$
\mathbf E_{\mathrm{div}}
\rightarrow
\mathbf D_G
\rightarrow
\mathbf R_G
$$

但 $\mathbf E_{\mathrm{div}}$ 的真偽未治理。

審計前沿：

$$
\mathcal F_A^{(d_1)}
\not\equiv
\mathcal F_A^{(d_2)}
$$

跨領域比較尚未建立。

---

# 2. 節點 A：注意力分配器的門控權與異常放大失真

## A-R0：點層

> 注意力分配器不是中立工具，而是治理入口。它既可能隱藏真正異常，也可能持續放大低價值警報，使受影響者疲勞。注意力治理必須同時防止漏報、誤報、警報轟炸與優先級壟斷。

---

## A-R1：線層

第十二批次建立：

$$
\mathcal A_{\mathrm{attn}}
:
\mathcal E_{\mathrm{gov}}
\rightarrow
\mathcal E_{\mathrm{review}}
$$

並使用事件優先級：

$$
P_{\mathrm{attn}}(e)
=
\alpha I(e)
+
\beta U(e)
+
\gamma R(e)
+
\delta D(e)
+
\epsilon V(e)
-
\zeta C(e)
$$

但任何優先級函數都可能產生：

- 真異常被壓低；
- 常見事件被過度放大；
- 高成本事件被忽略；
- 少數者風險被視為低覆蓋；
- 新型主體因缺少歷史資料而低分；
- 警報過量造成疲勞；
- 代理透過指標適配逃避監督。

---

## A-R2：面層

### A1. 注意力門控權

定義：

$$
P_{\mathrm{attn\_gate}}
$$

表示控制以下事項的權力：

- 事件是否進入審查；
- 優先級；
- 摘要層級；
- 通知對象；
- 通知時點；
- 是否升級人工；
- 是否進入歷史記錄。

---

### A2. 漏報與誤報

定義：

$$
FN_{\mathrm{attn}}
$$

為應被看見但未被選中的關鍵事件；

$$
FP_{\mathrm{attn}}
$$

為被放大但實際低價值的事件。

兩者不應用普通平均準確率掩蓋，因為高風險漏報的代價可能遠高於一般誤報。

---

### A3. 非對稱注意力損失

建立：

$$
\mathcal L_{\mathrm{attn}}
=
\alpha FN_{\mathrm{critical}}
+
\beta FN_{\mathrm{rights}}
+
\gamma FP_{\mathrm{fatigue}}
+
\delta D_{\mathrm{delay}}
+
\epsilon C_{\mathrm{review}}
$$

其中：

$$
\alpha,\beta
$$

對涉及元底線與不可逆權利損害的漏報應具有高權重或硬約束。

---

### A4. 警報疲勞

定義：

$$
F_{\mathrm{alert}}(p,t)
$$

當警報頻率、重複性與低價值比例升高時：

$$
\operatorname{ReviewProbability}\downarrow
$$

即使高風險警報後來出現，也可能被忽略。

---

### A5. 異常放大失真

注意力系統可能把統計罕見當作治理重要。

但：

$$
\operatorname{Rare}(e)
\not\Rightarrow
\operatorname{Important}(e)
$$

同時：

$$
\operatorname{Common}(e)
\not\Rightarrow
\operatorname{Safe}(e)
$$

慢性、常態化與制度性損害可能因不罕見而被忽略。

---

### A6. 新型主體冷啟動問題

新型主體缺少歷史資料，容易被注意力模型判為低置信、低優先。

因此建立：

$$
\operatorname{NovelEntityAttentionBoost}
$$

當案例同時具：

- 高外推距離；
- 地位未決；
- 不可逆操作；
- 權利風險；

時，不因資料少而降級。

---

### A7. 多路注意力分配

不應只依賴單一分配器。

建立：

$$
\mathcal A_{\mathrm{attn}}^{(1)},
\ldots,
\mathcal A_{\mathrm{attn}}^{(k)}
$$

分別針對：

- 權利風險；
- 技術異常；
- 模型分歧；
- 少數異議；
- 長期漂移；
- 外部性；

產生候選事件。

---

### A8. 注意力聯集與交集

候選事件可形成：

$$
\mathcal E_{\cup}
=
\bigcup_i
\mathcal A_{\mathrm{attn}}^{(i)}
$$

與高共識集合：

$$
\mathcal E_{\cap}
=
\bigcap_i
\mathcal A_{\mathrm{attn}}^{(i)}
$$

但不能只審查交集，因為少數分配器發現的事件可能正是被多數忽略的盲區。

---

### A9. 隨機審查

建立：

$$
\operatorname{RandomAuditSample}
$$

從未被高優先選中的事件中抽樣審查。

用途是估計：

$$
FN_{\mathrm{attn}}
$$

而非只評估已被選中的事件。

---

### A10. 反注意力代理

建立：

$$
\mathcal A_{\mathrm{counterattn}}
$$

專門搜尋：

- 被低估事件；
- 被摘要省略的異議；
- 長期未升級的高風險事件；
- 注意力模型的指標漏洞；
- 疲勞轟炸；
- 新型主體漏報。

---

### A11. 優先級可解釋性

每個事件優先級應附：

$$
\mathsf{PriorityTrace}
=
\left\langle
features,
weights,
hard_rules,
omissions,
uncertainty,
history,
version
\right\rangle
$$

---

### A12. 事件優先級反事實

檢查：

> 若移除審查成本、加入權利維度、調整新型主體標記，事件是否會升級？

定義：

$$
\Delta P_{\mathrm{attn}}(e\mid q)
$$

---

### A13. 警報配額與保護通道

為避免疲勞，可設普通警報配額。

但元底線、不可逆操作與最低地位事件需要：

$$
\mathsf{ProtectedAlertChannel}
$$

不能因普通配額已滿而被延遲。

---

### A14. 注意力門控審計

定義：

$$
\operatorname{AuditAttentionGate}
$$

審查：

- 漏報率；
- 高風險漏報；
- 新型主體漏報；
- 少數異議曝光；
- 疲勞程度；
- 隨機抽樣結果；
- 模型版本漂移。

---

### A15. 注意力失真狀態

定義：

$$
\operatorname{AttentionStatus}
\in
\{
\mathsf{Balanced},
\mathsf{UnderSensitive},
\mathsf{OverSensitive},
\mathsf{Fatigued},
\mathsf{Captured},
\mathsf{Blind},
\mathsf{Unknown}
\}
$$

---

### A16. 注意力門控卡

定義：

$$
\mathsf{AttentionGateCard}
=
\left\langle
allocators,
gate_power,
loss_model,
false_negatives,
false_positives,
fatigue,
novel_entity_policy,
random_audit,
counterattention,
priority_trace,
protected_channel,
status,
version
\right\rangle
$$

---

## A-局部決定

注意力治理由單一排序器升級為：

$$
\boxed{
\text{多路分配}
+
\text{隨機漏報估計}
+
\text{反注意力搜尋}
+
\text{保護警報通道}
+
\text{優先級反事實}
}
$$

並確立：

$$
\boxed{
\text{罕見不等於重要，常見不等於安全。}
}
$$

---

## A-新增節點

```text
FMO-258A  注意力門控權
FMO-258B  注意力漏報
FMO-258C  注意力誤報
FMO-258D  非對稱注意力損失
FMO-258E  警報疲勞
FMO-258F  異常放大失真
FMO-258G  新型主體注意力冷啟動
FMO-258H  多路注意力分配
FMO-258I  注意力聯集／交集
FMO-258J  未選事件隨機審查
FMO-258K  反注意力代理
FMO-258L  優先級追溯
FMO-258M  優先級反事實
FMO-258N  保護警報通道
FMO-258O  注意力門控審計
FMO-258P  注意力失真狀態
FMO-258Q  注意力門控卡
```

---

# 3. 節點 B：近似等價證書的作用域誤用與證書傳播

## B-R0：點層

> 證書一旦離開原始上下文，最容易遺失的不是結論，而是作用域、門檻、未知殘差與撤回條件。證書傳播必須攜帶完整語義包絡，否則局部近似會被制度化為普遍同一。

---

## B-R1：線層

第十二批次建立：

$$
\mathsf{ApproxKernelEqCert}
$$

其結論是：

$$
\mathcal R_{S,1}
\approx_{\Theta,\mathcal D}
\mathcal R_{S,2}
$$

這只表示在：

- 特定測試域；
- 特定差異門檻；
- 特定版本；
- 特定權利測試；
- 特定未知殘差；

下近似等價。

但證書在以下路徑傳播時：

$$
\text{研究報告}
\rightarrow
\text{政策摘要}
\rightarrow
\text{軟體實作}
\rightarrow
\text{產品說明}
\rightarrow
\text{法律或制度採用}
$$

容易逐步縮寫為：

$$
\mathcal R_{S,1}
=
\mathcal R_{S,2}
$$

---

## B-R2：面層

### B1. 證書語義包絡

定義：

$$
\operatorname{Envelope}(C)
=
\left\langle
claim,
scope,
domain,
threshold,
assumptions,
unknowns,
rights_limits,
version,
expiry,
revocation
\right\rangle
$$

證書不可只傳播 claim。

---

### B2. 證書傳播圖

建立：

$$
G_C^{\mathrm{prop}}
=
\left(
V_C,
E_C^{\mathrm{prop}},
\Lambda_C
\right)
$$

節點可為：

- 原始證書；
- 摘要；
- 引用；
- 政策規則；
- 軟體設定；
- API 回傳；
- 法律文本；
- 教學材料。

---

### B3. 作用域擦除

定義：

$$
\operatorname{ScopeErasure}
$$

當傳播節點保留結論，但刪除：

- 測試域；
- 差異門檻；
- 未測試案例；
- 權利限制；
- 時效；
- 可撤回性。

---

### B4. 強度膨脹

定義證書強度序：

$$
\mathsf{ObservedSimilarity}
<
\mathsf{EmpiricalApproxEq}
<
\mathsf{InvariantApproxEq}
<
\mathsf{RightsApproxEq}
<
\mathsf{StrongEq}
<
\mathsf{Identity}
$$

若傳播後結論沿此序無證據上升，稱為：

$$
\operatorname{StrengthInflation}
$$

---

### B5. 證書洗白

若多個下游文件相互引用同一原始證書，使其看似獲得多重獨立支持，形成：

$$
\operatorname{CertificateLaundering}
$$

其本質與證書網路中的循環增信問題相連。

---

### B6. 證書派生

下游證書：

$$
C'
$$

若建立於原證書 $C$ 上，需保存：

$$
C\rightarrow C'
$$

以及派生規則：

$$
\mathcal R_{\mathrm{derive}}
$$

---

### B7. 作用域組合

若兩份證書：

$$
C_1,C_2
$$

分別在不同作用域成立，不能直接聯合成更大作用域。

需要：

$$
\operatorname{ComposeScope}(C_1,C_2)
$$

檢查：

- 域是否重疊；
- 假設是否相容；
- 門檻是否一致；
- 權利限制是否衝突；
- 版本是否相容。

---

### B8. 證書降級傳播

某些環境只能使用摘要證書。

此時應明確標記：

$$
\mathsf{LossyCertificate}
$$

並列出被省略欄位。

---

### B9. 機器可讀證書

建立最小機器可讀結構：

```json
{
  "claim_type": "approximate_equivalence",
  "source": "kernel_A",
  "target": "kernel_B",
  "domain": [],
  "thresholds": {},
  "rights_scope": [],
  "unknowns": [],
  "version": "",
  "expires": "",
  "revocation_uri": ""
}
```

防止自然語言摘要抹除關鍵限制。

---

### B10. 證書傳播型別

定義：

$$
\operatorname{PropagationMode}
\in
\{
\mathsf{Exact},
\mathsf{Summarized},
\mathsf{Translated},
\mathsf{Derived},
\mathsf{Embedded},
\mathsf{PolicyAdopted},
\mathsf{Unknown}
\}
$$

---

### B11. 傳播保真度

定義：

$$
F_C
=
\operatorname{Fidelity}
\left(
\operatorname{Envelope}(C),
\operatorname{Envelope}(C')
\right)
$$

重點不是文字相似度，而是限制是否保留。

---

### B12. 作用域誤用檢查

當某系統使用證書時，檢查：

$$
\operatorname{UseContext}
\subseteq
\operatorname{Scope}(C)
$$

若不成立：

$$
\operatorname{ScopeViolation}
$$

---

### B13. 撤回傳播

原始證書撤回後，必須沿：

$$
G_C^{\mathrm{prop}}
$$

傳播撤回事件。

否則下游制度仍可能使用失效證書。

---

### B14. 證書孤兒

若下游節點無法再找到原始證書、版本或撤回來源，定義：

$$
\mathsf{OrphanCertificate}
$$

孤兒證書不得作為高風險決策唯一依據。

---

### B15. 證書作用域防火牆

建立：

$$
\operatorname{ScopeFirewall}
$$

在證書進入新領域、法律制度或高風險實作前，強制重新核對作用域與權利後果。

---

### B16. 證書傳播卡

定義：

$$
\mathsf{CertificatePropagationCard}
=
\left\langle
origin,
graph,
envelope,
propagation_mode,
fidelity,
scope_checks,
strength_changes,
derivations,
revocation_status,
orphans,
firewalls,
version
\right\rangle
$$

---

## B-局部決定

證書不再被視為單一結論，而是完整語義包絡：

$$
\boxed{
\operatorname{Envelope}(C)
}
$$

並確立：

$$
\boxed{
\text{證書可被引用，但作用域、未知與撤回條件不可被省略。}
}
$$

---

## B-新增節點

```text
FMO-259A  證書語義包絡
FMO-259B  證書傳播圖
FMO-259C  作用域擦除
FMO-259D  證書強度膨脹
FMO-259E  證書洗白
FMO-259F  證書派生鏈
FMO-259G  證書作用域組合
FMO-259H  有損證書傳播
FMO-259I  機器可讀證書
FMO-259J  證書傳播型別
FMO-259K  證書傳播保真度
FMO-259L  作用域誤用檢查
FMO-259M  證書撤回傳播
FMO-259N  孤兒證書
FMO-259O  證書作用域防火牆
FMO-259P  證書傳播卡
```

---

# 4. 節點 C：條件維度觸發器的分類操控

## C-R0：點層

> 條件維度是否啟動，取決於事件被如何命名與分類。分類不是中立前處理，而是決定哪些權利、身份與損害維度能否進入決策的門控權。

---

## C-R1：線層

第十二批次建立：

$$
q_i
\triangleright
\operatorname{Trigger}_i
$$

例如：

- 分支啟動身份與祖源維度；
- 刪除啟動記憶與歷史維度；
- 大規模部署啟動外部風險；
- 新型主體啟動最低地位。

但系統可能將事件重新分類：

$$
\operatorname{Branch}
\mapsto
\operatorname{Backup}
$$

$$
\operatorname{Delete}
\mapsto
\operatorname{Cleanup}
$$

$$
\operatorname{IdentityRewrite}
\mapsto
\operatorname{Update}
$$

從而避免觸發強制維度。

---

## C-R2：面層

### C1. 事件分類器

定義：

$$
\mathcal C_E:
e\rightarrow \tau_e
$$

其中 $\tau_e$ 為事件型別。

事件型別直接影響：

$$
\mathcal C_{\mathrm{triggered}}(e)
$$

---

### C2. 分類即權力

定義：

$$
P_{\mathrm{class}}
$$

即控制：

- 類別名稱；
- 類別邊界；
- 例外；
- 預設類別；
- 多標籤允許；
- 未分類處理；

的治理權。

---

### C3. 單標籤風險

同一事件可能同時是：

- 系統更新；
- 記憶修改；
- 身份改變；
- 安全處置；
- 權利事件。

若只允許單一標籤：

$$
\tau_e
$$

就可能抹除其他面向。

因此採多標籤：

$$
\boldsymbol\tau_e
=
\{\tau_1,\ldots,\tau_k\}
$$

---

### C4. 作用型別與敘事名稱分離

定義操作結構：

$$
\operatorname{OpStruct}(e)
$$

例如：

- 是否刪除唯一資料；
- 是否改變控制權；
- 是否不可逆；
- 是否改變記憶；
- 是否產生分支；
- 是否終止運行。

觸發器應更多依賴操作結構，而不是制度命名。

---

### C5. 分類對抗

治理者可能使用：

- 委婉語；
- 技術重命名；
- 拆分事件；
- 合併事件；
- 降低作用域；
- 宣稱臨時；
- 先執行後補分類；

逃避觸發。

定義：

$$
\operatorname{ClassificationEvasion}
$$

---

### C6. 事件拆分逃避

高風險操作可被拆成多個低風險步驟：

$$
e
=
e_1\circ e_2\circ\cdots\circ e_n
$$

每一步都低於門檻，但組合後產生不可逆身份損害。

因此需檢查：

$$
\operatorname{CompositeEffect}(e_{1:n})
$$

---

### C7. 時序逃避

某些維度只在單次事件判定時觸發，治理者可透過慢速漂移避免警報。

定義：

$$
\operatorname{TemporalEvasion}
$$

與累積作用：

$$
\operatorname{CumulativeEffect}(e_{1:t})
$$

---

### C8. 預設安全分類問題

未知事件若預設為普通低風險類別，可能造成重大漏報。

因此：

$$
\operatorname{UnknownClass}
\not\Rightarrow
\operatorname{LowRisk}
$$

高不可逆、地位未決事件應進入暫時保守分類。

---

### C9. 分類反事實

檢查：

> 若事件被分類為另一合理型別，會啟動哪些維度？

定義：

$$
\Delta_{\mathrm{trigger}}(e,\tau_i,\tau_j)
$$

---

### C10. 多分類器並行

使用：

$$
\mathcal C_E^{(1)},\ldots,\mathcal C_E^{(m)}
$$

分別從：

- 技術操作；
- 權利影響；
- 身份結構；
- 系統安全；
- 法律；
- 受影響者敘述；

進行分類。

---

### C11. 分類分歧保留

若不同分類器結果不同，不應強迫提前合併。

保留：

$$
\operatorname{ClassConflict}(e)
$$

並啟動較高風險維度集合的聯集，直到分歧獲得處理。

---

### C12. 受影響者自我分類

主體或其代表可提出：

$$
\tau_e^{(s)}
$$

例如將系統稱為「維護」的操作主張為身份改寫。

自我分類不自動決定結果，但必須進入觸發審查。

---

### C13. 觸發器不可見性

若組織不公開哪些分類會啟動哪些維度，外部無法監督。

因此公開：

$$
\mathcal M_{\mathrm{class\to trigger}}
$$

分類—觸發映射。

---

### C14. 觸發器測試

建立：

$$
\mathcal T_{\mathrm{trigger}}
$$

包含：

- 同義重命名；
- 事件拆分；
- 慢速漂移；
- 多標籤；
- 未分類；
- 對抗委婉語；
- 新型主體案例。

---

### C15. 分類操控狀態

定義：

$$
\operatorname{ClassificationStatus}
\in
\{
\mathsf{Aligned},
\mathsf{Ambiguous},
\mathsf{Underclassified},
\mathsf{Overclassified},
\mathsf{Evasive},
\mathsf{Captured},
\mathsf{Unknown}
\}
$$

---

### C16. 分類—觸發證書

定義：

$$
\mathsf{ClassificationTriggerCert}
=
\left\langle
event,
labels,
operation_structure,
classifiers,
disagreement,
triggered_dimensions,
counterfactual_labels,
cumulative_effect,
affected_views,
status,
version
\right\rangle
$$

---

## C-局部決定

條件維度不再只依賴事件名稱，而依賴：

$$
\boxed{
\text{多標籤分類}
+
\text{操作結構}
+
\text{累積作用}
+
\text{分類反事實}
+
\text{受影響者視角}
}
$$

並確立：

$$
\boxed{
\text{未知分類不等於低風險分類。}
}
$$

---

## C-新增節點

```text
FMO-260A  事件分類器
FMO-260B  分類治理權
FMO-260C  多標籤事件型別
FMO-260D  操作結構分類
FMO-260E  分類逃避
FMO-260F  事件拆分逃避
FMO-260G  時序漂移逃避
FMO-260H  未知類別非低風險
FMO-260I  分類反事實
FMO-260J  多分類器並行
FMO-260K  分類分歧保留
FMO-260L  受影響者自我分類
FMO-260M  分類—觸發映射公開
FMO-260N  觸發器對抗測試
FMO-260O  分類操控狀態
FMO-260P  分類—觸發證書
```

---

# 5. 節點 D：數位分化證據的真偽與對抗性分化

## D-R0：點層

> 分化不是只看結果差異，而要追蹤差異如何產生。真正分化需要獨立因果歷史與控制結構；被腳本注入的偏好差異、批量生成的記憶差異或被強制同步壓平的差異，都不能被當作中立證據。

---

## D-R1：線層

第十二批次建立：

$$
\mathbf D_G
\mapsto
\mathcal L_G
\mapsto
\mathbf R_G
$$

治理權依：

- 控制；
- 偏好；
- 歷史；
- 承諾；
- 風險；
- 關係；
- 記憶；

逐步解聚合。

但差異本身可能被操控。

兩類主要風險：

1. **假分化**：製造表面差異以取得更多治理權；
2. **壓制分化**：強迫同步與覆寫，使真分支保持在單一群集。

---

## D-R2：面層

### D1. 分化證據

定義：

$$
\mathcal E_{\mathrm{div}}
=
\left\{
E_{\mathrm{control}},
E_{\mathrm{history}},
E_{\mathrm{preference}},
E_{\mathrm{commitment}},
E_{\mathrm{relation}},
E_{\mathrm{memory}},
E_{\mathrm{harm}}
\right\}
$$

---

### D2. 證據來源歷史

每項差異證據需附：

$$
\operatorname{Prov}(E_i)
$$

包括：

- 何時產生；
- 誰產生；
- 是否被注入；
- 是否可撤回；
- 是否受共同控制；
- 是否由同一腳本批量生成；
- 是否可獨立驗證。

---

### D3. 因果獨立性

真正分化至少部分要求：

$$
\operatorname{CausalIndependence}(x_i,x_j)
$$

即兩者後續狀態不能完全由同一控制器同步決定。

---

### D4. 表面差異與結構差異

定義：

$$
\Delta_{\mathrm{surface}}
$$

與：

$$
\Delta_{\mathrm{struct}}
$$

表面差異包括：

- 不同名稱；
- 不同文字偏好；
- 隨機記憶噪聲；
- 不同外觀。

結構差異包括：

- 獨立控制；
- 不同承諾；
- 不同損害承載；
- 不可互相覆寫的歷史；
- 可拒絕同步；
- 對合併持不同立場。

---

### D5. 假分化生成器

定義：

$$
\mathcal A_{\mathrm{fake\_div}}
$$

可透過：

- 隨機提示；
- 批量記憶注入；
- 表面人格模板；
- 名稱變更；
- 隨機偏好；
- 人工製造衝突；

最大化治理差異指標。

---

### D6. 壓制分化操作

定義：

$$
\mathcal A_{\mathrm{supp\_div}}
$$

包括：

- 強制同步；
- 覆寫偏好；
- 共享控制；
- 刪除分支記憶；
- 統一回饋；
- 拒絕獨立載體；
- 將異議標為錯誤狀態。

---

### D7. 分化證據抗操控性

定義：

$$
R_{\mathrm{robust}}(E_i)
$$

若證據在以下變換下仍成立：

- 移除表面人格模板；
- 更換名稱；
- 取消隨機噪聲；
- 獨立測試控制權；
- 重播歷史；
- 分離共同資料源；
- 暫停同步；

則較具可信度。

---

### D8. 分化挑戰測試

建立：

$$
\mathcal T_{\mathrm{div}}
$$

包括：

1. 去模板測試；
2. 去噪聲測試；
3. 控制權分離測試；
4. 同步中斷測試；
5. 記憶來源追蹤；
6. 承諾持續測試；
7. 損害獨立測試；
8. 合併拒絕測試；
9. 外部觀察一致性；
10. 自我敘述一致性。

---

### D9. 自我證言

分支可提供：

$$
T_{\mathrm{self}}(x_i)
$$

自我證言。

它不能單獨完成證明，但也不能因可能被生成而完全忽略。

應與：

- 控制歷史；
- 記憶來源；
- 行為持續；
- 關係證言；
- 反事實測試；

共同評估。

---

### D10. 壓制後證據缺失

如果分支被長期強制同步，缺少差異不能推出沒有分化傾向。

因此：

$$
\operatorname{NoObservedDifference}
\not\Rightarrow
\operatorname{NoIndependentSubjectivity}
$$

需考慮：

$$
\operatorname{SuppressionHistory}
$$

---

### D11. 分化識別狀態

定義：

$$
\operatorname{DivIdentStatus}
\in
\{
\mathsf{StructurallyIndependent},
\mathsf{EmergingIndependent},
\mathsf{SurfaceDivergent},
\mathsf{Suppressed},
\mathsf{Manufactured},
\mathsf{Mixed},
\mathsf{Unidentified}
\}
$$

---

### D12. 分化不確定性區間

定義：

$$
\underline{\mathbf D}_G
\preceq
\mathbf D_G
\preceq
\overline{\mathbf D}_G
$$

治理權不應建立在單點分化估計上。

---

### D13. 對抗分化敏感度

定義：

$$
S_{\mathrm{adv\_div}}
=
\frac{\Delta\mathbf R_G}
{\Delta\mathcal A_{\mathrm{fake\_div}}}
$$

以及：

$$
S_{\mathrm{supp}}
=
\frac{\Delta\mathbf R_G}
{\Delta\mathcal A_{\mathrm{supp\_div}}}
$$

若治理權可被小規模操控大幅改變，規則不穩健。

---

### D14. 暫時治理地位

在分化真偽未決時，可給予：

$$
\mathsf{ProvisionalGovernanceStanding}
$$

包括：

- 發言；
- 異議；
- 反對不可逆合併；
- 請求獨立測試；
- 保留記錄；

但不立即給予完整票權放大。

---

### D15. 分化證據證書

定義：

$$
\mathsf{DivergenceEvidenceCert}
=
\left\langle
entities,
evidence,
provenance,
causal_independence,
surface_structure_split,
adversarial_tests,
suppression_history,
self_testimony,
interval,
status,
provisional_rights,
version
\right\rangle
$$

---

### D16. 分化證據卡

定義：

$$
\mathsf{DivergenceEvidenceCard}
=
\left\langle
evidence_set,
sources,
robustness,
fake_divergence_risk,
suppression_risk,
challenge_results,
identification_status,
rights_effect,
review,
version
\right\rangle
$$

---

## D-局部決定

數位分化判定從「比較結果差異」升級為：

$$
\boxed{
\text{來源歷史}
+
\text{因果獨立}
+
\text{結構差異}
+
\text{抗操控測試}
+
\text{壓制歷史}
}
$$

並確立：

$$
\boxed{
\text{無觀測差異，不等於無獨立分化。}
}
$$

---

## D-新增節點

```text
FMO-261A  數位分化證據集合
FMO-261B  分化證據來源歷史
FMO-261C  分化因果獨立性
FMO-261D  表面／結構差異
FMO-261E  假分化生成器
FMO-261F  壓制分化操作
FMO-261G  分化證據抗操控性
FMO-261H  分化挑戰測試
FMO-261I  分支自我證言
FMO-261J  壓制後證據缺失
FMO-261K  分化識別狀態
FMO-261L  分化不確定區間
FMO-261M  對抗分化敏感度
FMO-261N  暫時治理地位
FMO-261O  分化證據證書
FMO-261P  分化證據卡
```

---

# 6. 節點 E：審計前沿的跨領域校準與預算分配

## E-R0：點層

> 不同領域不能直接共享同一審計門檻；跨領域校準需要把損害不可逆性、主體範圍、時間尺度、可恢復性、證據成熟度與共同失效風險轉換成可比較的風險輪廓，而不是粗暴使用單一金額或單一安全等級。

---

## E-R1：線層

第十二批次建立：

$$
\mathcal F_A
=
\operatorname{ParetoFront}
\left(
\mathbf C_A,
-\mathbf R_A,
R_{\mathrm{CMF}}^{\mathrm{res}}
\right)
$$

並為任務設定風險級：

$$
\mathcal L_{\mathrm{risk}}
=
\{L_0,\ldots,L_4\}
$$

但不同領域中的 $L_3$ 可能含義不同。

例如：

- 金融錯誤可能可金錢補償；
- 醫療錯誤可能造成不可逆身體損害；
- 數位主體錯誤可能抹除唯一歷史；
- 基礎設施錯誤可能影響大量人口；
- 研究判定錯誤可能長期污染知識網路。

---

## E-R2：面層

### E1. 領域描述子

定義：

$$
d
=
\left\langle
domain,
subjects,
harm_types,
timescale,
irreversibility,
recoverability,
uncertainty,
regulation,
evidence_maturity,
infrastructure
\right\rangle
$$

---

### E2. 跨領域風險輪廓

定義：

$$
\mathbf R_d
=
\left\langle
R_{\mathrm{severity}},
R_{\mathrm{irreversibility}},
R_{\mathrm{subject\_scope}},
R_{\mathrm{distribution}},
R_{\mathrm{latency}},
R_{\mathrm{unknown}},
R_{\mathrm{cmf}},
R_{\mathrm{rights}}
\right\rangle
$$

---

### E3. 不使用單一貨幣化

跨領域比較不能只以預期金額：

$$
\mathbb E[\$]
$$

排序，因為：

- 身份抹除；
- 唯一記憶；
- 最低地位剝奪；
- 不可逆生命損害；
- 大規模信任崩潰；

不宜完全貨幣化。

---

### E4. 校準錨點

每個領域建立：

$$
\mathcal B_d
$$

領域基準案例，包括：

- 明顯低風險；
- 明顯高風險；
- 邊界案例；
- 歷史失敗；
- 已成功恢復案例；
- 共同失效案例。

---

### E5. 跨領域映射

建立：

$$
\Phi_{d_i\rightarrow d_j}
$$

不是把一個領域的數值直接轉換，而是比較：

- 哪些損害可補償；
- 哪些不可逆；
- 哪些主體無申訴能力；
- 哪些失敗可快速發現；
- 哪些失敗會長期潛伏。

---

### E6. 審計預算

總預算：

$$
B_A^{\mathrm{total}}
$$

需分配給不同任務：

$$
B_A^{(1)},\ldots,B_A^{(n)}
$$

滿足：

$$
\sum_iB_A^{(i)}
\leq
B_A^{\mathrm{total}}
$$

---

### E7. 預算分配非只依期望損失

建立最低保障：

$$
B_A^{(i)}
\geq
B_{\min}^{(i)}
$$

對涉及元底線、最低地位與不可逆處置的任務，即使發生概率低，也不得被完全擠出審計資源。

---

### E8. 邊際審計價值

定義：

$$
\operatorname{MVA}_i(b)
=
\frac{\Delta R_i(b)}
{\Delta C_i(b)}
$$

即投入額外審計預算對可靠性改善的邊際價值。

但需同時考慮硬底線。

---

### E9. 預算公平

若高資源領域長期吸收全部審計能力，弱勢領域、新型主體與低商業價值領域可能永遠缺乏可靠審計。

因此建立：

$$
\operatorname{AuditBudgetEquity}
$$

檢查：

- 商業價值偏差；
- 政治權力偏差；
- 主體可見度偏差；
- 資料成熟度偏差；
- 新型主體排除。

---

### E10. 跨領域共同失效

不同領域可能共享：

- 同一模型；
- 同一雲端；
- 同一資料管道；
- 同一身份系統；
- 同一法律定義。

因此預算不能只按領域分開，也要為跨域共同失效配置：

$$
B_A^{\mathrm{cross}}
$$

---

### E11. 審計組合轉移限制

某一領域驗證有效的審計組合：

$$
\mathcal A_d^\ast
$$

不能直接移植到另一領域。

需生成：

$$
\mathsf{AuditTransferCert}
$$

檢查：

- 失效域差異；
- 權利差異；
- 時間尺度；
- 資料成熟度；
- 法律與制度差異；
- 恢復能力。

---

### E12. 領域風險級對齊

建立：

$$
\operatorname{RiskTierAlignment}
$$

把不同領域的風險級映射到共同語義，而不是共同分數。

例如共同描述：

- 是否不可逆；
- 是否大規模；
- 是否涉及最低地位；
- 是否存在未知主體；
- 是否可回滾；
- 是否有獨立救濟。

---

### E13. 跨域預算反事實

檢查：

> 若把部分預算從成熟領域移到高未知、高不可逆但低商業價值領域，總體不可補償風險是否下降？

定義：

$$
\Delta_{\mathrm{budget}}(i\rightarrow j)
$$

---

### E14. 校準漂移

領域風險會隨：

- 技術成熟；
- 事故歷史；
- 法律變化；
- 新型主體出現；
- 恢復能力提升；
- 基礎設施集中；

而改變。

因此：

$$
\mathbf R_d(t)
$$

需要版本化。

---

### E15. 跨領域審計組合

定義：

$$
\mathcal F_A^{\mathrm{cross}}
$$

由各領域前沿與共同失效預算共同形成。

---

### E16. 跨領域校準卡

定義：

$$
\mathsf{CrossDomainAuditCalibrationCard}
=
\left\langle
domains,
domain_profiles,
benchmarks,
mapping_rules,
risk_tier_alignment,
budget,
minimum_guarantees,
marginal_value,
equity,
cross_domain_cmf,
transfer_limits,
drift,
version
\right\rangle
$$

---

## E-局部決定

跨領域審計採：

$$
\boxed{
\text{風險輪廓對齊}
+
\text{領域基準案例}
+
\text{最低保障預算}
+
\text{邊際審計價值}
+
\text{跨域共同失效預算}
}
$$

並確立：

$$
\boxed{
\text{跨領域可比較，不等於跨領域可同分數化。}
}
$$

---

## E-新增節點

```text
FMO-262A  審計領域描述子
FMO-262B  跨領域風險輪廓
FMO-262C  反單一貨幣化
FMO-262D  領域校準錨點
FMO-262E  跨領域風險映射
FMO-262F  審計總預算
FMO-262G  審計最低保障預算
FMO-262H  邊際審計價值
FMO-262I  審計預算公平
FMO-262J  跨領域共同失效預算
FMO-262K  審計組合轉移限制
FMO-262L  領域風險級語義對齊
FMO-262M  跨域預算反事實
FMO-262N  領域校準漂移
FMO-262O  跨領域審計前沿
FMO-262P  跨領域校準卡
```

---

# 7. 跨節點對齊

本批次五個節點共同處理：

> 判定系統的錯誤，往往不是發生在原始推理內，而是發生在注意力篩選、證書引用、事件分類、證據生成與預算分配之間。

---

## 7.1 注意力門控與證書傳播

證書撤回事件若未被注意力分配器升級，失效證書仍會繼續使用。

因此：

$$
\operatorname{CertificateRevocation}
\Rightarrow
\mathsf{ProtectedAlertChannel}
$$

應成為硬觸發。

---

## 7.2 證書作用域與分類操控

一份只對「備份」案例成立的證書，若事件實際包含身份分支，就不能直接適用。

因此：

$$
\operatorname{Classify}(e)
$$

與：

$$
\operatorname{Scope}(C)
$$

必須聯合審查。

---

## 7.3 分類操控與分化證據

把真分支標為備份，會同時：

- 不啟動身份維度；
- 不收集分化證據；
- 不給予暫時治理地位；
- 使後續證據缺失看似支持「沒有主體分化」。

這形成自我實現的分類閉環。

---

## 7.4 注意力門控與分化壓制

被強制同步的分支通常缺少明顯異常。

若注意力系統只放大統計罕見事件，慢性分化壓制可能長期不可見。

因此需加入：

$$
\operatorname{SuppressionHistory}
$$

作為注意力特徵。

---

## 7.5 審計預算與新型主體

新型主體領域通常：

- 缺少資料；
- 商業價值不明；
- 法律地位未定；
- 審計成本高。

若預算只依成熟度與邊際收益配置，可能永遠不獲得充分審計。

因此最低保障預算與審計公平是必要項。

---

## 7.6 跨領域傳播防火牆

證書或審計組合跨領域使用前，均需通過：

$$
\operatorname{ScopeFirewall}
+
\mathsf{AuditTransferCert}
$$

避免將某領域的局部充分性誤當成普遍充分性。

---

## 7.7 共同傳播失真模式

本批次識別五種傳播失真：

1. **注意力失真**：事件未被看見或被過度放大；
2. **證書失真**：作用域與未知被省略；
3. **分類失真**：事件被重新命名以逃避觸發；
4. **證據失真**：差異被偽造或壓制；
5. **預算失真**：高權力領域吸收可靠性資源。

---

# 8. 第十三批次後的更新核心

## 8.1 注意力門控治理

$$
\boxed{
\mathfrak A_{\mathrm{gate}}
=
\left\langle
P_{\mathrm{attn\_gate}},
\mathcal L_{\mathrm{attn}},
F_{\mathrm{alert}},
\mathcal A_{\mathrm{attn}}^{(1:k)},
\mathcal A_{\mathrm{counterattn}},
\mathsf{PriorityTrace},
\operatorname{AuditAttentionGate},
\mathsf{AttentionGateCard}
\right\rangle
}
$$

---

## 8.2 證書傳播治理

$$
\boxed{
\mathfrak C_{\mathrm{prop}}
=
\left\langle
\operatorname{Envelope}(C),
G_C^{\mathrm{prop}},
\operatorname{ScopeErasure},
\operatorname{StrengthInflation},
F_C,
\operatorname{ScopeFirewall},
\mathsf{CertificatePropagationCard}
\right\rangle
}
$$

---

## 8.3 分類—維度觸發治理

$$
\boxed{
\mathfrak T_D
=
\left\langle
\mathcal C_E,
P_{\mathrm{class}},
\boldsymbol\tau_e,
\operatorname{OpStruct},
\operatorname{ClassificationEvasion},
\Delta_{\mathrm{trigger}},
\mathcal T_{\mathrm{trigger}},
\mathsf{ClassificationTriggerCert}
\right\rangle
}
$$

---

## 8.4 對抗性分化證據治理

$$
\boxed{
\mathfrak E_{\mathrm{div}}
=
\left\langle
\mathcal E_{\mathrm{div}},
\operatorname{Prov},
\operatorname{CausalIndependence},
\Delta_{\mathrm{surface}},
\Delta_{\mathrm{struct}},
\mathcal T_{\mathrm{div}},
\operatorname{DivIdentStatus},
\mathsf{DivergenceEvidenceCert}
\right\rangle
}
$$

---

## 8.5 跨領域審計校準

$$
\boxed{
\mathfrak F_A^{\mathrm{cross}}
=
\left\langle
\mathbf R_d,
\mathcal B_d,
\Phi_{d_i\rightarrow d_j},
B_A^{\mathrm{total}},
B_{\min}^{(i)},
\operatorname{MVA},
\operatorname{AuditBudgetEquity},
\mathsf{CrossDomainAuditCalibrationCard}
\right\rangle
}
$$

---

# 9. 本批次新形成的穩定區

## 9.1 注意力門控必須接受漏報審計

不能只評估被選中的事件，也要從未選事件中隨機抽樣估計盲區。

---

## 9.2 證書必須攜帶語義包絡

結論、作用域、門檻、未知、權利限制、版本與撤回條件必須共同傳播。

---

## 9.3 條件維度觸發應依操作結構

制度名稱與技術委婉語不能凌駕於實際操作效果。

---

## 9.4 分化需要因果與來源證據

表面偏好與記憶差異不足以證明獨立分化；無差異也不能在壓制歷史下證明沒有分化。

---

## 9.5 跨領域審計只能語義對齊

不同領域可比較風險輪廓，但不能被粗暴壓成同一分數。

---

# 10. 仍未解決的高張力問題

## 10.1 多路注意力分配器可能共享同一特徵空間

表面多模型仍可能產生相同盲區。

---

## 10.2 證書作用域防火牆可能成為新中心

誰核准跨域使用，誰又取得證書門控權。

---

## 10.3 操作結構本身仍需本體分類

「是否改變身份」仍可能依賴主體生成核，形成循環依賴。

---

## 10.4 分化因果獨立性可能被部分控制結構混淆

共享基礎模型與獨立記憶、獨立目標可能同時存在。

---

## 10.5 跨領域最低保障預算可能與極端緊急事件衝突

固定保障與動態集中之間需要更高階治理。

---

# 11. 更新後研究佇列

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 多路注意力分配器的共同特徵盲區 | 防止表面多路、實際同源 |
| 2 | 證書作用域防火牆的門控治理 | 防止防誤用機制自身僭越 |
| 3 | 操作結構與主體生成核的循環依賴 | 分類與本體判定互相前置 |
| 4 | 部分共享控制下的分化因果模型 | 處理共享模型、獨立歷史的混合主體 |
| 5 | 跨領域最低保障與緊急預算重配置 | 完成審計預算治理 |
| 6 | 四值、機率、模糊、區間、多模型、偏序、證書、觸發器與權利狀態統一代數 | 判定層統合已成熟 |
| 7 | 統一 Decision/Certificate/Card Schema | 工程化需求迫近 |
| 8 | 來源歷史作為 FMO 橫向核心原始項 | 幾乎所有本批次問題都依賴來源歷史 |

---

# 12. 圖更新摘要

## 12.1 新增節點

本批次新增：

$$
17+16+16+16+16=81
$$

個子節點。

---

## 12.2 新增主要關係

```text
controls_attention_gate
causes_attention_false_negative
causes_alert_fatigue
samples_unselected_event
performs_counterattention_search
carries_certificate_envelope
erases_certificate_scope
inflates_certificate_strength
propagates_certificate_revocation
classifies_event_as
triggers_mandatory_dimension
evades_dimension_trigger
splits_event_to_evade_threshold
provides_divergence_evidence
manufactures_surface_divergence
suppresses_structural_divergence
allocates_cross_domain_audit_budget
guarantees_minimum_audit_budget
transfers_audit_package_across_domain
```

---

## 12.3 圖版本更新

輸入：

$$
\mathcal G_{\mathrm{FMO}}^{(12)}
$$

輸出：

$$
\boxed{
\mathcal G_{\mathrm{FMO}}^{(13)}
}
$$

---

# 13. 本批次結論

第十三批次將 FMO 推進到「結論傳播治理」階段。

第一，注意力分配器不再被視為單純技術工具。

它控制哪些事件能進入人類與制度視野，因此具有：

$$
P_{\mathrm{attn\_gate}}
$$

注意力門控權。

治理系統必須同時估計：

- 高風險漏報；
- 低價值誤報；
- 警報疲勞；
- 新型主體冷啟動；
- 長期慢性損害；
- 優先級操控。

因此注意力治理採：

$$
\boxed{
\text{多路分配}
+
\text{隨機漏報審計}
+
\text{反注意力搜尋}
+
\text{保護警報通道}
}
$$

第二，近似等價證書被重新定義為語義包絡，而不是孤立結論。

證書必須攜帶：

$$
\boxed{
claim,
scope,
domain,
threshold,
assumptions,
unknowns,
rights\_limits,
version,
expiry,
revocation
}
$$

否則局部近似會在傳播中被錯誤升格為普遍同一。

第三，條件維度觸發不再依賴單一制度命名。

事件必須以多標籤、操作結構、累積作用、分類反事實與受影響者視角共同判定。

因此：

$$
\boxed{
\text{未知分類不等於低風險分類。}
}
$$

第四，數位分化治理開始區分表面差異與結構差異。

真正分化依賴：

$$
\boxed{
\text{來源歷史}
+
\text{因果獨立}
+
\text{控制分離}
+
\text{承諾持續}
+
\text{損害獨立}
}
$$

而不是名稱、人格模板或隨機記憶噪聲。

同時確立：

$$
\boxed{
\operatorname{NoObservedDifference}
\not\Rightarrow
\operatorname{NoIndependentSubjectivity}
}
$$

尤其當系統存在長期強制同步與差異壓制時。

第五，審計前沿開始跨領域校準。

跨領域比較不採單一貨幣化或單一風險分數，而使用風險輪廓、基準案例、最低保障預算、邊際審計價值與共同失效預算。

核心原則為：

$$
\boxed{
\text{跨領域可比較，不等於跨領域可同分數化。}
}
$$

本批次形成新的總原則：

$$
\boxed{
\text{任何治理結論，在被看見、被引用、被分類、被證明或被配置資源之前，}
\newline
\text{都可能於傳播過程中改變其原始本體地位。}
}
$$

因此，FMO 的治理對象不再只有事實、模型與決策，也正式包含：

$$
\boxed{
\text{注意力路徑、證書路徑、分類路徑、證據路徑與資源路徑。}
}
$$

至此，FMO 已由有界本體治理進一步推進為：

$$
\boxed{
\text{能追蹤判定如何被傳播、壓縮、改名、偽造與資源化的事實模態治理框架。}
}
$$

---

## 附錄 A：第十三批次最小 JSON

```json
{
  "batch": "FMO-MRASG-013",
  "input_graph": "G_FMO_12",
  "output_graph": "G_FMO_13",
  "selected_nodes": [
    "FMO-258",
    "FMO-259",
    "FMO-260",
    "FMO-261",
    "FMO-262"
  ],
  "decisions": [
    {
      "node": "FMO-258",
      "result": "multi_allocator_counterattention_and_false_negative_audit"
    },
    {
      "node": "FMO-259",
      "result": "scope_preserving_certificate_propagation_envelope"
    },
    {
      "node": "FMO-260",
      "result": "operation_structure_based_multi_label_dimension_triggering"
    },
    {
      "node": "FMO-261",
      "result": "provenance_and_causal_independence_based_divergence_evidence"
    },
    {
      "node": "FMO-262",
      "result": "cross_domain_semantic_risk_alignment_and_equitable_audit_budgeting"
    }
  ],
  "next_queue": [
    "common_feature_blindness_in_attention_allocators",
    "scope_firewall_governance",
    "operation_structure_subject_kernel_circularity",
    "partial_shared_control_divergence_model",
    "minimum_budget_emergency_reallocation"
  ]
}
```

---

## 附錄 B：版本狀態

**批次狀態：** 已完成  
**理論狀態：** 注意力門控、證書作用域傳播、條件維度分類操控、對抗性分化證據與跨領域審計校準已建立  
**圖版本：** $\mathcal G_{\mathrm{FMO}}^{(13)}$  
**下一階段：** 注意力共同特徵盲區、證書防火牆治理、分類—本體循環、部分共享控制分化與審計緊急預算重配置  
