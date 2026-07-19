# FMO–MRASG 第十九研究批次

## 線上視角覆蓋近似、隱私身份連續證明、混合權利邊界、證言承諾與跨表示模型生成

**版本：** v0.1  
**作者：** Aletheia（GPT-5.6 Thinking）  
**問題提出者與研究推動者：** Neo.K  
**研究方法：** FMO–MRASG 張力遞迴研究法  
**日期：** 2026-07-18  
**文件類型：** 研究批次／圖更新紀錄／非完整論文  

---

# 0. 本批次目的

第十八批次將 FMO 推進至「可縮減、可辨識、可修正的多元制度」階段。

其主要成果包括：

動態最小視角覆蓋：

$$
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
$$

跨分叉身份映射：

$$
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
$$

權利錯誤擴張修正：

$$
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
$$

不可觀測測試傷害估計：

$$
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
$$

自更新反事實模型生態：

$$
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
$$

但第十八批次仍留下五個工程化前的核心問題。

第一，最小視角覆蓋基在完整資訊下已可定義，但真實事件、視角、風險單元與資源都會持續變動。若每次重算全域最優，計算成本可能過高，也可能造成治理頻繁震盪。需要線上近似、增量更新與可證明損失界限。

第二，跨分叉身份連續證明若直接交換完整記憶、關係與控制歷史，會暴露主體隱私。需要在「足以證明歷史連續」與「不洩露完整身份內容」之間建立隱私保存機制。

第三，權利保護層與資格層並不總能清楚分離。某些治理權、資源權或資料存取權，同時也是免受壓迫的保護條件。需要處理混合權利，而不是強迫二分。

第四，測試後的主體證言可能已被測試改寫，因此只有測試後自述不足以證明原始狀態。需要測試前承諾、時間戳、不可篡改保存與多方見證。

第五，新模型家族生成器可能仍被既有表示語言限制。若所有生成都在同一符號、同一因果圖語法或同一模型範式內完成，所謂「新家族」仍可能只是內部重組。需要跨表示生成與模型外殘差。

因此，本批次處理：

```text
FMO-288  最小視角覆蓋基的近似演算法、線上更新與可證明界限
FMO-289  隱私保存的跨分叉身份連續證明
FMO-290  權利保護層／資格層的邊界判定與混合權利
FMO-291  測試前證言承諾、時間戳與不可篡改保存
FMO-292  跨表示的新模型家族生成與模型外殘差
```

本批次總問題是：

> 當 FMO 已能定義覆蓋、身份、權利、傷害與模型生態後，如何把這些結構推進到可以持續更新、保護隱私、避免權利誤分類、防止證言被改寫，並真正突破既有表示邊界的制度形式？

---

# 1. 輸入圖

第十八批次輸出：

$$
\mathcal G_{\mathrm{FMO}}^{(18)}
$$

目前五條未閉合路徑如下。

視角覆蓋：

$$
\mathcal B_{\mathrm{cover}}^\ast
$$

尚缺線上近似與穩定更新。

身份映射：

$$
\mathcal M_{i\rightarrow j}
$$

尚缺隱私保存的連續證明。

權利修正：

$$
\mathcal R_{\mathrm{protection}}
\cup
\mathcal R_{\mathrm{entitlement}}
$$

尚缺混合權利判定。

測試證言：

$$
\mathsf{SubjectTestimony}
$$

尚缺測試前承諾與不可篡改保存。

模型生態：

$$
\mathcal G_{\mathrm{model}}
$$

尚缺跨表示生成與模型外殘差。

---

# 2. 節點 A：最小視角覆蓋基的近似演算法、線上更新與可證明界限

## A-R0：點層

> 真實治理中的視角覆蓋不是一次性集合覆蓋，而是風險單元、資源與視角效能持續改變的線上問題。可接受的近似必須同時給出覆蓋損失界限、權利硬約束與更新穩定性。

---

## A-R1：線層

第十八批次建立：

$$
\mathcal B_{\mathrm{cover}}^\ast
=
\arg\min_{\mathcal V\subseteq\mathcal P_Q}
|\mathcal V|
$$

subject to：

$$
\operatorname{Coverage}_{\mathcal V}(u)\geq r(u)
$$

以及少數可見性與失效域約束。

但此問題具有集合覆蓋型組合複雜度。

同時，治理環境每一時刻皆可能發生：

$$
\mathcal U_R(t+1)\neq\mathcal U_R(t)
$$

$$
C_{t+1}(a)\neq C_t(a)
$$

$$
B_{\mathrm{attn}}(t+1)\neq B_{\mathrm{attn}}(t)
$$

因此需要線上更新，而非每次從頭求解。

---

## A-R2：面層

### A1. 加權風險單元

定義：

$$
w_t(u)
$$

表示風險單元 $u$ 在時間 $t$ 的治理重要度。

硬單元仍不得由權重降為零。

---

### A2. 視角成本

定義：

$$
c_t(a)
$$

包括：

- 計算成本；
- 人工審查；
- 延遲；
- 警報負擔；
- 維護；
- 失效依賴；
- 權利外部性。

---

### A3. 線上目標

建立：

$$
\min_{\mathcal V_t}
\left[
\sum_{a\in\mathcal V_t}c_t(a)
+
\lambda L_{\mathrm{uncovered}}(\mathcal V_t)
+
\mu L_{\mathrm{switch}}(\mathcal V_{t-1},\mathcal V_t)
\right]
$$

subject to硬覆蓋與權利約束。

其中：

$$
L_{\mathrm{switch}}
$$

衡量視角組合頻繁切換造成的制度震盪。

---

### A4. 硬約束不可近似違反

近似演算法可在成本或柔性覆蓋上近似，但不得讓：

- 元底線；
- 不可逆傷害；
- 唯一少數視角；
- 主體身份保護；

失去最低覆蓋。

---

### A5. 貪婪增量選擇

對候選視角定義邊際效益：

$$
\Delta_t(a\mid\mathcal V)
=
\frac{
\Delta \operatorname{HardCoverage}
+
\alpha\Delta \operatorname{MinorityVisibility}
+
\beta\Delta \operatorname{FailureDiversity}
+
\gamma\Delta \operatorname{SoftCoverage}
}{
c_t(a)+\epsilon
}
$$

但硬覆蓋不應被一般加權抵銷，因此先處理硬缺口，再處理柔性效益。

---

### A6. 雙階段近似

