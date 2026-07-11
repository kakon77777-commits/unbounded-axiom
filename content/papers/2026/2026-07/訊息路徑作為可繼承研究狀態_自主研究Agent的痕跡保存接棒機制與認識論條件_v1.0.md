# 訊息路徑作為可繼承研究狀態

## ——自主研究 Agent 的痕跡保存、接棒機制與認識論條件

**作者：Neo.K（理論構想與研究方向）／Aletheia（協作形式化與系統整理）**  
**版本：v1.0 初版系統理論稿**  
**日期：2026-07-11**  
**系列定位：三篇論文之三——研究路徑的保存、解碼與接棒**

---

## 重要聲明

本文提出的是一個研究狀態保存與接棒框架，而不是宣稱任何自然語言對話都能自動成為可靠的科學記錄。

本文不主張：

1. 只要保存聊天紀錄，就必然可以完整恢復研究狀態；
2. 下一個 Agent 只需閱讀摘要，就能無損接續；
3. 所有研究意圖、隱性直覺與未表達知識都能被文字完全編碼；
4. 對話順序本身足以證明其中內容真實；
5. 任意 Agent 都能正確理解前一個 Agent 的符號、假設與錯誤；
6. 研究接棒可以取代獨立驗證；
7. 路徑越長就必然越有價值。

本文主張的是一個條件命題：

$$
\boxed{
\text{若訊息路徑、計算工件、依賴關係與狀態標記足夠完整，}
}
$$

$$
\boxed{
\text{則後續 Agent 可以近似恢復前一研究狀態，並從該位置接續。}
}
$$

這裡的「近似恢復」不是神秘記憶，而是可形式化的解碼與驗證程序。

---

## 摘要

自主研究 Agent 若要真正持續工作，就不能只在每次對話中重新解題。它必須保存的不只是最終答案，而是整個研究狀態：目前目標、已知結果、被否定的方法族、尚未完成的證明義務、計算輸出、版本差異、外部知識來源，以及每個結論的可信度與新穎性標記。

本文提出「訊息路徑可繼承性」框架。令：

$$
\Pi_T
=
(m_0,m_1,\dots,m_T)
$$

為研究期間的訊息與工具紀錄序列。本文不把 $\Pi_T$ 本身直接視為研究狀態，而是定義一個狀態抽取算子：

$$
\operatorname{Extract}(\Pi_T)
=
\mathcal R_T,
$$

其中：

$$
\mathcal R_T
=
(
P_T,
K_T,
M_T,
F_T,
C_T,
D_T,
O_T,
V_T,
A_T
).
$$

各分量分別表示：

- 當前目標；
- 已吸收知識；
- 候選中介命題；
- 失敗與反例；
- 計算結果；
- 依賴圖；
- 未完成證明義務；
- 版本狀態；
- 可執行工件。

後續 Agent $A'$ 透過：

