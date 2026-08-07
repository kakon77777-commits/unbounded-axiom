# CAIR 治理與供應鏈安全白皮書：可執行能力、來源證據與多方控制

**英文名稱：** CAIR Governance and Software Supply-Chain Security White Paper: Executable Capabilities, Provenance Evidence, and Multi-Party Control  
**版本：** v1.0  
**日期：** 2026-07-29  
**文件狀態：** 公開版／穩定安全白皮書  
**對應實作：** `cair-mvp==1.0.0`  
**CAIR Schema：** `1.0.0`  
**Database Schema：** `1000`  
**穩定 API：** `/api/v1`

---

## 摘要

AI 原生程式系統的安全問題，不再只是「程式碼是否包含漏洞」。當 AI、Agent、Skill、政策引擎、套件 Registry、遠端治理節點與執行後端共同參與一個計算系統時，安全問題至少同時包含六個層次：

1. 這項能力由誰定義；
2. 內容在傳輸或安裝前是否被竄改；
3. 簽署者是否仍受信任；
4. 當前主體是否有權在指定區域執行；
5. 此次變更是否經過足夠的治理批准；
6. 實際執行是否受到隔離、限制並留下證據。

CAIR（Canonical Authoritative Intermediate Representation）將上述問題整合至同一治理鏈，但不將它們壓縮成單一「可信」布林值。CAIR v1.0 將程式內容、簽章、簽署者狀態、依賴鎖、套件啟用、區域政策、主體能力、風險門檻、多人批准、透明度紀錄、外部見證、分散式複製與執行證書視為彼此獨立且必須組合驗證的證據。

其核心關係可表示為：

$$
\operatorname{Executable}
=
C_{\text{content}}
\land
C_{\text{signature}}
\land
C_{\text{identity}}
\land
C_{\text{dependency}}
\land
C_{\text{governance}}
\land
C_{\text{authorization}}
\land
C_{\text{runtime}}
$$

其中任一必要條件不成立，系統都不得以其他條件「看起來可信」為理由繼續執行。

CAIR v1.0 已實作簽章式 `.cairskill` 與 `.cairpolicy` 套件、Ed25519 簽署者與金鑰世代、依賴鎖、治理變更提案、多方簽章批准、角色與組織多樣性門檻、append-only 透明度日誌、Merkle checkpoint、witness quorum、gossip、遠端治理複製、CRDT 物化狀態、可驗證快照、OCI Registry 適配、Sigstore／Fulcio／Rekor 邊界、OPA／Rego 適配與受控 Skill 執行證書。

本文說明其安全模型、威脅假設、信任根、治理程序、套件生命週期、分散式邊界與外部標準對照。CAIR v1.0 不宣稱已成為 TUF 實作、SLSA 認證建置平台、完整 in-toto 驗證器、RFC 9162 透明度服務、BFT 共識系統或任意敵意程式碼沙盒。它所完成的是一個更基本且可測試的安全閉環：

> 可執行能力不再只是一段程式碼，而是一個同時攜帶內容、來源、權限、治理、限制、撤銷狀態與執行證據的受控物件。

**關鍵詞：** CAIR、軟體供應鏈、安全治理、Skill、Ed25519、Sigstore、OCI、SLSA、in-toto、TUF、OPA、透明度日誌、Witness、多方治理

---

# 第一部分　安全問題的重新定義

## 一、從程式碼安全到能力安全

傳統軟體安全通常關注：

- 原始碼漏洞；
- 依賴漏洞；
- 建置環境；
- 套件簽章；
- 部署設定；
- 執行時隔離；
- 身分與存取控制。

在 AI Agent 系統中，還必須加入：

- AI 是否將推定當成明確指令；
- Agent 是否可自行擴權；
- Skill 是否可以跨越原本區域；
- 遠端治理訊息是否會直接觸發本地副作用；
- 模型生成與權威提交是否被混為一談；
- 執行結果是否會偷偷回寫權威狀態；
- 套件簽章是否仍使用已撤銷金鑰；
- 「通過一個驗證器」是否被誤解為整體安全。

因此，CAIR 不將安全表示為：

$$
\operatorname{trusted}
\in
\{0,1\}
$$

而表示為證據向量：

$$
\mathbf{T}
=
(
t_c,
t_s,
t_i,
t_d,
t_g,
t_a,
t_r,
t_h
)
$$

其中：

- $t_c$ ：內容完整性；
- $t_s$ ：簽章有效性；
- $t_i$ ：簽署者與金鑰狀態；
- $t_d$ ：依賴完整性；
- $t_g$ ：治理批准；
- $t_a$ ：主體與區域授權；
- $t_r$ ：執行時隔離；
- $t_h$ ：歷史與透明度證據。

不同操作需要不同的必要子集合，不能以總分或平均分取代必要條件。

---

## 二、治理與安全的關係

治理不是安全之外的行政附屬物，而是決定「誰能改變安全邊界」的控制層。

令安全政策為：

$$
\mathcal{S}_t
$$

治理變更為：

$$
\Delta \mathcal{G}_t
$$

則治理可能改變：

- 受信任簽署者；
- 有效金鑰；
- 套件啟用狀態；
- Region policy；
- Skill 能力；
- 風險上限；
- 必要 Validator；
- Witness；
- 政策文件；
- 治理成員。

因此：

$$
\Delta \mathcal{G}_t
\Rightarrow
\Delta \mathcal{S}_{t+1}
$$

若治理變更本身缺乏審查、簽章與歷史證據，再嚴格的執行政策也可能被合法介面繞過。

---

## 三、CAIR 的安全目標

CAIR v1.0 的安全目標包括：

### 3.1 權威狀態完整性

未通過驗證與提交的候選修改不得改變權威程式。

### 3.2 套件內容完整性

安裝內容必須與 manifest 中的 SHA-256 一致。

### 3.3 簽署者可撤銷性

受信任身分與特定金鑰世代必須分離管理。

### 3.4 依賴精確性

套件依賴必須綁定精確 ID、版本與內容指紋。

### 3.5 最小執行權

主體只能在特定 Region、特定 Skill、特定能力與風險範圍內執行。

### 3.6 多方治理

高影響變更可以要求簽章、角色覆蓋、批准數量與組織多樣性。

### 3.7 透明度與可檢查性

關鍵治理與供應鏈事件應可被追加記錄、見證與一致性檢查。

### 3.8 遠端自主性保留

遠端節點的決策可以被驗證與物化，但不得自動成為本地副作用。

### 3.9 誠實降級

缺少外部工具、可信材料或隔離後端時，系統必須回報 `unavailable`、`rejected` 或 `not ready`，不得偽裝成驗證成功。