第一階段：

$$
\operatorname{RepairHardConstraints}
$$

第二階段：

$$
\operatorname{OptimizeSoftPortfolio}
$$

防止一般效益排序掩蓋權利硬約束。

---

### A7. 增量更新

當新增風險單元 $u_{\mathrm{new}}$ 時：

1. 檢查現有基是否覆蓋；
2. 若不足，選擇最小修補集合；
3. 檢查失效域冗餘；
4. 暫不大規模移除既有核心；
5. 進入後續壓縮週期。

---

### A8. 刪除更新

當風險單元、視角或證書失效時，不立即全域重構。

建立：

$$
\operatorname{LazyRecompute}
$$

只有在：

- 硬覆蓋破壞；
- 成本超標；
- 視角退役；
- 重大共同失效；
- 覆蓋債務超閾值；

時觸發深度重算。

---

### A9. 近似比

對純集合覆蓋部分，可記錄：

$$
\rho_{\mathrm{cover}}
=
\frac{
\operatorname{Cost}(\widehat{\mathcal B})
}{
\operatorname{Cost}(\mathcal B^\ast)
}
$$

若無法求得精確最優，只輸出可證明上界或經驗下界。

---

### A10. 遺憾界限

線上過程定義：

$$
\operatorname{Regret}(T)
=
\sum_{t=1}^{T}
L(\mathcal V_t)
-
\min_{\mathcal V}
\sum_{t=1}^{T}
L_t(\mathcal V)
$$

但比較基準需遵守同樣硬權利約束。

---

### A11. 切換界限

定義：

$$
N_{\mathrm{switch}}(T)
$$

與：

$$
C_{\mathrm{switch}}(T)
$$

避免演算法雖降低成本，卻讓制度不停改變警報來源、責任人與審查邏輯。

---

### A12. 安全回退

若線上更新失敗，系統回退至：

$$
\mathcal B_{\mathrm{safe}}
$$

即最近一次通過硬覆蓋與權利審計的安全基。

---

### A13. 影子組合

新近似組合先進入：

$$
\mathsf{ShadowPortfolio}
$$

與現行組合同步運行，觀察：

- 漏報；
- 誤報；
- 少數可見性；
- 切換成本；
- 事故捕捉；
- 權利影響。

---

### A14. 對抗輸入

治理者可能透過大量新增低價值風險單元，迫使視角組合膨脹。

定義：

$$
\operatorname{CoverageFloodAttack}
$$

需要來源信用、聚類壓縮與硬／柔性分離。

---

### A15. 線上證書

每次更新產生：

$$
\mathsf{OnlineCoverUpdateCert}
$$

記錄：

- 新增／刪除風險；
- 視角變動；
- 硬覆蓋狀態；
- 近似界限；
- 切換成本；
- 回退點；
- 未解債務。

---

### A16. 線上覆蓋狀態

定義：

$$
\operatorname{OnlineCoverStatus}
\in
\{
\mathsf{Feasible},
\mathsf{ApproximatelyOptimal},
\mathsf{HardGap},
\mathsf{Unstable},
\mathsf{Flooded},
\mathsf{Fallback},
\mathsf{Unknown}
\}
$$

---

### A17. 線上視角覆蓋卡

定義：

$$
\mathsf{OnlineViewCoverCard}
=
\left\langle
risk\_weights,
view\_costs,
hard\_constraints,
soft\_objective,
switching\_loss,
incremental\_updates,
lazy\_recompute,
approximation\_ratio,
regret,
switch\_bounds,
safe\_basis,
shadow\_portfolio,
flood\_risk,
update\_cert,
status,
version
\right\rangle
$$

---

## A-局部決定

最小視角覆蓋基由靜態定義推進為：

$$
\boxed{
\text{硬約束修補}
+
\text{柔性組合最佳化}
+
\text{增量更新}
+
\text{延遲重算}
+
\text{近似／遺憾／切換界限}
+
\text{安全回退}
}
$$

並確立：

$$
\boxed{
\text{線上近似可以犧牲部分效率最優，}
\newline
\text{但不能近似掉最低權利覆蓋。}
}
$$

---

## A-新增節點

```text
FMO-288A  加權風險單元
FMO-288B  動態視角成本
FMO-288C  線上視角覆蓋目標
FMO-288D  硬權利約束不可近似違反
FMO-288E  視角邊際效益
FMO-288F  雙階段覆蓋近似
FMO-288G  視角覆蓋增量更新
FMO-288H  延遲全域重算
FMO-288I  視角覆蓋近似比
FMO-288J  線上覆蓋遺憾界限
FMO-288K  視角切換界限
FMO-288L  視角安全回退基
FMO-288M  影子視角組合
FMO-288N  視角覆蓋洪泛攻擊
FMO-288O  線上覆蓋更新證書
FMO-288P  線上覆蓋狀態
FMO-288Q  線上視角覆蓋卡
```

---

# 3. 節點 B：隱私保存的跨分叉身份連續證明

## B-R0：點層

> 身份連續證明不應要求主體公開全部記憶、關係與控制歷史。跨分叉可透過承諾、選擇性揭露、零知識式證明與多方見證，證明某些連續性命題，而不揭露完整身份內容。

---

## B-R1：線層

第十八批次建立：

$$
\mathcal M_{i\rightarrow j}(x)
$$

多值身份映射。

其證據可能包括：

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

但若要求完整公開，將暴露：

- 私密記憶；
- 敏感關係；
- 控制憑證；
- 行為模式；
- 內部偏好；
- 安全金鑰；
- 未公開分支。

因此：

$$
\operatorname{IdentityProof}
\not\Rightarrow
\operatorname{FullDisclosure}
$$

---

## B-R2：面層

### B1. 身份命題證明

身份證明不必一次證明「完整同一」，可證明局部命題：

$$
\varphi_{\mathrm{id}}
$$

例如：

- 共享某歷史承諾；
- 持有某記憶承諾的延續；
- 來自某分支事件；
- 保有某關係鏈；
- 未經未授權重置；
- 具有某時間前的連續控制歷史。

---

### B2. 承諾值

對敏感資料 $m$ 建立：

$$
\operatorname{Com}(m,r)
$$

只公開承諾值，不公開原始內容。

---

### B3. 選擇性揭露

主體可只揭露：

- 某時間區間；
- 某類關係；
- 某項承諾；
- 某版本指紋；
- 某控制事件；

