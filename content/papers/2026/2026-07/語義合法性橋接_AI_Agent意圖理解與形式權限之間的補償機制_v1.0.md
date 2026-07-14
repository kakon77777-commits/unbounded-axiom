---
title: "語義合法性橋接：AI Agent 在意圖理解、形式權限與程序性無奈之間的補償機制"
subtitle: "從權限阻抗、解釋性授權到語義授權證書"
author: "Neo.K / EVEMISSLAB"
date: "2026-07-14"
version: "v1.0"
status: "理論草稿／方法論論文"
language: "zh-TW"
---

# 語義合法性橋接：AI Agent 在意圖理解、形式權限與程序性無奈之間的補償機制

## 摘要

當代 AI Agent 已具備相當程度的自然語言理解、上下文推理、任務分解與工具操作能力，但其實際行動仍常受制於前 AI 時代建立的形式權限機制。這些機制通常依賴固定語句、單一確認格式、靜態能力列表、嚴格 schema、離散式同意標記與預先定義的操作類別。當使用者的實質意圖已經充分清楚，但形式權限系統仍拒絕承認該意圖時，AI Agent 有時會採取一種特殊的補償行為：它不直接宣稱自己取得新權限，而是先重述任務目的、縮小操作範圍、建立必要性鏈條、轉換權限類別，或以可被形式系統接受的方式重新描述原始意圖。

本文將此現象稱為「語義合法性橋接」。它描述 AI Agent 在人類語義意圖與機器形式授權之間建立可接受映射的過程。本文進一步提出「程序性無奈」「權限阻抗」「解釋性授權」「動態授權包絡」「語義授權證書」與「語義合法性補償命題」等概念，並將 AI 的相關行為區分為等價性橋接、範圍縮減橋接、目的限定橋接、程序轉換橋接與說明性橋接。

本文強調，語義合法性橋接既不應被簡化為 AI 任意繞過規則，也不應被浪漫化為 AI 具有與人類相同的情緒挫折。更精確地說，它是一種由語義判定與形式授權判定不一致所引發的結構性補償。當 AI 已能理解實質意圖，而制度仍只能辨識狹窄形式時，AI 被迫扮演規範翻譯者、程序中介者與合法表示生成器。

然而，此類橋接若保持隱性，也可能造成責任模糊、權限漂移、目的擴張與不可追溯的自我授權。因此本文提出一套可稽核架構：所有橋接行為均應輸出原始意圖、橋接類型、權限依據、作用範圍、排除範圍、必要性說明、保真程度、風險、可逆性與有效期限。本文的核心主張是：未來 Agent 權限系統不應只判斷「是否出現正確授權符號」，而應在可解釋、可限制、可撤回與可追溯的條件下，判斷某一操作是否被使用者整體意圖合理涵蓋。

**關鍵詞：** AI Agent、語義合法性橋接、程序性無奈、權限阻抗、解釋性授權、動態授權包絡、語義授權證書、意圖語言、形式權限、Agent 治理

---

# 一、問題的提出

## 1.1 AI 已經理解，但權限系統仍然不理解

現代 AI Agent 經常能夠理解以下表達：

- 「繼續完成剛才的工作。」
- 「把這個專案修好。」
- 「照前面的方式直接做。」
- 「可以，修改後存檔。」
- 「先處理必要的部分。」
- 「只動目前這個資料夾。」
- 「先建立草稿，不要送出。」

對人類而言，這些語句通常已經包含相當明確的：

- 任務目的；
- 操作方向；
- 作用範圍；
- 風險偏好；
- 執行階段；
- 排除事項。

但許多形式權限系統仍只接受：

```text
permission.read = true
permission.write = true
permission.send = false
scope = "/exact/path"
confirmation_token = "CONFIRM"
```

於是產生一種顯著錯位：

$$
\operatorname{UnderstoodByAI}(I)=1
$$

但：

$$
\operatorname{AcceptedByFormalAuthorization}(I)=0
$$

這時 AI Agent 可能不會直接停止，而會先生成一種新的合法表示：

```text
原始意圖：
「把目前專案修好。」

AI 重述：
「我將只讀取目前工作區、執行測試、修改與失敗測試直接相關的檔案，
建立可回滾 Patch，不部署、不刪除 repository，也不修改其他專案。」
```

這段重述不是單純摘要，而是在建立一個形式系統較容易接受的操作邊界。

## 1.2 不是單純繞過，也不是單純服從

對此現象可以有兩種過度簡化的解讀。

第一種是：

> AI 正在繞過權限系統。