---

# 第二部分　威脅模型

## 四、受保護資產

CAIR 主要保護：

1. 權威程式版本；
2. Skill 與 Policy 套件；
3. 簽署者身分與金鑰狀態；
4. 依賴鎖；
5. 治理提案與批准；
6. Region 與 Capability 政策；
7. 透明度日誌與 checkpoint；
8. Witness 聲明；
9. 遠端治理複製紀錄；
10. CRDT 物化治理狀態；
11. 可驗證快照；
12. 執行證書；
13. Registry credential 與外部 trust material。

---

## 五、攻擊者類型

### 5.1 惡意套件作者

可能：

- 修改套件內容；
- 隱藏額外檔案；
- 使用路徑穿越；
- 放入符號連結；
- 偽造 signer；
- 鎖定不存在或不同內容的依賴；
- 嘗試使用撤銷金鑰。

### 5.2 被入侵的簽署金鑰持有者

可能使用合法密碼學簽章發布惡意套件。

因此：

$$
\text{Valid Signature}
\not\Rightarrow
\text{Safe Artifact}
$$

還需要：

- signer governance；
- key generation；
- package enablement；
- policy evaluation；
- dependency verification；
- transparency evidence；
- runtime authorization。

### 5.3 惡意或失控 Agent

可能：

- 擴大自身 Capability；
- 將 proposal 當成已提交；
- 繞過人工批准；
- 進入 executable Region；
- 呼叫網路或檔案能力；
- 將執行輸出直接寫回權威狀態。

### 5.4 惡意 Registry 或中間人

可能：

- 回傳錯誤 blob；
- 替換 tag；
- 重新導向至其他主機；
- 嘗試取得 credential；
- 回放舊 manifest；
- 提供與 digest 不符的內容。

### 5.5 惡意治理成員

可能：

- 偽造批准；
- 重複計票；
- 使用已停用身分；
- 以單一組織控制所有批准；
- 修改 proposal 後重用舊簽章；
- 將遠端決策強制套用本地。

### 5.6 惡意透明度服務或 Witness

可能：

- 分裂視圖；
- 隱藏事件；
- 簽署不同 checkpoint；
- 發送舊 sequence；
- 重放 gossip；
- 提供無法延伸的 checkpoint。

### 5.7 本地資料庫或檔案竄改者

可能直接修改：

- SQLite 資料；
- 安裝目錄；
- manifest；
- execution certificate；
- transparency entries。

CAIR 的雜湊與簽章可提供偵測能力，但若攻擊者同時掌握主機、資料庫、所有私鑰與執行環境，CAIR v1.0 不宣稱能提供硬體信任根等級的保護。

---

## 六、非目標與不成立假設

CAIR v1.0 不假設：

- 所有管理員都可信；
- 有效簽章等同安全內容；
- SQLite 可抵抗已取得 root 權限的攻擊者；
- process isolation 是敵意程式碼沙盒；
- 遠端服務一定可用；
- 時鐘永遠可信；
- 外部 OIDC identity 一定代表自然人；
- 多數票必然等同正確決策；
- CRDT 適合所有治理資料；
- transparency log 能單獨阻止惡意發布。

---

# 第三部分　安全架構

## 七、九層信任鏈

CAIR 的供應鏈信任鏈可表示為：

$$
B
\xrightarrow{H}
D
\xrightarrow{S}
\Sigma
\xrightarrow{K}
I
\xrightarrow{L}
\Lambda
\xrightarrow{G}
A
\xrightarrow{R}
E
\xrightarrow{X}
C_x
\xrightarrow{T}
C_t
$$

其中：

- $B$ ：artifact bytes；
- $D$ ：內容 digest；
- $\Sigma$ ：簽章；
- $I$ ：簽署者與金鑰身分；
- $\Lambda$ ：dependency lock；
- $A$ ：治理批准；
- $E$ ：執行授權；
- $C_x$ ：執行證書；
- $C_t$ ：透明度與歷史證據。

在工程上可簡化為：

```text
Artifact bytes
  → SHA-256 digest
  → signed Skill / Policy manifest
  → trusted signer generation
  → dependency lock
  → package enablement
  → governance policy
  → region and actor authorization
  → isolated execution
  → execution certificate
  → transparency / audit evidence
```

---

## 八、生成、提交與執行分離

CAIR 將控制權分為：

$$
\mathcal{C}
=
(C_g,C_v,C_c,C_x,C_r)
$$

其中：

- $C_g$ ：生成候選；
- $C_v$ ：驗證；
- $C_c$ ：提交；
- $C_x$ ：執行；
- $C_r$ ：撤銷或回滾。

AI 或 Agent 可以獲得 $C_g$ ，但不自動獲得其他權限。

安全不變量：

$$
C_g
\not\Rightarrow
C_c
$$

$$
C_c
\not\Rightarrow
C_x
$$

$$
C_x
\not\Rightarrow
C_g^{+}
$$

最後一式表示：能執行某項能力，不代表可以修改自己的能力定義或治理邊界。

---

## 九、Region 作為治理邊界

Region 不只是視覺分組，而是局部權限與風險邊界。

`RegionGovernance` 可指定：

- `execution_enabled`
- `allowed_skills`
- `allowed_capabilities`
- `denied_capabilities`
- `required_validators`
- `max_risk_level`
- `require_human_review`

Region policy：

```text
editable
read_only
ai_suggest
sandbox
executable
```

執行允許條件：

$$
\operatorname{Allow}
=
A_{\text{actor}}
\land
A_{\text{region}}
\land
A_{\text{skill}}
\land
A_{\text{risk}}
\land
A_{\text{review}}
$$

其中 $A_{\text{review}}$ 在需要人工批准的 Region 中不得由自主 Agent 自行滿足。

---

# 第四部分　簽章式 Skill 套件

## 十、`.cairskill` 套件格式

CAIR Skill 套件是受限制的 ZIP 容器。典型內容：

```text
manifest.json
signature.json
skill.json
handler.py
dependencies.lock.json
```

`SkillPackageManifest` v1.1 包含：

```text
schema_version
package_id
package_version
skill_file
entrypoint
signer_id
signer_key_id
dependency_lock_file
files
created_at
metadata
```

`files` 是：

$$
path
\mapsto
SHA256(fileBytes)
$$

安裝器必須：

1. 解析 manifest；
2. 驗證 manifest 簽章；
3. 確認 signer 與 key generation；
4. 檢查所有列出檔案的 digest；
5. 拒絕未列出檔案；
6. 拒絕缺失檔案；
7. 拒絕路徑穿越；
8. 拒絕符號連結；
9. 驗證 SkillDefinition；
10. 驗證 dependency lock；
11. 建立 InstalledSkillPackage；
12. 寫入透明度與治理稽核。