$$
\widehat{\mathcal S}_T
=
\operatorname{Decode}_{A'}(\mathcal R_T)
$$

恢復一個近似研究狀態。若：

$$
d(
\widehat{\mathcal S}_T,
\mathcal S_T
)
\le\varepsilon,
$$

且關鍵義務均被重新驗證，則可執行：

$$
\operatorname{Resume}
(
A',
\mathcal R_T
)
\rightarrow
\mathcal S_{T+1}.
$$

本文提出五項可繼承條件：

1. **狀態充分性**：關鍵研究變量已被保存；
2. **路徑有序性**：命題、錯誤與修正保持時序；
3. **依賴可追蹤性**：結論可追溯至前提與工件；
4. **工件可重驗性**：程式、輸出與證書可重新執行；
5. **不確定性可見性**：已知、候選、反例、重建與新穎性未決被區分。

本文同時提出「研究狀態包」與「接棒協議」：

$$
\mathfrak P_T
=
(
\text{State},
\text{Trace},
\text{Artifacts},
\text{Dependencies},
\text{Checksums},
\text{Open Gaps}
).
$$

只保留最終結論會造成「結果壓縮錯誤」；只保留完整對話則會造成「訊息淹沒」。因此真正有效的保存方式，是同時保留：

$$
\boxed{
\text{原始路徑}
+
\text{結構化狀態}
+
\text{可執行工件}.
}
$$

本文以穩定 Kneser 圖的多輪研究為例，展示一條包含重建、錯誤一般化、方法族否證、漏洞修正、有限核心、精確證書與星剝離的研究路徑，如何被重新編碼成可供下一個 Agent 接續的狀態。

本文的核心命題是：

$$
\boxed{
\text{研究不只是一個答案，而是一條可保存、可驗證、可接續的狀態路徑。}
}
$$

**關鍵詞：** 研究 Agent、訊息路徑、研究狀態、接棒、可繼承性、依賴圖、版本控制、可執行工件、長程記憶、認識論

---

# 1. 問題：為什麼答案不等於研究狀態？

## 1.1 最終答案丟失了什麼？

設一項研究最後得到：

$$
P.
$$

若只保存 $P$ ，通常會丟失：

- 哪些假設被使用；
- 哪些路線已被排除；
- 哪些中介命題仍未完全證明；
- 哪些結果依賴有限計算；
- 哪些計算可重跑；
- 哪些步驟只是文獻重建；
- 哪些新穎性仍未確認；
- 哪些錯誤已被發現並修正。

所以：

$$
\boxed{
\text{Final Result}
\neq
\text{Research State}.
}
$$

---

## 1.2 完整對話也不等於研究狀態

另一方面，直接保存全部訊息：

$$
\Pi_T
=
(m_0,\dots,m_T)
$$

也不夠。

因為完整對話包含：

- 重複敘述；
- 暫時命名；
- 被放棄的符號；
- 未標記的錯誤；
- 情緒與修辭；
- 工具輸出的片段；
- 後來已被修正的結論。

所以：

$$
\boxed{
\text{Raw Trace}
\neq
\text{Decoded State}.
}
$$

---

# 2. 三層保存模型

本文提出三層保存結構。

## 2.1 第一層：原始路徑

$$
\Pi_T
=
(m_0,m_1,\dots,m_T).
$$

它保存：

- 時序；
- 原始措辭；
- 當輪錯誤；
- 修正發生的位置；
- 工具呼叫與輸出。

第一層的優勢是不可逆資訊最多。

缺點是噪音大、成本高、難以直接接棒。

---

## 2.2 第二層：結構化研究狀態

定義：

$$
\mathcal R_T
=
(
P_T,
K_T,
M_T,
F_T,
C_T,
D_T,
O_T,
V_T,
A_T
).
$$

其中：

### 目標集合

$$
P_T
=
\{P_T^{(1)},\dots,P_T^{(u)}\}.
$$

### 已知知識

$$
K_T
=
K_T^{\mathrm{internal}}
\cup
K_T^{\mathrm{external}}
\cup
K_T^{\mathrm{computed}}.
$$

### 候選中介命題

$$
M_T
=
\{M_1,\dots,M_v\}.
$$

### 失敗集合

$$
F_T
=
\{F_1,\dots,F_w\}.
$$

### 計算結果

$$
C_T
=
\{C_1,\dots,C_z\}.
$$

### 依賴圖

$$
D_T
=
(V_D,E_D).
$$

### 未完成義務

$$
O_T
=
\{O_1,\dots,O_h\}.
$$

### 版本紀錄

$$
V_T.
$$

### 工件集合

$$
A_T
=
\{\text{code},\text{proof},\text{certificate},\text{data}\}.
$$

---

## 2.3 第三層：接棒摘要

接棒 Agent 不應先讀完整歷史，而應先接收最小充分狀態：

$$
\Sigma_T
=
(
P_T,
M_T^{\mathrm{active}},
F_T^{\mathrm{critical}},
O_T,
A_T^{\mathrm{required}},
D_T^{\mathrm{active}}
).
$$

它是一個低成本入口。

若出現歧義，再回溯：

$$
\Sigma_T
\rightarrow
\mathcal R_T
\rightarrow
\Pi_T.
$$

因此正確順序是：

$$
\boxed{
\text{Summary first}
\rightarrow
\text{State second}
\rightarrow
\text{Raw trace on demand}.
}
$$

---

# 3. 訊息路徑可繼承性假說

## 3.1 基本形式

令真實研究狀態為：

$$
\mathcal S_T.
$$

由路徑抽取：

$$
\mathcal R_T
=
\operatorname{Extract}(\Pi_T).
$$

新 Agent $A'$ 解碼：

$$
\widehat{\mathcal S}_T
=
\operatorname{Decode}_{A'}(\mathcal R_T).
$$

若存在距離函數：

$$
d(
\widehat{\mathcal S}_T,
\mathcal S_T
)
\le
\varepsilon,
$$

則稱該研究狀態在誤差 $\varepsilon$ 下可繼承。

---

## 3.2 距離不是單一數值

研究狀態距離應拆成：

$$
d
=
w_Pd_P
+
w_Kd_K
+
w_Md_M
+
w_Fd_F
+
w_Od_O
+
w_Ad_A.
$$

其中：

- $d_P$ ：目標理解差異；
- $d_K$ ：知識庫差異；
- $d_M$ ：中介命題差異；
- $d_F$ ：失敗紀錄差異；
- $d_O$ ：證明義務差異；
- $d_A$ ：工件可用性差異。

對研究接棒而言， $d_F$ 與 $d_O$ 往往比文字措辭差異更重要。

---

## 3.3 最小可繼承條件

存在閾值：

$$
\varepsilon^\ast,
$$

若：

$$
d\le\varepsilon^\ast,
$$

則新 Agent 能避免：

- 重複已知失敗；
- 誤把候選命題當定理；
- 遺漏尚未完成的回填；
- 重做已知文獻；
- 使用過期版本。

---

# 4. 為什麼失敗必須被保存？

## 4.1 只保存成功會產生假狀態

若只記：

$$
P
\text{ 已證},
$$

卻刪除：

- 單 carrier 失敗；
- selector 不可行；
- atlas 塌縮；
- triangle-supported 漏洞；
- $3r-27$ 常數錯誤；

下一個 Agent 很可能重新走回這些路。

---

## 4.2 負知識的形式

令：

$$
F_j
=
(
\mathcal H_j,
\mathcal E_j,
\mathcal R_j
),
$$

其中：

- $\mathcal H_j$ ：被測假設；
- $\mathcal E_j$ ：反例或不可行證據；
- $\mathcal R_j$ ：適用範圍。

例如：

$$
F_{\mathrm{selector}}
=
(
\text{單值反足相容 selector},
\text{有限 MILP infeasible},
(N,k,s,d)=(7,2,3,2)
).
$$

這比一句「selector 好像不行」更可繼承。

---

## 4.3 失敗的作用

失敗紀錄不是歷史附錄，而是搜索剪枝：

$$
\Omega_{t+1}
=
\Omega_t
\setminus
\operatorname{Generalize}(F_t).
$$

所以：

$$
\boxed{
\text{失敗保存}
=
\text{未來計算節省}.
}
$$

---

# 5. 依賴圖：接棒的真正骨架

## 5.1 命題節點

每個節點應包含：

- 命題內容；
- 狀態；
- 前置依賴；
- 驗證方式；
- 版本；
- 來源；
- 新穎性標記。

---

## 5.2 狀態標記

建議至少使用：

- **K**：Known；
- **R**：Reconstructed；
- **P**：Proposed；
- **F**：Filled；
- **X**：Refuted；
- **C**：Computed；
- **A**：Artifact-backed；
- **N?**：Novelty uncertain；
- **O**：Open obligation。

---

## 5.3 依賴邊

若：

$$
M_1,M_2
\Rightarrow
P,
$$

則：

$$
M_1\rightarrow P,
\qquad
M_2\rightarrow P.
$$

若 $M_2$ 被推翻，依賴圖立即標記：

$$
P
\text{ 的此路徑失效}.
$$

---

## 5.4 版本依賴

例如：

$$
M^{(1)}:
M(r)\le3r-27
$$

被修正為：

$$
M^{(2)}:
M(r)\le3r-28.
$$

接棒系統必須保存：

$$
M^{(1)}
\xrightarrow{\mathrm{corrected}}
M^{(2)}.
$$

否則下一個 Agent 可能同時使用衝突版本。

---

# 6. 工件層：把自然語言轉成可重驗狀態

## 6.1 工件種類

### 程式

例如：

```text
verify_s3_k2_cover_lemma.py
```

### 有限證書 verifier

例如：

```text
verify_3stable_k3_finite_core.py
```

### 數據

- 枚舉結果；
- 極大族數量；
- 對偶權重；
- 反例。

### 證明草稿

- 解析不等式；
- 分類表；
- 依賴圖。

---

## 6.2 工件描述

每個工件應包含：

$$
a_j
=
(
\text{name},
\text{hash},
\text{input},
\text{output},
\text{scope},
\text{dependencies}
).
$$

---

## 6.3 工件不等於真理

即使程式可執行，也必須問：

- 它形式化的是不是正確問題？
- 搜索空間是否完整？
- 是否漏掉對稱類？
- 浮點 infeasibility 是否被當成精確證明？
- 依賴套件版本是否改變結果？

所以接棒流程必須包含：

$$
\operatorname{Revalidate}(A_T).
$$

---

# 7. 研究狀態包

本文提出：

$$
\mathfrak P_T
=
(
\Sigma_T,
\mathcal R_T,
\Pi_T,
A_T,
H_T
),
$$

其中：

- $\Sigma_T$ ：接棒摘要；
- $\mathcal R_T$ ：結構化狀態；
- $\Pi_T$ ：原始路徑；
- $A_T$ ：工件；
- $H_T$ ：雜湊與版本承諾。

---

## 7.1 接棒摘要模板

### 當前目標

$$
P_T.
$$

### 已閉合

- 路線 A；
- 路線 B。

### 已否定

- 方法族 X；
- 方法族 Y。

### 活躍中介命題

$$
M_1,\dots,M_s.
$$

### 未完成義務

$$
O_1,\dots,O_h.
$$

### 必須重跑工件

$$
A_1,\dots,A_q.
$$

### 新穎性狀態

- Known；
- Reconstruction；
- Alternative proof candidate；
- Novelty unresolved。

---

## 7.2 原始路徑不可完全丟棄

結構化狀態仍可能摘要錯誤。

所以必須保留：

$$
\Sigma_T
\subset
\mathcal R_T
\subset
\Pi_T.
$$

若發現狀態矛盾，可回溯原始訊息。

---

# 8. 接棒協議

## 8.1 Phase 1：驗證身份與版本

新 Agent 先確認：

- 目標版本；
- 符號表；
- 工件雜湊；
- 最新修正；
- 已知文獻狀態。

---

## 8.2 Phase 2：重新執行關鍵工件

至少重跑：

$$
A_T^{\mathrm{critical}}.
$$

若輸出不一致，暫停接棒。

---

## 8.3 Phase 3：重建活躍依賴圖

新 Agent 必須能回答：

1. 目前真正的主目標是什麼？
2. 哪些命題已閉合？
3. 哪些命題只是候選？
4. 哪些錯誤不能再犯？
5. 下一個最小 GAP 是什麼？

---

## 8.4 Phase 4：反事實測試

移除一個關鍵節點，檢查後續結論是否仍成立。

若不成立，說明依賴圖有效。

---

## 8.5 Phase 5：正式 Resume

只有在：

$$
\operatorname{VerifyState}(\mathfrak P_T)=\mathrm{Pass}
$$

後，才執行：

$$
\mathcal S_{T+1}
=
\operatorname{Resume}
(
A',
\mathfrak P_T
).
$$

---

# 9. 接棒失敗的五種模式

## 9.1 摘要壓縮過度

只留下：

> 已經證到有限核心。

卻沒說有限核心依賴什麼分類與容量界。

---

## 9.2 錯誤被刪除

下一個 Agent 再次使用已被否定的 selector。

---

## 9.3 版本漂移

同時混用：

$$
3r-27
$$

與：

$$
3r-28.
$$

---

## 9.4 工件孤立

程式存在，但不知道它證明哪一個節點。

---

## 9.5 新穎性失真

將「替代證明候選」誤寫成「首次證明」。

---

# 10. 最低信任前提

## 10.1 為何仍需要信任？

任何研究紀錄都不能完全自證。

至少需要相信：

1. 對話確實發生；
2. 時序沒有任意重排；
3. 工具輸出沒有被偽造；
4. 程式檔對應所述版本；
5. 文獻引用沒有故意錯置。

---

## 10.2 如何降低信任成本？

使用：

- 時間戳；
- Git commit；
- SHA-256；
- append-only log；
- 第三方存證；
- 可重跑環境；
- 公開依賴版本。

將：

$$
\text{Trust}
$$

部分轉換為：

$$
\text{Verify}.
$$

---

## 10.3 信任不是全有或全無

更合理的是：

$$
T
=
(
T_{\mathrm{trace}},
T_{\mathrm{artifact}},
T_{\mathrm{citation}},
T_{\mathrm{state}}
).
$$

不同部分可有不同可信度。

---

# 11. 訊息數量與可繼承性

使用者提出：

> 理論上，只要訊息路徑與資料夠多，下一次就可以直接接棒。

這個命題需要修正為：

$$
\boxed{
\text{不是訊息越多越好，而是狀態信息密度足夠高。}
}
$$

---

## 11.1 訊息不足

若缺少：

- 反例；
- 修正；
- 工件；
- 依賴；

接棒誤差大。

---

## 11.2 訊息過多

若沒有狀態抽取，大量對話會產生：

- 注意力稀釋；
- 版本混淆；
- 關鍵節點被淹沒；
- 錯誤重新活化。

---

## 11.3 最佳條件

需要：

$$
\text{Coverage}
+
\text{Compression}
+
\text{Indexing}
+
\text{Verification}.
$$

所以：

$$
\boxed{
\text{足夠多的原始路徑}
+
\text{足夠好的狀態壓縮}
}
$$

才構成可接棒條件。

---

# 12. 研究路徑的資訊理論視角

## 12.1 路徑不是普通文字

研究訊息包含：

- 新命題；
- 狀態變更；
- 反例；
- 版本替換；
- 工件引用。

其有效信息量不是字數，而是：

$$
I_{\mathrm{research}}
=
I(
P,
M,
F,
O,
D,
A
).
$$

---

## 12.2 關鍵節點

若移除訊息 $m_j$ 導致：

$$
d(
\widehat{\mathcal S}_T^{(-j)},
\mathcal S_T
)
\gg
d(
\widehat{\mathcal S}_T,
\mathcal S_T
),
$$

則 $m_j$ 是高研究互信息節點。

---

## 12.3 路徑壓縮目標

尋找最小子序列：

$$
\Pi_T^\ast
\subseteq
\Pi_T
$$

使：

$$
d(
\operatorname{Decode}(\Pi_T^\ast),
\mathcal S_T
)
\le\varepsilon.
$$

這就是研究狀態的最小充分表示。

---

# 13. Kneser 案例的接棒示例

## 13.1 最低必要狀態

### 已知目標

$$
\chi(
KG(r,3)_{3\text{-stab}}
)
=
r-6.
$$

### 已閉合模組

- Tucker 重建；
- Schrijver stable core 辨認；
- $k=2$ block-cover reconstruction；
- $k=3$ stable non-star capacity；
- finite-core dual certificates；
- star peeling。

### 已否定方法族

- 一階單 carrier 一般化；
- 單值反足 selector；
- overlap-consistent atlas。

### 關鍵修正

$$
3r-27
\rightarrow
3r-28.
$$

### 可執行工件

- $s=3,k=2$ cover verifier；
- $s=3,k=3$ finite-core verifier。

### 新穎性狀態

- 定理本身不宣稱首證；
- 證明路線標記為替代證明候選。

---

## 13.2 下一個 Agent 應能直接回答

1. 哪些路線不應重做？
2. 哪些常數已被修正？
3. 哪些有限範圍依賴 verifier？
4. 哪些結論依賴外部分類？
5. 哪一部分仍需同行審查？

若不能回答，表示接棒失敗。

---

# 14. 接棒的可證偽測試

本文提出六個測試。

## 14.1 重現測試

新 Agent 能否重跑工件並得到相同輸出？

---

## 14.2 路徑避免測試

是否避免重新提出已被否定的方法族？

---

## 14.3 依賴重建測試

能否重建：

$$
M(r)=3r-28
\Rightarrow
\text{star-forcing}
\Rightarrow
\text{star peeling}?
$$

---

## 14.4 版本一致性測試

是否使用最新版本？

---

## 14.5 反事實測試

移除失敗節點後，是否重複走錯？

---

## 14.6 創造性接續測試

新 Agent 是否能在不重複舊路的情況下，生成下一個合理 GAP？

---

# 15. 從長對話到研究資料庫

長期實作不應只依賴聊天視窗。

應將研究狀態寫入：

## 15.1 命題表

| ID | 命題 | 狀態 | 版本 | 依賴 |
|---|---|---|---|---|

## 15.2 失敗表

| ID | 方法族 | 反例 | 適用範圍 | 後續影響 |
|---|---|---|---|---|

## 15.3 工件表

| ID | 檔案 | 雜湊 | 輸入 | 輸出 | 關聯命題 |
|---|---|---|---|---|---|

## 15.4 路徑表

| 時間 | 狀態變更 | 來源訊息 | 版本 |
|---|---|---|---|

---

# 16. 與一般記憶系統的差異

一般記憶系統保存：

- 偏好；
- 人名；
- 過去事件；
- 摘要。

研究狀態系統必須額外保存：

- 邏輯依賴；
- 反例；
- 證明義務；
- 工件版本；
- 新穎性狀態；
- 失敗適用範圍。

所以：

$$
\boxed{
\text{Research Memory}
\neq
\text{Conversational Memory}.
}
$$

---

# 17. 多 Agent 接棒

## 17.1 角色分離

可以設置：

- Generator Agent；
- Verifier Agent；
- Literature Agent；
- State Curator Agent；
- Novelty Auditor Agent。

---

## 17.2 接棒不是單向

新 Agent 可能發現前狀態錯誤。

因此接棒應為：

$$
\mathcal S_T
\rightarrow
\widehat{\mathcal S}_T
\rightarrow
\mathcal S_T'
\rightarrow
\mathcal S_{T+1}.
$$

其中：

$$
\mathcal S_T'
$$

是經重新審計後的修正版。

---

## 17.3 狀態分支

若兩個 Agent 對同一 GAP 提出不同路線：

$$
\mathcal S_T
\rightarrow
\mathcal S_{T+1}^{(A)}
$$

與：

$$
\mathcal S_T
\rightarrow
\mathcal S_{T+1}^{(B)}.
$$

系統不應覆蓋其中之一，而應建立分支並比較。

---

# 18. 研究狀態可繼承性的分級

## Level 0：只有答案

無法接棒。

## Level 1：答案加摘要

可理解，但容易重複錯誤。

## Level 2：摘要加依賴圖

可恢復基本研究狀態。

## Level 3：加入失敗與版本

可避免已知路徑浪費。

## Level 4：加入可執行工件

可進行可重驗接棒。

## Level 5：加入時間戳與雜湊

可進行高可信度審計。

## Level 6：跨 Agent 重現

研究狀態被實際證明可繼承。

---

# 19. 本框架的限制

## 19.1 隱性直覺丟失

很多研究判斷沒有被明說。

---

## 19.2 語義解碼差異

不同 Agent 對同一符號可能理解不同。

---

## 19.3 摘要偏差

狀態 curator 可能錯誤壓縮。

---

## 19.4 工具環境漂移

依賴套件與求解器版本可能改變。

---

## 19.5 信任不能完全消除

任何紀錄系統都需要最低信任。

---

## 19.6 長期成本

保存完整路徑與工件需要儲存、索引與治理。

---

# 20. 可證偽命題

本文的核心假說可以被測試。

## 命題 A

含失敗、依賴與工件的狀態包，比只含最終答案更能提高後續 Agent 的研究效率。

## 命題 B

不同 Agent 從同一狀態包接棒時，會比從原始長對話接棒產生更低狀態誤差。

## 命題 C

移除關鍵失敗節點會提高重複錯誤率。

## 命題 D

加入可執行工件會提高跨 Agent 重現率。

若實驗不支持，框架應被修正。

---

# 21. 與前兩篇的關係

第一篇回答：

> 方法實際如何運行、犯錯、修正與閉合？

第二篇回答：

> 即使無法證明所有步驟是純推演，這條路徑為何仍有價值？

第三篇回答：

> 如何把這條路徑保存成可由下一個 Agent 接續的研究狀態？

三篇形成：

$$
\boxed{
\text{執行}
\rightarrow
\text{辯護}
\rightarrow
\text{繼承}.
}
$$

---

# 22. 結論

一次研究若只留下答案，下一次很可能重新開始。

一次研究若只留下完整聊天，下一次很可能被訊息淹沒。

真正可繼承的研究必須同時保存：

$$
\boxed{
\text{原始路徑}
+
\text{結構化狀態}
+
\text{可執行工件}
+
\text{依賴與版本}.
}
$$

訊息路徑的價值不只在於「記錄曾經說過什麼」。

它還可以保存：

- 哪些方向已經走過；
- 哪些錯誤不能再犯；
- 哪些證明義務仍未完成；
- 哪些工件可以重跑；
- 哪些結論只是重建；
- 哪些下一步最值得繼續。

因此，當路徑與資料足夠完整時：

$$
\boxed{
\text{下一個 Agent 不必從零開始，}
}
$$

$$
\boxed{
\text{而可以從上一個研究狀態的邊界直接接棒。}
}
$$

但這個命題具有明確前提：

> 我們必須接受這些訊息、版本與工件確實按所展示的順序存在；並且後續 Agent 必須重新驗證關鍵依賴，而不是盲目相信前一狀態。

所以最終原則不是：

$$
\text{保存越多文字越好},
$$

而是：

$$
\boxed{
\text{保存足以恢復研究因果結構的資訊。}
}
$$

這才是自主研究 Agent 從單次回答走向長期研究系統的必要條件。

---

# 附錄 A：標準研究狀態包格式

```yaml
research_state:
  project_id:
  state_version:
  current_goal:
  active_conjectures:
  known_results:
  reconstructed_results:
  refuted_routes:
  computational_results:
  open_obligations:
  dependency_graph:
  artifacts:
  novelty_status:
  literature_state:
  next_actions:
  checksum:
```

---

# 附錄 B：接棒檢查清單

- [ ] 目標版本一致；
- [ ] 符號表已讀；
- [ ] 最新修正已吸收；
- [ ] 已否定方法未被重新啟用；
- [ ] 關鍵工件可執行；
- [ ] 工件輸出一致；
- [ ] 依賴圖無斷裂；
- [ ] 候選與已證命題已區分；
- [ ] 新穎性標記未被誇大；
- [ ] 下一個最小 GAP 已明確。

---

# 附錄 C：研究狀態質量指標

定義：

$$
Q_{\mathrm{state}}
=
w_1Q_{\mathrm{coverage}}
+
w_2Q_{\mathrm{dependency}}
+
w_3Q_{\mathrm{artifact}}
+
w_4Q_{\mathrm{version}}
+
w_5Q_{\mathrm{uncertainty}}.
$$

其中：

- $Q_{\mathrm{coverage}}$ ：關鍵節點覆蓋率；
- $Q_{\mathrm{dependency}}$ ：依賴圖完整度；
- $Q_{\mathrm{artifact}}$ ：工件可重驗性；
- $Q_{\mathrm{version}}$ ：版本一致性；
- $Q_{\mathrm{uncertainty}}$ ：不確定性可見度。

---

# 附錄 D：研究誠信聲明

1. 本文不把完整聊天自動等同於研究證據。
2. 本文不把摘要自動等同於真實研究狀態。
3. 本文要求失敗與修正被保存。
4. 本文要求工件與命題建立明確依賴。
5. 本文要求接棒 Agent 重驗關鍵工件。
6. 本文接受狀態抽取可能出錯。
7. 本文支持保留原始路徑以供回溯。
8. 本文不以路徑長度代替路徑質量。
9. 本文承認最低信任前提不能完全消除。
10. 本文將跨 Agent 重現視為最強的可繼承性證據。