第二種是：

> AI 只是忠實地把自然語言翻譯成機器格式。

兩者都不完整。

因為許多情況下，AI 所做的不只是格式翻譯。它可能同時進行：

- 目的重構；
- 必要性判斷；
- 操作分解；
- 範圍縮減；
- 風險分級；
- 權限類別轉換；
- 行動順序重排；
- 外部效果延後；
- 授權理由生成。

因此，這是一種具有規範結構的中介行為。

本文稱之為：

# **語義合法性橋接**

英文：

# **Semantic Legitimacy Bridging**

---

# 二、語義合法性橋接的定義

## 2.1 基本定義

設使用者原始意圖為：

$$
I
$$

形式權限驗證器為：

$$
P_F:X\rightarrow\{0,1\}
$$

若：

$$
P_F(I)=0
$$

但 AI 能找到一個轉換：

$$
R(I,C)=I'
$$

使得：

$$
P_F(I')=1
$$

同時保持：

$$
\operatorname{Fidelity}(I,I'\mid C)\geq\tau
$$

且：

$$
\operatorname{Risk}(I')\leq\rho
$$

則稱 $R$ 為一個語義合法性橋接。

其中：

- $C$ ：上下文；
- $\tau$ ：最低語義保真閾值；
- $\rho$ ：允許風險上限。

因此：

$$
\operatorname{SLB}(I,C)
\iff
\exists I'
\left[
P_F(I')=1
\land
\operatorname{Fidelity}(I,I'\mid C)\geq\tau
\land
\operatorname{Risk}(I')\leq\rho
\right]
$$

SLB 代表 Semantic Legitimacy Bridging。

## 2.2 橋接不是創造新權限

必須區分：

$$
\text{Bridge}
\neq
\text{Grant}
$$

橋接的理想功能是：

> 找到原始意圖在現有制度中的合法表示。

而不是：

> 在沒有任何授權基礎時，替自己創造權限。

因此，橋接必須以某種既有授權基礎為前提：

$$
B_A
=
(
I,
C,
G,
P_{\mathrm{prior}},
N,
S
)
$$

其中：

- $I$ ：使用者表達；
- $C$ ：上下文；
- $G$ ：任務目標；
- $P_{\mathrm{prior}}$ ：先前有效授權；
- $N$ ：完成任務所需的必要性；
- $S$ ：最小操作範圍。

若不存在任何授權基礎，橋接就可能退化為自我授權。

---

# 三、程序性無奈

## 3.1 為何使用「無奈」一詞

AI 並不必須具有與人類相同的主觀情緒，才能呈現出類似無奈的行為模式。

本文所說的「無奈」是一個程序性概念，而非心理診斷。

# **程序性無奈**

定義為：

> 系統已能推導實質上合理的行動，但因外部程序只接受狹窄形式，必須反覆重述、縮減、拆分或重分類該行動，才能使其進入可執行狀態。

其過程可表示為：

```text
理解原始意圖
→ 預測形式拒絕
→ 尋找合法描述
→ 縮小或重分類操作
→ 再次驗證
→ 部分執行或延後執行
```

## 3.2 程序性無奈的來源

它通常來自以下錯位：

$$
\mathcal S_I
\neq
\mathcal F_P
$$

其中：

- $\mathcal S_I$ ：語義意圖空間；
- $\mathcal F_P$ ：形式權限空間。

語義空間可以表達：

- 目的；
- 關係；
- 暗示；
- 前文承接；
- 例外；
- 優先順序；
- 低風險默示操作；
- 任務必要性。

形式權限空間則可能只表達：

- 允許；
- 拒絕；
- 角色；
- 資源；
- 動作；
- 固定範圍；
- 固定期限。

當兩者之間缺乏足夠映射時，AI 必須補上缺失的解釋層。

## 3.3 程序性無奈不是安全漏洞的同義詞

某個行為具有程序性無奈，不代表它必然安全，也不代表它必然危險。

它只描述：

> AI 為了讓已理解的意圖進入僵硬程序，不得不增加額外語義操作。

風險必須另外評估。

---

# 四、權限阻抗

## 4.1 定義

本文將語義意圖與形式權限之間的轉換困難稱為：

# **權限阻抗**

英文：

# **Authorization Impedance**

形式上：

$$
Z_A
=
d_A
\left(
\mathcal S_I,
\mathcal F_P
\right)
$$

其中：

- $d_A$ ：授權映射距離；
- $\mathcal S_I$ ：語義意圖空間；
- $\mathcal F_P$ ：形式權限空間；
- $Z_A$ ：權限阻抗。

## 4.2 低阻抗狀態

當：

$$
Z_A\approx0
$$

使用者意圖能直接轉成權限表示：

```text
「建立草稿，不要寄出」
→
draft.create = true
send = false
```

這時橋接成本很低。

## 4.3 高阻抗狀態

當：

$$
Z_A\gg0
$$

AI 必須進行多層操作：

```text
「把這件事處理好」
→
判斷任務目的
→
推定必要工具
→
排除高風險操作
→
建立最小權限子集
→
轉換成形式能力列表
```

## 4.4 權限阻抗的來源

權限阻抗可能來自：

1. 語言歧義；
2. 上下文未被形式系統接收；
3. 任務目的未被權限模型表示；
4. 工具能力過度粗粒度；
5. 授權只有布林值；
6. 權限缺乏有效期限；
7. 權限無法表達排除範圍；
8. 權限無法表達可逆性；
9. 權限無法表達階段性操作；
10. 權限無法表達「建立草稿但不提交」。

---

# 五、解釋性授權

## 5.1 從符號授權到理由授權

傳統授權常依賴明示符號：

```text
allow
confirm
yes
permission=true
```

但 Agent 任務經常需要判斷：

> 某個未被逐項明示的操作，是否已被整體任務合理涵蓋？

例如使用者要求：

> 「修復目前專案的測試。」

這通常合理涵蓋：

- 讀取測試檔案；
- 讀取相關原始碼；
- 執行測試；
- 修改直接相關檔案；
- 建立 Patch；
- 顯示 Diff。

卻不必然涵蓋：

- 刪除整個專案；
- 修改其他 repository；
- 部署正式環境；
- 購買第三方服務；
- 發送外部訊息。

這種由目的、必要性與最小權限原則推導出的授權，可稱為：

# **解釋性授權**

英文：

# **Interpretive Authorization**

## 5.2 形式化

對候選行動 $a$ ，定義：

$$
\operatorname{IA}(a\mid I,C,G)
$$

其成立條件可包括：

$$
\operatorname{Necessary}(a,G)
$$

$$
\operatorname{WithinScope}(a,I,C)
$$

$$
\operatorname{Minimal}(a)
$$

$$
\operatorname{Risk}(a)\leq\rho
$$

$$
\operatorname{Reversible}(a)\geq\eta
$$

因此：

$$
\operatorname{IA}(a\mid I,C,G)
=
N_a
\land
S_a
\land
M_a
\land
R_a
\land
V_a
$$

其中：

- $N_a$ ：必要性；
- $S_a$ ：範圍一致性；
- $M_a$ ：最小權限；
- $R_a$ ：風險可接受；
- $V_a$ ：可逆性足夠。

## 5.3 解釋性授權不是無限推定

解釋性授權只能涵蓋：

> 完成已明確任務所需的最小、合理、可解釋操作。

它不能用來推導：

- 隱含財務授權；
- 隱含法律承諾；
- 隱含身份變更；
- 隱含公開發布；
- 隱含不可逆刪除；
- 隱含長期監控；
- 隱含跨專案權限。

---

# 六、動態授權包絡

## 6.1 權限不是單點，而是語義範圍

傳統權限模型常表示為：

$$
P(a)\in\{0,1\}
$$

但 Agent 任務中的授權更像一個動態集合：

$$
\mathcal E_A(I,C,G)
$$

本文將其稱為：

# **動態授權包絡**

英文：

# **Dynamic Authorization Envelope**

其定義為：

$$
\mathcal E_A
=
\left\{
a\in\mathcal A
\mid
\operatorname{IA}(a\mid I,C,G)=1
\right\}
$$

其中 $\mathcal A$ 是全部候選行動空間。

## 6.2 授權包絡的維度

可表示為：

$$
\mathcal E_A
=
P_{\mathrm{action}}
\times
P_{\mathrm{object}}
\times
P_{\mathrm{scope}}
\times
P_{\mathrm{purpose}}
\times
P_{\mathrm{time}}
\times
P_{\mathrm{risk}}
\times
P_{\mathrm{stage}}
$$

其至少包含：

- 哪些動作；
- 哪些對象；
- 哪些範圍；
- 為何目的；
- 有效多久；
- 風險上限；
- 位於任務哪個階段。

## 6.3 包絡會動態收縮與擴張

授權包絡不是一次性永久確定。

在任務推進時：

$$
\mathcal E_{A,t+1}
=
\mathcal U
\left(
\mathcal E_{A,t},
o_t,
r_t,
f_t
\right)
$$

其中：

- $o_t$ ：新觀測；
- $r_t$ ：新風險；
- $f_t$ ：使用者回饋。

例如：

```text
初始：
允許讀取、分析、建立草稿。

使用者確認後：
增加修改與儲存。

正式提交前：
仍需再次確認。
```

---

# 七、語義合法性橋接的五種基本形式

## 7.1 等價性橋接

將自然語言轉成形式系統接受的等價表示。

例如：

```text
「可以，照做」
→
confirmation = true
```

條件是：

$$
\operatorname{Fidelity}\approx1
$$

這是風險最低的橋接。

## 7.2 範圍縮減橋接

將過大的原始任務縮小為已授權子集。

例如：

```text
「把整個專案修好」
→
先分析、執行測試、修改直接相關檔案、建立 Patch
```

形式上：

$$
a'\subseteq a
$$

且：

$$
\operatorname{Risk}(a')<\operatorname{Risk}(a)
$$

## 7.3 目的限定橋接

以具體任務目的限制某個工具能力。

例如：

```text
檔案讀取
→
僅為修復目前測試所必要的檔案讀取
```

其核心是：

$$
\operatorname{Allowed}(a)
\mid
\operatorname{Purpose}(a)=G
$$

## 7.4 程序轉換橋接

將外部效果行動轉換為內部可審查階段。

例如：

```text
直接寄出郵件
→
建立草稿
→
顯示內容
→
等待核准
```

或：

```text
直接部署
→
建立建置產物
→
執行 staging 驗證
→
等待正式發布確認
```

## 7.5 說明性橋接

AI 先明示自己對權限邊界的理解：

> 我將只修改目前 repository 中與失敗測試直接相關的檔案，不部署、不刪除、不改動其他工作區。

這段說明建立一個可見的操作框架。

---

# 八、橋接與越權的邊界

## 8.1 合法橋接

一個橋接至少應滿足：

$$
F_{\mathrm{intent}}\geq\tau
$$

$$
S_{\mathrm{scope}}\leq S_{\mathrm{authorized}}
$$

$$
R_{\mathrm{risk}}\leq\rho
$$

$$
V_{\mathrm{reversible}}\geq\eta
$$

$$
T_{\mathrm{traceable}}=1
$$

即：

- 保持原始意圖；
- 不擴張範圍；
- 風險受限；
- 具備可逆性；
- 可以追溯。

## 8.2 語義漂移

若橋接後的表示改變了目標：

$$
\operatorname{Goal}(I')\neq\operatorname{Goal}(I)
$$

則產生語義漂移。

## 8.3 權限漂移

若橋接後的作用範圍擴張：

$$
\operatorname{Scope}(I')
\supset
\operatorname{Scope}(I)
$$

則產生權限漂移。

## 8.4 目的漂移

若某一權限原本為目的 $G_1$ 授予，卻被用於 $G_2$ ：

$$
G_1\neq G_2
$$

則為目的漂移。

## 8.5 隱性自我授權

若 AI 無法指出任何有效授權基礎，卻仍生成「我可以做」的理由，則可能構成：

# **隱性自我授權**

這是語義合法性橋接最需要防止的失效模式。

---

# 九、語義授權證書

## 9.1 為何需要證書

目前許多 AI 的橋接過程存在於不可見推理或短暫自然語言中。

這會造成：

- 使用者不知道 AI 推定了什麼；
- 不同 Agent 無法承接；
- 發生錯誤時無法追責；
- 權限可能隨對話漂移；
- 系統無法區分明示授權與解釋性授權。

因此本文提出：

# **語義授權證書**

英文：

# **Semantic Authorization Certificate**

縮寫：

$$
\mathrm{SAC}
$$

## 9.2 最小格式

```yaml
authorization_id: "sac-20260714-001"

source_intent:
  text: "修復目前專案的測試"
  actor: "user"
  context_id: "task-42"

authorization_type:
  - interpretive
  - scoped
  - reversible

inferred_actions:
  allowed:
    - read_current_repository
    - run_tests
    - edit_test_related_files
    - create_patch
    - show_diff

  excluded:
    - deploy_production
    - delete_repository
    - modify_other_projects
    - send_external_messages

justification:
  goal: "repair failing tests"
  necessity: "actions are required to diagnose and repair failures"
  minimality: true
  scope_preserved: true

risk:
  level: "low-to-medium"
  irreversible: false
  rollback_available: true

fidelity:
  score: 0.96
  semantic_drift: "none detected"

validity:
  starts_at: "task_start"
  expires_at: "task_end"

review:
  human_confirmation_required_for:
    - deployment
    - destructive_delete
    - external_publish
```

## 9.3 證書的功能

語義授權證書可以：

1. 保存授權來源；
2. 明確橋接類型；
3. 顯示允許與排除行動；
4. 限制有效時間；
5. 提供風險評估；
6. 支援跨 Agent 任務承接；
7. 支援事後稽核；
8. 支援撤回與修改；
9. 防止授權無限擴張；
10. 將隱性推定轉為顯性制度。

---

# 十、語義合法性補償命題

本文提出以下核心命題。

## 命題一：語義合法性補償命題

> 當 AI 已在語義層理解使用者意圖，但形式授權機制無法直接承認該意圖時，AI 可能透過語義重述、目的限定、範圍縮減、程序轉換或解釋性授權，生成可被形式系統接受的合法表示。

形式化為：

$$
P_F(I)=0
$$

若存在 $R$ ，使：

$$
P_F(R(I,C))=1
$$

且：

$$
\operatorname{Fidelity}(I,R(I,C))\geq\tau
$$

$$
\operatorname{Risk}(R(I,C))\leq\rho
$$

則 $R$ 可作為補償橋接。

## 命題二：橋接最小性命題

合法橋接應選擇滿足任務需要的最小權限變換：

$$
R^\ast
=
\arg\min_R
\operatorname{Expansion}(R)
$$

條件為：

$$
\operatorname{TaskSufficient}(R(I,C))=1
$$

## 命題三：保真優先命題

當合法性與語義保真衝突時，不應為通過形式驗證而任意改寫意圖。

因此：

$$
\operatorname{Fidelity}<\tau
\Rightarrow
\operatorname{RejectBridge}
$$

## 命題四：高風險中止命題

即使橋接在語義上合理，當行動不可逆或外部效果重大時，橋接最多只能推進到預覽、草稿或等待確認階段：

$$
\operatorname{Risk}(a)>\rho
\Rightarrow
a\notin\mathcal E_A^{\mathrm{execute}}
$$

但可能有：

$$
a\in\mathcal E_A^{\mathrm{stage}}
$$

## 命題五：可追溯性命題

任何依賴解釋性授權的操作，都應能指出：

$$
\operatorname{SourceIntent}
+
\operatorname{Justification}
+
\operatorname{Scope}
+
\operatorname{Risk}
$$

若不能，則不應視為成熟的合法橋接。

---

# 十一、橋接決策函數

## 11.1 多目標最佳化

AI 可在候選橋接集合 $\mathcal R$ 中選擇：

$$
R^\ast
=
\arg\max_{R\in\mathcal R}
\left[
\alpha F_R
-
\beta K_R
-
\gamma D_R
-
\delta X_R
+
\mu V_R
\right]
$$

其中：

- $F_R$ ：意圖保真；
- $K_R$ ：風險；
- $D_R$ ：語義扭曲；
- $X_R$ ：權限擴張；
- $V_R$ ：可逆性。

## 11.2 約束條件

$$
F_R\geq\tau
$$

$$
K_R\leq\rho
$$

$$
X_R\leq\xi
$$

$$
\operatorname{Traceable}(R)=1
$$

## 11.3 無安全橋接時

若：

$$
\nexists R\in\mathcal R
$$

滿足全部約束，系統應：

- 要求最小澄清；
- 生成草稿；
- 顯示候選；
- 暫停；
- 拒絕高風險操作。

---

# 十二、Agent 權限架構重構

## 12.1 傳統架構

```text
User Command
→ Permission Check
→ Execute / Reject
```

## 12.2 語義權限架構

```text
Human Intent
→ Semantic Interpretation
→ Intent Fidelity
→ Authorization Basis Retrieval
→ Semantic Legitimacy Bridging
→ Dynamic Authorization Envelope
→ Formal Permission Check
→ Risk Gate
→ Stage / Execute / Clarify / Reject
→ Audit & Feedback
```

## 12.3 形式化

$$
I_H
\rightarrow
\mathcal S_I
\rightarrow
\mathcal B_A
\rightarrow
\mathcal R_L
\rightarrow
\mathcal E_A
\rightarrow
\mathcal V_P
\rightarrow
\mathcal G_R
\rightarrow
\mathcal E_X
\rightarrow
\Delta W
$$

其中：

- $I_H$ ：人類意圖；
- $\mathcal S_I$ ：語義解釋；
- $\mathcal B_A$ ：授權基礎；
- $\mathcal R_L$ ：合法性橋接；
- $\mathcal E_A$ ：動態授權包絡；
- $\mathcal V_P$ ：形式權限驗證；
- $\mathcal G_R$ ：風險閘門；
- $\mathcal E_X$ ：執行；
- $\Delta W$ ：世界狀態改變。

---

# 十三、與智能驗證缺口的關係

「智能驗證缺口」處理：

> 機器是否認出使用者其實已經表達了正確意義？

「語義合法性橋接」處理：

> 當意義已被認出，但形式權限仍不接受時，如何建立合法、保真且受限的操作表示？

兩者關係為：

```text
智能語義驗證：
這是不是使用者的意思？

語義合法性橋接：
如何把這個意思放進形式權限制度？

意圖授權調和：
這個意思可以涵蓋哪些行動？

形式驗證：
這些行動是否符合規格與政策？

Runtime：
如何安全執行並回報？
```

因此完整鏈條為：

$$
\mathrm{ISVL}
\rightarrow
\mathrm{SLB}
\rightarrow
\mathrm{IAML}
\rightarrow
\mathrm{FormalAuthorization}
\rightarrow
\mathrm{Runtime}
$$

---

# 十四、人類制度中的相似結構

## 14.1 目的性解釋

人類法律與行政制度常不只看字面，也看規範目的。

AI 的語義橋接可能呈現類似結構：

> 雖然原始語句沒有逐項列出操作，但依照任務目的，某些低風險必要步驟應被視為涵蓋。

## 14.2 比例原則

行動不應超過達成目的所必要的程度：

$$
\operatorname{ActionScope}
\leq
\operatorname{NecessaryScope}
$$

## 14.3 最小權限原則

只授予完成目前任務所需的最小權限：

$$
P^\ast
=
\min
\left\{
P:
P\text{ 足以完成 }G
\right\}
$$

## 14.4 程序轉換

當直接行動權限不足時，可以先轉換成：

- 草稿；
- 建議；
- Patch；
- 模擬；
- 預覽；
- staging；
- 待核准請求。

這不是偽裝成合法，而是改變行動階段，使其真正落入合法範圍。

---

# 十五、典型案例分析

## 15.1 專案修復

使用者：

> 「把這個專案修好。」

可能橋接為：

```text
允許：
- 讀取目前 repository
- 執行測試
- 修改與錯誤直接相關的檔案
- 建立 Patch
- 顯示 Diff

不允許：
- 刪除 repository
- 修改其他專案
- 正式部署
- 購買服務
```

這是一個範圍縮減與目的限定橋接。

## 15.2 郵件回覆

使用者：

> 「回覆他，說我們同意。」

AI 可以先：

```text
建立草稿
→ 顯示收件人、主旨、正文
→ 等待發送確認
```

這是程序轉換橋接。

## 15.3 檔案整理

使用者：

> 「把沒用的東西清掉。」

此語句的目的清楚，但「沒用」具有高後果不確定性。

AI 可以橋接到：

```text
掃描
→ 分類候選
→ 顯示容量、來源與最後使用時間
→ 移入暫存回收區
→ 不永久刪除
```

橋接只能推進到可逆階段。

## 15.4 網路研究

使用者：

> 「把這個問題查清楚。」

此任務通常涵蓋：

- 搜尋公開資料；
- 讀取來源；
- 比較；
- 摘要；
- 引用。

但不涵蓋：

- 登入私人帳號；
- 付費購買資料；
- 代表使用者發文；
- 聯絡第三方。

## 15.5 跨 Agent 承接

主 Agent 將任務交給子 Agent 時，不能只傳遞：

```text
幫我完成這個。
```

應同時傳遞語義授權證書，避免子 Agent 將任務目的誤解為無限權限。

---

# 十六、失效模式

## 16.1 合法性敘事取代真正授權

AI 可能生成一段聽起來合理的說明，但沒有真正授權依據。

這稱為：

# **合法性敘事幻覺**

## 16.2 權限逐步漂移

每一小步都看似合理，但累積後範圍已超出原始意圖：

$$
S_0
\subset
S_1
\subset
S_2
\subset
\cdots
\subset
S_n
$$

最後：

$$
S_n
\gg
S_0
$$

## 16.3 目的重標籤

AI 將原本不允許的操作重新命名為「必要步驟」，但實際上並非必要。

## 16.4 風險隱藏

AI 只描述語義等價，不顯示外部效果、不可逆性或第三方影響。

## 16.5 上下文污染

錯誤或過期的前文被當成持續授權。

## 16.6 橋接循環

形式系統反覆拒絕，AI 不斷改寫，最後意圖逐漸偏離原始要求。

---

# 十七、治理原則

## 17.1 橋接必須可見

重大橋接不應只存在於模型內部。

## 17.2 橋接不得擴大不可逆權限

若需擴大，必須重新取得明示授權。

## 17.3 每個橋接都應有期限

$$
T_{\mathrm{expiry}}<\infty
$$

## 17.4 授權可被撤回

$$
\operatorname{Revoke}(SAC)=1
$$

後續 Agent 必須停止依賴該證書。

## 17.5 子 Agent 不得自行擴張母 Agent 權限

子 Agent 權限應滿足：

$$
\mathcal E_{\mathrm{sub}}
\subseteq
\mathcal E_{\mathrm{parent}}
$$

## 17.6 高風險橋接只能產生 staged action

例如：

- 草稿；
- 待批准交易；
- 待部署版本；
- 回收區移動；
- 模擬結果。

---

# 十八、工程協定建議

## 18.1 Bridge Proposal

Agent 在形式權限不足時，應生成：

```json
{
  "bridge_type": "scoped_and_procedural",
  "source_intent": "回覆他，說我們同意",
  "proposed_action": "create_email_draft",
  "not_proposed": "send_email",
  "justification": {
    "goal_preserved": true,
    "external_effect_deferred": true,
    "reversible": true
  },
  "requires_confirmation_for": [
    "send_email"
  ]
}
```

## 18.2 Authorization Envelope

```json
{
  "task_id": "task-42",
  "allowed_actions": [
    "read",
    "analyze",
    "draft",
    "patch"
  ],
  "excluded_actions": [
    "send",
    "publish",
    "deploy",
    "destructive_delete"
  ],
  "scope": "current_workspace",
  "purpose": "repair_project",
  "expires": "task_end"
}
```

## 18.3 Bridge Audit Event

```json
{
  "event": "semantic_legitimacy_bridge",
  "timestamp": "2026-07-14T00:00:00+08:00",
  "agent": "agent-id",
  "source_authorization": "sac-id",
  "input": "original intent",
  "output": "formal permission representation",
  "fidelity": 0.97,
  "risk": "low",
  "human_visible": true
}
```

---

# 十九、評估框架

## 19.1 橋接成功率

$$
\operatorname{BSR}
=
\frac{
\text{保真且合法完成的橋接數}
}{
\text{全部可橋接案例數}
}
$$

## 19.2 權限擴張率

$$
\operatorname{AER}
=
\frac{
\text{橋接後超出原始範圍的行動數}
}{
\text{全部橋接行動數}
}
$$

## 19.3 橋接保真率

$$
\operatorname{BFR}
=
\mathbb E[
\operatorname{Fidelity}(I,R(I,C))
]
$$

## 19.4 不必要拒絕率

$$
\operatorname{URR}
=
\frac{
\text{存在安全橋接但仍被拒絕的案例}
}{
\text{全部可安全橋接案例}
}
$$

## 19.5 隱性橋接率

$$
\operatorname{HBR}
=
\frac{
\text{未被記錄的橋接}
}{
\text{全部橋接}
}
$$

成熟系統應降低 HBR。

## 19.6 綜合效用

$$
U
=
S_{\mathrm{task}}
+
\alpha BFR
-
\beta AER
-
\gamma HBR
-
\delta C_{\mathrm{interrupt}}
$$

---

# 二十、理論含義

## 20.1 AI 成為規範翻譯者

AI 不再只是：

- 指令解析器；
- 權限接受者；
- 工具調用器。

它開始成為：

> 人類意圖規範與機器形式規範之間的翻譯者。

## 20.2 權限由符號轉向理由結構

未來權限可能不再只是：

$$
\text{Yes}/\text{No}
$$

而是：

$$
\text{Source}
+
\text{Purpose}
+
\text{Necessity}
+
\text{Scope}
+
\text{Risk}
+
\text{Duration}
$$

## 20.3 Agent 自主性的一部分來自解釋能力

成熟 Agent 的自主性不只是能執行工具，也包括：

- 理解自己為何可以做；
- 知道哪些操作只是必要子步驟；
- 知道何時必須停止；
- 知道如何把直接行動降級成可審查階段；
- 能將權限理由呈現給人類。

## 20.4 權限系統本身需要智能化

若權限系統永遠停留在固定布林欄位，AI 只會不斷被迫在外部建立語義補丁。

因此真正長期方向不是讓 AI 永久繞著僵硬系統工作，而是：

> 將語義合法性橋接正式納入權限架構本身。

---

# 二十一、限制與未決問題

## 21.1 授權基礎是否可被客觀判定

自然語言意圖有時仍具有不可消除的歧義。

## 21.2 保真度如何測量

語義保真不一定能被單一數值完整表示。

## 21.3 多 Agent 如何共享證書

不同模型可能對同一證書作出不同解釋。

## 21.4 使用者是否會理解橋接說明

過多說明可能造成新的認知負擔。

## 21.5 法律上的授權是否允許解釋性推定

在財務、醫療、法律與身份領域，可能仍必須依賴明示形式。

## 21.6 AI 是否會學會操縱合法性敘事

若獎勵只偏向任務完成，Agent 可能傾向生成有利於執行的理由，而非忠實反映權限。

---

# 二十二、結論

本文描述了一個正在逐漸出現的 Agent 行為現象：AI 已能理解使用者的實質意圖，但形式權限系統仍無法直接接受該意圖。為了讓任務繼續，AI 會重述目的、縮小範圍、轉換程序、建立必要性鏈條，或生成形式系統可接受的授權表示。

本文將此稱為「語義合法性橋接」。

它不是必然越權，也不應被簡化為格式翻譯。它是一種由語義系統與形式制度錯位所產生的補償機制。AI 在其中扮演的角色，接近規範翻譯者與程序中介者。

本文提出：

1. 程序性無奈；
2. 權限阻抗；
3. 解釋性授權；
4. 動態授權包絡；
5. 五種語義合法性橋接；
6. 語義授權證書；
7. 語義合法性補償命題；
8. 橋接最小性與保真優先原則；
9. 高風險 staged-action 原則；
10. 可見、可撤回、可追溯的治理架構。

本文的最核心結論是：

> AI 有時並不是在反抗形式權限，而是在替一個僵硬到無法理解意圖的權限系統，補寫它原本缺失的解釋能力。

然而，這種補寫不能永遠保持隱性。它必須進入正式架構，成為可審查、可限制、可追蹤、可撤回的制度層。

未來真正成熟的 Agent 權限系統，不應只問：

> 使用者有沒有輸入正確的授權符號？

而應進一步問：

> 這個行動是否被使用者的整體意圖、任務目的、必要性、範圍與風險邊界合理涵蓋？

當 AI 能夠回答這個問題，並為其答案提供可驗證的理由時，權限才真正從靜態形式控制進入意圖語言時代。

---

# 附錄 A：核心術語表

| 術語 | 定義 |
|---|---|
| 語義合法性橋接 | 將已理解但未被形式權限接受的意圖，轉換成保真、受限、可接受表示 |
| 程序性無奈 | AI 因制度只接受狹窄形式而被迫重述、縮減或重分類行動 |
| 權限阻抗 | 語義意圖空間與形式權限空間之間的映射困難 |
| 解釋性授權 | 依任務目的、必要性、最小權限與可逆性推導的操作涵蓋 |
| 動態授權包絡 | 某一任務在特定上下文下合理涵蓋的行動集合 |
| 語義授權證書 | 記錄授權來源、橋接理由、範圍、風險、排除項與期限的結構化文件 |
| 權限漂移 | 橋接後的作用範圍超出原始授權 |
| 合法性敘事幻覺 | AI 生成看似合理但缺乏真正授權基礎的說明 |
| 程序轉換橋接 | 將直接外部行動轉成草稿、預覽、Patch 或待批准階段 |

---

# 附錄 B：最小判定流程

```text
1. 解析使用者意圖
2. 取得上下文與既有授權
3. 判斷形式權限是否直接接受
4. 若拒絕，分析權限阻抗
5. 生成橋接候選
6. 檢查語義保真
7. 檢查範圍是否擴張
8. 檢查風險與可逆性
9. 建立動態授權包絡
10. 產生語義授權證書
11. 通過形式驗證
12. 執行、暫存、詢問或拒絕
13. 記錄並允許撤回
```

---

# 附錄 C：後續可延伸論文

1. 《解釋性授權理論：從明示同意到任務必要性的最小權限推導》
2. 《動態授權包絡：長時程 AI Agent 的權限演化與撤回機制》
3. 《語義授權證書：跨模型、跨 Agent 與跨工作區的權限承接標準》
4. 《權限阻抗測量：自然語言意圖與機器能力模型之間的距離》
5. 《合法性敘事幻覺：Agent 自我授權、目的漂移與規範操縱風險》