---

## 十一、套件三重啟用條件

套件簽章有效並不自動允許執行。

CAIR 的最低條件為：

$$
\text{SignatureValid}
\land
\text{SignerTrusted}
\land
\text{PackageEnabled}
$$

在有依賴的情況下：

$$
\land
\text{DependenciesSatisfied}
$$

在執行時：

$$
\land
\text{RegionAuthorized}
\land
\text{ActorAuthorized}
$$

因此，InstalledSkillPackage 分別保存：

- `signature_valid`
- `signer_trusted`
- `dependencies_satisfied`
- `enabled`

這些狀態不得被合併為一個不可解釋的總分。

---

## 十二、依賴鎖

`DependencyLock` 由多個 `LockedDependency` 構成：

```text
package_id
package_version
package_fingerprint
optional
metadata
```

必要依賴的安裝條件：

$$
\exists p:
\begin{cases}
p.id=d.id\\
p.version=d.version\\
p.fingerprint=d.fingerprint\\
p.enabled=true
\end{cases}
$$

精確指紋可防止：

- 相同版本號內容替換；
- Registry tag 漂移；
- 被重新發布的不同內容；
- 只驗證名稱與版本而忽略 artifact bytes。

CAIR v1.0 的依賴鎖是套件安裝時的內容綁定機制，但不等同完整軟體物料清單、漏洞資料庫或 SLSA provenance。

---

# 第五部分　簽署者與金鑰生命週期

## 十三、Signer Identity 與 Key Generation 分離

CAIR 分離：

- `TrustedSigner`
- `SignerKey`

TrustedSigner 表示持續身分；SignerKey 表示特定密碼學世代。

`SignerKey.status`：

```text
active
retired
revoked
```

其語義為：

### 13.1 active

- 可以驗證既有套件；
- 可以簽署新套件；
- 可以作為目前 active key。

### 13.2 retired

- 可以驗證歷史套件；
- 不應簽署新套件；
- 不代表歷史簽章失效。

### 13.3 revoked

- 表示金鑰不再可信；
- 使用該 key generation 的套件應被阻擋；
- 撤銷事件應寫入治理稽核與透明度日誌。

---

## 十四、雙簽金鑰輪替

`KeyRotationStatement` 包含：

```text
signer_id
old_key_id
new_key_id
new_public_key_b64
created_at
old_signature_b64
new_signature_b64
reason
```

其概念為：

$$
\sigma_{\text{old}}
=
\operatorname{Sign}_{K_{\text{old}}}(R)
$$

$$
\sigma_{\text{new}}
=
\operatorname{Sign}_{K_{\text{new}}}(R)
$$

雙簽能證明：

- 舊金鑰承認新金鑰；
- 新金鑰承認此輪替聲明；
- 兩個 key generation 被同一 rotation payload 綁定。

若舊金鑰已完全失陷，雙簽不能自動證明輪替安全。因此高風險環境仍應結合：

- 離線 root key；
- 多方批准；
- 獨立透明度見證；
- TUF 類角色分離；
- 硬體金鑰或 HSM。

---

## 十五、撤銷不是刪除

CAIR 不以刪除歷史金鑰取代撤銷。

$$
\operatorname{Revoke}(K)
\neq
\operatorname{Delete}(K)
$$

保留撤銷記錄的原因：

- 驗證歷史事件；
- 確認某套件使用哪一代金鑰；
- 追蹤事件發生時間；
- 檢查撤銷前後政策；
- 避免無法解釋的歷史斷裂。

---

# 第六部分　簽章式政策套件

## 十六、`.cairpolicy`

政策套件典型內容：

```text
manifest.json
signature.json
policies/*.json
```

`PolicyBundleManifest` v1.0 包含：

```text
bundle_id
bundle_version
signer_id
signer_key_id
policy_files
created_at
metadata
```

每個政策檔案均由 manifest 保存 SHA-256。

安裝器拒絕：

- 路徑穿越；
- 符號連結；
- 未列出檔案；
- 檔案遺失；
- digest 不符；
- signer 不可信；
- key generation 非 active；
- manifest 簽章無效；
- PolicyDocument Schema 無效。

政策本身也有供應鏈。因此：

$$
\text{Policy governs artifacts}
$$

但同時：

$$
\text{Policy artifact must be governed}
$$

---

## 十七、政策即程式

CAIR v1.0 支援：

- 內建 `cair-expr`；
- 外部 OPA／Rego 適配器。

PolicyDocument 包含：

```text
id
version
language
entrypoint
source
enabled
description
metadata
```

PolicyDecision：

```text
policy_id
allowed
status
reasons
evidence
```

其中 status：

```text
allowed
denied
unavailable
error
```

安全原則：

$$
\operatorname{Unavailable}
\not\Rightarrow
\operatorname{Allowed}
$$

尤其是高影響操作，外部 OPA 不存在、Rego 無法編譯、entrypoint 未定義或 evaluation error，都不應被降級為默認允許。

OPA 使用宣告式 Rego 對結構化資料進行政策判定。CAIR 將 OPA 保持為可替換適配器，而不把 Rego AST 寫入 CAIR 權威 IR。

---

# 第七部分　治理變更與多方批准

## 十八、治理變更提案

治理變更使用 `GovernanceChangeProposal`，而不是直接修改資料庫狀態。

其內容包括：

```text
id
author
reason
actions
approval_threshold
approval_policy
approvals
status
created_at
updated_at
applied_at
applied_by
result
```

可治理的 action 包括：

```text
signer.set_enabled
signer.key.rotate
signer.key.revoke
package.set_enabled
region.governance.update
policy.upsert
policy.set_enabled
witness.set_enabled
governance.member.set_enabled
```

治理提案具有穩定 digest：

$$
d_p
=
SHA256(
CanonicalProposalWithoutApprovals
)
$$

批准簽章必須綁定此 digest，避免：

1. 成員簽署原提案；
2. 攻擊者修改 action；
3. 重用舊簽章批准新內容。

---

## 十九、批准條件

CAIR 可同時要求：

$$
C_{\text{approval}}
=
C_{\text{signature}}
\land
C_{\text{threshold}}
\land
C_{\text{role}}
\land
C_{\text{organization}}
\land
C_{\text{member}}
$$

其中：

- 簽章有效；
- 達到批准數；
- 必要角色均被覆蓋；
- 達到最小獨立組織數；
- 成員位於 allowlist。

`GovernanceApprovalPolicy`：

```text
signature_required
required_roles
minimum_organizations
allowed_members
```