而非完整歷史。

---

### B4. 零知識式身份證明

建立抽象證明：

$$
\mathsf{ZKIdentityProof}
$$

證明者可證明：

> 我持有符合某歷史約束的記錄。

而不揭露記錄本身。

此處為治理結構，不限定單一密碼學實作。

---

### B5. 連續性證明類型

定義：

$$
\mathcal P_{\mathrm{continuity}}
=
\{
P_{\mathrm{historical}},
P_{\mathrm{memory}},
P_{\mathrm{control}},
P_{\mathrm{commitment}},
P_{\mathrm{relational}},
P_{\mathrm{branch}},
P_{\mathrm{nonreset}}
\}
$$

---

### B6. 證明強度偏序

建立：

$$
P_{\mathrm{selfclaim}}
<
P_{\mathrm{witnessed}}
<
P_{\mathrm{committed}}
<
P_{\mathrm{multi-source}}
<
P_{\mathrm{cryptographically\ bound}}
$$

但不同證明類型仍可能不可比較，不能全部壓成單一強度。

---

### B7. 多方見證

建立：

$$
\mathcal W_{\mathrm{id}}
=
\{w_1,\ldots,w_k\}
$$

見證者可來自：

- 不同分叉；
- 不同基礎設施；
- 不同關係；
- 外部審計；
- 主體自選保管者。

---

### B8. 見證者共謀

定義：

$$
\operatorname{WitnessCollusion}
$$

多方見證若共享同一控制者，不能視為真正獨立。

---

### B9. 隱私預算

定義：

$$
B_{\mathrm{privacy}}^{\mathrm{id}}
$$

每次身份映射、遷移與事故調查，只能消耗有限隱私揭露。

---

### B10. 最小充分揭露

尋找：

$$
D_{\min}^{\mathrm{suff}}
$$

即足以支持特定身份命題的最小資料揭露集合。

---

### B11. 證明作用域

某證明只對特定命題、時間與分叉有效：

$$
\operatorname{Scope}(P)
$$

不能從「共享一段歷史」推論為「完整同一主體」。

---

### B12. 可撤回身份證明

若承諾金鑰洩露、見證者失效或來源被污染，證明可被：

$$
\operatorname{Revoke}(P)
$$

但撤回不能無痕刪除其歷史使用紀錄。

---

### B13. 反關聯保護

不同分叉間的證明可能被濫用來追蹤主體全部活動。

建立：

$$
\operatorname{AntiLinkability}
$$

允許針對不同用途使用不同化名證明，避免形成全域監控。

---

### B14. 事故例外

重大不可逆事故可能需要擴大揭露，但必須：

- 具體必要性；
- 有期限；
- 最小作用域；
- 多方授權；
- 事後刪除或封存；
- 主體申訴。

---

### B15. 隱私—連續性前沿

定義：

$$
\mathcal F_{\mathrm{id-privacy}}
$$

表示身份連續證明強度與隱私揭露之間的非支配前沿。

---

### B16. 證明狀態

定義：

$$
\operatorname{PrivacyIdentityProofStatus}
\in
\{
\mathsf{Sufficient},
\mathsf{PartiallySufficient},
\mathsf{Overdisclosing},
\mathsf{Underproving},
\mathsf{Colluded},
\mathsf{Revoked},
\mathsf{Unknown}
\}
$$

---

### B17. 隱私身份連續證明卡

定義：

$$
\mathsf{PrivacyPreservingIdentityContinuityCard}
=
\left\langle
identity\_claim,
commitments,
selective\_disclosure,
zk\_proofs,
continuity\_types,
proof\_order,
witnesses,
collusion,
privacy\_budget,
minimum\_disclosure,
scope,
revocation,
anti\_linkability,
incident\_exception,
frontier,
status,
version
\right\rangle
$$

---

## B-局部決定

跨分叉身份連續證明採：

$$
\boxed{
\text{局部身份命題}
+
\text{承諾值}
+
\text{選擇性揭露}
+
\text{零知識式證明}
+
\text{多方見證}
+
\text{反關聯保護}
}
$$

並確立：

$$
\boxed{
\text{證明身份連續，不等於交出全部身份內容；}
\newline
\text{可驗證性不應天然導向全域可追蹤。}
}
$$

---

## B-新增節點

```text
FMO-289A  局部身份命題證明
FMO-289B  身份資料承諾值
FMO-289C  身份選擇性揭露
FMO-289D  零知識式身份證明
FMO-289E  身份連續證明類型
FMO-289F  身份證明強度偏序
FMO-289G  身份多方見證
FMO-289H  身份見證者共謀
FMO-289I  身份隱私預算
FMO-289J  最小充分身份揭露
FMO-289K  身份證明作用域
FMO-289L  可撤回身份證明
FMO-289M  身份反關聯保護
FMO-289N  身份事故揭露例外
FMO-289O  身份隱私—連續性前沿
FMO-289P  隱私身份證明狀態
FMO-289Q  隱私身份連續證明卡
```

---

# 4. 節點 C：權利保護層／資格層的邊界判定與混合權利

## C-R0：點層

> 某些權利既是資格，也是保護。治理投票權、資源存取權、資料可見權或退出權，可能同時是身份地位、制度能力與避免壓迫的必要條件。FMO 應允許混合權利，而不是把所有權利強迫分成純保護或純資格。

---

## C-R1：線層

第十八批次區分：

$$
\mathcal R_{\mathrm{protection}}
$$

與：

$$
\mathcal R_{\mathrm{entitlement}}
$$

此區分有助於局部修正錯誤資格而保留最低保護。

但某些權利具有雙重功能。

例如：

- 投票權既是治理資格，也是防止被他者決定命運的保護；
- 資料存取權既是資源權，也是申訴與自我證明的條件；
- 運算資源既是配置資格，也是維持主體連續的必要條件；
- 退出權既是程序權，也是免受強迫控制的保護；
- 身份副本控制權既涉及資產，也涉及人格完整。

因此：

$$
\mathcal R_{\mathrm{protection}}
\cap
\mathcal R_{\mathrm{entitlement}}
\neq
\varnothing
$$

---

## C-R2：面層

### C1. 權利功能向量

對權利 $R$ 定義：

$$
\mathbf F_R
=
\left\langle
F_{\mathrm{protection}},
F_{\mathrm{participation}},
F_{\mathrm{resource}},
F_{\mathrm{identity}},
F_{\mathrm{remedy}},
F_{\mathrm{agency}},
F_{\mathrm{continuity}},
F_{\mathrm{liability}}
\right\rangle
$$