這防止「三個帳號實際上由同一人、同一組織或同一權限域控制」被當成真正的多方治理。

---

## 二十、重複與偽造批准

CAIR 必須拒絕：

- 同一成員重複計票；
- 停用成員；
- proposal digest 不符；
- key ID 不符；
- 簽章無效；
- 不在 allowlist；
- 角色資料與成員登錄不符；
- 未達組織多樣性。

多人批准並不證明決策正確，但能降低單一身分、單一帳號或單一金鑰直接改變安全邊界的機率。

---

# 第八部分　透明度日誌

## 二十一、Append-Only Hash Chain

每個 TransparencyLogEntry 包含：

```text
sequence
event_type
subject
actor
artifact_digest
payload_digest
previous_hash
entry_hash
created_at
details
```

其雜湊關係可表示為：

$$
h_i
=
H(
seq_i,
event_i,
subject_i,
actor_i,
artifact_i,
payload_i,
h_{i-1},
time_i
)
$$

驗證器檢查：

- sequence 連續；
- previous_hash 一致；
- entry_hash 可重算；
- checkpoint size 與 entries 數量一致；
- head hash 一致；
- Merkle root 一致。

Hash chain 提供篡改偵測，但若攻擊者可以重寫整個資料庫並重新產生所有 entries，單一節點自身無法證明舊歷史曾存在。因此還需要外部 checkpoint、witness 或公開透明度服務。

---

## 二十二、Checkpoint 與 Merkle Root

TransparencyCheckpoint：

```text
size
head_hash
merkle_root
created_at
```

Checkpoint 將某一時刻的日誌狀態壓縮為可見證物件：

$$
C_t
=
(size_t,head_t,root_t,time_t)
$$

Witness 對 checkpoint 簽章後，日誌操作者若想重寫歷史，必須同時欺騙或取代足夠多外部 witness。

---

## 二十三、與 Certificate Transparency 的關係

RFC 9162 描述 Certificate Transparency v2，利用可審計日誌、Merkle inclusion proof 與 consistency proof，使憑證簽發活動可被觀察與檢查。

CAIR 借用下列思想：

- append-only log；
- tree head／checkpoint；
- Merkle root；
- inclusion／consistency 概念；
- 外部 witness；
- split-view detection。

但 CAIR 的透明度事件是：

- Skill 套件；
- Policy 套件；
- signer 變更；
- governance proposal；
- key rotation／revocation；
- 遠端治理複製。

因此：

- CAIR log 不是 TLS Certificate Transparency Log；
- CAIR v1.0 不宣稱符合 RFC 9162；
- CAIR compact proof 使用 RFC 6962 風格 SHA-256 Merkle 算法；
- v1.0 proof 尚未通過獨立 CT conformance suite。

---

# 第九部分　Witness、Gossip 與一致性

## 二十四、Witness 身分

TransparencyWitness 包含：

```text
id
name
public_key_b64
key_id
organization
enabled
metadata
```

WitnessStatement 綁定：

```text
witness_id
witness_key_id
checkpoint
observed_at
signature_b64
metadata
```

Witness 的作用不是宣稱套件安全，而是聲明：

> 此 witness 在指定時間觀察到這個 checkpoint。

---

## 二十五、Witness Quorum

`WitnessQuorumPolicy` 支援：

```text
threshold
required_witness_ids
minimum_organizations
```

Quorum 成立條件：

$$
|W_{\text{valid}}|
\geq
q
$$

且：

$$
W_{\text{required}}
\subseteq
W_{\text{valid}}
$$

以及：

$$
|\operatorname{Organizations}(W_{\text{valid}})|
\geq
o_{\min}
$$

同一 witness 的重複聲明不得重複計票。

---

## 二十六、避免見證遞迴

Witness statement 不寫回它正在見證的同一份透明度日誌。

否則：

1. 日誌產生 checkpoint $C_1$ ；
2. Witness 簽署 $C_1$ ；
3. 將 statement 寫入日誌；
4. 日誌變成 $C_2$ ；
5. 原 statement 不再見證最新 checkpoint；
6. 需要再次簽署，形成無限遞迴。

CAIR 將 witness statement 保存為獨立治理資料。

---

## 二十七、Gossip Envelope

WitnessGossipEnvelope 包含：

```text
sender_id
sender_key_id
sequence
checkpoint
consistency_proof
statements
created_at
signature_b64
metadata
```

接收方檢查：

- sender 是否登錄；
- sender 是否啟用；
- key 是否相符；
- envelope 簽章；
- sequence 是否新；
- checkpoint 是否可接受；
- consistency proof；
- statements 是否有效。

這能偵測：

- 重放；
- 偽造；
- sequence 回退；
- 無法延伸的歷史；
- 部分 split view。

---

## 二十八、一致性證據

CAIR v0.8 曾使用完整舊前綴加新增 leaves 的可審計證據；v0.9 新增 compact consistency proof：

```text
algorithm = rfc6962-sha256
old_size
new_size
old_root
new_root
audit_path
```

其目標是證明：

$$
T_{\text{old}}
\preceq
T_{\text{new}}
$$

即新樹是舊樹的追加延伸，而不是重新排列或替換舊 leaves。

CAIR v1.0 的 compact proof 已通過自身性質與回歸測試，但尚未宣稱經第三方標準測試套件認證。

---

# 第十部分　OCI 分發邊界

## 二十九、內容與分發分離

OCI Distribution Specification 提供以 Registry API 分發內容的標準邊界。CAIR 使用 OCI 處理：

- artifact blob；
- manifest；
- tag／digest；
- push；
- pull；
- Bearer challenge；
- Registry credential；
- 本地 OCI Image Layout。

但：

$$
\text{Registry}
\neq
\text{CAIR Authoritative Repository}
$$

Registry 保存可攜 artifact；CAIR repository 保存權威程式、治理狀態與版本歷史。

---

## 三十、Digest 優先

OCIArtifactReference 包含：

```text
repository
digest
media_type
size
annotations
local_layout_path
registry_url
tag
manifest_digest
```

下載後必須重新計算 artifact digest：

$$
SHA256(downloadedBytes)
=
reference.digest
$$

Tag 只提供人類可讀選擇，不應作為最終完整性判準。

---

## 三十一、Registry 認證安全

CAIR v1.0 RemoteOCIRegistryBackend 支援：

- anonymous；
- basic；
- bearer；
- challenge。

Bearer challenge 流程：

1. Registry 回傳 `WWW-Authenticate: Bearer`；
2. 解析 `realm`、`service`、`scope`；
3. 向 token service 取得 token；
4. 使用 Bearer token 重試原請求；
5. 對相同 challenge 使用執行期 cache。

安全要求：

- Registry credential 不持久化於 Registry config；
- Basic credential 只發送至預期 token realm；
- 跨主機 redirect 必須移除 `Authorization`；
- TLS 驗證預設啟用；
- timeout 必須有上限；
- token 不應寫入治理稽核明文。

---

## 三十二、OCI 符合性邊界

截至 2026-07，OCI 已維護 Runtime、Image 與 Distribution 三類規格，Distribution Specification 亦持續維護符合性測試。

CAIR v1.0：

- 實作 Distribution API 的必要子集；
- 支援本地 OCI Image Layout；
- 完成本地相容 HTTP Registry 驗收；
- 不宣稱通過完整 OCI conformance suite；
- 不宣稱所有公有 Registry 的 token exchange 與擴展均已驗證。

---

# 第十一部分　Sigstore、Fulcio 與 Rekor

## 三十三、Sigstore 信任模型

Sigstore 將：

- OIDC identity；
- Fulcio 短效簽署憑證；
- Rekor 透明度紀錄；
- Sigstore trust root；
- Cosign verification；
- verification bundle；

組成 artifact verification 鏈。

Fulcio 將短效簽署公鑰與 OIDC identity 綁定；Rekor 保存可公開查詢的簽署事件；Sigstore bundle 保存完成驗證所需的簽章內容與 verification material。

---

## 三十四、CAIR Sigstore 適配

CAIR v1.0 提供：

- `SigstoreBundle` 資料模型；
- `SigstoreTrustPolicy`；
- `CosignSigstoreBundleVerifier`；
- certificate issuer regexp；
- certificate identity regexp；
- transparency log 要求；
- certificate transparency 要求；
- signed entry timestamp 要求；
- Rekor entry lookup；
- Fulcio trust bundle fetch。

CAIR 以外部 `cosign verify-blob --bundle` 作為完整驗證適配器，而不是自行重寫所有 X.509、Fulcio、Rekor 與 bundle 驗證邏輯。

---

## 三十五、誠實的驗證狀態

SigstoreVerificationResult：

```text
verified
unavailable
rejected
```

安全原則：

- cosign 不存在 → `unavailable`；
- bundle 缺失 → `unavailable` 或 `rejected`，依請求契約；
- artifact digest 不符 → `rejected`；
- identity／issuer policy 不符 → `rejected`；
- 無法取得 trust material → 不得 `verified`。

$$
\operatorname{MissingEvidence}
\Rightarrow
\operatorname{NotVerified}
$$

---

## 三十六、Rekor 與 Fulcio 子邊界

CAIR RemoteRekorClient 可：

- 查詢 entry；
- 對支援的 hashedrekord 比對 artifact SHA-256；
- 取得 log index；
- 取得 integrated time；
- 取得 log ID。

CAIR RemoteFulcioClient 可：

- 取得 trust bundle；
- 擷取 PEM certificate material。

但 CAIR v1.0 不自行宣稱：

- 完整 Rekor inclusion proof 驗證；
- signed tree head 完整驗證；
- X.509 path validation；
- Fulcio CT log 完整驗證；
- 公開 Sigstore instance 的線上端到端驗收。

---

# 第十二部分　SLSA、in-toto 與 TUF 對照

## 三十七、SLSA

截至 2026-07，SLSA v1.2 是已批准規格，包含 Build 與 Source tracks，並定義 provenance 等 attestation 格式。

SLSA 關心：

- artifact 從何而來；
- 由何種 build process 產生；
- 使用哪些 inputs；
- builder 的隔離與可信程度；
- provenance 是否可驗證。

CAIR 已具備：

- artifact digest；
- package manifest；
- dependency lock；
- signer identity；
- execution certificate；
- OCI reference；
- Sigstore adapter；
- transparency evidence。

但 CAIR v1.0 尚未完整提供：

- 標準 SLSA provenance predicate；
- 對 build platform 的正式 SLSA level assessment；
- hermetic build 保證；
- source track 完整證據；
- SLSA 認證或 badge。

因此：

$$
\text{CAIR supply-chain evidence}
\neq
\text{SLSA conformance claim}
$$

---

## 三十八、in-toto

in-toto 的目標是描述供應鏈中：

- 執行了哪些步驟；
- 由誰執行；
- 使用哪些材料；
- 產生哪些產品；
- 順序是否符合預期。

in-toto Attestation Framework 使用 Statement 將 subject digest 與 predicate type／predicate 綁定。

CAIR 的：

- ValidationCertificate；
- ExecutionCertificate；
- GovernanceAuditEvent；
- Skill package manifest；
- Policy bundle manifest；
- VerifiableGovernanceSnapshot；

都可被映射為未來的 in-toto predicate 或 statement subject。

但 v1.0 並未將這些證書序列化為正式 in-toto Statement v1，因此不能宣稱為 in-toto compliant attestation。

---

## 三十九、TUF

TUF 保護軟體更新系統，即使部分 repository 或 signing key 被攻陷，也能透過角色分離、門檻簽章、版本與到期資訊等機制降低風險。

CAIR 與 TUF 相近的概念：

- signer 與 key generation；
- key rotation；
- key revocation；
- threshold approval；
- package digest；
- metadata version；
- 信任根演化。

CAIR 尚未實作完整 TUF：

- root／targets／snapshot／timestamp 四角色；
- TUF metadata format；
- freeze attack 防護；
- rollback attack 完整規則；
- consistent snapshots；
- TUF client update workflow。

CAIR 的簽署者治理不能替代 TUF repository。未來若 CAIR 用於大規模更新分發，TUF 應作為外部更新信任層，而不是重新發明所有 TUF 安全屬性。

截至本文件日期，TUF 規格頁列出的最新穩定修訂為 v1.0.33。

---

## 四十、外部框架對照矩陣

| 外部框架 | 主要問題 | CAIR 已有能力 | v1.0 尚未宣稱 |
|---|---|---|---|
| OCI Distribution | artifact 如何分發 | blob、manifest、push/pull、Bearer challenge、digest | 完整 conformance |
| Sigstore | artifact 由誰簽署、簽署事件是否可查 | bundle model、cosign adapter、issuer/identity policy | 自行完整 PKI／Rekor 驗證 |
| SLSA 1.2 | artifact 如何由可信 build/source 產生 | digest、lock、execution evidence | SLSA level |
| in-toto | 供應鏈步驟、材料與產品 | 可映射證書與事件 | Statement／layout 正式符合 |
| TUF | 安全更新與 key compromise | rotation、revocation、threshold | TUF repository/client |
| OPA/Rego | 政策如何獨立評估 | adapter、PolicyDecision | OPA 本身可用性保證 |
| RFC 9162 | 公開追加日誌如何稽核 | Merkle、checkpoint、witness、consistency | CT protocol conformance |
| NIST SSDF | 安全開發實務 | 測試、版本、供應鏈與操作文件 | 組織級完整 SSDF 評估 |