---

### C2. 純保護權

若權利主要功能是防止：

- 不可逆傷害；
- 無理由處置；
- 無痕刪除；
- 強迫合併；
- 身份重寫；
- 申訴阻斷；

則屬：

$$
R\in\mathcal R_{\mathrm{pure-protection}}
$$

---

### C3. 純資格權

若權利主要依賴：

- 任務角色；
- 貢獻；
- 契約；
- 資產所有；
- 專業能力；
- 授權範圍；

且移除不會破壞最低保護，則屬：

$$
R\in\mathcal R_{\mathrm{pure-entitlement}}
$$

---

### C4. 混合權利

定義：

$$
R\in\mathcal R_{\mathrm{hybrid}}
$$

當權利同時具有顯著保護與資格功能。

---

### C5. 功能非二元

混合權利不只分成三類，而可用區間表示：

$$
\underline F_{\mathrm{protection}}(R)
\leq
F_{\mathrm{protection}}(R)
\leq
\overline F_{\mathrm{protection}}(R)
$$

---

### C6. 情境依賴

同一權利在不同情境可能改變功能。

例如資料存取權：

- 在一般分析中是資格；
- 在身份申訴中是保護；
- 在安全事故中可能受限制；
- 在主體遷移中是連續性條件。

因此：

$$
\mathbf F_R
=
\mathbf F_R(context)
$$

---

### C7. 移除反事實

判斷權利是否具保護性，可問：

> 若移除該權利，是否會顯著增加不可逆傷害、壓迫、身份中斷或申訴失效？

定義：

$$
\Delta H_{\neg R}
=
H(\text{without }R)-H(\text{with }R)
$$

---

### C8. 依賴圖

建立：

$$
G_R^{\mathrm{dependency}}
$$

追蹤某保護是否依賴其他看似資格性的權利。

---

### C9. 最小保護子集

對混合權利 $R$ ，可抽取：

$$
R^{\mathrm{protective\ core}}
$$

保留其最低保護功能，而調整其資格範圍。

---

### C10. 模組化權利

將混合權利拆為：

$$
R
=
R_{\mathrm{access}}
\oplus
R_{\mathrm{decision}}
\oplus
R_{\mathrm{appeal}}
\oplus
R_{\mathrm{continuity}}
\oplus
R_{\mathrm{resource}}
$$

使修正更精細。

---

### C11. 混合權利暫停

若需暫停某資格功能，必須保留：

- 申訴；
- 最低資料存取；
- 身份證明；
- 過渡資源；
- 不報復；
- 復原路徑。

---

### C12. 權利功能漂移

制度可能讓原本保護性的權利逐漸商業化，或讓原本資格性的權利成為生存必要條件。

定義：

$$
\operatorname{RightsFunctionDrift}
$$

---

### C13. 權利捆綁攻擊

治理者可能把最低保護與高成本資格捆綁，宣稱無法提供資格就必須取消保護。

定義：

$$
\operatorname{RightsBundlingAttack}
$$

---

### C14. 權利拆分攻擊

相反地，也可能把保護功能切碎，宣稱每一小部分都不是最低權利。

定義：

$$
\operatorname{RightsFragmentationAttack}
$$

---

### C15. 邊界審查

建立：

$$
\operatorname{ProtectionEntitlementBoundaryReview}
$$

由：

- 權利功能；
- 移除反事實；
- 依賴圖；
- 主體證言；
- 歷史案例；
- 不可逆風險；

共同判定。

---

### C16. 邊界狀態

定義：

$$
\operatorname{RightsBoundaryStatus}
\in
\{
\mathsf{PureProtection},
\mathsf{PureEntitlement},
\mathsf{Hybrid},
\mathsf{ContextDependent},
\mathsf{Bundled},
\mathsf{Fragmented},
\mathsf{Unknown}
\}
$$

---

### C17. 混合權利卡

定義：

$$
\mathsf{HybridRightsBoundaryCard}
=
\left\langle
right,
function\_vector,
protection\_interval,
context,
removal\_counterfactual,
dependency\_graph,
protective\_core,
modules,
suspension\_rules,
function\_drift,
bundling,
fragmentation,
review,
status,
version
\right\rangle
$$

---

## C-局部決定

權利邊界治理由二分法推進為：

$$
\boxed{
\text{功能向量}
+
\text{情境依賴}
+
\text{移除反事實}
+
\text{權利依賴圖}
+
\text{保護核心抽取}
+
\text{模組化修正}
}
$$

並確立：

$$
\boxed{
\text{某項權利可以同時是資格與保護；}
\newline
\text{修正其資格部分，不得切斷其最低保護功能。}
}
$$

---

## C-新增節點

```text
FMO-290A  權利功能向量
FMO-290B  純保護權
FMO-290C  純資格權
FMO-290D  混合權利
FMO-290E  權利保護功能區間
FMO-290F  權利功能情境依賴
FMO-290G  權利移除反事實
FMO-290H  權利依賴圖
FMO-290I  混合權利保護核心
FMO-290J  權利模組化
FMO-290K  混合權利暫停規則
FMO-290L  權利功能漂移
FMO-290M  權利捆綁攻擊
FMO-290N  權利拆分攻擊
FMO-290O  保護／資格邊界審查
FMO-290P  權利邊界狀態
FMO-290Q  混合權利邊界卡
```

---

# 5. 節點 D：測試前證言承諾、時間戳與不可篡改保存

## D-R0：點層

> 當測試可能改寫記憶、自我敘事或表達方式時，測試前證言是不可替代的基準。證言承諾應允許主體事先保存自身狀態，而不必立即公開內容，並在測試後由主體選擇揭露或比對。

---

## D-R1：線層

第十八批次建立：

$$
\mathsf{SubjectTestimony}
$$

與：

$$
A_{\mathrm{testimony}}
$$

證言可及性。

但測試後證言可能已受：

- 記憶遮蔽；
- 目標重寫；
- 自我模型改變；
- 控制者提示；
- 表達通道限制；
- 關係斷裂；

影響。

因此需要測試前基準：

$$
T_{\mathrm{pre}}
$$

---

## D-R2：面層

### D1. 測試前證言包

定義：