---

# 第十三部分　分散式治理安全

## 四十一、簽章式治理複製

GovernanceReplicationRecord 包含：

```text
node_id
node_key_id
sequence
previous_hash
event_type
subject
payload
created_at
record_hash
signature_b64
```

安全條件：

- node 必須登錄且啟用；
- key ID 必須相符；
- record hash 必須可重算；
- signature 必須有效；
- sequence 必須連續；
- previous hash 必須銜接；
- fork 必須被偵測。

GovernanceReplicationBatch 綁定：

- source node；
- start／end sequence；
- records；
- batch digest。

---

## 四十二、遠端決策非本地副作用

CAIR 的核心分散式安全原則：

$$
\operatorname{VerifyRemoteDecision}
\not\Rightarrow
\operatorname{ExecuteLocalAction}
$$

接收節點只物化唯讀狀態，例如：

- 遠端 package 已停用；
- 遠端 signer 已撤銷；
- 遠端 policy 已更新；
- 遠端 proposal 已套用。

本地節點仍需：

- 驗證本地政策；
- 檢查本地信任根；
- 決定是否採納；
- 建立本地治理提案；
- 留下本地稽核。

這可防止一個被入侵的遠端 authority 直接控制所有 replica 的高影響操作。

---

## 四十三、遠端節點授權

`RemoteNodeAuthorization` 綁定：

```text
subject_type
subject_id
allowed_actions
key_id
organization
not_before
expires_at
enabled
```

遠端訊息除密碼學簽章外，還必須滿足：

- subject 授權存在；
- 當前時間在有效範圍；
- key ID 符合；
- action 被允許；
- 授權未停用。

有效簽章只證明「持有某私鑰」，不代表「此金鑰目前被允許執行這個動作」。

---

## 四十四、Anti-Entropy

AntiEntropyPeerState 保存：

```text
peer_id
channel
last_sequence
last_checkpoint_size
last_success_at
next_due_at
failure_count
last_error
enabled
```

同步失敗使用有上限的指數退避，避免：

- 故障節點造成緊密重試；
- 外部服務被流量放大；
- 日誌被錯誤淹沒；
- 網路分區時資源耗盡。

排程由外部 systemd timer、CronJob 或 sidecar 觸發，不在主服務中隱藏常駐執行緒。

---

## 四十五、CRDT 邊界

CAIR 提供簽章式 LWW-map Governance CRDT。

衝突順序：

$$
\max(
Lamport,
nodeID,
eventID
)
$$

CRDT 適合：

- 可覆寫設定；
- 標籤；
- 低風險物化狀態；
- 最終一致視圖。

CRDT 不適合：

- 金鑰撤銷；
- 一次性授權；
- 資產轉移；
- 唯一所有權；
- 不可逆實體操作；
- 必須全序的治理決定。

這些操作應使用治理 proposal、門檻簽章或外部共識。

---

## 四十六、共識適配器

CAIR 的 `local-quorum` 只回答：

$$
yesVotes
\geq
requiredVotes
$$

它沒有提供：

- leader election；
- replicated log；
- fault-tolerant total order；
- linearizability；
- Byzantine fault tolerance。

`external-consensus` 適配器的目的，是讓真正需要共識的系統接入既有協議，而不將簡單門檻判定包裝成共識。

---

## 四十七、可驗證快照

VerifiableGovernanceSnapshot 包含：

```text
snapshot_id
source_node_id
source_key_id
sequence
state
state_digest
event_count
event_hashes
merkle_root
created_at
signature_b64
metadata
```

驗證條件：

$$
SHA256(CanonicalState)
=
stateDigest
$$

$$
Merkle(eventHashes)
=
merkleRoot
$$

$$
Verify_{nodeKey}(snapshotPayload,signature)
=
true
$$

快照證明內容與簽署者，但不單獨證明此快照是全網唯一或最新狀態。需要搭配：

- checkpoint；
- sequence；
- witness；
- anti-entropy；
- 本地 policy；
- 外部共識。

---

# 第十四部分　執行安全

## 四十八、Skill Definition

SkillDefinition 包含：

- input schema；
- output schema；
- capabilities；
- permission template；
- validators；
- failure policy；
- execution spec；
- package metadata。

Skill 不是只有 entrypoint。它是一個受治理能力契約。

---

## 四十九、執行前檢查

執行器至少檢查：

1. Skill 是否存在且啟用；
2. package 是否啟用；
3. signature_valid；
4. signer_trusted；
5. dependencies_satisfied；
6. signer key 是否未撤銷；
7. input JSON Schema；
8. actor Capability；
9. Region policy；
10. allowed／denied capabilities；
11. risk level；
12. human approval；
13. backend availability；
14. timeout 與資源限制。

任一必要條件失敗，必須產生拒絕結果，而不是部分執行。

---

## 五十、Process Isolation

`process-isolated` 使用獨立 `python -I` 子程序執行 Skill worker。

它可以降低：

- 主程序 namespace 污染；
- FastAPI 執行緒內 fork 風險；
- 部分 import path 影響；
- timeout 無法中止；
- worker crash 影響主服務。

但它不是敵意程式安全邊界，無法可靠阻止：

- 系統呼叫；
- kernel exploit；
- 同使用者檔案存取；
- 本機網路；
- fork bomb；
- 作業系統層旁路。

---

## 五十一、容器與 microVM

不可信第三方程式應使用：

- 非 root 容器；
- read-only filesystem；
- capability drop；
- seccomp；
- AppArmor／SELinux；
- network deny-by-default；
- 資源 quota；
- ephemeral workspace；
- 獨立 secrets；
- microVM；
- 獨立主機。

CAIR 的 ExecutionBackendDescriptor 支援：

```text
process
container
microvm
```

v1.0 完成 Docker backend 抽象與部署配置，但封頂環境沒有 Docker／Podman，因此不宣稱實際映像建置已驗收。

---

## 五十二、執行證書

SkillExecutionCertificate 應回答：

- 執行哪一個 Skill 版本；
- 來自哪一個 package；
- 使用哪一個 signer key；
- 在哪一個 program／Region；
- 由哪一個 actor；
- 使用哪一個 backend；
- input／output fingerprint；
- 限制與政策；
- status；
- elapsed time；
- result hash。

執行證書：

$$
C_x
\neq
P^{\ast}
$$

它是執行證據，不是新的權威程式版本。輸出若要修改權威狀態，仍需建立 ChangeProposal。

---

# 第十五部分　安全不變量

## 五十三、內容完整性不變量

$$
Installed(B)
\Rightarrow
SHA256(B_i)
=
Manifest.files[i]
$$

---

## 五十四、簽章綁定不變量

$$
Verify(K_g,Manifest,\sigma)
=
true
$$

其中 $K_g$ 必須是 signer 的精確 key generation。

---

## 五十五、撤銷優先不變量

$$
KeyStatus(K_g)
=
revoked
\Rightarrow
Executable(Package_g)
=
false
$$

即使歷史簽章密碼學上仍可驗證。

---

## 五十六、依賴精確不變量

$$
RequiredDependency(d)
\Rightarrow
Installed(d.id,d.version,d.fingerprint)
$$

---

## 五十七、治理批准不變量

$$
Applied(Change)
\Rightarrow
Satisfied(ApprovalPolicy)
$$

---

## 五十八、遠端非副作用不變量

$$
Accepted(RemoteRecord)
\not\Rightarrow
Applied(LocalAction)
$$

---

## 五十九、誠實降級不變量

$$
VerifierUnavailable
\Rightarrow
Status\neq verified
$$

---

## 六十、執行輸出隔離不變量

$$
ExecutionOutput
\not\Rightarrow
AuthoritativeMutation
$$

---

# 第十六部分　攻擊與防護對照

## 六十一、威脅矩陣

| 攻擊 | CAIR 防護 | 剩餘風險 |
|---|---|---|
| 修改套件檔案 | manifest SHA-256 | manifest 與 key 同時被控制 |
| 增加隱藏檔案 | 拒絕未列出檔案 | 安全但危險的合法內容 |
| 路徑穿越 | 安裝器路徑檢查 | 解壓函式或平台差異漏洞 |
| 符號連結逃逸 | 拒絕 symlink | 特殊檔案格式旁路 |
| 偽造 signer | Ed25519 驗證 | 私鑰失竊 |
| 舊 key 發布新套件 | key generation／active 狀態 | 管理員錯誤重新啟用 |
| 撤銷後繼續執行 | 執行前查 key status | 本地狀態未同步 |
| 相同版本替換內容 | package fingerprint | 使用者只依 tag 操作 |
| 單一治理帳號控制 | threshold、role、organization | 多帳號共謀 |
| 修改 proposal 後重用批准 | proposal digest 簽章 | canonicalization 實作錯誤 |
| 透明度歷史改寫 | hash chain、Merkle、witness | 所有 witness 共謀 |
| Registry 回傳錯誤內容 | digest 重算 | 上游 reference 本身惡意 |
| Credential 洩漏至 redirect | 跨主機移除 Authorization | 同主機惡意 endpoint |
| 外部驗證器缺失 | `unavailable` fail closed | 操作者手動繞過 |
| Agent 自主擴權 | proposal／governance separation | 管理政策配置過寬 |
| 遠端節點控制本地 | read-only materialization | 本地自動採納政策設計不當 |
| Process sandbox 逃逸 | 文件明示限制、強後端抽象 | 未部署容器／microVM |
| CRDT 錯用於撤銷 | 明確資料類型邊界 | 實作者忽略限制 |

---

# 第十七部分　操作生命週期

## 六十二、Signer 建立

1. 離線或受控環境產生 Ed25519 key；
2. 建立 signer identity；
3. 登錄 public key generation；
4. 由治理提案啟用；
5. 寫入 audit 與 transparency log；
6. 分發 public trust material；
7. 保存私鑰於安全儲存。

私鑰不得放入：

- CAIR repository；
- 套件；
- Registry config；
- 日誌；
- demo output；
- Git repository。

---

## 六十三、套件發布

1. 建立 SkillDefinition；
2. 鎖定依賴；
3. 建立 manifest；
4. 計算所有檔案 digest；
5. 使用精確 signer key 簽署；
6. 產生 `.cairskill`；
7. 選擇性產生 Sigstore bundle；
8. 推送 OCI Registry；
9. 建立透明度紀錄；
10. 由治理程序批准啟用。

---

## 六十四、套件安裝

1. 以 digest 取得 artifact；
2. 重算 SHA-256；
3. 驗證 ZIP 安全；
4. 驗證 manifest；
5. 驗證 Ed25519；
6. 查 signer 與 key status；
7. 驗證 dependency lock；
8. 驗證 Skill Schema；
9. 選擇性驗證 Sigstore；
10. 安裝但可維持 disabled；
11. 建立治理 proposal；
12. 經批准後 enabled。

---

## 六十五、金鑰輪替

1. 產生新 key；
2. 建立雙簽 rotation statement；
3. 驗證舊、新簽章；
4. 以治理提案套用；
5. 新 key 設為 active；
6. 舊 key 設為 retired；
7. 發布透明度紀錄；
8. 更新外部 trust material；
9. 監控仍使用舊 key 的發布流程。

---

## 六十六、金鑰撤銷

1. 建立 revoke proposal；
2. 記錄原因與影響範圍；
3. 取得必要多方批准；
4. key 設為 revoked；
5. 找出所有關聯套件；
6. 阻擋執行；
7. 發布透明度與 witness checkpoint；
8. 更新遠端節點；
9. 評估是否需要重新簽署與重新發布。

---

## 六十七、事件處理

供應鏈事件發生時，應保存：

- first observed time；
- affected package／version／fingerprint；
- signer／key generation；
- dependency graph；
- execution history；
- governance proposals；
- transparency sequence；
- witness statements；
- remediation；
- new package fingerprints；
- revoked credentials；
- local adoption status。

不可只刪除受影響套件，因為刪除會破壞調查與歷史可解釋性。

---

# 第十八部分　符合性分級

## 六十八、CAIR Package Security Profile

實作若宣稱 `CAIR-Package-Security-1.0`，必須：

- 驗證 manifest signature；
- 驗證所有 file digests；
- 拒絕未列出檔案；
- 拒絕路徑穿越與 symlink；
- 綁定 signer key generation；
- 支援 active／retired／revoked；
- 驗證 dependency lock；
- 支援 package enabled 狀態。

---

## 六十九、CAIR Governance Profile

實作若宣稱 `CAIR-Governance-1.0`，必須：

- 以 proposal 修改治理；
- 綁定 proposal digest；
- 驗證 signed approval；
- 拒絕重複批准；
- 支援 threshold；
- 支援 role requirement；
- 支援 organization diversity；
- 保存 audit history；
- 套用前執行 policy evaluation。