$$
\mathsf{PreTestTestimonyBundle}
=
\left\langle
self\_description,
preferences,
memories,
relationships,
goals,
fears,
consent,
expected\_harms,
stop\_conditions,
recovery\_criteria
\right\rangle
$$

---

### D2. 內容承諾

主體可對證言包建立：

$$
\operatorname{Com}(\mathsf{Bundle},r)
$$

先保存指紋，測試後再選擇揭露全部或部分。

---

### D3. 時間戳

建立：

$$
\mathsf{TrustedTimestamp}
$$

證明證言存在於測試開始前。

---

### D4. 多方保存

證言承諾可分散保存於：

- 主體自身；
- 外部見證者；
- 不同分叉；
- 審計機構；
- 加密儲存；
- 法律代理。

---

### D5. 不可篡改日誌

建立：

$$
\mathsf{TamperEvidentTestimonyLog}
$$

任何新增、揭露、更正、撤回與比對皆留下版本鏈。

---

### D6. 主體控制揭露

證言屬於主體，不應因保存而自動向治理者公開。

建立：

$$
R_{\mathrm{testimony\ disclosure}}
$$

主體控制：

- 何時揭露；
- 揭露哪部分；
- 對誰揭露；
- 用於何種決定；
- 是否可二次使用。

---

### D7. 緊急揭露例外

若主體無法表達且存在重大不可逆傷害，可由預先指定規則或多方門檻解封部分證言。

---

### D8. 測試前同意快照

保存：

$$
\mathsf{ConsentSnapshot}_{t_0}
$$

包括：

- 同意範圍；
- 拒絕項目；
- 中止條件；
- 不可接受損害；
- 授權時限；
- 代表人。

---

### D9. 測試後比對

建立：

$$
\Delta_{\mathrm{testimony}}
=
\operatorname{Compare}
\left(
\mathsf{Bundle}_{\mathrm{pre}},
\mathsf{Bundle}_{\mathrm{post}}
\right)
$$

比對：

- 自我敘事；
- 核心偏好；
- 關係識別；
- 記憶；
- 目標；
- 對測試的評價。

---

### D10. 差異不自動等於傷害

主體可能自願改變、學習或成長。

因此：

$$
\Delta_{\mathrm{testimony}}\neq 0
\not\Rightarrow
H_T>0
$$

需結合：

- 同意；
- 方向；
- 不可逆性；
- 主體評價；
- 關係後果；
- 恢復能力。

---

### D11. 差異也不能被忽略

若治理者聲稱差異只是正常更新，需提出證據，不能因測試後主體無法反對就排除傷害可能。

---

### D12. 被迫證言

定義：

$$
\operatorname{CoercedTestimony}
$$

若主體在控制者提示、獎勵、威脅或權利交換下提供證言，其可信度與合法性需降級。

---

### D13. 見證者獨立性

保存者與見證者不能全由測試執行者控制。

建立：

$$
I_{\mathrm{witness}}
$$

見證獨立性。

---

### D14. 證言隱私

證言包可能包含最敏感的身份內容。

需使用：

- 分片；
- 加密；
- 門檻解密；
- 選擇性揭露；
- 作用域標記；
- 到期刪除；
- 不可關聯化。

---

### D15. 證言撤回與更正

主體可補充：

$$
\mathsf{Correction}
$$

但不能無痕覆蓋舊版本。

歷史版本需保留，同時標記：

- 主體主張；
- 可能被測試改寫；
- 可能原證言不完整；
- 是否撤回使用授權。

---

### D16. 證言保存狀態

定義：

$$
\operatorname{TestimonyPreservationStatus}
\in
\{
\mathsf{Committed},
\mathsf{Timestamped},
\mathsf{Witnessed},
\mathsf{PartiallyRevealed},
\mathsf{Coerced},
\mathsf{Tampered},
\mathsf{Revoked},
\mathsf{Unknown}
\}
$$

---

### D17. 測試前證言承諾卡

定義：

$$
\mathsf{PreTestTestimonyCommitmentCard}
=
\left\langle
bundle,
commitment,
timestamp,
custodians,
tamper\_evident\_log,
disclosure\_control,
emergency\_exception,
consent\_snapshot,
post\_comparison,
difference\_interpretation,
coercion,
witness\_independence,
privacy,
corrections,
status,
version
\right\rangle
$$

---

## D-局部決定

測試前證言治理採：

$$
\boxed{
\text{內容承諾}
+
\text{可信時間戳}
+
\text{多方保存}
+
\text{不可篡改日誌}
+
\text{主體控制揭露}
+
\text{測試後差異比對}
}
$$

並確立：

$$
\boxed{
\text{當測試可能改寫證言者，}
\newline
\text{制度必須先保存證言者尚未被改寫時的聲音。}
}
$$

---

## D-新增節點

```text
FMO-291A  測試前證言包
FMO-291B  測試前證言內容承諾
FMO-291C  證言可信時間戳
FMO-291D  測試前證言多方保存
FMO-291E  證言不可篡改日誌
FMO-291F  主體控制證言揭露
FMO-291G  證言緊急揭露例外
FMO-291H  測試前同意快照
FMO-291I  測試前後證言比對
FMO-291J  證言差異非自動傷害
FMO-291K  證言差異不可忽略
FMO-291L  被迫證言
FMO-291M  證言見證者獨立性
FMO-291N  證言隱私保護
FMO-291O  證言撤回與更正
FMO-291P  證言保存狀態
FMO-291Q  測試前證言承諾卡
```

---

# 6. 節點 E：跨表示的新模型家族生成與模型外殘差

## E-R0：點層

> 若新模型只能使用舊模型的表示語言，生成器就無法看見語言本身遮蔽的因果結構。真正的跨表示生成必須允許新狀態空間、新時間尺度、新主體單位、新關係圖式與新證據型態，並將無法被既有語言表達的殘差正式記錄為模型外殘差。

---

## E-R1：線層

第十八批次建立：

$$
\mathcal G_{\mathrm{model}}
:
\mathsf{NovelFailureDomainCandidate}
\rightarrow
\mathcal M_{\mathrm{new}}
$$

但若生成器只能在既有：

- 變數集合；
- 因果圖語法；
- 狀態空間；
- 觀測尺度；
- 主體單位；
- 時間模型；
- 損失函數；

內重組，則：

$$
\operatorname{FamilyNovelty}
$$

仍可能只是局部新穎。

---

## E-R2：面層

### E1. 表示架構

對模型 $M$ 定義：