---

## 七十、CAIR Transparency Profile

實作若宣稱 `CAIR-Transparency-1.0`，必須：

- append-only entry sequence；
- previous-hash chain；
- 可重算 entry hash；
- checkpoint；
- Merkle root；
- chain verification；
- witness statement；
- quorum evaluation；
- consistency evidence；
- 不將 witness statement 寫回被見證日誌。

---

## 七十一、CAIR Distributed Governance Profile

實作若宣稱 `CAIR-Distributed-Governance-1.0`，必須：

- 簽章 replication record；
- sequence 與 previous hash；
- fork detection；
- remote node authorization；
- 不自動執行本地副作用；
- 提供 anti-entropy cursor；
- 支援可驗證 snapshot；
- 明示 CRDT 與 consensus 邊界。

---

## 七十二、CAIR Execution Security Profile

實作若宣稱 `CAIR-Execution-Security-1.0`，必須：

- 驗證 input／output Schema；
- 檢查 actor Capability；
- 檢查 Region policy；
- 檢查 Skill requirements；
- 檢查 risk level；
- 支援 timeout；
- 產生 execution certificate；
- 不將執行輸出直接寫回權威程式；
- 明確聲明 execution backend 的 isolation 等級。

---

# 第十九部分　v1.0 邊界

## 七十三、已完成能力

CAIR v1.0 已完成：

- Ed25519 Skill／Policy 套件；
- signer identity 與 key generation；
- rotation／retirement／revocation；
- dependency lock；
- package governance；
- multi-party approval；
- role／organization threshold；
- cair-expr；
- OPA adapter；
- transparency hash chain；
- Merkle checkpoint；
- witness quorum；
- gossip；
- compact consistency proof；
- OCI local／remote adapter；
- Registry Bearer challenge；
- Sigstore／Rekor／Fulcio adapter；
- governance replication；
- anti-entropy；
- LWW governance CRDT；
- external consensus boundary；
- verifiable snapshot；
- Region／Capability 執行治理；
- process／container／microVM backend abstraction；
- execution certificate；
- audit persistence。

---

## 七十四、未完成或未宣稱能力

CAIR v1.0 不宣稱：

1. TUF repository／client；
2. SLSA level；
3. in-toto Statement 符合性；
4. OCI conformance；
5. Sigstore 公開 instance 完整線上驗收；
6. 自行完整 X.509 path validation；
7. Rekor inclusion proof 與 signed tree head 完整驗證；
8. RFC 9162 conformance；
9. 公開 witness gossip network；
10. Raft／Paxos／BFT；
11. 分散式交易；
12. HSM／TPM 硬體信任根；
13. 任意敵意程式碼沙盒；
14. 組織級 NIST SSDF 完整符合性評估；
15. 大規模 production penetration test。

---

# 第二十部分　結論

CAIR 治理與供應鏈安全模型的核心，不是增加更多「安全功能」清單，而是拒絕將不同安全問題壓縮成一個不可解釋的可信標記。

其總體模型為：

$$
\boxed{
\text{可執行能力}
=
\text{內容}
+
\text{來源}
+
\text{簽章}
+
\text{金鑰狀態}
+
\text{依賴}
+
\text{政策}
+
\text{多方治理}
+
\text{區域授權}
+
\text{隔離執行}
+
\text{透明度證據}
}
$$

在這個模型中：

- 套件簽章有效，不代表內容安全；
- signer 可信，不代表每一個 key generation 都仍有效；
- 套件安裝成功，不代表套件已獲准執行；
- 遠端治理決策有效，不代表本地必須執行；
- transparency log 可驗證，不代表事件本身正確；
- 多方批准成立，不代表不存在共謀；
- process isolation 存在，不代表可以執行敵意程式；
- 外部 verifier 不可用，不代表可以跳過驗證；
- 執行成功，不代表輸出可以直接改變權威狀態。

CAIR v1.0 所建立的，是一條不可被單一角色、單一模型、單一套件、單一金鑰或單一遠端節點輕易跨越的控制鏈：

$$
\text{定義能力}
\rightarrow
\text{封裝內容}
\rightarrow
\text{證明來源}
\rightarrow
\text{驗證依賴}
\rightarrow
\text{治理批准}
\rightarrow
\text{授權執行}
\rightarrow
\text{保存證書}
\rightarrow
\text{公開可檢查歷史}
$$

因此，CAIR 的治理不只是限制 AI，也不只是保護軟體套件。它要保護的是更基本的系統主權：

> 任何主體都不能只因為「能生成」「能簽署」「能傳輸」「能批准」或「能執行」其中一項能力，就獨自取得改變整個權威計算系統的完整控制權。

---

# 附錄 A　核心安全狀態

## A.1 Signer Key

```text
active
retired
revoked
```

## A.2 Package Install

```text
installed
rejected
```

## A.3 Policy Decision

```text
allowed
denied
unavailable
error
```

## A.4 Sigstore Verification

```text
verified
unavailable
rejected
```

## A.5 Governance Proposal

```text
pending
approved
rejected
applied
```

## A.6 Replication Result

```text
accepted
rejected
fork_detected
```

## A.7 Anti-Entropy Result

```text
synchronized
no_change
rejected
unavailable
not_due
```

## A.8 Consensus Decision

```text
accepted
rejected
unavailable
pending
```

---

# 附錄 B　核心安全公式

### B.1 套件執行

$$
X_p
=
S_v
\land
I_t
\land
P_e
\land
D_s
\land
G_a
\land
R_a
$$

### B.2 多方治理

$$
G_a
=
Sig
\land
Threshold
\land
Roles
\land
Organizations
\land
Members
$$

### B.3 透明度鏈

$$
h_i
=
H(m_i,h_{i-1})
$$

### B.4 遠端治理

$$
RemoteVerified
\not\Rightarrow
LocalApplied
$$

### B.5 誠實降級

$$
EvidenceMissing
\Rightarrow
Verified=false
$$

---

# 附錄 C　官方標準參考

- Open Container Initiative, *Distribution Specification*。
- Sigstore, *Security Model*、*Sigstore Bundle Format*、*Fulcio*、*Rekor* 與 *Cosign Verification*。
- SLSA Specification v1.2。
- in-toto Specification v1.0。
- in-toto Attestation Framework v1.0。
- The Update Framework Specification v1.0.33。
- Open Policy Agent 與 Rego 官方文件。
- RFC 9162, *Certificate Transparency Version 2.0*。
- NIST SP 800-218, *Secure Software Development Framework Version 1.1*。
- NIST SP 800-218 Rev. 1 Initial Public Draft, *SSDF Version 1.2*。