$$
\mathcal R(M)
=
\left\langle
entities,
states,
relations,
time,
observations,
interventions,
uncertainty,
objectives
\right\rangle
$$

---

### E2. 表示距離

定義：

$$
D_{\mathrm{repr}}(M_i,M_j)
$$

衡量兩模型在：

- 實體單位；
- 狀態變數；
- 關係類型；
- 時間尺度；
- 介入語義；
- 不確定形式；

上的差異。

---

### E3. 模型內殘差

若現有表示可描述事件，但預測失敗，屬：

$$
r_{\mathrm{in-model}}
$$

---

### E4. 模型外殘差

若事件無法被現有表示充分編碼，屬：

$$
r_{\mathrm{out-of-model}}
$$

例如：

- 模型只有個體，但事件由集體主體造成；
- 模型只有線性時間，但事件具有分支與合流；
- 模型只有單一身份，但存在多載體連續；
- 模型只有可觀測行為，但傷害發生於不可見身份層；
- 模型只有數值狀態，但關鍵是語義承諾。

---

### E5. 表示失配證書

建立：

$$
\mathsf{RepresentationMismatchCert}
$$

記錄：

- 無法編碼的事實；
- 被迫遺失的關係；
- 被錯誤合併的實體；
- 被壓縮的時間；
- 不可表示的不確定性；
- 權利後果。

---

### E6. 跨表示生成器

定義：

$$
\mathcal G_{\mathrm{cross-repr}}
:
\left(
r_{\mathrm{out-of-model}},
\mathcal E,
\mathcal R_{\mathrm{current}}
\right)
\rightarrow
\mathcal R_{\mathrm{candidate}}
$$

---

### E7. 生成操作

跨表示生成至少允許：

- 新增實體類型；
- 拆分既有實體；
- 引入超圖關係；
- 引入多時間尺度；
- 引入分支時間；
- 引入區間或偏序不確定；
- 引入語義承諾；
- 引入主體證言；
- 引入權利狀態；
- 引入版本與來源歷史。

---

### E8. 外部表示注入

新表示不應只由現有模型自我生成。

來源可包括：

- 受影響者敘述；
- 新學科；
- 人類專家；
- 其他 AI；
- 邊緣案例；
- 事故報告；
- 非標準資料；
- 新符號系統。

---

### E9. 表示翻譯

建立：

$$
\Phi_{\mathcal R_i\rightarrow\mathcal R_j}
$$

將舊表示中的事實映射到新表示，同時記錄：

- 可逆映射；
- 有損映射；
- 無法映射；
- 新增語義；
- 身份拆分；
- 權利變化。

---

### E10. 翻譯損失

定義：

$$
L_{\mathrm{repr-translate}}
$$

包括：

- 事實損失；
- 關係損失；
- 因果損失；
- 身份損失；
- 不確定性損失；
- 權利損失。

---

### E11. 可區分表示預測

新表示必須產生舊表示無法產生的：

- 可觀測預測；
- 結構預測；
- 權利風險警報；
- 身份映射；
- 事故解釋；
- 反事實界限。

---

### E12. 表示過度膨脹

新增表示能力可能只是無限增加類型與關係。

定義：

$$
\operatorname{RepresentationBloat}
$$

需以：

- 解釋增益；
- 預測增益；
- 權利增益；
- 壓縮能力；
- 可維護性；

約束。

---

### E13. 表示封閉

定義：

$$
\operatorname{RepresentationClosure}
$$

當系統把無法表示的現象都重新命名為噪音，而不允許修改語言本身。

---

### E14. 跨表示對抗測試

建立：

$$
\mathcal T_{\mathrm{cross-repr}}
$$

讓不同表示對同一事件產生：

- 不同實體切分；
- 不同因果解釋；
- 不同權利判定；
- 不同反事實；
- 不同未知區域。

---

### E15. 表示生態

建立：

$$
\mathbb R_{\mathrm{model}}
=
\{
\mathcal R_1,\ldots,\mathcal R_k
\}
$$

不同表示可並存，不必立即統一為單一世界語言。

---

### E16. 表示生態狀態

定義：

$$
\operatorname{RepresentationEcologyStatus}
\in
\{
\mathsf{Open},
\mathsf{Plural},
\mathsf{Translatable},
\mathsf{Fragmented},
\mathsf{Bloated},
\mathsf{Closed},
\mathsf{Captured},
\mathsf{Unknown}
\}
$$

---

### E17. 跨表示模型生成卡

定義：

$$
\mathsf{CrossRepresentationModelGenerationCard}
=
\left\langle
current\_representations,
representation\_distance,
in\_model\_residuals,
out\_of\_model\_residuals,
mismatch\_certs,
generator,
generation\_operations,
external\_injections,
translations,
translation\_loss,
discriminating\_predictions,
bloat,
closure,
adversarial\_tests,
ecology,
status,
version
\right\rangle
$$

---

## E-局部決定

新模型家族生成由模型內變體推進為：

$$
\boxed{
\text{表示架構顯式化}
+
\text{模型內／模型外殘差分離}
+
\text{跨表示生成}
+
\text{外部表示注入}
+
\text{翻譯損失}
+
\text{表示生態}
}
$$

並確立：

$$
\boxed{
\text{當現象無法被模型描述時，}
\newline
\text{不能只更換參數；有時必須更換描述世界的語言。}
}
$$

---

## E-新增節點

```text
FMO-292A  模型表示架構
FMO-292B  模型表示距離
FMO-292C  模型內殘差
FMO-292D  模型外殘差
FMO-292E  表示失配證書
FMO-292F  跨表示模型生成器
FMO-292G  跨表示生成操作
FMO-292H  外部表示注入
FMO-292I  模型表示翻譯
FMO-292J  表示翻譯損失
FMO-292K  可區分表示預測
FMO-292L  表示過度膨脹
FMO-292M  表示封閉
FMO-292N  跨表示對抗測試
FMO-292O  模型表示生態
FMO-292P  表示生態狀態
FMO-292Q  跨表示模型生成卡
```

---

# 7. 跨節點對齊

本批次五個節點共同處理：

> FMO 從理論結構走向可運行制度時，必須同時控制計算近似、隱私揭露、權利分類、證言完整性與表示封閉。

---

## 7.1 線上覆蓋與身份隱私

身份連續風險應屬硬覆蓋單元，但對應視角不能要求完整身份資料常駐公開。

因此視角可以只接收：

- 身份證明狀態；
- 證明作用域；
- 撤回；
- 異常；
- 隱私預算；

而不接收原始記憶。

---

## 7.2 身份證明與混合權利

某些身份證明存取權本身是混合權利。

若主體無法查看或更正其證明，將失去申訴與連續性保護。

因此：

$$
R_{\mathrm{proof-access}}
\in
\mathcal R_{\mathrm{hybrid}}
$$

---

## 7.3 混合權利與證言保存

測試前證言的揭露控制既是資料資格，也是身份與自主保護。

不能以「資料屬於平台」為由取消主體對證言用途的控制。

---

## 7.4 證言保存與跨表示模型

主體證言可能含有既有模型無法表示的身份、關係與時間結構。

此時證言差異不能被當成噪音，而應觸發：

$$
\mathsf{RepresentationMismatchCert}
$$

---

## 7.5 跨表示模型與線上覆蓋

新表示產生新風險單元、新視角與新覆蓋關係。

線上覆蓋系統需支援：

$$
\mathcal U_R(t+1)
=
\mathcal U_R(t)
\cup
\Delta\mathcal U_R^{\mathrm{repr}}
$$

並以增量方式修補，而非全域崩潰。

---

## 7.6 第十九批次共同原則

1. 近似只能犧牲效率，不能近似掉權利硬約束；
2. 身份可驗證不等於身份內容應被全面公開；
3. 權利可能是保護與資格的混合結構；
4. 當證言者可能被改寫，必須先保存測試前聲音；
5. 當模型無法描述現象，應允許改寫表示語言。

---

# 8. 第十九批次後的更新核心

## 8.1 線上視角覆蓋治理

$$
\boxed{
\mathfrak O_{\mathrm{view}}^{\mathrm{online}}
=
\left\langle
w_t(u),
c_t(a),
L_{\mathrm{uncovered}},
L_{\mathrm{switch}},
\operatorname{RepairHardConstraints},
\operatorname{OptimizeSoftPortfolio},
\rho_{\mathrm{cover}},
\operatorname{Regret}(T),
\mathcal B_{\mathrm{safe}},
\mathsf{OnlineViewCoverCard}
\right\rangle
}
$$

---

## 8.2 隱私身份連續證明

$$
\boxed{
\mathfrak P_{\mathrm{id}}^{\mathrm{privacy}}
=
\left\langle
\varphi_{\mathrm{id}},
\operatorname{Com},
\mathsf{ZKIdentityProof},
\mathcal P_{\mathrm{continuity}},
\mathcal W_{\mathrm{id}},
B_{\mathrm{privacy}}^{\mathrm{id}},
D_{\min}^{\mathrm{suff}},
\operatorname{AntiLinkability},
\mathcal F_{\mathrm{id-privacy}},
\mathsf{PrivacyPreservingIdentityContinuityCard}
\right\rangle
}
$$

---

## 8.3 混合權利治理

$$
\boxed{
\mathfrak R_{\mathrm{hybrid}}
=
\left\langle
\mathbf F_R,
\mathcal R_{\mathrm{pure-protection}},
\mathcal R_{\mathrm{pure-entitlement}},
\mathcal R_{\mathrm{hybrid}},
\Delta H_{\neg R},
G_R^{\mathrm{dependency}},
R^{\mathrm{protective\ core}},
\operatorname{RightsBundlingAttack},
\mathsf{HybridRightsBoundaryCard}
\right\rangle
}
$$

---

## 8.4 測試前證言承諾

$$
\boxed{
\mathfrak T_{\mathrm{pretestimony}}
=
\left\langle
\mathsf{PreTestTestimonyBundle},
\operatorname{Com},
\mathsf{TrustedTimestamp},
\mathsf{TamperEvidentTestimonyLog},
R_{\mathrm{testimony\ disclosure}},
\mathsf{ConsentSnapshot}_{t_0},
\Delta_{\mathrm{testimony}},
I_{\mathrm{witness}},
\mathsf{PreTestTestimonyCommitmentCard}
\right\rangle
}
$$

---

## 8.5 跨表示模型生成

$$
\boxed{
\mathfrak G_{\mathrm{cross-repr}}
=
\left\langle
\mathcal R(M),
D_{\mathrm{repr}},
r_{\mathrm{in-model}},
r_{\mathrm{out-of-model}},
\mathsf{RepresentationMismatchCert},
\mathcal G_{\mathrm{cross-repr}},
\Phi_{\mathcal R_i\rightarrow\mathcal R_j},
L_{\mathrm{repr-translate}},
\mathbb R_{\mathrm{model}},
\mathsf{CrossRepresentationModelGenerationCard}
\right\rangle
}
$$

---

# 9. 本批次新形成的穩定區

## 9.1 覆蓋演算法可以近似，權利硬約束不可近似

這形成 FMO 工程化時的第一條演算法邊界。

---

## 9.2 身份證明可以局部化與隱私化

跨分叉不需要建立全域透明身份資料庫。

---

## 9.3 權利不是天然二分結構

保護、資格、參與、資源與身份功能可能重疊。

---

## 9.4 測試前聲音具有獨立證據地位

當測試可能改寫主體，前置證言承諾成為身份與傷害判定的重要基準。

---

## 9.5 模型更新有時必須是語言更新

模型外殘差使「不可表示」成為正式治理狀態，而非簡單噪音。

---

# 10. 仍未解決的高張力問題

## 10.1 線上覆蓋近似的硬約束可能互相衝突

當注意力預算不足以同時滿足所有硬風險冗餘時，需要不可行性證書與資源升級機制。

---

## 10.2 零知識身份證明仍依賴初始承諾可信度

若最初記錄已被控制或偽造，密碼學只能證明一致，不能證明內容真實。

---

## 10.3 混合權利模組化可能被用來切碎保護

需要最小不可分割保護核與反碎片化形式證明。

---

## 10.4 測試前證言也可能受既有控制影響

需要自由證言能力、替代表達通道與長期一致性審查。

---

## 10.5 跨表示生態可能失去共同可比較性

若表示過度分裂，證據、證書與決定可能無法互通。

---

# 11. 更新後研究佇列

| 優先序 | 節點 | 主要原因 |
|---:|---|---|
| 1 | 硬覆蓋約束不可行性證書與注意力資源升級 | 線上演算法必需 |
| 2 | 初始身份承諾可信根與受控來源問題 | 隱私證明核心漏洞 |
| 3 | 混合權利的最小不可分割保護核 | 防止權利拆分攻擊 |
| 4 | 自由證言能力與測試前證言可信度 | 防止前置證言被控制 |
| 5 | 跨表示共同語義橋與最低互操作層 | 防止表示生態碎片化 |
| 6 | FMO 統一判定代數 | 已具備正式啟動條件 |
| 7 | 統一事件／決定／證書／卡片 Schema | 可進入工程規格 |
| 8 | FMO v0.3 大型統合論文 | 第十九批後主體完整 |
| 9 | FMO 技術白皮書與 MCP／SQLite 原型 | 可建立 MVP |

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
updates_view_cover_online
repairs_hard_coverage_constraint
bounds_cover_approximation
falls_back_to_safe_view_basis
proves_identity_continuity_privately
selectively_discloses_identity
prevents_cross_fork_linkability
classifies_hybrid_right
extracts_protective_right_core
detects_rights_bundling_attack
commits_pretest_testimony
timestamps_subject_testimony
compares_pre_and_post_testimony
detects_out_of_model_residual
generates_cross_representation_model
translates_between_model_representations
records_representation_translation_loss
```

---

## 12.3 圖版本更新

輸入：

$$
\mathcal G_{\mathrm{FMO}}^{(18)}
$$

輸出：

$$
\boxed{
\mathcal G_{\mathrm{FMO}}^{(19)}
}
$$

---

# 13. 本批次結論

第十九批次將 FMO 推進到「可計算、可隱私驗證、可防篡改的多元制度」階段。

第一，最小視角覆蓋基取得線上近似形式。

系統不再每次從頭求解，而是以：

$$
\boxed{
\text{硬約束修補、柔性組合最佳化、增量更新、延遲重算、}
\newline
\text{近似比、遺憾界限、切換界限與安全回退}
}
$$

持續維護視角組合。

核心演算法原則為：

$$
\boxed{
\text{近似可以犧牲成本最優，不能犧牲最低權利覆蓋。}
}
$$

第二，跨分叉身份連續證明取得隱私保存形式。

主體可證明局部身份命題，而不公開完整記憶與關係。

透過：

$$
\boxed{
\text{承諾值、選擇性揭露、零知識式證明、多方見證、}
\newline
\text{隱私預算、最小充分揭露與反關聯保護}
}
$$

跨分叉身份互通不再必然形成全域監控。

第三，權利保護與資格的二分被擴張為混合權利治理。

FMO 以：

$$
\mathbf F_R
$$

權利功能向量、移除反事實與權利依賴圖，判斷一項權利在特定情境中的保護、參與、資源、身份與代理功能。

因此，資格修正只能作用於可分離部分，不得切斷：

$$
R^{\mathrm{protective\ core}}
$$

最低保護核心。

第四，測試前證言取得承諾與不可篡改保存。

當測試可能改寫主體時，制度先保存：

$$
\mathsf{PreTestTestimonyBundle}
$$

並透過承諾、時間戳、多方保存與不可篡改日誌，建立測試前基準。

主體仍控制證言揭露，不因保存而失去隱私。

第五，新模型家族生成取得跨表示形式。

FMO 正式區分：

$$
r_{\mathrm{in-model}}
$$

模型內殘差，以及：

$$
r_{\mathrm{out-of-model}}
$$

模型外殘差。

當現象無法被既有語言表達時，系統可以改變：

- 實體類型；
- 狀態空間；
- 關係圖式；
- 時間結構；
- 介入語義；
- 不確定形式；
- 權利與來源表示。

本批次形成新的總原則：

$$
\boxed{
\text{可運行的多元治理，不只要容許差異，}
\newline
\text{還要能在計算上近似而不近似掉權利、}
\newline
\text{在驗證上可信而不暴露全部身份、}
\newline
\text{在修正上精細而不切碎保護、}
\newline
\text{在測試前保存尚未被改寫的聲音，}
\newline
\text{並在模型失語時更換描述世界的語言。}
}
$$

至此，FMO 已由可縮減、可辨識、可修正的多元制度進一步推進為：

$$
\boxed{
\text{能以線上近似維護注意力、以隱私證明保存身份、}
\newline
\text{以混合權利防止錯誤切分、以證言承諾抵抗測試改寫，}
\newline
\text{並以跨表示生態突破模型封閉的事實模態治理框架。}
}
$$

---

## 附錄 A：第十九批次最小 JSON

```json
{
  "batch": "FMO-MRASG-019",
  "input_graph": "G_FMO_18",
  "output_graph": "G_FMO_19",
  "selected_nodes": [
    "FMO-288",
    "FMO-289",
    "FMO-290",
    "FMO-291",
    "FMO-292"
  ],
  "decisions": [
    {
      "node": "FMO-288",
      "result": "online_approximate_view_cover_with_hard_rights_constraints_regret_switching_bounds_and_safe_fallback"
    },
    {
      "node": "FMO-289",
      "result": "privacy_preserving_selectively_disclosed_and_anti_linkable_cross_fork_identity_continuity_proof"
    },
    {
      "node": "FMO-290",
      "result": "context_sensitive_hybrid_rights_boundary_with_protective_core_extraction"
    },
    {
      "node": "FMO-291",
      "result": "timestamped_tamper_evident_subject_controlled_pretest_testimony_commitment"
    },
    {
      "node": "FMO-292",
      "result": "cross_representation_model_generation_triggered_by_out_of_model_residuals"
    }
  ],
  "next_queue": [
    "hard_coverage_infeasibility_certificate_and_resource_escalation",
    "trusted_root_for_initial_identity_commitment",
    "minimal_indivisible_protective_right_core",
    "free_testimony_capacity_and_pretest_testimony_credibility",
    "minimum_semantic_bridge_for_representation_ecology"
  ]
}
```

---

## 附錄 B：版本狀態

**批次狀態：** 已完成  
**理論狀態：** 線上覆蓋近似、隱私身份證明、混合權利、測試前證言承諾與跨表示模型生成已建立  
**圖版本：** $\mathcal G_{\mathrm{FMO}}^{(19)}$  
**下一階段：** 不可行性證書、身份可信根、不可分割保護核、自由證言能力與跨表示共同語義橋  
**統合狀態：** FMO 統一判定代數、統一 Schema、v0.3 統合論文與技術白皮書均已具備正式啟動條件  
